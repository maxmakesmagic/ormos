import logging
import re
from typing import Generator, Optional
from urllib.parse import unquote

from pony import orm
import requests
from requests.adapters import HTTPAdapter, Retry
import wayback

db = orm.Database()
log = logging.getLogger(__name__)


class ImageUrl(db.Entity):
    input_url = orm.Required(str, unique=True, max_len=384)
    output_url = orm.Required(str, max_len=384)
    strategy = orm.Required(str)


class ImageCache:
    def __init__(self) -> None:
        with orm.db_session:
            self.counter = ImageUrl.select().count()

        self.s = requests.Session()
        retries = Retry(total=5, backoff_factor=5)
        self.s.mount("http://", HTTPAdapter(max_retries=retries))
        self.s.mount("https://", HTTPAdapter(max_retries=retries))

        session = wayback.WaybackSession(retries=20)
        self.client = wayback.WaybackClient(session=session)

    def cache_insert(self, key, value, identifier, strategy):
        with orm.db_session:
            _db_url = ImageUrl(input_url=key, output_url=value, strategy=strategy)

        self.counter += 1
        if self.counter % 50 == 0:
            log.debug("[%s] Cached %d images", identifier, self.counter)
        return value

    def image_url(self, img_src: str, identifier: str = "") -> Optional[str]:
        try:
            r = self.s.head(img_src, allow_redirects=True, timeout=30)
            if r.status_code == 200:
                # Check the Content-Type to make sure it's actually an image.
                content_type = r.headers.get("Content-Type")
                if "image/" in content_type:
                    return r.url
                else:
                    log.error(
                        "[%s] %s was redirected to non-image URL %s",
                        identifier,
                        img_src,
                        identifier,
                    )
        except requests.RequestException:
            log.debug("[%s] Failed to find URL", identifier)

        return None

    def verified_image(
        self, img_src: str, identifier: str = "", image_prefix: str = None
    ) -> str:
        if img_src.startswith("/"):
            # Refers to top-level domain
            img_src = f"https://magic.wizards.com{img_src}"
            log.debug("[%s] Set image to full URL: %s", identifier, img_src)

        with orm.db_session:
            db_url = ImageUrl.get(input_url=img_src)  # type: Optional[ImageUrl]

        if db_url is None:
            # Best effort to get a working image.
            log.debug("[%s] Checking image: %s", identifier, img_src)

            # For gatherer.wizards.com, just use the URL directly.
            if "gatherer.wizards.com" in img_src:
                log.debug("[%s] Use gatherer.wizards.com direct", identifier)
                return self.cache_insert(img_src, img_src, identifier, "gatherer")

            # Skip archive.wizards.com, it no longer resolves.
            if "archive.wizards.com" not in img_src:
                checked_img_src = self.image_url(img_src, identifier=identifier)
                if checked_img_src:
                    log.debug("[%s] Using image %s", identifier, checked_img_src)
                    return self.cache_insert(
                        img_src, checked_img_src, identifier, "checked"
                    )

            # Check for URL rewrites
            m = re.match(
                r"http[s]?://magic.wizards.com/sites/mtg/files/([^\?]+)", img_src
            )
            if m:
                rewrite = f"https://media.magic.wizards.com/{m.group(1)}"
                log.debug("[%s] Checking media magic rewrite: %s", identifier, rewrite)
                rewrite_src = self.image_url(rewrite, identifier=identifier)
                if rewrite_src:
                    log.debug("[%s] Using image %s", identifier, rewrite_src)
                    return self.cache_insert(
                        img_src, rewrite_src, identifier, "rewrite"
                    )

            # Image doesn't exist. Try checking the Wayback image.
            if image_prefix:
                wayback_url = f"{image_prefix}/{img_src}"
                log.debug(
                    "[%s] Not found; checking wayback image: %s",
                    identifier,
                    wayback_url,
                )
                wayback_img = self.image_url(wayback_url, identifier=identifier)
                if wayback_img:
                    log.debug("[%s] Using wayback image %s", identifier, wayback_img)
                    return self.cache_insert(
                        img_src, wayback_img, identifier, "wayback"
                    )

            # If in doubt, just return the original source.
            # Record a failure just in case we want to fix these up later.
            log.debug("[%s] Not found; using original %s", identifier, img_src)
            return self.cache_insert(img_src, img_src, identifier, "failure")

        if db_url.output_url == img_src:
            log.debug("[%s] Using database: %s", identifier, db_url.output_url)
        else:
            log.debug(
                "[%s] Using map: %s => %s", identifier, img_src, db_url.output_url
            )
        return db_url.output_url

    def wayback_failures(self):
        # Find all the "failure" images. Let's see if we can find working links.

        with orm.db_session:
            failures = orm.select(
                i for i in ImageUrl if i.strategy == "failure"
            )  # type: Generator[ImageUrl]
            for failure in failures:
                identifier = failure.input_url[-15:]
                log.info("[%s] Processing failed URL %s", identifier, failure.input_url)
                url = self.wayback_failure(failure.input_url, identifier=identifier)
                if url:
                    # Update the database
                    log.info("[%s] Updating mapping: => %s", identifier, url)
                    failure.set(output_url=url, strategy="wayback2")

    def wayback_failure(self, failure_url: str, identifier: str = "") -> Optional[str]:
        urls_to_try = [failure_url]

        # Try replacing subdomains with sensible guesses
        for search, replacement in {
            "archive.wizards.com": "wizards.com",
            "staging.wizards.com": "wizards.com",
            "edit.magic.wizards.com": "magic.wizards.com",
            "www.wizards.comhttp//www.wizards.com": "www.wizards.com",
        }.items():
            if f"{search}/" in failure_url:
                urls_to_try.append(failure_url.replace(search, replacement))

        # Some URLs have URL-encoded characters at the end by mistake. Try fixing that.
        urldecoded = unquote(failure_url).strip()
        if urldecoded not in urls_to_try:
            urls_to_try.append(urldecoded)

        # Some URLs have a file extension that's a little wrong.
        if failure_url.endswith(".pngg"):
            urls_to_try.append(failure_url.replace(".pngg", ".png"))

        for url in urls_to_try:
            # find the URL in wayback
            log.debug("[%s] Checking URL in wayback: %s", identifier, url)
            results = self.client.search(url)  # type: Generator[wayback.CdxRecord]
            # get the raw URLs from the records
            raw_urls = [result.raw_url for result in results]
            for (index, raw_url) in enumerate(raw_urls):
                loop_id = f"{identifier}:{index+1}/{len(raw_urls)}"
                log.debug("[%s] Found wayback URL: %s", loop_id, raw_url)
                test_url = self.image_url(raw_url, identifier)
                if test_url:
                    log.debug("[%s] Found working wayback URL: %s", loop_id, test_url)
                    return test_url

        return None

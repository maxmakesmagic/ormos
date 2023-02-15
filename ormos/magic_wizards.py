#!/usr/bin/env python3

import argparse
import cProfile
from datetime import datetime
import json
import logging
import multiprocessing
import os
from pathlib import Path
import re
import sys
from typing import Generator, List, Optional, Tuple
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup, Tag
from markdownify import MarkdownConverter
from tqdm import tqdm

from tqdm.contrib.logging import logging_redirect_tqdm

from ormos.database import DistinctPage, db, Scraped, orm
from ormos.imagecache import ImageCache

log = logging.getLogger(__name__)


DATE_MATCHER = re.compile(r"^(.*?)([^/]+-(\d{4})-(\d{2})-(\d{2})(:?-\d+)?)$")


class MagicWizardsConverterSingle:
    def __init__(
        self,
        hash_url: str,
        identifier: str = "",
        distinct_url: str = "",
        image_cache: Optional[ImageCache] = None,
    ):
        self.identifier = identifier
        self.url_path = None
        self.path_date = None
        self.parts = None
        self.noleading = None

        # This is a speedy cutout to not do work if it isn't necessary
        if distinct_url:
            url_path = self.generate_url_path(distinct_url)
            if url_path and url_path.exists():
                log.debug(
                    "[%s] Skipping %s as path exists", self.identifier, distinct_url
                )
                return

        # Try with the database if no distinct URL given
        with orm.db_session:
            distinct = DistinctPage[hash_url]

            self.url_path = self.generate_url_path(distinct.url)
            if self.url_path and self.url_path.exists():
                log.debug(
                    "[%s] Skipping %s as path exists", self.identifier, distinct.url
                )
                return

            scraped = distinct.scraped
            self.url = scraped.url
            self.raw_url = scraped.raw_url
            self.view_url = scraped.view_url

            # Read in the HTML file
            self.soup = BeautifulSoup(scraped.html_content, "html.parser")
            scrape_time = scraped.time

        # Actual work to do!
        self.cache = {}
        self.image_cache = image_cache if image_cache else ImageCache()
        self.date = None
        self.title = None

        # Start a metadata dictionary, which can be added to.
        self.metadata = {
            "wayback_url": self.url,
            "wayback_raw_url": self.raw_url,
            "wayback_capture_timestamp": str(scrape_time),
        }

        # Calculate the wayback prefix for images
        m = re.match(r"^(https://web.archive.org/web/[^/]+)", self.view_url)
        if m:
            self.image_prefix = f"{m.group(1)}im_"
            log.debug("[%s] Wayback prefix is %s", self.identifier, self.image_prefix)
        else:
            self.image_prefix = None
        self.process()

    def generate_url_path(self, url: str) -> Optional[Path]:
        # Attempt to generate the path from the URL
        self.parts = urlparse(url)
        log.debug("[%s] URL parts: %s", self.identifier, self.parts)

        # URL-unquote the path, and remove any slashes from the
        # front or end.
        self.noleading = unquote(self.parts.path.strip("/"))

        # Try and calculate the article path at this point
        m = DATE_MATCHER.match(self.noleading)
        if m:
            # "Normal" article URL!
            path = Path(
                "archive", m.group(1), m.group(3), m.group(4), f"{m.group(2)}.md"
            )
            self.path_date = f"{m.group(3)}-{m.group(4)}-{m.group(5)}"
            return path

        return None

    def _main_content(self) -> Optional[Tag]:
        log.debug("[%s] Processing HTML", self.identifier)

        # Store off some metadata if it exists.
        for tag in self.soup.find_all("meta"):
            name = tag.get("name", None)
            if name in ["generator", "description"]:
                self.metadata[name] = tag.get("content", "")

            prop = tag.get("property", None)
            if prop in ["og:title"]:
                self.title = tag.get("content", "")

        if not self.title:
            title_tag = self.soup.find("title")
            if title_tag:
                self.title = title_tag.getText()

        if self.title:
            self.metadata["title"] = self.title

        for tag in self.soup.find_all("link"):
            rel = tag.get("rel", None)
            href = tag.get("href", None)
            if rel and "shortlink" in rel and href:
                if "node" in href:
                    self.metadata["node"] = href.rsplit("/", 1)[1]

        # Content can be in one of several places.
        # Try each of them in turn!
        #
        main_content = self.soup.find("div", id="main-content")
        if main_content:
            self.metadata["source"] = "div-main-content"
            return main_content

        # Try another tag
        main_content = self.soup.find("div", id="main")
        if main_content:
            self.metadata["source"] = "div-main"
            return main_content

        # If there's an article, just use that.
        main_content = self.soup.find("article")
        if main_content:
            self.metadata["source"] = "article"
            return main_content

        # If the title doesn't start with "Article" (as it's probably
        # "Article Archives" or "ARTICLES") then capture the content
        # from block-system-main
        if self.title and not self.title.lower().startswith("article"):
            main_content = self.soup.find("div", id="block-system-main")
            if main_content:
                log.debug(
                    "[%s] Allowing article with title %s", self.identifier, self.title
                )
                self.metadata["source"] = "div-block-system-main"
                return main_content

        # Assume not an article. Check later from logs.
        log.error(
            "[%s] Not an article:\n- URL: %s\n- Title: %s",
            self.identifier,
            self.url,
            self.title,
        )
        return None

    def _store_data_from_soup(self, main_content: Tag):
        # Store off the publish date if it can be found
        DATE_REX = re.compile(
            r"((January|February|March|April|May|June|July|August|September|October|November|December) ([0-3]?[0-9]), (\d{4}))"
        )

        posted_in = main_content.find("p", class_="posted-in")
        header_pub_date = main_content.find("span", class_="headerPubDate")

        if posted_in:
            posted_text = posted_in.getText()
        elif header_pub_date:
            posted_text = header_pub_date.getText()
        else:
            posted_text = ""

        m = DATE_REX.search(posted_text)
        if m:
            full_date = m.group(1)
            parsed_date = datetime.strptime(full_date, "%B %d, %Y")
            self.date = parsed_date.strftime("%Y-%m-%d")
            log.debug("[%s] Detected article date as %s", self.identifier, self.date)

        # Try and find the author
        author_div = main_content.find("div", class_="author")
        if author_div:
            # the author is in the first p tag
            author_text = author_div.p.getText()
            if author_text.startswith("By "):
                author_text = author_text[3:]

            # Split out the first comma
            if "," in author_text:
                author_text = author_text.split(",")[0]

            # Replace any slashes.
            author_text = author_text.replace("/", "-")

            log.debug(
                "[%s] Detected article author as %s", self.identifier, author_text
            )
            self.metadata["author"] = author_text

    # Converts HTML content into Markdown content
    def process_html(self) -> Optional[str]:
        main_content = self._main_content()
        if not main_content:
            # Failed to find main content
            return None

        # Store data from the main content soup
        self._store_data_from_soup(main_content)

        # Remove content that isn't necessary
        #
        # Remove breadcrumb links
        for bc in main_content.find_all(id="breadcrumb"):
            bc.decompose()

        # Remove author links (Bio, Archive)
        for p_class in ["links"]:
            for p in main_content.find_all("p", class_=p_class):
                p.decompose()
        for s_class in ["links"]:
            for s in main_content.find_all("span", class_=s_class):
                s.decompose()

        # Remove in-body styles and scripts
        for tagtype in ["style", "script"]:
            for tag in main_content.find_all(tagtype):
                tag.decompose()

        # Remove sharing links and the article footer
        # Also remove sample hands
        for div_class in [
            "sharing",
            "article-footer",
            "data-sample-hand-cards",
            "toggle-samplehand",
        ]:
            for ds in main_content.find_all("div", class_=div_class):
                ds.decompose()

        # Convert iframes to hyperlinks
        for iframe in main_content.find_all("iframe"):
            if "src" in iframe.attrs:
                new_a = self.soup.new_tag("a")
                new_a.attrs["href"] = iframe.attrs["src"]
                new_a.string = iframe.attrs["src"]
                iframe.replace_with(new_a)

        # Verify that any images exist; and if they don't, then
        # try and replace them with a Wayback URL.
        for img in main_content.find_all("img"):
            if "src" in img.attrs and img.attrs["src"]:
                new_src = self.image_cache.verified_image(
                    img.attrs["src"], self.identifier, self.image_prefix
                )
                img.attrs["src"] = new_src
            else:
                log.warning("[%s] Removing weird image: %s", self.identifier, img)
                # Image is weird. One example seen: <img style="magic">
                img.decompose()

        # Convert the remainder into Markdown
        mc = MarkdownConverter().convert_soup(main_content)

        # log.debug("Markdown content: %s", mc)
        return mc

    # Generates a path for this content in the archive
    def generate_path(self, url: str) -> Path:
        if self.url_path:
            # "Normal" article URL!
            path = self.url_path
            date = self.path_date
            if self.date is None:
                self.date = date
            elif self.date != date:
                log.warning(
                    "[%s] Article date and URL date differ: %s vs %s",
                    self.identifier,
                    self.date,
                    date,
                )
                self.metadata["path_date"] = date
        elif self.date is not None:
            # Not a normal URL - there's no date in the URL, but there is one in the body
            # Add the article date into the URL
            m = re.match(r"^(.*?)([^/]+)$", self.noleading)
            if not m:
                raise Exception(f"URL wrong: {self.noleading}")

            n = re.match(r"(\d{4})-(\d{2})-(\d{2})", self.date)
            if not n:
                raise Exception(f"Date wrong: {self.date}")

            path = Path(
                "archive", m.group(1), n.group(1), n.group(2), f"{m.group(2)}.md"
            )
        else:
            # There's no date in the body nor in the URL!
            path = Path("archive", f"{self.noleading}.md")

        if self.date is not None:
            self.metadata["publish_date"] = self.date

        log.debug("[%s] Generated path: %s", self.identifier, path)
        parent = path.parent
        os.makedirs(parent, exist_ok=True)
        return path

    def process(self):
        # Process the HTML into Markdown
        markdown = self.process_html()
        if markdown:
            # Calculate the archive path
            archive_path = self.generate_path(self.url)

            # Check to see if the path already exists
            if archive_path.exists():
                log.debug("[%s] Path already exists: %s", self.identifier, archive_path)
            else:
                log.info("[%s] Writing %s", self.identifier, archive_path)

                # Write out the Markdown.
                with open(archive_path, "w", encoding="utf-8") as f:
                    f.write("\n---\n")
                    # Write the link to the Wayback page
                    f.write(f"[Link to Wayback Machine]({self.view_url})\n\n")

                    # Add the metadata as Markdown metadata at the start of the file
                    for key in sorted(self.metadata):
                        escvalue = self.metadata[key].replace('"', "`")
                        f.write(f'[_metadata_:{key}]:- "{escvalue}"\n')
                    f.write("---\n")
                    f.write(markdown)


class MagicWizardsConverterMany:
    SEARCH_TERM_BASE = "magic.wizards.com"

    def __init__(self, search_term: Optional[str] = None):
        self.search_term = search_term if search_term else self.SEARCH_TERM_BASE
        self.image_cache = ImageCache()

        with orm.db_session:
            if self.search_term:
                items = orm.select(
                    (s.hash_url, s.url)
                    for s in DistinctPage
                    if self.search_term in s.url
                )  # type: Generator[Tuple[str, str]]
            else:
                items = orm.select(
                    (s.hash_url, s.url) for s in DistinctPage
                )  # type: Generator[Tuple[str, str]]
            self.total = items.count()
            self.items = list(items)

    def process(self):
        log.info("Processing %d entries", self.total)

        # with tqdm(total=self.total) as pbar:
        #     with ThreadPoolExecutor(max_workers=2) as ex:
        #         futures = [
        #             ex.submit(
        #                 MagicWizardsConverterSingle,
        #                 distincthash,
        #                 f"{index+1}/{self.total}",
        #                 distincturl,
        #             )
        #             for index, (distincthash, distincturl) in enumerate(self.items)
        #         ]
        #         for future in as_completed(futures):
        #             try:
        #                 result = future.result()
        #             except Exception as e:
        #                 log.exception("Failed processing")
        #             pbar.update(1)

        # for index, (distincthash, distincturl) in enumerate(tqdm(self.items)):
        #     log.debug("[%d/%d] Processing %s", index + 1, self.total, distincturl)
        #     try:
        #         MagicWizardsConverterSingle(
        #             distincthash,
        #             f"{index+1}/{self.total}",
        #             image_cache=self.image_cache,
        #             distinct_url=distincturl,
        #         )
        #     except Exception as e:
        #         log.exception("Failed processing")

        p = multiprocessing.Pool(initializer=image_initializer)
        for i in tqdm(p.imap(singler, enumerate(self.items)), total=self.total):
            pass


global_image_cache = None


def image_initializer(*args):
    global global_image_cache
    global_image_cache = ImageCache()


def singler(item):
    index, (distincthash, distincturl) = item
    try:
        MagicWizardsConverterSingle(
            distincthash,
            f"{index+1}",
            image_cache=global_image_cache,
            distinct_url=distincturl,
        )
    except Exception as e:
        log.exception("Failed processing")


if __name__ == "__main__":
    streamhandler = logging.StreamHandler(stream=sys.stdout)
    streamhandler.setLevel(logging.INFO)
    streamhandler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-5.5s %(message)s")
    )
    filehandler = logging.FileHandler(filename="magic_wizards.log", mode="w")
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-5.5s %(message)s")
    )
    errorhandler = logging.FileHandler(filename="magic_wizards_errors.log", mode="w")
    errorhandler.setLevel(logging.ERROR)
    errorhandler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-5.5s %(message)s")
    )

    root_logger = logging.getLogger()
    # root_logger.addHandler(streamhandler)
    root_logger.addHandler(filehandler)
    root_logger.addHandler(errorhandler)
    root_logger.setLevel(logging.INFO)

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Bind to the database
    with open("database.json", "rb") as f:
        creds = json.load(f)
    db.bind(**creds)
    db.generate_mapping(create_tables=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("--searchterm", help="override default search term")

    args = parser.parse_args()

    converter = MagicWizardsConverterMany(search_term=args.searchterm)
    converter.process()

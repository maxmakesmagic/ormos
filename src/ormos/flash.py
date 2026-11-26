"""Render recovered Flash movies and their archived dependencies."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile
from typing import TYPE_CHECKING, Any
from urllib.parse import parse_qs, parse_qsl, unquote, urljoin, urlsplit

from .html import FLASH_ROUTE, IMAGE_ORIGIN, MEDIA_ORIGIN, render_page
from .paths import component

if TYPE_CHECKING:
    from .content import Document
    from .site import Site

RUFFLE_RUNTIME_FILES = (
    "LICENSE_APACHE",
    "LICENSE_MIT",
    "ruffle.js",
    "ruffle_web-wasm_mvp_bg.UMWKJ7EM.wasm",
    "ruffle_web_bg.QDRSAAAZ.wasm",
)
CHECKSUM = re.compile(r"[0-9a-f]{64}")
WIZARDS_MEDIA_HOSTS = {
    "archive.wizards.com",
    "magic.wizards.com",
    "media.magic.wizards.com",
    "media.wizards.com",
    "wizards.com",
    "www.wizards.com",
}
FlashURL = tuple[str, str, tuple[tuple[str, str], ...]]


def _reference_url(target: str, base: str = "") -> FlashURL | None:
    try:
        url = urlsplit(urljoin(base, target))
        host = url.hostname
    except ValueError:
        return None
    if not host or url.scheme not in {"http", "https"}:
        return None
    path = unquote(url.path)
    if not path.lower().endswith(".swf"):
        return None
    if host in WIZARDS_MEDIA_HOSTS:
        host = "wizards.com"
        path = path.removeprefix(
            "/sites/mtg/files/image_legacy_migration"
        ).removeprefix("/image_legacy_migration")
    return host, path, tuple(sorted(parse_qsl(url.query, keep_blank_values=True)))


@dataclass(slots=True)
class FlashReferences:
    """Look up movies by catalog ID, original URL, or related article."""

    items: dict[str, FlashItem]
    urls: dict[FlashURL, FlashItem | None]
    articles: dict[str, list[FlashItem]]

    def matches(
        self,
        article_id: str,
        source_url: str,
        targets: tuple[str, ...],
        *,
        marker_ids: tuple[str, ...] = (),
    ) -> tuple[FlashItem, ...]:
        """Find the movies referenced by an article, in the recorded order."""
        matches = {
            item_id: self.items[item_id]
            for item_id in marker_ids
            if item_id in self.items
        }
        for target in targets:
            key = _reference_url(target, source_url)
            if key is not None and (item := self.urls.get(key)):
                matches.setdefault(item.id, item)
        for item in self.articles.get(article_id, ()):
            matches.setdefault(item.id, item)
        return tuple(matches.values())


@dataclass(frozen=True, slots=True)
class FlashItem:
    """One recovered movie and the images used with it."""

    id: str
    digest: str
    title: str
    source_urls: tuple[str, ...]
    filename: str
    parameters: dict[str, str]
    image_digest: str
    article_ids: tuple[str, ...] = ()
    wallpaper_url: str = ""
    wallpaper_archive_url: str = ""
    poster_url: str = ""

    @classmethod
    def read(cls, row: dict[str, Any]) -> FlashItem:
        """Validate the source, movie checksum, and any jigsaw parameters."""
        digest = row.get("sha256")
        identifier = row.get("id", digest)
        urls = row.get("original_urls")
        title = row.get("title")
        image = row.get("image_sha256", "")
        articles = row.get("article_ids", [])
        if (
            not isinstance(digest, str)
            or not CHECKSUM.fullmatch(digest)
            or not isinstance(identifier, str)
            or not CHECKSUM.fullmatch(identifier)
            or not isinstance(urls, list)
            or not urls
            or not all(isinstance(url, str) and _reference_url(url) for url in urls)
            or not isinstance(title, str)
            or not title.strip()
            or not isinstance(articles, list)
            or not all(isinstance(article, str) for article in articles)
        ):
            raise ValueError(f"Invalid Flash catalog entry: {digest!r}")
        source = urlsplit(urls[0])
        filename = unquote(source.path.rsplit("/", 1)[-1])
        if not filename.lower().endswith(".swf") or "/" in filename or "\\" in filename:
            raise ValueError(f"Invalid Flash filename: {filename!r}")
        query = parse_qs(source.query, keep_blank_values=True)
        if any(len(values) != 1 for values in query.values()):
            raise ValueError(f"Repeated Flash parameters: {digest}")
        parameters = {name: values[0] for name, values in query.items()}
        if row.get("parameters", parameters) != parameters:
            raise ValueError(
                f"Flash parameters differ from the original location: {identifier}"
            )
        relative_image = parameters.get("stgImage", "")
        if not isinstance(image, str) or bool(image) != bool(relative_image):
            raise ValueError(f"Missing Flash image or parameters: {digest}")
        if image:
            if not CHECKSUM.fullmatch(image) or not relative_image.lower().endswith(
                ".jpg"
            ):
                raise ValueError(f"Invalid Flash image: {digest}")
            for part in relative_image.split("/"):
                component(part)
        wallpaper = row.get("wallpaper_url", "")
        wallpaper_archive = row.get("wallpaper_archive_url", "")
        poster = row.get("poster_url", "")
        for url in (wallpaper, wallpaper_archive, poster):
            if not isinstance(url, str):
                raise TypeError(f"Flash media URL must be a string: {identifier}")
            if url:
                target = urlsplit(url)
                if target.scheme != "https" or not target.hostname:
                    raise ValueError(f"Invalid Flash media URL: {identifier}")
        if (wallpaper or wallpaper_archive) and not image:
            raise ValueError(f"Flash wallpaper requires a puzzle image: {identifier}")
        return cls(
            identifier,
            digest,
            title,
            tuple(urls),
            filename,
            parameters,
            image,
            tuple(component(article) for article in articles),
            wallpaper,
            wallpaper_archive,
            poster,
        )

    @property
    def path(self) -> str:
        """Return the archive page for this movie."""
        return f"{FLASH_ROUTE}/{self.id}"

    @property
    def movie_url(self) -> str:
        """Return the archived movie URL on the media host."""
        digest = self.digest
        # Use a separate cache entry from responses stored before CORS was enabled.
        return f"{MEDIA_ORIGIN}/{digest[:2]}/{digest[2:4]}/{digest}.swf?cors=1"

    @property
    def puzzle_base(self) -> str:
        """Return the base used to resolve this jigsaw's original relative image path."""
        return f"/assets/flash/{self.id}/" if self.image_digest else ""

    @property
    def puzzle_image_url(self) -> str:
        """Return the published image that replaces the original relative request."""
        if not self.image_digest:
            return ""
        digest = self.image_digest
        return f"{IMAGE_ORIGIN}/{digest[:2]}/{digest[2:4]}/{digest}.jpg?cors=1"

    @property
    def parameters_json(self) -> str:
        """Return the original movie parameters for the browser player."""
        return json.dumps(self.parameters)


@dataclass(frozen=True, slots=True)
class FlashLibrary:
    """The recovered Flash catalog."""

    items: tuple[FlashItem, ...]

    @classmethod
    def read(cls, data: Path) -> FlashLibrary:
        """Read the optional Flash catalog."""
        path = data / "flash.json"
        if not path.is_file():
            return cls(())
        catalog = json.loads(path.read_bytes())
        if (
            not isinstance(catalog, dict)
            or catalog.get("version") != 1
            or not isinstance(catalog.get("items"), list)
            or not all(isinstance(row, dict) for row in catalog["items"])
        ):
            raise ValueError(f"Unsupported Flash catalog: {path}")
        items = tuple(FlashItem.read(row) for row in catalog["items"])
        if len({item.id for item in items}) != len(items):
            raise ValueError(f"Repeated Flash item IDs in {path}")
        return cls(items)

    def references(self) -> FlashReferences:
        """Index recorded references without guessing between ambiguous matches."""
        urls: dict[FlashURL, FlashItem | None] = {}
        articles: defaultdict[str, list[FlashItem]] = defaultdict(list)
        for item in self.items:
            for url in item.source_urls:
                key = _reference_url(url)
                if key is not None and urls.setdefault(key, item) is not item:
                    urls[key] = None
            for article in item.article_ids:
                articles[article].append(item)
        return FlashReferences(
            items={item.id: item for item in self.items},
            urls=urls,
            articles=dict(articles),
        )

    @staticmethod
    def write_assets(assets: Path, runtime: Path) -> None:
        """Copy the pinned Ruffle runtime."""
        if not all((runtime / name).is_file() for name in RUFFLE_RUNTIME_FILES):
            raise ValueError("Run npm ci to install the local Ruffle runtime")
        destination = assets / "ruffle"
        destination.mkdir()
        for name in RUFFLE_RUNTIME_FILES:
            copyfile(runtime / name, destination / name)

    def write_pages(self, site: Site) -> None:
        """Write the Flash directory and a player page for every recovered movie."""
        items = sorted(self.items, key=lambda item: (item.title.casefold(), item.id))
        related: defaultdict[str, list[Document]] = defaultdict(list)
        for document in site.entries.values():
            for item_id in document.flash_ids:
                related[item_id].append(document)
        site.page(
            FLASH_ROUTE,
            render_page(
                "flash-index.html",
                "Flash",
                FLASH_ROUTE,
                jigsaws=[item for item in items if item.image_digest],
                movies=[item for item in items if not item.image_digest],
            ),
        )
        for item in items:
            site.page(
                item.path,
                render_page(
                    "flash.html",
                    item.title,
                    item.path,
                    flash_player=True,
                    flash_puzzle=bool(item.image_digest),
                    item=item,
                    articles=sorted(
                        related[item.id],
                        key=lambda article: (article.title.casefold(), article.path),
                    ),
                ),
            )

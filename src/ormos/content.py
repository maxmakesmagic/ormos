"""Read archived Markdown documents and render their public pages."""

from __future__ import annotations

import re
from dataclasses import dataclass, replace
from datetime import date
from html import escape, unescape
from pathlib import Path
from typing import TYPE_CHECKING, Any
from urllib.parse import urlsplit

import cmarkgfm
import nh3
import yaml
from markupsafe import Markup

from .html import FLASH_ROUTE, render_page, render_template
from .paths import component, route, site_file, write_new

if TYPE_CHECKING:
    from .flash import FlashItem, FlashReferences
    from .media_links import MediaLinks

_FRONT_MATTER_START = "---\n"
_FRONT_MATTER_END = "\n---\n"
_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
_UNKNOWN_PUBLICATION_DAYS = frozenset({date(1969, 12, 31), date(1970, 1, 1)})
_RAW_TABLE = re.compile(r"<table\b[^>]*>.*?</table\s*>", re.IGNORECASE | re.DOTALL)
_TABLE_INTERRUPTION = re.compile(r"\n[ \t]*\n")
_FLASH_MARKER = re.compile(
    rf'<p><img loading="lazy" decoding="async" src="{re.escape(FLASH_ROUTE)}/'
    r'([0-9a-f]{64})" alt="([^"]*)"(?: title="[^"]*")?></p>'
)
_FLASH_LINK = re.compile(r'<a\b[^>]*\bhref="([^"<>]*\.swf[^"<>]*)"', re.IGNORECASE)
_BODY_CLEANER = nh3.Cleaner(
    tags={
        "a",
        "abbr",
        "b",
        "blockquote",
        "br",
        "caption",
        "code",
        "dd",
        "del",
        "div",
        "dl",
        "dt",
        "em",
        "figcaption",
        "figure",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "hr",
        "i",
        "img",
        "li",
        "ol",
        "p",
        "pre",
        "s",
        "small",
        "span",
        "strong",
        "sub",
        "sup",
        "table",
        "tbody",
        "td",
        "tfoot",
        "th",
        "thead",
        "tr",
        "u",
        "ul",
    },
    clean_content_tags={"script", "style", "iframe", "object", "svg", "template"},
    attributes={
        "*": {"id", "lang"},
        "a": {"href", "name", "title"},
        "abbr": {"title"},
        "img": {"src", "alt", "title", "width", "height"},
        "ol": {"start"},
        "td": {"align", "colspan", "rowspan"},
        "th": {"align", "colspan", "rowspan", "scope"},
    },
    tag_attribute_values={
        "td": {"align": {"left", "center", "right"}},
        "th": {"align": {"left", "center", "right"}},
    },
    url_schemes={"https", "http", "mailto"},
    link_rel=None,
)


def publication_day(value: str | None) -> date | None:
    """Return the publication date if the archive records a known day."""
    if not value:
        return None
    try:
        day = date.fromisoformat(value[:10])
    except ValueError:
        return None
    return None if day in _UNKNOWN_PUBLICATION_DAYS else day


def web_url(value: str) -> bool:
    """Return whether the URL uses HTTP or HTTPS and names a host."""
    try:
        parsed = urlsplit(value)
        return parsed.scheme in {"http", "https"} and bool(parsed.hostname)
    except ValueError:
        return False


def render_body(markdown: str) -> str:
    """Convert Markdown to sanitized HTML for an archive page."""
    # Blank lines end a CommonMark raw HTML block. Keep them from splitting tables.
    markdown = _RAW_TABLE.sub(
        lambda match: _TABLE_INTERRUPTION.sub("\n", match[0]), markdown
    )
    html = cmarkgfm.github_flavored_markdown_to_html(
        markdown,
        options=cmarkgfm.Options.CMARK_OPT_UNSAFE,
    )
    clean = _BODY_CLEANER.clean(html)
    # Adjust the converted markup before inserting it into the page template.
    clean = clean.replace("<img ", '<img loading="lazy" decoding="async" ')
    return clean.replace(
        "<table>",
        '<div class="table-scroll" tabindex="0" role="region" aria-label="Table"><table>',
    ).replace("</table>", "</table></div>")


def _place_flash(body: str, items: tuple[FlashItem, ...]) -> tuple[str, str]:
    movies = {item.id: item for item in items}
    placed: set[str] = set()

    def player_at_marker(marker: re.Match[str]) -> str:
        item = movies.get(marker[1])
        label = unescape(marker[2])
        if item is None:
            return f"<p>{escape(label or 'Flash animation unavailable')}</p>"
        placed.add(item.id)
        return render_template(
            "flash-player.html", item=item, embedded=True, label=label
        )

    body = _FLASH_MARKER.sub(player_at_marker, body)
    players = "".join(
        render_template("flash-player.html", item=item, embedded=True)
        for item in items
        if item.id not in placed
    )
    return body, players


@dataclass(frozen=True, slots=True)
class Person:
    """Store an author name and its archive path component."""

    slug: str
    name: str


@dataclass(frozen=True, slots=True)
class Document:
    """Store the metadata for an archived page."""

    id: str
    kind: str
    lang: str
    path: str
    title: str
    published: str
    column_slug: str
    column: str
    authors: tuple[Person, ...]
    flash_ids: tuple[str, ...] = ()

    @classmethod
    def read(cls, metadata: dict[str, Any]) -> Document:
        """Read page metadata from the article header."""
        authors = tuple(
            Person(component(person["slug"]), str(person["name"]))
            for person in metadata.get("authors") or ()
        )
        column_slug = metadata.get("column_slug")
        return cls(
            id=component(metadata["id"]),
            kind=component(metadata["kind"]),
            lang=component(str(metadata.get("lang") or "en")),
            path=route(metadata["path"]),
            title=str(metadata.get("title") or metadata["id"]),
            published=str(metadata.get("published") or ""),
            column_slug=component(column_slug) if column_slug else "",
            column=str(metadata.get("column") or column_slug or ""),
            authors=authors,
        )

    @property
    def day(self) -> date | None:
        """Return the publication day if it is known."""
        return publication_day(self.published)

    def column_route(self) -> str:
        """Return the localized column path for an article's canonical route."""
        parts = self.path.split("/")
        if len(parts) == 6 and parts[1:3] == [self.lang, "articles"]:
            return f"/{self.lang}/articles/{self.column_slug}"
        return f"/columns/{self.column_slug}"

    def event_group(self) -> str:
        """Return the parent path of an event page, if it belongs to one."""
        pieces = self.path.split("/")
        if self.kind == "event" and len(pieces) == 6 and pieces[2] == "events":
            return self.path.rpartition("/")[0]
        return ""


@dataclass(frozen=True, slots=True)
class ArticleSource:
    """Store article Markdown, page metadata, and source links."""

    document: Document
    markdown: str
    wayback_url: str = ""
    event_code: str = ""
    description: str = ""
    image_url: str = ""
    source_url: str = ""

    @classmethod
    def read(cls, source: Path) -> ArticleSource:
        """Read an archived article and its YAML header."""
        text = source.read_text(encoding="utf-8")
        if not text.startswith(_FRONT_MATTER_START):
            raise ValueError(f"Missing YAML front matter in {source}")
        header, boundary, markdown = text[len(_FRONT_MATTER_START) :].partition(
            _FRONT_MATTER_END
        )
        if not boundary:
            raise ValueError(f"Unclosed YAML front matter in {source}")
        try:
            metadata = yaml.load(header, Loader=_YAML_LOADER)
        except yaml.YAMLError as error:
            raise ValueError(f"Invalid YAML front matter in {source}") from error
        # A malformed YAML value is an archive data error.
        if not isinstance(metadata, dict):
            raise ValueError(  # noqa: TRY004
                f"Expected YAML front matter to be a mapping in {source}"
            )
        archive_source = metadata.get("source") or metadata.get("archive_source") or {}
        if not isinstance(archive_source, dict):
            raise ValueError(  # noqa: TRY004
                f"Expected the archive source to be a mapping in {source}"
            )
        description = metadata.get("description")
        image_url = metadata.get("image")
        return cls(
            Document.read(metadata),
            markdown,
            wayback_url=str(archive_source.get("wayback_url") or ""),
            event_code=str(metadata.get("event_code") or ""),
            description=description.strip() if isinstance(description, str) else "",
            image_url=image_url.strip() if isinstance(image_url, str) else "",
            source_url=str(archive_source.get("url") or ""),
        )

    def render(
        self, *, body: str | None = None, embeds: tuple[FlashItem, ...] = ()
    ) -> str:
        """Render the article page with its byline and source links."""
        document = self.document
        event_path = document.event_group() if not document.column_slug else ""
        event_label = (
            (self.event_code or event_path.rpartition("/")[2]).replace("_", " ")
            if event_path
            else ""
        )
        description = self.description
        if not description and document.authors:
            description = "By " + ", ".join(person.name for person in document.authors)
        if body is None:
            body = render_body(self.markdown)
        body, extra = _place_flash(body, embeds)
        return render_page(
            "article.html",
            document.title,
            document.path,
            lang=document.lang,
            document=document,
            day=document.day,
            body=Markup(body),
            flash_after_body=Markup(extra),
            flash_player=bool(embeds),
            flash_puzzle=any(item.image_digest for item in embeds),
            event_path=event_path,
            event_label=event_label,
            wayback_url=self.wayback_url if web_url(self.wayback_url) else "",
            description=description,
            image_url=self.image_url if web_url(self.image_url) else "",
        )


def render_document(
    job: tuple[Path, Path],
    *,
    flash: FlashReferences | None = None,
    media_links: MediaLinks | None = None,
) -> Document:
    """Write the rendered page and return its metadata."""
    source, output = job
    article = ArticleSource.read(source)
    document = article.document
    body = render_body(article.markdown)
    embeds: tuple[FlashItem, ...] = ()
    if flash is not None:
        linked = tuple(unescape(target) for target in _FLASH_LINK.findall(body))
        embeds = flash.matches(
            document.id,
            article.source_url,
            linked,
            marker_ids=tuple(marker[1] for marker in _FLASH_MARKER.finditer(body)),
        )
    if media_links is not None:
        body = media_links.rewrite(body)
    write_new(
        site_file(output, document.path), article.render(body=body, embeds=embeds)
    )
    return (
        replace(document, flash_ids=tuple(item.id for item in embeds))
        if embeds
        else document
    )

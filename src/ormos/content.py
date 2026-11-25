"""Read archived Markdown documents and render their public pages."""

import re
from dataclasses import dataclass
from datetime import date
from html import escape
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import cmarkgfm
import nh3
import yaml

from .html import layout, link
from .paths import component, route, site_file, write_new

_FRONT_MATTER_START = "---\n"
_FRONT_MATTER_END = "\n---\n"
_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
_UNKNOWN_PUBLICATION_DAYS = frozenset({date(1969, 12, 31), date(1970, 1, 1)})
_RAW_TABLE = re.compile(r"<table\b[^>]*>.*?</table\s*>", re.IGNORECASE | re.DOTALL)
_TABLE_INTERRUPTION = re.compile(r"\n[ \t]*\n")
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


def time_element(value: str) -> str:
    """Render a time element for a known publication date."""
    day = publication_day(value)
    if day is None:
        return ""
    return f'<time datetime="{day.isoformat()}">{day.day} {day:%B %Y}</time>'


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
    clean = clean.replace("<img ", '<img loading="lazy" decoding="async" ')
    return clean.replace(
        "<table>",
        '<div class="table-scroll" tabindex="0" role="region" aria-label="Table"><table>',
    ).replace("</table>", "</table></div>")


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

    @classmethod
    def read(cls, metadata: dict[str, Any]) -> "Document":
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

    def column_route(self) -> str:
        """Return the archive path for the document's column."""
        local = f"/{self.lang}/articles/{self.column_slug}"
        return (
            local
            if self.path.startswith(f"{local}/")
            else f"/columns/{self.column_slug}"
        )

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

    @classmethod
    def read(cls, source: Path) -> "ArticleSource":
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
        return cls(
            Document.read(metadata),
            markdown,
            wayback_url=str(archive_source.get("wayback_url") or ""),
            event_code=str(metadata.get("event_code") or ""),
        )

    def render(self) -> str:
        """Render the article page with its byline and source links."""
        document = self.document
        details = []
        if document.authors:
            people = ", ".join(
                link(f"/{document.lang}/authors/{person.slug}", person.name)
                for person in document.authors
            )
            byline = f'<span data-pagefind-meta="author">{people}</span>'
            details.append(f"<span>By {byline}</span>")
        if published := time_element(document.published):
            details.append(published)
        if document.column_slug:
            details.append(
                link(
                    document.column_route(),
                    document.column,
                    **{"data-pagefind-meta": "column"},
                )
            )
        elif group := document.event_group():
            label = (self.event_code or group.rpartition("/")[2]).replace("_", " ")
            details.append(link(group, label, **{"data-pagefind-meta": "event"}))
        metadata = f'<div class="byline">{"".join(details)}</div>' if details else ""
        source_links = [link(f"/id/{document.id}", "Permanent link")]
        if web_url(self.wayback_url):
            source_links.append(
                link(self.wayback_url, "Archived capture", rel="nofollow")
            )
        provenance = " · ".join(source_links)
        content = f"""
<article data-pagefind-body>
<header class="article-header">
<h1 data-pagefind-meta="title">{escape(document.title)}</h1>
{metadata}
</header>
<div class="article-body">{render_body(self.markdown)}</div>
<footer class="article-footer" data-pagefind-ignore>{provenance}</footer>
</article>"""
        return layout(document.title, document.path, content, lang=document.lang)


def render_document(job: tuple[Path, Path]) -> Document:
    """Write the rendered page and return its metadata."""
    source, output = job
    article = ArticleSource.read(source)
    write_new(site_file(output, article.document.path), article.render())
    return article.document

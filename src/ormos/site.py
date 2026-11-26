"""Generate archive navigation pages and redirects."""

import json
import re
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Literal

from .content import Document
from .flash import FlashLibrary
from .html import (
    FLASH_ROUTE,
    MEDIA_ROUTE,
    SITE_NAME,
    VIDEO_ROUTE,
    render_page,
    render_template,
)
from .paths import component, route, site_file, write_new
from .videos import VideoLibrary

PAGE_SIZE = 200
CountedLink = tuple[str, str, int]


def publication_order(entry: Document) -> tuple[bool, date | None]:
    """Return a sort key that puts undated documents last."""
    published = entry.day
    return published is None, published


def _page_path(path: str, index: int) -> str:
    return path if index == 1 else f"{path}/page/{index}"


EVENT_TYPES = {
    "leagues": "Leagues",
    "preliminaries": "Preliminaries",
    "challenges": "Challenges",
    "showcases": "Showcases",
    "daily-events": "Daily events",
    "premier-events": "Premier events",
    "qualifiers": "Qualifiers",
    "pro-tours": "Pro Tours",
    "players-tours": "Players Tours",
    "grand-prix": "Grand Prix",
    "trials": "Grand Prix Trials",
    "world-championships": "World Championships",
    "world-magic-cups": "World Magic Cups",
    "regional-championships": "Regional Championships",
    "nationals": "National Championships",
    "mythic-championships": "Mythic Championships",
    "championships": "Other championships",
    "opens": "Opens",
    "other": "Other events",
}
EVENT_RULES = tuple(
    (kind, re.compile(rf"\b(?:{pattern})\b"))
    for kind, pattern in (
        ("showcases", "showcases?"),
        ("qualifiers", "qualifiers?|ptq|pptq|champ qual"),
        ("preliminaries", "preliminar(?:y|ies)|prelims?"),
        ("leagues", "leagues?"),
        ("challenges", "challenges?"),
        ("daily-events", "daily"),
        ("premier-events", "premier"),
        ("world-championships", "world championships?|worlds"),
        ("world-magic-cups", "world magic cups?"),
        ("regional-championships", "regional championships?|regionals"),
        ("nationals", "national championships?|nationals"),
        ("pro-tours", "pro tours?"),
        ("players-tours", "players tours?"),
        ("trials", "grand prix trials?"),
        ("grand-prix", "grand prix"),
        ("mythic-championships", "mythic championships?"),
        ("championships", "championships?|mocs"),
        ("opens", "opens?"),
    )
)
LEGACY_EVENT_RULES = tuple(
    (kind, re.compile(pattern))
    for kind, pattern in (
        ("grand-prix", r"gp[a-z][a-z0-9]{1,}(?: [a-z0-9]+)?"),
        ("pro-tours", r"pt(?!q|tq)[a-z][a-z0-9]{1,}(?: [a-z0-9]+)?"),
        ("world-championships", r"worlds(?: ?\d{2,4})?"),
        ("nationals", r"[a-z]{2}nat(?:\d{2,4})?(?:[a-z]{2})?"),
    )
)
EVENT_FORMATS = {
    "alchemy": "Alchemy",
    "block": "Block Constructed",
    "brawl": "Brawl",
    "commander": "Commander",
    "draft": "Draft",
    "explorer": "Explorer",
    "historic": "Historic",
    "legacy": "Legacy",
    "limited": "Limited",
    "modern": "Modern",
    "pauper": "Pauper",
    "pioneer": "Pioneer",
    "sealed": "Sealed",
    "standard": "Standard",
    "vintage": "Vintage",
}
EVENT_FORMAT = re.compile(
    rf"^(?:team )?({'|'.join(EVENT_FORMATS)})\b(?! horizons\b| masters\b)"
)
EVENT_NAME_PREFIX = re.compile(
    r"^(?:(?:19|20)\d{2}(?: \d{1,2} \d{1,2})? |magic online |mtgo |competitive |friendly )+"
)
FORMATTED_EVENT_TYPES = {
    "leagues",
    "preliminaries",
    "challenges",
    "showcases",
    "daily-events",
    "premier-events",
    "opens",
}


def event_evidence(value: str, *, code: bool = False) -> tuple[str | None, str | None]:
    """Find an event type and game format in a title or event code."""
    name = EVENT_NAME_PREFIX.sub(
        "", re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()
    )
    match = EVENT_FORMAT.match(name)
    format_slug = match[1] if match else None
    if code:
        kind = next((kind for kind, rule in EVENT_RULES if rule.search(name)), None)
        legacy = next(
            (kind for kind, rule in LEGACY_EVENT_RULES if rule.fullmatch(name)), None
        )
        return kind or legacy, format_slug

    if match:
        name = re.sub(
            r"^(?:constructed |1 v 1 |festival |[a-z0-9]+ block )+",
            "",
            name[match.end() :].lstrip(),
        )
    for kind, rule in EVENT_RULES:
        if rule.match(name) and (format_slug or kind not in FORMATTED_EVENT_TYPES):
            return kind, format_slug
    return None, format_slug


def classify_event(code: str, records: list[Document]) -> tuple[str, str | None]:
    """Classify an event by its code and the titles of its documents."""
    kind, format_slug = event_evidence(code, code=True)
    if kind and format_slug:
        return kind, format_slug
    title_evidence = {event_evidence(record.title) for record in records}
    if not kind:
        title_kinds = {candidate for candidate, _ in title_evidence if candidate}
        if len(title_kinds) == 1:
            kind = title_kinds.pop()
    if not format_slug:
        formats = {
            candidate
            for title_kind, candidate in title_evidence
            if title_kind == kind and candidate
        }
        if len(formats) == 1:
            format_slug = formats.pop()
    return kind or "other", format_slug


@dataclass(frozen=True, slots=True)
class Redirect:
    """A source path, its canonical destination, and the reason for the move."""

    path: str
    target: str
    kind: str


class Site:
    """Track the pages and redirects written to one site directory."""

    def __init__(self, output: Path):
        """Start with an empty page registry for the output directory."""
        self.output = output
        self.entries: dict[str, Document] = {}
        self.paths: set[str] = set()
        self.redirects: dict[str, Redirect] = {}

    def _record_path(self, path: str) -> None:
        if path in self.paths:
            raise ValueError(f"Multiple pages use {path}")
        self.paths.add(path)

    def page(self, path: str, html: str) -> None:
        """Register the page path and write its HTML file."""
        path = route(path)
        self._record_path(path)
        write_new(site_file(self.output, path), html)

    def add_document(self, document: Document) -> None:
        """Register a document after its page is written."""
        if document.id in self.entries:
            raise ValueError(f"Duplicate document ID {document.id}")
        self._record_path(document.path)
        self.entries[document.id] = document

    def entries_page(
        self,
        path: str,
        title: str,
        entries: list[Document],
        *,
        lang: str = "en",
        table_column: Literal["author", "column"] | None = None,
        paginate: bool = True,
        year_links: Sequence[tuple[str, str]] = (),
        formats: Sequence[CountedLink] = (),
    ) -> int:
        """Sort documents in place, write their pages, and return the page count."""
        # Stable path ordering breaks ties between documents with the same publication day.
        entries.sort(key=lambda entry: entry.path)
        if table_column:
            entries.sort(key=publication_order)
        else:
            entries.sort(key=lambda entry: entry.published, reverse=True)
        page_size = PAGE_SIZE if paginate else max(1, len(entries))
        pages = max(1, (len(entries) + page_size - 1) // page_size)
        for index in range(1, pages + 1):
            page = _page_path(path, index)
            selected = entries[(index - 1) * page_size : index * page_size]
            page_title = title if index == 1 else f"{title} (page {index})"
            self.page(
                page,
                render_page(
                    "entries.html",
                    page_title,
                    page,
                    lang=lang,
                    script="/assets/column-sort.js"
                    if table_column and selected
                    else "",
                    heading=title,
                    records=selected,
                    table_column=table_column,
                    year_links=year_links if index == 1 else (),
                    formats=formats if index == 1 else (),
                    index=index,
                    pages=pages,
                    previous=_page_path(path, index - 1) if index > 1 else "",
                    next_page=_page_path(path, index + 1) if index < pages else "",
                ),
            )
        return pages

    def groups_page(
        self,
        path: str,
        title: str,
        groups: list[CountedLink],
        *,
        lang: str = "en",
        column_directory: bool = False,
    ) -> None:
        """Write a directory page with links and document counts for each group."""
        self.page(
            path,
            render_page(
                "directory.html",
                title,
                path,
                lang=lang,
                groups=groups,
                column_directory=column_directory,
            ),
        )

    def column_year_pages(
        self,
        path: str,
        title: str,
        years: dict[str, list[Document]],
        *,
        lang: str = "en",
        segment: str = "",
    ) -> list[tuple[str, str]]:
        """Write the yearly article tables and return links to them."""
        links = []
        for year, records in sorted(years.items(), reverse=True):
            year_path = f"{path}/{segment}{year}"
            label = "Undated" if year == "undated" else year
            links.append((year_path, label))
            self.entries_page(
                year_path,
                f"{title} · {label}",
                records,
                lang=lang,
                table_column="author",
            )
        return links

    def column_pages(
        self, slug: str, title: str, records: list[Document]
    ) -> list[tuple[str, CountedLink]]:
        """Write pages for a column and return its entries in each language directory."""
        years = defaultdict(list)
        localized = defaultdict(list)
        localized_years: defaultdict[str, defaultdict[str, list[Document]]] = (
            defaultdict(lambda: defaultdict(list))
        )
        for entry in records:
            if day := entry.day:
                years[str(day.year)].append(entry)
            parts = entry.path.split("/")
            if len(parts) == 6 and parts[1:4] == [entry.lang, "articles", slug]:
                localized[entry.lang].append(entry)
                localized_years[entry.lang][parts[4]].append(entry)

        path = f"/columns/{slug}"
        year_links = self.column_year_pages(path, title, years, segment="year/")
        self.entries_page(
            path, title, records, year_links=year_links, table_column="author"
        )

        choices = []
        for lang, language_records in localized.items():
            path = f"/{lang}/articles/{slug}"
            year_links = self.column_year_pages(
                path, title, localized_years[lang], lang=lang
            )
            self.entries_page(
                path,
                title,
                language_records,
                lang=lang,
                year_links=year_links,
                table_column="author",
            )
            choices.append((lang, (path, title, len(language_records))))
        return choices

    def column_navigation(self, columns: dict[str, list[Document]]) -> None:
        """Write column pages and the directories that link to them."""
        names = {
            slug: min(records, key=lambda entry: entry.path).column
            for slug, records in columns.items()
        }
        slugs = sorted(names, key=lambda slug: (names[slug].casefold(), slug))
        self.groups_page(
            "/columns",
            "Columns",
            [(f"/columns/{slug}", names[slug], len(columns[slug])) for slug in slugs],
            column_directory=True,
        )
        language_columns = defaultdict(list)
        for slug in slugs:
            for lang, choice in self.column_pages(slug, names[slug], columns[slug]):
                language_columns[lang].append(choice)
        for lang, groups in language_columns.items():
            self.groups_page(
                f"/{lang}/articles",
                "Columns",
                sorted(groups, key=lambda row: (row[1].casefold(), row[0])),
                lang=lang,
                column_directory=True,
            )

    def article_navigation(self, articles: list[Document]) -> None:
        """Write the Articles landing page and the full chronological list."""
        all_path = "/articles/all"
        self.entries_page(all_path, "All articles", articles)
        self.page(
            "/articles",
            render_page(
                "articles.html",
                "Articles",
                "/articles",
                all_path=all_path,
                count=len(articles),
            ),
        )

    def event_navigation(
        self,
        events: list[Document],
        *,
        has_decks: bool = False,
        has_videos: bool = False,
    ) -> None:
        """Write event directories by name, type, and game format."""
        event_groups = defaultdict(list)
        event_types: defaultdict[str, defaultdict[str | None, list[Document]]] = (
            defaultdict(lambda: defaultdict(list))
        )
        for event in events:
            if group := event.event_group():
                event_groups[group].append(event)
            else:
                kind, format_slug = classify_event("", [event])
                event_types[kind][format_slug].append(event)

        event_choices = []
        for group, records in sorted(
            event_groups.items(), key=lambda item: item[0].split("/")[3:], reverse=True
        ):
            _, lang, _, year, code = group.split("/")
            kind, format_slug = classify_event(code, records)
            event_types[kind][format_slug].extend(records)
            title = f"{code.replace('-', ' ')} ({year})"
            self.entries_page(group, title, records, lang=lang)
            label = title if lang == "en" else f"{title} · {lang}"
            event_choices.append((group, label, len(records)))
        if event_choices:
            self.groups_page("/events/by-event", "Browse by event", event_choices)

        sections = []
        for kind, title in EVENT_TYPES.items():
            buckets = event_types.get(kind)
            if not buckets:
                continue
            path = f"/events/by-type/{kind}"
            records = [entry for bucket in buckets.values() for entry in bucket]
            formats: list[CountedLink] = []
            if any(buckets):
                for format_slug in sorted(
                    buckets, key=lambda value: (value is None, value or "")
                ):
                    format_title = EVENT_FORMATS.get(
                        format_slug or "", "Format not recorded"
                    )
                    format_path = f"{path}/{format_slug or 'unknown-format'}"
                    matches = buckets[format_slug]
                    self.entries_page(format_path, f"{format_title} · {title}", matches)
                    formats.append((format_path, format_title, len(matches)))
            self.entries_page(path, title, records, formats=formats)
            sections.append((path, title, len(records), formats))

        links = [("/events/all", "All event documents")]
        if event_choices:
            links.append(("/events/by-event", "Browse by event name"))
        if has_decks:
            links.append(("/decks", "Decks"))
        if has_videos:
            links.append((VIDEO_ROUTE, "Videos"))
        self.page(
            "/events",
            render_page(
                "events.html", "Events", "/events", links=links, sections=sections
            ),
        )
        pages = self.entries_page("/events/all", "All event documents", events)
        for index in range(2, pages + 1):
            self.redirect(
                f"/events/page/{index}",
                f"/events/all/page/{index}",
                "events-pagination",
            )

    def navigation(
        self, library: VideoLibrary, flash: FlashLibrary | None = None
    ) -> None:
        """Write the home page, archive directories, and search pages."""
        videos = library.videos
        authors = defaultdict(list)
        author_names: dict[str, str] = {}
        columns = defaultdict(list)
        years = defaultdict(list)
        articles = []
        events = []
        decks = []
        localized_authors = defaultdict(list)
        for entry in sorted(self.entries.values(), key=lambda value: value.path):
            if entry.kind == "event":
                events.append(entry)
            elif entry.kind.startswith("deck"):
                decks.append(entry)
            else:
                articles.append(entry)
            if day := entry.day:
                years[str(day.year)].append(entry)
            if entry.column_slug:
                columns[entry.column_slug].append(entry)
            for person in dict.fromkeys(entry.authors):
                authors[person.slug].append(entry)
                author_names.setdefault(person.slug, person.name)
                localized_authors[(entry.lang, person.slug)].append(entry)

        self.article_navigation(articles)
        self.event_navigation(events, has_decks=bool(decks), has_videos=bool(videos))
        if decks:
            self.entries_page("/decks", "Decks", decks)

        author_slugs = sorted(
            author_names, key=lambda slug: (author_names[slug].casefold(), slug)
        )
        self.groups_page(
            "/authors",
            "Authors",
            [
                (f"/authors/{slug}", author_names[slug], len(authors[slug]))
                for slug in author_slugs
            ],
        )
        for slug in author_slugs:
            self.entries_page(
                f"/authors/{slug}",
                author_names[slug],
                authors[slug],
                table_column="column",
                paginate=False,
            )
        for (lang, slug), records in localized_authors.items():
            self.entries_page(
                f"/{lang}/authors/{slug}",
                author_names[slug],
                records,
                lang=lang,
                table_column="column",
                paginate=False,
            )

        self.column_navigation(columns)

        self.groups_page(
            "/years",
            "Years",
            [
                (f"/years/{year}", year, len(records))
                for year, records in sorted(years.items(), reverse=True)
            ],
        )
        for year, records in years.items():
            self.entries_page(f"/years/{year}", year, records)

        choices = [
            ("/articles", "Articles", len(articles)),
            ("/columns", "Columns", len(columns)),
            ("/authors", "Authors", len(authors)),
            ("/years", "Years", len(years)),
            ("/events", "Events", len(events)),
        ]
        if decks:
            choices.append(("/decks", "Decks", len(decks)))
        media: list[CountedLink] = []
        if videos:
            library.write(self)
            media.append((VIDEO_ROUTE, "Videos", len(videos)))
        if flash and flash.items:
            flash.write_pages(self)
            media.append((FLASH_ROUTE, "Flash", len(flash.items)))
        self.groups_page(MEDIA_ROUTE, "Media", media)
        if media:
            choices.append((MEDIA_ROUTE, "Media", sum(count for _, _, count in media)))
        self.groups_page("/", SITE_NAME, choices)
        self.search_navigation(articles)

    def search_navigation(self, articles: list[Document]) -> None:
        """Write localized search pages with filters for archived articles."""
        columns: defaultdict[str, dict[str, str]] = defaultdict(dict)
        authors: defaultdict[str, dict[str, str]] = defaultdict(dict)
        years: defaultdict[str, set[int | None]] = defaultdict(set)
        for article in articles:
            if article.kind != "article":
                continue
            lang = article.lang.lower()
            if article.column_slug:
                columns[lang].setdefault(article.column_slug, article.column)
            for author in article.authors:
                authors[lang].setdefault(author.slug, author.name)
            day = article.day
            years[lang].add(day.year if day else None)

        languages = sorted(
            {component(entry.lang).lower() for entry in self.entries.values()} | {"en"}
        )
        search_pages = {
            lang: ("/search" if lang == "en" else f"/search/{lang}")
            for lang in languages
        }
        for language, path in search_pages.items():
            known_years = sorted(
                (year for year in years[language] if year is not None), reverse=True
            )
            year_options = [(str(year), str(year)) for year in known_years]
            if None in years[language]:
                year_options.append(("undated", "Undated"))
            filter_options = [
                (
                    name,
                    label,
                    sorted(
                        values[language].items(),
                        key=lambda option: (option[1].casefold(), option[0]),
                    ),
                )
                for name, label, values in (
                    ("column", "Column", columns),
                    ("author", "Author", authors),
                )
            ]
            filter_options.append(("year", "Publication year", year_options))
            self.page(
                path,
                render_page(
                    "search.html",
                    "Search",
                    path,
                    lang=language,
                    script="/assets/search.js",
                    search_pages=search_pages,
                    filter_options=filter_options,
                ),
            )

    def redirect(self, source: str, target: str, kind: str) -> None:
        """Write a redirect page to an existing canonical destination."""
        source = route(source)
        target = route(target)
        if source == target:
            return
        previous = self.redirects.get(source)
        if previous:
            if previous.target != target:
                raise ValueError(
                    f"Conflicting redirect targets for {source}: {previous.target} and {target}"
                )
            return
        if target not in self.paths or target in self.redirects:
            raise ValueError(
                f"Redirect {source} needs a canonical destination, got {target}"
            )
        if source in self.paths:
            raise ValueError(f"Redirect {source} conflicts with a site page")
        self.page(source, render_template("redirect.html", target=target))
        self.redirects[source] = Redirect(source, target, kind)

    def write_redirects(self, path: Path) -> None:
        """Write the redirect table as JSON lines in source path order."""
        with path.open("w", encoding="utf-8", newline="\n") as stream:
            for source in sorted(self.redirects):
                stream.write(
                    json.dumps(asdict(self.redirects[source]), ensure_ascii=False)
                    + "\n"
                )

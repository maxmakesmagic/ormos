"""Mark unavailable recordings and substitute known recovered copies."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import SplitResult, urlencode, urlsplit

from .html import MEDIA_ORIGIN
from .paths import read_json_lines

MEDIA_NOT_FOUND_ROUTE = "/media-not-found"
MEDIA_NOT_FOUND_SCRIPT = "media-not-found.js"
_WARNING = (
    '<span class="missing-media-warning" aria-hidden="true">⚠</span>'
    '<span class="visually-hidden"> (Media not found)</span>'
)
_WIZARDS = re.compile(r"wizards\.com", re.IGNORECASE)
_WAYBACK_SOURCE = re.compile(
    r"https?://web\.archive\.org/web/[0-9]{1,14}(?:[a-z]{1,8}_)?/(https?://.+)",
    re.IGNORECASE,
)
_TRAILING_SPACE = re.compile(r"(?:%20|[ \t])+\Z", re.IGNORECASE)
_UNSAFE_TARGET = re.compile(r"[\s\x00-\x1f\x7f\\#]")


def _wizards_url(url: object) -> SplitResult | None:
    if not isinstance(url, str):
        return None
    try:
        parts = urlsplit(url)
        host = parts.hostname or ""
        if (
            parts.scheme in {"http", "https"}
            and (host == "wizards.com" or host.endswith(".wizards.com"))
            and parts.username is None
            and parts.port in {None, 80 if parts.scheme == "http" else 443}
        ):
            return parts
    except ValueError:
        pass
    return None


def _recovery_key(parts: SplitResult) -> tuple[str, str, str]:
    host = parts.hostname or ""
    if host == "www.wizards.com":
        host = "wizards.com"
    return host, parts.path, parts.query


def _media_target(target: object) -> str | None:
    if (
        not isinstance(target, str)
        or not target.startswith("https://")
        or _UNSAFE_TARGET.search(target)
    ):
        return None
    if target.startswith((f"{MEDIA_ORIGIN}/", "https://media.wizards.com/")):
        return target
    if (replay := _WAYBACK_SOURCE.fullmatch(target)) and _wizards_url(replay[1]):
        return target
    return None


@dataclass(frozen=True, slots=True)
class MediaLinks:
    """Keep link decisions for reviewed media addresses."""

    missing: frozenset[str]
    recovered: dict[tuple[str, str, str], str | None]

    @classmethod
    def read(cls, data: Path) -> MediaLinks:
        """Read media mappings and the list of unavailable addresses."""
        registry = data / "missing-media.jsonl"
        missing = set()
        if registry.is_file():
            for row in read_json_lines(registry):
                url = row.get("url")
                if _wizards_url(url) is None:
                    raise ValueError(f"Invalid missing media address: {url!r}")
                missing.add(row["url"].partition("#")[0])

        hosted: defaultdict[tuple[str, str, str], set[str]] = defaultdict(set)
        external: defaultdict[tuple[str, str, str], set[str]] = defaultdict(set)
        mapping = data / "media-urls.jsonl"
        if mapping.is_file():
            for row in read_json_lines(mapping):
                if row.get("kind") != "media":
                    continue
                source = _wizards_url(row.get("original_url"))
                target = _media_target(row.get("target_url"))
                if source is not None and target is not None:
                    copies = (
                        hosted if target.startswith(f"{MEDIA_ORIGIN}/") else external
                    )
                    copies[_recovery_key(source)].add(target)
        podcasts = data / "podcasts.json"
        if podcasts.is_file():
            explicit_keys = set(hosted)
            for row in json.loads(podcasts.read_bytes())["podcasts"]:
                target = _media_target(row["url"])
                if target is None or not target.startswith(f"{MEDIA_ORIGIN}/"):
                    continue
                for alias in row.get("original_urls", []):
                    if (source := _wizards_url(alias)) is not None and (
                        key := _recovery_key(source)
                    ) not in explicit_keys:
                        hosted[key].add(target)
        # Several copies suppress the warning without choosing a version.
        recovered = {
            key: next(iter(copies)) if len(copies) == 1 else None
            for key, copies in (external | hosted).items()
        }
        return cls(frozenset(missing), recovered)

    def destination(self, url: str) -> tuple[str | None, bool]:
        """Return the replacement destination and whether a warning is needed."""
        address, marker, fragment = url.partition("#")
        if replay := _WAYBACK_SOURCE.fullmatch(address):
            address = replay[1]
        if (parts := _wizards_url(address)) is None:
            return None, False
        key = _recovery_key(parts)
        if address not in self.missing and key not in self.recovered:
            path, separator, query = address.partition("?")
            address = _TRAILING_SPACE.sub("", path) + separator + query
            key = (key[0], _TRAILING_SPACE.sub("", key[1]), key[2])
        if key in self.recovered:
            target = self.recovered[key]
            return (target + marker + fragment if target else None), False
        if address in self.missing:
            return f"{MEDIA_NOT_FOUND_ROUTE}?{urlencode({'url': url})}", True
        return None, False

    def rewrite(self, body: str) -> str:
        """Rewrite anchors in sanitized HTML while preserving everything around them."""
        if not (self.missing or self.recovered) or not _WIZARDS.search(body):
            return body
        parser = _MediaAnchorRewriter(self, body)
        parser.feed(body)
        parser.close()
        return parser.result()


class _MediaAnchorRewriter(HTMLParser):
    def __init__(self, links: MediaLinks, body: str) -> None:
        super().__init__(convert_charrefs=False)
        self.links = links
        self.body = body
        self.line_offsets = [0, *(newline.end() for newline in re.finditer("\n", body))]
        self.edits: list[tuple[int, int, str]] = []
        self.warn = False

    def _offset(self) -> int:
        line, column = self.getpos()
        return self.line_offsets[line - 1] + column

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        url = dict(attrs).get("href")
        if url is None:
            return
        target, self.warn = self.links.destination(url)
        if target is None:
            return
        start = self._offset()
        opening = self.get_starttag_text()
        if opening is not None:
            markup = [
                f' {name}="{escape(target if name == "href" else (value or ""))}"'
                for name, value in attrs
            ]
            self.edits.append((start, start + len(opening), f"<a{''.join(markup)}>"))

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self.warn:
            offset = self._offset()
            self.edits.append((offset, offset, _WARNING))
            self.warn = False

    def result(self) -> str:
        output = []
        cursor = 0
        for start, end, value in self.edits:
            output += [self.body[cursor:start], value]
            cursor = end
        return "".join([*output, self.body[cursor:]])

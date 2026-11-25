"""Write the public sitemap index and its URL lists."""

from collections.abc import Iterable
from pathlib import Path
from xml.sax.saxutils import escape

from .html import PUBLIC_ARCHIVE_ORIGIN
from .paths import route, write_new

MAX_URLS = 50_000
MAX_BYTES = 50 * 1024 * 1024
XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n'
NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
URLSET_START = f'{XML_HEADER}<urlset xmlns="{NAMESPACE}">\n'
URLSET_END = "</urlset>\n"
URLSET_OVERHEAD = len((URLSET_START + URLSET_END).encode("utf-8"))


class Sitemap:
    """Split canonical URLs into sitemaps under the protocol size limits."""

    def __init__(self, output: Path) -> None:
        """Use the site output directory for the sitemap and robots files."""
        self.output = output

    def write(self, paths: Iterable[str]) -> None:
        """Write sitemaps for unique canonical paths."""
        canonical = sorted({route(path) for path in paths})
        if not canonical:
            raise ValueError("A sitemap needs at least one page")

        files: list[str] = []
        entries: list[str] = []
        size = URLSET_OVERHEAD
        for path in canonical:
            location = PUBLIC_ARCHIVE_ORIGIN + path
            if len(location) >= 2048:
                raise ValueError(f"Sitemap URL is too long: {path}")
            entry = f"  <url><loc>{escape(location)}</loc></url>\n"
            entry_size = len(entry.encode("utf-8"))
            if len(entries) == MAX_URLS or size + entry_size > MAX_BYTES:
                files.append(self._write_urls(len(files) + 1, entries))
                entries = []
                size = URLSET_OVERHEAD
            entries.append(entry)
            size += entry_size
        files.append(self._write_urls(len(files) + 1, entries))

        index = "".join(
            f"  <sitemap><loc>{PUBLIC_ARCHIVE_ORIGIN}/{name}</loc></sitemap>\n"
            for name in files
        )
        write_new(
            self.output / "sitemap.xml",
            f'{XML_HEADER}<sitemapindex xmlns="{NAMESPACE}">\n{index}</sitemapindex>\n',
        )
        write_new(
            self.output / "robots.txt",
            f"Sitemap: {PUBLIC_ARCHIVE_ORIGIN}/sitemap.xml\n",
        )

    def _write_urls(self, number: int, entries: list[str]) -> str:
        name = f"sitemap-{number:03}.xml"
        write_new(self.output / name, URLSET_START + "".join(entries) + URLSET_END)
        return name

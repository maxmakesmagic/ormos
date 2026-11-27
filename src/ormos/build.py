"""Build a static archive site from Markdown and its companion data."""

import argparse
import logging
import os
from dataclasses import dataclass
from itertools import chain
from multiprocessing import get_context
from pathlib import Path
from shutil import copyfile
from tempfile import TemporaryDirectory

from .content import Document, render_document
from .flash import FlashLibrary, FlashReferences
from .html import FLASH_ROUTE, FLASH_SCRIPT, MEDIA_ROUTE, PODCAST_ROUTE
from .paths import read_json_lines
from .podcasts import PodcastLibrary
from .search import SearchIndex
from .site import Site
from .sitemap import Sitemap
from .videos import VIDEO_SCRIPT, VideoLibrary

ASSETS = Path(__file__).with_name("assets")
SITE_ASSETS = ("archive.css", "column-sort.js", "search.js")
URL_MAPS = ("wizards-urls.csv", "wizards-urls.jsonl")
logger = logging.getLogger(__name__)
_worker_flash: FlashReferences | None = None


def _init_render_worker(flash: FlashReferences | None) -> None:
    global _worker_flash
    _worker_flash = flash


def _render_archive_document(job: tuple[Path, Path]) -> Document:
    return render_document(job, flash=_worker_flash)


@dataclass(frozen=True, slots=True)
class BuildResult:
    """Counts of documents and redirects in the generated site."""

    documents: int
    redirects: int


@dataclass(frozen=True, slots=True)
class ArchiveBuilder:
    """Own the input paths and settings for one complete site build."""

    source: Path
    data: Path
    output: Path
    jobs: int

    def build(self) -> BuildResult:
        """Render the archive and publish the output after indexing succeeds."""
        source = self.source.resolve()
        data = self.data.resolve()
        output = self.output.resolve()
        content = source / "content"
        if not content.is_dir():
            raise ValueError(f"Expected a content directory in {source}")
        if not data.is_dir():
            raise ValueError(f"Expected an archive data directory at {data}")
        if self.jobs < 1:
            raise ValueError("Use at least one rendering process")
        for directory in (source, data):
            if (
                output == directory
                or directory in output.parents
                or output in directory.parents
            ):
                raise ValueError(
                    "The site destination must be separate from the inputs"
                )
        if output.exists() or self.output.is_symlink():
            raise FileExistsError(f"Destination already exists: {self.output}")

        files = sorted(content.rglob("*.md"))
        if not files:
            raise ValueError(f"No Markdown documents in {content}")
        library = VideoLibrary.read(data)
        flash = FlashLibrary.read(data)
        podcasts = PodcastLibrary.read(data)
        output.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(
            prefix=f".{output.name}-", dir=output.parent
        ) as staging_directory:
            site = Site(Path(staging_directory))
            self._copy_assets(site.output, library, flash, podcasts)
            self._render_documents(
                site, files, flash.references() if flash.items else None
            )
            site.navigation(library, flash, podcasts)
            self._add_redirects(site, data)
            self._copy_url_map(site.output, data)
            Sitemap(site.output).write(
                chain(
                    ("/", MEDIA_ROUTE),
                    (document.path for document in site.entries.values()),
                    (video.path for video in library.videos),
                    (FLASH_ROUTE,) if flash.items else (),
                    (item.path for item in flash.items),
                    (PODCAST_ROUTE,) if podcasts.episodes else (),
                    (episode.path for episode in podcasts.episodes),
                )
            )
            plan = data / "search-plan.json"
            SearchIndex(site.output).build(
                site.entries.values(), plan if plan.is_file() else None
            )
            if output.exists() or output.is_symlink():
                raise FileExistsError(f"Destination already exists: {output}")
            site.output.rename(output)
        return BuildResult(len(site.entries), len(site.redirects))

    def _render_documents(
        self, site: Site, files: list[Path], flash: FlashReferences | None
    ) -> None:
        jobs = ((file, site.output) for file in files)
        # Recycle processes because the Markdown converter retains native memory.
        with get_context("spawn").Pool(
            self.jobs,
            initializer=_init_render_worker,
            initargs=(flash,),
            maxtasksperchild=32,
        ) as pool:
            for document in pool.imap(_render_archive_document, jobs, chunksize=8):
                site.add_document(document)
                rendered = len(site.entries)
                if rendered % 10_000 == 0:
                    logger.info("Rendered %s documents", f"{rendered:,}")

    @staticmethod
    def _copy_assets(
        output: Path,
        library: VideoLibrary,
        flash: FlashLibrary,
        podcasts: PodcastLibrary,
    ) -> None:
        destination = output / "assets"
        destination.mkdir()
        names = (
            (*SITE_ASSETS, VIDEO_SCRIPT)
            if library.videos or podcasts.episodes
            else SITE_ASSETS
        )
        for name in names:
            copyfile(ASSETS / name, destination / name)
        if flash.items:
            copyfile(ASSETS / FLASH_SCRIPT, destination / FLASH_SCRIPT)
            flash.write_assets(
                destination, Path.cwd() / "node_modules/@ruffle-rs/ruffle"
            )

    @staticmethod
    def _add_redirects(site: Site, data: Path) -> None:
        source = data / "redirects.jsonl"
        if source.is_file():
            for record in read_json_lines(source):
                kind = record.get("kind") or "old-path"
                if kind != "old-repo-path":
                    site.redirect(record["path"], record["target"], kind)
        for document in site.entries.values():
            site.redirect(f"/id/{document.id}", document.path, "permanent-id")
        site.write_redirects(site.output / "redirects.jsonl")

    @staticmethod
    def _copy_url_map(output: Path, data: Path) -> None:
        maps = [data / name for name in URL_MAPS if (data / name).is_file()]
        if len(maps) > 1:
            raise ValueError("The archive data directory has multiple Wizards URL maps")
        for mapping in maps:
            copyfile(mapping, output / mapping.name)


def main() -> None:
    """Read command-line arguments and build the archive site."""
    current_dir = Path.cwd()

    parser = argparse.ArgumentParser(
        description="Build the Ormos archive as a static site."
    )
    parser.add_argument(
        "--source", type=Path, default=current_dir, help="Checkout containing content/"
    )
    parser.add_argument(
        "--data",
        type=Path,
        help="Archive data directory (defaults to data/ in the checkout)",
    )
    parser.add_argument("--output", type=Path, required=True, help="New site directory")
    parser.add_argument(
        "--jobs",
        type=int,
        default=min(8, max(1, (os.cpu_count() or 1) // 2)),
        help="Number of rendering processes",
    )
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )
    builder = ArchiveBuilder(
        args.source, args.data or args.source / "data", args.output, args.jobs
    )
    try:
        result = builder.build()
    except (OSError, ValueError) as error:
        parser.error(str(error))
    logger.info(
        "Built %s documents and %s redirects.",
        f"{result.documents:,}",
        f"{result.redirects:,}",
    )

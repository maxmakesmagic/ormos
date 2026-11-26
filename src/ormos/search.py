"""Build the archive's language-specific search indexes with Pagefind."""

from __future__ import annotations

import json
import logging
import os
import re
import shutil
import subprocess
from collections import defaultdict
from collections.abc import Iterable, Iterator
from concurrent.futures import ThreadPoolExecutor
from itertools import islice
from pathlib import Path
from typing import TYPE_CHECKING, TypedDict

from .paths import component, site_file, write_new

if TYPE_CHECKING:
    from .content import Document


logger = logging.getLogger(__name__)

PAGEFIND_VERSION = "1.6.0"
SEARCH_SHARD_BYTES = 512 * 1024 * 1024
SEARCH_SHARD_PAGES = 10_000
SEARCH_WORKERS = 2


class TitleRecord(TypedDict):
    """An article title and filters to index as a Pagefind custom record."""

    url: str
    content: str
    language: str
    meta: dict[str, str]
    filters: dict[str, list[str]]


class SearchIndex:
    """Index the canonical documents already rendered in a site directory."""

    def __init__(self, output: Path) -> None:
        """Use the site output directory for search input and output."""
        self.output = output

    def build(
        self, documents: Iterable[Document], plan_path: Path | None = None
    ) -> None:
        """Build full-text and article-title indexes for each language."""
        documents = tuple(documents)
        search = self.output / "pagefind"
        html_shards = (
            self._planned_shards(documents, plan_path)
            if plan_path is not None
            else self._partition(documents)
        )
        self._build_bundle(
            search,
            (
                (name, [path.relative_to(self.output).as_posix() for path in files])
                for name, files in html_shards
            ),
            copy_runtime=True,
        )
        self._build_bundle(search / "titles", self._title_shards(documents))

    def _build_bundle(
        self,
        directory: Path,
        shards: Iterable[tuple[str, list[str] | list[TitleRecord]]],
        *,
        copy_runtime: bool = False,
    ) -> None:
        directory.mkdir()
        manifest: dict[str, list[str]] = defaultdict(list)
        cpus = os.cpu_count() or 1
        workers = min(SEARCH_WORKERS, cpus)
        threads = min(8, max(1, cpus // workers))
        first: Path | None = None
        shards = iter(shards)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            while batch := list(islice(shards, workers)):
                indexes = [directory / name for name, _ in batch]
                if first is None:
                    first = indexes[0]
                results = []
                for index, (_, sources) in zip(indexes, batch, strict=True):
                    logger.info(
                        "Indexing %s (%s documents)",
                        index.relative_to(self.output / "pagefind").as_posix(),
                        f"{len(sources):,}",
                    )
                    results.append(
                        pool.submit(self._build_shard, index, sources, threads)
                    )
                for index, result in zip(indexes, results, strict=True):
                    for language in result.result():
                        path = index.relative_to(self.output).as_posix()
                        manifest[language].append(f"/{path}/")

        if copy_runtime and first is not None:
            for name in ("pagefind.js", "pagefind-worker.js"):
                shutil.copyfile(first / name, directory / name)
        write_new(
            directory / "shards.json", json.dumps(manifest, sort_keys=True) + "\n"
        )

    @staticmethod
    def _title_shards(
        documents: Iterable[Document],
    ) -> Iterator[tuple[str, list[TitleRecord]]]:
        articles: dict[str, list[Document]] = defaultdict(list)
        for document in documents:
            if document.kind == "article":
                articles[component(document.lang.lower())].append(document)
        for language, records in sorted(articles.items()):
            ordered = iter(sorted(records, key=lambda document: document.path))
            number = 1
            while batch := list(islice(ordered, SEARCH_SHARD_PAGES)):
                title_records: list[TitleRecord] = []
                for document in batch:
                    day = document.day
                    filters = {
                        "author": list(dict.fromkeys(p.slug for p in document.authors)),
                        "year": [str(day.year) if day else "undated"],
                    }
                    if document.column_slug:
                        filters["column"] = [document.column_slug]
                    title_records.append(
                        {
                            "url": document.path,
                            "content": document.title,
                            "language": language,
                            "meta": {"title": document.title},
                            "filters": filters,
                        }
                    )
                yield f"{language}-{number:03}", title_records
                number += 1

    def _partition(
        self, documents: Iterable[Document]
    ) -> Iterator[tuple[str, list[Path]]]:
        # Keep documents in the same language together to reduce browser requests.
        ordered = sorted(
            documents, key=lambda document: (document.lang.lower(), document.path)
        )
        number = 1
        sources: list[Path] = []
        total_bytes = 0
        for document in ordered:
            html = site_file(self.output, document.path)
            size = html.stat().st_size
            if sources and (
                total_bytes + size > SEARCH_SHARD_BYTES
                or len(sources) == SEARCH_SHARD_PAGES
            ):
                yield f"part-{number:03}", sources
                number += 1
                sources = []
                total_bytes = 0
            sources.append(html)
            total_bytes += size
        if sources:
            yield f"part-{number:03}", sources

    def _planned_shards(
        self, documents: Iterable[Document], path: Path
    ) -> Iterator[tuple[str, list[Path]]]:
        plan = json.loads(path.read_text(encoding="utf-8"))
        if (
            not isinstance(plan, dict)
            or plan.get("version") != 1
            or plan.get("pagefind_version") != PAGEFIND_VERSION
            or not isinstance(plan.get("shards"), list)
        ):
            raise ValueError(f"Unsupported search plan in {path}")

        expected = {document.path for document in documents}
        seen: set[str] = set()
        shards = []
        previous = 0
        for shard in plan["shards"]:
            if not isinstance(shard, dict) or not isinstance(shard.get("name"), str):
                # The CLI reports invalid plan data through ValueError.
                raise ValueError(f"Invalid search shard in {path}")  # noqa: TRY004
            name = shard["name"]
            match = re.fullmatch(r"part-([0-9]{3,})", name)
            if match is None:
                raise ValueError(f"Invalid search shard name {name!r} in {path}")
            number = int(match[1])
            if number <= previous or name != f"part-{number:03}":
                raise ValueError(f"Unordered search shard name {name!r} in {path}")
            members = shard.get("paths")
            if not isinstance(members, list) or not members:
                raise ValueError(f"Search shard {name} has no members")
            for member in members:
                if (
                    not isinstance(member, str)
                    or member not in expected
                    or member in seen
                ):
                    raise ValueError(
                        f"Unexpected or repeated search path {member!r} in {path}"
                    )
                seen.add(member)
            shards.append((name, members))
            previous = number

        if seen != expected:
            raise ValueError(
                f"Search plan is missing {len(expected - seen):,} canonical paths in {path}"
            )
        for name, members in shards:
            # Pagefind assigns page numbers in the order recorded in the plan.
            yield name, [site_file(self.output, member) for member in members]

    def _build_shard(
        self, index: Path, sources: list[str] | list[TitleRecord], threads: int
    ) -> list[str]:
        index.mkdir()
        environment = {**os.environ, "RAYON_NUM_THREADS": str(threads)}
        # Keep the selected executable and index settings tied to the lockfile.
        for override in (
            "PAGEFIND_BINARY_PATH",
            "PAGEFIND_EXTENDED_BINARY_PATH",
            "PAGEFIND_UNSTABLE_INDEX_CHUNK_SIZE",
            "npm_config_arch",
        ):
            environment.pop(override, None)
        driver = Path(__file__).with_name("pagefind.mjs")
        # Resolve the locked Node package from the checkout, even when the
        # Python package is installed into a virtual environment elsewhere.
        result = subprocess.run(
            [
                "node",
                "--input-type=module",
                "--eval",
                driver.read_text(encoding="utf-8"),
                "--",
                str(self.output),
                str(index),
            ],
            env=environment,
            input=json.dumps(sources),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            check=False,
        )
        level = logging.ERROR if result.returncode else logging.INFO
        for line in result.stdout.splitlines():
            if line.strip():
                logger.log(level, "%s: %s", index.name, line)
        if result.returncode:
            raise ValueError(
                f"Pagefind failed for {index.name} (exit {result.returncode})"
            )

        entry = json.loads((index / "pagefind-entry.json").read_text(encoding="utf-8"))
        if entry["version"] != PAGEFIND_VERSION:
            raise ValueError(
                f"Search shard {index.name} used Pagefind {entry['version']}"
            )
        languages = entry["languages"]
        indexed = sum(language["page_count"] for language in languages.values())
        if indexed != len(sources):
            raise ValueError(
                f"Search shard {index.name} indexed {indexed} of {len(sources)} documents"
            )
        return list(languages)

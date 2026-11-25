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
from typing import TYPE_CHECKING

from .paths import site_file, write_new

if TYPE_CHECKING:
    from .content import Document


logger = logging.getLogger(__name__)

PAGEFIND_VERSION = "1.6.0"
SEARCH_SHARD_BYTES = 512 * 1024 * 1024
SEARCH_SHARD_PAGES = 10_000
SEARCH_WORKERS = 2


class SearchIndex:
    """Index the canonical documents already rendered in a site directory."""

    def __init__(self, output: Path) -> None:
        """Use the site output directory for search input and output."""
        self.output = output

    def build(
        self, documents: Iterable[Document], plan_path: Path | None = None
    ) -> None:
        """Build index shards and record which shards cover each language."""
        search = self.output / "pagefind"
        search.mkdir()
        shards = (
            self._planned_shards(documents, plan_path)
            if plan_path is not None
            else self._partition(documents)
        )
        manifest: dict[str, list[str]] = defaultdict(list)
        cpus = os.cpu_count() or 1
        workers = min(SEARCH_WORKERS, cpus)
        threads = min(8, max(1, cpus // workers))
        first: Path | None = None
        with ThreadPoolExecutor(max_workers=workers) as pool:
            while batch := list(islice(shards, workers)):
                indexes = [search / name for name, _ in batch]
                if first is None:
                    first = indexes[0]
                results = []
                for index, (_, sources) in zip(indexes, batch, strict=True):
                    logger.info(
                        "Indexing %s (%s documents)", index.name, f"{len(sources):,}"
                    )
                    results.append(
                        pool.submit(self._build_shard, index, sources, threads)
                    )
                for index, result in zip(indexes, results, strict=True):
                    for language in result.result():
                        manifest[language].append(f"/pagefind/{index.name}/")

        if first is not None:
            for name in ("pagefind.js", "pagefind-worker.js"):
                shutil.copyfile(first / name, search / name)
        write_new(search / "shards.json", json.dumps(manifest, sort_keys=True) + "\n")

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

    def _build_shard(self, index: Path, sources: list[Path], threads: int) -> list[str]:
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
            input=json.dumps(
                [source.relative_to(self.output).as_posix() for source in sources]
            ),
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

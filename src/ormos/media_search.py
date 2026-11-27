"""Build search indexes for podcast and video transcripts."""

from __future__ import annotations

import json
import logging
import os
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Literal

from .paths import write_new
from .search import PAGEFIND_VERSION

if TYPE_CHECKING:
    from collections.abc import Sequence

    from .podcasts import PodcastLibrary
    from .videos import VideoLibrary, VideoTranscript

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class MediaSearchRecord:
    """A canonical media page and its verified transcript."""

    url: str
    title: str
    kind: Literal["podcast", "video"]
    language: str
    content: str

    @classmethod
    def from_transcript(
        cls,
        url: str,
        title: str,
        kind: Literal["podcast", "video"],
        transcript: VideoTranscript,
    ) -> MediaSearchRecord:
        """Use the primary language subtag from the transcript locale."""
        language = transcript.locale.partition("-")[0].lower()
        return cls(url, title, kind, language, transcript.text.strip())


class MediaSearchIndex:
    """Write independent Pagefind indexes for the available transcript languages."""

    def __init__(self, output: Path) -> None:
        """Use the rendered archive's output directory."""
        self.output = output

    @staticmethod
    def records(
        videos: VideoLibrary, podcasts: PodcastLibrary
    ) -> tuple[MediaSearchRecord, ...]:
        """Collect media with searchable transcript text in a deterministic order."""
        records = [
            MediaSearchRecord.from_transcript(
                video.path, video.title, "video", transcript
            )
            for video in videos.videos
            if (transcript := videos.transcripts.get(video.url))
            and transcript.text.strip()
        ]
        records.extend(
            MediaSearchRecord.from_transcript(
                episode.path, episode.title, "podcast", episode.transcript
            )
            for episode in podcasts.episodes
            if episode.transcript.text.strip()
        )
        return tuple(sorted(records, key=lambda record: (record.language, record.url)))

    def build(self, records: Sequence[MediaSearchRecord]) -> None:
        """Build one bundle per language and publish the Media search manifest."""
        directory = self.output / "pagefind" / "media"
        directory.mkdir(parents=True)
        groups: dict[str, list[MediaSearchRecord]] = defaultdict(list)
        for record in records:
            if not re.fullmatch(r"[a-z]{2,3}", record.language):
                raise ValueError(
                    f"Invalid transcript index language: {record.language}"
                )
            groups[record.language].append(record)

        manifest: dict[str, list[str]] = {}
        for language, group in sorted(groups.items()):
            index = directory / language
            logger.info(
                "Indexing %s media transcripts in %s", f"{len(group):,}", language
            )
            self._build_bundle(index, group)
            entry = json.loads((index / "pagefind-entry.json").read_bytes())
            if entry["version"] != PAGEFIND_VERSION:
                raise ValueError(f"Media search used Pagefind {entry['version']}")
            languages = entry["languages"]
            if tuple(languages) != (language,) or languages[language][
                "page_count"
            ] != len(group):
                raise ValueError(
                    f"Media search did not index all {len(group)} transcripts in {language}"
                )
            manifest[language] = [f"/pagefind/media/{language}/"]
        write_new(
            directory / "shards.json", json.dumps(manifest, sort_keys=True) + "\n"
        )

    @staticmethod
    def _build_bundle(index: Path, records: Sequence[MediaSearchRecord]) -> None:
        environment = {
            **os.environ,
            "RAYON_NUM_THREADS": str(min(8, os.cpu_count() or 1)),
        }
        for override in (
            "PAGEFIND_BINARY_PATH",
            "PAGEFIND_EXTENDED_BINARY_PATH",
            "PAGEFIND_UNSTABLE_INDEX_CHUNK_SIZE",
            "npm_config_arch",
        ):
            environment.pop(override, None)
        driver = Path(__file__).with_name("pagefind-media.mjs")
        result = subprocess.run(
            [
                "node",
                "--input-type=module",
                "--eval",
                driver.read_text(encoding="utf-8"),
                "--",
                str(index),
            ],
            env=environment,
            input=json.dumps(
                [
                    {
                        "url": record.url,
                        "content": f"{record.title}\n{record.content}",
                        "language": record.language,
                        "meta": {"title": record.title, "kind": record.kind},
                        "filters": {"media": [record.kind]},
                    }
                    for record in records
                ],
                ensure_ascii=False,
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
            raise ValueError(f"Pagefind failed for Media search in {index.name}")

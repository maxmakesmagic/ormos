"""Read the podcast catalog and render the episode pages."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from math import isfinite
from pathlib import Path
from typing import TYPE_CHECKING, Any

from .html import MEDIA_ORIGIN, PODCAST_ROUTE, render_page
from .paths import component
from .videos import VIDEO_SCRIPT, VideoTranscript, duration_label

if TYPE_CHECKING:
    from .site import Site

PODCAST_TRANSCRIPT_ROUTE = "/podcast-transcripts"
_AUDIO_URL = re.compile(
    rf"{re.escape(MEDIA_ORIGIN)}/([0-9a-f]{{2}})/([0-9a-f]{{2}})/"
    r"(\1\2[0-9a-f]{60})\.(mp3|m4a)\Z"
)


@dataclass(frozen=True, slots=True)
class Podcast:
    """Store the page information for one archived recording."""

    digest: str
    media_url: str
    playback_url: str
    title: str
    date: str
    duration_seconds: float
    notes: str
    article_ids: tuple[str, ...]
    transcript: VideoTranscript

    @classmethod
    def read(cls, data: Path, row: dict[str, Any]) -> Podcast:
        """Load the episode and its verified transcript files."""
        url = row["url"]
        match = _AUDIO_URL.fullmatch(url) if isinstance(url, str) else None
        if match is None or match[3] != row["id"]:
            raise ValueError(f"Invalid podcast media URL: {url!r}")
        playback_url = row.get("playback_url", url)
        if "playback_url" in row:
            playback = (
                _AUDIO_URL.fullmatch(playback_url)
                if isinstance(playback_url, str)
                else None
            )
            if playback is None or playback[4] != "m4a":
                raise ValueError(f"Invalid podcast playback URL: {playback_url!r}")
        title, notes, published = row["title"], row["description"], row["published"]
        if (
            not isinstance(title, str)
            or not title.strip()
            or not isinstance(notes, str)
        ):
            raise ValueError(f"Invalid podcast title or description: {url}")
        if not isinstance(published, str) or (
            published and date.fromisoformat(published).isoformat() != published
        ):
            raise ValueError(f"Invalid podcast publication date: {url}")
        duration = row["duration_seconds"]
        if (
            type(duration) not in (int, float)
            or not isfinite(duration)
            or duration <= 0
        ):
            raise ValueError(f"Invalid podcast duration: {url}")
        article_ids = row.get("article_ids", [])
        if not isinstance(article_ids, list):
            raise ValueError(f"Invalid podcast article IDs: {url}")  # noqa: TRY004
        stem = url.removeprefix(f"{MEDIA_ORIGIN}/").rsplit(".", 1)[0]
        transcript = VideoTranscript.from_record(
            data,
            {**row, "audio_duration_seconds": duration, "status": "transcribed"},
            url=url,
            media_stem=stem,
        )
        return cls(
            match[3],
            url,
            playback_url,
            title,
            published,
            duration,
            notes,
            tuple(map(component, article_ids)),
            transcript,
        )

    @property
    def path(self) -> str:
        """Use the audio checksum as the permanent episode route."""
        return f"{PODCAST_ROUTE}/{self.digest}"

    @property
    def duration_label(self) -> str:
        """Show the episode duration in hours, minutes, and seconds."""
        return duration_label(round(self.duration_seconds))

    @property
    def download_filename(self) -> str:
        """Suggest a readable filename with the original audio extension."""
        slug = re.sub(r"[^a-z0-9]+", "-", self.title.casefold()).strip("-")
        return f"{slug or self.digest}.{self.media_url.rsplit('.', 1)[1]}"


@dataclass(frozen=True, slots=True)
class PodcastLibrary:
    """Store the archive's podcast recordings."""

    episodes: tuple[Podcast, ...]

    @classmethod
    def read(cls, data: Path) -> PodcastLibrary:
        """Read the podcast catalog when the checkout includes it."""
        catalog = data / "podcasts.json"
        if not catalog.is_file():
            return cls(())
        record = json.loads(catalog.read_bytes())
        if not isinstance(record, dict) or record.get("version") != 1:
            raise ValueError(f"Unsupported podcast catalog in {catalog}")
        rows = record.get("podcasts")
        if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
            raise ValueError(f"Expected a list of podcast records in {catalog}")
        episodes = tuple(Podcast.read(data, row) for row in rows)
        if len({episode.digest for episode in episodes}) != len(episodes):
            raise ValueError(f"Repeated recordings in {catalog}")
        return cls(episodes)

    def write(self, site: Site) -> None:
        """Write the podcast index and each episode with its captions."""
        podcasts = sorted(
            self.episodes,
            key=lambda episode: (
                not episode.date,
                episode.date,
                episode.title.casefold(),
                episode.digest,
            ),
        )
        site.page(
            PODCAST_ROUTE,
            render_page(
                "podcasts.html",
                "Podcasts",
                PODCAST_ROUTE,
                script="/assets/column-sort.js",
                podcasts=podcasts,
            ),
        )
        for podcast in podcasts:
            transcript = podcast.transcript
            transcript.write_sidecars(
                site.output / PODCAST_TRANSCRIPT_ROUTE.lstrip("/")
            )
            site.page(
                podcast.path,
                render_page(
                    "podcast.html",
                    podcast.title,
                    podcast.path,
                    script=f"/assets/{VIDEO_SCRIPT}",
                    podcast=podcast,
                    download_url=f"{podcast.media_url}?download=1",
                    locale=transcript.locale,
                    captions_path=f"{PODCAST_TRANSCRIPT_ROUTE}/{transcript.captions_key}",
                    transcript=transcript.blocks(),
                    related=[
                        site.entries[identifier] for identifier in podcast.article_ids
                    ],
                ),
            )

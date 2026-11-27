"""Read the video catalog and render its archive pages and captions."""

from __future__ import annotations

import json
import re
from collections.abc import Iterator
from dataclasses import dataclass
from hashlib import sha256
from html import unescape
from math import isfinite
from pathlib import Path
from typing import TYPE_CHECKING, Any

from .html import MEDIA_ORIGIN, VIDEO_ROUTE, render_page
from .paths import component

if TYPE_CHECKING:
    from .content import Document
    from .site import Site


VIDEO_SCRIPT = "videos.js"
TRANSCRIPT_ROUTE = "/video-transcripts"
_VIDEO_URL = re.compile(
    rf"{re.escape(MEDIA_ORIGIN)}/([0-9a-f]{{2}})/([0-9a-f]{{2}})/\1\2[0-9a-f]{{60}}\.mp4\Z"
)
_CHECKSUM = re.compile(r"[0-9a-f]{64}\Z")
_LOCALE = re.compile(r"[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})+\Z")
_CUE_TIME = re.compile(r"([0-9]{2,}):([0-5][0-9]):([0-5][0-9])\.([0-9]{3})")
_CUE_VOICE = re.compile(r"<v ([^<>\r\n]{1,100})>(.*?)</v>\Z", re.DOTALL)


def duration_label(seconds: int) -> str:
    """Format a duration and include hours when needed."""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02}:{seconds:02}" if hours else f"{minutes}:{seconds:02}"


def _read_catalog(path: Path) -> list[dict[str, Any]]:
    content = json.loads(path.read_bytes())
    if not isinstance(content, dict) or content.get("version") != 1:
        raise ValueError(f"Unsupported video catalog in {path}")
    records = content.get("videos")
    if not isinstance(records, list) or not all(
        isinstance(record, dict) for record in records
    ):
        raise ValueError(f"Expected a list of video records in {path}")
    return records


@dataclass(frozen=True, slots=True)
class Video:
    """Store a video catalog entry and its related article IDs."""

    url: str
    title: str
    article_ids: tuple[str, ...]
    filenames: tuple[str, ...]
    duration_seconds: int | None
    alternate: bool
    event: str = ""
    segment: str = ""

    @property
    def segment_title(self) -> str:
        """Use the archived segment label when it is known."""
        return self.segment or self.title

    @property
    def display_title(self) -> str:
        """Include the event when the title appears outside the video list."""
        title = self.segment_title
        if self.event and self.event.casefold() != title.casefold():
            return f"{self.event} · {title}"
        return title

    @property
    def path(self) -> str:
        """Return the video page path based on the media checksum."""
        digest = self.url.rsplit("/", 1)[1].removesuffix(".mp4")
        return f"{VIDEO_ROUTE}/{digest}"

    @property
    def media_stem(self) -> str:
        """Return the media path without its origin or file extension."""
        return self.url.removeprefix(f"{MEDIA_ORIGIN}/").removesuffix(".mp4")

    @property
    def duration(self) -> str:
        """Return the display duration, or an empty string when it is unknown."""
        return (
            duration_label(self.duration_seconds)
            if self.duration_seconds is not None
            else ""
        )

    @classmethod
    def from_record(cls, row: dict[str, Any]) -> Video:
        """Read a video entry from a catalog record."""
        url, title = row["url"], row["title"]
        if not isinstance(url, str) or not _VIDEO_URL.fullmatch(url):
            raise ValueError(f"Invalid video URL: {url!r}")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Missing video title: {url}")
        duration = row["duration_seconds"]
        if duration is not None and (type(duration) is not int or duration < 0):
            raise ValueError(f"Invalid video duration: {url}")
        alternate = row["alternate"]
        if type(alternate) is not bool:
            raise ValueError(f"Invalid video encoding marker: {url}")
        article_ids, filenames = row["article_ids"], row["filenames"]
        event, segment = row.get("event", ""), row.get("segment", "")
        if not isinstance(event, str) or not isinstance(segment, str):
            # The build reports malformed catalog data as a ValueError.
            raise ValueError(f"Invalid video context: {url}")  # noqa: TRY004
        if not isinstance(article_ids, list):
            # A malformed JSON field is an archive data error.
            raise ValueError(f"Invalid video article IDs: {url}")  # noqa: TRY004
        if not isinstance(filenames, list) or not all(
            isinstance(name, str) for name in filenames
        ):
            raise ValueError(f"Invalid video filenames: {url}")
        return cls(
            url,
            title,
            tuple(map(component, article_ids)),
            tuple(filenames),
            duration,
            alternate,
            event.strip(),
            segment.strip(),
        )


@dataclass(frozen=True, slots=True)
class VideoTranscript:
    """Store transcript text, captions, and the paths for both files."""

    locale: str
    audio_duration_seconds: float
    text: str
    text_key: str | None = None
    captions_key: str | None = None
    captions: bytes = b""

    @classmethod
    def from_record(
        cls, data: Path, row: dict[str, Any], *, url: str, media_stem: str
    ) -> VideoTranscript:
        """Read a catalog entry and match each transcript file to its checksum."""
        locale = row["locale"]
        duration = row["audio_duration_seconds"]
        if (
            not isinstance(locale, str)
            or not _LOCALE.fullmatch(locale)
            or type(duration) not in (int, float)
            or not isfinite(duration)
            or duration <= 0
        ):
            raise ValueError(f"Invalid transcript metadata for {url}")

        text_hash, captions_hash = row["text_sha256"], row["vtt_sha256"]
        status = row["status"]
        if status == "no_speech" and text_hash is None and captions_hash is None:
            return cls(locale, duration, "")
        if status != "transcribed":
            raise ValueError(f"Invalid transcript status for {url}")

        def read_asset(digest: object, suffix: str) -> tuple[str, bytes]:
            if not isinstance(digest, str) or not _CHECKSUM.fullmatch(digest):
                raise ValueError(f"Invalid transcript checksum for {url}")
            key = f"{media_stem}.{locale}.{digest}.{suffix}"
            content = (data / "media-transcripts" / key).read_bytes()
            if sha256(content).hexdigest() != digest:
                raise ValueError(f"Transcript file differs from its checksum: {key}")
            return key, content

        text_key, text_bytes = read_asset(text_hash, "txt")
        captions_key, captions = read_asset(captions_hash, "vtt")
        text = text_bytes.decode("utf-8")
        if not text.strip() or not captions.startswith(b"WEBVTT\n"):
            raise ValueError(f"Missing transcript text or WebVTT header for {url}")
        return cls(locale, duration, text, text_key, captions_key, captions)

    def write_sidecars(self, output: Path) -> None:
        """Write the transcript text and captions as separate files."""
        if self.text_key is None or self.captions_key is None:
            return
        for key, content in (
            (self.text_key, self.text.encode("utf-8")),
            (self.captions_key, self.captions),
        ):
            target = output / key
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(content)

    def _blocks(self) -> Iterator[tuple[int, str | None, str]]:
        body = self.captions.decode("utf-8").removeprefix("WEBVTT\n\n").rstrip("\n")
        start: int | None = None
        speaker: str | None = None
        words: list[str] = []
        for cue in body.split("\n\n"):
            timing, _, text = cue.partition("\n")
            timestamp = _CUE_TIME.fullmatch(timing.partition(" --> ")[0])
            if timestamp is None or not text.strip():
                raise ValueError("Invalid transcript cue")
            hours, minutes, seconds, milliseconds = map(int, timestamp.groups())
            cue_start = ((hours * 60 + minutes) * 60 + seconds) * 1000 + milliseconds
            voice = _CUE_VOICE.fullmatch(text)
            cue_speaker, cue_words = (
                (unescape(voice[1]), voice[2]) if voice else (None, text)
            )
            if start is not None and (
                cue_speaker != speaker or cue_start - start >= 30_000
            ):
                yield start, speaker, " ".join(words)
                start = None
                words.clear()
            if start is None:
                start, speaker = cue_start, cue_speaker
            words.append(unescape(cue_words))
        if start is not None:
            yield start, speaker, " ".join(words)

    def blocks(self) -> Iterator[tuple[str, str, str | None, str]]:
        """Yield each transcript block with a seek offset and display time."""
        for milliseconds, speaker, words in self._blocks():
            position = f"{milliseconds // 1000}.{milliseconds % 1000:03}"
            yield position, duration_label(milliseconds // 1000), speaker, words


@dataclass(frozen=True, slots=True)
class VideoLibrary:
    """Store the archive's videos and transcripts."""

    videos: tuple[Video, ...]
    transcripts: dict[str, VideoTranscript]

    @classmethod
    def read(cls, data: Path) -> VideoLibrary:
        """Load the video catalog and its companion transcript catalog."""
        catalog = data / "videos.json"
        videos = (
            tuple(Video.from_record(row) for row in _read_catalog(catalog))
            if catalog.is_file()
            else ()
        )
        urls = {video.url for video in videos}
        if len(urls) != len(videos):
            raise ValueError(f"Repeated media URLs in {catalog}")

        captions = data / "video-transcripts.json"
        if not captions.is_file():
            return cls(videos, {})
        rows = _read_catalog(captions)
        by_url = {row["url"]: row for row in rows}
        if len(by_url) != len(rows) or by_url.keys() != urls:
            raise ValueError("Transcript catalog must match the video catalog")
        return cls(
            videos,
            {
                video.url: VideoTranscript.from_record(
                    data, by_url[video.url], url=video.url, media_stem=video.media_stem
                )
                for video in videos
            },
        )

    def write(self, site: Site) -> None:
        """Write the video index and a page for each video."""
        if not self.videos:
            return
        rows = []
        for video in sorted(
            self.videos,
            key=lambda video: (
                not video.event,
                video.event.casefold(),
                video.segment_title.casefold(),
                video.url,
            ),
        ):
            entries = sorted(
                (site.entries[identifier] for identifier in video.article_ids),
                key=lambda entry: (entry.title.casefold(), entry.path),
            )
            terms = " ".join(
                (
                    video.event,
                    video.title,
                    *video.filenames,
                    *(f"{entry.title} {entry.published}" for entry in entries),
                )
            ).strip()
            rows.append((video, terms))
            self._write_page(site, video, entries)

        site.page(
            VIDEO_ROUTE,
            render_page(
                "videos.html",
                "Videos",
                VIDEO_ROUTE,
                script=f"/assets/{VIDEO_SCRIPT}",
                rows=rows,
            ),
        )

    def _write_page(self, site: Site, video: Video, coverage: list[Document]) -> None:
        transcript = self.transcripts.get(video.url)
        captions_path = ""
        captions_language = ""
        audio_end = ""
        if transcript is not None:
            if (
                video.duration_seconds is not None
                and video.duration_seconds - transcript.audio_duration_seconds > 5
            ):
                audio_end = duration_label(round(transcript.audio_duration_seconds))
            if transcript.captions_key and transcript.text_key:
                captions_path = f"{TRANSCRIPT_ROUTE}/{transcript.captions_key}"
                captions_language = {"en": "English", "nl": "Nederlands"}.get(
                    transcript.locale.split("-")[0], transcript.locale
                )
                transcript.write_sidecars(site.output / TRANSCRIPT_ROUTE.lstrip("/"))

        site.page(
            video.path,
            render_page(
                "video.html",
                video.display_title,
                video.path,
                script=f"/assets/{VIDEO_SCRIPT}" if captions_path else "",
                video=video,
                coverage=coverage,
                audio_end=audio_end,
                captions_path=captions_path,
                captions_language=captions_language,
                locale=transcript.locale if transcript else "",
                blocks=transcript.blocks() if transcript and captions_path else (),
            ),
        )

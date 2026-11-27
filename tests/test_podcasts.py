"""Check that podcast playback repairs preserve the archive's originals."""

from hashlib import sha256
from pathlib import Path

import pytest

from ormos.paths import site_file
from ormos.podcasts import Podcast, PodcastLibrary
from ormos.site import Site

_DIGEST = "abcd" + "1" * 60
_STEM = f"ab/cd/{_DIGEST}"
_ORIGINAL_URL = f"https://media.ormos.uk/{_STEM}.mp3"
_DERIVED_URL = f"https://media.ormos.uk/12/34/1234{'2' * 60}.m4a"
_TITLE = "Grand Prix Example"


@pytest.fixture
def podcast_record(tmp_path: Path) -> dict[str, object]:
    """Write transcript assets addressed by the original audio digest."""
    row = {
        "id": _DIGEST,
        "url": _ORIGINAL_URL,
        "title": _TITLE,
        "published": "2008-06-01",
        "duration_seconds": 42.0,
        "description": "",
        "locale": "en-US",
    }
    for field, suffix, body in (
        ("text_sha256", "txt", b"The final round."),
        (
            "vtt_sha256",
            "vtt",
            b"WEBVTT\n\n00:00:01.000 --> 00:00:02.000\nThe final round.\n",
        ),
    ):
        digest = sha256(body).hexdigest()
        path = tmp_path / "media-transcripts" / f"{_STEM}.en-US.{digest}.{suffix}"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
        row[field] = digest
    return row


@pytest.mark.parametrize("corrected", [False, True])
def test_podcast_playback_routes(
    tmp_path: Path, podcast_record: dict[str, object], *, corrected: bool
) -> None:
    """Play the selected audio in both views and retain original media links."""
    if corrected:
        podcast_record["playback_url"] = _DERIVED_URL
    expected = _DERIVED_URL if corrected else _ORIGINAL_URL
    podcast = Podcast.read(tmp_path, podcast_record)
    output = tmp_path / "site"
    PodcastLibrary((podcast,)).write(Site(output))

    listing = site_file(output, "/podcasts").read_text(encoding="utf-8")
    episode_path = f"/podcasts/{_DIGEST}"
    assert f'<a href="{episode_path}">{_TITLE}</a>' in listing
    assert f'<a href="{expected}" aria-label="Listen to {_TITLE}">Listen</a>' in listing
    assert "<audio" not in listing

    page = site_file(output, episode_path).read_text(encoding="utf-8")
    assert f'<audio class="podcast-player" src="{expected}"' in page
    assert (
        f'href="{_ORIGINAL_URL}?download=1" download="grand-prix-example.mp3"' in page
    )
    captions = f"podcast-transcripts/{_STEM}.en-US.{podcast_record['vtt_sha256']}.vtt"
    assert f'href="/{captions}"' in page
    assert (output / captions).is_file()


@pytest.mark.parametrize(
    "playback_url",
    [
        None,
        _ORIGINAL_URL,
        _DERIVED_URL.replace("media.ormos.uk", "other.example"),
        _DERIVED_URL.replace("/12/", "/ff/"),
        f"{_DERIVED_URL}?download=1",
    ],
)
def test_invalid_podcast_playback_url(
    tmp_path: Path, podcast_record: dict[str, object], playback_url: object
) -> None:
    """Require corrected streams to use a hashed M4A on the media origin."""
    podcast_record["playback_url"] = playback_url
    with pytest.raises(ValueError, match="Invalid podcast playback URL"):
        Podcast.read(tmp_path, podcast_record)

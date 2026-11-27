"""Check that missing historic downloads reach the archive fallback."""

from __future__ import annotations

import json
import re
from html import unescape
from typing import TYPE_CHECKING
from urllib.parse import parse_qs, urlsplit

import pytest

from ormos.build import ArchiveBuilder
from ormos.media_links import MediaLinks
from ormos.paths import site_file, write_new

if TYPE_CHECKING:
    from pathlib import Path

_MISSING = "http://webcast2.wizards.com/podcasts/11philadelphia/ptphi_1.mp3?a=1&b=2"
_RECOVERED = "http://www.wizards.com/sideboard/match.zip"
_TARGET = f"https://media.ormos.uk/ab/cd/abcd{'1' * 60}.mp4"
_ARTICLE = "/en/articles/podcast/2011/09-02-podcasting-from-magic-weekend-philadelphia"
_WAYBACK = "https://web.archive.org/web/20040223000000id_/"


def test_archive_build_routes_known_missing_links(tmp_path: Path) -> None:
    """Mark curated missing links and prefer recovered copies in the normal build."""
    data = tmp_path / "data"
    replay = _WAYBACK + _MISSING.replace("?", "%20?") + "#t=6"
    registry = data / "missing-media.jsonl"
    write_new(
        registry,
        "".join(json.dumps({"url": url}) + "\n" for url in (_MISSING, _RECOVERED)),
    )
    write_new(
        data / "media-urls.jsonl",
        json.dumps(
            {
                "kind": "media",
                "original_url": _RECOVERED.replace("http://www.", "https://"),
                "target_url": _TARGET,
            }
        )
        + "\n",
    )
    write_new(
        tmp_path / "source" / "content" / "philadelphia.md",
        f"---\nid: philadelphia\npath: {_ARTICLE}\nkind: article\ntitle: Philadelphia podcast\n---\n"
        f"\n[**Modern Metagame Madness**]({_MISSING}#t=12)\n\n"
        f'<a title="Archived &quot;match&quot;" href="{_RECOVERED}#t=4">Recovered clip</a>\n\n'
        f"[Missing replay]({replay})\n\n"
        f"[Recovered replay]({_WAYBACK}{_RECOVERED}%20#t=8)\n\n"
        f"[Unreviewed link]({_MISSING.replace('a=1', 'a=3')})\n\n"
        f"[Unreviewed replay]({_WAYBACK}{_MISSING.replace('a=1', 'a=3')})\n\n"
        f"![Original image]({_MISSING})\n",
    )
    output = tmp_path / "site"
    ArchiveBuilder(tmp_path / "source", data, output, 1).build()

    article = site_file(output, _ARTICLE).read_text()
    assert article.count('class="missing-media-warning"') == 2
    assert "<strong>Modern Metagame Madness</strong>" in article
    assert '<span class="visually-hidden"> (Media not found)</span></a>' in article
    fallbacks = re.findall(r'href="(/media-not-found\?[^"]*)"', article)
    assert [parse_qs(urlsplit(unescape(url)).query) for url in fallbacks] == [
        {"url": [f"{_MISSING}#t=12"]},
        {"url": [replay]},
    ]
    assert f'href="{_TARGET}#t=4">Recovered clip</a>' in article
    assert f'href="{_TARGET}#t=8">Recovered replay</a>' in article
    assert 'title="Archived &quot;match&quot;"' in article
    assert 'ptphi_1.mp3?a=3&amp;b=2">Unreviewed link</a>' in article
    assert 'ptphi_1.mp3?a=3&amp;b=2">Unreviewed replay</a>' in article
    assert 'ptphi_1.mp3?a=1&amp;b=2" alt="Original image"' in article
    page = site_file(output, "/media-not-found").read_text()
    assert "<h1>Media not found</h1>" in page
    assert "Fblthp took a wrong turn." in page
    assert 'src="/assets/media-not-found.js"' in page
    assert (output / "assets" / "media-not-found.js").is_file()


def test_podcast_source_lookup_precedes_missing_warning(tmp_path: Path) -> None:
    """Use the original recovered MP3 when the podcast catalog supplies the alias."""
    audio = _TARGET.removesuffix(".mp4") + ".mp3"
    write_new(tmp_path / "missing-media.jsonl", json.dumps({"url": _MISSING}) + "\n")
    write_new(
        tmp_path / "podcasts.json",
        json.dumps(
            {
                "podcasts": [
                    {
                        "url": audio,
                        "original_urls": [_MISSING.replace("http:", "https:")],
                    }
                ]
            }
        ),
    )
    assert MediaLinks.read(tmp_path).destination(_MISSING) == (audio, False)


def test_registry_rejects_urls_outside_wizards(tmp_path: Path) -> None:
    """Only recorded Wizards media addresses qualify for a missing-media warning."""
    write_new(
        tmp_path / "missing-media.jsonl",
        json.dumps({"url": _MISSING.replace(".wizards.com", ".wizards.com.invalid")})
        + "\n",
    )
    with pytest.raises(ValueError, match="Invalid missing media address"):
        MediaLinks.read(tmp_path)

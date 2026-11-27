"""Check that media transcript search builds separately from article search."""

import json
import re
from hashlib import sha256
from pathlib import Path

from ormos.build import ArchiveBuilder
from ormos.content import ArticleSource
from ormos.media_search import MediaSearchIndex
from ormos.paths import site_file, write_new
from ormos.podcasts import PodcastLibrary
from ormos.search import PAGEFIND_VERSION, SearchIndex
from ormos.videos import VideoLibrary

VIDEO = "a" * 64
PODCAST = "b" * 64
SILENT = "c" * 64
VIDEO_TEXT = "この決勝戦では青いデッキが優勝しました。"
PODCAST_TEXT = "The designer explains the original Mirrodin artifact lands."


def _transcript_files(
    data: Path, digest: str, locale: str, text: str
) -> dict[str, str]:
    directory = data / "media-transcripts" / digest[:2] / digest[2:4]
    directory.mkdir(parents=True)
    checksums = {}
    for field, extension, content in (
        ("text_sha256", "txt", text),
        ("vtt_sha256", "vtt", f"WEBVTT\n\n00:00:01.000 --> 00:00:02.000\n{text}\n"),
    ):
        body = content.encode()
        checksum = sha256(body).hexdigest()
        (directory / f"{digest}.{locale}.{checksum}.{extension}").write_bytes(body)
        checksums[field] = checksum
    return checksums


def _media_fixtures(data: Path) -> None:
    video_url = f"https://media.ormos.uk/aa/aa/{VIDEO}.mp4"
    silent_url = f"https://media.ormos.uk/cc/cc/{SILENT}.mp4"
    videos = [
        {
            "url": url,
            "title": title,
            "article_ids": [],
            "filenames": [],
            "duration_seconds": 4,
            "alternate": False,
        }
        for url, title in ((video_url, "大会決勝"), (silent_url, "Silent footage"))
    ]
    videos[0].update(event="Pro Tour Kobe (2004)", segment="Finals")
    transcripts = [
        {
            "url": video_url,
            "locale": "ja-JP",
            "audio_duration_seconds": 4,
            "status": "transcribed",
            **_transcript_files(data, VIDEO, "ja-JP", VIDEO_TEXT),
        },
        {
            "url": silent_url,
            "locale": "fr-FR",
            "audio_duration_seconds": 4,
            "status": "no_speech",
            "text_sha256": None,
            "vtt_sha256": None,
        },
    ]
    podcasts = [
        {
            "id": PODCAST,
            "url": f"https://media.ormos.uk/bb/bb/{PODCAST}.mp3",
            "title": "Drive to Work",
            "published": "2014-05-05",
            "duration_seconds": 4,
            "description": "Design stories from the archive.",
            "locale": "en-US",
            **_transcript_files(data, PODCAST, "en-US", PODCAST_TEXT),
        }
    ]
    for name, key, records in (
        ("videos.json", "videos", videos),
        ("video-transcripts.json", "videos", transcripts),
        ("podcasts.json", "podcasts", podcasts),
    ):
        (data / name).write_text(
            json.dumps({"version": 1, key: records}), encoding="utf-8"
        )


def _article_index(site: Path) -> dict[Path, str]:
    bundle = site / "pagefind"
    return {
        path.relative_to(bundle): sha256(path.read_bytes()).hexdigest()
        for path in bundle.rglob("*")
        if path.is_file() and path.relative_to(bundle).parts[0] != "media"
    }


def _select(page: str, selector: str) -> re.Match[str]:
    match = re.search(
        rf'<select\b([^>]*\bid="{selector}"[^>]*)>(.*?)</select>', page, re.DOTALL
    )
    assert match is not None
    return match


def test_media_search_keeps_the_planned_article_index(tmp_path: Path) -> None:
    """Index verified media text in its own language bundles during a site build."""
    data = tmp_path / "data"
    _media_fixtures(data)
    source = tmp_path / "source"
    articles = []
    baseline = tmp_path / "baseline"
    for lang, slug, title in (
        ("en", "lotus", "Black Lotus"),
        ("en", "mox", "Mox Sapphire"),
        ("ja", "tournament", "大会の結果"),
    ):
        metadata = {
            "id": slug,
            "kind": "article",
            "lang": lang,
            "path": f"/{lang}/articles/{slug}",
            "title": title,
        }
        markdown = source / "content" / f"{slug}.md"
        write_new(
            markdown, f"---\n{json.dumps(metadata)}\n---\nThe archive records {slug}.\n"
        )
        article = ArticleSource.read(markdown)
        write_new(site_file(baseline, article.document.path), article.render())
        articles.append(article.document)
    plan = data / "search-plan.json"
    plan.write_text(
        json.dumps(
            {
                "version": 1,
                "pagefind_version": PAGEFIND_VERSION,
                "shards": [
                    {
                        "name": "part-001",
                        "paths": [doc.path for doc in reversed(articles)],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    planned = plan.read_bytes()
    SearchIndex(baseline).build(articles, plan)
    site = tmp_path / "site"
    index = MediaSearchIndex(site)
    records = index.records(VideoLibrary.read(data), PodcastLibrary.read(data))
    assert {
        (row.url, row.title, row.kind, row.language, row.content) for row in records
    } == {
        (
            f"/videos/{VIDEO}",
            "Pro Tour Kobe (2004) · Finals",
            "video",
            "ja",
            VIDEO_TEXT,
        ),
        (f"/podcasts/{PODCAST}", "Drive to Work", "podcast", "en", PODCAST_TEXT),
    }

    ArchiveBuilder(source, data, site, 1).build()

    assert plan.read_bytes() == planned
    assert _article_index(site) == _article_index(baseline)
    manifest = json.loads((site / "pagefind/media/shards.json").read_bytes())
    assert manifest == {"en": ["/pagefind/media/en/"], "ja": ["/pagefind/media/ja/"]}
    for language, (directory,) in manifest.items():
        entry = json.loads(
            (site / directory.lstrip("/") / "pagefind-entry.json").read_bytes()
        )
        assert {
            code: details["page_count"] for code, details in entry["languages"].items()
        } == {language: 1}
    assert not site_file(site, "/media/search").exists()
    media = site_file(site, "/media").read_text(encoding="utf-8")
    assert 'href="/search"' in media
    assert 'href="/media/search"' not in media

    for route, locale in (("/search", "en"), ("/search/ja", "ja")):
        panel = site_file(site, route).read_text(encoding="utf-8")
        assert '<form id="search"' in panel
        assert 'id="query"' in panel
        assert 'href="/media/search"' not in panel
        assert "/assets/search.js" in panel
        scope = _select(panel, "search-scope")
        assert 'name="scope"' in scope[1]
        assert re.findall(r'<option\b[^>]*\bvalue="([^"]*)"', scope[2]) == [
            "text",
            "article",
            "titles",
            "podcast",
            "video",
        ]
        assert all(
            "selected" not in option
            for option in re.findall(r"<option\b[^>]*>", scope[2])[1:]
        )

        languages = _select(panel, "search-language")
        destinations = {}
        selected = []
        for option in re.findall(r"<option\b([^>]*)>", languages[2]):
            attributes = dict(re.findall(r'([\w-]+)="([^"]*)"', option))
            value = attributes["value"]
            destinations[value] = attributes["data-path"]
            if re.search(r"\bselected\b", option):
                selected.append(value)
        assert destinations == {"en": "/search", "ja": "/search/ja"}
        assert selected == [locale]

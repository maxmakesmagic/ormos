"""Check the video index and transcript templates."""

from pathlib import Path

from ormos.content import Document
from ormos.paths import site_file
from ormos.site import Site
from ormos.videos import Video, VideoLibrary, VideoTranscript


def test_video_templates_keep_search_and_transcript_links(tmp_path: Path) -> None:
    """Render the video index, caption track, transcript, and sidecar links."""
    site = Site(tmp_path)
    site.add_document(
        Document.read(
            {
                "id": "coverage",
                "kind": "article",
                "title": "Coverage & notes",
                "path": "/en/articles/coverage",
            }
        )
    )
    video = Video(
        url=f"https://media.ormos.uk/00/00/{'0' * 64}.mp4",
        title='Video "test"',
        article_ids=("coverage",),
        filenames=("archive.mp4",),
        duration_seconds=75,
        alternate=True,
    )
    captions = (
        b"WEBVTT\n\n00:00:01.500 --> 00:00:04.000\n<v Alice>Cards &amp; notes</v>\n"
    )
    transcript = VideoTranscript(
        locale="en-US",
        audio_duration_seconds=60,
        text="Cards & notes\n",
        text_key="test.txt",
        captions_key="test.vtt",
        captions=captions,
    )
    VideoLibrary((video,), {video.url: transcript}).write(site)

    index = site_file(tmp_path, "/videos").read_text(encoding="utf-8")
    assert 'data-video-search="archive.mp4 Coverage &amp; notes "' in index
    assert 'data-video-page="">Video &quot;test&quot;</a>' in index
    assert '<time datetime="PT75S">1:15</time>' in index
    assert "Alternate encoding" in index

    page = site_file(tmp_path, video.path).read_text(encoding="utf-8")
    assert '<script type="module" src="/assets/videos.js"></script>' in page
    assert 'src="/video-transcripts/test.vtt" srclang="en-US" label="English"' in page
    assert '<a href="/video-transcripts/test.vtt" download="">' in page
    assert '<a href="#t=1.500" data-video-seek="" aria-label="Seek to 0:01">' in page
    assert "<p>Cards &amp; notes</p>" in page
    assert "The archived audio ends at 1:00 of this 1:15 video." in page
    assert 'href="/en/articles/coverage" data-video-article=""' in page
    assert (tmp_path / "video-transcripts/test.vtt").read_bytes() == captions

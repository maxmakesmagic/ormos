"""Check the shared HTML layout and its article template."""

from pathlib import Path
from textwrap import dedent

from ormos.content import ArticleSource, Document
from ormos.html import PUBLIC_ARCHIVE_ORIGIN, render_page


def test_page_template_renders_shared_metadata() -> None:
    """Render the canonical link, page title, and common layout."""
    page = render_page("page.html", "Example", "/example")

    assert '<link rel="canonical" href="/example">' in page
    assert "<title>Example · Ormos</title>" in page
    assert '<main id="main" tabindex="-1"></main>' in page
    assert '<meta property="og:' not in page


def test_article_template_renders_metadata_and_clean_body(tmp_path: Path) -> None:
    """Use article metadata for previews and keep the body markup and search hooks."""
    source = tmp_path / "article.md"
    source.write_text(
        dedent("""\
        ---
        id: example
        kind: article
        lang: fr
        path: /fr/articles/feature/2024/example
        title: 'Teferi "quoted" & <cards>'
        published: '2024-07-17'
        column_slug: feature
        column: Feature
        description: 'A "preview" & <summary>'
        image: https://media.ormos.uk/example.jpg?x=1&y=2
        authors:
          - slug: example-author
            name: Alice & Bob
        archive_source:
          wayback_url: https://example.org/capture?x=1&y=2
        ---
        Some **article text**.

        <script>discard this block</script>

        <img src="https://media.ormos.uk/example.jpg" alt="Card" data-unused="remove">
        """),
        encoding="utf-8",
    )
    page = ArticleSource.read(source).render()
    head = page.split("</head>", 1)[0]
    url = PUBLIC_ARCHIVE_ORIGIN + "/fr/articles/feature/2024/example"

    assert '<html lang="fr">' in page
    assert '<link rel="canonical" href="/fr/articles/feature/2024/example">' in head
    assert '<meta property="og:type" content="article">' in head
    assert '<meta property="og:site_name" content="Ormos">' in head
    assert f'<meta property="og:url" content="{url}">' in head
    assert (
        'property="og:title" content="Teferi &quot;quoted&quot; &amp; &lt;cards&gt;"'
        in head
    )
    assert (
        'property="og:description" content="A &quot;preview&quot; &amp; &lt;summary&gt;"'
        in head
    )
    assert (
        'property="og:image" content="https://media.ormos.uk/example.jpg?x=1&amp;y=2"'
        in head
    )
    assert 'property="article:published_time" content="2024-07-17"' in head
    assert 'property="article:section" content="Feature"' in head
    assert "<article data-pagefind-body>" in page
    assert '<h1 data-pagefind-meta="title">Teferi' in page
    assert (
        'data-pagefind-meta="author"><a href="/fr/authors/example-author">Alice &amp; Bob</a>'
        in page
    )
    assert (
        '<a href="/fr/articles/feature" data-pagefind-meta="column">Feature</a>' in page
    )
    assert '<time datetime="2024-07-17">17 July 2024</time>' in page
    assert (
        '<div class="article-body"><p>Some <strong>article text</strong>.</p>' in page
    )
    assert "<script>" not in page
    assert '<img loading="lazy" decoding="async"' in page
    assert "data-unused" not in page
    assert '<footer class="article-footer" data-pagefind-ignore>' in page
    assert '<a href="/id/example">Permanent link</a>' in page
    assert (
        '<a href="https://example.org/capture?x=1&amp;y=2" rel="nofollow">Archived capture</a>'
        in page
    )


def test_article_template_handles_missing_preview_metadata() -> None:
    """Use the known author when no description exists and omit unknown fields."""
    document = Document.read(
        {
            "id": "results",
            "kind": "event",
            "path": "/en/events/2024/challenge/results",
            "title": "Results",
            "published": "1970-01-01",
            "authors": [{"slug": "alice", "name": "Alice"}],
        }
    )
    page = ArticleSource(
        document, "", event_code="modern_challenge", image_url="/relative.jpg"
    ).render()

    assert '<meta property="og:description" content="By Alice">' in page
    assert 'property="og:image"' not in page
    assert 'property="article:published_time"' not in page
    assert 'property="article:section"' not in page
    assert (
        '<a href="/en/events/2024/challenge" data-pagefind-meta="event">modern challenge</a>'
        in page
    )

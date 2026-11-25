"""Smoke test for the shared HTML layout."""

from ormos.html import layout


def test_layout_renders_page_content() -> None:
    """Render the page content and its canonical link."""
    page = layout("Example", "/example", "<p>Example content.</p>")

    assert '<link rel="canonical" href="/example">' in page
    assert '<main id="main" tabindex="-1"><p>Example content.</p></main>' in page

"""Check the generated archive navigation."""

import re
from dataclasses import replace
from pathlib import Path

import pytest

from ormos.content import ArticleSource, Document, Person
from ormos.paths import site_file, write_new
from ormos.site import Site
from ormos.videos import VideoLibrary


def _document(slug: str, published: str, kind: str = "article") -> Document:
    directory = "articles" if kind == "article" else "events"
    return Document.read(
        {
            "id": slug,
            "kind": kind,
            "path": f"/en/{directory}/{slug}",
            "published": published,
        }
    )


def _write_navigation(output: Path, documents: list[Document]) -> Site:
    site = Site(output)
    for document in documents:
        write_new(
            site_file(output, document.path), ArticleSource(document, "").render()
        )
        site.add_document(document)
    site.navigation(VideoLibrary((), {}))
    return site


def _pagination(page: str) -> str:
    start = page.index('<nav class="pagination"')
    return page[start : page.index("</nav>", start)]


def test_articles_landing_page(tmp_path: Path) -> None:
    """Use the landing page to direct readers to article directories."""
    articles = [_document(f"article-{day}", f"2024-01-{day:02}") for day in range(1, 9)]
    other_records = [
        _document("undated", ""),
        _document("later-event", "2024-02-01", "event"),
        _document("later-decklist", "2024-02-02", "decklist"),
    ]
    _write_navigation(tmp_path, articles + other_records)
    landing = site_file(tmp_path, "/articles").read_text(encoding="utf-8")

    assert "<h1>Articles</h1>" in landing
    assert "Browse 9 archived articles." in landing
    start = landing.index('aria-label="Browse articles"')
    browse = landing[start : landing.index("</nav>", start)]
    assert 'href="/search?scope=titles"' in browse
    assert site_file(tmp_path, "/search").exists()
    for path in ("/columns", "/authors", "/years", "/articles/all"):
        assert f'href="{path}"' in browse
        assert site_file(tmp_path, path).exists()

    for entry in articles + other_records:
        assert f'href="{entry.path}"' not in landing
    assert "<script" not in landing


def test_search_filters_use_local_article_metadata(tmp_path: Path) -> None:
    """Offer distinct article filters for each language and retain undated articles."""
    dated = replace(
        _document("article", "2024-05-15"),
        authors=(Person("markrosewater", "Mark Rosewater"),),
        column_slug="makingmagic",
        column="Making Magic",
    )
    undated = replace(
        _document("undated", "1970-01-01"),
        authors=dated.authors,
    )
    french = replace(
        _document("french", "2023-05-15"),
        lang="fr",
        path="/fr/articles/french",
        authors=(Person("author-fr", "Auteur français"),),
    )
    event = replace(
        _document("event", "2025-05-15", kind="event"),
        authors=(Person("event-author", "Event Reporter"),),
    )
    _write_navigation(tmp_path, [dated, undated, french, event])

    english = site_file(tmp_path, "/search").read_text(encoding="utf-8")
    translated = site_file(tmp_path, "/search/fr").read_text(encoding="utf-8")
    assert '<option value="titles">Article titles</option>' in english
    assert '<input type="search" id="query" name="q">' in english
    assert '<fieldset id="search-filters" hidden>' in english
    assert english.count('<option value="markrosewater">Mark Rosewater</option>') == 1
    assert '<option value="makingmagic">Making Magic</option>' in english
    assert '<option value="2024">2024</option>' in english
    assert '<option value="undated">Undated</option>' in english
    assert 'value="1970"' not in english
    assert 'value="2025"' not in english
    assert 'value="event-author"' not in english
    assert 'value="author-fr"' not in english
    assert '<option value="author-fr">Auteur français</option>' in translated
    assert 'value="markrosewater"' not in translated
    assert 'value="2023"' in translated


def test_all_articles_preserves_pagination(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """List every article and link directly between the listing pages."""
    monkeypatch.setattr("ormos.site.PAGE_SIZE", 2)
    articles = [_document(f"article-{day}", f"2024-01-{day:02}") for day in range(1, 6)]
    site = _write_navigation(tmp_path, articles)
    paths = ("/articles/all", "/articles/all/page/2", "/articles/all/page/3")
    rows = (articles[3:], articles[1:3], articles[:1])
    for index, (path, records) in enumerate(zip(paths, rows, strict=True), 1):
        page = site_file(tmp_path, path).read_text(encoding="utf-8")
        assert f'<link rel="canonical" href="{path}">' in page
        pagination = _pagination(page)
        assert page.index("</ol>") < page.index(pagination)
        active = '<span aria-current="page"><span class="visually-hidden">Page </span>'
        assert f"{active}{index}</span>" in pagination
        for number, target in enumerate(paths, 1):
            if number != index:
                assert (
                    f'<a href="{target}" aria-label="Page {number}">{number}</a>'
                    in pagination
                )
        assert f'<a href="{path}" aria-label="Page {index}">' not in pagination
        if index > 1:
            assert f'href="{paths[index - 2]}" rel="prev"' in pagination
        else:
            assert 'rel="prev"' not in pagination
        if index < len(paths):
            assert f'href="{paths[index]}" rel="next"' in pagination
        else:
            assert 'rel="next"' not in pagination
        for entry in articles:
            assert (f'href="{entry.path}"' in page) == (entry in records)
        if index > 1:
            old_path = f"/articles/page/{index}"
            assert old_path not in site.redirects
            assert not site_file(tmp_path, old_path).exists()

    assert "/articles/all/page/1" not in site.redirects
    assert not site_file(tmp_path, "/articles/all/page/1").exists()


def test_numbered_pagination_collapses_only_long_gaps(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Keep the endpoints and nearby pages visible with compact long gaps."""
    monkeypatch.setattr("ormos.site.PAGE_SIZE", 1)
    articles = [
        _document(f"article-{day}", f"2024-01-{day:02}") for day in range(1, 13)
    ]
    cases = {
        7: {1: "1 2 3 4 5 6 7"},
        12: {
            1: "1 2 3 … 12",
            5: "1 2 3 4 5 6 7 … 12",
            6: "1 … 4 5 6 7 8 … 12",
            12: "1 … 10 11 12",
        },
    }
    for total, expected in cases.items():
        output = tmp_path / str(total)
        _write_navigation(output, articles[:total])
        for index, labels in expected.items():
            path = "/articles/all" if index == 1 else f"/articles/all/page/{index}"
            page = _pagination(site_file(output, path).read_text(encoding="utf-8"))
            assert re.findall(r">\s*(\d+|…)\s*</(?:a|span|li)>", page) == labels.split()
            assert page.count('<li aria-hidden="true">…</li>') == labels.count("…")


def test_articles_landing_page_without_dated_articles(tmp_path: Path) -> None:
    """Count an undated article on the landing page and list it in the archive."""
    undated = _document("undated", "1970-01-01")
    _write_navigation(tmp_path, [undated])
    landing = site_file(tmp_path, "/articles").read_text(encoding="utf-8")
    archive = site_file(tmp_path, "/articles/all").read_text(encoding="utf-8")

    assert "Browse 1 archived article." in landing
    assert f'href="{undated.path}"' in archive


def test_author_tables_show_all_articles_in_date_order(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """List all articles in date order on global and localized author pages."""
    monkeypatch.setattr("ormos.site.PAGE_SIZE", 4)
    articles = [
        replace(
            _document(slug, day),
            lang=language,
            path=f"/{language}/articles/feature/2024/{slug}",
            authors=(Person("alice", "Alice"),),
            column_slug="feature",
            column="Feature",
        )
        for slug, day, language in (
            ("undated", "", "fr"),
            ("same-b", "2024-06-01", "fr"),
            ("late", "2024-07-17", "fr"),
            ("english", "2023-12-15", "en"),
            ("early", "2024-01-01", "fr"),
            ("sentinel", "1969-12-31", "fr"),
            ("same-a", "2024-06-01", "fr"),
        )
    ]
    _write_navigation(tmp_path, articles)
    paths = {article.id: article.path for article in articles}

    french_rows = ("early", "same-a", "same-b", "late", "sentinel", "undated")
    for author, rows in (
        ("/authors/alice", ("english", *french_rows)),
        ("/fr/authors/alice", french_rows),
    ):
        page = site_file(tmp_path, author).read_text(encoding="utf-8")
        assert not site_file(tmp_path, f"{author}/page/2").exists()
        assert 'class="pagination"' not in page
        assert "data-sort-scope" not in page
        assert page.count(">Undated</td>") == 2
        assert 'datetime="1969-12-31"' not in page
        assert '<script type="module" src="/assets/column-sort.js"></script>' in page
        assert 'aria-sort="ascending"' in page
        assert re.findall(r'data-sort-key="([a-z]+)"', page) == [
            "date",
            "title",
            "column",
        ]
        table = page.split("<tbody>", 1)[1].split("</tbody>", 1)[0]
        assert re.findall(r'href="([^"]+)"', table) == [
            link for row in rows for link in (paths[row], "/columns/feature")
        ]


def test_column_tables_show_all_articles_in_date_order(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """List all articles in date order on global and localized column pages."""
    monkeypatch.setattr("ormos.site.PAGE_SIZE", 2)
    articles = {
        slug: replace(
            _document(slug, day),
            lang=language,
            path=f"/{language}/articles/feature/{day[:4] or 'undated'}/{slug}",
            column_slug="feature",
            column="Feature",
            authors=(Person("alice", "Alice"),),
        )
        for slug, day, language in (
            ("late", "2024-07-17", "fr"),
            ("undated", "", "fr"),
            ("english", "2023-03-01", "en"),
            ("early", "2004-12-17", "fr"),
        )
    }
    _write_navigation(tmp_path, list(articles.values()))

    assert not site_file(tmp_path, "/columns/feature/year/2024").exists()
    assert not site_file(tmp_path, "/fr/articles/feature/2024").exists()
    assert not site_file(tmp_path, "/fr/articles/feature/undated").exists()
    assert site_file(tmp_path, "/years/2024").exists()

    for column, rows in (
        ("/columns/feature", ("early", "english", "late", "undated")),
        ("/fr/articles/feature", ("early", "late", "undated")),
    ):
        page = site_file(tmp_path, column).read_text(encoding="utf-8")
        assert not site_file(tmp_path, f"{column}/page/2").exists()
        assert 'class="pagination"' not in page
        assert 'aria-label="Years"' not in page
        assert "data-sort-scope" not in page
        assert '<script type="module" src="/assets/column-sort.js"></script>' in page
        assert '<th scope="col" aria-sort="ascending">' in page
        assert re.findall(r'data-sort-key="([a-z]+)"', page) == [
            "date",
            "title",
            "author",
        ]
        table = page.split("<tbody>", 1)[1].split("</tbody>", 1)[0]
        assert re.findall(r'href="([^"]+)"', table) == [
            link
            for row in rows
            for link in (articles[row].path, f"/{articles[row].lang}/authors/alice")
        ]
        assert 'data-sort-value="2004-12-17"' in table
        assert table.count(">Undated</td>") == 1

"""Check the Pagefind bundle produced for the archive."""

import json
from gzip import decompress
from hashlib import sha256
from pathlib import Path

import pytest

from ormos.content import ArticleSource, Document
from ormos.paths import site_file, write_new
from ormos.search import PAGEFIND_VERSION, SearchIndex

ARTICLES = (
    ("en", "mox", "Mox Sapphire", "The sapphire artifact adds blue mana."),
    ("en", "lotus", "Black Lotus", "Play the lotus before the sapphire."),
    ("ja", "tournament", "大会の結果", "トーナメントの結果を発表しました。"),
    ("ja", "report", "試合のレポート", "決勝戦のデッキを紹介します。"),
)


@pytest.fixture
def search_plan(tmp_path: Path) -> Path:
    """Keep the release's shard membership and member order fixed."""
    plan = tmp_path / "search-plan.json"
    plan.write_text(
        json.dumps(
            {
                "version": 1,
                "pagefind_version": PAGEFIND_VERSION,
                "shards": [
                    {
                        "name": f"part-{number:03}",
                        "paths": [
                            f"/{lang}/articles/{slug}" for lang, slug, *_ in rows
                        ],
                    }
                    for number, rows in enumerate((ARTICLES[:2], ARTICLES[2:]), 1)
                ],
            }
        ),
        encoding="utf-8",
    )
    return plan


def _build(
    site: Path,
    plan: Path | None,
    *,
    reverse: bool = False,
    changed_body: str | None = None,
) -> Path:
    documents = []
    for lang, slug, title, body in reversed(ARTICLES) if reverse else ARTICLES:
        document = Document.read(
            {
                "id": slug,
                "kind": "article",
                "lang": lang,
                "path": f"/{lang}/articles/{slug}",
                "title": title,
            }
        )
        if slug == "mox" and changed_body is not None:
            body = changed_body
        article = ArticleSource(document, body)
        write_new(site_file(site, document.path), article.render())
        documents.append(document)
    SearchIndex(site).build(documents, plan)
    return site / "pagefind"


def _bundle_files(bundle: Path) -> dict[Path, str]:
    return {
        path.relative_to(bundle): sha256(path.read_bytes()).hexdigest()
        for path in bundle.rglob("*")
        if path.is_file()
    }


@pytest.mark.parametrize("use_plan", [True, False], ids=["planned", "unplanned"])
def test_search_bundle_is_reproducible(
    tmp_path: Path,
    search_plan: Path,
    use_plan: bool,
) -> None:
    """Write identical search files when article enumeration changes."""
    plan = search_plan if use_plan else None
    before = _build(tmp_path / "before", plan)
    after = _build(tmp_path / "after", plan, reverse=True)

    manifest = json.loads((before / "shards.json").read_text(encoding="utf-8"))
    assert set(manifest) == {"en", "ja"}
    assert list(before.rglob("*.pf_index"))
    assert _bundle_files(before) == _bundle_files(after)


def test_changed_article_only_changes_its_shard(
    tmp_path: Path, search_plan: Path
) -> None:
    """Keep other search shards identical after an article edit."""
    before = _bundle_files(_build(tmp_path / "before", search_plan))
    after = _bundle_files(
        _build(
            tmp_path / "after", search_plan, changed_body="An artifact taps for mana."
        )
    )

    changed = {
        path
        for path in before.keys() | after.keys()
        if before.get(path) != after.get(path)
    }
    assert {path.parts[0] for path in changed} == {"part-001"}


def test_search_uses_the_planned_page_order(tmp_path: Path, search_plan: Path) -> None:
    """Changing only the planned page order changes the shard's page numbers."""
    before = _build(tmp_path / "before", search_plan)
    plan = json.loads(search_plan.read_text(encoding="utf-8"))
    plan["shards"][0]["paths"].reverse()
    search_plan.write_text(json.dumps(plan), encoding="utf-8")
    after = _build(tmp_path / "after", search_plan)

    entry = "part-001/pagefind-entry.json"
    assert (before / entry).read_bytes() != (after / entry).read_bytes()
    assert _bundle_files(before / "titles") == _bundle_files(after / "titles")


def test_title_index_has_only_article_titles_and_filter_values(tmp_path: Path) -> None:
    """Keep body text and searchable author names out of the title index."""
    article = Document.read(
        {
            "id": "lotus",
            "kind": "article",
            "path": "/en/articles/lotus",
            "title": "Black Lotus",
            "published": "2004-02-03",
            "authors": [
                {"slug": "alice", "name": "Alice Example"},
                {"slug": "bob", "name": "Bob Example"},
            ],
            "column_slug": "feature",
            "column": "Feature",
        }
    )
    undated = Document.read(
        {
            "id": "mox",
            "kind": "article",
            "path": "/en/articles/mox",
            "title": "Mox Sapphire",
            "published": "1969-12-31",
        }
    )
    event = Document.read(
        {
            "id": "finals",
            "kind": "event",
            "path": "/en/events/finals",
            "title": "Finals",
        }
    )
    for document in (article, undated, event):
        source = ArticleSource(document, "Only articles can win the tournament.")
        write_new(site_file(tmp_path, document.path), source.render())

    SearchIndex(tmp_path).build(document for document in (article, undated, event))
    bundle = tmp_path / "pagefind" / "titles"
    assert json.loads((bundle / "shards.json").read_text(encoding="utf-8")) == {
        "en": ["/pagefind/titles/en-001/"]
    }
    fragments = {}
    for path in bundle.rglob("*.pf_fragment"):
        payload = decompress(path.read_bytes())
        assert payload.startswith(b"pagefind_dcd")
        fragment = json.loads(payload.removeprefix(b"pagefind_dcd"))
        fragments[fragment["url"]] = fragment
    assert set(fragments) == {article.path, undated.path}
    indexed = fragments[article.path]
    assert indexed["content"] == article.title
    assert indexed["meta"] == {"title": article.title}
    assert indexed["filters"] == {
        "author": ["alice", "bob"],
        "column": ["feature"],
        "year": ["2004"],
    }
    assert fragments[undated.path]["filters"]["year"] == ["undated"]

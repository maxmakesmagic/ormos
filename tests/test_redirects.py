"""Check which redirects the archive build publishes."""

import json
from pathlib import Path

from ormos.build import ArchiveBuilder
from ormos.content import Document
from ormos.paths import read_json_lines, site_file, write_new
from ormos.site import Site


def test_old_markdown_redirects_are_omitted(tmp_path: Path) -> None:
    """Keep public redirects and permanent links when using older data."""
    site = Site(tmp_path / "site")
    document = Document.read(
        {"id": "example", "kind": "article", "path": "/en/articles/example"}
    )
    write_new(site_file(site.output, document.path), "<article>Example</article>")
    site.add_document(document)

    markdown_alias = "/archive/en/Deck Lists/example"
    public_redirect = {
        "path": "/en/articles/previous-example",
        "target": document.path,
        "kind": "path-history",
    }
    permanent_redirect = {
        "path": f"/id/{document.id}",
        "target": document.path,
        "kind": "permanent-id",
    }
    data = tmp_path / "data"
    write_new(
        data / "redirects.jsonl",
        json.dumps(
            {"path": markdown_alias, "target": document.path, "kind": "old-repo-path"}
        )
        + "\n"
        + json.dumps(public_redirect)
        + "\n",
    )

    ArchiveBuilder._add_redirects(site, data)

    assert list(read_json_lines(site.output / "redirects.jsonl")) == [
        public_redirect,
        permanent_redirect,
    ]
    assert not (site.output / markdown_alias.lstrip("/") / "index.html").exists()
    for redirect in (public_redirect, permanent_redirect):
        html = site_file(site.output, redirect["path"]).read_text(encoding="utf-8")
        assert f'<meta http-equiv="refresh" content="0; url={document.path}">' in html
        assert f'<link rel="canonical" href="{document.path}">' in html

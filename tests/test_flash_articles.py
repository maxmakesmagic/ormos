"""Verify archived Flash placement and article backlinks."""

from html import unescape
from pathlib import Path

from ormos.content import render_document
from ormos.flash import RUFFLE_RUNTIME_FILES, FlashItem, FlashLibrary
from ormos.html import render_template
from ormos.paths import site_file
from ormos.site import Site


def test_jigsaw_offers_puzzle_image_without_wallpaper(tmp_path: Path) -> None:
    """Fetch the movie and image from their public archive URLs."""
    image_digest = "b" * 64
    puzzle = FlashItem.read(
        {
            "sha256": "a" * 64,
            "title": "Archive puzzle",
            "original_urls": [
                "http://wizards.com/mtg_puzzle.swf?stgImage=images/mtg_puzzle1.jpg"
            ],
            "image_sha256": image_digest,
        }
    )
    site = Site(tmp_path / "site")
    assets = site.output / "assets"
    assets.mkdir(parents=True)
    runtime = tmp_path / "runtime"
    runtime.mkdir()
    for filename in RUFFLE_RUNTIME_FILES:
        (runtime / filename).touch()
    library = FlashLibrary((puzzle,))
    library.write_assets(assets, runtime)
    library.write_pages(site)
    page = site_file(site.output, puzzle.path).read_text(encoding="utf-8")
    index = site_file(site.output, "/flash").read_text(encoding="utf-8")
    image = f"https://i.ormos.uk/bb/bb/{image_digest}.jpg?cors=1"
    movie = f"https://media.ormos.uk/aa/aa/{puzzle.digest}.swf?cors=1"
    flash_connect = "connect-src 'self' https://media.ormos.uk https://i.ormos.uk"

    assert not any(assets.rglob("*.swf"))
    assert not any(assets.rglob("*.jpg"))
    assert f'data-flash-player="{movie}"' in page
    assert f'data-flash-image="{image}"' in page
    assert '"stgImage": "images/mtg_puzzle1.jpg"' in unescape(page)
    assert f'<a href="{movie}">Open SWF file</a>' in page
    assert f'<a href="{image}">Open puzzle image</a>' in page
    assert "Open wallpaper" not in page
    assert flash_connect in page
    assert flash_connect not in index


def test_embedded_movie_uses_poster_as_player_control() -> None:
    """Use the archived artwork to open the embedded player."""
    poster = "https://i.ormos.uk/eye.jpg"
    movie = FlashItem.read(
        {
            "sha256": "a" * 64,
            "title": "The Secrets of the Eye",
            "original_urls": ["http://wizards.com/eye.swf"],
            "poster_url": poster,
        }
    )
    embed = render_template("flash-player.html", item=movie, embedded=True)
    standalone = render_template("flash-player.html", item=movie, embedded=False)

    assert "<details data-flash-preview" in embed
    assert f'src="{poster}"' in embed
    assert "data-flash-preview" not in standalone


def test_flash_marker_embeds_in_place_and_links_back(tmp_path: Path) -> None:
    """Embed the eye animation once between the surrounding paragraphs."""
    eye = FlashItem.read(
        {
            "sha256": "b9039d6a10b41cd7ba52e99f076dac6e969213562da6896d36fa64b176fbf7c2",
            "title": "stf84 eye",
            "original_urls": ["http://wizards.com/mtg/images/daily/stf/stf84_eye.swf"],
        }
    )
    source = tmp_path / "fort-keff.md"
    source.write_text(
        f"""---
id: gz3z68ec
kind: article
path: /en/articles/savortheflavor/2010/03-31-the-battle-of-fort-keff
title: The Battle of Fort Keff
---
A world that lured planeswalkers, then killed them in any number of gruesome ways.

![Eye of Ugin animation]({eye.path})

Chandra wasn't a woman who would appreciate his protectiveness.
""",
        encoding="utf-8",
    )
    library = FlashLibrary((eye,))
    site = Site(tmp_path / "site")
    document = render_document((source, site.output), flash=library.references())
    site.add_document(document)
    library.write_pages(site)

    article = site_file(site.output, document.path).read_text(encoding="utf-8")
    player = f'data-flash-player="{eye.movie_url}"'
    assert document.id == "gz3z68ec"
    assert document.flash_ids == (eye.id,)
    assert article.count(player) == 1
    assert article.count("/assets/ruffle/ruffle.js") == 1
    assert "connect-src 'self' https://media.ormos.uk" in article
    assert "connect-src 'self' https://media.ormos.uk https://i.ormos.uk" not in article
    assert (
        article.index("killed them in any number of gruesome ways.")
        < article.index(player)
        < article.index("Chandra wasn't a woman who would appreciate")
    )
    assert f'href="{eye.path}"' in article
    assert 'aria-label="Eye of Ugin animation Flash player"' in article
    assert f'src="{eye.path}"' not in article

    detail = site_file(site.output, eye.path).read_text(encoding="utf-8")
    assert f'<a href="{document.path}">The Battle of Fort Keff</a>' in detail


def test_flash_uses_source_links_and_catalog_associations(tmp_path: Path) -> None:
    """Use durable references and leave extraction warnings as metadata."""
    recovered = FlashItem.read(
        {
            "sha256": "a" * 64,
            "title": "Recovered movie",
            "original_urls": ["http://wizards.com/mtg/images/recovered.swf"],
        }
    )
    linked = FlashItem.read(
        {
            "sha256": "b" * 64,
            "title": "Linked movie",
            "original_urls": ["http://wizards.com/linked.swf?style=1&size=2"],
        }
    )
    unrelated = FlashItem.read(
        {
            "sha256": "c" * 64,
            "title": "Unrelated movie",
            "original_urls": ["http://wizards.com/other.swf"],
        }
    )
    related = FlashItem.read(
        {
            "sha256": "d" * 64,
            "title": "Related movie",
            "original_urls": ["http://wizards.com/related.swf"],
            "article_ids": ["example"],
        }
    )
    flash = FlashLibrary((recovered, linked, unrelated, related)).references()
    source = tmp_path / "article.md"
    source.write_text(
        """---
id: example
kind: article
title: Article with Flash
path: /en/articles/example
archive_source:
  url: https://magic.wizards.com/en/articles/example
render_recovery:
- code: unsupported_embedded_media
  target: /mtg/images/recovered.swf
- code: unsupported_embedded_media
  target: https://example.org/other.swf
---
The **original body** is still here.

[Watch the movie](https://www.wizards.com/linked.swf?size=2&style=1)

[Unrelated location](https://example.org/other.swf)

[Open a catalog entry](/flash/cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc)

![Regular image](/assets/example.png)

![Unknown animation](/flash/eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee)
""",
        encoding="utf-8",
    )
    output = tmp_path / "output"
    document = render_document((source, output), flash=flash)
    article = site_file(output, document.path).read_text(encoding="utf-8")

    assert document.flash_ids == (linked.id, related.id)
    assert article.count("data-flash-embedded") == 2
    assert "The <strong>original body</strong> is still here." in article
    assert "Watch the movie</a>" in article
    assert "Unrelated location</a>" in article
    assert f'href="{unrelated.path}">Open a catalog entry</a>' in article
    assert 'src="/assets/example.png" alt="Regular image"' in article
    assert "<p>Unknown animation</p>" in article
    assert "Archived Flash" not in article
    assert article.index(f'data-flash-player="{linked.movie_url}"') > article.index(
        "Unrelated location</a>"
    )
    assert recovered.movie_url not in article
    assert unrelated.movie_url not in article

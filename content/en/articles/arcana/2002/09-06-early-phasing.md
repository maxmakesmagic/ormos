---
id: c81dv9hs
kind: article
lang: en
path: /en/articles/arcana/2002/09-06-early-phasing
title: Early phasing
published: '2002-09-06'
column_slug: arcana
column: Arcana
authors:
- slug: magic-arcana
  name: Magic Arcana
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/arcana/178
    lang_detected: en
    capture_id: 1862767
    url: http://www.wizards.com/default.asp?x=mtgcom/arcana/178
    captured_at: '2008-05-03 18:56:36+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/arcana/178
    lang_detected: en
    capture_id: 1862767
    url: http://www.wizards.com/default.asp?x=mtgcom/arcana/178
    captured_at: '2008-05-03 18:56:36+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/arcana/178
    lang_detected: en
    capture_id: 1862767
    url: http://www.wizards.com/default.asp?x=mtgcom/arcana/178
    captured_at: '2008-05-03 18:56:36+00'
    rule: classic.byline
  column:
    page_key: wizards.com/default.asp?x=mtgcom/arcana/178
    lang_detected: en
    capture_id: 1862767
    url: http://www.wizards.com/default.asp?x=mtgcom/arcana/178
    captured_at: '2008-05-03 18:56:36+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: c81dv9hs
  url: http://www.wizards.com/default.asp?x=mtgcom/arcana/178
  page_key: wizards.com/default.asp?x=mtgcom/arcana/178
  lang: en
  template: classic_asp
  captured_at: '2008-05-03 18:56:36+00'
  capture_id: 1862767
  wayback_url: https://web.archive.org/web/20080503185636id_/http://www.wizards.com/default.asp?x=mtgcom/arcana/178
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: c81dv9hs
  capture_id: 1862767
  url: http://www.wizards.com/default.asp?x=mtgcom/arcana/178
  wayback_url: https://web.archive.org/web/20080503185636id_/http://www.wizards.com/default.asp?x=mtgcom/arcana/178
  captured_at: '2008-05-03 18:56:36+00'
  template: classic_asp
  sha256: cd8f4f1596d1421baf3254f55f37738563791471e59bb592de2f60ec9010404f
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Tawnos[s_Coffin')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Tawnos's Coffin
  occurrences: 2
---
* * *

I never realized phasing was so popular in the early days of **Magic**.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Tawnos's Coffin" src="https://i.ormos.uk/9d/25/9d25ebe7410e8ab64b7781fca8ebad9f416868d6f93bfa4b00144def7ab6c49d.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Just like [Oubliette](/en/articles/arcana/2002/08-09-old-cards-new-words-2) before it, *Antiquities'* Tawnos's Coffin was created as a way to remove a creature from the game temporarily. The creature could let out of the coffin at which point it would return to play in tact, complete with counters, enchantments, and so on.

Modern rules state that a creature that is removed from the game has no memory of ever being in play… so how does the Coffin handle such interactions under *Sixth Edition* rules? With phasing.

The Oracle wording reads:

> You may choose not to untap Tawnos's Coffin during your untap step.  
> ![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif), ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Target creature phases out. It can't phase in as long as Tawnos's Coffin remains tapped. When Tawnos's Coffin leaves play or becomes untapped, the creature phases in tapped.

Phasing moves a creature to another zone (called the "phase zone") which behaves differently than the "removed-from-play" zone. Phased creatures remember all their characteristics and come back into play as if they never left.
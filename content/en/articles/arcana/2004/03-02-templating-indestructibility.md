---
id: 14pp88s5
kind: article
lang: en
path: /en/articles/arcana/2004/03-02-templating-indestructibility
title: Templating indestructibility
published: '2004-03-02'
column_slug: arcana
column: Arcana
authors:
- slug: magic-arcana
  name: Magic Arcana
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/arcana/514
    lang_detected: en
    capture_id: 1890744
    url: http://www.wizards.com/default.asp?x=mtgcom/arcana/514
    captured_at: '2008-05-03 19:49:34+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/arcana/514
    lang_detected: en
    capture_id: 1890744
    url: http://www.wizards.com/default.asp?x=mtgcom/arcana/514
    captured_at: '2008-05-03 19:49:34+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/arcana/514
    lang_detected: en
    capture_id: 1890744
    url: http://www.wizards.com/default.asp?x=mtgcom/arcana/514
    captured_at: '2008-05-03 19:49:34+00'
    rule: classic.byline
  column:
    page_key: wizards.com/default.asp?x=mtgcom/arcana/514
    lang_detected: en
    capture_id: 1890744
    url: http://www.wizards.com/default.asp?x=mtgcom/arcana/514
    captured_at: '2008-05-03 19:49:34+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: 14pp88s5
  url: http://www.wizards.com/default.asp?x=mtgcom/arcana/514
  page_key: wizards.com/default.asp?x=mtgcom/arcana/514
  lang: en
  template: classic_asp
  captured_at: '2008-05-03 19:49:34+00'
  capture_id: 1890744
  wayback_url: https://web.archive.org/web/20080503194934id_/http://www.wizards.com/default.asp?x=mtgcom/arcana/514
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 14pp88s5
  capture_id: 1890744
  url: http://www.wizards.com/default.asp?x=mtgcom/arcana/514
  wayback_url: https://web.archive.org/web/20080503194934id_/http://www.wizards.com/default.asp?x=mtgcom/arcana/514
  captured_at: '2008-05-03 19:49:34+00'
  template: classic_asp
  sha256: e187b1184a81579cbaebebe36d239c74db29bd64f772037dcc03979a0457f7b9
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Severed_Legion')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - fear
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Darksteel_Colossus')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - trample
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Birds_of_Paradise')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - flying
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Darksteel_Pendant')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Darksteel Pendant
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Slobad,_Goblin_Tinkerer')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Slobad, Goblin Tinkerer
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Neurok_Spy')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - unblockable
  occurrences: 1
---
* * *

Templating, in the context of **Magic** R&D, is the process of bringing the wording of a **Magic** card's rules text into alignment with the text of similar cards, or coming up with sensible wording for new rules text. 

![The indestructibility mechanic](https://i.ormos.uk/04/9c/049ce53b6611fe662c0970dd40183a865e480ab3258e5e47f78b84ec0a70d0e4.jpg)

The indestructibility mechanic took some serious templating. 

At first, indestructible was a keyword mechanic, meaning that it would be like fear or trample or flying. So a card like Darksteel Pendant would have been templated initially this way (shown here with a first pass at some reminder text):

> Darksteel Pendant  
> ![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)  
>  Indestructible *(This card can't be destroyed but can be sacrificed or removed from the game.)*  
> ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif), ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Look at the top card of your library. You may put that card on the bottom of your library.

![Indestructo](https://i.ormos.uk/5f/b0/5fb0bd53f3ede6168481fc97787683df4f74ca2c8d6f57a75d86dbd63517b3e2.jpg)The templating team worked on the reminder text, and came up with this (as seen on the playtest card at left):

> Indestructible *(If this card would be put into the graveyard from play, instead leave this card in play. This ability does not work if this card is sacrificed.)*

(Note #1: This playtest card, a 2/2 indestructible artifact creature called "Indestructo," never became a card in a real **Magic** set. Note #2: indestructibility was once going to be included in "Bacon," a.k.a. *Mirrodin*, but was pushed off into *Darksteel*.)

As Randy Buehler's [January 9 article](/en/articles/latestdevelopments/2004/01-09-developing-indestructibility) mentions, using "indestructible" as a keyword caused some weird phrasing. Cards would "gain indestructible until end of turn" (via Slobad, Goblin Tinkerer's ability, for example), which just didn't sound natural.

So "indestructible" is now templated the way "unblockable" is, as a regular English adjective that has specific rules implications.
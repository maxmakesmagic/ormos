---
id: 0a207hfe
kind: article
lang: en
path: /en/articles/feature/2017/04-04-amonkhet-split-card-rules-changes
title: Amonkhet Split Card Rules Changes
published: '2017-04-04'
column_slug: feature
column: Feature
authors:
- slug: eli-shiffrin-3d3539fb
  name: Eli Shiffrin
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
    lang_detected: en
    capture_id: 125848
    url: https://magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
    captured_at: '2024-05-31 13:38:53+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
    lang_detected: en
    capture_id: 125848
    url: https://magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
    captured_at: '2024-05-31 13:38:53+00'
    rule: jsonld.date_published
  column:
    page_key: magic.wizards.com/en/articles/archive/news/amonkhet-split-card-rules-changes-2017-04-04
    lang_detected: en
    capture_id: 1083249
    url: https://magic.wizards.com/en/articles/archive/news/amonkhet-split-card-rules-changes-2017-04-04
    captured_at: '2022-09-03 14:29:44+00'
    rule: url.article_section
    registry_match: registry.explicit
  authors:
    page_key: magic.wizards.com/en/articles/archive/news/amonkhet-split-card-rules-changes-2017-04-04
    lang_detected: en
    capture_id: 1083249
    url: https://magic.wizards.com/en/articles/archive/news/amonkhet-split-card-rules-changes-2017-04-04
    captured_at: '2022-09-03 14:29:44+00'
    rule: drupal.div_author
sources:
- document_id: 0a207hfe
  url: https://magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
  page_key: magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
  lang: en
  template: contentful
  captured_at: '2024-05-31 13:38:53+00'
  capture_id: 125848
  wayback_url: https://web.archive.org/web/20240531133853id_/https://magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
- document_id: 0a207hfe
  url: https://magic.wizards.com/en/articles/archive/news/amonkhet-split-card-rules-changes-2017-04-04
  page_key: magic.wizards.com/en/articles/archive/news/amonkhet-split-card-rules-changes-2017-04-04
  lang: en
  template: drupal
  captured_at: '2022-09-03 14:29:44+00'
  capture_id: 1083249
  wayback_url: https://web.archive.org/web/20220903142944id_/https://magic.wizards.com/en/articles/archive/news/amonkhet-split-card-rules-changes-2017-04-04
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 0a207hfe
  capture_id: 125848
  url: https://magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
  wayback_url: https://web.archive.org/web/20240531133853id_/https://magic.wizards.com/en/news/announcements/amonkhet-split-card-rules-changes-2017-04-04
  captured_at: '2024-05-31 13:38:53+00'
  template: contentful
  sha256: cd984080d00924f2a36f1e879c9c3723cf525bc80ef9c020de37ac2b6fc97db2
render_recovery: []
---
Starting with the release of *Amonkhet*, we're streamlining split cards a bit. This applies to all split cards, not just the aftermath cards.

Previously, we played a delicate dance when asking about the converted mana cost of split cards.

![Destined to Lead](http://media.wizards.com/2017/dw466ytu5_akh/en_ruO9016cNL.png)

*   Sometimes Destined to Lead's converted mana cost was most like two: [Goblin Dark-Dwellers](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Dark-Dwellers) could target it.
*   Sometimes it was more like four: [Transgress the Mind](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Transgress+the+Mind) could exile it.
*   Sometimes it was more like six: [Dark Confidant](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Confidant) made you lose 6 life if you revealed it.
*   Sometimes it was . . . multiples of the above. [Counterbalance](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterbalance) could reveal Destined to Lead and counter both [Negate](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Negate) and [Mindbreak Trap](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindbreak+Trap).

This rewarded players who dug into the rules and figured that out, but it baffled a lot of players, too. We've had this in the back of our minds for a while as something to fix—split cards are strange. Their weirder interactions are fun if you understand them, but you must explain them every time you play against someone for the first time, and your opponent never quite believes you at first. Judges have a long and storied history of trying (sometimes in vain) to explain split cards to players. Once we knew *Amonkhet* was returning split cards to the Standard stage, we determined that it was time to simplify split cards.

The core of the change is that we're no longer assuming split cards have two sets of characteristics when they're not on the stack. Some characteristics have multiple pieces of information very naturally—Destined to Lead is an instant sorcery, the same as [Ornithopter](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter) is an artifact creature. It's black and green just like [Winding Constrictor](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winding+Constrictor) because its mana cost has B and G in it. Continuing that, the mana cost combines the components, and a card asking for Destined to Lead's mana cost sees 4BG.

So now, the converted mana cost question is simple: if Destined to Lead isn't on the stack, it has a converted mana cost of 6. Destined on the stack is still a black instant with a converted mana cost of 2, and Lead on the stack is still a green sorcery with a converted mana cost of 4, but Destined to Lead, any time it's not one or the other, is a black and green instant sorcery with a converted mana cost of 6.

We're aware that this puts a halt to a handful of decks that relied on taking advantage of split card converted mana cost interactions.

*   [Kari Zev's Expertise](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kari+Zev%27s+Expertise) won't let you cast [Breaking // Entering](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breaking+%2F%2F+Entering) or [Beck // Call](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beck+%2F%2F+Call).
*   [Violent Outburst](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Violent+Outburst) can't cascade into [Boom // Bust](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boom+%2F%2F+Bust).
*   [Isochron Scepter](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Isochron+Scepter) can't imprint [Far // Away](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Far+%2F%2F+Away) or [Bound // Determined](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bound+%2F%2F+Determined).
*   [Counterbalance](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterbalance) revealing [Wear // Tear](https://web.archive.org/web/20170404000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wear+%2F%2F+Tear) counters a spell with converted mana cost 3, but not 1 or 2.

We believe that these changes will improve the player experience when playing with split cards, old and new.
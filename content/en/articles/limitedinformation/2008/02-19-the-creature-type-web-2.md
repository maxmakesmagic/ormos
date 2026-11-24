---
id: k493zmwt
kind: article
lang: en
path: /en/articles/limitedinformation/2008/02-19-the-creature-type-web-2
title: The Creature Type Web
published: '2008-02-19'
column_slug: limitedinformation
column: Limited Information
authors:
- slug: daveguskin
  name: Dave Guskin
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?page=2&x=mtgcom/daily/nw51
    lang_detected: en
    capture_id: 1394113
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/nw51&page=2
    captured_at: '2008-05-07 17:34:08+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?page=2&x=mtgcom/daily/nw51
    lang_detected: en
    capture_id: 1394113
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/nw51&page=2
    captured_at: '2008-05-07 17:34:08+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?page=2&x=mtgcom/daily/nw51
    lang_detected: en
    capture_id: 1394113
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/nw51&page=2
    captured_at: '2008-05-07 17:34:08+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?page=2&x=mtgcom/daily/nw51
    lang_detected: en
    capture_id: 1394113
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/nw51&page=2
    captured_at: '2008-05-07 17:34:08+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: k493zmwt
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/nw51&page=2
  page_key: wizards.com/default.asp?page=2&x=mtgcom/daily/nw51
  lang: en
  template: classic_asp
  captured_at: '2008-05-07 17:34:08+00'
  capture_id: 1394113
  wayback_url: https://web.archive.org/web/20080507173408id_/http://www.wizards.com/default.asp?x=mtgcom/daily/nw51&page=2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: k493zmwt
  capture_id: 1394113
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/nw51&page=2
  wayback_url: https://web.archive.org/web/20080507173408id_/http://www.wizards.com/default.asp?x=mtgcom/daily/nw51&page=2
  captured_at: '2008-05-07 17:34:08+00'
  template: classic_asp
  sha256: b9be110574857188c68165964a35fe1d06bd3dc5abd19d859dd703ba1f188799
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Eyeblight[s_Ending')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Eyeblight's Ending
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Veteran[s_Armaments')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Veteran's Armaments
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Squeaking_Pie_Grubfellows')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Squeaking Pie Grubfellows
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Ponder')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Ponder
  occurrences: 1
---
* * *

### Math It Up

\*dons math hat\*

It's like a wizard hat, but less stars and more equations. We're about to get into some complex stuff, so hopefully only the most math-y (and least murderous) of you are reading this!

The initial problem question I thought up was:

> How is the Creature Type Web affected by a change in tribal count?

Considering my conception of the Creature Type Web is more of a qualitative concept than something that can be put directly into numbers, I backed off of this and considered just the kinship mechanic:

> How is the reliability of kinship affected by a change in tribal count? Specifically, are there interesting correlations between tribal count and kinship triggers?

To solve this problem analytically, I looked up [hypergeometic distribution](https://web.archive.org/web/20080219000000/http://www.wizards.com/leaving.asp?url=http://en.wikipedia.org/wiki/Hypergeometric_distribution&origin=mtgcom_daily_nw51), which gives an equation for determining various probabilities on drawing without replacement. However, this distribution could not account for the intricacies of when to play the kinship card, and considering the incremental effect of sequential triggers made my head hurt.

At this point, I decided to go with the scientist's mainstay: the [Monte Carlo method](https://web.archive.org/web/20080219000000/http://www.wizards.com/leaving.asp?url=http://en.wikipedia.org/wiki/Monte_Carlo_method&origin=mtgcom_daily_nw51), which would allow me to configure the scenario as one would play it in a goldfish-type situation, and then iterate a hojillion times to get a better estimate of the trends.

As I mentioned in my article, I made quite a few assumptions to simplify this scenario and allow these simulated games to complete without complex branching into many possible states. The results I found are still valid when applied to a real-game situation. One just needs to be aware of the differences between your game and the simulated one, and use those differences to estimate the effectiveness of the Monte Carlo results.

For those interested in the algorithm behind the simulated game, here's how it went down:

*   Create a deck of 40 cards.
*   T of them are tribal matches to the kinship in question.
*   K of them are kinship cards (which of course match each other in this analysis).
*   The rest are neither T or K.
*   Randomize this deck and draw twenty times (representing a game of thirteen turns).
*   Assume you make every land drop.
*   Assume you play the kinship cards you draw at the first opportunity.
*   Assume your kinship card remains in play the remainder of the game after you play it.
*   Count up the number of triggers you would have before the game ends.

I varied T (the number of tribally relevant cards in the deck) of between 1 and 15, with the assumption that 15 would be close to maxing out your creature count. Your results would be better if you played fewer lands and more matching creatures of the relevant type, and they would be better if you played tribal spells such as Eyeblight's Ending or Veteran's Armaments.

I varied K (the number of kinship cards in the deck) between 1 and 5. To simplify things, and to allow us to visualize the results at all, multiple kinship cards in play are treated as a multiplier to the effect. This is true in most, but not all, of the kinship cards' cases, such as Pyroclast Council (where two triggers would kill both) or Squeaking Pie Grubfellows (where two triggers might be giving away information for free if they have only one card in hand). At the very least, the option to trigger twice increases value.

There are plenty of library manipulation effects you could use to increase the chances of the top card matching, especially in *Lorwyn* / *Morningtide* Limited, including clash, Harbingers, and Ponder. So keep those in mind when applying these results to your own Draft and Sealed experience!
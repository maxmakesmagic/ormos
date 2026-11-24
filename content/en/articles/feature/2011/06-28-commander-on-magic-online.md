---
id: mxkvabq9
kind: article
lang: en
path: /en/articles/feature/2011/06-28-commander-on-magic-online
title: Commander on Magic Online
published: '2011-06-28'
column_slug: feature
column: Feature
authors:
- slug: lee-sharpe-29bdd696
  name: Lee Sharpe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
    lang_detected: en
    capture_id: 615921
    url: https://magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
    captured_at: '2021-10-27 05:10:58+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
    lang_detected: en
    capture_id: 615921
    url: https://magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
    captured_at: '2021-10-27 05:10:58+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
    lang_detected: en
    capture_id: 615921
    url: https://magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
    captured_at: '2021-10-27 05:10:58+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
    lang_detected: en
    capture_id: 615921
    url: https://magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
    captured_at: '2021-10-27 05:10:58+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: mxkvabq9
  url: https://magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
  page_key: magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
  lang: en
  template: drupal
  captured_at: '2021-10-27 05:10:58+00'
  capture_id: 615921
  wayback_url: https://web.archive.org/web/20211027051058id_/https://magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
- document_id: mxkvabq9
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/06282011e
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/other/06282011e
  lang: en
  template: aspx
  captured_at: '2013-06-30 14:34:10+00'
  capture_id: 662360
  wayback_url: https://web.archive.org/web/20130630143410id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/06282011e
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: mxkvabq9
  capture_id: 615921
  url: https://magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
  wayback_url: https://web.archive.org/web/20211027051058id_/https://magic.wizards.com/en/articles/archive/feature/commander-magic-online-2011-06-28
  captured_at: '2021-10-27 05:10:58+00'
  template: drupal
  sha256: 21a2d439defc37d488e7ba3dec116b29667b75d4327d778ecf32d0e40aa419b4
render_recovery: []
---
A little over four years ago, I was excited to accept a dream job working at Wizards of the Coast as a **Magic Online** game server developer. Accepting this job did come at a significant cost: I was no longer allowed to play in **Magic Online** tournaments. I miss this a lot.

Since I couldn't play in tournaments, I started thinking about what **Magic Online** had to offer. I remembered enjoying crazy awesome EDH games that I would play with my fellow judges in the evenings after Pro Tours and other major paper **Magic** tournaments. EDH, however, didn't exist online. But could it?

I decided it could. I came in over two Saturdays and programmed away. At the next build opportunity, EDH—renamed Commander—came to **Magic Online**. I didn't think that many other people would be interested; as far as I knew it was mostly a niche format that those of us in the judging community had adopted. Let's just say I underestimated the interest. Now, if you want to get a Commander game in on **Magic Online**, you only have to wait a few minutes. 

***Magic: The Gathering** Commander* was recently released in paper, and I had the pleasure of working on the R&D development team. I mostly worked on the green-blue-black "Devour for Power" deck, but all five decks are fantastic. I'm really proud of how well the community has received them and their ability to expand the format. All five decks will be available in the **Magic Online** store on July 4, 2011. 

I've moved on from game server development to working on business analysis here at Wizards, but current game server developers Jason Radabaugh and Peter Beckfield took the opportunity to improve my initial implementation of the format, and I'm excited to be able to announce their changes. The changes, which will take effect after the June 29 downtime, are as follows: 

1\. Commander Goes in the Sideboard

Instead of choosing your commander after the game has started, you make your commander selection as you build your deck by placing it in the sideboard. This means that Commander decks will now have a 99-card main deck and a 1-card sideboard **Magic Online**'s deck legality system will help you know in advance whether you've built a legal Commander deck or not. **Magic Online** will automatically move each player's commander from the sideboard to the command zone as the game begins. 

2\. Color Identity Instead of Color

Previously, a deck wasn't legal commander unless the color(s) of each card in the deck were a subset of the commander's color(s). To bring **Magic Online** Commander more in line with the paper rules, legality will now be based on color identity rather than color. 

> 903.4. The color identity of a deck's commander is the color or colors of any mana symbols in that card's mana cost or rules text, plus any colors defined by its characteristic-defining abilities.

This means you can no longer use a card with an off-color mana symbol in the cost of an activated ability (such as Wormwood Dryad with a nonblack commander), cards with an off-color kicker cost (such as Dismantling Blow with a nonblue commander), or cards that otherwise use mana symbols that are not in your commander's colors (such as Bringer of the Red Dawn with a nonred commander). Partially off-color hybrid cards remain illegal. 

This change also allows cards like Bosh, Iron Golem to be used as commanders. Bosh, Iron Golem's color identity is red, so if it is your commander, you can add red or colorless mana to your mana pool and have red or colorless cards in your deck. 

3\. Banned or Banned as a Commander

**Magic Online** previously did not have the ability to ban cards as commanders without banning them entirely. This is no longer true. Braids, Cabal Minion and Rofellos, Llanowar Emissary will now be allowed in decks, but you won't be able to use them as commanders. 

4\. No More Super-Legendary

Previously, **Magic Online** Commanders did not follow the legend rule. Now they will. If someone else in the game has the same commander as you, they won't be able to be on the battlefield at the same time. 

Hello and Good Luck! 

I am excited about these changes as we make the paper and **Magic Online** Commander formats more similar, and I hope to see you playing some Commander on **Magic Online**. Don't forget that all five ***Magic: The Gathering** Commander* decks are playable as soon as they go on sale on July 4.
---
id: zaxp679w
kind: article
lang: en
path: /en/articles/play-design/2017/09-29-four-rules-for-a-balanced-format
title: Four Rules for a Balanced Format
published: '2017-09-29'
column_slug: play-design
column: Play Design
authors:
- slug: melissa-detora-b431380a
  name: Melissa DeTora
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
    lang_detected: en
    capture_id: 1133909
    url: https://magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
    captured_at: '2022-08-14 07:10:09+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
    lang_detected: en
    capture_id: 1133909
    url: https://magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
    captured_at: '2022-08-14 07:10:09+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
    lang_detected: en
    capture_id: 1133909
    url: https://magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
    captured_at: '2022-08-14 07:10:09+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
    lang_detected: en
    capture_id: 1133909
    url: https://magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
    captured_at: '2022-08-14 07:10:09+00'
    rule: url.article_section
sources:
- document_id: zaxp679w
  url: https://magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
  page_key: magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
  lang: en
  template: drupal
  captured_at: '2022-08-14 07:10:09+00'
  capture_id: 1133909
  wayback_url: https://web.archive.org/web/20220814071009id_/https://magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: zaxp679w
  capture_id: 1133909
  url: https://magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
  wayback_url: https://web.archive.org/web/20220814071009id_/https://magic.wizards.com/en/articles/archive/play-design/four-rules-balanced-format-2017-09-29
  captured_at: '2022-08-14 07:10:09+00'
  template: drupal
  sha256: 07333469f1078e98ac33c913bb8745e690a7a70940689e0e037a63b07539b3b9
render_recovery: []
---
Hello, and welcome back to Play Design. Today's article will again talk about format balance with a focus on general philosophy rather than individual cards. Our head developer, Erik Lauer, came up with this philosophy. Like with all *Magic* philosophy, it should be taken with a grain of salt but always considered when crafting a Standard format.

Before we get started, here are some things you should know about Erik Lauer:

1.  He just celebrated his ten-year anniversary at Wizards.
2.  He loves math, steak, and dogs, in that order.
3.  He is one of the smartest people I know and someone I highly respect.

Without further ado, here are four rules for a balanced format.

**1.Decks should have interaction.**

If you take two decks with zero interaction and match them up against each other, it comes down to a pure race. At that point, there is no point in playing the matchup. You could both go in separate rooms, [goldfish](/en/articles/feature/2017/08-04-philosophy-of-combo#goldfishing) your deck, and then tell the other player on which turn your deck won to determine who wins the matchup. That's not a very fun way to play *Magic*.

Some combo decks suffer from this problem. Most combo decks play interaction such as [Force of Will](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) in Legacy or [Thoughtseize](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtseize) in Modern. These days, it's pretty rare to see a Standard deck with zero ways to stop the opponent from doing their thing. Even the most linear of decks, like Mono-Red Aggro or Burn, play something. [Revel in Riches](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Revel+in+Riches) and [Spitfire Bastion](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spitfire+Bastion) are both difficult to deal with. If those cards faced off against one another, it would be a pure race, so interaction is needed. Of course, there are decks that will play zero interaction, such as a green stompy deck that only plays Forests and creatures. The issue only arises when a matchup exists in which *both* decks have zero interaction.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Spitfire+Bastion)](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spitfire+Bastion)[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vance%27s+Blasting+Cannons)](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vance%27s+Blasting+Cannons)

When we find that our Standard decks in [Future Future League](/en/articles/play-design/2017/07-07-designing-hour-of-devastation-cards-to-meet-ffl-goals) are not playing interaction, whether the reason is that they are combo decks that need all of their slots dedicated to the combo or decks that are too linear to play ways to interact, we mitigate the problem by making our interaction stronger. However, having too much interaction leads to the next problem.

**2.Decks should not be a battle of resource exchange.**

If the key to a matchup becomes all about trading resources, then whoever gains the most card advantage wins. It doesn't matter what cards are actually played; all that matters is whoever has the most cards wins the matchup. When this happens, deck-building choices become irrelevant.

One example of this problem occurring in the real world is with Draw-Go Control decks. There was a time when this deck played cards that went one-for-one on curve with everything the opponent was doing. Turn one [Force Spike](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+Spike), turn two [Counterspell](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell), turn three [Dissipate](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dissipate), turn four [Dismiss](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss). The key card here is [Dismiss](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss) because in this trade, the player is up a card. If this player continues to make these incremental trades, then eventually they will just have so much card advantage that they will inevitably win. It doesn't matter what they win with; the opponent cannot possibly come back. This deck also played [Treachery](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treachery) and [Whispers of the Muse](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whispers+of+the+Muse) as ways to gain a card with one spell.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Treachery)](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treachery)

Exchanging cards for cards and gaining card advantage is important, but that shouldn't be what the matchup is about. When we have this problem, we mitigate it by adding more things to do in the late game, hard-to-deal with threats, or stronger planeswalkers. We want variety, trump cards in particular matchups, and ways to come back if you're behind.

However, these late-game cards that help mitigate the card advantage problem can lead to a different problem, which leads to rule number three.

**3.Avoid the early/late game dichotomy.**

We have this rule in place to make sure there isn't one deck that can only win early, and one that cannot survive the early game. When these two decks face each other, one of two things will happen. Either the deck that wins early wins, or they get to the late game and the early deck is unable to win. [Gishath, Sun's Avatar](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gishath%2C+Sun%27s+Avatar) and [Vraska, Relic Seeker](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vraska%2C+Relic+Seeker) are very powerful late-game cards, but you need to build your deck in a way to survive the early game. Similarly, [Rigging Runner](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rigging+Runner) is a powerful early game card but not strong enough to win a long game. In both scenarios, one of the players is unable to do anything meaningful throughout the game.

One example of a deck that can only win early is a mono-red deck with no late game burn or [Falter](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Falter) effects. During [Pro Tour *Dragon's Maze*](https://web.archive.org/web/20170929000000/https://magic.wizards.com/en/content/pro-tour-dragons-maze-2013) (Block Constructed), I played this deck to poor results. The deck was all one- and two-drop creatures and no burn. If I ever drew more than four lands in a game, I could not possibly win. My wins were nail-biters, and the losses were hopeless. Luckily, my undefeated Draft record saved my Pro Tour performance. This deck's problem was solved in the next core set when we were given [Stoke the Flames](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stoke+the+Flames) and [Goblin Rabblemaster](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Rabblemaster). Even adding a few late-game cards can change a deck dramatically.

Late-game-only decks are much more rare because decks that can't beat a quick aggressive deck just don't perform well competitively. A deck that doesn't take mana curve into consideration and plays a lot of four- and five-drops will suffer from this problem. We try to make a variety of early and late-game spells so that players have the option to play at the speed they want to, whether it's aggro, midrange, or control. However, when we add cards to a format to deal specifically with a strong late-game strategy, we have yet another problem, which leads to rule number four.

**4.All threats should have answers.**

If a card is too strong, it will become the pivotal card in the matchup, and whoever plays it first wins. We add answers to these types of cards to avoid this problem; in *Ixalan* specifically, we added [Duress](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duress) and [Sorcerous Spyglass](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorcerous+Spyglass) for precisely this reason. Every threat should have an answer, and these answers should be strong and versatile enough so that you can play them main deck. We don't want to be in a situation in which there is a card that exists that is an auto-win when you get to a certain point in the game.

![Sorcerous Spyglass](https://media.wizards.com/2017/images/daily/cardart_XLN_Sorcerous-Spyglass.jpg)

[Sorcerous Spyglass](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorcerous+Spyglass) | Art by [Kieran Yanner](https://web.archive.org/web/20170929000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Kieran+Yanner%22%5d)

Going back to *Return to Ravnica* era, cards that I felt met this criterion were [Sphinx's Revelation](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation) and [Ætherling](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%C3%86therling). I played a lot of [Sphinx's Revelation](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation) control decks and felt that resolving this spell for a high amount caused the opposing player to feel "hopeless." Once the [Sphinx's Revelation](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation) player drew five or more cards, the game was over and the opposing player just sat there until they killed them.

[Ætherling](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%C3%86therling) attempted to solve this problem by giving you a quick way to kill your opponent after you resolved your [Sphinx's Revelation](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation). However, this creature had its own problems in that it was impossible to remove. Once you had one in play with mana up, there was no way to get it off the board, which made the mirror match even more frustrating because you knew that resolving this one pivotal card would decide the game.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sphinx%27s+Revelation)](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=%C3%86therling)](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%C3%86therling)

A more reasonable answer to this problem is something like [Pearl Lake Ancient](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pearl+Lake+Ancient). This creature is also very hard to remove, but since you have to return lands to your hand, there was always a window in which you couldn't recast it, giving your opponent the chance to turn the corner. Hard-to-deal with threats are always going to exist, but there will be counter play to these threats and shields-down moments so that the opponent doesn't feel like they have no chance.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pearl+Lake+Ancient)](https://web.archive.org/web/20170929000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pearl+Lake+Ancient)

Again, these four rules are not hard rules, but rather guidelines and things we look for as we balance Standard. We have many tools to mitigate these problems, and the idea is that if we identify these problems as we playtest, we can solve them by adding the appropriate cards to the format.

Thanks for reading and until next time,

Melissa DeTora  
[@MelissaDeTora](http://www.twitter.com/melissadetora)
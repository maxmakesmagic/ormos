---
id: dvwxddtq
kind: article
lang: en
path: /en/articles/makingmagic/2003/03-31-this-land-is-my-land
title: This Land is My Land
published: '2003-03-31'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
    lang_detected: en
    capture_id: 222473
    url: https://magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
    captured_at: '2024-03-05 10:30:29+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
    lang_detected: en
    capture_id: 222473
    url: https://magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
    captured_at: '2024-03-05 10:30:29+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
    lang_detected: en
    capture_id: 222473
    url: https://magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
    captured_at: '2024-03-05 10:30:29+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
    lang_detected: en
    capture_id: 222473
    url: https://magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
    captured_at: '2024-03-05 10:30:29+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: dvwxddtq
  url: https://magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
  page_key: magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
  lang: en
  template: contentful
  captured_at: '2024-03-05 10:30:29+00'
  capture_id: 222473
  wayback_url: https://web.archive.org/web/20240305103029id_/https://magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
- document_id: dvwxddtq
  url: http://wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr65&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr65
  lang: en
  template: aspx
  captured_at: '2013-07-31 20:20:36+00'
  capture_id: 256868
  wayback_url: https://web.archive.org/web/20130731202036id_/http://wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr65&print=true
- document_id: dvwxddtq
  url: https://magic.wizards.com/en/articles/archive/making-magic/land-my-land-2003-03-31
  page_key: magic.wizards.com/en/articles/archive/making-magic/land-my-land-2003-03-31
  lang: en
  template: drupal
  captured_at: '2022-02-07 05:06:59+00'
  capture_id: 891575
  wayback_url: https://web.archive.org/web/20220207050659id_/https://magic.wizards.com/en/articles/archive/making-magic/land-my-land-2003-03-31
- document_id: dvwxddtq
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr65,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr65
  lang: en
  template: classic_asp
  captured_at: '2005-01-08 09:38:26+00'
  capture_id: 1980476
  wayback_url: https://web.archive.org/web/20050108093826id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr65,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: dvwxddtq
  capture_id: 222473
  url: https://magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
  wayback_url: https://web.archive.org/web/20240305103029id_/https://magic.wizards.com/en/news/making-magic/land-my-land-2003-03-31
  captured_at: '2024-03-05 10:30:29+00'
  template: contentful
  sha256: 869ee6d84fe16927f4be442bc5e0a5973cec46a083c39b0658d03d7b41d10da0
render_recovery: []
---
Welcometo Nonbasic Land Week! This week is dedicated to the card type that does the most amount of work and receives the least amount of attention. And as this is a design column, I thought I'd take my time today to explain how land is designed.

### Land Ho

When a designer sits down to design a land, the first thing he has to confront is a number of rules about how R&D has decided land needs to work. (For those of you that feel rules to design are ruining the game, I ask you to stay tuned for next week when I talk about the importance of structure in design.) I thought I'd run through each rule and explain what ramification it has on design.

### Rule #1 – No Land Can Be “Strictly Better” Than a Basic Land

I guess I should start by explaining what I mean by “strictly better.” This is a phrase R&D tosses around a lot. “Strictly better” means that one card is in all occurrences (within reason) better than another. An example of a “strictly better” would be [Lightning Bolt](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) versus [Shock](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock). Barring a really convoluted set-up (you know your opponent has [Eye for an Eye](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eye+for+an+Eye) and you're at 3 life while he's at 2), you would always want [Lightning Bolt](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) over [Shock](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock). For an identical cost, it just does exactly the same thing, but better.

The ramification of the “strictly better” rule is that we cannot design lands that tap for a colored mana without having some kind of drawback. The nonbasic land status, incidentally, is not considered by R&D to be enough of a drawback. While there are spells that hose nonbasic lands (like [Price of Progres](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Price+of+Progres)s), there are also spells that hose specific basic lands (like [Boil](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boil)) that do not affect nonbasic lands (other than the original [Tundra](https://web.archive.org/web/20030331000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Tundra)). As such, we consider the ability to be a slight negative but not enough to avoid the “strictly better” problem.

<table><tbody><tr><td><br><i>Each of these lands has advantages and disadvantages over basic lands, leading to interesting deckbuilding decisions.</i></td></tr></tbody></table>

Designing lands requires us to create drawbacks. Here are some of the more popular drawbacks we use:

1.  **Tap For Colorless ([Goblin Burrows](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Burrows), [Rishadan Port](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rishadan+Port), etc.) –** One way we avoid the color problem is to not have the lands produce colored mana. This is enough of a drawback that we can add a second ability. Although, once again, R&D needs to be careful. Most of our mistakes with lands occur in this category. Colorless lands are a lot like artifacts in that they can go in any deck. This general utility has to be accounted for both to keep it from usurping colored abilities and for overall power level.
2.  **Comes Into Play Tapped ([Forgotten Cave](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forgotten+Cave), [Coastal Tower](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coastal+Tower), etc.) –** The most popular technique for lands that produce colored mana is to have the land come into play tapped making it unusable for the first turn it's in play. The advantage to this method is that it's very simple and straight-forward. The downside is the drawback is terrible for cards designed to fit into an aggressive deck and overall is a bit overused.
3.  **Requires Life Payment ([Karplusan Forest](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karplusan+Forest), [City of Brass](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=City+of+Brass), etc.) –** This is the second most popular answer to keep color producing lands in check. The idea here is that the drawback is an additional cost. Life is the best answer as its always relevant and easy to both write and understand.
4.  **Use Every Other Turn ([Lava Tubes](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Tubes), [Teferi's Isle](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teferi%27s+Isle), etc.) –** Another drawback is to keep the player from using the lands every turn. Numerous techniques – such as depletion counters, self-boomeranging, phasing – have been used to accomplish this.
5.  **Limited Number Of Uses ([Gemstone Mine](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gemstone+Mine), [Remote Farm](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remote+Farm), etc.) –** This drawback has the advantage in that it works well in aggressive decks. The downside is that it requires the use of counters.
6.  **Cost Required When Land Is Played ([Kjeldoran Outpost](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kjeldoran+Outpost), [Rith's Grove](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rith%27s+Grove), etc.) –** This drawback requires a payment to play the land. The most popular payments are sacrificing a permanent or returning a permanent to your hand. This drawback makes you pay up front for the bonus you will receive for the remainder of the game.
7.  **Don't Provide Mana By Themselves ([Reflecting Pool](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reflecting+Pool), [Mossfire Valley](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mossfire+Valley), [Gaea's Cradle](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Cradle), etc.) –** Another drawback is to create cards that need other cards (usually lands) to work. These cards cause problems because you don't want them to be your first land in play.
8.  **Requires Another Permanent In Play ([Thran Quarry](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thran+Quarry)) –** The idea behind this drawback is that the land can only be used in a certain type of deck (a deck with creatures, for example).

One of the challenges of designing lands is finding new drawbacks or interesting twists on existing drawbacks.

<table><tbody><tr><td><br><i>Maze of Shadows is a &quot;modernized&quot; spin-off of Maze of Ith: it can tap for mana.</i></td></tr></tbody></table>

### Rule #2 – Lands Must Produce Mana

I spend a great deal of time talking about the importance of color identity, how it's important that each color do something unique. The same arguments hold true for card types (artifact, creature, enchantment, instant, land and sorcery). Like color, each card type should have its own unique role in the game.

In early **Magic**, the designers fooled around with lands that had effects other than mana production. Through trial and error, R&D learned that non-mana producing lands started feeling more like artifacts or enchantments. To keep land's identity pure, R&D created this rule. This doesn't mean that lands can't do non-mana related things, it just means that in addition each land must provide mana.

There is one big exception to this rule. Lands that either filter for mana or allow you to get access to lands (which will in turn provide mana) are allowed. This is why lands like [Mossfire Valley](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mossfire+Valley) or [Windswept Heath](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Windswept+Heath) are acceptable under this rule. The idea is that these lands are being true to land's identity because their main function is helping players get mana.

### Rule #3 – Lands Cannot Produce More Than One Mana

This rule is a result of the *Urza's Saga* block. R&D recognized that one of the key elements to the craziness of the block was the fast mana available in the format. As such, R&D decided to slow down mana production. One way to do this was to prevent creating lands that created more than one mana. We do occasionally break this rule (with a card like [Cabal Coffers](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cabal+Coffers)), but we do so very carefully to make sure that the land does not contribute to creating a recklessly fast environment.

### Rule #4 – Lands That Produce Colored Mana Must Come In Cycles

Just as we balance colored cards in any one set (with a few prominent exceptions), we also balance cards that produce colored mana. If a card produces all five colors it may stand on its own, but if it produces any less than all five, we have the card appear in a cycle to make sure that all the colors get equal representation. Most commonly this leads to single-color cycles (such as the [Lonely Sandbar](https://web.archive.org/web/20030331000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Lonely%2BSandbar) in *Onslaught*) and dual-color cycles (the [Underground River](https://web.archive.org/web/20030331000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Underground%2BRiver) in *Ice Age*).

This means that designing lands often comes very early in the process as you have to carve out space for five cards. Also, this means that we do not have the freedom of making a random colored land. The one pseudo-exception to this rule was our “[mega mega cycle](https://web.archive.org/web/20030331000000/https://magic.wizards.com/en/articles/archive/moons-mirrodin-2003-09-11)” ([Teferi's Isle](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teferi%27s+Isle), [Volrath's Stronghold](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volrath%27s+Stronghold), [Kor Haven](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kor+Haven), [Yavimaya Hollow](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yavimaya+Hollow), and [Keldon Necropolis](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keldon+Necropolis)). These cards were alone in the set they appeared but were part of a cycle that came out once a year over a five-year period. And of the five, only [Teferi's Isle](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teferi%27s+Isle)—the first one printed—produces colored mana.

<table><tbody><tr><td><br><i>Dominant colorless lands are often looked at by R&amp;D as mistakes, as they start showing up in a disproportionate number of decks.</i></td></tr></tbody></table>

### Rule #5 – Lands Cannot Do Colored Abilities Without Requiring the Use of Colored Mana

One of the strengths of land (and artifacts) is that they can be used in any deck. As such, R&D has to be very careful about what abilities we put on lands. Land destruction, for example, is an ability centered in red that also appears in black and green (and occasionally in white in the mass variety). This makes [Strip Mine](https://web.archive.org/web/20030331000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strip+Mine) a mistake (for many reasons other than this one, incidentally) because it allows a blue deck access to a non-blue ability with little or no effort.

To combat this problem, we always require colored mana to use an effect we are uncomfortable giving to all five colors. What this means is that we allow small effects for colorless, but most large effects or highly color-aligned effects require the use of a colored mana symbol in their activation. Occasionally, this can be accomplished by means other than mana (for example, sacrificing the appropriate basic land).

### Land of the Free

As you can see, designing a land is not as easy as it might first appear. Given the above rules, here is the most common process a designer will take when designing a land.

**Step #1 –** Come up with a new twist for a land.  
**Step #2 –** If it doesn't have a drawback, create a drawback (this is often tied into step #1).  
**Step #3 –** Decide whether or not the land can stand on its own or whether it requires a five card cycle.  
**Step #4 –** If the card uses any color-associated abilities, make sure that the ability cannot be used by off-color.  
**Step #5 –** If the land produces more than one mana, red flag it for development to study.

And thus a land is born. Hopefully, this has given you a better insight into the many issues that go into designing a land.

Join me next week when I explain the role of structure in the design process.

Until then, may you draw the lands you want in your opening hand.

Mark Rosewater

*Mark may be reached at makingmagic@wizards.com.*
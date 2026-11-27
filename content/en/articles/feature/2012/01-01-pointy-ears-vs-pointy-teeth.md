---
id: fvghjbe2
kind: article
lang: en
path: /en/articles/feature/2012/01-01-pointy-ears-vs-pointy-teeth
title: Pointy Ears vs. Pointy Teeth
published: '2012-01-01'
column_slug: feature
column: Feature
authors:
- slug: devinlow
  name: Devin Low
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
    lang_detected: en
    capture_id: 656899
    url: https://magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
    captured_at: '2021-10-20 01:32:50+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
    lang_detected: en
    capture_id: 656899
    url: https://magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
    captured_at: '2021-10-20 01:32:50+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
    lang_detected: en
    capture_id: 656899
    url: https://magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
    captured_at: '2021-10-20 01:32:50+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
    lang_detected: en
    capture_id: 656899
    url: https://magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
    captured_at: '2021-10-20 01:32:50+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: fvghjbe2
  url: https://magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
  page_key: magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
  lang: en
  template: drupal
  captured_at: '2021-10-20 01:32:50+00'
  capture_id: 656899
  wayback_url: https://web.archive.org/web/20211020013250id_/https://magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: fvghjbe2
  capture_id: 656899
  url: https://magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
  wayback_url: https://web.archive.org/web/20211020013250id_/https://magic.wizards.com/en/articles/archive/feature/pointy-ears-vs-pointy-teeth-2007-11-19
  captured_at: '2021-10-20 01:32:50+00'
  template: drupal
  sha256: 474a44c21bd8b37fc6585dc3737fa9b493ba588ee3549cc06192d38e05a7e4ea
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 2
---
Few topics could call me forth from my new lair in Friday's [Latest Developments](https://web.archive.org/web/20120101000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/columnarchive) column, but this week is one of them. It's the debut of a new breed of double theme deck: *Duel Decks: Elves vs. Goblins* (check out the product page [here](https://web.archive.org/web/20120101000000/http://archive.wizards.com/Magic/TCG/Article.aspx?x=magic/expansion/elvesvsgoblins)). But even though I developed these decks with all-star development intern Noah Weil, I couldn't talk about them only in the development column... because we designed them, too. That's why I'd like to take you through some of the ways we made the Goblin explosives tick and the Elvish arrows tock.

[![](http://archive.wizards.com/global/images/magic_expansion_ElvesvsGoblins_expansionLogo_en.jpg)](http://archive.wizards.com/global/images/magic_expansion_ElvesvsGoblins_expansionLogo_en.jpg)

"I have a project for you," director of **Magic** R&D Aaron Forsythe said, and he laid out a simple idea. We were to make a fun holiday gift box themed around an ancient rivalry with a lot of flavor: Elves vs. Goblins. It should have two sixty-card decks and they should be Extended-legal. The company wanted to price the two-deck-package at less than the price of two normal theme decks.

> "Ok, two sixty-card decks," I responded. "How many rares?"
> 
> "Well, normal theme decks have two rares apiece," Aaron replied. "This costs less than two theme decks, but I was thinking we could still give it four rares. Or actually, more than that."
> 
> "How many more?" I asked.
> 
> "Five would be okay," he said. "Or six."
> 
> He paused. I looked at him questioningly.
> 
> "Well, it is the holidays," he said. "How about *eight*."

The **Magic** Brand team gave the okay to eight rares. Then the creative team agreed to commission unique alternate artwork for two of the rares. The production team agreed to create some new packaging that would show off the alternate art through a visible pane in the box and look good in wrapping paper. Then we got approval to make the alternate-art rares foil. And we decided to make one of the alternate-art foil rares be Siege-Gang Commander. When Noah and Aaron and I started talking about classic Elf and Goblin cards we could put into the box, an idea emerged for one more additional bonus: we could add token cards to the box for all the tokens that the Goblin and Elf decks created. In they went. All the departments had come together, and the *Elves vs. Goblins* box had everything we could possibly give it. Noah and I just had to do one little thing: make the decks.

### Gathering Gobs of Goblins

Before hitting the keyboards, Noah and I came up with a couple of goals for building the decks: They have to be fun to play. They have to be a fun matchup against each other. They should be much more powerful than normal theme decks. They should showcase as many as possible of the greatest and most powerful Elves and Goblins in Extended history. They should have lots of diversity to ensure lots of replayability. They should show off some cool interactions between *Lorwyn* block's Elf and Goblin tribal themes, *Onslaught* block's Elf and Goblin tribal themes, and all the sets in between. And if you put a couple of them together, they should give you a solid foundation to play a hardcore Goblin or Elf deck for Extended tournaments.

 ![Elves vs. Goblins Harmonize](http://archive.wizards.com/magic/images/mtgcom/fcpics/features/432_Harmonize.jpg)

 Next Noah and I talked about some famously powerful Elves and Goblins, including some of the most powerful Elves and Goblins (and appropriate support cards) ever to tear up Standard and Extended tournaments, and whether they were too powerful to include in a gift box. Timberwatch Elf? In. Wellwisher? In. Wren's Run Vanquisher? In. Llanowar Elves, Harmonize, Wirewood Symbiote? In. Goblin Warchief? In. Siege-Gang Commander? In. Goblin Sledder and Skirk Prospector? In. Clickslither? In. Gempalm Incinerator? In. Mogg Fanatic? In. Everything was in-bounds.

Then we talked about the classic Elves vs. Goblins fights across history. Llanowar Elves faced down Goblin Balloon Brigade in Alpha in 1993, and they've basically been punching each other in the face ever since. *Urza's Saga* included Legacy powerhouses Priest of Titania and Goblin Lackey, two- and one-mana creatures that ludicrously tapped to produce about five mana apiece. This fit them in perfectly with *Urza's Saga*'s theme of ludicrous mana acceleration and lands that tapped to produce about five mana apiece. Then *Onslaught* redefined the Elves vs. Goblins rivalry with powerful tribal effects like Wellwisher and Goblin Warchief that catapulted Elves and Goblins to the top of Standard decklists in popularity and power. *Lorwyn* marks a new chapter in the eternal Elves vs. Goblins war, delivering the best lords these tribes have ever had, in the form of Imperious Perfect and Mad Auntie.

In *Onslaught* block, both tribes were powerful, but when they met head-to-head, Goblins had the advantage. The reason was that Goblins could kill the key Elf creatures like Wellwisher with tons of burn effects, while mono-green Elves couldn't return the favor, and had to let powerful Goblin creatures like Goblin Warchief survive. *Lorwyn* solves this disparity by giving Elves access to black mana, with Elf-subtyped spells like Eyeblight's Ending and Nameless Inversion.

For the Duel Decks, however, Noah and I decided to keep them mono-green and mono-red, in keeping with the classic, timeless feel of the matchup. Staying monocolored also kept these decks distinct from the *Lorwyn* Elf and Goblin theme decks, which are black-green and black-red respectively. The *Lorwyn* theme decks are a better introduction to *Lorwyn* itself, an exploration of how the tribes integrate their new colors, focus 100% on cards from the newest set, and are a better teaching tool for new players. *Duel Decks: Elves vs. Goblins* is meant for advanced players, and is more "no-holds-barred."

### Establishing Echelons of Elves

Since the Elves were staying monogreen, we used other methods to address the historical disparity in removal. To let the Elves burn back, we gave the Elves three Moonglove Extracts, a *Lorwyn* direct damage card any color can use. And we made sure that the Elf deck had more "must-kill" targets than the Goblin deck, so that even the Goblins' many burn spells would be hard-pressed to take care of them all. Putting multiple 3-toughness Elves into the mix, from Elvish Warrior to Lys Alana Huntmaster to Wren's Run Vanquisher, also helped set up an Elvish defensive line that could give the Goblins' 2-point burn effects and 2-power attackers some serious holdup.

Once we had our initial decklists, we put them through the playtesting grinder, fighting both sides of the matchup dozens of times, tweaking as we went, then handing them to other R&D members and watching them play. We knew we were getting close when one playtest pair assured us that the Goblins were better, while another playtest pair with the same decks assured us that the Elves were better. Without further ado, here are the *Elves vs. Goblins* final decklists, previously presented in a Magic Arcana:

#### 

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (29)

1 [Ambush Commander](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAmbush%5D+%5BCommander%5D) 1 [Allosaurus Rider](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAllosaurus%5D+%5BRider%5D) 2 [Elvish Eulogist](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BEulogist%5D) 1 [Elvish Harbinger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BHarbinger%5D) 3 [Elvish Warrior](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BWarrior%5D) 2 [Gempalm Strider](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGempalm%5D+%5BStrider%5D) 1 [Heedless One](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeedless%5D+%5BOne%5D) 2 [Imperious Perfect](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImperious%5D+%5BPerfect%5D) 3 [Llanowar Elves](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLlanowar%5D+%5BElves%5D) 2 [Lys Alana Huntmaster](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BHuntmaster%5D) 1 [Stonewood Invoker](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStonewood%5D+%5BInvoker%5D) 1 [Sylvan Messenger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BMessenger%5D) 1 [Timberwatch Elf](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTimberwatch%5D+%5BElf%5D) 1 [Voice of the Woods](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoice%5D+%5Bof%5D+%5Bthe%5D+%5BWoods%5D) 2 [Wellwisher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWellwisher%5D) 1 [Wirewood Herald](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BHerald%5D) 1 [Wirewood Symbiote](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BSymbiote%5D) 2 [Wood Elves](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 1 [Wren's Run Vanquisher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWren%5D+%5BRun%5D+%5BVanquisher%5D) 

##### Sorcery (2)

1 [Elvish Promenade](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BPromenade%5D) 1 [Harmonize](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHarmonize%5D) 

##### Instant (3)

2 [Giant Growth](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Wildsize](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildsize%5D) 

##### Artifact (4)

3 [Moonglove Extract](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoonglove%5D+%5BExtract%5D) 1 [Slate of Ancestry](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlate%5D+%5Bof%5D+%5BAncestry%5D) 

##### Land (22)

19 [Forest](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 2 [Tranquil Thicket](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTranquil%5D+%5BThicket%5D) 1 [Wirewood Lodge](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BLodge%5D) 

60 Cards 

##### Green (34)

1 [Ambush Commander](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAmbush%5D+%5BCommander%5D) 1 [Allosaurus Rider](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAllosaurus%5D+%5BRider%5D) 2 [Elvish Eulogist](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BEulogist%5D) 1 [Elvish Harbinger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BHarbinger%5D) 3 [Elvish Warrior](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BWarrior%5D) 2 [Gempalm Strider](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGempalm%5D+%5BStrider%5D) 1 [Heedless One](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeedless%5D+%5BOne%5D) 2 [Imperious Perfect](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImperious%5D+%5BPerfect%5D) 3 [Llanowar Elves](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLlanowar%5D+%5BElves%5D) 2 [Lys Alana Huntmaster](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BHuntmaster%5D) 1 [Stonewood Invoker](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStonewood%5D+%5BInvoker%5D) 1 [Sylvan Messenger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BMessenger%5D) 1 [Timberwatch Elf](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTimberwatch%5D+%5BElf%5D) 1 [Voice of the Woods](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoice%5D+%5Bof%5D+%5Bthe%5D+%5BWoods%5D) 2 [Wellwisher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWellwisher%5D) 1 [Wirewood Herald](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BHerald%5D) 1 [Wirewood Symbiote](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BSymbiote%5D) 2 [Wood Elves](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 1 [Wren's Run Vanquisher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWren%5D+%5BRun%5D+%5BVanquisher%5D) 1 [Elvish Promenade](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BPromenade%5D) 2 [Giant Growth](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Harmonize](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHarmonize%5D) 1 [Wildsize](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildsize%5D) 

##### Colorless (26)

19 [Forest](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 2 [Tranquil Thicket](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTranquil%5D+%5BThicket%5D) 1 [Wirewood Lodge](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BLodge%5D) 3 [Moonglove Extract](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoonglove%5D+%5BExtract%5D) 1 [Slate of Ancestry](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlate%5D+%5Bof%5D+%5BAncestry%5D) 

60 Cards 

##### 1 (8)

2 [Elvish Eulogist](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BEulogist%5D) 3 [Llanowar Elves](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLlanowar%5D+%5BElves%5D) 1 [Wirewood Symbiote](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BSymbiote%5D) 2 [Giant Growth](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 

##### 2 (10)

3 [Elvish Warrior](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BWarrior%5D) 2 [Gempalm Strider](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGempalm%5D+%5BStrider%5D) 1 [Stonewood Invoker](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStonewood%5D+%5BInvoker%5D) 2 [Wellwisher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWellwisher%5D) 1 [Wirewood Herald](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BHerald%5D) 1 [Wren's Run Vanquisher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWren%5D+%5BRun%5D+%5BVanquisher%5D) 

##### 3 (10)

1 [Elvish Harbinger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BHarbinger%5D) 2 [Imperious Perfect](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImperious%5D+%5BPerfect%5D) 1 [Timberwatch Elf](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTimberwatch%5D+%5BElf%5D) 2 [Wood Elves](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 1 [Wildsize](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildsize%5D) 3 [Moonglove Extract](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoonglove%5D+%5BExtract%5D) 

##### 4 (7)

1 [Heedless One](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeedless%5D+%5BOne%5D) 2 [Lys Alana Huntmaster](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BHuntmaster%5D) 1 [Sylvan Messenger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BMessenger%5D) 1 [Elvish Promenade](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BPromenade%5D) 1 [Harmonize](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHarmonize%5D) 1 [Slate of Ancestry](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlate%5D+%5Bof%5D+%5BAncestry%5D) 

##### 5 (2)

1 [Ambush Commander](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAmbush%5D+%5BCommander%5D) 1 [Voice of the Woods](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoice%5D+%5Bof%5D+%5Bthe%5D+%5BWoods%5D) 

##### 7 (1)

1 [Allosaurus Rider](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAllosaurus%5D+%5BRider%5D) 

38 Cards 

##### Common (44)

19 [Forest](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 2 [Tranquil Thicket](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTranquil%5D+%5BThicket%5D) 2 [Elvish Eulogist](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BEulogist%5D) 3 [Elvish Warrior](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BWarrior%5D) 3 [Llanowar Elves](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLlanowar%5D+%5BElves%5D) 2 [Lys Alana Huntmaster](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLys%5D+%5BAlana%5D+%5BHuntmaster%5D) 1 [Stonewood Invoker](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStonewood%5D+%5BInvoker%5D) 1 [Timberwatch Elf](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTimberwatch%5D+%5BElf%5D) 2 [Wellwisher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWellwisher%5D) 1 [Wirewood Herald](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BHerald%5D) 2 [Wood Elves](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 2 [Giant Growth](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 1 [Wildsize](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildsize%5D) 3 [Moonglove Extract](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoonglove%5D+%5BExtract%5D) 

##### Uncommon (9)

1 [Wirewood Lodge](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BLodge%5D) 1 [Elvish Harbinger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BHarbinger%5D) 2 [Gempalm Strider](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGempalm%5D+%5BStrider%5D) 1 [Heedless One](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeedless%5D+%5BOne%5D) 1 [Sylvan Messenger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvan%5D+%5BMessenger%5D) 1 [Wirewood Symbiote](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWirewood%5D+%5BSymbiote%5D) 1 [Wren's Run Vanquisher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWren%5D+%5BRun%5D+%5BVanquisher%5D) 1 [Elvish Promenade](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BPromenade%5D) 

##### Rare (7)

1 [Ambush Commander](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAmbush%5D+%5BCommander%5D) 1 [Allosaurus Rider](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAllosaurus%5D+%5BRider%5D) 2 [Imperious Perfect](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BImperious%5D+%5BPerfect%5D) 1 [Voice of the Woods](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoice%5D+%5Bof%5D+%5Bthe%5D+%5BWoods%5D) 1 [Harmonize](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHarmonize%5D) 1 [Slate of Ancestry](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlate%5D+%5Bof%5D+%5BAncestry%5D) 

60 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

[Deal Another Hand](https://web.archive.org/web/20120101000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Stonewood+Invoker)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lys+Alana+Huntmaster)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Llanowar+Elves)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Allosaurus+Rider)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ambush+Commander)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Elvish+Warrior)

a:28:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"19";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Tranquil Thicket";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Wirewood Lodge";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Ambush Commander";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Allosaurus Rider";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Elvish Eulogist";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Elvish Harbinger";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Elvish Warrior";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Gempalm Strider";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Heedless One";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Imperious Perfect";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Llanowar Elves";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Lys Alana Huntmaster";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Stonewood Invoker";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Sylvan Messenger";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Timberwatch Elf";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Voice of the Woods";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Wellwisher";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Wirewood Herald";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Wirewood Symbiote";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Wood Elves";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Wren's Run Vanquisher";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Elvish Promenade";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Giant Growth";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Harmonize";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Wildsize";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Moonglove Extract";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Slate of Ancestry";s:22:"field\_card\_image\_front";a:0:{}}}} 

#### 

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (30)

1 [Siege-Gang Commander](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSiege-Gang%5D+%5BCommander%5D) 1 [Akki Coalflinger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAkki%5D+%5BCoalflinger%5D) 1 [Clickslither](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClickslither%5D) 3 [Emberwilde Augur](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEmberwilde%5D+%5BAugur%5D) 1 [Flamewave Invoker](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamewave%5D+%5BInvoker%5D) 1 [Gempalm Incinerator](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGempalm%5D+%5BIncinerator%5D) 3 [Goblin Cohort](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BCohort%5D) 1 [Goblin Matron](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BMatron%5D) 1 [Goblin Ringleader](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BRingleader%5D) 1 [Goblin Sledder](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BSledder%5D) 1 [Goblin Warchief](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BWarchief%5D) 1 [Ib Halfheart, Goblin Tactician](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIb%5D+%5BHalfheart,%5D+%5BGoblin%5D+%5BTactician%5D) 1 [Mogg Fanatic](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMogg%5D+%5BFanatic%5D) 2 [Mogg War Marshal](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMogg%5D+%5BWar%5D+%5BMarshal%5D) 2 [Mudbutton Torchrunner](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMudbutton%5D+%5BTorchrunner%5D) 2 [Raging Goblin](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaging%5D+%5BGoblin%5D) 1 [Reckless One](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BReckless%5D+%5BOne%5D) 2 [Skirk Drill Sergeant](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BDrill%5D+%5BSergeant%5D) 1 [Skirk Fire Marshal](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BFire%5D+%5BMarshal%5D) 1 [Skirk Prospector](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BProspector%5D) 1 [Skirk Shaman](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BShaman%5D) 1 [Tar Pitcher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTar%5D+%5BPitcher%5D) 

##### Sorcery (1)

1 [Spitting Earth](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpitting%5D+%5BEarth%5D) 

##### Enchantment (2)

2 [Boggart Shenanigans](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoggart%5D+%5BShenanigans%5D) 

##### Land (24)

22 [Mountain](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Goblin Burrows](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BBurrows%5D) 1 [Forgotten Cave](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForgotten%5D+%5BCave%5D) 

##### Tribal instant (3)

3 [Tarfire](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTarfire%5D) 

60 Cards 

##### Red (36)

1 [Siege-Gang Commander](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSiege-Gang%5D+%5BCommander%5D) 1 [Akki Coalflinger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAkki%5D+%5BCoalflinger%5D) 1 [Clickslither](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClickslither%5D) 3 [Emberwilde Augur](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEmberwilde%5D+%5BAugur%5D) 1 [Flamewave Invoker](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamewave%5D+%5BInvoker%5D) 1 [Gempalm Incinerator](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGempalm%5D+%5BIncinerator%5D) 3 [Goblin Cohort](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BCohort%5D) 1 [Goblin Matron](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BMatron%5D) 1 [Goblin Ringleader](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BRingleader%5D) 1 [Goblin Sledder](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BSledder%5D) 1 [Goblin Warchief](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BWarchief%5D) 1 [Ib Halfheart, Goblin Tactician](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIb%5D+%5BHalfheart,%5D+%5BGoblin%5D+%5BTactician%5D) 1 [Mogg Fanatic](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMogg%5D+%5BFanatic%5D) 2 [Mogg War Marshal](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMogg%5D+%5BWar%5D+%5BMarshal%5D) 2 [Mudbutton Torchrunner](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMudbutton%5D+%5BTorchrunner%5D) 2 [Raging Goblin](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaging%5D+%5BGoblin%5D) 1 [Reckless One](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BReckless%5D+%5BOne%5D) 2 [Skirk Drill Sergeant](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BDrill%5D+%5BSergeant%5D) 1 [Skirk Fire Marshal](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BFire%5D+%5BMarshal%5D) 1 [Skirk Prospector](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BProspector%5D) 1 [Skirk Shaman](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BShaman%5D) 1 [Tar Pitcher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTar%5D+%5BPitcher%5D) 2 [Boggart Shenanigans](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoggart%5D+%5BShenanigans%5D) 1 [Spitting Earth](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpitting%5D+%5BEarth%5D) 3 [Tarfire](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTarfire%5D) 

##### Colorless (24)

22 [Mountain](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Goblin Burrows](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BBurrows%5D) 1 [Forgotten Cave](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForgotten%5D+%5BCave%5D) 

60 Cards 

##### 1 (11)

3 [Goblin Cohort](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BCohort%5D) 1 [Goblin Sledder](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BSledder%5D) 1 [Mogg Fanatic](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMogg%5D+%5BFanatic%5D) 2 [Raging Goblin](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaging%5D+%5BGoblin%5D) 1 [Skirk Prospector](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BProspector%5D) 3 [Tarfire](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTarfire%5D) 

##### 2 (8)

3 [Emberwilde Augur](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEmberwilde%5D+%5BAugur%5D) 2 [Mogg War Marshal](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMogg%5D+%5BWar%5D+%5BMarshal%5D) 2 [Skirk Drill Sergeant](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BDrill%5D+%5BSergeant%5D) 1 [Spitting Earth](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpitting%5D+%5BEarth%5D) 

##### 3 (10)

1 [Akki Coalflinger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAkki%5D+%5BCoalflinger%5D) 1 [Flamewave Invoker](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamewave%5D+%5BInvoker%5D) 1 [Gempalm Incinerator](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGempalm%5D+%5BIncinerator%5D) 1 [Goblin Matron](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BMatron%5D) 1 [Goblin Warchief](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BWarchief%5D) 2 [Mudbutton Torchrunner](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMudbutton%5D+%5BTorchrunner%5D) 1 [Skirk Shaman](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BShaman%5D) 2 [Boggart Shenanigans](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoggart%5D+%5BShenanigans%5D) 

##### 4 (5)

1 [Clickslither](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClickslither%5D) 1 [Goblin Ringleader](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BRingleader%5D) 1 [Ib Halfheart, Goblin Tactician](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIb%5D+%5BHalfheart,%5D+%5BGoblin%5D+%5BTactician%5D) 1 [Reckless One](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BReckless%5D+%5BOne%5D) 1 [Tar Pitcher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTar%5D+%5BPitcher%5D) 

##### 5 (2)

1 [Siege-Gang Commander](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSiege-Gang%5D+%5BCommander%5D) 1 [Skirk Fire Marshal](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BFire%5D+%5BMarshal%5D) 

36 Cards 

##### Common (45)

22 [Mountain](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Forgotten Cave](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForgotten%5D+%5BCave%5D) 3 [Emberwilde Augur](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEmberwilde%5D+%5BAugur%5D) 3 [Goblin Cohort](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BCohort%5D) 1 [Goblin Sledder](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BSledder%5D) 1 [Mogg Fanatic](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMogg%5D+%5BFanatic%5D) 2 [Mogg War Marshal](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMogg%5D+%5BWar%5D+%5BMarshal%5D) 2 [Mudbutton Torchrunner](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMudbutton%5D+%5BTorchrunner%5D) 2 [Raging Goblin](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaging%5D+%5BGoblin%5D) 2 [Skirk Drill Sergeant](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BDrill%5D+%5BSergeant%5D) 1 [Skirk Prospector](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BProspector%5D) 1 [Skirk Shaman](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BShaman%5D) 1 [Spitting Earth](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpitting%5D+%5BEarth%5D) 3 [Tarfire](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTarfire%5D) 

##### Uncommon (11)

1 [Goblin Burrows](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BBurrows%5D) 1 [Akki Coalflinger](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAkki%5D+%5BCoalflinger%5D) 1 [Flamewave Invoker](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamewave%5D+%5BInvoker%5D) 1 [Gempalm Incinerator](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGempalm%5D+%5BIncinerator%5D) 1 [Goblin Matron](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BMatron%5D) 1 [Goblin Ringleader](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BRingleader%5D) 1 [Goblin Warchief](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BWarchief%5D) 1 [Reckless One](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BReckless%5D+%5BOne%5D) 1 [Tar Pitcher](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTar%5D+%5BPitcher%5D) 2 [Boggart Shenanigans](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoggart%5D+%5BShenanigans%5D) 

##### Rare (4)

1 [Siege-Gang Commander](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSiege-Gang%5D+%5BCommander%5D) 1 [Clickslither](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClickslither%5D) 1 [Ib Halfheart, Goblin Tactician](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIb%5D+%5BHalfheart,%5D+%5BGoblin%5D+%5BTactician%5D) 1 [Skirk Fire Marshal](https://web.archive.org/web/20120101000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkirk%5D+%5BFire%5D+%5BMarshal%5D) 

60 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

[Deal Another Hand](https://web.archive.org/web/20120101000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mudbutton+Torchrunner)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Goblin+Warchief)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Raging+Goblin)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flamewave+Invoker)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mogg+Fanatic)

a:28:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"22";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Goblin Burrows";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Forgotten Cave";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Siege-Gang Commander";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Akki Coalflinger";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Clickslither";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Emberwilde Augur";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Flamewave Invoker";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Gempalm Incinerator";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Goblin Cohort";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Goblin Matron";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Goblin Ringleader";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Goblin Sledder";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Goblin Warchief";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:30:"Ib Halfheart, Goblin Tactician";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Mogg Fanatic";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Mogg War Marshal";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Mudbutton Torchrunner";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Raging Goblin";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Reckless One";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Skirk Drill Sergeant";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Skirk Fire Marshal";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Skirk Prospector";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Skirk Shaman";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Tar Pitcher";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Boggart Shenanigans";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Spitting Earth";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:14:"tribal instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Tarfire";s:22:"field\_card\_image\_front";a:0:{}}}} 

### Cross-Block Synergy: Elves

In R&D, "Cross-Block Synergy" helps a lot of cards get into files. The phrase refers to occasions when cards from different blocks create cool combos together, and we prize it highly. Like when treefolk lord Verdeloth the Ancient in *Time Spiral* combines awesomely with all the Treefolk creatures in *Lorwyn*. We definitely wanted to take advantage of our access to Extended's huge card pool by looking for opportunities to show how *Lorwyn*'s Elf and Goblin cards interact with old-school Elves and Goblins in some pretty cool ways.

**Imperious Perfect**  
 The more Elves you have, the more insane Wellwisher and Timberwatch Elf get. Imperious Perfect sure cranks out Elves in a hurry.

**Lys Alana Huntmaster**  
 Use Wirewood Symbiote to return Elves to your hand to play again and again to generate vast number of tokens.

 ![Elves vs. Goblins Sylvan Messenger](http://archive.wizards.com/magic/images/mtgcom/fcpics/features/432_SylvanMessenger.jpg) **Sylvan Messenger**  
 This one is my favorite. This very tribal Elf showed up in *Apocalypse*, a set which had nothing to do with tribal, in *Invasion* block, a block that had nothing to do with tribal. He's a cool card, with some fun hold-your-breath moments, but it was really hard for he and his Merfolk, Soldier, and Zombie buddies to find homes in decks, since there were so few rewards for playing tribal decks in that period. By combining this *Apocalypse* card with *Onslaught* and *Lorwyn* block buddies, it finally gets a chance to shine. And now it also fetches non-creature Elf cards like Elvish Promenade. Play an Elvish Harbinger first to make sure there's an Elf on top you can scoop up with you Sylvan Messenger for your top four cards.

**Slate of Ancestry**  
 Some Elf decks played the Slate because they could generate a lot of mana, a lot of creatures, and empty their hands very quickly. That was before Elf tokens existed. Watch the Slate go into overdrive.

**Wirewood Lodge**  
 In addition to untapping Wellwisher and Timberwatch Elf, now the Lodge untaps Imperious Perfect.

**Elvish Promenade**  
 If you play this tribal sorcery with Ambush Commander out, you had better have a *lot* of tokens ready.

**Cross-Block Synergy: Goblins**

**Goblin Matron**  
 Playing Goblin Matron for Tarfire is a classic example of cross-block synergy, and one of the examples on which "Tribal Instant – Goblin" was built.

 ![Elves vs. Goblins Goblin Ringleader](http://archive.wizards.com/magic/images/mtgcom/fcpics/features/432_GoblinRingleader.jpg) **Goblin Ringleader**  
 While Sylvan Messenger didn't get much attention the first time around, this guy definitely did. In addition to all the Goblin creatures this guy could always get, often reduced in cost by Goblin Warchief or Skirk Prospector, now the Ringleader also rustles up Tarfires and Boggart Shenanigans. I've seen this guy catch four Goblin spells multiple times, and the 5-for-1 card advantage is just filthy.

**Siege-Gang Commander, Goblin Sledder, and Tar Pitcher**  
 Each of these fellows can turn Goblins pretty directly into damage. Remember: Your initial creature rush of Goblin Cohorts only has to do about half the work. You can easily bomb the rest of the damage over the top with these sacrifice outlets. Goblin Cohort makes a good Goblin to sacrifice once you start running out of creature spells to play from the hand.

**Mogg War Marshal**  
 Getting three Goblins out of just two mana and one card makes this an insanely efficient fuel for all the "sacrifice a Goblin" effects. The Elves definitely envy this burst of creature generation.

**Mudbutton Torchrunner**  
 Having tons of manaless "sacrifice a Goblin" outlets means you can often activate this guy at will. He's perfect for offing those Lys-Alana Huntmasters or pesky Elvish Warriors. When you sacrifice this guy to Goblin Sledder you get two effects in one: It's the [*Lorwyn* Goblins and the Circle of Death](https://web.archive.org/web/20120101000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl5) meets Cross-Block Synergy.

**Skirk Drill Sergeant**  
 This guy leads to a lot of fun card flips. With all the "sacrifice a Goblin" costs around, it's easy to trigger this guy right when you have ![2 Mana](http://archive.wizards.com/images/Symbols/Symbol_2_mana.gif)![Red Mana](http://archive.wizards.com/images/Symbols/red_mana.gif) up. If you flip a free Goblin Warchief or Tar Pitcher, it's awesome. On my third turn, I once ran this into an enemy Gempalm Strider, had no other play that turn, and decided to pay the ![2 Mana](http://archive.wizards.com/images/Symbols/Symbol_2_mana.gif)![Red Mana](http://archive.wizards.com/images/Symbols/red_mana.gif) when the Drill Sergeant died. Fate shook my hand, and I put a free turn-three Siege-Gang Commander and three little buddies into play from the top of my deck. (I won!)

**Boggart Shenanigans**  
 It's fetchable by Goblin Ringleader, Skirk Drill Sergeant, and Goblin Matron. It works with Goblin Sledder to let you sacrifice five blocked Goblins to pump the unblocked Goblin and deal an additional 10 damage. But remember that while you're sacrificing all your other Goblins to trigger the Shenanigans, cards like Siege-Gang Commander and Goblin Sledder can also sacrifice the Shenanigans itself.

### On the Sidelines

For the Goblins, we specifically left out Sparksmith and Goblin Sharpshooter. In classic Elf vs. Goblin matchups, these two recurring-damage-sources are notorious for killing all the opposing Elves singlehandedly. Not fun. We liked Siege-Gang Commander and Tar Pitcher, because when they're killing the Elves off, at least they need to spend Goblins to do so, so the Elves are making some kind of progress. But Sparksmith and Goblin Sharpshooter are just too one-sided in the matchup.

For the Elves, we reluctantly left out Wirewood Pride, even though it's quite iconic and has great gameplay. The reason is that it reads like it would be a "Tribal Elf – Instant" if it came out in *Lorwyn*. But because it came out in *Onslaught* block, before "Tribal Instant – Elf" technology had been invented, it never got a subtype. We don't plan to errata any old non-creature cards to gain the tribal type and creature subtypes, because it would just be too hard for players to predict which spells had received errata and which had not. So it would just feel weird to have such an Elf-feeling spell in the deck not have the Elf subtype, not be fetchable with Wirewood Herald, and so on. Giant Growth and Wildsize provide enough combat tricks to keep the opponent guessing and keep combats surprising.

### Mirror Entities

One way we emphasized the duality of the conflict is by putting in a lot of mirrors between the two decks, where two cards share half their text, then differ on the second half. In a couple of cases, the card plays the same role in each deck, but in most of the cases the Elf version and the Goblin version end up doing pretty different things.

<table><tbody><tr><td><a>Ambush Commander</a></td>&#10;			<td><a>Siege-Gang Commander</a></td>&#10;		</tr><tr><td><a>Gempalm Strider</a></td>&#10;			<td><a>Gempalm Incinerator</a></td>&#10;		</tr><tr><td><a>Heedless One</a></td>&#10;			<td><a>Reckless One</a></td>&#10;		</tr><tr><td><a>Stonewood Invoker</a></td>&#10;			<td><a>Flamewave Invoker</a></td>&#10;		</tr><tr><td><a>Sylvan Messenger</a></td>&#10;			<td><a>Goblin Ringleader</a></td>&#10;		</tr><tr><td><a>Voice of the Woods</a></td>&#10;			<td><a>Skirk Fire Marshal</a></td>&#10;		</tr><tr><td><a>Wirewood Lodge</a></td>&#10;			<td><a>Goblin Burrows</a></td>&#10;		</tr></tbody></table>

### Battlefield Tips: Elves

 ![Wirewood_Herald](https://i.ormos.uk/f3/1d/f31d5dd363707d131a6531be6a1ee24fd48287f227c2ff6e18ee79c390f9319b.jpg)

*   The Elves have the advantage of long-term growth. Over time, Imperious Perfect, Lys-Alana Huntmaster and Voice of the Woods create a huge board advantage that the Goblins will not be able to overcome.

*   Toss in count-me effects like Wellwisher, Timberwatch Elf, and Heedless One, and your huge army will demoralize the puny Goblins, then demolish them.

*   Llanowar Elves and Wood Elves help you stay way ahead on mana, dropping your bombs faster than the Goblins can destroy them.

*   Wirewood Symbiote + Wood Elves is totally insane.

*   Elvish Warrior's three toughness is amazing against Team 2/1.

*   When you rumble onto the offense, if the Goblins set up a bunch of blocks, a cycled Gempalm Strider will smash them flat. If they don't set up enough blocks, a cycled Gempalm Strider will smash them dead.

*   Try to bait out enemy burn spells with random dudes, then play your key utility creatures like Wellwisher or Voice of the Woods later, so they will have a higher chance to survive.

*   You only have three removal spells, and you'll want to kill Tar Pitcher, Siege-Gang Commander and Goblin Warchief on sight. Conserve your removal carefully.

*   Elvish Eulogist is a surprisingly sick tutor target when you are low on life and worried about Goblins burning you out.

*   Have fun! (And think like an Elf!)

### Battlefield Tips: Goblins

*   Goblin Cohort and Mogg Fanatic can really get their beats on. If you can clear away early Elves with burn, these one-drops can stack up a lot of damage in a hurry.

*   Goblin Sledder makes it almost impossible for the Elves to set up favorable blocks early on. Sledder can spend Mogg War Marshal tokens to make Goblin Cohort beat up Elvish Warrior. Goblin Burrows, Ib Halfheart, and Tar Pitcher help you "trade up" your 1/1s for enemy 2/3s a little later.

*   If you get an active Tar Pitcher or Siege-Gang Commander, try to stack up combat damage before sacrificing your Goblins for burn effects. That lets you get double the killpower out of each of your Goblins.

*   ![Ib_halfheart_Goblin_Tactician](https://i.ormos.uk/90/a4/90a430b121c534f7d953e1832b13b6fdb84d4f4a4192e498ab86cd4d3f926d20.jpg)\*Between Sledder, Drill Sergeant, Tar Pitcher, Siege-Gang Commander, and Boggart Shenanigans, you can get tons of benefits every time one of your Goblins is about to die. Since Ringleader, Siege-Gang Commander, and Mogg War Marshal all make a lot of extra Goblins very efficiently, you'll have a lot of Goblin deaths from which to benefit.

*   You have a lot of burn, but not infinite. It's very tempting to Tarfire the enemy Stonewood Invoker on turn two so that you can attack with your Goblin Cohort and Raging Goblin. But if you do, and an enemy Wellwisher later survives long enough to activate a couple of times, the Wellwisher will erase all the damage you caused and then some. Sometimes it's right to burn away the random Elf and smash, and sometimes it's better to conserve the kill spells for later. This is your toughest decision.

*   Ib Halfheart, Goblin Tactician can make your tactics a lot easier. When you run out of spells, sac all your mountains to Ib, untap and attack with everybody! You've got to show you're braver than Ib. While he's a Halfheart, you can't afford to be. Don't sac "all but four mountains" in case you draw more spells. Sometimes you've got to go all-in. Likewise, after blockers are declared, sometimes Clickslither needs to eat your whole army and inflict 11 points of trample.

*   It's important to remember that you only need your weenie attackers to do half the work. Eventually the Elves will get too big to beat through. Direct damage to the head can do the rest. Emberwilde Augur and Flamewave Invoker easily transform from "Melee Mode" to "Artillery Mode." You can switch Tarfire, Mudbutton Torchrunner, Tar Pitcher and Siege-Gang Commander from the motto "I hate blockers!" to the slogan "I hate YOUR FACE!"

*   If you get the enemy life total low, and you get Boggart Shenanigans out, all you have to do is chump-block and chump-attack your way to victory. If your opponent has 3 life and three 7/7 Elemental tokens from Voice of the Woods, and you have Boggart Shenanigans, you can just send your 2 Raging Goblins and your Skirk Prospectors into the enemy 7/7s. You give them an impossible choice: death or death.

*   Always try keep your life total just above 10 and your opponent's life just below 10. Just as the Elves are starting to hit critical mass, you can just play Skirk Fire Marshal and suddenly win. Skirk Fire Marshal can also provide an unexpected wrath effect in the midgame. And in a real pinch, Skirk Fire Marshal can produce a sudden tie game.

*   Have fun! (And scheme like a Goblin!)

I had a lot of fun playing the matchup from both sides. We worked hard to pack a ton of awesome cards and extras into the box, and I hope you get the chance to get ahold of one and play the battle out!

<table><tbody><tr><td><img alt="Ambush Commander" src="http://archive.wizards.com/global/images/magic_expansion_elvesvsgoblins_famous2LargePic_en.jpg"></td>&#10;			<td><img alt="Siege-Gang Commander" src="http://archive.wizards.com/global/images/magic_expansion_elvesvsgoblins_famous1LargePic_en.jpg"></td>&#10;		</tr></tbody></table>
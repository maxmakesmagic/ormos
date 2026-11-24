---
id: 4m95kvgk
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/07-03-developing-an-answer
title: Developing an Answer
published: '2009-07-03'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: eriklauer
  name: Erik Lauer
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
    lang_detected: en
    capture_id: 720586
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
    captured_at: '2021-12-02 10:41:57+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
    lang_detected: en
    capture_id: 720586
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
    captured_at: '2021-12-02 10:41:57+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
    lang_detected: en
    capture_id: 720586
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
    captured_at: '2021-12-02 10:41:57+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
    lang_detected: en
    capture_id: 720586
    url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
    captured_at: '2021-12-02 10:41:57+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - 5bhrjz1v
  - pvrf4y3x
sources:
- document_id: 4m95kvgk
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
  lang: en
  template: drupal
  captured_at: '2021-12-02 10:41:57+00'
  capture_id: 720586
  wayback_url: https://web.archive.org/web/20211202104157id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
- document_id: 5bhrjz1v
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/45
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/45
  lang: en
  template: aspx
  captured_at: '2013-07-07 19:39:53+00'
  capture_id: 622980
  wayback_url: https://web.archive.org/web/20130707193953id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/45
- document_id: pvrf4y3x
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-03
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-03
  lang: en
  template: drupal
  captured_at: '2022-08-15 06:26:26+00'
  capture_id: 720589
  wayback_url: https://web.archive.org/web/20220815062626id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-03
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 4m95kvgk
  capture_id: 720586
  url: https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
  wayback_url: https://web.archive.org/web/20211202104157id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-answer-2009-07-01
  captured_at: '2021-12-02 10:41:57+00'
  template: drupal
  sha256: cc7dfbed75e4f6d340af84fcf5125f78a64108ac314d6f57d0bfa679ca643cb5
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 3
---
*Wait a minute (you might find yourself wondering), what’s a new article doing on the site today? Isn't Wizards out of the office for the Independence Day holiday? Indeed we are, but we couldn't take the day completely off—not when there are cards to preview! Below, developer Erik Lauer fills in for Tom LaPille (who was busy writing [this week's feature article](https://web.archive.org/web/20090703000000/https://magic.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/45)). Erik has a preview card for you, plus a brief look at how that card came to be. Enjoy!*

Kelly Digges  
 Daily MTG Editor, **magicthegathering.com**

The ***Magic** 2010* design team created an excellent set that captured the feel of **Magic**'s first card set, Alpha, and enriched it with years of experience in card design. The set has many cards that each give a translation of a single piece of fantasy into a viable **Magic** card. The development team balanced these cards, and the set as a whole, for a variety of play environments from Limited and casual play up to cutthroat competitive play.

![](http://wizards.com//mtg/images/daily/ld/ld45_2010.jpg)  

Sometimes the development team changed the sets in other ways. One day we were looking at reducing the wordiness of commons to make a greater contrast with some of the wordy rares. We had ten common vanilla creatures total, roughly two per color, and I asked Randy Buehler what he thought about that. Randy walked over to a framed set of the "Beta" card set we have on the wall, and we counted out: [Pearled Unicorn](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pearled+Unicorn), [Merfolk of the Pearl Trident](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+of+the+Pearl+Trident), [Mons's Goblin Raiders](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mons%27s+Goblin+Raiders), [Grey Ogre](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grey+Ogre), [Hurloon Minotaur](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hurloon+Minotaur), [Hill Giant](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hill+Giant), [Scathe Zombies](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scathe+Zombies), [Grizzly Bears](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears), [Ironroot Treefolk](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironroot+Treefolk), and [Craw Wurm](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Craw+Wurm). With a chuckle, Randy approved.

Today's preview card isn't one of those vanilla commons, but for a rare, it isn't very wordy either. Here it is:

![Great Sable Stag](http://wizards.com//mtg/images/tcg/products/magic2010/direc18apt_EN.jpg)  

You might wonder why we chose to print such a powerful hoser.

Blue-black decks have been powerful in Standard for years. At Worlds 2006 Guillaume Wafo-Tapa played Dralnu du Louvre with great success. After [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) was printed, lists such as this one from Frank Karsten became very popular.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Damnation)](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation)

  

#### Frank Karsten's Dralnu Control

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (6)

1 [Dralnu, Lich Lord](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDralnu,%5D+%5BLich%5D+%5BLord%5D) 1 [Skeletal Vampire](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BVampire%5D) 1 [Aeon Chronicler](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D) 3 [Teferi, Mage of Zhalfir](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D) 

##### Sorcery (3)

3 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 

##### Instant (25)

3 [Mana Leak](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Remand](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 2 [Repeal](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D) 4 [Rewind](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRewind%5D) 1 [Seize the Soul](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeize%5D+%5Bthe%5D+%5BSoul%5D) 2 [Cancel](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D) 1 [Careful Consideration](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D) 3 [Mystical Teachings](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D) 3 [Spell Snare](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 1 [Sudden Death](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D) 1 [Think Twice](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D) 

##### Land (26)

2 [Tolaria West](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTolaria%5D+%5BWest%5D) 2 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 1 [Urza's Factory](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D) 2 [Dimir Aqueduct](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BAqueduct%5D) 9 [Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 [Watery Grave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 4 [Dreadship Reef](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D) 

60 Cards 

##### Sideboard (15)

1 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 1 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 3 [Bottle Gnomes](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 2 [Persecute](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D) 3 [Tormod's Crypt](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTormod%5D+%5BCrypt%5D) 1 [Extirpate](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D) 1 [Grim Harvest](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHarvest%5D) 2 [Tendrils of Corruption](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D) 1 [Trickbind](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrickbind%5D) 

##### Blue (28)

1 [Aeon Chronicler](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D) 3 [Teferi, Mage of Zhalfir](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D) 3 [Mana Leak](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Remand](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 2 [Repeal](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D) 4 [Rewind](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRewind%5D) 2 [Cancel](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D) 1 [Careful Consideration](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D) 3 [Mystical Teachings](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D) 3 [Spell Snare](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 1 [Think Twice](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D) 1 [Trickbind](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrickbind%5D) 

##### Black (13)

1 [Skeletal Vampire](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BVampire%5D) 1 [Seize the Soul](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeize%5D+%5Bthe%5D+%5BSoul%5D) 4 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 1 [Sudden Death](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D) 2 [Persecute](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D) 1 [Extirpate](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D) 1 [Grim Harvest](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHarvest%5D) 2 [Tendrils of Corruption](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D) 

##### Multi colored (1)

1 [Dralnu, Lich Lord](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDralnu,%5D+%5BLich%5D+%5BLord%5D) 

##### Colorless (33)

2 [Tolaria West](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTolaria%5D+%5BWest%5D) 3 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 1 [Urza's Factory](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D) 2 [Dimir Aqueduct](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BAqueduct%5D) 9 [Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 [Watery Grave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 4 [Dreadship Reef](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D) 3 [Bottle Gnomes](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 3 [Tormod's Crypt](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTormod%5D+%5BCrypt%5D) 

75 Cards 

##### 1 (6)

2 [Repeal](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D) 3 [Spell Snare](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 1 [Extirpate](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D) 

##### 2 (10)

3 [Mana Leak](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Remand](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 1 [Think Twice](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D) 1 [Grim Harvest](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHarvest%5D) 1 [Trickbind](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrickbind%5D) 

##### 3 (6)

2 [Cancel](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D) 1 [Sudden Death](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D) 3 [Bottle Gnomes](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 

##### 4 (17)

4 [Rewind](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRewind%5D) 1 [Seize the Soul](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeize%5D+%5Bthe%5D+%5BSoul%5D) 1 [Careful Consideration](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D) 4 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 3 [Mystical Teachings](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D) 2 [Persecute](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D) 2 [Tendrils of Corruption](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D) 

##### 5 (5)

1 [Dralnu, Lich Lord](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDralnu,%5D+%5BLich%5D+%5BLord%5D) 1 [Aeon Chronicler](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D) 3 [Teferi, Mage of Zhalfir](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D) 

##### 6 (1)

1 [Skeletal Vampire](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BVampire%5D) 

45 Cards 

##### Common (29)

9 [Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 3 [Mana Leak](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Remand](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 2 [Repeal](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D) 2 [Cancel](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D) 1 [Think Twice](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D) 3 [Bottle Gnomes](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 1 [Grim Harvest](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHarvest%5D) 2 [Tendrils of Corruption](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D) 

##### Uncommon (22)

1 [Urza's Factory](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D) 2 [Dimir Aqueduct](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BAqueduct%5D) 4 [Dreadship Reef](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D) 4 [Rewind](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRewind%5D) 1 [Careful Consideration](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D) 3 [Mystical Teachings](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D) 3 [Spell Snare](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 1 [Sudden Death](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D) 3 [Tormod's Crypt](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTormod%5D+%5BCrypt%5D) 

##### Rare (17)

2 [Tolaria West](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTolaria%5D+%5BWest%5D) 3 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 4 [Watery Grave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatery%5D+%5BGrave%5D) 1 [Dralnu, Lich Lord](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDralnu,%5D+%5BLich%5D+%5BLord%5D) 1 [Skeletal Vampire](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkeletal%5D+%5BVampire%5D) 1 [Aeon Chronicler](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D) 1 [Seize the Soul](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeize%5D+%5Bthe%5D+%5BSoul%5D) 2 [Persecute](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D) 1 [Extirpate](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D) 1 [Trickbind](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrickbind%5D) 

##### Mythic (7)

3 [Teferi, Mage of Zhalfir](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D) 4 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tolaria+West)

[Deal Another Hand](https://web.archive.org/web/20090703000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Remand)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dreadship+Reef)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sudden+Death)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mystical+Teachings)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Watery+Grave)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

a:31:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Tolaria West";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:24:"Urborg, Tomb of Yawgmoth";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Urza's Factory";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Dimir Aqueduct";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Watery Grave";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Dreadship Reef";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Dralnu, Lich Lord";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Skeletal Vampire";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Aeon Chronicler";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Teferi, Mage of Zhalfir";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mana Leak";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Remand";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Repeal";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Rewind";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Seize the Soul";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Cancel";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Careful Consideration";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Damnation";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Mystical Teachings";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Spell Snare";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Sudden Death";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Think Twice";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Bottle Gnomes";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Persecute";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Tormod's Crypt";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Extirpate";s:22:"field\_card\_image\_front";a:0:{}}}i:28;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Grim Harvest";s:22:"field\_card\_image\_front";a:0:{}}}i:29;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Tendrils of Corruption";s:22:"field\_card\_image\_front";a:0:{}}}i:30;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Trickbind";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

At Worlds 2007, Kotaro Otsuka also has success with a blue-black deck, this time using evoke creatures alongside [Makeshift Mannequin](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makeshift+Mannequin) and [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command).

#### Kotaro Otsuka's Blue-Black Control

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (23)

4 [Epochrasite](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEpochrasite%5D) 4 [Mulldrifter](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D) 3 [Phyrexian Ironfoot](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BIronfoot%5D) 4 [Riftwing Cloudskate](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D) 4 [Shadowmage Infiltrator](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D) 4 [Shriekmaw](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShriekmaw%5D) 

##### Sorcery (2)

2 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 

##### Instant (7)

3 [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D) 4 [Makeshift Mannequin](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMakeshift%5D+%5BMannequin%5D) 

##### Artifact (4)

1 [Loxodon Warhammer](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BWarhammer%5D) 3 [Mind Stone](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D) 

##### Land (24)

4 [Faerie Conclave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D) 2 [Mouth of Ronom](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMouth%5D+%5Bof%5D+%5BRonom%5D) 4 [River of Tears](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiver%5D+%5Bof%5D+%5BTears%5D) 5 [Snow-Covered Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BIsland%5D) 4 [Snow-Covered Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BSwamp%5D) 4 [Underground River](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 1 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 

60 Cards 

##### Sideboard (15)

2 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 2 [Liliana Vess](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BVess%5D) 3 [Nameless Inversion](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D) 2 [Persuasion](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersuasion%5D) 2 [Pithing Needle](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 4 [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D) 

##### Blue (13)

4 [Mulldrifter](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D) 4 [Riftwing Cloudskate](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D) 3 [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D) 2 [Persuasion](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersuasion%5D) 

##### Black (21)

4 [Shriekmaw](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShriekmaw%5D) 4 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 4 [Makeshift Mannequin](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMakeshift%5D+%5BMannequin%5D) 2 [Liliana Vess](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BVess%5D) 3 [Nameless Inversion](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D) 4 [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D) 

##### Multi colored (4)

4 [Shadowmage Infiltrator](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D) 

##### Colorless (37)

4 [Faerie Conclave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D) 2 [Mouth of Ronom](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMouth%5D+%5Bof%5D+%5BRonom%5D) 4 [River of Tears](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiver%5D+%5Bof%5D+%5BTears%5D) 5 [Snow-Covered Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BIsland%5D) 4 [Snow-Covered Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BSwamp%5D) 4 [Underground River](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 1 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 4 [Epochrasite](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEpochrasite%5D) 3 [Phyrexian Ironfoot](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BIronfoot%5D) 1 [Loxodon Warhammer](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BWarhammer%5D) 3 [Mind Stone](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D) 2 [Pithing Needle](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 

75 Cards 

##### 1 (6)

2 [Pithing Needle](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 4 [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D) 

##### 2 (10)

4 [Epochrasite](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEpochrasite%5D) 3 [Mind Stone](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D) 3 [Nameless Inversion](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D) 

##### 3 (8)

3 [Phyrexian Ironfoot](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BIronfoot%5D) 4 [Shadowmage Infiltrator](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D) 1 [Loxodon Warhammer](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BWarhammer%5D) 

##### 4 (11)

3 [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D) 4 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 4 [Makeshift Mannequin](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMakeshift%5D+%5BMannequin%5D) 

##### 5 (16)

4 [Mulldrifter](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D) 4 [Riftwing Cloudskate](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D) 4 [Shriekmaw](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShriekmaw%5D) 2 [Liliana Vess](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BVess%5D) 2 [Persuasion](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersuasion%5D) 

51 Cards 

##### Common (15)

5 [Snow-Covered Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BIsland%5D) 4 [Snow-Covered Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BSwamp%5D) 3 [Mind Stone](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D) 3 [Nameless Inversion](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D) 

##### Uncommon (31)

4 [Faerie Conclave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D) 2 [Mouth of Ronom](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMouth%5D+%5Bof%5D+%5BRonom%5D) 4 [Mulldrifter](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D) 3 [Phyrexian Ironfoot](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BIronfoot%5D) 4 [Riftwing Cloudskate](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D) 4 [Shadowmage Infiltrator](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D) 4 [Shriekmaw](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShriekmaw%5D) 4 [Makeshift Mannequin](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMakeshift%5D+%5BMannequin%5D) 2 [Persuasion](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersuasion%5D) 

##### Rare (23)

4 [River of Tears](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiver%5D+%5Bof%5D+%5BTears%5D) 4 [Underground River](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 1 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 4 [Epochrasite](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEpochrasite%5D) 3 [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D) 1 [Loxodon Warhammer](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BWarhammer%5D) 2 [Pithing Needle](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 4 [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D) 

##### Mythic (6)

4 [Damnation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D) 2 [Liliana Vess](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BVess%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Faerie+Conclave)

[Deal Another Hand](https://web.archive.org/web/20090703000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Snow-Covered+Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shriekmaw)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Faerie+Conclave)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Underground+River)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shadowmage+Infiltrator)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shriekmaw)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cryptic+Command)

a:23:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Faerie Conclave";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Mouth of Ronom";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"River of Tears";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"5";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Snow-Covered Island";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Snow-Covered Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Underground River";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:24:"Urborg, Tomb of Yawgmoth";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Epochrasite";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Mulldrifter";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Phyrexian Ironfoot";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Riftwing Cloudskate";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Shadowmage Infiltrator";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Shriekmaw";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Cryptic Command";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Damnation";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Loxodon Warhammer";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Makeshift Mannequin";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Mind Stone";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Liliana Vess";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:14:"tribal instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Nameless Inversion";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Persuasion";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Pithing Needle";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Thoughtseize";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

At Worlds 2008, yet again blue-black decks were having a great deal of success. Five of the Top 8 players were playing Faeries including Antti Malin, the eventual world champion. 

#### Antti Malin's Blue-Black Faeries

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (12)

4 [Mistbind Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistbind%5D+%5BClique%5D) 2 [Sower of Temptation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D) 4 [Spellstutter Sprite](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpellstutter%5D+%5BSprite%5D) 2 [Vendilion Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVendilion%5D+%5BClique%5D) 

##### Sorcery (4)

4 [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D) 

##### Instant (15)

4 [Agony Warp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAgony%5D+%5BWarp%5D) 3 [Broken Ambitions](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBroken%5D+%5BAmbitions%5D) 4 [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D) 3 [Remove Soul](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemove%5D+%5BSoul%5D) 1 [Terror](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D) 

##### Enchantment (4)

4 [Bitterblossom](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBitterblossom%5D) 

##### Land (25)

1 [Faerie Conclave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D) 6 [Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Mutavault](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D) 4 [Secluded Glen](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSecluded%5D+%5BGlen%5D) 4 [Sunken Ruins](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D) 2 [Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 [Underground River](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 

60 Cards 

##### Sideboard (15)

1 [Sower of Temptation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D) 4 [Flashfreeze](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 2 [Glen Elendra Archmage](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BArchmage%5D) 4 [Infest](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInfest%5D) 2 [Jace Beleren](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 1 [Mind Shatter](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BShatter%5D) 1 [Ponder](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D) 

##### Blue (32)

4 [Mistbind Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistbind%5D+%5BClique%5D) 3 [Sower of Temptation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D) 4 [Spellstutter Sprite](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpellstutter%5D+%5BSprite%5D) 2 [Vendilion Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVendilion%5D+%5BClique%5D) 3 [Broken Ambitions](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBroken%5D+%5BAmbitions%5D) 4 [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D) 3 [Remove Soul](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemove%5D+%5BSoul%5D) 4 [Flashfreeze](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 2 [Glen Elendra Archmage](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BArchmage%5D) 2 [Jace Beleren](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 1 [Ponder](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D) 

##### Black (14)

4 [Bitterblossom](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBitterblossom%5D) 1 [Terror](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D) 4 [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D) 4 [Infest](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInfest%5D) 1 [Mind Shatter](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BShatter%5D) 

##### Multi colored (4)

4 [Agony Warp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAgony%5D+%5BWarp%5D) 

##### Colorless (25)

1 [Faerie Conclave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D) 6 [Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Mutavault](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D) 4 [Secluded Glen](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSecluded%5D+%5BGlen%5D) 4 [Sunken Ruins](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D) 2 [Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 [Underground River](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 

75 Cards 

##### 1 (8)

3 [Broken Ambitions](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBroken%5D+%5BAmbitions%5D) 4 [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D) 1 [Ponder](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D) 

##### 2 (21)

4 [Spellstutter Sprite](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpellstutter%5D+%5BSprite%5D) 4 [Agony Warp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAgony%5D+%5BWarp%5D) 4 [Bitterblossom](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBitterblossom%5D) 3 [Remove Soul](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemove%5D+%5BSoul%5D) 1 [Terror](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D) 4 [Flashfreeze](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 1 [Mind Shatter](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BShatter%5D) 

##### 3 (8)

2 [Vendilion Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVendilion%5D+%5BClique%5D) 4 [Infest](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInfest%5D) 2 [Jace Beleren](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 

##### 4 (13)

4 [Mistbind Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistbind%5D+%5BClique%5D) 3 [Sower of Temptation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D) 4 [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D) 2 [Glen Elendra Archmage](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BArchmage%5D) 

50 Cards 

##### Common (16)

6 [Island](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Swamp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 3 [Broken Ambitions](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBroken%5D+%5BAmbitions%5D) 3 [Remove Soul](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemove%5D+%5BSoul%5D) 1 [Terror](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerror%5D) 1 [Ponder](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPonder%5D) 

##### Uncommon (13)

1 [Faerie Conclave](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaerie%5D+%5BConclave%5D) 4 [Agony Warp](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAgony%5D+%5BWarp%5D) 4 [Flashfreeze](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 4 [Infest](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInfest%5D) 

##### Rare (34)

4 [Mutavault](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutavault%5D) 4 [Secluded Glen](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSecluded%5D+%5BGlen%5D) 4 [Underground River](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 4 [Mistbind Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistbind%5D+%5BClique%5D) 3 [Sower of Temptation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSower%5D+%5Bof%5D+%5BTemptation%5D) 4 [Spellstutter Sprite](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpellstutter%5D+%5BSprite%5D) 4 [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BCommand%5D) 4 [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThoughtseize%5D) 2 [Glen Elendra Archmage](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlen%5D+%5BElendra%5D+%5BArchmage%5D) 1 [Mind Shatter](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BShatter%5D) 

##### Mythic (12)

4 [Sunken Ruins](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BRuins%5D) 2 [Vendilion Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVendilion%5D+%5BClique%5D) 4 [Bitterblossom](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBitterblossom%5D) 2 [Jace Beleren](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Faerie+Conclave)

[Deal Another Hand](https://web.archive.org/web/20090703000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mistbind+Clique)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mutavault)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Broken+Ambitions)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vendilion+Clique)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Broken+Ambitions)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sower+of+Temptation)

a:24:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Faerie Conclave";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"6";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mutavault";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Secluded Glen";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Sunken Ruins";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Underground River";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Mistbind Clique";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Sower of Temptation";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Spellstutter Sprite";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Vendilion Clique";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Agony Warp";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Bitterblossom";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Broken Ambitions";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Cryptic Command";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Remove Soul";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Terror";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Thoughtseize";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Flashfreeze";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Glen Elendra Archmage";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Infest";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Jace Beleren";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Mind Shatter";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Ponder";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Standard currently has cards such as [Deathmark](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deathmark) and [Celestial Purge](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Celestial+Purge) to keep each allied-color pair from getting out of control. If blue-black decks are too strong, shouldn't green have a card that helps keep things in check? Not only did green have [Karplusan Strider](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karplusan+Strider), but it also got [Marshdrinker Giant](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marshdrinker+Giant). While these cards punish blue and black, they just haven't proven strong enough to keep things in check.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Celestial+Purge"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Celestial+Purge"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karplusan+Strider"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Karplusan+Strider"></a></div></div></td></tr></tbody></table>

Paladin *en*-Vec is a card that has helped white. The card doesn't completely shut down black-red decks, but it is a thorn in their side. The development team set out to make a green card that would do similar things. While many of the cards in ***Magic** 2010* are based on high fantasy, this is more of a nuts-and-bolts type card. The creative team breathed life into once we were done and created a fantasy concept based on a mythical stag, but that's not how we made the card.

![](http://wizards.com//mtg/images/daily/ld/ld45_mana.jpg)  

We started off with a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) creature with protection from blue and protection from black. We soon realized that if the card could be countered, it would not be particularly hard for the blue-black deck to deal with, so the card should have "can't be countered" as its third ability.

![](http://wizards.com//mtg/images/daily/ld/ld45_textBox.jpg)  

The next issue was the creature's toughness. We knew Faeries would still be a strong Standard deck, and that this card would need to be useful against them. [Volcanic Fallout](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout) is also useful against Faeries, so this card should work well in the same deck with Fallout. That means that the toughness must be at least 3. Since the card is supposed to have answers in other colors, we left the toughness at 3, making it vulnerable to [Lightning Bolt](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt).

Finally we had to decide on the creature's power. We determined that 2 power was not enough to seriously threaten the Faerie deck, while 3 power was sufficient. The result is powerful, but fair, and as a 3/3 for three mana, it's aesthetically pleasing too.

![](http://wizards.com//mtg/images/daily/ld/ld45_pt.jpg)  

We have Future Future League tournaments were we build decks in formats that will come out in the future. I decided to test the Stag by playing Faeries. It occurred to me that I could add another color, such as red for [Lightning Bolt](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt). However I wanted to see how a blue-black deck would work. I figured [Vendilion Clique](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vendilion+Clique) would frequently come out too slowly to take Great Sable Stag from my opponent's hand, so I played [Thoughtseize](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtseize). However, when my opponent was able to cast a Stag, I felt stepped on. I couldn't counter it, and there wasn't much I could do to it was it entered the battlefield. How unfair! Maybe I could race, possibly with a couple [Cryptic Command](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command)s to tap the Stag. The real hero was [Chameleon Colossus](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chameleon+Colossus), who held the fort against the Stag while my [Sower of Temptation](https://web.archive.org/web/20090703000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sower+of+Temptation) pecked away!

![](http://wizards.com//mtg/images/daily/ld/ld45_stagSplash.jpg)  

After playing against the Stag, I could tell it was powerful, but not too powerful. It was a bit more than a thorn in my side, but it wasn't enough to make any matchup hopeless. The Stag was filling its role, and we look forward to seeing it do the same out in the real world.

[![](https://i.ormos.uk/68/ec/68ec07851d2d15bbd56f585b153259cae53ded2aa093340e0d5ed77c51a5ebda.jpg)](https://web.archive.org/web/20090703000000/https://magic.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/prereleases)
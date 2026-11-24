---
id: 06wzz5cy
kind: article
lang: en
path: /en/articles/latestdevelopments/2006/05-26-standard-now-and-then
title: 'Standard: Now and Then'
published: '2006-05-26'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
    lang_detected: en
    capture_id: 734980
    url: https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
    captured_at: '2022-08-13 23:34:49+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
    lang_detected: en
    capture_id: 734980
    url: https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
    captured_at: '2022-08-13 23:34:49+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
    lang_detected: en
    capture_id: 734980
    url: https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
    captured_at: '2022-08-13 23:34:49+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
    lang_detected: en
    capture_id: 734980
    url: https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
    captured_at: '2022-08-13 23:34:49+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - 2fd50vg7
  - qmwyh0p2
sources:
- document_id: 06wzz5cy
  url: https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
  lang: en
  template: drupal
  captured_at: '2022-08-13 23:34:49+00'
  capture_id: 734980
  wayback_url: https://web.archive.org/web/20220813233449id_/https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
- document_id: 2fd50vg7
  url: https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26-0
  lang: en
  template: drupal
  captured_at: '2021-10-28 17:11:50+00'
  capture_id: 734981
  wayback_url: https://web.archive.org/web/20211028171150id_/https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26-0
- document_id: qmwyh0p2
  url: http://wizards.com/default.asp?x=mtgcom/daily/af120
  page_key: wizards.com/default.asp?x=mtgcom/daily/af120
  lang: en
  template: classic_asp
  captured_at: '2007-10-23 00:23:56+00'
  capture_id: 1926139
  wayback_url: https://web.archive.org/web/20071023002356id_/http://wizards.com/default.asp?x=mtgcom/daily/af120
- document_id: qmwyh0p2
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af120&=RSS-MTGCOM
  page_key: wizards.com/default.asp?=RSS-MTGCOM&x=mtgcom/daily/af120
  lang: en
  template: classic_asp
  captured_at: '2007-10-09 14:01:42+00'
  capture_id: 1260893
  wayback_url: https://web.archive.org/web/20071009140142id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af120&=RSS-MTGCOM
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 06wzz5cy
  capture_id: 734980
  url: https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
  wayback_url: https://web.archive.org/web/20220813233449id_/https://magic.wizards.com/en/articles/archive/latest-developments/standard-now-and-then-2006-05-26
  captured_at: '2022-08-13 23:34:49+00'
  template: drupal
  sha256: 46e342b885e3459c7cfba591956e1348a5b1ea40f8ab2b204d6fbfba7f89871e
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 7
---
Whenever a big Standard tournament like Regionals happens, I can't wait to see all the new decklists, as are most fans of the format. Of course, most people are trying to get an accurate read of what the metagame will look like going forward, but I'm interested in how R&D did with their own internal metagame a year ago.

Below I'm going to compare seven decks that finished highly (second or better) in Regionals this year with their vague analogues from the R&D labs—the “Future Future League”—of a year ago, when Guildpact and Dissension were in development.

A reminder about what we try to do as developers: The FFL wants to understand future metagames in a general sense. We want to know what colors are powerful and which are weak, how many cards each set looks to be contributing to the environment, and what we'll need to push in future sets to shake things up or balance them out. To that end, we build and play tons and tons of decks, of which the seven I chose are but a small sampling.

We generally come close to what ends up really happening a year later once the cards hit the streets. For example, we knew that Zoo and Gruul beats would be defining decks, but we never made a great “[Steam Vents](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steam+Vents)” deck at all—we couldn't tweak the numbers quite right, and didn't try the Urzatron in two-color builds. We had “Ghost Husk” pegged as a major player for the Orzhov, but couldn't get our [Early Harvest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Early+Harvest) combo decks to be consistent enough. In every case, *the decks that you took to Regionals were better than the decks we had internally*, so I wouldn't look to this column for much in the way of “tech” - instead look at it as a glimpse into the world of development. We walk a fine line—know too little, and the environment could be a train wreck; know too much and it feels hyper-engineered and “pre-built.”

I'll present the “real” deck first, and then follow it up with R&D's decklist pasted exactly as it appeared in our email folder where we collect competitive deck ideas during development. Our decklists are full of playtest names and shorthand, but they'll give you an accurate view of how we communicate with one another. I'll follow up each R&D deck with some notes explaining our card choices and how our decks influenced how cards were printed.

### 1) Ghost Husk

#### Brett Blackman

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (25)

1 [Eight-and-a-Half-Tails](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEight-and-a-Half-Tails%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 2 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 4 [Nantuko Husk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNantuko%5D+%5BHusk%5D) 3 [Ghost Council of Orzhova](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhost%5D+%5BCouncil%5D+%5Bof%5D+%5BOrzhova%5D) 4 [Dark Confidant](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BConfidant%5D) 4 [Plagued Rusalka](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlagued%5D+%5BRusalka%5D) 4 [Orzhov Pontiff](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BPontiff%5D) 

##### Sorcery (4)

4 [Castigate](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCastigate%5D) 

##### Instant (4)

4 [Mortify](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMortify%5D) 

##### Enchantment (4)

4 [Promise of Bunrei](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPromise%5D+%5Bof%5D+%5BBunrei%5D) 

##### Land (23)

6 [Swamp](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 5 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Orzhov Basilica](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BBasilica%5D) 4 [Caves of Koilos](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Godless Shrine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGodless%5D+%5BShrine%5D) 1 [Shizo, Death's Storehouse](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShizo,%5D+%5BDeath%5D+%5BStorehouse%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 

60 Cards 

##### Sideboard (15)

2 [Mindslicer](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMindslicer%5D) 2 [Pithing Needle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 3 [Cranial Extraction](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCranial%5D+%5BExtraction%5D) 2 [Wrath of God](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWrath%5D+%5Bof%5D+%5BGod%5D) 2 [Grave Pact](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrave%5D+%5BPact%5D) 4 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 

##### White (16)

1 [Eight-and-a-Half-Tails](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEight-and-a-Half-Tails%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 2 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 4 [Promise of Bunrei](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPromise%5D+%5Bof%5D+%5BBunrei%5D) 2 [Wrath of God](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWrath%5D+%5Bof%5D+%5BGod%5D) 4 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 

##### Black (19)

4 [Nantuko Husk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNantuko%5D+%5BHusk%5D) 4 [Dark Confidant](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BConfidant%5D) 4 [Plagued Rusalka](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlagued%5D+%5BRusalka%5D) 2 [Mindslicer](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMindslicer%5D) 3 [Cranial Extraction](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCranial%5D+%5BExtraction%5D) 2 [Grave Pact](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrave%5D+%5BPact%5D) 

##### Multi colored (15)

3 [Ghost Council of Orzhova](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhost%5D+%5BCouncil%5D+%5Bof%5D+%5BOrzhova%5D) 4 [Orzhov Pontiff](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BPontiff%5D) 4 [Mortify](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMortify%5D) 4 [Castigate](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCastigate%5D) 

##### Colorless (25)

6 [Swamp](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 5 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Orzhov Basilica](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BBasilica%5D) 4 [Caves of Koilos](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Godless Shrine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGodless%5D+%5BShrine%5D) 1 [Shizo, Death's Storehouse](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShizo,%5D+%5BDeath%5D+%5BStorehouse%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 2 [Pithing Needle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 

75 Cards 

##### 1 (9)

3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 4 [Plagued Rusalka](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlagued%5D+%5BRusalka%5D) 2 [Pithing Needle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 

##### 2 (15)

1 [Eight-and-a-Half-Tails](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEight-and-a-Half-Tails%5D) 2 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 4 [Dark Confidant](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BConfidant%5D) 4 [Castigate](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCastigate%5D) 4 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 

##### 3 (16)

4 [Nantuko Husk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNantuko%5D+%5BHusk%5D) 4 [Orzhov Pontiff](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BPontiff%5D) 4 [Mortify](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMortify%5D) 4 [Promise of Bunrei](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPromise%5D+%5Bof%5D+%5BBunrei%5D) 

##### 4 (12)

3 [Ghost Council of Orzhova](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhost%5D+%5BCouncil%5D+%5Bof%5D+%5BOrzhova%5D) 2 [Mindslicer](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMindslicer%5D) 3 [Cranial Extraction](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCranial%5D+%5BExtraction%5D) 2 [Wrath of God](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWrath%5D+%5Bof%5D+%5BGod%5D) 2 [Grave Pact](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrave%5D+%5BPact%5D) 

52 Cards 

##### Common (29)

6 [Swamp](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 5 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 4 [Nantuko Husk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNantuko%5D+%5BHusk%5D) 4 [Plagued Rusalka](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlagued%5D+%5BRusalka%5D) 4 [Mortify](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMortify%5D) 4 [Castigate](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCastigate%5D) 

##### Uncommon (6)

2 [Orzhov Basilica](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BBasilica%5D) 4 [Orzhov Pontiff](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BPontiff%5D) 

##### Rare (36)

4 [Caves of Koilos](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Godless Shrine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGodless%5D+%5BShrine%5D) 1 [Shizo, Death's Storehouse](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShizo,%5D+%5BDeath%5D+%5BStorehouse%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 1 [Eight-and-a-Half-Tails](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEight-and-a-Half-Tails%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 3 [Ghost Council of Orzhova](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhost%5D+%5BCouncil%5D+%5Bof%5D+%5BOrzhova%5D) 4 [Promise of Bunrei](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPromise%5D+%5Bof%5D+%5BBunrei%5D) 2 [Mindslicer](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMindslicer%5D) 2 [Pithing Needle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 3 [Cranial Extraction](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCranial%5D+%5BExtraction%5D) 2 [Wrath of God](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWrath%5D+%5Bof%5D+%5BGod%5D) 2 [Grave Pact](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrave%5D+%5BPact%5D) 4 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 

##### Mythic (4)

4 [Dark Confidant](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BConfidant%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)

[Deal Another Hand](https://web.archive.org/web/20060526000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Orzhov+Basilica)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kami+of+Ancient+Law)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Isamaru%2C+Hound+of+Konda)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dark+Confidant)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Godless+Shrine)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plagued+Rusalka)

a:24:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"6";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"5";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Orzhov Basilica";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Caves of Koilos";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Godless Shrine";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Shizo, Death's Storehouse";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Eiganjo Castle";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Eight-and-a-Half-Tails";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Isamaru, Hound of Konda";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Kami of Ancient Law";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Nantuko Husk";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:24:"Ghost Council of Orzhova";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Dark Confidant";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Plagued Rusalka";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Orzhov Pontiff";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Mortify";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Castigate";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Promise of Bunrei";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Mindslicer";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Pithing Needle";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";i:0;}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Cranial Extraction";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Wrath of God";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;}i:22;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Grave Pact";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";i:0;}i:23;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Shining Shoal";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}} 

“Ghost Husk”—Orzhov decks featuring [Nantuko Husk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Husk) and [Promise of Bunrei](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Promise+of+Bunrei)—were the big stars of Regionals. Many pundits call it the best deck because it is resilient, has good threat diversity, and can win out of nowhere.

Internally, our version of the deck was very good, winning a couple small tournaments. The following list features [Soul Warden](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Warden) as the one-drop of choice (over Isamaru) simply because the card is more “combo-riffic.”

**Wilt-Free Zone – FFL – Aaron Forsythe**

> 4 Jack Spicer  
>  4 Soul Warden  
>  4 Bob  
>  4 Hand of Cruelty  
>  1 Trent  
>  4 Pontiff  
>  4 Husk  
>  3 Ghost Council
> 
>  
> 
> 4 Jitte  
>  4 City of Kids
> 
>  
> 
> 1 Eiganjo  
>  1 Shizo  
>  4 Caves  
>  4 WB2  
>  6 Plains  
>  8 Swamp
> 
>  
> 
> SB  
>  4 Castigate  
>  3 Terashi's Grasp  
>  2 Shortfang  
>  2 Seize the Soul  
>  2 Darkblast  
>  2 Moratorium Stone

What's going on with that decklist:

![](http://media.wizards.com/legacy/global/images/mtgcom_daily_af120_picmain_en.jpg)  
*Some call her....Trent.*

1.   “Wilt-Free Zone” refers to the fact that this is an Orzhov deck without [Mortify](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify). The playtest names of [Putrefy](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrefy) and [Mortify](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify) were “Wither” and “Wilt” respectively, and this deck oddly didn't pack the latter. I believe my earlier attempts at this deck had Wilts instead of Jittes, as I figured I could handle opposing Jittes with all my sacrifice outlets. I ended up relenting and playing Jittes anyway. It's interesting to note that the real-world version of Ghost Husk played Mortifies but no Jittes.
2.   All the *Guildpact* Rusalkas had playtest names taken from the kids cartoon Xiaolin Showdown; Jack Spicer is [Plagued Rusalka](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plagued+Rusalka).
3.   Everyone should know that “Bob” is [Dark Confidant](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Confidant), named after Bob Maher, Jr. Bob's mana cost was changed from BB to 1B so that decks like this one would be enabled.
4.   “Trent” is [Teysa, Orzhov Scion](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teysa%2C+Orzhov+Scion). Her design name was “Trent, Goth Executioner.” I had no idea at the time that I was designing the card that was meant to be the *Guildpact* novel protagonist, which is why her abilities aren't a great match for her character.
5.   [Orzhov Pontiff](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Orzhov+Pontiff) was an interesting card in development. It took us a long time to come up with an ability we liked for it (his art was commissioned based on a previous ability that wouldn't fit on a card). We eventually came up with a 1WB 2/1 that had haunt and did *both* of the Pontiff's current abilities instead of being modal. He got taken down a couple notches and still ended up being a powerful card.
6.   The Ghost Council used to cost zero mana to activate. He was really dumb. The funny thing is that we left him that way for a long time.
7.   I had several versions of this deck that featured multiple copies of [Belfry Spirit](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Belfry+Spirit). Hence, the Spirit's mana cost was increased from 2WW to 3WW. As you can imagine, he was ridiculous at four mana.
8.   “City of Kids” is shorthand for [Promise of Bunrei](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Promise+of+Bunrei)'s playtest name—“City of Lost Children.” The City was one of development's pet cards; we expected it to show up a lot in Standard. Until recently, it never really delivered. And yes, I had to find out the hard way that creative and/or templating made the tokens colorless. That's why there's only one Teysa left in the deck.
9.   “WB2” is shorthand for “white-black dual land that costs me two life,” otherwise known as [Godless Shrine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Godless+Shrine). It is not [Orzhov Basilica](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Orzhov+Basilica).
10.  [Grave-Shell Scarab](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grave-Shell+Scarab), [Firemane Angel](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firemane+Angel), [Soulless Revival](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soulless+Revival), and [Life from the Loam](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Life+from+the+Loam) were all very heavily played internally, hence the [Moratorium Stone](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moratorium+Stone)s in the 'board.

### 2) Zoo

#### Caleb Parry

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (20)

3 [Burning-Tree Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning-Tree%5D+%5BShaman%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 4 [Kird Ape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKird%5D+%5BApe%5D) 3 [Savannah Lions](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSavannah%5D+%5BLions%5D) 4 [Watchwolf](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwolf%5D) 3 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 

##### Instant (10)

4 [Char](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChar%5D) 4 [Lightning Helix](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BHelix%5D) 2 [Bathe in Light](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBathe%5D+%5Bin%5D+%5BLight%5D) 

##### Artifact (3)

3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 

##### Enchantment (3)

3 [Seal of Fire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BFire%5D) 

##### Land (22)

4 [Stomping Ground](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStomping%5D+%5BGround%5D) 1 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 4 [Temple Garden](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5BGarden%5D) 1 [Karplusan Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKarplusan%5D+%5BForest%5D) 4 [Battlefield Forge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 4 [Sacred Foundry](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 2 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 1 [Brushland](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrushland%5D) 

58 Cards 

##### Sideboard (13)

1 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 1 [Bathe in Light](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBathe%5D+%5Bin%5D+%5BLight%5D) 2 [Giant Solifuge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BSolifuge%5D) 3 [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BHierarch%5D) 3 [Giant Growth](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 3 [Flames of the Blood Hand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlames%5D+%5Bof%5D+%5Bthe%5D+%5BBlood%5D+%5BHand%5D) 

##### White (13)

3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 3 [Savannah Lions](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSavannah%5D+%5BLions%5D) 4 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 3 [Bathe in Light](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBathe%5D+%5Bin%5D+%5BLight%5D) 

##### Red (14)

4 [Kird Ape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKird%5D+%5BApe%5D) 4 [Char](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChar%5D) 3 [Seal of Fire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BFire%5D) 3 [Flames of the Blood Hand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlames%5D+%5Bof%5D+%5Bthe%5D+%5BBlood%5D+%5BHand%5D) 

##### Green (3)

3 [Giant Growth](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 

##### Multi colored (16)

3 [Burning-Tree Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning-Tree%5D+%5BShaman%5D) 4 [Watchwolf](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwolf%5D) 4 [Lightning Helix](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BHelix%5D) 2 [Giant Solifuge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BSolifuge%5D) 3 [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BHierarch%5D) 

##### Colorless (25)

4 [Stomping Ground](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStomping%5D+%5BGround%5D) 1 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 4 [Temple Garden](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5BGarden%5D) 1 [Karplusan Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKarplusan%5D+%5BForest%5D) 4 [Battlefield Forge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 4 [Sacred Foundry](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 2 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 1 [Brushland](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrushland%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 

71 Cards 

##### 1 (16)

3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 4 [Kird Ape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKird%5D+%5BApe%5D) 3 [Savannah Lions](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSavannah%5D+%5BLions%5D) 3 [Seal of Fire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BFire%5D) 3 [Giant Growth](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 

##### 2 (18)

4 [Watchwolf](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwolf%5D) 4 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 4 [Lightning Helix](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BHelix%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 3 [Bathe in Light](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBathe%5D+%5Bin%5D+%5BLight%5D) 

##### 3 (10)

3 [Burning-Tree Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning-Tree%5D+%5BShaman%5D) 4 [Char](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChar%5D) 3 [Flames of the Blood Hand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlames%5D+%5Bof%5D+%5Bthe%5D+%5BBlood%5D+%5BHand%5D) 

##### 4 (5)

2 [Giant Solifuge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BSolifuge%5D) 3 [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BHierarch%5D) 

49 Cards 

##### Common (16)

1 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 2 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 3 [Savannah Lions](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSavannah%5D+%5BLions%5D) 4 [Kami of Ancient Law](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BAncient%5D+%5BLaw%5D) 3 [Seal of Fire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BFire%5D) 3 [Giant Growth](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BGrowth%5D) 

##### Uncommon (18)

4 [Kird Ape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKird%5D+%5BApe%5D) 4 [Watchwolf](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwolf%5D) 4 [Lightning Helix](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BHelix%5D) 3 [Bathe in Light](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBathe%5D+%5Bin%5D+%5BLight%5D) 3 [Flames of the Blood Hand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlames%5D+%5Bof%5D+%5Bthe%5D+%5BBlood%5D+%5BHand%5D) 

##### Rare (33)

4 [Stomping Ground](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStomping%5D+%5BGround%5D) 4 [Temple Garden](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5BGarden%5D) 1 [Karplusan Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKarplusan%5D+%5BForest%5D) 4 [Battlefield Forge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 4 [Sacred Foundry](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSacred%5D+%5BFoundry%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 1 [Brushland](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrushland%5D) 3 [Burning-Tree Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning-Tree%5D+%5BShaman%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 2 [Giant Solifuge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGiant%5D+%5BSolifuge%5D) 3 [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BHierarch%5D) 

##### Mythic (4)

4 [Char](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChar%5D) 

71 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Stomping+Ground)

[Deal Another Hand](https://web.archive.org/web/20060526000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Char)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning+Helix)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Seal+of+Fire)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Watchwolf)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bathe+in+Light)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kird+Ape)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Savannah+Lions)

a:24:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Stomping Ground";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Temple Garden";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Karplusan Forest";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Battlefield Forge";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Sacred Foundry";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Eiganjo Castle";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Brushland";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Burning-Tree Shaman";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Isamaru, Hound of Konda";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Kird Ape";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Savannah Lions";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Watchwolf";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Kami of Ancient Law";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:4:"Char";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Lightning Helix";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Umezawa's Jitte";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"3";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Bathe in Light";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Seal of Fire";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"3";}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Giant Solifuge";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Loxodon Hierarch";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:22;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Giant Growth";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}i:23;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:24:"Flames of the Blood Hand";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}} 

Zoo, popularized by Craig Jones at PT--Honolulu, seems to have outlasted “Heezy Street” (Gruul) as the beatdown deck of choice. With a fabulous suite of burn spells and a horde of super-efficient creatures, the deck can win blazingly fast.

Internally, lead developer Brian Schneider first put forth the idea that RGW beatdown had to be insane with *Guildpact*, even if the deck's mana did 14 damage to its controller. Paul Sottosanti built the “touchstone” version that we all used to bounce our other decks off of. If a deck couldn't hang with RGW, it probably wasn't a “real” deck.

**Three-Deuce – FFL – Paul Sottosanti**

> 4 Kird Ape  
>  4 Isamaru  
>  4 RG 3/3  
>  4 WG 3/3  
>  4 Jitte  
>  2 Baloth  
>  2 Kids  
>  4 Stone Rain  
>  4 Char  
>  4 Shambling City  
>  4 RG Land  
>  4 WG Land  
>  4 RW Land  
>  1 R Legend Land  
>  1 G Legend Land  
>  1 W Legend Land  
>  3 WG Pain  
>  2 RW Pain  
>  4 RG Pain  
>  ---  
>  3 Position  
>  4 Creeping Mold  
>  2 Naturalize  
>  3 Pink Bolt  
>  3 Terrarion

What's going on with that decklist:

1.  “RG 3/3” and “WG 3/3” are [Scab-Clan Mauler](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scab-Clan+Mauler) and [Watchwolf](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Watchwolf), obv.
2.  “Baloth” is [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Loxodon+Hierarch), also obv. Note that most of these cards had real names by this point, but we generally take the path of least effort when writing decklists.
3.  “Kids” is, again, [Promise of Bunrei](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Promise+of+Bunrei) (I told you we liked it), and “[Stone Rain](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain)” is, well, [Stone Rain](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain). Paul's version wasn't as burn-heavy as the successful real-world Zoo builds; instead, it was more of a fast, disruptive, three-color beatdown deck. (“Three-Deuce” was the name of a popular RGW Extended deck that packed efficient creatures and disruptive elements.)
4.  “Shambling City” was going to be the name of [Rumbling Slum](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rumbling+Slum) until someone reminded Matt Cavotta that there was already a card named [Shambling Shell](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Shell) in the block. The Slums only lasted a week or so in the deck before they were replaced with the faster “Christmas Ants,” now known as [Giant Solifuge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Solifuge).
5.  Why no [Burning-Tree Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning-Tree+Shaman)? Simple… it didn't exist yet. We created the Shaman relatively late in *Guildpact* development as a foil to some of *Kamigawa's* annoying hallmarks—[Sensei's Divining Top](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sensei%27s+Divining+Top), [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa%27s+Jitte), and Meloku. Later versions of this deck contained the Shaman.
6.  In the sideboard you'll see “Position” and “Pink Bolt.” The former is [Glare of Subdual](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glare+of+Subdual)—it has the name “Position” because it wasn't quite “[Opposition](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Opposition).” The latter is [Lightning Helix](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Helix), given this cute moniker because, well, red and white make pink.
7.  The [Terrarion](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terrarion)s in the board are part of the “I'm scared of [Blood Moon](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Moon)” package that Paul devised. The [Creeping Mold](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Creeping+Mold)s can up the number of LD spells to eight; we loved playing Karoos in the FFL and Paul frequently made us pay for it.

### 3) Graft

#### Michael S Catopano

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (25)

4 [Llanowar Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLlanowar%5D+%5BElves%5D) 4 [Vinelasher Kudzu](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVinelasher%5D+%5BKudzu%5D) 4 [Wood Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 4 [Cytoplast Root-Kin](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCytoplast%5D+%5BRoot-Kin%5D) 4 [Plaxcaster Frogling](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlaxcaster%5D+%5BFrogling%5D) 3 [Kodama of the North Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKodama%5D+%5Bof%5D+%5Bthe%5D+%5BNorth%5D+%5BTree%5D) 2 [Keiga, the Tide Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeiga,%5D+%5Bthe%5D+%5BTide%5D+%5BStar%5D) 

##### Instant (10)

4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 2 [Voidslime](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidslime%5D) 

##### Artifact (3)

3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 

##### Land (22)

4 [Breeding Pool](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 4 [Yavimaya Coast](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYavimaya%5D+%5BCoast%5D) 2 [Simic Growth Chamber](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BGrowth%5D+%5BChamber%5D) 1 [Novijen, Heart of Progress](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNovijen,%5D+%5BHeart%5D+%5Bof%5D+%5BProgress%5D) 6 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 5 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

60 Cards 

##### Sideboard (15)

2 [Voidslime](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidslime%5D) 4 [Spell Snare](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 3 [Plaxmanta](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlaxmanta%5D) 3 [Pithing Needle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 3 [Naturalize](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNaturalize%5D) 

##### Blue (17)

2 [Keiga, the Tide Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeiga,%5D+%5Bthe%5D+%5BTide%5D+%5BStar%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Spell Snare](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 3 [Plaxmanta](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlaxmanta%5D) 

##### Green (22)

4 [Llanowar Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLlanowar%5D+%5BElves%5D) 4 [Vinelasher Kudzu](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVinelasher%5D+%5BKudzu%5D) 4 [Wood Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 4 [Cytoplast Root-Kin](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCytoplast%5D+%5BRoot-Kin%5D) 3 [Kodama of the North Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKodama%5D+%5Bof%5D+%5Bthe%5D+%5BNorth%5D+%5BTree%5D) 3 [Naturalize](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNaturalize%5D) 

##### Multi colored (8)

4 [Plaxcaster Frogling](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlaxcaster%5D+%5BFrogling%5D) 4 [Voidslime](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidslime%5D) 

##### Colorless (28)

4 [Breeding Pool](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 4 [Yavimaya Coast](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYavimaya%5D+%5BCoast%5D) 2 [Simic Growth Chamber](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BGrowth%5D+%5BChamber%5D) 1 [Novijen, Heart of Progress](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNovijen,%5D+%5BHeart%5D+%5Bof%5D+%5BProgress%5D) 6 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 5 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 3 [Pithing Needle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 

75 Cards 

##### 1 (11)

4 [Llanowar Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLlanowar%5D+%5BElves%5D) 4 [Spell Snare](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 3 [Pithing Needle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 

##### 2 (21)

4 [Vinelasher Kudzu](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVinelasher%5D+%5BKudzu%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 3 [Plaxmanta](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlaxmanta%5D) 3 [Naturalize](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNaturalize%5D) 

##### 3 (12)

4 [Wood Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 4 [Plaxcaster Frogling](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlaxcaster%5D+%5BFrogling%5D) 4 [Voidslime](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidslime%5D) 

##### 4 (4)

4 [Cytoplast Root-Kin](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCytoplast%5D+%5BRoot-Kin%5D) 

##### 5 (3)

3 [Kodama of the North Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKodama%5D+%5Bof%5D+%5Bthe%5D+%5BNorth%5D+%5BTree%5D) 

##### 6 (2)

2 [Keiga, the Tide Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeiga,%5D+%5Bthe%5D+%5BTide%5D+%5BStar%5D) 

53 Cards 

##### Common (30)

6 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 5 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Llanowar Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLlanowar%5D+%5BElves%5D) 4 [Wood Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 3 [Naturalize](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNaturalize%5D) 

##### Uncommon (18)

2 [Simic Growth Chamber](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BGrowth%5D+%5BChamber%5D) 1 [Novijen, Heart of Progress](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNovijen,%5D+%5BHeart%5D+%5Bof%5D+%5BProgress%5D) 4 [Cytoplast Root-Kin](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCytoplast%5D+%5BRoot-Kin%5D) 4 [Plaxcaster Frogling](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlaxcaster%5D+%5BFrogling%5D) 4 [Spell Snare](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 3 [Plaxmanta](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlaxmanta%5D) 

##### Rare (27)

4 [Breeding Pool](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 4 [Yavimaya Coast](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYavimaya%5D+%5BCoast%5D) 4 [Vinelasher Kudzu](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVinelasher%5D+%5BKudzu%5D) 3 [Kodama of the North Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKodama%5D+%5Bof%5D+%5Bthe%5D+%5BNorth%5D+%5BTree%5D) 2 [Keiga, the Tide Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeiga,%5D+%5Bthe%5D+%5BTide%5D+%5BStar%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 4 [Voidslime](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidslime%5D) 3 [Pithing Needle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPithing%5D+%5BNeedle%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Breeding+Pool)

[Deal Another Hand](https://web.archive.org/web/20060526000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Llanowar+Elves)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Breeding+Pool)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vinelasher+Kudzu)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wood+Elves)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wood+Elves)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

a:21:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Breeding Pool";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Yavimaya Coast";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Simic Growth Chamber";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:26:"Novijen, Heart of Progress";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"6";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"5";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Llanowar Elves";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Vinelasher Kudzu";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Wood Elves";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Cytoplast Root-Kin";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Plaxcaster Frogling";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:24:"Kodama of the North Tree";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Keiga, the Tide Star";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Remand";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mana Leak";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Umezawa's Jitte";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"3";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Voidslime";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Spell Snare";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Plaxmanta";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Pithing Needle";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";i:0;}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Naturalize";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}} 

Some people call this deck “Critical Mass,” but because the (Gnarled) Mass has been removed for the new hotness—[Plaxcaster Frogling](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plaxcaster+Frogling)—I'll stick to the simpler moniker “Graft.”

Internally, we had doubts as to whether or not Simic creature decks would be competitive in *Dissension* Standard, as we figured [Wrath of God](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) was a great answer to every damage source the deck could muster. Of course, with ten counterspells to keep Wrath at bay, the deck turned out to be pretty darned good. Out versions were a little lighter on the counters… unless you're talking +1/+1 counters…

**Doubling Graft – FFL – Nate Heiss**

> 4 BOP  
>  4 Wood snake  
>  4 Troll  
>  4 Plaxcaster  
>  4 Shambler  
>  4 Scatter the Seeds  
>  4 Acorn Couatl  
>  4 Double Trouble  
>  4 Cytoshaping  
>  3 Instant 2/2 Kicker-untargetable-man  
>  4 U/G Karoo  
>  4 Tropical  
>  8 Forest  
>  5 Island

[![](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Patagia%20Viper)](https://web.archive.org/web/20060526000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Patagia%20Viper)  
*A.K.A Acorn Couatl*

What's going on with that decklist:

1.  “Wood Snake” was the design name for [Coiling Oracle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coiling+Oracle). It was a wanna-be [Sakura-Tribe Elder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder) (which was “Rampant Snake” here in development) with the size and stats of [Wood Sage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wood+Sage), a little-known card from *Tempest*.
2.  There are twelve graft creatures here—four [Plaxcaster Frogling](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plaxcaster+Frogling), four [Cytoplast Root-Kin](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cytoplast+Root-Kin) (which was “[Cytospawn Shambler](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cytospawn+Shambler)”), and four [Sporeback Troll](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sporeback+Troll). Say what? Ah, the Troll. The Troll originally cost just 1G, and at that cost, Nate was willing to put him in the “best two-mana creatures of all time” category. Combined with the Frogling, you could set up a board position where your creatures couldn't die in combat, and they couldn't be targeted outside of combat. (Frogling had an activation of 1 instead of 2 initially, which was incredibly frustrating to face.) We came to our senses eventually and swapped the costs on the Troll and [Aquastrand Spider](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aquastrand+Spider).
3.  Other playtest names: “Acorn Couatl” was [Patagia Viper](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Patagia+Viper), “Double Trouble” was [Doubling Season](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doubling+Season), and “Instant 2/2 Kicker-untargetable-man” was [Plaxmanta](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plaxmanta). “Tropical” is short for [Tropical Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tropical+Island), which is what we called [Breeding Pool](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Breeding+Pool).
4.  [Cytoshape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cytoshape), at various points in its life, was (a) two mana, and (b) uncommon. Its power made us change the former, and Mark Gottlieb made us change the latter, as the card presented too many rules problems to be considered simple, regardless of how easy to read the text was. In Nate's deck it plays a lot like [Terminate](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terminate)—when you 'Shape an opponent's guy into a graft creature, it becomes a 0/0 and dies.
5.  Wait a second… Where are the Jittes? The Melokus? Heck, the [Yavimaya Coast](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yavimaya+Coast)s? This is a block deck, built to test graft in the most un-diluted environment possible. This gives us a good sense of how powerful the deck and mechanic are going into the next block.

### 4) [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovescape)

#### Nick Eisel

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (26)

4 [Wood Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 4 [Sakura-Tribe Elder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSakura-Tribe%5D+%5BElder%5D) 4 [Birds of Paradise](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D) 4 [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BHierarch%5D) 3 [Grand Arbiter Augustin IV](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrand%5D+%5BArbiter%5D+%5BAugustin%5D+%5BIV%5D) 1 [Simic Sky Swallower](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BSky%5D+%5BSwallower%5D) 1 [Indrik Stomphowler](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIndrik%5D+%5BStomphowler%5D) 2 [Patron of the Kitsune](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPatron%5D+%5Bof%5D+%5Bthe%5D+%5BKitsune%5D) 3 [Selesnya Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BGuildmage%5D) 

##### Instant (4)

3 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 1 [Congregation at Dawn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCongregation%5D+%5Bat%5D+%5BDawn%5D) 

##### Enchantment (3)

1 [Glare of Subdual](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlare%5D+%5Bof%5D+%5BSubdual%5D) 2 [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDovescape%5D) 

##### Land (23)

4 [Temple Garden](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5BGarden%5D) 4 [Breeding Pool](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 3 [Vitu-Ghazi, the City-Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVitu-Ghazi,%5D+%5Bthe%5D+%5BCity-Tree%5D) 2 [Selesnya Sanctuary](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BSanctuary%5D) 1 [Simic Growth Chamber](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BGrowth%5D+%5BChamber%5D) 3 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 2 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Okina, Temple to the Grandfathers](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOkina,%5D+%5BTemple%5D+%5Bto%5D+%5Bthe%5D+%5BGrandfathers%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 1 [Brushland](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrushland%5D) 

##### Other (4)

4 Supply/Demand 

60 Cards 

##### Sideboard (15)

1 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 1 [Glare of Subdual](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlare%5D+%5Bof%5D+%5BSubdual%5D) 1 [Congregation at Dawn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCongregation%5D+%5Bat%5D+%5BDawn%5D) 1 [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDovescape%5D) 3 [Faith's Fetters](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaith%5D+%5BFetters%5D) 1 [Viridian Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BShaman%5D) 2 [Kodama of the North Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKodama%5D+%5Bof%5D+%5Bthe%5D+%5BNorth%5D+%5BTree%5D) 3 [Yosei, the Morning Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYosei,%5D+%5Bthe%5D+%5BMorning%5D+%5BStar%5D) 1 [Arashi, the Sky Asunder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArashi,%5D+%5Bthe%5D+%5BSky%5D+%5BAsunder%5D) 1 [Silklash Spider](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilklash%5D+%5BSpider%5D) 

##### White (12)

2 [Patron of the Kitsune](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPatron%5D+%5Bof%5D+%5Bthe%5D+%5BKitsune%5D) 4 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 3 [Faith's Fetters](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaith%5D+%5BFetters%5D) 3 [Yosei, the Morning Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYosei,%5D+%5Bthe%5D+%5BMorning%5D+%5BStar%5D) 

##### Green (18)

4 [Wood Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 4 [Sakura-Tribe Elder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSakura-Tribe%5D+%5BElder%5D) 4 [Birds of Paradise](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D) 1 [Indrik Stomphowler](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIndrik%5D+%5BStomphowler%5D) 1 [Viridian Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BShaman%5D) 2 [Kodama of the North Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKodama%5D+%5Bof%5D+%5Bthe%5D+%5BNorth%5D+%5BTree%5D) 1 [Arashi, the Sky Asunder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArashi,%5D+%5Bthe%5D+%5BSky%5D+%5BAsunder%5D) 1 [Silklash Spider](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilklash%5D+%5BSpider%5D) 

##### Multi colored (18)

4 [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BHierarch%5D) 3 [Grand Arbiter Augustin IV](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrand%5D+%5BArbiter%5D+%5BAugustin%5D+%5BIV%5D) 1 [Simic Sky Swallower](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BSky%5D+%5BSwallower%5D) 3 [Selesnya Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BGuildmage%5D) 2 [Glare of Subdual](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlare%5D+%5Bof%5D+%5BSubdual%5D) 2 [Congregation at Dawn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCongregation%5D+%5Bat%5D+%5BDawn%5D) 3 [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDovescape%5D) 

##### Colorless (27)

4 [Temple Garden](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5BGarden%5D) 4 [Breeding Pool](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 3 [Vitu-Ghazi, the City-Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVitu-Ghazi,%5D+%5Bthe%5D+%5BCity-Tree%5D) 2 [Selesnya Sanctuary](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BSanctuary%5D) 1 [Simic Growth Chamber](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BGrowth%5D+%5BChamber%5D) 3 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 2 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Okina, Temple to the Grandfathers](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOkina,%5D+%5BTemple%5D+%5Bto%5D+%5Bthe%5D+%5BGrandfathers%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 1 [Brushland](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrushland%5D) 4 Supply/Demand 

75 Cards 

##### 1 (4)

4 [Birds of Paradise](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D) 

##### 2 (11)

4 [Sakura-Tribe Elder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSakura-Tribe%5D+%5BElder%5D) 3 [Selesnya Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BGuildmage%5D) 4 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 

##### 3 (7)

4 [Wood Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 2 [Congregation at Dawn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCongregation%5D+%5Bat%5D+%5BDawn%5D) 1 [Viridian Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BShaman%5D) 

##### 4 (12)

4 [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BHierarch%5D) 3 [Grand Arbiter Augustin IV](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrand%5D+%5BArbiter%5D+%5BAugustin%5D+%5BIV%5D) 2 [Glare of Subdual](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlare%5D+%5Bof%5D+%5BSubdual%5D) 3 [Faith's Fetters](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaith%5D+%5BFetters%5D) 

##### 5 (5)

1 [Indrik Stomphowler](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIndrik%5D+%5BStomphowler%5D) 2 [Kodama of the North Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKodama%5D+%5Bof%5D+%5Bthe%5D+%5BNorth%5D+%5BTree%5D) 1 [Arashi, the Sky Asunder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArashi,%5D+%5Bthe%5D+%5BSky%5D+%5BAsunder%5D) 1 [Silklash Spider](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilklash%5D+%5BSpider%5D) 

##### 6 (8)

2 [Patron of the Kitsune](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPatron%5D+%5Bof%5D+%5Bthe%5D+%5BKitsune%5D) 3 [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDovescape%5D) 3 [Yosei, the Morning Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYosei,%5D+%5Bthe%5D+%5BMorning%5D+%5BStar%5D) 

##### 7 (1)

1 [Simic Sky Swallower](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BSky%5D+%5BSwallower%5D) 

48 Cards 

##### Common (18)

3 [Forest](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 2 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Wood Elves](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWood%5D+%5BElves%5D) 4 [Sakura-Tribe Elder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSakura-Tribe%5D+%5BElder%5D) 4 Supply/Demand 

##### Uncommon (16)

3 [Vitu-Ghazi, the City-Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVitu-Ghazi,%5D+%5Bthe%5D+%5BCity-Tree%5D) 2 [Selesnya Sanctuary](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BSanctuary%5D) 1 [Simic Growth Chamber](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BGrowth%5D+%5BChamber%5D) 1 [Indrik Stomphowler](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIndrik%5D+%5BStomphowler%5D) 3 [Selesnya Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BGuildmage%5D) 2 [Congregation at Dawn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCongregation%5D+%5Bat%5D+%5BDawn%5D) 3 [Faith's Fetters](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFaith%5D+%5BFetters%5D) 1 [Viridian Shaman](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BShaman%5D) 

##### Rare (41)

4 [Temple Garden](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5BGarden%5D) 4 [Breeding Pool](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBreeding%5D+%5BPool%5D) 1 [Okina, Temple to the Grandfathers](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOkina,%5D+%5BTemple%5D+%5Bto%5D+%5Bthe%5D+%5BGrandfathers%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 1 [Brushland](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrushland%5D) 4 [Birds of Paradise](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D) 4 [Loxodon Hierarch](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLoxodon%5D+%5BHierarch%5D) 3 [Grand Arbiter Augustin IV](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrand%5D+%5BArbiter%5D+%5BAugustin%5D+%5BIV%5D) 1 [Simic Sky Swallower](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSimic%5D+%5BSky%5D+%5BSwallower%5D) 2 [Patron of the Kitsune](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPatron%5D+%5Bof%5D+%5Bthe%5D+%5BKitsune%5D) 4 [Shining Shoal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShining%5D+%5BShoal%5D) 2 [Glare of Subdual](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlare%5D+%5Bof%5D+%5BSubdual%5D) 3 [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDovescape%5D) 2 [Kodama of the North Tree](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKodama%5D+%5Bof%5D+%5Bthe%5D+%5BNorth%5D+%5BTree%5D) 3 [Yosei, the Morning Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYosei,%5D+%5Bthe%5D+%5BMorning%5D+%5BStar%5D) 1 [Arashi, the Sky Asunder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArashi,%5D+%5Bthe%5D+%5BSky%5D+%5BAsunder%5D) 1 [Silklash Spider](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilklash%5D+%5BSpider%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+Garden)

[Deal Another Hand](https://web.archive.org/web/20060526000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dovescape)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wood+Elves)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vitu-Ghazi%2C+the+City-Tree)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Eiganjo+Castle)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Birds+of+Paradise)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Selesnya+Guildmage)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Birds+of+Paradise)

a:31:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Temple Garden";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Breeding Pool";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Vitu-Ghazi, the City-Tree";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Selesnya Sanctuary";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Simic Growth Chamber";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:33:"Okina, Temple to the Grandfathers";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Eiganjo Castle";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Brushland";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Wood Elves";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Sakura-Tribe Elder";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Birds of Paradise";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Loxodon Hierarch";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Grand Arbiter Augustin IV";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Simic Sky Swallower";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Indrik Stomphowler";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Patron of the Kitsune";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Selesnya Guildmage";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Shining Shoal";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Glare of Subdual";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";}i:22;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Congregation at Dawn";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:23;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Dovescape";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"2";}i:24;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":0:{}s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"4";}i:25;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Faith's Fetters";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";i:0;}i:26;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Viridian Shaman";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:27;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:24:"Kodama of the North Tree";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:28;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Yosei, the Morning Star";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:29;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Arashi, the Sky Asunder";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:30;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Silklash Spider";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}} 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dovescape)](https://web.archive.org/web/20060526000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovescape)

I love Nick's deck. Nick had a keen eye for Constructed back when we'd play against each other in tournaments around Pittsburgh (*Tempest* / *Urza's Saga* days), but in recent years he's shifted his attention almost totally to Limited play. So I don't know if he's the inventor of this wacky masterpiece, but it wouldn't surprise me if he was.

[Grand Arbiter Augustin IV](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grand+Arbiter+Augustin+IV) and [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovescape) are two cards that most people had a hard time nailing down. Was there a deck for them to go into? Do they spawn their own decks? Even here in R&D we could never quite find good homes for these cards, although we knew they were both very powerful. I'm glad that Nick found some place to feature both of them that looks like it works very well.

The following deck doesn't have all that much to do with Nick's deck, but it is an interesting concoction that was built to put [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovescape) through the wringer. It actually did fairly well for me.

**Spells Alive! – FFL – Aaron Forsythe**

> 4 Spells Alive!  
>  4 GW Guildmage  
>  4 Baloth  
>  4 Pontiff  
>  4 BoP  
>  4 Chord of Calling  
>  1 Tolsimir  
>  4 Mortify  
>  2 Trophy Hunter  
>  1 Nullmage Shepherd  
>  4 Scatter  
>  Land

What's going on with this decklist:

1.  This is another block deck.
2.  “Spells Alive!”, a.k.a. [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovescape), was five mana for a period of time. Many decks just scooped to the card, and those types of effects should be expensive.
3.  The goal here was to break the symmetry of [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovescape) in as many ways as possible. Blue didn't offer many ways to do that, so I went with green and black instead. Tolsimir and [Selesnya Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Selesnya+Guildmage) can make my doves bigger, and Pontiff and [Trophy Hunter](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trophy+Hunter) can kill my opponents'.
4.  [Chord of Calling](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chord+of+Calling) is ridiculous with [Dovescape](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dovescape) in play… you can pay X mana+creatures to get X+3 more doves.
5.  The “Land” included multiple copies of Vitu-Ghazi.

### 5) Owl

#### Alex Etzel

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (5)

3 [Kami of the Crescent Moon](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5Bthe%5D+%5BCrescent%5D+%5BMoon%5D) 2 [Walking Archive](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWalking%5D+%5BArchive%5D) 

##### Sorcery (12)

4 [Sleight of Hand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSleight%5D+%5Bof%5D+%5BHand%5D) 4 [Eye of Nowhere](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEye%5D+%5Bof%5D+%5BNowhere%5D) 4 [Exhaustion](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExhaustion%5D) 

##### Instant (13)

4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 2 [Evacuation](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEvacuation%5D) 4 [Boomerang](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoomerang%5D) 3 [Sudden Impact](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BImpact%5D) 

##### Artifact (8)

4 [Ebony Owl Netsuke](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEbony%5D+%5BOwl%5D+%5BNetsuke%5D) 4 [Howling Mine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHowling%5D+%5BMine%5D) 

##### Land (22)

10 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Mikokoro, Center of the Sea](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMikokoro,%5D+%5BCenter%5D+%5Bof%5D+%5Bthe%5D+%5BSea%5D) 4 [Steam Vents](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 4 [Shivan Reef](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 2 [Adarkar Wastes](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 

60 Cards 

##### Sideboard (15)

1 [Evacuation](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEvacuation%5D) 4 [Threads of Disloyalty](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThreads%5D+%5Bof%5D+%5BDisloyalty%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 2 [Magnivore](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagnivore%5D) 4 [Meloku the Clouded Mirror](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 

##### Blue (38)

3 [Kami of the Crescent Moon](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5Bthe%5D+%5BCrescent%5D+%5BMoon%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 3 [Evacuation](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEvacuation%5D) 4 [Sleight of Hand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSleight%5D+%5Bof%5D+%5BHand%5D) 4 [Eye of Nowhere](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEye%5D+%5Bof%5D+%5BNowhere%5D) 4 [Boomerang](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoomerang%5D) 4 [Exhaustion](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExhaustion%5D) 4 [Threads of Disloyalty](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThreads%5D+%5Bof%5D+%5BDisloyalty%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Meloku the Clouded Mirror](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 

##### Red (5)

3 [Sudden Impact](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BImpact%5D) 2 [Magnivore](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagnivore%5D) 

##### Colorless (32)

10 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Mikokoro, Center of the Sea](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMikokoro,%5D+%5BCenter%5D+%5Bof%5D+%5Bthe%5D+%5BSea%5D) 4 [Steam Vents](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 4 [Shivan Reef](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 2 [Adarkar Wastes](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 2 [Walking Archive](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWalking%5D+%5BArchive%5D) 4 [Ebony Owl Netsuke](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEbony%5D+%5BOwl%5D+%5BNetsuke%5D) 4 [Howling Mine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHowling%5D+%5BMine%5D) 

75 Cards 

##### 1 (4)

4 [Sleight of Hand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSleight%5D+%5Bof%5D+%5BHand%5D) 

##### 2 (27)

3 [Kami of the Crescent Moon](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5Bthe%5D+%5BCrescent%5D+%5BMoon%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Ebony Owl Netsuke](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEbony%5D+%5BOwl%5D+%5BNetsuke%5D) 4 [Howling Mine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHowling%5D+%5BMine%5D) 4 [Eye of Nowhere](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEye%5D+%5Bof%5D+%5BNowhere%5D) 4 [Boomerang](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoomerang%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 

##### 3 (10)

2 [Walking Archive](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWalking%5D+%5BArchive%5D) 4 [Exhaustion](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExhaustion%5D) 4 [Threads of Disloyalty](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThreads%5D+%5Bof%5D+%5BDisloyalty%5D) 

##### 4 (5)

3 [Sudden Impact](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BImpact%5D) 2 [Magnivore](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagnivore%5D) 

##### 5 (7)

3 [Evacuation](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEvacuation%5D) 4 [Meloku the Clouded Mirror](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 

53 Cards 

##### Common (34)

10 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Sleight of Hand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSleight%5D+%5Bof%5D+%5BHand%5D) 4 [Eye of Nowhere](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEye%5D+%5Bof%5D+%5BNowhere%5D) 4 [Boomerang](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoomerang%5D) 4 [Threads of Disloyalty](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThreads%5D+%5Bof%5D+%5BDisloyalty%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 

##### Uncommon (11)

4 [Ebony Owl Netsuke](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEbony%5D+%5BOwl%5D+%5BNetsuke%5D) 4 [Exhaustion](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExhaustion%5D) 3 [Sudden Impact](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BImpact%5D) 

##### Rare (30)

2 [Mikokoro, Center of the Sea](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMikokoro,%5D+%5BCenter%5D+%5Bof%5D+%5Bthe%5D+%5BSea%5D) 4 [Steam Vents](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 4 [Shivan Reef](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 2 [Adarkar Wastes](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 3 [Kami of the Crescent Moon](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5Bthe%5D+%5BCrescent%5D+%5BMoon%5D) 2 [Walking Archive](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWalking%5D+%5BArchive%5D) 3 [Evacuation](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEvacuation%5D) 4 [Howling Mine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHowling%5D+%5BMine%5D) 2 [Magnivore](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagnivore%5D) 4 [Meloku the Clouded Mirror](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

[Deal Another Hand](https://web.archive.org/web/20060526000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Walking+Archive)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Evacuation)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Steam+Vents)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Evacuation)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Exhaustion)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Remand)

a:20:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"10";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:27:"Mikokoro, Center of the Sea";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Steam Vents";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Shivan Reef";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Adarkar Wastes";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Kami of the Crescent Moon";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Walking Archive";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Remand";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Ebony Owl Netsuke";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Evacuation";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Howling Mine";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Sleight of Hand";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Eye of Nowhere";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Boomerang";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Exhaustion";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sudden Impact";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Threads of Disloyalty";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";i:0;}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mana Leak";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Magnivore";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Meloku the Clouded Mirror";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}} 

When I first saw “Owl” posted on a message board somewhere prior to Honolulu, I showed it to my coworkers and our reactions were generally the same: “This is really a deck?”

Internally, the closest we came was a goofy [Howling Mine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howling+Mine) Burn deck tossed together by Nate Heiss. It had the capability to catch other decks off guard, but I don't think we ever expected something like it to actually burst onto an unsuspecting metagame. I'm tempted to say we missed this deck internally, but to Nate's credit, I'll only call it a half-miss.

**Howling Butt – FFL – Nate Heiss**

> 1 10 at 10  
>  4 Lava Spike  
>  4 Gaze of Adamaro  
>  4 Frostling  
>  3 Adamaro  
>  4 Flames of the Blood Hand  
>  3 Kami of the Crescent Moon  
>  4 Cerebral Vortex  
>  4 Glacial Ray  
>  4 Volcanic Hammer  
>  4 Howling Mine  
>  4 Volcanic Island  
>  4 U/R Painland  
>  1 Mikokoro  
>  3 Island  
>  9 Mountain  
>  60
> 
> SB  
>  4 Pyroclasm  
>  4 Pithing Needle  
>  3 Blood Moon  
>  4 Geddon

What's going on with this deck:

1.  “Howling Butt” refers to [Kami of the Crescent Moon](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kami+of+the+Crescent+Moon), affectionately known as “The Butt.”
2.  This deck is clearly more focused on burn as opposed to full-hand tricks. After all, it doesn't even have [Ebony Owl Netsuke](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ebony+Owl+Netsuke), a card we didn't put much stock in for constructed play.
3.  “10 at 10” is [Hidetsugu's Second Rite](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hidetsugu%27s+Second+Rite). That Nate is full of wacky surprises.
4.  “Volcanic Island” is a nickname for [Steam Vents](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steam+Vents), and “Geddon” in the sideboard is [Thoughts of Ruin](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughts+of+Ruin).
5.  This deck was built to test [Cerebral Vortex](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cerebral+Vortex) during *Guildpact* development. The Vortex was a late add to the set when we had to kill a [Wheel of Fortune](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wheel+of+Fortune) variant.

### 6) Skies

#### Robert Cuvelier

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (29)

4 [Pride of the Clouds](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPride%5D+%5Bof%5D+%5Bthe%5D+%5BClouds%5D) 3 [Ninja of the Deep Hours](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNinja%5D+%5Bof%5D+%5Bthe%5D+%5BDeep%5D+%5BHours%5D) 4 [Azorius First-Wing](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BFirst-Wing%5D) 4 [Suntail Hawk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSuntail%5D+%5BHawk%5D) 4 [Lantern Kami](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLantern%5D+%5BKami%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 2 [Leonin Skyhunter](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeonin%5D+%5BSkyhunter%5D) 2 [Azorius Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BGuildmage%5D) 3 [Azorius Herald](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 

##### Instant (3)

3 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 

##### Artifact (3)

3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 

##### Enchantment (3)

3 [Glorious Anthem](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlorious%5D+%5BAnthem%5D) 

##### Land (22)

4 [Adarkar Wastes](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 4 [Hallowed Fountain](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHallowed%5D+%5BFountain%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 8 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

60 Cards 

##### Sideboard (15)

2 [Azorius Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BGuildmage%5D) 1 [Azorius Herald](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 4 [Condemn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCondemn%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Ghostway](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhostway%5D) 

##### White (28)

4 [Suntail Hawk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSuntail%5D+%5BHawk%5D) 4 [Lantern Kami](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLantern%5D+%5BKami%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 2 [Leonin Skyhunter](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeonin%5D+%5BSkyhunter%5D) 4 [Azorius Herald](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 3 [Glorious Anthem](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlorious%5D+%5BAnthem%5D) 4 [Condemn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCondemn%5D) 4 [Ghostway](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhostway%5D) 

##### Blue (10)

3 [Ninja of the Deep Hours](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNinja%5D+%5Bof%5D+%5Bthe%5D+%5BDeep%5D+%5BHours%5D) 3 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 

##### Multi colored (12)

4 [Pride of the Clouds](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPride%5D+%5Bof%5D+%5Bthe%5D+%5BClouds%5D) 4 [Azorius First-Wing](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BFirst-Wing%5D) 4 [Azorius Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BGuildmage%5D) 

##### Colorless (25)

4 [Adarkar Wastes](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 4 [Hallowed Fountain](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHallowed%5D+%5BFountain%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 8 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 

75 Cards 

##### 1 (15)

4 [Suntail Hawk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSuntail%5D+%5BHawk%5D) 4 [Lantern Kami](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLantern%5D+%5BKami%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 4 [Condemn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCondemn%5D) 

##### 2 (24)

4 [Pride of the Clouds](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPride%5D+%5Bof%5D+%5Bthe%5D+%5BClouds%5D) 4 [Azorius First-Wing](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BFirst-Wing%5D) 2 [Leonin Skyhunter](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeonin%5D+%5BSkyhunter%5D) 4 [Azorius Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BGuildmage%5D) 3 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 

##### 3 (11)

4 [Azorius Herald](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 3 [Glorious Anthem](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlorious%5D+%5BAnthem%5D) 4 [Ghostway](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhostway%5D) 

##### 4 (3)

3 [Ninja of the Deep Hours](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNinja%5D+%5Bof%5D+%5Bthe%5D+%5BDeep%5D+%5BHours%5D) 

53 Cards 

##### Common (34)

8 [Plains](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 3 [Ninja of the Deep Hours](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNinja%5D+%5Bof%5D+%5Bthe%5D+%5BDeep%5D+%5BHours%5D) 4 [Azorius First-Wing](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BFirst-Wing%5D) 4 [Suntail Hawk](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSuntail%5D+%5BHawk%5D) 4 [Lantern Kami](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLantern%5D+%5BKami%5D) 3 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 

##### Uncommon (14)

2 [Leonin Skyhunter](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLeonin%5D+%5BSkyhunter%5D) 4 [Azorius Guildmage](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BGuildmage%5D) 4 [Azorius Herald](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 4 [Condemn](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCondemn%5D) 

##### Rare (27)

4 [Adarkar Wastes](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 4 [Hallowed Fountain](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHallowed%5D+%5BFountain%5D) 1 [Eiganjo Castle](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEiganjo%5D+%5BCastle%5D) 4 [Pride of the Clouds](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPride%5D+%5Bof%5D+%5Bthe%5D+%5BClouds%5D) 3 [Isamaru, Hound of Konda](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 3 [Glorious Anthem](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlorious%5D+%5BAnthem%5D) 3 [Umezawa's Jitte](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUmezawa%5D+%5BJitte%5D) 4 [Ghostway](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhostway%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Adarkar+Wastes)

[Deal Another Hand](https://web.archive.org/web/20060526000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Guildmage)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lantern+Kami)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Herald)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Umezawa%27s+Jitte)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Guildmage)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Herald)

a:21:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Adarkar Wastes";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:30:"Minamo, School at Water's Edge";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Hallowed Fountain";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Eiganjo Castle";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"8";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Pride of the Clouds";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Ninja of the Deep Hours";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Azorius First-Wing";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Suntail Hawk";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Lantern Kami";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Isamaru, Hound of Konda";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Leonin Skyhunter";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Azorius Guildmage";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Azorius Herald";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Remand";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Glorious Anthem";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"3";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Umezawa's Jitte";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"3";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Condemn";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mana Leak";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Ghostway";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}} 

I'm really happy that this deck showed up. We figured Blue-White control would exist simply by virtue of us printing [Hallowed Fountain](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hallowed+Fountain), but we wanted to push another class of Azorius cards as well. Because the colors are 1-2 in flying, we figured a flying creature theme might work well. Looks like it did.

**Skies – FFL – Brian Schneider**

> 4 Pup  
>  4 Suntail Hawk  
>  4 Lantern Kami  
>  4 2/1 Flier  
>  4 Leonin Skyhunter  
>  4 Kami of Ancient Law  
>  2 U/W Guildmage (Ugh -- should be pro-black Bushido guy)  
>  2 Eight-and-a-Half-Tails  
>  4 Umezawa's Jitte  
>  4 Brainwave \*/\* Flier  
>  4 2/1 Unblockable gain 4 guy  
>  4 U/W  
>  4 U/W2  
>  4 Tendo Ice Bridge  
>  1 Eiganjo Castle  
>  7 Plains

What's going on with this deck:

1.  This was one of the first attempts at making Blue/White aggro. Our later versions were much better.
2.  Playtest names: “Pup” = Isamaru, “2/1 Flier” = [Mistral Charger](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistral+Charger), “Brainwave \*/\* Flier” = [Pride of the Clouds](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pride+of+the+Clouds), “2/1 Unblockable gain 4 guy” = [Azorius Herald](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Azorius+Herald). Brainwave was the original name of forecast.
3.  [Pride of the Clouds](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pride+of+the+Clouds) was three mana (1WU) for a long time, and its forecast ability was five mana (3WU). In an attempt to make a “hallmark” forecast card, both numbers were reduced.

### 7) [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildfire)

#### Tommy Ashton

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (5)

4 [Keiga, the Tide Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeiga,%5D+%5Bthe%5D+%5BTide%5D+%5BStar%5D) 1 [Meloku the Clouded Mirror](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 

##### Sorcery (14)

3 [Pyroclasm](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 3 [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildfire%5D) 4 [Compulsive Research](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCompulsive%5D+%5BResearch%5D) 2 [Tidings](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidings%5D) 2 [Demonfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonfire%5D) 

##### Instant (12)

4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Repeal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D) 

##### Artifact (6)

4 [Izzet Signet](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BSignet%5D) 2 [Dimir Signet](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BSignet%5D) 

##### Land (23)

4 [Urza's Tower](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BTower%5D) 4 [Urza's Power Plant](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BPower%5D+%5BPlant%5D) 4 [Urza's Mine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BMine%5D) 4 [Steam Vents](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 4 [Shivan Reef](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 2 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 

60 Cards 

##### Sideboard (15)

4 [Annex](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnex%5D) 4 [Threads of Disloyalty](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThreads%5D+%5Bof%5D+%5BDisloyalty%5D) 3 [Hinder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHinder%5D) 4 [Spell Snare](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 

##### Blue (38)

4 [Keiga, the Tide Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeiga,%5D+%5Bthe%5D+%5BTide%5D+%5BStar%5D) 1 [Meloku the Clouded Mirror](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Repeal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D) 4 [Compulsive Research](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCompulsive%5D+%5BResearch%5D) 2 [Tidings](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidings%5D) 4 [Annex](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnex%5D) 4 [Threads of Disloyalty](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThreads%5D+%5Bof%5D+%5BDisloyalty%5D) 3 [Hinder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHinder%5D) 4 [Spell Snare](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 

##### Red (8)

3 [Pyroclasm](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 3 [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildfire%5D) 2 [Demonfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonfire%5D) 

##### Colorless (29)

4 [Urza's Tower](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BTower%5D) 4 [Urza's Power Plant](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BPower%5D+%5BPlant%5D) 4 [Urza's Mine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BMine%5D) 4 [Steam Vents](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 4 [Shivan Reef](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 2 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 4 [Izzet Signet](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BSignet%5D) 2 [Dimir Signet](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BSignet%5D) 

75 Cards 

##### 1 (10)

4 [Repeal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D) 2 [Demonfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonfire%5D) 4 [Spell Snare](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 

##### 2 (17)

4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 3 [Pyroclasm](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 4 [Izzet Signet](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BSignet%5D) 2 [Dimir Signet](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BSignet%5D) 

##### 3 (11)

4 [Compulsive Research](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCompulsive%5D+%5BResearch%5D) 4 [Threads of Disloyalty](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThreads%5D+%5Bof%5D+%5BDisloyalty%5D) 3 [Hinder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHinder%5D) 

##### 4 (4)

4 [Annex](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnex%5D) 

##### 5 (3)

1 [Meloku the Clouded Mirror](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 2 [Tidings](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidings%5D) 

##### 6 (7)

4 [Keiga, the Tide Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeiga,%5D+%5Bthe%5D+%5BTide%5D+%5BStar%5D) 3 [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildfire%5D) 

52 Cards 

##### Common (40)

4 [Urza's Tower](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BTower%5D) 4 [Urza's Power Plant](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BPower%5D+%5BPlant%5D) 4 [Urza's Mine](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BMine%5D) 2 [Island](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Mana Leak](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Remand](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Repeal](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepeal%5D) 4 [Compulsive Research](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCompulsive%5D+%5BResearch%5D) 4 [Izzet Signet](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BSignet%5D) 2 [Dimir Signet](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BSignet%5D) 4 [Threads of Disloyalty](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThreads%5D+%5Bof%5D+%5BDisloyalty%5D) 

##### Uncommon (16)

3 [Pyroclasm](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 2 [Tidings](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidings%5D) 4 [Annex](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnnex%5D) 3 [Hinder](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHinder%5D) 4 [Spell Snare](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BSnare%5D) 

##### Rare (19)

4 [Steam Vents](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteam%5D+%5BVents%5D) 4 [Shivan Reef](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 4 [Keiga, the Tide Star](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeiga,%5D+%5Bthe%5D+%5BTide%5D+%5BStar%5D) 1 [Meloku the Clouded Mirror](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 3 [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWildfire%5D) 2 [Demonfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonfire%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Urza%27s+Tower)

[Deal Another Hand](https://web.archive.org/web/20060526000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Repeal)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Compulsive+Research)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Izzet+Signet)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Compulsive+Research)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Remand)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Keiga%2C+the+Tide+Star)

a:23:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Urza's Tower";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Urza's Power Plant";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Urza's Mine";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Steam Vents";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Shivan Reef";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:30:"Minamo, School at Water's Edge";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Keiga, the Tide Star";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Meloku the Clouded Mirror";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mana Leak";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Remand";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Repeal";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Pyroclasm";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"3";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Wildfire";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"3";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Compulsive Research";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Tidings";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Izzet Signet";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Dimir Signet";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Demonfire";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Annex";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";i:0;}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Threads of Disloyalty";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";i:0;}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Hinder";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}i:22;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Spell Snare";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}} 

[Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildfire) decks were a tough nut for us to crack. Historically, its power level has fluctuated between World Championship winning when it appeared in *Urza's Saga* to complete dud when it returned in *Seventh Edition*. When it came back in *Ninth Edition*, several decks that used it evolved, from Adrian Sullivan's Eminent Domain to Anton Jonsson's early [Magnivore](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magnivore) versions, to recent Urzaton versions like Tommy's here.

In R&D, we messed around with Red/Green [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildfire) for a long, long, time before Devin Low figured out how key [Annex](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annex) was to the deck.

**UWR [Annex](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annex)-[Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildfire) – FFL – Devin Low**

> 2 Mark of Eviction  
>  3 UR Signet  
>  3 RW Signet  
>  4 Ghostly Prison  
>  1 Copy Enchantment  
>  4 Annex  
>  4 Faith's Fetters  
>  2 Gifts Ungiven  
>  4 Dream Leash  
>  1 Meloku  
>  4 Confiscate  
>  1 Keiga  
>  1 Yosei  
>  1 Ryusei  
>  3 Wildfire  
>  38 spells
> 
> 22 lands  
>  3 RW Karoo  
>  3 UR Karoo  
>  3 RW Tapland  
>  3 UR Tapland  
>  4 UW Painland  
>  2 UR Painland  
>  2 RW Painland  
>  1 Plains  
>  1 Island

What's going on with this deck:

1.  [Ghostly Prison](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghostly+Prison) was a card we played a ton, yet never caught on all that much in the real world. It works amazingly well in combination with [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildfire) and [Annex](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annex), but perhaps that's overkill.
2.  [Copy Enchantment](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Copy+Enchantment) works really powerfully with [Dream Leash](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dream+Leash); it lets you steal untapped permanents.
3.  Most of our [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildfire) decks were Red/Green with [Rumbling Slum](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rumbling+Slum)s and Arashi in addition to Green acceleration. We certainly never had the Urzatron in a [Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildfire) deck. We did build a version of [Magnivore](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magnivore)-[Wildfire](https://web.archive.org/web/20060526000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildfire), which [you can see here](https://web.archive.org/web/20060526000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/arcana/788).

And there you have it. Not bad guesses on our part…granted, I'm only highlighting the decks that we came close on. There are plenty of decks I could show you that never caught on, and there are plenty of Regionals decks that we didn't predict. But that's all part of the fun!

### Last Week's Polls

Do you watch the following Discovery Channel shows?

<table><tbody><tr><td><b>Show</b></td>&#10;			<td><b>Yes</b></td>&#10;			<td><b>%</b></td>&#10;			<td><b>No</b></td>&#10;			<td><b>%</b></td>&#10;			<td><b>Total</b></td>&#10;		</tr><tr><td>Mythbusters</td>&#10;			<td>6249</td>&#10;			<td>76.9%</td>&#10;			<td>1873</td>&#10;			<td>23.1%</td>&#10;			<td>8122</td>&#10;		</tr><tr><td>Monster Garage</td>&#10;			<td>1262</td>&#10;			<td>22.2%</td>&#10;			<td>4421</td>&#10;			<td>77.8%</td>&#10;			<td>5683</td>&#10;		</tr><tr><td>American Chopper</td>&#10;			<td>1509</td>&#10;			<td>27.1%</td>&#10;			<td>4060</td>&#10;			<td>72.9%</td>&#10;			<td>5569</td>&#10;		</tr><tr><td>I Shouldn't Be Alive</td>&#10;			<td>774</td>&#10;			<td>14.3%</td>&#10;			<td>4654</td>&#10;			<td>85.7%</td>&#10;			<td>5428</td>&#10;		</tr><tr><td>Extreme Engineering</td>&#10;			<td>1929</td>&#10;			<td>29.9%</td>&#10;			<td>4522</td>&#10;			<td>70.1%</td>&#10;			<td>6451</td>&#10;		</tr></tbody></table>

Through a bit of market research, we found out that Discovery Channel was popular within the *Magic*-playing demographic—something we didn't anticipate. We were curious as to what programs on that channel were popular.
---
id: nwyp5q19
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/10-29-thing-of-many-decks
title: Thing of Many Decks
published: '2010-10-29'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
    lang_detected: en
    capture_id: 735372
    url: https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
    captured_at: '2021-10-25 08:53:37+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
    lang_detected: en
    capture_id: 735372
    url: https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
    captured_at: '2021-10-25 08:53:37+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
    lang_detected: en
    capture_id: 735372
    url: https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
    captured_at: '2021-10-25 08:53:37+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
    lang_detected: en
    capture_id: 735372
    url: https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
    captured_at: '2021-10-25 08:53:37+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - zmqvfyec
sources:
- document_id: nwyp5q19
  url: https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
  page_key: magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
  lang: en
  template: drupal
  captured_at: '2021-10-25 08:53:37+00'
  capture_id: 735372
  wayback_url: https://web.archive.org/web/20211025085337id_/https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
- document_id: nwyp5q19
  url: https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-29
  page_key: magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-29
  lang: en
  template: drupal
  captured_at: '2021-10-23 21:52:01+00'
  capture_id: 735373
  wayback_url: https://web.archive.org/web/20211023215201id_/https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-29
- document_id: zmqvfyec
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/114
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/114
  lang: en
  template: aspx
  captured_at: '2013-07-06 16:13:41+00'
  capture_id: 612844
  wayback_url: https://web.archive.org/web/20130706161341id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/114
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: nwyp5q19
  capture_id: 735372
  url: https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
  wayback_url: https://web.archive.org/web/20211025085337id_/https://magic.wizards.com/en/articles/archive/latest-developments/thing-many-decks-2010-10-28
  captured_at: '2021-10-25 08:53:37+00'
  template: drupal
  sha256: 07bb4b82303e07bda6492265d01c3e410697d4ff894f05e40e31632609806ab1
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 7
---
Making **Magic** is one of the most fun jobs I've had, but it can sometimes be lonely. We spend hours and hours working on cards, trying to sculpt environments and make **Magic** as fun as we can. We often have a good idea what will happen with cards before we make them, but in many ways we work inside an echo chamber. For us, there is a long delay between finishing work on a card set and seeing what the printed cards do in the real world. We love the feedback that we get from the audience, and waiting several months to get it can be frustrating.

As you might expect, some of the most fun we have from watching the real world happens soon after a set releases. When you do things that we expected to happen, we get to feel smart, which is fun. When you do things that we didn't expect to happen, we are surprised, and most of the time it's fun to see what happened. Occasionally you discover something that we didn't expect, and most of the time we're excited to see what you found. Sometimes there's something that we all thought was both strong and cool, and you don't collectively latch onto it, which can be sad. No matter what happens, though, it's fun and instructive for us to watch it.

I can't speak for other developers, but looking through tournament deck lists and results often triggers memories of developing the set in question. Today, I'll take a walk through some recent deck lists and tell some related stories.

First, we'll go to some **Magic Online** Daily Event Standard deck lists.

#### CruelAjani's Pyromancer Ascension

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (2)

2 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 

##### Sorcery (14)

2 [Call to Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCall%5D+%5Bto%5D+%5BMind%5D) 4 [Foresee](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForesee%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [See Beyond](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSee%5D+%5BBeyond%5D) 

##### Instant (17)

4 [Burst Lightning](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurst%5D+%5BLightning%5D) 2 [Deprive](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeprive%5D) 3 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 

##### Enchantment (4)

4 [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyromancer%5D+%5BAscension%5D) 

##### Land (23)

3 [Halimar Depths](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHalimar%5D+%5BDepths%5D) 9 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 

60 Cards 

##### Sideboard (15)

1 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 4 [Flashfreeze](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 1 [Frost Titan](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrost%5D+%5BTitan%5D) 3 [Negate](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D) 3 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 2 [Spell Pierce](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BPierce%5D) 1 [Wurmcoil Engine](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D) 

##### Blue (36)

2 [Call to Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCall%5D+%5Bto%5D+%5BMind%5D) 2 [Deprive](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeprive%5D) 4 [Foresee](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForesee%5D) 3 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 3 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [See Beyond](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSee%5D+%5BBeyond%5D) 4 [Flashfreeze](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 1 [Frost Titan](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrost%5D+%5BTitan%5D) 3 [Negate](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D) 2 [Spell Pierce](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BPierce%5D) 

##### Red (15)

4 [Burst Lightning](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurst%5D+%5BLightning%5D) 4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyromancer%5D+%5BAscension%5D) 3 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 

##### Colorless (24)

3 [Halimar Depths](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHalimar%5D+%5BDepths%5D) 9 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 1 [Wurmcoil Engine](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D) 

75 Cards 

##### 1 (14)

4 [Burst Lightning](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurst%5D+%5BLightning%5D) 4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 2 [Spell Pierce](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BPierce%5D) 

##### 2 (27)

2 [Deprive](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeprive%5D) 3 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyromancer%5D+%5BAscension%5D) 4 [See Beyond](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSee%5D+%5BBeyond%5D) 4 [Flashfreeze](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 3 [Negate](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D) 3 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 

##### 3 (5)

2 [Call to Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCall%5D+%5Bto%5D+%5BMind%5D) 3 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 

##### 4 (4)

4 [Foresee](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForesee%5D) 

##### 6 (2)

1 [Frost Titan](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrost%5D+%5BTitan%5D) 1 [Wurmcoil Engine](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D) 

52 Cards 

##### Common (44)

3 [Halimar Depths](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHalimar%5D+%5BDepths%5D) 9 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Burst Lightning](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurst%5D+%5BLightning%5D) 2 [Deprive](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDeprive%5D) 4 [Foresee](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForesee%5D) 3 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [See Beyond](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSee%5D+%5BBeyond%5D) 

##### Uncommon (12)

2 [Call to Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCall%5D+%5Bto%5D+%5BMind%5D) 4 [Flashfreeze](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 3 [Negate](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D) 3 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 

##### Rare (14)

4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyromancer%5D+%5BAscension%5D) 2 [Spell Pierce](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BPierce%5D) 

##### Mythic (5)

3 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 1 [Frost Titan](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrost%5D+%5BTitan%5D) 1 [Wurmcoil Engine](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Halimar+Depths)

[Deal Another Hand](https://web.archive.org/web/20101029000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Foresee)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Jace+Beleren)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=See+Beyond)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scalding+Tarn)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Call+to+Mind)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning+Bolt)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Preordain)

a:21:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Halimar Depths";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Scalding Tarn";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Burst Lightning";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Call to Mind";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Deprive";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Foresee";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Into the Roil";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Jace Beleren";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Lightning Bolt";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mana Leak";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Preordain";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Pyromancer Ascension";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"See Beyond";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Flashfreeze";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Frost Titan";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Negate";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Pyroclasm";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Spell Pierce";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Wurmcoil Engine";s:22:"field\_card\_image\_front";a:0:{}}}} 

  
![](http://media.wizards.com/images/magic/daily/ld/ld114_pyromancer.jpg)  

We did not think of the five *Zendikar* Ascensions as Constructed cards during development. We understood that [Luminarch Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Luminarch+Ascension) would likely show up as a sideboard card at some point, but our attempts to find [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyromancer+Ascension) and [Beastmaster Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beastmaster+Ascension)-based decks that were strong enough for Standard or Block Constructed did not succeed. I always thought that was too bad, as having a rare cycle of cards with a tight naming convention that has no Constructed-strong card in it is a great recipe for player disdain. "The Ascensions? Yeah, those all suck." On the other hand, one or two flag-bearer members of the cycle can save everything. For example, many players have positive associations with the cycle of [Oaths](https://web.archive.org/web/20101029000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;name=+%5Boath%5Damp;set=%5B%22Exodus%22%5D) in *Exodus* thanks to [Oath of Druids](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oath+of+Druids) and to a lesser extent [Oath of Ghouls](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oath+of+Ghouls) even though the other three didn't see much play.

![](http://media.wizards.com/images/magic/daily/ld/ld114_beastmaster.jpg)  

I was quite relieved, then, to see [Beastmaster Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beastmaster+Ascension) stake a strong claim to status as one of the strongest decks in *Zendikar* Block Constructed at Pro Tour–San Juan. I suspected at the time that we would be seeing more of [Beastmaster Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beastmaster+Ascension) in Standard after *Shards of Alara* block rotated out, and **Magic Online** results indicate that this is the case. I was even more relieved at U.S. Nationals this year to see [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyromancer+Ascension) become a real deck. Although [Beastmaster Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beastmaster+Ascension) is part of a relatively normal creature-based deck, [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyromancer+Ascension) is a deck so far off the normal Standard map that it feels like you're playing a totally different game. Although I don't want the "different game" to become the norm, I like that it's available in Standard if you're looking for that. It feels very similar in its role to the Seismic Assault / [Swans of Bryn Argoll](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swans+of+Bryn+Argoll) deck from a little over a year ago, and I'm glad that there's a deck out there that does that.

I found a further surprise when I was looking for [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyromancer+Ascension) decks:

#### PauloCabral\_Br's Pyromancer Ascension

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Sorcery (12)

1 [Call to Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCall%5D+%5Bto%5D+%5BMind%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [See Beyond](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSee%5D+%5BBeyond%5D) 3 [Treasure Hunt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTreasure%5D+%5BHunt%5D) 

##### Instant (22)

4 [Archive Trap](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArchive%5D+%5BTrap%5D) 4 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 2 [Ravenous Trap](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRavenous%5D+%5BTrap%5D) 4 [Trapmaker's Snare](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrapmaker%5D+%5BSnare%5D) 

##### Enchantment (4)

4 [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyromancer%5D+%5BAscension%5D) 

##### Land (22)

4 [Halimar Depths](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHalimar%5D+%5BDepths%5D) 7 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 

60 Cards 

##### Sideboard (15)

4 [Forked Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForked%5D+%5BBolt%5D) 4 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 4 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 3 [Spell Pierce](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BPierce%5D) 

##### Blue (35)

4 [Archive Trap](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArchive%5D+%5BTrap%5D) 1 [Call to Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCall%5D+%5Bto%5D+%5BMind%5D) 4 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [See Beyond](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSee%5D+%5BBeyond%5D) 4 [Trapmaker's Snare](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrapmaker%5D+%5BSnare%5D) 3 [Treasure Hunt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTreasure%5D+%5BHunt%5D) 4 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 3 [Spell Pierce](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BPierce%5D) 

##### Black (2)

2 [Ravenous Trap](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRavenous%5D+%5BTrap%5D) 

##### Red (16)

4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyromancer%5D+%5BAscension%5D) 4 [Forked Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForked%5D+%5BBolt%5D) 4 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 

##### Colorless (22)

4 [Halimar Depths](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHalimar%5D+%5BDepths%5D) 7 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 

75 Cards 

##### 1 (15)

4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [Forked Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForked%5D+%5BBolt%5D) 3 [Spell Pierce](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BPierce%5D) 

##### 2 (27)

4 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyromancer%5D+%5BAscension%5D) 4 [See Beyond](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSee%5D+%5BBeyond%5D) 4 [Trapmaker's Snare](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrapmaker%5D+%5BSnare%5D) 3 [Treasure Hunt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTreasure%5D+%5BHunt%5D) 4 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 

##### 3 (5)

1 [Call to Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCall%5D+%5Bto%5D+%5BMind%5D) 4 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 

##### 4 (2)

2 [Ravenous Trap](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRavenous%5D+%5BTrap%5D) 

##### 5 (4)

4 [Archive Trap](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArchive%5D+%5BTrap%5D) 

53 Cards 

##### Common (41)

4 [Halimar Depths](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHalimar%5D+%5BDepths%5D) 7 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [See Beyond](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSee%5D+%5BBeyond%5D) 3 [Treasure Hunt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTreasure%5D+%5BHunt%5D) 4 [Forked Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForked%5D+%5BBolt%5D) 

##### Uncommon (11)

1 [Call to Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCall%5D+%5Bto%5D+%5BMind%5D) 2 [Ravenous Trap](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRavenous%5D+%5BTrap%5D) 4 [Trapmaker's Snare](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrapmaker%5D+%5BSnare%5D) 4 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 

##### Rare (19)

4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 4 [Archive Trap](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArchive%5D+%5BTrap%5D) 4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Pyromancer Ascension](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyromancer%5D+%5BAscension%5D) 3 [Spell Pierce](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpell%5D+%5BPierce%5D) 

##### Mythic (4)

4 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Halimar+Depths)

[Deal Another Hand](https://web.archive.org/web/20101029000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning+Bolt)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=See+Beyond)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning+Bolt)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning+Bolt)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Preordain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Trapmaker%27s+Snare)

a:19:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Halimar Depths";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Scalding Tarn";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Archive Trap";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Call to Mind";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Into the Roil";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Lightning Bolt";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mana Leak";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Preordain";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Pyromancer Ascension";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Ravenous Trap";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"See Beyond";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Trapmaker's Snare";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Treasure Hunt";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Forked Bolt";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Jace Beleren";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Pyroclasm";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Spell Pierce";s:22:"field\_card\_image\_front";a:0:{}}}} 

  
![](http://media.wizards.com/images/magic/daily/ld/ld114_trapmaker.jpg)  

I won't claim that this list is a consistent tournament contender, as this is the only copy of anything like this I've seen yet. More than any other person internally, Ken Nagle loved Traps, and built several [Trapmaker's Snare](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trapmaker%27s+Snare)-based decks. I didn't expect that card to be a Constructed all-star, but I did want it to be attractive enough to build decks around in more casual arenas. We don't get much data about that, but when I see decks like this every once in a while doing well enough to get posted in the [Decks of the Week](https://web.archive.org/web/20101029000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?tag=activity), that's good enough for me to know that there are people out there having fun with this.

#### Christopher Reed's Vampires

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (29)

4 [Bloodghast](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodghast%5D) 4 [Bloodthrone Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodthrone%5D+%5BVampire%5D) 3 [Captivating Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaptivating%5D+%5BVampire%5D) 4 [Gatekeeper of Malakir](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGatekeeper%5D+%5Bof%5D+%5BMalakir%5D) 4 [Kalastria Highborn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKalastria%5D+%5BHighborn%5D) 3 [Vampire Hexmage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BHexmage%5D) 3 [Vampire Nighthawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BNighthawk%5D) 4 [Viscera Seer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViscera%5D+%5BSeer%5D) 

##### Sorcery (3)

3 [Sign in Blood](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSign%5D+%5Bin%5D+%5BBlood%5D) 

##### Artifact (6)

4 [Blade of the Bloodchief](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlade%5D+%5Bof%5D+%5Bthe%5D+%5BBloodchief%5D) 2 [Brittle Effigy](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrittle%5D+%5BEffigy%5D) 

##### Land (22)

2 [Bojuka Bog](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBojuka%5D+%5BBog%5D) 4 [Marsh Flats](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D) 10 [Swamp](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 4 [Verdant Catacombs](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVerdant%5D+%5BCatacombs%5D) 

60 Cards 

##### Sideboard (15)

1 [Captivating Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaptivating%5D+%5BVampire%5D) 1 [Vampire Hexmage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BHexmage%5D) 1 [Brittle Effigy](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrittle%5D+%5BEffigy%5D) 2 [Disfigure](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 2 [Doom Blade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDoom%5D+%5BBlade%5D) 4 [Duress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 2 [Malakir Bloodwitch](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMalakir%5D+%5BBloodwitch%5D) 2 [Memoricide](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemoricide%5D) 

##### Black (46)

4 [Bloodghast](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodghast%5D) 4 [Bloodthrone Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodthrone%5D+%5BVampire%5D) 4 [Captivating Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaptivating%5D+%5BVampire%5D) 4 [Gatekeeper of Malakir](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGatekeeper%5D+%5Bof%5D+%5BMalakir%5D) 4 [Kalastria Highborn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKalastria%5D+%5BHighborn%5D) 4 [Vampire Hexmage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BHexmage%5D) 3 [Vampire Nighthawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BNighthawk%5D) 4 [Viscera Seer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViscera%5D+%5BSeer%5D) 3 [Sign in Blood](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSign%5D+%5Bin%5D+%5BBlood%5D) 2 [Disfigure](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 2 [Doom Blade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDoom%5D+%5BBlade%5D) 4 [Duress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 2 [Malakir Bloodwitch](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMalakir%5D+%5BBloodwitch%5D) 2 [Memoricide](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemoricide%5D) 

##### Colorless (29)

2 [Bojuka Bog](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBojuka%5D+%5BBog%5D) 4 [Marsh Flats](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D) 10 [Swamp](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 4 [Verdant Catacombs](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVerdant%5D+%5BCatacombs%5D) 4 [Blade of the Bloodchief](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlade%5D+%5Bof%5D+%5Bthe%5D+%5BBloodchief%5D) 3 [Brittle Effigy](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrittle%5D+%5BEffigy%5D) 

75 Cards 

##### 1 (17)

4 [Viscera Seer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViscera%5D+%5BSeer%5D) 4 [Blade of the Bloodchief](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlade%5D+%5Bof%5D+%5Bthe%5D+%5BBloodchief%5D) 3 [Brittle Effigy](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrittle%5D+%5BEffigy%5D) 2 [Disfigure](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 4 [Duress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 

##### 2 (25)

4 [Bloodghast](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodghast%5D) 4 [Bloodthrone Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodthrone%5D+%5BVampire%5D) 4 [Gatekeeper of Malakir](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGatekeeper%5D+%5Bof%5D+%5BMalakir%5D) 4 [Kalastria Highborn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKalastria%5D+%5BHighborn%5D) 4 [Vampire Hexmage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BHexmage%5D) 3 [Sign in Blood](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSign%5D+%5Bin%5D+%5BBlood%5D) 2 [Doom Blade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDoom%5D+%5BBlade%5D) 

##### 3 (7)

4 [Captivating Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaptivating%5D+%5BVampire%5D) 3 [Vampire Nighthawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BNighthawk%5D) 

##### 4 (2)

2 [Memoricide](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemoricide%5D) 

##### 5 (2)

2 [Malakir Bloodwitch](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMalakir%5D+%5BBloodwitch%5D) 

53 Cards 

##### Common (28)

2 [Bojuka Bog](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBojuka%5D+%5BBog%5D) 10 [Swamp](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 [Bloodthrone Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodthrone%5D+%5BVampire%5D) 4 [Vampire Hexmage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BHexmage%5D) 4 [Viscera Seer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViscera%5D+%5BSeer%5D) 4 [Duress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 

##### Uncommon (9)

4 [Gatekeeper of Malakir](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGatekeeper%5D+%5Bof%5D+%5BMalakir%5D) 3 [Vampire Nighthawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BNighthawk%5D) 2 [Disfigure](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisfigure%5D) 

##### Rare (36)

4 [Marsh Flats](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D) 4 [Verdant Catacombs](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVerdant%5D+%5BCatacombs%5D) 4 [Bloodghast](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodghast%5D) 4 [Captivating Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaptivating%5D+%5BVampire%5D) 4 [Kalastria Highborn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKalastria%5D+%5BHighborn%5D) 4 [Blade of the Bloodchief](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlade%5D+%5Bof%5D+%5Bthe%5D+%5BBloodchief%5D) 3 [Brittle Effigy](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrittle%5D+%5BEffigy%5D) 3 [Sign in Blood](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSign%5D+%5Bin%5D+%5BBlood%5D) 2 [Doom Blade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDoom%5D+%5BBlade%5D) 2 [Malakir Bloodwitch](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMalakir%5D+%5BBloodwitch%5D) 2 [Memoricide](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemoricide%5D) 

##### Mythic (2)

2 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bojuka+Bog)

[Deal Another Hand](https://web.archive.org/web/20101029000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vampire+Hexmage)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bloodthrone+Vampire)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kalastria+Highborn)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Blade+of+the+Bloodchief)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Brittle+Effigy)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bloodghast)

a:21:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Bojuka Bog";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Marsh Flats";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"10";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Tectonic Edge";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Verdant Catacombs";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Bloodghast";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Bloodthrone Vampire";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Captivating Vampire";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Gatekeeper of Malakir";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Kalastria Highborn";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Vampire Hexmage";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Vampire Nighthawk";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Viscera Seer";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Blade of the Bloodchief";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Brittle Effigy";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sign in Blood";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Disfigure";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Doom Blade";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Duress";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Malakir Bloodwitch";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Memoricide";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

There are a lot of things going on here that make me happy.

I was part of the Vampire team for *Zendikar* development. [Blade of the Bloodchief](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blade+of+the+Bloodchief) evolved out of a card that we made, and I was always a little sad that a card that screamed "VAMPIRE!" so loudly was ignored by actual vampire decks. With [Viscera Seer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viscera+Seer) and [Bloodthrone Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodthrone+Vampire) though, it's good enough.

![](http://media.wizards.com/images/magic/daily/ld/ld114_3Cards1.jpg)  

[Captivating Vampire](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captivating+Vampire) is a totally sweet card to me. Mind control as a trope has been associated with vampires in many places, and **Magic** has a rough time with that because control effects are often blue. Here we managed to get that onto a Vampire, but it didn't show up in Standard immediately. With the rotation, though, he's good enough, and Vampire decks are playing enough Vampires to activate him. That's awesome.

![](http://media.wizards.com/images/magic/daily/ld/ld114_captivating.jpg)  

The details of this deck indicate that the answer cards we're putting in are good enough to be worth using. [Bojuka Bog](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bojuka+Bog), [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tectonic+Edge), [Vampire Hexmage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampire+Hexmage), [Duress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duress), [Memoricide](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memoricide), and [Brittle Effigy](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brittle+Effigy) were all built to let people solve weird problems in decks that might not otherwise be able to, and this deck contains all of them. That tells me that our cards are working.

I want to deviate from Constructed to talk for a moment about the following Limited deck, which Jason Hager drafted on the way to winning a Pro Tour Qualifier (and a trip to Paris) in Louisville earlier this season.

#### Jason Hager's Draft Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (14)

1 [Clone Shell](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D+%5BShell%5D) 1 [Dross Hopper](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDross%5D+%5BHopper%5D) 2 [Ferrovore](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFerrovore%5D) 1 [Fume Spitter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFume%5D+%5BSpitter%5D) 2 [Iron Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIron%5D+%5BMyr%5D) 2 [Moriok Replica](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoriok%5D+%5BReplica%5D) 1 [Necrogen Scudder](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNecrogen%5D+%5BScudder%5D) 1 [Oxidda Daredevil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidda%5D+%5BDaredevil%5D) 1 [Perilous Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPerilous%5D+%5BMyr%5D) 2 [Vulshok Replica](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BReplica%5D) 

##### Instant (3)

1 [Galvanic Blast](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalvanic%5D+%5BBlast%5D) 2 [Shatter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShatter%5D) 

##### Artifact (5)

1 [Heavy Arbalest](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeavy%5D+%5BArbalest%5D) 1 [Panic Spellbomb](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPanic%5D+%5BSpellbomb%5D) 1 [Rusted Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRusted%5D+%5BRelic%5D) 1 [Strider Harness](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrider%5D+%5BHarness%5D) 1 [Sylvok Lifestaff](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvok%5D+%5BLifestaff%5D) 

##### Enchantment (2)

2 [Furnace Celebration](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFurnace%5D+%5BCelebration%5D) 

##### Land (16)

9 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Swamp](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

40 Cards 

##### Sideboard (18)

2 [Goblin Gaveleer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BGaveleer%5D) 4 [Golden Urn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGolden%5D+%5BUrn%5D) 1 [Lumengrid Drake](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLumengrid%5D+%5BDrake%5D) 1 [Melt Terrain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMelt%5D+%5BTerrain%5D) 1 [Painful Quandary](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPainful%5D+%5BQuandary%5D) 1 [Riddlesmith](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiddlesmith%5D) 1 [Scoria Elemental](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScoria%5D+%5BElemental%5D) 1 [Scrapdiver Serpent](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrapdiver%5D+%5BSerpent%5D) 1 [Screeching Silcaw](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScreeching%5D+%5BSilcaw%5D) 1 [Sky-Eel School](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky-Eel%5D+%5BSchool%5D) 1 [Steel Hellkite](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5BHellkite%5D) 1 [Turn to Slag](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BSlag%5D) 1 [Wall of Tanglecord](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BTanglecord%5D) 1 [Whitesun's Passage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitesun%5D+%5BPassage%5D) 

##### White (1)

1 [Whitesun's Passage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitesun%5D+%5BPassage%5D) 

##### Blue (5)

1 [Lumengrid Drake](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLumengrid%5D+%5BDrake%5D) 1 [Riddlesmith](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiddlesmith%5D) 1 [Scrapdiver Serpent](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrapdiver%5D+%5BSerpent%5D) 1 [Screeching Silcaw](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScreeching%5D+%5BSilcaw%5D) 1 [Sky-Eel School](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky-Eel%5D+%5BSchool%5D) 

##### Black (4)

1 [Dross Hopper](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDross%5D+%5BHopper%5D) 1 [Fume Spitter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFume%5D+%5BSpitter%5D) 1 [Necrogen Scudder](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNecrogen%5D+%5BScudder%5D) 1 [Painful Quandary](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPainful%5D+%5BQuandary%5D) 

##### Red (13)

2 [Ferrovore](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFerrovore%5D) 1 [Oxidda Daredevil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidda%5D+%5BDaredevil%5D) 2 [Furnace Celebration](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFurnace%5D+%5BCelebration%5D) 1 [Galvanic Blast](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalvanic%5D+%5BBlast%5D) 2 [Shatter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShatter%5D) 2 [Goblin Gaveleer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BGaveleer%5D) 1 [Melt Terrain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMelt%5D+%5BTerrain%5D) 1 [Scoria Elemental](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScoria%5D+%5BElemental%5D) 1 [Turn to Slag](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BSlag%5D) 

##### Colorless (35)

9 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Swamp](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Clone Shell](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D+%5BShell%5D) 2 [Iron Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIron%5D+%5BMyr%5D) 2 [Moriok Replica](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoriok%5D+%5BReplica%5D) 1 [Perilous Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPerilous%5D+%5BMyr%5D) 2 [Vulshok Replica](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BReplica%5D) 1 [Heavy Arbalest](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeavy%5D+%5BArbalest%5D) 1 [Panic Spellbomb](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPanic%5D+%5BSpellbomb%5D) 1 [Rusted Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRusted%5D+%5BRelic%5D) 1 [Strider Harness](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrider%5D+%5BHarness%5D) 1 [Sylvok Lifestaff](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvok%5D+%5BLifestaff%5D) 4 [Golden Urn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGolden%5D+%5BUrn%5D) 1 [Steel Hellkite](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5BHellkite%5D) 1 [Wall of Tanglecord](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BTanglecord%5D) 

58 Cards 

##### 1 (10)

1 [Fume Spitter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFume%5D+%5BSpitter%5D) 1 [Galvanic Blast](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalvanic%5D+%5BBlast%5D) 1 [Panic Spellbomb](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPanic%5D+%5BSpellbomb%5D) 1 [Sylvok Lifestaff](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvok%5D+%5BLifestaff%5D) 2 [Goblin Gaveleer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BGaveleer%5D) 4 [Golden Urn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGolden%5D+%5BUrn%5D) 

##### 2 (11)

1 [Dross Hopper](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDross%5D+%5BHopper%5D) 2 [Iron Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIron%5D+%5BMyr%5D) 1 [Oxidda Daredevil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidda%5D+%5BDaredevil%5D) 1 [Perilous Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPerilous%5D+%5BMyr%5D) 2 [Shatter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShatter%5D) 1 [Riddlesmith](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiddlesmith%5D) 1 [Screeching Silcaw](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScreeching%5D+%5BSilcaw%5D) 1 [Wall of Tanglecord](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BTanglecord%5D) 1 [Whitesun's Passage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitesun%5D+%5BPassage%5D) 

##### 3 (11)

2 [Ferrovore](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFerrovore%5D) 2 [Moriok Replica](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoriok%5D+%5BReplica%5D) 1 [Necrogen Scudder](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNecrogen%5D+%5BScudder%5D) 2 [Vulshok Replica](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BReplica%5D) 2 [Furnace Celebration](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFurnace%5D+%5BCelebration%5D) 1 [Heavy Arbalest](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeavy%5D+%5BArbalest%5D) 1 [Strider Harness](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrider%5D+%5BHarness%5D) 

##### 4 (3)

1 [Rusted Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRusted%5D+%5BRelic%5D) 1 [Lumengrid Drake](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLumengrid%5D+%5BDrake%5D) 1 [Melt Terrain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMelt%5D+%5BTerrain%5D) 

##### 5 (5)

1 [Clone Shell](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D+%5BShell%5D) 1 [Painful Quandary](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPainful%5D+%5BQuandary%5D) 1 [Scoria Elemental](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScoria%5D+%5BElemental%5D) 1 [Sky-Eel School](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky-Eel%5D+%5BSchool%5D) 1 [Turn to Slag](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BSlag%5D) 

##### 6 (1)

1 [Steel Hellkite](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5BHellkite%5D) 

##### 7 (1)

1 [Scrapdiver Serpent](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrapdiver%5D+%5BSerpent%5D) 

42 Cards 

##### Common (50)

9 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 7 [Swamp](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 1 [Dross Hopper](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDross%5D+%5BHopper%5D) 2 [Ferrovore](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFerrovore%5D) 1 [Fume Spitter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFume%5D+%5BSpitter%5D) 2 [Iron Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIron%5D+%5BMyr%5D) 2 [Moriok Replica](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMoriok%5D+%5BReplica%5D) 1 [Oxidda Daredevil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidda%5D+%5BDaredevil%5D) 1 [Perilous Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPerilous%5D+%5BMyr%5D) 2 [Vulshok Replica](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BReplica%5D) 1 [Galvanic Blast](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalvanic%5D+%5BBlast%5D) 1 [Panic Spellbomb](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPanic%5D+%5BSpellbomb%5D) 1 [Rusted Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRusted%5D+%5BRelic%5D) 2 [Shatter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShatter%5D) 1 [Strider Harness](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrider%5D+%5BHarness%5D) 1 [Sylvok Lifestaff](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSylvok%5D+%5BLifestaff%5D) 2 [Goblin Gaveleer](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGoblin%5D+%5BGaveleer%5D) 4 [Golden Urn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGolden%5D+%5BUrn%5D) 1 [Lumengrid Drake](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLumengrid%5D+%5BDrake%5D) 1 [Melt Terrain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMelt%5D+%5BTerrain%5D) 1 [Scoria Elemental](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScoria%5D+%5BElemental%5D) 1 [Scrapdiver Serpent](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrapdiver%5D+%5BSerpent%5D) 1 [Screeching Silcaw](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScreeching%5D+%5BSilcaw%5D) 1 [Sky-Eel School](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky-Eel%5D+%5BSchool%5D) 1 [Turn to Slag](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTurn%5D+%5Bto%5D+%5BSlag%5D) 1 [Wall of Tanglecord](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BTanglecord%5D) 1 [Whitesun's Passage](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitesun%5D+%5BPassage%5D) 

##### Uncommon (6)

1 [Clone Shell](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D+%5BShell%5D) 1 [Necrogen Scudder](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNecrogen%5D+%5BScudder%5D) 2 [Furnace Celebration](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFurnace%5D+%5BCelebration%5D) 1 [Heavy Arbalest](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeavy%5D+%5BArbalest%5D) 1 [Riddlesmith](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiddlesmith%5D) 

##### Rare (2)

1 [Painful Quandary](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPainful%5D+%5BQuandary%5D) 1 [Steel Hellkite](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5BHellkite%5D) 

58 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

[Deal Another Hand](https://web.archive.org/web/20101029000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Galvanic+Blast)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Clone+Shell)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Oxidda+Daredevil)

a:34:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Clone Shell";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Dross Hopper";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Ferrovore";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Fume Spitter";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Iron Myr";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Moriok Replica";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Necrogen Scudder";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Oxidda Daredevil";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Perilous Myr";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Vulshok Replica";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Furnace Celebration";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Galvanic Blast";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Heavy Arbalest";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Panic Spellbomb";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Rusted Relic";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Shatter";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Strider Harness";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Sylvok Lifestaff";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Goblin Gaveleer";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Golden Urn";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Lumengrid Drake";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Melt Terrain";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Painful Quandary";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Riddlesmith";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Scoria Elemental";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Scrapdiver Serpent";s:22:"field\_card\_image\_front";a:0:{}}}i:28;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Screeching Silcaw";s:22:"field\_card\_image\_front";a:0:{}}}i:29;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Sky-Eel School";s:22:"field\_card\_image\_front";a:0:{}}}i:30;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Steel Hellkite";s:22:"field\_card\_image\_front";a:0:{}}}i:31;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Turn to Slag";s:22:"field\_card\_image\_front";a:0:{}}}i:32;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Wall of Tanglecord";s:22:"field\_card\_image\_front";a:0:{}}}i:33;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Whitesun's Passage";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

When *Scars of Mirrodin* was handed from Design to Development, there was a red theme of sacrificing your own stuff for benefit. This theme is still present in cards like [Barrage Ogre](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barrage+Ogre), [Kuldotha Rebirth](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kuldotha+Rebirth), and [Furnace Celebration](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Celebration), but there used to be much more. There were also cards that read "When you sacrifice CARDNAME, do something." We found that it wasn't particularly fun to have a huge mass of cards that asked you to throw your own cards away. We also discovered that to many players, there's not much difference between "When you sacrifice CARDNAME, do something," and "Sacrifice CARDNAME: do something," which internally caused the same sort of confusion that caused arguments to break out when I played **Magic** in grade school. 

![](http://media.wizards.com/images/magic/daily/ld/ld114_perilous.jpg)  

Rather than fight that confusion and general lack of appeal, we reduced the theme in number and changed some cards from "Whenever you sacrifice CARDNAME" to "Whenever CARDNAME is put into a graveyard from the battlefield." (That's where [Perilous Myr](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Perilous+Myr) came from, if I remember correctly.) However, we kept a few cards, like [Barrage Ogre](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barrage+Ogre) and [Furnace Celebration](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Celebration), so that the theme could come up in the right quantity. Mark Rosewater was sad that his theme was reduced in number; I was happy, but hoped that it would still show up enough to add texture. Both of us were happy when I was able to email him this Limited deck, as it shows that Mark's vision is still present at a high enough level to matter.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barrage+Ogre"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Barrage+Ogre"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Celebration"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Furnace+Celebration"></a></div></div></td></tr></tbody></table>

Let's go back to Constructed now.

#### Nomorecards's White Weenie

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (31)

4 [Glint Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlint%5D+%5BHawk%5D) 4 [Kor Duelist](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BDuelist%5D) 4 [Kor Outfitter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BOutfitter%5D) 4 [Kor Skyfisher](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BSkyfisher%5D) 4 [Memnite](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemnite%5D) 4 [Ornithopter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrnithopter%5D) 3 [Squadron Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSquadron%5D+%5BHawk%5D) 4 [Stoneforge Mystic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStoneforge%5D+%5BMystic%5D) 

##### Artifact (4)

2 [Argentum Armor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArgentum%5D+%5BArmor%5D) 1 [Basilisk Collar](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBasilisk%5D+%5BCollar%5D) 1 [Sword of Body and Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BBody%5D+%5Band%5D+%5BMind%5D) 

##### Enchantment (4)

4 [Quest for the Holy Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuest%5D+%5Bfor%5D+%5Bthe%5D+%5BHoly%5D+%5BRelic%5D) 

##### Land (21)

4 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 4 [Marsh Flats](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D) 13 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### Sideboard (15)

1 [Argentum Armor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArgentum%5D+%5BArmor%5D) 2 [Emerge Unscathed](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEmerge%5D+%5BUnscathed%5D) 1 [Kemba, Kha Regent](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKemba,%5D+%5BKha%5D+%5BRegent%5D) 4 [Kor Firewalker](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BFirewalker%5D) 3 [Revoke Existence](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D) 4 [War Priest of Thune](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWar%5D+%5BPriest%5D+%5Bof%5D+%5BThune%5D) 

##### White (41)

4 [Glint Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlint%5D+%5BHawk%5D) 4 [Kor Duelist](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BDuelist%5D) 4 [Kor Outfitter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BOutfitter%5D) 4 [Kor Skyfisher](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BSkyfisher%5D) 3 [Squadron Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSquadron%5D+%5BHawk%5D) 4 [Stoneforge Mystic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStoneforge%5D+%5BMystic%5D) 4 [Quest for the Holy Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuest%5D+%5Bfor%5D+%5Bthe%5D+%5BHoly%5D+%5BRelic%5D) 2 [Emerge Unscathed](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEmerge%5D+%5BUnscathed%5D) 1 [Kemba, Kha Regent](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKemba,%5D+%5BKha%5D+%5BRegent%5D) 4 [Kor Firewalker](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BFirewalker%5D) 3 [Revoke Existence](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D) 4 [War Priest of Thune](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWar%5D+%5BPriest%5D+%5Bof%5D+%5BThune%5D) 

##### Colorless (34)

4 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 4 [Marsh Flats](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D) 13 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Memnite](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemnite%5D) 4 [Ornithopter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrnithopter%5D) 3 [Argentum Armor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArgentum%5D+%5BArmor%5D) 1 [Basilisk Collar](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBasilisk%5D+%5BCollar%5D) 1 [Sword of Body and Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BBody%5D+%5Band%5D+%5BMind%5D) 

75 Cards 

##### 1 (15)

4 [Glint Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlint%5D+%5BHawk%5D) 4 [Kor Duelist](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BDuelist%5D) 1 [Basilisk Collar](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBasilisk%5D+%5BCollar%5D) 4 [Quest for the Holy Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuest%5D+%5Bfor%5D+%5Bthe%5D+%5BHoly%5D+%5BRelic%5D) 2 [Emerge Unscathed](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEmerge%5D+%5BUnscathed%5D) 

##### 2 (26)

4 [Kor Outfitter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BOutfitter%5D) 4 [Kor Skyfisher](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BSkyfisher%5D) 3 [Squadron Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSquadron%5D+%5BHawk%5D) 4 [Stoneforge Mystic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStoneforge%5D+%5BMystic%5D) 4 [Kor Firewalker](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BFirewalker%5D) 3 [Revoke Existence](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D) 4 [War Priest of Thune](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWar%5D+%5BPriest%5D+%5Bof%5D+%5BThune%5D) 

##### 3 (2)

1 [Sword of Body and Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BBody%5D+%5Band%5D+%5BMind%5D) 1 [Kemba, Kha Regent](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKemba,%5D+%5BKha%5D+%5BRegent%5D) 

##### 6 (3)

3 [Argentum Armor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArgentum%5D+%5BArmor%5D) 

46 Cards 

##### Common (33)

13 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Glint Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlint%5D+%5BHawk%5D) 4 [Kor Outfitter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BOutfitter%5D) 4 [Kor Skyfisher](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BSkyfisher%5D) 3 [Squadron Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSquadron%5D+%5BHawk%5D) 2 [Emerge Unscathed](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEmerge%5D+%5BUnscathed%5D) 3 [Revoke Existence](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D) 

##### Uncommon (24)

4 [Kor Duelist](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BDuelist%5D) 4 [Memnite](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMemnite%5D) 4 [Ornithopter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrnithopter%5D) 4 [Quest for the Holy Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuest%5D+%5Bfor%5D+%5Bthe%5D+%5BHoly%5D+%5BRelic%5D) 4 [Kor Firewalker](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BFirewalker%5D) 4 [War Priest of Thune](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWar%5D+%5BPriest%5D+%5Bof%5D+%5BThune%5D) 

##### Rare (17)

4 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 4 [Marsh Flats](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMarsh%5D+%5BFlats%5D) 4 [Stoneforge Mystic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStoneforge%5D+%5BMystic%5D) 3 [Argentum Armor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArgentum%5D+%5BArmor%5D) 1 [Basilisk Collar](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBasilisk%5D+%5BCollar%5D) 1 [Kemba, Kha Regent](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKemba,%5D+%5BKha%5D+%5BRegent%5D) 

##### Mythic (1)

1 [Sword of Body and Mind](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BBody%5D+%5Band%5D+%5BMind%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Arid+Mesa)

[Deal Another Hand](https://web.archive.org/web/20101029000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kor+Duelist)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Squadron+Hawk)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Squadron+Hawk)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Memnite)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Memnite)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Basilisk+Collar)

a:20:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Arid Mesa";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Marsh Flats";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"13";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Glint Hawk";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Kor Duelist";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Kor Outfitter";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Kor Skyfisher";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Memnite";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Ornithopter";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Squadron Hawk";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Stoneforge Mystic";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Argentum Armor";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Basilisk Collar";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:24:"Quest for the Holy Relic";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Sword of Body and Mind";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Emerge Unscathed";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Kemba, Kha Regent";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Kor Firewalker";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Revoke Existence";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"War Priest of Thune";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

There are once again several things going on in this deck that I like.

White attack decks are popular, baseline strategies that many players gravitate toward when deck building. When we aren't careful to sculpt an environment so that such decks are playable, they often aren't. Based on how many decks there are that look like this in the **Magic Online** results, this is a fine thing to be doing.

![](http://media.wizards.com/images/magic/daily/ld/ld114_dayOf.jpg)  

Both as a player and a developer, I like attack decks to have lots of play into the late game. I find it frustrating to be left with nothing to do after a [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment) or two and have to sit there miserably. I find it sad to watch other people have to do that. For a deck with four [Ornithopter](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter)s and four [Memnite](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memnite)s, this deck has shocking amounts of play into the late game with [Squadron Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk)s and equipment found by [Stoneforge Mystic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stoneforge+Mystic)s.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Squadron+Hawk"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quest+for+the+Holy+Relic"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Quest+for+the+Holy+Relic"></a></div></div></td></tr></tbody></table>

[Squadron Hawk](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk) and [Quest for the Holy Relic](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quest+for+the+Holy+Relic) are two cards that I personally think are pretty cool, but wasn't sure would find a home in competitive Constructed. I'm happy to see them hanging out here.

Let's go to one last deck for today.

#### Michael Svein's Red-White-Blue Control

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (6)

4 [Jace, the Mind Sculptor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5Bthe%5D+%5BMind%5D+%5BSculptor%5D) 2 [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Creature (6)

2 [Frost Titan](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrost%5D+%5BTitan%5D) 4 [Sea Gate Oracle](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSea%5D+%5BGate%5D+%5BOracle%5D) 

##### Sorcery (6)

4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 2 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 

##### Instant (11)

2 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 3 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 2 [Stoic Rebuttal](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStoic%5D+%5BRebuttal%5D) 

##### Artifact (1)

1 [Ratchet Bomb](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D) 

##### Enchantment (5)

4 [Spreading Seas](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpreading%5D+%5BSeas%5D) 1 [Volition Reins](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolition%5D+%5BReins%5D) 

##### Land (25)

1 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 4 [Celestial Colonnade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BColonnade%5D) 2 [Glacial Fortress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlacial%5D+%5BFortress%5D) 7 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 1 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 1 [Terramorphic Expanse](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D) 

60 Cards 

##### Sideboard (15)

1 [Volition Reins](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolition%5D+%5BReins%5D) 1 [Celestial Purge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BPurge%5D) 1 [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 2 [Flame Slash](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlame%5D+%5BSlash%5D) 4 [Flashfreeze](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 1 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 4 [Negate](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D) 1 [Ulamog, the Infinite Gyre](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUlamog,%5D+%5Bthe%5D+%5BInfinite%5D+%5BGyre%5D) 

##### White (2)

1 [Celestial Purge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BPurge%5D) 1 [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 

##### Blue (37)

2 [Frost Titan](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrost%5D+%5BTitan%5D) 4 [Sea Gate Oracle](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSea%5D+%5BGate%5D+%5BOracle%5D) 2 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Jace, the Mind Sculptor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5Bthe%5D+%5BMind%5D+%5BSculptor%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [Spreading Seas](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpreading%5D+%5BSeas%5D) 2 [Stoic Rebuttal](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStoic%5D+%5BRebuttal%5D) 2 [Volition Reins](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolition%5D+%5BReins%5D) 4 [Flashfreeze](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 1 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 4 [Negate](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D) 

##### Red (7)

3 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 2 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 2 [Flame Slash](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlame%5D+%5BSlash%5D) 

##### Multi colored (2)

2 [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Colorless (27)

1 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 4 [Celestial Colonnade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BColonnade%5D) 2 [Glacial Fortress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlacial%5D+%5BFortress%5D) 7 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 1 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 1 [Terramorphic Expanse](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D) 1 [Ratchet Bomb](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D) 1 [Ulamog, the Infinite Gyre](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUlamog,%5D+%5Bthe%5D+%5BInfinite%5D+%5BGyre%5D) 

75 Cards 

##### 1 (9)

3 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 2 [Flame Slash](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlame%5D+%5BSlash%5D) 

##### 2 (22)

2 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 2 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 1 [Ratchet Bomb](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D) 4 [Spreading Seas](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpreading%5D+%5BSeas%5D) 1 [Celestial Purge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BPurge%5D) 4 [Flashfreeze](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 4 [Negate](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D) 

##### 3 (7)

4 [Sea Gate Oracle](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSea%5D+%5BGate%5D+%5BOracle%5D) 2 [Stoic Rebuttal](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStoic%5D+%5BRebuttal%5D) 1 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 

##### 4 (5)

4 [Jace, the Mind Sculptor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5Bthe%5D+%5BMind%5D+%5BSculptor%5D) 1 [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 

##### 5 (2)

2 [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### 6 (4)

2 [Frost Titan](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrost%5D+%5BTitan%5D) 2 [Volition Reins](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolition%5D+%5BReins%5D) 

##### 11 (1)

1 [Ulamog, the Infinite Gyre](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUlamog,%5D+%5Bthe%5D+%5BInfinite%5D+%5BGyre%5D) 

50 Cards 

##### Common (35)

7 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Terramorphic Expanse](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D) 4 [Sea Gate Oracle](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSea%5D+%5BGate%5D+%5BOracle%5D) 2 [Into the Roil](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInto%5D+%5Bthe%5D+%5BRoil%5D) 4 [Mana Leak](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BLeak%5D) 4 [Preordain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 4 [Spreading Seas](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpreading%5D+%5BSeas%5D) 2 [Stoic Rebuttal](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStoic%5D+%5BRebuttal%5D) 2 [Flame Slash](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlame%5D+%5BSlash%5D) 

##### Uncommon (13)

2 [Pyroclasm](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D) 2 [Volition Reins](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolition%5D+%5BReins%5D) 1 [Celestial Purge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BPurge%5D) 4 [Flashfreeze](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfreeze%5D) 4 [Negate](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNegate%5D) 

##### Rare (11)

1 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 2 [Glacial Fortress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlacial%5D+%5BFortress%5D) 4 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 3 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 1 [Ratchet Bomb](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D) 

##### Mythic (16)

4 [Celestial Colonnade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BColonnade%5D) 1 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 2 [Frost Titan](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrost%5D+%5BTitan%5D) 4 [Jace, the Mind Sculptor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5Bthe%5D+%5BMind%5D+%5BSculptor%5D) 2 [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 1 [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 1 [Jace Beleren](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 1 [Ulamog, the Infinite Gyre](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUlamog,%5D+%5Bthe%5D+%5BInfinite%5D+%5BGyre%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Arid+Mesa)

[Deal Another Hand](https://web.archive.org/web/20101029000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Celestial+Colonnade)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sea+Gate+Oracle)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Venser%2C+the+Sojourner)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Arid+Mesa)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sea+Gate+Oracle)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Frost+Titan)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

a:29:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Arid Mesa";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Celestial Colonnade";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Glacial Fortress";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Scalding Tarn";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Tectonic Edge";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Terramorphic Expanse";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Frost Titan";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Sea Gate Oracle";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Into the Roil";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Jace, the Mind Sculptor";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Lightning Bolt";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Mana Leak";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Preordain";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Pyroclasm";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Ratchet Bomb";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Spreading Seas";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Stoic Rebuttal";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Venser, the Sojourner";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Volition Reins";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Celestial Purge";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Day of Judgment";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Flame Slash";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Flashfreeze";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Jace Beleren";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Negate";s:22:"field\_card\_image\_front";a:0:{}}}i:28;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Ulamog, the Infinite Gyre";s:22:"field\_card\_image\_front";a:0:{}}}} 

  
![](http://media.wizards.com/images/magic/daily/ld/ld114_venser.jpg)  

One of the cards I had the most fun with in the Future Future League while we developed *Scars of Mirrodin* was [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venser%2C+the+Sojourner). For quite a long time, I didn't see any results that included decks with Venser, which had me worried. I'm not usually attached to one particular card or deck being powerful, but I knew from playing Venser that he was really fun. We err on the side of making things that we identify as being extra fun a little stronger, and Venser was something that I thought was totally sweet. As it turns out, finding the right deck for Venser just might have been tricky. On the surface, he seems to want to be in a base white-blue deck. Perhaps it could look something like this deck, which I played in the Future Future League at the time of *Scars of Mirrodin* development:

#### Tom LaPille's Red-White-Blue Control

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (10)

4 [Jace, the Mind Sculptor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5Bthe%5D+%5BMind%5D+%5BSculptor%5D) 3 [Gideon Jura](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGideon%5D+%5BJura%5D) 3 [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Creature (12)

4 [Wall of Omens](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BOmens%5D) 4 [Sea Gate Oracle](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSea%5D+%5BGate%5D+%5BOracle%5D) 4 [Baneslayer Angel](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBaneslayer%5D+%5BAngel%5D) 

##### Sorcery (4)

4 [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 

##### Instant (4)

4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 

##### Enchantment (4)

4 [Spreading Seas](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpreading%5D+%5BSeas%5D) 

##### Land (26)

4 [Celestial Colonnade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BColonnade%5D) 4 [Glacial Fortress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlacial%5D+%5BFortress%5D) 3 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 3 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 2 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 4 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

60 Cards 

##### White (15)

4 [Wall of Omens](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BOmens%5D) 4 [Baneslayer Angel](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBaneslayer%5D+%5BAngel%5D) 4 [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 3 [Gideon Jura](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGideon%5D+%5BJura%5D) 

##### Blue (12)

4 [Sea Gate Oracle](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSea%5D+%5BGate%5D+%5BOracle%5D) 4 [Spreading Seas](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpreading%5D+%5BSeas%5D) 4 [Jace, the Mind Sculptor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5Bthe%5D+%5BMind%5D+%5BSculptor%5D) 

##### Red (4)

4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 

##### Multi colored (3)

3 [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Colorless (26)

4 [Celestial Colonnade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BColonnade%5D) 4 [Glacial Fortress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlacial%5D+%5BFortress%5D) 3 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 3 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 2 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 4 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

60 Cards 

##### 1 (4)

4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 

##### 2 (8)

4 [Wall of Omens](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BOmens%5D) 4 [Spreading Seas](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpreading%5D+%5BSeas%5D) 

##### 3 (4)

4 [Sea Gate Oracle](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSea%5D+%5BGate%5D+%5BOracle%5D) 

##### 4 (8)

4 [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 4 [Jace, the Mind Sculptor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5Bthe%5D+%5BMind%5D+%5BSculptor%5D) 

##### 5 (10)

4 [Baneslayer Angel](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBaneslayer%5D+%5BAngel%5D) 3 [Gideon Jura](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGideon%5D+%5BJura%5D) 3 [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

34 Cards 

##### Common (18)

4 [Plains](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Island](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 2 [Mountain](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Sea Gate Oracle](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSea%5D+%5BGate%5D+%5BOracle%5D) 4 [Spreading Seas](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpreading%5D+%5BSeas%5D) 

##### Uncommon (4)

4 [Wall of Omens](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BOmens%5D) 

##### Rare (14)

4 [Glacial Fortress](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGlacial%5D+%5BFortress%5D) 3 [Scalding Tarn](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScalding%5D+%5BTarn%5D) 3 [Arid Mesa](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArid%5D+%5BMesa%5D) 4 [Lightning Bolt](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLightning%5D+%5BBolt%5D) 

##### Mythic (24)

4 [Celestial Colonnade](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCelestial%5D+%5BColonnade%5D) 2 [Tectonic Edge](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTectonic%5D+%5BEdge%5D) 4 [Baneslayer Angel](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBaneslayer%5D+%5BAngel%5D) 4 [Day of Judgment](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDay%5D+%5Bof%5D+%5BJudgment%5D) 4 [Jace, the Mind Sculptor](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5Bthe%5D+%5BMind%5D+%5BSculptor%5D) 3 [Gideon Jura](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGideon%5D+%5BJura%5D) 3 [Venser, the Sojourner](https://web.archive.org/web/20101029000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

60 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Celestial+Colonnade)

[Deal Another Hand](https://web.archive.org/web/20101029000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wall+of+Omens)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tectonic+Edge)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Baneslayer+Angel)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wall+of+Omens)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Baneslayer+Angel)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Jace%2C+the+Mind+Sculptor)

a:17:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Celestial Colonnade";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Glacial Fortress";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Scalding Tarn";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Arid Mesa";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Tectonic Edge";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Wall of Omens";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Sea Gate Oracle";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Baneslayer Angel";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Lightning Bolt";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Spreading Seas";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Day of Judgment";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Jace, the Mind Sculptor";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Gideon Jura";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Venser, the Sojourner";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Michael Svein might sneer at my deck, as he has a strong claim that a Venser deck is supposed to be base blue-red instead of base white-blue. Although I'm maximizing Venser a little more, which is appropriate when I'm playtesting the card, he won a State Championships tournament. At this point, I'd say that he has the chips.

As I said at the beginning of this article, we love seeing what everyone does with the cards we make. Although we love hearing back from you in articles, tweets, and emails, the best feedback we get from you is seeing what you actually do when you play, be it through reading your tournament results or from traveling to events and playing against you in person. Both of those things are fun for us to do, and we couldn't do it if you weren't all out there playing. Thanks as always, keep up the good work, and we'll keep putting out more cards for you to explore.

Last Week's Poll

<table><tbody><tr><td colspan="3"><b> Which faction do you side with? </b></td></tr><tr><td>Mirrodin!</td><td>2892</td><td>41.3%</td></tr><tr><td>Phyrexia!</td><td>2743</td><td>39.2%</td></tr><tr><td>Neither.</td><td>1362</td><td>19.5%</td></tr><tr><td><b>Total</b></td><td><b>6997</b></td><td><b>100.0%</b></td></tr></tbody></table>

  

This Week's Poll

**Of the formats for this year's World Championships, which are you most excited to read coverage about?**StandardExtended*Scars of Mirrodin* Booster DraftLegacyNone of These

  
[![](https://i.ormos.uk/96/f8/96f8240a453a6bfdf11d04eaa34389bb32f8cb9cac8666ec851e063dc0f011f4.jpg)](https://web.archive.org/web/20101029000000/http://staging.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/gameday-facts)
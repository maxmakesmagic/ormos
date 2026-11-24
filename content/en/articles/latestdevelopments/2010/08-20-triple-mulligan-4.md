---
id: xb5qencg
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/08-20-triple-mulligan-4
title: Triple Mulligan
published: '2010-08-20'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
    lang_detected: en
    capture_id: 735541
    url: https://magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
    captured_at: '2022-06-27 05:31:22+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
    lang_detected: en
    capture_id: 735541
    url: https://magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
    captured_at: '2022-06-27 05:31:22+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
    lang_detected: en
    capture_id: 735541
    url: https://magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
    captured_at: '2022-06-27 05:31:22+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
    lang_detected: en
    capture_id: 735541
    url: https://magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
    captured_at: '2022-06-27 05:31:22+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: xb5qencg
  url: https://magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
  page_key: magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
  lang: en
  template: drupal
  captured_at: '2022-06-27 05:31:22+00'
  capture_id: 735541
  wayback_url: https://web.archive.org/web/20220627053122id_/https://magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: xb5qencg
  capture_id: 735541
  url: https://magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
  wayback_url: https://web.archive.org/web/20220627053122id_/https://magic.wizards.com/en/articles/archive/latest-developments/triple-mulligan-2010-08-19
  captured_at: '2022-06-27 05:31:22+00'
  template: drupal
  sha256: a9ec6795483582d6efd878ac68b96c4d02d19902066fb8f6801b0e138ddad98e
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 3
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 1
---
There are many large-scale development questions that we ask ourselves from time to time. For example, we might ask how many creatures we want in average Limited decks, what range of strategies we want a color to have in Constructed, or what the right amount of niche draft strategies within a set is. One such question that we often ask is how important opening hands should be.

![](http://archive.wizards.com/magic/images/tournamentcenter/2007/mi07/finals_vintage1.jpg)  

For an extreme, let's go back in time to the 2007 **Magic** Invitational. One of the final three matches between Tiago Chan and Rich Hoaen used the Vintage format. At the time, [Flash](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash) was unrestricted, and Tiago had chosen to play a deck built around it. Rich's deck, on the other hand, was a [Mishra's Workshop](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop)-based artifact deck. In the first game of their match, Tiago won the die roll, then plopped this hand onto the table.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Flash"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Protean+Hulk"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Protean+Hulk"></a></div></div></td></tr></tbody></table>

[Mox Sapphire](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Sapphire) and [Lotus Petal](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotus+Petal). Cast [Summoner's Pact](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Summoner%27s+Pact) for [Protean Hulk](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Protean+Hulk). Cast [Flash](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash). Put [Protean Hulk](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Protean+Hulk) into play, then let it die. Search for three [Virulent Sliver](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Virulent+Sliver)s and a [Heart Sliver](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heart+Sliver), put them onto the battlefield, and attack for twelve poison counters. Bang, you're dead. Rich's deck didn't have [Force of Will](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) in it, so that was that.

This seems utterly lame, but even crazier things were possible at the same time. In the last round of Day One of Grand Prix–Columbus in 2007, I died to a [Flash](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash) deck in my first upkeep. My opponent chose to draw, then used [Gemstone Caverns](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gemstone+Caverns), [Elvish Spirit Guide](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Spirit+Guide), [Flash](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash), and [Protean Hulk](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Protean+Hulk) to plop four [Disciple of the Vault](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault), four [Shifting Wall](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shifting+Wall)s, and a [Phyrexian Marauder](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Marauder) into play. His five 0/0 artifacts died immediately, then I lost 20 life before I played my first land.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Vault"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Disciple+of+the+Vault"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shifting+Wall"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Shifting+Wall"></a></div></div></td></tr></tbody></table>

One of the most important things to **Magic** being fun over time is that players feel that skill matters. It's hard to feel that this is the case when games end on turn one with any degree of regularity. One.

There is an opposite extreme as well, although it's a little harder to see. I'll do my best to show it to you. The Draft Extravaganza, a day-long tournament that features drafts of several older formats, is a Seattle tradition. At the most recent one, I drafted this deck in a *Ravnica*-*Guildpact*-*Dissension* Draft:

#### Ravnica-Guildpact-Dissension Draft Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (10)

1 [Azorius First-Wing](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BFirst-Wing%5D) 2 [Dimir Infiltrator](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BInfiltrator%5D) 1 [Soulsworn Jury](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulsworn%5D+%5BJury%5D) 1 [Guardian of the Guildpact](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGuardian%5D+%5Bof%5D+%5Bthe%5D+%5BGuildpact%5D) 1 [Steamcore Weird](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteamcore%5D+%5BWeird%5D) 1 [Dimir House Guard](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BHouse%5D+%5BGuard%5D) 1 [Izzet Chronarch](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BChronarch%5D) 1 [Tidewater Minion](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidewater%5D+%5BMinion%5D) 1 [Ratcatcher](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatcatcher%5D) 

##### Sorcery (3)

1 [Train of Thought](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrain%5D+%5Bof%5D+%5BThought%5D) 1 [Brainspoil](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrainspoil%5D) 1 [Ribbons of Night](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRibbons%5D+%5Bof%5D+%5BNight%5D) 

##### Instant (2)

1 [Thunderheads](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThunderheads%5D) 1 [Douse in Gloom](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDouse%5D+%5Bin%5D+%5BGloom%5D) 

##### Artifact (4)

1 [Terrarion](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerrarion%5D) 1 [Azorius Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BSignet%5D) 2 [Orzhov Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BSignet%5D) 

##### Enchantment (4)

2 [Seal of Doom](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BDoom%5D) 2 [Plumes of Peace](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlumes%5D+%5Bof%5D+%5BPeace%5D) 

##### Land (17)

1 [Azorius Chancery](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 5 [Island](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 6 [Swamp](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 3 [Plains](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Mountain](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

40 Cards 

##### White (2)

1 [Soulsworn Jury](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulsworn%5D+%5BJury%5D) 1 [Guardian of the Guildpact](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGuardian%5D+%5Bof%5D+%5Bthe%5D+%5BGuildpact%5D) 

##### Blue (4)

1 [Steamcore Weird](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteamcore%5D+%5BWeird%5D) 1 [Tidewater Minion](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidewater%5D+%5BMinion%5D) 1 [Train of Thought](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrain%5D+%5Bof%5D+%5BThought%5D) 1 [Thunderheads](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThunderheads%5D) 

##### Black (7)

1 [Dimir House Guard](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BHouse%5D+%5BGuard%5D) 1 [Ratcatcher](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatcatcher%5D) 2 [Seal of Doom](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BDoom%5D) 1 [Douse in Gloom](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDouse%5D+%5Bin%5D+%5BGloom%5D) 1 [Brainspoil](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrainspoil%5D) 1 [Ribbons of Night](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRibbons%5D+%5Bof%5D+%5BNight%5D) 

##### Multi colored (6)

1 [Azorius First-Wing](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BFirst-Wing%5D) 2 [Dimir Infiltrator](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BInfiltrator%5D) 1 [Izzet Chronarch](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BChronarch%5D) 2 [Plumes of Peace](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlumes%5D+%5Bof%5D+%5BPeace%5D) 

##### Colorless (21)

1 [Azorius Chancery](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 5 [Island](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 6 [Swamp](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 3 [Plains](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Mountain](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Terrarion](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerrarion%5D) 1 [Azorius Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BSignet%5D) 2 [Orzhov Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BSignet%5D) 

40 Cards 

##### 1 (1)

1 [Terrarion](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerrarion%5D) 

##### 2 (7)

1 [Azorius First-Wing](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BFirst-Wing%5D) 2 [Dimir Infiltrator](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BInfiltrator%5D) 1 [Train of Thought](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrain%5D+%5Bof%5D+%5BThought%5D) 1 [Azorius Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BSignet%5D) 2 [Orzhov Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BSignet%5D) 

##### 3 (7)

1 [Soulsworn Jury](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulsworn%5D+%5BJury%5D) 2 [Seal of Doom](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BDoom%5D) 1 [Thunderheads](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThunderheads%5D) 2 [Plumes of Peace](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlumes%5D+%5Bof%5D+%5BPeace%5D) 1 [Douse in Gloom](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDouse%5D+%5Bin%5D+%5BGloom%5D) 

##### 4 (3)

1 [Guardian of the Guildpact](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGuardian%5D+%5Bof%5D+%5Bthe%5D+%5BGuildpact%5D) 1 [Steamcore Weird](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteamcore%5D+%5BWeird%5D) 1 [Dimir House Guard](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BHouse%5D+%5BGuard%5D) 

##### 5 (4)

1 [Izzet Chronarch](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BChronarch%5D) 1 [Tidewater Minion](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidewater%5D+%5BMinion%5D) 1 [Brainspoil](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrainspoil%5D) 1 [Ribbons of Night](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRibbons%5D+%5Bof%5D+%5BNight%5D) 

##### 6 (1)

1 [Ratcatcher](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatcatcher%5D) 

23 Cards 

##### Common (35)

5 [Island](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 6 [Swamp](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 3 [Plains](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Mountain](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Azorius First-Wing](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BFirst-Wing%5D) 2 [Dimir Infiltrator](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BInfiltrator%5D) 1 [Soulsworn Jury](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulsworn%5D+%5BJury%5D) 1 [Guardian of the Guildpact](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGuardian%5D+%5Bof%5D+%5Bthe%5D+%5BGuildpact%5D) 1 [Steamcore Weird](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteamcore%5D+%5BWeird%5D) 1 [Dimir House Guard](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDimir%5D+%5BHouse%5D+%5BGuard%5D) 1 [Izzet Chronarch](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIzzet%5D+%5BChronarch%5D) 1 [Tidewater Minion](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTidewater%5D+%5BMinion%5D) 1 [Terrarion](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerrarion%5D) 1 [Train of Thought](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTrain%5D+%5Bof%5D+%5BThought%5D) 2 [Seal of Doom](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BDoom%5D) 2 [Plumes of Peace](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlumes%5D+%5Bof%5D+%5BPeace%5D) 1 [Douse in Gloom](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDouse%5D+%5Bin%5D+%5BGloom%5D) 1 [Brainspoil](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrainspoil%5D) 2 [Orzhov Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOrzhov%5D+%5BSignet%5D) 

##### Uncommon (4)

1 [Azorius Chancery](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 1 [Thunderheads](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThunderheads%5D) 1 [Ribbons of Night](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRibbons%5D+%5Bof%5D+%5BNight%5D) 1 [Azorius Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BSignet%5D) 

##### Rare (1)

1 [Ratcatcher](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatcatcher%5D) 

40 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Chancery)

[Deal Another Hand](https://web.archive.org/web/20100820000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Signet)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dimir+House+Guard)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Steamcore+Weird)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Guardian+of+the+Guildpact)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plumes+of+Peace)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Izzet+Chronarch)

a:24:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Azorius Chancery";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"5";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"6";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Azorius First-Wing";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Dimir Infiltrator";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Soulsworn Jury";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Guardian of the Guildpact";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Steamcore Weird";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Dimir House Guard";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Izzet Chronarch";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Tidewater Minion";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Ratcatcher";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Terrarion";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Train of Thought";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Seal of Doom";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"2";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Thunderheads";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Plumes of Peace";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"2";}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Douse in Gloom";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Brainspoil";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Ribbons of Night";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:22;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Azorius Signet";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";}i:23;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Orzhov Signet";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";}} 

  

This deck may look like a pile to you. In fact, it looked like a pile to me while I was building it. However, I entered the draft with some knowledge about how the format plays. Almost every deck is three or more colors, which means plenty of time setting up and deploying cards like [Azorius Chancery](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Azorius+Chancery) and [Orzhov Signet](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Orzhov+Signet) to get the necessary mana to cast spells. Aggressive decks are rare because of how hard it is to come out quickly. This means that card-drawing cards like [Compulsive Research](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsive+Research) and [Consult the Necrosages](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Consult+the+Necrosages) are very powerful because most games come down to wars of attrition. 

![](http://media.wizards.com/images/magic/daily/ld/ld104_chancery.jpg)  

Unfortunately, I didn't have any of those. What I had was a single [Train of Thought](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Train+of+Thought), two [Dimir Infiltrator](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dimir+Infiltrator)s to find it with, and an [Izzet Chronarch](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Izzet+Chronarch) to use to get it back a for a second use. Those two uses of my one [Train of Thought](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Train+of+Thought) needed to be enough to power me into enough cards to actually put a game away ... with my single [Ratcatcher](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ratcatcher). I had plenty of creature removal, so I guessed that I might have enough time to actually implement this crazy plan. 

As it turned out, I did. I went 2-1 in this draft, and I would have won the third round if I had not misplayed. Every game, I looked at my opening hand, saw that it had lands and some kill spells, and trusted that my [Train of Thought](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Train+of+Thought) or one of its two surrogates would show up in time. My opponents usually figured out what was going on about halfway through the second game. Even if they had a good start, the format was so slow that their opening hand just didn't matter. A huge percentage of both my deck and my opponent's deck would be in on the table, and it didn't matter which seven cards started there. Paradoxically, this also reduces the amount of skill present in the play of the game as the importance of other factors rises. When almost all of the cards in a deck matter over the course of a twenty-turn game, deck building becomes a much bigger determinant of the winner than play.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Train+of+Thought)](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Train+of+Thought)

  

I chose the most extreme examples I could think of for this section, and as you would expect most formats fall somewhere in between Summer 2007 Vintage and *Ravnica* Block Draft in speed. We try to vary the speed of formats in order to keep the experience of **Magic** varied, but we occasionally still get outside a comfortable range. *Zendikar* Limited is much faster than I think we intended it to be, and it can be so fast it's hard to come back from a bad opening hand. *Worldwake* was intended to slow the format down some to compensate, but one pack of *Worldwake* could only do so much. None of the other Limited formats we've released in recent memory have been uncomfortably fast or slow to me, so I can't be too unhappy about our record.

Unhappy with this article? If you are, then you can...

[![](http://media.wizards.com/images/magic/daily/ld/ld104_mulliganButton.jpg)](https://web.archive.org/web/20100820000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/104amp;date=8/20amp;page=Mulligan)  

Making Leylines

I was part of both the design and development teams for ***Magic** 2011*. If the [Titans](https://web.archive.org/web/20100820000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;name=+%5Btitan%5Damp;set=%5B%22Magic+2011%22%5D) received the most time and effort during the process, then [Leylines](https://web.archive.org/web/20100820000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;name=+%5Bleyline%5Damp;set=%5B%22Magic+2011%22%5D) probably received the most worry. Why do you think that might be?

Before you clicked the mulligan button, you had an article that discussed how we want the game play of **Magic** to feel like it matters to the outcome. Imagine this card:

> Leyline of Haste  
>  2RR  
>  Enchantment  
>  If Leyline of Haste is in your opening hand, you may begin the game with it on the battlefield.
> 
> All creatures have Haste.

With this card, you are obviously supposed to make a little red creature deck. The problem with it is that the difference in power level between a game that begins with this card in play and a game that does not is enormous; even more so when the opponent doesn't have creatures that they're interested in attacking with early in the game. Some of Standard's fastest red decks can win a game unopposed on turn four, and with this card that could be cut to three easily. On the other hand, when you draw this card on turn two, it's a total blank. Many proactive Leyline designs we tried had this same effect on the game—they made the opening hand feel too important.

At first glance, the line of text that comes with the Leyline territory seems very difficult to use without this opening-hand-magnifying effect. However, we took our inspiration from the superstar of the first Leyline cycle...

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Leyline_Of_The_Void)](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline_Of_The_Void)

  

... which we also decided to repeat ...

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Leyline+of+the+Void)](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+the+Void)

  

... and made Leylines that were reactive rather than proactive. By this, I mean that rather than helping you do something, they make it harder for your opponent to do certain things. [Leyline of the Void](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+the+Void) plays the hero against degenerate graveyard strategies like Dredge, even in Vintage where Dredge decks have cards like [Bazaar of Baghdad](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bazaar+of+Baghdad). [Leyline of Punishment](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Punishment) stops many of the white effects that traditionally vex red burn players. [Leyline of Sanctity](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Sanctity) messes, in turn, with those same burn decks, and hurts combination decks that need to target you to win. [Leyline of Anticipation](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Anticipation) messes with opponents who plan to use lots of countermagic against you.

In all cases, you might argue that these still increase the importance of the opening hand. In certain match-ups, they can, but this tends to happen when the deck on the receiving end of a Leyline is particularly non-interactive. Extended dredge decks in the past few Extended Pro Tour Qualifier seasons could easily win on turn three, and with a deck that fast sometimes only a Leyline can bring the two decks back into interaction. Similarly, a mono-red deck playing against a [Circle of Protection: Red](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Circle+of+Protection%3A+Red) is hardly a game, but adding [Leyline of Punishment](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Punishment) into the mix gives a higher chance for an interactive game. Our goal with these Leylines was to increase the total interaction in **Magic** rather than decrease it.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Vitality"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Leyline+of+Vitality"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stabbing+Pain"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Stabbing+Pain"></a></div></div></td></tr></tbody></table>

You might also point out that [Leyline of Vitality](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Vitality) doesn't quite conform to the "reactive card" model. It does less of an obvious job than the other four Leylines in ***Magic** 2011*, but it still does that job at times. Just last Friday, I saw a red-green drafter with lots of one toughness creatures sideboard this in against a black drafter who showed multiple [Stabbing Pain](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stabbing+Pain)s in the first game. He indeed got to start the third game with his Leyline in play, and that was the difference that allowed him to win his match. I was pleased to see that interaction.

Still want to try again? You'll get less content, but you can still ...

[![](http://media.wizards.com/images/magic/daily/ld/ld104_mulliganButton.jpg)](https://web.archive.org/web/20100820000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/104amp;date=8/20amp;page=Mulligan2)  

How We Mulligan

I am often asked practical questions about life inside **Magic** Ramp;D. How do we proxy cards? How do we build packs for drafting? How quickly can cards change? Every once in a while, I also get asked how we handle mulligans. Because it's Opening Hand Week, I get to answer that one today! Best of all, I get to correct Mark Rosewater's [statements](https://web.archive.org/web/20100820000000/http://archive.wizards.com/magic/Magazine/Article.aspx?x=mtg/daily/mm/104) earlier in the week! Well, I get to go into more detail, at least.

![](http://media.wizards.com/images/magic/daily/ld/ld104_Leyline_of_Anticipation.jpg)  

As Mark said on Monday, during design we are more interested in finding out whether the thing we are doing is fun in broad strokes. Therefore, we always mulligan back to seven cards, trusting each other not to abuse the rule to mulligan mediocre but keepable hands into better ones in search of victory. During most of development, we mulligan back to seven cards whenever a mulliganed hand contains zero, one, six, or seven lands, and go down a card under any other circumstance. This includes color screw, top-heavy spells, or whatever else. This is because the extreme ends of land quantity distribution don't teach us a lot, but we do need to know how decks are punished when they have the wrong mana colors or somewhat land-light or land-heavy draws. During Future Future League tournaments, we always go down a card for mulligans in order to simulate real world conditions.

You're getting pretty low on paragraphs now, but I guess you still can ...

[![](http://media.wizards.com/images/magic/daily/ld/ld104_mulliganButton.jpg)](https://web.archive.org/web/20100820000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/104amp;date=8/20amp;page=Mulligan3)  

Last Week's Polls

<table><tbody><tr><td colspan="3"><b> Have you ever gone to a game convention—for example, Gen Con, Origins, PAX? </b></td></tr><tr><td>Yes, and I played <b>Magic</b> there.</td><td>790</td><td>17.2%</td></tr><tr><td>Yes, and I didn't play <b>Magic</b> there.</td><td>414</td><td>9.0%</td></tr><tr><td>No.</td><td>3377</td><td>73.7%</td></tr><tr><td><b>Total</b></td><td><b>4581</b></td><td><b>100.0%</b></td></tr></tbody></table>

  

<table><tbody><tr><td colspan="3"><b> Have you ever attended a Grand Prix? </b></td></tr><tr><td>Yes, and I played in it.</td><td>1042</td><td>20.3%</td></tr><tr><td>Yes, and I didn't play in it.</td><td>181</td><td>3.5%</td></tr><tr><td>No.</td><td>3902</td><td>76.1%</td></tr><tr><td><b>Total</b></td><td><b>5125</b></td><td><b>100.0%</b></td></tr></tbody></table>

  

Every time I ask a poll like this, some of you email me with statements like "I really wanted to vote 'no, but X'," where X is any number of things. I think this is because just saying no feels bad. In the future, I release you from any obligation to feel bad about voting no. The point behind these questions is to gather information. I'm not here to judge you. You all care about **Magic**, that's all I could ever ask, and I'm not going to ask for more. On the other hand, I am statistically confident that if you're reading this, you care enough about **Magic** that you would have fun if you went to a gaming convention or a Grand Prix. I recommend trying it at least once. My first Origins and my first Grand Prix were both life-changing experiences, and aside from the fact that I work for Wizards and you probably don't, it's unlikely that there are huge differences between me and you that would cause you to enjoy these events less. If one is near you, I think it would be worth your time to go and experience it.

This Week's Poll

**Which Leyline is your favorite?**[Leyline of Anticipation](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Anticipation)[Leyline of Lifeforce](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Lifeforce)[Leyline of Lightning](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Lightning)[Leyline of Punishment](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Punishment)[Leyline of Sanctity](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Sanctity)[Leyline of Singularity](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Singularity)[Leyline of the Meek](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+the+Meek)[Leyline of the Void](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+the+Void)[Leyline of Vitality](https://web.archive.org/web/20100820000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+Vitality) None
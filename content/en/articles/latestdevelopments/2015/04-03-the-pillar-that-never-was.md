---
id: 2dn95h44
kind: article
lang: en
path: /en/articles/latestdevelopments/2015/04-03-the-pillar-that-never-was
title: The Pillar That Never Was
published: '2015-04-03'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
    lang_detected: en
    capture_id: 729499
    url: http://magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
    captured_at: '2015-12-24 12:11:18+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
    lang_detected: en
    capture_id: 729499
    url: http://magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
    captured_at: '2015-12-24 12:11:18+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
    lang_detected: en
    capture_id: 729499
    url: http://magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
    captured_at: '2015-12-24 12:11:18+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
    lang_detected: en
    capture_id: 729499
    url: http://magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
    captured_at: '2015-12-24 12:11:18+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: 2dn95h44
  url: http://magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
  page_key: magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
  lang: en
  template: drupal
  captured_at: '2015-12-24 12:11:18+00'
  capture_id: 729499
  wayback_url: https://web.archive.org/web/20151224121118id_/http://magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 2dn95h44
  capture_id: 729499
  url: http://magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
  wayback_url: https://web.archive.org/web/20151224121118id_/http://magic.wizards.com/en/articles/archive/latest-developments/pillar-never-was-2015-04-03
  captured_at: '2015-12-24 12:11:18+00'
  template: drupal
  sha256: b4dfd481dfa6e00655bfbd12a305ef4d61c0d3a6d43a36b368ba6994334ce43d
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 3
---
It's very hard for *Magic* R&D to predict everything in the metagame. We play hundreds, if not thousands, of games of Future Future League Standard when working on a set, but unlike the real world, our cards keep changing. We get the set to a point where we are generally happy with things, and we send it off into the world.

In general, we get a lot right. Not everything, but a lot. We miss a few cards that were hits, and we have a few cards we expect to show up that miss in the real world. Usually, they are kind of minor, but sometimes they are pillars of our own format that spawn multiple tier-1 decks. This article is about one card we were expecting to show up, but didn't—although it's one we were pretty happy didn't. That card?

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=First+Response)](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response)

It might seem strange to you that we had pegged this as a top Constructed card, so let me go through why we thought the card was so powerful, and what kind of things we did to try and keep it from dominating the metagame.

# First Response's History

Let me start off by giving you the version that design handed over to us:

Supply Chain

1W

Enchantment

At the beginning of each end step, if you lost life this turn, put a 1/1 white Soldier creature token onto the battlefield.

We played it with [Mana Confluence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Confluence) and found that making tokens on turn two and beyond was too Bitterblossomy, so we moved it to three mana. That might have been it, if not for one very big thing—early on in *Khans of Tarkir* FFL, we found that we just couldn't cast our spells. Wedge decks weren't working because the mana wasn't strong enough. The problem was that the *Innistrad* [check lands](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+%5b%22Innistrad%22%5d&type=+%5b%22Land%22%5d&text=+%5bunless%5d+%5bcontrol%5d) that were in *Magic 2015* at the time worked with the allied-color fetch lands to make two-color and shard decks work, but not to make wedge decks work. Casting a [Mantis Rider](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mantis+Rider) on turn three was difficult, which led to people mostly playing two-color decks. We could've kept bumping up the power level of the cards in Khans until people played the wedge cards, but instead we went back to M15 (which had not yet gone to typesetting), and tried to see what we could do. This led to a late change of swapping the check lands for the [pain lands](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&type=+%5b%22Land%22%5d&text=+%5b%22deals+1+damage+to+you%22%5d&set=+%5b%22Magic%202015%20Core%20Set%22%5d). A few days later, someone pointed out "Boy, this [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response) card is a lot better with the pain lands." A little testing later and that was confirmed, it was quite good. More than just that, we found the gameplay of the card very frustrating when it was good. Each turn, a player would get two tokens per [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response). It was almost impossible to fight through unless you had a ton of creatures with evasion, and control decks had a hard time dealing with the onslaught.

We were just about out of time for testing *Magic 2015*, so we moved it up to four mana, assuming that would keep it out of being a top-tier Constructed card. We didn't think about it a ton for a little while, until Khans became more settled as a set, but then we started putting together decks that included the card, just to see how it was doing. Here are some of the resulting decklists from both the *Khans of Tarkir* and *Fate Reforged* Standard environments:

#### WB Tokens by Gerry Thompson

##### 

 ![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (4)

4 [Sorin, Solemn Visitor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BSolemn%5D+%5BVisitor%5D) 

##### Creature (18)

4 [Soldier of the Pantheon](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoldier%5D+%5Bof%5D+%5Bthe%5D+%5BPantheon%5D) 4 [Herald of Anafenza](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHerald%5D+%5Bof%5D+%5BAnafenza%5D) 4 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 2 [Eidolon of Countless Battles](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEidolon%5D+%5Bof%5D+%5BCountless%5D+%5BBattles%5D) 

##### Instant (4)

4 [Raise the Alarm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaise%5D+%5Bthe%5D+%5BAlarm%5D) 

##### Artifact (3)

2 [Spear of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpear%5D+%5Bof%5D+%5BHeliod%5D) 1 [Hall of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHall%5D+%5Bof%5D+%5BTriumph%5D) 

##### Enchantment (8)

3 [Banishing Light](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanishing%5D+%5BLight%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 1 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 

##### Land (23)

4 [Temple of Silence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 4 [Caves of Koilos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 1 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 1 [Mana Confluence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 9 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### White (32)

4 [Soldier of the Pantheon](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoldier%5D+%5Bof%5D+%5Bthe%5D+%5BPantheon%5D) 4 [Herald of Anafenza](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHerald%5D+%5Bof%5D+%5BAnafenza%5D) 4 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [Raise the Alarm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaise%5D+%5Bthe%5D+%5BAlarm%5D) 4 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 2 [Spear of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpear%5D+%5Bof%5D+%5BHeliod%5D) 3 [Banishing Light](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanishing%5D+%5BLight%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 2 [Eidolon of Countless Battles](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEidolon%5D+%5Bof%5D+%5BCountless%5D+%5BBattles%5D) 1 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 

##### Multi colored (4)

4 [Sorin, Solemn Visitor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BSolemn%5D+%5BVisitor%5D) 

##### Colorless (24)

1 [Hall of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHall%5D+%5Bof%5D+%5BTriumph%5D) 4 [Temple of Silence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 4 [Caves of Koilos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 1 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 1 [Mana Confluence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 9 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### 1 (8)

4 [Soldier of the Pantheon](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoldier%5D+%5Bof%5D+%5Bthe%5D+%5BPantheon%5D) 4 [Herald of Anafenza](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHerald%5D+%5Bof%5D+%5BAnafenza%5D) 

##### 2 (8)

4 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [Raise the Alarm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaise%5D+%5Bthe%5D+%5BAlarm%5D) 

##### 3 (12)

4 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 2 [Spear of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpear%5D+%5Bof%5D+%5BHeliod%5D) 3 [Banishing Light](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanishing%5D+%5BLight%5D) 1 [Hall of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHall%5D+%5Bof%5D+%5BTriumph%5D) 2 [Eidolon of Countless Battles](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEidolon%5D+%5Bof%5D+%5BCountless%5D+%5BBattles%5D) 

##### 4 (8)

4 [Sorin, Solemn Visitor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BSolemn%5D+%5BVisitor%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 

##### 5 (1)

1 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 

37 Cards 

##### Common (13)

4 [Raise the Alarm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaise%5D+%5Bthe%5D+%5BAlarm%5D) 9 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

##### Uncommon (11)

4 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 3 [Banishing Light](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanishing%5D+%5BLight%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 

##### Rare (28)

4 [Soldier of the Pantheon](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoldier%5D+%5Bof%5D+%5Bthe%5D+%5BPantheon%5D) 4 [Herald of Anafenza](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHerald%5D+%5Bof%5D+%5BAnafenza%5D) 2 [Spear of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpear%5D+%5Bof%5D+%5BHeliod%5D) 1 [Hall of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHall%5D+%5Bof%5D+%5BTriumph%5D) 2 [Eidolon of Countless Battles](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEidolon%5D+%5Bof%5D+%5BCountless%5D+%5BBattles%5D) 1 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 4 [Temple of Silence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 4 [Caves of Koilos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 1 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D) 1 [Mana Confluence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 

##### Mythic (8)

4 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 4 [Sorin, Solemn Visitor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BSolemn%5D+%5BVisitor%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Soldier+of+the+Pantheon)

[Deal Another Hand](https://web.archive.org/web/20150403000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Raise+the+Alarm)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Caves+of+Koilos)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Silence)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Soldier+of+the+Pantheon)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=First+Response)

#### Mardu Control by Adam Prosak

##### 

 ![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (6)

2 [Sorin, Solemn Visitor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BSolemn%5D+%5BVisitor%5D) 4 [Elspeth, Sun's Champion](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElspeth,%5D+%5BSun%5D+%5BChampion%5D) 

##### Creature (10)

3 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 3 [Butcher of the Horde](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BButcher%5D+%5Bof%5D+%5Bthe%5D+%5BHorde%5D) 

##### Instant (8)

2 [Crackling Doom](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrackling%5D+%5BDoom%5D) 4 [Mardu Charm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMardu%5D+%5BCharm%5D) 2 [Utter End](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUtter%5D+%5BEnd%5D) 

##### Artifact (1)

1 [Spear of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpear%5D+%5Bof%5D+%5BHeliod%5D) 

##### Enchantment (9)

4 [Banishing Light](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanishing%5D+%5BLight%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 1 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 

##### Land (26)

4 [Temple of Silence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 4 [Temple of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 1 [Temple of Malice](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMalice%5D) 4 [Caves of Koilos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 1 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Bloodstained Mire](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodstained%5D+%5BMire%5D) 2 [Swamp](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Mountain](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

60 Cards 

##### White (21)

3 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 4 [Banishing Light](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanishing%5D+%5BLight%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 1 [Spear of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpear%5D+%5Bof%5D+%5BHeliod%5D) 1 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 4 [Elspeth, Sun's Champion](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElspeth,%5D+%5BSun%5D+%5BChampion%5D) 

##### Multi colored (13)

2 [Crackling Doom](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrackling%5D+%5BDoom%5D) 4 [Mardu Charm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMardu%5D+%5BCharm%5D) 2 [Utter End](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUtter%5D+%5BEnd%5D) 3 [Butcher of the Horde](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BButcher%5D+%5Bof%5D+%5Bthe%5D+%5BHorde%5D) 2 [Sorin, Solemn Visitor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BSolemn%5D+%5BVisitor%5D) 

##### Colorless (26)

4 [Temple of Silence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 4 [Temple of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 1 [Temple of Malice](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMalice%5D) 4 [Caves of Koilos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 1 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Bloodstained Mire](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodstained%5D+%5BMire%5D) 2 [Swamp](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Mountain](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

60 Cards 

##### 2 (3)

3 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 

##### 3 (15)

4 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 2 [Crackling Doom](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrackling%5D+%5BDoom%5D) 4 [Banishing Light](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanishing%5D+%5BLight%5D) 4 [Mardu Charm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMardu%5D+%5BCharm%5D) 1 [Spear of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpear%5D+%5Bof%5D+%5BHeliod%5D) 

##### 4 (11)

2 [Utter End](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUtter%5D+%5BEnd%5D) 3 [Butcher of the Horde](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BButcher%5D+%5Bof%5D+%5Bthe%5D+%5BHorde%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 2 [Sorin, Solemn Visitor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BSolemn%5D+%5BVisitor%5D) 

##### 5 (1)

1 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 

##### 6 (4)

4 [Elspeth, Sun's Champion](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElspeth,%5D+%5BSun%5D+%5BChampion%5D) 

34 Cards 

##### Common (5)

1 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Swamp](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Mountain](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

##### Uncommon (15)

3 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [Banishing Light](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBanishing%5D+%5BLight%5D) 4 [Mardu Charm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMardu%5D+%5BCharm%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 

##### Rare (30)

2 [Crackling Doom](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrackling%5D+%5BDoom%5D) 2 [Utter End](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUtter%5D+%5BEnd%5D) 3 [Butcher of the Horde](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BButcher%5D+%5Bof%5D+%5Bthe%5D+%5BHorde%5D) 1 [Spear of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpear%5D+%5Bof%5D+%5BHeliod%5D) 1 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 4 [Temple of Silence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BSilence%5D) 4 [Temple of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 1 [Temple of Malice](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BMalice%5D) 4 [Caves of Koilos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCaves%5D+%5Bof%5D+%5BKoilos%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 4 [Bloodstained Mire](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodstained%5D+%5BMire%5D) 

##### Mythic (10)

4 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 2 [Sorin, Solemn Visitor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSorin,%5D+%5BSolemn%5D+%5BVisitor%5D) 4 [Elspeth, Sun's Champion](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElspeth,%5D+%5BSun%5D+%5BChampion%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Seeker+of+the+Way)

[Deal Another Hand](https://web.archive.org/web/20150403000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Battlefield+Forge)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Triumph)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Triumph)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mardu+Charm)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=First+Response)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Malice)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Brimaz%2C+King+of+Oreskos)

#### Jeskai First Response—Adam Prosak

##### 

 ![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (13)

4 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 3 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 4 [Monastery Mentor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMonastery%5D+%5BMentor%5D) 2 [Ephara, God of the Polis](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEphara,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BPolis%5D) 

##### Instant (12)

4 [Raise the Alarm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaise%5D+%5Bthe%5D+%5BAlarm%5D) 4 [Jeskai Charm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJeskai%5D+%5BCharm%5D) 4 [Reality Shift](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BReality%5D+%5BShift%5D) 

##### Enchantment (10)

4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 4 [Jeskai Ascendancy](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJeskai%5D+%5BAscendancy%5D) 2 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 

##### Land (25)

4 [Temple of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 2 [Temple of Epiphany](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BEpiphany%5D) 1 [Temple of Enlightenment](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BEnlightenment%5D) 4 [Flooded Strand](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlooded%5D+%5BStrand%5D) 4 [Shivan Reef](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 1 [Mana Confluence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 3 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Island](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

60 Cards 

##### White (21)

4 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [Raise the Alarm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaise%5D+%5Bthe%5D+%5BAlarm%5D) 3 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 4 [Monastery Mentor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMonastery%5D+%5BMentor%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 2 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 

##### Blue (4)

4 [Reality Shift](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BReality%5D+%5BShift%5D) 

##### Multi colored (10)

2 [Ephara, God of the Polis](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEphara,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BPolis%5D) 4 [Jeskai Ascendancy](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJeskai%5D+%5BAscendancy%5D) 4 [Jeskai Charm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJeskai%5D+%5BCharm%5D) 

##### Colorless (25)

4 [Temple of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 2 [Temple of Epiphany](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BEpiphany%5D) 1 [Temple of Enlightenment](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BEnlightenment%5D) 4 [Flooded Strand](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlooded%5D+%5BStrand%5D) 4 [Shivan Reef](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 1 [Mana Confluence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 3 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Island](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

60 Cards 

##### 2 (12)

4 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [Raise the Alarm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaise%5D+%5Bthe%5D+%5BAlarm%5D) 4 [Reality Shift](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BReality%5D+%5BShift%5D) 

##### 3 (15)

3 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 4 [Monastery Mentor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMonastery%5D+%5BMentor%5D) 4 [Jeskai Ascendancy](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJeskai%5D+%5BAscendancy%5D) 4 [Jeskai Charm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJeskai%5D+%5BCharm%5D) 

##### 4 (6)

4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 2 [Ephara, God of the Polis](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEphara,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BPolis%5D) 

##### 5 (2)

2 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 

35 Cards 

##### Common (9)

4 [Raise the Alarm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRaise%5D+%5Bthe%5D+%5BAlarm%5D) 3 [Plains](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 2 [Island](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

##### Uncommon (16)

4 [Seeker of the Way](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeeker%5D+%5Bof%5D+%5Bthe%5D+%5BWay%5D) 4 [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirst%5D+%5BResponse%5D) 4 [Jeskai Charm](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJeskai%5D+%5BCharm%5D) 4 [Reality Shift](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BReality%5D+%5BShift%5D) 

##### Rare (26)

4 [Jeskai Ascendancy](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJeskai%5D+%5BAscendancy%5D) 2 [Dictate of Heliod](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDictate%5D+%5Bof%5D+%5BHeliod%5D) 4 [Temple of Triumph](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BTriumph%5D) 2 [Temple of Epiphany](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BEpiphany%5D) 1 [Temple of Enlightenment](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemple%5D+%5Bof%5D+%5BEnlightenment%5D) 4 [Flooded Strand](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlooded%5D+%5BStrand%5D) 4 [Shivan Reef](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 4 [Battlefield Forge](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBattlefield%5D+%5BForge%5D) 1 [Mana Confluence](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 

##### Mythic (9)

3 [Brimaz, King of Oreskos](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrimaz,%5D+%5BKing%5D+%5Bof%5D+%5BOreskos%5D) 4 [Monastery Mentor](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMonastery%5D+%5BMentor%5D) 2 [Ephara, God of the Polis](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEphara,%5D+%5BGod%5D+%5Bof%5D+%5Bthe%5D+%5BPolis%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Seeker+of+the+Way)

[Deal Another Hand](https://web.archive.org/web/20150403000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Battlefield+Forge)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flooded+Strand)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Monastery+Mentor)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=First+Response)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temple+of+Epiphany)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shivan+Reef)

Now, these decks were naturally less tuned than the ones in the real world. We also made them because of a quirk of FFL testing—it's a lot easier to get onto playing a four-mana card that used to be three mana when that version was very strong. The card just looks a lot stronger to us because we've seen what it can do. In the outside world, nobody knows the card used to cost three, or even two mana, and it's much harder to think that the card could even be Constructed playable. This was a card we were hoping people wouldn't put a lot of effort into testing for [Pro Tour *Magic 2015*](https://web.archive.org/web/20150403000000/http://magic.wizards.com/events/coverage/ptm15), and from what we gather, they didn't.

# The Anatomy of a Miss

This leads to a big question—if we were so afraid of [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response) being a major player in our FFL Standard, why didn't it hit in the real world? Well, there are a few reasons.

The first reason is that our decks are just way less tuned than in the real world. We change cards very rapidly—often making five or more substantial buffs or debuffs a week, which means that it's very hard to fine tune a decklist. The advantages you get from that fine tuning are often just overshadowed by one card being a mana undercosted, or having a little too much toughness. We also have a duty to test a lot of cards and not just focus on the few that we view as being the best of the best.

The second reason is that our own metagame was more about control and midrange than the real world metagame. The average deck was just not fast enough to get in before [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response) started taking hold. In addition, we didn't have a ton of great tools to fight the card. It matched up really well against most of our most-played creatures like Polukranos, [Savage Knuckleblade](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savage+Knuckleblade), and even [Goblin Rabblemaster](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Rabblemaster).

Finally, the third reason is that development is all about changing cards. Because of the timing, changing [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response) wasn't possible, so it meant changing the cards in Khans to be better against [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response). It wouldn't help us for Pro Tour *Magic 2015*, but even if things went wrong there, we could make it so it wasn't also dominating Khans Standard.

As an example, this was the original version of [Siege Rhino](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Rhino):

[Siege Rhino](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Rhino)

WBG

Creature – Beast

When CARDNAME enters the battlefield, each opponent loses 2 life and you gain 2 life.

If a spell or ability an opponent controls causes you to discard CARDNAME, put it onto the battlefield instead of putting it into your graveyard.

3/4

This card was here to fight a different card that was in and out of FFL—[Liliana of the Veil](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana+of+the+Veil). When she was removed from M15, [Siege Rhino](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Rhino) instead got "can't be countered" text. As the [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response) threat in our FFL grew, the deck that was most heavily impacted by it was Abzan, since they were supposed to be the clan that outlasted their opponents, but getting two 1/1s a turn wasn't something they could easily overcome. As a result, we moved [Siege Rhino](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Rhino) up from 3 to 4 mana, and gave it trample to go over the top of the [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response) tokens. At the same time, we had to move a 4-mana Abzan card down, which meant changing:

[Anafenza, the Foremost](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anafenza%2C+the+Foremost)

1WBG

Creature – Human Soldier

Whenever CARDNAME attacks, put two +1/+1 counters on another target tapped creature you control. If a creature an opponent controls would die, exile it instead.

4/6

This swap let us make sure that the Abzan had a creature that could go over the top of [First Response](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=First+Response).

![](http://media.wizards.com/2015/images/daily/cardart_PromiseofPower.jpg)

[Promise of Power](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Promise+of+Power) | Art by [Kev Walker](https://web.archive.org/web/20150403000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Kev+Walker%22%5d)

# The Power of Hindsight

It's easy to look back on this as a failure of R&D to identify which cards were weak and strong, but I think it is instead a view of the system working. Standard isn't perfect right now—not that I even know what a perfect Standard environment is—but it is very good. It has only gotten to be that way because we work on making our environment as diverse as possible, putting in a number of safeguards in the format to keep any one deck from becoming too dominant.

Ultimately, our goal in testing is to create a lot of decks that are fun, and to make a format that is diverse enough that we can't solve it ourselves. After all, if a handful of developers could figure it out in the time we have to work on it, there is no way it would not be solved very quickly in the real world. I think it is good that we have times like this where cards we think are major pillars miss, because it reminds us how robust our game is, and how well our system for developing cards work.

That's it for this week. Next week, I'll be back with Dragon Week, and I'll talk about how we made Dragons-matter cards work in *Dragons of Tarkir*.

Until next time,

Sam ([@samstod](https://twitter.com/@samstod))
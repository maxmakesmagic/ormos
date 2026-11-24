---
id: 8xm29k6t
kind: article
lang: en
path: /en/articles/latestdevelopments/2015/02-13-developing-manifest
title: Developing Manifest
published: '2015-02-13'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
    lang_detected: en
    capture_id: 720924
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
    captured_at: '2015-12-24 23:40:40+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
    lang_detected: en
    capture_id: 720924
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
    captured_at: '2015-12-24 23:40:40+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
    lang_detected: en
    capture_id: 720924
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
    captured_at: '2015-12-24 23:40:40+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
    lang_detected: en
    capture_id: 720924
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
    captured_at: '2015-12-24 23:40:40+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: 8xm29k6t
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
  lang: en
  template: drupal
  captured_at: '2015-12-24 23:40:40+00'
  capture_id: 720924
  wayback_url: https://web.archive.org/web/20151224234040id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 8xm29k6t
  capture_id: 720924
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
  wayback_url: https://web.archive.org/web/20151224234040id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-manifest-2015-02-13
  captured_at: '2015-12-24 23:40:40+00'
  template: drupal
  sha256: bbb6e53a363dff75e78e021b84f946ca31aa60aa8e1c35f57f95a8e7f5263c5e
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 1
---
It's Manifest Week on DailyMTG.com, and to end the week, I'm going to talk a bit about how the mechanic came to be and what we are expecting out of it in Limited and Constructed.

# Setting the Stage

You may have noticed that between *Theros* block, *Magic 2015*, and *Khans of Tarkir*, there are a total of two blink effects (also called flicker effects), and neither of them are really Constructed-power leveled. This wasn't a coincidence, it was something that design asked that we do in order to set up morph/manifest (recruit in playtesting), and so that they wouldn't be constrained with their designs because blink would allow for "cheating" of morph costs.

Now, before people get all up in arms by looking at the morphs in Khans and how development thought they would be broken with blink effects—this rule was put into place long before we knew what those morphs would even look like. Since we were returning to morph for the third time, design tried a lot of really crazy variants on the mechanic. We didn't want to put the kibosh onto things before design had time to explore whether something would even be fun or interesting—like a creature that is huge, but can't be cast except by turning it face up.

In the end, controlling for how good a blink effect is with a morph is really easy. Perhaps there are "busted" things like blinking [Akroma, Angel of Fury](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%2C+Angel+of+Fury), but those kinds of effects are easy to figure out and plan for.

In all honesty, manifest was the mechanic variant we were actually the most concerned about when it came to blinking, and ultimately why we made sure to keep cards like [Cloudshift](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloudshift) out of Standard at the same time. We can easily control for what creatures can have Morph on them, but when going out into the larger arena of manifest, we all of a sudden need to be worried about every expensive creature or other permanent in the game.

![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=247358&type=card)![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=240006&type=card)

Would we be happy if there was a deck that cast a manifest spell on turn two, then blinked in an enchantment like [Omniscience](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Omniscience), or even just a Planeswalker? It might be interesting, but it could easily get out of hand. A big part of development is deciding where to take risks, and where to play it safe, and blinking with manifest felt like something that might be fun in Modern, but would constrain our designs too much for Standard.

Of course, at the time, a lot of the recruiting wasn't from the top of the library—but from hands, graveyards, and libraries—so there were more dangers in being able to randomly blink those creatures. Most of those effects changed to being to the top of the deck, because we found the mystery to be the most fun part. In hindsight, it's possible we played the whole "manifest/blink" thing too conservatively, but that's coming at it with a lot of extra knowledge that we didn't have at the time, and I'm glad we took the position we did when we did.

# A Revolution in Turning Up

Probably the most important thing that took manifest from a risky mechanic that seemed to not be worth it to something really fun in Limited with Constructed applications happened pretty late in the design process. The earliest versions of manifest actually didn't involve a cost to turn the permanents face up. The idea was that the permanents would be locked as 2/2s unless they had morph (which is one of the reasons we had manifest from hand, library, and graveyard—to make this actually work).

To compensate, *Fate Reforged* was full of gating effects and the like that would let you "rescue" good cards that were manifested, while leaving your lands or otherwise unexciting things in their 2/2 form. Conceptually this worked, but it was pretty unsatisfying as a mechanic. After playtesting Khans/Khans/Fate Sealed, it was obvious that the number of times that a manifested card actually turned face up was basically nil. It led to people treating manifested creatures as if they had no text, because for all intents and purposes, they didn't.

I'm not sure if it was Dave or Ken who first came up with the idea, but I remember Dave championing the idea that you could turn up a manifested creature for paying its mana cost. There was some skepticism due to the amount of complexity it added to the set, but after playing with it and getting blown out by a manifest creature, it was pretty obvious that it was a huge improvement to the mechanic. We had to do a quick check through the FFL to make sure we didn't have any rogue [Phyrexian Dreadnought](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Dreadnought) running around, but we didn't see anything that looked like it would tank the mechanic, so we moved forward.

As a side benefit, this change quickly allowed us to create manifest cards that would be powerful and fun in Constructed. Under the old paradigm, the odds of ever hitting a morph creature were pretty low, but all of a sudden it's possible that the manifested creature attacking on turn four could be a Polukranos, and it's something your opponent needs to respect. It led us down the path of making some of the more interesting cards in the set.

![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=3263&type=card)![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=373549&type=card)

# Manifesting in Limited

As I mentioned before, a big reason for the manifest change was to make the mechanic more interesting in Limited. Part of making a mechanic more interesting is creating a wider variety of gameplay within the different cards of the mechanic and making sure they play differently in concert with other cards in the set and on different board states.

The manifest Auras are, I think, a good example of how we creatively solved for some of the problems with manifest and created some really fun and powerful effects. If you look at the uncommon Auras, they are all pretty good on average, but they're not tremendous cards. I'd definitely pay 1WW for a 2/2 flying creature with lifelink, but the fun part comes in the fact that it might be something even better. Like flipping up a [Salt Road Patrol](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Salt+Road+Patrol) after being blocked in combat, or even just a [Disowned Ancestor](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disowned+Ancestor) in response to a removal spell. It's these little unexpected things that keep people guessing with the mechanic, and I think they add the right amount of randomness and fun to the whole package.

![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=391810&type=card)![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=391867&type=card)![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=391899&type=card)

I think we hit a really good spot with how manifest works in Fate/Khans/Khans Limited, and I think it will continue to Dragons/Dragons/Fate. The goal from the beginning was to make the mechanic play somewhat differently in each format, and while it ended up being a lot less than originally planned (and that's something I will explain in a future article), I think the relative values of the cards do change quite a bit.

# Manifesting in Constructed

Questions we always ask ourselves when working on a mechanic are "What would the Constructed-powered versions of this mechanic look like?" and "Would it be fun if we had Constructed-powered cards?" Some mechanics are easy—prowess, for example, has plenty of knobs and ways to make Constructed cards. Outlast was a mechanic we were less sure of, and the card that we thought might be close, [Herald of Anafenza](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Herald+of+Anafenza), seems to have missed the mark.

The change to manifest made it much easier for us to picture what kind of cards we could make that would be fun in Constructed. The first one that comes to mind is [Whisperwood Elemental](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whisperwood+Elemental). The goal would be to find a deck for it that had plenty of big creatures, but not to lose out too much on those creature's enters-the-battlefield effects (sorry [Siege Rhino](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Rhino), but you just aren't your best when a Whisperwood gets you out).

![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=391958&type=card)![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=386666&type=card)

For us, that meant RG Monsters, or a Temur deck, where the Whisperwood can get powerful creatures like [Stormbreath Dragon](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbreath+Dragon), Polukranos, or a plain-old [Savage Knuckleblade](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savage+Knuckleblade). The deck would probably look something like this:

#### Whisperwood Monsters

##### 

 ![](http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (27)

4 [Elvish Mystic](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BMystic%5D) 4 [Heir of the Wilds](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeir%5D+%5Bof%5D+%5Bthe%5D+%5BWilds%5D) 3 [Rattleclaw Mystic](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRattleclaw%5D+%5BMystic%5D) 3 [Yasova Dragonclaw](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYasova%5D+%5BDragonclaw%5D) 4 [Savage Knuckleblade](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSavage%5D+%5BKnuckleblade%5D) 4 [Polukranos, World Eater](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolukranos,%5D+%5BWorld%5D+%5BEater%5D) 2 [Stormbreath Dragon](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStormbreath%5D+%5BDragon%5D) 3 [Whisperwood Elemental](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhisperwood%5D+%5BElemental%5D) 

##### Sorcery (3)

3 [Crater's Claws](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrater%5D+%5BClaws%5D) 

##### Instant (6)

3 [Temur Charm](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemur%5D+%5BCharm%5D) 3 [Stubborn Denial](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStubborn%5D+%5BDenial%5D) 

##### Land (24)

4 [Frontier Bivouac](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrontier%5D+%5BBivouac%5D) 4 [Yavimaya Coast](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYavimaya%5D+%5BCoast%5D) 4 [Shivan Reef](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 4 [Wooded Foothills](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWooded%5D+%5BFoothills%5D) 1 [Mana Confluence](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 2 [Mountain](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Forest](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 1 [Island](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

60 Cards 

##### Blue (3)

3 [Stubborn Denial](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStubborn%5D+%5BDenial%5D) 

##### Red (5)

2 [Stormbreath Dragon](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStormbreath%5D+%5BDragon%5D) 3 [Crater's Claws](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrater%5D+%5BClaws%5D) 

##### Green (21)

4 [Elvish Mystic](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BMystic%5D) 4 [Heir of the Wilds](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeir%5D+%5Bof%5D+%5Bthe%5D+%5BWilds%5D) 3 [Rattleclaw Mystic](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRattleclaw%5D+%5BMystic%5D) 3 [Yasova Dragonclaw](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYasova%5D+%5BDragonclaw%5D) 4 [Polukranos, World Eater](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolukranos,%5D+%5BWorld%5D+%5BEater%5D) 3 [Whisperwood Elemental](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhisperwood%5D+%5BElemental%5D) 

##### Multi colored (7)

4 [Savage Knuckleblade](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSavage%5D+%5BKnuckleblade%5D) 3 [Temur Charm](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemur%5D+%5BCharm%5D) 

##### Colorless (24)

4 [Frontier Bivouac](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrontier%5D+%5BBivouac%5D) 4 [Yavimaya Coast](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYavimaya%5D+%5BCoast%5D) 4 [Shivan Reef](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 4 [Wooded Foothills](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWooded%5D+%5BFoothills%5D) 1 [Mana Confluence](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 2 [Mountain](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Forest](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 1 [Island](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

60 Cards 

##### 1 (10)

4 [Elvish Mystic](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BMystic%5D) 3 [Crater's Claws](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrater%5D+%5BClaws%5D) 3 [Stubborn Denial](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStubborn%5D+%5BDenial%5D) 

##### 2 (7)

4 [Heir of the Wilds](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeir%5D+%5Bof%5D+%5Bthe%5D+%5BWilds%5D) 3 [Rattleclaw Mystic](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRattleclaw%5D+%5BMystic%5D) 

##### 3 (10)

3 [Yasova Dragonclaw](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYasova%5D+%5BDragonclaw%5D) 4 [Savage Knuckleblade](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSavage%5D+%5BKnuckleblade%5D) 3 [Temur Charm](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemur%5D+%5BCharm%5D) 

##### 4 (4)

4 [Polukranos, World Eater](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolukranos,%5D+%5BWorld%5D+%5BEater%5D) 

##### 5 (5)

2 [Stormbreath Dragon](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStormbreath%5D+%5BDragon%5D) 3 [Whisperwood Elemental](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhisperwood%5D+%5BElemental%5D) 

36 Cards 

##### Common (11)

4 [Elvish Mystic](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BMystic%5D) 2 [Mountain](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Forest](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 1 [Island](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

##### Uncommon (14)

4 [Heir of the Wilds](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeir%5D+%5Bof%5D+%5Bthe%5D+%5BWilds%5D) 3 [Temur Charm](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemur%5D+%5BCharm%5D) 3 [Stubborn Denial](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStubborn%5D+%5BDenial%5D) 4 [Frontier Bivouac](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFrontier%5D+%5BBivouac%5D) 

##### Rare (26)

3 [Rattleclaw Mystic](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRattleclaw%5D+%5BMystic%5D) 3 [Yasova Dragonclaw](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYasova%5D+%5BDragonclaw%5D) 4 [Savage Knuckleblade](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSavage%5D+%5BKnuckleblade%5D) 3 [Crater's Claws](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCrater%5D+%5BClaws%5D) 4 [Yavimaya Coast](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BYavimaya%5D+%5BCoast%5D) 4 [Shivan Reef](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShivan%5D+%5BReef%5D) 4 [Wooded Foothills](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWooded%5D+%5BFoothills%5D) 1 [Mana Confluence](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BConfluence%5D) 

##### Mythic (9)

4 [Polukranos, World Eater](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolukranos,%5D+%5BWorld%5D+%5BEater%5D) 2 [Stormbreath Dragon](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStormbreath%5D+%5BDragon%5D) 3 [Whisperwood Elemental](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhisperwood%5D+%5BElemental%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Elvish+Mystic)

[Deal Another Hand](https://web.archive.org/web/20150213000000/http://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temur+Charm)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Stormbreath+Dragon)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Savage+Knuckleblade)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Temur+Charm)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Savage+Knuckleblade)

I'll admit that our FFL was much higher on the Temur decks as a whole than the real world has been—in particular [Temur Charm](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Temur+Charm) and [Stubborn Denial](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stubborn+Denial)—but I wouldn't be surprised to see a deck very much like this show up at a tournament Top 8 in the near future. Also, while missing out on the ETB triggers for creatures like [Siege Rhino](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Rhino) may be sad, I think the [Whisperwood Elemental](https://web.archive.org/web/20150213000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whisperwood+Elemental) would be more than home in an Abzan build.

That's it for this week. Join me next week on Latest Developments, when I'm going to talk about the role of the lead developer on a set and what makes that role so different than just being a team member.

Until next time,

Sam ([@samstod](http://www.twitter.com/samstod/))
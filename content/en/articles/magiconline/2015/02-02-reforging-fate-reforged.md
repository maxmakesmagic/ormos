---
id: z2c12gn1
kind: article
lang: en
path: /en/articles/magiconline/2015/02-02-reforging-fate-reforged
title: Reforging Fate Reforged
published: '2015-02-02'
column_slug: magiconline
column: Magic Online
authors:
- slug: alli-medwin-da9174fd
  name: Alli Medwin
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
    lang_detected: en
    capture_id: 111325
    url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
    captured_at: '2016-04-27 16:28:40+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
    lang_detected: en
    capture_id: 111325
    url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
    captured_at: '2016-04-27 16:28:40+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
    lang_detected: en
    capture_id: 111325
    url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
    captured_at: '2016-04-27 16:28:40+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
    lang_detected: en
    capture_id: 111325
    url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
    captured_at: '2016-04-27 16:28:40+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: z2c12gn1
  url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
  page_key: magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
  lang: en
  template: drupal
  captured_at: '2016-04-27 16:28:40+00'
  capture_id: 111325
  wayback_url: https://web.archive.org/web/20160427162840id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: z2c12gn1
  capture_id: 111325
  url: http://magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
  wayback_url: https://web.archive.org/web/20160427162840id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/reforging-fate-reforged-2015-02-02
  captured_at: '2016-04-27 16:28:40+00'
  template: drupal
  sha256: 48573e22eba4d883b5308058b81bb9a68c7c4d53945e33f732f4208e6084adfb
render_recovery: []
---
It’s a very exciting time to be a *Magic Online* player! The year is 735 CE, and the ancient Turkish khagan is about to construct a giant monument in Mongolia’s Orkhon Valley. And more importantly, we’re only 1,280 years away from launching the first set of the world’s greatest game, and…

…crap. Wait. Wait a second. We didn’t really go back in time. Only Sarkhan went back in time. And there aren’t dragons here. We’re in the wrong place. So hang on. Let me start over.

# Re-reforging *Fate Reforged*

It’s a very exciting time to be a *Magic Online* player! Every few months, when a new set comes out, it’s time to open those digital cards, explore some new strategies, and draft some new decks.

And as is tradition, let’s talk about some of the design work that went into bringing *Fate Reforged* to life on *Magic Online*. I’m the digital editor for *Magic Online*, and one of my primary responsibilities is to work with the programmers and designers on how we present a faithful game of *Magic* to you online. Like every other set, *Fate Reforged* brings with it a bunch of new mechanics. Some of them are twists on old mechanics, and each of them presented some level of challenge. So let’s jump in!

# Many Festive Manifests

At the employee Prerelease, I made a really poor attack just so I could get the raid benefit from [Howl of the Horde](https://web.archive.org/web/20150202000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howl+of+the+Horde) to triple an [Ethereal Ambush](https://web.archive.org/web/20150202000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ethereal+Ambush). I took the top six cards from my library and put them on the table between me and my opponent. I didn’t have enough manifest overlay cards , though, so we just had to remember that the face-down cards were manifested. This can be a real memory issue: which of these face-down cards are manifested and which were cast as face-down creatures via Morph?

In person, the physicality of the cards helps you recall what happened with them, so it’s easier to remember where you put the card down on the table. The battlefield on *Magic Online* dynamically updates, so you can’t rely on your memory of where you put a card. To solve this, from day one of planning the block’s implementation, we resolved to use the manifest overlays.

Similar to the text tweaks on the morph overlay, though, we wanted to take advantage of the digital medium to make life a little easier for *Magic Online* players. The reminder text you’ll see on your manifested cards is going to be somewhat different than on the manifest overlay cards you can pull out of a pack of physical *Fate Reforged*. Manifested cards with Morph (even you, [Zoetic Cavern](https://web.archive.org/web/20150202000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zoetic+Cavern)!) are clear that they can be turned up for their morph cost. Manifested creature cards (not you, [Zoetic Cavern](https://web.archive.org/web/20150202000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zoetic+Cavern)!) are clear about how they can be turned face up, and manifested creature cards with morph (still not you, [Zoetic Cavern](https://web.archive.org/web/20150202000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zoetic+Cavern)!) spell out that you can do either. And of course, manifested creatures that aren’t creature cards or have a morph cost won’t even be highlighted, because you can’t turn them face up at all.

![](http://media.wizards.com/2015/mtgo/MTGO_2-2-2015_img3.png)

Your opponent, on the other hand, won’t see any of this. All your opponent will be able to tell is if your face-down creature is manifested or cast as a face-down creature, and the order in which they showed up. And as an added bonus for *Magic Online* players, your opponent won't see if your face-down card is premium or not, though you’ll still see the foil treatment on a face-down premium card you control.

# Choose Khans or Dragons

There’s a little something special that we included for the six cards that have you choosing between Khans and Dragons. Check out the watermark on the card while it’s in your hand, then once you’ve made your choice, take another look. In your collection, in your hand, or anywhere else where a decision hasn’t been made, the watermark moves back and forth between the *Khans of Tarkir* expansion symbol and the expansion symbol for [the upcoming Dragons of Tarkir set](/en/articles/feature/2014/11-03-announcing-dragons-of-tarkir). Once you’ve chosen a side, the watermark “locks in” and won’t shift between the two possible futures anymore.

We’re exploring lots of ways to improve the look and feel of *Magic Online* going forward, and this versatile watermark came out of one of those explorations. This isn’t the time to go into detail about what the future will hold or when it will arrive—we’re still choosing between Khans or Dragons ourselves!—but these improvements are in the works. In the meantime, please enjoy the special treatment we were able to give to these six cards, so important to the story of *Fate Reforged*.

# Confusion in the Ranks

This might look familiar to some of you:

![](http://media.wizards.com/2015/mtgo/MTGO_2-2-2015_img1.png)

This was one of the early design decisions we made starting with *Magic 2015* that didn’t work out quite as well as we wanted. Our goal was noble: we wanted to reduce the number of clicks the opponent had to make in order to get through your Demon’s triggered ability. The opponent is suffering enough, there’s no point in prolonging it with a multi-stage process. So we presented players with this prompt box, and we highlighted creatures, intending for players to discover the ability to click on the creature itself to opt for the sacrifice option.

The consistent feedback we heard was that this was a miss. Players were looking for the “Sacrifice a Creature” button to choose that option, and that button was secretly hidden on every creature that they could sacrifice. It’s a design truism that if players need to decipher how to use your design with the tools you present them, the design is flawed.

To address this issue, we went back to the source material and found a tool that’s long been in *Magic*’s toolbox: reminder text. Experienced *Magic* players are used to ignoring reminder text that’s not relevant to them (and to reflect that, we’ve hidden it on cards except on zoom). The reason we have it at all, though, is that the first few times many players use a card or a mechanic, it teaches how to do the thing the players want to do. After the first few times, use becomes old hat, and it can once again be safely ignored.

Here’s the prompt box from the resolution of [Write into Being](https://web.archive.org/web/20150202000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Write+into+Being):

![](http://media.wizards.com/2015/mtgo/MTGO_2-2-2015_img2.png)

The game is asking you to manifest a card, and as a faithful translation of *Magic* the game asks you to do the same. The first time a player manifests a card, absent this reminder text, trying to figure out what to do next can pull the player out of the zen of the game. With it there, the game is telling you not only what it’s time to do, but how to do the thing that you just cast the spell to do.

Design is an iterative process, and it’s tricky—but very important—to get right.

Allison Medwin  
 Digital Editor, *Magic Online*
---
id: ec4d2ddf
kind: article
lang: en
path: /en/articles/makingmagic/2022/12-19-storm-scale-throne-of-eldraine-through-strixhaven-part-1
title: 'Storm Scale: Throne of Eldraine through Strixhaven, Part 1'
published: '2022-12-19'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
    lang_detected: en
    capture_id: 230608
    url: https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
    captured_at: '2024-05-18 01:29:48+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
    lang_detected: en
    capture_id: 230608
    url: https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
    captured_at: '2024-05-18 01:29:48+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
    lang_detected: en
    capture_id: 230608
    url: https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
    captured_at: '2024-05-18 01:29:48+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
    lang_detected: en
    capture_id: 230608
    url: https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
    captured_at: '2024-05-18 01:29:48+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: ec4d2ddf
  url: https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
  page_key: magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:29:48+00'
  capture_id: 230608
  wayback_url: https://web.archive.org/web/20240518012948id_/https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ec4d2ddf
  capture_id: 230608
  url: https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
  wayback_url: https://web.archive.org/web/20240518012948id_/https://magic.wizards.com/en/news/making-magic/storm-scale-throne-of-eldraine-through-strixhaven-part-1
  captured_at: '2024-05-18 01:29:48+00'
  template: contentful
  sha256: 1d4b8ce493c26ac28b9e7dfa15b8780fbe181c5c44ad45f65116234a307b11cf
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
Many years ago on my blog (Blogatog on [Tumblr](http://markrosewater.tumblr.com/)), I created the Storm Scale as a fun way to predict the likelihood of certain mechanics or other features returning to a premier set (something legal in Standard). I named it the Storm Scale after the mechanic storm, which I felt was unlikely to return to Standard. The scale became popular enough that I've done several Storm Scale articles for "Making *Magic*":

*   [*Khans of Tarkir* block](/en/articles/makingmagic/2016/12-20-storm-scale-khans-of-tarkir-block)
*   [*Ravnica* and *Return to Ravnica* blocks](/en/articles/makingmagic/2016/05-02-storm-scale-ravnica-and-return-to-ravnica)
*   [*Zendikar* and *Battle for Zendikar* blocks](/en/articles/makingmagic/2016/11-22-storm-scale-zendikar-and-battle-for-zendikar)
*   [*Innistrad* and *Shadows over Innistrad* blocks](/en/articles/makingmagic/2017/03-27-storm-scale-innistrad-and-shadows-over-innistrad)
*   [*Mirrodin* and *Scars of Mirrodin* blocks](/en/articles/makingmagic/2018/06-11-storm-scale-mirrodin-and-scars-of-mirrodin-blocks)
*   [*Kaladesh* and *Amonkhet* blocks](/en/articles/makingmagic/2019/03-25-storm-scale-kaladesh-and-amonkhet)
*   [*Theros* block and *Theros Beyond Death*](/en/articles/makingmagic/2020/12-08-storm-scale-theros-and-theros-beyond-death)

In this column, I look back at the mechanics from two years' worth of premier sets: *Throne of Eldraine*, *Ikoria: Lair of Behemoths*, *Zendikar Rising*, *Kaldheim*, and *Strixhaven: School of Mages* (I left out *Theros Beyond Death* as I'd already done it in [a previous Storm Scale article](/en/articles/makingmagic/2020/12-08-storm-scale-theros-and-theros-beyond-death)). The Storm Scale is a scale from 1 to 10, with 1 meaning the mechanical item is very likely to return and 10 meaning the item is very unlikely to return. Here's what each point means on the scale:

* * *

**Level 1: Will definitely see again, most likely in the next set**

Examples: flying, deathtouch, scry

* * *

**Level 2: Will definitely see again, but not necessarily right away**

Examples: cantrips, hybrid mana, double-faced cards

* * *

**Level 3: Will most likely do again, probably many times**

Examples: cycling, flashback, landfall

* * *

**Level 4: Will most likely do again, but they have issues that make them less of a guarantee**

Examples: morph, convoke, exalted

* * *

**Level 5: We need to find the right place to bring it back, but I'm optimistic**

Examples: evolve, monstrous, morbid

* * *

**Level 6: We need to find the right place to bring it back, but I'm a little less optimistic**

Examples: devour, ninjutsu, living weapon

* * *

**Level 7: It's unlikely to return, but possible if the right environment comes along**

Examples: snow mana, retrace, split second

* * *

**Level 8: It's unlikely to return, but possible if the stars align**

Examples: madness, echo, suspend

* * *

**Level 9: I never say never, but this would require a minor miracle**

Examples: phasing, threshold, clash

* * *

**Level 10: I never say never, but this would require a major miracle**

Examples: storm, dredge

* * *

Next, here are the five criteria I use to determine where mechanics fall on the Storm Scale:

**Popularity** – Did players like this mechanic? The more players like something, the more likely we are to bring it back. The less they like it, the less likely its return. This metric is mostly covering the "was it fun?" question. This lens will have one of four potential labels:

*   **Very Popular** – This means that through our market research, this mechanic falls in the top 25% of mechanics of all time. Note that all these categories are comparing the current mechanics against the mechanics of all time (well, since we started doing market research many years ago), so getting in this top section is difficult.
*   **Popular** – This means that through our marketing research, this mechanic falls above the average but not in the top 25%.
*   **Liked** – This means that through our research, this mechanic falls below average but not in the bottom 25%. I should note that we aim for our average to be well liked, so being below average doesn't mean most players don't like it, just that there are other mechanics they like more. Being in this category doesn't stop things from having a chance to return.
*   **Unpopular** – This means that our research puts this mechanic in the bottom 25%. Falling in this last section does decrease the chance of a return.

**Design Space** – How many more cards could we design with this mechanic? Design space is important because if we can't make more cards, it doesn't matter how much players like it or how easy it is for development to balance. This lens will have three labels:

*   **Large** – This means that this mechanic has lots and lots of design space. We can bring it back again and again and most likely won't have any issues making new cards.
*   **Medium** – This means that this mechanic has a decent amount of design space and we could easily bring it back, but possibly a limited number of times.
*   **Small** – This mechanic is pushing the boundaries of its design space in this set. It would be difficult to make enough new cards to bring it back.

**Versatility** – How well does this mechanic mix and match with other mechanics? Does this mechanic require a lot of infrastructure or does it require minimal support? In short, does this mechanic make design easier or harder? This lens has three labels:

*   **Flexible** – This mechanic is easy to use, requires minimal support, and interconnects easily with other mechanics.
*   **Neutral** – This mechanic is a bit harder to use, often requires some support, and/or has issues when connecting to other mechanics.
*   **Rigid** – This mechanic is very hard to use, requires extensive infrastructure to work, and/or is actively hostile when trying to mix with other mechanics.

**Development/Play Design** – How easy is this mechanic to cost? How easy is it to balance? How easy is it to make this mechanic? This lens looks at whether the mechanic can be easily developed and balanced. This lens has three labels:

*   **Not Problematic** – Easy to develop. No major challenges for play design to overcome.
*   **Neutral** – There are challenges in play design that require special care in testing and development. Most mechanics fall into this category.
*   **Problematic** – There are major challenges in play design. It may cause us to pull back on the theme, erring on the side of less impact in Constructed.

**Playability** – Did players have problems understanding this mechanic, both in how it worked and how it interacted with other mechanics? Was the mechanic logistically hard to use? Did it have memory issues? Does it require a play aide? This lens looks at whether the mechanic had some barrier that made it harder to play. This lens has two labels:

*   **Playability Not Affected** – This means the mechanic had no issues interfering with playing it.
*   **Playability Affected** – This means the mechanic had one or more issues that interfered with playing it.

As always, I want to stress that the Storm Scale is just my opinion and done for fun and I don't use any advanced knowledge in predicting things. For example, I might know we're doing mechanic X in two years, but I'm predicting not using that information as a certainty.

With that explained, it's time to start grading mechanics.

* * *

## **Adamant (*Throne of Eldraine*)**

Rally for the ThroneForeboding FruitOnce and Future

**Popularity: Unliked**

Adamant was just barely in the bottom fourth, but I would say more that people aren't bothered by it as much as they like it. It was a workhorse mechanic that mattered a little in Limited and almost not at all in Constructed. I don't think it would upset most players if it returned, but very few are eager for it. Only a handful of players have ever asked for its return.

**Design Space: Medium**

This is one of those mechanics that seems to have more design space than it does, not because you couldn't make cards with it, but it's a bit trickier to make cards that will play well with it. Also, it has a challenging "delta." That's the term R&D uses to talk about the power level difference between the two states of a card. Because adamant is a bit harder to do, it gets a larger delta, and there's a little less design space for larger deltas. It's fine if the effect has a number but trickier when it's not number based.

**Versatility: Neutral**

The mechanic would only go in a set with a monocolor theme, which isn't something we do a lot. That said, the mechanic doesn't require much beyond having a mana base that supports it, which is less of an ask than many other mechanics.

**Development/Play Design: Neutral**

For all my answers in this category today, I talked with Andrew Brown, who's in charge of the Play Design team. Andrew said that adamant had three challenges. One, you must have the mana bases correct to test it properly. Monocolor themes are harder on mana needs than you might think at first blush. Two, it's a lot trickier to make cards with adamant work in decks with more than one color. Three, it's hard to balance because of the higher deltas.

**Playability: Playability Not Affected**

There are no rules issues, memory issues, logistics issues, and outside play aides required.

**Storm Scale: 7**

The biggest strike against this mechanic is that it just doesn't have that many fans. It has a few challenges, but nothing we couldn't do if we wanted. The best chance for this to return is a set with a monocolor theme where it just exactly fills the roll we need.

* * *

## **Adventures (*Throne of Eldraine* and *Commander Legends: Battle for Baldur's Gate*)**

![Brazen Borrower](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=473001&type=card) ![Murderous Rider](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=473059&type=card) ![Bonecrusher Giant](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=567598&type=card)

**Popularity: Very Popular**

Adventure is one of the best rated mechanics of all time. Players absolutely adore it. (In general, cards that are basically two spells are well liked.)

**Design Space: Large**

Adventure is a very open-ended mechanic design-wise. *Throne of Eldraine* only put it on creatures, but as *Battle for Baldur's Gate* demonstrated, it can go on any permanent. The best adventurer cards tell a fun story, but there are many different types of stories you can tell. The biggest restriction design-wise is that you don't have a lot of rules text, especially for the Adventure spell itself.

**Versatility: Neutral**

You could just throw an adventurer card in any set, but if you want to make them more integral to the design, it requires a little bit of structural support, often with cards that call out Adventures by name.

**Development/Play Design: Neutral**

Andrew says the balancing of adventurer cards is more time-consuming than difficult. There are plenty of numbers to play with (the mechanic has a lot of what we call "knobs," things that can be adjusted to balance a card, usually numbers). The biggest challenge during play design is the same one we have during vision design and set design, there's just not a lot of rules-text space, meaning there's less flexibility in how to tweak an effect.

**Playability: Playability Not Affected**

Adventures come with a little bit of rules baggage, but luckily things that don't come up too often. It doesn't require any play aides but can have a little bit of a memory issue in that you have to remember that the spell is in exile and can be cast. This is on the line, but I've dubbed it "not affected."

**Storm Scale: 3**

This is a home run mechanic that the players adore. Yes, it comes with a little bit of work on the design side, but nothing we can't handle. This is a mechanic I expect to keep returning.

* * *

## **Food Tokens (*Throne of Eldraine*, *Commander (2021 Edition)*, *Modern Horizons 2*, *Streets of New Capenna*, and *Unfinity*)**

![Food token](https://media.wizards.com/2019/eld/en_8MSslzedLY.png) ![Food token](https://media.wizards.com/2019/eld/en_zSLS0TURcJ.png) ![Food token](https://media.wizards.com/2019/eld/en_4OwNtoBgbf.png)

**Popularity: Liked**

Food tokens fall just below the line between the top half and the bottom half of the ratings. Players seem to like the flavor of the token, but it's not something players seem to adore or loathe.

**Design Space: Large**

Artifact tokens are easy to design as they can be the byproduct of many different things. Food tokens want to be as flavorful as possible (pun, as always, intended), which makes their design a little more challenging but doesn't really cut off design space.

**Versatility: Flexible**

Life gain is about as universal as things come, so it's never hard to make Food tokens matter.

**Development/Play Design: Neutral**

Life gain can slow down gameplay if not carefully used, so Play Design must ensure that it's not just about adding life to the game. This usually means ensuring there are other ways to make use of Food tokens, which creates difficulties for Play Design. The more you have in the set, the trickier it is to balance.

**Playability: Playability Affected**

Food tokens are tokens, so the player must find a way to represent them. They're straightforward other than that, though.

**Storm Scale: 2**

Food tokens are so flavorful (again, pun intended) that they're very easy to want to include in many sets. We've made them deciduous, so I expect to see them a lot in the future. I should note that the token cost (having to make a token that will appear in the set, and all the mind space that comes along with having a noncreature token) will make us think twice before including it, so it's not something I think will show up too frequently.

* * *

## **Companion (*Ikoria: Lair of Behemoths*)**

Yorion, Sky NomadJegantha, the WellspringLurrus of the Dream-Den

**Popularity: Unpopular**

Companion has one of the lowest rankings of any mechanic since we started doing ratings. Part of this was that we made a huge mistake balancing them and they were causing problems across almost all Constructed formats.

**Design Space: Small**

Companions require effects that are interesting to build around while being something the opponent can monitor to make sure you're following the limitation. We made ten in *Ikoria* and were already running out of available space, so I'm dubious how much space remains for this mechanic.

**Versatility: Neutral**

Companions don't have a lot of structural needs (i.e., you could just throw one in any set), but usually you want to make sure that what you're asking for has some support in the set, especially if you do some at uncommon, which will impact Limited.

**Development/Play Design: Problematic**

Never have we needed to revise an entire mechanic for power-level concerns, so that's a pretty good indication that this is a troublesome mechanic. Andrew has two main concerns about the mechanic: one, the real world has much better deck-building efficiency because there are millions of players, and two, the mechanic has so many variables to monitor. It's one of the hardest mechanics we've ever made to properly balance.

**Playability: Playability Affected**

There are rules issues, memory issues, logistical issues. It makes the opponent feel they must carefully monitor what's in the other player's deck. It's a mechanic with a lot of baggage.

**Storm Scale: 9**

I should probably give companion a 10. It's unpopular, has little design space, and is hard to balance, but it's a mechanic that I get asked about a lot (I believe the ratings don't totally reflect the public's interest), and I'd like to believe if the perfect opportunity arose, we'd at least think about it.

* * *

## **Cycling (*Urza's Saga* block, *Onslaught* block, *Time Spiral* block, *Shards of Alara* block, *Amonkhet* block, *Modern Horizons*, *Ikoria*, and *Streets of New Capenna*)**

Shark TyphoonYidaro, Wandering MonsterKetria Triome

**Popularity: Popular**

Cycling is a beloved mechanic that has dropped over time in our ratings, not because players don't like it but because it's become familiar. It's no longer the sexy, new thing. Players are always happy to see it, though. This is a good place to point out that market research is a good tool to get a general sense of a mechanic, but there are issues that affect it that aren't indicative of whether players enjoy it.

**Design Space: Large**

Cycling has about as big of a design space as they come. It can go on any card type and can be tweaked a lot. I never worry about our ability to design new cycling cards.

**Versatility: Flexible**

A set could have just one cycling card or a whole theme for players to build around. The designers love cycling as it's very useful and can be added to just about any design.

**Development/Play Design: Neutral**

The experiment with a bunch of cycling 1 cards in *Ikoria* showed that there are ways to cause balance problems with cycling. The good news is that because we've used it so often, we have a pretty good understanding of how it interacts with other game elements.

**Playability: Playability Not Affected**

No major rules issues, no memory issues, no logistical issues, no play aides required. Cycling is easy to use.

**Storm Scale: 3**

As of *Streets of New Capenna*, cycling has become deciduous. I thought about moving it to 2, which is where most of the deciduous things live, but I decided to keep the deciduous named keyword/ability word mechanics at 3 as I don't think we use them on average quite as often as what I'll call the design tools.

* * *

## **Mutate (*Ikoria*)**

Sea-Dasher OctopusGemrazerNethroi, Apex of Death

**Popularity: Liked**

Mutate is very polarizing. The players who like it adore it, but there are a lot of players who simply aren't fans (probably because it's a complicated mechanic with odd rules interactions).

**Design Space: Medium**

Mutate is a good example of a mechanic with a lot of potential but far less that would lead to good gameplay. It does have a big enough design space that a future set could take it in a bit of a different direction.

**Versatility: Rigid**

You can't just throw one mutate card in a set. It requires a significant amount of infrastructure, and you have to care how all the mutate cards interact with the non-mutate cards.

**Development/Play Design: Neutral**

This was the one mechanic I was most surprised that Andrew didn't label it "problematic." He said that the biggest issue with making mutate cards isn't doing it within the "biosphere" of its Limited environment (that wasn't as hard as I had assumed) but getting it to interact with everything around it in sets that weren't designed with mutate in mind. The other big issue is that mutate is a bit of a rules nightmare, which can cause all sorts of weird interactions (which, of course, is tied to the difficulty of making it work with cards from other sets).

**Playability: Playability Affected**

Mutate is in contention for the most complex mechanic rules-wise we've ever made. A lot of players don't like it because they simply don't understand how it works in many practical situations.

**Storm Scale: 7**

This probably should be a little higher as it's a hard mechanic to wrangle, but it's a mechanic that's beloved by its fans, and it's something I'm asked about all the time. So, I'm eager to find a home for it but am aware that it's not going to be an easy thing to do (outside of a return to Ikoria).

* * *

## **Kicker (*Invasion* block, *Time Spiral* block, *Zendikar* block, *Dominaria*, *Modern Horizons*, *Modern Horizons 2*, *Zendikar Rising*, and *Dominaria United*)**

Maddening CacophonyScourge of the SkyclavesSkyclave Relic

**Popularity: Liked**

Kicker, much like cycling, has gone down in our ratings over time, but more for familiarity reasons than for any dislike of the mechanic.

**Design Space: Large**

Kicker has a humongous design space, larger than I assume *Magic* could ever do. It can go on any card type and has a lot of utility. My biggest issue with kicker is not what it can do but that we design it such that it doesn't step on the toes of other mechanics. I've talked at length in other columns and podcasts that with 20/20 hindsight, we might not have done kicker so broadly as a mechanic but chopped it up more so new mechanics didn't get the "that's just kicker" response for the audience.

**Versatility: Flexible**

You could have one kicker card in a set, or you could build themes around it. Kicker is as flexible a mechanic as they come.

**Development/Play Design: Not Problematic**

To quote Andrew: "It's easy. It's kicker."

**Playability: Playability Not Affected**

Kicker has no rules issues, no memory issues, no logistical issues, no play-aide issues. It's easy. It's kicker.

**Storm Scale: 3**

Kicker is easy to use and plays great. We will use it again and again.

* * *

## **Landfall (*Zendikar* block, *Battle for Zendikar* block, and *Zendikar* Rising)**

Moraug, Fury of AkoumNissa of Shadowed BoughsOmnath, Locus of Creation

**Popularity: Liked**

This is basically the same thing I said for cycling and kicker. Landfall was super popular when it premiered and is still well liked but slowly slipped down in rating as players have become more familiar with it. (I should note that its initial rating is up there with the best of all time.)

**Design Space: Large**

Okay, nowhere near as big as either cycling or kicker, but still big. It can go on every card type (although we've yet to do it on sorceries), but it works best on permanents.

**Versatility: Neutral**

Here's where landfall differs from cycling and kicker. It requires a bit more structural support. Usually, a set with landfall will add a few extra ways to trigger landfall. Also, the focus on playing lands has ripples on other parts of the design. For instance, it tends to lead to more mana, which makes you want more mana sinks than normal.

**Development/Play Design: Not Problematic**

We've spent a lot of time making landfall cards, so Play Design understands the nooks and crannies of how it interacts with other cards.

**Playability: Playability Not Affected**

It does require an extra attention to lands being played, so I had to think about how to grade this. Luckily, it's not something that's hard to pay attention to.

**Storm Scale: 3**

Landfall has also been upgraded to deciduous status, but I decided to keep deciduous named keywords/ability words at 3.

## "There's a Storm Scale a-Brewin'"

I was halfway through this article when I realized I was far from done, so I've decided to make it a two-parter. Note that Part 2 will publish in the new year on Tuesday, January 3, 2023. As always, I'm eager to hear your feedback about today's column and any of my ratings. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me in two weeks for Part 2 of this article.

Until then, may you have the happiest of holidays.
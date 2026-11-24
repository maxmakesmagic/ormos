---
id: 1pdnjn4r
kind: article
lang: en
path: /en/articles/latestdevelopments/2007/07-13-making-sealed-work
title: Making Sealed Work
published: '2007-07-13'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
    lang_detected: en
    capture_id: 727485
    url: https://magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
    captured_at: '2022-05-24 18:27:14+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
    lang_detected: en
    capture_id: 727485
    url: https://magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
    captured_at: '2022-05-24 18:27:14+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
    lang_detected: en
    capture_id: 727485
    url: https://magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
    captured_at: '2022-05-24 18:27:14+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
    lang_detected: en
    capture_id: 727485
    url: https://magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
    captured_at: '2022-05-24 18:27:14+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - 6fgrvgda
sources:
- document_id: 1pdnjn4r
  url: https://magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
  lang: en
  template: drupal
  captured_at: '2022-05-24 18:27:14+00'
  capture_id: 727485
  wayback_url: https://web.archive.org/web/20220524182714id_/https://magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
- document_id: 6fgrvgda
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af179
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af179
  lang: en
  template: aspx
  captured_at: '2009-06-18 06:46:43+00'
  capture_id: 780650
  wayback_url: https://web.archive.org/web/20090618064643id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af179
- document_id: 6fgrvgda
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af179
  page_key: wizards.com/default.asp?x=mtgcom/daily/af179
  lang: en
  template: classic_asp
  captured_at: '2008-03-24 15:01:12+00'
  capture_id: 1927436
  wayback_url: https://web.archive.org/web/20080324150112id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af179
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 1pdnjn4r
  capture_id: 727485
  url: https://magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
  wayback_url: https://web.archive.org/web/20220524182714id_/https://magic.wizards.com/en/articles/archive/latest-developments/making-sealed-work-2007-07-13-0
  captured_at: '2022-05-24 18:27:14+00'
  template: drupal
  sha256: 437836f46e8aa331d198cc88fbd6319a3d0395098610720e0b10c3a7b9846239
render_recovery: []
---
Just this week, I put together the department's [limited pointing](https://web.archive.org/web/20070713000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb5) for the upcoming "Jelly" set (the set coming out next summer; I'm leading the development team. You can read more about it this coming Monday in Mark Rosewater's column). Typically the first round of pointing is followed by a ton of reconfiguring of cards as the color balance is out of whack, but not this time! The dev team and I had made a big round of changes in the previous month after our initial Limited testing showed black and red to be too strong (a typical problem early in development—black and red get the best removal and the rest of the set needs to bend to accommodate that), and those changes, once quantified via pointing, showed the five colors to be of equivalent power level +/– less than 2%. It was a nice validation that I am indeed getting better at my job as the years go by.

[![Balance_of_Power](https://i.ormos.uk/d5/bb/d5bb2b97c9e0a4f318233212bdefb10cec1b3602d95d887cf263542b529f72c8.jpg)](https://web.archive.org/web/20070713000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Balance%2Bof%2BPower)Of course, just because the pointing showed that each color was balanced against the others in the abstract didn't mean we were done working on the set for Limited. We've been spending this week "curving" the set, meaning making sure each mana cost has enough cards per color. Curving usually involves tons of tiny tweaks and subtle shifts and is the real nitty-gritty of set development. If white and blue come out even in the pointing but all of white's cards cost one or two mana and all of blue's cards cost four or five mana, white will almost certainly beat blue a vast majority of the time in actual gameplay. Both of them would lose to a third color that pointed the same but had the correct curve of cards at all mana costs.

Even after we curve the set, the imminent Constructed playtesting that Jelly will undergo in the upcoming months will force us to make changes that will upset the limited balance again, forcing up to do all the pointing, adjusting, and curving all over again.

We go through all this mathematical rigmarole just to make sure that Sealed Deck play is fun for each set. Draft doesn't typically require a high level of precision on our part as it is a "self-correcting" format. If red and black were far and away the best colors in a draft format, many people at each draft table would try to force those colors, leaving the door open for those few that are drafting white, blue, and green to get decent decks. But if a roomful of people played Sealed Deck using the same card pool, it would be feasible for a huge percentage—maybe even all of them—to play black and/or red.

We don't want Sealed environments to be lopsided or "solvable." Each color should feel worthy of playing about the same percentage of the time as each of the other colors. Each color has its place in the game—and its fans—and we don't ever want any of them to feel "lesser" than any of the others.

### Systems Online

Whereas "Jelly" is still a year in your future, I imagine many of you will be experiencing a new Sealed Deck environment tomorrow at [**Magic** Game Day](https://web.archive.org/web/20070713000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/events/07gameday&dcmp=ILC-MTGDAILY) with *Tenth Edition*. Our Limited testing for *Tenth Edition* was done in an interesting new way—via **Magic Online**. Because most of the cards in the set were already coded online, we had Rachel Reynolds and Mike "elf" Feuell create the set on the internal online servers so that we could play Sealed Deck and draft the set whenever we wanted.

[Assassinate](https://web.archive.org/web/20070713000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Assassinate)Normally when testing Limited we use playtest stickers, but those have a ton of flaws. One, it takes lots and lots of time to print and affix the stickers to old cards. Two, we have to assemble our own boosters from scratch every time we want to play. Three, the cards just aren't very attractive (compared to real cards) and most people that aren't hardcore playtesters don't enjoy playing with them at all. Using **Magic Online** alleviated all these problems, although it isn't a tactile experience, which I consider a downside. A few other problems did arise, however, mainly due to the fact that Rachel and elf don't work in R&D and we're doing this work for us out of the kindness of their hearts. Not all the cards worked—it was weeks before [Treetop Village](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treetop+Village) and [Prodigal Pyromancer](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prodigal+Pyromancer) were functional, and weird rares like [Abundance](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Abundance) never worked at all. And we couldn't make changes on the fly the way we can with other sets—every alteration to the set had to be entered into Multiverse and then exported in **Magic Online**, something that happened only once or twice a week.

I consider the experiment of testing the core set online successful, although it showed me that testing expert-level sets online will probably never be a reality for us unless R&D were to hire a dedicated programmer that would do little else besides make sure the cards were are testing at the moment work on our internal MTGO server—a luxury that can't possibly be worth the hassle considering that there's really not that much wrong with our current system.

### Out with the Old

[Overrun](https://web.archive.org/web/20070713000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Overrun)With each core set, one of the development goals is to make sure that it plays differently than the previous one in Draft and Sealed Deck. To that end, here are some of the things you may notice about *Tenth Edition* tomorrow:

 

*   We rotated out some of the top-pick commons like [Dark Banishing](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing) and [Master Decoy](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+Decoy).
*   We swapped out some of the game-winning bomb uncommons like [Vulshok Morningstar](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vulshok+Morningstar) and [Flame Wave](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Wave) for different game-winning bomb uncommons like [Overrun](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun) and [Cone of Flame](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cone+of+Flame).
*   We swapped out a huge swath of basic cards like [Mending Hands](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mending+Hands), [Raise Dead](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raise+Dead), and [Shatter](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shatter) for cantrip versions ([Bandage](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bandage), [Recover](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recover), and [Smash](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smash)). While I don't think cantrips are the best learning tool, they do make gameplay better.
*   We replaced the UrzaTron lands—typically "dead" cards in Limited—with the very playable *Urza's Legacy* "man-lands" ([Treetop Village](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treetop+Village), [Ghitu Encampment](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghitu+Encampment), [Faerie Conclave](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Conclave), [Forbidding Watchtower](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forbidding+Watchtower), and [Spawning Pool](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spawning+Pool)).

All of these, in addition to the normal card rotation that we do each core set, add up to make *Tenth Edition* a real blast in Limited. Make sure you don't miss out—check out [**Magic** Game Day](https://web.archive.org/web/20070713000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/events/07gameday&dcmp=ILC-MTGDAILY) at your local store tomorrow!

### Get to the Point

What would an article from "Sealed Deck Week" be without a pointing exercise? [Randy Buehler](https://web.archive.org/web/20070713000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb6), [Noah Weil](https://web.archive.org/web/20070713000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/nw32), and [myself](https://web.archive.org/web/20070713000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af93) have all posted similar articles before wherein we ask you to point cards for Limited play. I'll follow this article up with a discussion of the results and a look at how R&D pointed the same cards next week.

I'll give you, once again, the relevant section from our developers' handbook and then set you loose. Things to remember are:

 

*   The scale goes from 0 to 5.
*   There have been historically very few 5s ([Masticore](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Masticore), [Umezawa's Jitte](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa%27s+Jitte), [Skullclamp](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullclamp)). Anything above a 4 is a certified bomb.
*   The average rating across a whole set should be about 1.6.

The cards you get to point are from *Tenth Edition*. Tune in next week for the results!

> *...\[H\]ere is the fundamental definition of our rating: Given that this is the first card you see (of your 75-card sealed deck or first pack, first pick in draft), how happy are you—on a scale of 0.0 - 5.0—to see it? Furthermore, your ratings should be linear (that is, you'd be just as happy with a 3.5 and a 2.5 or with two 3.0's). Also, to be technically correct, this all assumes that your goal is to win—winning makes you "happy."*
> 
> *The following elaborations of this scale are merely guidelines, designed to clarify the scale defined above:*
> 
> ***5.0**: I will always play this card. Period.*
> 
> ***4.5**: I will almost always play this card, regardless of what else I get.*
> 
> ***4.0**: I will strongly consider playing this as the only card of its color.*
> 
> ***3.5**: I feel a strong pull into this card's color.*
> 
> ***3.0**: This card makes me want to play this color. (Given that I'm playing that color, I will play this card 100% of the time.)*
> 
> ***2.5**: Several cards of this power level start to pull me into this color. If playing that color, I essentially always play these. (Given that I'm playing that color, I will play this card 90% of the time.)*
> 
> ***2.0**: If I'm playing this color, I usually play these. (70%)*
> 
> ***1.5**: This card will make the cut into the main deck about half the times I play this color. (50%)*
> 
> ***1.0**: I feel bad when this card is in my main deck. (30%)*
> 
> ***0.5**: There are situations where I might sideboard this into my deck, but I'll never start it. (10%)*
> 
> ***0.0**: I will never put this card into my deck (main deck or after sideboarding). (0%)*
> 
> *Those guidelines break down for artifacts and gold cards—fall back onto the fundamental definition when rating these categories of cards: the happiness scale.*

<table><tbody><tr><td> </td>&#10;			<td><b>Common</b></td>&#10;			<td><b>Uncommon</b></td>&#10;			<td><b>Rare</b></td>&#10;		</tr><tr><td><b>White</b></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Griffin">Wild Griffin</a>, <a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism">Pacifism</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel+of+Mercy">Angel of Mercy</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Righteousness">Righteousness</a></td>&#10;		</tr><tr><td><b>Blue</b></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloud+Sprite">Cloud Sprite</a>, <a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel">Cancel</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer">Puppeteer</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcanis+the+Omnipotent">Arcanis the Omnipotent</a></td>&#10;		</tr><tr><td><b>Black</b></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Assassinate">Assassinate</a>, <a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dusk+Imp">Dusk Imp</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Tears">Rain of Tears</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare">Nightmare</a></td>&#10;		</tr><tr><td><b>Red</b></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate">Incinerate</a>, <a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smash">Smash</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cone+of+Flame">Cone of Flame</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Manabarbs">Manabarbs</a></td>&#10;		</tr><tr><td><b>Green</b></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth">Giant Growth</a>, <a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kavu+Climber">Kavu Climber</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enormous+Baloth">Enormous Baloth</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hurricane">Hurricane</a></td>&#10;		</tr><tr><td><b>Colorless</b></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse">Terramorphic Expanse</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Stone">Mind Stone</a></td>&#10;			<td><a href="https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Platinum+Angel">Platinum Angel</a></td>&#10;		</tr></tbody></table>

[Wild Griffin](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Griffin)  
[Pacifism](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism)  
[Angel of Mercy](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel+of+Mercy)  
[Righteousness](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Righteousness)  
[Cloud Sprite](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloud+Sprite)  
[Cancel](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel)  
[Puppeteer](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer)  
[Arcanis the Omnipotent](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcanis+the+Omnipotent)  
[Assassinate](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Assassinate)  
[Dusk Imp](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dusk+Imp)  
[Rain of Tears](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Tears)  
[Nightmare](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare)  
[Incinerate](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate)  
[Smash](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smash)  
[Cone of Flame](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cone+of+Flame)  
[Manabarbs](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Manabarbs)  
[Giant Growth](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)  
[Kavu Climber](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kavu+Climber)  
[Enormous Baloth](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enormous+Baloth)  
[Hurricane](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hurricane)  
[Terramorphic Expanse](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse)  
[Mind Stone](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Stone)  
[Platinum Angel](https://web.archive.org/web/20070713000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Platinum+Angel)

### Last Week's Poll:

<table><thead><tr><td colspan="3"><b>What team format would you rather see at the Pro Tour and PTQs?</b></td>&#10;		</tr></thead><tbody><tr><td>2HG limited</td>&#10;			<td>2304</td>&#10;			<td>35.0%</td>&#10;		</tr><tr><td>2HG constructed</td>&#10;			<td>2136</td>&#10;			<td>32.5%</td>&#10;		</tr><tr><td>There shouldn't be team play at that level</td>&#10;			<td>861</td>&#10;			<td>13.1%</td>&#10;		</tr><tr><td>Three-person constructed</td>&#10;			<td>647</td>&#10;			<td>9.8%</td>&#10;		</tr><tr><td>Three-person limited</td>&#10;			<td>629</td>&#10;			<td>9.6%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>6577</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

All of this input will be taken into consideration prior to the finalization of next year’s schedule.
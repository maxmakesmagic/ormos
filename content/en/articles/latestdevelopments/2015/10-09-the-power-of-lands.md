---
id: baqygc6g
kind: article
lang: en
path: /en/articles/latestdevelopments/2015/10-09-the-power-of-lands
title: The Power of Lands
published: '2015-10-09'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
    lang_detected: en
    capture_id: 729818
    url: http://magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
    captured_at: '2016-04-29 20:07:48+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
    lang_detected: en
    capture_id: 729818
    url: http://magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
    captured_at: '2016-04-29 20:07:48+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
    lang_detected: en
    capture_id: 729818
    url: http://magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
    captured_at: '2016-04-29 20:07:48+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
    lang_detected: en
    capture_id: 729818
    url: http://magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
    captured_at: '2016-04-29 20:07:48+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: baqygc6g
  url: http://magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
  page_key: magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
  lang: en
  template: drupal
  captured_at: '2016-04-29 20:07:48+00'
  capture_id: 729818
  wayback_url: https://web.archive.org/web/20160429200748id_/http://magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: baqygc6g
  capture_id: 729818
  url: http://magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
  wayback_url: https://web.archive.org/web/20160429200748id_/http://magic.wizards.com/en/articles/archive/latest-developments/power-lands-2015-10-09
  captured_at: '2016-04-29 20:07:48+00'
  template: drupal
  sha256: 99241cb30e21fd1e628310e8d80305f1584f9f19155c5ae5acf5cb25688cee6e
render_recovery: []
---
In the beginning there were basic lands, and they were good. There were dual lands as well, and they were also good. Strong, but good. By the time *Arabian Nights* came along, there was some obvious design space for lands that did something other than just add colors of mana. Perhaps some could add only colorless mana, then have another small ability to make up for it. These lands would offer a trade-off where you might risk not being able to cast your spells, but you could also use the land's utility sometimes. Of course, like many things in the early days of *Magic*, the power level may have been slightly off the mark.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Library+of+Alexandria)](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Library+of+Alexandria)

Fortunately, the designers of *Antiquities* had the perfect answer for such a powerful land, and it could be used in any deck.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Strip+Mine)](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strip+Mine)

Yeah, about that . . . I will at least say that I believe we have come a long way since then. Lands are still some of the more powerful cards in our sets, but I think they are powerful in a much more reasonable and responsible way. Today in Latest Developments, I'm going to talk a bit about how we make them.

# Making Dual Lands

The first question you might have is, "Why do we have dual lands?" A big part of their function is to manage the amount of variance that we have in our game, and increase the likelihood that people play multicolored decks. We want to minimize the percentage of games in Constructed wherein the result is decided by a player being mana hosed when they're playing a reasonable amount of colors. While there is some value in formats that reward people for playing monocolored, if that goes too far then there will just not be enough variety in the metagame as a whole. Mechanics like devotion can push monocolored decks, but in a way that rewards you for making the choice as opposed to just punishing you for having the audacity to try and cast your spells in more than one color. It's a balancing point, though, since we want to make it suitably difficult to cast your spells. In some environments (like *Khans of Tarkir*), we go out of our way to let you cast three-color spells. In most, we don't—and want decks to mostly be two-color, with options for people to go into three colors if they don't mind taking a few risks.

The absolute bottom line for dual lands at this point in Standard *Magic* is the [Elfhame Palace](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elfhame+Palace) cycle—lands that enter the battlefield tapped and whose "only" advantage is that they tap for two colors of mana. While we have lands close to that in Standard most of the time, we don't consider them a necessity to get a two-color deck to work. If everyone’s decks are running them, then something is going wrong. The level that is too high is the *Alpha* dual land cycle that (barring nonbasic land hate or [Choke](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choke)s) has no disadvantages when compared to basic lands. The entirety of all dual lands that we print in Standard fall in between these two cycles. That is a pretty small range when you get down to it, and one that requires a lot of work. We want to ensure we create lands that allow players to smooth out their mana, but not so much that players feel like they can easily play five-color decks without making some very large concessions.

As a whole, development tries to plan dual land cycles years in advance because of how difficult they are to work on, and because they impact a lot about Standard in the sets around them. For example, knowing that we wanted to come back to Zendikar meant that we wanted to have fetch lands in a set that didn't overlap with landfall, and that we should do the enemy color creature lands. So we avoided creature lands in the *Theros* and *Khans* blocks. We also would have a lot of utility lands in a return to Zendikar, so we avoided any creature lands for the years leading up to *Battle for Zendikar*. Because we included the *Zendikar* enemy dual lands that entered the battlefield tapped, we decided to also have a cycle of enemy duals that didn't enter tapped (hence the enemy color pain lands). And since the fetch lands fixed allied color mana untapped, the cycle of dual lands in *BFZ* enters the battlefield tapped on the first turn.

That is just a glimpse of the level of planning that goes into the dual lands for Standard, before we even get close to designing the actual lands. Once we know the parameters, then we can start making the right lands for the set. There are two basic varieties of dual lands that we make in Standard-legal sets: lands that enter the battlefield untapped but have a drawback, or lands that enter the battlefield tapped and have some advantage. If possible, we would like to use a set mechanic on those lands to maintain variety (like the scry lands), but it is rarely the case that those line up.

![](http://media.wizards.com/2015/images/daily/c4rd4r7_6TOB6TuQWl.jpg)

[Sunken Hollow](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=402051) | Art by[Adam Paquette](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Adam+Paquette%22%5d)

It's very important for development to get these lands correct as soon as possible, because of just how large of an impact they have on Standard. We have a limited amount of time to test a set in the Future Future League, and a huge part of what makes different archetypes work in Standard is their mana base. Imagine a world where we put the *Scars of Mirrodin* fast lands in *Battle for Zendikar* instead of the lands we used. Beyond just not being searchable, they would reward basics and fetch lands in very different ways, and also make the mana bases for our three-color decks quite different. If we spend a lot of time trying to balance a format around those and suddenly swap them for the *Ravnica* shock lands, we have invalidated a ton of testing. Not only would cards that we had identified as fine now possibly be too strong, but there may also be other cards that are now too weak. We can make some pretty minor tweaks to lands over time, but getting something close in power and function is important for gameplay.

# Utility Lands

Of course, dual lands are not the only lands that we print in our sets; we also have lands that don't fix mana but still provide a wide variety of upsides. The most basic version of those is usually a land that taps for colorless mana but has a high-mana, low-impact activated ability. We also provide lands that tap for one color and have an extra ability on top, but enter the battlefield tapped. *Battle for Zendikar*, being a Zendikar set, has a wide variety of these—from the common lands with enters-the-battlefield triggers, the uncommon cycle of lands that sacrifice with colored mana for a spell effect, and a variety of rare lands that have both utility and extra mana production.

We make these lands to help mitigate another aspect of *Magic*'s resource system that people get frustrated with: mana flood. One of the advantages of *Magic*'s system, which randomizes how many lands people draw over the course of the game, is that it creates interesting decisions on how to make your mana curve. Run more lands and cards higher up, or end your curve at three or four mana and play fewer lands? Even if you make reasonable choices here, you can end up getting draws that do not suit your deck—and utility lands trade some of the reliability of basic or even dual lands for, well, utility. Most commonly, these lands are there to push people toward playing more lands, or at least giving people who flood out some extra utility. Occasionally, we print cards like Ally Encampment that act kind of like a dual land, but also work toward pushing one particular type of deck.

![](http://media.wizards.com/2015/images/daily/c4rd4r7_NlqBS1Kf87.jpg)

[Ally Encampment](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ally+Encampment) | Art by [Jonas De Ro](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Jonas+De+Ro%22%5d)

If you look at many early *Magic* sets, it was obvious that the designers had not correctly gauged the level of power these lands provide through replacement value. By that, I mean how much better is your deck if you replace one of your basic lands with this card? What about the second copy? The third? What about the next land? If mana bases are made up of zero lands that don't do something, and not because your deck is being very ambitious on what it is trying to cast, then I think we probably have a problem.

In the old days, simply being a legendary land was a downside—so that was often used on lands that were in every other way superior to basic lands. It worked (despite being a bit hokey), because there would be games where your opponent would play one first, which would then make the land a huge downside for you. Since the "legend rule" no longer works that way, we would be hard-pressed to put a card like [Pendelhaven](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pendelhaven) or [Okina, Temple to the Grandfathers](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Okina%2C+Temple+to+the+Grandfathers) into Standard, because almost every green deck would just run one for free and get some kind of advantage from the times they randomly drew it. As a whole, we want our utility lands to have some inherent downside next to a basic lands, so that there is an interesting choice surrounding whether to run the cards or not, and how many to run. If you look at the lands in *Battle for Zendikar* that enter the battlefield tapped but give you a spell effect, you are paying for that effect with the speed of your deck. Playing some may not be a huge cost, but there is definitely an upper limit to the number of utility lands a deck can run.

I don't want to simply throw the older lands totally under the bus, though, because I believe we made a mistake pretty recently when we put [Mutavault](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault) into *Magic 2014*. We thought it would be interesting in the set following *Return to Ravnica* block to give you a land that pushed you away from just playing all the gold cards, but we didn't expect that it would end up showing up in the vast majority of all Standard decks. Some of that was undervaluing how important [Mutavault](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault) being a Rat was, and part was not appreciating that with no other real options for utility lands in Standard, any deck that wanted to play something in that range came up with the same card. While there is certainly room for powerful utility lands, if the vast majority of all players end up using the same one, we have probably gone wrong somewhere. The sweet spot here is where a wide variety of decks are often running a few of these, but which one depends on both what their core strategies are and what the metagame looks like. If people are playing [Blighted Fen](https://web.archive.org/web/20151009000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blighted+Fen) to fight decks casting one creature, but move to something else if there are mostly swarm decks, then I think we have done something very right.

That's it for this week. Join me next week when I talk about how we set up the Eldrazi and Zendikari to face each other in *Battle for Zendikar*.

Until next time,

Sam ([@samstod](http://www.twitter.com/samstod))
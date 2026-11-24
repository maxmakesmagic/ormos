---
id: 5gj9s3gd
kind: article
lang: en
path: /en/articles/latestdevelopments/2015/09-11-challenges-of-revisiting-sets
title: Challenges of Revisiting Sets
published: '2015-09-11'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
    lang_detected: en
    capture_id: 719436
    url: http://magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
    captured_at: '2016-08-26 08:13:32+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
    lang_detected: en
    capture_id: 719436
    url: http://magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
    captured_at: '2016-08-26 08:13:32+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
    lang_detected: en
    capture_id: 719436
    url: http://magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
    captured_at: '2016-08-26 08:13:32+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
    lang_detected: en
    capture_id: 719436
    url: http://magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
    captured_at: '2016-08-26 08:13:32+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 5gj9s3gd
  url: http://magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
  page_key: magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
  lang: en
  template: drupal
  captured_at: '2016-08-26 08:13:32+00'
  capture_id: 719436
  wayback_url: https://web.archive.org/web/20160826081332id_/http://magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 5gj9s3gd
  capture_id: 719436
  url: http://magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
  wayback_url: https://web.archive.org/web/20160826081332id_/http://magic.wizards.com/en/articles/archive/latest-developments/challenges-revisiting-sets-2015-09-11
  captured_at: '2016-08-26 08:13:32+00'
  template: drupal
  sha256: f74848f82189e1b97b8f6b3020b16ce0563e1e0d0ce801acfdd6889c099a7798
render_recovery: []
---
It's the end of the first week for *Battle for Zendikar* preview cards, but I guarantee that we have a lot more to show you, both today and in the coming week. *Battle for Zendikar* is an epic set, and one that provided a number of challenges to both the design and the development teams. The goal of the set was not just to mash together *Rise of the Eldrazi* and *Zendikar* and see what happened, but to create a new and dynamic play environment that took many of the best parts of both sets and combined them into something special and new.

*Battle for Zendikar* is the first set that I've worked on that was a truly a return to a world we had previously seen. I did some work on *Dragon's Maze*, but the *Return to Ravnica* block went back to Ravnica without reusing a single mechanic—because so much of the world's identity is based around the guilds. When we were looking at returning to Zendikar, we knew that landfall, the Eldrazi, and Allies would all need to return, but that meant revisiting mechanics that had a limited amount of design space. It was a real challenge at times to figure out how to make the mechanics feel both nostalgic and new.

As I mentioned earlier, that meant combining two very different Draft environments: *Zendikar*, known as one of the fastest Draft environments of all time, and *Rise of the Eldrazi*, known as one of the slowest. *Rise* had a number of very different things going on, and it was trying to create a type of "battlecruiser *Magic*" where lowly Glory Seekers were not only low picks, they were basically unplayable—all in favor of eight-mana 8/8s that had to attack each turn, but forced your opponent to sacrifice two permanents. Simply doing a mash-up wasn't going to work; we had to break down the essence of the Eldrazi and the essence of Zendikar and figure out how to make *Battle for Zendikar* feel like the next chapter in an epic storyline.

# Recreating the Eldrazi

The Eldrazi proved to be the most difficult part of *Battle for Zendikar*. Part of the problem with them was that they were defined by their size in *Rise of the Eldrazi*, and we didn't feel we could easily make another set where they went even bigger. We also needed this to feel like a real war between the Eldrazi and the plane of Zendikar, which meant having soldiers other than just the titans and some mammoth Eldrazi supported by some spawn. Mark Rosewater quickly hit upon colorlessness to be the "thing" to define the Eldrazi this time, and we went forward with it, creating the devoid mechanic as a way to make the Eldrazi feel like a cohesive group of characters, even if they were inscrutable. By creating a group of Eldrazi that was all over the curve, we could create Eldrazi control or beatdown decks that functioned in a way that was different than the Zendikar decks, but still could be intermixed with cards from the Zendikari side of the conflict.

![](http://media.wizards.com/2015/images/daily/c4rd4r7_18nqULPwEy.jpg)

Art by [James Zapata](https://web.archive.org/web/20150911000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22James+Zapata%22%5d)

A big part of melding the two sets together was moving from the Eldrazi Spawn of *Rise of the Eldrazi* to the Eldrazi Scions of *Battle for Zendikar*. One of the challenges with Spawn was that we had to give you a ton of them to make the cards worth playing, but then they were really only useful for chump blocking or casting huge Eldrazi. We didn't want the play pattern of the Eldrazi decks to just be stall until the Zendikar deck was out of gas, then cast a huge Eldrazi to win the game. We wanted them to have all kinds of strategies, some fast and some slow. If you look at the set, the green-based Eldrazi decks are the closest to the original *Zendikar*, ramping out the big guys. But we also have red-black turbo-aggressive strategies that can put the Zendikari landfall draws to shame. Further still, we have the black-green sacrifice deck that gets to work in the "combo" space in a satisfying way that still feels like it is Eldrazi.

Making the spawns 1/1s meant they could meaningfully gang block and take out larger creatures, but also go into aggressive decks as attackers, or still be used for their old purpose of casting larger Eldrazi. The other advantage to making 1/1s was that we didn't have to give you quite so many when you cast an Eldrazi, so we could do a better job of making cards that felt powerful at all points in the game, rather than providing often largely useless fodder that just gummed up your opponent's future board plans.

# Fetching From The Past

Figuring out the Zendikari was pretty straightforward, although still challenging. We knew that *Zendikar* was about land, and that we would need landfall back. But we wanted to do it in a way that felt different than the first time and wouldn't make Standard be all about landfall for eighteen months straight. To solve this, the first thing we did when we knew we were going back to Zendikar was to place the fetch lands in a set that was far enough away that they would not overlap in Standard for the entire lifespan of *Battle for Zendikar*.

We knew that the thing that kept landfall in check the first time was just how strong all of the removal was when the original *Zendikar* set came out. Although we are trying to swing the pendulum a little further along the "strong removal" axis than we were in *Theros* block, we still did not fill the environment with the kinds of cards needed to deal with the turn-one [Steppe Lynx](https://web.archive.org/web/20150911000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steppe+Lynx), turn-two [Plated Geopede](https://web.archive.org/web/20150911000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plated+Geopede) draws—and we would rather not have had those kinds of games defining what Standard can look like. Having some period of time where that was a thing was fine, just not the entire lifespan of the set.

![](http://media.wizards.com/2015/images/daily/c4rd4r7_erDyfK4HqD.jpg)

Art by [Chris Rahn](https://web.archive.org/web/20150911000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Chris+Rahn%22%5d)

By placing the fetch lands in *Khans*, we did open up a new way to get extra power from the cards, though, in cards without landfall—the new cycle of dual lands in *Battle for Zendikar*. I was probably as surprised as anyone when the decision was made to put dual lands with basic land types into *Battle*, but I think it does a great job of creating a really high-powered environment where landfall and the wedge cards in *Khans* can compete on near-even footing, while still allowing for monocolor decks to exist. I think we hit a really good balance with these lands, and I look forward to seeing how they play out in Standard over the next six months.

# Revisiting Landfall

If you look at the landfall cards that saw Constructed play in the first *Zendikar* set, the vast majority of them were one- or two-drops. That's not surprising, since you are far more likely to get four or five landfall triggers out of a one-drop than a six-drop. But when we returned to Zendikar, we wanted to do a little more with the landfall mechanic—namely, create decks that were landfall decks without being super all-in, low-to-the-ground decks or ramp decks. We wanted there to be options for creatures you would play in decks that had plans other than just landfall. Creatures where a lot of the strength was on the front of the card, and the landfall trigger provided a bonus, instead of the creature being nigh-unplayable unless you were hitting at least one land a turn. To give you an idea of the kind of card we wanted to create in *Battle for Zendikar*, I present the Akoum Firebird.

![](http://media.wizards.com/2015/bfz_8asdifk2Sk2cs/en_WCk4QzMZNS.png)

The object of this card is simple: It wants to provide a resilient clock that your opponent is not going to have an easy time dealing with. While it may be reminiscent of cards like [Bloodghast](https://web.archive.org/web/20150911000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodghast) from the first *Zendikar*, it trades the raw speed of that card for evasion. While there certainly are cards in Standard that can block a 3/3 flyer every turn, they are few and far between, and there aren't a ton of ways to deal with Firebird for good, now that [Anger of the Gods](https://web.archive.org/web/20150911000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anger+of+the+Gods) has left Standard. I suspect that Firebird will provide a very solid option for either the top end of some aggressive decks, or for the middle of the curve in a variety of removal-heavy red decks (of the Mardu or black-red variety). While this is often competing for space with [Thunderbreak Regent](https://web.archive.org/web/20150911000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thunderbreak+Regent), I believe that it has advantages in some matchups that will lead to it seeing play.

# Further Adventures in Zendikaring

That's all the time I have for this week, but I will be back next week. I won't have a new preview card (because the Card Image Gallery will go up on the same day that my article does, allowing all of you to peruse the entire set), but I will be talking about some more of the nitty-gritty details about how *Battle for Zendikar* was made, and how we hope it will impact Standard in the future.

Until next time,

Sam ([@samstod](http://www.twitter.com/samstod))
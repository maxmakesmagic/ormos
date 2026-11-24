---
id: knz58c13
kind: article
lang: en
path: /en/articles/latestdevelopments/2015/10-23-developing-devoid
title: Developing Devoid
published: '2015-10-23'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
    lang_detected: en
    capture_id: 720737
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
    captured_at: '2016-05-11 00:49:25+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
    lang_detected: en
    capture_id: 720737
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
    captured_at: '2016-05-11 00:49:25+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
    lang_detected: en
    capture_id: 720737
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
    captured_at: '2016-05-11 00:49:25+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
    lang_detected: en
    capture_id: 720737
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
    captured_at: '2016-05-11 00:49:25+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: knz58c13
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
  lang: en
  template: drupal
  captured_at: '2016-05-11 00:49:25+00'
  capture_id: 720737
  wayback_url: https://web.archive.org/web/20160511004925id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: knz58c13
  capture_id: 720737
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
  wayback_url: https://web.archive.org/web/20160511004925id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-devoid-2015-10-23
  captured_at: '2016-05-11 00:49:25+00'
  template: drupal
  sha256: ac0b43f460b99ae156035731c8b978d7e92646e313ee6a84de221a7102615ed3
render_recovery: []
---
When we started working on *Battle for Zendikar*, the design team was challenged to come up with a way to include a large number of Eldrazi in the set without including a number of large Eldrazi. It was difficult, as the Eldrazi the first time were so defined by their huge size, and we couldn't exactly have half of the set be huge eight-plus-drops. *Rise of the Eldrazi* went way out of its way to make the Eldrazi work by having a crazy draft environment where attacking was bad, and you had more than enough time to either ramp or do your crazy thing.

We wanted *Battle for Zendikar* to be about more than the Eldrazi, though—we needed it to be a blend of both *Rise* and the original *Zendikar* block, which meant having decks of all speeds. *Battle for Zendikar* is, above all else, a set about conflict, and that meant having both sides, much like *Mirrodin Besieged* did. That meant finding a way that the Eldrazi and the Zendikari could fight each other in more ways than just "I am the quick deck," "I am the high-end deck." We knew we needed a way for Eldrazi to come to life other than just high-end eight-to-ten-drops and ways to speed them out. If we were going to make the set not just show off a battle, but also feel like one is playing out in a fun way, we would need Zendikari decks that went long, as well as Eldrazi decks that were blazing fast with weenies.

# Fewer Colors, More Problems

As the set approached divign (the step between design and development), we still had a lot of work to do. While it was okay to define the Eldrazi by their colorlessness, it was causing big roadblocks to making spells in the set work. We had a few creatures that were colorless (even with colors of mana in their casting cost), but also had a lot more cards that were true colorless, including spells like the following:

2

Eldrazi Growth

Instant

Target creature gets +2/+2 until end of turn. If that creature is colorless, it gains trample until end of turn.

The problems with cards like this are twofold: One, it made the actual process of drafting more difficult (since so much of the process is figuring out what colors are open and paring down cards for your deck), and two, it also caused some real struggles for the color pie. As an aside, color pie isn't just a minor inconvenience for making cards, it's all about giving different colors different strengths and weaknesses so that the decks play differently. Generally, a blue/black deck is just not going to have efficient combat tricks—it gets good removal instead. You have to worry a bit about a -N/-N effect when blocking, but the rates on those tend to be different than the rates on combat tricks. All of a sudden, you block a creature and your opponent plays this—it makes the individual decks start feeling less different from each other.

Some of the problem on this card is rate—it's way too close to what we would give you in green as a common. Imagine:

1G

Green Growth

Instant

Target creature gets +2/+2 until end of turn. If that creature is green, it gains trample until end of turn.

The card wouldn't be very strong, but if there wasn't much else in the way of combat tricks, there is a reasonable chance you would run it in your Limited decks. Despite that, we just wouldn't make the following card:

1U

Blue Growth

Instant

Target creature gets +2/+2 until end of turn.

We don't want to put the rate of cards that can go into any deck that close to the rate of those that we would put into the correct color. So, the only reasonable way to make the card is to charge at least three mana, which suddenly pushes it pretty far away from being useful in anything but the most desperate decks. The solution for design was to keep colorlessness as the main characteristic of the Eldrazi, but scale back on the number of cards that are fully colorless. We still have spells like [Scour from Existence](https://web.archive.org/web/20151023000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scour+from+Existence) in that realm, but we kept it away from the cheap combat tricks. We also tried to make the Eldrazi in the set have at least a little bit of character. [Kozilek's Channeler](https://web.archive.org/web/20151023000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kozilek%27s+Channeler), for example, started off as Elfdrazi, with the idea that even their mana elves are 4/4s.

Still looking for solutions, design decided to further embrace the Eldrazi that took colored mana to cast, but had rules text that made them colorless, and all of a sudden we had more cards with the devoid ability, giving a through line for the Eldrazi.

# Making Devoid Matter

Once we had settled on devoid as being the "thing" that united the Eldrazi, we needed to do something to make it more than just a random marker on a card. While we certainly could have just made:

1G

Eldrazi Bear

Devoid

2/2

or

2U

Eldrazination

Sorcery

Devoid

Draw 2 cards

. . . those cards don't have any character or show off the Eldrazi in a meaningful way. It's not really any different than marking them as tribal—Eldrazi for no real reason. Instead, we went out of our way to try and make the devoid Eldrazi either care about colorlessness (like [Kozilek's Sentinel](https://web.archive.org/web/20151023000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kozilek%27s+Sentinel) and [Nettle Drone](https://web.archive.org/web/20151023000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nettle+Drone)), have unusual power and toughness for what they did (like [Silent Skimmer](https://web.archive.org/web/20151023000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Skimmer) or [Vestige of Emrakul](https://web.archive.org/web/20151023000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vestige+of+Emrakul) . . . or [Kozilek's Sentinel](https://web.archive.org/web/20151023000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kozilek%27s+Sentinel)), or care about ingest or process. As a whole, I believe this means that the devoid ability on the cards is more than just flavor text or something arbitrary. The creatures, when put together as a whole package, definitely feel cohesive with each other, and different than the Allies or the rest of Zendikar, even if things like awaken are intended to provide some amount of overlap in mechanics.

Ingest/process actually did a lot to tie the whole set together, and solved a big problem I talked about earlier with having a ton of true colorless spells. It let us put words on instants and sorceries that worked as more than just flavor text. Without a reason for exile to matter, having all of the removal spells exile creatures wouldn't really make sense. We do it now and again on spells, usually for development reasons, but I don't think we've ever had a set that had that line appear quite so many times and through so many colors. Heck, we even have a green fight card that exiles. I think that goes a long way toward helping the set really fit together. It is something that is very hard to get just from reading through the set, but I think it comes through very well once you actually start playing it and exploring it in Limited.

# Bringing Devoid to Paper

Once we had a purpose behind the cards, it was all about making them look right in the pack. I talked a little about this [in a previous article](/en/articles/latestdevelopments/2015/09-18-developing-new-mechanics-in-a-returning-world), but I wanted to talk a bit more about how much work the actual frames do for selling the Eldrazi as something different in this set. The cards do a good job of standing out pretty loudly from the Allies in the set, but giving you enough cohesiveness that you can draft or make mulligan decisions accurately by determining the cards' colors. It was a real challenge, but one that was very important for the final set.

One thing I've seen mentioned that I wanted to explain is why we use the keyword devoid instead of just a colorless color indicator (and yes, we did use that mouthful in development to discuss the feature). Double-faced cards and things like Pacts or some of the uncastable suspend cards from *Time Spiral* have a small dot that tells you the card's color without needing text that says "This card is blue."

![](http://media.wizards.com/2015/images/daily/LD20151023_Ancestral-Vision-Card-Type-Slice.png)

This was a cool advancement from *Innistrad* that we are more than willing to put into greater use if we have the spot—we just felt that this wasn't the right place. Technically, we could write a quick rule, leave the frames the same, and cut out the color indicator, and the cards would work the same way, but they would likely play much worse, making their status much harder to understand. We could've given them a colorless frame with the colored mana symbols and the dot, which would be a little better, but still would be very hard for a new player to figure out. Besides, if that clear dot for the colorless indicator happened to fall over a tree or the sky in a piece of art, it might look like a color it wasn't. All these factors meant that writing it out on the cards was our ideal implementation. While newer or less-enfranchised players may not immediately get what is cool about devoid when they open up their first pack of *Battle for Zendikar*, at least they will understand what the cards do.

That's it for this week. I will be back next week with some of our FFL decklists, and I'll give you a peek into what our own internal metagame looked like.

Until next time,

Sam ([@samstod](https://twitter.com/@samstod))
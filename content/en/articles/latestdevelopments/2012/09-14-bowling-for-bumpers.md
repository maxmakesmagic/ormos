---
id: m4jpdc0s
kind: article
lang: en
path: /en/articles/latestdevelopments/2012/09-14-bowling-for-bumpers
title: Bowling for Bumpers
published: '2012-09-14'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
    lang_detected: en
    capture_id: 718401
    url: https://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
    captured_at: '2022-10-03 21:34:50+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
    lang_detected: en
    capture_id: 718401
    url: https://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
    captured_at: '2022-10-03 21:34:50+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
    lang_detected: en
    capture_id: 718401
    url: https://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
    captured_at: '2022-10-03 21:34:50+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
    lang_detected: en
    capture_id: 718401
    url: https://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
    captured_at: '2022-10-03 21:34:50+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: m4jpdc0s
  url: https://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
  lang: en
  template: drupal
  captured_at: '2022-10-03 21:34:50+00'
  capture_id: 718401
  wayback_url: https://web.archive.org/web/20221003213450id_/https://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
- document_id: m4jpdc0s
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/212
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/212
  lang: en
  template: aspx
  captured_at: '2013-07-06 06:08:32+00'
  capture_id: 618778
  wayback_url: https://web.archive.org/web/20130706060832id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/212
- document_id: m4jpdc0s
  url: http://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-13
  page_key: magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-13
  lang: en
  template: drupal
  captured_at: '2015-03-24 05:07:18+00'
  capture_id: 718399
  wayback_url: https://web.archive.org/web/20150324050718id_/http://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-13
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: m4jpdc0s
  capture_id: 718401
  url: https://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
  wayback_url: https://web.archive.org/web/20221003213450id_/https://magic.wizards.com/en/articles/archive/latest-developments/bowling-bumpers-2012-09-14
  captured_at: '2022-10-03 21:34:50+00'
  template: drupal
  sha256: 73ace3ac87d64188cb2144d33256822fb9804e3db3d7d977f7f39920843fdecb
render_recovery: []
---
Have you ever gone ten-pin bowling?

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_lane_nixucpxpiw.jpg)  

For those of you who haven't, here's how it works. Ten pins stand in a triangular array sixty feet away from you. Between you and the pins, there is an oiled wooden lane that is 41.5 inches wide. You have a ball a little less than nine inches in diameter that weighs up to sixteen pounds. Your goal is to roll your ball down the lane and knock down as many pins as you can.

Here's the bad news: on the left and right edges of the lane, there are gutters. If your ball falls into the gutter, you don't get to knock down any pins. The good news is that if this happens, you probably get to try again in a minute or so when your turn comes around again. In one round of bowling, you'll have somewhere between twelve and twenty rolls; one dead roll isn't a huge deal.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_tenpin_brubymgrvb.jpg)  

That's enough for most adults. Kids, however, can get frustrated at even one ball going in the gutter. In order to fix this, Phil Kinzer invented the concept of "bumper bowling," in which something keeps balls from getting into the gutters. The first such system was jury rigged out of cardboard tubes, which developed into large inflatable tubes that completely fill the gutters, and modern systems tend to be retractable rails that are built into the lane. Running into the bumper robs the ball of some power, but still keeps the ball heading toward the pins so the throw can be marginally successful. Your goal is always to avoid the bumper, but even experienced bowlers occasionally make a mistake and hit it anyway.

Being a **Magic** developer is a lot like bowling. We have a pretty good idea about what we want our play environments to look like, and we see that off in the distance. Releasing a set is a lot like rolling a bowling ball down the lane. We do our best to hit the target, but we aren't perfect, and sometimes we roll off center. When that happens, we'd still like to hit some pins.

The big difference between **Magic** development and bowling—and here's where I start slaughtering the metaphor—is that we can't actually see what the lane looks like. We can see the pins at the end of the lane, but the path that the ball has to travel through is full of random obstacles that we have almost no control over. I visualize it as the sort of bowling alley that Dr. Seuss would have drawn, but that's not important. What is important is that this whimsical metaphorical bowling alley is mysteriously shaped and three months long, and the gutter is a scary, scary place to be.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_suess_ukecjrmppa.jpg)  

What's in our gutter? Environments where one deck is obviously the best. Environments where one card is far more powerful than other cards. Environments where there aren't reactions a player can make during deck building that make his or her deck better against the dominant strategy. This matters in both Limited and Constructed, as draft formats get tons of attention on **Magic Online** and Constructed formats get tons of attention on various independent open tournament series.

The good news for us is that we get to build our own rails. Cards like [Celestial Purge](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Celestial+Purge), [Ground Seal](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ground+Seal), [Gainsay](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gainsay), and [Grafdigger's Cage](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grafdigger%27s+Cage) can happily sit outside of Constructed while the things they are good against aren't being played. On the other hand, when the metagame takes a turn toward something that needs a specific answer that normal cards don't provide, they're there to play bumper. Some of these are pretty general; [Celestial Purge](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Celestial+Purge) usually shows up only when black or red creatures that need to be exiled are running around, and [Gainsay](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gainsay) was only good when there were blue spell decks that needed to be better against other blue spell decks. Some cards get more specific: [Ground Seal](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ground+Seal) and [Grafdigger's Cage](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grafdigger%27s+Cage) show up only if there's a graveyard strategy that needs to be attacked.

The cards I listed above are mostly sideboard cards. However, sometimes we want an answer card that you can think about playing in your main deck, and one of the best ways we have to get that done is to attach an interesting ability to a creature. You might have seen one or two of these guys before.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_cards_duecgiuuaf.jpg)  

Each of these creatures targets some strategy or category of cards that we felt needed an answer. [Stigma Lasher](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stigma+Lasher) stops people from gaining life. [Kataki, War's Wage](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kataki%2C+War%27s+Wage) blows up artifacts. [Vexing Shusher](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vexing+Shusher) beats up on counterspells. [Riftsweeper](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper) goes after suspended cards. As it turns out, creatures are generally pretty strong, so we can usually get these cards in range by putting them on a reasonable body. We've also noticed that players tend to like these cards. Even in enormous formats like Legacy and Vintage that are full of crazy powerful things to do, there's a category of player out there who would rather not bother with casting [Show and Tell](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Show+and+Tell) or [Tendrils of Corruption](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tendrils+of+Corruption+) and instead tries to get in there with [Meddling Mage](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meddling+Mage)s, so they're clearly hitting a nerve.

These cards don't always hit, of course. [Leonin Arbiter](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Arbiter) and [Tunnel Ignus](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tunnel+Ignus) were mostly misses, [Phyrexian Revoker](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Revoker) didn't really find anything to revoke, and [Stigma Lasher](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stigma+Lasher) was never what people needed to beat lifegain cards. That's all okay. Sometimes the thing a creature like this was built to beat up on just never gets good. Other times, the creature isn't the right answer to the problem. With [Phyrexian Revoker](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Revoker), it's possible that [](https://web.archive.org/web/20120914000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/twtw/212)[Pithing Needle](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pithing+Needle) would have hit some sideboards, but a creature that is susceptible to death by 1 damage couldn't serve that purpose. Sometimes, the card might be effective at its job, but there's never a deck that can use both the creature and the creature's ability at the same time. I'd say that's what happened to [Tunnel Ignus](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tunnel+Ignus) and [Leonin Arbiter](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Arbiter). Finally, sometimes the problem a creature is trying to solve never becomes a problem. I think that's what happened to [Stigma Lasher](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stigma+Lasher) during its tenure in Standard—no one ever tried to gain tons of life, so it was never needed.

You might have already guessed that my preview card today is one of these cards. We don't know if the environment will dictate that it is needed, but it is here to serve regardless.

![Ash Zealot](https://i.ormos.uk/ee/e1/eee11271b85e67caa4dfba214de176e9555ccc2d6919b1744f2e8ba709422898.jpg)  

Many **Magic** cards naturally spring forth into being. Little creatures like this don't. [Gaddock Teeg](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaddock+Teeg) is my favorite example of this—I'm not sure how a little kithkin guy notices that a card has an X in its cost and prevents it from happening, so I try not to ask what's going on there. We engineer this kind of card as heavily as we can to do exactly what we want, so let's talk about what's going on in this card.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_rr_mmqmcogmja.jpg)  

### RR?

There are three reasons for this mana cost. First, *Return to Ravnica* is a set about two-color combinations. As popular as Ravnica was the first time, not everyone likes to play more than one color. We wanted there to be some goodies in the set for people who wanted to play monocolored decks. Second, red is historically short on this kind of card, so we thought it would be good to give it one. Third, Black-Red Zombies is a pretty strong deck going into *Return to Ravnica*, and we didn't want it to be easy to play this card in the same deck as [Geralf's Messenger](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geralf%27s+Messenger).

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_22_dahewtzzct.jpg)  

### 2/2?

This is about the size a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) card has needed to be to stay competitive in the past, and we went with it here too.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_haste_dahewtzzct.jpg)  

### Haste?

Here's where the real engineering starts. Rather than make a card that's interesting in a vacuum and hope there's a deck for it, this guy is aimed much more closely at being part of a mono-red deck. Red decks love haste guys, so Ash Zealot already has a leg up at the task of getting into decks.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_damage_izfhtuturi.jpg)  

### Damage to the Face?

Speaking of getting a card into red decks, red decks love dealing damage to people. This was a natural fit, especially for a card with a double-red cost.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_graveyard_wrgonmneok.jpg)  

### Spells Cast From Graveyards?

It's pretty clear that this card is good against [Snapcaster Mage](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage), but that's not the real reason we made the card. We had several decks in our [Future Future League](https://web.archive.org/web/20120914000000/http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/80) that made heavy use of the graveyard for flashback spells. We had [Burning Vengeance](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Vengeance) decks with [Forbidden Alchemy](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forbidden+Alchemy) and such, and we also had Frites-like decks with [Unburial Rites](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unburial+Rites), [Faithless Looting](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faithless+Looting), and [Tracker's Instincts](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tracker%27s+Instincts). There were also plenty of [Gravecrawler](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravecrawler)s creeping around. The marginal value you get from playing against [Snapcaster Mage](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage) decks with this card is certainly not zero, but this card is hardly at its best if the only thing on the other side for it to pay attention to is Snapcasters.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_first_fkcktaaoty.jpg)  

### First Strike?

We found in playtesting that it was very important to this card's purpose that it not die in combat with a [Snapcaster Mage](https://web.archive.org/web/20120914000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage), so we gave it first strike.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld212_ash_uxiyudxxey.jpg)

Ash Zealot | Art by [Eric Deschamps](https://web.archive.org/web/20120914000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Eric%20Deschamps%22%5D)

I can't say with any certainty that this card will see tons of play like I could with a card like Dreadbore or Abrupt Decay. If you like to play mono-red or if you really hate graveyard strategies, this guy might be up your alley. If you like balanced and fresh competitive formats, though, cards like Ash Zealot are a huge part of how we try to make sure you get what you want. We want there to always be something new to discover, and the more cards we can put into the environment that serve as bumpers to move the format to a different place, the more likely there will be room for discovery.

It's time for me to get back to making **Magic** cards. I hope you enjoy the Prerelease, and we'll be talking again in a few weeks.
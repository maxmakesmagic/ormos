---
id: t2yyxspa
kind: article
lang: en
path: /en/articles/latestdevelopments/2012/07-06-the-cards-of-magic-2013-part-1
title: The Cards of Magic 2013, Part 1
published: '2012-07-06'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: zac-hill-263da3f4
  name: Zac Hill
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
    lang_detected: en
    capture_id: 719371
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
    captured_at: '2021-10-21 11:32:21+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
    lang_detected: en
    capture_id: 719371
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
    captured_at: '2021-10-21 11:32:21+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
    lang_detected: en
    capture_id: 719371
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
    captured_at: '2021-10-21 11:32:21+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
    lang_detected: en
    capture_id: 719371
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
    captured_at: '2021-10-21 11:32:21+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: t2yyxspa
  url: https://magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
  page_key: magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
  lang: en
  template: drupal
  captured_at: '2021-10-21 11:32:21+00'
  capture_id: 719371
  wayback_url: https://web.archive.org/web/20211021113221id_/https://magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
- document_id: t2yyxspa
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/202
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/202
  lang: en
  template: aspx
  captured_at: '2013-07-04 05:34:04+00'
  capture_id: 618596
  wayback_url: https://web.archive.org/web/20130704053404id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/202
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: t2yyxspa
  capture_id: 719371
  url: https://magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
  wayback_url: https://web.archive.org/web/20211021113221id_/https://magic.wizards.com/en/articles/archive/latest-developments/cards-magic-2013-part-1-2012-07-05
  captured_at: '2021-10-21 11:32:21+00'
  template: drupal
  sha256: 7129fedfcea77f45ae46964bb6292d9b08b89dd9da04346031b106e976c7bb27
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
Hey, y'all. It's the first week of "***Magic** 2013* being on public display for all to feast their eyes upon"—the official title—so I wanted to carry forward the tradition of a card-by-card development crawl through the set a'la Rosewater. What rhyme or reason is there to the cards I choose to talk about? None whatsoever! Yay! First, though, I promised last week I'd talk a little more about the M13 development team, since without it the set wouldn't... well, be a set at all. Without further ado, then:

![](https://i.ormos.uk/6a/2d/6a2dfd2fbe08ca3802bbdfcb713ff3ee5b59a73cc3885118225f5c2f298f25be.jpg)

Pearl Trident | Art by [Ryan Pancoast](https://web.archive.org/web/20120706000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Ryan%20Pancoast%22%5D)

Introducing the Guy on the Development Team Who Has His Own Column and Can Give Himself a Heading Because Why Not

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_zachill.jpg)

**Zac Hill**

Hi, I'm ***Magic** 2013's* Lead Developer, Zac. \*waves\*

  

Introducing the Rest of the M13 Development Team Who Aren't So Lucky As to Lord Their Friday Mouthpiece Despotically Over Everyone Else

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_tomlapille.jpg)

**Tom LaPille**

If you've been reading this column for a while, you already know [Tom](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Tom%20Lapille). He was the development lead for ***Magic** 2012* and guided me through a lot of the process-oriented portions of running my own team. A huge part of **Magic's** recent success has come about because of how seriously we take the fusion of flavor and mechanics, and Tom might be the person in Ramp;D who most strongly leads that charge. He took a brief hiatus from **Magic** to work on the latest iteration of the **Dungeons amp; Dragons** experience, but we're happy to have him back on the "Friends" development team and look forward to what he comes up with in the future.

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_ethanfleischer.jpg)

**Ethan Fleischer**

![](https://i.ormos.uk/f8/c4/f8c42ad5f12ccf5a760043e96b779415b0fc82bb493be172461ec7cc297c72dc.jpg)

Great Designer Search 2 winner [Ethan Fleischer](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Ethan%20Fleischer) donned a developer hat for ***Magic** 2013* and came up with some of our most awesome individual card designs. He blends an unparalleled aesthetic understanding of well-crafted cards with a refined intuitive sense of fun play patterns, and lent what I would describe as a certain "crispness" to the set that it could not have had otherwise. He also sounds exactly like a Mooninite from *Aqua Teen Hunger Force*, but that is neither here nor there.

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_maxmccall.jpg)

**Max McCall**

[Max](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Max%20McCall) is a former Pro Tour player and Grand Prix Top 8 competitor who works inside Ramp;D's digital wing. What I appreciate most about Max is how little patience he has for bad ideas, and how keen his sense of what makes a bad idea really is. Oftentimes, I get so immersed in a set that I can't see the bigger picture, and I end up thinking every arcane twist is a stroke of unparalleled brilliance. Max is awesome at bringing you back down to Earth and keeping you on track, while managing to solve the problem you're approaching clumsily with a far more deft touch.

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_ryanmiller.jpg)

**Ryan Miller**

[Ryan](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Ryan%20Miller) was the "design representative" on the set from the ***Magic** 2013* design team, and made sure we were adhering to [Doug Beyer](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Doug%20Beyer)'s overall vision. He also contributed some totally sweet rares, but to me the best part of having Ryan on a team is how insistent he is upon having fun. This probably seems silly at first glance—after all, we're making games, so they had *better* be fun, right?—but sometimes after you've been playing for a while you aren't able to see the forest for the trees. Ryan is passionate about not letting mechanics get in the way of the experience, and much of what I'd call M13's "purity" emerged because of him.

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_markgottlieb.jpg)

**Mark Gottlieb**

[Mark](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Gottlieb) has been around forever and harbors obscene amounts of knowledge about **Magic** design. What I like the most about him, though, is that he looks at sets in a totally different way than I do. He sees every trend and pattern and has a better sense of the overall *whole* than almost anyone else. He routinely combs Multiverse, taking in each and every card, and provides probably the most voluminous "DevComments" feedback of anybody in the Pit—all of which is thoughtful and well-considered. I've worked with Mark on a number of teams now, both design and development, and I appreciate the extent to which he contributes a ton of different skills that I myself just do not have.

It's All In The Cards

![](https://i.ormos.uk/13/50/13506c41279d2920cb2380e861812ae3309a736f26a563f0af567deffb790640.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card01b.jpg)

We'll start out with a goodie. I knew I wanted a three-mana Ajani, and the version handed over by design did a lot of stuff with Equipment that I felt would be repetitive, given the extent to which Standard is defined by Swords of Stuff and Things. Given that Ajani's whole shtick is that he helps everyone else out but relies upon them to fuel his own powers, it made sense to me that he would make his presence known by boosting your other guys. The ultimate, meanwhile, drew its strength from *your own* power.

I've gotten a lot of feedback that the "life" portion of the card is disconnected from the rest. I feel where that's coming from, but the decision was deliberate. The thought process goes like this: First, the M13 Planeswalkers are intended to function in concert with all of the cards in the set that bear their name. Both Ajani's common and uncommon gain you life, as does his common enchantment from previous core sets. So if you buy into Ajani's "gimmick"—or play a deck that's similar to his **Duels** 2013 deck thematically—you get an extra bonus from the ultimate. The second point is just that your life total is a big number that's keyed into **Magic** from the core. Even if you're not doing a lot to keep it artificially inflated, you're still going to get yourself a pretty decent number of Creature – Cats.

![](https://i.ormos.uk/f9/3e/f93e9db06e2e55a63cac9b823f1e103905b142f1f163a6494cde3b6f2e463666.jpg)  

I cannot shake the sensation that this guy needs to star in his own Hanna-Barbera Saturday-morning cartoon. "To the skies, kids! Caw!!"

![](https://i.ormos.uk/14/68/1468ec689f1ffd48a1105d8747878ff6b901d0e8eb3221870857dd81687a78d3.jpg)  
![](https://i.ormos.uk/b5/05/b5057661057d1c23c06ede8e6f7a8ceb2322995ba2cab4981fdd9fb3152b3cda.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card03b.jpg)

Basically, every set has its run-of-the-mill standard-issue white enchantment-destruction slot. For M13, we knew [Rancor](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rancor) would be one of the set's key selling points, and we wanted it to be one of the most high-impact cards in both Standard and Draft alike. We therefore decided that we needed to put a common answer to the card into the set, so you didn't just depend upon being able to [Unsummon](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon) the creature in response to the enchantment (or whatever). You're not going to go jamming it into every one of your main decks or anything, but with removal spells like [Pacifism](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism), [Encrust](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Encrust), and [Oblivion Ring](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) playing a central role, this card can do a surprising amount of work.

![](https://i.ormos.uk/25/78/25788598f4562f7c273cddbed8d58b77a7f22e8c3c5da3fa9348cafa20318588.jpg)  

"Exalted" is and has always been a kind of "knightly" mechanic, debuting as it did inside the ritual-oriented battle ceremonies of Bant. Given how exalted exists in white and black, and given the long core set history of knights-as-mirrored-pairs, we decided we wanted our own flavor of [Black Knight](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Knight) and [White Knight](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=White+Knight) in ***Magic** 2013*. These guys depart a bit from the traditional formula of ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)/![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2s, though, because we wanted it to be realistic for you to play and cast both Knights in a Black-White Exalted deck.

![](https://i.ormos.uk/fc/90/fc90cba26841204ecb442d0425ae8c03d1f3512b20bfc5cfb3bd3dac852e701e.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card05b.jpg)

One of the things I believe very strongly as a **Magic** developer is that your mythic rares need to be breathtaking and awe-inspiring without being powerful simply by virtue of their ability to, say, kill all your opponents' creatures and then kill them. It's also important to me that certain cards from **Magic's** past get to enjoy another day in the sun.

I remember when I played on the Junior Super Series, I received a foil [Serra Avatar](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Avatar) as a participation prize and my jaw dropped. It gave me a deck to build—just gain life and think of how big this guy could be! It gave me security—even if it dies, I can cast it again! It gave me, once I thought about it a little more, the promise of power—just [Sneak Attack](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sneak+Attack) it into play, and oftentimes your opponent is out for the count! Obviously, Serra requires you to do a fair amount of work; it doesn't have evasion, you can't reanimate it, and it costs seven to get into play the hard way. But there aren't many creatures that even have the *potential* to one-hit your opponent, and sometimes that's worth working for.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baneslayer+Angel"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Baneslayer+Angel"></a></div></div></td><td><img src="https://i.ormos.uk/cf/b3/cfb36e69854e5ab5fc00012c29d5c2350a919a9207217e4ccebb9d980aaec59f.jpg"></td></tr></tbody></table>

It seems silly now, in a way, that [Sneak Attack](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sneak+Attack)ing this card into play was actually a viable tournament strategy. But that's the thing about [Serra Avatar](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Avatar)—you don't necessarily know what you want to do with it, and you're not necessarily sure that it's going to be good, but the potential for massive upside is very plainly present. A lot of what makes games powerful and resonant is the ability they give you to realize potential, to create order out of chaos. A good mythic rare, in my opinion, should give you a *taste* of that power without necessarily doing all the work for you on the front end. This isn't true for all of them, of course—sometimes, as with [Baneslayer Angel](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baneslayer+Angel) or [Thundermaw Hellkite](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thundermaw+Hellkite), the awesomeness needs to be clearly and obviously evident from the moment you see the card. But sometimes, the cards should take a little bit more time to "unpack," and I feel like [Serra Avatar](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Avatar) is a successful example of the times when that is true.

![](https://i.ormos.uk/34/a0/34a0360b54006d0f4f9b79f903e6fface2afa7cf7798312d259781740faf37b4.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card06b.jpg)

An important part of **Magic** is the ability to answer threats. While I severely dislike the part of [O-Ring](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=O-Ring) that lets you put the ability on the stack, bounce it, and exile something permanently, I think it's perfectly positioned in terms of cost, power level, and ability to control virtually any category of threat for the right price. If it were up to me, this card (or something very close to it) would be Standard-legal for the rest of **Magic's** history.

![](https://i.ormos.uk/2c/50/2c503cd8a8ecbe0c9999ce19b886d3f4e7e7b8260ddecd7ae88c88ac08d268de.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card07b.jpg)

***Magic** 2013* contains a cycle of three creatures devoted to [Lord Nicol Bolas](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker), all of whom generate potential card advantage when they enter the battlefield. [Augur of Bolas](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Augur+of+Bolas) is perhaps the most tournament-viable of all of these, providing you with a card and a 1/3 body for two mana if you construct your deck accordingly and get just a little lucky. We try to make sure that a bunch of strategies are viable in Standard beyond simple raw resource advantage, but that doesn't mean we want to eradicate finesse and the eking out of gradual gains. We just want to apportion that power much more deliberately, and this card (and his brethren) are examples of how we're trying to do that.

![](https://i.ormos.uk/2b/12/2b1204e4b245bba53666660d64eab420faa1b1bc81e82905f90cf72f8b136a5b.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card08b.jpg)

Aah, yes. The good ol' Battle, one of my favorite cards of all time.

[Battle of Wits](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+of+Wits) is, to me, the exact kind of card that's fun every once in awhile. You don't want the best deck in Standard to involve having to shuffle two-hundred twenty-nine cards, but it also creates a *ton* of cool stories when it *does* happen. I remember when Billy Jensen (who's on my Hall of Fame ballot) didn't even *try* to split Anthony Justice's upkeep [Fact or Fiction](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction), [slamming Battle onto the table while Anthony was tapped out](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=sideboard/gpmil02/fm14b). I remember when Masahiko Morita and Akira Asahara jammed [Wandering Ones](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wandering+Ones) into the two-hundred-forty-plus card lists that took them both to the [Top 8 of The Finals in Japan](https://web.archive.org/web/20120706000000/http://archive.wizards.com/magic/magazine/Article.aspx?x=mtgcom/daily/mf119). Battle decks are decks unlike any other, and make for awesome moments when they work.

The question, of course, is why to print it *now*?

As you probably know already, *Return to Ravnica* is just around the corner, and spoiler alert: it's going to be a multicolor-matters set. I know, I know, Earth-shaking news. But when it's easier for a deck to branch into other colors, it's easier to put together two-hundred-plus cards into the same list. So now, it seems like, is as good a time as any.

![](https://i.ormos.uk/1c/73/1c7346d994b963d673918d51b165ca544c08e53bfb2b2efdf04f5443d6533912.jpg)  

[Essence Scatter](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Scatter), [Negate](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Negate), and [Rewind](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind) I suppose aren't as notable as what's being left out: *[Cancel](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel)*.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Rewind"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Cancel"></a></div></div></td></tr></tbody></table>

The design handoff totally did feature [Cancel](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel), of course, as do a lot of sets nowadays. It weirded me out, though, to look at Scatter and [Negate](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Negate) and [Cancel](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) next to each other. It's like, "Here are two different spells with two different restrictions, and now here is this other spell without these restrictions but with another teardrop in its mana cost." The differences just seemed too marginal to me to justify using up a slot to reprint a card we've reprinted a zillion times. Instead, I created space at uncommon for [Rewind](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind), which does something cool and sweet and operates along a totally different axis from the common spells. Meanwhile, [Essence Scatter](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Scatter) and [Negate](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Negate) embody (to me) the blue philosophy of possessing powerful but narrow answers to the threats you most expect, rewarding preparation and planning and diligent study of your opponents' vulnerabilities.

![](https://i.ormos.uk/e8/32/e8328c5b8f8c275d32278a92efed839f5def310b6742ae28bb54454aa9f728f4.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card10b.jpg)

I couldn't even begin to count how many "Merfolk Lord" variants we had in this slot before we agreed upon this design. We knew we had [Merfolk of the Pearl Trident](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+of+the+Pearl+Trident) and [Augur of Bolas](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Augur+of+Bolas) and [Talrand, Sky Summoner](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Talrand%2C+Sky+Summoner) and so we wanted a way to help these guys get their beatdown on. The problem was that we felt [Merfolk Sovereign](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Sovereign) was kind of old news and didn't like the way it went both "tall" and "wide," boosting your whole team but granting unblockability to only one creature at a time. We kept falling back to [Lord of Atlantis](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+Atlantis), talking about how it was the perfect power level and design and flavor—of *course* they have [Island](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)walk; he's the master of the seas! We didn't want to straight-up reprint it, though, because we don't like to force you to make your opponent's creatures bigger with your own hard-earned cards.

We kept dancing around and dancing around with clumsy design after clumsy design, until one day in a meeting we simply asked, "Why don't we just do [Lord of Atlantis](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+Atlantis) the right way this time around?"

The idea took hold, and this guy stuck.

![](https://i.ormos.uk/5b/04/5b04cb24c960cb38145105a6f035ccbc23929f69451d2e0b1528cefa0253d81a.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card11b.jpg)

I'm a vocal proponent of offering alternative draft strategies for most environments I find myself involved in developing. Something I loved about *Ravnica* draft was that milling was viable even though it didn't occupy a ton of real-estate in the file—it wasn't as though every single Dimir card milled your opponent! Instead, the ones that pulled weight pulled a *lot* of weight, and as a result, milling was a thing you were able to do, but it wasn't the *only* thing you were able to do.

In M13, the goal was to have [Entrancer](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vedalken+Entrancer) + [Mind Sculpt](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Sculpt) + [Archaeomancer](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Archaeomancer) produce a "mill deck" that could happen *sometimes*, but not all the time—and Entrancer is a perfectly good win condition by himself, if he has to be. I'm interested to see the extent to which that pans out in the real world.

![](https://i.ormos.uk/0a/5e/0a5ec01b2972679307626e310b2b8dd59b56da650766e05c0ac91603446463ac.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card12b.jpg)

This card is bound to cause some headaches in more casual formats, but at a mana cost of ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif), you've got to do some work to enjoy the payoff.

One of my favorite cards of all time is [Dregs of Sorrow](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dregs+of+Sorrow), which was so iconic that for a time it was known by nothing but its mana cost. That definitely inspired the design of this card, and the art is a brilliant nod to Staples's inspired [Diabolic Tutor](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diabolic+Tutor). Mainly, though, I wanted there to be something in the set to do with a [Liliana](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana+of+the+Dark+Realms) ultimate—and I'm fairly sure that if every one of your [Swamp](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s taps for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif), you can find a way to win the game with this card.

![](https://i.ormos.uk/38/8d/388d7ac373cdf4e21399898d88e920a6f22790d1862092895f3fb6e81806eb8c.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card13b.jpg)

Like [Oblivion Ring](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) and [Negate](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Negate), I am pretty certain that [Duress](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duress) contributes to the health of any environment it's a part of. It constrains brokenness without itself being broken, and kickstarts (when executed properly) an evolving metagame wherein the card's strength against the environment waxes and wanes in direct proportion to its popularity. I was very happy to bring this card back after a year of being sidelined.

![](https://i.ormos.uk/0a/91/0a9134c14cb705c7892cd34c30cf1d9f7b8673b0a70fa6eaef52f99c5edd80f4.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card14b.jpg)

Destroy target creature.

It's amazing how long these words have taken to appear, absent any other accoutrements, on a **Magic** card. Not that it's a mistake for it to have taken this long, mind you—rather, it's a testament to the vast richness still out there that this game has yet to tap.

There's more going on than simply wanting to write words on a card, though. Something I feel is very important to a core set is its ability to communicate to newer players how they should react to strategies they face up against. One of the typical ways they tend to do that is by finding answers, ways of dealing with cards that cause problems. In order for them to do that, though, *those cards must exist in the first place.* Otherwise, what is there to find? Moreover, those cards must be immediately and viscerally comprehensible, or the ability for the newer player to adapt gets lost amid a sea of complexity.

That's why this set has "Destroy target land," "Destroy target creature," "Destroy target artifact," and "Exile target enchantment," all written on cards. They'll solve your problem. Eventually, you might realize you ought to be turning to [Oblivion Ring](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) or [Acidic Slime](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Acidic+Slime) or [Flames of the Firebrand](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flames+of+the+Firebrand) or whatever spell is most optimal for your deck, but the level-one option ought to be available for you, too.

![](https://i.ormos.uk/ff/8a/ff8ad32dfddf77419b5dc8b44560e769302a0591a5ff5a4b705b83ab9af5d45b.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card15b.jpg)

As I think I alluded to before, it's very important to all of us that a core set's containing roughly one-hundred fifty reprints continue to be a "feature" rather than a "bug." One of the ways to ensure that happens is to bring back popular, format-defining cards like this one. It also blends in nicely with the new Liliana and helps fill a hole left by the departure of [Day of Judgment](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment). Black isn't exactly hurting for mass removal in the current Standard environment, of course, but I can't exactly argue with another way to kill a [Geist of Saint Traft](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft). I remember packing four of these in *Odyssey* Block Constructed and I'm excited the card has another chance to shine more than a decade after it was first introduced.

![](https://i.ormos.uk/ac/a7/aca74809660cda4e649d3a6065c8d00357761e090445218214ee845355c17a3e.jpg)![](http://media.wizards.com/images/magic/daily/ld/ld202_card16b.jpg)

Another thing we try to do with our reprints is to ensure that they function differently in different contexts, so that the same card might not always carry the same play pattern. In ***Magic** 2012*, [Tormented Soul](https://web.archive.org/web/20120706000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tormented+Soul) was valuable primarily as a bloodthirst enabler. You played it on the first turn of the game, and it made all your guys bigger while continuing to deal damage. In ***Magic** 2013*, it combines powerfully with exalted, hitting your opponent every turn while the rest of your team holds back to block. A number of other reprints function similarly in the context of this set. It's the environment, not the cards, that sets the rules.

Part One and Done

Like I said, I've chosen to highlight only a fraction of the cards in ***Magic** 2013*. Some, of course, you'll hear about more over the upcoming weeks. Others I hope you play with and learn for yourself! Join me next week when I round out red, green, artifacts, and lands, and let me know of any other questions you have or cards you wish I'd talked about. As always, I can be reached on Twitter, in the forums, or via email.

Until next week,

Zac ([@zdch](https://twitter.com/#!/zdch))

* * *

  

![](https://i.ormos.uk/60/d8/60d87d61654a1f40c1e4806f9cbb8e1074ebce50f8b494311522c58ad958ea5f.jpg)![](https://i.ormos.uk/5a/54/5a54ab5a96d957f2715b57cd973ee070ec89c393fe81a313c742b559964251a3.jpg)[![](https://i.ormos.uk/94/75/9475d385402f55ca96b786c7712ed18a1fa2195c4e2b025f0fd971d4849cff1b.jpg)](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/prerelease-facts)![](https://i.ormos.uk/c2/4b/c24b45e1f4d82852fe7a27da6fc8ee4409cc4dd1aac2b11d5f34c919df79cfbb.jpg)![](https://i.ormos.uk/b2/1f/b21fd987a9b5bc9e80daf06a051885597bbb5880fdca75e11e98e7b6b8d1413f.jpg)[![](https://i.ormos.uk/9f/7f/9f7fe24b78c649a08392c6eb5fe504cc342e09e2f4db27343603176a962e853d.jpg)](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/Digital/DuelsOfThePlaneswalkers.aspx)[![](https://i.ormos.uk/a0/d2/a0d2a8773432e0974435624cf792218a96fa428fea6333c1937f0d770a8ddcc9.jpg)](https://web.archive.org/web/20120706000000/http://archive.wizards.com/Magic/TCG/products.aspx?x=mtg/tcg/products/magic2013)

![](http://archive.wizards.com/mtg/images/widgets/storelocator/SmallStoreLocator_Background_Left.png)

![](http://archive.wizards.com/mtg/images/widgets/storelocator/EN_SmallStoreLocatorGOText.png)
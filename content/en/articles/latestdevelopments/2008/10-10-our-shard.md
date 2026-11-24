---
id: 9kt90xz4
kind: article
lang: en
path: /en/articles/latestdevelopments/2008/10-10-our-shard
title: Our Shard
published: '2008-10-10'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: miketurian
  name: Mike Turian
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
    lang_detected: en
    capture_id: 729431
    url: https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
    captured_at: '2022-10-07 02:25:32+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
    lang_detected: en
    capture_id: 729431
    url: https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
    captured_at: '2022-10-07 02:25:32+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
    lang_detected: en
    capture_id: 729431
    url: https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
    captured_at: '2022-10-07 02:25:32+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
    lang_detected: en
    capture_id: 729431
    url: https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
    captured_at: '2022-10-07 02:25:32+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 9kt90xz4
  url: https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
  page_key: magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
  lang: en
  template: drupal
  captured_at: '2022-10-07 02:25:32+00'
  capture_id: 729431
  wayback_url: https://web.archive.org/web/20221007022532id_/https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
- document_id: 9kt90xz4
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/7
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/7
  lang: en
  template: aspx
  captured_at: '2013-07-07 19:19:31+00'
  capture_id: 623499
  wayback_url: https://web.archive.org/web/20130707191931id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/7
- document_id: 9kt90xz4
  url: https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-10
  page_key: magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-10
  lang: en
  template: drupal
  captured_at: '2022-10-01 05:07:39+00'
  capture_id: 729433
  wayback_url: https://web.archive.org/web/20221001050739id_/https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-10
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9kt90xz4
  capture_id: 729431
  url: https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
  wayback_url: https://web.archive.org/web/20221007022532id_/https://magic.wizards.com/en/articles/archive/latest-developments/our-shard-2008-10-09
  captured_at: '2022-10-07 02:25:32+00'
  template: drupal
  sha256: 6c0819ac3afae4ffc08a4fc46a1cbbbdecd6da1efbba52d1f4ccf5b41d6066c5
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
*As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on **Magic** development. Enjoy!*  
 –Kelly Digges, **magicthegathering.com** editor 

Welcome back!

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bant+Charm)](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bant+Charm)

"Mike we missed you so!" I know, and I've missed you too. So much has happened since I wrote those [three great preview articles](https://web.archive.org/web/20081010000000/https://magic.wizards.com/Magic/Magazine/Archive.aspx?author=Mike%20Turian). It feels like months, years have gone by since we saw each other last. Since then we've finished the development of *Shards of Alara* block, celebrated the launch of the new Gatherer, been a part of [*Duel Decks: Jace versus Chandra*](https://web.archive.org/web/20081010000000/https://magic.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/arcana/1608), and had some awesome exciting surprises (From the Vault: Squirrels)! Sweet.

Wait, you mean [From the Vault: Squirrels](https://web.archive.org/web/20081010000000/https://magic.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr30) was never released, and *Shards of Alara* just came out last week? This week is actually Bant Week? Didn't I just preview [Bant Charm](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bant+Charm)? I can only write so many great stories about awesome abilities like "Destroy target artifact."

You caught me; I knew that it has only been two weeks since I wrote my last Latest Developments column, but in **Magic** Ramp;D, the timing gets a little confusing. The world of **Magic** Ramp;D plays **Magic** like the rest of the world, except we use Sharpie cards without art. If you ever want to appreciate the card art more, try living without it.

Welcome to Magic Ramp;D!

I started playing **Magic** during *Revised*. The day *The Dark* was released I was hopping up and down at my local card store, I couldn't wait for the newest cards to be released. Today, as a **Magic** developer, I feel the same way as I did back then, but for totally different reasons.

Imagine this scenario. You stay up late one night preparing for a big test. You really care about the test because a lot of people are counting on you to not only pass but to get an A+. During the test there are lots of ups and downs, you have to make some tough decisions and educated guesses, but at the end of the day you feel like you really nailed it.

You stride up to the teacher and think, man I can't wait until I find out what grade I got on the exam. As you turn over your paper, the teacher announces "Well kids, I'm going on a sabbatical. I'll grade these tests and get them back to you in 365 days." Drat.

**Magic** Ramp;D works years in advance. Right now there are teams working on the sets codenamed "Live," "Long," and "Prosper." Those sets won't be released for 1-2 years. Kamigawa block is my **Magic** Black Hole. Considering my knowledge of **Magic** cards, *Champions of Kamigawa* cards are foreign to me. 

As a new employee to Wizards of the Coast in 2004, I left the real **Magic**-playing world at the beginning of *Fifth Dawn* and reentered with *Ravnica: City of Guilds*. When I started working at Wizards, *Saviors of Kamigawa* cards were in their final days of development. I was in the room when [Kataki, War's Wage](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kataki%2C+War%27s+Wage) got its final tweak, but that is the only *Saviors* card I can remember being altered. 

It Is Time to Sticker!

![](http://wizards.com//mtg/images/daily/ld/ld7_peter.jpg)  

Here are some of the many cards we have proxied with stickers sitting in our work area. Last week we ran a 30+ person play test of "Live" for people in every department of Wizards to try out our latest set and give feedback. For the play test we proxied 2500 cards. That is a whole lot of stickers!

Our newest intern Peter Knudson has been initiated by doing a lot of stickering for us. He was relating to me that for white cards he was stickering over [Enduring Ideal](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enduring+Ideal). He said that [Enduring Ideal](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enduring+Ideal) was one of his favorite **Magic** cards before he came to Wizards, and he was sad to be turning them into play test cards. I could relate; I was initiated using [Fact or Fiction](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction)s as my sticker bait. That day gave me great insight into how different our world was from the real world. Even today, it still hurts when we sticker over some of my all-time favorite **Magic** cards.

Customer Service

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=%5Bcard%5D)](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%5Bcard%5D)

One great resource that **Magic** Ramp;D relies on is our Customer Service department. Not only do they contribute to our play test sessions, but they compile a list of questions that people call in asking about. 

Steve Warner used to work in Customer Service before switching to Research and Development years ago. In meetings, developers will often talk about how "simple" an ability like regeneration is. Steve would then speak up, "When I worked in Customer Service, people would always call in asking if they could regenerate from a sacrifice." You can't, but if you could a card like [Augur of Skulls](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Augur+of+Skulls) would become a lot better.

For *Shards of Alara*, take a guess as to which card causes the most confusion. I'll give you a hint: it is actually a full cycle of cards.

The cycle of Herald creatures ([Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald), [Sphinx's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Herald), [Demon's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demon%27s+Herald), [Dragon's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon%27s+Herald), [Behemoth's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Behemoth%27s+Herald)) has caused the most calls to Customer Service. People all wanted to believe that you could sacrifice just one gold creature, say [Rhox War Monk](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rhox+War+Monk), to satisfy all three colors mentioned on [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald).

As outlined in a recent [Ask Wizards Rules Corner](https://web.archive.org/web/20081010000000/https://magic.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/askwizards/1008#1003), you must sacrifice three creatures (one blue, one white, one green) in order to pay the cost on [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald). Then you can go fetch [Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel).

In the Beginning

For me, these articles are a look backwards in time. For example, [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) was created almost exactly 365 days ago. At the time it was known as " ." Then two weeks later it was given its first actual name, Herald of Triple Angel. The Herald was a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 1/3 with the following text.

> Sacrifice CARDNAME, a green creature, and a blue creature: Get a \[Super Angel\] from anywhere and put it into play.

The idea for the cycle of Heralds came from cards like [Spirit of the Night](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spirit+of+the+Night) and [Scion of Darkness](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scion+of+Darkness). One of the ideas that the Jund team toyed with early on was having Shamans summon super-powerful Dragons along the lines of [Spirit of the Night](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spirit+of+the+Night) and [Scion of Darkness](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scion+of+Darkness) by sacrificing themselves. 

We had even gone so far to suggest a mega-cycle in which nine little Shamans fetched three Dragons, which in turn fetched one ultimate ridiculous Dragon. While the Jund team originally liked the idea, it decided to go with the devour mechanic in the end.

Bill Rose was still disappointed to see the Shaman fetchers go. Bill was the lead designer of *Mirage* and the original proponent of [Spirit of the Night](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spirit+of+the+Night). He liked the "Herald mechanic" enough to reinsert the mechanic into all five colors of *Shards of Alara*. In fact, when [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) first entered the file, "Super Angel" (which would become [Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel)) hadn't been created yet. 

WUBRG

![](http://wizards.com//mtg/images/daily/ld/ld7_cardback.jpg)  

WUBRG stands for white, blue, black, red, green. Everything we work on with **Magic** is put into WUBRG order (and often in rarity order as well). The practical implication of this is that when you load up a new **Magic** card file the first card you view is a common white card. For a while [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) was a common, and was the first card you would see when looking at *Shards of Alara*.

It isn't an easy job being CW01 (common white #1). A lot more people view you than, say, UG07 (uncommon green #7). Green is hidden way deep into the file, while CW01 is unavoidably at the top. CW01 is the first impression.

[Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) had the task of representing *Shards of Alara*. After a number of weeks [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) was moved to uncommon. Two factors went into this decision. First, we were worried about the confusion the card would cause. The bigger factor was when the "Super Angel" cycle was included as mythic rares. When we drafted the set with [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) at common, you would see tons of Heralds and few of their mythic rare partners. We wanted the experience of fetching the awesome mythic rare to occur, but rarely, in Draft. That would make for the best overall experience. I like to think that the flavor text on [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) makes this point well.

*Rigorous faith and belief are rewarded on occasion, and richly so.*

Another change from the original version was that the final version tapped to fetch the [Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel). Before the change you could surprise your opponent by having out a green creature and a blue creature. Then when you would play [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald), your opponent wouldn't be able to stop the Herald from activating by killing it. They could only stop the fetch by killing your "side-colored" creatures.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Angel%27s+Herald)](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald)

By adding the tap activation, the Herald's became more vulnerable letting us put maximum power into their mythic rare back-up. 

The power / toughness started out as different on all five Heralds. [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) was a 1/3. Changing them all to one-mana 1/1s was a controversial decision. Some Ramp;D members liked the ability to play the Heralds based on their power / toughness stats alone. In the end, the development team disagreed. We valued the maximum contrast available. If [Behemoth's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Behemoth%27s+Herald) was a 4/4 creature, you would sacrifice it less often, and it would take away from the fact that it is fetching [Godsire](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Godsire), an 8/8 that makes 8/8s.

In my opinion, I love the idea that by making [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) a 1/1 it shouldn't be in your opponent's deck unless they have the [Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel). That means if they do play the [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) then you must kill it or they will fetch out the [Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel). This leads us to the Herald's bluff!

The Herald's bluff is simple. Put a Herald into your appropriately colored Draft deck when you don't have the mythic rare to fetch! Your opponent may very well be fooled into wasting a removal spell on the poor little Herald so that you aren't able to fetch out your non-existent mythic rare. It may not be the best strategy in the world to run this bluff, but the first time it works you will be satisfied knowing your little 1/1 bluffed them.

Empyrial Archangel

[Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel) was created by designers a full month and a half after [Angel's Herald](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel%27s+Herald) came into existence. This is a common occurrence; often our first impressions of cards and mechanics are based on ideas that aren't fully formed.

Here was the original text of [Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel).

> Flying  
>  All damage that would be dealt to you is dealt to CARDNAME instead.  
>  If a spell or ability targets CARDNAME, counter that spell or ability unless its controller pays 4.

Being in the time-delayed world of **Magic** Ramp;D, it becomes difficult to recall exactly what one felt about a given subject. For instance, I remember getting mad about [Nath's Buffoon](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nath%27s+Buffoon) and [Warren-Scourge Elf](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warren-Scourge+Elf). Looking at those cards now I can't exactly remember why, but I do know I was wrong. I remember that [Notorious Throng](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Notorious+Throng) didn't used to [Time Walk](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk) for its prowl bonus, but I couldn't tell you what it did instead

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Empyrial+Archangel)](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel)

[Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel) is a card I have a distinct memory of working on. The old wording above just doesn't feel right. Our mythic rare cycle of giant creatures are all supposed to be super-exciting Timmy cards. They are supposed to be immediately recognizable as kick-ass **Magic** cards.

The words "If a spell or ability targets CARDNAME, counter that spell or ability unless its controller pays ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)" don't scream out, "awesome." Instead they were giving everybody problems. As a developer, in a crisis such as this one, I go to my old standby technique: figure out what the heart of the card is, and go from there.

This was an Angel that was supposed to protect its controller from harm and be tough to deal with itself. So in that spirit, I suggested removing "If a spell or ability targets CARDNAME, counter that spell or ability unless its controller pays 4" and adding shroud. Shroud is just a cooler way to say that giant block of text, and it does practically the same thing. That is exactly what we did, and made the Angel a 5/8 for good measure.

Since shroud makes the Angel seem unstoppable, here is a hint for dealing with her. The next time your friend brings out his [Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel) deck, reach for your deathtouch creatures. A [Wren's Run Vanquisher](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wren%27s+Run+Vanquisher) proves to be a big problem for the Archangel. When the deathtouch damage is redirected from your opponent to the Archangel, the Archangel will die from the deathtouch. The best [Empyrial Archangel](https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel) can do against a deathtouch creature is to block and kill it, since it will die anyhow.

Last Week's Poll Question

<table><tbody><tr><td colspan="3"><b>Which mythic rare are you looking forward to getting the most?</b></td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sarkhan+Vol">Sarkhan Vol</a></td><td>2129</td><td>26.0%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elspeth%2C+Knight-Errant">Elspeth, Knight-Errant</a></td><td>1109</td><td>13.5%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tezzeret+the+Seeker">Tezzeret the Seeker</a></td><td>1108</td><td>13.5%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rafiq+of+the+Many">Rafiq of the Many</a></td><td>627</td><td>7.7%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lich%27s+Mirror">Lich's Mirror</a></td><td>542</td><td>6.6%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hellkite+Overlord">Hellkite Overlord</a></td><td>439</td><td>5.4%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Empyrial+Archangel">Empyrial Archangel</a></td><td>426</td><td>5.2%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Godsire">Godsire</a></td><td>422</td><td>5.1%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kresh+the+Bloodbraided">Kresh the Bloodbraided</a></td><td>243</td><td>3.0%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prince+of+Thralls">Prince of Thralls</a></td><td>237</td><td>2.9%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Vengeant">Ajani Vengeant</a></td><td>224</td><td>2.7%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedris%2C+the+Traitor+King">Sedris, the Traitor King</a></td><td>215</td><td>2.6%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx+Sovereign">Sphinx Sovereign</a></td><td>174</td><td>2.1%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sharuum+the+Hegemon">Sharuum the Hegemon</a></td><td>171</td><td>2.1%</td></tr><tr><td><a href="https://web.archive.org/web/20081010000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mayael+the+Anima">Mayael the Anima</a></td><td>129</td><td>1.6%</td></tr><tr><td><b>Total</b></td><td><b>8195</b></td><td><b>100.0%</b></td></tr></tbody></table>

  

I'm glad to see three of the four planeswalkers living at the top of this list. Even though they're just a handful of cards in a 249-card set, **Magic** Ramp;D spends extra time and effort making sure that the planeswalkers come out great. We like seeing that A+ grade come back for all of our hard work.

This Week's Poll Question

<table><tbody><tr><td><div><b>What is your favorite card type?</b>InstantSorceryEnchantmentArtifactCreatureLandPlaneswalkerTribal<a href="https://web.archive.org/web/20081010000000/https://magic.wizards.com/Magic/tcg/NewtoMagic.aspx?x=mtg/tcg/newtomagic/gamebasics">I don’t know what card type means.</a></div></td></tr></tbody></table>
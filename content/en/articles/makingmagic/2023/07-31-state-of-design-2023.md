---
id: 6qzgqkre
kind: article
lang: en
path: /en/articles/makingmagic/2023/07-31-state-of-design-2023
title: State of Design 2023
published: '2023-07-31'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/state-of-design-2023
    lang_detected: en
    capture_id: 230455
    url: https://magic.wizards.com/en/news/making-magic/state-of-design-2023
    captured_at: '2024-06-09 03:31:00+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/state-of-design-2023
    lang_detected: en
    capture_id: 230455
    url: https://magic.wizards.com/en/news/making-magic/state-of-design-2023
    captured_at: '2024-06-09 03:31:00+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/state-of-design-2023
    lang_detected: en
    capture_id: 230455
    url: https://magic.wizards.com/en/news/making-magic/state-of-design-2023
    captured_at: '2024-06-09 03:31:00+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/state-of-design-2023
    lang_detected: en
    capture_id: 230455
    url: https://magic.wizards.com/en/news/making-magic/state-of-design-2023
    captured_at: '2024-06-09 03:31:00+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 6qzgqkre
  url: https://magic.wizards.com/en/news/making-magic/state-of-design-2023
  page_key: magic.wizards.com/en/news/making-magic/state-of-design-2023
  lang: en
  template: contentful
  captured_at: '2024-06-09 03:31:00+00'
  capture_id: 230455
  wayback_url: https://web.archive.org/web/20240609033100id_/https://magic.wizards.com/en/news/making-magic/state-of-design-2023
- document_id: 6qzgqkre
  url: https://magic.wizards.com/en/news/making-magic/state-of-design-2023?a
  page_key: magic.wizards.com/en/news/making-magic/state-of-design-2023?a
  lang: en
  template: contentful
  captured_at: '2023-07-31 15:56:06+00'
  capture_id: 230458
  wayback_url: https://web.archive.org/web/20230731155606id_/https://magic.wizards.com/en/news/making-magic/state-of-design-2023?a
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 6qzgqkre
  capture_id: 230455
  url: https://magic.wizards.com/en/news/making-magic/state-of-design-2023
  wayback_url: https://web.archive.org/web/20240609033100id_/https://magic.wizards.com/en/news/making-magic/state-of-design-2023
  captured_at: '2024-06-09 03:31:00+00'
  template: contentful
  sha256: 36cda8021ece7112de0e9f890574b04acaa39fcf95208c123587c24875f82f21
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - Email
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
When I became head designer back in 2003 (yes, this year is my 20th anniversary in the role), one of the things I started doing was writing a yearly column about the design of the previous "*Magic* year." The series is titled after a speech the US president gives once a year. My first column appeared in 2005, as we work a couple years ahead and that's when the first sets I oversaw as head designer were released.

Here are my last eighteen columns:

*   [2005](/en/articles/makingmagic/2013/12-03-state-of-design-2005)
*   [2006](/en/articles/makingmagic/2006/08-21-state-of-design-2006)
*   [2007](/en/articles/makingmagic/2013/12-03-state-of-design-2007)
*   [2008](/en/articles/makingmagic/2013/12-03-state-of-design-2008)
*   [2009](/en/articles/makingmagic/2009/08-23-state-of-design-2009)
*   [2010](/en/articles/makingmagic/2010/09-27-state-of-design-2010)
*   [2011](/en/articles/makingmagic/2011/08-22-state-of-design-2011)
*   [2012](/en/articles/makingmagic/2012/08-27-state-of-design-2012)
*   [2013](/en/articles/makingmagic/2013/08-26-state-of-design-2013)
*   [2014](/en/articles/makingmagic/2014/08-18-state-of-design-2014)
*   [2015](/en/articles/makingmagic/2015/08-24-state-of-design-2015)
*   [2016](/en/articles/makingmagic/2016/12-27-state-of-design-2016)
*   [2017](/en/articles/makingmagic/2017/08-28-state-of-design-2017)
*   [2018](/en/articles/makingmagic/2018/08-20-state-of-design-2018)
*   [2019](/en/articles/makingmagic/2019/08-26-state-of-design-2019)
*   [2020](/en/articles/makingmagic/2020/08-17-state-of-design-2020)
*   [2021](/en/articles/makingmagic/2021/08-16-state-of-design-2021)
*   [2022](/en/articles/makingmagic/2022/08-01-state-of-design-2022)

Here's how this column is structured: I'll begin by looking back at the last year, talking about the highlights and the lessons of the year. I then examine each booster release and talk about the highlights and lessons of that set. Note, as always, I'll be talking big-picture design rather than making card-by-card comments. Also, as *The Lord of the Rings: Tales of Middle-earth™* hasn't released at the time of my writing this article, I'll be talking about it in next year's "State of Design" column.

As always, I begin with the same question: How was the last year of *Magic* design?

I think it was a pretty good year. We made sets that had players talking and managed to do things we'd never done before. I think each set had a strong vision and plenty of fun mechanics. That's not to say we optimized every decision, but all in all, I think it was a good year for *Magic* sets.

## Overall *Magic* Design

### Highlights

*   **The sets managed to each have their own identity while telling a singular story.**

One of the challenges we've had since moving away from the block model is trying to tell a singular story through sets with their own mechanical identity. I think the sets this year did a good job handling the main story focus (the advancement of the Phyrexians) while each having their own feel, both in play and in creative expression. For example, I could show you four different Phyrexian cards from the four different premier sets, and you would have a good chance to identify which card was from which set, because each set approached the Phyrexians in a different mechanical context. In the past, we tended to approach storylines through one mechanical identity. This new approach gives more nuance and allows players more flexibility in how they can express that story element through deck building and gameplay.

*   **We leaned well into nostalgia.**

Each set this year allowed us to dip into various elements of the game's past. *Dominaria United* looked at the various sets that have taken place on *Magic*'s original plane. *The Brothers' War* let us tell the most famous story of the game through the lens of gameplay, letting us finally make characters that have existed for almost three decades into cards. *Phyrexia: All Will Be One* tapped into the long history of the Phyrexians. *March of the Machine* revisited almost every plane the game has taken us to. It was nice to showcase so much of *Magic*'s past during its 30th year.

*   **We were bold in set concepts.**

One of the complaints games get when they last long enough is that the game designers are just resting on their laurels and aren't pushing boundaries. That wasn't the case this year. While *Dominaria United* was a more traditional set, *The Brothers' War*, *Phyrexia: All Will Be One*, and *March of the Machine* were bold in their design. Even *Unfinity* and *March of the Machine: Aftermath*, which were the two biggest stumbles of the year, were each trying something new.

### Lessons

*   **The sets were a little too creatively insular.**

This is the flip side of the sets being so nostalgic. I think we were a little too insular in our themes this year. If you'd never heard of Dominaria, the Brothers' War, the Phyrexians, or if you weren't aware of all the planes of the Multiverse, this year was a bit daunting. We were shy in simple top-down sets based on genre clusters or story tropes. Every set this year came with a little "previously . . ." explanation, and that's not ideal for a game that's growing as fast as *Magic*. It's crucial that new players can find things to identify with without a lot of reading first.

*   **The sets were more polarizing than normal.**

While I'm a big believer that individual cards, themes, and mechanics can be polarizing, we must be careful how polarizing entire sets are. We want our sets, especially the premier ones, to be a product that has something to offer every *Magic* player. I appreciate the boldness of this year's sets and how focused they were in their vision, but we must also ensure we're not creating premier sets that make too many players go "I'm going to sit this one out."

*   **There needs to be more synergy between sets.**

This has been an ongoing theme ever since blocks went away. We want consecutive sets to have mechanical overlap so you can continue to update a deck as new sets come out. We did have some mechanical themes (artifacts, Phyrexians, etc.) run through multiple sets this year, but we also had other themes that were too linear, too focused on a single set. I'll admit that this is a hard problem to solve, as each set has so many different factors that it has to address, but it's something we need to learn to do better in the world of each set being played in Limited by itself.

## *Dominaria United*

### Highlights

*   **Players enjoyed the *Invasion* feel of the set.**

*Dominaria* had been modeled off *Alpha*, so the *Dominaria United* Set Design team decided to model *Dominaria United* after another famous set that took place on Dominaria—*Invasion*, as the set followed a new Phyrexian invasion. With kicker, domain, and a theme of splashing colors, the set did a lot to mechanically call back to the earlier set. A lot of players appreciated this.

*   **The many references to the past were appreciated.**

Dominaria has been home to the most *Magic* sets, especially ones from the game's first decade. *Dominaria United* tapped into the nostalgia of this by having a lot of nods to characters, objects, and events from Dominaria's past. This included the *Legends Retold* promotion, which redesigned several legendary characters that had been introduced in *Legends*. Many players responded positively to all the references in the set.

*   **The set had enjoyable Limited play.**

The set's themes led to Limited play being a bit slower, which allowed more build-up. This combined with the ability to more easily splash other colors led to a dynamic Limited game that got a lot of high marks from players. The Limited theme that was called out the most was the defender theme.

### Lessons

*   **The set felt a bit generic for some players.**

A common complaint I got about *Dominaria United* was that it felt a little bland when compared to other premier sets of the year. Many players called it "safe" and noted that, while it played well and had usable cards, it just wasn't a very memorable set. The set just didn't have much innovation.

*   **The set had a number of flavor-related issues.**

There were a lot of legendary creatures in the set, but some players felt not enough of them had any lore built around them. Others complained that the sleeper-agent element, which was key to the story, was not represented in the set. Finally, players wished the *Weatherlight* crew was more involved in the story.

*   **Limited had some issues.**

Some players felt it was too easy to splash other colors of mana, claiming that too many players were playing some variation of green domain (having a green base and splashing many or all the other colors). There was also some concern that there was a bit too much recursion.

## *Unfinity*

### Highlights

*   **Many players loved the flavor and humor in the set.**

Many players were fans of the set's creative, from its worldbuilding and card concepts to its art, names, and flavor text. The set also had a lot of Easter eggs that enfranchised players could have fun discovering.

*   **There were a lot of positive comments about the set's Limited play.**

From outside assistance and minigames to quirky individual designs, the set pushed boundaries in fun ways that many players enjoyed. Both stickers and Attractions, the set's two main mechanics, led to unique Limited interactions.

*   **Some players appreciated that over half of the cards were Eternal legal.**

This was a very divisive topic, but numerous players seemed excited by the fact that a portion of the cards in the set could be played in eternal formats. One of the biggest liabilities of previous *Un-* sets was that they weren't legal in the most-played formats. Many fans of *Un-* sets were excited that they could play the cards in formats they formerly couldn't, especially Commander.

### Lessons

*   **Other players greatly disliked that there were Eternal-legal cards in the set.**

The Eternal legality of over half the cards was a big point of contention. Many players felt it turned them off the product. Regardless of whether you liked them, there was a general agreement that players would have preferred the non-legal ones to be in a silver border. The acorn was hard to see and made it trickier to tell what was Eternal legal and what was not.

*   **The set had too much complexity.**

Both main mechanics, stickers and Attractions, require a lot of concentration to track. In addition, we filled the set with a lot of one-off cards that ask you to care about things players don't normally care about. This all combined to create a play environment that was too taxing for many players.

*   **Stickers had several logistical issues.**

The stickers were small. They were easy to lose. The glue didn't hold out well, so the stickers would quickly lose their stickiness when reused. The stickers didn't stick back on their sheet well once you removed them. This all combined to create a barrier to play. It also led to a lot of players complaining that most of the sticker cards were Eternal legal.

## *The Brothers' War*

### Highlights

*   **Many players liked having a set that looked back at one of *Magic*'s greatest stories.**

Players liked seeing old characters they recognized in card form. They enjoyed how we conveyed the story through the cards. They enjoyed how the play matched the feel of the story they'd come to know. They also liked how the design made the artifacts feel like a throwback while still applying modern design technology. (A good example of this included most artifacts having a generic cost, with many having monocolor activations.)

*   **The mechanics were generally well received.**

Prototype was seen as a cool new mechanic. Unearth on artifacts was flavorful. The meld cards were splashy and cool. Powerstones finally got a mechanical identity. All in all, players thought the design team created a nice suite of mechanics that matched well with the story and plane.

*   **We upped our bonus sheet game.**

The bonus sheet did a good job of reflecting the set it was in by being all artifacts. The retro frames helped capture the story's timeline. The biggest compliment from fans concerned how the cards on the sheet were chosen to help make the Limited gameplay better. Many cards on the sheet enhanced existing archetypes or created interesting new draft themes that were synergistic with the main cards in the set.

### Lessons

*   **The set was hard to connect to if you didn't know the source material.**

For long-time fans who have talked about the Brothers' War for years, the set was an exciting opportunity to finally see things they'd heard of come to life in card form. But if you weren't familiar with the story, it was hard to connect with the set since driving force of its structure matched the story. Many less enfranchised players reported they were a bit lost and had trouble connecting with the set.

*   **Limited was a bit fast for a set with a theme of giant robots.**

Many players thought the set would draft closer to *Rise of the Eldrazi* where the environment kept aggro at bay and allowed players to build up their giant creatures. While some of this was possible, the existence of some strong aggro archetypes dashed this hope for a lot of players.

*   **The Transformer cards felt out of place.**

Transformer as an overlay made some sense because the set was about giant robots, but the core of the set for many players was nostalgia. These players felt seeing cards of a different IP flew in the face of that.

## *Phyrexia: All Will Be One*

### Highlights

*   **Players generally enjoyed the reworking of poison.**

The use of toxic instead of infect, corrupted, or proliferate created environments in both Limited and Constructed that allowed more variance with how poison played out. Poison in *Scars of Mirrodin* block forced players to choose to be all in or not in at all. The revamped version in *Phyrexia: All Will Be One* added a lot of nuances to how poison played and was generally seen as an improvement (although there were some infect fans that were sad to see it not return).

*   **The use of oil counters created a unique environment that was appreciated.**

*Magic* sets most often have one primary counter in them to ease Limited play. In most sets, it's +1/+1 counters. Occasionally we make sets that use -1/-1 counters. *Phyrexia: All Will Be One* tried a brand-new counter: oil counters. It allowed us to craft a different kind of "counters matter" environment, one which allowed proliferate to function differently than its previous two uses (in *Scars of Mirrodin* block and *War of the Spark*). Because oil could have numerous functions, some players noted it was a bit harder to track. Others pointed out that they would have rather we used an existing counter type (charge was the one most often noted) rather than oil.

*   **The Phyrexian feel permeated throughout the set.**

The Phyrexians are *Magic*'s oldest villains (premiering in the second-ever expansion, *Antiquities*). Many players enjoyed how the set truly captured the feel of the Phyrexians from the gameplay to the mechanical themes to the art to the overall look and feel of the cards.

### Lessons

*   **The Phyrexian flavor was off-putting.**

While the Phyrexians are beloved by some, they're polarizing characters, meaning there was a swath of players that disliked the set for all the things I just noted above. For those players, the set was too bleak and "icky," and they wished the set wasn't quite so monolithic in its overall feel.

*   **The set was too parasitic (within the confines of Standard).**

The mechanics in the set, with poison being the biggest culprit, really relied on other things in the set. If you wanted to build decks around them, it was hard to include lots of cards from any other set in Standard. Many players voiced a desire for us to spread some of Phyrexia's mechanics to other sets in the year, particularly *March of the Machine*, where the Phyrexians were the main villains of the set, with fans wanting more cards that create poison counters or care about poison.

*   **Limited was too fast.**

Another common complaint was that the Limited environment was a bit too aggressive. There were a lot of themes, oil counters being called out the most, that players felt they didn't get to explore because the games didn't last long enough.

## *March of the Machine*

### Highlights

*   **The set had very solid and enjoyable mechanics.**

There was a lot mechanically going on in *March of the Machine*. There was a new card type, there were a bunch of different uses of double-faced cards, there were multiple team-up mechanics. Battles were continually called out as a cool new addition to the game, with many players eager to see them in other sets (although I got numerous notes about how the sideways orientation made them hard to read on the site). Incubate and the Phyrexian transformation cards were seen as a good way to capture the feel of the Phyrexians. The Phyrexian Praetors that turned into Sagas were particularly popular. Players liked the gameplay of backup and were happy to see convoke return. Team-up legendary creatures were also a huge hit. All in all, the general response was that the mix of mechanics was great.

*   **The set had a very fun Limited environment.**

Some of the most common feedback I got involved the fun Limited environment. It had a lot of depth, making it very replayable. All the mechanics I listed above had good synergy with one another, and players enjoyed the various archetypes (with "double-faced cards matter" as a standout). Some players have called *March of the Machine* one of the top Limited environments of all time. Another common compliment concerned how cleverly the bonus sheet was used to enhance Limited gameplay, with many cards on the sheet enhancing various draft archetypes. Finally, the theme of legendary creatures was called out as a positive by a lot of players.

*   **Many players loved the immense scope of the set.**

*Magic* has never told a story before of this scope, and a lot of players enjoyed the breadth of it. They liked seeing all the references to the various planes and the characters and creatures from them. Most *Magic* sets have Easter eggs, but never at this volume. A note I got a lot was that players wished there had been some mechanism, such as watermarks, that might have helped them identify where each card took place.

### Lessons

*   **The story was too big for one set.**

While players generally loved the scope, many felt we had bitten off too much for just one set. The common reply was that they wished this had been two sets (with some suggesting that it should have been more than that). There was just too much going on to do it justice with the number of cards available.

*   **The Phyrexians were too easily defeated.**

This complaint is connected to the last one. As the invasion and the response to the invasion all had to be done in a single set, it felt as if the Phyrexians lost almost instantaneously upon attacking. The Phyrexian threat had been built up for over a decade, so the quick defeat felt frustrating for the many fans of the Phyrexians. If we had two sets, we could have made the Phyrexians successful in the first set and included a surprise victory for our heroes in the second set.

*   **Limited was too complex and a bit bomb-y.**

While players seemed to generally enjoy the Limited formats, a common complaint was that there was a little too much going on, and victory was too often tied to opening one of the bombs, either from the main set or from the bonus sheet (which generally had high marks other than this issue).

## *March of the Machine: Aftermath*

### Highlights

*   **Players liked that Wizards of the Coast was experimenting.**

Some players have asked us for years to produce sets without Limited in mind. Others just liked the fact that we were willing to think of products in a different way, as it might allow us to do things we normally couldn't.

*   **There were a bunch of fun individual designs.**

Most of the positive comments on the set came down to card-by-card reviews. There were numerous fun designs. We were called out on one group of cards in particular: the legendary creatures that had formerly gotten planeswalker cards. There were many Commander players who enjoyed that some of their favorite characters could now be commanders.

### Lessons

*   **The set was too small.**

Fifty cards just isn't enough for a whole set. There was too much duplication when opening a box, and there just wasn't enough in the set to explore.

*   **Most players didn't like paying the same amount for fewer cards.**

This was probably the loudest complaint. We experimented with selling boosters without the commons, and it didn't go well. The notes I got were either "give us the same number of cards as normal" or "charge less."

*   **The set was sold as story focused, but not much happened story-wise in the set.**

The premise of the set was that it was going to tell the aftermath of the latest Phyrexian war. Yes, many Planeswalkers lost their sparks and King Kenrith and Queen Linden were killed, but not much else was told through the cards. Players expected story spotlights and more online stories. The set should have delivered more on its premise of showing the aftermath of the war.

*   **Many players seemed unhappy with the Planeswalkers losing their sparks.**

Planeswalkers have always been the special characters of *Magic*. Many players didn't understand why we had decided to remove their sparks. The game has plenty of legendary creatures, so why did we turn what was the most unique group of characters into something more mundane? Also, the fact that there wasn't a definitive list meant players would have to wait and worry about the fate of their favorite Planeswalkers.

## Another Year Gone By

We've come to the end of our *Magic* year. I hope my insights reflect a lot of your feelings about this year's sets. I think it's important to look back critically and understand what we did right and wrong to help guide future *Magic* sets, and I want to thank everyone who took the time to give me your feedback about any of the sets I talked about.

As always, I'm curious for your feedback on today's column and my thoughts on the last year of set releases. Email me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Until next time, may you enjoy the fruits of the last year's releases.
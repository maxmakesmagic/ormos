---
id: 2n41jsfp
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/03-01-magical-powers-of-ten
title: Magical Powers of Ten
published: '2013-03-01'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: daveguskin
  name: Dave Guskin
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
    lang_detected: en
    capture_id: 727335
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
    captured_at: '2022-08-17 12:54:39+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
    lang_detected: en
    capture_id: 727335
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
    captured_at: '2022-08-17 12:54:39+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
    lang_detected: en
    capture_id: 727335
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
    captured_at: '2022-08-17 12:54:39+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
    lang_detected: en
    capture_id: 727335
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
    captured_at: '2022-08-17 12:54:39+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 2n41jsfp
  url: https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
  page_key: magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
  lang: en
  template: drupal
  captured_at: '2022-08-17 12:54:39+00'
  capture_id: 727335
  wayback_url: https://web.archive.org/web/20220817125439id_/https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
- document_id: 2n41jsfp
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/236&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/236
  lang: en
  template: aspx
  captured_at: '2013-07-01 20:23:43+00'
  capture_id: 231399
  wayback_url: https://web.archive.org/web/20130701202343id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/236&print=true
- document_id: 2n41jsfp
  url: https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-02-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-02-26
  lang: en
  template: drupal
  captured_at: '2021-09-27 16:44:08+00'
  capture_id: 727328
  wayback_url: https://web.archive.org/web/20210927164408id_/https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-02-26
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 2n41jsfp
  capture_id: 727335
  url: https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
  wayback_url: https://web.archive.org/web/20220817125439id_/https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-03-01
  captured_at: '2022-08-17 12:54:39+00'
  template: drupal
  sha256: 29e3b8d0fa0db90efea1130553705b4592649bcfc059c8ec446316e9063a18a9
render_recovery: []
---
Hello! My R&D title is now experience designer, so I thought I would spend an article on the idea of development from that perspective. What does an experience designer do, you may ask? I spend the vast bulk of my time (and some of the time of other developers, designers, editors, creative writers, artists, marketers, production specialists, sales/trade reps, and many more!) working to provide in-store experiences like:

*   The *Return to Ravnica*/*Gatecrash* Prerelease Packs;
*   The slightly-different-but-still-awesome *Dragon's Maze* Prerelease Packs, along with the Implicit Maze–running activity;
*   Epic moments like the opening of the Helvault; and
*   As-yet-unannounced "Friends"-block-related activities that will blow your proverbial socks off.

These experiences have one very specific purpose: ***they enhance fun***. We are always looking for ways to enhance fun; the tricky bit is in using a light touch, since **Magic** itself is fun and we don't want to stray too far from its core identity as the strategy game you all know and love. Plus, enforced fun just isn't fun, you know?

![](https://i.ormos.uk/a7/b0/a7b07d2be85b45e6c1ab1f376075f1f03a61001dc8e43fbef4e3e7599ddb190d.jpg)

Take a trip with me through the layers of experiencing **Magic**, and we'll see where development can enhance fun. What are the ways in which **Magic** is fun to experience? These recent designs for big events are the latest in our toolbox, but as you'll see, we try to apply fun at every scale of **Magic**!

(As an aside, while I do my best to replicate the feel of the old educational video "Powers of Ten" in **Magic** terms, I recommend going to view [that video in its entirety on YouTube](http://www.youtube.com/watch?v=0fKBhvDjuy0). It's a little campy, but super interesting. Especially if you love science. SCIENCE!)

### 10^0: The Card

The most basic unit we affect as developers is the ***card***, the atom of our **Magic** universe. Cards can be changed in a number of ways to make things fun. A lot of folk think of this as the primary job of development: to "garden," or carefully shape, each card in a set to provide fun play experiences and/or balanced environments. There is certainly work to be done here—if the individual cards aren't fun, the rest of the work we might build on top of the cards is probably not going to enhance anything!

Let's use an example card I designed—[Remember the Fallen](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remember+the+Fallen) from *New Phyrexia* (codenamed "Guts and Bolts" in design and development). What maximizes the experience of this card? Here are a few things that make this card fun to play and think about:

*   It has a straightforward pair of effects that both have sweet "what if?" scenarios associated with them.
*   It lets you do both, at an appealing price (free), because it is a reward for playing into set themes.
*   It has a story thread—Elspeth is lamenting the loss of *Mirrodin* to the (new) Phyrexians.

![Remember the Fallen](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Remember+the+Fallen)

 

Is ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) the right cost for this card? Wouldn't it be more appealing and powerful at ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) or ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)? Maybe at some cost for "both" it would be much harder to get to work properly and thus give more of an ecstatic moment when it finally works. Through testing, we try to approach the limit of the most impactful spot for a card's mana cost. We are not trying to figure out how far something can be pushed, but rather what position the card should occupy to maximize its fun-potential for the intended target audience. Sometimes that's a tough choice about whether to draft it, sometimes it's an obvious Constructed all-star, and sometimes it's so bad that players seek it out as a way to win with a certain style (e.g., [Chimney Imp](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chimney+Imp)).

Each card has a role—usually that it was quite literally designed to fill—and development tries to make sure it clicks into place. If you think of the purpose of a **Magic** card as its primary game function, then its secondary role in generating memories about **Magic** is like its secret purpose. The mechanics are necessary to make the game work, but their role in making stories are the true power of the cards in the **Magic** experience.

### 10^1: Card Interactions

Each card can only do so much. Cards are played in the context of other cards. In these ***interactions*** among many cards, we get some additional ways to enhance fun. Think on the kinds of memorable interactions you have encountered and the fun of exploring their impact on games:

*   Discovering a two-card combo;
*   Executing a series of back-and-forth attacks in a draft game, culminating in a Falter effect; and
*   The rock-paper-scissors game of weenie rush vs. sweeper effects vs. resilient creature in Constructed.

These are the stories that stick with you about a particular format or game-play experience. In fact, most **Magic** players, when they discuss **Magic** excitedly with each other, are going over a play-by-play of recent games. This is the story of interaction.

The most obvious place for us to identify, tweak, and enhance these interactions is in playtesting. As we've discussed previously in this column, development does the bulk of its work in Limited at this level, trying to ensure there are enough different thematic archetypes to draft, as well as some open-ended opportunity for being creative (e.g., [Axebane Guardian](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Axebane+Guardian) in *Return to Ravnica*, or the [Memory's Journey](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memory%27s+Journey)/[Runic Repetition](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runic+Repetition) duo in *Innistrad*).

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Memory's Journey" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Memory%27s+Journey"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Runic Repetition" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Runic+Repetition"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

### 10^2: Decks

A ***deck*** is in many ways just a way to group a bunch of interactions together. I know when I am first exploring a new set or format, I think in terms of what new decks I can build (and then, less excitedly but still somewhat hopefully, how I can update my old decks using new cards). How can we maximize fun at the deck level? Often, decks arise from the previous two layers—specific cards point toward an entire deck, or specific interactions point the way to some game breaker that a deck can be built around. Here are two of the tools we use with respect to developing decks and fun.

In most Standard formats, development tries to identify powerful uncommons and commons that can be used by newer and/or more casual players to shore up weaknesses they might have against other players at their store. Because these rarities are encountered at much higher frequency, it gives players with more limited card resources a way to keep their decks in fighting shape. Similarly, entire decks built around powerful commons and/or uncommons—a mostly red deck using [Skullcrack](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullcrack) and other powerful burn spells combined with one-drops like [Rakdos Cackler](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakdos+Cackler), for example—can be fun to build and powerful enough to compete.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Skullcrack" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Skullcrack"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Rakdos Cackler" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Rakdos+Cackler"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

We also try to put crazy powerful cards that ask you to jump through specific hoops into sets so players have a chance to explore the combo side of **Magic**. Two such cards are [Laboratory Maniac](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Laboratory+Maniac) from *Innistrad* and [Biovisionary](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Biovisionary) from *Gatecrash*. Both of these cards have the most powerful line of text we write on cards—"you win the game"—but ask you to do something pretty difficult to get there. The fun baked into these two cards comes in when you build the deck around them—what about [Chronic Flooding](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chronic+Flooding) as a way to mill out my deck quickly? Maybe [Cackling Counterpart](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cackling+Counterpart) for two [Clone](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone)s in a single card, to build up a force of [Biovisionary](https://web.archive.org/web/20130301000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Biovisionary)s?

Decks are the first major place where a player gets to take creative control of his or he experience and begins the transition from where development is in control (by choosing the words and numbers that appear on cards and determining the range of interactions among those cards) to where the player is in control (by choosing which cards to include in decks). As we continue outward in scale, development can apply less pressure toward a particular experience and relies much more heavily on partnering with players to try to create fun experiences together.

### 10^3: Tournaments

So what comes after you have a deck? The ***tournament*** is where players come together and test the ideas their decks represent. I'm speaking in a very general sense of "a structured play event at a store" when I say tournament, since we don't need to be talking cutthroat to be discussing a place you go to see how your deck performs.

[Sam has written previously](/en/articles/latestdevelopments/2013/02-15-developing-standard) in Latest Developments on an important thing development does with respect to the tournament level—working on the ebb and flow of Standard. I don't want to dwell on that aspect of developing tournaments.

On the more casual side, one simple way we've been supporting tournament fun is achievement cards. These innocuous items, around since *Scars of Mirrodin* Prereleases, help beef up Prerelease fun for folk who opt into trying to do impressive things beyond just winning matches. They may not be for everyone, but they do provide an opportunity for more exciting moments.

![](https://i.ormos.uk/2c/cc/2ccc47f932a141ab268f7d3e60a136a7440a02e25ddad1ad22c46ad8c37b533a.jpg)

This level—the store tournament—is my pick for the place we have the most opportunity for growth in terms of designing fun experiences. Such a light touch—improving the environment for newer/more casual players and finding products that can enrich players looking for a new **Magic** experience—can have such a large impact on the opportunity for fun.

### 10^4: Big Events

Of course, the discussion of creating more memorable events naturally leads into discussion of ***big events*** like the premiere of a new set (Prereleases) and even huge high-level events like the recent the [Pro Tour](https://web.archive.org/web/20130301000000/https://magic.wizards.com/en/events/coverage/martell-calls-down-reckoning-pro-tour) or the record-breaking [Grand Prix Charlotte](/en/articles/event-coverage/undated/skarrens-skarrg-rampage-in-charlotte).

Sam has once again scooped me in discussing [the players' experience with a new set using guild packs](/en/articles/latestdevelopments/2013/01-25-first-impressions). We are looking at ways to extend this successful experience, which combines choice with direction in a way that feels thematic and encapsulated, to future sets. Every new set comes with a huge extended universe of theme and story, and if we can find ways to communicate those into a fun, optional experience with memorable events, I'll consider my job well done.

![](https://i.ormos.uk/a4/a3/a4a36fc56c501faed1df55127b369db0740dee30d9c9183cd97172eca97cb37a.jpg)

On the opposite end of the casual-competitive spectrum, we have premier events and their coverage. Greg Collins—the man behind the scenes ensuring that players have access to top-notch coverage—has been working on improving it for many years, and has definitely succeeded, as evidenced in recent round-the-clock video coverage. We in R&D try to support him with small but important resources: the slides you see talking about cards, strategies, and decks at the Pro Tour. At this scale, it's difficult for us to "develop" anything directly, so instead we try to provide resources that let an exploring player enhance his or her own fun.

There are many other kinds of events that happen at this scale (conventions like PAX and the panels and parties we host at them, huge announcements and previews, etc.), and we've begun to look at all of them holistically through this lens of maximizing fun thinking about **Magic**. I'm looking forward to talking through the way we've done this with Friends... but not for another few months!

### 10^5 and Beyond—the Conversation

In a sense, we've been talking about this "birds' eye view" scale all along—this is the scale at which people share stories about **Magic** with other **Magic**-aware people. Whether it's on our forums, on [Twitter](https://twitter.com/wizards_magic) or [Facebook](https://web.archive.org/web/20130301000000/https://magic.wizards.com/en/articles/archive/magicthegatheringcom-author-archive-magicthegatheringcom-staff-2003-02-06), on the [/r/magicTCG subreddit](http://www.reddit.com/r/magicTCG/), or in myriad other social [spheres](https://plus.google.com/115867258402597168527/posts), there are many venues in which a =**Magic** fan can connect to other **Magic** fans. And it's on these venues that players will have discussions like:

*   "I can't believe how powerful CARD is in Limited!"
*   "Have you seen that combo of NEW CARD with OLD, FORGOTTEN CARD? How do you beat that?"
*   "Check out my new ARCHETYPE deck; I think the new set really makes a lot of things possible."

One of the interesting things about conversations, and the spaces in which they occur, is they are naturally immune to enforced design. People can see through engineering of a conversation and, in fact, the value of a conversation comes from its freedom and honesty. So, as developers of **Magic**, our primary responsibility with respect to the conversation is to listen and learn.

### There and Back Again

Hopefully, this exploration of the scales of **Magic** and where the fun comes from has been informative! I know thinking about things in this way has been another perspective that helps me realize how the tiny (cards) and the epic (worldwide events) connect to grow **Magic**'s fun in sometimes unexpected ways.

Until next time, enjoy all of the fun **Magic** has to offer!
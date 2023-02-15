
---
[Link to Wayback Machine](https://web.archive.org/web/20210502124054/https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-02-26)

[_metadata_:author]:- "Dave Guskin"
[_metadata_:description]:- "Hello! My Ramp;D title is now experience designer, so I thought I would spend an article on the idea of development from that perspective. What does an experience designer do, you may ask?"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "197646"
[_metadata_:path_date]:- "2013-02-26"
[_metadata_:publish_date]:- "2013-03-01"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Magical Powers of Ten"
[_metadata_:wayback_capture_timestamp]:- "2021-05-02 12:40:54"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210502124054id_/https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-02-26"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/magical-powers-ten-2013-02-26"
---


Magical Powers of Ten
=====================



 Posted in **Latest Developments**
 on March 1, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DaveGuskin.jpg)
By Dave Guskin











Hello! My Ramp;D title is now experience designer, so I thought I would spend an article on the idea of development from that perspective. What does an experience designer do, you may ask? I spend the vast bulk of my time (and some of the time of other developers, designers, editors, creative writers, artists, marketers, production specialists, sales/trade reps, and many more!) working to provide in-store experiences like:

* The *Return to Ravnica*/*Gatecrash* Prerelease Packs;
* The slightly-different-but-still-awesome *Dragon's Maze* Prerelease Packs, along with the Implicit Maze–running activity;
* Epic moments like the opening of the Helvault; and
* As-yet-unannounced "Friends"-block-related activities that will blow your proverbial socks off.
 These experiences have one very specific purpose: ***they enhance fun***. We are always looking for ways to enhance fun; the tricky bit is in using a light touch, since **Magic** itself is fun and we don't want to stray too far from its core identity as the strategy game you all know and love. Plus, enforced fun just isn't fun, you know? 

![](https://media.wizards.com/images/magic/daily/ld/ld236_havoc_festival.jpg)  
 Take a trip with me through the layers of experiencing **Magic**, and we'll see where development can enhance fun. What are the ways in which **Magic** is fun to experience? These recent designs for big events are the latest in our toolbox, but as you'll see, we try to apply fun at every scale of **Magic**! 

 (As an aside, while I do my best to replicate the feel of the old educational video "Powers of Ten" in **Magic** terms, I recommend going to view [that video in its entirety on YouTube](http://www.youtube.com/watch?v=0fKBhvDjuy0). It's a little campy, but super interesting. Especially if you love science. SCIENCE!) 

10^0: The Card
 The most basic unit we affect as developers is the ***card***, the atom of our **Magic** universe. Cards can be changed in a number of ways to make things fun. A lot of folk think of this as the primary job of development: to "garden," or carefully shape, each card in a set to provide fun play experiences and/or balanced environments. There is certainly work to be done here—if the individual cards aren't fun, the rest of the work we might build on top of the cards is probably not going to enhance anything! 

 Let's use an example card I designed—[Remember the Fallen](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remember+the+Fallen) from *New Phyrexia* (codenamed "Guts and Bolts" in design and development). What maximizes the experience of this card? Here are a few things that make this card fun to play and think about: 

* It has a straightforward pair of effects that both have sweet "what if?" scenarios associated with them.
* It lets you do both, at an appealing price (free), because it is a reward for playing into set themes.
* It has a story thread—Elspeth is lamenting the loss of *Mirrodin* to the (new) Phyrexians.
  
 Is ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) the right cost for this card? Wouldn't it be more appealing and powerful at ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) or ![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)? Maybe at some cost for "both" it would be much harder to get to work properly and thus give more of an ecstatic moment when it finally works. Through testing, we try to approach the limit of the most impactful spot for a card's mana cost. We are not trying to figure out how far something can be pushed, but rather what position the card should occupy to maximize its fun-potential for the intended target audience. Sometimes that's a tough choice about whether to draft it, sometimes it's an obvious Constructed all-star, and sometimes it's so bad that players seek it out as a way to win with a certain style (e.g., [Chimney Imp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chimney+Imp)). 

 Each card has a role—usually that it was quite literally designed to fill—and development tries to make sure it clicks into place. If you think of the purpose of a **Magic** card as its primary game function, then its secondary role in generating memories about **Magic** is like its secret purpose. The mechanics are necessary to make the game work, but their role in making stories are the true power of the cards in the **Magic** experience. 

10^1: Card Interactions
Each card can only do so much. Cards are played in the context of other cards. In these ***interactions*** among many cards, we get some additional ways to enhance fun. Think on the kinds of memorable interactions you have encountered and the fun of exploring their impact on games:

* Discovering a two-card combo;
* Executing a series of back-and-forth attacks in a draft game, culminating in a Falter effect; and
* The rock-paper-scissors game of weenie rush vs. sweeper effects vs. resilient creature in Constructed.
 These are the stories that stick with you about a particular format or game-play experience. In fact, most **Magic** players, when they discuss **Magic** excitedly with each other, are going over a play-by-play of recent games. This is the story of interaction. 

 The most obvious place for us to identify, tweak, and enhance these interactions is in playtesting. As we've discussed previously in this column, development does the bulk of its work in Limited at this level, trying to ensure there are enough different thematic archetypes to draft, as well as some open-ended opportunity for being creative (e.g., [Axebane Guardian](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Axebane+Guardian) in *Return to Ravnica*, or the [Memory's Journey](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memory%27s+Journey)/[Runic Repetition](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runic+Repetition) duo in *Innistrad*). 



|  |  |
| --- | --- |
| [card]Memory's Journey[/card] |  |

  
10^2: Decks
A ***deck*** is in many ways just a way to group a bunch of interactions together. I know when I am first exploring a new set or format, I think in terms of what new decks I can build (and then, less excitedly but still somewhat hopefully, how I can update my old decks using new cards). How can we maximize fun at the deck level? Often, decks arise from the previous two layers—specific cards point toward an entire deck, or specific interactions point the way to some game breaker that a deck can be built around. Here are two of the tools we use with respect to developing decks and fun.

 In most Standard formats, development tries to identify powerful uncommons and commons that can be used by newer and/or more casual players to shore up weaknesses they might have against other players at their store. Because these rarities are encountered at much higher frequency, it gives players with more limited card resources a way to keep their decks in fighting shape. Similarly, entire decks built around powerful commons and/or uncommons—a mostly red deck using [Skullcrack](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullcrack) and other powerful burn spells combined with one-drops like [Rakdos Cackler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakdos+Cackler), for example—can be fun to build and powerful enough to compete. 



|  |  |
| --- | --- |
|  |  |

  
 We also try to put crazy powerful cards that ask you to jump through specific hoops into sets so players have a chance to explore the combo side of **Magic**. Two such cards are [Laboratory Maniac](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Laboratory+Maniac) from *Innistrad* and [Biovisionary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Biovisionary) from *Gatecrash*. Both of these cards have the most powerful line of text we write on cards—"you win the game"—but ask you to do something pretty difficult to get there. The fun baked into these two cards comes in when you build the deck around them—what about [Chronic Flooding](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chronic+Flooding) as a way to mill out my deck quickly? Maybe [Cackling Counterpart](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cackling+Counterpart) for two [Clone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone)s in a single card, to build up a force of [Biovisionary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Biovisionary)s? 

Decks are the first major place where a player gets to take creative control of his or he experience and begins the transition from where development is in control (by choosing the words and numbers that appear on cards and determining the range of interactions among those cards) to where the player is in control (by choosing which cards to include in decks). As we continue outward in scale, development can apply less pressure toward a particular experience and relies much more heavily on partnering with players to try to create fun experiences together.

10^3: Tournaments
So what comes after you have a deck? The ***tournament*** is where players come together and test the ideas their decks represent. I'm speaking in a very general sense of "a structured play event at a store" when I say tournament, since we don't need to be talking cutthroat to be discussing a place you go to see how your deck performs.

[Sam has written previously](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/234) in Latest Developments on an important thing development does with respect to the tournament level—working on the ebb and flow of Standard. I don't want to dwell on that aspect of developing tournaments. 

 On the more casual side, one simple way we've been supporting tournament fun is achievement cards. These innocuous items, around since *Scars of Mirrodin* Prereleases, help beef up Prerelease fun for folk who opt into trying to do impressive things beyond just winning matches. They may not be for everyone, but they do provide an opportunity for more exciting moments. 

![](https://media.wizards.com/images/magic/daily/ld/ld236_achievementcards.jpg)  
 This level—the store tournament—is my pick for the place we have the most opportunity for growth in terms of designing fun experiences. Such a light touch—improving the environment for newer/more casual players and finding products that can enrich players looking for a new **Magic** experience—can have such a large impact on the opportunity for fun. 

10^4: Big Events
Of course, the discussion of creating more memorable events naturally leads into discussion of ***big events*** like the premiere of a new set (Prereleases) and even huge high-level events like the recent the [Pro Tour](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/ptgtc13/welcome) or the record-breaking [Grand Prix Charlotte](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/gpcha13/welcome).

 Sam has once again scooped me in discussing [the players' experience with a new set using guild packs](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/231). We are looking at ways to extend this successful experience, which combines choice with direction in a way that feels thematic and encapsulated, to future sets. Every new set comes with a huge extended universe of theme and story, and if we can find ways to communicate those into a fun, optional experience with memorable events, I'll consider my job well done. 

![](https://media.wizards.com/images/magic/daily/ld/ld236_plains.jpg)  
On the opposite end of the casual-competitive spectrum, we have premier events and their coverage. Greg Collins—the man behind the scenes ensuring that players have access to top-notch coverage—has been working on improving it for many years, and has definitely succeeded, as evidenced in recent round-the-clock video coverage. We in Ramp;D try to support him with small but important resources: the slides you see talking about cards, strategies, and decks at the Pro Tour. At this scale, it's difficult for us to "develop" anything directly, so instead we try to provide resources that let an exploring player enhance his or her own fun.

 There are many other kinds of events that happen at this scale (conventions like PAX and the panels and parties we host at them, huge announcements and previews, etc.), and we've begun to look at all of them holistically through this lens of maximizing fun thinking about **Magic**. I'm looking forward to talking through the way we've done this with Friends... but not for another few months! 

10^5 and Beyond—the Conversation
 In a sense, we've been talking about this "birds' eye view" scale all along—this is the scale at which people share stories about **Magic** with other **Magic**-aware people. Whether it's on our forums, on [Twitter](https://twitter.com/wizards_magic) or [Facebook](https://www.facebook.com/MagicTheGathering), on the [/r/magicTCG subreddit](http://www.reddit.com/r/magicTCG/), or in myriad other social [spheres](https://plus.google.com/115867258402597168527/posts), there are many venues in which a =**Magic** fan can connect to other **Magic** fans. And it's on these venues that players will have discussions like: 

* "I can't believe how powerful CARD is in Limited!"
* "Have you seen that combo of NEW CARD with OLD, FORGOTTEN CARD? How do you beat that?"
* "Check out my new ARCHETYPE deck; I think the new set really makes a lot of things possible."
 One of the interesting things about conversations, and the spaces in which they occur, is they are naturally immune to enforced design. People can see through engineering of a conversation and, in fact, the value of a conversation comes from its freedom and honesty. So, as developers of **Magic**, our primary responsibility with respect to the conversation is to listen and learn. 

There and Back Again
 Hopefully, this exploration of the scales of **Magic** and where the fun comes from has been informative! I know thinking about things in this way has been another perspective that helps me realize how the tiny (cards) and the epic (worldwide events) connect to grow **Magic**'s fun in sometimes unexpected ways. 

 Until next time, enjoy all of the fun **Magic** has to offer! 

![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_Top.jpg)![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_leftOfButton.jpg)[![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_Button_Static.jpg)](http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/league-facts)![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_RightOfButton.jpg)[![](https://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_LeagueNow_Bottom_Static.jpg)](http://archive.wizards.com/magic/tcg/products.aspx?x=mtg/tcg/products/gatecrash)  








---
[Link to Wayback Machine](https://web.archive.org/web/20160926054431/http://magic.wizards.com/en/articles/archive/latest-developments/developing-fabricate-2016-09-23)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "Sam talks about what it took to make the fabricate mechanic work into Kaladesh."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1080176"
[_metadata_:publish_date]:- "2016-09-23"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Fabricate"
[_metadata_:wayback_capture_timestamp]:- "2016-09-26 05:44:31"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160926054431id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-fabricate-2016-09-23"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/developing-fabricate-2016-09-23"
---


Developing Fabricate
====================



 Posted in **Latest Developments**
 on September 23, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 






Fabricate's earliest roots actually start in *Magic* *Origins*. While we were looking for a way to incorporate artifacts into the set, we tried out some blank artifact tokens called Gizmos that different cards used in different ways. It was an interesting idea, but ultimately it made the cards too siloed in a set that really wasn't about artifacts. The Thopter angle was an interesting one, where we could add in those same Kaladesh-pointing cards that used artifacts in different ways (see [Ghirapur Æther Grid](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghirapur+%C3%86ther+Grid) and [Reclusive Artificer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reclusive+Artificer)), while still having the cards that would function in non-artifact based decks. It was a good way to get a feel of Kaladesh we were happy to showcase before we really knew what the set was about.


As Kaladesh went through exploratory design, it became more and more clear that the energy mechanic that Maro had wanted to use for quite a while was going to work in the set. At the same time, we had a version of Vehicles that design was relatively happy with. It was around that time, as *Battle for Zendikar* was finishing up its development, we knew we had drifted a bit too far in complexity of our *Magic* sets. *Battle for Zendikar*, along with *Oath of the Gatewatch*, had a real inflation of keywords that was unsustainable. We had a few less in *Shadows* block, but we were still above where we wanted to be. The move to two blocks per year also put pressure on us to have each of our sets to be a little less complicated. Considering *Kaladesh* already had one very complicated mechanic in energy (that offered a lot of hard choices), and Vehicles (that did something new and a bit difficult), we knew that the other mechanic in the block needed to be more workhorse and simple. This led to the creation of fabricate—a mechanic that would give players the ability to feel like an inventor by customizing their cards to come with either tokens, or higher power and toughness.


Making Fabricate Work
=====================


Because of how complex both energy and Vehicles were for the risk of on-boardyness, we really wanted fabricate to offer a different kind of choice—one that you could make once and forget it. We enjoyed the kinds of mental space that energy was playing in, but when you have a mechanic as wide open as that in a block, it's very hard to have a ton else competing for the mind space of players. Whatever other mechanic the set actually launched with would need to be pretty simple.


The initial version of fabricate that design created made the same 1/1 flying Thopters of *Magic* *Origins*. It was a good callback, and we had done a lot in worldbuilding to make sure that Thopters were still a part of this world. The problem was that, much like what happened with energy, the way that developers and designers played fabricate was quite different. Designers enjoyed the decisions the cards gave them, and being able to have their games play out very different when they cast the card. The developers just chose the 1/1 flying tokens every time. I don't point this out to say anything bad about the design process—the developers are just much more likely to not care about whether or not a given player will make different decisions, they are more interested in what the right decision is. The problem with the mechanic was that it wasn't really leading to the kind of interesting decisions in competitive game play that the designers were having in their games. A big part of what separates the design and development process, in my mind, is that design often creates a set that plays the way they want it to play in a vacuum, and development tries to actually ensure that the set does play that way when given to a wider audience of *Magic* players.



![Ambitious Aetherborn](https://media.wizards.com/2016/images/daily/cardart_KLD_Ambitious-Aetherborn.jpg)[Ambitious Aetherborn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ambitious+Aetherborn) | Art by [Josu Hernaiz](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Josu+Hernaiz%22%5d)
The challenge for us was to make it so that people who were trying to get the maximum power out of the cards each time were having these kinds of interesting decisions, and not just the players who were content to play them, make an arbitrary choice, and see what happens. This was difficult, because the set at that point rewarded artifact tokens even more than it does now. At the time: Vehicles required the tapping of multiple creatures (making 1/1s even stronger), there were more pure 'artifact matters' cards, and on top of that the tokens had flying. While we certainly could create a few cards where the decisions were interesting, the power level of 1/1 flyers was just so much higher than a +1/+1 counter on a regular card. At the same time, if we went with a single 1/1 flyer or two +1/+1 counters, then it would have been very tilted toward the counters. We were just not in a spot where there was an obvious pivot point for many cards. If you were to take a vanilla creature, then add two or more keywords, you can get into versions where the choice is interesting but few. Probably not enough to actually make it into a set.


The decision was made to move from flyers to ground creatures during design, to make the power level difference between a +1/+1 counter and a 1/1 much closer. Deciding whether to make a 3/3 ground creature for 2W vs. a 2/2 and a 1/1 ground creature looked more interesting on paper. And once we actually played games, we found that it also played much more interestingly. Suddenly, we had the ability to make a lot of different creatures where you had interesting decisions to make, and they would play differently in different games. That variability and modular feel of game play was something the design team was working very hard to incorporate into *Kaladesh*, and we could now make pretty simple cards with fabricate that got that feeling across.


Creating Interesting Decisions
==============================


Once the set was in development, we were in a better spot, but there was still work to find the right versions of fabricate cards to ensure interesting decisions. That meant finding spots on the curve where we could make interesting decisions. A 1W 1/1 with Fabricate 1, for example, is strong, but it is very rare you would ever choose a vanilla 2/2 over two 1/1s. About the only time that would be really useful is if your opponent has multiple 1/1s or 1/2s. [Peema Outrider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Peema+Outrider), on the other hand, takes the tools at our disposal (like adding a keyword) to find a spot where both options make a lot of sense. If you are doing "artifact things" or pumping your team, the 3/3 and 1/1 make more sense, but if you are trying to get over a 3/3 or block it, then the 4/4 version of [Peema Outrider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Peema+Outrider) makes more sense. Being able to make a wide array of cards with interesting decisions is really important to us when making a mechanic. Often, we find the ability to make three or four that work, but not the rest. Which means that we don't have enough cards to satisfyingly call it a mechanic, and those cards will be almost impossible to change for balance tweaks. That's not great. With fabricate, we made a lot of cards in *Kaladesh*, and I feel like there were enough different sizes and combinations left that we had the breathing room to change them if we'd needed to.


The mechanic appears in three colors (white, black, and green), but we wanted the mechanic to have a different feel in each of those colors. Not exactly how those cards are constructed, but more how those colors use +1/+1 counters and the creature tokens differently. White, for example, may want a 3/2 flyer for four, or it may want the token because it has team pump effects, or because it plans on somehow blinking the creature and getting extra tokens out of it. Black may want the extra power on its menace creature, or it may want multiple different tokens so it can sacrifice them. Green gets some +1/+1 counter synergy cards like [Fairgrounds Trumpeter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fairgrounds+Trumpeter), which may make you want to use the counters, but it also could combine with the other two colors to create different play patterns.


Fabricate may not be nearly as pervasive or flashy as energy in *Kaladesh* Limited, but it does a great job as a workhorse mechanic that really pulls some of the very different ideas of the set together. I consistently found it to be a very fun mechanic in playtesting, and I think it's one you will enjoy during your Prerelease.


That's it for this week.


Join me next week on Latest Developments, when I talk about how having an artifact-matters set impacted how we develop Limited.


Until next time,


Sam ([@samstod](https://twitter.com/@samstod))








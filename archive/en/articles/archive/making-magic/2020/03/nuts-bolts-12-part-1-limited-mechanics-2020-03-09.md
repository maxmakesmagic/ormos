
---
[Link to Wayback Machine](https://web.archive.org/web/20200323180048/https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-12-part-1-limited-mechanics-2020-03-09)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark discusses the importance of Limited and how it affects the design of mechanics in a return to his series on designing your own sets."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1496592"
[_metadata_:publish_date]:- "2020-03-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Nuts & Bolts #12, Part 1: Limited (Mechanics)"
[_metadata_:wayback_capture_timestamp]:- "2020-03-23 18:00:48"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200323180048id_/https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-12-part-1-limited-mechanics-2020-03-09"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-12-part-1-limited-mechanics-2020-03-09"
---


Nuts & Bolts #12, Part 1: Limited (Mechanics)
=============================================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on March 9, 2020 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






It's a few months into a new year, which means it's time for another installment of "Nuts & Bolts," my annual series dedicated to helping players design their own *Magic* cards and/or sets. This series is intended to provide hands-on technical advice for amateur *Magic* designers but also gives the rest of you a peek behind the curtain to see how we design sets.


Here's a recap of what I've written so far.


[**Nuts & Bolts #1: Card Codes**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-card-codes-2009-01-12)


The first column is the most technical, explaining how we use a system to make sure everyone is always talking about the same card.


[**Nuts & Bolts #2: Design Skeleton**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-design-skeleton-2010-02-15)


The second column introduces the most important tool in designing a set, something called a design skeleton. (It makes use of card codes, which is why that article came first.)


[**Nuts & Bolts #3: Filling in the Design Skeleton**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-filling-design-skeleton-2011-02-28)


The third column talks about how you begin filling in your design skeleton, starting with the common cards.


[**Nuts & Bolts #4: Higher Rarities**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-higher-rarities-2012-02-27)


The fourth column talks about filling in all the other rarities.


[**Nuts & Bolts #5: Initial Playtesting**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-initial-playtesting-2013-02-11)


The fifth column discusses how best to use playtesting to gather feedback and make improvements on your set.


[**Nuts & Bolts #6: Iteration**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-iteration-2014-03-03)


The sixth column talks about the concept of iteration and how you can incrementally improve your set.


[**Nuts & Bolts #7: Three Stages of Design**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-three-stages-design-2015-03-30)


The seventh column explains the three different stages of design, walking you through how your priorities shift as the set evolves.


[**Nuts & Bolts #8: Troubleshooting**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-troubleshooting-2016-02-15)


The eighth column answers a number of questions about common problems that can happen in the early-to-mid design stages.


[**Nuts & Bolts #9: Evaluation**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-evaluation-2017-02-20)


The ninth column talks about how you can look at your set as a whole and figure out what fine-tuning it still needs.


[**Nuts & Bolts #10: Creative Elements**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-10-creative-elements-2018-03-26)


The tenth column discusses how you interweave your mechanical and creative elements into a cohesive set. It discusses both top-down (starting with the flavor) and bottom-up (starting with the mechanics) design. I then go into detail about how to handle names, creature types, and flavor text.


[**Nuts & Bolts #11: Art**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-art-2019-02-11)


The eleventh column talks about the importance of using art in later playtests and how to incorporate it into your set.


Which all brings us to the twelfth column in the series. Today and next week (yes, my first two-part "Nuts & Bolts"), I'm going to talk about the importance of Limited and how it affects your design.


Playing with What Was Dealt to You
==================================


One of the challenges in writing this series is that there are a lot of different things you have to worry about as you design a set. I have to write about it in some order, but it can't be reflexive of the order in which you need to care about it as you have to care about many different things concurrently along the way. Case in point, today I'm going to talk about the impact of Limited (Sealed Deck and Booster Draft, mostly) on your design. These concerns should be thought about earlier in the process even though I'm just getting to it now.


Another caveat—we design every booster product so that it can be played in Limited, as Limited is a big part of the *Magic* experience for a lot of players. All that said, if you're designing a *Magic* set that you never plan to play with in Sealed or Booster Draft, you can ignore a lot of what I'll be talking about today (although, even then, there might be a few lessons you can still apply). Note that if you do ignore Limited, you're going to want to use preconstructed decks to do your playtesting.


Let's begin with examining why Limited is important to a set design:


**1. It allows more of the set to be relevant.**


Even if you're consciously designing for as many Constructed formats as you can, there's a limit to how many cards you can make that will actually see play (assuming you're not doing things like power creeping—aka making the set more powerful than all the sets before it). Limited formats allow you to take giant swaths of cards, often very fun and interesting designs, and ensure that people actually play them. The vast majority of your commons and uncommons will fall into this group.


**2. It gives players a way to experience the set as a whole.**


One of the fun things about making a set is building a new environment. Limited is the means by which you get to show off that environment in the strongest terms. A big part of this is that you get to control what is and isn't in the environment, something that gets much harder to do when existing sets are already playable in a format.


**3. It serves as a good sampler of the set.**


Limited play serves as a great opportunity for players to try out the new set and experience the new mechanics and themes. Often, it's after playing in Limited that players get inspired to try out mechanics and themes in their favorite Constructed formats. Also, Limited play is a great way for players to decide if they like your set and whether they want to purchase more of it.


**4. It helps give your set definition.**


One of the biggest challenges of making an expansion of a 27-year-old game is that it's easy for all the sets to blur together. We avoid this by giving each set a strong mechanical (and creative) identity. The needs of Limited force you to be extra vigilant about this and push you to pay more attention to the finer details of your synergies.


**5. It aids in playtesting.**


A set having the ability to be played in Limited is a giant advantage for playtesting. It means you can play with nothing but the cards of the set, which can help you focus better on what is and isn't working.


So, what do you need to do to make a set play well in Limited? There are two major things to look at—your mechanics and your themes. Today, I'll be looking at how mechanics shape Limited and thus how you structure your set. Next week, I'll be looking at themes.



![](https://media.wizards.com/2020/images/daily/6isMYUeXPI.jpg)[Thassa, Deep-Dwelling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thassa%2C+Deep-Dwelling) | Art by: [Jason A. Engle](https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&artist=+%5B%22Jason%20A.%20Engle%22%5D)
Your Mechanics
--------------


One of the first things you need to examine is how well your mechanics play in Limited. To do this, we have to look at several aspects of each mechanic (for each of these, I'm going to use the three named mechanics from *Theros Beyond Death*—constellation, devotion, and escape—as an example):


**Is it modular or linear?** (For more on these terms, read [this article](https://magic.wizards.com/en/articles/archive/making-magic/come-together-2003-10-06-0).)


Does a card with the mechanic play well by itself or does it require having other specific types of cards to play with it? For example, flashback is very modular. You can put just one flashback card in your deck and play it. It doesn't require you having other flashback cards. Other than requiring mana, a pretty basic requirement, it doesn't ask anything else specifically be in your deck. Slivers, in contrast, are very linear. Odds are you're not just playing one Sliver in your deck as the power of Slivers comes from their interaction with one another. The more modular your mechanic is, the better it will play in Limited without adjustment on your part. Linear mechanics can work in Limited, but they require more support from the design.


**Constellation** – This is a linear mechanic in that it requires you play with enchantments. Note, though, that none of the cards with constellation in *Theros Beyond Death* are enchantments. (The opposite was true when the mechanic first appeared in *Journey into Nyx* but got changed this time due to play design concerns.) This means it's an A/B mechanic in that it requires you to have cards of group A (constellation cards) and cards of group B (enchantments). This is the biggest ask of a mechanic for the purposes of Limited. It means that you have to make sure your [as-fan](http://magic.wizards.com/en/articles/archive/making-magic/state-design-2017-2017-08-28#as-fan) of cards from group A and cards from group B is high enough. ("As-fan" is short for "as-fanned" and talks about what percentage of your theme or mechanic shows up in any random booster. An as-fan of 2, for example, means there will be an average of two cards in every booster with that theme or mechanic.) Usually that's going to mean a significant appearance at common for both groups.


**Devotion** – This is also a linear mechanic, but a little less severe in its requirements than constellation as the thing it cares about, having colored mana symbols, is something almost all nonland cards are going to have. However, this doesn't mean that it's not asking something of your design. First, it strongly encourages you to play all or heavily in one color, which dictates something about the kind of environment it works in. Second, it wants more cards with multiple colored mana in their mana costs, something we don't normally do at common. Unlike constellation, devotion can be more easily splashed, although best in a deck heavy in one color.


**Escape** – This is a modular mechanic in that you can easily just play a single card with it. Interestingly, this mechanic is anti-linear in that all the cards with it require the same resource, cards in your graveyard, making it difficult to play too many of them in the same deck without some support. (I'll get to this next.)


**What kind of enablers does it want?**


If this mechanic is in your set, what else will you have to add or subtract in your set? Are you going to want more of a thing you normally have, less or none of a thing you normally have, or are you going to need something that doesn't show up in an average set at all? Understanding what impact your mechanic is going to have on the other cards in your set is key.


**Constellation** – This mechanic's needs are pretty straightforward. You're going to need more enchantments in your set, a lot more. The challenge is going to be how to do that? A normal set has nowhere near a high enough as-fan of enchantments to be something you can mechanically care about. The only way to get enough space is to encroach on the creatures. This is why, for example, Theros sets have enchantment creatures. The "enchantments matter" theme can't work without them.


**Devotion** – This mechanic wants two things. First, it wants more permanents with multiple colored mana in their mana costs. As I said above, this isn't something we normally do a lot of at common. Second, it wants cards that encourage and reward monocolor play. That's a larger ask of the set in that it's dictating a theme. (More on themes next week.)


**Escape** – The anti-linear quality of this mechanic is going to encourage you to have support cards that let you play more escape cards in your deck. Good examples would be cards that allow you to mill yourself to get more cards into your graveyard, permanents that can sacrifice themselves or other items for an effect, and cheap instants and sorceries. It's important not just to think about what your mechanic might require to work but also what enables you to play more of it.


**How much space does it require and how much space can it fill?**


This is asking about the size of your mechanic. How many cards is it going to require? How much of an as-fan will it need? How much design space does it have? Part of scoping out your mechanic for Limited is understanding what it requires and what it's capable of? This is important to comprehend as you're mapping out what it needs to do to work properly. I should note that Sealed and Draft have different requirements. Usually a mechanic or theme has to exist in a larger number to work in Sealed. We tend to shoot for numbers that function in Sealed but play best in Booster Draft.


**Constellation** – There are thirteen cards with this mechanic in *Theros Beyond Death*, all on creatures, in three colors (white, blue, and green) and three rarities (five commons, five uncommons, and three rares). The mechanic needs output effects, so it's limited by how many different effects you can generate. As enchantments are mostly played during your main phase, it limits the effects to things that are proactive and generally useful, meaning you're happy to get the effect whenever you get it. Because it's so linear, it requires a significant as-fan to make sure you can get enough cards to build a Limited deck out of it.


**Devotion** – There are 22 cards with this mechanic in *Theros Beyond Death* (plus one Buy-a-Box card and one Planeswalker Deck card) mostly on creatures but showing up in other card types, focused in three colors (blue, black, and green) but appearing in all five colors and four rarities (three commons, eleven uncommons, two rares, and six mythic rares—all Gods). Devotion requires effects that can scale, which greatly cuts into its design space. This is the reason, for instance, why it has so few commons and so many uncommons—scaling effects tend to skew to higher rarities. This is why there are so many uncommons, to help get the as-fan up because the mechanic is hard to do at common. Like constellation, the linear nature of the mechanic makes you want to generate enough cards that players can build decks around the mechanic in Limited.


**Escape** – There are 23 cards with this mechanic in *Theros Beyond Death*, in all five colors, on all different card types, in all four rarities (nine commons, six uncommons, three rares, and five mythic rares). The mechanic is pretty open-ended as it works on any card type and most effects. Its size was more dictated by what the set needed of it than what it needed of the set.



![](https://media.wizards.com/2020/images/daily/e5LmG8FvWm.jpg)[Mire's Grasp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mire%27s+Grasp) | Art by: [Chris Rallis](https://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5b%22Chris+Rallis%22%5d)
Reworking the Skeleton
----------------------


Once you've figured out the needs and restrictions of your mechanics, you can start mapping the structure of your set around them. This entails figuring out actual numbers which you will then apply directly to your design skeleton. I'm going to use the three *Theros Beyond Death* mechanics to give you an example of how you would do this.


Let's start with constellation. In order to make it work, you're going to need a significant as-fan of constellation cards and enchantments at common and uncommon. Getting to the right spot is not just a matter of math (while having a working understanding of how different as-fans feel helps, each mechanic is different), but of trial and error. You can make an educated guess or use a preexisting set with a similar mechanic as a guide to start. Then playtest to get a sense of whether you have enough of it to work. Each time you try a new set of numbers, apply it to your design skeleton. The key is understanding what variables you need to fiddle with to make the mechanic happen consistently in Limited. In R&D, we tend to start with Sealed and then shift to Booster Draft once we feel we have the larger environmental concerns understood.


Often what will happen and why using your design skeleton is so important is you will start to see where stresses begin to form in your design. For instance, it was doing the set math that made it clear we needed enchantment creatures to make an "enchantments matter" theme work. Also, putting the numbers into the design skeleton forces you to think about where you can fit in the things you need. For example, upping the number of enchantments might have you look at spell effects and ask, could we shift this into an aura? In *Theros Beyond Death*, [Mire's Grasp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mire%27s+Grasp) is an aura that grants -3/-3. There's a good chance that early in design it was a sorcery that granted -3/-3 and it was shifted to an aura to up enchantment numbers. Doing the numbers will also force you to think about things like how many colors you want to be in. A good trick to help your as-fan is to concentrate your mechanic into less colors. This, as an example, is why constellation is only in three colors.


Devotion is going to ask you to raise the as-fan of cards with multiple colored mana in their mana costs. This is also something you want to add into your design skeleton. The pressure with this ask is going to make you want to use it on midsize to large spells as they can more easily absorb the extra colored mana. Note that different parts of your set are going to ask for different things and those things can overlap. The cycle of common vanilla creatures in *Theros Beyond Death* were used to up both the number of enchantments and the number of cards with multiple colored mana costs. Devotion is also going to encourage you to have more cards that play into a monocolored theme. Don't be afraid to add new elements like this to your design skeleton. Often, part of designing a set is figuring out that you care about things you initially didn't know you would care about. The design skeleton is a living document and should be constantly changing to represent what the design needs in the present.


Escape will pressure you to add more effects to the set that play nicely with a "graveyard as resource" theme. First, look at your existing set to see what already exists and then brainstorm what kinds of effects could be added to up the number. It's fine to set as-fan for things like enablers. Then, add it to your design skeleton. Note that it's okay to have something like "graveyard enabler" listed on a card even if you're not sure yet what it's going to be. Its existence helps you contextualize it as something that needs adding.


I should note that all this comes a bit later in the process as you have to figure out your mechanics first. This means you will have built an initial design skeleton that will need to change as you adapt your set to your mechanics. A big part of the iterative process is understanding what needs the existing parts of your set has and then shifting the rest of your cards to accommodate. The design skeleton is a great place to mark this down so that you can see what you have to change. Your Constructed cards will also dictate things, but more often on a card-by-card basis than on a set basis (and also later in the process), which is why Limited tends to be better at determining the structure of your set.


Finally, I can't stress enough that playtesting is ultimately the best tool to finalize as-fan numbers. No matter how much you theorize something, nothing is going to beat actually playing with the set to see what is working and not working. Remember that you have to mimic actual boosters (ten commons, three uncommons, rare seven-eighths of the time, mythic rare one-eighth of the time) once you get to the point where you're trying to figure out as-fan. Also, you need to playtest a number of times to get a true sense of as-fan balance. Individual variance can give you odd readings in small doses.


I like to say that *Magic* design is part art, part science. The part I'm talking about today leans toward the science side where you have to actually do the math to make sure that what you want to happen is happening in the right volume. The key is to use your design skeleton and constantly update it as you learn new things. One of the things that will happen is that you will start to get squeezed for space. This will mean one of two things. Either you have to find ways to combine multiple needs on one card (as with the vanilla cycle I talked about above) or you have too much stuff and something needs to go. Never be afraid to pull something if its absence makes the rest of the set play better.


Zen and the Art of Set Maintenance
==================================


The stuff I'm talking about today is a lot of work, but it's what makes a design truly shine. I hope you've enjoyed hearing about the nuts and bolts of set design. That's all the time I have for today, but I'll be back next week with the other half of the puzzle—themes. As always, I'm eager to hear what you have to say on today's article. You can [email me](mailto:making.magic@hotmail.com) or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumble](http://markrosewater.tumblr.com/), and [Instagram](http://instagram.com/mtgmaro)).


Join me next week for Part 2.


Until then, may all the work make your sets sing.




 

##### 
 #719: Broadwaycon 2020






##### 
 #719: Broadwaycon 2020


41:00



My eldest daughter and I traveled to New York City to attend Broadwaycon. This podcast talks all about it and how it made me rethink how I do *Magic* design.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork719_broadwaycon_Ikm2D6pD.mp3)



  


 

##### 
 #720: What Was in Alpha






##### 
 #720: What Was in Alpha


34:43



This is another trivia podcast. I ask about elements of *Magic* and see if you can identify whether it was part of *Magic* at the start of the game back in *Alpha*.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork720_whatwasinalpha_D2maSidj.mp3)




* [**Episode 718**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork718_greenwhite_ksUd39Ud.mp3) Green-White
* [**Episode 717**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork717_makinguncards_Hu39sDoA.mp3) Making *Un-* Cards
* [**Episode 716**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork716_undp2_Md92HDus.mp3) *Unsanctioned*, Part 2







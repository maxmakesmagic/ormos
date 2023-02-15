
---
[Link to Wayback Machine](https://web.archive.org/web/20200921094010/https://magic.wizards.com/en/articles/archive/making-magic/zendikar-rising-stars-2020-09-14)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark talks about aspects of Zendikar Rising's design through his card-by-card design stories from the set."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1509110"
[_metadata_:publish_date]:- "2020-09-14"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Zendikar Rising Stars"
[_metadata_:wayback_capture_timestamp]:- "2020-09-21 09:40:10"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200921094010id_/https://magic.wizards.com/en/articles/archive/making-magic/zendikar-rising-stars-2020-09-14"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/zendikar-rising-stars-2020-09-14"
---


Zendikar Rising Stars
=====================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on September 14, 2020 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






The last two weeks, I walked you through the design of *Zendikar Rising* ([Part 1](https://magic.wizards.com/en/articles/archive/making-magic/zendikar-rising-challenge-2020-09-01) and [Part 2](https://magic.wizards.com/en/articles/archive/making-magic/zendikar-rising-challenge-part-2-2020-09-07)). This week, I'm going to start talking about aspects of the set's design through the lens of the design of different cards from the set. Yes, it's time for some *Zendikar Rising* card-by-card design stories.


**Acquisitions Expert**


![Acquisitions Expert](https://media.wizards.com/2020/znr/en_GucK6u0sW4.png)


The party mechanic is what's known as a scaling mechanic. A scaling mechanic is any mechanic that can exist at different levels and thus must be designed to have its effects work at a variety of scale. Here are the issues you need to address when designing a scaling card. I'll be using Acquisitions Expert as my example.


**Question #1: Does this effect scale by number or by volume?** 


An effect that scales by number is something where the effect involves a number and some element can change what that number is. Examples of scaling by number are domain or an X spell. An effect that scales by volume is one where a basic effect can be copied numerous times. Examples of scaling by volume are replicate or multikicker. Mechanics that scale by number have less design space as the effect has to involve a number. Mechanics that scale by volume can do most effects because the number you care about is how many times you're generating the effect. (I should note that some effects are synergistic with themselves and some are anti-synergistic.) Usually, an entire mechanic either scales by number or by volume. Party obviously scales by number. Each effect has to work at 1, 2, 3, or 4. When scaling by a number effect, you're limited to effects that have a number in them. That means you have to have some game element that you're counting. With Acquisition Expert, that number would be cards in the opponent's hand.


**Question #2: Is this effect endless or capped?** 


An endless scaling effect usually cares about some variable that has no set restriction. For instance, tribal effects often count how many of a particular creature type you have on the battlefield. That number can get quite large. Note that endless means that there isn't a restriction built into the mechanic, not that there aren't some functional constraints, such as the number of creatures in your deck. A capped effect only scales up to a point. For example, domain counts the number of basic land types you have on the battlefield. That value is capped at 5—*Magic* only has five basic land types. This is another category that tends to be true of the entire mechanic. Party, obviously, is capped, there are only four class creature types you can count. Capped effects allow you a little more freedom as you know the top end of what's possible. That tends to open up a little more space from a balance perspective. Party's top end being four was useful in that we'd done the domain mechanic which stops at five, allowing us the ability to look at those cards as a jumping-off point.


**Question #3: Is the effect linear or non-linear?** 


A linear scaling effect is one where each increment has full value. For example, "draw a card for each creature you control"—each card drawn is a full extra card. The differential is the same between each number. Each extra 1 draws you a whole extra card. A non-linear scaling effect is one where each increment does not have full value to each one that came before it. For example, "look at the top X cards of your library where X is the number of creatures you control, put one in your hand and the rest on the bottom of your library in a random order"—each extra 1 lets you look at an additional card, thus improving the quality of your draw, but it doesn't net you a whole extra card. The value of the differential between 0 and 1 (going up a card) is much higher than the differential between any of the rest of the numbers. This is the first category that can change between cards with the same mechanic. Acquisition Expert is non-linear. 1 makes the opponent discard a card. 2, 3, and 4 only increase your ability to affect what card gets discarded. Other party effects, such as Coveted Prize, are linear (each extra creature makes the spell cost one less mana).


**Question #4: Is the effect contained or uncontained?** 


A contained scaling effect is one where there's a limit to how much the effect can do. An example would be "target creature gets -1/-1 until end of turn for each card in your hand." No matter how many cards I have in my hand, the effect is contained to killing a single creature. An uncontained effect does not limit the effect. An example would be "destroy X creatures where X is the number of cards in your hand." Isn't this the same thing as being linear or non-linear? No—my example for a contained effect is linear because each added 1 gets you another -1/-1, but it limits how much the overall effect can do by containing its potential. Usually, for Limited power-level reasons, we try to keep lower-rarity scaling cards contained. Acquisition Expert is contained. The most you can ever do is make the opponent discard one card.


When designing a scaling effect card, you want to know what parameters you're working with. Acquisition Expert was designed during vision design as a common card. That meant we wanted a contained card, probably one that was also non-linear (although, as with Coveted Prize, linear cards can work at lower rarities). We'd already done a -1/-1 card and a "drain an opponent" card, so we were interested in something that was playing in a different space. That got us to consider a discard effect. But how do we do a discard effect that scales? Discard X cards are non-contained and too high variance for Limited (and thus common). How else could we use a number and tie it to discard? The key is looking at discard effects we've done and finding a place where there's a number built in. The answer is the coercion effect (named after the *Mirage* card [Coercion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coercion)) where you have some ability to choose what the opponent discards. This allows us to add a number—cards in the opponent's hand—and thus make the effect scale. The card would later get moved up to uncommon for Limited concerns.


And that, in so many words, is how you design a scaling effect.


**Branchloft Pathway, Brightclimb Pathway, Clearwater Pathway, Cragrown Pathway, Needleverge Pathway, and Riverglide Pathway** 





![Branchloft Pathway](https://media.wizards.com/2020/znr/en_hJ9A9jefon.png "Branchloft Pathway")
![Boulderloft Pathway](https://media.wizards.com/2020/znr/en_CRbN12OiLF.png "Boulderloft Pathway")

Turn Over



![Brightclimb Pathway](https://media.wizards.com/2020/znr/en_KUqTQ5MqhG.png "Brightclimb Pathway")
![Grimclimb Pathway](https://media.wizards.com/2020/znr/en_4CawLfHUZe.png "Grimclimb Pathway")

Turn Over



![Clearwater Pathway](https://media.wizards.com/2020/znr/en_5HYGFHM0Kg.png "Clearwater Pathway")
![Murkwater Pathway](https://media.wizards.com/2020/znr/en_k88z4OsOjj.png "Murkwater Pathway")

Turn Over





![Cragcrown Pathway](https://media.wizards.com/2020/znr/en_26pLsDL96C.png "Cragcrown Pathway")
![Timbercrown Pathway](https://media.wizards.com/2020/znr/en_XFCBs5p1d5.png "Timbercrown Pathway")

Turn Over



![Needleverge Pathway](https://media.wizards.com/2020/znr/en_bEX3pwCEOA.png "Needleverge Pathway")
![Pillarverge Pathway](https://media.wizards.com/2020/znr/en_5i0bnLGiOo.png "Pillarverge Pathway")

Turn Over



![Riverglide Pathway](https://media.wizards.com/2020/znr/en_piHdkf3FZP.png "Riverglide Pathway")
![Lavaglide Pathway](https://media.wizards.com/2020/znr/en_j0asbS9IPk.png "Lavaglide Pathway")

Turn Over


As I explained [last week](https://magic.wizards.com/en/articles/archive/making-magic/zendikar-rising-challenge-part-2-2020-09-07), the Pathways came about as I was exploring ways to take advantage of the design space modular double-faced cards (MDFCs) gave us. Fundamentally, they're a combination of split cards and double-faced cards. The big question—what did that allow us to do that neither split cards nor transforming double-faced cards let us do? The big limitation to split cards is that they can only be instants or sorceries. You can mimic creatures by making creature tokens, but there are limitations to how complex we let creature tokens be. That meant that at least one side of each MDFC had to be a permanent. (Technically, there is space for a MDFC where both sides are an instant or sorcery, but something with enough rules text that it couldn't fit on a split card—that isn't where I wanted to start.)


I started by making a list of every possible combination available with that constraint:


Artifact/artifact  

Artifact/creature  

Artifact/enchantment  

Artifact/instant  

Artifact/land  

Artifact/planeswalker  

Artifact/sorcery  

Creature/artifact  

Creature/creature  

Creature/enchantment  

Creature/instant  

Creature/land  

Creature/planeswalker  

Creature/sorcery  

Enchantment/artifact  

Enchantment/creature  

Enchantment/enchantment  

Enchantment/instant  

Enchantment/land  

Enchantment/planeswalker  

Enchantment/sorcery  

Land/artifact  

Land/creature  

Land/enchantment  

Land/instant  

Land/land  

Land/planeswalker  

Land/sorcery  

Planeswalker/artifact  

Planeswalker/creature  

Planeswalker/enchantment  

Planeswalker/instant  

Planeswalker/land  

Planeswalker/planeswalker  

Planeswalker/sorcery


It was clear that some of these constraints had a lot more design space than others. One of the ones that drew my eye was land/land. When tackling a design vein, I always like to start with the most basic design. What if it was a different basic land on each side? In many ways, this harkened back to "fetch lands."


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=3570)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=3570) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=39504)](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=39504)
The *Mirage* design team had an idea for a dual land where you got to pick one of two colors and then the land from then on would tap for that color. Having to remember which color you'd chosen for each individual land ended up being too much of a memory issue, so the *Mirage* design team came up with a clever solution. You would sacrifice the land and then search your library for one of two basic land types, which you would then put onto the battlefield. This captured that basic functionality.


One of the issues that came up, though, was if the land could do this the turn it entered the battlefield, the lands would be (almost) "strictly better" than basic lands. (*Alpha* had this problem with the original dual lands.) Why play an island when I could have a land that's an island or a swamp? The *Mirage* design team solved this by having the land enter the battlefield tapped. This ended up being a bit on the weak side (a few years later in *Invasion*, we'd print dual lands that came into play tapped and could always tap for either color), so in *Onslaught*, we made an improved version where instead of entering the battlefield tapped, it forced you to pay 1 life.


The reason I bring all this up—I basically had to solve the same problem. I had a land where you could choose for it to be an island or a swamp. I couldn't use "enters the battlefield tapped" as the drawback as that would be *just* worse than a tap land, which we print all the time (and even have room to put something extra on like scry or being a gate). My first attempt was to treat it like an *Onslaught* fetch land.


**Dirty Island 1.0**   

Land - Island  

When CARDNAME enters the battlefield, lose 1 life.  

///  
**Watery Swamp 1.0**   

Land - Swamp  

When CARDNAME enters the battlefield, lose 1 life.


At first blush, this seemed close. Just like a fetch land, you could get one of two colors at the cost of 1 life. On closer inspection, it was a bit worse, as fetch lands both thin your deck, increasing your ability to draw nonlands, and allow you to get cards with more than one basic land type, helping you fix your mana beyond the two colors. My second attempt borrowed from a trick I'd used when designing the "shock lands" from original *Ravnica* (used in all the Ravnica sets).


**Dirty Island 2.0**   

Land - Island  

As CARDNAME enters the battlefield, you may pay 1 life. If you don't, it enters the battlefield tapped.  

///  
**Watery Swamp 2.0**   

Land - Swamp  

As CARDNAME enters the battlefield, you may pay 1 life. If you don't, it enters the battlefield tapped.


You can pay 1 life if you need it entering untapped, but if you didn't, you weren't out the life. This was the version that I first showed to Aaron Forsythe. Aaron liked the design but questioned whether we had to have the life payment. What if both sides just entered the battlefield untapped without any penalty?


I expressed my concern that it would make them pretty close to being "strictly better" than a basic land. Technically, they're non-basic lands, and we occasionally make non-basic land hate, but that just didn't seem like enough. Aaron then suggested we remove the basic land type. One of the ways we've slightly juiced up dual lands is to give them basic lands types. What if we did the reverse? Now, you can't tutor it out when searching for the basic land type and it wouldn't count for cards which counted that basic land type. It was only a minor downgrade, but we felt enough to justify printing the cards in their coolest form.


And that is how the Pathways came to be.


**Farsight Adept** 


![Farsight Adept](https://media.wizards.com/2020/znr/en_LMfE8EfXrI.png)


One of the ongoing tasks of the Council of Colors has been finding ways to get some card draw into white in a way that both feels white and doesn't undercut white's weakness. I should note that we're not trying to solve this through only one means but are looking at a variety of different solutions. One such solution was something that popped up during *Throne of Eldraine* on the card [Happily Ever After](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Happily+Ever+After).


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Happily+Ever+After)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Happily+Ever+After)
Erik Lauer, *Throne of Eldraine*'s lead set designer, was trying to add a little something extra to the card and felt that universal draw (aka everyone draws) felt appropriate. That wasn't something white did though, so he came to the Council of Colors to see if he could. We all agreed that it philosophically felt white, as white is the color most associated with providing for the group as a whole. Also, because it let others draw, it wasn't letting you get ahead on answers because other players were drawing threats. We agreed to add this ability to white on a provisional basis.


As a quick aside, the ability got added to [Happily Ever After](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Happily+Ever+After) because that's the card in the set that needed the effect. We didn't design the card from the ground up to test that effect. I got a lot of feedback on [Happily Ever After](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Happily+Ever+After) that the card didn't help in Commander because it was limited to a deck playing five colors, which meant the deck already had plenty of access to card drawing. We were testing the general response to how it felt. Did it feel white? It was not, by itself, meant to be the answer as much as a card in a line of progression allowing us to get to an answer, and again, not even the only answer.


We did get some feedback from this card—some externally, some internally. Externally, no one had a problem with the effect being white. I did get plenty of the feedback I mentioned above, though. Internally, we tested out this mechanic on other sets, and the feedback we got was that it's not that useful an effect in Commander if everyone draws a card. What if the effect was that you and target opponent each draw a card? This way, it wouldn't be any different in two-player play, which didn't need the effect, but useful in multiplayer play, which did. I particularly like how it adds a political aspect because you get to choose which opponent gets the card.


As with [Happily Ever After](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Happily+Ever+After), this is us testing space with the card we had available more than us creating a card specifically for this effect, but as we move closer to the right execution, you will see this effect start to show up on more Commander-focused cards.


**Feed the Swarm** 


![Feed the Swarm](https://media.wizards.com/2020/znr/en_o0Kj7j1jfC.png)


While we're on the topic of the color pie, here's another card with us testing some new space. As I've explained in previous columns, we've decided that we want black to be able to destroy enchantments, but our goal is to have it be third to white and green in the ability. Our previous attempts ended up hitting a little too low, so we're experimenting with something a little better while still being clearly third in enchantment removal. As with any testing, I don't know where we're going to end up (and maybe this is slightly above where we finish up at), but I'm eager to see what people think of this card. Player feedback is important on changes like this because we're trying to get a sense of what feels right, so I'm eager to hear your thoughts.


Feeling *Zen-dikar Rising*
==========================


That's all the time I have for today. As always, I want feedback from all of you. Targeted black enchantment removal, white card draw, MDFC dual lands, the party mechanic—let me know what you think of them all, or just *Zendikar Rising* in general. You can [email me](mailto:making.magic@hotmail.com) or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).


Join me next week for more card-by-card stories.


Until then, may you shuffle a lot less when choosing which of two lands to play.




 

##### 
 #773: Adam Prosak






##### 
 #773: Adam Prosak




In this podcast, I interview Adam Prosak, a *Magic* designer who most recently led the set design for *Core Set 2021*.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork773_adamprosak_Kw4O32Pd.mp3)



  


 

##### 
 #774: Replies with Rachel #5






##### 
 #774: Replies with Rachel #5


36:14



Before Rachel heads back to college, I thought it would be fun to do another mailbag podcast with her.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork774_replieswithrachel5_su23S9dD.mp3)




* [**Episode 772**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork772_makingmagicinapandemic_su72Ss93.mp3) Making *Magic* in the Pandemic
* [**Episode 771**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork771_coreybowen_we2Ds992.mp3) Corey Bowen
* [**Episode 770**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork770_ikoriapart2_8Hdw7HHs.mp3) *Ikoria*, Part 2








---
[Link to Wayback Machine](https://web.archive.org/web/20220126201320/https://magic.wizards.com/en/articles/archive/latest-developments/one-planeswalker%E2%80%99s-journey-2007-11-02)

[_metadata_:author]:- "Devin Low"
[_metadata_:description]:- "How development got from Theseus the White to Ajani Goldmane. As Magic States and Champs approached, R&D has been abuzz with excitement to see Lorwyn debut on the tournament scene. Which cards would be the early breakout hits? Which new deck types would Lorwyn unlock in Standard? Which tribes would win or make Top 8? (Elves, Kithkin, Goblins, Merfolk, Faeries, and Elementals"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "623856"
[_metadata_:publish_date]:- "2007-11-02"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "One Planeswalker’s Journey"
[_metadata_:wayback_capture_timestamp]:- "2022-01-26 20:13:20"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220126201320id_/https://magic.wizards.com/en/articles/archive/latest-developments/one-planeswalker%E2%80%99s-journey-2007-11-02"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/one-planeswalker%E2%80%99s-journey-2007-11-02"
---


One Planeswalker’s Journey
==========================



 Posted in **Latest Developments**
 on November 2, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DevinLow.jpg)
By Devin Low












How development got from Theseus the White to Ajani Goldmane.
-------------------------------------------------------------


As **Magic** States and Champs approached, R&D has been abuzz with excitement to see *Lorwyn* debut on the tournament scene. Which cards would be the early breakout hits? Which new deck types would *Lorwyn* unlock in Standard? Which tribes would win or make Top 8? (Elves, Kithkin, Goblins, Merfolk, Faeries, and Elementals so far.) And which planeswalkers would win or make Top 8? (It turns out: all five.) Some of our most important goals in planeswalker development involved making planeswalkers unique, strategic, fun, and powerful parts of Constructed play. Feedback from players has been very positive on both planeswalkers and *Lorwyn* Standard, and it warms my heart to hear that we seem to have reached those goals.


### The Nineteen Principles for Developing Planeswalkers


Principle 1) They must feel like a totally new card type.  

Principle 2) They must feel like another **Magic** player has sat down to play with you.  

Principle 3) They must match the creative team's top-down designs.  

Principle 4) They should embody the core essence of their colors.  

Principle 5) The cycle must be loose, not tight, so they feel like individuals.  

Principle 6) They must work well in any deck against any opponent's deck.  

Principle 7) They must each be a path to victory.  

Principle 8) The abilities should have some cool synergies.  

Principle 9) Each should give you multiple paths to take.  

Principle 10) Each has a +N ability, a -N ability, and a -BIG N "Ultimate" ability  

Principle 11) Their abilities don't explicitly mention the world they're in.  

Principle 12) The Ultimate should be jaw-droppingly awesome.  

Principle 13) They must each be powerful in Limited.  

Principle 14) They should all be decent in Constructed, and some of them should be awesome in Constructed.  

Principle 15) They must appeal to Timmy.  

Principle 16) They must appeal to Johnny.  

Principle 17) They must appeal to Spike.  

Principle 18) They must play well, and they must be fun!  

Principle 19) They must be interactive, and every color must have answers to them.


Last week I laid out [Nineteen Principles of Planeswalker Development](/en/articles/archive/latest-developments/nineteen-principles-developing-planeswalkers-2007-10-26). This week I'd like to show you how we put those principles into practice, taking you through the evolutions and developmental details of one of *Lorwyn*'s planeswalkers from start to finish. Instead of taking a general survey of all five planeswalkers, I'll zoom in on one in detail. This week's article is very much a companion piece to last week's, so I encourage you to read that one first.


### Liquid Justice


As Mark Rosewater will describe next Monday, the overall planeswalker implementation took designers a long time to figure out, and I'm glad they took the time to get it right. Then the individual card designs took a lot of time after that. So the *Lorwyn* development team saw our first planeswalker cards a month after *Lorwyn*'s formal handoff to development. We were definitely curious to see what they would do, and here is what we found:



> 
> RW11\_PEA  
> 
> Theseus the White (v1.0)  
> 
> 3WW  
> 
> Planeswalker - Theseus  
> 
> Loyalty 9  
> 
> +0) Until the beginning of your next turn, opponents' permanents come into play tapped.  
> 
> -2) Tap target creature. Creatures don't untap during their controllers' next untap steps.  
> 
> -4) Destroy all tapped creatures.
> 


Yup, that's pretty different from where we ended up.


The planeswalker rules were very similar to their final form, with one big difference: They had "Play one of these abilities at the beginning of your upkeep," *not* "Play up to one of these abilities per turn, whenever you could play a sorcery." The upkeep timing made them a full turn slower to activate.


Some of the magic is there in this design, but there is still a lot missing. Although we didn't have a list of principles of planeswalker development at the time, it's interesting to look at that list and see where this design fulfills them and where it doesn't. The Planeswalker rules did a good job of making them feel like a totally new card type and making them feel like another Magic player has sat down to help you. These abilities also have an inherent synergy, where the first and second abilities naturally toll into the third. And the design also matched the creative team's top-down planeswalker concepts, which Doug Beyer laid out in his recent article [Planeswalkers Unmasked](/en/node/623126). In particular, the white planeswalker concept at the time focused even more on punitive justice—*those who have wronged you must pay!*—and the "destroy tapped creatures" ability does a good job of punishing those creatures who attacked you the previous turn, as well as combining with the other tap effects on the card.


So what does this design lack? One element missing here is an awesome "Ultimate" you build his loyalty up to hit. With 9 starting loyalty, and the third ability costing –4, you can activate his third ability right away if you want (that is, right away in your next turn's upkeep). The idea of the planeswalkers all having an Ultimate hadn't yet occurred to us as a global principle. It was only after we had spent some time playing the initial "Hippolyta the Red" design (later [Chandra Nalaar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar)), which *did* build up loyalty to reach a giant third ability, that R&D saw how fun that was and decided to implement Ultimates across the board.


![Kismet, Blinding Beam, and Vengeance](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/dl9_cardfan.jpg)Another thing missing here is a path to victory. Theseus can [Kismet](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kismet) your opponent, lock down opposing creatures in a recurring [Blinding Beam](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blinding+Beam), then smash all the tapped creatures with a multi-[Vengeance](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vengeance) effect. But when he's done with all that, he doesn't have an offensive plan to complement his defensive one. Once all the creatures are smashed, Theseus has to go back to passive [Kismet](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kismet) mode and wait for some more creatures to show up. He's "that guy" who once sat down at your multiplayer table with his card drawing / double Pendrell Mists / [Living Lands](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Living+Lands) deck, successfully blew up everyone's creatures and lands, and prevented them from ever playing any more... but he never thought about what he would do after he pulled that off, he didn't have any ways to win, and he decked himself. Now, tons of **Magic** cards don't operate unless enemy creatures are on the board. You know what I mean if you've ever controlled a [Torture Chamber](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torture+Chamber) on an empty battlefield. And it's okay that many cards only work on creatures. But since **Magic** players always have a way to win, it felt wrong to us that Theseus did not.


Another thing missing here is multiple ways you can use him. Opponents generally wouldn't all-out attack into Theseus unless they could bring him below the 4 loyalty he needed to destroy all their tapped creatures. And he only activated in your upkeep. That meant you would almost always play him and say go, then tap down two creatures over two turns for –2 loyalty a piece. Then destroy those two tapped creatures. Then you would go into [Kismet](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kismet) mode for the rest of the game, since you'd be down to 1 loyalty. There was very little reason to deviate from this timetable unless Theseus took a bunch of damage.


The loyalty total also seems hilariously high. *Nine?* With nothing to base them on, the first loyalty numbers were a stab in the dark. The initial planeswalker designs all showed up in that loyalty ballpark. After all, a player has 20 life, right? In our early games with planeswalkers, the opponent would be at 9 life and play a 10-loyalty planeswalker. You'd look at your 3/3 flier and your 2/1 Islandwalker and think, "I can destroy that permanent with a couple of attacks...or I can destroy that player with a couple of attacks. Hmm, I think I figured it out...." The planeswalker designers had expressed the goal of giving players an interesting choice: "Should I attack the opponents' planeswalkers or their heads? But 9 loyalty was so high that attacking the player was almost always the correct option, taking out the interesting strategic question we had sought.


### [Glorious Anthem](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glorious+Anthem) / [Knighthood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knighthood) / [Martyrdom](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Martyrdom) / [Folk Medicine](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Folk+Medicine)


After three weeks of play, the *Lorwyn* development team dropped all the loyalties by almost half. Theseus went down to 5 loyalty, and his loyalty costs shrunk to match, going to –0, –1, and –2 respectively. The *Lorwyn* developers also requested some ability changes. CQI stands for "Continuous Quality Improvement"—an R&D euphemism for "Ability killed. Please redesign it." DAL is myself, AF is Aaron Forsythe, DB is fellow columnist Doug Beyer, and SW and MJ are **Magic** developers Steve Warner and Mons Johnson.



> 
> DAL 9/22: Chops lifetotals by 45%. Team likes first 2 abilities. We feel final ability is very non-white. White's very occasional "destroy tapped creature" effects have been flavored as Reciprocate, where you kill the guy because he attacked you or tapped. You can combo Vengeance with Master Decoy to kill a guy, but it is a weird sideways combo like many other weird sideways combos. This Planeswalker systematically marking creatures for death then killing all of them is too nonwhite for us. CQI the third ability - that might make you want to redesign the whole thing, we don't know. Infinite tapdown of perms is fine, but not this third ability.  
> 
> AF 10/25: This guy is a tough nut to crack. He is not a typical white soldier or cleric--he is some kind of embodiment of justice. It's hard to do "justice" with effects that go off on your upkeep or that you're trying to build up to. This was our best shot.  
> 
> DAL 10/27: Key problem is that all the other Planeswalkers are liked by team and make us smile. For whatever reason, this one does not. It does seem a tough challenge to design.  
> 
> DB 11/2: Seems strange that the white one can't heal itself.  
> 
> DB 11/2: For more justice-themed creature kill: "Target creature deals damage to itself equal to its power"?  
> 
> AF 11/3: This guy should heal himself.  
> 
> SW 11/10: This guy has not been very good in limited, I don't think he will be good in constructed unless he can heal himself somehow.  
> 
> MJ 11/16: suggestion: change first ability to +1, last ability to -4 or 5  
> 
> DAL 12/6: WTB White Planeswalker
> 


Towards the end of these comments, you can see a growing dissatisfaction with the ability set as a whole, as well as a desire to adopt some of the cool things that other planeswalkers were doing, like moving their loyalties *up* instead of down. The final cryptic comment here marks the demise of Theseus v1.0, and the clearing of his rules text box, using an online shortcut for "Want to Buy White Planeswalker."


In December, we also made a breakthrough that made the planeswalkers much more fun: In addition to triggering at the beginning of your upkeep, we let the planeswalkers trigger on coming into play as well. Last week I explained how valuable this change was under Principle 19. Instead of coming out and hoping to survive the world around them long enough to make it to their next upkeep, planeswalkers now came out and did something to the world, making the world try to survive *them*. Instead of the prey, they became the predator.


[![Ajani_Goldmane](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/LRW/Ajani_Goldmane.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Ajani%2BGoldmane)
By Christmastime, we had a new design, and Theseus the White had a new name: "Ajani."



> 
> RW11\_PEA  
> 
> Ajani (v2.0)  
> 
> 2W  
> 
> Loyalty 3  
> 
> +1) Creatures you control get +1/+1 and First strike until end of turn.  
> 
> +X) You gain X life where X is the number of creatures you control (intent is both you and the planeswalker gain X).  
> 
> +0) Until the start of your next turn, redirect all damage that would be dealt to you or a creature you control to CARDNAME.
> 


This design shows the evolution of our planeswalker design and development technology in the previous months. He could now heal himself. He could now heal you. He now had a fun [Glorious Anthem](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glorious+Anthem) ability that's inherently good in Limited and Constructed. His loyalty was low enough to be more interactive and invite strategic choices. He matched the new focus of Ajani's flavor concept well: coaxing out the best in others. And he had a couple of different paths he could take: pumping up your team, gaining life, or martyring himself to save you and your creatures.


This design also has some big flaws. First of all, while several of the other planeswalkers were cooking up serious Ultimates by now, this card's third ability is weak and uninspiring. I don't want to lose my planeswalker just to save my [Suntail Hawk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Suntail+Hawk)! In addition, damage prevention & redirection is inherently reactive, and doesn't play well as an effect you have to play during your own turn (e.g. [Divine Light](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divine+Light)). In addition to that, planeswalkers were already being attacked and sucking up damage that would otherwise go to their controllers. Having an ability that does the same thing is inelegant. People were really enjoying the other planeswalkers' Ultimates, and they were asking for Ajani to have one too. Finally, the fact that all three abilities basically depend on having creatures in play was too one-dimensional: if you didn't have creatures in play, this design couldn't do anything except take hits. Lame.


### The Avatar Cometh


Just after New Year's, we had a new design:


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/dl9_Avatar.jpg)
> 
> RW11\_LRW  
> 
> Ajani Goldmane (v3.0)  
> 
> 2WW  
> 
> Loyalty 4  
> 
> +1) You gain 2 life.  
> 
> -1) Creatures you control gain +1/+1 and vigilance until end of turn.  
> 
> -8) Put a \*/\* White Avatar creature token into play with "This creature's power and toughness are each equal to your life total."
> 


Now we had some action. In contrast to our first planeswalker design, this one has a built-in path to victory. It has multiple viable strategies to pursue. The planeswalker can defend himself by giving your creatures vigilance while they get a temporary [Warrior's Honor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warrior%27s+Honor). And he has a cool, exciting Ultimate that has synergies with the first two abilities: the Avatar token is bigger because you gained life from the first ability. The Avatar can keep getting bigger after you make it by using more of the first ability. And the second ability can give the Avatar vigilance while it's bashing faces.


For text length reasons, there was a chance we might need to lock the Avatar's power/toughness when it was created, instead of having it be a \*/\* creature that dynamically updated its P/T as you gained life. But the combo was so cool that we tried hard to make it work out as a changing \*/\*, and fortunately it did. Some people also felt that if *Ajani* is summoning a [Serra Avatar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Avatar), then the Avatar should match *Ajani's* loyalty, not your own life total. It could still grow over time as Ajani used his +1 loyalty ability. The problem with that suggestion is it means if you crank out the quickest Avatar you can, spending Ajani down to zero...the Avatar would die on arrival. And even if you make the Avatar the turn after that... it would be a 1/1. Something told us players would like the 26/26 Avatar more than the 1/1.


At the end of January, we decided to make Ajani more powerful. We wanted this guy to be powerful in Limited and Constructed after all. We changed the middle ability from [Marshaling Cry](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marshaling+Cry) to the much more powerful:



> 
> -1) Put a +1/+1 counter on each creature you control. Those creatures gain vigilance until end of turn.
> 


Now even if your opponent destroyed Ajani immediately on sight, Ajani would leave behind a permanent reminder of his passing in the form of +1/+1 counters on all your guys. Unlike the previous version, your vigilant creatures were now also pumped up for blocking purposes. And now the pump ability stacked with itself: if you used the ability twice in a row, all your creatures were +2/+2 bigger. If you used it three times in a row, all your creatures were +3/+3 bigger. And if you used it four times in a row, all your creatures were... You get the idea. We also dropped his Ultimate cost to –7.


In early March, as the typesetters were gearing up their presses, we clapped Ajani on the back, shook his furry paw, and gave him a final push to wish him good luck, shaving down his Ultimate cost again, to –6. This really sped up the big token: you could play him and gain life (turn zero), gain life the next turn (turn one), then have him summon the 24/24 Avatar the following turn (turn two)—or wait a turn longer if you wanted to keep Ajani around after the fact. We had played him a ton by this point, and we had a lot of fun with him. And that's his final form:



> 
> RW11\_LRW  
> 
>  Ajani Goldmane (v3.5)  
> 
>  2WW  
> 
>  Loyalty 4  
> 
>  +1) You gain 2 life.  
> 
>  -1) Put a +1/+1 counter on each creature you control. Those creatures gain vigilance until end of turn.  
> 
>  -6) Put a \*/\* white Avatar creature token into play with "This creature's power and toughness are each equal to your life total."
> 



[![Ajani_Goldmane](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/LRW/Ajani_Goldmane.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Ajani%2BGoldmane)

### Tips n' Templates


There are usually a couple of rules details to iron out during the final templating meetings, and Planeswalkers had more than most. We had moved from "Play one of these abilities at the beginning of your upkeep" to "When CARDNAME comes into play, or at the beginning of your upkeep, play one of these abilities." We changed this to say basically "You may play one of these abilities per turn, whenever you could play a sorcery." That way there's a single time you can play the ability, instead of the weird duality of triggering both upon coming into play and at the beginning of your upkeep.


![Garruk Wildspeaker, tapped, with a big red X](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/dl9_Garruk.jpg)That version of the planeswalker rules led us to a new question: "Now the planeswalkers can use their abilities once per turn. **Magic** has a mechanic that expresses 'Use this once a turn': Tapping. Should the planeswalkers tap to use their abilities?" We tossed this idea around, but it would mean uncontrolled loyalty acceleration with cards that untap target permanent, like [Rimewind Taskmage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rimewind+Taskmage). We really didn't want to weaken the planeswalkers' numbers to account for little [Rimewind Taskmage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rimewind+Taskmage) and his friends. Tapping would also make the planeswalkers feel a little more like artifacts or creatures, which we did not want. We avoided tapping and stayed with "once per turn."


When people hear the planeswalker rules, another question is often "Okay, so [Incinerate](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate) can lower my planeswalkers' loyalty. Can [Healing Salve](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Healing+Salve) raise my planeswalkers' loyalty?" If so, you could play [Bottle Gnomes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bottle+Gnomes) turn three, then play out [Ajani Goldmane](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Goldmane), sacrifice [Bottle Gnomes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bottle+Gnomes) to increase his loyalty by 3, then immediately use his Ultimate to make a turn-four 23/23 Avatar token, leaving Ajani still on the board. Yeah, that does not sound like good game play. Again, allowing lifegain effects to raise planeswalker loyalty would force us to raise the cost on several of the planeswalkers' Ultimates, and we preferred to disallow the lifegain interaction so we could keep the Ultimates sleek and powerful.


And that's how we put our planeswalker development theories into practice, redesigning and redesigning "Theseus the White" until we had a white planeswalker with fun, power and personality.


### Last Week's Poll




| **Which of the nineteen principles is the most important for us to remember when developing planeswalkers?** |
| --- |
| Principle 18) They must play well, and they must be fun! | 1695 | 22.6% |
| Principle 2) They must feel like another Magic player has sat down to play with you. | 815 | 10.9% |
| Principle 19) They must be interactive, and every color must have answers to them. | 762 | 10.2% |
| Principle 1) They must feel like a totally new card type. | 539 | 7.2% |
| Principle 12) The Ultimate should be jaw-droppingly awesome. | 511 | 6.8% |
| Principle 6) They must work well in any deck against any opponent's deck. | 406 | 5.4% |
| Principle 9) Each should give you multiple paths to take. | 388 | 5.2% |
| Principle 4) They should embody the core essence of their colors. | 380 | 5.1% |
| Principle 14) They should all be decent in Constructed, and some of them should be awesome in Constructed. | 360 | 4.8% |
| Principle 5) The cycle must be loose, not tight, so they feel like individuals. | 294 | 3.9% |
| Principle 7) They must each be a path to victory. | 272 | 3.6% |
| Principle 8) The abilities should have some cool synergies. | 269 | 3.6% |
| Principle 10) Each has a +N ability, a –N ability, and a –BIG N 'Ultimate' ability | 175 | 2.3% |
| Principle 17) They must appeal to Spike. | 138 | 1.8% |
| None of the above | 118 | 1.6% |
| Principle 11) Their abilities don't explicitly mention the world they're in. | 99 | 1.3% |
| Principle 3) They must match the creative team's top-down designs. | 87 | 1.2% |
| Principle 16) They must appeal to Johnny. | 87 | 1.2% |
| Principle 13) They must each be powerful in Limited. | 54 | 0.7% |
| Principle 15) They must appeal to Timmy. | 53 | 0.7% |
| **Total** | **7502** | **100.0%** |

This is a tough poll to answer because there are so many choices, and several of the choices seem totally necessary. The four leading answers all revolved around good gameplay, fun, and planeswalkers feeling more like another **Magic** player than another **Magic** card. The clear reader favorite was Principle 18: *They must play well and they must be fun.* That's also the one I would pick. Making fun cards and a fun game is absolutely the most important thing we do here, and no other goal is more important than that.


Next Week: They're cheap, they hit hard, and they love attacking so much, sometimes they even [Militia's Pride](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Militia%2527s%2BPride). They're the Kithkin!









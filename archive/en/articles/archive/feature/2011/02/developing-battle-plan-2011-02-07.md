
---
[Link to Wayback Machine](https://web.archive.org/web/20210429042445/https://magic.wizards.com/en/articles/archive/feature/developing-battle-plan-2011-02-07)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/developing-battle-plan-2011-02-07"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429042445id_/https://magic.wizards.com/en/articles/archive/feature/developing-battle-plan-2011-02-07"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 04:24:45+00:00"
[_metadata_:publish_date]:- "2011-02-07"
[_metadata_:description]:- "Mirrodin Besieged was my first development team. Big step up from the old Brainburst.com `Fantasy Card` forums, gotta say, though if you cruise the archives for `Wumpus Jr.` I am sure you'll unearth some real gems. Big step up from spot-errata-ing Phantasmal Fiend's `effects that further alter ... ` clause on my living room floor because none of my playgroup had any idea what"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Developing a Battle Plan
========================



 Posted in **Feature**
 on February 7, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 






M*irrodin Besieged* was my first development team. Big step up from the old Brainburst.com "Fantasy Card" forums, gotta say, though if you cruise the archives for "Wumpus Jr." I am sure you'll unearth some real gems. Big step up from spot-errata-ing [Phantasmal Fiend](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Fiend)'s "effects that further alter ... " clause on my living room floor because none of my playgroup had any idea what it meant or how it worked. 


Of course, I had no idea what being on a Development team meant or how it worked, really, the first time that Mad Genius Erik Lauer called me into the Ivory Tower and handed me a Multiverse printout of the entire set. I knew I was excited. I knew it seemed cool. I knew I'd seen people's faces on the website, the little smiling bio-blurbs. I knew that I'd be tweaking some numbers and turning some knobs and saying "Nah, dawg" to the latest Designerly take on Ancestral Lotus Ritual of Twisted Walking Time or whatever was most broken on this particular Thursday. But beyond that, I didn't really know what development, um, *did.*


### What Does Development Do?


One of the things that surprised me the most after I started working at Wizards was how much of a set's identity is determined by the developers. This ought to have been obvious, I suppose—after all, there are five full-time paper **Magic** developers (Erik Lauer, Tom LaPille, Dave Humpherys, Mark Gottlieb, and myself) and only one full-time paper **Magic** designer (Mark Rosewater). But I had gotten a sense from reading the website and from thinking about the process of building a set that Design did most of the heavy-lifting and Development made sure that things didn't get too crazy from there.


That's not really how it works.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature129_blightsteel.jpg)  
The majority of the **Magic** experience is shaped by **Magic**'s developers. Scout's honor. I'm not tooting my own horn, either, since at the present moment I'm on way more Design than Development teams. So it's not an issue of territory. What happens, rather, is that different aspects of **Magic**'s game play require very different sets of skills to nurture properly. Mark Rosewater has famously said that far, far fewer than 1% of his card ideas ever actually make it to print—but what he didn't mention is that without those other 99% of ideas that he created and discarded, the sets that *do* see the light of day would be exponentially worse. In other words, Design lays the foundation that allows Development to do its job in the first place.


To use an example, if *Mirrodin Besieged* is a building, it's Design that says "We need a building on the corner of 8th and Madison, and that building should probably be a bank, and it seems like a good idea that it should be built out of steel and glass, and you should probably avoid constructing it in the style of '70s Neo-Brutalist fortress-academia." Then Development comes along and says, "Cool," and develops a blueprint and designs the building and erects a bunch of scaffolding and conceptualizes a sweet lobby with, like, vaulted ceilings and abundant fluted, refractive glass. Sometimes Design reminds Development that if you want to transact currency and open 401(k)s and leverage assets and all this awesome, complex, sophisticated behavior, it's pretty important that your columns prevent your roof from caving in. Other times Design says, "Hey, you know this problem you're having with the shape of your Men's restroom faucet handles? I've got the *perfect* fix!" 


![Distant Memories](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Distant+Memories)  
As you can see, then, Design does some vital work. But Development also has an important role to play. In general—and concerns vary from set to set, of course—Development wants to:


a) Ensure a dynamic, rich, and robust Limited environment that feels operatively different from the previous one, even if those differences are subtle.  
 b) Maintain the fun, health, and game-play experience of the current Standard Constructed format.  
 c) Provide players of all persuasions (Timmy, Johnny, Spike, casual, competitive, highly- or lightly-enfranchised ... ) something cool that inspires them to play, and enjoy, **Magic**.


There are other issues too, naturally. We have a host of supplementary products that are accomplishing specific objectives, and those need to be up to par. Other formats exist beyond Standard, and those need to continually evolve. And it's absolutely crucial to never forget, after you've applied thirty different metrics and attempted to meet a zillion different needs, how your set *feels*, at the end of the day. Sometimes, even though you can't put your finger on it, things just aren't quite right.


With all of that said, let's take a look at how this applies to *Mirrodin Besieged*.


### Well Of Course You Know, This Means War!


A top-line goal for *Mirrodin Besieged* was that it conveyed, on a visceral level, the war between the Mirrans and Phyrexians. This goal permeated every aspect of both Design and Development but was most important for Limited, since you couldn't help but stare over and over again at the "soldiers" for both sides. If a substantial portion of your deck consisted of *Scars* and *Besieged* cards, and yet it nevertheless didn't feel like a war was going on, then we had a problem.




|  |  |
| --- | --- |
| Gold Myr | Carnifex Demon |

A more straightforward game play related concern involved the desire to shift, in style, away from *Scars* Limited. Both Erik and I had severe issues with the ponderous, bomb-intensive nature of *Scars* Sealed Deck. A combination of a) five common mana Myr, b) an artifact set, and c) an abundance of powerful attrition-intensive effects rendered it possible to play almost all of your bombs in any given pool. Add to this the fact that a huge percentage of *Scars*' powerful rares dominated the board by killing everything else, and you can see pretty clearly that you don't want to head further down the same road. 


Another issue was the power of the infect deck in draft. Both Mark Rosewater and I argued that it was totally legitimate to play a mixture of infect and non-infect creatures in the same deck. I, in fact, was *happy* to do so, viewing the keyword as an all-upside combat mechanic (when pressed by developer Tom LaPille about how bad it was to be attacking along multiple axes, I pointed out that I rarely found myself losing games of **Magic: The Gathering** that involved multiple creatures connecting with my opponent). The trouble was that if drafters at a table *did* view infect as an all-or-nothing strategy, what tended to happen was that a table would have one completely insane black-green infect deck (due to ridiculousness like [Plague Stinger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Stinger), Vault Scavenger, and [Untamed Might](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Untamed+Might) going 8-10th pick) that absolutely slaughtered everything else. With *Mirrodin Besieged* in the environment, we hoped to dampen this effect. 


As it happened, solving the first problem helped to solve the other two. We realized that having a viable non-infect aggressive strategy would help combat the attrition-into-bombs game play of Scars Sealed, and we wanted to build that strategy into red and white since black and green already had an effective aggro deck of their own. Red and white are also, not-so-coincidentally, the two strongest Mirran sides, so it became clear that they ought to get a combat mechanic that would serve both to tie that aggressive deck together and message loud and clear that some rambunctious fightin' was in fact going on. That mechanic became battle cry—and when battle cries resound, a war can't be too far away. Meanwhile, the inclusion of living weapon gave the Phyrexian decks a little more identity and visibility, and offered a strategy along a separate axis from the "poison" decks that already existed.




|  |  |
| --- | --- |
| Plague Stinger | Priests of Norn |

Dealing with the infect problem required a little more subtlety. We knew that we wanted to "bleed" infect into other colors with *Mirrodin Besieged* to convey the pervasive creep of Phyrexian power across the plane. What we realized was that we needed to do it in such a way that the cards would still be useful in non-infect decks, while simultaneously evolving infect in existing colors to provide broader situational utility. 


The poster child for the former is the 1/4 common [Priests of Norn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Priests+of+Norn). Erik Lauer loves to tell the story about how he played a couple copies of the Priests in a regular white-blue flying deck. The flyers raced while the Priests held the ground, hitting for a poison here and there while shrinking the opposing army over time. Eventually, though, he had to hold back his flyers to survive a lethal attack. They all chumped, he managed to stabilize, and eventually it was a [Contagion Clasp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Contagion+Clasp) that killed his opponent even though his board of regular old creatures had dealt something like 15 damage combined. 


A solid example of the latter vision for infect, meanwhile, is a card like [Rot Wolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rot+Wolf). Because you can use it to aggressively trade at advantage, its value as an Infect creature that purely races the "goldfish" goes correspondingly down. That said, there's still plenty of potential for the infect deck to just get you out of nowhere. [Flesh-Eater Imp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flesh-Eater+Imp), which lets you sacrifice creatures to grow it a la [Phyrexian Ghoul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Ghoul), becomes lethal in a hurry—especially when you pair it with a [Myrsmith](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Myrsmith), or a [Master's Call](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master%27s+Call) or two!


### BRB Sculpting Formats And/Or Minds


Going into *Mirrodin Besieged*, we were all pretty happy with the state of our Standard environment—and, in retrospect, our predictions were pretty accurate. Our in-house Red-Green [Primeval Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primeval+Titan)/[Valakut, the Molten Pinnacle](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Valakut%252C%2Bthe%2BMolten%2BPinnacle) decks were worse than the ones in the real world, since we were married to the idea of resolving [Destructive Force](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Destructive+Force), but overall the rest of the metagame looked similar. That meant we all had our eyes on a) not screwing everything up via some kind of colossally broken mistake, b) fleshing out the themes introduced in *Scars of Mirrodin*, and c) giving other colors something to do in the four-slot that wasn't just embarrassed by a resolved [Jace, the Mind Sculptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+the+Mind+Sculptor).




|  |  |
| --- | --- |
| Creeping Corrosion | Kataki, War's Wage |

The first point deserves some explanation, since there've been no small number of raised eyebrows at the inclusion of [Creeping Corrosion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Creeping+Corrosion) and [Into the Core](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Into+the+Core) in *Mirrodin Besieged*. Why, after all, would you want to put a ton of artifact hosers in your artifact block?


On the surface, it isn't intuitive, and you definitely run the risk of telling people not to do the cool stuff your set wants them to do. For *Mirrodin Besieged*, however, we were terrified of what happened during *Darksteel*, the last middle set of an artifact block. That set had a number of Development mishaps, but one of the most egregious was that there was no "safety valve" to pull if things got out of control. It wasn't until *Saviors of Kamigawa*, in fact, that [Kataki, War's Wage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kataki%2C+War%27s+Wage) came around to put a dent in what was left of Affinity. 


We believe that the smartest approach isn't to wait until your format breaks in half to start offering solutions. So anytime a set has a linear theme (like metalcraft) that's potentially too powerful, we like to make sure there's a way to hose it just in case. Moreover, we like to make sure that those cards are messaged loud and clear so that people know what they need to get their hands on if they want to deal with a problem. [Riftsweeper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riftsweeper), for example, was an *awesome* way to punish suspend cards—but a huge percentage of players weren't able to understand that, because it attacked the problem obliquely. 


As for point B, some players bemoaned the fact that despite infect and metalcraft offering enticing incentives ([Putrefax](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrefax), [Ezuri's Brigade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ezuri%27s+Brigade), [Tempered Steel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tempered+Steel)) in *Scars*, the decks haven't really panned out yet in Standard. While I maintain that an [Overgrown Battlement](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overgrown+Battlement)-fueled mono-green infect deck is at least a reasonable player in the current environment, the fact remains that none of the *Scars* themes immediately hit the ground at Tier 1. This is something we're thinking a lot about. 


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature129_clique.jpg)  
A number of factors suggest that you don't want to debut an archetype at its strongest level. For one thing, developers screw up. If you put all the good Faeries cards into *Lorwyn*—here, have a [Bitterblossom](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bitterblossom) and a [Mutavault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault)—you certainly message loud and clear that new strategies are powerful. If they're *too* good, though, you have to live with that deck for two whole years without anything rotating out. It's also relevant that you want to be able to deliver something exciting for new archetypes later on in a block. It would have been entirely possible, for example, to have delivered the *Onslaught* block-era Goblin deck on a platter full-stop in *Onslaught*. Here, have it, etc. However, it's really important to avoid just creeping power set after set after set. So what would happen is that the Goblin player would have left disappointed once in *Legions* and again in *Scourge*, because the overall power level of the deck would still need to cap at a certain point, so it would have been impossible to print new goodies.


At the same time, you also don't want people looking at a new set and shrugging their shoulders. So we've tried to expand upon some of the themes introduced in *Scars* that will hopefully pay off the players who have been waiting patiently for their favorite deck's time to shine. I battled this past weekend at the Mirrodin Besieged Prerelease in New York, for example, with a [Signal Pest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Signal+Pest)-fueled mono-red metalcraft deck that makes phenomenal use of its [Kuldotha Rebirth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kuldotha+Rebirth)s and [Mox Opal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Opal)s. Meanwhile, cards like [Phyrexian Crusader](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Crusader), [Phyrexian Vatmother](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Vatmother), and [Inkmoth Nexus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkmoth+Nexus) (I probably Future Future League'd with over a hundred of these guys) give the infect deck some real punch *beyond* an end-of-turn [Carrion Call](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carrion+Call) and a fistful of [Groundswell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Groundswell)s. 


Last, but not least, we have that Jace guy.


You see him sitting there in his hoodie and context-independent loincloth being all, "Yo, check out my Slinky of arcane-symbols—don't you wish you knew what THESE meant?" Then he draws some cards, bounces your guy, and COMPLETELY CRUSHES YOUR MIND OMG WHERE DID MY HAND AND DECK GO??!! before you even know what's hit you.


Yeah. I'm tired of that, too.


I'm not saying Jace is going away. Secretly, I *may* even like casting a Jace myself even more than I like casting a [Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command), which is quite a bit indeed. But it was definitely a priority of ours to give other colors something they could do at the four-slot that was at least not *embarrassing* when staring down our favorite shoulder-bullseyed blue-haired Anime extra. 


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature129_3cards1.jpg)  
Want to protect that Jace with a bunch of [Squadron Hawk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk)s (ca-CAW!!!!) and [Wall of Omens](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Wall%2Bof%2BOmens)? Get out! Want to protect it with a flurry of [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak)s and [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade)s? Sorry brah! Hope that a blocker or two will keep him alive until you untap? Cool story, bro, but I'm attacking with like thirty creatures, and they're all *huge*. 


Alright, alright, I'll settle down and brush my shoulders off. Give me a break—I heard the words "Draw Cards," "[Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command)," and "[Squadron Hawk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk)" in the same sentence, and thought I'd died and gone to Heaven! 


In general, though, we wanted to do a little more than ensure Jace wasn't just winning every *heads-up* fistfight. We tried to give control decks somewhat fewer cards—though, if you happen to be listening to a certain [Black Sun's Zenith](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Black%2BSun%2527s%2BZenith) song you might disagree with me—and amp up the power of creature decks with spells like [Accorder Paladin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Accorder+Paladin), [Contested War Zone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Contested+War+Zone), and [Lead the Stampede](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lead+the+Stampede). 


### The Rest


I've talked a lot about the intricate, technical things that Development pursues in order to make **Magic** the best game on Earth. As I mentioned before, though, at the end of the day it's important for every type of player to have something cool that speaks to them. To that end, we're hoping any number of jaw-dropping "Can't-be-real"-s like [Blightsteel Colossus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightsteel+Colossus), "Well-now-what-can-we-do-with-this-anyway"-s like [Mitotic Manipulation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mitotic+Manipulation), or even straightforward "Why hasn't this been printed yet"-s like [Crush](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crush) help create the resonant, fun, identity-affirming experience we crave in a game of **Magic: The Gathering**. Being on a **Magic** Development team was something of a dream for me—and, by the end of the process, it had certainly lived up to my expectations. As artists, we're all in the business of creating experiences that connect people to one another and to themselves. I hope we've done our job!


[![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/twtw/twtw128_paris.jpg)](http://www.wizards.com/Magic/tcg/events.aspx?x=mtg/event/magicweekend/paris11)  







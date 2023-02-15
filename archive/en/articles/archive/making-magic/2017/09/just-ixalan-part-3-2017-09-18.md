
---
[Link to Wayback Machine](https://web.archive.org/web/20170918160036/https://magic.wizards.com/en/articles/archive/making-magic/just-ixalan-part-3-2017-09-18)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark completes his look at the full story of Ixalan's design and development."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1202631"
[_metadata_:publish_date]:- "2017-09-18"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Just for Ix(alan), Part 3"
[_metadata_:wayback_capture_timestamp]:- "2017-09-18 16:00:36"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170918160036id_/https://magic.wizards.com/en/articles/archive/making-magic/just-ixalan-part-3-2017-09-18"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/just-ixalan-part-3-2017-09-18"
---


Just for Ix(alan), Part 3
=========================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on September 18, 2017 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Welcome back! I've been using these weeks to tell the full story of *Ixalan*'s design and development. (You can see Part 1 [here](https://magic.wizards.com/en/articles/archive/making-magic/just-ixalan-part-1-2017-09-04) and Part 2 [here](https://magic.wizards.com/en/articles/archive/making-magic/just-ixalan-part-2-2017-09-11); today's column assumes you've already read the last two columns.) I'm not quite done with the story yet, though. When last we left, Ken Nagle (he and I were the co-design leads of *Ixalan*) had just turned over the design file to development, so that's where I'm going to start today.


*Ixalan* Development
====================


When the file was handed over, the state of the various mechanics was as follows:


**Explore** – Ken had messed around with "land-trips," a rider on spells that let you look at the top of your library and keep it if it was a land. Design team member Mark Gottlieb convinced Ken to tweak and keyword it. The tweak was to put the ability only on creatures and then add a +1/+1 counter as an alternate reward if the top card wasn't a land. It also allowed you to put the nonland card either on top or bottom of your library. Development would redesign most of the cards that used the mechanic, but how it functioned didn't change much during the process. (The mechanic was the top-rated mechanic for one of our internal polls.) Explore runs through all five colors and all four tribes; there are thirteen creatures that explore and three cards that care about creatures exploring.


**Crew** – When we made *Kaladesh*, we were so happy with Vehicles that we decided to make them evergreen and put some into *Amonkhet*. For example, the barge that carries the worthy dead from the Trials through the [Gate to the Afterlife](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gate+to+the+Afterlife) was originally a Vehicle. We eventually realized that we had a lot going on mechanically in *Amonkhet* and decided that we should make Vehicles deciduous rather than evergreen. If a set really needed Vehicles, it could have them, but we recognized that there was a cost to using them and thus, they shouldn't be something we use every set. Once we knew we were doing Pirates, it became clear that we wanted pirate ships, so Vehicles were added pretty early in design and never left. The one change that was made in development (due to a lot of feedback from *Kaladesh* block) was a global R&D decision that Vehicles are complex enough that we no longer wanted to do them at common (*Ixalan* has two uncommon Vehicles and three rare ones).


**Transform** – We also latched early on in design to using double-faced cards where the front side was a flavorful nod to exploration and the back side was a land representing the location discovered. The individual card designs went through many, many changes, but the basic concept stayed throughout design and development.


**A Pirate Mechanic** – Design knew it wanted a mechanic dedicated to the Pirates and had explored a bunch of different options, but at the time of the handoff, design hadn't found one they liked.


**A Dinosaur Mechanic** – Likewise, design wanted a mechanic dedicated to just the Dinosaurs, but none of the ones they'd played with seemed like the right execution.


**A Vampire Mechanic Theme and Merfolk Mechanical Theme** – To keep the number of keyword mechanics down, we decided to only give one to the two three-color tribes. The two-color tribes would have a mechanical theme, just not one that required a keyword. I'll talk more about the exploration of each of these tribes when I get to them below.


**The Tribes** – Design knew pretty early on that *Ixalan* was going to be a tribal set, but what exactly the tribes were going to be and what colors they were going to be in went through a number of changes. By the time of the handoff, though, we had settled on the creature types and their colors:


* Pirates (blue-black-red)
* Dinosaurs (red-green-white)
* Vampires (white-black)
* Merfolk (green-blue)

How exactly they were going to play and what exactly their mechanical themes were was still in flux.


Sam Stoddard was the lead developer for *Ixalan*. He and his development team had a lot of things to figure out. As *Ixalan* revolved around the four tribes, I'm going to walk through development using the lens of how each tribe evolved.


Pirates (Blue-Black-Red)
========================


The goal of this tribe was pretty straightforward. Make the Pirates feel like Pirates. *Mercadian Masques* had a tiny Pirate theme in blue back in the day, and a few creatures, mostly retroactively, had a Pirate creature type. But much like Werewolves at the time of *Innistrad*, Pirates were a resonant trope that *Magic* had never properly captured on cards, so the goal of this tribe was to deliver strong, resonant flavor.


We spent a lot of time in design talking about what this meant exactly. We knew the tribe wanted to be sneaky and underhanded. We knew attacking had to matter. We knew that they weren't going to be particularly large. We'd made a lot of cool individual cards, but we'd yet to stumble upon the right mechanic. As I talked about last week, we spent a bunch of time with a mechanic called plunder that acted as a rider on creatures, allowing you to loot if you'd previously dealt combat damage that turn—a tweak on the bloodthirst mechanic that originally appeared as the Gruul mechanic in *Guildpact*.


Development continued searching to find the perfect Pirate mechanic. They agreed that design had been searching in the right place, so they started by continuing the keyword search where design had left off. The solution to the problem ended up being what I call a "Daryl Hannah moment."


Let me explain. Back in the late '80s, actress Daryl Hannah had mentioned to her agent that she had always been interested in being in a Woody Allen film. It came to her agent's attention a few years later that Woody Allen was casting the film *Crimes and Misdemeanors*, and one of the parts was described as a "Daryl Hannah type." Well, who better to play a Daryl Hannah type than Daryl Hannah? She obviously got the part.



![Deadeye Tormentor](https://media.wizards.com/2017/images/daily/cardart_XLN_Deadeye-Tormentor.jpg)Deadeye Tormentor | Art by [Eric Deschamps](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5b%22Eric+Deschamps%22%5d)
One of the things we often do when looking for a new mechanic is identify an existing mechanic that we feel hits the right spot to help give everyone a sense of what we're looking for. Throughout our search for a Pirate mechanic, we kept saying we wanted a "raid-like mechanic." Well, what better to fill the spot of a raid-like mechanic than raid? It just took one person in a development meeting to utter this aloud to get the development team to just try using raid. It obviously got the part.


Once the development team had the mechanic, the next step was to figure out just what type of effects Pirates needed to have. This would also shape how each of the three two-color combinations would play mechanically. Before I get to the individual effects, let me first talk about another mechanical thread that runs through Pirates: Treasure.


As a three-color tribe, the Pirates needed some support to enable three-color play. Gold tokens (artifact tokens that you can sacrifice for any color of mana, first seen on two *Theros* block cards) seemed like a flavorful answer. Pirates are always seeking out treasure, so it seemed like a great fit. Unfortunately, playtesting showed that Gold tokens were too good with the *Aether Revolt* mechanic improvise as it essentially let each one produce two mana of any color. The development team added a tap to the activation to prevent this interaction and renamed the tokens to Treasure.


Now let's talk about each of the two-color combination of Pirates:


**Blue-Black** – Between their love of Pirate ships, weapons, and treasure, there was a decent amount of synergy between Pirates and artifacts. Development played this aspect up in blue-black. It also allowed blue and black aspects to things like counterspelling, discard, and card drawing to help this combination be a bit more controlling. This combination plays up the Pirates' craftiness.


**Firebreathing**


*n*. shorthand for "R: This creature gets +1/+0 until end of turn."


There are other variations, such as paying more than R for a bigger effect, but +1/+0 is the purest form of firebreathing. The name is derived from [Firebreathing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firebreathing), an Aura first printed in *Limited Edition (Alpha)* that grants this ability to a creature.


**Black-Red** – This is the most aggressive two-color combination. It makes use of things like firebreathing, temporary creature stealing, creature/permanent removal, and the raid mechanic to hit the opponent fast and furiously. This combination plays up the Pirates' ruthlessness.


**Blue-Red** – This is the tempo version of Pirates. It makes use of evasion, card sifting, creature tapping, counterspells, and a stream of creatures to constantly keep the opponent off balance. This combination plays up the Pirates' trickiness.


Design and development also worked with the creative team to create creature types for the Pirates. Humans appear in all three colors. Orcs show up in black and red. Goblins show up in just red. And Sirens show up in just blue (they were the choice to represent the blue Pirate fliers).


Dinosaurs (Red-Green-White)
===========================


Development cracked the Pirate mechanic relatively early in the process. The Dinosaur mechanic though took a lot longer, mostly because it was a trickier target to hit. The Pirates wanted to be sneaky and attack, usually with small to medium bodies. Well, normal *Magic* does that in volume. The Dinosaurs, in contrast, wanted to be big, scary monsters that had a large impact on the game. There's just not as much of that in a typical set. That meant the Dinosaur mechanic had to enable big bruisers without requiring it.


This was a similar problem we had when we did *Dragons of Tarkir* where we needed to have a lot of Dragons. Luckily, Dinosaurs had two advantages over Dragons. One, they come in more shapes and sizes. Yes, there were giant Dinosaurs, but there also were small ones. Second, while a few flying Dinosaurs existed (yes, we know the real-world fliers were technically not dinosaurs) they were mostly ground creatures. These two things together helped immensely.


The development team played around with mechanics in the monstrosity space (from *Theros*) where creatures could be upgraded once into larger creatures. They experimented with mechanics that kept smaller things from blocking them and cheaper spells from affecting them. They tried making a mechanic similar to the Phantom mechanic (from *Judgment*) where creatures entered with +1/+1 counters and then would lose a counter in place of dying. But none of them quite fit what Dinosaurs needed. They were too clever or too limited in design space or just didn't capture the Dinosaur feel the team was looking for.


The solution to the problem was solved in hole filling by a man named John Stone. What if the power of the Dinosaurs was that they didn't like being damaged? The mechanic, called enrage, triggers whenever the Dinosaur takes damage, which could happen in combat or when a spell or effect damages it. This makes Dinosaurs more challenging to deal with in combat and more troublesome to kill with damage. It also allows the Dinosaur's controller to damage their own Dinosaur with a small enough amount that it doesn't die but still generates the effect.



![Ranging Raptors](https://media.wizards.com/2017/images/daily/cardart_XLN_Ranging-Raptors.jpg)Ranging Raptors | Art by [Simon Dominic](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5b%22Simon+Dominic%22%5d)
Interestingly, the exact same mechanic had been created a month earlier in the design of a future set, but neither John nor the *Ixalan* development team was aware of it. When enrage proved to be a perfect fit for the Dinosaurs, the future set had to give the mechanic up. (The rule in R&D is that earlier sets trump later sets for mechanics—obviously, the importance of a mechanic to the set it's in can override this.)


As with Pirates, the development team had to come up with a mechanical strategy for each of the two-color pairings:


**Red-Green** – This is the enrage combination. Green is the color with the most enrage effects (with red being number two), and red has the direct damage that can allow you to trigger your own enrage abilities. This combination was playing up the ferocity of the Dinosaurs.


**Green-White** – This is the combination that cares the most about toughness. Its Dinosaurs lean toward having higher toughness, allowing the deck to be more defensive. It then has effects that help use the toughness offensively, such as allowing creatures to deal damage equal to their toughness. This combination played up the size of the Dinosaurs.


**Red-White** – This is the aggro combination. It has the cheapest Dinosaurs, often with drawbacks to allow you to get bigger creatures for less mana. It's also the color combination that has the most aggressive abilities, often things that aid in combat. This combination played up the aggressiveness of the Dinosaurs.


The one other thing to remember about this tribe is that it's not just made up of Dinosaurs but also the many Humans that make up the Sun Empire. To capture the synergy between the people and the Dinosaurs, there are numerous cards that aren't Dinosaurs but get better when you control at least one Dinosaur. This is one of the main ways we're able to fill in a lot of the lower end of the creature curve in the deck.


Vampires (White-Black)
======================


Vampires are the one tribe that didn't shift at all during the course of design. The Vampires were always a tribe (in fact, as I explained two weeks ago, they were the original impetus for the world), and they started in white-black and ended in white-black. Between capturing the flavor of Vampires and finding overlap between white and black, the mechanical theme of the Vampires was never a mystery.


The Vampires are all about a resource and that resource is life. They can drain life, they can gain life, they can force life loss, they can use life as a resource to pay for things. The Vampires form a midrange deck that uses its life manipulations to be aggressive and plink away at the opponent's life total.


The other resource used by the Vampires is the making of Vampire tokens. They are white 1/1 creatures with lifelink. White tends to make them, and black finds different ways to use them. The Vampires tend to attack early and then sit back and whittle you down to 0 from afar in the mid to late game.


Merfolk (Green-Blue)
====================


The Merfolk were the opposite of the Vampires. They were a tribe that we didn't start with, and the green-blue faction was the one that went through the most changes through design and development. For a while, for example, this faction was the one with the Dinosaurs. By the time we got to development, though, this faction was locked down as Merfolk Shaman casting elemental magic.


Design had played around with a spellcasting-matters theme for this tribe, so in early development, Sam tried something radical. He gave the Merfolk prowess. Remember prowess is primary in blue, secondary in red, and tertiary in white. It's not in green, but Sam made a strong argument that the thing green would most care about in a spells-matter environment was getting its creatures bigger, which was exactly what prowess did, so for a while we tried prowess just on the Merfolk. In the end, it was a bit more complicated than we liked. We've learned over time that prowess is a mechanic that needs to show up in smaller numbers at common. Also, green prowess just felt weird.


The other problem the development team recognized was that focusing a tribal theme on noncreature cards leads to problems. You want to have a lot of creature cards of the tribe to pay off the synergy, but if the tribe requires a lot of noncreature cards, then you have this uncomfortable tension. In the end, the decision was made to shift the focus onto something more creature-centric, so development changed Merfolk to a +1/+1-counter theme. Green buffs up the Merfolk and blue either grants them evasion or helps remove the blockers.


There are a lot of smaller pieces to the design, but I'll hit that over the next few weeks as I start examining more micro-aspects of *Ixalan*.


Time to Explore
===============


And that, in just three short weeks, is the story of *Ixalan*'s design and development. It went through a lot of changes, significantly more than the average set, but it ended up in a pretty sweet place. I hope you all enjoyed these columns, and as always, I'm interested in your feedback. You can [email me](mailto:making.magic@hotmail.com) or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro)) and let me know what you think about both the preview columns and *Ixalan*. In particular, I'm curious what you think about each of the four factions.


Join me next week when I begin the *Ixalan* card-by-card design stories.


Until then, may you have fun exploring the world of Ixalan.




---



 

##### 
 #470: The Pit






##### 
 #470: The Pit


30:41



In this podcast, I talk about the history of the Pit—the area where R&D works.

 



 Play
[Download MP3 Format](http://media.wizards.com/2017/podcasts/magic/drivetowork470_thepit.mp3)






 

##### 
 #471: San Diego Comic-Con 2017






##### 
 #471: San Diego Comic-Con 2017


33:34



I attended another SDCC and had another Blogatog Live *Magic* panel where I talked for the first time about *Unstable*. In this podcast, I talk all about what happened, including a few tidbits about *Unstable* from the panel that didn't make it out to...

 



 Play
[Download MP3 Format](http://media.wizards.com/2017/podcasts/magic/drivetowork471_sdcc2017.mp3)




* [**Episode 469**](http://media.wizards.com/2017/podcasts/magic/drivetowork469_startingadesign.mp3) Starting a Design (25.2 MB)
* [**Episode 468**](http://media.wizards.com/2017/podcasts/magic/drivetowork468_poison.mp3) Poison (20.8 MB)
* [**Episode 467**](http://media.wizards.com/2017/podcasts/magic/drivetowork467_multicolorblocks.mp3) Multicolor Blocks (22.4 MB)








---
[Link to Wayback Machine](https://web.archive.org/web/20201112000309/https://magic.wizards.com/en/articles/archive/feature/commander-2017-edition-design-handoff-2017-08-23)

[_metadata_:author]:- "Gavin Verhey"
[_metadata_:description]:- "If you've ever wanted to see what a set looks like when a design team hands it over to development, here's your chance!"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:publish_date]:- "2017-08-23"
[_metadata_:title]:- "Commander (2017 Edition) Design Handoff"
[_metadata_:wayback_capture_timestamp]:- "2020-11-12 00:03:09+00:00"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201112000309id_/https://magic.wizards.com/en/articles/archive/feature/commander-2017-edition-design-handoff-2017-08-23"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/commander-2017-edition-design-handoff-2017-08-23"
---


Commander (2017 Edition) Design Handoff
=======================================



 Posted in **Feature**
 on August 23, 2017 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorPic_GavinVerhey.jpg)
By Gavin Verhey




 When Gavin Verhey was eleven, he dreamt of a job making Magic cards—and now as a Magic designer, he's living his dream! Gavin has been writing about Magic since 2005. 






*Have you ever heard the term "design handoff"? Perhaps you've seen Mark Rosewater mention it in his column, or it referred to offhand in a preview article. Whispered about in the corners of* Magic *design writing, it's something you never really see more than a glimpse of.*


*Until now.*


*Today, I have a real treat for you. Below is the* Commander (2017 Edition) *design handoff document. When I passed the set off to Bryan Hawley, the lead developer of* Commander 2017*, I gave him three things: the set file, the decklists, and this document. This was the guide the development team referred back to throughout the process. In it, you can see the end product of a design team. What was important to us? What rules did we set? What were we trying to accomplish?*


*It's all in here.*


In boxes like this one, you'll find comments by me, 2017 Gavin (as opposed to 2016 Gavin).


*Below is what I sent and presented to Bryan Hawley and his team on March 14, 2016, with some minor edits for grammatical and visual clarity. All the art you see has been added purely to break up the text a bit; it wasn't included in the original handoff. The commentary boxes you'll see off to the right (like the one here) will contain notes and explanations of terms to provide context without necessitating further changes to the original text.*


*Enjoy this look inside the process of how we make a set!*


*Gavin Verhey*  
[@GavinVerhey](http://www.twitter.com/gavinverhey)  
[GavInsight](http://www.gavinverhey.tumblr.com/)




---

***Commander (2017 Edition)* Design Handoff**
=============================================


*Commander 2017* – Tribal
=========================


Design Team:


Gavin Verhey (Lead)  

Kelly Digges  

Bryan Hawley  

Ben Hayes  

Mark Gottlieb  

Jules Robins


Drake set code: C17


R&D used to work in a system called Multiverse to catalog cards during design and development and leave comments on those cards. The system was upgraded in late 2015 to something new called Drake. It's pretty much the same thing, but better.


Deliverables: Four 100-card decks


**Index**


1. Introduction
	1. Design Topline
	2. Product Philosophy Overview
2. Pillars of Design
3. *Commander 2017* New Mechanics and Cycles
4. Deck Overview
	1. Cats – Mark Gottlieb
	2. Dragons – Ben Hayes and Bryan Hawley
	3. Vampires – Gavin Verhey
	4. Wizards – Jules Robins
5. Design Favorites

Introduction
============


**Design Topline** 


Choose a creature type and prepare to play Commander with something we've never done before: tribal-themed decks!


**Product Philosophy Overview** 


*Commander 2017* heralds a change in the *Commander* product line. Rather than being five decks all linked together by color (monocolor, four-color, etc.), this year we have moved down to four decks that are united by a theme. **That theme this year is tribal.** (Meaning a focus on specific creature types.)


This is the first time we have ever promoted tribal Commander decks, and while some people have certainly built around popular tribes before, the vast majority of Commander decks are not tribal. Furthermore, many tribes are short on cards necessary to build an entire Commander deck. This set provides a look at four tribes, and includes a multitude of cards that are flexible and can help build a tribal deck for your favorite tribe.


The creature types featured in the decks range from "So popular people were already building this kind of deck" to "There aren't enough cards to support this kind of deck, but I would love to play with one!" This serves as an intrigue point for players old and new: perhaps a new player gravitates toward Dragon tribal to give them a deck to start off with, where an experienced player who has seen that before gives Cat tribal a try because it's never really been possible before.


Blue-Black Wizards? Wait what? Where's the red?! The red was added during development. We had talked about it during design, but thought we could make it work with just blue and black. As development tuned the decks, they felt the deck really needed the red, so they added it in.


The four decks are:


* Green-White Cats
* Five-Color Dragons
* Red-White-Black Vampires
* Blue-Black Wizards

Additionally, this product gets about 60 new cards throughout the four decks. The file at handoff is over that number by twelve and is over intentionally to give development extra cards to play and experiment with.


Pillars of Design
=================


During design, we kept several goals forefront in our mind.


1. **Deliver on the Promise of Tribal *Commander* Decks**

Tribal is a theme players love and has been a staple of our mainline booster sets for ages. We have built entire blocks around tribal. We even named a card type after tribal. This is a big deal—and we expect players to be very excited about the chance to play tribal decks in Commander.


A few key elements to this:


* **Each deck should care about the creature type the deck is built around.** It isn't just about having some Dragons in your Dragon deck; you should have some cards that specifically reward you for having Dragons.
* **You should win because of your creature type** **(or what your creature type enables).** It's a miss if you're playing the Vampire deck, but then end up winning with a bunch of Demons. Winning with elements that were generated from your tribal creatures is fine (such as your Wizards enabling you to reanimate a huge creature, or your Vampires' lifelink turning on [Sanguine Bond](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sanguine+Bond)), but your creatures should be instrumental in your victory.
* **Your deck should be all creatures of your type except in rare exceptions.** With the exception of not-on-tribe creatures that help out your tribe (for example, [Dragonspeaker Shaman](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragonspeaker+Shaman) in the Dragon deck), the deck should be composed entirely of creatures of the appropriate tribal type.
* **Each deck has one commander that is loudly about tribal.** This ensures every game you play with that commander automatically feels tribal. (More on this later in the document.)
1. **Include a Mix of Tribes that Appeals to a Wide Range of Players**

We like to make data-driven decisions whenever we can. However, it can be hard to get clean data sometimes, since it's hard to ask outside the building; we can't really scoop ourselves by asking the world, "Which tribes should we make for *Commander* in two years?" Mark's head-to-head series is one way for us to measure popularity, and we also do polls inside the building as well. In this case, I ran a survey of everybody who came to our internal *Commander 2015* release event. (Dragons were the most popular there as well, if you were curious.)


The Pit is the slang term for the place where R&D sits and works. It is called as such because we all have low cubicles, meaning it's an open space to encourage collaboration. And, most importantly, so that we can call whoever our director is (Aaron Forsythe) "the [Lord of the Pit](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+the+Pit)."


Our first goal in design was trying to determine which tribes our four decks should include. We gathered a lot of feedback on this, from internal polls at the *Commander (2015 Edition)* release event to external polls in the form of Mark Rosewater's head-to-head to asking around the pit.


We wanted to hit a wide range of players here. So the goals we set were:


* To have at least one established tribe players already know and love (Dragons, Vampires);
* To have at least one new tribe that hasn't been strongly supported before and will catch people's attention (Cats);
* To have at least one tribe that appeals to extremely casual players (Dragons, Vampires);
* To have at least one tribe that appeals to enfranchised players in either uniqueness or play style (Wizards, Cats);
* To have at least one tribe that people who prefer tricky, slower decks will identify as something for them (Wizards); and
* To have a good color balance between the decks.

After a lot of discussion, we reached the current mix. This satisfies all our goals, while making for good gameplay.


1. **Create Cards That Can Support Other Tribal Decks**

In a perfect world, to maximize appeal, a tribal *Commander* release would support every creature type players could possibly want. However, with four decks, we really only have the opportunity to showcase four tribes. This is a tricky problem to solve for.


The solution: with careful design, we can release pieces that allow players to build a tribal deck for their favorite tribe. The decks contain a number of cards that let you choose a creature type on resolution and reward you for playing a lot of that type.


Inside their *Commander* deck, of course you'll always choose Cat, Dragon, Vampire, or Wizard as appropriate, but their flexibility allows you to add them into your Goblin, Angel, Construct, Spider, or whatever other deck you want to build. We expect these cards to not only be popular in Commander, but in all casual formats as a way to help build your favorite tribal deck.



![Kindred Discovery](https://media.wizards.com/2017/images/daily/cardart_C17_Kindred-Discovery.jpg)[Kindred Discovery](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindred+Discovery) | Art by [Lake Hurwitz](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Lake+Hurwitz%22%5d)
1. **Still Attract Players Who Aren't Interested in Tribal**

Development later gave the Dragons deck an official "ramp" subtheme—which was really there all along anyway.


While tribal is the key focus of these *Commander* decks, and it is very popular, we don't want that focus to exclude of every other kind of Commander player. We worked hard to make sure these decks could still appeal to people who don't care as much for tribal.


* Each deck, with the exception of Dragons, features a subtheme in addition to its main tribal theme. There is also a commander that matches this theme in the product. So if you don't want to play tribal, you can play the subtheme commander and have fun focusing on a different element.
* Exciting characters from our story showing up in Commander has really helped drive excitement in the past, and some of our best designs have come from melding together flavor and function. We worked closely with creative to create cards for several characters people have been asking for.
* For part of design, we focused on making individual cool cards that could go into cubes or other Commander decks.
* Similarly, we also made several cards and mechanics that are specifically geared toward multiplayer, which still play well in Commander regardless of the tribe you choose.
* The Wizard deck is partially attempting to be a less tribal deck. It still has a tribal component, but it has a lot of tricky spell interactions as well to keep the player who prefers that kind of gameplay satisfied.
1. **Play Well in the *Commander 2017* Biodome**

The way many people experience Commander is to buy the current on-sale decks and play them against each other, almost like a board-game experience. It's important that these decks play well against each other and create an interesting metagame.


To this end, we attempted to make it so that the decks are all relatively balanced and that they have themes that enable them to be good at different points in the game. For example, the Vampires tend to shine early, whereas Dragons tend to dominate the midgame and Wizards want to survive until the end game.


1. **Help Tribal Be Resilient Outside of the Biodome**

Once you take these decks into the Commander field at large, you're kind of in the Wild West; one thing that was important to us was that you didn't feel silly for playing tribal against the Commander field at large. Here are some steps we took to try and help with this:


* Many Commander decks feature board sweepers, and those are naturally strong against creature-heavy decks. These decks feature some rewards such as enchantments that stay on the battlefield even through sweepers to help keep your tribal engine rolling.
* In Commander, giving +1/+1 to your creatures (a typical "lord" bonus) is often less impressive than granting them a keyword or some kind of special bonus. We focused many of our tribal cards on enhancing creatures in ways other than just stat bonuses.
* Having powerful rewards that don't require a ton creatures to be good. You shouldn't have to have eight Wizards in play before they start doing good things for you. Some tribal cards that can be strong if you have just a couple other creatures of the appropriate type in play are important.
1. **Have Something New and Flashy—That's Also Tied into Creatures and Tribal**

**Key Selling Point**


The key selling point, or KSP, is the awesome new thing that makes you really excited!


*Commander* products tend to have something mechanically new and exciting—a KSP that draws your interest, like planeswalker commanders, partner, or otherwise.


After a lot of iteration, the team is thrilled to have the coach mechanic, an ability that highlights the tribal themes while also doing something pretty exciting: functioning from the command zone! More on this in the coach section, but having a KSP like this was important to our team.


And speaking of the coach section . . .


*Commander 2017* New Mechanics and Cycles
=========================================


We tried many new mechanics for *Commander 2017*, and after a lot of iteration are passing off three of them to development: one to appear on commanders and two to appear on non-commanders.


**Coach**


At this stage in the process, cards and mechanics aren't anywhere close to having real names yet. So, we use playtest names. Coach was the playtest name for eminence. Get in there, coach!


Coach appears only on legendary commanders. Here's an example of coach text from the Dragon deck:


*Coach* – As long as CARDNAME is on the battlefield or in your command zone, other Dragons you cast cost 1 less to cast.


All coach abilities enhance creatures of your tribe. There are a number of great things this mechanic does, both for the product and in gameplay. Three big ones are:


* **It puts tribal front and center.** All coach abilities make your creatures of that tribe better. Tying the KSP into something tribal that can go on the front of the box and loudly say "This is about Vampires!" helps the product feel tribal from the get-go.
* **It creates inherent tribal gameplay.** Every game with a coach commander is going to feel tribal because you are benefitting from having cards of a single tribe.
* **It helps the tribes be competitive.** When you are building a 99-card singleton deck and focusing on a tribe, you're going to end up with a couple cards that are a tad below the line of what you would prefer to play. However, the coaches help enhance their tribes to pull individual cards up above that bar. For example, Dragons that may have been slightly too weak for Commander are now attractive at one mana less.

A passive ability like this that works from the command zone has only ever shown up on one other card: [Oloro, Ageless Ascetic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oloro%2C+Ageless+Ascetic). Oloro is very powerful, and we are not keen to make a bunch more Oloros.


However, this plays very different from Oloro. The key difference is this: Oloro works in any deck from the command zone, and provides something that increments a number in an uninteractive way rather than affecting cards you play. Coach, on the other hand, affects cards you cast—meaning you can interact with them—and forces you to build a deck that works with it instead of working in any deck. These are major differences that make coach play very differently from Oloro.



![Edgar Markov](https://media.wizards.com/2017/images/daily/cardart_C17_Edgar-Markov.jpg)[Edgar Markov](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Edgar+Markov) | Art by [Volkan Baga](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Volkan+Baga%22%5d)
I expect coach to be popular and for a very common request to be "Please make a coach for tribe X or a generic coach any tribe could use." We did briefly talk about trying to make a generic coach, but designing that so it could both fit in any color and provided a benefit that didn't break with a specific tribe proved troublesome. If you think this is worth pursuing, feel free to experiment in development.


**Buddy System**


The goal of these cards from Mark Gottlieb was to help make multiplayer politics and allegiances matter. They eventually morphed into [the five new Curses](http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&set=+%5b%22Commander%202017%22%5d&name=+%5b%22Curse%22%5d), which was a great call on Bryan's part that accomplishes the goals with much cleaner cards. This is just one example of how design provides the general picture of what it's looking for, and then development finds another, better way to meet those goals that leaves everybody happy.


Buddy system and the mechanic I'll talk about next, vendetta, are cool multiplayer mechanics that are entirely context-independent from tribal. It is my expectation that only one of these will survive as a keyword and the other will have some number of cards (from one to five) remain in the decks without using a keyword to call them out.


Buddy system cards are beneficial enchantments that you can use politically. Here's an example card with buddy system:


Buddy system *(When this enchantment enters the battlefield or at the beginning of your upkeep, target opponent becomes your buddy until your next turn.)*  

At the beginning of your draw step and your buddy's draw step, that player draws an additional card.


You always receive the bonus, and each turn you can pick someone else to receive it, too. Here's what we found was important about this mechanic:


* **Buddy system encourages fun politics.** Picking a buddy is enjoyable, and having the power to share it around can provide a minor political reward to encourage people to attack other places. At the same time, the reward isn't so tremendous that people feel horribly slighted for not being chosen as a buddy. I generally hate political gameplay, and I enjoyed buddy system.
* **It is important that you can switch.** Part of the fun is being able to move around your buddy as things happen in the game.
* **It is important that you choose your buddy ahead of time.** A natural thing to do is to strip off words and just say that on your upkeep you and target player each draw a card. However, when we tried this, suddenly it felt very different. Instead of making deals with people about the future and feeling like you were in some kind of pact, removing that whole aspect, though a very subtle change, drastically modified how they played.

We have played with buddy system a lot and enjoyed the mechanic. It has very limited design space and is multiplayer friendly, making it a good fit for *Commander*. It is worth noting that the black one has been very difficult to find a good design for, and I encourage development to look at all the effects and see what works best where.


**Vendetta**


Vendetta is a unique mechanic that plays around in space we don't often touch. With vendetta cards, you secretly choose a player, and then when that player tries to wrong you in some way, you can reveal the vendetta and harm them for going after you.


An example card from the file:


Vendetta *(As this creature enters the battlefield, secretly choose an opponent. You may reveal the choice at any time.)*  

When you reveal the chosen player, destroy target creature that player controls if it is attacking you.


This mechanic, also from Mark Gottlieb, survived on one card in the set: [Stalking Leonin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stalking+Leonin). It was ultimately extremely difficult to make a full cycle of and was most fun in small doses. We only had two designs we really liked, and doing one let us make our favorite design for it instead of making two good designs and three mediocre ones. I do hope to see the other one show up someday.


This has been a ton of fun in gameplay. Here's some of what it does that we like:


* **It creates a minigame.** Who did you choose? Is it safe to attack them? It causes a lot of table talk and fun moments.
* **It is very satisfying and fun.** Revealing the name you wrote down is just a good feeling; you get to feel like you "got" someone.
* **It does a good job of rattlesnaking your opponents**. Many of these decks are attack-heavy, and so having a couple cards that deterrent people and redirect attacks to other players is exciting.

**Rattlesnake**


*n*. A card or effect that discourages an opponent from attacking you or engaging with you in a way that would be detrimental to you, often by promising a disproportionate retaliation or response (e.g., [Karmic Justice](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karmic+Justice), [No Mercy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=No+Mercy), and [Teysa, Envoy of Ghosts](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teysa%2C+Envoy+of+Ghosts))


One of the major challenges with vendetta is that it has very limited design space. It is also a bit wordy. However, to squeeze out five cards for a *Commander* set is entirely reasonable. Whether it is a named mechanic or not, I hope some number of these cards make it into the final set—they are a blast to play.


 


**Cycles**


No, not the mechanic. In R&D slang, a "cycle" means a group of cards, usually one of each color, that all have some thematic or functional tie together.


In addition to the keyword mechanics, which cycle out throughout the decks, there are two cycles that appear throughout the decks as well. These are the "protector" creatures and the "kindred" spells.


**The Protector Creatures**


The protector cycle is expanding on the card [Bastion Protector](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bastion+Protector), which originally appeared in *Commander (2015 Edition)*. It is a creature that reads, "Commander creatures you control get +2/+2 and have indestructible."


This was a suggestion from Jules Robins originally. One of these ended up surviving, in the form of [Bloodsworn Steward](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodsworn+Steward). Instead of doing all four more here, Bryan thought it smart to launch one more and see how the reaction was to doing more of these. If you enjoy this one, perhaps you'll see more like it in the future.


We thought this was a cool, baseline appealing effect, so we expanded it out. **Each deck has one protector that grants +2/+2 and a keyword.** We intentionally did not make a white one because it already exists.


The protectors are not integral to *Commander 2017*, but are nice, appealing cards to Commander players of all kinds—which are important for us to have given the linear tribal theme. Additionally, they play extremely well with the partner commanders from *Commander (2016 Edition)*. This gives people who are still playing with the partners from the year before a good reason to pick up these commander decks.


**The Kindred Spells**


Commander products traditionally have a spell cycle. Ours is attached to tribal, in the form of the kindred spells. **These are expensive spells that allow you to choose a tribe (helping you build whatever tribe you want to good effect) and give you a massive reward for it.** 


Similar to the protectors, these are not integral to the design as-is. However, I believe the set would like to have both a spell cycle and some big cards that can reward any tribe, and this is an excellent way to marry the two.


**Cycle Philosophy**


With the shift to four decks, it poses the question of how we want to split up cards between the decks.


We are fine with decks getting uneven amounts of cycles—for example, in a five-card rare cycle, one deck can have two rares. **The one stake in the ground that is very important is that each color gets a card in a cycle.** Excluding blue, for example, leaves the player who wants access to that effect out in the cold, which is far from ideal.


Deck Overviews
==============


Each of the four decks was managed by one team member, with oversight and opinions from each other person on the team. It broke down like this:


**Cats** – Mark Gottlieb  
**Dragons** – Ben Hayes (Bryan Hawley toward the very end of design)  
**Vampires** – Gavin Verhey  
**Wizards** – Jules Robins


In each section, you'll find the new cards followed by the written thoughts of the team member who worked on that deck (in their own words).


These vary in length but provide the foremost thoughts about the person who owned that deck and worked thoroughly on it. The full decklists can be found separately in Drake. If you have any questions, it is recommended you contact the person who owned the deck—they are going to know best why or why not a specific card was included.


Let's get started with Cats!


![](https://media.wizards.com/2017/images/daily/FEAT20170823_Cats.jpg)


Cats – Mark Gottlieb
--------------------


**New Cards**


Here are all the new cards handed off for the Cat deck. I could tell you what they all turned into . . . but it sounds like a lot more fun to see how many you can figure out for each of these decks. I'll be watching for the Reddit thread!


* Ancestral Blade
* Buddy Buddies
* Buddy Growth
* Burly Protector
* Calico Librarian
* Cat o' Nine Tails
* Cops on the Take
* Darlo Manx, The Inscrutable
* Dragonhunter Nacatl
* Frisky Cat
* Hissing Watchcat
* Jedit Ojanen, Leader
* Kindred Birth
* Mirri, Crafty Duelist
* Ornate Courtyard
* Rapalzi, the Jagged Blade
* Send Home
* Territorial Tiger
* Vindictive Leonin
* Wasitora's Watchkeeper

**Designer Insights**


There are several themes in the Cat deck, which are as follows.


1. **Cat tribal**

There's only one legit Cat tribal reward that we've ever printed ([Raksha Golden Cub](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raksha+Golden+Cub)), but this is a tribal product. The deck is supplemented by nonspecific tribal rewards ([Door of Destinies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Door+of+Destinies)) and unique cards, including a commander that provides a tribal reward. This theme might still be a little light.


1. **Equipment**

The loudest, most consistent theme through the Cats we've printed is a connection to Equipment. They find them, they get better when equipped, they enable equipping, they protect artifacts, etc. The deck features a number of strong Equipment and a new commander that cares about Equipment. Note that there are plenty more Equipment-loving Cats that haven't made the cut.


1. **Go big!**

Synergizing with the Equipment theme, the primary play style for Cats is to build a gigantic creature that's hard to kill. This meshes with some +1/+1 counters, giant bonuses like [Door of Destinies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Door+of+Destinies) and [Collective Blessing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Blessing), and some huge six-drop Cats that already exist.


1. **Craftiness**

Cats protect themselves. Within existing Cats, there are mini-themes of indestructible ([Fleecemane Lion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fleecemane+Lion), [Temur Sabertooth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Temur+Sabertooth)), rescue ([Temur Sabertooth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Temur+Sabertooth), [Whitemane Lion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whitemane+Lion), [Fleetfoot Panther](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fleetfoot+Panther)), Phantoms ([Phantom Nishoba](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Nishoba), [Phantom Tiger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Tiger)), and protection ([Jareth, Leonine Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jareth%2C+Leonine+Titan)). They're crafty. Although the bounce doesn't work well with Equipment, it does allow for some combos, particularly with [enters-the-battlefield effects](http://magic.wizards.com/en/articles/archive/play-design/m-files-hour-devastation-part-1-2017-07-14#enters-the-battlefield-effects) (Dragonhunter Nacatl, [Taj-Nar Swordsmith](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Taj-Nar+Swordsmith)) and [Glare of Subdual](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glare+of+Subdual).


1. **Certain Kinds of Removal**

This color combination provides access to strong board sweepers and artifact/enchantment removal.


1. **Tokens**

Some themes work better than others. Development helps cull down to the best themes the deck has to offer. In this case, a lot of the go-wide tokens elements like [Collective Blessing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Blessing) and [Beastmaster Ascension](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beastmaster+Ascension) were removed to help in other areas of the deck.


Cats aren't a go-wide deck. But there are multiple token-makers among existing Cats, and some of them make a *lot* of tokens (one every turn, or a bunch at once). If those cards come up in a game, the deck can move that way as a change of pace. They're supported with cards like [Collective Blessing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Collective+Blessing) and [Beastmaster Ascension](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beastmaster+Ascension).


**Weaknesses of the Cat deck**


The Cat deck is weak at card draw and weak at flying defense. It can sometimes have a hard time breaking through a ground stall (particularly if its one big creature is chumped by tokens), but this hasn't often manifested in our games.


![](https://media.wizards.com/2017/images/daily/FEAT20170823_Dragons.jpg)


Dragons – Ben Hayes and Bryan Hawley
------------------------------------


**New Cards** 


* Buddy Brains
* Buddy Growth
* Build a Community
* Dragon Protector
* Dragonlords' Distribution
* Duck and Cover
* Haze, the Maelstrom Dragon
* Hidden Dragon
* Kindred Birth
* Ornate Courtyard
* Retribution Regent
* Taigam A
* The Ur-Dragon
* Treasure Dragon
* Vindictive Dracomancer
* Wasitora of the Nekoru
* Wasitora's Warder
* Wasitora's Watchkeeper

**Designer Insights**


At its core, this is a ramp deck that uses Dragons as ramp targets. Mana ramp is a powerful strategy in Commander, so as long as the deck stays in this space, I don't have any concerns that the deck will be satisfying and powerful.


Why would making a deck more powerful be bad? Well, remember, we want these decks to work fine against one another in the biodome. While you may be trying to make your deck as strong as possible, we're trying to make them balanced.


It's tempting to add big card drawing spells to this deck because that tends to combo well with mana ramp, but I think it's important to be disciplined with how much of this you add because overloading in this area can threaten to make this deck too much more powerful than the other decks and especially invalidate the Wizards deck.


This deck is a natural fit to have more board clears than the other decks. Board clears in healthy numbers are great for keeping things from getting too cluttered and stalled, but too many also runs the risk of stalling the game out through resource depletions.


I think it's important to include some defensive elements in this deck in addition to ramp and Dragons so that the Dragons player doesn't have to rely too heavily on just hoping people don't mess with them while they set up their game plan. I really like rattlesnake cards for these roles, such as [Soul Snare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Snare) and [Seal of Doom](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seal+of+Doom), as opposed to permanent deterrents like [Ghostly Prison](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghostly+Prison).


**This deck should be highly effective in the mid to late game but should not consistently outclass the Wizards deck in the late game.**


**![](https://media.wizards.com/2017/images/daily/FEAT20170823_Vampires.jpg)**


Vampires – Gavin Verhey
-----------------------


**New Cards**


* Aether Spasm
* Baron's Pridemate
* Blood Balancer
* Buddy Elementalism
* Coffin Protector
* Double-Edged Ward
* Edgar Markov
* Grudgebuilder
* Inciter of Action
* Jerk School
* Morkel, Essence Cultivator
* Ornate Courtyard
* Vampire Caterer
* Vampire Hooligan
* Vampire with Refined Tastes
* Van Sengirsing, Bounty Hunter
* Vanish in Smoke
* Visiting Vampire
* Wild Spellhowler

**Designer Insights**


Vampires play an important role in *Commander 2017*. Here are several notes on why Vampires were chosen and why the deck is built the way it is.


* **Vampires gets the ball rolling.** Out of all the decks, Vampires is the one that should feel the most aggressive. After all: they're Vampires! Vampires has some small creatures that ensure life totals start changing early on. However . . .
* **Vampires is a midrange deck.** We tried Vampires as an aggressive deck, and it just consistently fell short. Being an aggressive deck in Commander is perilous, and while Vampires is perhaps the most aggressive out of these four decks, it fits much more in the midrange camp. While its creatures are individually smaller than some of the other decks, it has a variety of powerful artifacts, enchantments, and synergies that help put it over the top.
* **Vampires has a life-gain subtheme.** Every deck (other than Dragons—Dragons doesn't need a subtheme) has a subtheme in addition to its tribal main theme. Cats have Equipment. Wizards have reanimation. Vampires have cards that synergize with gaining life. These range from effects like [Well of Lost Dreams](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Well+of+Lost+Dreams) to [Cradle of Vitality](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cradle+of+Vitality) and a couple new cards too. This works well because many Vampires have lifelink, and benefitting from taking others' life feels inherently vampiric.

At one point, the Vampire deck had three goad cards. Bryan did a great job of keeping the coolest effect around while chopping the less cool ones by sticking with the card that would eventually become [Disrupt Decorum](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disrupt+Decorum).


* **The Vampire deck plays around with goad.** Goad is a *Conspiracy: Take the Crown* mechanic, which happens to also play very well (although differently!) in Commander. The Vampire deck has a few goad cards, which have each been very fun. These are important because the deck can get a lot of heat on it early while it's poking through a bit of damage, and goad helps turn the focus elsewhere.
* **The Vampire deck can run out of gas.** Because it does focus more on the midgame, occasionally Vampires can become empty-handed when the game goes long. Ensuring it has some card-draw engines like [Underworld Connections](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Connections) or [Skeletal Scrying](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skeletal+Scrying) is important to make sure it can push through damage and be relevant late game. This is one of the deck's biggest weaknesses.
* **The Vampire deck should not be overly complex.** This should be a deck that you can play pretty straightforwardly. That's not to say the deck can't have complex interactions to learn, but when you pick it up out of the box, most of what's going on should make sense to you.

![](https://media.wizards.com/2017/images/daily/FEAT20170823_Wizards.jpg)


Wizards – Jules Robins
----------------------


**New Cards**


* Archmage of Darkness
* Broomstick Instructor
* Buddiest Banquet
* Buddiest Brains
* Cursecone Witch
* Dark Arts
* Grand Finalomancer
* Grudgebuilder
* Hall of Heritage
* Kindred Body
* Kindred Survival
* Magus of the Desire
* Necromantic Master
* Ornate Courtyard
* Rent-a-Warlock
* Runo Stromkirk, Reverent of Depths
* Taigam B
* Tenpkoshe, Lichmaker
* Vindictive Dracomancer

**Designer Insights**


At its core, the Wizard deck's identity rests on how it takes a unique approach to tribal for Commander. The deck isn't trying to leverage tribal synergies to steamroll an opponent, build an army, or do something huge and awe-inspiring. **Its goal is to use tribal as a means to be clever.**


Toward that end, the deck should avoid making or breaking the game on the back of one swingy card, but it should also avoid locking others out of the game. Ideally the deck lives in a state of anticipation, using tricky plays to make things turn out better for itself than its opponents anticipate and turning unfavorable situations on their heads. Its power should come from putting pieces together to result in big plays.


Speaking a bit more concretely, there are two interlocking essential pieces of the Wizard deck's feel:


* **Options**: The Wizard player should feel a sense of agency. Rather than having a prescribed sequence of plays, they should have multiple lines available. This is dangerous territory because different people can handle different levels of complexity in this kind of decision making, and we don't want to leave people feeling lost or making their opponents wait while they tank on which line to take.
* **Cleverness**: The Wizard player isn't looking to [Lava Axe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe) their opponent; they're looking to feel clever. They can do this either through mastering their cards (say, finding a cool little synergy between three of them) or mastering their opponents (say, figuring out when somebody's about to Wrath and holding back their best creature). We should give them opportunities to do both.

Design Favorites
================


Ben, Gavin, Jules, and Mark all submitted design favorites. Here are all the cards that received two or more votes for design favorite, along with reasons why they were chosen.


Sometimes at the end of design, a design team lead asks their team to list a small number of their favorite designs. This is to indicate to development what cards we liked the most and to try and preserve them and their goals if possible.


Aether Spasm (4 votes)  

2R  

Enchantment – Aura  

Enchant Creature  

Enchanted Creature has haste.  

At the beginning of enchanted creature's controller's upkeep, exile enchanted creature. Then that player reveals cards from the top of his or her library until he or she reveals a creature card. Put that card onto the battlefield and the rest on the bottom of their library in a random order. Attach CARDNAME to that creature.


**What We Liked About It**: It's a fun, top-down Timmy chaos card.




---

Vanish in Smoke (3 Votes)  

2W  

Instant  

Until your next turn, you gain protection from everything and your life total can't change. Exile all permanents you control. At the beginning of the player to your right's next end step, return them to the battlefield tapped.  

Exile CARDNAME.


**What We Liked About It**: Awesome top-down flavor, mixed with something Commander players love—"Don't mess with my stuff!"




---

Cursecone Witch (3 Votes)  

3BB  

Creature – Human Wizard  

2/4  

When CARDNAME dies, target opponent sacrifices a creature, up to one different target opponent discards 2 cards, and up to one different target opponent loses 3 life.


**What We Liked About It**: A nice rattlesnake card that can mete out punishment in exactingly cruel fashion. The specific effects aren't important here—hurting each of your opponent's in different ways is.




---

Visiting Vampire (3 Votes)  

3RR  

Creature – Vampire Warrior  

6/5  

Flying, haste  

CARDNAME attacks each turn if able.


At the beginning of your combat step, the player CARDNAME last dealt combat damage to chooses an opponent. CARDNAME attacks that player if able this turn.


**What We Liked About It**: It's a giant threat that keeps the game progressing in a political way. It's often unclear whether to kill it, and it takes some of the heat off the Vampire deck despite being a creature in the Vampire deck. "It's not my fault . . . really!"




---

Frisky Cat (3 Votes)  

2GW  

Creature – Cat  

3/3  

At the beginning of your end step, target opponent creates a 1/1 black Rat creature token with deathtouch.  

Cats you control have protection from Rats.  

Whenever a Rat dies, put a +1/+1 counter on target Cat.


Something Bryan brought up in development, and rightfully so, is that being multicolored really limits the decks your cards can go into. Bryan made this card a lot more awesome by turning it into a 1G 2/2—and by putting the counter on each Cat!


**What We Liked About It**: It's a home run! Not only is it politically interesting, not only does it give a tribal bonus, but it's also an incredibly adorable, great top-down card. "Cats you control have protection from Rats" is the next "Cowards can't block warriors."




---

Van Sengirsing, Bounty Hunter (3 Votes)  

WBR  

Creature – Vampire Advisor  

3/3  

First strike  

At the beginning of your end step, put a bounty counter on target creature an opponent controls.  

Whenever a creature with a bounty counter on it leaves the battlefield, each player other than its controller gains 2 life and draws a card.


**What We Liked About It**: It creates a fun minigame that helps everyone stay interested and maintains card flow for everyone. This was a favorite of outside-R&D playtesters, and it tells a fun story.




---

Inciter of Action (2 Votes)  

3R  

Creature – Vampire Warrior  

4/3  

At the beginning of each player's end step, CARDNAME deals 3 damage to that player if they don't control their commander.


**What We Liked About It**: It's got a unique line of text that incentivizes/punishes a unique aspect of the Commander format. It's a good way to fight those [Progenitus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Progenitus) players.




---

Dragonlords' Distribution (2 Votes)  

3WU  

Sorcery  

Exile target nonland permanent. Each player other than its controller creates a token that's a copy of that permanent.


**What We Liked About It**: Multiplayer fun for (almost) everyone! Not as fun-killing as "exile a permanent," not as one-sided as [Confiscate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confiscate), this card really shakes up the board. It's reminiscent of the unique play pattern of [Death by Dragons](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+by+Dragons).


We would love for these cards to be preserved in some way if possible, though if one or more of them need to go we understand.




---

That's all! Feel free to email me (or walk over to my desk) at any point if you have any questions at all. (And, once again, the people in charge of each deck are the best point for questions about strategy or designs for that deck.)


Have fun! I can't wait to play the final product.








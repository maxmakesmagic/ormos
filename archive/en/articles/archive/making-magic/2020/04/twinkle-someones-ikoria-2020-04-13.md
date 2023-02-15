
---
[Link to Wayback Machine](https://web.archive.org/web/20200416074839/https://magic.wizards.com/en/articles/archive/making-magic/twinkle-someones-ikoria-2020-04-13)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark's second Ikoria: Lair of Behemoths preview article steps away from mutate to discuss the set's other major mechanics and themes."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1497124"
[_metadata_:publish_date]:- "2020-04-13"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "A Twinkle in Someone's Ikoria"
[_metadata_:wayback_capture_timestamp]:- "2020-04-16 07:48:39"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200416074839id_/https://magic.wizards.com/en/articles/archive/making-magic/twinkle-someones-ikoria-2020-04-13"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/twinkle-someones-ikoria-2020-04-13"
---


A Twinkle in Someone's Ikoria
=============================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on April 13, 2020 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






[Last week](https://magic.wizards.com/en/articles/archive/making-magic/more-meets-ikoria-2020-04-06), I talked all about how the mutate mechanic came to be. This week I'll be discussing the creation of all the other major mechanics and themes from *Ikoria: Lair of Behemoths*. I have a lot to talk about, so let's get to it.


Keyword Counters
================


I started talking about keyword counters last week as they were part of the story of how the mutate mechanic was created, but they have their own design story that I wanted to touch on today.


![Punch-Out Counters](https://media.wizards.com/2020/images/daily/AKH_counters.png)


Ever since we'd done *Amonkhet* block with its punch-out cards, we were aware it was a tool that we could make use of again. In the R&D Hackathon on future design space, my mini team, which focused on "using other components," tested with keyword counters, and it was instantly clear that there was a lot of fun design space to play in. There were two big questions for the *Ikoria* Vision Design team. What keywords did we want to use? And how did we want to make use of them?


The low-hanging fruit that the Vision Design team first attempted was seeing if there were ten mechanics covering all ten two-color pairs. These were the evergreen mechanics we had at the time (sixteen in all, with each color that they were primary or secondary in):


* Deathtouch (black, green)
* Defender (all colors)
* Double strike (white, red)
* Flash (blue, black, green)
* Flying (white, blue, black)
* First strike (white, red)
* Haste (black, red, green)
* Hexproof (blue, green)
* Indestructible (white, green)
* Lifelink (white, black)
* Menace (black, red)
* Protection (white)
* Prowess (blue, red)
* Reach (red, green)
* Trample (red, green)
* Vigilance (white, green)

When you break it down by color combination, it looks like this:


* White-blue – defender, flying
* Blue-black – defender, flash
* Black-red – defender, haste, menace
* Red-green – defender, haste, reach, trample,
* Green-white – defender, vigilance, indestructible
* White-black – defender, lifelink
* Blue-red – defender, prowess
* Black-green – deathtouch, defender, flash
* Red-white – defender, double strike, first strike
* Green-blue – defender, flash, hexproof

The first problem is not all keywords were created equal when it comes to wanting to make keyword counters out of them. Defender was a downside mechanic which wasn't something you wanted to play on your own creatures. Flash couldn't be used at a time where it functioned, as cards in your hand can't have counters on them. Haste was of very limited use. Double strike and indestructible were a bit too powerful to be used, at least on commons. When you took away those keywords, you ended up with the following:


* White-blue – flying
* Blue-black – none
* Black-red – menace
* Red-green – reach, trample
* Green-white – vigilance
* White-black – lifelink
* Blue-red – prowess
* Black-green – deathtouch
* Red-white –first strike
* Green-blue – hexproof

Okay, we were close. Red-green had two keywords and blue-black had none. Also, prowess was a bit problematic as it was the only evergreen keyword that stacked, that is, it functionally mattered if you had two copies of the keyword counter. Our solution was to make a brand-new keyword for blue-black, something we thought could maybe one day become an evergreen mechanic. We called it "sneaky," and it had the following text: "This creature can't be blocked by creatures with power 3 or greater." There were also a few other ones we messed around with over the length of design: ward (*Once each turn, you may draw a card while this creature's the target of an opponent's spell or ability*), resistance (*This creature isn't a legal target of a spell or ability an opponent controls unless they pay {o2} as that spell or ability resolves)*, and camouflage (*As long as this is untapped, it can't be the target of spells or abilities your opponents control).*


Set Design played around with the keyword counters a bit and decided on three things. One, they got rid of sneaky and the other new keywords as they decided, for cleanliness and ease of comprehension, just to use mechanics players knew well. Two, they got rid of prowess as R&D had decided to stop making it evergreen. Three, they gave up on trying to find ten keywords that overlapped all the color combinations. They just used the remaining nine keywords and applied them to the colors they made sense in. (The *Ikoria* Commander decks have cards that make double strike and indestructible keyword counters.)


As for how to use the keyword counters, the Vision Design team (and later the Set Design team) came up with a number of uses:


![Helica Glider](https://media.wizards.com/2020/iko/en_T53em8nJnz.png)


**Modal enters-the-battlefield effects** – We make cards with modal choices all the time, but normally, you can't use keywords as it would create memory issues. Keyword counters solve that problem by having a reminder of what you chose. This let us make a common cycle of creatures where you choose one of two keywords as it enters the battlefield.


![Fully Grown](https://media.wizards.com/2020/iko/en_TMdGoiGhkZ.png)


**Permanent bonuses** – Another use is to combine a permanent effect with a temporary one. For example, green normally pumps power and toughness and often grants trample temporarily along with it. With keyword counters, we can take that effect and make the keyword granting permanent. So now, maybe I'm pickier about who I use the spell on because the trample will stick around. Whenever we would normally grant a keyword temporarily, in *Ikoria*, we instead granted it permanently.


![Frillscare Mentor](https://media.wizards.com/2020/iko/en_nsvsZmhqcL.png)


**Mentors** – Another advantage of keyword counters is that we can care about keywords mechanically in ways we often don't in normal sets. For example, uncommon has a cycle of cards with activated abilities that only work on creatures with a specific keyword. To allow the card to work by itself, we gave the creatures an enters-the-battlefield effect that puts the appropriate keyword counter on a creature, guaranteeing that you have at least one creature the ability works on. Thematically, we tied this cycle to the flavor of humans bonding with monsters. I'll be talking more about this theme and how we mechanically represent it on cards below.


![Luminous Broodmoth](https://media.wizards.com/2020/iko/en_G675QDWuXp.png)


**Using counters as a marker** – A common use for +1/+1 counters is a means to mark whether a creature has been the target of a certain effect. For instance, on the mechanics monstrosity and adapt, we use +1/+1 counters to show that they are monstrous or adapted. Keyword counters allow us to do that but flavored in different ways. Luminous Broodmoth, for example, wants only to bring back dead creatures once. Persist and undying did this using -1/-1 counters and +1/+1 counters respectively. Luminous Broodmoth gets to use flying counters, both of which have a different mechanical implication and give it a cool flavor.


![Avian Oddity](https://media.wizards.com/2020/iko/en_T4HOiGr7fx.png)


**Small incremental effects** – Another nice thing about keyword counters is that we can use keyword granting in smaller ways. Normally, granting just flying with an aura isn't enough to justify a whole card, but the keyword counter lets us use it as an effect which is part of a larger card. For instance, we were looking for small effects to put on a cycling trigger (I'll get to how cycling came back below), and we were able to make a cycle of uncommon creatures with cycling that all had a keyword allowing them to grant that keyword with a counter if you cycle the card.


![Vivien, Monsters' Advocate](https://media.wizards.com/2020/iko/en_ZRghg5xsF8.png)


**Increasing options of effects** – As keyword counters solve the memory issues of granting keywords permanently, they start allowing designers a bit more flexibility in their designs. Vivien, for example, wants to be making Beast creature tokens. In a normal set, they would have to all be the same so that you can remember what they do. Keyword counters change this up, allowing Vivien to have some option in what her Beasts do.


![Crystalline Giant](https://media.wizards.com/2020/iko/en_uR9RL2zGb5.png)


**Miscellaneous** – As we dove into exploring the design space of keyword counters, we found there were a lot of interesting nooks and crannies. We started mostly with the low-hanging fruit (as keyword counters can easily return one day), but there are a few designs like Crystalline Giant that we simply couldn't resist making.


I walked into design optimistic about keyword counters. I walked away even more optimistic. Their return is a when, not an if.


Companion
=========


![Lurrus of the Dream Den](https://media.wizards.com/2020/iko/en_ayrXu97mbX.png)![Lutri, the Spellchaser](https://media.wizards.com/2020/iko/en_GREFydXCLN.png)![Umori, the Collector](https://media.wizards.com/2020/iko/en_eLoI2F1pWb.png)


Keyword counters weren't the only thing to come out of the Hackathon. Dave Humpherys oversaw a mini team that was called "no gimmicks," which focused on new design space that used the cards as is (no new frames, no external components, etc.). One of their ideas was for a mechanic inspired by Commander. It was a card that sat outside of your deck that you could cast at any time but had the constraint that your deck needed to meet certain criteria. Dave had been interested in something that encouraged players to build their deck around some constraint, and this mechanic seemed like the cleanest execution. I liked the idea of the mechanic and felt it could be flavored as something that went on monsters. A key part of the vision for the set was that it was the monster set, and I wanted to make sure that every mechanic in it pushed toward the monster theme.


To make companion designs, the first thing we had to do was come up with deck-building constraints. We made a bunch but quickly realized there were several restrictions we had to be careful of:


**#1: It had to be verifiable.**


Let's say I'm playing against my opponent and they play a creature with companion. How do I know that their deck actually follows the constraints of that companion? We didn't want players to have to call a judge and have them verify the deck every time a companion got cast. What this meant was that the constraint had to be something straightforward and applied to the whole deck. A constraint like "half the nonland cards in the deck had to be all the same card type" wasn't verifiable. Saying "*all* the nonland cards in your deck had to be the same card type" was. This requirement is probably the thing that knocked out the most designs. I will note, there was one card, Lutri, the Spellchaser, that technically didn't follow this constraint, but not having any repeated cards felt like a thing people could grok easily enough that it was okay.


**#2: It had to be something you could build around.**


The constraint also had to lead to an interesting deck-building challenge that would result in fun, playable decks. All the cards having to have a converted mana cost of 5 is something verifiable, but is that something you could make a playable deck out of? Unlikely. This was another big barrier to designs.


**#3: It had to work in Limited (mostly).**


While this mechanic was designed to be more of a Constructed mechanic, we wanted it to be viable in Limited. Playtesting had shown drafting around one of these constraints was quite fun. During vision design, we had two cycles, one at uncommon and one at rare. The uncommons ended up having a little too much of an impact on Limited, so Set Design moved them to rare. All of our companion designs are possible in Limited, although a few require you to be a bit lucky to actually pull off.


These constraints did make it challenging to find enough designs, but between Vision Design and Set Design, we found ten designs that we liked (and for a while, there was a colorless eleventh one). The next big challenge was designing the creatures themselves. We wanted them to be something that you wanted to play, enough to encourage you to build the deck, but not so good that they created repetitive game states. Finding the sweet spot between them playing with the deck constraint while not being too overpowered or repetitive took a lot of work from Set Design and Play Design.


There were two other changes made during set design. One, during vision design, we let you play multiple companions if your deck met the constraints of all your companion cards, but later, playtesting showed that it was a bit overpowering to have multiple cards you could play at any time, so the mechanic was changed so that you could only have one. Two, Set Design decided to make the whole ten-card cycle hybrid to increase the decks that could use the companion cards. I'm happy with how they turned out and excited to see what decks you are all able to build with them.


Cycling
=======


One of the things we always look for in our sets are returning mechanics that can play into the theme of the set. *Ikoria* had a monster theme. What would play well with that? Also, we were eager for a mechanic that would allow players to do something with their excess mana. This type of mechanic allows players to play a bit more land to ensure they make their early land drops and gives them something to do with their mana later in the game. Was there a mechanic that could meet both criteria? The obvious choice was monstrosity. Just one small problem—we had recently tweaked monstrosity and redone it as adapt in *Ravnica Allegiance*, a set still in Standard with *Ikoria*.


After exploring other options, we settled on cycling. It helps you get mana in the early game and allows you to play additional large monsters in your deck because you can cycle them away if you can't cast them. Here are the different ways we made use of cycling:


![Easy Prey](https://media.wizards.com/2020/iko/en_zVIsReLzm5.png)


**Narrow cards** – Some cards have a very specific function that is useful, but only some of the time. These cards are usually fun cards to play but often don't make the cut because they have the risk of being a dead card in your hand too much of the time. Cycling fixes this by allowing you to cycle them away for a different card if currently you can't use them.


![Ominous Seas](https://media.wizards.com/2020/iko/en_vor968yXQq.png)


**Self-synergistic** – These are cards where the card having cycling helps the card function better. For example, take Ominous Seas. It wants to go into a deck where you have a lot of card drawing. Putting cycling on it means that once you've cast the first one, you can cycle future copies to generate foreshadow counters.


![Indatha Crystal](https://media.wizards.com/2020/iko/en_zUs7kBr1wt.png)


**Card flow** – Cycling also goes well on general utility cards like mana-producing cards that you can cycle away when you no longer need the resource. There is both an uncommon cycle of mana rocks and a rare cycle of tri-lands with cycling (more on the latter below).


![Yidaro, Wandering Monster](https://media.wizards.com/2020/iko/en_YYU6m84TeU.png)


**Larger spells** – Another great use for cycling is large spells that you will often draw but be unable to cast. This lets you put more in your deck as you have a means to use them in the early game if needed.


![Shark Typhoon](https://media.wizards.com/2020/iko/en_TxiY4in8gd.png)


**Cycling effects** – Another thing you can do is have effects that happen when you cycle the card. Above, for example, I talked about the mentor cycle that grants creature keyword counters. I do want us to be careful with how much we do this as it's not our intent to make cycling feel too much like kicker, but a little bit is fine.


![Flourishing Fox](https://media.wizards.com/2020/iko/en_5bKJPqkG1o.png)


**Cycling build-arounds** – Finally, you can create cards that encourage you to build cycling decks. These cards all tend to have both cycling triggers and cycling on them so that other copies can help one another.


The Set Design and Play Design teams were a bit more aggressive with the cycling costs than we'd been in *Amonkhet* block, the last time we'd used the mechanic. You'll notice a number of cards cycle for 1. Also, other than on the cards that generate effects and thus need colored activations, all the cycling costs are generic mana.


Human and Non-Human Tribal
==========================


Another trope space of monster movies is the relationship between humans and monsters. (I talked about the history of Humans in *Magic* [two weeks ago](https://magic.wizards.com/en/articles/archive/making-magic/human-history-2020-03-30).) There are two basic relationships: adversaries and allies. *Ikoria* plays with both.


![General Kudro of Drannith](https://media.wizards.com/2020/iko/en_wSLpNAZQSm.png)


Adversaries
-----------


What would monster movies be without monsters rampaging through a city? You can't have monsters without having victims, and those victims tend be humans. Some of those humans then fight back, becoming threats to the monsters. The set plays into this aspect by having Human tribal, focused in white and black.


![Fight as One](https://media.wizards.com/2020/iko/en_dUXtmT9U1F.png)


Allies
------


Not every human, though, hates the monsters. Some bond with them. This relationship is played up through a Human and non-Human mechanical theme that runs through the set. These cards either require you to have one of each, a Human and a non-Human, or have an effect that can affect one of each, encouraging you to play both.


![Illuna, Apex of Wishes](https://media.wizards.com/2020/iko/en_67Bpl60YS6.png)


Three-Color Theme
=================


The final theme of the set is the result of us realizing a cool opportunity. We were making a monster-themed set with giant monsters. It was the last non-Core expansion before rotation in the fall. The sets rotating were all multicolor sets. This would be a golden opportunity to do a small three-color theme. This would boost up the Ravnica years' worth of cards for six months before they left Standard. As we've been saying, this is the year of Commander, and three-color themes are very synergistic with the format. We had the option of doing arcs (a color and its allies) or wedges (a color and its enemies). We chose to do wedges as Commander had more need for wedges due to some bias toward shards early in *Magic*'s life.


The mantra of the set was that *Ikoria* was a "monster set with a three-color theme" not a "three-color set with monsters." This was not a faction set. Other than a creature type for its monsters, the wedges weren't given any factioning. There's no keyword per faction and no larger philosophy tying them together. The set has no gold cards at common, three uncommon enemy color cycles, and three-color cards at rare and mythic rare. The idea is that you can draft enemy colors or wedge, similar to how *Khans of Tarkir* drafted. There are some ally color cards, but mostly in hybrid (there is one rare cycle).


The three-color theme did lead to two major splashy cycles:


![Ruinous Ultimatum](https://media.wizards.com/2020/iko/en_TPxc9iZ6jm.png)


**The Ultimatums** – In Vision Design, we made a list of every arc cycle that hadn't yet been done in wedge. The list wasn't actually that long, but one cycle stood out above all the rest—the Ultimatums. The original five Ultimatums were done back in *Shards of Alara* and had been a fan favorite. It was clear we wanted to do them here. Set Design and Play Design spent a lot of time making them as exciting as possible.


![Savai Triome](https://media.wizards.com/2020/iko/en_oUOuLfSIdb.png)


**The Triomes** – *Shards of Alara* also made the tapped tri-lands. These were lands that entered the battlefield tapped and could tap for one of three colors (arc-based, of course). *Khans of Tarkir* did the wedge version of these lands. We were discussing reprinting the *Khans of Tarkir* lands for the set when we started talking about if we could make stronger lands. The set had cycling. What if we gave them cycling? After some discussion with Play Design, we ended up giving them cycling 3.


Seeing Eye to *Ikoria*
======================


So that's what *Ikoria* is up to. I'm excited for you all to play it and see it all come together. As always, I'm eager to hear your feedback both on today's and last week's column as well as on *Ikoria* itself. You can [email me](mailto:making.magic@hotmail.com) or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).


Join me next week as I start my card-by-card design stories from *Ikoria*.


Until then, may your monsters do much mashing.




 

##### 
 #729: Michael Ryan, Part 1






##### 
 #729: Michael Ryan, Part 1


32:28



I've started recording "Drive to Work" from home due to the pandemic, so I decided to use the opportunity to do something that's hard to do in the car, interview people over the phone. This podcast is part one of a talk I have with Michael Ryan,...

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork729_michaelryanp1_82Hyeh76.mp3)



  


 

##### 
 #730: Michael Ryan, Part 2






##### 
 #730: Michael Ryan, Part 2


35:43



This podcast is part 2 of my interview with Michael Ryan. We continue talking about the making of the *Weatherlight* Saga.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork730_michaelryanp2_Hujs77yY.mp3)




* [**Episode 728**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork728_thbpart5_jdj7Y29I.mp3) *Theros Beyond Death* Cards, Part 5
* [**Episode 727**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork727_thbpart4_d19Uye8U.mp3) *Theros Beyond Death* Cards, Part 4
* [**Episode 726**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork726_bluered_kUd83ILd.mp3) Blue-Red








---
[Link to Wayback Machine](https://web.archive.org/web/20170502220636/http://magic.wizards.com/en/articles/archive/nineteen-principles-developing-planeswalkers-2007-10-26)

[_metadata_:author]:- "Devin Low"
[_metadata_:description]:- "*/"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "296456"
[_metadata_:publish_date]:- "2007-10-26"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Nineteen Principles for Developing Planeswalkers"
[_metadata_:wayback_capture_timestamp]:- "2017-05-02 22:06:36"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170502220636id_/http://magic.wizards.com/en/articles/archive/nineteen-principles-developing-planeswalkers-2007-10-26"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/nineteen-principles-developing-planeswalkers-2007-10-26"
---


The Nineteen Principles for Developing Planeswalkers
====================================================



 Posted in [ARTICLES HOME](/en/articles)
 on October 26, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DevinLow.jpg)
By Devin Low











Lorwyn's planeswalkers were the most challenging cycle I've ever seen us develop. One of our most reliable development tools is comparing new cards to benchmarks from the past, then analyzing how the new cards' changes make them different. [Wren's Run Vanquisher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wren%27s+Run+Vanquisher) is like [Watchwolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Watchwolf) but costs 1G and gains deathtouch in exchange for requiring some Elves. [Cloudgoat Ranger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloudgoat+Ranger) is like a jumping [Deranged Hermit](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deranged+Hermit) without echo. [Dauntless Dourbark](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dauntless+Dourbark) is like a [Jade Leech](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jade+Leech) that gets much bigger, doesn't tax your other spells, and often tramples. Weird cards like [Rebellion of the Flamekin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rebellion+of+the+Flamekin) are harder to compare directly to benchmarks of the past, but at least we have a good sense of how fragile or resilient an enchantment is going to be.


![Jace Beleren = ?](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/dl8_jace.jpg)


Planeswalkers robbed us of all these benchmarks. We found ourselves asking:



> 
> *"What if this guy went from 7 to 8 loyalty... would that feel impossible to kill? Or still too easy to kill and it should start at 10?"*
> 
> 
> *"Does waiting three turns to charge up the 'Ultimate' ability feel like a really long time or a really short time?"*
> 
> 
> *"How much harder are they to chip away if they have a +2 loyalty ability?"*
> 
> 
> 


With a totally new card type activating in unique ways, destroyed in unique ways, and covered in tweakable loyalty numbers, we had zero basis for comparison. Each of the five planeswalkers changed its abilities multiple times, and the ones we released bear little resemblance to the first versions designed. Hours of discussions over the roles of planeswalker cards in *Magic* led us to identify guidelines and constraints that would ultimately help us move forward. Thinking back on all those "unwritten rules," I decided to write them down. Without further ado, here are nineteen principles we used to develop *Lorwyn*'s planeswalkers.


### Mechanical Flavor


"Mechanical flavor" is a term I use to describe how some cards' rules text inherently convey flavor. Without a name, art, or flavor text, [Lowland Oaf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lowland+Oaf)'s type line and rules text inherently convey the idea of a giant hurling some goblins through the air. The name, flavor text, and art then build on that mechanical flavor and really make it pop. By contrast, the rules text of [Veteran of the Depths](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Veteran+of+the+Depths) has no inherent mechanical flavor. So that fellow relies on his name, art, and flavor text to let you know who he is in the world. We made a lot of choices in planeswalker development to enhance their mechanical flavor.


**Principle 1) They must feel like a totally new card type.**


It was crucial that planeswalkers felt like something totally different, that couldn't possibly be represented as a trumped-up creature or enchantment. We didn't want anyone to think "Oh they made a new card type? Let me see it. Couldn't they just have done that same card as an enchantment or a creature?" The designers took care of this with several rules that made the planeswalkers feel totally different from the other existing types. The big one? *You can attack these permanents with creatures*. That makes them feel awfully different than [Glorious Anthem](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glorious+Anthem). The other big one is that unlike creatures, [Terminate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terminate) can't kill planeswalkers. [Demystify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demystify) can't kill them. [Putrefy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrefy), [Mortify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify), and [Wrecking Ball](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrecking+Ball) combined can't kill them. They can't attack or block. They can be damaged, but they remember the damage they've taken from turn to turn, like a player, instead of clearing the damage they've taken at the end of each turn like creatures.


**Principle 2) They must feel like another Magic player has sat down to play with you.**


Though we don't belabor the metaphor, each player in *Magic* represents a planeswalker, traveling from plane to plane (e.g. from Kamigawa to Ravnica) combining each world's most powerful spells to battle other planeswalkers (players). The planeswalker designers wanted playing a planeswalker card to feel like you had literally brought another *Magic* player into the game, one who can do all the things that any human player can do.


To support this mechanical flavor, one of their demands was that the planeswalker abilities never cost you mana to activate. If you have a [Staff of Domination](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Staff+of+Domination) or a [Crystal Shard](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crystal+Shard) in play, you need to pump mana through it to activate it, because it's an inanimate object until you use your own mana to make it work. But [Chandra Nalaar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar) has her own mana sources, with her own mountains tucked away somewhere that only she knows about. She doesn't need *your* red mana to activate her burn effects—she has *her* *own* (implied) red mana that she uses to fuel it.


Another element is that just like a real *Magic* player has lots of different spells in his or her deck, each planeswalker had to be able to cast multiple different spells. One of the things that stops [Prodigal Sorcerer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prodigal+Sorcerer) from feeling anything like a human *Magic* player is that [Prodigal Sorcerer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prodigal+Sorcerer) only knows how to do one "spell" effect: ping.


 [![Gifts Ungiven](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Gifts%20Ungiven&options=)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts%20Ungiven)  
*We definitely couldn't let this target planeswalkers.* 
The designers also emphasized that planeswalkers should be targetable like players, not like creatures. [Terror](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terror) shouldn't kill them, they argued, because [Terror](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terror) only targets creatures. But [Lava Axe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe) targets players, so you should be able to target [Lava Axe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe) at planeswalkers. They started by saying that anything that targets a player or an opponent can target a planeswalker. That worked well for [Incinerate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate), but created some amusing problems with non-damage cards that targeted players. "I play [Gifts Ungiven](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven), targeting [Liliana Vess](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana+Vess). Which cards does she let me have?" Under *Magic* Rules Manager Mark Gottlieb's care, this evolved into the current rules where you officially target your [Lava Axe](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe) at the actual human player, then you can choose to have that damage be applied to one of that player's planeswalkers instead.


Planeswalkers can't themselves attack or block, because players can't themselves attack or block. But they can *be* attacked like players can, and they remember their damage over multiple turns like human players do.


(Click [here](http://archive.wizards.com/Magic/TCG/Article.aspx?x=magic/rules/planeswalkers) to see the full planeswalker rules.)


**Principle 3) They must match the creative team's top-down designs.**


Most cards are designed "bottom-up." This means that designers come up with rules text first, then developers refine and finalize that text, then the creative team looks at the text and decides what name, concept, art, and flavor text to use. Because the creative team had such high involvement in creating the planeswalkers and such a stake in how they turned out, the cards were designed "top-down." First, the creative team summoned into being initial versions of the five planeswalker concepts that Doug Beyer describes in [his article this week](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/db7). Then designers went to work supposing what their abilities should be, intertwined with those concepts. As developers played and changed and played and changed the cards over time, it was important to keep the planeswalkers' concepts in mind, and make sure their abilities continued to match.


For some planeswalkers this was easier than for others. From the beginning [Jace Beleren](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren) was, as Doug writes, a "natural at magic having to do with thought and memory." While Jace's abilities changed over time, we always kept them revolving around card drawing, library manipulation, milling, and [Jester's Cap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jester%27s+Cap) abilities.


[Ajani Goldmane](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Goldmane) made this a little more difficult, because his initial concept focused even more tightly on Ajani embodying the white concepts of justice, retribution, and punishing those who had hurt his friends. To match this concept, Ajani's first design focused on keeping creatures tapped who had attacked you last turn with a [Blinding Beam](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blinding+Beam) style ability, leading up to an "Ultimate" ability that said "Destroy all tapped creatures" to finish off all the perpetrators in an explosion of punishment. But then a time a came when we decided to push all the "Ultimate" third abilities to be not just regular spells, but effects that truly went above and beyond, and we had a lot of trouble finding an Ultimate for Ajani that did this but still focused on punishing creatures that had hurt you. As Aaron Forsythe said after another grueling examination of potential Ajani abilities, "It's hard to embody punishing creatures for attacking you when your abilities only go off in your own turn." So the creative team agreed to move more of the emphasis to the way, as Doug writes, "Ajani's true power lies in the ability to see strength in others, and to coax it out."


**Principle 4) They should embody the core essence of their colors.**


This principle was a little more controversial. Mark Rosewater felt very strongly that the first time we ever did planeswalkers, it was crucial for each of them to go straight down the middle of that color's color pie. He urged the rest of the department towards designs that hit the most classic, iconic abilities that color had, without using anything more closely associated with another color. For example, [Chandra Nalaar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar)'s concept says "If she outstrips her abilities and tries to manifest more fire than she can handle, she'll rupture." One proposal to represent this rupturing for Chandra's Ultimate was "Put a 5/5 red Djinn creature token with flying into play. That Djinn deals 5 damage to each other creature and each opponent." Rosewater was adamant that this would be a bad direction for Chandra because it would make the red planeswalker win with a big creature, and that's not the core of how red wins *Magic* games. "But Red has tons of big Dragon fliers, and they're great at winning games," others protested, but most of us came around to the idea that these first planeswalkers should hit the most iconic abilities for their colors. [Garruk Wildspeaker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker) isn't just green—the dude is GREEN.


It's also important to us that when we first release a concept or mechanic, we should keep it as simple as possible. Then we can twist it and play off of it in future sets. Planeswalkers were already complicated enough, without having excessively narrow or bizarre abilities.


**Principle 5) The cycle must be loose, not tight, so they feel like individuals.**


*Dissension*'s [Verdant Eidolon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Verdant+Eidolon) and friends are a good example of a very tight cycle. Each Eidolon costs exactly 3C, is exactly 2/2, has "C, Sacrifice CARDNAME: Do something", and has "Whenever you play a multicolored spell..." The only ways they vary are their colors and the effects of their sacrifice abilities. By contrast, *Future Sight*'s Grandeur legends like [Korlash, Heir to Blackblade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Korlash%2C+Heir+to+Blackblade) are a very loose cycle. Each one has totally different cost, size, and abilities. The only things tying them together are their legendary status and the grandeur activation cost.


It was important that we make planeswalkers feel like individuals, not like five tightly cycled [Granite Shard](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Granite+Shard)s with faces on them. To that end, we gave them a lot of flexibility to vary in their mana costs, loyalty numbers, loyalty costs, and so on. We even let some of them have a +2 loyalty cost instead of +1, or –X instead of –[some fixed number]. The things that tied them together were obviously their type and their unique shared rules. Beyond that, we gave a little nod towards being a cycle by saying they all had two colored mana symbols in their cost, a trick we've also used with loose cycles like [Silvos, Rogue Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silvos%2C+Rogue+Elemental) and friends, the loosely cycled *Onslaught* Pit Fighter legends.


### **Planeswalker Abilities**


**Principle 6) They must work well in any deck against any opponent's deck.**


Some cards in *Magic* can be very narrow in which decks they go in. [Verduran Enchantress](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Verduran+Enchantress) isn't for every green deck, just the ones focused on enchantments. But we needed the planeswalkers to be universally applicable in order to make them universally appealing. Imagine if Jace's abilities were:



> 
> +2: Untap all artifacts you control.  
> 
> -1: Search your deck for an artifact and put it into your hand.  
> 
> -14: For each artifact you control, gain control of target permanent
> 


Then he would be very appealing for heavily artifact-focused decks, but wouldn't do anything at all in the vast majority of random blue decks. That would be awful—we made it a priority to have these guys play well no matter what your deck does. It would also be bad if Garruk said:



> 
> +1: Destroy target enchantment.  
> 
> -2: Destroy all artifacts.  
> 
> -4: For each artifact and enchantment in your opponents' graveyards, put a 3/3 green Beast creature token into play.
> 


Likewise, this guy would be awesome against some opponents, like the Jace artifact deck above, but he would be useless against way too many opponents. So none of the planeswalkers spend a lot of time destroying enchantments or artifacts. Some opponents just don't have those permanents. But every opponent has a life total for Chandra to torch, a deck for Jace to mill, and a face for Ajani's Avatar to bash. We were happy to make some abilities interact with creatures, since those appear in most decks with pretty high regularity.


**Principle 7) They must each be a path to victory.**


 [![Liliana Vess](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Liliana%20Vess&options=)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana%20Vess)
As a powerful planeswalker yourself, you wouldn't sit down to play *Magic* without having a way to win, would you? Well neither would they! The designers decided it was important in order for the planeswalker cards to feel like additional players to make sure that each one could win the game all by itself, with a little bit of time and breathing room. Among other things, this ensures that your opponent really has to think hard about findings ways to hurt your planeswalkers just to slow them down, destroy them, or get killed by them. If you play [Honden of Cleansing Fire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Honden+of+Cleansing+Fire), your opponent can sometimes just ignore it and keep fighting you. Your opponents can't ignore your planeswalkers.


**Principle 8) The abilities should have some cool synergies.**


The fact that each planeswalker has three abilities provides an opportunity to make the abilities go together. And the principles of elegant design say that when a card does multiple things, they should usually connect somehow, not just be random abilities who met in the night. It's a fun moment when you realize that when you first make Ajani's avatar, it's not "just" 20/20, it's got potential to be at least 24/24. And then when you realize that if Ajani sticks around after making his token, his life gain keeps making the avatar even bigger, turn after turn, that's a fun moment too.


Likewise, Liliana, Garruk, and Jace's abilities all have internal synergies in obvious and not-so-obvious ways. Chandra's first and third abilities go together too: what's a classic, powerful combo with burning your opponent's life total? Burning a lot MORE of your opponent's life total!


**Principle 9) Each should give you multiple paths to take.**


To emphasize the synergies above, the first designs for planeswalkers focused on having all three abilities go together in a very clear path of "First do A, then do B, then do C." For example, here's a version of [Garruk Wildspeaker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker)—the same one that Erik Lauer mentioned [last week](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl7), with numbers from a couple weeks later:



> 
> **Garruk Wildspeaker**   
> 
> 3GG  
> 
> Planeswalker  
> 
> 4 loyalty  
> 
> +1: Put a 2/2 green Beast creature token into play.  
> 
> -2: For each Beast creature you control, put a 2/2 green Beast creature token into play.  
> 
> -5: All Beast creatures you control get +3/+3 and gain trample until end of turn.
> 


These three abilities definitely go together... a little too much in fact. It's pretty clear from reading and playing him that first you always have to activate the first ability for a few turns, then you should activate the second ability, then you should activate the third ability. There's never a reason to deviate from this recipe. That metronomic ticking feels too robotic to be a player. It feels more like a Homarid.


The development team cared passionately about making the planeswalkers give you multiple paths to play them, and not just one recipe. *"Hmm, should I use Chandra's second ability to kill that guy so I can attack past him? Or should I build up her loyalty with the first ability so she can survive if my opponent has [Incinerate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate)? Should I build her up to kill that bigger guy my opponent has, or should I build all the way to the Ultimate? Am I going to be able to protect her long enough to get there?"* The fact that they give you interesting choices about what to do, with different viable ways to win, is part of what makes them fun. The development team also made it a priority to balance the first and second abilities so that you would want to do each one a reasonable percentage of the time, with neither one always better than the other. When we found people were activating one of a planeswalker's first two abilities much more than the other, we'd change numbers until they were more even.


**Principle 10) Each one has a +N ability, a –N ability, and a –BIG N "Ultimate" ability.**


From very early on, all of us were excited about each planeswalker having an "Ultimate" ability that would take several turns to build up to, and would be totally totally worth it. (By the way, you should call a planeswalker's third ability its "Ultimate.") Planeswalkers were designed to provide exactly that opportunity, without requiring all the clunky rules text of the nefarious [Goblin Bomb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Bomb). An Ultimate you have to build towards basically means that ability has to cost more loyalty than the planeswalker has to start. We could also make an ability you have to build towards by using a resource other than loyalty, like the original Garruk using his [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun) ability only on Beasts, but it's not as elegant as letting the loyalty costs build it right in. If an Ultimate costs more than the planeswalker's starting loyalty, than he or she has to have a +N ability (meaning +1 or +2 or whatever) in order to be able to build there.


That left the second ability. We wanted to make this ability an alternate gameplay path for the planeswalker—something you could do besides hammering the first ability and building towards the Ultimate. It also gives some interesting decisions about how you build and use your loyalty. When is it worth it to build up more loyalty to make your planeswalker survive, or use its Ultimate, or use its second ability even more in the future? The second ability is also often a bribe that tempts you away from the Ultimate. Can you afford to build Chandra up a little bit, or do you need to burn a creature right now?


**Principle 11) Their abilities don't explicitly mention the world they're in.**


 [![Garruk Wildspeaker](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Garruk%20Wildspeaker&options=)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%20Wildspeaker)
Planeswalkers appear in the *Lorwyn* set, but they're definitely not from Lorwyn. How do we know they're from somewhere else? First of all, Lorwyn has no humans, and second, they're *planeswalkers*. The whole idea of them is that they travel from one plane to another. With that in mind, we intentionally avoided any abilities like "Each Kithkin you control gets +2/+2 until end of turn." Because that would tie them way too closely into this particular world, undermining the idea that they came from somewhere else and they're going somewhere else after they're done here. Avoiding any interactions with specific tribes also helps the planeswalkers to provide an appealing *Lorwyn* side dish that's totally separate from tribal, giving deckbuilding options that are totally different than what tribal is all about.



### Appeal


**Principle 12) The Ultimate should be jaw-droppingly awesome.**


Once upon a time, the Ultimates included abilities like "Destroy all tapped creatures" that the old Ajani's [Blinding Beam](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blinding+Beam)s led you towards. That was something you wanted to do, but it was not "call up your friends" amazing. Developers and designers did a lot of processing on all the planeswalkers' Ultimates until we had:



> 
> 
> -6: Put a white Avatar creature token into play with "This creature's power and toughness are each equal to your life total."
> 
> 
> 
> 
> -10: Target player puts the top twenty cards of his or her library into his or her graveyard.
> 
> 
> 
> 
> -8: Put all creature cards in all graveyards into play under your control.
> 
> 
> 
> 
> -8: Chandra Nalaar deals 10 damage to target player and each creature he or she controls.
> 
> 
> 
> 
> -4: Creatures you control get +3/+3 and gain trample until end of turn.
> 
> 
> 
> 


We were excited that these pretty clearly *were* "call up your friends" amazing, and player feedback has really confirmed that. The cheapest one is [Garruk Wildspeaker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker)'s [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun) ability. When you have a bunch of creatures [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun) has always been totally devastating, with [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun)'s drawback being the fact that it's dead if you have zero guys, and just okay if you have only one. Garruk's [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun) gets around this by providing two other amazingly powerful ways to use him if you don't control a lot of creatures already, one of which even generates the army you need to make the [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun) a slam dunk.


**Principle 13) They must each be powerful in Limited.**


It's important that when you open one of these in a Draft and feel the stirrings of excitement over the card type, that excitement is rewarded by the card's raw power. Developers made sure that each of these is a powerful weapon in Sealed and Draft. In many cases, you hear people saying "I managed to kill his planeswalker, but it took so much effort to kill it that the rest of his stuff killed me."


**Principle 14) They should all be decent in Constructed, and some of them should be awesome in Constructed.**


Rares that are powerful in Limited and rares that are powerful in Constructed are often extremely different. Just ask [Gurzigost](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gurzigost) and [Cunning Wish](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cunning+Wish). It's tough to get a rare to straddle both sides of the pond and be powerful in both contexts. But it was important that each of the planeswalkers do that. Each has the potential for a role in Constructed, and some of them have enormous potential for Constructed. Which ones are they? Time will tell.


**Principle 15) They must appeal to Timmy.**


As well as being powerful for Spikes, the Ultimates in particular are tailor-made for Timmy, with awesomely powerful, exciting effects that lead to hugely fun moments and great stories afterwards


**Principle 16) They must appeal to Johnny.**


We achieved this by keeping the abilities as open-ended as we could. [Liliana Vess](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana+Vess) used to target only opponents with her discard ability. By opening the ability up to target any player, we made her into a "[Putrid Imp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrid+Imp) / Akroma / [Reanimate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reanimate)" style self-reanimation engine in addition to being a manaless [Vampiric Tutor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampiric+Tutor) (that hurts her instead of you), a manaless repeating [Planar Portal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Planar+Portal), and a huge, all-for-me dodectuple [Zombify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombify) caster.


We also made sure the planeswalkers as a whole worked with cards like [Rings of Brighthearth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rings+of+Brighthearth) (yes, you can copy the planeswalker abilities), [Doubling Season](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doubling+Season) (you can double the loyalty counters, although not the loyalty gains from using +N abilities), [Fertile Ground](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertile+Ground) or [Pendelhaven](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pendelhaven) (in the case of [Garruk Wildspeaker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker)), and many others.


**Principle 17) They must appeal to Spike.**


Spike is famous for loving powerful cards, so our other principles ensured the planeswalkers had that covered. But Spike also loves cards that let him or her make deeply strategic choices that allow him or her to out-think and outplay opponents. Spike also loves resource management cards like [Compulsion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsion), [Wild Mongrel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Mongrel), or [Mindless Automaton](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindless+Automaton) that let Spike convert one thing into another. The planeswalkers' multiple abilities, each of them appealing and creating an interesting strategic puzzle to solve as well as a resource management challenge, make planeswalkers appealing to Spike as well.


### Gameplay


**Principle 18) They must play well, and they must be fun!**


 [![Chandra Nalaar](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Chandra%20Nalaar&options=)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra%20Nalaar)
This is the most important principle. And this is the most important thing that developers do, across all *Magic* sets. More than tweaking numbers, more than ensuring the correct amount of [Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant)s, this is what's important to us. For planeswalkers, we played and analyzed design after design, tossing them again and again for not being as fun as our high standard for planeswalkers needed to be until we hit ones we liked in all five slots. When I take you through the specific stories of each planeswalker's individual evolution in future articles, you'll get a look into all the designs that tried and died so that these planeswalkers could live.


As Erik Lauer explained last week, the move from "At the beginning of your upkeep, play one of these abilities," which we played for weeks, to "You may play one of these abilities during each of your turns, as a sorcery" made them hugely more fun. Before the change, it felt like you built up your defenses to house your planeswalker, then played him or her out, said go, and cringed, praying your planeswalker would survive until your next upkeep step. The change let the planeswalkers impact the board right away. Instead of [Chandra Nalaar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar) coming out and immediately getting whacked by [Serra Avenger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Avenger), Chandra now came out and smashed the [Serra Avenger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Avenger). The change also basically gave the planeswalkers a sort of "comes into play" effect, ensuring that they could always two-for-one the opponent. Even if your opponent [Blaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blaze)s your planeswalker to death on sight, as soon as possible, trading a card for a card, you still get to keep the first ability you played from your planeswalker, whether it's a bunch of +1/+1 counters and extra damage, drawing a card, forcing a discard, burning out a creature, or making a 3/3 beast.


**Principle 19) They must be interactive, and every color must have answers to them.**


One of my favorite parts about playing *Magic* is the interactivity. My opponent makes a move, and I have to make a counter-move. How can I dismantle the machine that he is putting together? How can I kill his guys before they kill me? Do I have to [Naturalize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize) right now to stop her combo from going off, or can I afford to tap out for a fatty and [Naturalize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize) next turn? [Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant) and [Last Gasp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Last+Gasp) can't kill planeswalkers. To maintain that interactivity, it was very important to us that viable answers to planeswalkers exist, just like it's important to us to have viable answers to graveyard strategies ([Tormod's Crypt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tormod%27s+Crypt), [Extirpate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Extirpate)), answers to counterspells ([Eyes of the Wisent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eyes+of+the+Wisent)), answers to land destruction (*Ninth Edition*'s [Sacred Ground](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sacred+Ground)) and so on.


The good news is that every *Magic* set has dozens and dozens and dozens of built-in answers to planeswalkers: creatures. The fact that creatures can attack planeswalkers directly means that most *Magic* decks already have many built-in ways to weaken and banish planeswalkers. Red burn spells, black [Consume Spirit](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Consume+Spirit) effects, and good ol' "timeshifted" blue [Psionic Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psionic+Blast) can all wound or banish planeswalkers and are already popular and frequently played.


Designers urged us not to have any cards that said "Destroy target planeswalker," and we agreed. At least for the time being, it made sense to us that planeswalkers should be separated from paltry creatures partly by not having cards that explicitly talked about planeswalkers. Also, planeswalkers are visitors to Lorwyn, not residents. They are inherently separated from the world of Lorwyn—they just appear in the same set. For the same reason that it would be weird and bad to have a planeswalker saying "Untap all Merfolk you control," it would be weird and bad to have the other *Lorwyn* cards saying "Destroy target planeswalker." Most Merfolk probably don't even realize the planeswalkers exist.


 [![Rootgrapple](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Rootgrapple&options=)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootgrapple)
Instead we seeded *Lorwyn* with a lot of sideways answers to planeswalkers, for Limited, casual Constructed, and Tournament constructed purposes. There are tons of them in there, many of them extremely subtle. Can you find them all? Even if you've found a lot, there are probably some that have escaped your eye. If you've noticed that [Rootgrapple](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootgrapple) says "Destroy target noncreature permanent" instead of [Creeping Mold](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Creeping+Mold)'s template of "Destroy target artifact, enchantment, or land," you're on the right track. If you noticed that on a clogged board, [Protective Bubble](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Protective+Bubble) will let you sneak through a creature to assassinate an enemy planeswalker, you just might have a future in R&D. I'll go through all of these planeswalker answers in a future column.


Throughout development, we were continually tweaking each planeswalker's loyalty total and loyalty costs, every week publishing a new set of numbers for people to test. One of the benchmarks for interactivity I used was "Does it die to [Psionic Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psionic+Blast)?" naming one of the few blue answers to a planeswalker on the board. In general, I felt like the 4 damage dealt by [Psionic Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psionic+Blast), and Limited-format planeswalker answer [Giant's Ire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant%27s+Ire) should tend to kill the Planeswalkers. If a powerful burn spell like Psi Blast couldn't even kill them, wouldn't they just be too hard to kill? And remember that you have to add the first +N loyalty ability to each planeswalker's loyalty total to see how hard it is to kill when its owner announces the +N ability as soon as the planeswalker comes into play. In one meeting, we wanted to make the planeswalkers even better, and increasing their loyalty totals was on the table. I said something about how important it was that [Psionic Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psionic+Blast) could still kill them. Then Aaron said, "One of the things that makes [Shivan Dragon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shivan+Dragon) an awesome *Magic* card is that it doesn't die to [Psionic Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psionic+Blast)." His point was excellent. It was very important to me to make the planeswalkers awesome *Magic* cards, and part of that meant making them really hard to kill. We moved the loyalty totals up.


And there you have it: The nineteen principles we used to develop *Lorwyn's* planeswalkers. Many thanks to excellent *Magic* developer Erik Lauer for guest-writing the column during my absence last week. I was attending [Pro Tour–Valencia](http://archive.wizards.com/Magic/Magazine/Events.aspx?x=mtgevent/ptval07/welcome) in Spain, where I fought all comers at the gunslinging table and analyzed the Pro Tour's Extended format.


### Recent Weeks' Polls




|  |
| --- |
| **What do you think of "Becomes #/#" as a combat trick for future Magic sets?**  |
| It's a nice change as long as you keep it in small doses. | 7576 | 64.6% |
| It's great. Do it more often. | 3381 | 28.8% |
| It's a bad idea. Avoid doing this. | 779 | 6.6% |
| **Total** | **11736** | **100.0%** |

Wow, over 90% of respondents called the power/toughness-setting combat trick either "a nice change" or "great." One of the elements that makes [Wings of Velis Vel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wings+of+Velis+Vel) work as an overall card is that it's a tribal instant with changeling, which explains why blue can make a creature bigger (and sometimes smaller). I plan to keep doing P/T-setting effects in small doses, only where the card makes sense in its flavor and in the color pie. Email respondents also had valuable feedback. [Lignify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lignify) is also a good example of P/T-setting working well, with good flavor.




|  |
| --- |
| **Which is your favorite planeswalker (overall, both card and character)?** |
| Garruk Wildspeaker | 4091 | 30.4% |
| Jace Beleren | 3223 | 23.9% |
| Chandra Nalaar | 2547 | 18.9% |
| Liliana Vess | 2211 | 16.4% |
| Ajani Goldmane | 1406 | 10.4% |
| **Total** | **13478** | **100.0%** |

At least a thousand people named each of the planeswalkers as their personal favorite, which is always a good sign that warms my heart. It means that each of the cards has good appeal to a lot of people, each of them has a lot of people it makes happy, and none of them is a slouch. And I doff my hat to you, good sir Wildspeaker.








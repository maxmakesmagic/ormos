
---
[Link to Wayback Machine](https://web.archive.org/web/20210429024140/https://magic.wizards.com/en/articles/archive/feature/four-short-stories-about-eventide-2008-07-21)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/four-short-stories-about-eventide-2008-07-21"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429024140id_/https://magic.wizards.com/en/articles/archive/feature/four-short-stories-about-eventide-2008-07-21"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 02:41:40+00:00"
[_metadata_:description]:- "Welcome to Mimic Week! All this week on magicthegathering.com, the regular columns will appear as usual… but with a twist. Your eight regular writers, plus at least two guest authors who've written for the site before, are hiding in the ten regular column slots—maybe even their own—under a clever pseudonym: The Mimic! Can you figure out who actually wrote each article? Tune in"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Four Short Stories about *Eventide*
===================================



 Posted in **Feature**
 on July 21, 2008 






![](https://web.archive.org/web/20211024110319im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By The Mimic











*Welcome to Mimic Week! All this week on **magicthegathering.com**, the regular columns will appear as usual… but with a twist. Your eight regular writers, plus at least two guest authors who've written for the site before, are hiding in the ten regular column slots—maybe even their own—under a clever pseudonym: The Mimic! Can you figure out who actually wrote each article? Tune in Monday, July 28 for the answers!*

**Development Story**One of the major duties of developers is to make sure its Limited environment is both fun and balanced. Heavy saturations of hybrid mana costs is a new beast; it can be difficult to tell whether [Recumbent Bliss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recumbent+Bliss) or [Soul Reap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Reap) is making white or black too powerful and overplayed in Sealed when [Unmake](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unmake) is running around masquerading as either color.


The first ever *Shadowmoor* / *Shadowmoor* / *Eventide* draft led to a harrowing revelation: drafters weren't getting enough "hybrid rewards" from their *Eventide* gambits.


![Nightsky Mimic](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nightsky+Mimic)To address this, *Eventide* lead developer Matt Place called for an emergency meeting with the *Eventide* designers and developers with these goals in mind:





* Design a tight cycle of commons that reward enemy-color hybrid.
* This cycle is most likely creatures.
* This cycle is most likely two mana, either 1H or HH since there's already a cycle of H 1/1 common creatures, HHH uncommon creatures, 2H 2/2 uncommon Hedge-Mages, and (at the time) 1HH 1/1 to 5/5 Hatchlings.
* The cycle must be powerful enough for drafters salivating for a reason why they cut off their left arm and right leg during two entire *Shadowmoor* boosters full of ally-color hybrid rewards.
* This cycle ideally does "color matters" mechanically differently from *Shadowmoor*.

Upon the conclusion of this meeting, the Mimic cycle was born. Many of the potential templates we felt would confuse players, as blue-red Mimic might trigger on:





* When you've played both a red spell and a blue spell this turn
* Any spell you play that is precisely blue and red
* Any spell you play that is both blue and red
* On the first spell you play each turn that is both blue and red
* On your blue spells, but only if you've also played a red spell this turn
* On your red spells, but only if you've also played a blue spell this turn
* When you play a blue spell, [P/T change]. When you play a red spell, [keyword].
* Lots more...

We like simple, clean, and grokkable commons, so the template we used for a few playtests was the narrower but cleaner "Any spell that is both blue and red." This particular implementation grew on us because we were audibly hearing each other yell, "C'MON HYBRID CARD!" when topdecking. This is a fantastic thing to hear players say when the main theme of the expansion is hybrid cards, so we kept their printed template.


The double dose of high-octane Mimics plus God-Auras (such as [Gift of the Deity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity)) at common rewarding enemy-colored hybrids brought subsequent *Shadowmoor* / *Shadowmoor* / *Eventide* drafts up to satisfactory levels of enemy-colored goodness.


As we all know, Development is the awesomest thing about **Magic** cards, because otherwise the cards would be broken, and an unbalanced game is about as challenging and fun as stealing candy from babies.


**Rules Story**Salutations, mortals! Though *Eventide* was a tame set on the rules side compared to the debilitating (for feeble-minded humans) questions raised while working on *Future Sight*, it wasn't completely without need of **Magic** Rules Manager Mark Gottlieb's omniscient thought.



> 
> Evershrike  
>  3(w/b)(w/b)  
>  Creature - Wombat  
>  2/2  
>  Flying  
>  CARDNAME gets +2/+2 for each Aura attached to it.  
>  When you play an Aura spell targeting CARDNAME in your graveyard, return CARDNAME from your graveyard to play.
> 




[![Holy_Strength](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/2e/Holy_Strength.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Holy%2BStrength)While the "Wombat" gesture is both adoring and trite, this card is still with sin; the universe, as the rules have created it, does not support this card's text. An Aura has to target a permanent unless something (including itself) is explicitly giving it permission to target something else. This card has a trigger that does something when it's in the graveyard and targeted by an Aura—but nothing is giving an Aura the ability to target it in a graveyard in the first place! You can't target an [Evershrike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evershrike) in your graveyard with [Holy Strength](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength) just because [Evershrike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evershrike) expects you to; [Holy Strength](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength) can target only a creature in play.


The second problem is that [Evershrike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evershrike) changes zones when the trigger resolves, which means that the Aura that was targeting it in the graveyard says, "Oh, it's gone" and is countered on resolution. It can't follow it to the in-play zone. A compounded failure!


The rules team gave the development team three different options for salvaging this card:



> **Option 1**  
>  X: Return CARDNAME from your graveyard to play. You may put an Aura card with converted mana cost X from your hand into play attached to CARDNAME. If you don't, remove CARDNAME from the game. Play this ability only any time you could play a sorcery.



> **Option 2**  
>  As long as CARDNAME is in your graveyard, it may be targeted by Aura spells you control as though it were in play.  
>  Whenever CARDNAME becomes the target of an Aura spell, if it's in your graveyard, return it to play. Change that spell's target to CARDNAME.



> **Option 3**  
>  As long as CARDNAME is in your graveyard, it can be targeted by Aura spells [you control] and enchanted by Auras [you control] as though it were in play.  
>  When CARDNAME becomes enchanted, if it's in your graveyard, return it to play. All Auras attached to CARDNAME in your graveyard become attached to it in play.


The team chose Option 3, but that was a trick; Option 3 is too long to fit on a **Magic** card! Those hilarious humans forgot about [Evershrike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evershrike)'s flying and "Wombat" abilities. Oh, how great it feels to tantalize humankind with seemingly feasible gifts, like Option 3, world peace, or unsoggy waffles. They cannot be achieved!


The team quickly chose Option 1, edited it for space, and averted yet another crisis in **Magic**. It might not be parting the Red Sea, but the snake did get its apple.


![Evershrike](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Evershrike)
As we all know, rules are the most important thing about **Magic** cards, because otherwise none of the cards would work, no one could play **Magic** games, and (modus ponens) there would be no need for **Magic** cards.


**Art Story**[![Vendilion_Clique](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/MOR/Vendilion_Clique.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Vendilion%2BClique)The **Magic** creative team in R&D works hard to refine the settings, characters, and events for new **Magic** expansions. Concept illustrator Richard Whitters's main duty is providing style guide sketches that other artists use to guide their illustrations, but he does on occasion get to put pen to card art.


For *Eventide*, Whitters was tasked with illustrating the card named "Springing Sprite," though you know the card as "[Groundling Pouncer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Groundling+Pouncer)." [Groundling Pouncer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Groundling+Pouncer)'s flavor is based on the army of Endry (who you may remember as one of the three faeries of the [Vendilion Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vendilion+Clique)). In the *Eventide* novel, Endry's army is composed of non-flying faeries called "groundlings."


Here is the card concept, written by *Eventide* concepter Doug Beyer:



> Color: Green and blue creature  
>  Location: The floor of a creepy dead forest  
>  Action: Show a strange little woodland sprite, like the one on pg. 61 of the style guide (the blue spindly guy in the upper left corner). It has no wings, but has grasshopper-like legs as if it could leap well, and it has thin stretches of skin under its arms like a flying squirrel. It is creeping along, looking for something good to eat. Moths flit above it.  
>  Focus: The sprite. Be sure it's clear it could be capable of flight.  
>  Mood: It might fly at any moment.




While the concept was solid and concrete (instead of, say, "a fire spell!"), the catch was that this character is neither flying nor not flying, yet is clearly capable of flight while having no wings, and ready to fly at any moment.


Pressing forward, Whitters roughed out an initial sketch for Springing Sprite:


[Groundling Pouncer](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Groundling%2BPouncer)
The art borrows elements of the insectoid, the arm flaps, the flitting moths, and the hunched down frog-leaping pose and situated them to make the most of the tiny space that is a piece of card art. At this point, Whitters scanned the sketch and worked on the piece using self-taught Photoshop, the finalized art looking like so:


[Groundling Pouncer](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Groundling%2BPouncer)
The moth element grew to re-establish scale and shrink the sprite down to faerie-size. The wing flaps took on skin, making them neither translucent nor bony like a bat wing. The lighting in *Eventide* is never solar due to perpetual nighttime, so the scene is lit with a more lunar, almost bioluminescent light. A couple texture passes on the shoulders and legs to more closely emulate chitin, a color correction step, and that was that! [Groundling Pouncer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Groundling+Pouncer) was finished and ready to be printed in booster packs as you see it today:


![Groundling Pouncer](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Groundling+Pouncer)
As we all know, art is the greatest thing about **Magic** cards, because without art, the cards would be ugly and boring, and nobody would want them.


**Design Story**![Favor of the Overbeing](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Favor+of+the+Overbeing)Mark Rosewater—lead designer of *Eventide*, lead designer of *Shadowmoor*, and one-time compensated writer for the hit TV sitcom *Roseanne*—gets a ton of mail about **Magic**, and he reads all of it. He recently received a unique compliment / insult. The sender's metaphor was that he is "the Lance Armstrong of card design." At first he thought it was a compliment, but it soon turned sour. The sender explained that it's not because he dominates the main event of his field, or because his spirit is indomitable, or any unpleasant anatomical metaphors. Apparently, he's the Lance Armstrong of card design because he's "completely infatuated with cycles."


Speaking of exercise equipment that could help John Goodman lose weight, cycles run through all of *Shadowmoor* and *Eventide*, including Tour de France-sized ten-card cycles that all had to be carefully designed to not step on each other or drink from the same well too many times. My favorite cycle of all of these is the God-Aura cycle: [Shield of the Oversoul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shield+of+the+Oversoul), [Steel of the Godhead](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steel+of+the+Godhead), [Helm of the Ghastlord](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Helm+of+the+Ghastlord), [Fists of the Demigod](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fists+of+the+Demigod), and [Runes of the Deus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runes+of+the+Deus) in *Shadowmoor*, and [Edge of the Divinity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Edge+of+the+Divinity), [Gift of the Deity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity), [Clout of the Dominus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clout+of+the+Dominus), [Favor of the Overbeing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Favor+of+the+Overbeing), and [Scourge of the Nobilis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scourge+of+the+Nobilis) in *Eventide*.


The God-Auras actually began as a *Shadowmoor* cycle:



> 
> Selesnya's ColorTrick  
>  (g/w)  
>  Instant (Common)  
>  Target creature gets +2/+2 until end of turn if it's green and +2/+2 until end of turn if it's white.
> 


A plucky intern made the off-hand comment that "Maybe this would feel more hybrid as '+1/+2 if white, +2/+1 if green.'" Bill Rose, the Vice President of R&D and an original playtester of Alpha, retorted, "No, that's a white-black card. If enchanted creature is white, [Holy Strength](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength). If black, [Unholy Strength](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Strength)."


From that little parlay, Bill Rose's card immediately went into the *Eventide* design file. The so-called "Un/[Holy Strength](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength)" Aura playtested so fantastically in our *Eventide* design meetings (which happened simultaneously with *Shadowmoor* development) that everyone was in love with the spectacular result of enchanting a white-black hybrid creature with its custom-made Aura. [Edge of the Divinity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Edge+of+the+Divinity) made any and all white-black hybrid creatures awesome, it broke stalemates and ended the game so another game could start, and it was a draftable build-around-me. There's even variance, because sometimes it's the correct play to enchant your mono-white or mono-black creature, given the board state.


In order to maximize the impact of God-Auras and hybrid, we specifically chose Aura abilities that are *un*likely to be on the corresponding hybrid creatures. Here is an abridged chart showing how heavily we pulled from the unshared keywords:




|  |  |  |
| --- | --- | --- |
| Color | Shared Keywords | Unshared Keywords |
|  | vigilance, token creatures | **flying**, trample, first strike, lifelink, **indestructible** |
|  | flying, flash | **lifelink**, **unblockable**,  |
|  | flying, protection from green | **Specter**, **Ophidian** |
|  | haste, **wither** | **first strike**, fear, regeneration |
|  | **trample** | **double strike**, reach, first strike, haste |
|  | shroud, islandwalk | **flying**, trample, **vigilance** |
|  | unblockable | **haste, shroud** |
|  | first strike, double strike | **lifelink**, haste, **Firebreathing** |
|  | lifelink, flying | **Holy Strength, Unholy Strength** |
|  | regenerate, wither, **deathtouch** | trample, **Lure** |

The three Auras using shared keywords are also the sickest keyword combos: trample + double strike, deathtouch + [Lure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure), and wither + first strike (which, interestingly enough, could be red-green, black-green, or black-red). Though all colors have persist, persist is too "feel bad" when granted on an Aura. After much fidgeting, the God-Auras were printed as you know them today, quelling many a doubting Forsythe and creating as many "triple-upside" moments as possible:


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/features/467_rith.jpg)*Sorry for the double flying bonus...*As we all know, Design is the best thing about **Magic** cards, for without Design, there would never be any new cards!


Can you guess who wrote this? Click Discuss below to talk about this article, or head to the [Mimic Week thread](http://forums.gleemax.com/showthread.php?t=1062820) in the forums to talk about all your guesses!

Mimic Week is over! Did you guess who wrote this article?


Click here to find out if you're right.


![Kenneth Nagle](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_kennethnagle.jpg)This article was written by *Eventide* designer / developer Kenneth Nagle!








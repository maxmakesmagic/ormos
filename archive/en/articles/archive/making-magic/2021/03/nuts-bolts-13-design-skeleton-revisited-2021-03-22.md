
---
[Link to Wayback Machine](https://web.archive.org/web/20210324115858/https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-13-design-skeleton-revisited-2021-03-22?utm_source=dlvr.it&utm_medium=twitter)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark continues is annual dive into designing sets, taking a fresh look at his iconic design skeleton breakdown."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1532687"
[_metadata_:publish_date]:- "2021-03-22"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Nuts & Bolts #13: Design Skeleton Revisited"
[_metadata_:wayback_capture_timestamp]:- "2021-03-24 11:58:58"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210324115858id_/https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-13-design-skeleton-revisited-2021-03-22?utm_source=dlvr.it&utm_medium=twitter"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-13-design-skeleton-revisited-2021-03-22?utm_source=dlvr.it&utm_medium=twitter"
---


Nuts & Bolts #13: Design Skeleton Revisited
===========================================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on March 22, 2021 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






In the first quarter of every year, I write a series called "Nuts & Bolts" where I talk about the nitty-gritty of how to make a *Magic* set. The series is aimed at amateur *Magic* designers, but I hope it's interesting to everyone else as a means to peek behind the curtain and see how exactly we handle the minutiae of the job.


This is my thirteenth year doing a "Nuts & Bolts" column. Here are the previous twelve (thirteen if you count last year's two-part article):


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


[**Nuts & Bolts #12, Part 1: Limited (Mechanics)**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-12-part-1-limited-mechanics-2020-03-09)


This twelfth column got broken into two parts. Both talk about how to make sure your set is working properly in Limited. The first article focuses on making sure your mechanics work for Limited play.


[**Nuts & Bolts #12, Part 2: Limited (Themes)**](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-12-part-2-limited-themes-2020-03-16)


The second part focuses on building out themes for Limited play.


Which brings us to my thirteenth "Nuts & Bolts" column. This year, I decided to go back to a topic that I talked about nine years ago, the design skeleton. This is the basic tool for building a *Magic* set. I've gotten a lot of mail that the design skeleton article is getting a little dated, so I thought I would take an updated look at it to help you make a set that looks a little more like current design. Also, R&D has upped its game a little, so I have a much more robust default design skeleton to show you. More on that in a second.


For those unfamiliar with a design skeleton, it's a structural tool to let the designer see, at a glance, the needs of the set and where different elements can be slotted in. If you want more information on the basics of a design skeleton, take a look at [my original article on the topic](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-design-skeleton-2010-02-15).


Today, I'm going to be showing you a much more fleshed-out starting point for making a *Magic* set. Last year, R&D started doing this thing where the more seasoned designers would put on talks about various topics for the rest of the studio. (My talk is on the importance of the color pie.) One designer, Adam Prosak, made a default design skeleton to help new designers get a running start when making their first set. This default design skeleton is very detailed and something I think will be very helpful to anyone interested in designing their own *Magic* set.


This default design skeleton is for all the commons and uncommons. It's essentially a generic design skeleton that can be used as a starting point. Remember, the design skeleton is a living, breathing document that should be changing as you build your set. What I'm presenting today, with a big thanks to Adam Prosak, is something to use as a starting point. A big part of making your set will be adapting the design skeleton to the needs of your particular set. What I'm presenting today is just a tool to give you something to start with.


Design of the Times
===================


We begin by looking at our set size. The default *Magic* set is what we used to call a "large set" (back when it was followed by two "small sets"). It has 101 commons and 80 uncommons. At common, the default design skeleton assumes that you're going to have nineteen cards of each color and six artifacts. At uncommon, it assumes you're going to have thirteen cards of each color, a ten-card cycle of two-color cards, and five artifacts. The default does not add in any lands to common or uncommon, but I will explain below the various ways you can mix them in if your set needs them.


The creature ratios are figured as such. The *Magic* colors have an order for how many creatures they have, with #1 being the most and #5 being the least. #1 is white, #2 is green, #3 is black, #4 is red, and #5 is blue. We start with 62% creatures in white and drop it three percent as you advance to the next color, ending with blue at 50%. These percentages don't work perfectly, so there's a little wiggle room on your creature numbers as you can round up or down. That means these are the ratios:


White – 62%  

Blue – 50%  

Black – 56%  

Red – 53%  

Green – 59%


The default puts three artifact creatures at common and three at uncommon.


It's very important, especially at common, to have a smooth creature curve built into your creatures, so below, I am going to spell out what mana value each creature slot should be at (with a little bit of wiggle room). I'll be abbreviating mana value as MV. The spells want a variety of mana costs but don't have to be quite as prescriptive, so the default design skeleton doesn't list their mana value.


Now let's get to the nuts and bolts of each color (and multicolor and artifacts).


White
-----


**Common Creatures**


Of white's nineteen common cards, twelve of them are creatures. Here's the breakdown. (I'm using card codes. Go read [my very first "Nuts & Bolts" column](https://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-card-codes-2009-01-12) if this is confusing to you.) We list our creatures in mana-value order to make it easier to keep track of the creature curve in each color.


CW01 – 1 MV  

CW02 – 1 or 2 MV (don't pick 2 for this and CW06)  

CW03 – 2 MV  

CW04 – 2 MV  

CW05 – 2 MV  

CW06 – 2 or 3 MV  

CW07 – 3 MV  

CW08 – 3 MV  

CW09 – 4 MV  

CW10 – 4 MV  

CW11 – 5 MV  

CW12 – 5 or 6 MV


An instant or sorcery that creates one or more tokens is considered a creature for design-skeleton purposes and is put here. A creature with zero power or one that can't attack usually is not counted as a creature.


Keywords found in white at common (with the defaults in number listed beside them):


* Defender (0–1, this isn't counted as a creature)
* First Strike (1, sometimes only on your turn or on attack)
* Flash (0–1)
* Flying (2–3, try not to repeat stats, you want a mix of different powers)
* Indestructible (0–1, only granted temporarily by a spell)
* Lifelink (1, power 3 or less)
* Vigilance (1)

Common creatures don't often have more than one keyword. When they do, flying is usually one of them.


**Common Spells**


CW13 – Small removal (usually damage to an attacker or blocker)  

CW14 – Can't attack or block (sometimes also stops activated abilities, usually an Aura)  

CW15 – Destroy large/tapped creature  

CW16 – Combat trick (usually +2/+2 or smaller)  

CW17 – Positive Aura/Equipment  

CW18 – Go-wide team-pump effect  

CW19 – Destroy artifact/enchantment (oftentimes, it can destroy either)


In all colors, you want to make sure there's a mix of instants, sorceries, enchantments, and artifacts. At common, enchantments tend to be Auras.


**Uncommon Creatures**


UW01 – 1 MV  

UW02 – 2 MV  

UW03 – 2 or 3 MV  

UW04 – 3 MV  

UW05 – 4 MV  

UW06 – 5 MV  

UW07 – Any MV (no more than two creatures at uncommon should have the same MV)  

UW08 – Any MV


The creature curve can be a little more flexible at uncommon, so there are two slots that you can make any size. This is true in all colors.


Keywords found in white at uncommon:


* Defender (0–1, not counted as a creature)
* Double strike (0–1, if you use double strike, you often won't use first strike)
* First Strike (0–1)
* Flash (0–1)
* Flying (2 fliers of different powers, one is usually larger, like an Angel)
* Indestructible (0–1)
* Lifelink (1)
* Vigilance (1)

Uncommon is more likely to have creatures with multiple keywords. Again, this is true in all colors.


**Uncommon Spells**


UW09 – Creature removal (usually very efficient)  

UW10 – Non-creature  

UW11 – Non-creature  

UW12 – Non-creature  

UW13 – Non-creature


Uncommon is much more open to its spell mix. You want to make sure you have a variety of spell types with your non-creature spells.


Some options for the non-creature spells:


* An effect that exiles a permanent (or some subset) while it's on the battlefield
* Making multiple creature tokens
* Permanent team boosting (with enchantment or +1/+1 counters)
* Life gain (often repeatable)
* Interactions with Equipment and/or Vehicles
* Enchantment with static rules-setting ability
* An Aura or Equipment

Blue
----


**Common Creatures**


Blue has the smallest number of creatures, giving it nine at common.


CU01 – 1 MV  

CU02 – 2 MV  

CU03 – 2 MV  

CU04 – 3 MV  

CU05 – 3 MV  

CU06 – 4 MV  

CU07 – 4 MV  

CU08 – 5 MV  

CU09 – 6+ MV (this, or sometimes CU08, often has some attacking restriction)


Blue is more likely to have a greater number of creatures with tap abilities at common than other colors.


Keywords found in blue at common (with the defaults in number listed beside them):


* Defender (0–1, this isn't counted as a creature)
* Flash (1)
* Flying (3 fliers, try not to repeat stats, you want a mix of different powers)
* Hexproof (0–1, used sparingly, only on small creatures at common, no evasion)

**Common Spells**


CU10 – Either 0 power creature, creature with defender, or non-creature  

CU11 – Counterspell that can counter anything (what R&D calls a "hard counter")  

CU12 – Counterspell with some restriction (what R&D calls a "soft counter")  

CU13 – Lockdown Aura  

CU14 – Card drawing (usually no more than three cards)  

CU15 – Cantrip/card filtering (aka drawing some number of cards and then discarding)  

CU16 – Bounce spell (usually returning a creature to hand, never returning a land)  

CU17 – Positive Aura or combat trick  

CU18 – Disrupt opposing creatures (freezing, tapping, lowering power, etc.)  

CU19 – Anything


**Uncommon Creatures**


UU01 – 1 or 2MV  

UU02 – 2 MV  

UU03 – 3 MV  

UU04 – 4 MV  

UU05 – 5 MV  

UU06 – Any MV  

UW07 – Any MV (no MV should be on more than two uncommon creatures)


Keywords found in blue at uncommon (with the defaults in number listed beside them):


* Defender (0–1, this isn't counted as a creature)
* Flash (0–1)
* Flying (2–3 fliers, try not to repeat stats, at least one is usually larger)
* Hexproof (0–1, can appear on slightly larger creature at uncommon, sometimes conditional)

**Uncommon Spells**


UU08 – Card draw  

UU09 – Counterspell  

UU10 – Non-creature  

UU11 – Non-creature  

UU12 – Non-creature  

UU13 – Non-creature


Some options for the non-creature spells:


* Card draw (either drawing more cards than at common or repeatable)
* Creature stealing (usually with some limitations)
* Milling effect (most often repeatable)
* Bouncing multiple targets (returning things to their owner's hand)
* Freezing multiple targets (tapping things that don't untap next turn)
* Creature transformation
* Tapping or untapping permanents (often repeatable)
* An Aura or Equipment

Black
-----


**Common Creatures**


CB01 – 1 MV  

CB02 – 2 MV  

CB03 – 2 MV  

CB04 – 2 or 3 MV  

CB05 – 3 MV  

CB06 – 3 MV  

CB07 – 4 MV  

CB08 – 4 MV  

CB09 – 5 MV  

CB10 – 6+ MV


Keywords found in black at common (with the defaults in number listed beside them):


* Deathtouch (1)
* Defender (0–1, this isn't counted as a creature)
* Flash (1, on a low toughness creature)
* Flying (1)
* Haste (0–1)
* Indestructible (0–1, only granted temporarily by an activation or spell)
* Lifelink (1, power 3 or less)
* Menace (1)

**Common Spells**


CB11 – Removal spell, can kill anything  

CB12 – Removal spell, can kill small things  

CB13 – Removal spell, edict (forced sacrifice), or conditional  

CB14 – Removal spell, limitations, different from the others, usually weaker  

CB15 – Card draw (for some resource in addition to mana, usually life)  

CB16 – Return creature card from graveyard to hand (one or two creatures)  

CB17 – Discard (one or two cards, if you choose what gets discarded, not land)  

CB18 – Positive Aura or combat trick  

CB19 – Anything


**Uncommon Creatures**


UB01 – 1 or 2MV  

UB02 – 2 MV  

UB03 – 3 MV  

UB04 – 4 MV  

UB05 – 5 MV  

UB06 – Any MV (no more than two creatures at uncommon should have the same MV)  

UB07 – Any MV


Keywords found in black at uncommon (with the defaults in number listed beside them):


* Deathtouch (1)
* Defender (0–1, this isn't counted as a creature)
* Flash (0–1)
* Flying (1)
* Indestructible (0–1, only granted temporarily by an activation or spell)
* Lifelink (1)
* Menace (1)

**Uncommon Spells**


UB08 – Removal  

UB09 – Reanimation  

UB10 – Non-creature  

UB11 – Non-creature  

UB12 – Non-creature  

UB13 – Non-creature


Some options for the non-creature spells:


* A mass-removal spell that kills smaller things
* A tutor (searching your library for a card and putting it into your hand)
* A discard effect (that can be larger than common or repeatable)
* Draining creatures or players (dealing damage and gaining an equal amount of life, often repeatable)
* Exiling cards in graveyards (sometimes for an effect)
* Removing counters
* An Aura or Equipment

Red
---


**Common Creatures**


CR01 – 1 MV  

CR02 – 2 MV  

CR03 – 2 MV  

CR04 – 2 MV  

CR05 – 3 MV  

CR06 – 3 MV  

CR07 – 4 MV  

CR08 – 4 MV  

CR09 – 5 MV  

CR10 – 5+ MV


Keywords found in red at common (with the defaults in number listed beside them):


* Defender (0–1, this isn't counted as a creature)
* First strike (1, sometimes only on your turn or on attack)
* Haste (1–2)
* Menace (1)
* Reach (0–1)
* Trample (1)

**Common Spells**


CR11 – Efficient direct-damage spell (usually one of this and CB12 is any target)  

CR12 – Other direct-damage spell  

CR13 – Steal effect/inefficient direct damage  

CR14 – Team pump (power greater than toughness)/land destruction  

CR15 – Cantrip (draw a card rider)/card filtering (usually rummaging—discard and draw)  

CR16 – Positive Aura or Equipment  

CR17 – Combat trick  

CR18 – Can't block/destroy artifact/direct damage to player  

CR19 – Anything


**Uncommon Creatures**


UR01 – 1 or 2MV  

UR02 – 2 MV  

UR03 – 3 MV  

UR04 – 4 MV  

UR05 – 5+ MV  

UR06 – Any MV (no more than two creatures at uncommon should have the same MV)  

UR07 – Any MV


Keywords found in red at uncommon (with the defaults in number listed beside them):


* Defender (0–1, this isn't counted as a creature)
* Double Strike (0–1, usually only one of this and first strike)
* Haste (1)
* First strike (0–1)
* Menace (1)
* Reach (0–1)
* Trample (1–2)

**Uncommon Spells**


UR08 – Direct damage (most often any target)  

UR09 – Small sweeper/multi-target direct damage  

UR10 – Non-creature  

UR11 – Non-creature  

UR12 – Non-creature  

UR13 – Non-creature


Some options for the non-creature spells:


* Temporary creature stealing (usually only one between common and uncommon)
* Rummaging (sometimes repeatable)
* Making creatures fight
* Pumping your team (usually with an enchantment, grants more power than toughness)
* Spell copying
* Getting back instants or sorceries (sometimes casting them from the graveyard)
* An Aura or Equipment

Green
-----


**Common Creatures**


CG01 – 1 MV  

CG02 – 2 MV  

CG03 – 2 MV  

CG04 – 3 MV  

CG05 – 3 MV  

CG06 – 3 OR 4 MV  

CG07 – 4 MV  

CG08 – 4 MV  

CG09 – 5 MV  

CG10 – 5 OR 6 MV  

CG11 – 6+ MV


Keywords found in green at common (with the defaults in number listed beside them):


* Deathtouch (1, usually on a smaller creature)
* Defender (0–1, this isn't counted as a creature)
* Flash (0–1, usually on a creature with power 3 or higher)
* Haste (1)
* Hexproof (0–1, usually on a small or medium creature without evasion)
* Reach (1)
* Trample (1–2)
* Vigilance (1)

**Common Spells**


CG12 – Fight or bite (dealing damage equal to power)  

CG13 – Power/toughness pumping (usually on an instant)  

CG14 – Another combat trick  

CG15 – Cantrip/card filtering  

CG16 – Positive Aura or Equipment  

CG17 – Anti-flying  

CG18 – Mana ramp (usually fetching land, but sometimes an Aura)  

CG19 – Artifact or enchantment destruction


**Uncommon Creatures**


UG01 – 1 or 2MV  

UG02 – 2 MV  

UG03 – 3 MV  

UG04 – 4 MV  

UG05 – 5 MV  

UG06 – 6+ MV  

UG07 – Any MV (no more than two creatures at uncommon should have the same MV)  

UG08 – Any MV


Keywords found in green at uncommon (with the defaults in number listed beside them):


* Deathtouch (0–1)
* Defender (0–1, this isn't counted as a creature)
* Flash (0–1, usually on a creature with power 3 or higher)
* Haste (1)
* Indestructible (0–1)
* Hexproof (0–1, usually on a small or medium creature without evasion)
* Reach (0–1)
* Trample (1)
* Vigilance (1)

**Uncommon Spells**


UG09 – Mana ramp (usually creating more mana than mana-ramp commons)  

UG10 – Non-creature  

UG11 – Non-creature  

UG12 – Non-creature  

UG13 – Non-creature


Some options for the non-creature spells:


* Regrowth (getting any card back from graveyard to hand)
* Token making (usually of tokens bigger than 1/1)
* Fight or bite (uncommon is usually stronger than the common one if both exist)
* Power/toughness pumping (either to many creatures or a larger pump to one creature)
* Granting of +1/+1 counters
* Artifact and/or enchantment destruction
* An Aura or Equipment

Multicolor
----------


It's default in sets for uncommon to have a full ten-card cycle of creatures to act as draft "signposts," that is, cards that helped communicate to players what each two-color archetype is doing in the draft. The card also allows you to draft around it if you draft it early. The slots don't always have to be creatures, but we tend to start there as the default.


UZ01 – Creature  

UZ02 – Creature  

UZ03 – Creature  

UZ04 – Creature  

UZ05 – Creature  

UZ06 – Creature  

UZ07 – Creature  

UZ08 – Creature  

UZ09 – Creature  

UZ010 – Creature


If you're unsure of what your Draft archetypes are early on, just make these generic good cards for early playtests.


Artifacts
---------


**Common Creatures**


As I said above, the default is to have three artifact creatures at common.


CA01 – 1 or 2 MV  

CA02 – 3 or 4 MV  

CA03 – 5 or 6 MV


Keywords found in artifacts at common (with the defaults in number listed beside them):


* Defender (0–1, this isn't counted as a creature)
* Flash (0–1, usually on a creature with power 3 or higher)
* Flying (1)
* Haste (0–1)
* Trample (0–1)
* Vigilance (0–1)

Other keywords can be used. These are the ones we tend to use the most often on common artifact creatures. The same is true for uncommon.


**Common Spells**


CA04 – Equipment  

CA05 – Land fetching/color fixing  

CA06 – Mana production


**Uncommon Creatures**


UA01 – 1 or 2 MV  

UA02 – 3 or 4 MV  

UA03 – 5 or 6 MV


Keywords found in artifacts at uncommon (with the defaults in number listed beside them):


* Defender (0–1, this isn't counted as a creature)
* Flash (0–1, usually on a creature with power 3 or higher)
* Flying (1)
* Haste (0–1)
* Trample (0–1)
* Vigilance (0–1)

**Uncommon Spells**


UA04 – Removal (often conditional and usually costed somewhat inefficiently)  

UA05 – Non-creature  

UA06 – Non-creature


Some options for the non-creature spells:


* Equipment
* Evasion granting (often repeatable)
* Card drawing (often repeatable)
* Creature pumping (often repeatable)

Remember that these slots are colorless. Colored artifacts should be counted in the colored slots.


Mixing in Lands
---------------


If you find your set needs nonbasic lands, there are several ways to add them to your design skeleton. First, you can swap any colorless slot for a land. Second, you can remove a card of each color to add a cycle of lands. Third, you can add nonbasic lands to the basic land slot, and it can be at some ratio other than 100%. If you do this, it doesn't remove anything from the design skeleton, although you probably want to indicate that somewhere.


Rank and Set File
=================


That is the default design skeleton for common and uncommon. I know today's column was super technical, but I hope it will be a big boon for all the amateur *Magic* designers out there. As always, I'm eager for your feedback on today's column. You can [email](mailto:making.magic@hotmail.com) me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).


Join me next week for the start of the design story for *Strixhaven: School of Mages*.


Until then, may you have fun making your own *Magic* sets.




 

##### 
 #817: Invasion with Bill Rose






##### 
 #817: Invasion with Bill Rose


32:45



I sit down with the senior vice president of tabletop *Magic*, Bill Rose, to talk about the design of *Invasion*.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork817_invasionwithbill_su76f6sD.mp3)



  


 

##### 
 #818: From the Vault






##### 
 #818: From the Vault


32:04



In this podcast, I talk about the *From the Vault* product line.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork818_fromthevault_Jsu73yDh.mp3)




* [**Episode 816**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork816_innsitradwitherik_sh36dSse.mp3) *Innistrad* with Erik Lauer
* [**Episode 815**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork815_trivialongestnames_Dseu3DsD.mp3) Trivia – Longest Names
* [**Episode 814**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork814_triviashortestnames_us32AsdD.mp3) Trivia – Shortest Names







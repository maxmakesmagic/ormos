
---
[Link to Wayback Machine](https://web.archive.org/web/20210720102027/https://magic.wizards.com/en/articles/archive/making-magic/dungeon-tales-part-1-2021-07-19?utm_source=dlvr.it&utm_medium=twitter)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Every story needs compelling characters. For Adventures in the Forgotten Realms, that means each card had its own story to tell."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1555173"
[_metadata_:publish_date]:- "2021-07-19"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Dungeon Tales, Part 1"
[_metadata_:wayback_capture_timestamp]:- "2021-07-20 10:20:27"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210720102027id_/https://magic.wizards.com/en/articles/archive/making-magic/dungeon-tales-part-1-2021-07-19?utm_source=dlvr.it&utm_medium=twitter"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/dungeon-tales-part-1-2021-07-19?utm_source=dlvr.it&utm_medium=twitter"
---


Dungeon Tales, Part 1
=====================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on July 19, 2021 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Over the last two weeks, I talked about the overall design of *Dungeons & Dragons: Adventures in the Forgotten Realms* (see [part one](https://magic.wizards.com/en/articles/archive/making-magic/dd-esign-part-1-2021-07-05) and [part two](https://magic.wizards.com/en/articles/archive/making-magic/dd-esign-part-2-2021-07-12)). That means this week (and next), I'll be sharing design stories for individual cards.


I wasn't on any of the design teams, but I do have access to Drake (our card database that tracks all the changes that happen to a card), so I'm going to explore the evolution of several legendary cards from the set. I tried to pick cards that were popular D&D characters *and* went through some interesting evolutions.


**Drizzt Do'Urden**


![Drizzt Do'Urden](https://media.wizards.com/2021/afr/en_bEEL983ifV.png)![Alt Drizzt Do'Urden](https://media.wizards.com/2021/afr/en_EsMIq1FMyL.png)


It seems only appropriate to start with what is probably the best-known character from D&D (thanks to a series of wonderful novels by R. A. Salvatore), Drizzt Do'Urden. Drizzt is a drow (dark elf) ranger that has become the hero of the North. He's best known for two things: being an excellent fighter and having a black panther companion named Guenhwyvar. Those were the two things the designers knew they had to capture in his card. In fact, the very first version of Drizzt's card in the file was simply the following:


**Drizzt (version #1)**  

(g/w)  

Legendary Creature — Elf Warrior Scout  

2/2  

Double strike  

Create a legendary Cat token.


We write the green-white hybrid symbol as (g/w) in card files. In this case, it's not being used to signify that this card costs hybrid mana but rather that it's a green and white card. Sometimes early on, when we don't quite know what the card is going to be yet but want to create a slot in the file for it, we list one mana symbol to indicate what color the slot will be. For two-color cards, we use a hybrid symbol.


What this partially filled-in card meant is Drizzt was going to have one or more combat abilities and create a legendary Cat creature token. Let's look at version two.


**Drizzt (version #2)**  

2GW  

Legendary Creature — Elf Warrior Scout  

2/2  

At the beginning of your end step, if you don't control a creature named Guenhwyvar, create a 2/2 green legendary Cat creature token named Guenhwyvar.  

GW: Target Cat and CARDNAME gain double strike until end of turn. (You can't activate this ability without targeting a Cat.)


The second version is the first to define Guenhwyvar (as a 2/2). It makes use of a mechanic I first used on a card called [Spirit Mirror](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spirit+Mirror) all the way back in the first set I led, *Tempest*. It creates a specific token each turn as a trigger, but only if you don't already have one. This version makes the double strike an activated ability, but it requires that you have both Drizzt and Guenhwyvar on the battlefield (technically, it merely requires another Cat). After playtesting showed having to target both was a bit frustrating, they changed the second ability to:


1GW: CARDNAME and up to one target Cat gain double strike until end of turn.


The next version changed up a few things:


**Drizzt (version #3)**  

1GW  

Legendary Creature — Elf Warrior Scout  

1/1  

Double strike  

When CARDNAME enters the battlefield, create Guenhwyvar, a 3/3 green legendary Cat creature token.  

4GW: CARDNAME and Guenhwyvar each get +X/+X until end of turn, where X is the other's power.


For starters, Drizzt is back to having double strike without needing to activate it. He also gets cheaper and a little smaller, but as you'll see, the card does give him a way to offset that. Guenhwyvar is now a 3/3 rather than a 2/2 but no longer has the respawning trigger. You only get one Guenhwyvar. Finally, the card gets an activated ability that allows you to make either Drizzt or Guenhwyvar bigger. Without outside assistance, the ability turns Drizzt from a 1/1 to a 3/3 which allows him to deal 4 additional damage with his double strike.


Which brings us to version four:


**Drizzt (version #4)**  

3GW  

Legendary Creature — Elf Warrior Scout  

3/3  

Haste, vigilance, double strike, lifelink, trample, reach, armor {o3}  

Whenever a creature with greater power than CARDNAME dies, put a number of +1/+1 counters on CARDNAME equal to the difference.


This version costs a little more but gives Drizzt a whole mess of creature abilities, basically everything you can get from green or white that flavorfully made sense. (Okay, I guess they could have given him flash.) Armor is ward, by the way. It didn't have its final name yet.


They then gave him a second ability that let him grow over time. I'm not sure how serious this version was, because it doesn't make a Guenhwyvar creature token, which was one of the two requirements of the card. (It's possible they briefly toyed with giving Guenhwyvar his own card.)


This leads to version five:


**Drizzt (version #5)**  

3GW  

Legendary Creature — Elf Warrior Scout  

3/3  

Double strike, reach, trample, armor {o2}  

When CARDNAME enters the battlefield, create Guenhwyvar, a legendary 4/1 green Cat creature token. Whenever a creature with power greater than CARDNAME dies, put a number of +1/+1 counters on CARDNAME equal to the difference.


This version is a cleaned-up design of the fourth. It reduces the number of creature abilities and adds Guenhwyvar, now a 4/1. It's close to the final version. Drizzt loses reach, trample, and armor and gains the Ranger creature type. There was a bunch of back and forth over whether we should add Ranger as a creature type, but in the end, it was decided it's something we should add to *Magic*. (And yes, we will see Ranger in future non-D&D *Magic* sets.)


**Eye of Vecna, Hand of Vecna, and The Book of Vile Darkness**


![Eye of Vecna](https://media.wizards.com/2021/afr/en_1RVmktB1oj.png)![Hand of Vecna](https://media.wizards.com/2021/afr/en_04gTdIqblm.png)![The Book of Vile Darkness](https://media.wizards.com/2021/afr/en_KjFx5Hwwqe.png)


![Alt Eye of Vecna](https://media.wizards.com/2021/afr/en_HecLV31uTM.png)![Alt Hand of Vecna](https://media.wizards.com/2021/afr/en_xgRr24jiLd.png)![Alt The Book of Vile Darkness](https://media.wizards.com/2021/afr/en_T7GpLWlcYX.png)


Vecna was a lich, formerly human, that ascended to godhood on Oerth. He was the author of a very evil book called The Book of Vile Darkness. He was killed by his lieutenant, and all that remains of him are an eye and a hand.


The Eye of Vecna, The Hand of Vecna, and The Book of Vile Darkness are all famous artifacts in D&D. The Eye and Hand would give you power but forced you to replace your existing eye or hand with it. The Book taught evil people magic, but it was so evil that it could harm non-evil people, even by them looking at it. We knew we wanted artifacts for each of these three objects as they were fan favorites.


We'll start with the Eye and the Hand, as they began design connected:


**Eye of Vecna (version #1)**  

1  

Legendary Artifact — Equipment  

Whenever equipped creature attacks, reveal the top card of your library, then draw X cards and lose X life, where X is that card's converted mana cost.  

Whenever CARDNAME becomes unattached from a permanent, destroy that permanent.  

Equip 3


**Hand of Vecna (version #1)**  

2  

Legendary Artifact — Equipment  

Whenever equipped creature attacks, it gets +X/+X until end of turn, where X is the number of cards in your hand. Whenever CARDNAME becomes unattached from a permanent, destroy that permanent.  

Equip 3


Both the Eye of Vecna and the Hand of Vecna start as Equipment. The design team thought this would capture the flavor of them being used. Both had the rider that the equipped creature would die if the Equipment ever became unattached. The two were designed to be synergistic, as the Eye draws cards, and the Hand gets stronger the larger your hand is. The first version of The Book of Vile Darkness was created to work with the Eye and Hand:


**The Book of Vile Darkness (version #1)**  

2BB  

Legendary Artifact  

Whenever a spell or ability you control causes you to lose life, each opponent loses that much life.  

T: Reveal the top card of your library. Put it into your hand and you lose life equal to its level. (A card's level is the amount of mana it costs to play.)


The life loss from the Eye can trigger the first ability, and the second ability draws cards to help the Hand. I'll note that this card was designed so even if you just have The Book of Vile Darkness, the second ability can be used to trigger the first.


Both the Eye of Vecna and the Hand of Vecna shift away from being Equipment in their next versions:


**Eye of Vecna (version #2)**  

3  

Legendary Artifact  

Each card you discard while casting a spell pays for {o1} or one mana of that card's color.  

You may look at the top card of your library any time. You may cast it if you discard another card of the same level as part of the cost to do so.


**Hand of Vecna (version #2)**  

5  

Legendary Artifact  

Whenever you draw a card, you lose 1 life. At the beginning of your end step, if you have fewer than five cards in hand, draw cards equal to the difference. If you have more than five, discard cards equal to the difference.


The new versions are again made to be synergistic, but in different ways. The Eye lets you discard cards to cast spells, and the Hand helps you refill your hand. You'll note the word "level" shows up on a bunch of the cards today. The Set Design team used it as a replacement for "mana value" (at the time, "converted mana cost"). We'd been looking to change "converted mana cost" for many years, so the *Adventures in the Forgotten Realms* team pitched "level."


The Book of Vile Darkness finds a new way to tie the three cards together, this time a little more bluntly:


**The Book of Vile Darkness (version #2)**  

2BB  

Legendary Artifact  

At the beginning of your end step, each opponent loses life equal to the amount of life you lost this turn.  

{oB}, {oT}: Draw a card and reveal it. You lose life equal to its base cost. If you control artifacts named Hand of Vecna and Eye of Vecna, exile them and CARDNAME and create an 8/8 black legendary Zombie Wizard creature token named Vecna. It gains indestructible and all of their abilities.


The Book uses the life loss from the Hand to hurt each opponent. It also allows you to get a Vecna creature token if you manage to get all three objects on the battlefield together. Note that Vecna is an 8/8 indestructible creature that has the abilities of all three cards, so there's no loss of functionality when you create Vecna. This is the earliest in the file that Vecna shows up as a creature token.


The Eye of Vecna went through the most changes.


**Eye of Vecna (version #3)**  

3  

Legendary Artifact  

Discard a card: Add {oC} or one mana of one of the discarded card's colors. You may look at the top card of your library at any time. You may cast it if you spend at least one mana produced by CARDNAME to do so.


This version keeps the "discard to produce mana" function and allows you to cast cards off the top of your library but changes up how each works.


**Eye of Vecna (version #4)**  

4  

Legendary Artifact  

T, Pay X life: Scry X, then draw a card.


The next version tries something completely different. What if it helps you draw better cards?


**Eye of Vecna (version #5)**  

4  

Legendary Artifact  

You may look at the top card of your library any time.  

{oT}: You may pay 1 life. If you do, put the top card of your library on the bottom. Draw a card.


**Eye of Vecna (version #6)**  

3  

Legendary Artifact  

At the beginning of your upkeep, look at the top card of your library. You may pay 3 life, if you do, draw a card. Otherwise, mill a card.


Versions five and six have the same basic goals as version four, but execute them a bit differently.


**Eye of Vecna (version #7)**  

2  

Legendary Artifact  

Whenever CARDNAME enters the battlefield or you discard a card, you may pay 2 life. If you do, draw a card.


**Eye of Vecna (version #8)**  

1  

Legendary Artifact  

Whenever CARDNAME enters the battlefield or you discard a card, you may pay {o1} and 3 life. If you do, draw a card.


Versions seven and eight create synergies with discarding, allowing you to turn discards into loots. Keeping with the flavor, there's always some life loss involved. The final version turns into more of a card-drawing card.


Hand of Vecna, meanwhile, goes back to becoming an Equipment:


**Hand of Vecna (version #3)**  

2  

Legendary Artifact — Equipment  

Equipped creature gets +X/+0, where X is the number of cards in your hand.  

Equip {o2} and 2 life


It again rewards you for having cards in hand by boosting your power (although no longer boosts your toughness). It also starts experimenting with alternate equip costs, in this case life.


**Hand of Vecna (version #4)**  

2  

Legendary Artifact — Equipment  

At the beginning of combat on your turn, equipped creature or a creature you control named Vecna gets +X/+0 until end of turn, where X is the number of cards in your hand.  

Equip Sacrifice a creature and pay 1 life


The next version has two differences. First, it allows you to boost the equipped creature *and* Vecna. (Remember that Vecna has all the abilities of the three artifacts.) Second, it experiments with creature sacrifice as an equip cost.


**Hand of Vecna (version #5)**  

3  

Legendary Artifact — Equipment  

At the beginning of combat on your turn, equipped creature or a creature you control named Vecna gets +X/+X until end of turn, where X is the number of cards in your hand.  

Equip {o1} and pay 1 life


The next version went back to +X/+X and mana, along with the life, as an equip cost. This is close to the final version, but the printed card has two different equip costs, one which is just life and one which is just mana rather than a single cost that combines them.


The Book also went through several changes:


**The Book of Vile Darkness (version #3)**  

1B  

Legendary Artifact  

XB: Return target creature card with base cost X from your graveyard to the battlefield. If it would leave the battlefield, exile it instead of putting it anywhere else.  

T, Exile artifacts you control named The Book of Vile Darkness, Hand of Vecna, and Eye of Vecna: Create an 8/8 black legendary Zombie Wizard creature token named Vecna. It has indestructible and all of the abilities of the exiled cards.


To capture the flavor of the Book being able to raise the dead, it now has an activated animation ability.


**The Book of Vile Darkness (version #4)**  

2B  

Legendary Artifact  

At the beginning of each end step, create a 2/2 black Zombie creature token if you lost life this turn.  

T, Exile artifacts you control named The Book of Vile Darkness, Hand of Vecna, and Eye of Vecna: Create an 8/8 black legendary Zombie Wizard creature token named Vecna. It has indestructible and all of the abilities of the exiled cards.


The next version makes 2/2 Zombies instead of reanimating creatures out of the graveyard. This is close to the final version except it triggers off any amount of life loss. The final card requires you to lose 2 or more life.


The printed versions of all three cards create a nice synergy. The Eye can draw you cards and help you spend life, the Hand can turn cards in hand into damage through creature pumping, and the Book can turn the life loss into Zombie creature tokens, which you can equip with the hand. All three combo to get you Vecna. I think the designers did a good job giving each object the proper flavor while mechanically tying them all together.


**Farideh, Devil's Chosen**


![Farideh, Devil's Chosen](https://media.wizards.com/2021/afr/en_IXiUmWDx5i.png)![Alt Farideh, Devil's Chosen](https://media.wizards.com/2021/afr/en_s7qbBHZo95.png)


Farideh is a Tiefling (a humanoid with devilish influences) warlock who accidentally made a pact with an evil character (a half-fiend named Lorcan). Here's how her card began its design:


**\_\_\_\_\_\_\_\_, Learned Wizard (version #1)**  

2UR  

Legendary Creature — Wizard  

3/2  

When CARDNAME enters the battlefield, return target instant or sorcery card from your graveyard to your hand. If that card is level 3 or lower, you may cast it without paying its mana cost.


Interestingly, this slot didn't start as a top-down design for Farideh but rather a bottom-up design playing into blue-red's spell theme. Again, "level" was being used in place of mana value.


**\_\_\_\_\_\_\_\_, Learned Wizard (version #2)**  

UR  

Legendary Creature — Wizard  

2/2  
*Grant an Advantage* – If you would roll a die, instead roll two of those dice and ignore one of those results.


The second version is when the card shifted to start caring about rolling a d20. The first attempt is basically the card [Krark's Other Thumb](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krark%27s+Other+Thumb) (from *Unstable*). Like many of the cards in the set, it was given flavor words to help describe what this effect meant in the world. Note that the card is still an unnamed Wizard.


**\_\_\_\_\_\_\_\_, Wild Magic Sorcerer (version #3)**  

2UR  

Legendary Creature — Shaman  

3/3  
*Grant an Advantage* – If you would roll a die, instead roll two of those dice and ignore one of those results.  

At the beginning of combat on your turn, roll a twenty-sided die. If you succeed (10+), target creature gains flying and haste until end of turn.


The next version, still unnamed, added a second ability, one that used die rolling, so that the first ability was meaningful even if you didn't have another die-rolling card. It also made her more expensive and gave her larger stats.


**Farideh, Chosen of Asmodeus (version #4)**  

UR  

Legendary Creature — Tiefling Warlock  

3/2  

Flying, haste  
*Grant an Advantage* – If you would roll a die, instead roll two of those dice and ignore one of those results. Whenever CARDNAME attacks, roll a twenty-sided die. If you succeed (10+), untap target permanent you control.


The card finally becomes Farideh, and the die-rolling effect changes from granting her an ability to helping you reuse a permanent by untapping it. The mana cost drops again, and the card loses a toughness.


**Farideh, Chosen of Asmodeus (version #5)**  

1UR  

Legendary Creature — Tiefling Warlock  

2/2  
*Grant an Advantage* – If you would roll a die, instead roll two of those dice and ignore one of those results.  

Whenever you roll dice, CARDNAME gets +1/+0 and gains flying and menace until end of turn.


It was decided that this was going to be an uncommon build-around for blue-red, so the card goes back to requiring other die-rolling cards to be effective. It helps die rolling and getting rewarded for die rolling. Again, the mana cost and stats are tweaked.


**Farideh, Chosen of Asmodeus (version #6)**  

1UR  

Legendary Creature — Tiefling Warlock  

1/4  
*Grant an Advantage* – If you would roll one or more dice, instead roll that many dice plus one and ignore one.  

Whenever you roll one or more dice, CARDNAME gets +2/+0 and gains flying and menace until end of turn.


This version has smaller tweaks. The power/toughness goes from 2/2 to 1/4. The die-rolling modifier gets tweaked, so it's clearer what happens when you roll more than one die. (I assume the team was messing around with cards that rolled more than one die at this time.) Finally, the second ability gets a bigger boost.


**Farideh, Chosen of Asmodeus (version #7)**  

1UR  

Legendary Creature — Tiefling Warlock  

1/4  

Flying, menace  
*Grant an Advantage* – If you would roll one or more dice, instead roll that many dice plus one and ignore one.  

Whenever you roll one or more dice, CARDNAME gets +1/+0 until end of turn and you draw a card.


This version gets flying and menace standard, shrinks the bonus, and adds card drawing to the mix.


**Farideh, Chosen of Asmodeus (version #8)**  

1UR  

Legendary Creature — Tiefling Warlock  

2/2  

Flying, menace  

Whenever you roll one or more dice, also get the result here,  

1-9 | Put a +1/+1 counter on CARDNAME.  

10-19 | Draw a card.  

20+ | CARDNAME deals damage equal to its power to target creature or planeswalker an opponent controls.


The next version gives Farideh a die-rolling chart. Farideh has a fireball spell in the set which has a die-rolling chart, so I assume the design team thought it would be cool to give her one, too. Again, the stats are tweaked.


**Farideh, Chosen of Asmodeus (version #9)**  

1UR  

Legendary Creature — Tiefling Warlock  

2/2  

Flying, menace  

Whenever you roll one or more dice, put a +1/+1 counter on CARDNAME. If you rolled a 10 or higher, draw a card.


This version finally has her stop affecting die rolls and just makes her affected by them. This version is close to the printed version except it grants a +1/+1 counter instead of temporarily granting flying and menace. The finished version also raises her mana cost and her stats from 2/2 to 3/3.


**Minsc, Beloved Ranger**


![Minsc, Beloved Ranger](https://media.wizards.com/2021/afr/en_SBXtB8hn2t.png)![Alt Minsc, Beloved Ranger](https://media.wizards.com/2021/afr/en_5Djm7BuF7E.png)


Minsc is a kind-hearted ranger with a hamster companion named Boo. Minsc believes Boo is a miniature giant space hamster. There was a period in the story where Boo accidentally drank a potion of growth and got very large. Minsc and Boo are much beloved, so we knew we wanted to give them a card.


**Minsc, Hero of Baldur's Gate (version #1)**  

2RW  

Legendary Creature — Human Ranger  

3/3  

Whenever CARDNAME attacks, create a legendary Hamster creature token named Boo with "Whenever this deals combat damage to a player, that player discards a card at random then draws a card" that's tapped and attacking. Exile that token at the end of combat. Whenever Boo becomes blocked, CARDNAME gets +2/+2 and gains first strike until end of turn.


I believe there were two demands on the card from the start. One, it had to create a Boo creature token; and two, there had to be some way for the card to make Boo larger. This first stab was a red-white card (as were most of the incarnations of the design) that created Boo when the card was attacking. Almost all the abilities of the card are about what Boo does. Note that this has the creature type Ranger. Ranger wasn't yet a creature type, but you can see whoever made this card was trying to pitch that it should be.


**Minsc, Hero of Baldur's Gate (version #2)**  

2RW  

Legendary Creature — Human Ranger  

3/4  

When CARDNAME enters the battlefield, create a 1/1 red legendary Hamster creature token named Boo. Whenever a Hamster you control deals combat damage to a player, put a +1/+1 counter on CARDNAME.


The next version just has Minsc make the Boo token when it enters the battlefield. This version doesn't have any way to make Boo larger but does allow Boo to make Minsc larger. Minsc also gains a toughness.


**Minsc, Hero of Baldur's Gate (version #3)**  

1RW  

Legendary Creature — Human Scout  

3/3  

When CARDNAME enters the battlefield, create a 1/1 red legendary Hamster creature token named Boo with first strike and menace. Whenever a Hamster you control deals combat damage to a player, put a +1/+1 counter on CARDNAME.


This version gives the Boo creature token first strike and menace and makes Minsc cheaper, although drops it back to a 3/3. Note that the creature type changes to Scout. This is because Ranger wasn't yet a creature type and they were trying to get the design closer to what they think will be the printed version.


**Minsc, Hero of Baldur's Gate (version #4)**  

RW  

Legendary Creature — Human Scout  

2/1  

When CARDNAME enters the battlefield, create Boo, a legendary 1/1 red Hamster creature token with menace.  

Whenever a Hamster you control deals combat damage to a player, put a +1/+1 counter on CARDNAME. Then, if CARDNAME has five or more +1/+1 counters on it, untap it, and after this phase there is an additional combat phase. Only CARDNAME can attack that combat.


This version shrinks Minsc to a two-drop 2/1, Boo loses first strike, and the design team tries out a [Relentless Assault](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Relentless+Assault)-like extra attack mechanic once Minsc gets big enough.


There were a lot of changes between this and the final version. Minsc goes from being a two-color to a three-color card (I assume to make him a better Commander), and Boo loses menace for trample and haste. (I'm kind of surprised it took so many versions for Boo to get haste—yes, I guess the first version sort of had haste.) Everything else is dropped so that we can get back to the thing the design team wanted from the beginning: the ability for Minsc to make Boo bigger. The power is expanded now so that it works on any creature, not just Boo. Adding the Giant creature type is a nice nod to the giant space hamster reference in D&D.


The End of Today's Adventure
============================


That's all the time I have for today. As always, I'm eager to hear your thoughts on today's article, any card I talked about, or about *Adventures in the Forgotten Realms* in general. You can [email](mailto:making.magic@hotmail.com) me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).


Join me next week when I share more card-by-card design stories from *Adventures in the Forgotten Realms*.


Until then, may you have your own D&D adventures with the new set.




 

##### 
 #851: Dominaria with Kelly Digges






##### 
 #851: Dominaria with Kelly Digges


31:06



I sit down with former R&D member Kelly Digges to talk about the making of *Dominaria*.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork851_domwithkelly_nw7dhhwy.mp3)



  


 

##### 
 #852: Creature Tokens, Part 1






##### 
 #852: Creature Tokens, Part 1


31:01



In this podcast, I talk about the history of creature tokens in *Magic*.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork852_tokenspart1_2377sdhd.mp3)




* [**Episode 850**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork850_faeries_suwed76D.mp3) Faeries
* [**Episode 849**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork849_futwithmike_j3sdy7sd.mp3) *Future Sight* with Mike Turian
* [**Episode 848**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2021/podcasts/magic/drivetowork848_minimaster_J3hsdyfw.mp3) Mini-Master







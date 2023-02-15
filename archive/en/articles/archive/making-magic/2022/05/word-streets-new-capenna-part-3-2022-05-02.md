
---
[Link to Wayback Machine](https://web.archive.org/web/20220502150709/https://magic.wizards.com/en/articles/archive/making-magic/word-streets-new-capenna-part-3-2022-05-02)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark concludes his card-by-card design stories from Streets of New Capenna."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1586550"
[_metadata_:publish_date]:- "2022-05-02"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Word on the Streets of New Capenna, Part 3"
[_metadata_:wayback_capture_timestamp]:- "2022-05-02 15:07:09"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220502150709id_/https://magic.wizards.com/en/articles/archive/making-magic/word-streets-new-capenna-part-3-2022-05-02"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/word-streets-new-capenna-part-3-2022-05-02"
---


Word on the Streets of New Capenna, Part 3
==========================================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on May 2, 2022 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






The last two weeks ([Part 1](https://magic.wizards.com/en/articles/archive/making-magic/word-streets-new-capenna-part-1-2022-04-18) and [Part 2](https://magic.wizards.com/en/articles/archive/making-magic/word-streets-new-capenna-part-2-2022-04-25)), I've been sharing card-by-card design stories from *Streets of* *New Capenna*, but there's more to tell, so today will be the third and final part of this series.


**Strangle**


![Strangle](https://media.wizards.com/2022/snc/en_Jw0SmvsI7Z.png)


In past columns on card-by-card design stories, I've tended to focus on higher rarity cards, planeswalkers, and legendary creatures. However, some have commented that they want to hear more stories about the lower rarity cards, so I decided to tell the story of Strangle, a cool little red common. What I was not prepared for when I dug into its past was how long and convoluted its design was. Who could have guessed that this simple common would have the longest design story of any single card in *Streets of New Capenna*?


**[Gangland Hit] (version #1)**  

5R  

Instant  

CARDNAME deals 5 damage to target creature or planeswalker. Its controller sacrifices a land.


This card started as a common red direct-damage spell that dealt damage to creatures or planeswalkers (but not players). Interestingly, it didn't begin as a one-drop but as a six-drop. This was obviously designed exclusively for Limited as no one would ever pay six mana for removal in a tournament Constructed format. We do like having expensive common removal cards that don't get picked so highly in Draft to help them float to the people who are a little more desperate for removal. I assume it was a forced sacrifice instead of a targeted removal because this is a three-color environment and we want to be careful with land destruction. The forced sacrifice slows down overall mana without specifically "color hosing" (denying access to a specific color) the opponent.


**[Illegal Explosives] (version #2)**  

4RR  

Instant  

Smuggle (3, Exile this card from your hand face down: Create a Treasure token. It's an artifact with "T, Sacrifice this artifact: Add one mana of any color." You may still play this card from exile.)  

CARDNAME deals 5 damage to target creature or planeswalker. It deals 3 damage to that permanent's controller if mana from a Treasure was spent to cast CARDNAME.


The next version made use of a sixth mechanic, smuggle, we had early in design. The idea behind smuggle was a means to help people with color fixing, allowing them to play three-color spells. *Khans of Tarkir*, the set *Streets of New Capenna* used as its model, had morph, which allowed players to have access to a 2/2 creature while waiting to get their third color mana. The Vision Design team explored having a new sixth non-faction mechanic that also helped enable the three-color environment. The smuggle mechanic allowed you to spend three generic mana and exile the card from your hand to get a Treasure artifact token. The exiling was a way to limit the Treasure-making to one use. The card still did five damage to a creature or planeswalker but had a rider that you acquired for using Treasure to cast the spell.


**[Illegal Explosives] (version #3)**  

4RR  

Instant  

Smuggle (Instead of playing a land this turn, you may pay two and exile this card from your hand face down to create a Treasure token. You may still play this card from exile.)  

CARDNAME deals 5 damage to target creature or planeswalker. It deals 3 damage to that permanent's controller if mana from a Treasure was spent to cast CARDNAME.


The next version had only one change, smuggle went from costing three generic mana to costing two.


**[Illegal Explosives] (version #4)**  

4RR  

Instant  

Smuggle (2, Reveal CARDNAME from your hand and put it beneath the top three cards of your library: Create a Treasure token.) CARDNAME deals 5 damage to target creature or planeswalker. It deals 3 damage to that permanent's controller if mana from a Treasure was spent to cast CARDNAME.


The following incarnation of this spell again kept the spell effect the same but changed how smuggle works. This change was a little bigger. Now instead of exiling the spell, you would put it as the fourth card in your library. This is a bigger drawback because you're now losing a card because four turns from now, you'll draw the card that was already in your hand before you used this ability. My best guess is that this change came about because the previous version was too strong.


**[Illegal Explosives] (version #5)**  

4RR  

Instant  

CARDNAME deals 5 damage to target creature or planeswalker and 2 damage to its controller.


They decided to remove smuggle in the next version. The set already had a lot going on and was a little high in color fixing at the time. The effect itself stayed mostly the same except the damage to the opponent was no longer conditional (and it was lowered from 3 to 2).


**[Illegal Explosives] (version #6)**  

4RR  

Instant  

CARDNAME deals 5 damage to target creature or planeswalker. It deals 3 damage to that permanent's controller if mana from a Treasure was spent to cast CARDNAME.


The Set Design team went back on that decision and reverted to the version that rewards you for using Treasure to pay for it, although no longer with smuggle. My best guess is that this had to do with the Treasure theme that became part of the red-green draft archetype.


**[Paid Hit] (version #7)**  

3RR  

Sorcery  

CARDNAME deals 4 damage to target creature or planeswalker. If mana from a Treasure was spent to cast this spell, CARDNAME deals 4 damage divided as you choose among any number of target creatures and/or planeswalkers instead.


The design team liked the basic design but started tweaking the numbers and the conditional effect. Instead of doing damage to the permanent's controller, it changed how the damage would be distributed, from just one target to any number of targets. This, in turn, resulted in them dropping the damage from 5 to 4 and mana value by 1.


**[Paid Hit] (version #8)**  

2R  

Instant  

CARDNAME deals 3 damage to any target. If that target is a player, create a Treasure token. <i>(It's an artifact with "{oT}, Sacrifice this artifact: Add one mana of any color.")</i>


This is the one and only version where they allowed the spell to hit any target. It was also turned into a Treasure enabler (i.e., it helps you get Treasure tokens) rather than a Treasure reward (it empowers you for using Treasure tokens).


Looking at the text and seeing things like <i>and</i> (to show where italics start and end) or {oT} (how we tell layout that this is a tap symbol), I know this was pretty late in design, meaning this change was probably Play Design trying out something different to help adjust the Limited environment.


**[Golden Garrote] (version #9)**  

R  

Instant  

CARDNAME deals 4 damage to target creature or planeswalker. Its controller creates a Treasure token. <i>(It's an artifact with "{oT}, Sacrifice this artifact: Add one mana of any color.")</i>


Once Play Design started tweaking it, they made a version while keeping Constructed in mind over Limited. This version tested whether four damage for one red mana was acceptable with an additional cost to it, in this case giving your opponent a Treasure token. I assume that was a little too strong, so they reduced it to 3 damage and dropped the Treasure rider.


The big takeaway here is that making commons is just as complicated as making mythic rares and can require just as much tweaking along the way.


**Titan of Industry**


![Titan of Industry](https://media.wizards.com/2022/snc/en_jAOr6JQPgk.png)


Now that I told the story of a common, it's time to tell the story of a mythic rare.


**[Decorated Officer] (version #1)**  

2GG  

Creature — Dog Soldier  

5/1  

CARDNAME enters the battlefield with three shield counters on it.  

Armor 3  

CARDNAME attacks each turn if able.


This card started as a 5/1 that was very hard to kill. Armor was an early name for ward. We'd decided early on that we didn't want to put a lot of shield counters on any one card (the printed product has the only card that comes with more than one shield counter), so the fact that this got three is why it was a mythic rare.


**[Determined Agent] (version #2)**  

2GG  

Creature — Cat Soldier  

5/1  

CARDNAME enters the battlefield with three shield counters on it. (When a creature with a shield counter on it is targeted by an opponent, or if it would be dealt damage, remove a shield counter from it instead.)  

CARDNAME attacks each turn if able.  

1, Remove a shield counter from CARDNAME: Destroy target artifact or enchantment.


The next version of the card gave you a secondary use for the shield counters. You could now use them to get rid of artifacts and enchantments. To get this ability, the card had to give up ward. I think this change came about because we were trying to broaden the uses for shield counters. Often at higher rarities, we like to push the boundaries of a new mechanic.


**[Determined Agent] (version #3)**  

XGGGG  

Creature — Cat Soldier  

5/5  

CARDNAME enters the battlefield with X shield counters on it. (If a creature with shield would be destroyed or dealt damage, remove a shield counter from it instead.) When CARDNAME enters the battlefield, you gain X life.


The next version tried to up the splashiness. Instead of three shield counters, you now got X. Instead of a 5/1, you get a 5/5. And the "must attack" downside is gone. Also, because the card needed an X, we gave you a second bonus for it, life gain. Life gain is an incremental reward, so it's easy to add to things.


**[Skyscraper Elemental] (version #4)**  

7GGG  

Creature — Elemental  

10/10  

CARDNAME can't be countered.  

Haste  

CARDNAME enters the battlefield with two shield counters on it. (If a creature with shield would be destroyed or dealt damage, remove a shield counter from it instead.)  

Whenever one or more creatures attacks you, CARDNAME fights target attacking creature.


I think playtesting showed that having a lot of shield counters wasn't all that fun. It just becomes impossible to ever get rid of them, so the design dropped down to two shield counters. This meant other parts of the card had to get more exciting. For starters, it got twice as big. It gained abilities (can't be countered and haste). And the biggest addition was a fight trigger when the opponent attacks essentially allowing you to kill one attacker each turn. Obviously, to pay for all of this, the mana value shot up to 7GGG. This was also the version where it became an Elemental.


**[Skyscraper Elemental] (version #5)**  

5GGG  

Creature — Elemental  

9/9  

When you cast CARDNAME, you gain 5 life, draw a card, untap target land, it becomes a 7/7 creature with haste, destroy target artifact, enchantment, or land.  

Trample, reach


Killing a creature every attack proved to be too good/too frustrating for the opponent, so the design team took a shot at a new design. It got different abilities, it changed size slightly, and it got a whole bunch of "enters the battlefield" effects.


**[Skyscraper Elemental] (version #6)**  

5GGG  

Creature — Elemental  

8/8  

When you cast CARDNAME, choose two —  

• CARDNAME enters the battlefield with a shield counter on it.  

• When CARDNAME enters the battlefield, it deals damage equal to its power to target creature or planeswalker.  

• Each opponent sacrifices an artifact, an enchantment, and a land.  

• You gain 8 life.  

Trample, reach


The last design seemed a little too "kitchen sink" (R&D lingo for a card that just has a whole bunch of abilities on it that seem to impress by their volume rather than having inherent synergy with one another). The team decided to turn the next version into a creature that's a living command—that is, it gives you the choice of two out of four "enters the battlefield" effects. The four effects were chosen to be things that were conditionally useful, the key to making command modes shine. Interestingly, two out of the four end up being effects the printed product would use, only in a less flexible version. On the printed card, both the shield counter placement and the life gain have an option of targets (targeted life gain is nice in multiplayer formats where it can be used as a diplomacy tool).


**[Skyscraper Elemental] (version #7)**  

5GGG  

Creature — Elemental  

8/8  

Trample, reach  

When you cast this spell, choose two —  

• CARDNAME enters the battlefield with a defense counter on it.  

• Create a 4/4 green Rhino Warrior creature token with Trample.  

• Destroy target artifact, enchantment, or land.  

• You gain 8 life.


This version gets pretty close to the printed version. All four modes are using their final effects, although many of them are executed differently. The mana cost and power/toughness both go down, probably as a means of tinkering from Play Design. It took a lot of tweaking, but the card ended up with a pretty cool card design.


**Urabrask, Heretic Praetor**


![Urabrask, Heretic Praetor](https://media.wizards.com/2022/snc/en_GAhtbW0J2r.png)


*Kaldheim* and *Kamigawa: Neon Dynasty* each had a Praetor. Why not *Streets of New Capenna*? As with all Phyrexian Praetor designs, they follow a simple template. They all have two abilities, one that rewards you, and then a mirrored version that punishes your opponents. Many of them, but not all, also have a creature keyword.


**[Urabrask, Rebel Praetor] (version #1)**  

4RR  

Legendary Creature — Phyrexian Praetor  

6/6  

Menace  

At the beginning of your upkeep, exile the top card of your library. You may cast that card this turn.  

At the beginning of each opponent's upkeep, they exile the top card of their library. CARDNAME deals damage to that player equal to that card's mana value.


The design started with the idea that the positive ability for you was an impulsive draw each turn (R&D lingo for exiling the top card of your library and allowing you to cast it for the remainder of the turn).


The big question was, what's the opposite of impulsive draw? The first attempt exiles the opponent's card as a means to: one, deny them from drawing it; and two, determine how much damage Urabrask deals them. Urabrask was given menace, because, well, he's scary looking.


**[Urabrask, Rebel Praetor] (version #2)**  

4RR  

Legendary Creature — Phyrexian Praetor  

6/6  

Menace  

At the beginning of your upkeep, exile cards from the top of your library until you exile a nonland card. You may cast that card this turn.  

At the beginning of each opponent's upkeep, they exile cards from the top card of their library until they exile a nonland card. CARDNAME deals damage to that player equal to that card's mana value.


To improve the negative effect, both abilities now exile until they get a nonland card. With a mana value of 6, I think this is an upgrade to the positive ability.


**[Urabrask, Rebel Praetor] (version #3)**  

RRRR  

Legendary Creature — Phyrexian Praetor  

4/4  

Menace  

Whenever you cast your first spell each turn, it deals damage equal to its mana value to each opponent. Whenever an opponent cast their first spell each turn, it deals damage equal to its mana value to them.


The next version tried a completely different set of abilities. It rewarded you for playing a spell each turn by damaging the opponent. It then punished the opponent for playing a spell each turn. I think this design ended up being a little too much "just damage."


**[Urabrask, Rebel Praetor] (version #4)**  

1RRR  

Legendary Creature — Phyrexian Praetor  

3/3  

At the beginning of your upkeep, exile the top card of your library. You may play it this turn.  

At the beginning of each opponent's upkeep, the next time they would draw a card this turn, instead they exile the top card of your library. They may play it this turn.


This version went back to the impulsive draw but found a better way to make a negative version. You would get an opportunity to cast an extra card each turn, while your opponent would be forced to cast their draw each turn or lose it. These mirrored abilities are what ended up on the printed card, but the card's mana value, keyword ability, and power/toughness went through numerous changes.


The team would then go back and forth on haste and menace and end up going with haste. They also experimented with different mana values and power/toughness combinations but ended up with 3RR and 4/4.


**Vivien on the Hunt**


![Vivien on the Hunt](https://media.wizards.com/2022/snc/en_ia0gtKWvFu.png)


I talked about Elspeth [last week](https://magic.wizards.com/en/articles/archive/making-magic/word-streets-new-capenna-part-2-2022-04-25). Ob Nixilis didn't go through enough changes to be interesting to discuss. Vivien, though, had an interesting genesis I want to talk about.


**[Vivien] (version #1)**  

4GG  

Legendary Planeswalker — Vivien  

Starting Loyalty – 5  

+2: Look at the top seven cards of your library. You may reveal a creature card from among them and put it into your hand. Put the rest on the bottom of your library in a random order.  

-3: You may reveal a creature card from your hand. CARDNAME deals damage equal to the greatest power among that card and creatures you control to target creature or planeswalker.  

-8: Put any number of creature cards from your hand onto the battlefield. Creatures you control get +3/+3 and gain trample and haste until end of turn.


Vivien's power suite revolves around creatures, so the first stab at it was a more traditional design (small plus ability, small minus ability, large minus ultimate ability) involving creature-related effects. It had a "get creatures from your library to your hand" ability, a "use the creatures in your hand" ability, and a "get the creatures in your hand onto the battlefield" plus a "buff your creatures" ability. All very Vivien.


**[Vivien] (version #2)**  

4GG  

Legendary Planeswalker — Vivien  

Starting Loyalty – 5  

+2: Reveal the top five cards of your library. Put each creature card revealed this way into your hand and the rest on the bottom in a random order.  

-X: Put a creature card from your hand with mana value X or less onto the battlefield. When you do, it deals damage equal to its power to target creature an opponent controls.  

-8: Search your library for a creature card and put it onto the battlefield with ten +1/+1 counters on it. Then shuffle.


The library ability changed from an impulse (R&D lingo for looking at the top N cards of your library and taking something) to an ability that let you draw all the creature you revealed. The second ability was a combination of the second and third abilities from the previous design. The ultimate was brand new, a splashy ability that gets a creature from your library onto the battlefield and makes it huge. This batch of changes was mostly buffs intended to make the card more powerful and read better.


**[Vivien] (version #3)**  

4GG  

Legendary Planeswalker — Vivien  

Starting Loyalty – 5  

+2: Mill five cards. Return each creature card milled this way to your hand.  

+1: Choose target card in a graveyard, artifact, or enchantment. Its owner gains life equal to its mana value. Then exile it.  

-X: You may put a creature card with mana value X or less from your hand onto the battlefield. When that creature enters the battlefield, it deals damage equal to its power to target creature or planeswalker an opponent controls.


The plus ability was simplified by making you first mill the cards. I'm not sure if there was also a desire to help enable graveyard strategies in the set. The ultimate was replaced by a new small plus loyalty ability, one used to help remove certain types of threats. This is a bit odd on Vivien as it's got nothing to do with creatures (although the card in a graveyard could be a creature).


**[Vivien, Urban Tracker] (version #4)**  

4GG  

Legendary Planeswalker — Vivien  

Starting Loyalty – 5  

+2: Reveal the top five cards of your library. Put any number of creature cards from among them into your hand and the rest on the bottom of your library in a random order.  

+1: You may sacrifice a creature. If you do, search your library for a creature card with mana value equal to 1 plus the sacrificed creature's mana value, put it onto the battlefield, then shuffle.  

−7: You get an emblem with "As long as it's your turn, creatures you control have vigilance, trample, indestructible, and haste."


The top ability reverted to the previous version, although interestingly would change back to the last version for the printed card. This is the first version of the card to feature the "birthing pod" ability, an ability first seen on the card [Birthing Pod](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birthing+Pod) in *New Phyrexia*.


It was then given a new ultimate with a splashy emblem. The printed version swapped the first two abilities' loyalty costs and then exchanged the ultimate for a small loyalty ability that creates 4/4 Rhino Warrior creature tokens. I know Play Design has been trying to shake up how we make planeswalkers, so a move away from having an ultimate is a nice change of pace.


"And so it goes"
================


I hope you all enjoyed hearing my stories about *Streets of New Capenna*'s card designs. As always, I'm eager to hear your feedback on this column, any of the cards I talked about, or *Streets of New Capenna* in general. You can [email](mailto:making.magic@hotmail.com) me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).


Join me next week when I answer your questions about *Streets of New Capenna* in a mailbag column.


Until then, may you create your own stories with all these cards.




 

##### 
 #927: Worldbuilding with Emily Teng






##### 
 #927: Worldbuilding with Emily Teng


30:40



I sit down with Creative Team Member Emily Teng to talk about worldbuilding and the making of *Kamigawa: Neon Dynasty*.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2022/podcasts/magic/drivetowork927_worldbuildingwithemily_d23ufn23.mp3)




  


 

##### 
 #928: Streets of New Capenna Design






##### 
 #928: Streets of New Capenna Design


33:09



In this podcast, I talk about designing *Streets of New Capenna*.

 



 Play
[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2022/podcasts/magic/drivetowork928_sncdesign_2348sndf.mp3)





* [**Episode 926**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2022/podcasts/magic/drivetowork926_myr_237sndye.mp3) Myr
* [**Episode 925**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2022/podcasts/magic/drivetowork925_managementwithbrady_D23nsyde.mp3) Managing Teams with Brady Bell
* [**Episode 924**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2022/podcasts/magic/drivetowork924_makingmagictrivia_2438hnsd.mp3) Making *Magic* Trivia







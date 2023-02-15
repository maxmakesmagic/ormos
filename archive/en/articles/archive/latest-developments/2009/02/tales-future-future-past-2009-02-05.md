
---
[Link to Wayback Machine](https://web.archive.org/web/20211127232402/https://magic.wizards.com/en/articles/archive/latest-developments/tales-future-future-past-2009-02-05)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "One of the most powerful tools that developers in Magic Ramp;D use is playing Magic. Every day, developers ask each other to play Future Future League, which is our internal name for the Standard format which has the set currently in development as the most recent legal set. However, Magic games include tons of randomness, so we never know exactly what we'll learn when we"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "187161"
[_metadata_:path_date]:- "2009-02-05"
[_metadata_:publish_date]:- "2009-02-06"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Tales of Future Future Past"
[_metadata_:wayback_capture_timestamp]:- "2021-11-27 23:24:02"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211127232402id_/https://magic.wizards.com/en/articles/archive/latest-developments/tales-future-future-past-2009-02-05"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/tales-future-future-past-2009-02-05"
---


Tales of Future Future Past
===========================



 Posted in **Latest Developments**
 on February 6, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld24_clone.jpg)One of the most powerful tools that developers in **Magic** Ramp;D use is playing **Magic**. Every day, developers ask each other to play Future Future League, which is our internal name for the Standard format which has the set currently in development as the most recent legal set. However, **Magic** games include tons of randomness, so we never know exactly what we'll learn when we play. Some cards get played a lot and tuned to a fine edge, while other cards escape notice completely for a while and must be deliberately checked when we realize that we don't know how they play. We do test every card, but some cards have better stories than others. Today I'll be talking about some *Conflux* cards that have interesting stories from their time in the Future Future League.

Volcanic Fallout
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Volcanic+Fallout)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout)  
[Volcanic Fallout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout) began life as an instant [Steam Blast](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steam+Blast) for ![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif). Testing quickly showed that this was better than we wanted to print, since it was incredibly punishing against small creature decks and happened at instant speed. We don't mind having cards that punish small creature decks, but we like those cards to not be strong elsewhere. This card, however, was very main-deckable in red burn decks, since the worst case scenario was 2 damage to the face.

Around this time Erik Lauer was looking for ways to make cards that were naturally good against Faeries, and he suggested that [Volcanic Fallout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout) gain a mana and become uncounterable. Many players love it when their spells can't be messed with, and Faeries' main weapon against sweeping effects is counterspells, so that was a logical choice.

About a month later, I arrived at Wizards and started building tons of FFL decks. I built lots of variations of [Demigod of Revenge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demigod+of+Revenge) mono-red and red-black and started with [Volcanic Fallout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout) as a sideboard card. However, I kept sideboarding them in over and over again, and I eventually decided that I wanted to main-deck a few of them. They are awesome against small creature decks, they are awesome against Faeries, and against control decks you often are happy with picking off a [Mulldrifter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mulldrifter) and dealing 2 damage to your opponent. It also has great synergy with the many strong red creatures in the environment that have more than 2 toughness.

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld24_fallout.jpg)  
My personal favorite part of the card's journey happened in templating. Our standard template for uncounterability on instants and sorceries is "CARDNAME can't be countered by spells or abilities," and this is what was on [Volcanic Fallout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout) for a long time. We do it this way to allow the rules of the game to counter a spell that no longer has a target. However, rules manager Mark Gottlieb pointed out that [Volcanic Fallout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout) has no target, so the rules of the game can't counter it! Thanks to him, the card received the much more appealing template "CARDNAME can't be countered." Even the rules of the game can't touch it!

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld24_nocounter.jpg)  
Charnelhoard Wurm
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Charnelhoard+Wurm)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Charnelhoard+Wurm)  
[Charnelhoard Wurm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Charnelhoard+Wurm) was a card that the Future Future league ignored for a long time. This was not because of malice or indiscretion. It's just not easy to make a competitive constructed deck that effectively uses a seven mana creature that doesn't have an immediate impact on the game. However, developer Matt Place's developer sense tingled after he played with an early version of one of the *Conflux* Intro Packs that contained the card, and he built a mana ramp control deck that contained it.

You might read the card and wonder why his developer sense was tingling. The reason is that at the time the card had this text box:


> Trample  
>  When CARDNAME is put into a graveyard from play, shuffle CARDNAME into its owner's library, then return cards from your graveyard to your hand until you have seven cards in hand.
> 
> 

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld24_wurm.jpg)  
This was, to put it mildly, a beating. The mana ramp control deck that Matt built would play some removal spells and some [Mulldrifter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mulldrifter)s, and later he would dump one of these on the table. If you didn't kill it, it would kill you pretty quickly. If you did kill it, he wasn't going to run out of things to do for a very long time. We knew that the card still probably wouldn't cause tons of problems for competitive Constructed just because it did cost seven mana, but we also recognized that this ability produced horrible game play and needed to change. The new version is just as brutal in Limited without the despair-inducing game play.

Kederekt Parasite
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kederekt+Parasite)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite)  
This card began life as a ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) 1/1, and instead of requiring a red permanent it required a [Mountain](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain). From the perspective of a Constructed player that isn't that exciting. For red-black decks, it proved annoying to choose between running nonbasic lands for a smoother mana base and running more [Mountain](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s to turn this on. Also, ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) is a lot for a 1/1. As part of the overall change to keying off of permanent colors as opposed to basic lands, this changed to become a ![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) 1/1 that requires a red permanent, which is much more appealing. Unfortunately, it then promptly sat in the file for a long time while no one tried to play it.

Midway through *Conflux* development, Devin Low made a list of cards that had not been played much in their current incarnations. This card was on that list, and I sprang into action. At the time we were experimenting with playing *Shards of Alara* Block Constructed instead of Standard, and the quick black-red beatdown deck I made was a perfect natural foil to the slower mana ramp decks that many other developers and playtesters were playing. [Kederekt Parasite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) was also very powerful against them since much of their creature defense was expensive mass removal and their [Path to Exile](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Path+to+Exile)s were busy dealing with my unearthable [Shambling Remains](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Remains). 

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld24_parasite.jpg)  
Playtester Steve Warner discovered another interesting avenue to take the deck when we returned to playing Standard. His version used [Spiteful Visions](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spiteful+Visions), which in combination with [Kederekt Parasite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) deals 4 damage to the opponent each turn while also feeding Steve more and more burn spells. He also discovered the nasty trick of using [Ghitu Encampment](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghitu+Encampment) as a hard-to-remove red permanent for turning on the Parasite during an opponent's turn. In the end we decided that [Kederekt Parasite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) was strong enough to be interesting, so after all that testing we let the card go as it was.

Noble Hierarch
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Noble+Hierarch)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch)  
Everyone in the Pit loved [Noble Hierarch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch) essentially from the beginning. In fact, we loved it so much that we struggled with ourselves every time we made it worse, since we wanted so much for it to be awesome.

The exalted mechanic is a great fit for creatures that have tap abilities. That combinations lets a creature provide bonus damage without attacking and therefore still be able to use its ability later. One of the most popular tap abilities that green gets is making mana, so the earliest versions of the *Conflux* file had space for a common exalted mana creature that would help players play spells of many colors. Their first version was a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) 1/1 with exalted and "![](https://web.archive.org/web/20170424152623im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/tap.gif): Add one mana of any color to your mana pool." Here are some reactions to that card:


> AJ 3/18: Love this card.  
>  GTH 4/7: One of my favorites  
>  DAL 4/11: This is one of my favorites as well.
> 
> 

As you can see, the card was a huge hit in early playtesting, so the developers started to look for ways to make it stronger.


> DAL 4/11: Let's push this for constructed at 1G 1/1, and see if we like what it does or not.  
>  GTH 4/14: That sounds insane! In other words, I'm fully behind it.   
>  MT 4/14: Now 2 mana.
> 
> 

Everyone still loved the way it played. However, now it was so powerful that it distorted Limited play. Other colors just didn't have commons that good, and we didn't want to start an arms race that resulted in escalated power all over the set. People who were further away from the set's development also pointed out how much better it was than any other existing common two-mana creature that tapped for mana.


> MLG 4/21: As a 2-mana 1/1 that taps for any color, this card obsoletes Harvester Druid, Quirion Elves, Quirion Explorer, Sylvok Explorer, Urborg Elf, and Druid of the Anima -- an ALA card! -- and that doesn't even take "exalted" into account! Good luck ever making another 2-mana Elf. 
> 
> 
> 
> |  |  |
> | --- | --- |
> |  |  |
> 
> 

However, we loved its game play in Constructed so much that we didn't want to give it up. What to do? Devin Low's answer was to embrace how powerful we wanted the card to be and put it at rare to protect Limited from the shockwaves.


> DAL 4/22: Changing to 0/1 (still exalted) is the best way to address that. Then it blocks worse and mass attacks worse than all those guys, but is still awesome. Alternatively, we could make this rare, either at 1G 1/1 or (gasp!) G 0/1 and do a different green exalted common.  
>  AF 4/25: G 0/1 rare sounds totally hot. I'd cast Rafiq off that guy.
> 
> 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rafiq+of+the+Many)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rafiq+of+the+Many)We decided to try it. Amusingly, the person who put the new cheaper mana cost into the file neglected to reduce the creature's power as well, so mad genius Erik Lauer was forced to swoop in.


> EVL 4/28: Right now it is G for a 1/1 with exalted and tap for any color of mana. You have made a strong card. I am making it a 0/1.
> 
> 

"You have made a strong card" is a hilarious understatement. That version would have been [Llanowar Elves](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves) with bonus colors of mana production and the ability to either attack as a 2/2 or give a lone friend a bonus. That's clearly over the top, so Erik toned it down a little bit. With that fixed, we started playing it in Constructed. It was still just as fun as before. Unfortunately, it kept proving to be better and better.


> sw 4/29: I think even at 0/1 it's still rather insane, it can attack like lawnmowers and can produce any color like birds.  
>  MP 5/1: Seems too strong.
> 
> 

The quandary we were in was a tough one. We had identified a card that was incredibly fun, and a very important part of our job is to find things that are fun and protect them. However, we also didn't want to make people wonder why they even had [Birds of Paradise](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise). Happily, some inspiration came to lead developer Mike Turian in the shower one morning, and he put his solution into the file.


> MT 5/5: Now only adds Bant mana.
> 
> 

This out-of-the-box solution only makes any sense because of the flavor of the five shards. Exalted is the mechanic assigned to Bant, and it makes lots of sense for a Bant druid to not know how to make red or black mana. Everyone was hopeful that this change would be enough to give the card a printable power level without losing the fun we were having with it, and testing proved that that was exactly what it did. We never changed the card again after this.

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld24_noble.jpg)  
After all that, the card remains very powerful. It fits perfectly into Bant exalted decks and I'll be surprised if I don't see people casting [Rafiq of the Many](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rafiq+of+the+Many) with it at some point in *Shards of Alara* Block Constructed. It also fits great into decks that happen to be green-white or green-blue. Although [Noble Hierarch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch) does not attack well in groups, she is sometimes amusingly better in multiples against other creatures than [Llanowar Elves](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves) is. A pair of [Llanowar Elves](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves) must look wistfully at an opposing 2/2 creature and stay home; on the other hand, a pair of [Noble Hierarch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch)s lets their controller choose one to attack with and become a 2/3. We have played [Noble Hierarch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch) a lot, and we hope that you like it as much as we do.

That's the story of my second-favorite card in *Conflux*. I'll write an article later about my favorite card. For now, it remains a mystery!

Reliquary Tower
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Reliquary+Tower)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reliquary+Tower)  
We developers do our best to get everything done with plenty of time to spare. However, sometimes things go wrong right before a handoff, and that's exactly what happened to this card. We had a card we liked for this slot, but the rules team simply couldn't figure out a way to make the card work properly in all situations. (Mark Rosewater's article on Monday will talk about exactly what went wrong.) In the end we were left with four days to make a completely new card for our final set handoff. It had to be a colorless land and use this art:

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld24_tower.jpg)  
Mark was sad to see his card go, but when the developers asked for hole submissions he was ready with a pile of abilities, one of which was "[Spellbook](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spellbook) Land." More than any of the submissions, [Spellbook](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spellbook) Land caused an enormous amount of discussion in the pit. Some people vehemently claimed that the card would never be played seriously. Other people argued that [Spellbook](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spellbook) was a very well-loved card and that this land would be popular. I made the point that many monocolored decks often had extra land slots that they didn't need for colored mana production, and that if this was the best bonus a blue deck could get from a colorless land then I would not hesitate to play a few. Five minutes later, Erik Lauer returned from a meeting and confirmed that he would have tried to play some quantity of [Spellbook](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spellbook) Lands in his Worlds 1998 Standard deck if it had existed then.

Mike Turian had been quietly watching all of the discussion and astutely realized that of all the options on the list we had, this was the one that was exciting people the most. We just couldn't stop talking about it. Therefore, he put it in the file and the rest was history.

Here are the exciting Multiverse comments from editor extraordinaire Del Laugel!


> Del 8/4: This card is dead. Waiting for new card.  
>  Del 8/6: New card.
> 
> 

Conclusion
**Magic** development is sometimes a messy process. However, we do pay attention to every card by the end, and most cards have interesting stories as they go through development. We're excited to finally have you all playing with the cards we have now known for so long.

Last Week's Poll


|  |
| --- |
| **What is your favorite format to play at Prereleases?**  |
| Traditional Sealed Deck | 4438 | 52.8% |
| Two-Headed Giant Sealed Deck | 969 | 11.5% |
| Draft | 1999 | 23.8% |
| Open Dueling | 235 | 2.8% |
| I don't go to Prereleases. | 763 | 9.1% |
| **Total** | **8404** | **100.0%** |

  
Many of us here in **Magic** Ramp;D attended a Prerelease in the Seattle area. We were happy with what we saw, and we're glad that those of you who love to draft are once again able to do that!

This Week's Poll


|  |
| --- |
| **What is your favorite *Conflux* rare?**[Banefire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Banefire)[Blood Tyrant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Tyrant)[Bloodhall Ooze](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze)[Charnelhoard Wurm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Charnelhoard+Wurm)[Cliffrunner Behemoth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth)[Cylian Sunsinger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Sunsinger)[Exotic Orchard](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exotic+Orchard)[Extractor Demon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Extractor+Demon)[Font of Mythos](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Font+of+Mythos)[Giltspire Avenger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giltspire+Avenger)[Goblin Razerunners](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Razerunners)[Gwafa Hazid, Profiteer](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gwafa+Hazid%2C+Profiteer)[Inkwell Leviathan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkwell+Leviathan)[Kederekt Parasite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite)[Knight of the Reliquary](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Reliquary)[Magister Sphinx](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magister+Sphinx)[Mark of Asylum](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mark+of+Asylum)[Martial Coup](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Martial+Coup)[Master Transmuter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+Transmuter)[Meglonoth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Meglonoth)[Noble Hierarch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch)[Nyxathid](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nyxathid)[Obelisk of Alara](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Obelisk+of+Alara)[Paleoloth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Paleoloth)[Rakka Mar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakka+Mar)[Scepter of Dominance](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scepter+of+Dominance)[Scepter of Fugue](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scepter+of+Fugue)[Scepter of Insight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scepter+of+Insight)[Sigil of the Empty Throne](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sigil+of+the+Empty+Throne)[Soul's Majesty](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul%27s+Majesty)[Sphinx Summoner](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx+Summoner)[Telemin Performance](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Telemin+Performance)[Voracious Dragon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voracious+Dragon)[Wall of Reverence](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Reverence)[Worldheart Phoenix](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Worldheart+Phoenix) |

  
[![](https://media.wizards.com/legacy//mtg/images/daily/ads/conflux-release-day-1.jpg)](/magic/tcg/products.aspx?x=mtg/tcg/products/conflux)






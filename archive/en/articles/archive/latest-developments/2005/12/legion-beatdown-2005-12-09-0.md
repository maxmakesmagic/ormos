
---
[Link to Wayback Machine](https://web.archive.org/web/20220812120519/https://magic.wizards.com/en/articles/archive/latest-developments/legion-beatdown-2005-12-09-0)

[_metadata_:author]:- "Aaron Forsythe"
[_metadata_:description]:- "This is the final of my four articles on Ravnica guild development—you can read the other three here: “Completing the Conclave” (Selesnya), “Golgari Query” (Golgari), and “Secrets of the Secret Guild” (Dimir). The red-white guild—the Boros Legion—required the most development work of the four pairs in the set. The guild is schizophrenic—at its core, it is very beatdown"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "613171"
[_metadata_:publish_date]:- "2005-12-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Legion of Beatdown"
[_metadata_:wayback_capture_timestamp]:- "2022-08-12 12:05:19"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220812120519id_/https://magic.wizards.com/en/articles/archive/latest-developments/legion-beatdown-2005-12-09-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/legion-beatdown-2005-12-09-0"
---


The Legion of Beatdown
======================



 Posted in **Latest Developments**
 on December 9, 2005 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_aaronforsythe.jpg)
By Aaron Forsythe












![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af96_borosmana.jpg)This is the final of my four articles on *Ravnica* guild development—you can read the other three here: “[Completing the Conclave](/en/articles/archive/latest-developments/completing-conclave-2005-10-07-0)” (Selesnya), “[Golgari Query](/en/articles/archive/latest-developments/golgari-query-2005-10-28-0)” (Golgari), and “[Secrets of the Secret Guild](/en/articles/archive/latest-developments/secrets-secret-guild-2005-11-11-0)” (Dimir).


The red-white guild—the Boros Legion—required the most development work of the four pairs in the set. The guild is schizophrenic—at its core, it is very beatdown oriented, with lots of two-mana creatures and combat tricks, but it also sports a slew of slower control-oriented cards like [Firemane Angel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firemane+Angel) and [Razia's Purification](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Razia%27s+Purification). And there are a number of cards that straddle the fence, like [Lightning Helix](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Helix) and [Sunhome Enforcer](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunhome+Enforcer). Development had to make sure to allocate sufficient resources to both sides of this strategic spectrum, while at the same time maintaining a guild identity. Throw in a mechanic that was proving troublesome from the get-go, and you can see that we had our hands full with this bunch.


### Who's the Beatdown?


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af96_swiftblade.jpg)In preparation for *Ravnica*, the **Magic** developers played constructed for several weeks using only *Kamigawa* block and *Ninth Edition* in order to get a feel for what *Ravnica* should be trying to add to the constructed card pool. Our top performing decks week after week were [Greater Good](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Good) with Dragons and White Weenie. The success of the latter proved to be a real thorn in the side of the Boros guild during design, as the developers were not interested in making that deck even faster. In other words, the word came down from on high that while the flavor of red-white was supposed to be ordered aggression, design shouldn't actually implement that idea with actual aggressive cards, as the constructed environment couldn't afford them. A beating indeed!


So what design handed over was a bunch of semi-aggressive cards that got the job done in limited but were far too weak to be considered in constructed. A good example would be the card eventually known as [Screeching Griffin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Screeching+Griffin)—it came in from design costing ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif). While a white [Wind Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wind+Drake) with extra evasive capabilities was a real winner in sealed deck and draft, it was not good enough for Standard thanks to older cards like [Leonin Skyhunter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leonin+Skyhunter).


As development began, the lack of power in the Boros guild was kind of depressing. As has been mentioned on this site many times before, red-white was already known to be the color pair least liked by most players and was chosen to be one of the first guilds highlighted in the block just so it could be given extra love and attention. All post-design indicators hinted that the guild wasn't going to cut it in constructed, which meant it would go on being unloved.


 



![Searing Meditation](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Searing+Meditation)

Development initially tried to carve a niche for red-white in constructed by upping the power-level of its control cards. After all, red-white has a long history of control decks, ranging from [Ivory Gargoyle](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ivory+Gargoyle)/[Jokulhaups](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jokulhaups) decks to [Astral Slide](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide)/[Lightning Rift](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Rift). We created [Firemane Angel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firemane+Angel) and [Searing Meditation](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Meditation). [Razia's Purification](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Razia%27s+Purification) was playtested at four mana. [Brightflame](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brightflame) was added in.

The attempt to make red-white control viable worked a little. The Angel proved itself to be a good card, and Purification was a certified wrecking ball—so much so that it was complained about incessantly, and was eventually raised in cost from four to five and then to six mana.


Over time, however, a fortuitous turn of events was shaping up in aggro red-white's favor. As the other three guilds in the set came together, it became clear that each of them was capable of holding its own against our current crop of beatdown weenie decks. Green-white had bombs like [Glare of Subdual](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glare+of+Subdual) and [Loxodon Hierarch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Loxodon+Hierarch) at its disposal, blue black could throw up early defenses and then ride out the storm with card drawing and removal, and black-green could hold off weenies indefinitely with [Plague Boiler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Boiler), [Putrefy](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrefy), and Kagemaro. There was actually room to make aggro decks better.


Limited was playing out in much the same way. Everything from [Drift of Phantasms](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drift+of+Phantasms) to [Scatter the Seeds](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scatter+the+Seeds) made life difficult for the beatdown player, and red-white was in need of some juice if it wanted to compete. So eventually development reversed its earlier position on red-white beatdown and started adding in aggressive cards.


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af96_char.jpg)[Skyknight Legionnaire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skyknight+Legionnaire). [Thundersong Trumpeter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thundersong+Trumpeter). [Boros Swiftblade](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Swiftblade). [Lightning Helix](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Helix). [Char](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Char). [Sunhome, Fortress of the Legion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunhome%2C+Fortress+of+the+Legion). [Boros Guildmage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Guildmage). These are the cards that many of you associate with the Boros guild in both limited and constructed play, and the funny thing is that every one of these cards was added to the set by the development team. As the one person that worked on both design and development of this set, I'm happy that the design vision of the guild was finally implemented by development; ironic, really, since it was development that prevented design from doing what they wanted in the first place.


Personally, I was always enamored with the idea of red-white beatdown and was thrilled to see it come to fruition. Fast two-color decks are generally hard to pull off because of the strict mana requirements—it is often difficult to have access to two different colors of mana on turn two consistently. In the early days of the Extended format, red-white beatdown was enabled by cards like [Plateau](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plateau), [Tithe](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tithe), and *Mirage* fetchlands, but even then the decks were often mainly White Weenie decks that splashed for [Lightning Bolt](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) and [Incinerate](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate). Rare were the decks that played both [Savannah Lions](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savannah+Lions) and [Jackal Pup](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jackal+Pup). I had hopes that by having both [Battlefield Forge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battlefield+Forge) and [Sacred Foundry](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sacred+Foundry) in the format that the mana bases might be good enough to play a creature on turn one and then a multicolored spell on turn two, and so far it seems like that strategy is viable in Standard (and actually good in Extended, where the *Onslaught* fetchlands all but guarantee access to ![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) on turn two).


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af96_charart.jpg)
### When a Keyword Isn't a Keyword


There has been a bit of consternation—at least in our forums—that each of the guilds in *Ravnica* got a “real” keyword except Boros, which got an *ability word*, or “fake keyword.” Why would we do such a thing?


We certainly never planned that to be the case, and in fact the mechanic *was* a keyword in design. For example:



> 
> CZ16\_CON  
> 
> Radiant Surprise  
> 
> 1RW  
> 
> Instant  
> 
> Radiant *(As you play this spell, choose color, creature type, or converted mana cost.)*  
> 
> Untap target creature and each creature that shares the chosen characteristic with it. Those creatures get +3/+0 until end of turn.
> 
> 
> 


Mark Rosewater mentioned this initial incarnation of radiance in his article “[City Planning, Part III](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr194),” but he misremembered the details. When a “radiant” (the original name) spell was played, it didn't affect *all* creatures that shared color, type, and cost with the target, but rather only the one of those three groups that you chose. So if you were to play Radiant Surprise on a [Flame-Kin Zealot](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame-Kin+Zealot), you could choose to have it affect all red and white creatures (color), all Elementals and Berserkers (creature type), or all four-mana creatures (CMC). The mechanic was incredibly decision-intensive; if there were five creatures in play, you could have the radiant spell do any of fifteen different things. Often the ramifications of your choice weren't realized until the spell was played, and I'd constantly hear things like, “That guy is Human, too? Crap! My Armorer dies!” during playtests. At development's behest, design removed CMC from the list of options before handing the file over just to reduce the mental anguish that came from playing one of these cards on a complicated board.


As we playtested the mechanic in development, we found that the creature type clause was responsible for bogging games down. Any time a radiant spell was about to be played, the caster would have to pick up every creature in play and read it just to verify its types. If you haven't noticed, *Ravnica* is full of oddball types like Skeleton Troll, Plant Zombie, Elephant Cleric, Insect Horror, Giant Soldier, Faerie Rogue, Human Mercenary, Sphinx, Ooze, Wolf, Lammasu, Lizard, Avatar, and the aforementioned Elemental Berserker. Creature types are not compartmentalized in this world and are not particularly intuitive on any given card. Color, on the other hand, is readily visible on every creature on the table. So we eventually made the decision to yank type from the list of radiant options as well, leaving color as the only remaining “choice.” Even though a huge percentage of the decisions had been removed from the mechanic, we felt it would play well like this thanks to the presence of gold and hybrid cards in the environment.


Throughout all these changes, we were still writing the cards as if radiant was going to be a keyword. It wasn't until the editors got their hands on the set that we became aware of the fact that the cleanest way to write the rules text on these cards was *without reminder text*. With no reminder text, we were left without a proper keyword and had to opt for the less-sexy ability word instead. Considering how far we'd come in the process, we had no choice but to go forward with the ability word.


The Boros ended up not being alone in that boat, however; a similar thing happened with one of the other guilds later in the block. You'll be seeing a second ability word before we leave the world of *Ravnica*.


### Snippets from the Vault


Finally, here are some of the juicier Multiverse comments from Boros cards.


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af96_cleansing.jpg)**[Cleansing Beam](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cleansing+Beam)** had a wildly fluctuating mana cost. We eventually settled on five, partially because we felt that if it was any cheaper, it would really wreck casual tribal decks.



> 
> bs 10/12: reduced cost.  
> 
> ps 10/15: so like...this card was a bomb in limited at 4R. and now it's 2R. and it's still common. this is...insane.  
> 
> ps 10/19: i hear other people don't agree with me, but i've found this to be very very good. keep an eye on this, that's all i ask. :)  
> 
> bs 10/19: cc.  
> 
> HS 10/28 depends a lot on what deck you are playing against. But I agree I think this is too often wrath my opponents board for 3 mana.  
> 
> bs 10/29: should at least be uncommon. can discuss other changes.  
> 
> AF 11/9: Red needs goodies. This seems ok.  
> 
> bs 12/17: is uncommon now, was common.  
> 
> bs 12/22: wrath your opponent will cost more than 3 mana.  
> 
> bs 1/3: radiant shock is 4r.  
> 
> ps 1/5: the fact that i still hear people talking about putting this into constructed decks makes me really happy about this change.
> 
> 
> 


 



![Flame-Kin Zealot](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flame-Kin+Zealot)

**[Flame-Kin Zealot](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame-Kin+Zealot)** began life as a ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 common that gave all your creatures +1/+2 and haste when he came into play. He was pretty insane.


> 
> RB 8/3: Seems too good in limited for a common right now.  
> 
> DAL 8/26: Seriously. 4xRaging Kavu were in 4 of the PT Osaka top 8 decks. At 3/4 haste, this guy has +3 toughness and crusades all his friends at the same cost. . .  
> 
> bs 9/29: sometimes nerfs are good. changed 1 to r.  
> 
> bs 10/5: could be uncommon.  
> 
> AF 10/5: What is our philosphy on "unbalanced" mana costs? (CCD, 1CDD, etc)  
> 
> RB 10/8: At this power-level, this should probably be UC (unless the RW guild needs a LOT of help in Lim). Meanwhile I was complaining about assymmetrical mana costs, but I'm going to stop ...  
> 
> bs 10/29: i dislike this card at this cost. i'd like it to go up a mana.  
> 
> MP 11/3: Should give +1/+0 for balance sake.  
> 
> AF 11/9: We need to watch how many RW guys have "+1/+0"... this guy, Gendarme Giant, Major Etc.  
> 
> MJ 11/17: it saddens me that RW no longer is a beatdown guild. With the weakest guildmage and only a couple playable creatures at less than 4 mana RWs only home seems to be the board control deck. :(  
> 
> bs 12/21: is this still true.  
> 
> bs 1/3: moved to uncommon.  
> 
> AF 1/6: Consider RRW? If we want to help RW, it needs to hit the curve and has only 2/2 flier at 3 right now.  
> 
> bs 1/10: this format doesn't really exist... we can give this guild a few creatures in the next two set... in fact, we can give all of the guilds stuff in the next few sets. i believe that each guild has a lot of deck building options now (r/w included)... and that will only improve with time.
> 
> 
> 


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af96_helix.jpg)**[Lightning Helix](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Helix)** is in fact eerily similar to the *Darksteel* card [Essence Drain](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Drain)…



> 
> Del 2/3: Weird how this could be a black card with no change but the mana cost . . .
> 
> 
> 


There were several arguments about whether **[Master Warcraft](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+Warcraft)** should be a sorcery or an instant. It was initially a sorcery that said, “You choose attackers and assign blockers during the next combat step,” so that if you played it during your second main phase it would affect your opponent's turn.



> 
> DAL 8/26: third 'you must block' card in the set.  
> 
> bs 9/9: 2rw armageddon is an option.  
> 
> MP 10/6: How does this card interact with "costs" to attack?  
> 
> Carter 10/17: The Mindslaver precedent is "This includes choices and decisions".  
> 
> bs 10/26: was, "You choose attackers and assign blockers during the next combat step."  
> 
> bs 10/29: 1/2, 1/2.  
> 
> MT 11/4: A total savaging in limited. Mindslaver for the attack step.  
> 
> MJ 1/4: can this please be an instant for multiplayer play?  
> 
> Del 1/7: Truly bizarre that the function depends on which main phase you play it in.  
> 
> Del 1/7: I think if you made this an instant, you'd have to either restrict it to being played before combat or add "this turn."  
> 
> MT 1/31: Can we please find some way to make this an instant? It is such an ugly sorcery.  
> 
> AF 2/3: It would be an uglier instant I think, assuming we had to word it so people wouldn't play it wrong. If we can just change what it is right now to "instant," go for it.  
> 
> Del 2/3: There are several options for an instant version, but the one with the least memory issues probably looks like this:  
> 
> Play CARDNAME only before the combat phase [or "before the declare attackers step," or whatever].  
> 
> Instead of attacking player, you choose which creatures attack this turn. Instead of defending player, you choose how each creature blocks this turn.  
> 
> ps 2/6: the sorcery version is already tough to play correctly, isn't it? start my turn, get excited and cast this, then pass the turn and my opponent says, "you haven't gone to your attack step yet"? oops.  
> 
> Del 3/16: Brian changes from a sorcery to this. (Retemplated so it's not as much of a mouthful.)
> 
> 
> 


### Last Week's Poll




| **Which of the following old mechanics do you like the best?**  |
| --- |
| Buyback | 2494 | 14.9% |
| Flashback | 2353 | 14.1% |
| Cycling | 2280 | 13.7% |
| Kicker | 1903 | 11.4% |
| Threshold | 1739 | 10.4% |
| Madness | 1735 | 10.4% |
| Shadow | 1407 | 8.4% |
| Morph | 1280 | 7.7% |
| Flanking | 568 | 3.4% |
| Echo | 487 | 2.9% |
| Phasing | 445 | 2.7% |
| **Total** | **16691** | **100.0%** |

Here in R&D we often talk about mechanics like shadow and buyback in terms that make them seem like they were bad for the game. Shadow, for instance, removes interactivity by taking blocking out of the game. Buyback creates redundant game states and can be frustrating for the guy on the other side of the table. But because we as developers think they were kind of “bad” in a big-picture sort of way, does that mean they were actually bad ideas? This poll was put forth to try to put these so-called “bad” mechanics into context with other mechanics that we feel were better implemented.









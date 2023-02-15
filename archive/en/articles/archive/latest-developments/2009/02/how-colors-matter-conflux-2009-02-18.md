
---
[Link to Wayback Machine](https://web.archive.org/web/20160711110246/http://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-18)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Many Latest Developments columns talk about the journeys of individual cards in painstaking detail, which paints a picture of a world where developers take fully formed design files and quietly tweak numbers and text boxes until the set is ready to print. This is not an entirely accurate picture. Often we identify something that we want a card somewhere in a set to do, discover that there is no such card at the moment, and create one that does what we need done."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "187246"
[_metadata_:path_date]:- "2009-02-18"
[_metadata_:publish_date]:- "2009-02-20"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "How Colors Matter in Conflux"
[_metadata_:wayback_capture_timestamp]:- "2016-07-11 11:02:46"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160711110246id_/http://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-18"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/how-colors-matter-conflux-2009-02-18"
---


How Colors Matter in Conflux
============================



 Posted in **Latest Developments**
 on February 20, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






Many Latest Developments columns talk about the journeys of individual cards in painstaking detail, which paints a picture of a world where developers take fully formed design files and quietly tweak numbers and text boxes until the set is ready to print. This is not an entirely accurate picture. Often we identify something that we want a card somewhere in a set to do, discover that there is no such card at the moment, and create one that does what we need done. Other times, we identify cards that aren't working, realize that we don't have anything in mind for the slot, and ask designers for submissions. We are also not afraid to make sweeping changes to entire mechanics to improve game play. This happened during *Conflux* development with the suite of monocolored cards that mechanically encourage multicolor play. Today I'll talk about what happened to those cards and why we decided to change them.

![](https://web.archive.org/web/20130606200831im_/http://wizards.com/mtg/images/daily/ld/ld26_shardConvergence.jpg)  
The designers of *Conflux* were obligated to continue the multicolor theme of *Shards of Alara* while also introducing new twists. *Shards of Alara* contained many monocolored cards with activation costs that used other colors of mana from the card's home shard. *Conflux* does contain some of these, but the designers also chose to include monocolored cards that have conditional static and triggered abilities that turn on based on multicolor play. They tried various incarnations of these, and eventually chose to key off of basic lands. For example, a black card would give you a bonus if you controlled an [Island](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island). The file that the designers handed off to development contained about ten cards like that, and they emphasized to the developers that those cards were important because they gave the set more of a multicolor feel without using tons of gold cards.

One of the first things that developers do with sets fresh out of design is play lots of Limited. This helps us identify what is fun and not fun about what the commons in the set are doing. It's also useful because if a set's commons have problems, then it's likely that the uncommons and rares that are riffs on the themes of those commons also have problems.

Our early Sealed Deck and draft playtests quickly showed us that much of the power at common was located in the "basic land matters" cards. For example, the design handoff versions of [Parasitic Strix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix) and [Sedraxis Alchemist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) looked like this:


> Parasitic Strix  
>  2U  
>  Artifact Creature – Bird  
>  2/2  
>  Flying   
>  When Parasitic Strix comes into play, if you control a Swamp, target player loses 2 life and you gain 2 life.
> 
> 


> Sedraxis Alchemist  
>  2B  
>  Creature - Zombie Wizard  
>  2/2  
>  When Sedraxis Alchemist comes into play, if you control an Island, return target nonland permanent to its owner's hand.
> 
> 

Those cards were very, very powerful. Seasoned players might recall that [Blind Hunter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blind+Hunter) and [Man-o'-War](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War) were both famously high picks in their respective draft formats. [Parasitic Strix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix) doesn't give you a second chance at draining your opponent, but it also costs one less and gives you the ability to play it before you have a [Swamp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp), which are both big advantages. [Sedraxis Alchemist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) doesn't compare quite as well to its predecessor as [Parasitic Strix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix) does, but it was still very powerful compared to our modern commons. [Dark Temper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Temper) was also comically strong in Limited when it only required a [Swamp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp). It did a pretty good impression of [Terminate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terminate), and when it wasn't doing that, 2 damage was still quite exciting much of the time.



|  |  |
| --- | --- |
|  |  |

One way to handle this would have been to add some mana to the costs of those cards. The basic land–requiring versions of [Parasitic Strix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix) and [Sedraxis Alchemist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) are both still powerful at four mana. However, we weren't thrilled with having great Limited cards that should be showing off the themes of the set be anemic-looking four-mana 2/2's. We noted the problem and kept looking at the rest of the set.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dark+Temper)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Temper)  
We also play Constructed early in a set's development, but with much less structure than we use when specifically testing competitive Standard. By encouraging people to play whatever they want, we can identify which new cards are the most exciting and fun, and we try to protect those cards as the set moves through development.

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld26_cross1.jpg)  
When we did this, we discovered that requiring basic lands plays very poorly in Constructed. Playing multiple colors almost always involves playing some number of nonbasic lands. Using "basic land matters" to reward multicolor play worked fine for Limited, but in Constructed it was really frustrating. We wanted to run multiple colors to play the new cards, but the very thing that we had to do to support the actual gold cards made the "basic land matters" cards worse. This is clearly very bad for cards that are supposed to be exciting and fun to play with in any multicolor deck.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cliffrunner+Behemoth)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth)For example, [Cliffrunner Behemoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth) stood out to many people as a card that they wanted to play with. At the time, it looked like this:


> Cliffrunner Behemoth  
>  3G  
>  Creature - Rhino Beast  
>  5/3  
>  Cliffrunner Behemoth has haste as long as you control a Mountain. Cliffrunner Behemoth has lifelink as long as you control a Plains.
> 
> 

The most natural thing to do with it was to put it in a mainly green deck that splashed white or green. Those decks wanted to use cards like [Noble Hierarch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch) and [Birds of Paradise](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise) to speed out big creatures. However, those decks didn't have room for very many [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) or [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s if they wanted to both consistently play a mana creature on turn one and be able to play white or red cards if their mana creatures got killed. This left playtesters who tried to build for [Cliffrunner Behemoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth) frustrated. Some people built awkward mana bases to try to play with the card despite the difficulties; others simply gave up.

The same thing happened to people who tried to play [Bloodhall Ooze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze) and [Kederekt Parasite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) together. At the time, they looked like this:


> Bloodhall Ooze  
>  R  
>  Creature – Ooze  
>  1/1  
>  At the beginning of your upkeep, if you control a Swamp, you may put a +1/+1 counter on Bloodhall Ooze. At the beginning of your upkeep, if you control a Forest, you may put a +1/+1 counter on Bloodhall Ooze.
> 
> Kederekt Parasite  
>  B  
>  Creature – Horror  
>  1/1  
>  Whenever an opponent draws a card, if you control a Mountain, you may have Kederekt Parasite deal 1 damage to that player.
> 
> 

Suppose you are trying to build a black-red FFL deck. You probably want to play four each of [Sulfurous Springs](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sulfurous+Springs) and [Graven Cairns](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Graven+Cairns), and you might play some [Auntie's Hovel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auntie%27s+Hovel)s if you choose to play some Goblins. [Bloodhall Ooze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze) asks you to control a [Swamp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) and [Kederekt Parasite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) asks you to control a [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain), so you might think about splitting the rest of your lands between those two basic land types. However, that fights with the rest of the cards you want to be playing. You would like to be able to play [Flame Javelin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Javelin)s and [Figures of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figures+of+Destiny), but those cards are clearly maximized when all of your lands make red. However, you also don't want to play [Bloodhall Ooze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze) without [Swamp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s! This was not a fun situation.

![](https://media.wizards.com/legacy//mtg/images/daily/ld/ld26_equation.jpg)  
The final realization that we made was that in many cases there wasn't a ton of difference in play between actual gold cards and the basic land–requiring monocolored versions of these cards. How different is that version of [Sedraxis Alchemist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) from a ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) 2/2 [Man-o'-War](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War)? How different is that version of [Rhox Meditant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rhox+Meditant) from a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/4 that draws you a card? Clearly there is some upside to being able to play them without getting the bonus, but under optimal conditions they felt very close to just being gold. *Conflux* already had tons of gold cards, so we weren't happy if all this mechanic was doing was giving it even more of them even if they weren't gold by mana cost.

It was clear at this point that there were problems across the board with these cards. We were struggling with ourselves about whether to cost them so that they were attractive and very powerful or awkward-looking but still good. They weren't fun in Constructed, and they didn't feel that different from gold cards. At this point, lead developer Mike Turian decided that something needed to be done. Of course, we also needed to preserve the structure that design had built for us. In order to solve this problem, we went back to the designers. The mechanic that they liked second best in design was keying off of controlling colored permanents, so we changed all the cards that required basic lands to the new mechanic and started testing again.

We knew that the Limited cards we were worried about before were now less powerful. [Parasitic Strix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parasitic+Strix), [Sedraxis Alchemist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist), and [Dark Temper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Temper) were previously all sure bets when you cast them, because we avoid making land destruction spells that work at instant speed. Now, people could respond to these cards by destroying the permanent that you were planning on using to satisfy the condition. This is clearly less powerful. However, we were okay with that because it meant that we were no longer fighting with ourselves about whether to make the cards exciting or properly balanced. Because they were weaker, we could do the cheaper and more attractive versions and feel good about it.

Although this worked in our favor in Limited, we initially worried that it would hurt us in competitive Constructed. If the cards that were on the edge of Constructed that used the mechanic before were now weaker there also, they might be too weak to play at all. Happily, the opposite turned out to be true and the cards thought would be good in Constructed actually became stronger thanks to the ability to get full value out of them while playing lots of nonbasic lands that supported the actual gold cards you wanted to play.

[Cliffrunner Behemoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth) improved a lot because of the change. Lots of people had blue-white-green decks with [Noble Hierarch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch)s, [Birds of Paradise](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise), and tons of cheap efficient gold creatures. Most of these creatures were white, so [Cliffrunner Behemoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth) didn't have to work hard to gain lifelink in these decks. It also played very well in red-green decks with *Shadowmoor* cards like [Vexing Shusher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vexing+Shusher), [Boggart Ram-Gang](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Ram-Gang), and Boar-Tusk Liege. We also discovered the amusing combination of [Figure of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny) and [Cliffrunner Behemoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cliffrunner+Behemoth), which worked out much better than I thought it would when we tried it with all of the *Shadowmoor* filter lands that include green.



|  |  |
| --- | --- |
|  |  |

[Kederekt Parasite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) and [Bloodhall Ooze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodhall+Ooze) also profited from the change. Black-red beatdown decks including some combination of those cards with [Shambling Remains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Remains), [Ashenmoor Gouger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashenmoor+Gouger)s, Demigods of Revenge, and [Blightning](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightning)s were staples of our *Conflux*-era FFL testing. Those decks were all fun. Playtester Steve Warner also discovered the amusing combination of [Spiteful Visions](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spiteful+Visions) and [Kederekt Parasite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite), and he has killed me before by using [Ghitu Encampment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghitu+Encampment)s as red permanents for his Parasites.

![](https://web.archive.org/web/20130606192526im_/http://wizards.com/mtg/images/daily/ld/ld26_3Cards.jpg)  
Finally, we were excited because the new versions of the cards didn't feel exactly like gold cards. Even if you have all the right mana, you still need to put together the right group of permanents to get the bonuses. This is exactly the sort of thing that we like to see in a second set twist of a mechanic. It's different from gold cards, but it plays great with gold cards because your gold cards help trigger them and because the nonbasic lands you want to play to support your gold cards don't get in the way. I also really enjoy how swingy and interactive the printed versions of the cards are. Sometimes your [Sedraxis Alchemist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedraxis+Alchemist) is a full-blown [Man-o'-War](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War), which feels very powerful. Other times, your opponent gets to thwart you with a removal spell and you become sad. That kind of back-and-forth interaction makes for great **Magic**.

In the end, I'm thrilled with where the "color matters" cards ended up. They are fun and exciting in Limited and better in Constructed than I ever thought they could be, and they feel like a unique and new development of the block's themes. I hope you enjoy playing with them in the real world as much as I did in the Pit!

Last Week's Poll


|  |
| --- |
| **Is your favorite mythic rare in *Conflux*[Nicol Bolas, Planeswalker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker)?**  |
| Yes | 2604 | 40.3% |
| No | 3862 | 59.7% |
| **Total** | **6466** | **100.0%** |

  


|  |
| --- |
| **What is your favorite *Conflux* mythic rare that is not [Nicol Bolas, Planeswalker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker)?** |
| [Progenitus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Progenitus) | 1654 | 23.3% |
| [Maelstrom Archangel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maelstrom+Archangel) | 1620 | 22.8% |
| [Ethersworn Adjudicator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ethersworn+Adjudicator) | 899 | 12.7% |
| [Apocalypse Hydra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Apocalypse+Hydra) | 692 | 9.8% |
| [Mirror-Sigil Sergeant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirror-Sigil+Sergeant) | 663 | 9.3% |
| [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) | 624 | 8.8% |
| [Child of Alara](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Child+of+Alara) | 394 | 5.6% |
| [Malfegor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Malfegor) | 346 | 4.9% |
| [Conflux](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conflux) | 205 | 2.9% |
| **Total** | **7097** | **100.0%** |

  
I asked this week's question in a sideways way because I thought that [Nicol Bolas, Planeswalker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas%2C+Planeswalker) was the obvious leading candidate for favorite mythic rare, and I didn't want the poll to come back with tons of votes for him and none for anyone else. I would have guessed that more people would have Nicol Bolas as a favorite. Although he did get a plurality of votes, it seems now that I could have run one poll with all ten mythic rares and gotten something reasonable out of it. I was happy to see that the five-color theme clearly was speaking to people since the top two non-Nicol Bolas picks were [Progenitus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Progenitus) and [Maelstrom Archangel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maelstrom+Archangel), but I was sad to see that less than ten percent of respondents picked my favorite card in the set. Once again, thanks for your feedback.

This Week's Poll


|  |
| --- |
| **How do you feel about *Shards of Alara* draft with *Conflux* compared to drafting only *Shards of Alara*?**I like *Shards of Alara* / *Conflux* draft more.I like them both equally.I like triple-*Shards* draft more.I have only drafted *Shards of Alara* with *Conflux*.I have only drafted *Shards of Alara* by itself.I have never drafted *Shards of Alara* block cards. |








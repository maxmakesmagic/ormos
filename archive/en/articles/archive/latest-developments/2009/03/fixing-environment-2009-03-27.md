
---
[Link to Wayback Machine](https://web.archive.org/web/20210429123233/https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Hello everyone, and welcome to the end of Mana Fixing Week. Magic developers like mana fixers. We know that it isn't any fun when you can't cast your spells, and mana-fixing cards let you cast spells of various colors much more reliably. On top of being fun, casting cards of many colors more consistently is also powerful, and the most powerful mana fixing cards are often"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646491"
[_metadata_:publish_date]:- "2009-03-27"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Fixing the Environment"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 12:32:33"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429123233id_/https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27"
---


Fixing the Environment
======================



 Posted in **Latest Developments**
 on March 27, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







Hello everyone, and welcome to the end of Mana Fixing Week. **Magic** developers like mana fixers. We know that it isn't any fun when you can't cast your spells, and mana-fixing cards let you cast spells of various colors much more reliably. On top of being fun, casting cards of many colors more consistently is also powerful, and the most powerful mana fixing cards are often played heavily. Different categories of mana fixing cards being powerful can have subtle but significant effects on environments, and **Magic** developers think about those effects while they build sets. Today I'll talk about the non-obvious effects that various kinds of mana fixing have on **Magic** environments and what we've learned from watching them play out in the real world.


One obvious thing we do to fix mana is to print two-color dual lands, and from set to set they tend to work in very similar ways. We avoid making them strictly better than basic lands to make sure that there are costs to playing multiple colors. One way we do this is making them come into play tapped some of the time, like *Lorwyn*'s tribal lands. Another is to put an extra cost on making each of the two colors the dual land produces, like *Tenth Edition*'s painlands. The last trick we use is to make lands that produce two colors of mana but don't simply tap for one mana of either color, like *Shadowmoor* and *Eventide*'s filter lands.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_3CardsAcross.jpg)Different cycles of dual lands have slightly different effects; for example, *Lorwyn*'s dual lands encourage you to play tribal decks and *Shadowmoor* and *Eventide* filter lands make playing colorless lands more costly. However, their overall effect on Constructed **Magic** is very similar from cycle to cycle. They let you play two-color decks fairly effortlessly and let you think about playing three or more colors if you are willing to stretch. Because dual lands tend to work very similarly, they don't radically effect the environments they are in.


Dual lands are by no means the only tools that we give players to help fix their mana, and those other tools often have much more noticeable effects on **Magic** environments. Today I'll talk about three kinds of mana fixers we have printed. I'll cover why each of them is appealing as well as the subtle side effects they have.


### Mana Artifacts


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_cross1.jpg)On a very basic level, mana acceleration cards are fun because they let you play spells faster than you should be able to. We normally put this effect only in green as part of the mechanical definition of the colors. However, we also print artifacts that make mana, which lets every color get in on the fun. Some of these artifacts produce only colorless mana, and others make one or more colors. The most recent example of powerful mana artifacts are *Ravnica*'s signets. These did a fantastic job of letting players play all the exciting multicolored cards that *Ravnica* had to offer.


Efficient mana artifacts hurt green by taking away one of its strengths and giving it to every color. Part of green's color pie is efficient mana acceleration. Many green mana accelerators are creatures such as [Birds of Paradise](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise), but cards like [Rampant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampant+Growth), [Fertile Ground](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertile+Ground), and [Kodama's Reach](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kodama%27s+Reach) are still perfect for people who don't want the fragility that comes with mana-accelerating creatures. They also are perfect for decks that use mass removal spells like [Wrath of God](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) to defend themselves while ramping up to big spells. Those decks often go to green to get the mana acceleration they need. However, when there are efficient mana artifacts around, they can get the same ramping effect without having to add a color.




|  |  |
| --- | --- |
| 
Azorius Signet
 | 
Gruul Signet
 |

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_mindStone.jpg)This is very crushing for green. Decks that would have played green to get access to mana acceleration that also want other things green has to offer must consider if they would be better off just playing artifacts for mana acceleration instead and doing without the other green cards they wanted. Decks that only wanted green for mana acceleration can ignore green entirely and play artifacts. Decks that are based in green and use green's mana acceleration cards need a very compelling reason to stay green, or they might also be better off moving to other colors where they can get mana accelerators that are nearly as good as green's while having access to other colors' best cards too. Blue decks in particular love it when powerful artifact mana accelerators exist. Mana acceleration and card drawing are two of the most powerful mechanics in **Magic**, and good mana artifacts mean that blue gets access to both of them at the same time!


Another effect of efficient mana artifacts that produce colored mana is that they allow you to play many more colorless lands than you otherwise would be able to. Colorless lands normally hurt you by making it less likely that you can play your colored spells, but a deck that plays a bunch of mana artifacts in addition to lands can just use the artifacts to get the colored mana they need and play tons of interesting colorless lands too. For example, check out this mana base from the Top 8 of [the World Championships in 2006](/en/events/coverage/mihara-dutch-crowned-world-champions).


4 [Urza's Tower](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Tower)  

4 [Urza's Power Plant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Power+Plant)  

4 [Urza's Mine](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Mine)  

1 [Urza's Factory](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Factory)  

1 [Academy Ruins](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Academy+Ruins)  

4 [Hallowed Fountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hallowed+Fountain)  

4 [Adarkar Wastes](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adarkar+Wastes)  

1 [Island](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)  

4 [Azorius Signet](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Azorius+Signet)  

3 [Dimir Signet](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dimir+Signet)


This mana base came from [a blue-white control deck](/en/articles/archive/event-coverage/decklists-top-8-decks-2006-12-01). Only nine of its lands make blue mana, but thanks to the whopping seven Signets the deck will not often be lacking for blue mana despite playing fourteen lands that produce only colorless. Without the Signets, there's no way a blue control deck could get away with having over half its lands not produce any color of mana.


### Mana Creatures That Block Well


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_cross2.jpg)We print lots of creatures that help you make mana. They are mostly green, and range from the humble [Llanowar Elves](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves) to flashy block-specific cards like [Noble Hierarch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch). Many of these creatures have tap abilities that make mana, which means that they can't make mana and block on the same turn. Most of these also have low toughness, so if they block early in the game they are in the graveyard and don't keep making you mana. You can always use them to chump-block later on but then they won't have protected you in the early game.


We sometimes print mana-accelerating creatures that can both block and accelerate mana. The most notable of these have been [Wall of Roots](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Roots), [Vine Trellis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vine+Trellis), and [Sakura-Tribe Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder). [Vine Trellis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vine+Trellis) can't block if you just used it for mana, but it often doesn't die when it blocks. [Sakura-Tribe Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder) will almost certainly die when it blocks, but it was always going to die eventually when it fetched you a land. [Wall of Roots](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Roots) is in the best of both of these worlds; it survives combat with most cheap creatures and lets you block even immediately after using it to make mana.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_3CardsAcross1.jpg)These cards do exactly what many midrange green-based decks want. Not only do they accelerate mana so that expensive spells can come down faster, but they also provide some defense against aggressive creature swarms. Without these cards, those decks would have had to include one set of cards to accelerate their mana and another set of cards to defend against early creature beatdown. With them, they get to skimp on early defense and crutch on their mana accelerators instead. Of course, that's also exactly why these cards are so appealing. Playing expensive and splashy spells is fun, and these cards both get you the mana you need to do it and keep you from dying before you get there.




|  |  |
| --- | --- |
| 
Sylvan Scrying
 | 
Reap and Sow
 |

Midrange green decks that have access to these cards can go surprisingly low on defensive cards without becoming weak to creature assaults. In the summer of 2005, I spent a lot of time playing a mono-green deck built around the Urza's lands. That deck used [Sylvan Scrying](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sylvan+Scrying) and [Reap and Sow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reap+and+Sow) to assemble the Urzatron, then used big spells like [Tooth and Nail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tooth+and+Nail) to put the opponent away. Almost everyone who played that deck used [Sakura-Tribe Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder), and many players also used [Oblivion Stone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Stone) to have defense against creature swarms. Someone suggested to me that I try adding [Vine Trellis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vine+Trellis), and when I did I was shocked to find that I no longer needed [Oblivion Stone](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Stone) against creature swarms. My anti-creature package consisted only of four each of [Sakura-Tribe Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder) and [Vine Trellis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vine+Trellis) and a single [Duplicant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duplicant), and that usually bought me enough time to cast [Tooth and Nail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tooth+and+Nail) before dying.


This effect has also played out on a large scale in real-world tournament formats. One example is Kamigawa Block Constructed, which in many ways was dominated by [Sakura-Tribe Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder). The Top 8 of Pro Tour Philadelphia contained seven midrange green decks that each had four Elders, and the qualifier season following it was dominated by green-based [Gifts Ungiven](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven) control decks, which used [Kagemaro, First to Suffer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kagemaro%2C+First+to+Suffer) and [Sickening Shoal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickening+Shoal) as their main creature removal. Both of these cards have problems; [Kagemaro, First to Suffer](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Kagemaro%252C%2BFirst%2Bto%2BSuffer) costs six total mana to use, and [Sickening Shoal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickening+Shoal) is very expensive if it is not played with the alternate cost. [Sakura-Tribe Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder)'s one-turn Fog effect was key to the Gifts deck's ability to survive early assaults from against mono-white and mono-black creature decks.


### Five-Color Mana


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_cross3.jpg)Two of the most fundamental things about how **Magic** works as a game are the mana system and the color pie. The mana system ensures that the player must make a choice of which color to play, and the color pie makes that choice meaningful. Mana fixers that help you play two colors don't undermine that feeling of choice because you still have to pick two of the five colors to play. Five-color mana fixers, however, let you avoid having to make a choice and instead play cards of any color. On the other hand, they are appealing exactly because they let you "break the rules." Playing all five colors feels like getting away with something, which is exciting. It's also fun to have the freedom to play any card you can think of putting in your deck.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_handOfCards.jpg)Devin Low wrote [an article](/en/articles/archive/latest-developments/dark-side-mana-fixers-2007-05-25-0) about how *Time Spiral* block flirted with five-color mana after the *Time Spiral* Block Constructed [Pro Tour–Yokohama](/en/events/coverage/wafo-tapa-tops-them-all). He is absolutely right about how cards like [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse) and [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) let players play extra colors for little cost. However, I don't think that it's automatically a bad thing when colors bleed a little bit. I was still in the real world when Time Spiral block was new, and I had a lot of fun playing the multicolor blue control decks that Devin talks about in that article. It's not every day that you get to play [Bogardan Hellkite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bogardan+Hellkite), [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation), [Careful Consideration](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Consideration), and [Gaea's Blessing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Blessing) in the same deck, and I really enjoyed the change of pace. I also felt that playing five colors had some serious consequences for my deck. Have a look at the mana base that I played in the *Time Spiral* block [Grand Prix–San Francisco](/en/events/coverage/scott-vargas-repeats-golden-state).


4 [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens)  

4 [Coalition Relic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coalition+Relic)  

4 [River of Tears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears)  

4 [Tolaria West](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolaria+West)  

4 [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse)  

3 [Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth)  

2 [Urza's Factory](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Factory)  

1 [Academy Ruins](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Academy+Ruins)  

1 [Dreadship Reef](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dreadship+Reef)  

1 [Molten Slagheap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Molten+Slagheap)  

1 [Forest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest)  

1 [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)  

1 [Swamp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)  

1 [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains)  

3 [Island](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)


I don't think that it's automatically a bad thing when a mana base like this can function in a format. I enjoyed playing this deck a lot because it was markedly different from other blue control decks I had played. It also required me to make some serious sacrifices to get access to all five colors of mana. [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) is nowhere near as powerful as the *Ravnica* Signets, and spending my third turn doing nothing but casting [Coalition Relic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coalition+Relic) was often painful. [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse) required that I put one of each basic land other than [Island](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island) in my deck, which introduced inconsistency because sometimes I would draw the [Forest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest) and [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) and then have trouble casting [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) and [Careful Consideration](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Consideration). Also take note of the fact that my mana base was 35 cards. That meant that I only had 25 other cards in my deck that could do other things. I had the ability to transmute [Tolaria West](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolaria+West) for [Slaughter Pact](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slaughter+Pact) and [Pact of Negation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pact+of+Negation), but just as often I would search for [Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth) and sometimes I would just play it as a land.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_3CardsAcross3.jpg)All of these factors meant that the decision to play all five colors had some real consequences. I could have cut some of the extra colors and had a more consistent deck, but I chose not to. Amusingly, **Magic** developer Erik Lauer thinks that I made the wrong choice with that deck. His *Time Spiral* block blue decks didn't play [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse) and instead had enough [Island](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)s to consistently suspend [Ancestral Vision](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Vision) on turn one. He also played [Cancel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) because he had the ability to consistently cast [Careful Consideration](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Consideration) and still have two more blue mana open, which my list did not. He also played fewer total mana sources than I did because he only needed to support two colors most of the time, so he simply had more spells that did things in his deck. The fact that we could have that discussion and not be sure who is right at the end shows that the choice to seriously extend to five colors or not was interesting in that format.




|  |  |
| --- | --- |
| 
Vivid Creek
 | 
Reflecting Pool
 |

On the other hand, I think that five-color mana fixing goes wrong when that discussion stops being interesting. Unfortunately, *Lorwyn*'s Vivid lands create a situation similar to that in Standard right now. Thanks to them and [Reflecting Pool](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reflecting+Pool), control decks in Standard can play all five colors very easily. In contrast to *Time Spiral* Block, where playing all five colors seriously impacted your mana base's consistency and made you play more mana sources than you might have otherwise wanted to, modern five-color control decks in standard get all the colors they need from their lands alone. The Vivid lands do come into play tapped, but control decks often don't do many things on their early turns so this is not a huge cost. We regret the Vivid lands because they do not create the same level of consequence for players who want to play all five colors as *Time Spiral* block's mana fixing did.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld31_cross4.jpg)Today I discussed three kinds of mana-fixing cards we print and the effects they have on **Magic** environments. All three of the categories I talked about have been popular and are things we like to do. However, you might have read some of the effects I listed and wondered to yourself if they were actually reasons to not print them. For example, one could say that [Sakura-Tribe Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder) was a mistake because it hurt aggressive decks, or that *Ravnica*'s Signets were a mistake because they gave blue decks access to mana acceleration they shouldn't have had. While those cards did have those effects, that doesn't mean that we shouldn't have made them. **Magic** is a great game because it changes over time, and the mana fixers we print each year have different subtle effects. It's our job as developers to recognize exactly what those effects are, be responsible for their impact, and change them over time to keep the game fresh. I hope you enjoyed Mana Fixing Week!


### Last Week's Poll




| **How many colors does your favorite Magic deck play?** |
| --- |
| 0 | 99 | 1.3% |
| 1 | 1146 | 15.1% |
| 2 | 2950 | 38.8% |
| 3 | 2173 | 28.6% |
| 4 | 301 | 4.0% |
| 5 | 925 | 12.2% |
| **Total** | **7594** | **100.0%** |








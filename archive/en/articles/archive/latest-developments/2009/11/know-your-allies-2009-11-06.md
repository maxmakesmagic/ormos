
---
[Link to Wayback Machine](https://web.archive.org/web/20210429024137/https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Welcome to the end of Ally Week! Today, I'll be telling the story of the overall development of the Allies, and then I'll tell the stories of a few Allies in particular. The Allies Developers Tell I'd like you to put on your Magic developer hat and ponder a question for a moment. How far below the power curve should an Ally be in a Limited deck that has no other Allies? Before"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646971"
[_metadata_:publish_date]:- "2009-11-06"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Know Your Allies"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 02:41:37"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429024137id_/https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/know-your-allies-2009-11-06"
---


Know Your Allies
================



 Posted in **Latest Developments**
 on November 6, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







Welcome to the end of Ally Week! Today, I'll be telling the story of the overall development of the Allies, and then I'll tell the stories of a few Allies in particular.


### The Allies Developers Tell


I'd like you to put on your **Magic** developer hat and ponder a question for a moment. How far below the power curve should an Ally be in a Limited deck that has no other Allies?


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld63_allyCross.jpg)Before you go running in horror, let me explain. Allies are a linear mechanic; the more Allies you have in your deck, the better they all are. If each Ally alone were as powerful as a normal card, everyone would take them very high in drafts, and you would never have the chance to accumulate lots of them to make an awesome-feeling deck. However, if they were all worse than normal cards, few people would think to draft an Ally deck to begin with. What to do?


We've done a linear mechanic with similar consequences for Limited before. Do you remember where?




|  |  |
| --- | --- |
| 
Krovikan Mist
 | 
Sound the Call
 |

Yes, that's right! We did it in *Coldsnap*. *Coldsnap* had a number of commons like this that scaled in power based on the number of them you had in your deck. A single [Krovikan Mist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krovikan+Mist) is a two mana 1/1 flyer, and a lone Wolf from a [Sound the Call](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sound+the+Call) is a three mana 2/2; neither of these are anything to write home about. However, *Coldsnap* was a small set that was drafted as though it were a big set, so it was very possible to collect large numbers of either of these cards. I've seen *Coldsnap* draft decks with seven of each of these two cards, and with that many copies of them the cards were quite powerful.


We started the Allies in *Zendikar* in a spot similar to this. Have a look at Low Level Wizard and Faithful Robot, two Allies from early *Zendikar* design.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld63_playtest.jpg)Note that these cards are templated so that they do not give themselves a +1/+1 counter. A Low Level Wizard without a party is actually a two mana 1/2, and a Faithful Robot with no one to be faithful to is a sad four mana 2/3.


This made the Allies look bad, but it had a hidden benefit. In draft playtests, no one would touch the things if they weren't drafting a teamwork deck. That left the door wide open for someone who wanted to draft a dedicated teamwork deck to swoop in and get almost every Ally at the table. I won a playtest draft once with a whopping seven Low Level Wizards and two Faithful Robots, which could only happen because no one else was interested in taking them. Nothing as amazing as that happened again, because after that draft people started to wise up and began to hate draft Allies late in the pack when nothing else was there for them. However, generally speaking the Allies were still making it to the people who wanted them, and everyone else refused to touch them.


This is exactly what allowed people to collect upwards of seven copies of [Krovikan Mist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krovikan+Mist) and [Sound the Call](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sound+the+Call) in triple *Coldsnap* drafts. However, there was also a real cost to having the Allies only be appealing to people who were playing Allies. That cost is that, well, they simply looked weak. Two mana 1/3's and four mana 2/3's are not the kind of cards that get most people excited about a mechanic. The Allies were important for conveying the flavor of the set, but they wouldn't do that work if no one wanted to play them in the first place!




|  |  |
| --- | --- |
| 
Whipcorder
 | 
Exalted Angel
 |

To accomplish our goals, we needed to include some Allies that were reasonable to play without a big pile of fellow Allies. *Zendikar* developer Erik Lauer observed that a player's journey toward liking a **Magic** mechanic often begins with one or two cards that are obviously powerful enough to play. For example, Whipcorder and Exalted Angel served as flagbearers for morph in *Onslaught*, showing players the fun that was present in the mechanic. We needed to have Allies that mimicked this effect, drawing players into having Allies in their deck. This would both show them that Allies were fun to play with and make all the rest of the Allies more powerful.


Mark Rosewater [talked in his article this week](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/63) about the division that the *Zendikar* designers made between "fighters," "clerics," and "wizards." They decreed that every Ally would have an ability that triggered every time an Ally entered the battlefield. However, fighters were Allies whose abilities put +1/+1 counters on themselves, clerics were Allies who gave temporary bonuses to every Ally you controlled, and wizards were Allies whose triggered abilities explicitly counted the number of Allies you controlled.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld63_oranUmaraCross.jpg)By nature, the clerics and wizards needed lots of other Allies to be powerful. Therefore, it fell to the fighters to carry the flag for the rest of the Allies. We chose to give each of the fighters numbers that would let you play them in any Limited deck with a straight face. For example, [Oran-Rief Survivalist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oran-Rief+Survivalist) and [Umara Raptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umara+Raptor) have the same numbers as [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) and [Wind Drake](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wind+Drake), both of which are cards that are more than reasonable to play in any Limited format. However, with only a little help they get significantly better.




|  |  |
| --- | --- |
| 
Oran-Rief Survivalist
 | 
Umara Raptor
 |

Making this change did exactly what we wanted in our playtesting. It was not uncommon in *Zendikar* limited for me to take a [Nimana Sell-Sword](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nimana+Sell-Sword) to fill in my black deck's curve, then take a second [Nimana Sell-Sword](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nimana+Sell-Sword) over something that I might have taken over the first one. Suddenly, the next [Hagra Diabolist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hagra+Diabolist) I see has gone up in value even though I didn't go out of my way to make an Ally deck. This is exactly how Erik hoped the Allies would work in practice.


One of the most exhilarating things I experience as a **Magic** developer is when I interact with players in the real world and watch things happen exactly how we hoped they would. I got to experience that recently when I hosted a draft at my apartment with some friends. I opened a [Murasa Pyromancer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murasa+Pyromancer), which is an extremely strong card in an Ally deck–so strong, in fact, that I decided to move in on Allies with my first pick. It was clear to me by the end of the draft that I was the only pure Ally drafter at the table; I got all of the [Stonework Puma](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stonework+Puma)s and [Tajuru Archer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tajuru+Archer)s I could handle. However, my friend Jon had picked a [Tuktuk Grunts](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tuktuk+Grunts) to fill in his curve, which prompted him to take a [Murasa Pyromancer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murasa+Pyromancer) just before it got to me in pack two. I was unhappy, but I was satisfied that the Allies were working the way we meant them too. I was also quite satisfied with my deck, which had a whopping fifteen Allies in it!


### True Stories, Honest Allies


Now, let's investigate a few Allies in particular that have interesting stories.


### Makindi Shieldmate


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld63_makindiSlice.jpg)One development tool that *Zendikar* lead developer Henry Stern used was something that he called "league". In the Future Future League, we play as though we have access to four copies of every card so that we can get a picture of competitive Standard, but we need to make sure that **Magic** is fun at every level. To get a different picture, Henry gave each of us ten rares, and asked us to build decks using up to one copy of each of those rares, up to two copies of any *Zendikar* uncommon, and up to four copies of any *Zendikar* common. I received both [Kazuul Warlord](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kazuul+Warlord) and [Turntimber Ranger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turntimber+Ranger) in my rares, so I tried to build an Ally deck. However, the very first Ally I hit in the file was [Makindi Shieldmate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makindi+Shieldmate). I wanted my deck to attack, so I made this comment, and moved on.



![Makindi Shieldmate](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Makindi+Shieldmate)

 



> 
> TML 11/20/2008: This card disappointed me when I went to build a teamwork league deck. :B
> 
> 
> 


This prompted a similar comment from Greg Marques, an experienced designer who has worked on many **Magic** sets.


 



> 
> GM 11/21: What's the upside here? If I have a teamwork deck I will have several huge creatures that are big enough to block anything, what does this guy add to the team?
> 
> 
> 


I later returned to the file with a few weeks' perspective, and suddenly I was defending the card. I still don't know what prompted this comment, but **Magic** development is as much an art as it is a science and I suppose I just had a feeling here.


 



> 
> TML 12/1/2008: I don't really have a good reason why, but I think this is a reasonable thing to have around. Big defenders are fun, and this guy does get big.
> 
> 
> 


Aaron Forsythe and Ken Nagle both have more game design experience than I, and they were able to articulate the reasons why [Makindi Shieldmate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makindi+Shieldmate) should exist.


 



> 
> AF 1/4: People who like linear scaling mechanics often like to sit around and grow their team. This guy is perfect for that.
> 
> 
> KEN 1/12/2009: It's like SimCity but with Magic cards – as long as you still have stuff in your hand to cast, you're not done building up and thusly not at full fighting capacity. In StarCraft we didn't attack until we had 200 food armies.
> 
> 
> 


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld63_starcraft.jpg)Ken Nagle is a fascinating person to talk to about games. He's very smart, and many people with his intelligence would have used that skill to become an expert player, then do their best to crush everyone they played against, eventually finding their way to the Pro Tour. It is a little-known fact that Ken *has* played in a Pro Tour; he describes this as an accident, but it still demonstrates that Ken is very good at **Magic**. However, he is extremely self-aware and he uses that self-awareness to maximize his own fun rather than his winning. Many of his casual decks are as carefully tuned as any deck I've ever played in a tournament, with exactly the right numbers of each card to be the most fun to play with.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld63_nowItsTime.jpg)The kind of insight that Ken conveyed in this comment field is exactly why he is so valuable to **Magic** R&D. In Starcraft, every unit has a "population" cost, and you aren't allowed to build a unit that would put you over 200 "population" across your entire army. As Ken notes here, much of the fun of Starcraft is the buildup of an enormous army while you watch your population count tick higher and higher. [Makindi Shieldmate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makindi+Shieldmate) both buys you the time you need in a game of **Magic** to tick your army higher and higher and is fun to watch as it gets bigger and bigger!


### Turntimber Ranger


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld63_turnSlice.jpg)The idea of an Elf Ranger who has "pets" was something that we knew was going to have to be on an Ally somewhere. It's a classic trope that is expressed in games like **Dungeons & Dragons**, which is what we were trying to convey in *Zendikar*. However, putting tokens onto the battlefield would make Ranger fall into the "Wizard" bucket, which meant that we were going to need to somehow count the number of Allies on the battlefield when we put a token onto the battlefield. We thought it would be too weird to have an X/X token with X as the number of Allies on the battlefield, because there wasn't a single creature type that would cover all possible values of X. Instead, we decided to have [Turntimber Ranger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turntimber+Ranger) put X 1/1 Wolves onto the battlefield, because X 2/2's seemed crazy to us. As you can see here, Aaron Forsythe and Doug Beyer found the problem with this plan.



![Turntimber Ranger](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Turntimber+Ranger)

 

 



> 
> AF 11/20: Several cards in LRW, MOR, SHM, EVE, and M10 say "Wolves are 2/2." Snakes are 1/1 green tokens in this file...Find a cost that lets the Wolves be 2/2s. I think one 2/2 at a time is enough incentive...It doesn't have to explode exponentially to be really fun.
> 
> 
> DB 11/25/08: Agree with AF, making this guy's Wolves 2/2 would really help me make 1/1 green Snakes.
> 
> 
> AF 1/4: These will somehow be 2/2s; Del's issue to be discussed.
> 
> 
> 


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld63_wolfs.jpg)Aaron put his foot down, forcing us to come up with a different ability. We felt quite stuck for a while; we didn't want to put X 2/2's onto the battlefield, but we also needed Ranger to create Wolves, and Wolves are 2/2's. In a frantic meeting, someone came up with the idea of making [Turntimber Ranger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turntimber+Ranger) a "dual-class" Ally; that is, it would be a fighter, but do something else too. We found this satisfying, and now [Turntimber Ranger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turntimber+Ranger) gets both a +1/+1 counter and a Wolf friend every time a new Ally arrives on the battlefield.


### Last Week's Poll




|  |  |  |
| --- | --- | --- |
| **When was the last time you played Magic Online?** |  |  |
| I've never played Magic Online. | 4166 | 55.8% |
| More than 6 months ago | 1145 | 15.3% |
| Within the last 6 months | 218 | 2.9% |
| Within the last 3 months | 270 | 3.6% |
| Within the last month | 274 | 3.7% |
| Within the last week | 633 | 8.5% |
| Today | 416 | 5.6% |
| I'm logged into Magic Online right now! | 344 | 4.6% |
| **Total** | **7466** | **100.0%** |

There is no greater meaning to this poll. I was merely curious. Thanks for the feedback!









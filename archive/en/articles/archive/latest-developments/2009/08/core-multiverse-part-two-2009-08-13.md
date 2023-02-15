
---
[Link to Wayback Machine](https://web.archive.org/web/20211201011949/https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-two-2009-08-13)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Four weeks ago, I showed you some behind-the-scenes discussions from the making of Magic 2010 that happened in Multiverse, the database that we use to make Magic cards. I also promised that there would be more, and this week I will deliver on that promise. Let's jump right in!Alluring Siren[card]Alluring Siren[/card]I started working as a Magic developer when Conflux was about"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "188431"
[_metadata_:path_date]:- "2009-08-13"
[_metadata_:publish_date]:- "2009-08-14"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Core of the Multiverse, Part Two"
[_metadata_:wayback_capture_timestamp]:- "2021-12-01 01:19:49"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211201011949id_/https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-two-2009-08-13"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-two-2009-08-13"
---


The Core of the Multiverse, Part Two
====================================



 Posted in **Latest Developments**
 on August 14, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






Four weeks ago, I showed you some behind-the-scenes discussions from the making of ***Magic** 2010* that happened in Multiverse, the database that we use to make **Magic** cards. I also promised that there would be more, and this week I will deliver on that promise. Let's jump right in!

Alluring Siren
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Alluring+Siren)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alluring+Siren)I started working as a **Magic** developer when *Conflux* was about halfway through development. At that time, we were turning knobs that determined card power, like mana costs and creature power and toughness, and similar conversations happened through the development of *Alara Reborn*. Many similar conversations happened during ***Magic** 2010* development, but I was surprised and delighted to see another kind of conversation dominate the early stages of our work on the set. These new conversations were about whether or not we matched top-down design concepts. Here's an example from [Alluring Siren](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alluring+Siren).


> Del 5/20: Attacks, or attacks you? Planeswalkers and multiplayer fans want to know.  
>  LS 6/9: "Attacks you" seems bad to me, mostly because of multiplayer.  
>  KEN 6/25: "attack you" makes flavor sense, as the Siren is alluring. "Must attack" has a berserking flavor.  
>  AF 7/22: You.
> 
> 

Popular opinion was moving toward "attacks you" already, but as the lead designer Aaron decided to put his foot down and save everyone some time. As Ken Nagle observes, "attacks you" is just correct for a Siren, and it was more important for this card that it be a good siren than it have a particular power level. We knew that this particular card was unlikely to cause problems in Constructed, but if it had, we would have sacrificed card power before sacrificing its fundamental siren-ness.

The card changed a little bit more in templating based on some later comments.


> MT 7/23: Seems like I can make my own creatures attack me!  
>  DAL 7/28: If they are able, they will do it!  
>  MT 11/10: Added "An opponent controls."
> 
> 

![](http://wizards.com//mtg/images/daily/ld/ld51_sirenAliver.jpg)  
The rules don't allow you to attack yourself with your own creature, but we added a few extra words to avoid implying that the Siren could make that happen.

No matter how experienced a **Magic** player is, there's always more room to learn about what can happen in a game of **Magic**. I have learned from focus tests that [Alluring Siren](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alluring+Siren) is a card that can expose entirely new players to deeper layers of what **Magic** can be. People who are new to **Magic** do not find the card appealing because they don't want to be attacked, but an hour or two into their interaction with **Magic** cards they discover that they can use it to pull an opponent's creature into a [Craw Wurm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Craw+Wurm) or even just a [Wall of Frost](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Frost). Those moments of discovery are beautiful, and they are why I and many others find **Magic** so engaging.

Wall of Bone
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wall+of+Bone)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Bone)As the [Alluring Siren](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alluring+Siren) record indicates, we spent a lot of time thinking about whether top-down ***Magic** 2010* cards matched expectation or not. This resulted in a lot of great cards, but it also caused a bit of wasted time when we debated decisions that we didn't know had already been made. Here's the Multiverse record from [Wall of Bone](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Bone).


> DB 6/11/08: Creature - Skeleton Wall? Nah.  
>  DAL 7/28: Skeleton Wall sounds awesome. If the white Exorcist exiles Skeletons, Zombies, and Vampires, do you want him to hit this? I think yes.  
>  AJ 7/28: I remember seeing a fan-made cardset and several cards had the phrase "Target Skeleton, Zombie, or [Wall of Bone](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Bone)" in it. And Skeleton Wall sounds awesome.  
>  TML 8/4: I love Skeleton Wall.  
>  MP 8/7: Agree with Skeleton Wall.  
>  Del 11/12: Temporary insanity seems to have taken hold. What on earth are you guys trying to vote on here? It's been a Skeleton Wall in Oracle since January!
> 
> 

[Wall of Bone](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Bone) is a reprint, but it hadn't been printed since *Seventh Edition* so updating its creature type was something we could have done. However, Mark Gottlieb had beaten us to it during the Grand Creature Type Update. At least we got what we were hoping for!

Stone Giant
Sometimes it takes a lot of words to make a card's mechanics match its concept, and [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant) uses a lot of words. Check out the beta text box:

![](http://wizards.com//mtg/images/daily/ld/ld51_giantSliver.jpg)  
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Stone+Giant)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant)No one in **Magic** Ramp;D claims that this original wording is clear. However, many cards in Alpha have evocative and mildly bewildering text like this, and those are the cards that made early **Magic** successful. Aaron wanted ***Magic** 2010* to recapture that, so he put some of those Alpha cards in. That prompted some conversations about what amount of flavorful rules text was acceptable. Here is an example of one of those conversations.


> NH 9/26: I like the concept of stone giant, but as long as we are making new cards, why not do a cleaner version of this? The whole comparing toughness to power thing seems not worth it for what this card is trying to do.  
>  AF 10/9: It is trying to be flavorful and say a 3/4 giant can't throw a 7/7 baloth!  
>  LS 11/3: Agree with NH. I think we can say what this card is trying to say without a lot of awkward, confusing words.  
>  Del 11/6: I'm not convinced that the old-style flavor cards make sense in the context of modern card sets. Take [War Barge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Barge), for example. It was one of the TSP "timeshifted" cards, and it proved to be completely baffling. Read this:  
>  {o3}: Target creature gains islandwalk until end of turn. When [War Barge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Barge) leaves play this turn, destroy that creature. A creature destroyed this way can't be regenerated."  
>  The flavor is there -- if the barge sinks, the creature drowns -- but I don't think the incremental flavor bonus of those last two sentences is worth the extra effort required to figure out what the card does.  
>  AF 1/5: Somewhat disagree. Many people made decks to try and sink their own [War Barge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Barge)... while YOUR creatures were on it! MUHAHAH!
> 
> 

Aaron is the only person who defends [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant) in this Multiverse record. However, he was not alone in his support for it; the ***Magic** 2010* development team also liked the card, both as an individual unit and for what it did in Limited. Many [Looming Shade](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Looming+Shade)s and [Fiery Hellhound](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Hellhound)s were harmed by [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant)s in the making of ***Magic** 2010*. We also enjoyed throwing [Goblin Piker](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Piker)s and [Runeclaw Bear](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runeclaw+Bear)s at attacking [Wind Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wind+Drake)s and [Stormfront Pegasus](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormfront+Pegasus)es. Finally, [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant)'s 3/4 body was much appreciated by Limited playtesters, so it got to stay.



|  |  |
| --- | --- |
|  |  |

I'm glad that [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant) survived. However, the debate in this Multiverse record is a very reasonable one. As I pointed out with [Raging River](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raging+River) in [Developing Alpha](/magic/magazine/article.aspx?x=mtg/daily/ld/43), it's easy to make a top-down card that is complicated but gets across a concept. The question each time is whether it is worth it. Was [War Barge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Barge) worth the words? Is [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant)? Where would you draw the line?

Dragon Whelp
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dragon+Whelp)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp)[Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) is another ***Magic** 2010* card that came from Alpha in the same wordy tradition as [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant). Just like things thrown by a [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant) die on impact with the ground, [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) explodes if it breathes too much fire. 

***Magic** 2010* left design with [Furnace Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Whelp) as its uncommon dragon. I went on a successful campaign to reprint [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) instead, partially because I love the card and partially because I wanted the word "dragon" in the name of whatever card it ended up being. There were no development comments made about the card after this change was made. This is telling, especially because [Furnace Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Whelp) comes right after [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant) in the ***Magic** 2010* Multiverse file. As we just saw, [Stone Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant) drew some ire from people who questioned the extra rules text, but [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) received no such attention. That tells me that either this card's extra text is more understandably connected to the flavor of a baby dragon or the text itself isn't as hard to process. My guess is that whether or not it was conscious, people found the concept of the exploding baby dragon more resonant and appealing than the concept of a giant who throws things, and because of that they didn't think to say anything about [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp).

During my campaign for [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) I was accused of being too attached to nostalgia. The people who said this may have been correct, but that nostalgia didn't go back as far as they thought it did. The first time I ever cast a [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) was in a *Time Spiral* draft! I fell in love with the card then, and fought for its return based on that. Most of **Magic** Ramp;D has been playing long enough to have cast many [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp)s before *Time Spiral*. My first set was *Tempest*, so compared to them I'm a relative newcomer.

![](http://wizards.com//mtg/images/daily/ld/ld51_twoSliversofCards.jpg)  
A side note that amuses me is that one of the arguments against [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) is that it is confusing to new players, but the opposite of this turned out to be true. People who try to learn to play **Magic** from printed rules rather than being taught by a friend often do not understand that activated abilities without tap symbols can be played more than once in a turn. [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) tells those players explicitly that this can be done. Every time I saw someone run into their first [Dragon Whelp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragon+Whelp) in focus testing, they started playing activated abilities correctly soon after.

Honor of the Pure
[Honor of the Pure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Honor+of+the+Pure) began life with the name Erik's Personal [Crusade](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusade). It doesn't sound like much of a name, but it is a triple entendre. First, ***Magic** 2010* lead developer Erik Lauer designed a version of [Crusade](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusade) that only works on your own creatures and requested that it be added to ***Magic** 2010*. Second, Erik knows that many people enjoy White Weenie strategies, likes them to be powerful, and fought hard to have a powerful card for those decks in his set. Third, Erik personally finds White Weenie decks boring to play with and would be unlikely to play a deck containing [Honor of the Pure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Honor+of+the+Pure) in a real **Magic** tournament if he had the choice.

![](http://wizards.com//mtg/images/daily/ld/ld51_knightsOfRAndD.jpg)  
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Honor+of+the+Pure)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Honor+of+the+Pure)Aaron's name for this card was a source of many laughs, including Erik's first comment in the card's Multiverse record.


> EVL 7/24: LOL  
>  TML 7/25: Stench of horses and hay is overwhelming in Erik's apartment, obvious enemies not apparent. Request for crusade to end  
>  DAL 7/25: If you look in both directions and you don't see the enemy....  
>  DAL 7/25: I like this card. WW has a certain charm, partially because white has a history of awesome WW cards, but I guess that 1W is better for gameplay.  
>  TML 8/7: Clarification: I also like this card.
> 
> 

We tested [Honor of the Pure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Honor+of+the+Pure) in decks very similar to the Kithkin and Soldier decks that are played in the real world today. The card was strong, but we were happy with its power level, so we printed it with no changes.

Virtually every set has a few cards, like [Honor of the Pure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Honor+of+the+Pure), that spring fully formed from a designer or developer's mind, enter the file, and are never changed. We refer to these as "brain-to-print" cards. Many designers and developers have fond memories of their first such card. Due to his position as the lead developer of ***Magic** 2010*, Erik Lauer has a few brain-to-print cards in the set, including this one and [Great Sable Stag](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Great+Sable+Stag). I didn't manage to get any of my own brain-to-print cards into ***Magic** 2010*, but *Zendikar* has one that I'm very proud of. It won't be too much longer before I get to tell you about it!

I was proud of the work that Erik Lauer, myself, and the rest of the development team did on ***Magic** 2010*, and I'm also proud of how well it has been received. I hope you've enjoyed these two looks at the process that created it. Next week is Exiled Week, but I already wrote [my preview article](/Magic/Magazine/Article.aspx?x=mtg/daily/ld/50) about *From the Vault: Exiled*. I'll be doing a Johnny Week article next week instead.

Last Week's Poll


|  |
| --- |
| **Which of the following best describes your favorite non-Magic game?** |
| Board game | 1788 | 17.3% |
| Traditional card game | 604 | 5.9% |
| Paper trading card game | 164 | 1.6% |
| Online trading card game | 40 | 0.4% |
| Tabletop roleplaying game | 1395 | 13.5% |
| Massively multiplayer online game | 1458 | 14.1% |
| Other console or computer video game | 4412 | 42.8% |
| None of the above categories describes my favorite non-Magic game well. | 456 | 4.4% |
| **Total** | **10317** | **100.0%** |

  
I feel that I made an error in this poll by not including an option for tabletop wargames, one of the earliest hobby game categories to ever exist. Unfortunately, it appears that this category is not as strong as it once was based on how few people responded none of the above. The thing that surprised me most about the results of this poll was how popular an option "board game" was. Many **Magic** players in Washington like to play board games more than I was used to in my home state, but I suspected that was only because the demographic of gamers that I interact with here is older than the one that I interacted with back in the Midwest. This poll suggests that they are not the exception even among the general **Magic** population.

This Week's Poll


|  |
| --- |
| **Which of the following ***Magic** 2010* cards do you like the most?**[Alluring Siren](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alluring+Siren)[Burning Inquiry](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Inquiry)[Hive Mind](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hive+Mind)[Megrim](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Megrim)[Mirror of Fate](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirror+of+Fate)[Open the Vaults](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Open+the+Vaults)[Polymorph](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Polymorph)[Warp World](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warp+World) |

[![](https://media.wizards.com/legacy//mtg/images/daily/youdecide/youdecided.jpg)  
(Click here for today's results!)](/Magic/Magazine/Article.aspx?x=mtg/daily/youdecide/08142009)






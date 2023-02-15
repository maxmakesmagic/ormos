
---
[Link to Wayback Machine](https://web.archive.org/web/20210207083131/https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646501"
[_metadata_:publish_date]:- "2009-04-03"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Winding Path"
[_metadata_:wayback_capture_timestamp]:- "2021-02-07 08:31:31"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210207083131id_/https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03"
---


The Winding Path
================



 Posted in **Latest Developments**
 on April 3, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld32_piper.jpg)M**agic** developers treat the game of **Magic** with utmost respect. We choose to work on **Magic** rather than do other things because we love the game, and we do everything with its best interests in mind. Sometimes, the path that this takes us down leads to strange places, and we make decisions that we never thought we would when we began to attack a problem. Many of these interesting and odd decisions are hidden from those who do not work on the game, because only we see the winding path that cards, mechanics, and sets take as they make their way from design to print. Today I'll talk about two different choices **Magic** developers have made that both developers and players found strange, and talk about the reasons we made them.


### Thornling


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld32_thornlingSplash.jpg)[Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) is a throwback to [Morphling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling), a famously powerful **Magic** card that was referred to as "Superman" for many years. Players who recognized the reference asked me over and over at the Prerelease why [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) does not have the ability to untap itself like [Morphling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) and its *Planar Chaos* homage [Torchling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling) do. This was not a mistake. We knew that it looked strange; in fact, it looked strange to many of us as well. However, we were still willing to put that aside and print the most fun [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) we thought we could make.


Like all human beings, **Magic** designers enjoy completing patterns. [Torchling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling) hinted that [Morphling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling)s of other colors might be running around the Multiverse somewhere, so it wasn't a huge surprise when a green version showed up in a design file. The first version was exactly what many people thought [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) was supposed to be:



> 
> Ultraling  
> 
>  3GG  
> 
>  Creature – Shapeshifter  
> 
>  4/4  
> 
>  G: CARDNAME gains trample until end of turn.  
> 
>  G: CARDNAME is indestructible until end of turn.  
> 
>  G: Untap CARDNAME.  
> 
>  1: CARDNAME gets +1/-1 until end of turn.  
> 
>  1: CARDNAME gets -1/+1 until end of turn.
> 
> 
> 


I started working at Wizards about halfway through *Conflux* development, and Constructed playtesting usually becomes the focus at about that point in the development cycle. Being new meant that I had much to learn about how things were done at Wizards, but I was able to contribute immediately by building lots of Future Future League decks. For whatever reason [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) was one of the cards that appealed to me most as I went through the *Conflux* file, so I started building mana ramp decks that showed it off.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld32_3VsG.jpg)I quickly realized that not only was [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) fun to read, it was also one of the most potent cards in my decks. I built them to have lots of mana quickly, and with a little mana [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) dominates the board against ground creature decks. Over and over again, I would attack with a [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) and invite my opponent to block it. I usually had enough mana to pump its power high enough to both kill any blocker and make [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) indestructible, so most of the time my opponents didn't block. I would then still have enough mana to both untap it and make it indestructible, which kept my opponent from attacking me back. Although [Morphling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) and [Torchling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling) do have the ability to untap, giving them enough toughness to survive combat with a high-power creature can be quite expensive. [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) requires only that you pay ![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) to get the same effect.




|  |  |
| --- | --- |
| 
Morphling
 | 
Torchling
 |

More people began playing [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling)s when they saw how powerful it was against creature swarms in decks that had access to a lot of mana. This led to the realization that [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling)-on-[Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) fights were very annoying thanks to the untap ability. When a [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) blocked a [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling), what usually happened was both [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling)s became indestructible, the attacking [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) gained trample and went to 7/1, and the defending one went to 1/7. The next turn, the [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) that just blocked would attack, the other [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) would untap for ![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), then the process would repeat. This was very mathy and turned games into mana arms races, and it was even worse when there were multiple [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling)s on each side.


We grew unhappy with the untap ability, so we explored alternatives. Speaking abstractly, the original [Morphling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling)'s three abilities helped it race, gave it evasion, and protected it from harm. Evasion was already covered by trample and protection was covered by indestructible, so we looked for a different ability that could help it win a race. Vigilance was raised as a simple alternative that frontloaded the untapping cost, but that didn't solve the gameplay problems. Haste was the next suggestion, with the logic that it helps [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) race by letting it attack on the first turn.



![Thornling](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thornling)

  

 I fell in love with the haste idea. It made the card better against control decks because I could attack immediately with it in the late game, and it made the card worse against creature swarm decks because it couldn't both attack and prevent the opponent from attacking. I also thought that [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) standoffs would be less miserable because the decision to attack with one would be more meaningful. I played it that way for a few days and discovered that not only was that logic correct on all counts, but it was also more fun in intangible ways. There was something viscerally awesome about attacking with it immediately, and I fought for the change until it found way into the file. That ability survived all the way to print despite the double-take many of us did every time we read it in the file.


I can't blame anyone familiar with [Morphling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) and [Torchling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling) for thinking that [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) looks strange next to its Shapeshifter brethren. We also found it a little odd, and the decision to take the untap ability away from [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) was contentious. However, I believe we ended up with a more fun **Magic** card because we were willing to let the oddness remain.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld32_cross1.jpg)As a final note, [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) is my favorite *Conflux* card. I played four of it in the Standard deck that I used to gunsling at the *Conflux* Prerelease I attended, and I had tons of fun attacking for 7 over and over again. I hope that it will get a chance to shine at [Pro Tour–Honolulu](/en/node/640716) or in this summer's Standard format Pro Tour–Austin qualifiers!


### Ponder


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld32_ponderSplash.jpg)Vintage is the **Magic** tournament format that gives players the opportunity to play with the widest variety of cards. Only cards that are not legal in any tournament format and those that involve manual dexterity, ante, or subgames are banned. The worst fate that other cards can suffer is being placed on the restricted list, which means that only one copy can be played in a 60-card Vintage deck. We enjoy it when cards like [Tezzeret the Seeker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tezzeret+the+Seeker) and [Inkwell Leviathan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkwell+Leviathan) make a splash in Vintage, but we do not go out of our way to make cards for the format because only the most powerful cards in **Magic** thrive there, and it is impossible to compete with cards like the Moxes while keeping a reasonable power level in Standard. We use [the restricted list](http://archive.wizards.com/Magic/TCG/Resources.aspx?x=judge/resources/sfrvintage) to keep the format fun while still allowing players to play with the largest variety of cards possible.




|  |  |
| --- | --- |
| 
Tezzeret the Seeker
 | 
Inkwell Leviathan
 |

Many restricted cards are famously powerful. However, the DCI does not create the restricted list by applying an objective measurement of power across all **Magic** cards and restricting all cards that are above a certain power level. Instead, the DCI uses the restricted list to sculpt an environment that is fun and diverse. **Magic** developers test standard to make sure there are lots of different reasonable decks to play that are enjoyable. We have the same goals for other formats, and we recommend changes to the DCI when we notice that one of them is becoming stagnant.


On June 1, 2008, the DCI announced the restriction of five cards in Vintage: [Flash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash), [Gush](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush), [Merchant Scroll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll), [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm), and [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder). The motivation for restricting the first three of those cards was clear at the time to most Vintage players, although not all agreed that it was strictly necessary. Using [Flash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash) to put a [Protean Hulk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Protean+Hulk) into play allowed players to immediately win the game if they had the right set of creatures in their library, and decks built to do just that could consistently win the game in the first two turns. Decks built around the [Fastbond](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fastbond)-[Gush](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush) mana engine were also winning tournaments left and right. [Merchant Scroll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll) was a key piece of the decks built around both [Flash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash) and [Gush](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush), and it was not a huge surprise when it eventually joined similar cards like [Mystical Tutor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Tutor) and [Demonic Tutor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Tutor) on the restricted list.




|  |  |
| --- | --- |
| 
Brainstorm
 | 
Ponder
 |

The restrictions of [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) and [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder), however, confused many players. [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm)'s restriction was understandable, although somewhat surprising. A player who casts [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm), puts two useless cards on top of his or her library, and then shuffles his or her library is effectively up three cards, and Vintage has no shortage of cards that let a player shuffle his or her library. [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder)'s restriction was more difficult to explain. Some blue Vintage decks were playing both [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) and [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder), but some only played [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm). It was also difficult to compare [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) in a satisfying way to other previously restricted cards. Because of this, many players were rightfully confused about the DCI's choice to restrict it.


I was not a Wizards employee when I read the announcement of that restriction, and it confused me just as much as it did other **Magic** players. I have since learned the reasoning. I fully acknowledge that it looks strange on paper, but the **Magic** developers had good reasons for their decision. I was pleasantly surprised to learn them.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld32_cross2.jpg)Ever since *Future Sight* was released, the most powerful Vintage decks have revolved around one or more of [Dark Ritual](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual), [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will), [Bazaar of Baghdad](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bazaar+of+Baghdad), and [Mishra's Workshop](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop). These are some of the most powerful unrestricted cards in the format; in fact, some of them are more powerful than cards that are restricted! For example, [Dark Ritual](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual) is stronger than [Lotus Petal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotus+Petal), and [Mishra's Workshop](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop) is stronger than [Grim Monolith](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grim+Monolith).


We are happy despite that apparent inconsistency because each of the four cards I listed creates Vintage deck archetypes. [Dark Ritual](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual) fuels decks built around the Storm mechanic. [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) decks usually build around other unrestricted blue cards; [Mana Drain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain) currently fills that role, but [Gush](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush), [Gifts Ungiven](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven), and [Fact or Fiction](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction) all spent time in that slot before their restrictions. [Bazaar of Baghdad](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bazaar+of+Baghdad) decks abuse *Ravnica*'s dredge mechanic to win the game out of the graveyard in the first three turns. [Mishra's Workshop](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop) decks cast artifacts quickly to lock their opponents out of the game. We acknowledge that these cards are overpowered. However, we value the existence of different decks in a Constructed format, and each of those cards fuels an entire archetype.


In early 2008, members of **Magic** R&D were not happy with the direction that tournament Vintage was going. There were two problems that needed to be solved. The first was that [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) decks were much, much stronger than decks built around [Mishra's Workshop](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop), [Bazaar of Baghdad](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bazaar+of+Baghdad), and [Dark Ritual](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual). The second issue was that [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) and [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) had a homogenizing effect on Vintage blue decks. Once you put four [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will), four [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm), four [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder), a bunch of restricted cards, and some mana sources in your deck, there simply isn't much room to put in anything else. This meant that the differences between different [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) decks were usually very small, and that hurt the format's variety.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld32_cross3.jpg)The developers believed that restricting [Flash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash), [Gush](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush), and [Merchant Scroll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll) would mitigate the first problem because they were the key pieces to the most powerful [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) decks. They considered restricting only [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) to solve the second problem, but [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) was strong enough that many players who did not play [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) before would just replace their [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm)s with [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder)s and the situation would be similar. Therefore, they chose to restrict both cards instead despite how odd it felt to restrict a card as innocuous as [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder).


In the end, even though restricting [Brainstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) and [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) looked strange, it accomplished our goals for Vintage because it forced blue players to make meaningful decisions about what cards they would play with their [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will)s. Many players have chosen [Mana Drain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain) and [Thirst for Knowledge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thirst+for+Knowledge). Others have experimented with [Intuition](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Intuition+) and [Accumulated Knowledge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Accumulated+Knowledge). Some players are willing to play four [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will)s with as few as seventeen blue cards in their deck and accept the inconsistency that this invites. Any of these decisions is meaningful, and the format is much more diverse even within the blue decks.


### Unexpected




|  |  |
| --- | --- |
| 
Thirst for Knowledge
 | 
Accumulated Knowledge
 |

We never expected to make a [Morphling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) variant that had haste when [Thornling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) first arrived from **Magic**'s designers, and no one expected that [Ponder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) would be restricted while *Lorwyn* was being developed. Despite that, we think that **Magic** is a better game because we were willing to do those things even though they looked strange. We don't make decisions that affect **Magic** lightly, we never lose sight of how cool it is that you like our game as much as we do, and we're glad you keep playing even if you occasionally disagree with us.


### Last Week's Poll




| **What is your favorite paper **Magic** Constructed format?** |
| --- |
| Standard | 3218 | 35.1% |
| Legacy | 1335 | 14.5% |
| I don't worry about formats. | 1321 | 14.4% |
| Extended | 1245 | 13.6% |
| EDH/Commander | 872 | 9.5% |
| Vintage | 787 | 8.6% |
| Other | 400 | 4.4% |
| **Total** | **9178** | **100.0%** |








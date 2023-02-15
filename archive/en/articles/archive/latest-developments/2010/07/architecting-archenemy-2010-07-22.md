
---
[Link to Wayback Machine](https://web.archive.org/web/20210429025705/https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Welcome to the end of Multiplayer Week. I do not often play multiplayer, and amusingly, I wrote a multiplayer development column a year ago for Planechase Week. If that's what you're looking for today, you might want to check that out. Rather than do that again, I'll be talking about Archenemy today, as I never quite got the chance to do that the way I wanted to before Magic"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "190511"
[_metadata_:path_date]:- "2010-07-22"
[_metadata_:publish_date]:- "2010-07-23"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Architecting Archenemy"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 02:57:05"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429025705id_/https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/architecting-archenemy-2010-07-22"
---


Architecting Archenemy
======================



 Posted in **Latest Developments**
 on July 23, 2010 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






Welcome to the end of Multiplayer Week. I do not often play multiplayer, and amusingly, I wrote a multiplayer development [column](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/54) a year ago for [*Planechase*](http://archive.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/planechase/productinfo) Week. If that's what you're looking for today, you might want to check that out. Rather than do that again, I'll be talking about [*Archenemy*](http://archive.wizards.com/Magic/TCG/ProductArticle.aspx?x=mtg/tcg/archenemy/productinfo) today, as I never quite got the chance to do that the way I wanted to before ***Magic** 2011* came out.

As is tradition, let's meet the team ...

The Team
![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_tomlapille.jpg)**Tom LaPille:** That's me! *Archenemy* was the first paper product I led; my previous leads were **Magic Online** sets—*Masters Edition III* and the upcoming *Masters Edition IV*, which you'll see later this year. Also, as Aaron [mentioned](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/97) earlier on this site, I'm currently leading a little project with the code name "M12." I'm not the biggest fan of Free-For-All multiplayer because I don't enjoy politics, but I do love the team interaction that Two-Headed Giant brings. That made this the perfect mulitplayer product for me to lead, and I had a blast doing it.

![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_scottlarabee.jpg)**Scott Larabee:** Scott manages the **Magic** tournament system from the ground up. Among other things, that means being at every Pro Tour, at which it's never difficult to find him playing EDH after hours with judges. Scott is building quite a resume of multiplayer product teams, as he also worked on the *Planechase* development team. His work on both products was awesome, and not that I'd know anything about this sort of thing, but I'd be surprised if he didn't end up on another multiplayer product team in the near future.

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_LeeSharpe.jpg)**Lee Sharpe:** Lee once worked on programming **Magic Online**, and has since moved on to a data analysis role. You can also often find him at conventions running the **Magic Online** live series tournaments. Lee demonstrated his passion for multiplayer when he disappeared into a cave one weekend and singlehandedly coded the Commander format for **Magic Online**. Lee also has been part of the team that does **Magic** rules and templating for several years, and that experience helped us navigate the rules issues that we ran into.

![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_AndySmith.jpg)**Andy Smith:** Andy is the scheduling guru who makes sure that everything at Wizards happens on time. He's somewhat soft-spoken and his role in the company is not one that most people think about regularly, but he's essential to getting you your **Magic** cards on time. He also loves to play **Magic** of any kind, multiplayer or not, and we learned a bunch from the several times he took early versions of *Archenemy* to his play groups inside Wizards.

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_MikeTurian.jpg)**Mike Turian:** Mike has led several sets: *Future Sight*, *Morningtide*, *Worldwake*, and now *Scars of Mirrodin*. He also led *Planechase*, last year's multiplayer product. He's also in the Pro Tour hall of fame, and is one of the greatest Limited players to have ever touched a **Magic** card. Mike's expertise was invaluable, as he is both very good at **Magic** and experienced at doing all the things that I was about to do on my first paper product lead.

The Rules
We don't normally get to craft rules when we make a **Magic** set. However, that is something that comes with the territory when you're dealing with entirely new card types and game structures. There were some questions that needed answers.

One category of questions had to do with the multiplayer mechanics that were independent of the schemes. We knew that we wanted turns to alternate between the archenemy and a team that took Two-Headed-Giant-style simultaneous turns. The design team handed off a starting life total system for the archenemy that scaled with the number of players, but it was a little bit more complicated than I wanted. We eventually chose to fix the archenemy's life total at 40 to simplify things. This also let us send the message that if you're having trouble beating the archenemy, you should find more friends.

![](https://media.wizards.com/images/magic/daily/ld/ld100_rules.jpg)  
The other category of questions had to do with the schemes. One question was when the archenemy would scheme. *Archenemy* lead designer Ken Nagle handed off the product with schemes happening at the beginning of the archenemy's upkeep, which didn't quite work the way we wanted. First, this often led to having to make decisions before you knew what card you would draw for the turn, which was tricky. Sometimes that decision even involved deciding how much mana to pay, which was an especially annoying thing to do before drawing a card. The other problem is that players are used to untapping, drawing a card, *then* doing interesting things. Getting them to insert an extra step in between those two actions was tough; what often happened was people would scheme after their draw because they just forgot to do it beforehand. We got to solve both of those problems by having the scheme happen at the beginning of the archenemy's main phase.

The Words
Another unique problem to this product was that we had oversized cards of a new type, and we needed to name them. Matt Tabak was the editor and rules manager for this product, so this task would be his responsibility. We called them "boss cards" for quite a while, but that's not exactly something we can print.

The first clue as to what we should do for these came when Creative lead Brady Dommermuth concepted the first five boss cards with names like "Say Hello to My Little Friend," "Your Fate is Thrice Sealed," and "Your Puny Minds Cannot Comprehend." These set the Creative tone for the product, and inspired Matt to look for a card type name that had the same flavor. The tentative name he settled on was "scheme," and it basically stuck from the beginning. There was some vacillation in the beginning between "ongoing" and "enduring" to describe the schemes that don't go away forever. I don't recall why he chose "ongoing"; I can guess in hindsight that it was because it doesn't imply the length of the duration through which it lasts, but I'm not sure.

![](https://media.wizards.com/images/magic/daily/ld/ld100_2Schemes.jpg)  
That wasn't the last of our problems, though. We also needed rules words to describe the act of playing a scheme card and what happens when an ongoing scheme is done. Matt continued his quest for flavorful words, and found "setting a scheme into motion." You can see from the printed scheme cards that this one stuck. He also found "thwart" for the game action of ending a scheme. We were all excited about the Scooby-Doo-esque vibe that "thwart" gave us, so we put it on cards and did some playtesting.

It was then that we discovered two problems. First, when an ongoing scheme is good for the archenemy, it feels weird to read "thwart this scheme" on it. One does not wish to thwart one's own schemes, but that's exactly what the card would command you to do. Our next try was the passive voice "This scheme is thwarted." We found the passive voice to be a little distasteful, and there were also several schemes that then read "thwart this scheme and [do something terrible to the players]." That's silly, because the scheme wasn't actually thwarted at all.

![](https://media.wizards.com/images/magic/daily/ld/ld100_abadon.jpg)  
We solved these two problems separately. First, we switched from "thwart" to "abandon" to avoid passive voice. Second, I cut all the schemes on which thwarting or abandonment was not unambiguously good for the players. That gave us cards that read both cool and sensibly.

The Schemes
![](https://media.wizards.com/images/magic/daily/ld/ld100_scheme01a.jpg)![](https://media.wizards.com/images/magic/daily/ld/ld100_scheme01b.jpg)This is one of the most powerful schemes we made. Extra turns are really good no matter what is going on, but are especially good when you have a whole team of hungry heroes ready to take advantage of the slightest "shields-down" moment. The design version of this card however, did not have the second sentence on it, which made it even more sick. In fact, it was so sick that it was better than every other scheme, because it gave you another scheme next turn. It's okay to have good cards, but it's not interesting when one card is better than every other card. Rather than make this strictly better than every other scheme, we took away the scheme on your extra turn.

  
![](https://media.wizards.com/images/magic/daily/ld/ld100_scheme02a.jpg)![](https://media.wizards.com/images/magic/daily/ld/ld100_scheme02b.jpg)Both Aaron Forsythe and Ken Nagle love putting their opponents in untenable positions and watching them squirm. Midway through *Archenemy* development, Aaron pitched the idea for "hot-seat" schemes that would force one player to make a decision for the whole team about what sort of bad thing happens. I pitched this to Ken, and Ken liked it so much that he asked to put one such scheme in each deck. In addition to those four schemes, we liked the hot-seat technology so much that we put it on other schemes. For example, Nature Demands an Offering once asked the archenemy's opponents to collectively make a decision about what permanents to lose. That was hard to do under the **Magic** rules, so instead we put the decision to a player of the archenemy's choice.

I'm glad we chose to run with Aaron's suggestion. One of my favorite things to do in *Archenemy* is point one of the hot-seat schemes at people who are not team players. Mike Turian and Ken Nagle, for example, can both be counted on to choose "others" whether or not it's better for the team. Exploiting things like that is one of the best ways for an archenemy to get an edge!

  
![](https://media.wizards.com/images/magic/daily/ld/ld100_scheme03a.jpg)![](https://media.wizards.com/images/magic/daily/ld/ld100_scheme03b.jpg)One of the cool things about developing products designed by Ken Nagle is that he often does a strange sort of development before he gives it to you. Ken understood that one of the ways that *Archenemy* goes wrong is for one of the players to have a spell-based combination deck that you aren't prepared to interact with. To help protect against that, he made this card, which seriously punishes an opponent for not playing along and having creatures. It's still good against creatures, of course, but it's far worse for someone who has no creatures to feed to this scheme.

Correction
I stated two weeks ago that [Stormtide Leviathan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormtide+Leviathan) was designed by Greg Marques. This was incorrect; it was actually designed by **Magic Online** architect Ryan Dhuse. My apologies to both of them for the mistake.

Last Week's Poll


|  |
| --- |
|  **What is your favorite ***Magic** 2011* mythic rare?**  |
| [Grave Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grave+Titan) | 1778 | 21.40% |
| [Primeval Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primeval+Titan) | 1209 | 14.50% |
| [Baneslayer Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baneslayer+Angel) | 1049 | 12.60% |
| [Time Reversal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Reversal) | 655 | 7.90% |
| [Gaea's Revenge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Revenge) | 598 | 7.20% |
| [Demon of Death's Gate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demon+of+Death%27s+Gate) | 590 | 7.10% |
| I'm not particularly fond of any of them | 578 | 6.90% |
| [Sun Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sun+Titan) | 523 | 6.30% |
| [Platinum Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Platinum+Angel) | 243 | 2.90% |
| [Jace Beleren](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren) | 236 | 2.80% |
| [Garruk Wildspeaker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker) | 219 | 2.60% |
| [Inferno Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inferno+Titan) | 194 | 2.30% |
| [Chandra Nalaar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar) | 128 | 1.50% |
| [Ajani Goldmane](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Goldmane) | 123 | 1.50% |
| [Frost Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frost+Titan) | 104 | 1.20% |
| [Liliana Vess](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana+Vess) | 96 | 1.20% |
| **Total** | **8323** | **100.0%** |

This Week's Poll


|  |
| --- |
| **Which pair of planeswalker cards is your favorite?**[Jace's Erasure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%27s+Erasure) and [Jace's Ingenuity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%27s+Ingenuity).[Liliana's Caress](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana%27s+Caress) and [Liliana's Specter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana%27s+Specter).[Chandra's Outrage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra%27s+Outrage) and [Chandra's Spitfire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra%27s+Spitfire).[Garruk's Companion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%27s+Companion) and [Garruk's Packleader](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%27s+Packleader).[Ajani's Mantra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani%27s+Mantra) and [Ajani's Pridemate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani%27s+Pridemate).I do not like the Planeswalker signature spells.I'm not sure. |

[![](https://web.archive.org/web/20121120220404id_/http://www.wizards.com/mtg/images/daily/features/MTGOReleaseM11ArticleBanner.jpg)](http://archive.wizards.com/magic/Digital/MagicOnline.aspx)  







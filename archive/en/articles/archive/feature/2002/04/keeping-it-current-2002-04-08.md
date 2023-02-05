
---
[Link to Wayback Machine](https://web.archive.org/web/20211018182727/https://magic.wizards.com/en/articles/archive/feature/keeping-it-current-2002-04-08)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/keeping-it-current-2002-04-08"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211018182727id_/https://magic.wizards.com/en/articles/archive/feature/keeping-it-current-2002-04-08"
[_metadata_:wayback_capture_timestamp]:- "2021-10-18 18:27:27+00:00"
[_metadata_:publish_date]:- "2002-04-08"
[_metadata_:description]:- "When I told my friends and coworkers that I’d volunteered to write an article about why Magic Online won’t let players play with cards from sets before Invasion, their first reaction was to send for the exorcist. Thanks, guys!Let me get the official answer out of the way first. Why can’t you play with older card sets in Magic Online? Because the powers that be say so. You can"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Keeping It Current
==================



 Posted in **Feature**
 on April 8, 2002 






![](https://media.magic.wizards.com/styles/auth_small/public/generic-avatar-150_310.png)
By Del Laugel, technical editor











When I told my friends and coworkers that I’d volunteered to write an article about why **Magic** Online won’t let players play with cards from sets before *Invasion*, their first reaction was to send for the exorcist. Thanks, guys!

Let me get the official answer out of the way first. Why can’t you play with older card sets in **Magic** Online? Because the powers that be say so. You can read the [official press release](http://archive.wizards.com/news/pressrelease.asp?20020114a) for the details, but here’s the gist of that statement: You buy **Magic** Online cards the same way you buy physical **Magic** cards. **Magic** Online cards can be redeemed for physical **Magic** cards. Wizards of the Coast will redeem complete sets of cards from *Invasion* forward. Therefore, Wizards will only sell cards from *Invasion* on.



|  |
| --- |
| *These cards can be looked at in the binder, but won't be playable.* |

That’s not much fun to talk about, and there’s been a great deal of public debate on the subject already. You’ve probably already hear most of the pros and cons. So instead of trying to explain the redemption policy, I’d like to go over some of the less obvious reasons why including older card sets in **Magic** Online would be problematic. To do that, I’m going to have to delve into some things that, as a **Magic** editor, I don’t really want players thinking about. My apologies to the **Magic** community for pointing out the skeletons in the closet (if you’re in China, you can imagine me pointing out living, fully-clothed people), but here are some facts about the **Magic** game that you probably didn’t need to know:

**Fact 1.** The [**Magic** Comprehensive Rules](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=dci/oracle/MagicCompRules_022002.doc) is seventy-six pages long. It grows by about two pages a year as new mechanics are introduced. Rules 504.1–504.4 cover only two cards in the entire history of the game: [Illusionary Mask](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusionary+Mask) and [Camouflage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Camouflage).

For comparison, the word count of the Comp Rules is nine times that of the original Constitution of the United States, and phasing and “snow-covered” take twice as much text to explain as the powers and duties of the president.

**Fact 2.** Some older cards do really, really weird things. For example, [Channel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Channel)’s Oracle wording is “Until end of turn, any time you could play a mana ability you may pay 1 life. If you do, add one colorless mana to your mana pool.” I think it’s really interesting that [Channel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Channel) seems to splice a mana ability onto *me*. It makes me want to wear a Post-It for the rest of the turn that says “Pay 1 life: Add 1 to your mana pool.”

**Fact 3.** Some older cards look perfectly innocent, but they do strange things when they get together. As long as those cards are quietly ignored, the world spins merrily on its axis. Take too close a look and anything could happen.

Last year, Wizards put out a box set called Deckmasters, which included cards from the *Ice Age* and *Alliances* sets, and the templating team assembled to go over the small pool of cards selected for the decks. After we tossed out [Dance of the Dead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dance+of+the+Dead) rather than include a magnifying glass in the box along with the life counter (the rules text would have been roughly the same size as the legal text), we hit [Phantasmal Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Fiend). Click the card name and take a good look at this card.



|  |
| --- |
| *Some older cards interact in hard to predict -- and harder to code -- ways.* |

[Phantasmal Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Fiend) looks like it involves some math, but surely there are no rules problems with that, right? Wrong. Apparently, that last sentence occasionally makes the universe implode. I’d love share with you the convoluted scenario that the rules team had to sort out (it involves [Phantasmal Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Fiend), [Purelace](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Purelace), and a [Jihad](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jihad) or two), but everyone I asked to help me recreate it ran away screaming. The rules team clarified some of the dependency rules, and the rest of us decided to leave [Phantasmal Fiend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Fiend) alone. If all of you promise never to put those cards in the same deck, everything should work out just fine. (Now you know why the *Torment* card [Aquamoeba](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aquamoeba) doesn’t have the “effects that alter... and vice versa” line.)

**Fact 4.** The [Oracle card reference](http://archive.wizards.com/dci/main.asp?x=oracle) does a good job of bringing older cards in line with the game’s current rules and card wordings, but it isn’t perfect. Paul Barclay, the **Magic** rules manager, does an excellent job of patching up all the older card wordings. If you read his recent [Oracle update](/en/articles/archive/latest-oracle-update-2002-03-14), you know how subtle some of the changes are. What you may not know is that Paul always has more cards lurking on his “to fix” list. **Magic** Online can’t handle that kind of uncertainty; the program needs to be able to parse card text with infallible logic. There can be no "usually" or "close enough" interactions.

**Fact 5.** The **Magic** game has been around for eight-and-a-half years, and it has many, many cards. Exactly how many **Magic** cards are there? That’s a surprisingly difficult question to answer. Assume that we’re only talking about English cards, and premium (foil) cards are the same as regular cards.

If you count cards that can be distinguished from each other, there are probably 9,000-10,000 cards. However, that number includes 109 basic [Forest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest)s.

What about counting unique card names? That gets you an answer of about 5,640, but the group includes things like *Vanguard* and *Portal Three Kingdoms* cards. (Fun fact: The *Portal* card [Monstrous Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Monstrous+Growth) was renamed [Wielding the Green Dragon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wielding+the+Green+Dragon) for *Portal Three Kingdoms*. Wouldn’t it have been great if that version had made it into *Seventh Edition*?)

Let’s try counting Oracle records -- that tells us that about 5,020 cards with different names were printed in sets that are legal in tournament play. That list includes things like [Mind Twist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Twist), [Nalathni Dragon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nalathni+Dragon), and ante cards, but it doesn’t include *Unglued*. (Attack with [Hurloon Wrangler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hurloon+Wrangler) in **Magic** Online, and you could discover that your opponent is playing in the nude. We don't need to encourage such behavior.)

**Fact 6. Magic** Online lets you play with a lot of **Magic** cards already. Now here’s where the math gets interesting. If you add up all the cards in *Invasion*, *Planeshift*, *Apocalypse*, *Odyssey*, *Torment*, and *Seventh Edition*, you should get 1,479 cards. Subtract from that 55 of the 60 basic lands, one of the [Elvish Champion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Champion)s, one of the [Razorfoot Griffin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Razorfoot+Griffin)s, and one of the [Gravedigger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravedigger)s, and you’ll find that there are 1,422 unique cards that you should be able to play with in **Magic** Online right now.

So of the 5,020 cards that have ever been legal for tournament play, you’ll be able to play with 1,422 of them. That’s fully 28% of **Magic** cards. Frankly, I’m amazed that the percentage is so high.



|  |
| --- |
| *Mirari is finally coded after six months on the shelf.* |

**Fact 7. Magic** Online has just barely mastered all the cards it’s supposed to. Only a week or so ago, four cards still weren’t “working” in **Magic** Online: [Psychic Battle](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychic+Battle), [Mirari](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirari), [Delaying Shield](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Delaying+Shield), and [Alter Reality](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alter+Reality). (Granted, “working” is not the same as “working correctly,” but I understand that the programmers will be kept chained to their computers until launch.) They've all be implemented since, but [Mirari](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirari) was in print in the "real world" for close to six months before it was available online.

**Fact 8.** As *Judgment* will attest, R&D hasn’t stopped making weird cards just because **Magic** is going digital. (Would you believe that one of the proposed wordings of the *Torment* card [Radiate](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Radiate) involved changing all instances of “target” to “all?”)

**Fact 9.** Wizards puts out a new card set about every four months. Read Fact 8 again and think of Leaping Lizard, hard at work on 143 *Judgment* cards, 350 *Onslaught* cards, . . .

Which would you rather be able to play with in **Magic** Online: *Prophecy* or *Judgment*? *Homelands* or *Onslaught*? Personally, I want to see Wizards and Leaping Lizard prove to the public that they have all the cards and card interactions from *Invasion* forward working perfectly -- and that they can keep up with the new card sets -- before I even think about asking them to include older cards.

I expect **Magic** Online to be a dazzling part of **Magic**'s future as opposed to a snapshot of its past.

*Questions? Comments? Email editor@wizards.com.*






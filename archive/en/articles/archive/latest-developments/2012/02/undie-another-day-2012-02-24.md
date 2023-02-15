
---
[Link to Wayback Machine](https://web.archive.org/web/20210429034909/https://magic.wizards.com/en/articles/archive/latest-developments/undie-another-day-2012-02-24)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "Welcome to Undying Week! Of course, I always feel awkward saying `Welcome` at the end of a theme week. As though you haven't been here the entire time. Maybe we can interpret it as `Welcome to Latest Developments: Undying Week Edition.` Sort of like `Law and Order: SVU.` I want a cool acronym. With a correspondingly-cool logo. Doubly awkward now when it's some ambiguous turn"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "644771"
[_metadata_:publish_date]:- "2012-02-24"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "(Un)Die Another Day"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 03:49:09"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429034909id_/https://magic.wizards.com/en/articles/archive/latest-developments/undie-another-day-2012-02-24"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/undie-another-day-2012-02-24"
---


(Un)Die Another Day
===================



 Posted in **Latest Developments**
 on February 24, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 







Welcome to Undying Week!


Of course, I always feel awkward saying "Welcome" at the end of a theme week. As though you haven't been here the entire time. Maybe we can interpret it as "Welcome to Latest Developments: Undying Week Edition."


Sort of like "Law and Order: SVU."


I want a cool acronym. With a correspondingly-cool logo.


Doubly awkward now when it's some ambiguous turn of phrase like "Undying Week." Is it a week *about* the undying mechanic? Is it a week that never dies? It is a week that *un*-dies (heh heh, "undies")—you know, pulls a kind of ctrl+z on Saturday night and loops back over from the beginning one more time?


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld183_undying.jpg)The last option matches the mechanic most, I think. It's a little weird to write "Whenever this creature dies" on a mechanic called "undying," but it's totally sensible if you read it as literally undoing the act of death itself.


Food for thought. Just saying.


Mmm, thought-food! Chewy! Tastes like bacon!


#Imreallyweird.


### This Heading Heralds The Content-Rich Portion of Today's Development Article


I had no idea there was a J. Cole hip-hop pseudo-cover of "Straight Up" by Paula Abdul, or that such a pseudo-cover would be playing in a Renton coffee shop.


### No, Seriously!


Ahem.


Undying was one of the hardest-to-develop mechanics I've ever encountered. That might seem odd, given that it's a relatively straightforward riff on a mechanic—persist—we've already done before. It turns out, though, that persist itself had some issues, and many of those problems were exacerbated further by subtle differences that exist between the two mechanics.


Normally, we react to a card or mechanic on two distinct levels. There's the reaction we have when we first look at a card, our initial impression that forms based upon nothing but the act of opening a pack and reading a line of text. I like to call this our *felt* response. This is contrasted with our *learned* response, which is the reaction we internalize based upon how a card plays over the course of a number of games. The felt response is important because it affects peoples' initial opinions of a set—it's what entices them to play in the first place. The learned response is important because it determines how fun a set is to play over the long term. Without a powerful felt response, no one wants to play your set. Without a powerful learned response, the people who buy into playing your set have a bad experience. Good sets (and good mechanics) have to succeed on both levels.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld183_mob.jpg)When it comes to undying, it has a tendency to produce a comparatively weak felt response coupled with a disproportionately powerful learned response.


This is dangerous.


### What a Feeling


One of the reasons **Magic** has had so much success lately is that we've actively tried to align the cards and mechanics that *seem* powerful with the cards and mechanics that actually *are* powerful. This is why we've made creatures central to tournament play, for instance. You shouldn't feel stupid for thinking an awesome giant badass Dragon or Angel or Demon or Hydra is awesome and giant and badass.



![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld183_with.jpg)![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ftl/Sun_ArtTransformButton_Static.png)![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ftl/Moon_ArtTransformButton_Active.png)[Elbrus, the Binding Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elbrus%2C+the+Binding+Blade) and [Withengar Unbound](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Withengar+Unbound) | Art by [Eric Deschamps](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Eric+Deschamps%22%5D)



By contrast, when something that seems like it should be weak reveals itself to actually be very strong, it usually feels bad. It feels like a joke is being played on you. It makes you ask, "Why would I want to play this game if the fun things suck?"


Of course, this is a matter of degrees—it's sweet, after all, to discover power that isn't obvious at first glance. But the process has to involve just that: *discovery*. When you engineer a deck of superficially weak cards together to do something powerful, you're creating something. You're discovering interactions that weren't immediately apparent. When, by contrast, you're just announcing spells that are flagrantly imbalanced, it becomes very boring very quickly.


As I talked about [in this article](/en/articles/archive/latest-developments/bringing-flashback-back-2011-12-16), ßcard advantage is extremely, extremely good. The main advantage to undying is that it creates card advantage, which usually has a more pronounced impact on the game than it seems like it would at first glance. This means that, for most people, undying is naturally going to hit a little less hard in terms of appeal than it would after they played with the cards a few times. This was certainly true for us in R&D—our first swings at undying card designs were *way* too good for Limited, even though we *knew* coming in the mechanic would play out better than it looked. Missing on felt appeal is a huge potential problem for a mechanic that's central to the identity of the set.


### Learn to Play


"Well, okay," you might say. "Just develop undying so it's appealing enough, accept that undying cards are going to be some of the most powerful cards in the set, and deal with that."


We certainly tried that approach at first. Unfortunately, it turns out that as you develop your learned response, undying becomes even more powerful than it seems at first. Even our initial bad, unappealing undying designs were in practice very potent once we adapted our play patterns around them. This was one of the issues with persist in *Shadowmoor* block, in my opinion: it was just so easy to craft entire strategies around the ability to trade with value using persist creatures. This problem was even more magnified for us during the development of *Dark Ascension. Shadowmoor* block at least had wither and –1/–1 counters to kill persist creatures such that they didn't come back for round two. We didn't enjoy the same luxury.




|  |  |
| --- | --- |
| 
Vorapede
 | 
Puppeteer Clique
 |

All of this meant that even the very weak undying cards were overpowering game play. In theory, it's possible to just accept that constraint and move on. The problem was, we had a hunch that *Innistrad* was really awesome—that, we hoped, it would actually shape up to be one of the best Limited environments of all time. The last thing we wanted to do, then, was take everything awesome about *Innistrad* and say, "Nope, now Limited is about this other thing, and it has nothing to do with the fun stuff you were doing before."


### Fair Trade


So, we had a conundrum on our hands. Undying had to be powerful enough to *feel* exciting, but not so overpowering that it dominated the Limited environment. Even the weakest cards we could realistically see ourselves printing turned out to play far more powerfully than we initially had realized. What was there to do?


The breakthrough came when we realized most of the power of undying involved the frequency it was possible to trade profitably in combat. Some of undying's value was, of course, that it was largely invulnerable to removal, and that it enabled sacrifice effects like [Demonmail Hauberk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonmail+Hauberk) and [Skirsdag Cultist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skirsdag+Cultist). But a huge percentage of the cards' power—and a huge percentage of the frustrating game play—involved how difficult it was for your opponent to break through if you were willing to just sit back all day and play defense.


What if you weren't able to play as much defense?


In a single meeting we came up with four new common undying cards: [Nearheath Stalker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nearheath+Stalker), [Sightless Ghoul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sightless+Ghoul), [Stormbound Geist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbound+Geist), and [Young Wolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Young+Wolf).




|  |  |
| --- | --- |
| 
Young Wolf
 | 
Stormbound Geist
 |

Each of these attacked the problem in different ways. With [Young Wolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Young+Wolf), usually a one-mana 1/1 creature is substantially worse than any card you'd normally play in Limited, so you handicap yourself significantly in the turns *before* you're able to generate a two-for-one. With [Stormbound Geist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbound+Geist) and [Sightless Ghoul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sightless+Ghoul), we created blocking restrictions that outright prohibited them from sitting back, sipping lemonade, and begging for a fight. And with [Nearheath Stalker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nearheath+Stalker), we made him fragile enough for the cost that the value of his two-for-one would be mitigated somewhat by the quality of the cards with which he profitably traded.




|  |  |
| --- | --- |
| 
Sightless Ghoul
 | 
Nearheath Stalker
 |

Of course, this fix only addresses Limited. While the value of a two-for-one in Constructed diminishes substantially, we were still reasonably worried about the effect undying had on aggressive decks' ability to push through damage. To solve this problem, we changed [Strangleroot Geist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strangleroot+Geist) from a 2/2 trampler to a 2/1 with haste. This would incentivize attacking (since, if you don't take advantage of the ability to attack on the first turn, you're giving up value relative to the card's cost) while also making the card less of a brick wall back on D. We also forced [Geralf's Messenger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geralf%27s+Messenger) to enter the battlefield tapped—which was fitting, after all, for a hulking zombie. Given how many times we sacrificed the Messenger to [Birthing Pod](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birthing+Pod) to fetch up a [Phyrexian Metamorph](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Metamorph) on the fourth turn (copying the Messenger, of course), this change made it a *lot* easier for aggro decks to smash through on the ground.


### Biggie Smalls


As you'll notice, of course, I've hardly enumerated every single undying creature in *Dark Ascension*. And every single undying creature in *Dark Ascension* doesn't enter the battlefield tapped, or possess some kind of blocking restriction, or otherwise feature some design constraint that causes it to dodge combat. Part of the reason for this is that all the game-play issues I've talked about are really a matter of degrees. While we don't want an entire **Magic** environment to be about raw-resource-advantageous two-for-ones, it's certainly good for **Magic** for that to happen from time to time. Another part of the reason for this is that we found different fixes for the play patterns of undying creatures—like [Pyreheart Wolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyreheart+Wolf), for example, who plays more like a sorcery with rebound than anything else. But my favorite solution—one we used several times in the set and one that solves a fair amount of the "felt response" problem—is simply to make the undying creatures *big*.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld183_wolf.jpg)[Pyreheart Wolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyreheart+Wolf) | Art by [Lars Grant-West](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Lars+Grant-West%22%5D)


Take a card like [Alpha Tyrranax](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alpha+Tyrranax). As a 6/5 creature, he's already a sort of built-in two-for-one if your opponents try to trade with him. Sure, they might have [Terror](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terror)s (or thereabouts), but if they want to trade in combat they're almost always going to have to throw more than one creature at him anyway. What usually happens is that the game-play pattern shifts to accommodate the [Tyrranax](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tyrranax)'s presence on the table rather than attempting to remove it outright. Because of that, the undying keyword on larger creatures (like [Geralf's Mindcrusher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geralf%27s+Mindcrusher), [Relentless Skaabs](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Relentless+Skaabs), or [Vorapede](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vorapede)) functions more to evade removal than it does to generate combat-based two-for-ones, since those kinds of creatures trade in combat less frequently due to their inherent size.


### Professing an Undying Love


In the end, while undying was a challenging mechanic to develop, I feel like the team pulled it off. The goal was to create appealing creatures that also added to the texture of the Limited environment, and I think the mechanic accomplished that—while also seeding a couple spicy Constructed players in the process.


Join me next week, when you (oh, you) have got me feeling emotions.









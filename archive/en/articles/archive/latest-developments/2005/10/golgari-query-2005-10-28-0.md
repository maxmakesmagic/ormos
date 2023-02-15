
---
[Link to Wayback Machine](https://web.archive.org/web/20210429092012/https://magic.wizards.com/en/articles/archive/latest-developments/golgari-query-2005-10-28-0)

[_metadata_:author]:- "Aaron Forsythe"
[_metadata_:description]:- "For each “guild” theme week, I'm discussing how development handled that particular guild. My article on the Selesnya Conclave can be found here. As most of our decisions regarding this guild revolved around the dredge mechanic and how it eventually would end up working, this article will focus primarily on the development of that keyword and its respective cards."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "613101"
[_metadata_:publish_date]:- "2005-10-28"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Golgari Query"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 09:20:12"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429092012id_/https://magic.wizards.com/en/articles/archive/latest-developments/golgari-query-2005-10-28-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/golgari-query-2005-10-28-0"
---


Golgari Query
=============



 Posted in **Latest Developments**
 on October 28, 2005 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_aaronforsythe.jpg)
By Aaron Forsythe












For each “guild” theme week, I'm discussing how development handled that particular guild. My article on the Selesnya Conclave can be found [here](/en/articles/archive/latest-developments/completing-conclave-2005-10-07-0). As most of our decisions regarding this guild revolved around the dredge mechanic and how it eventually would end up working, this article will focus primarily on the development of that keyword and its respective cards.


### Dredge: Not Just a Bad *Invasion* Card


There's a movie trailer being run on television currently that has a tagline something like, “Some people are better left dead.” I didn't think much of it when I heard it, but Mark Gottlieb recently pointed out that that statement kind of implies that it's okay to resurrect most people. Just be careful which ones you choose. How absurd is that?


Well, the Golgari Guild must be big fans of that movie, because they buy into that whole “let's resurrect everyone” ideology. Nothing stays dead, and the living are often sacrificed for some grisly effect, only to be brought back later. If any guild views the graveyard as a resource, it is the black-green one.


The dredge mechanic exemplifies the belief that life and death are not so different after all. The mechanic was the brainchild of one Mark Rosewater, *Ravnica* lead designer and head honcho of all Magical designs. That mechanic was the last of the four to be nailed down by the design team; several other black-green mechanics were auditioned and dismissed.


The version design turned over—then called “reclaim”—was significantly different from the printed version of dredge in one regard:



> 
> Reclaim (If you would draw a card, you may instead return this card from your graveyard to your hand.)
> 
> 
> 


Yes, that version is much shorter and probably a lot easier to understand at a glance than the “real” version. But there is no cost to performing this action, which was a problem.


The draw step is a very important part of **Magic**, for two reasons. One, it adds variance to the game. The outcome of any given game remains in doubt for a long period of time; one player could rattle off several great draws in a row while his opponent drew land after land. And subsequent games would be different because of that variance. Two, the draw step is one of the most exciting events in the game. At the beginning of each of your turns, you get a Christmas present. What will it be? A shiny new [Fireball](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball), or some socks and underwear in the form of your seventh Forest? Reclaim made it too easy to take both of those essential ingredients away.


Rosewater would agree that the mechanic was not implemented correctly in design—the team simply ran out of time to search for solutions. So development was tasked with finding the fix.


### Finding the Fix


Here is a sample “problematic” reclaim card from design:



> 
> UB02\_CON  
> 
> Plague Butcher  
> 
> 3BB  
> 
> Creature – Horror  
> 
> 2/2  
> 
> Fear  
> 
> Whenever CARDNAME deals combat damage to a player, each creature gets -X/-X until end of turn, where X is CARDNAME's power.  
> 
> Reclaim (If you would draw a card, you may instead return this card from your graveyard to your hand.)
> 
> 
> 


If you had this card and your opponent was playing a deck full of little creatures that couldn't block this guy, you basically had the option of killing every one of them any time you felt like it. You'd have a smoking gun in your graveyard, ready to be reloaded and unleashed on your opponent at any time, for absolutely no investment. Before the fix for the mechanic was found, we removed all cards like these—the ones that would leave your opponent feeling helpless. Of course, after the fix was found, we'd bring some back.


 



![Vedalken Entrancer](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vedalken+Entrancer)

The other thing of relevance to reclaim was the heavy milling theme present in the Dimir cards. We knew we wanted milling to be a viable strategy in limited, and possibly constructed, and as worded the design version of reclaim simply trumped milling. Even with an empty library, you could replace the potentially fatal draw with the regrowing of a reclaim card. If you had one reclaim card in your library that could easily find its way back into your graveyard, such as an instant or a creature that can be sacrificed like [Shambling Shell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Shell), you were immune to ever being decked. That was not something we wanted.

Dredge needed a check—some additional cost that would say, “You can't draw this every turn for the rest of the game.” We tossed around using life payments or having to discard a card to use the dredge ability, but those both felt pretty steep and made the mechanic pretty unattractive. Eventually we settled on dumping some number of cards from your library.


This solution was great for two reasons. One, it created a fantastic tension between the Golgari and the Dimir. Dredge speeds up the enemy's attempts to win via decking, but at the same time milling cards give the Golgari player access to more dredge. Two, the mechanic could now feed itself. If you dredge a [Stinkweed Imp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stinkweed+Imp), there is also a chance that another dredge card is somewhere in the five cards you just dumped.


It was that second point that made me believe that the mechanic would be okay to print in this way. My big concern was that some (potentially large) segment of casual players—those that cannot appreciate [Arc-Slogger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arc-Slogger) for the efficient killing machine he is—wince at the thought of milling cards from their decks for some “minor” effect. Even though most games they play end with half of their libraries sitting there unused, they can't stand the idea of “losing” five cards to get back a 1/2 flier. To them, those are spells that they could no longer play, lost forever in the blackness that is the graveyard. The fact that dredge kind of justifies its own cost by fueling itself would hopefully lead some of these players to “get it,” and not dismiss the mechanic as a whole outright.


 



![Golgari Grave-Troll](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Golgari+Grave-Troll)

The next step for us was assigning dredge numbers to each of the cards. We didn't want the numbers to be too low on average, as it wouldn't end up actually being much of a cost to use that way. On the other hand, we didn't want the numbers to be too high either, as the mechanic would feed off of itself much easier that way, and the perception of the mechanic would potentially be pretty bad. So we settled on two or three cards for the average dredge number.

Of course, we picked spots where deviation made sense. [Golgari Grave-Troll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Golgari+Grave-Troll), for instance, makes great use of a full graveyard, so we gave him the highest dredge number in the set. [Stinkweed Imp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stinkweed+Imp) has a very high dredge as well, but his was more for the balancing of Limited play. With a dredge of 5, returning this very annoying little flier from the bin more than once or twice puts a real strain on any deck in the long game. Conversely, [Grave-Shell Scarab](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grave-Shell+Scarab) has the lowest dredge in the set—1. The reason there was that, even if you are dredging the Scarab every turn, its “draw a card” ability lets you see new cards from your library. The integrity of the draw step is maintained.


### Notes on Dredge Cards


Once the cost of dredge was determined to be self-milling, several dredge cards that made use of fuller graveyards were added by development, including [Life from the Loam](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Life+from+the+Loam), [Golgari Thug](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Golgari+Thug), and [Golgari Grave-Troll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Golgari+Grave-Troll). We had long-since cut a gold card in the design file that was similar to the Troll, except you had to remove the creatures from your graveyard when it came into play, and it couldn't kill itself as easily as the Troll.



> 
> UZ21\_CON  
> 
> Frankenstein's Brother  
> 
> 1BG  
> 
> Creature – Horror  
> 
> 2/2  
> 
> As CARDNAME comes into play, remove any number of creature cards in your graveyard from the game. CARDNAME comes into play with a +1/+1 counter for each card removed in this way.  
> 
> Reclaim (If you would draw a card, you may instead return this card from your graveyard to your hand.)
> 
> 
> 


Design should feel vindicated that a [Lhurgoyf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lhurgoyf)-type creature with dredge made its way back into the set after all. Development also added [Svogthos, the Restless Tomb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Svogthos%2C+the+Restless+Tomb), another “lhurgoyf” that plays nice with dredge.


When it came to making instants and sorceries with dredge, the design team understood they couldn't be too backbreaking, as they would tend to be played multiple times in a game. There could be no dredge [Dark Banishing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing), for instance, as many opponents would be hopeless before it. Design had [Darkblast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darkblast) costing ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif), which was conservative, but was generally the right idea. Some spells that had dredge coming out of design included [Farseek](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Farseek) and [Gaze of the Gorgon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaze+of+the+Gorgon). The former let decks cheat on land pretty significantly, as well as all but guarantee access to all five colors by turn four. The latter led to very repetitive games, as something like [Siege Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Wurm) backed up by unlimited Gazes proved to be a little frustrating to play against.


 



![Stinkweed Imp](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Stinkweed+Imp)

We did manage to fit a reusable way to kill larger creatures into the world of dredge with [Stinkweed Imp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stinkweed+Imp) (which was initially just [Bog Imp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bog+Imp) with reclaim) and [Necroplasm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necroplasm). If you've ever had to battle against little Stinky in Limited, you probably can appreciate the power of repeated-use creature destruction. [Necroplasm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necroplasm) was in the file for a long time without dredge, but people didn't like playing with a creature that tended to go away after three turns. Now he is a reusable, albeit slow, answer to tokens and other little critters. Plus, you can always be creative and use him to kill larger creature as well… just use [Shambling Shell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Shell) to make sure [Necroplasm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necroplasm) never ends a turn with exactly three counters. That way he'll bypass killing himself and just keep growing and growing!

Late in development (when theme decks were being built, actually), we realized that we only had one green common with dredge ([Greater Mossdog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Mossdog)), and we wanted to add a card that used dredge in an interesting way. We came up with the nifty little [Golgari Brownscale](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Golgari+Brownscale), the first card that does something when it goes from your graveyard to your hand.


That's the tale of dredge. It was a tough nut to crack, but we managed to preserve the intent of the design team, balance the power level, and make the whole thing more interesting to play. Hats off to my development teammates on this one!


### Multiverse Comments on the Golgari


Keeping with my short-lived tradition, here are development comments from some of the cards in the Golgari Guild (not just dredge cards)


 



![Life From the Loam](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Life+from+the+Loam)

**[Life from the Loam](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Life+from+the+Loam)** (originally called “Piff”) was an uncommon that eventually shifted to rare. One interesting tidbit about the card was that we actually made it worse by lowering its dredge number!


> 
> bs 11/1: added piff.  
> 
> AF 11/9: Powerful.  
> 
> AF 11/19: I'd like to see 1G, 3 lands.  
> 
> BB 1/10: added reminder text  
> 
> DAL 1/10: Should target so you can respond with rapid decay, cremate.  
> 
> Del 1/13: DAL's right -- abilities like this are almost always targeted. Changed, but let me know if you had a reason for this to work the other way.  
> 
> bs 2/21: seems powerful to me. clear engine card... could people post decks with this in the ffl folder?  
> 
> Del 4/21: Dev changed from dredge 4 to dredge 3.
> 
> 
> 


 

 



![Woodwraith Strangler](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Woodwraith+Strangler)

**[Woodwraith Strangler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woodwraith+Strangler)** has gotten a rap as being the worst common gold card in the set. We kept trying to find ways to make black-green better in limited by tweaking him, but eventually we decided to let him be mediocre, and instead lower [Golgari Rotwurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Golgari+Rotwurm)'s cost from 6 to 5.


> 
> bs 10/18: was, "At the end of each turn, if a card was put into an opponent's graveyard, put a +1/+1 counter on CARDNAME."  
> 
> bs 10/26: added this 2BG 2/2.  
> 
> AF 10/29: Good half-and-half candidate.  
> 
> MT 11/4: I think it should remove a creature card. More interesting and more restrictive.  
> 
> DAL 11/5: Can this get "Discard a card: +1/+1 UEOT. RFG 2 cards from GY: +1/+1 UEOT?"  
> 
> bs 12/13: changed from "regen CN to regen target black or green creature." will need adjustment in pointing pass.  
> 
> RB 12/20: Does this need to cost 5? Still mediocre at 3, I think.  
> 
> bs 1/3: back to just regenerating himself.  
> 
> bs 1/21: was 2BG, 2/2. now 3BG, 3/2.  
> 
> bs 1/27: green/black is the worst combination in limited. it isn't even worth looking at drafting. why is that?  
> 
> AF 1/30: I think because the way it wins (slow graveyard recursion) is trumped by both speed and milling. And its cards suck.  
> 
> bs 1/31: back to 2/2, 2BG.
> 
> 
> 


 



![Shambling Shell](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shambling+Shell)

**[Shambling Shell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shambling+Shell)**, at various points in development, was five mana, had a “goes to graveyard trigger” instead of a sacrifice ability, had a one-mana cost on its activation, and hand dredge 5. The final version, happily, is a tight little package that does, indeed work well with “Guldesta” (Savra).


> 
> bs 9/16: upped cost from 3 to 5.  
> 
> RB 10/8: Seems awful weak now that it's 5 mana ... that feels like the wrong answer to the potential recursion problem  
> 
> bs 10/12: reclaim 5 should do the trick. moved back to 3cc.  
> 
> bs 10/20: made a gtg condition instead of a easy-to-reclaim ability.  
> 
> AF 10/29: We've changed this card enough that Reclaim 5 seems harsh. 3?  
> 
> MT 11/9: Counter should be a may. Putting counters on your opponent's creatures sucks.  
> 
> RB 11/21: good point, Mike  
> 
> bs 12/17: made sacrifice.  
> 
> AF 12/23: Fringe now, and plays interestingly.  
> 
> Del 1/13: Are we really supporting creature type Plant? This guy doesn't look any more like a plant than some of the Elementals in 9ED.  
> 
> bs 1/21: made shell smaller. was 1BG, 3/1, dredge 4.  
> 
> bs 1/31: back to 3/1.  
> 
> bs 2/21: definitely potent with guldesta.
> 
> 
> 


In the comments for **[Plague Boiler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Boiler)**, Paul Sottosanti's dry wit is revealed yet again.



> 
> RB 12/1: Add \*or remove\* would be cooler and I think it might play better too.  
> 
> ps 12/1: don't know why, but this card reminds me of nevinyraal's disk, pernicious deed, and/or oblivion stone. i like it.  
> 
> bs 12/2: upped activation by 1.
> 
> 
> 


### Last Week's Poll




| Approximately how many theme decks (online or paper) do you purchase? |
| --- |
| One, rarely. | 4262 | 30.5% |
| A couple here and there. | 3839 | 27.5% |
| None, ever. | 2929 | 21.0% |
| Average of 1-3 per set. | 2143 | 15.4% |
| One of each, every time. | 785 | 5.6% |
| **Total** | **13958** | **100.0%** |

I hope that these numbers continue to go up—we're proud of the recent (*Ninth Edition* and *Ravnica*) theme decks, and hope to keep making them at that quality level.


### This Week's Poll


**Did you play in Champs (States, Provincials, etc.?)**Yes, and this was my first time doing so.Yes, and I have done so in previous years.No, but I have played in Champs in the past.No, I have never played in these events.







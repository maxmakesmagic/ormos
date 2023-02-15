
---
[Link to Wayback Machine](https://web.archive.org/web/20211205091935/https://magic.wizards.com/en/articles/archive/latest-developments/unearthing-grixis-2008-10-23)

[_metadata_:author]:- "Matt Place"
[_metadata_:description]:- "As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on Magic development. Enjoy! –Kelly Digges, magicthegathering.com editor [card][/card]Hi! I'm Matt Place. You may not know me, but I work in Magic Ramp;D. And yes, having a job in Magic Ramp;D is as awesome as you might think it would be. One way"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "186536"
[_metadata_:path_date]:- "2008-10-23"
[_metadata_:publish_date]:- "2008-10-24"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Unearthing Grixis"
[_metadata_:wayback_capture_timestamp]:- "2021-12-05 09:19:35"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211205091935id_/https://magic.wizards.com/en/articles/archive/latest-developments/unearthing-grixis-2008-10-23"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/unearthing-grixis-2008-10-23"
---


Unearthing Grixis
=================



 Posted in **Latest Developments**
 on October 24, 2008 






![](https://web.archive.org/web/20211024110319im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By Matt Place











*As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on **Magic** development. Enjoy!*  
 –Kelly Digges, **magicthegathering.com** editor 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=%5Bcard%5D)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%5Bcard%5D)Hi! I'm Matt Place. You may not know me, but I work in **Magic** Ramp;D. And yes, having a job in **Magic** Ramp;D is as awesome as you might think it would be. One way you know the job is great is that no one believes you when you tell them you have it. Trust me, I tell everyone I meet and none of them believe me! As further proof that this job rules, here are a few conversations I have overheard in **Magic** Ramp;D in the last couple weeks. 

Ken Nagle asks Aaron Forsythe, "Where is the employee *Shards of Alara* Prerelease that happens during work hours?

Aaron answers, "It is next to the room with the free pizza."

Another example: a co-worker asks me, "Matt, where is Frank's desk?"

I answer, "If you are standing by the eight gaming computers and are facing the two 54" TVs that each have every game system hooked up to them, he is on your right." 

But... the job is not all upside. As a developer, sometimes it's my job to reign in the ideas of designers like Mark Rosewater. Their job is to get crazy, kooky designs into **Magic** sets, and my job is to keep **Magic** from breaking, and that means we don't always see eye to eye.

I remember coming into work on the last day we could make changes to *Time Spiral*. We were sending the set out to the printers that day, and one of the designers was trying to get the people in production to change a card. He wanted to change [Walk the Aeons](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walk+the+Aeons) to take three extra turns instead of just one. Obviously that would have been broken beyond belief, but he wanted to get a good [Thallid](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thallid) enabler into the set... Needless to say, the other developers and I talked him down.

This is Grixis Week, so I want to share my perspective as a developer on the work done by the design team for Grixis. The designers were Devin Low, Mark Rosewater (not officially on the team, but he did make unearth), Erik Lauer, and Brian Tinsman. How did they deal with the challenges they faced?

Challenge #1: Make Fun Magic Cards
Believe it or not, this is the biggest challenge for **Magic**. I don't mean to imply that this is anything but the best game in the world, but design can go wrong. For example, you probably not only have a list of your favorite cards that are tons of fun, but also a list of your most hated cards that you despise playing with or against. 

I flipped my lid when I first started playing **Magic** and opened a [Gaea's Liege](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Liege). Both the power and the flavor of the card appealed to me. If only I could keep it out for seven turns or so, the Leige would spread its [Forest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest)y magic over all the lands, preventing my opponent from casting any more nongreen spells! Then I would start attacking with a 7/7 or bigger—insane! One of my least favorite cards to play against is [Stasis](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stasis). When my opponent has [Stasis](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stasis) and a few [Howling Mine](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howling+Mine)s I probably have a 3% chance to win on average, but I have to play another twenty minutes to find out. Not my idea of fun. Yes, as two or three of you may remember, I was famous for making the Top 4 with a Stasis deck back in 1996 at U.S. Nationals, but that doesn't mean I enjoy playing against the card.



|  |  |
| --- | --- |
|  |  |

The Grixis team attacked this challenge in a few ways. One is the keyword they designed, unearth, a graveyard mechanic that doesn't lead to turn-three wins like some of the mistakes of the past. Those who spend any time in Ramp;D quickly learn that I hate overpowered graveyards that beat the hell out of players, like dredge. (In my defense, I was new when that one slipped past me, but I I promise to fight against that sort of thing better in the future!)

Anyway, I have a high bar when it comes to fun graveyard mechanics. So what do I think of unearth? I like the power level of unearth for Limited. You can add just a few unearth cards to your deck, and they play well. In addition, for Constructed there are a couple of cards that give you the option to build around the mechanic. [Sedris, the Traitor King](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedris%2C+the+Traitor+King) gives the mechanic to every creature in your graveyard, which lets players explore unearth with anything they can think of. That scores a lot of points for me—he takes up just one card slot in the set but opens up a lot of new decks for a lot of players. Great bang for the buck. Another card that is a "build around" is [Corpse Connoisseur](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Corpse+Connoisseur). This isn't as open-ended as Sedris, but it does give players a reason to build an unearth deck, among other things.



|  |  |
| --- | --- |
|  |  |

They also added extra ways to discard cards and sacrifice creatures in the Grixis colors. These cards not only play well with unearth mechanic, but they synergize well with cards from other shards, a point I will talk about in Challenge #3.

**My Verdict on Challenge #1:**

They made a fun mechanic and a lot of fun individual cards. I worry that some players may find the reminder text on unearth too long or too confusing, but overall I think they succeeded. I have a good time playing Grixis in Limited and Constructed.

Challenge #2: Make the Fun Cards Flavorful
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=%5Bcard%5D)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%5Bcard%5D)First, let me ask you: if you worked in Ramp;D, what kinds of cards would you design to match a world that is running over with undeath, a world where the few that are still living live in fear of being consumed by the gory undead that surround them on every side?

Like most of the challenges we face in Ramp;D, this is a fun one to tackle. When Devin first presented the design for [Skeletonize](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skeletonize), I was excited at the power level (it cost ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) when it was first designed), and I was excited about the flavor. Not only is the art that was eventually made to go with it awesome, but the mechanic itself tells you the story of how this spell burns away the flesh of your target and leaves only a skeleton behind that is under your control. This card is a great example where good game play meets awesome art that links perfectly with the mechanic.

[Prince of Thralls](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prince+of+Thralls) is another example where a fun mechanic meets flavor. This is a demon who is a master of Grixis magic. He does a good job of mechanically showing that he has mastery over the undead. Not only does it have good mechanical flavor, but I believe a lot of players will find this card to read powerfully and play fun. 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Prince+of+Thralls)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prince+of+Thralls)**My Verdict on Challenge #2:**

I believe the team did an awesome job of meeting this challenge. The Grixis cards (and the set as a whole) do a better job at linking flavor and mechanics than the average set. I wouldn't have minded seeing even more of these ties!

Challenge #3: Build Synergy within and between Shards
Having strong synergy between different shards adds a lot of replay value to the set. If we don't do well at this players won't be excited to draft after the first few times, or explore constructed decks that mix shards. So it is important that we get this right.

*Ravnica* is a great example of a set that did this well. As Mark Rosewater has mentioned in a few of his articles, this was a major goal for *Ravnica*. Take the synergy between Selesnya and Golgari, for example. The Golgari had ways to sacrifice creatures and get rewards for their deaths, like [Golgari Rotwurm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Golgari+Rotwurm). Selesnya had powerful token generation, like [Scatter the Seeds](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scatter+the+Seeds), that provided perfect food for Golgari. Just thinking about it makes me miss the days of *Ravnica* draft....

Similarly, Grixis and Jund have great synergy. Not only do the two keywords, unearth and devour, interact well, but individual Jund cards, [Rockslide Elemental](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rockslide+Elemental) for example, play well with sacrifice effects from Grixis like [Bone Splinters](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bone+Splinters) and [Fleshbag Marauder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fleshbag+Marauder).



|  |  |
| --- | --- |
|  |  |

A side note, these two shards have an interesting backstory. Early on in *Shards of Alara* design, before unearth had been conceived, Grixis had another mechanic called "carnage." [Hissing Iguanar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hissing+Iguanar) and [Deathgreeter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deathgreeter) both had this mechanic, which said "Whenever a creature goes to the graveyard from play, [do my ability]." Blue wasn't a great fit for the mechanic, so later on we moved carnage from Grixis to Jund, and replaced it in Grixis with unearth. Even later on, we killed carnage as an ability word (but kept the mechanic) and replaced it with devour as the Jund keyword. This explains why there are a lot of synergy overlaps with the two shards.

**My Verdict on Challenge #3:**

Another overall success by the design team. I think Grixis and Jund play better together than any other two shards.

The Verdict
Overall I think Grixis is a big success and the designers did a great job. On the development side, I'm a bit disappointed that we're not seeing more Grixis cards in the top Standard decks right now. My guess is that it will just take time for them to show up at a higher number in Standard.

Thanks for reading my first article. I have to end here and get back to my real job of keeping **Magic** balanced. You never know what those crazy designers are going to slip in the file next....

I hope you enjoyed the article and I hope you have enjoyed playing *Shards of Alara*!








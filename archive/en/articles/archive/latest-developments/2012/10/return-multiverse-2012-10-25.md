
---
[Link to Wayback Machine](https://web.archive.org/web/20211023122446/https://magic.wizards.com/en/articles/archive/latest-developments/return-multiverse-2012-10-25)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "Frequent readers of this column will know that Multiverse is our internal database used to track Magic cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "196391"
[_metadata_:path_date]:- "2012-10-25"
[_metadata_:publish_date]:- "2012-10-26"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Return to Multiverse"
[_metadata_:wayback_capture_timestamp]:- "2021-10-23 12:24:46"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211023122446id_/https://magic.wizards.com/en/articles/archive/latest-developments/return-multiverse-2012-10-25"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/return-multiverse-2012-10-25"
---


Return to Multiverse
====================



 Posted in **Latest Developments**
 on October 26, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 






Frequent readers of this column will know that Multiverse is our internal database used to track **Magic** cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and development processes, and a few laughs. You'll find both here. 

But first, the cast of characters:

![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_alexisjanson.jpg)**AJ**—[Alexis Janson](http://archive.wizards.com/magic/magazine/archive.aspx?author=Alexis%20Janson)![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_BillyMoreno.jpg)**BM**—[Billy Moreno](http://archive.wizards.com/magic/magazine/archive.aspx?author=Billy%20Moreno)![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_dougbeyer.jpg)**DB**—[Doug Beyer](http://archive.wizards.com/magic/magazine/archive.aspx?author=Doug%20Beyer)![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)**EVL**—[Erik Lauer](http://archive.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer)![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorPic_GavinVerhey.jpg)**GSV**—[Gavin Verhey](http://archive.wizards.com/magic/magazine/archive.aspx?author=Gavin%20Verhey)![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_KenNagle.jpg)**KEN**—[Ken Nagle](http://archive.wizards.com/magic/magazine/archive.aspx?author=Ken%20Nagle)![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_maxmccall.jpg)**Max**—[Max McCall](http://archive.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)![](https://media.wizards.com/images/magic/daily/ld/ld218_mons_johnson.jpg) **MJ**—Mons Johnson ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_shawnmain.jpg) **SM**—[Shawn Main](http://archive.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main)![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_matttabak.jpg)**Tabak**—[Matt Tabak](http://archive.wizards.com/magic/magazine/archive.aspx?author=Matt%20Tabak)![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_tomlapille.jpg)**TML**—[Tom LaPille](http://archive.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_zachill.jpg)**ZH**—[Zac Hill](http://archive.wizards.com/magic/magazine/archive.aspx?author=Zac%20Hill)And now, on to the file:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Armada+Wurm)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armada+Wurm)
> **Playtest Name**: Broodmate Wurm  
>   
> **Tabak 1/26**: Continuing the proud [Broodmate Dragon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Broodmate+Dragon) tradition of having a peculiarly monocolored token. 
> 
> 

  
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cremate)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cremate)
>   
> **EVL 8/24**: Reprint from *Guildpact*, and minor FFL security blanket.  
> **ZH 9/1**: **Magic** is better if this card is legal at fairly regular intervals. 
> 
> 

  
 One of the things we like to do in Ramp;D is provide safety valves to popular strategies and provide those in multiple colors. [Cremate](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cremate) is a card that is generally much worse than, say, [Tormod's Crypt](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tormod%27s+Crypt), if people are playing a dedicated reanimator deck, but the fact that it is a cantrip means that it is easier to play in your main deck, if the format warrants it. By the time *Return to Ravnica* was being worked on, it was clear how powerful [Snapcaster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster) was, and that both undying and [Gravecrawler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravecrawler) would give [Cremate](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cremate) ample targets if the format got to that point. Scavenge was a graveyard mechanic, and having an out for it, just in case, wasn't overlooked either. 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ethereal+Armor)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ethereal+Armor)
> **Playtest Name**: Enchanted Armor   
>   
> **EVL 11/13**: Tangential deck: Enchantments.  
> **EVL 11/15**: Could also be 2W and +2/+2; I wanted to start here because I think the smaller version is a better fit for white.  
> **BM 11/30**: The 4G Shroud guy is doing a lot of work for things like this, scavenge, etc. Glad it costs five and has no evasion. I like this version though. I think +2/+2 will have people fighting over it too much rather than pushing a tangential deck.  
> **EVL 12/6**: Added first strike. 
> 
> 

  
*Return to Ravnica*, much like original *Ravnica*, has a sub-theme of enchantments running through it. [Arrest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arrest), [Security Blockade](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Security+Blockade), [Knightly Valor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knightly+Valor), and [Paralyzing Grasp](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Paralyzing+Grasp) are just a few of the other enchantments that can make their way into your deck naturally, and suddenly jump the value of [Ethereal Armor](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ethereal+Armor) or [Sphere of Safety](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphere+of+Safety) dramatically, creating a mini-theme that will come up every few drafts. This isn't a coincidence. One thing we look for while developing a set are ways to spice up Limited and throw in some strategies that can act as keys to "tangential decks." [Spider Spawning](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spider+Spawning) in *Innistrad* and the Blue-Red [Drake Familiar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drake+Familiar) deck in original *Ravnica* are two fairly well-known examples of this. 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gore-House+Chainwalker)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gore-House+Chainwalker)
> **Playtest Name**: Rakdos Rousty  
>   
> **EVL 9/21**: 1/3 -amp;gt; 2/1  
> **Max 9/26/11**: This guy doesn't mess around 
> 
> 

  
No, Max, no he doesn't.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Horncaller%27s+Chant)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Horncaller%27s+Chant)
> **Playtest Name**: Uh Oh, Rhino  
>   
> **EVL 9/25**: Trying big green tokens  
> **Max 9/26/11**: rawr!  
> **KEN 9/26/2011**: The [Crash of Rhinos](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crash+of+Rhinos) Returns!   
> **MJ 10/6**: This card's playtest name gives it protection from developers  
> **ZH 10/19**: This and the Super-Mythic rare Wurm are creeping closer and closer to one another.  
> **TML 10/19/2011**: Uh oh!  
> **EVL 10/20**: Tom wins. 
> 
> 

  
 The playtest name for this card was "Uh Oh, Rhino." As Mons (MJ above) identifies, albeit humorously, this does have an impact on the cards that finally make it to the set. I'm not saying that you could fit in a red [Mana Drain](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain) by giving it a clever enough name, but cards with resonant names are just going to draw people's attention more, and see more play during playtests. It's possible that this card might not have seen print if the name had been "Two Baloths," "Populate Elk," or "Gimme Some Boar" (okay, that one could've made it). 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Izzet+Keyrune)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Izzet+Keyrune)
> **Playtest Name**: Izzet Statuette  
>   
> **Tabak 2/27**: Changed to a new guy. Was 2/2 blue and red [Elemental](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elemental) artifact creature with "This creature can't be blocked except by creatures with defender."  
> **KEN 3/6/2012**: When I double activate this, it gets double looting?  
> **Tabak 3/7**: Not any more. 
> 
> 

  
Matt Tabak, our trusty rules manager, is here to do two things: answer rules questions and ruin everyone's fun.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Launch+Party)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Launch+Party)
> **Playtest Name**: Madcap Cannonade  
>   
> **SM 8/1**: [Innocent Blood](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Innocent+Blood) -amp;gt; fixed [Death Bomb](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Bomb).  
> **EVL 8/2**: Is this a repeat?  
> **KEN 8/2/2011**: It's cleaner [Death Bomb](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Bomb).  
>  **KEN 8/16/2011**: 3B -amp;gt; 4B.  
> **EVL 9/12**: 4B -amp;gt; 3B  
> **Max 9/27/11**: Reads odd considering [Hideous End](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hideous+End)  
> **TML 9/31/2011**: Some cards are worse than others? :B  
> **GSV: 9/25**: In the eyes of Rakdos cultists, sacrificing is an all-upside mechanic.  
> 
> 
> 

  
[Death Bomb](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Bomb) was often considered to be a "bad" card during *Planeshift*, but **Magic** sets need cards that are worse than other cards for Limited purposes. If every removal spell is the best card in the set, then drafting is all about taking cards in the right order and seeing how the chits fall. Besides, as Gavin indicates, the card just feels right for Rakdos in the set. 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Niv-Mizzet%2C+Dracogenius)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Niv-Mizzet%2C+Dracogenius)
>   
> **KEN 10/24/2011**: Boo to card-discarding [Masticore](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Masticore)s, hooray card-drawing [Masticore](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Masticore)! 
> 
> 

  
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nivmagus+Elemental)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nivmagus+Elemental)
> **Playtest Name**: Spell Weird  
>   
> **EVL 11/14**: New!  
> **KEN 11/15/2011**: Storm!! EOT [Sprouting Vines](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sprouting+Vines) nom nom nom.  
> **DB 11/15**: hrmm, storm, just what we want to make better.  
> **AJ 12/1**: I hope this gets some reminder text, because it's pretty confusing where the "spell" comes from :)  
> **MJ 12/19**: hopefully the spell you just cast comes from exile (i.e. [Misthollow Griffin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Misthollow+Griffin))  
> **EVL 12/19**: Only instants and sorceries. Also, 1 mana. The set was low on 1 mana rares, I would like to see if this is a fun one or not.  
> **KEN 12/20/2011**: This works kind of nicely with Flashback spells.  
> **MJ 12/21**: I am not so sure. The question will be asked, "what is the CC of a flashback'd spell?"...  
> **EVL 12/26**: Testing 2 counters instead of X.  
> **EVL 2/1**: Added a toughness 
> 
> 

  
 This began life as a flavorful design of a creature that ate spells, getting their converted mana cost in +1/+1 counters. This brought up some concerns from various designers and developers, both for understanding what the converted mana cost of different cards on the stack were, and for balance reasons. Mons Johnson, of [Goblin Raiders](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Raiders) fame, is one of the strongest Johnnies in the Pit, fondly making decks and breaking cards that on first sight might seem outlandish to the heavier Spikes. In this case, his decks led to the Elemental no longer eating [Misthollow Griffin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Misthollow+Griffin) and changing to just two counters—after a few miracles were eaten. 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rogue%27s+Passage)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rogue%27s+Passage)
> **Playtest Name**: Secret Gate  
>   
> **EVL 10/7**: New TOPDOWN  
> **TML 10/19/2011**: This is comical.  
> **GSV 10/25**: Comically awesome! Love this card, and the idea of a "secret gate." Reads well for limited, but has the hidden drawback of making colorless in a multicolored set.  
> **Tabak 2/23**: No longer a Gate. New name on the way. 
> 
> 

  
 During development, there were six gates in *Return to Ravnica*. Thematic changes in the set pushed [Rogue's Passage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rogue%27s+Passage) back to a regular nonbasic land, but Multiverse reminds us of what almost was. 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Seek+the+Horizon)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seek+the+Horizon)
> **EVL 9/1**: New card, reprint from SoK  
> **ZH 9/2**: Yeah, this is sweet.  
> **TML 9/21/2011**: This card is always way worse than I think it will be, which is cool. The name makes me think of nature, though, which is kind of wrong for us.  
> **DB 9/21/2011**: The tone changes. On Kamigawa it's a noble quest. On Ravnica it's kind of like saying "go jump in a lake." :) 
> 
> 

  
Sometimes comments in Multiverse are less helpful for the cards, and more humorous.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Slime+Molding)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slime+Molding)
> **EVL 9/25**: If I make a 5/5 Hydra and propagate, do I get another 5/5 Hydra?  
> **Max 9/26/11**: Yes. I like this card a lot.  
> **EVL 11/28**: Sorcery -amp;gt; Instant  
> **EVL 12/4**: Instant -amp;gt; Sorcery 
> 
> 

  
Iteration is an important part of development. Sometimes trying a sorcery as an instant provides a fun new angle for the card. Sometimes it creates a green removal spell that attacks back. You never know for sure until you try.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sphinx%27s+Revelation)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation)
> **EVL 9/8**: New card for playtest.  
> **MJ 10/6**: nice.  
> **EVL 12/9**: Trying the suggested "target player" version. I have my concerns that this makes it even better (win-condition), but the deflection aspect is worth trying.  
> **EVL 12/14**: Trying one more mana, and instant  
> **KEN 1/9/2011**: Do we want this to target?  
> **Tabak 3/8**: No longer targets 
> 
> 

  
 I've read a lot of people who thought this card would be better as a ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) sorcery. Well, it was at one point, and the decision was made that it fit better as an instant for interactive control decks, rather than over-incentivizing tap-out control. 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tower+Drake)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tower+Drake)
> **Playtest Name**: Stalwart Drake  
>   
> **TML 9/21/2011**: I enjoyed [Tower Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tower+Drake), so I'm looking forward to this.  
> **EVL 11/14**: 3/1 -amp;gt; 2/3  
> **SM 11/14**: Um... awkward next to the white griffin.  
> **EVL 12/2**: OK, back to 3/1.  
> **EVL 12/4**: Now a 2U 2/1.  
> **Tabak 12/5**: Now [Tower Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tower+Drake).  
> **DB 12/6/2011**: Huh. Well, it's a drake, and it's flying near some towers... it's not out of the question for this to be an actual reprint.  
> **EVL 12/7**: Wow you guys have great memories!  
> **KEN 12/16/2011**: [Tower Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tower+Drake) has found its proper plane! :) 
> 
> 

  
 Sometimes things just work out. This began life as a 3/1, costing ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif), and over time migrated closer and closer to the card it was intending to mimic. Luckily, creative lead on the set Doug Beyer was able to step in and point out that sometimes a [Tower Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tower+Drake) is just a [Tower Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tower+Drake). No reason to reinvent the wheel when you don't need to. Hooray! 

  
 That's it for this week. There are plenty of other great things hidden in the Multiverse file for *Return to Ravnica*, but those might have to wait for a later date when references to *Gatecrash* cards and mechanics can be included. 

Until next time,

Sam

![](https://web.archive.org/web/20150711050253im_/http://archive.wizards.com/mtg/images/widgets/storelocator/SmallStoreLocator_Background_Left.png)![](https://web.archive.org/web/20150711005846im_/http://archive.wizards.com/mtg/images/widgets/storelocator/EN_SmallStoreLocatorGOText.png)![](https://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_GameDay_Top_FIX.jpg)![](https://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_GameDay_LeftOfButton01.jpg)[![](https://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_GameDay_Button01_Static.jpg)](http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/gameday)![](https://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_GameDay_RightOfButton01.jpg)![](https://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_GameDay_Middle.jpg)![](https://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_GameDay_LeftOfButton02.jpg)[![](https://media.wizards.com/images/magic/daily/footers/EN_RTR_ArticleFooter_GameDay_Button02_Static.jpg)](http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/gameday)  








---
[Link to Wayback Machine](https://web.archive.org/web/20151225144441/http://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-06)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "Beginning with this article, Sam's series where he explores Multiverse comments will be known as the M Files. Look for the M Files image in the future if you're a fan of this popular series!Mike McArtor, copy editor of DailyMTG"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "201886"
[_metadata_:publish_date]:- "2013-11-06"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The M Files: Theros"
[_metadata_:wayback_capture_timestamp]:- "2015-12-25 14:44:41"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20151225144441id_/http://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-06"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/m-files-theros-2013-11-06"
---


The M Files: Theros
===================



 Posted in [Latest Developments](/en/articles/columns/latest-developments-archive)
 on November 6, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 






*Beginning with this article, Sam's series where he explores Multiverse comments will be known as the M Files. Look for the M Files image in the future if you're a fan of this popular series!*

Mike McArtor, copy editor of DailyMTG

![](https://media.wizards.com/images/magic/daily/ld/ld272_mfiles.jpg)  
It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track **Magic** cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and development processes, and a few laughs. You'll find both here. 

But first, the cast of characters:

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_davehumpherys.jpg)**DH**—[Dave Humphreys](http://archive.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humphreys)  
**Magic** development manager ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_ethanfleischer.jpg)**EEF**—[Ethan Fleischer](http://archive.wizards.com/magic/magazine/archive.aspx?author=ethan%20fleischer)  
**Magic** designer and [resident Greek-history expert](http://archive.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/feature/263)![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)**EVL**—[Erik Lauer](https://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Erik%20Lauer)  
lead developer of *Theros*![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_ianduke.jpg)**ID**—Ian Duke  
**Magic** developer ![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_kellydigges.jpg)**KD**—[Kelly Digges](http://archive.wizards.com/magic/magazine/archive.aspx?author=kelly%20digges)  
lead editor of *Theros*![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_kennagle.jpg)**KEN**—[Ken Nagle](http://archive.wizards.com/magic/magazine/archive.aspx?author=Ken%20Nagle)  
**Magic** designer ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_maxmccall.jpg)**Max**—[Max McCall](http://archive.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)  
**Magic** digital developer ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_markglobus.jpg)**MJG**—MJG: [Mark Globus](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Globus)  
**Magic** senior producer ![](https://media.wizards.com/images/magic/daily/ld/ld218_mons_johnson.jpg)**MJ**—Mons Johnson  
**Duel Masters**/**Kaijudo** developer and **Magic** playtester ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_markrosewater.jpg)**MR**—[Mark Rosewater](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater)  
lead designer of *Theros*![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_shawnmain.jpg)**SM**—[Shawn Main](http://archive.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main)  
**Magic** designer ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_samstoddard.jpg)**SPS**—[Sam Stoddard](http://archive.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard)  
That's a-me ![](http://archive.wizards.com/magic/images/mtgcom/authorpics/authorpic_SteveWarner.jpg)**SW**—Steve Warner  
**Duel Masters**/**Kaijudo** and **Magic** playtester ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_tomlapille.jpg)**TML**—[Tom LaPille](http://archive.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)  
**Magic** developer ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_zachill.jpg)**ZH**—[Zac Hill](http://archive.wizards.com/magic/magazine/archive.aspx?author=Zac%20Hill)  
Former **Magic** developer, current **Magic** talking head Now that we have that out of the way, onto the files:

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Unknown+Shores)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unknown+Shores) EVL 6/18: 5 color fixing.  
 EVL 9/14: Replaces [Evolving Wilds](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evolving+Wilds).  
 SPS 9/21: I like this change. Splashing is a path to take, not a basically free decision.  
 TML 10/15/2012: Replaced with functional reprint of [Shimmering Grotto](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shimmering+Grotto).  
 SPS 11/1/12: Yay functionally reprinted lands. 

 The first version of this card was [Evolving Wilds](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evolving+Wilds), which worked, but the slightly higher gold numbers in *Theros*, and so many of the bestow creatures only requiring a single colored mana, led to a lot of splashing. Just coming out of *Return to Ravnica* block, it seemed that it would be better to try and nudge people toward two-color decks. We started this out as [Terminal Moraine](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terminal+Moraine), which eventually became the functional reprint of [Shimmering Grotto](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shimmering+Grotto) you can see today. 

The important thing to note is that we didn't want to keep people from splashing in Limited, especially in Sealed, but to just make sure there was a reasonable cost involved. Ideally, splashing is usually incorrect, but can be correct in certain circumstances.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Opaline+Unicorn)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Opaline+Unicorn) DH 10/11: I like where this is at. I'd been refusing to play it but have been reconsidering as people put it to decent use against me.  
 EVL 11/21: Added a toughness.  
 DH 11/26: A bit too similar to Living Caryatid for my tastes in the same set. Would rather see this as a 1/1 or some other means of differentiation in function.  
 EVL 11/26: OK, 1/2.  
 SPS 11/29: Putting that horn to good use. 

This card started as a 0/1, and earned a lot of ire (most of it probably undeserved), because it looked so bad. It still served a purpose in Limited, but many people weren't playing it even when they probably should have. Improving it a bit helped out on that front and got people to start putting it in their decks when they had a lot of monsters or expensive bestows.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Witches%27+Eye)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Witches%27+Eye) EVL 8/29: From Romans. Sorry Ken!  
 KEN 8/29/2012: ;( my eyeball 

 Sometimes, as the development of a set moves on, we find that we have cards we don't like and we need to cut them. One of the easiest ways to fill a hole is to see if another, later set in the same block has a card that you could use. In this case, we stole the card from Ken's file for *Born of the Gods*. Sorry, Ken, but luckily the eye got put to good use! 

[Flamespeaker Adept](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flamespeaker+Adept)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flamespeaker+Adept)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flamespeaker+Adept) EVL 8/3: For the UR Scry deck.  
 SPS 8/30: This is cool  
 SM 8/30: So amusing. Glad he has Ken's eyeball to help him now. 

 We try to make each color pair in Limited "do" something; blue-red is the spells-matter color pair, but also it focuses on scry. When we do this, we usually put in some kind of build-around uncommon that isn't very strong if you aren't doing "the thing," but gets stronger when you do—as way to reward people in different color pairs. [Nemesis of Mortals](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nemesis+of+Mortals), for example, does this for green-black. Moving [Witches' Eye](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Witches%27+Eye) to *Theros* gave the blue-red deck another great way to trigger [Flamespeaker Adept](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flamespeaker+Adept). 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Centaur+Battlemaster)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Centaur+Battlemaster) DH 7/20: Feels a lot like a monster.  
 TML 7/20/2012: In this card's defense, I felt very heroic when I actually pulled it off. 

 Hulk Smash! 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pheres-Band+Centaurs)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pheres-Band+Centaurs)(was a 2/7)

 ZH 7/20: FILL OUT THAT SPREADSHEET! ;)  
 Max 8/30: This card looks black or white to me, not green.  
 EVL 9/3: Is 3/7 more green?  
 Max 9/6: Yes :) 

 Erik Lauer has, for the past several years, been attempting to make sure there is a vanilla of each power and toughness combination of 1–6 in **Magic**. He completed this is *Return to Ravnica* with [Catacomb Slug](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Catacomb+Slug), but has since moved on to making sure that 1–7 also have vanillas. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mistcutter+Hydra)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra) Oh, the long and crazy history of [Mistcutter Hydra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra). 

EEF 8/17/11: New card.

 The card began as a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) 12/12 with "cannot attack unless you control at least twelve permanents" as a nod to Hercules. Creative was unhappy with the largest creature in *Theros* being a human, and so it became a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) Hydra with that text. 

 ID 8/30: Not in love with this, seems like it would be a frustrating experience to try to turn this on.  
 DH 9/4: Like it in green better with ramp, fight, and possibly tokens.  
 Mago 9/11: Strange that both rare/mythic rare green Hydras cost 2GG  
 MJ 9/13: better to not turn it on, just play [Disciple of Bolas](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+Bolas)...  
 TML 10/15/2012: Now 3G for Johnny.  
 EVL 12/6: New design to attack control decks.

 The card then changed to something to better fight the [Sphinx's Revelation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation) decks we were seeing in the real world, as well as the white-blue control decks in our [FFL](http://archive.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/260) with Elspeth, and create a creature that was not killable by [Detention Sphere](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detention+Sphere). 

 Twelve-Headed Hydra  
 3GG  
 Trample  
 You may cast CARDNAME from your graveyard or exile. Whenever an opponent draws a card, put a +1/+1 counter on CARDNAME.  
 5/5  
 MJ 12/14: Testing shows this to be too powerful as is, imo. Might be ok as a 4/4.  
 EVL 12/18: removed some text, but now can't be countered and protection from blue.  
 EVL 12/31: New text. 

It was in between this time that we created the cycle of "protection from [color]" creatures, and that changed what we needed from this card.

The card then changed to:

[Mistcutter Hydra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra)  
 XG  
 Haste, protection from blue  
 CARDNAME enters the battlefield with X +1/+1 counters on it.  
 If an opponent has five or more cards in hand, you may cast CARDNAME from your graveyard.  
 0/0  
  
MR 1/03/13: Card feels very inelegant. I know it's serving a development purpose but I wonder if it can be made a little less Frankenstein looking.

 Besides just looking weird, one problem with being able to cast a Hydra from your graveyard meant that death or "enters the battlefield" triggers suddenly became live on just paying ![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). That was not okay. 

EVL 1/10: New text.  
  
[Mistcutter Hydra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra)  
 XG  
 Trample, haste, protection from blue  
 CARDNAME can't be countered.  
 CARDNAME enters the battlefield with X +1/+1 counters on it.  
 Remove two +1/+1 counters from CARDNAME: Regenerate CARDNAME.  
 0/0  
  
 Sw 1/14: I feel like this is a bit over what we would normally give a card. I could see this at XGG, or even XG if it didn't have haste. I don't think it's breaking much (besides blue) now, just a bit over.  
 EVL 1/15: Removed regenerate text.  
 Max 1/23: I think we will be unhappy with how powerful this is against next year's blue decks.  
 KD 1/28: Loses trample, now can't be blocked by small creatures. 

The card with trample and haste was powerful enough that many of our green decks were playing it main, which is not where we wanted this card. We wanted it to be something that could be main deck if the format was skewed toward blue, but would be more of a sideboard card, so we took that ability off. We were still worried about green decks not having a good answer to Elspeth, so the card morphed into:

[Mistcutter Hydra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra)  
 XG  
 Haste, protection from blue  
 CARDNAME can't be countered.  
 CARDNAME enters the battlefield with X +1/+1 counters on it.  
 CARDNAME can't be blocked by creatures with power 1 or less.  
 0/0  
  
 KD 3/28: Per Erik, cut pseudo-trample: [Mistcutter Hydra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistcutter+Hydra) can't be blocked by creatures with power 1 or less.  


Very late in development, Nylea's abilities changed and granted trample to all creatures. This was the exact change we needed to give green decks a way to beat an Elspeth, so we were able to take off the last super-wonky words from the card, and end up in a more sensible place.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Triton+Tactics)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Triton+Tactics) ID 12/10: This is super underwhelming compared to the others in the cycle. Should this give some extra bonus, like hexproof, or frosting creatures they block this turn?  
 EVL 12/12: Great idea.  
 KD 3/18: Template update: Now with [Joven's Ferrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Joven%27s+Ferrets) technology so it locks things down whether you play it before or after blockers. 

 It's not often that the editors need to go to *Homelands* to find templates. [Joven's Ferrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Joven%27s+Ferrets) provided the wording we needed but never answered the question of why [Joven](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Joven) was into Ferrets. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Anger+of+the+Gods)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anger+of+the+Gods) EVL 9/7: Changed to anti-regenerate due to [Lotleth Troll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotleth+Troll).  
 KEN 9/10/2012: [Lotleth Troll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotleth+Troll) must go big or go home!!  
 MJG 9/11/12: This is the second red card with the anti-regen clause. Seems like one too many.  
 TML 10/29/2012: Used to be anti-regen. Now exiles.  
 ID 11/12: I like that this answers [Voice of Resurgence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Voice+of+Resurgence) effectively. Provides a good tension between red and white sweepers. 

 It's not every day we get to create powerful red sweepers, but one of the things we have tried to do is give red some additional midrange options and keep it from being just a beatdown color. We had already seen Chandra in ***Magic** 2014* working great as a top-end card in red aggro, or as a card drawer in the red-based midrange decks. We also knew that devotion is a risky mechanic that can snowball, so making sure that multiple colors have options for sweepers would keep the format in a place where it could evolve. [Anger of the Gods](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anger+of+the+Gods) was in the right place to solve all of those issues. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cavalry+Pegasus)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cavalry+Pegasus) EVL 9/21: New ability to avoid looking like a heroic trigger.  
 EVL 11/21: Changed to a 2HG template!  
 EVL 1/2: Trigger free!  
 ID 1/8/13: Downside to trigger free is that if someone advances to declare blockers and doesn't realize a human has flying, there's no backing up. I can see myself doing this and getting frustrated.  
 EVL 1/9: Good point Ian. I think this is worth trying.  
 TML 2/6/2013: I prefer these being triggers now. I think this and power/toughness granting things should be the same, and anything that grants toughness needs to be a trigger until eot or things can just die out of nowhere.  
 KD 2/7: Now a trigger. Because it's an attack trigger, I dropped "you control" for 2HG. 

The original version of this card gave flying to one target Human when you attacked.

 One piece of early feedback we got on *Theros* was that playtesters were sometimes confused when their triggers on creatures didn't trigger heroic. We briefly tried out heroic working that way, but the cards were impossible to balance, considering a card like [Civic Saber](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Civic+Saber) turned [Labyrinth Champion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Labyrinth+Champion) into a machine gun, and there were already several Equipment in the set. 

Instead, what we did was to try and remove as many instances of creatures that could target your own creatures as we could, at least at lower rarities. There are still some, but most of them are there because the game play was just better to be able to target your own guys. We also tried a version of him that didn't trigger, which had some rules benefits, but which could create some huge blowouts if it was killed during combat. We opted to go with the current version instead.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fanatic+of+Mogis)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Mogis) EEF 5/24/12: 5R 2/3 -gt; 2R 3/1. Common -gt; uncommon.  
 EVL 11/21: Added a mana and a toughness.  
 DH 11/26: Can this be a 4/2 ? As uncommon I'd rather this not be completely trumped by the 2/4 Devotion Drainer in black.  
 EVL 11/26: OK, 4/2 if creative approves. 

 Devotion was a hard mechanic to get right, and we quickly found that a lot of cards with devotion were stronger than we were expecting. For [Fanatic of Mogis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Mogis), this was mostly due to the powerful ![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) cards like [Burning-Tree Emissary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning-Tree+Emissary), [Ash Zealot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ash+Zealot), and [Boros Reckoner](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Reckoner). Moving the cost on this to four mana meant that you could no longer curve out at one- two- three-drop and have your opponent at 8 life (or less) the beginning of his or her fourth turn. Upping the cost gave the opponent much more of an opportunity to interact with the board before Fanatic hit the table. 

That's it for this edition of the M Files.

Until next time,  
 Sam ([@samstod](https://twitter.com/@samstod)) 

  
  
![](https://media.wizards.com/images/magic/daily/footers/slice1.jpg)![](https://media.wizards.com/images/magic/daily/footers/slice2.jpg)![Sam Stoddard](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_samstoddard.jpg) **Sam Stoddard**[@SamStod](https://twitter.com/SamStod)[Email Sam](/company/emailtoauthor.asp?author=Sam%20Stoddardamp;amp;headline=%5BThe%20M%20Files:%20Theros%5D "Click to send email to the author.") | [Author Archive](/Magic/Magazine/Archive.aspx?author=Sam%20Stoddard)[Latest Developments Archive](/Magic/Magazine/Archive.aspx?tag=Latest%20Developmentsamp;description=Latest%20Developments) |  
 Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 








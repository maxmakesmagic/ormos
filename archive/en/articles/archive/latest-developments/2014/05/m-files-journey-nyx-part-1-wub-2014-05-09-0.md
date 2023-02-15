
---
[Link to Wayback Machine](https://web.archive.org/web/20151225144435/http://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track Magic cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646381"
[_metadata_:publish_date]:- "2014-05-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The M Files: Journey into Nyx, Part 1 (WUB)"
[_metadata_:wayback_capture_timestamp]:- "2015-12-25 14:44:35"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20151225144435id_/http://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0"
---


The M Files: Journey into Nyx, Part 1 (WUB)
===========================================



 Posted in [Latest Developments](/en/articles/columns/latest-developments-archive)
 on May 9, 2014 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 






![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld272_mfiles.jpg)It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track **Magic** cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and development processes, and a few laughs. You'll find both here.


*Journey into Nyx* had a lot of great comments in Multiverse, so I am going to actually break this up into two articles to make sure I can get more of them in.


But first, the cast of characters:




![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_aaronforsythe.jpg)
**AF**—[Aaron Forsythe](http://www.wizards.com/magic/magazine/archive.aspx?author=Aaron%20Forsythe)  
**Magic** Senior Director

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/2014/ld_wk18_298_benhayes.jpg)**BH**—Ben Hayes  

Developer

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_dellaugel.jpg)**DEL**—Del Laugel  
**Magic** Senior Editor




![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_danemmons.jpg)
**DE**—Dan Emmons  
**Magic** Designer

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_davehumpherys.jpg)**DH**—[Dave Humphreys](http://www.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humphreys)  
*Journey into Nyx*'s Lead Developer and Development Manager

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_ethanfleischer.jpg)**EEF**—[Ethan Fleischer](https://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ethan%20Fleischer)  
*Journey into Nyx*'s Lead Designer




![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)
**EVL**—[Erik Lauer](http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer)  

Head Developer

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_gavinverhey.jpg)**GSV**—[Gavin Verhey](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Gavin%20Verhey)  
**Magic** Experience Designer and ReConstructed Columnist

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_ianduke.jpg)**ID**—Ian Duke  
**Magic** Developer




![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_kennagle.jpg)
**Ken**—[Ken Nagle](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ken%20Nagle)  
**Magic** Designer, lover of fatties

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_maxmccall.jpg)**Max**—[Max McCall](http://www.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)  

Former **Magic** Digital Developer

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_markglobus.jpg)**MJG**—Mark Globus,  
**Magic** Senior Producer




![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_samstoddard.jpg)
**SPS**—[Sam Stoddard](http://www.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard)  

That's a-me

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_tomlapille.jpg)**TML**—[Tom LaPille](http://www.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)  
**Magic** Developer





![Akroan Mastiff](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Akroan+Mastiff)


 
ID 2/11/13: Tappers are brutal in this block, with all the "go tall" mechanics.  

DH 2/25: We can reduce rates on this but we are intentionally pushing back some on going so tall.  

TML 2/26/2013: I like this.



As I mentioned in [my recent mailbag article](/en/articles/archive/latest-developments/journey-mailbag-2014-04-25-0), [Akroan Mastiff](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroan+Mastiff) was intended for Limited, not to be too strong against regular Limited strategies, but instead to punish people attempting to go tall—which has been the defining characteristic of the block so far.





![Dictate of Heliod](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dictate+of+Heliod)


 
DH 2/21: New card for flash symmetric cycle.  

DH 2/25: Rule of Law variant at 2WW had some enemies. Trying Anthem instead.  

TML 2/26/2013: Hooray!  

SPS 3/8/2013: Strong.  

DH 3/12: Looking to differentiate more from Heliod's Weapon. Moved up numbers. [*At this point, the card cost 2WW and gave all of your white creatures +2/+2* —Sam]  

EEF 3/14/13: Rawr! Git 'em!  

TML 3/28/2013: Hope this works out.  

DH 4/2: Still happy with this if it is 3WW and we delete 'white'. Wondering if I should do that preemptively?  

TML 4/4/2013: I'd let it break first.  

DH 4/9: Moved to 5 mana and now all your creatures, not just white ones.



It didn't take long when testing with the ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) version to really push the white aggro decks over the top. I think we found a much more interesting cost—one where you probably will run a few, but probably not run four in every weenie deck.





![Sightless Brawler](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sightless+Brawler)


 
EEF 9/26/12: New card.


As an aside, the original version of the "downside bestow" cycle started off as an even larger downside—they didn't even add to the power and toughness of the creatures. So, this card said that the creature couldn't attack, but didn't give it an extra power and toughness. If for some reason that creature died, then you would end up with a defender. It was an interesting attempt at how to make bestow feel new, but one that was very confusing because of how different it was from the original versions.


EEF 11/13/12: Bestow 1W → 2W.  

MJG 1/8/13: It is really weird to me that these bestow creatures don't provide p/t.  

AF 2/8: I can sort of accept this being a Magic card, but I have a hard time accepting it as a common. I imagine that's true for all negative-bestow guys. They require such high levels of understanding things.  

EVL 2/11: I think the "unusual common" aspect would be acceptable if I enjoyed the game play enough, but I don't think the tradeoff is good in this case.  

DH 2/25: Moved common negative to uncommon.  

Max 3/18: Oh I actually like this card.  

DH 3/29: Not ideal, but adorable in some ways. Wouldn't like this if they all looked this way.  

DH 3/29: New power based on meeting idea from ID, given we are now apparently doing this in white too. Following model of using stats again, and usually putting on your own creatures but occasionally opponents.



The development that happened with the cards was to add back the power and toughness bonus but to change what the downsides were, so you were more likely to put it on your own creatures but could use it as a trick in a pinch against a creature an opponent controls.





![Banishing Light](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Banishing+Light)


 
EVL 4/26: Made into new-template Oblivion Ring for FFL purposes.  

ID 4/29: If this is our first new template o ring, it may want a name that's not specific to the plane for reprint/core set.  

GSV 4/30: Agree with ID. Was my first thought as well.  

TML 5/1/2013: Agreed.



The card-naming thing here is an interesting thing. While it is creative's job to name cards, development tries to pick out cards we might want to reprint (in places other than core sets), and try to give them generic-enough names that we can use them in other sets when we need to. [Banishing Light](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Banishing+Light) (like [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) before it) could be flavored to fit just about anywhere. If it was given a name like Heliod's Banishment, then we would've needed to create a second version of the card if we decided in two years that we needed the same card in Standard.





![Sage of Hours](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sage+of+Hours)


 
EEF 2/1/13: New card.  

ID 2/4/13: Feels bad giving my guy -5/-5 to take an extra turn and then not be able to attack with him. Could put "take an extra turn" in the heroic trigger. "...put a +1/+1 counter on it. Then, if it has exactly three +1/+1 counters on it, take an extra turn after this one." Much harder to loop and now pure upside.  

DH 2/5: Think this has room to be stronger, inclined to just try 4 counters. Think the exact wording still would be too easy to loop via removing/adding.  

EEF 2/6/13: Five → four. Not sure how to reword it. I'll leave it to the dev team and the editors.  

Del 2/26: Editing has no reason to suggest other words.  

DH 3/14: 2U → 1U.  

SPS 3/26: this +Ajani is just about game. Dangerous card is dangerous.  

DH 4/2: Noted. We'd seen that interaction. Open to seeing what this does in FFL. It might need to be: "Remove all +1/+1 counters from CARDNAME: If you removed four or more counters this way, take an extra turn after this one." so you can't build it up and increment like with Ajani.  

DH 4/9: And up to 5 counters.  

DH 5/7: May want this to be remove some (4–5) counters and return to hand as a further knob. Cleaner way to make sure it doesn't accumulate too many extras.  

ID 5/7: Returning to hand lets me attack into your blockers before taking an extra turn, without risk of him dying.  

DH 7/10: Tweaked to always remove all counters. Decided to keep scaling to multiple turns for now. We can revisit.



Any time you have a card that is a repeatable [Time Walk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk) effect, you need to be pretty careful with it. Early versions were strong enough that we worried that, if we were wrong, it would be very easy to turn games with cards like Ajani into kill-this-now-or-you-die-fests, which really isn't good game play. I think we got the card to a point where you can take infinite turns if you want to jump through a lot of hoops, but there isn't a way to do it incidentally. It's awesome if working hard gets you cool things. It's less awesome if everyone is doing it just because it is powerful.





![Interpret the Signs](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Interpret+the+Signs)


 
DH 3/4: Trying to stick with concept. Does this work? Making a counterpart to Riddle of Lightning. Although this is the same basic effect as the Sphinx I just added at rare.  

TML 3/4/2013: This is rad.  

SPS 3/8/2013: This card is sweet, even if it butts up poorly with Opposition in M14.  

ID 3/11: A satisfying mirror to Riddle of Lightning.  

KEN 4/11/2013: The best moment of Riddle of Lightning is when the opponent sees you scry 3 to the bottom and knows there's a chance his creature will live. Can this be a Mana Leak or a 1-shot Counterbalance for a similar moment with a dramatic moment where my Lava Axe might still kill you?  

TML 5/1/2013: I think that moment could still happen if someone gets two lands and a 2cc thing.  

DH 5/13: 4CC → 5C.



One of the ways we get inspiration for new cards is from the past. We liked [Riddle of Lightning](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riddle+of+Lightning) for the set, especially since it fit well into Keranos's flavor and the mechanics we were going for, with UR having a lot of scry. That cycle didn't have a great solution for blue, so we decided to make up a new card that felt like it would feel right next to Riddle.





![Pharika's Chosen](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pharika%27s+Chosen)


 
FUNCTIONAL REPRINT—Typhoid Rats—ISD  
  

DH 2/20: 1/2 → 1/1. Functional Reprint.  

TML 2/26/2013: We have this in THS though, right?  

DH 2/26: We have a bestow DT at 1B. Different enough I think?  

TML 3/4/2013: Yup, I think so.  

SPS 3/8/2013: To me, I'm reminded of the G deathtouch in Theros, not the 1B DT  

Max 3/18: G 1/1 deathtouch is in THS.  

DH 3/18: That doesn't really bother me. Should it?  

Max 3/21: It's another common that is super strong against tall strategies, and in general deathtouch creatures are I think boring.  

TML 3/28/2013: This is what green-black graveyard decks need, so I think I'd keep it.



I also mentioned this briefly [last week](/en/articles/archive/latest-developments/making-enchantments-matter-2014-05-02-0), but when you have a three-set block, it is hard to not have some overlap in cards. In this case, we had what is basically the same card in both green and black, but both fit individually.





![Worst Fears](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Worst+Fears)


 
DESIGN FAVORITE.  
  

DH 2/21: Cut the extra turn for them. Added 2 mana.  

TML 2/26/2013: Well then.  

BH 3/6/2013: Wow, this card is exciting!  

ID 3/11/13: Can't wait to cast this off of the tribute guy in BNG  

KEN 4/4/2013: Now I know to give ID big tribute guys.  

DH 7/19: 6BB → 7B. Cutting some CC from high rarity.



This card started off cheaper, but your opponent got an extra turn—so it didn't have the "[Time Walk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk)" part of [Mindslaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver). The wording was both confusing and meant that the card was much more narrow, so we changed to the newer, actual-[Mindslaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver) text.


You also notice that this card is labeled "Design Favorite." One part of design handoff is that the design team indicates its favorite cards in the set—the ones it would like to see kept to maintain the integrity of the team's vision. It's not required that the development team keeps all of them, especially as-is, but it's important for the development team to do as much as it can to keep the cards in the file, or at least make a good-faith effort to replace the card with something that fulfills the same design goals the design team is happy with.


That's all the space I have for this week. I'll be back next week... with Vintage Masters previews! But, the week after that, I have a sweet new *Conspiracy* card to show you! But in three weeks, I'll be back with the next edition of the M Files, including red, green, and gold, with the Gods of *Journey into Nyx*.












---
[Link to Wayback Machine](https://web.archive.org/web/20201202031852/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-12)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track Magic cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "207926"
[_metadata_:path_date]:- "2014-02-12"
[_metadata_:publish_date]:- "2014-02-14"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The M Files: Born of the Gods"
[_metadata_:wayback_capture_timestamp]:- "2020-12-02 03:18:52"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201202031852id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-12"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-12"
---


The M Files: Born of the Gods
=============================



 Posted in **Latest Developments**
 on February 14, 2014 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 






![](https://media.wizards.com/images/magic/daily/ld/ld272_mfiles.jpg)  
It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track **Magic** cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and development processes, and a few laughs. You'll find both here. 

But first, the cast of characters:

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_aaronforsythe.jpg)**AF**—[Aaron Forsythe](http://archive.wizards.com/magic/magazine/archive.aspx?author=Aaron%20Forsythe)  
 The Boss ![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_billymoreno.jpg)**BM**—[Billy Moreno](http://archive.wizards.com/magic/magazine/archive.aspx?author=Billy%20Moreno)  
 Former **Magic** Developer ![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_dougbeyer.jpg)**DB**—[Doug Beyer](https://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Doug%20Beyer)  
**Magic** Senior Creative Designer   
  
![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_danemmons.jpg)**DE**—Dan Emmons   
**Magic** Designer ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_davehumpherys.jpg)**DH**—[Dave Humphreys](http://archive.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humphreys)  
**Magic** Development Manager ![](https://media.wizards.com/legacy/magic/images/mtgcom/authorpics/authorpic_danhelland.jpg)**DOH**—Dan Helland   
**Magic** Design Coordinator   
  
![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_eriklauer.jpg)**EVL**—[Erik Lauer](http://archive.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer)  
 Head Developer ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_gavinverhey.jpg)**GSV**—[Gavin Verhey](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Gavin%20Verhey)  
**Magic** Experience Designer and ReConstructed Columnist ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_ianduke.jpg)**ID**—Ian Duke   
**Magic** Developer   
  
![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_kennagle.jpg)**Ken**—[Ken Nagle](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Ken%20Nagle)  
**Magic** Designer, Lead Designer for *Born of the Gods*![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_maxmccall.jpg)**Max**—[Max McCall](http://archive.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)  
**Magic** Digital Developer ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_markrosewater.jpg)**MR**—[Mark Rosewater](http://archive.wizards.com/magic/magazine/archive.aspx?author=Mark%20Rosewater)  
**Magic**'s Head Designer   
  
![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_samstoddard.jpg)**SPS**—[Sam Stoddard](http://archive.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard)  
 That's a-me ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_tomlapille.jpg)**TML**—[Tom LaPille](http://archive.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)  
**Magic** Developer, Lead Developer for *Born of the Gods*  
  
  
[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pain+Seer)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pain+Seer) KEN 1/21/2013: I've had lots of fun optioning this and its strong motivator to attack.   
 Max 2/6: This guy has places to go and people to see.   
 MR 4/17/13: My, we've come a long way since *Innistrad*.   
 SPS 5/6/13: Jiro dreams of card advantage.   
 TML 5/7/13: Please put that in an LD. 

Done.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Raised+by+Wolves)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raised+by+Wolves) TML 8/3/2012: Cute.   
 TML 9/27/2012: Tweaked for curve.   
 TML 10/5/2012: I like this card for the blue-green bounce Auras thing, but 2/2 green tokens are boars.   
 TML 10/31/2012: Now back to wolves.   
 SPS 11/15/12: Putting this on my opponent's guys is sometimes correct, and a horrible/bizarre play. Only thing I dislike about this card.   
 TML 10/31/2012: Now back to wolves.   
 TML 11/26/2012: Enchant creature you control? Trying something here.   
 TML 11/28/2012: Hoping this can create two wolves.   
 DE 1/3/12: Can't decide if I love or hate this card. I think I love it.   
 Max 1/8: I love it   
 AF 1/28: It exists to be loved, and I love it. Also, it seems really powerful.   
 KEN 2/28/2013: Is green 5-drop heavy on ASPLAYED? I had this, 2x lifegain tribute common, and Stomphowler tribute, and more 5-drops in Sealed, had to cut the 2x lifegainers.   
 TML 3/18/2013: Added GG when the spider lost it.   
 MR 4/17/13: Do we want to move this away from wolves as the impetus for this card is a Roman myth and not a Greek one? 

[As Mark mentioned](http://archive.wizards.com/Magic/magazine/Article.aspx?x=mtg/daily/mm/285), the raised by Wolf myth is primarily known as being a Roman myth, and not Greek, but we deemed it more important to meet expectations rather than be 100% accurate. I do still love when this was making Boars, though. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Charging+Badger)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Charging+Badger) [Playtest name Grumpy Badger]   
 SPS 11/15/12: I will be forever sad if this card name changes.   
 TML 11/26/2012: You will probably be forever sad by the end of editing. :)   
 TML 12/12/2012: SO GRUMPY   
 Max 2/6: I don't get it.   
 TML 2/18/2013: Put Auras on it! 

Sometimes, the hardest part about making cards is giving up on favorite playtest names.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scourge+of+Skola+Vale)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scourge+of+Skola+Vale) GSV 02/08/13: Haumph! 

I would've also accepted Om nom nom nom.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ashiok%27s+Adept)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashiok%27s+Adept) Max 1/8: I am sad to see another black heroic card that punishes me for completing my quest.   
 TML 1/8/2012: It is what black heroic creatures do in *Theros*. This one has been fun enough so far for a relatively throwaway card.   
 Max 2/6: Why is this symmetrical? Reads like downside.   
 ID 2/8/13: Agree. All the black heroic guys are symmetrical so far, and I never want to bother trying to trigger them. I think this would be way more fun as one-sided and a 2/2, for example.   
 TML 2/8/2013: This is just what black heroes do up to this point. Should we reevaluate that?   
 Max 2/18: I think so. I'm actively not interested in targeting this guy.   
 TML 3/4/2013: Moving to 1/3 and each opponent. Hooray for asymmetry. 

 This was a change that happened partway through development of *Theros*. In the original version, all the black heroic was both players, but as we worked on the set, we decided to push [Agent of the Fates](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agent+of+the+Fates) away from both player sacrificing a creature, to only an opponent. At that point, things just kind of fell into place, and the other black heroes were able to change their abilities in the same way. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fate+Unraveler)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Unraveler) AF 1/25: Feels like it wants to make them lose life.   
 TML 1/30/2013: [Kederekt Parasite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) and [Underworld Dreams](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Dreams) both go this way.   
 DB 2/19/2013: Agree w/ AF that this feels like it should be life loss, not damage. [Underworld Dreams](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Dreams) is too old to be precedent and [Kederekt Parasite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) requires a red permanent to deal its damage. Cool card though.   
 DH 3/5: Concur with above about this being life loss even though [Underworld Dreams](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Dreams) doesn't.   
 BM 3/5/13: I like that damage allows interaction with PWs. Life loss used to have benefits in world with COPs, now it's just less useful damage. Life loss is still useful for drawback text (see Plague Demon).   
 TML 3/7/2013: Made it life loss. Any defenders of damage other than Billy?   
 SPS 3/8/13: I will speak for Billy.   
 DOH 4/18/13: Agree with Billy. I like the effective hat tip to Hexmage. We still use [Vicious Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vicious+Hunger) effects anyway.   
 TML 5/3/2013: Damage so it gets Planeswalkers.   
 SPS 5/6/13: I enjoy this change. 

As is often the case, people will often have differing opinions on cards based on aesthetics vs. functionality. This is one where we have been debating as a group for a while about how black's color pie should be evolving over time. Life loss, which used to be better than damage, is now worse due to the interaction with Planeswalkers. On the other hand, we try to make sure that black and red feel different as colors, which necessitates black getting some amount of life loss.

[Fate Unraveler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Unraveler), which was trying to match [Underworld Dreams](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Dreams)'s template, ran into the problem of looking not a lot like a card we would do today. In the end, the upside of interacting with Planeswalkers was seen as more important than this one card feeling different than a red card. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Loyal+Pegasus)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Loyal+Pegasus) KEN 6/19/2012: Now W 2/1 flying attacks in tandem, theorycraft [Ember Beast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ember+Beast) as a white card.   
 SPS 10/1/12: Love this card. I like supporting going wide instead of just tall.   
 ID 10/12: Similar to [War Falcon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Falcon) but cleaner and more reprintable. I like it.   
 AF 1/10: This ability has only ever been red. I feel like this deserves 5 minutes at Cardcrafting.   
 TML 1/16/2013: Cardcrafting approves expansion into white. 

In another example of a card that spurred enough of a discussion to go into Cardcrafting. The result—white gets to do this, now!

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Great+Hart)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Great+Hart) TML 11/9/2012: Pumped up to 2/5 for blue-white.   
 SPS 3/8/13: Take that, [Pillarfield Ox](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox).   
 TML 3/8/2013: Now [Pillarfield Ox](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox). 

The Tom giveth, and the Tom taketh away.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Black+Oak+of+Odunos)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Oak+of+Odunos) TML 11/28/2012: To 2B so you can combine it with other colors' dreamweavers more easily.   
 TML 12/12/2012: Now just B to activate.   
 TML 12/19/2012: Now 0/5 so it doesn't float freely to only inspired players.   
 AF 1/25: Added "untapped."   
 MR 4/18: I don't mind the bleed but this ability is normally in green. Black usually sacrifices creatures while green taps them.   
 TML 4/19/2013: Inspired needs this. 

 In *Born of the Gods*, black and blue were the two main inspired colors and needed a few extra cards to help them take advantage of that fact. In this case, Black Oak's ability isn't what we normally think of as black, but it worked in the context of the set. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Reap+what+is+Sown)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reap+what+is+Sown) KEN 6/12/2012: New card. For GW Heroic growing guys.   
  
  
 New card   
 XGW   
 Instant   
 Put a +1/+1 counter on each of X target creatures.   
  
 SPS 10/1/12: Had heroic in limited. Worked well. Mission accomplished.   
 TML 10/16/2012: Pumped up to get an A.   
  
  
 New card   
 X1GW   
 Instant   
 Put two +1/+1 counters on each of X target creatures.   
  
 Max 2/6: In my head I can't imagine winning games where my opponent casts this mid-combat.   
 ID 2/8/13: This reads strong enough as a sorcery, I think.   
 TML 2/12/2013: New version.   
  
  
 Reap What Is Sown   
 1GW   
 Put a +1/+1 counter on each of up to three target creatures.   
  
 ID 2/18/13: Cool. Like this a lot.   
 TML 4/17/2013: Now up to three instead of any number of. 

  
 As part of the gold cards in the set, [Reap What Is Sown](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reap+What+Is+Sown) went through a few variations, depending on how strong we wanted it to be. We knew we wanted the card to be strong enough to be an "A" (i.e., stronger than a [Wind Drake](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wind+Drake)), but we also wanted to keep it below the level of cards like [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun). The goal was to be an anchor, not to dominate the draft. The second version of the card proved to be pushed too hard, so we pulled back a bit, and ended up with the version you can see today. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Archetype+of+Finality)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Archetype+of+Finality) TML 10/4/2012: Trying static abilities one last time.   
 TML 10/5/2012: Got meaner to numbers.   
 TML 12/12/2012: Now extra ability!   
 GSV 12/17/12: This guy seems brutal and not particularly fun. "All of my creatures trade with all of yours" makes size carry little relevance. It's especially brutal in a block with so many Auras.   
 TML 12/19/2012: Now worse due to being unfun. Was 3BB.   
 ID 2/4/13: Brutal to try to beat this without spot removal. There are also lots of ways to recur enchantments, especially in BW.   
 TML 2/4/2013: To 2/3 from 2/4.   
 KEN 4/2/2013: Had a super awesome game where this trumped my opponent's THS Gorgons that can't kill Gorgons and also lost deathtouch. 

It's important to make sure that when we are pushing cards, we do it on cards that are fun. More than any other of the Archetypes, Finality proved to risk being incredibly unfun in Limited. As a result, we kept increasing the cost and decreasing the toughness until it got to a point where you would still play it, but it wouldn't dominate every game where it was drawn. The card serves the role we wanted it to, and is at the right level of miserable.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swordwise+Centaur)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swordwise+Centaur) KEN 3/27/2013: Power uncreep!   
 TML 4/2/2013: I don't want GG 3/3 common. 

 While [Swordwise Centaur](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swordwise+Centaur) is, in fact, less powerful than [Kalonian Tusker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kalonian+Tusker), we need to balance for Limited, and green common wanted a ![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) vanilla to help out green devotion. We are careful about doing too many "strictly betters" and "strictly worses" but with the number of cards we have to make every year, some of that will just happen. 

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Eye+Gouge)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eye+Gouge) KEN 8/13/2012: Revived this dead FRI flavor removal design.   
 DH 8/29: Lol   
 AF 9/27: :)   
 SPS 10/1/12: God, I love this card.   
 MJG 10/10/12: Hehe!   
 TML 1/10/2012: New template from Tom Jenkot.   
 AF 1/25: Adorable!   
 MR 4/17/13: I am very happy this card found a home later in the block. 

 Often during the design process, there are cards that are wonderful, but just don't make it into sets, as [Eye Gouge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eye+Gouge) was to *Theros*. Luckily, Ken saved this one from the dead, and brought it to *Born of the Gods*. 

  


---

  
 Well, that's it for this week's edition. I hope you enjoyed it. Join me next week as we get ready for Pro Tour *Born of the Gods*. 

Until next time,

 Sam ([@samstod](https://twitter.com/@samstod)) 

[![](https://media.wizards.com/images/magic/daily/footers/BNG/EN_BNG_ArticleFooter_MTGOPre_Details_Static.png)](http://archive.wizards.com/Promo/HerosPath/Default.aspx#)  
  
![](https://media.wizards.com/images/magic/daily/footers/slice1.jpg)![](https://media.wizards.com/images/magic/daily/footers/slice2.jpg)![Sam Stoddard](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_samstoddard.jpg) **Sam Stoddard**[@SamStod](https://twitter.com/SamStod)[Email Sam](/company/emailtoauthor.asp?author=Sam%20Stoddardamp;headline=%5BThe%20M%20Files:%20Born%20of%20the%20Gods%5D "Click to send email to the author.") | [Author Archive](/Magic/Magazine/Archive.aspx?author=Sam%20Stoddard)[Latest Developments Archive](/Magic/Magazine/Archive.aspx?tag=Latest%20Developmentsamp;description=Latest%20Developments) |  
 Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 








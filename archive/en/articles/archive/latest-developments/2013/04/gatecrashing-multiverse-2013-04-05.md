
---
[Link to Wayback Machine](https://web.archive.org/web/20170717220143/http://magic.wizards.com/en/articles/archive/latest-developments/gatecrashing-multiverse-2013-04-05)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "645806"
[_metadata_:publish_date]:- "2013-04-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Gatecrashing the Multiverse"
[_metadata_:wayback_capture_timestamp]:- "2017-07-17 22:01:43"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170717220143id_/http://magic.wizards.com/en/articles/archive/latest-developments/gatecrashing-multiverse-2013-04-05"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/gatecrashing-multiverse-2013-04-05"
---


*Gatecrash*ing the Multiverse
=============================



 Posted in **Latest Developments**
 on April 5, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 







For the last few months, Latest Developments has been handled by a number of different developers working on weekly columns. As of this week, I am taking over as the main author of the column, with others jumping in from time to time when they have something they want to say. I'm very excited for this opportunity and look forward to bringing you a behind-the-scenes look at what happens on the development side of the Pit. If there are things any of you out there reading this would like to see, send me an email and I may be able to put an article together in the future.


With that out of the way, it's time to move on to what the French call " [*content*](http://fr.wiktionary.org/wiki/content#Anglais) ."


Multiverse is the database that R&D uses internally to keep track of the cards in sets. Designers and developers are encourage to go through the database about once a week and leave any comments they may have on cards. Sometimes they discuss power levels, sometimes it's leaving feedback on Limited play, and sometimes they just have a witty comment to leave. These are some of the more interesting comments in *Gatecrash*.


The cast of commentators




![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_aaronforsythe.jpg)
**AF**—[Aaron Forsythe](http://www.wizards.com/magic/magazine/archive.aspx?author=Aaron%20Forsythe)

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_DougBeyer.jpg)**DB**—[Doug Beyer](http://www.wizards.com/magic/magazine/archive.aspx?author=Doug%20Beyer)

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_dellaugel.jpg)**DEL**—Del Laugel



![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_davehumpherys.jpg)**DH**—[Dave Humpherys](http://www.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humpherys)

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_ethanfleischer.jpg)**EEF**—[Ethan Fleischer](http://www.wizards.com/magic/magazine/archive.aspx?author=Ethan%20Fleischer)

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_ErikLauer.jpg)**EVL**—[Erik Lauer](http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer)



![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_gavinverhey.jpg)**GSV**—[Gavin Verhey](http://www.wizards.com/magic/magazine/archive.aspx?author=Gavin%20Verhey)

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_KenNagle.jpg)**KEN**—[Ken Nagle](http://www.wizards.com/magic/magazine/archive.aspx?author=Ken%20Nagle)

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_MarkGottlieb.jpg)**Mago**—[Mark Gottlieb](http://www.wizards.com/magic/magazine/archive.aspx?author=Mark%20Gottlieb)



![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_maxmccall.jpg)**Max**—[Max McCall](http://www.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld218_mons_johnson.jpg)**MJ**—Mons Johnson

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_MarkGlobus.jpg)**MJG**—[Mark Globus](http://www.wizards.com/magic/magazine/archive.aspx?author=Mark%20Globus)



![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_markrosewater.jpg)**MR**—[Mark Rosewater](http://www.wizards.com/magic/magazine/archive.aspx?author=Mark%20Rosewater)

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_tomlapille.jpg)**TML**—[Tom LaPille](http://www.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_zachill.jpg)**ZH**—[Zac Hill](http://www.wizards.com/magic/magazine/archive.aspx?author=Zac%20Hill)


And onto the show:





![Shambleshark](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shambleshark)


 
ZH 10/20: This here is a generous common.  

AF 1/18: Beautiful.  

KEN 2/21/2012: For my CrabFishBeast deck!  

DH 2/22: 2/2 - 2/1 so easier to block and possibly more evolving possible  

Del 6/7: Now with flash.



You'll notice the last change in here was made by our trusty editor, Del Laugel. As the set nears completion, she "owns" the Multiverse file, and is in charge of making the actual changes that Dave Humphreys, as lead developer, wants done in the file. The final addition of flash was to give Simic a little extra oomph in Limited.





![Disciple of the Old Ways](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Disciple+of+the+Old+Ways)


 
Mago 10/11/11: Changed from 3G 3/3, 1R: FS to 1G 2/2, R: FS.  

EVL 12/9: MEOW!  

ZH 2/14: Confused as to why name is not Zan Zan the Clan Man.



Zac is sorely missed if for no other reason than his ability to give appropriate nicknames to cards in development.





![Assault Griffin](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Assault+Griffin)


 
DH 12/6: There is a 3W 2/3 flyer in Hook. Changed to 3/2 for now.  

KEN 12/12/2011: New World Order and simplicity pushes will have us doing this more.  

DH 1/3: Renamed to its repeat [Assault Griffin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Assault+Griffin), hope 'Assault' isn't named 'Assault'.  

DB 1/9/2011: Noted :)



Names can cause confusion internally, from time to time. At the time, battalion was named "assault," so a number of the cards with that ability were just generically called "Assault Whatever." Naming conventions like these can lead to [Assault Griffin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Assault+Griffin) being very confusing in playtests.





![Crocanura](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Crocanura)


 
GSV 1/14: Creative gets a hold of our set file and changes a Spider to an Alligator Frog Beast. Line is like some kind of bizarro world!  

DH 2/6: We need more Alligator Frog Beasts.  

TML 2/8/2012: Agree.



One of the most fun parts of working with *Gatecrash* was watching the Simic Combine's creatures wildy change in creature types—some of which stuck, and some of which changed. Usually, it meant the creature getting a little less silly over time, but not [Crocanura](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crocanura), which evolved from a lowly Spider into an Alligator Frog Beast before finally ending up as a Crocodile Frog, as Alligator isn't a supported creature type in **Magic**. Yet.





![Frontline Medic](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Frontline+Medic)


 
MJG 10/28/11: Cool.  

GSV 12/9: Playing with this card in my Boros draft deck was fun and worked well. Felt like a good rare without being insane, which was nice.  

Del 2/7: Note that this affects creatures that enter the battlefield later in the turn.  

DH 3/9: 3/2 - 3/3  

Del 6/22: Gained an ability.



Gained an ability, indeed. As you can see from the dates, this was a relatively late change. We already had a good idea just how strong [Sphinx's Revelation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation) would be, but [Bonfire of the Damned](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bonfire+of+the+Damned) decks were also making huge waves in the real world. Erik Lauer, as the head of the [FFL](http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/80), wanted to find a card to adjust slightly to put some pressure on all of the powerful X spells in Standard. In the end, it was decided that [Frontline Medic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frontline+Medic) was a card that was already just about good enough for Constructed and could most easily house text that made sense for combating these spells.





![Mystic Genesis](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mystic+Genesis)


 
DH 1/16: Changed to X/X instead of X 1/1s.  

DH 1/18: I hope Simic players like the letter 'X'  

Max 1/20/12: The entire set marks the spot.  

ZH 2/14: Really similar to [Draining Whelk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Draining+Whelk), which is probably cool actually.  

KEN 3/27/2012: Is this supposed to be a creature card doing the same thing?  

Del 4/17: Not after the art has been commissioned, no.



The earliest version of this card created a bunch of tokens, but that didn't play well enough into the Simic themes. Now, the card is able to trigger evolve when a large enough spell is countered, and also happens to work better with populate.





![Nightveil Specter](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nightveil+Specter)


 
Del 5/10: 2/3 - 3/3.  

Del 5/17: 3/3 - 3/2.  

Del 5/31: 3/2 - 2/3.  

MJ 6/7: life is circular...



One of the truisms of R&D is that if you aren't sure which is the correct value for a card, try another and see where it leads you. Sometimes it is back to the original, but at least we knew that we had the card at the place we wanted it to be.






![Treasury Thrull](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Treasury+Thrull)


 
[original name: Orzhov Vaultbeast]  

Max 2/20/12: Misread as 'valuebeast.' Was not disappointed.



Appropriate comment is appropriate.





![Aerial Maneuver](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Aerial+Maneuver)


 
Del 1/24: I had no idea the +1/+1 on [Daring Leap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Daring+Leap) was the blue part of that spell.  

DH 2/1: [Daring Leap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Daring+Leap) now apparently costs a blue less now. Changed to make better.  

TML 2/8/2012: I look forward to ambushing things with this spell.



The original version of this spell only gave the creature flying and first strike, leading to Del's comment. Making better versions of cards is a constant discussion in R&D, but it is something that we have to allow ourselves to do. The game has been around for nearly twenty years now, and trying to always operate within the confines of what exists is too much of a constraint when trying to make fun and exciting formats. Sometimes we do make cards like [Aerial Maneuver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aerial+Maneuver), which totally outclasses [Daring Leap](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Daring+Leap), and sometimes we make worse versions of existing cards. We try and keep all of it to a minimum, but if the right spell for a set is either better or worse than a previously printed **Magic** card, we won't constrain ourselves to trying to not outclass an old card.






![Crowned Ceratok](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Crowned+Ceratok)


 
KEN 9/21/2011: MOAR 'Human Elk Wizard' PLZ



I see you want a Human Elk Wizard. Best I can do is Rhino.





![Skyblinder Staff](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Skyblinder+Staff)


 
[playtest name: Umbrella]  

Mago 10/26/11: New card. Was [Neurok Hoversail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Neurok+Hoversail), but [Cobbled Wings](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cobbled+Wings) was in ISD. Might not be common.  

TML 10/28/2011: ella ella hey hey hey  

EVL 12/11: :-)  

DH 1/10: Changed from protection to can't be blocked by.  

EEF 1/17/12: It loses a lot of its flavor when it loses protection, IMO.  

ZH 2/14: I feel like this is too adorable of a card. When this isn't literally an umbrella, are we going to dig it?



Often when sets are between design and development, mini-teams will convene to take an aspect of the set that needs some work, such as Planeswalker designs, top-down themes, or mechanics that need some fleshing out. For *Gatecrash*, one such mini-team revolved around getting more cards into the set to bring out the "city" feel that was missing. This is where cards like [Bane Alley Broker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bane+Alley+Broker), [Skyblinder Staff](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skyblinder+Staff), and [Glaring Spotlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glaring+Spotlight) came from. Often, these teams produce cards that work on paper, but risk losing their identity once a final name is put on the card.





![Gruul Ragebeast](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gruul+Ragebeast)


 
DH 1/23: Added 'an opponent controls'.  

DH 2/29: Intentionally not optional fwiw.  

Max 3/30/12: THUNDERDOME



Once again, Max shows that he has a knack for concise descriptions.






![Experiment One](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Experiment+One)


 
Del 5/8: Now regenerates.  

Del 5/17: Activation cost from 1G to 2G.  

Del 6/7: Activation cost from 2G to remove a +1/+1 counter.  

Del 6/14: Activation cost from remove one +1/+1 counter to remove two.



Another card with late changes, [Experiment One](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Experiment+One) began as a vanilla 1/1 with evolve, which saw some play in our [Future Future League](http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/80). We found that the unfun part about decks trying to evolve creatures was that you were just so vulnerable to any sort of wraths. We fiddled around with [Experiment One](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Experiment+One)'s version of regeneration, quickly finding that the mana cost wasn't helping, since the decks that wanted to use it were forced to tap out if they wanted to put any pressure on White-Blue Control. Changing the activation to removing a counter was the most fun direction to push the card, but it wasn't quite right. Most of the decks we had with [Experiment One](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Experiment+One) were good at making it a 3/3 or a 4/4, but once you were there, the trick was to cast a creature of equal size to [Experiment One](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Experiment+One), regenerate it, get the evolve counter, then swing. It was fiddly and not the play pattern we wanted out of those decks. We found that moving it to two counters put the card in the spot we were aiming at: one where regeneration helped it survive removal, but not simply dominate combat.






![Giant Adephage](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Giant+Adephage)


 
GSV 1/23: Love it. It's like a [Chronozoa](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chronozoa) for Ken Nagle.



What else really needs to be said?


As a bonus section, below I've listed a number of playtest names. See if you can guess what the final card name ended up as:


Neighborhood Watch -


>> Click to Show

![Hold the Gates](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hold+the+Gates)


Friendly Demon -


>> Click to Show

![Alms Beast](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Alms+Beast)


Last Will and Testament -


>> Click to Show

![Dying Wish](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dying+Wish)


Stick It to the Man -


>> Click to Show

![Homing Lightning](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Homing+Lightning)


The Roof Is on Fire -


>> Click to Show

![Five-Alarm Fire](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Five-Alarm+Fire)


Balm Lightning -


>> Click to Show

![Spark Trooper](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Spark+Trooper)


G-G-G-Ghost! -


>> Click to Show

![Voidwalk](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Voidwalk)


Open the Tombs -


>> Click to Show

![Immortal Servitude](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Immortal+Servitude)


Surprise Me -


>> Click to Show

![Unexpected Results](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Unexpected+Results)


Kickboxing Viashino -


>> Click to Show

![Ghor-Clan Rampager](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ghor-Clan+Rampager)


Good Lieutenant -


>> Click to Show

![Boros Elite](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Boros+Elite)


Street Smarts -


>> Click to Show

![Way of the Thief](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Way+of+the+Thief)


Hurl into the Sun -


>> Click to Show

![Shattering Blow](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shattering+Blow)


Science! -


>> Click to Show

![Urban Evolution](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Urban+Evolution)


I'm Full of Tinier Men -


>> Click to Show

![Murder Investigation](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Murder+Investigation)


Bear Supply -


>> Click to Show

![Ooze Flux](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ooze+Flux)


Draft Board -


>> Click to Show

![Assemble the Legion](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Assemble+the+Legion)


The Joys of Pet Ownership -


>> Click to Show

![Predator's Rapport](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Predator%27s+Rapport)


Zac's Steatopygous Mutant -


>> Click to Show

![Elusive Krasis](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Elusive+Krasis)


Elder Spitemare -


>> Click to Show

![Boros Reckoner](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Boros+Reckoner)


Unexpected Swarm of Weasels -


>> Click to Show

![Merfolk of the Depths](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Merfolk+of+the+Depths)










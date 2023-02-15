
---
[Link to Wayback Machine](https://web.archive.org/web/20210224021345/https://magic.wizards.com/en/articles/archive/latest-developments/cross-block-synergies-theros-2013-10-11)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:description]:- "Pro Tour Theros is right around the corner... and may actually be goingmay actually be going on while you are reading this. Of course, that means that the best pros in the game will be competing against each other for the chance to hoist the trophy, but doing so is going to require that they have pretty good Standard decks. I am looking forward to seeing what they come up"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646096"
[_metadata_:publish_date]:- "2013-10-11"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Cross-Block Synergies in Theros"
[_metadata_:wayback_capture_timestamp]:- "2021-02-24 02:13:45"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210224021345id_/https://magic.wizards.com/en/articles/archive/latest-developments/cross-block-synergies-theros-2013-10-11"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/cross-block-synergies-theros-2013-10-11"
---


Cross-Block Synergies in *Theros*
=================================



 Posted in **Latest Developments**
 on October 11, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 







Pro Tour *Theros* is right around the corner... and [may actually be going](/en/events/coverage/dezani-proclaims-allez-les-bleus-pro-tour)may actually be going on while you are reading this. Of course, that means that the best pros in the game will be competing against each other for the chance to hoist the trophy, but doing so is going to require that they have pretty good Standard decks. I am looking forward to seeing what they come up with, and seeing which *Theros* cards make their debut at the Pro Tour.


One of the most important parts to designing and developing sets today is to create cross-block synergies so the sets within Standard play well with each other, but also so that there is enough of a change when Standard rotates to change things up. A diverse and shifting metagame is a healthy metagame. We are seeing that right now in Standard, where cards such as [Sphinx's Revelation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx%27s+Revelation) remain powerful tools, but at the same time cards like [Elspeth, Sun's Champion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elspeth%2C+Sun%27s+Champion); [Fleecemane Lion](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fleecemane+Lion); and [Nylea, God of the Hunt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nylea%2C+God+of+the+Hunt) are also showing up in force. This blending of the two sets (hopefully) creates a unique metagame that feels different from *Return to Ravnica* Block, *Theros* Block, or *Theros*-Huey Standard. This constant changing of the metagame is one of the things that keeps players coming back to Standard, and something we are interested in preserving. Getting it to work requires some architectural planning on our part, however.




|  |  |
| --- | --- |
| 
Sphinx's Revelation
 | 
Fleecemane Lion
 |

Looking back to some previous years, it is easy to see places where this totally falls apart. Because we were working so hard on getting the decks we wanted to push be good in a block, we ended up with a bunch of "block monsters" that required basically nothing from outside of their own blocks to be Standard-competitive decks. And once you introduced the cards around it, you ended up with the best deck in Standard by a wide margin. The most obvious case of this is Affinity, which played almost nothing from either *Onslaught* or *Champions of Kamigawa* block around it, yet was the strongest deck in Standard between when [Arcbound Ravager](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcbound+Ravager) was printed until nearly the entire deck was banned. While there is no question the block managed to work in-block, there was also nothing that was able to rotate to fix the problem. Also, because of the timeline we work on, the earliest we could put a really powerful hate card into the format was *Saviors of Kamigawa*, far too late to have a real impact.


Another, much more reasonable example is Faeries, which also managed to be one of—if not the—strongest deck for its entire life in Standard after the printing of [Bitterblossom](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bitterblossom). In some amount of contrast to Affinity, however, it did pull cards from the surrounding sets, although the core of the deck was the same that existed in Block—[Bitterblossom](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bitterblossom), [Spellstutter Sprite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spellstutter+Sprite), [Mistbind Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistbind+Clique), [Vendilion Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vendilion+Clique), [Mutavault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault), and [Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command). You might be playing [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation)s and [Ancestral Vision](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Vision)s, or [Agony Warp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agony+Warp)s as support spells, but nothing in the core of the deck rotated. Again, in order to properly fix the metagame, we had to put incredibly powerful hate cards like [Volcanic Fallout](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Fallout) and [Great Sable Stag](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Great+Sable+Stag) in late in the Alara year, which succeeded in needing a [Bitterblossom](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bitterblossom) ban, but didn't improve Standard in the in-between time.




|  |  |
| --- | --- |
| 
Bitterblossom
 | 
Great Sable Stag
 |

The goal of cross-block synergy is not just to prevent these block monsters from occurring, but also to keep space in the metagame open for cards from a new set. For *Theros*, that meant scaling back the enchantment-removal a bit during the *Return to Ravnica* year, so if people wanted to build an enchantment-heavy deck they weren't immediately punished.


In retrospect, one of the most dangerous cards we printed in the *Zendikar* year for the long-term health of standard wasn't actually something like the [fetch lands](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=%5B%22Zendikar%22%5D&type=+%5B%22Land%22%5D&text=+%5Bsearch%5D+%5Blibrary%5D), [Lotus Cobra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotus+Cobra), or [Goblin Guide](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Guide)—it was [Tuktuk Scrapper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tuktuk+Scrapper). While that may seem silly now, when we put the card into *Worldwake*, we didn't know exactly how *Scars of Mirrodin* would unfold, and if it was even close to as artifact-dense as the original *Mirrodin*, then that single card could've had a big hand at pushing out the entire year.



![Tuktuk Scrapper](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tuktuk+Scrapper)

 

Of course, that card ended up not being a whole lot next to [Stoneforge Mystic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stoneforge+Mystic) and [Jace, the Mind Sculptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+the+Mind+Sculptor), but one of the easiest ways to ensure that the metagame stagnates is to give a deck from the previous year too many tools to deal with what is coming the next year. In this case, if the Allies deck is very strong, then running artifacts is going to be a pretty big detriment. And even if it's not, this card alone in multiples could simply destroy an artifact-heavy opponent. Obviously, the direction the *Scars of Mirrodin* year took was more than different enough to keep that from being an issue, but that is the kind of mistake we actively try to avoid today. We're always going to be wrong on the individual power levels of specific cards, but we can make sure that the structure of what we are doing is correct.


### Seeding *Theros* Themes


By the time we are creating the seed cards for the next year, we rarely have a good grasp on what those decks could look like—the set is still in early design, after all. Instead, we work on seeding the themes for the next year. This gives us a solid foothold when we begin developing the set for Constructed, and hopefully gives us enough room that we can build fun and interesting cards and archetypes that don't require everything from the current year. These can be pretty blatant, like [Steel Overseer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steel+Overseer) in **Magic** 2011 or [Farseek](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Farseek) in **Magic** 2013. It can also be a lot more subtle, like [Grim Lavamancer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grim+Lavamancer) or [Visions of Beyond](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Visions+of+Beyond) in **Magic** 2012. Some of these will hit, some will miss, and sometimes the direction of the set doesn't quite line up with the seed cards, but that's okay. Their placement is what is most important. Having something that can rotate us lets us take some risks with the power level of a set and still be fairly sure that we won't have to power up the next set to make it relevant in Standard.


**Enchantments**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld268_enchantments.jpg)*[Sphere of Safety](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphere+of+Safety), [Ethereal Armor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ethereal+Armor), [Ajani's Chosen](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani%27s+Chosen), [Oath of the Ancient Wood](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oath+of+the+Ancient+Wood)*
 

Many people over the previous year successfully guessed that *Theros* would have a strong enchantment theme because we had seeded a few enchantment cards the year before. While the original Ravnica did also have a minor enhancement theme, we wanted to keep it to a minimum this time as to not do *Theros* before *Theros*.


While the direction of enchantments in *Theros* is much more related to bestow and the Gods, I think there is still a place for some of these cards. Plus, there are still two sets in the *Theros* block, which leaves plenty of room for these cards to show up.


**Devotion**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld268_devotion.jpg)*[Boros Reckoner](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Reckoner), [Burning-Tree Emissary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning-Tree+Emissary), [Kalonian Tusker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kalonian+Tusker), [Dark Prophecy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Prophecy), [Awaken the Ancient](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Awaken+the+Ancient)*
 

Devotion was the seed that was hiding in plain sight, and one that I think would've been basically impossible for people to pick up on. While it may seem odd that we went from a multicolor block right into one that has some rewards for having a lot of permanents with many mana symbols, it let us do it in one of the most creative ways possible—with hybrids.


The nice thing about a card like [Boros Reckoner](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Reckoner) is that it gets to pull triple duty, allowing you to run either Purphoros or Heliod in mono-white, mono-red, or red-white strategies. Not only that, but it nearly activates the Gods by itself. While you shouldn't expect to see a lack of color mana symbols this year or next, the number of triple-symbols is usually very low. Hybrid wasn't put into *Return to Ravnica* block to support *Theros*, but it's inclusion let us push devotion to a level that I believe is very fun in Standard, but one that shouldn't be too damaging for next year if it is too strong.


**Heroic**


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld268_heroic.jpg)*[Unflinching Courage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unflinching+Courage), [Ethereal Armor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ethereal+Armor), [Hidden Strings](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hidden+Strings), [Selesnya Charm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Selesnya+Charm)*
 

Heroic is probably one of the more fringe strategies for Standard, but it is one that could easily show up. While piling up lots of enchantments or pump spells on a single creature is historically a recipe for disaster, we have put some cards like [Gods Willing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gods+Willing) into *Theros* to make sure the heroic deck has some play. And let's face it, casting an [Unflinching Courage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unflinching+Courage) on a [Fabled Hero](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fabled+Hero) tends to swing games pretty quickly. Add a [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) on turn four, and that is just about lethal.


### Allowing Future Themes to Thrive


Just as important as supporting the year ahead with cards is making sure that we give the year the room to survive, like what I mentioned earlier about [Tuktuk Scrapper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tuktuk+Scrapper). Printing a card like [Ancient Grudge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancient+Grudge) in *Innistrad* helped us to ensure that *Scars of Mirrodin* block (or at least the artifacts of *Mirrodin*) won't be totally dominant the following year. Printing it the year before *Scars of Mirrodin* would be just asking for nothing in *Scars of Mirrodin* block to have a chance.


To that point, we did leave some stuff out of *Return to Ravnica* block when seeding for *Theros*. Several people sent me irritated messages that [Mortify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify) wasn't in *Gatecrash* or *Dragon's Maze*, and this is why—because we didn't know exactly how *Theros* would play out, we wanted to make sure to not risk too much. A card like [Wear & Tear](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wear+%26+Tear) works because it isn't easy to main deck it, while [Mortify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify) is rarely going to be dead and poses very little risk as a main-deck card. Also, much like how [Shatter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shatter), [Oxidize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oxidize), and [Viridian Shaman](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viridian+Shaman) saw a lot of play during *Mirrodin* Standard, we wanted to leave the door open for a more interesting suite of enchantment removal spells like [Destructive Revelry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Destructive+Revelry) to see play. The best way to do that was to leave those cards for *Theros* block.


So, how good a job did we do? That remains to be seen, but I have faith that *Theros* will make a huge impact on Standard. We are coming out of one of the most diverse Standard metagames we have ever produced with the *Innistrad*-*Return to Ravnica* year, and I look forward to another year of varied decks and interesting metagame changes to come.


Sam  
[@samstod](https://twitter.com/@samstod)










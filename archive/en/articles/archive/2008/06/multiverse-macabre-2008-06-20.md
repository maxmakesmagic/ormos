
---
[Link to Wayback Machine](https://web.archive.org/web/20220819141830/https://magic.wizards.com/en/articles/archive/multiverse-macabre-2008-06-20)

[_metadata_:author]:- "Devin Low"
[_metadata_:description]:- "Magic developers are responsible for improving and refining a set's identity, structure, and mechanics on a global, set-wide scale. But if you zoom in closer, Magic Developers also spend a lot of time fixing and improving individual abilities on individual cards. I've written about a lot of large-scale, macrocosmic topics in Shadowmoor development, so today I'm zooming in to a"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "311296"
[_metadata_:publish_date]:- "2008-06-20"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Multiverse Macabre"
[_metadata_:wayback_capture_timestamp]:- "2022-08-19 14:18:30"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220819141830id_/https://magic.wizards.com/en/articles/archive/multiverse-macabre-2008-06-20"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/multiverse-macabre-2008-06-20"
---


Multiverse Macabre
==================



 Posted in [NEWS](/en/articles)
 on June 20, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DevinLow.jpg)
By Devin Low











Magic developers are responsible for improving and refining a set's identity, structure, and mechanics on a global, set-wide scale. But if you zoom in closer, *Magic* Developers also spend a lot of time fixing and improving individual abilities on individual cards. I've written about a lot of large-scale, macrocosmic topics in *Shadowmoor* development, so today I'm zooming in to a microcosmic topic: guiding you through the changes and challenges of an individual *Shadowmoor* card.



Since we update our sets in a top-secret database called "Multiverse," we have a record of all the changes a card traversed, and all the comments designers and developers made on the card along the way. Ironically, a set's development team members are the least likely to type in comments for their own set. After all, they can just convey their suggestions and complaints in the development meetings in person. The Multiverse comments are primarily used for people not on the team to communicate their feedback to the development team, and for the set's lead developer to convey the development team's response to that feedback.


The *Shadowmoor* development team was the crew reading these comments and using the feedback to make changes. The team was Aaron Forsythe (lead), Doug Beyer, Alexis Janson, Devin Low, Matt Place, and Steve Warner (with contributions from Mark Gottlieb and Jake Theis).


Here are some key characters from the Multiverse comments, featuring both new-blood Great Designer Search participants Alexis, Ken, and Noah and hardcore fulltime developers Aaron, Mons, Matt, and Mike:


AF: Aaron "Iron Man" Forsythe  

AJ: Alexis "Wonder Woman" Janson  

KEN: Ken "Daredevil" Nagle  

MJ: Mons "Wolverine" Johnson  

MP: Matt "The Mighty Thor" Place  

MT: Mike "The Punisher" Turian  

NW: Noah "Wildcat" Weil


### Cremator Gets Cremated


![](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/dl42_faerie.jpg)


This faerie was born fifteen months ago on March 22, 2007, as a very different card:




> 
> CB11\_JEL  
> 
> Cremator  
> 
> 2B  
> 
> Creature - Elemental  
> 
> 2/2  
> 
> B, Sacrifice CARDNAME: Remove target card in a graveyard from the game.
> 



The development comments field was already active:



> 
> KEN 3/22: New card, Cremate man to snag Persist guys. Martyr of Bones is a good fit here!  
> 
> KEN 4/2: 2/2 ->; 2/1 Flying. I personally feel Sac: RFG target card in a graveyard should be a 'freebie' ability, and we don't charge a mana or even half a mana for it. We need more Cremate-like interactions in Constructed! Players get away with too many goodies in their graveyard! We print ways to disrupt all other zones, and we also print a graveyard-active card or more in every set, too.  
> 
> NW 5/3: A question of how defeatable persist wants to be. Since black already has curse I personally have no problem with this guy having mana activation.  
> 
> AF 6/4: If DOU has a similar card, this one will go away.  
> 
> KEN 6/6/2007: I'd like no mana to Cremate here, losing my 2/1 flyer after somehow killing your Persist guy is a big enough decision and hoop in my mind. The first Crypt Creeper was barely Constructed playable and he was good at his shtick.  
> 
> AJ 6/06: On one hand I like cards that hose graveyard cheats as side effects- players shouldn't have a free pass on recursion tricks. On the other hand, these cards make players stop and think about things that will end up being irrelevant 95% of the time- when this guy dies and I have B up, I feel obligated to study your graveyard and try to figure out which creature or spell you are most likely to want in there at some future point in time. Seems like a lot of mental energy wasted. Perhaps that's ok as one of those "0.1% edges" that better players will exploit. It's not an inordinate amount of time, it just feels like more effort than it's worth when it happens.  
> 
> AF 6/25: Now free to activate.  
> 
> AF 7/14: Discard instead of sac to distance from [Heap Doll].  
> 
> MT 8/1: I think the set could use a little more graveyard hate. I saw this guy and nothing else.
> 



Here's the version of the card at this point in development:



> 
> CB11\_JEL  
> 
> Cremator (#2)  
> 
> 2B  
> 
> Creature - Faerie  
> 
> 2/1  
> 
> Flying  
> 
> Discard CARDNAME: Remove target card in a graveyard from the game.
> 


Many reasons combined to lead us to move "Cremator" from "Sacrifice me: ~" to "Discard me: ~" Certainly the big similarity to [Heap Doll](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heap+Doll) is one of them, although we could also have just changed [Heap Doll](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heap+Doll).


![Heap Doll](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Heap%20Doll&options=)

The big graveyard mechanic in *Shadowmoor* is persist, and Cremator was originally intended to be an anti-persist weapon. But the "Sac me: ~" version of Cremator doesn't play very well against persist at all. Say the 3/3 vanilla persist creature [Gravelgill Axeshark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravelgill+Axeshark) went to your opponent's graveyard, and you had Cremator with "Sacrifice CARDNAME: Remove target card in a graveyard from the game" on the table. Would it be worth it to you to sacrifice your 2/1 flying Cremator just to RFG the enemy [Gravelgill Axeshark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravelgill+Axeshark) before it persisted back as a vanilla ground 2/2? Probably not.


[Heap Doll](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heap+Doll) is a better fit for the "Sac me: RFG target card in a graveyard" ability because players will more often be willing to sacrifice their one-mana 1/1 [Heap Doll](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heap+Doll) to prevent a persist creature from coming back, rather than sacrifice a 2/1 flier for which they already paid three mana.


With [Heap Doll](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heap+Doll) already in place, the Development team expanded their focus for the Cremator anti-graveyard slot. Changing Cremator from "Sacrifice me: ~" to "Discard me: ~" would move it from a Limited-format graveyard hoser to a Constructed-viable one. After all, the "Discard me: ~" version would cost zero mana to achieve the effect, whereas the "Sacrifice me: ~" version costs three mana. Beyond improving the card for Standard, bringing the total cost to use Cremator down to zero mana also gave the card a good shot to be useful in Constructed formats beyond Standard. In Extended and Eternal formats, you can't afford to pay three mana for a graveyard hoser, but you can afford to pay zero.


In addition, the "Discard me: ~" version would always be a surprise. Few Constructed opponents would try to play [Makeshift Mannequin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makeshift+Mannequin) if you had a "Sac me: ~" Cremator on the board. They would just find a way to kill Cremator, then cast [Makeshift Mannequin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makeshift+Mannequin) when it was safe. But tons of opponents would try to cast [Makeshift Mannequin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makeshift+Mannequin) or [Dread Return](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dread+Return) if you had "Discard me: ~" Cremator secretly in your hand, allowing to have you discard Cremator to fizzle the [Makeshift Mannequin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makeshift+Mannequin) or [Dread Return](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dread+Return) for zero mana.



> 
> KEN 8/13: I like this nice Spikey common. This guy is a zero mana nonDuress-able hose to a turn 0 Kiki-Jiki Flash kill. A bit late to the party, but he's here!  
> 
> MJ 8/15: this very narrow & powerful sideboard card could show up in ANY format, so it should be given a little extra love on the art/FT/etc.
> 


These comments show people outside the development team noticing that the new Cremator could be a contender in all kinds of old formats, as well as Standard. Zero mana is priced to move!



> 
> sw 8/20: The number of times I have thought this was an in play sac ability has been huge. Is it going to read discard <cardname> from your hand : Remove target card in a graveyard from the game.?  
> 
> KEN 8/22: Could it be 'Discard or sacrifice CARDNAME:'?  
> 
> AF 7/28: Are we obligated to have an annoying "Channel" conversation again?  
> 
> Del 8/30: I see no reason to have it for this card.  
> 
> Del 8/30: You could have two separate abilities, but there's no way that the same ability is going to function in multiple zones.  
> 
> Del 10/2: 2B -> 1BB, 2/1 -> 2/2. Activation cost changed from "Discard CN" to "Pay 1 life."  
> 
> Del 10/2: Card has changed to the other variety of Channel. (Mindslaver kills you, but it does that with lots of cards.)
> 




|  |  |
| --- | --- |
| 
 Arashi, the Sky Asunder
 | 
Channel
 |

Oh noes! Despite all the merits of "Discard me: Remove target card in a graveyard from the game," Cremator now changed to move in a new, third direction. It became this:



> 
> CB11\_JEL  
> 
> Cremator (#3)  
> 
> 1BB  
> 
> Creature - Faerie Rogue  
> 
> 2/2  
> 
> Flying  
> 
> Pay 1 life: Remove target card in a graveyard from the game.
> 


![Gravelgill Axeshark](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Gravelgill%20Axeshark&options=)The reasoning was that a common graveyard-hoser in a set full of persist...should focus on nailing persist! Just like you wouldn't want to sacrifice your 2/1 flying Cremator to stop an enemy [Gravelgill Axeshark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravelgill+Axeshark) from persisting back as a 2/2, you wouldn't often want to discard your 2/1 flying Cremator to stop an enemy [Gravelgill Axeshark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravelgill+Axeshark) from persisting back as a 2/2.


This third version of Cremator was actually phenomenal at stopping persist in *Shadowmoor* Limited. It stays on the board, flies overhead for 2 damage a turn, and whenever that pesky enemy [Gravelgill Axeshark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravelgill+Axeshark) tries to persist, you just pay 1 life and remove the offending Axeshark from the game, without losing any cards yourself.



> 
> KEN 10/4: I see this as a Tarmogoyf hose, but black has Shriekmaw and Extended Dredge can kill on turn 2.  
> 
> Del 10/9: Dev has requested that "Discard CARDNAME: Remove up to two target cards in graveyards from the game." replace the ability above  
> 
> Del 10/9: Dev change is waiting on a templating discussion.  
> 
> Del 10/9: We've never had an effect that removed multiple, specific cards from multiple graveyards at once. My guess is that the template is just confusing enough that the clarity of "in a single graveyard" was worth the loss of functionality. Confirm that it's worth it here?  
> 
> Del 10/10: I'm doing it. Enough templates have been tweaked for 2HG that this doesn't seem as odd as it once would have.  
> 
> Del 10/10: I put in the change. Activation cost was "Pay 1 life" and the ability was active in play.
> 


Yes! Personally, I liked the "Discard me: Remove target card in a graveyard from the game." version best of all. *Magic* has a long history of powerful graveyard mechanics. Since most spells can't affect the graveyard, it's important to make cards that can provide interactivity against graveyard shenanigans. And instant-speed surprises are among the best ways to promote interactivity.


Similar arguments carried the day in development meetings, and the team decided to move back to Cremator #2, a 2B 2/1 flier with "Discard me: Remove target card in a graveyard from the game." (By this time, the card had also received its final name: [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre).) But the team only agreed to move back to the "Discard me: ~" version under one condition: that we make the card more powerful. Since we wanted some Constructed potential here, we decided to give the card a little more gas in the tank.


First, that meant bringing [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) up from the 2B 2/1 flying of "Cremator #2" to 1BB 2/2 flying. Second, that meant making its discard ability more powerful, discarding from your hand for zero mana to remove two cards from graveyards instead of one.


![Reveillark](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Reveillark&options=) Based on our internal Future Future League results and our data from real world Standard up through *Future Sight*, what were the powerful graveyard strategies available in Standard? Some of the most prominent included [Makeshift Mannequin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Makeshift+Mannequin), [Reveillark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark), [Tarmogoyf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf), [Epochrasite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Epochrasite), [Mystical Teachings](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Teachings), [Dread Return](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dread+Return), [Torrent of Souls](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torrent+of+Souls), and persist.


Against [Reveillark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark), removing two cards from the game is much more useful than removing just one, since you can remove both Reveillark targets at the same time in response to [Reveillark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark)'s trigger. [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) is especially useful against [Reveillark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark) in decks that can tutor for one or two copies of the Faerie Rogue when they need her, using something like [Primal Command](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Command), [Beseech the Queen](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beseech+the+Queen), [Liliana Vess](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana+Vess), or [Teferi, Mage of Zhalfir](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teferi%2C+Mage+of+Zhalfir) + [Mystical Teachings](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Teachings). Those decks can fetch [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) when a [Reveillark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark) trigger is imminent, without as much chance of drawing [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) when [Reveillark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark) is not on the board.


While [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) isn't specialized for killing [Tarmogoyf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)s, if you have [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) in your deck to fight other graveyard strategies, in a pinch you can discard [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) during combat to remove two cards in graveyards from the game. If you remove [Nameless Inversion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nameless+Inversion) and [Thoughtseize](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtseize) for example, leaving [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) and other creature cards in graveyards, you can shrink all the [Tarmogoyf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)s by up to -3/-3 so that whatever you have in combat can suddenly kill the enemy [Tarmogoyf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)s without spending any mana.


That brought us to the final version of "Cremator" you see in packs today:




> 
> CB11\_JEL  
> 
> Faerie Macabre  
> 
> 1BB  
> 
> Creature - Faerie Rogue  
> 
> 2/2  
> 
> Flying  
> 
> Discard CARDNAME: Remove up to two target cards in graveyards from the game.
> 





 ![Faerie Macabre](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Faerie%20Macabre&options=)


One more benefit of the "Discard me: ~" version over the two "Activate me while I'm in play" versions is that the final [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) can be used as an anti-graveyard weapon in any deck, not just black decks, since you never need to have black mana to use it.


It's always interesting to see our development meeting theories play out in the real world, so it was fun to see Marijn Lybaert earning thousands of dollars in the Top 8 of last month's Standard-format [Pro Tour–Hollywood](http://archive.wizards.com/Magic/Magazine/Events.aspx?x=mtgevent/pthol08/welcome) partially because he had one [Faerie Macabre](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faerie+Macabre) in the sideboard of his red-green mana ramp deck to tutor up with [Primal Command](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Command) against [Reveillark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark) decks.


### Previous Poll




|  |
| --- |
| **Which red *Shadowmoor* card from Day 2 of Pro Tour–Hollywood will have the biggest long-term impact on Standard?**  |
| [Firespout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout) | 3288 | 26.7% |
| [Flame Javelin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Javelin) | 3054 | 24.8% |
| [Vexing Shusher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vexing+Shusher) | 1682 | 13.7% |
| [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) | 708 | 5.8% |
| [Fulminator Mage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fulminator+Mage) | 658 | 5.4% |
| [Tattermunge Maniac](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tattermunge+Maniac) | 613 | 5.0% |
| [Demigod of Revenge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demigod+of+Revenge) | 580 | 4.7% |
| [Everlasting Torment](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Everlasting+Torment) | 446 | 3.6% |
| [Boggart Ram-Gang](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boggart+Ram-Gang) | 438 | 3.6% |
| [Guttural Response](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Guttural+Response) | 319 | 2.6% |
| [Furystoke Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furystoke+Giant) | 227 | 1.8% |
| [Deus of Calamity](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deus+of+Calamity) | 111 | 0.9% |
| [Ashenmoor Gouger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashenmoor+Gouger) | 102 | 0.8% |
| [Smash to Smithereens](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smash+to+Smithereens) | 44 | 0.4% |
| [Intimidator Initiate](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Intimidator+Initiate) | 22 | 0.2% |
| **Total** | **12292** | **100.0%** |

Even with fifteen options, [Firespout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout) and [Flame Javelin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Javelin) each pulled about a quarter of the votes. In many Standards of the past, the lower mana cost of [Pyroclasm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyroclasm) would make it a more important sweeper than [Firespout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout). But in modern-day Standard, [Firespout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout) usually get the nod because so many key creatures boast 3 toughness, from [Wren's Run Vanquisher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wren%27s+Run+Vanquisher), to some combination of two [Lord of Atlantis](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+Atlantis) and/or [Merrow Reejerey](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merrow+Reejerey), to [Reveillark](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark), to a lot of [Tarmogoyf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)s. [Firespout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout) also allows red-green decks to sweep the ground without killing their own [Birds of Paradise](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise), sweep the air without killing their own ground troops, or just sweep everything away.


It will be interesting to see which cards on this list change places as the post-*Shadowmoor* metagame continues to develop.









---
[Link to Wayback Machine](https://web.archive.org/web/20201112003216/https://magic.wizards.com/en/articles/archive/latest-developments/developing-eternal-formats-2013-10-18)

[_metadata_:author]:- "Sam Stoddard"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "646106"
[_metadata_:publish_date]:- "2013-10-18"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing for Eternal Formats"
[_metadata_:wayback_capture_timestamp]:- "2020-11-12 00:32:16"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201112003216id_/https://magic.wizards.com/en/articles/archive/latest-developments/developing-eternal-formats-2013-10-18"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/developing-eternal-formats-2013-10-18"
---


Developing for Eternal Formats
==============================



 Posted in **Latest Developments**
 on October 18, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_samstoddard.jpg)
By Sam Stoddard




Sam Stoddard came to Wizards of the Coast as an intern in May 2012. He is currently a game designer working on final design and development for Magic: The Gathering.
 







If you have been following [the new *Commander* (2013 Edition) previews](https://www.wizards.com/Magic/tcg/article.aspx?x=mtg/tcg/commander2013/cig#), you may have seen a few cards that just might make an impact in Legacy or Vintage, namely Restore and True-Name Nemesis, but I have one more that I want to talk about today. While this card may not totally replace cards like [Swords to Plowshares](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swords+to+Plowshares) in the format, it certainly makes a good case for times when you might think twice about that StP. One of the awesome things that we have managed to accomplish in Standard over the past few years is to create answers that go up and down in value dependent on the metagame, getting to the point where people have interesting and important choices on how many [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade)s vs. [Hero's Downfall](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hero%27s+Downfall)s to run, as an example. I think that we have created a card that will do that with [Swords to Plowshares](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swords+to+Plowshares), or maybe more cards than even that. 


But, I'm getting ahead of myself. Let me present Unexpectedly Absent:




![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/cmd13/OW0TIk0s5j_EN.jpg)  
 Just a quick rules aside, to get it out of the way—X can be zero. If it is, then the card is put on top of your opponent's library. While this isn't nearly as good as [Swords to Plowshares](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swords+to+Plowshares) in most situations when dealing with creatures like [Tarmogoyf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf) or [Delver of Secrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Delver%2Bof%2BSecrets), it does have an advantage: you can't [Swords to Plowshares](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swords+to+Plowshares) a [Jace, the Mind Sculptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+the+Mind+Sculptor). [Batterskull](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Batterskull)'s token can easily be killed, but the 'skull itself has been immune from most of the same removal... until now. This kind of diversity makes the card an interesting choice, especially since it is hard to make an argument for cards like [Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant) in the main deck. Unexpectedly Absent may not be better than a large number of cards in every situation, but often in Legacy being the second best in a dozen different situations can be better than the best in just one. 




|  |  |
| --- | --- |
| Jace, the Mind Sculptor | Batterskull |

 While keeping a person off of a card for a few turns requires a hefty commitment of mana, it's easier to get much more by using one of the key factors of Legacy against your opponent—all of the shuffling. Because of the [fetch land](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&type=+%5B%22Land%22%5D&text=+%5Bsearch%5D+%5Blibrary%5D&set=%7C%5B%22Zendikar%22%5D%7C%5B%22Onslaught%22%5D)/[dual land](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&type=+%5B%22Land%22%5D&set=+%5B%22Limited+Edition+Beta%22%5D&rarity=+%5BR%5D) mana base, as well as cards like [Stoneforge Mystic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stoneforge+Mystic), people are often shuffling their library. Putting a [Jace, the Mind Sculptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+the+Mind+Sculptor) on top of an opponent's library in response to a [fetch land](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&type=+%5B%22Land%22%5D&text=+%5Bsearch%5D+%5Blibrary%5D&set=%7C%5B%22Zendikar%22%5D%7C%5B%22Onslaught%22%5D) will force the opponent to shuffle him back into the library. Putting a [Tarmogoyf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf) on top of an opponent's library in the upkeep can not only force the opponent to redraw it, but keeps his or her [Delver of Secrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Delver%2Bof%2BSecrets) from flipping for one more turn. Or, you can respond to a [Shardless Agent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shardless+Agent) and either put a card on the bottom of its owner's library or control exactly what card he or she will be getting. It's this kind of diversity that sets the card up to be a real player in the format. 



### Why We Print Cards for Eternal Formats


 With [the first Commander decks](http://www.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/commander/productinfo) released in 2011, we printed cards that impacted Legacy like [Scavenging Ooze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scavenging+Ooze); [Flusterstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flusterstorm); and [Edric, Spymaster of Trest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Edric%2C+Spymaster+of+Trest). Similarly, *Planechase* (2012 Edition) gave those formats both [Baleful Strix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baleful+Strix) and [Shardless Agent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shardless+Agent), which have seen a lot of Legacy play recently. These cards weren't an accident—we printed them (and a few others) with the hope that they would appear in eternal formats and have been generally happy with the results. While we don't put nearly as much effort into controlling or guiding eternal formats, we do want to make sure there are enough cards printed for them each year that the formats don't stagnate too much. One of the draws of the formats is that your deck can be legal and competitive for... well, decades, I suppose... but if nothing changes at all, then the appeal will fade. 




|  |  |
| --- | --- |
| Baleful Strix | Shardless Agent |

 Eternal formats, namely Vintage and Legacy, are very hard to print cards for—we're just going up against twenty years of history, and the first few years of that included some pretty wildly powerful cards. As it turns out, the most fruitful area for us to print cards for Standard-legal sets if we want to impact Legacy is in the form of creatures. As I wrote a few weeks ago in [my article on power creep](/en/articles/archive/latest-developments/dealing-power-creep-2013-08-09), we have spent the last few years trying to normalize the power level of spells and creatures in Standard, which has led to us printing some very powerful creatures for eternal formats. But it also means that aiming spells for these eternal formats is pretty hard. 


 Getting a counterspell into these formats, for instance, is pretty much impossible. Once every few years we can find a card like [Spell Pierce](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spell+Pierce) that is better than many other cards in most situations; going up against [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will), [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell), [Daze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Daze), and even [Stifle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stifle) is no easy task. Most counterspells that could compete against these would just be too powerful to print in Standard because of Standard or Modern. While we often find cards that fill up small niches in the format—better [Wish](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+%5BWish%5D&type=%7C%5B%22Instant%22%5D%7C%5B%22Sorcery%22%5D&text=+%5Boutside%5D) targets, slightly better answers, etc.—it is rare that we can print cards that can really shift the metagame. Looking back at *Return to Ravnica* Block, the card with the largest impact on Legacy was [Deathrite Shaman](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deathrite+Shaman), with a few other cards like [Abrupt Decay](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Abrupt+Decay) and [Izzet Charm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Izzet+Charm) showing up as support cards in a few decks now and then. 




|  |  |
| --- | --- |
| Spell Pierce | Deathrite Shaman |

 One of our goals, though, is to keep printing cards that are fun and interesting in these formats, and sets like *Commander* (2013 Edition) let us find the right balance. Looking back at my preview card—if we put Unexpectedly Absent into Standard, it would be one of the strongest cards in the format because we try not to print much very cheap and unconditional removal. We don't have nearly the same amount of shuffling in Standard to really make the card pop, but I have no doubts that it would be borderline oppressive in the format. Looking at its position in the actual Commander format, though, is much different. Here it is powerful, but just as any one-for-one removal spell, it's not going to shake up the format like many of the other cards in this set. 


 Finding that balance is one of the most interesting parts of this product—after all, the target audience is for Commander. We don't want to put in cards that are only good in Legacy, so we need to find interesting places for the cards where players will play them in both formats. The majority of very powerful cards in Commander are expensive, because the format is relatively slow and has a lot of acceleration, but that doesn't mean there isn't room for low-drop spells. Also, two-for-one card advantage isn't a bad thing, but with four or more players in a game, it's often far more important to swing for the fences than nickel or dime people. While a card like [Day of Judgment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment) can be a three-for-two or four-for-one in Standard, it will often be a sixteen-for-one in Commander. Instead of focusing these cards on raw card advantage, then, we wanted to make them provide something else—doing things that are powerful in Commander, but can also be powerful in Legacy. 


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/rgf7a2tn1d.jpg) Unexpectedly Absent | Art by [Min Yum](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Min%20Yum%22%5D)



 For a card like Unexpectedly Absent, that means putting a card on top of the library is actually a better match than simply exiling it, since "tucking" an opponent's commander is one of the best ways of dealing with it on a semi-permanent basis. True-Name Nemesis is very powerful in one-on-one, but in multiplayer it instead provides an interesting political angle. Restore is an acceleration spell or [Wasteland](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wasteland) recursion in Legacy, but it can also let you use one of your opponents' lands against him or her in Commander, or return something like [Gaea's Cradle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Cradle) to the battlefield. Finding spots where these cards play both roles was important to us and lets us design and develop these cards in a much more natural way than if we were just looking for powerful cards we could print in Legacy and trying to shoehorn them into a Commander product. 


 As a fan of the Legacy format, I am very excited to see what these cards are able to do to the format. I don't expect any of them to have the earth-shattering impact on the format that a card like [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage) had, but I do expect them to give several decks some interesting new options. Any time we can add cards like this to Legacy, I think we have a great opportunity to keep the most popular eternal format on its toes, and I think that has a lot of benefits for its players. 


Until next week,  
 Sam ([@samstod](https://twitter.com/@samstod)) 















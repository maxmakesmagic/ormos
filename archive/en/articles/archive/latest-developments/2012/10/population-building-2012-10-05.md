
---
[Link to Wayback Machine](https://web.archive.org/web/20170412192613/http://magic.wizards.com/en/articles/archive/latest-developments/population-building-2012-10-05)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "&#13;"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "645496"
[_metadata_:publish_date]:- "2012-10-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Population Building"
[_metadata_:wayback_capture_timestamp]:- "2017-04-12 19:26:13"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170412192613id_/http://magic.wizards.com/en/articles/archive/latest-developments/population-building-2012-10-05"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/population-building-2012-10-05"
---


Population Building
===================



 Posted in **Latest Developments**
 on October 5, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







One of the least-understood distinctions in **Magic** R&D is the distinction between design and development. I'm not sure I even understood it that well for a good few years when I started working here. Both roles involve making cards and tweaking environments. If you had forced me two years ago to put a fine point on the difference, I'm not sure I would have done a great job. After leading a few sets through development, though, I think I understand how it works. Now, I would say that it is design's job to come up with a vision for how a card set should work and get as close as possible to having it actually work that way. It's development's job to make sure the design team's idea is cool, then get it the rest of the way.


A good design makes a statement about the strategies that it wants different colors and color pairs to use. Those strategies can be placed on a continuum that goes from "completely natural and emergent from things **Magic** cards normally do" to "wild new thing that **Magic** has never done before."


Executing on the first kind of strategy tends to be a simple affair. For example, ***Magic** 2013*'s red-white deck was intended to be a strategy that went wide with tokens and used mass creature-pumping effects. [Captain's Call](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captain%27s+Call) and [Crusader of Odric](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crusader+of+Odric) were already in the set to support the mono-white strategy and [Krenko's Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krenko%27s+Command) already existed to support the mono-red Goblin strategy, so it's fairly trivial to put [Trumpet Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trumpet+Blast) in and get most of the way there. Part of this is because the stated strategy does not depend on a new kind of effect we've never made before, and part of this is because we have a strong understanding of how such a deck needs to work.




|  |  |
| --- | --- |
| 
Captain's Call
 | 
Krenko's Command
 |

Executing on the other kind of strategy is more complicated. When we've never made the kind of cards that it takes to deliver on a strategy, we don't know what the answer looks like and we've never had to find out before. That means we need to do some exploration. Things get especially tricky when we have to deliver on that new strategy in a Limited environment, as making something brand new work in Sealed Deck and Draft is even harder than making it happen in casual Constructed.


As you might have guessed, populate is a perfect example of this kind of new mechanic and strategy. We've had tokens as a strategy before, but never quite in this way. In a normal token strategy, the natural cards to make key off of you having lots of creatures, which might or might not be tokens. Populate only cares that you have at least one token, which is a new way to look at things. It also encourages you to have bigger tokens as opposed to more. The cards that just want more tokens still work, of course, but they aren't the main attraction when you could be populating Rhinos and Wurms.


Thankfully, we have a model that we can use to help. I learned what I'm about to tell you from master developer [Erik Lauer](http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer). It's how he looked at populate, and it's how I look at these problems now.


Let's suppose we want to put a completely new and weird strategy into a set that uses a new mechanic, and we want it to work in Limited. We can divide the cards that support the strategy into a few categories.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld215_trostanis_judgment.jpg)[Trostani's Judgment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trostani%27s+Judgment) | Art by [Christopher Moeller](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Christopher+Moeller%22%5D)


### Cards That Are Very Strong Independent of the Strategy


The first category is cards that you want to take and play whether or not you're doing the thing we are trying to support. [Armada Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armada+Wurm) and [Call of the Conclave](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Call+of+the+Conclave) are perfect examples of this.




|  |  |
| --- | --- |
| 
Armada Wurm
 | 
Call of the Conclave
 |

[Armada Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armada+Wurm) is a straight-up bomb, and if you open it in Sealed Deck or Draft, you are basically going to play it because it is awesome. [Call of the Conclave](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Call+of+the+Conclave) isn't quite that strong, but it does offer a very good rate on a very reasonable body, so it should push a sealed deck toward playing green and white and having more tokens. If someone were to open [Armada Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armada+Wurm) and be passed [Call of the Conclave](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Call+of+the+Conclave), it's quite likely he or she will be more open to taking a random populate card later in the draft, and then we have that player in the new strategy.


This type of card is important because some people are more motivated by winning than doing a cool new thing, but they will still enjoy doing a cool new thing if they end up there. By including enough cards that price you in on pure power, we can make sure our new mechanics are actually part of the experience for even highly picky players.


### Cards That Are Fine by Themselves and Very Strong with the Strategy


This next category of card is something you would be willing to play without extra motivation. There aren't any bombs here, but there are cards that can approach bombiness if you meet the conditions they set forth. My two examples of this are [Coursers' Accord](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coursers%27+Accord) and [Trostani's Judgment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trostani%27s+Judgment).




|  |  |
| --- | --- |
| 
Coursers' Accord
 | 
Trostani's Judgment
 |

I'd be willing to pay six mana for two 3/3s or an instant-speed removal spell in many Limited decks, especially if I have some mana acceleration or card drawing to help me get there. I'd be ecstatic to pay six mana for a 3/3 and an 8/8, though, and I'd also be happy with a removal spell and a 4/4 for that. Both of these cards offer a reasonable rate on the front end, but offer large potential upsides if I'm willing to play along with what they're up to.


This kind of card is important because it includes the bread-and-butter commons that make me willing to draft a strategy. They tend not to be that risky to take, as they are powerful on their own and might become very strong if my deck goes the right direction. When there are enough of these, a player can end up in a populate deck without taking too much risk even if he or she doesn't open something like an [Armada Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armada+Wurm).


### Cards That Are Weak Independent of the Strategy but Strong with It


These cards are weak enough outside of the strategy that I would almost never consider playing them, but strong enough inside the strategy that I want them. [Druid's Deliverance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Druid%27s+Deliverance) and [Rootborn Defenses](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootborn+Defenses) are two such cards.




|  |  |
| --- | --- |
| 
Druid's Deliverance
 | 
Rootborn Defenses
 |

No matter how appealing [Fog](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog) effects are to some players, they tend not to be strong cards in Limited. [Rootborn Defenses](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootborn+Defenses) is a reasonable trick, but three mana is more than I prefer to pay for a card that messes with a combat step. However, once either of these cards is leaving me with a bonus 2/2—or something even bigger—I'm excited, and you can bet I'll think about playing it.


These cards are important to Limited working because they provide the kind of bait that can get an observant player into a deck. If there are cards that are only good with populate, only the players who are trying to populate will draft them, so being the only populate player at a table could mean you are scooping up tons of strong late picks that are bad for everyone else but excellent for you. Knowing that, you can trust that it's worth valuing the [Coursers' Accord](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coursers%27+Accord)s of the world a little more highly than everyone else and feel secure that you'll be rewarded for doing so.


### Cards That Are Weak Independent of the Strategy and Acceptable with It


Finally, we build in cards that aren't particularly strong even with the strategy. Two examples of cards that I think fit this description are [Security Blockade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Security+Blockade) and [Eyes in the Skies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eyes+in+the+Skies).




|  |  |
| --- | --- |
| 
Security Blockade
 | 
Eyes in the Skies
 |

I'm willing to play [Security Blockade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Security+Blockade) if I really need a token to populate for cards that are weak otherwise, and I'm also willing to play [Eyes in the Skies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eyes+in+the+Skies) if I have some really great tokens to populate. However, neither of these cards excites me. Three mana is more than I like to pay for a 2/2 with vigilance, and unlike [Coursers' Accord](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coursers%27+Accord), [Eyes in the Skies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eyes+in+the+Skies) is quite weak if you can't find another token to populate with it. Bonuses from synergy can get these cards up to levels I'm willing to accept, but not every draw will be perfect, and in bad draws these cards have been quite low-impact for me.


Despite not being strong, these cards are still quite important to the overall experience of Draft. If there are too many players at a table trying to draft populate, there will probably be a run on the strong populate cards. If we only included cards that could be strong, then there might not be enough populate cards to go around at all. If something goes wrong, though, cards in this category can swoop in to save the day. They won't make someone's deck great, but they will make it at least deliver the shape of the experience the player was hoping to have when he or she moved into the strategy.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld215_security_blockade.jpg)[Security Blockade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Security+Blockade) | Art by [James Ryman](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22James+Ryman%22%5D)


It takes all kinds of cards to make a new mechanic like populate work cleanly, from the unambiguous bomb all the way down to the weakest token maker. Our hope is that every time you try to draft a populate deck, whether you're slamming [Armada Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armada+Wurm) or sheepishly preventing 1 damage to yourself with a Security Barricade, you at least have enough tokens to copy and things to copy them with.


Have a fantastic release weekend, and I'll see you around again before too long.









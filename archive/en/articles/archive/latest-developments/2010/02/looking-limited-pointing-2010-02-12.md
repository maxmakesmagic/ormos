
---
[Link to Wayback Machine](https://web.archive.org/web/20200818200848/https://magic.wizards.com/en/articles/archive/latest-developments/looking-limited-pointing-2010-02-12)

[_metadata_:author]:- "Erik Lauer"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "647236"
[_metadata_:publish_date]:- "2010-02-12"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Looking at Limited Pointing"
[_metadata_:wayback_capture_timestamp]:- "2020-08-18 20:08:48"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200818200848id_/https://magic.wizards.com/en/articles/archive/latest-developments/looking-limited-pointing-2010-02-12"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/looking-limited-pointing-2010-02-12"
---


Looking at Limited Pointing
===========================



 Posted in **Latest Developments**
 on February 12, 2010 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_eriklauer.jpg)
By Erik Lauer




Erik Lauer is a senior game designer who works on final game design and development. Recently, he has led the Return to Ravnica, Modern Masters, and Theros development teams. 






![Tom LaPille](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_tomlapille.jpg)*Hello! I've gotten lots of requests from readers to write an article about Limited pointing, something that this column hasn't [talked about](/en/articles/archive/latest-developments/pointing-out-obvious-2005-11-18-0) in quite a while. Rather than try to do it myself, I asked Erik Lauer, the man who manages the metrics we use while working on **Magic** sets, to write an article for you. He's our go-to guy when we have questions about how to use math to make **Magic** development better, and I leave you in his capable hands. I'll be back next week with a follow-up article that gives my take on the exercises he proposes below.*


*See you next Friday!*


*Tom LaPille*


Developers here in R&D play a lot **Magic**, and form opinions on all the cards in the card set. We need to condense all their opinions into something manageable so the lead developer of a set can have some understanding of what each developer thinks of each card. One way we do that is to numerically rate each card. We call this "pointing." For Limited environments such as Sealed and Draft, we rate on a scale from 0.0 to 5.0. Stronger cards get a higher rating than weaker cards.


### The Why


One goal of pointing is to help balance the strengths of the colors. If one color is weaker than the others, there are fewer options for players, and less fun. If one color has significantly more high-pointing cards than another, it is a sign that one or more cards in the stronger color should be weakened, or one or more cards in the other color should be strengthened. This is not a replacement for playing to see which color is stronger, but it is another method we use. Examining what people play from their Sealed pool gives a lot of information, but frequently it is a mix of what people find appealing with what they find powerful. Pointing gives a check that the results aren't overly skewed towards appeal in cases where the goal is to measure power.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld77_manaSymbols.jpg)We try to get a range of values for different cards. If every card were just as efficient as the last, Limited play would come down to find the most synergetic cards in the fewest colors possible. There is less reason to consider playing a third color if every card is equally good. Also, the stronger cards help form a seed for a Sealed Deck. We try to give each color an appropriate spread of values. However, some cards end up pointing too high for Limited at their rarity. Cards like [Fireball](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball) and [Pestilence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pestilence) used to be common cards. When a common card is that strong in Limited, we either change the card or change the rarity. [Baneslayer Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baneslayer+Angel) is extremely powerful in Limited, so it is our highest rarity, mythic rare.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld77_fireballTimeline.jpg)Another goal of pointing is to see how similarly different developers value the cards. Strong players tend to have a fair amount in common, but there should be some cards where they disagree. If there aren't, it is time to go back and create that controversy. Part of the fun of **Magic** is building with cards that you like and other people don't. Having a fair number of developers point a set and looking for cards with a high variance is a way of doing that. It also catches typos.


A variation on having multiple developers point at the same time is to have some developers point, play for a month, and point again to see if any opinions changed. I think it is a good sign if people change their opinions after playing. When I led the development of ***Magic** 2010*, [Merfolk Looter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Looter) was initially pointed as a strong card, but later was pointed as a very strong card. The environment was slower than a typical limited environment. In a long game, card flow is even more potent than normal. This process was repeated in the real world. Initially many people thought blue was the weakest color in ***Magic** 2010* Limited. Some people thought you should never draft blue, even if you would be the only person drafting it. Blue certainly had less appeal. However, by the end of the Grand Prix season blue was in multiple winning decks, and a favorite of many players.


### The How


Now that we have an idea of why we point, let's explore how we point. We give guidelines to help developers through the process of pointing. We used to descriptive guidelines for the various values, such as:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld77_pointing.jpg)
> 
> ***5.0**: I will always play this card. Period.*
> 
> 
> ***4.5**: I will almost always play this card, regardless of what else I get.*
> 
> 
> ***4.0**: I will strongly consider playing this as the only card of its color.*
> 
> 
> ***3.0**: This card makes me want to play this color. (Given that I'm playing that color, I will play this card 100% of the time.)*
> 
> 
> ***2.5**: Several cards of this power level start to pull me into this color. If playing that color, I essentially always play these. (Given that I'm playing that color, I will play this card 90% of the time.)*
> 
> 
> ***2.0**: If I'm playing this color, I usually play these. (70%)*
> 
> 
> ***1.5**: This card will make the cut into the main deck about half the times I play this color. (50%)*
> 
> 
> ***1.0**: I feel bad when this card is in my main deck. (30%)*
> 
> 
> ***0.5**: There are situations where I might sideboard this into my deck, but I'll never start it. (10%)*
> 
> 
> ***0.0**: I will never put this card into my deck (main deck or after sideboarding). (0%)*
> 
> 
> 


There were some issues with these descriptions that led to creating new guidelines. Suppose you built 100 Sealed Decks, and played blue in 10 of the decks, and black in 60 of the decks. When you add up how many of each card you played out of the total available, you are averaging over 10 decks for the blue cards, and over 60 decks for the black cards. There could be as many blue 3.0s as black 3.0s. The problem is that you divided by how frequently you played each color, which took away the key information: how strong each color is.




|  |  |
| --- | --- |
| 
Heartstabber Mosquito
 | 
Gatekeeper of Malakir
 |

Another issue is that the frequency that you play a given card can be different from power of that card because of color commitment and other similar issues. I have always played all my [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse)s, but I think [Baneslayer Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baneslayer+Angel) is a stronger card. This can also happen with two colored cards, where one has a higher color commitment. I play [Heartstabber Mosquito](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heartstabber+Mosquito) more frequently in my decks than [Gatekeeper of Malakir](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gatekeeper+of+Malakir). It has an easy color commitment, has evasion, and has its own creature-killing ability. However, I tend to draft the Gatekeeper before the Heartstabber. It is a more efficient creature, and gives me both a card advantage and a tempo advantage on turn three.


Instead of thinking about how frequently you put a card in your deck, we stick with our intuition of "stronger cards" in an imaginary Limited tournament. Before you open your Sealed pool, you get to add your choice of two cards to your pool, to increase your chance of winning matches. The card that you think increases your chances is the stronger card. If the issue of "an extra card" is distracting you, perhaps imagine that a card at random will also be removed from your pool.


In draft events, a similar guideline would be less clear since some cards are better as first picks overall, while others are better once you know what colors you are playing. Still, if you feel you can compare two cards in drafting and decide which one is better, that is a fine way of comparing those two cards.


While this notion is a good one, some guidelines help developers do the pointing. One guideline is that a 0.0 is a card you would not play. If you were intending to play 17 lands and 23 spells, and you could choose to play this as your 23rd spell, you would prefer to play an 18th land. Sets might not even have a 5.0; I would point [Umezawa's Jitte](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa%27s+Jitte) at 5.0.


We use also benchmark cards. Suppose you are given these seed values for *Worldwake*:


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld77_pointedCards.jpg)Maybe you prefer [Wolfbriar Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wolfbriar+Elemental) to [Admonition Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Admonition+Angel). If so, you would need to talk to the lead developer and have new benchmark cards selected. At the very least, the benchmarks should be correctly ordered from strongest ([Admonition Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Admonition+Angel)) to weakest ([Rest for the Weary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rest+for+the+Weary)). Another issue is that you might think [Goliath Sphinx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goliath+Sphinx) isn't "enough" better than a [Searing Blaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Blaze) to rate a 0.5 difference. However, the scale is fairly arbitrary, so you can cope. Since different developers are going to have different opinions (we hope!), there isn't going to be a perfect scale.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld77_cardTops.jpg)Once we have values for all the cards, can we add them up to figure out which color is the strongest? Not quite. First off, cards have different rarities, so they are opened at different rates. But there is another problem, which is a bit harder to fix. [Admonition Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Admonition+Angel) is a 4.0 because we defined it that way, and [Searing Blaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Blaze) is a 2.5 by definition as well. That does not mean that a [Searing Blaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Blaze) + a [Battle Hurda](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+Hurda) is a good as an [Admonition Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Admonition+Angel). While the values of the cards are in order from strongest to weakest, that is all we have so far. They aren't in a form where we can add them up the way developers like.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld77_notEqual.jpg)How can we fix this? We need to again go back to our idea of "which is stronger" for a pile of cards to add to a Sealed pool, but this time you get to add more than one card. How many [Searing Blaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Blaze)s is an [Admonition Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Admonition+Angel) worth? If you could take two [Searing Blaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Blaze)s to add to your sealed pool, would you do that, or would you take the Angel?


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld77_equalQuestionMark.jpg)Is a [Goliath Sphinx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goliath+Sphinx) worth 2 [Searing Blaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Blaze)s? If I could have 28 [Lightning Bolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt)s, I wouldn't want 28 [Admonition Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Admonition+Angel)s. At that point the 40-card decks are too small, so we would need to talk about 100-card Limited decks. However developers have a lot less experience with 100-card Limited decks than 40-card decks, so we try to keep the questions in line with the expertise. We ask how many of the weaker card you would need to be about equal with one copy of the stronger card. 


Pointing can take a couple hours. The process of entering numbers in a spreadsheet isn't that exciting. However, it generates a lot of discussion of which cards are good and what makes them good, or not so good. Analyzing the cards and learning how different developers look at the cards is fun and enlightening.


[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ads/WWK_ArticleBanner_InStores.jpg)](http://archive.wizards.com/magic/tcg/products.aspx?x=mtg/tcg/products/worldwake)






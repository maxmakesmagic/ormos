
---
[Link to Wayback Machine](https://web.archive.org/web/20220121181444/https://magic.wizards.com/en/articles/archive/latest-developments/wishing-made-easy-2002-05-03)

[_metadata_:author]:- "Randy Buehler"
[_metadata_:description]:- "When I first heard the idea of putting a cycle of variants on Ring of Ma'ruf into Judgment, I knew it was a cool idea. It would clearly appeal to casual players (`Timmy` and `Johnny`) and I believed we might even be able to make it interesting for tournament play. We knew right away that we would limit the options to sideboard card when the “Ma'rufs” got played in tournaments,"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "620931"
[_metadata_:publish_date]:- "2002-05-03"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Wishing Made Easy"
[_metadata_:wayback_capture_timestamp]:- "2022-01-21 18:14:44"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220121181444id_/https://magic.wizards.com/en/articles/archive/latest-developments/wishing-made-easy-2002-05-03"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/wishing-made-easy-2002-05-03"
---


Wishing Made Easy
=================



 Posted in **Latest Developments**
 on May 3, 2002 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Headshot%209-2014_3.jpg)
By Randy Buehler












When I first heard the idea of putting a cycle of variants on [Ring of Ma'ruf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ring+of+Ma%27ruf) into *Judgment*, I knew it was a cool idea. It would clearly appeal to casual players ("Timmy" and "Johnny") and I believed we might even be able to make it interesting for tournament play. We knew right away that we would limit the options to sideboard card when the “Ma'rufs” got played in tournaments, but 15 slots turns out to be plenty of options for “Spike” to work with.


When the set came in from design and we developers got our hands on it, here's what we found:


[Yard Sale of Ma'ruf]  

1W  

Sorcery  

Choose an artifact or enchantment card you own from outside the game and put it into your hand.


[Blue Ma'ruf]  

1U  

Sorcery  

Choose an instant or sorcery card you own from outside the game and put it into your hand.


[Ma'rufic Tutor]  

1B  

Sorcery  

Choose a card you own from outside the game and put it into your hand. You lose half your life, rounded up.


[Tintinabulation of Ma'ruf]  

1R  

Sorcery  

Choose a card you own from outside the game and put it into your hand unless a player has CARDNAME deal 6 damage to him or her.]


[Dog Whistle of Ma'ruf]  

1G  

Sorcery  

Choose a creature or land card you own from outside the game and put it into your hand.


The trick to reading a design file is not to worry about power level, but instead to concentrate on the mechanics themselves. We want our designers to concentrate on thinking up new ideas -- we don't want them to waste their time worrying about how much some neat new effect should cost or whether Zvi will be able to break it. That's what development is for.


The first card in this list -- the white one -- is quite obviously broken right in half. Historically, most good combo decks work by getting the right combination of artifacts and/or enchantments into play and then BANG, either they go off (and win the game) or they lock you up (and win the game later). Take any combo deck (or any lock deck), move one copy of each piece of the combo to the sideboard, put in four of these, and we just made life way too easy for the person running the deck. Note, however, that the idea behind the Ma'rufs isn't flawed, it's just that the mana cost on this one was way off.


The design intent here was to have all five of these cost 1C. (“1C” -- pronounced “one cee” -- is R&D lingo for one colorless mana and one mana of a specific color. “C” is a sort of algebraic variable that ranges over all five colors.) Linking their mana costs like this is a nice way to tie a cycle together aesthetically, but in this case we needed the flexibility of giving them different costs. In addition, this cycle still hangs together just fine even with a variety of costs.


The other thing the designer (Brian Tinsman) did was make them all sorceries. However, when we started talking about the blue one in development, I argued that it would be cool to be able to play it as an instant so you could go get the perfect card from your sideboard while your opponent's threat was still on the stack, hanging in limbo waiting to resolve. It just seemed very blue to me to watch your opponent tap put for, say, a [Fact or Fiction](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction), and then you play Blue Ma'ruf to go get the [Disrupt](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disrupt) that's been hiding in your sideboard, waiting for just this moment.


At the same time, I wasn't really happy with the red Ma'ruf. It looked too similar to the black one, I argued, and I also didn't think anyone was ever going to decline to take the six damage so you were pretty much never going to get to use the card as a Ma'ruf. I did like the designer's idea to put some really big, really splashy effects onto “punisher” cards, but I felt we could do that on other red rares and do something else with the red Ma'ruf.


So I suggested that we have the blue one just get instants and the red one just get sorceries. Ever since [Scrivener](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrivener) and [Anarchist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anarchist) first came out, I've though of blue as the instant color and red as the sorcery color. My suggestion also made it make more sense that the blue one was an instant -- the instant can get instants and the sorcery can get sorceries. Plus now the black one -- the one where you had to pay half your life -- would be the only one that could get any card whatsoever. The team liked my suggestion and decided to try out that plan. We put the white one at ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif), left the other four at 1C, and starting building decks around them.


Building decks with these cards is cool. That was the first thing we learned, and that was definitely good news. We also learned that getting instants at instant-speed for just two mana was too good. We briefly tried out [Cunning Wish](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cunning+Wish) at 3 mana, it still looked good, and we quickly went to ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif). The Wishes stayed that way for quite a while as we tuned our decks and learned how they worked in practice. The red one seemed pretty good, as did the green one.


We eventually added a mana to both the black and the white ones because we figured it was better to be safe than sorry. We knew those two were the most likely to wind up enabling fast combo decks, and that's not what we wanted the Wishes to do. Instead, we wanted everyone to have fun trying out a whole new deck-building experience. Our goal was to make the blue one, the red one, and maybe the green one good so players would wind up debating which 15 cards they are most likely to want in the middle of an otherwise relatively normal game. I'm not saying we don't want anyone to play with the other two -- I'm just saying that they are more powerful and so we have to charge you to gain access to all that power.


After a couple months of Future Future League play, we came to realize that there's a hidden cost to play with Wishes in tournament play. You do get access to your sideboard in game 1, but your sideboard is much worse for games 2 and 3. We usually build sideboards for Wish-decks with 15 fairly diverse cards to “tutor” for during game 1, but even if you limit yourself to, say, 5 or 10 cards to wish for, you're still playing with a smaller sideboard than everyone else. Everyone else gets to bring in all their hosers for game 2 but you probably only had one copy of that hoser card in your sideboard in the first place and now you're going to leave it in your sideboard, because your deck still has four Wishes in it.


Don't get me wrong, the Wishes are still plenty good. The Wishes looked better in our initial playtesting than they did in our later league because we, like almost everyone else, playtest game 1 a lot more than we test sideboarded games. That usually doesn't matter a lot, but it certainly matters more when you're testing with Wishes. Basically, what this insight did was make us feel better for putting the red and green ones at just two mana, plus we lowered the blue one back down to 3 mana.


The last little tweak we made to the Wishes was to have them remove themselves from the game. The main reason we did this was that we found ourselves constantly forgetting to put the cards we got back into our sideboards. We knew that lots of tournament players would make the same mistake and they would wind up playing with one too many cards in game 2 or game 3. That's a lot of potential game losses, we reasoned, and so we figured we would do everyone who forgets to count his deck and sideboard a favor. Now if you just shuffle up your cards after game 1, you'll have the right number of cards in your deck -- they probably aren't exactly the ones you wanted (what with a Wish still removed from the game and a sideboard card in your deck) but that's a lot better than not getting to play at all.


All in all, we're really happy with how the Wishes turned out. We think casual players will love to get their hands on them and we think we were able to price them at a point where tournament players will also want to play with them, but they aren't broken. On top of that, they're really cool. *And* they're fun to play with. It's rare that a mechanic comes along with all four of these virtues and I think players will be talking about these five cards for years to come.


[Last week's poll](/en/articles/archive/latest-developments/polls-and-pies-2002-04-26) asked whether you want this column to end in a poll every week:




|  |  |  |
| --- | --- | --- |
| Yes | 4794 | 92% |
| No | 431 | 8% |
| **Total** | **5225** | **100%** |

Fair enough ... that's what I'll do.


*Randy may be reached at latestdevelopments@wizards.com.*






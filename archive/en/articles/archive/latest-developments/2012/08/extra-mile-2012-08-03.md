
---
[Link to Wayback Machine](https://web.archive.org/web/20210502205857/https://magic.wizards.com/en/articles/archive/latest-developments/extra-mile-2012-08-03)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "I was talking to independent-website Magic personality and Seattle-area PTQ fixture Zaiem Beg the other day—by `talking` I mean `getting crushed by him in a Magic 2013 draft`—and he made a remark that really stuck with me.`I don't want to be that guy,` he said, `who is like reading a book and comes across a paragraph about a painting of a ship hanging in the corner of some"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "645321"
[_metadata_:publish_date]:- "2012-08-03"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Extra Mile"
[_metadata_:wayback_capture_timestamp]:- "2021-05-02 20:58:57"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210502205857id_/https://magic.wizards.com/en/articles/archive/latest-developments/extra-mile-2012-08-03"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/extra-mile-2012-08-03"
---


The Extra Mile
==============



 Posted in **Latest Developments**
 on August 3, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 






I was talking to independent-website **Magic** personality and Seattle-area PTQ fixture Zaiem Beg the other day—by "talking" I mean "getting crushed by him in a ***Magic** 2013* draft"—and he made a remark that really stuck with me.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld206_zaiem.jpg)"I don't want to be that guy," he said, "who is like reading a book and comes across a paragraph about a painting of a ship hanging in the corner of some room. He starts talking forever about what this ship means and what this painting means and why it's significant that it's hanging in the left rather than the right corner of the room, and he gets all *DaVinci Code* about the hidden layers of meaning in everything, when in truth it's just a painting of a ship hanging in a room.

"But," he said, "the more I play M13 Limited, the more I feel like that guy. There are all these little interactions that seem to fit together in these really intricate ways, and it seems to me like you guys actually did put a lot of that stuff together on the front end. So... am I crazy? Did you just get really lucky and have everything work out? Or did you think of this stuff when you were making the set?"

The truth is somewhere in between, of course. Whenever anything works out in a way you're satisfied with, there's always some amount of luck involved. And all of our sets, not just ***Magic** 2013*, are the result of thousands and thousands of person-hours testing what have got to be millions and millions of interactions, so we wind up going pretty deep. But as M13's lead developer, I have a whole lot more perspective about how this process worked for this particular set, and I wanted to talk about just a few of the minor tweaks we made that, I think, help contribute to its richness, texture, and robustness.


![Encrust](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Encrust)
 
All right, I will be the first to admit that [Encrust](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Encrust) is hardly the most elegant card ever designed. It has some weird words on it, which most certainly is a very real cost. At the same time, as much as we talk about how important it is to prioritize accessibility—especially in core sets—it's not correct to err on that side of the equation 100% of the time. Sometimes, you have to improve the environment even if that means using awkward tools.


In [Encrust](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Encrust)'s case, a couple of things were going on. First, by design, there are a number of very powerful artifacts in ***Magic** 2013*. For accessibility reasons, core sets don't have access to as many variance-reducing mechanics (like flashback and kicker) as expansion-level products, meaning you have got to carve out deliberate space for effects that allow you to do things with your mana as the game goes long. In practice, this typically means putting in artifacts like [Greatsword](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greatsword) or [Jayemdae Tome](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jayemdae+Tome) that allow you to trade short-term investment for long-term gain. In this case, the combination of [the five rings](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+%5bring%5d+%5bof%5d&set=+%5b%22Magic+2013%22%5d), [Tome](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tome), [Kitesail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitesail), and certain rares like [Trading Post](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trading+Post) and [Sands of Delirium](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sands+of+Delirium) meant that a lot of games came down to backbreaking artifacts that dominated the long game. Red, green, and white all possessed relatively straightforward solutions to these cards, and black tends to be soft to artifacts by design. Blue, though, had only the narrow [Negate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Negate) and the ponderous [Rewind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rewind)—and nothing to do once the problem artifact hit the board.

The second thing happening was the dominance of Swords (and to a lesser extent, [Runechanter's Pike](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=244681)) in Constructed. A splash of red for [Ancient Grudge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancient+Grudge) or white for [Divine Offering](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=213760) is certainly more effective at containing the Sword itself, but having the option to [Encrust](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Encrust) a Sword or alternatively "[Dehydrate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dehydrate)" a problematic creature gave blue decks an in-color option to try out. The idea was that you often couldn't afford to play dedicated artifact removal because it exposed you to vulnerabilities along different axes of interaction, so we wanted to make a roll at a card that could get around that particular drawback. It's not terribly efficient, of course, but it's a tool in the toolbox at least.

Taken together, then, we modified [Encrust](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Encrust) to enchant artifacts and to remove activated abilities immediately, so you didn't have to give your opponents a "final shot" if you played the card on an untapped permanent.


![Liliana's Shade](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Liliana%27s+Shade)
 
For a long time, [Liliana's Shade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana%27s+Shade) followed the model of most of our other Shades, and only had a single black mana in its mana cost. The idea was you can start out with just a single [Swamp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp), and build your creature up further with the ability if you wanted to.


A funny thing kept happening, though. We attempted very deliberately with this set to have two colored mana in the mana cost of its most powerful, game-ending commons and uncommons—[Serra Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Angel), [Talrand's Invocation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Talrand%27s+Invocation), [Volcanic Geyser](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volcanic+Geyser), [Sentinel Spider](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sentinel+Spider), [Duskdale Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duskdale+Wurm), and—most salient to this discussion—[Murder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murder) and [Vampire Nighthawk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampire+Nighthawk). The problem was that [Liliana's Shade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana%27s+Shade), as a creature that generates card advantage yet is capable of trading with a 2/2, was (counterintuitively) a reasonably splashable card on its own. Once you did that, though, the cost of splashing [Murder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murder) and Nighthawk decreased drastically, which defeated the whole purpose. I believe strongly that, for the most part, a color's best cards should function as rewards for playing that color. They shouldn't just go into every deck, because one of the ways you balance a Limited environment is ensuring that each color has access to game-breaking cards. If white gets [Archangel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Archangel), blue gets [Air Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Air+Elemental), black gets [Sengir Vampire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sengir+Vampire), green gets [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun), but red gets (say) [Disintegrate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disintegrate), well, red is getting the short end of the stick. You don't want to go too overboard with this philosophy—splashing is important to maintaining an environment's diversity, so you want it to happen some percentage of the time—but it's important to maintain meaningful differentiation between the colors.

Anyway, a splashable way to get a second [Swamp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) was contributing to this problem, so we moved the card to ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif).


![Merfolk of the Pearl Trident](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Merfolk+of+the+Pearl+Trident)
 
It's been years since **Magic** has printed a straightforward one-mana vanilla 1/1 creature with no abilities. We've talked before about how including this card led directly to the printing of [Master of the Pearl Trident](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+the+Pearl+Trident)—the idea (savagely ripping off of Alpha*)* being that your foot soldiers can grow much more substantial with help from their general—but that doesn't address how the card came to exist in the file in the first place.


We try to place two vanilla creatures in every color in the core set to minimize complexity for the entering player. Just because they're there to minimize complexity, though, doesn't mean they can't do a lot of load-bearing work for game play. You just have to design them right! My favorite example of this is *Innistrad*'s [Rotting Fensnake](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rotting+Fensnake), who helps contribute to both the morbid mechanic and the recursive Zombie archetype without having a single word printed in its rules text.

With [Merfolk of the Pearl Trident](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+of+the+Pearl+Trident), what we kept finding was that a lot of our blue decks were getting outpaced by quick red-deck starts of [Mogg Flunkies](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mogg+Flunkies) into [Reckless Brute](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reckless+Brute). The premier early-drop blue creature, [Welkin Tern](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Welkin+Tern), couldn't get in the way, and [Kraken Hatchling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kraken+Hatchling) (while effective) kept the Brute on the table to power up the Flunkies. Now, we could obviously slot any creature with power and toughness into the set to deal with this problem, but the better the card you print, the less likely it is to get to the person who is trying to use it deliberately—at some point, the card will get picked on raw power level alone! The solution was to print a very underpowered creature that a blue deck could nab thirteenth or fourteenth that could still be sideboarded in to deal with this particular issue.


![Turn to Slag](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Turn+to+Slag)
 
Originally, red's burn suite in ***Magic** 2013* consisted of [Flame Slash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Slash), [Searing Spear](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Spear), and [Chandra's Fury](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra%27s+Fury). One of red's more subtle quirks is that different varieties of damage spells are actually totally different cards even though they differ in their rules text by something like one word. That is, "CARDNAME deals 4 damage to target creature" and "CARDNAME deals 4 damage to target player" have basically nothing to do with one another in terms of the game play interactions they produce, yet they seem so similar that it's awkward to cram too many of both effects into the same set. This is why red's slice of the color pie often seems much more narrow than other colors'—the term "damage" really means so many different things!


Anyway, I wanted to make sure that each damage spell in the set did something different, that there wasn't, you know, [Shock](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) and [Searing Spear](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Spear) and [Lightning Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Blast) and the difference was a single Arabic numeral. This is how we arrived at (a) fixed damage to a single creature, (b) fixed damage to a single creature *or* player, (c) fixed damage to a player *and* multiple creatures, (d) fixed damage distributed to multiple creatures and/or players, and (e) variable damage to a single creature or player. For the most part I like such a distribution, and there are enough unused permutations in here that you've hardly exhausted all your options.

The trouble was that [Flame Slash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Slash) proved to be totally bananas with [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage) in Standard, so we had to find another option. We knew we wanted to only hit creatures, and we knew we didn't want to deal 1 or 3 points of damage. Eventually, we decided that because the rings cycle was proving to be more powerful than we initially expected, it'd be a good idea to have a card that helped keep them in check. We settled on [Turn to Slag](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turn+to+Slag)—and also dropped Yeva down to a 4/4, since her 5th point of toughness existed largely to keep her immune to [Flame Slash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Slash).


![War Priest of Thune](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=War+Priest+of+Thune)
 
Astute readers will notice that two cards left out of the whole "game-ending common and uncommon" discussion earlier were [Pacifism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism) and [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring)—two of the best cards in the format! One of the challenges with working with reprints is, well, you're stuck with their printed text. [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) is certainly powerful enough to warrant (for example) a ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) mana cost, but the card does good things for us in Constructed and I like presenting the option of splashing [O-Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=O-Ring) to (say) a black-red deck if it *really* needs to deal with like a [Stuffy Doll](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stuffy+Doll) or [Staff of Nin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Staff+of+Nin).


The cost, though, is obviously that fewer base-white decks wind up playing [Pacifism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism) and [Oblivion Ring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) than base-red decks get [Turn to Slag](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turn+to+Slag) or [Furnace Whelp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Whelp), etc. The solution was to give base-white decks a way to punish those splashes a little bit, making them vicariously better in their "home" color. [War Priest of Thune](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Priest+of+Thune)—a 2/2 for two mana—is a card you'll almost always main deck, but occasionally you enjoy a *gigantic* upside as it [Flametongue Kavu](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flametongue+Kavu)s (to create a verb on the fly) one of your opponent's highest picks!

I could go on and on and on about this, but it looks like I've hit my word limit. It's funny—I haven't thought about most of these decisions in like a year and a half, and it's easy to forget in retrospect how many hours were devoted to things that seem so terribly minute: whether [Omniscience](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Omniscience) should cost nine or ten, whether [Staff of Nin](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Staff+of+Nin) (then simply Archmage's Staff) should embed the card-drawing effect inside the activated ability, whether [War Falcon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Falcon) implied that both Soldiers *and* Knights should merit a creature-type "lord" at rare, and even whether the fact [Goblin Battle Jester](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Battle+Jester)'s 2nd point of toughness made the [Trumpet Blast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trumpet+Blast) deck less vulnerable to [Rain of Blades](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Blades) and [Cower in Fear](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cower+in+Fear) was a good or bad thing!

Here's the thing, though. We know y'all love **Magic**, and we do too. It's an honor and a privilege to help create something so many people care about, and we very badly want to live up to all the time and energy you guys invest in this game. It's something I couldn't take more seriously. **Magic** has built lifelong relationships and fostered innumerable connections between people that simply wouldn't exist otherwise. It's our duty, then, to respect that by ensuring our work lives up to the incredibly high standards those relationships demand.

I hope it does. I hope it has. I hope it always will.

  







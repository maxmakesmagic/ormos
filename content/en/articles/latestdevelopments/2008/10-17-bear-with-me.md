---
id: 9cbrnf29
kind: article
lang: en
path: /en/articles/latestdevelopments/2008/10-17-bear-with-me
title: Bear With Me
published: '2008-10-17'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: ken-nagle-1c7b6b00
  name: Ken Nagle
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
    lang_detected: en
    capture_id: 718264
    url: https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
    captured_at: '2022-10-06 14:23:27+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
    lang_detected: en
    capture_id: 718264
    url: https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
    captured_at: '2022-10-06 14:23:27+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
    lang_detected: en
    capture_id: 718264
    url: https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
    captured_at: '2022-10-06 14:23:27+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
    lang_detected: en
    capture_id: 718264
    url: https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
    captured_at: '2022-10-06 14:23:27+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 9cbrnf29
  url: https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
  page_key: magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
  lang: en
  template: drupal
  captured_at: '2022-10-06 14:23:27+00'
  capture_id: 718264
  wayback_url: https://web.archive.org/web/20221006142327id_/https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
- document_id: 9cbrnf29
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/8
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/8
  lang: en
  template: aspx
  captured_at: '2013-07-02 13:47:08+00'
  capture_id: 623607
  wayback_url: https://web.archive.org/web/20130702134708id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/8
- document_id: 9cbrnf29
  url: https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-17
  page_key: magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-17
  lang: en
  template: drupal
  captured_at: '2022-06-25 18:11:31+00'
  capture_id: 718267
  wayback_url: https://web.archive.org/web/20220625181131id_/https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-17
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9cbrnf29
  capture_id: 718264
  url: https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
  wayback_url: https://web.archive.org/web/20221006142327id_/https://magic.wizards.com/en/articles/archive/latest-developments/bear-me-2008-10-16
  captured_at: '2022-10-06 14:23:27+00'
  template: drupal
  sha256: 19138e065165797eff5778414757d5803ae6a4a1ac55a2447404e20374ad0d3d
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
*As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on **Magic** development. Enjoy!*  
 –Kelly Digges, **magicthegathering.com** editor 

> A customer sits at his reserved table in his favorite restaurant. A waiter delivers to him the restaurant's latest special. The customer recognizes the dish despite its different garnishing and shouts at the waiter increduously, "Caviar? Again?!"
> 
> The waiter reassures him, "Wait until you taste it—it's the best caviar we've ever made!" 
> 
> The customer pouts, "I've already HAD caviar once in my life, like 10 years ago. I want something ELSE. Something NEW!"
> 
> The waiter forces a smile; a bead of sweat pools on his temple. "But we know for a fact that you love caviar!"
> 
> The customer replies, "I KNOW I like caviar; what's the point of eating caviar again? I want something to eat that I've never had before."
> 
> The waiter whirls back to the kitchen. The customer yells behind him, "And make sure it's something I'll LOVE!"

There are 249 individual cards in *Shards of Alara* I could choose from to cover in my first development column. After subtracting the basic land cards, the cards already covered by our other authors, and the "boring" cards, there's one card in particular that I have the most to say about it:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cylian+Elf)](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf)

This seemingly innocuous Elf turned out to be, according to my Internet reading, the most controversial card in *Shards of Alara*. Frequent criticisms about [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) include:

1.  **I finished reading this card in less than three seconds.**

Congratulations, that means you have more time to play actual **Magic**. Wordiness is not a likeable attribute of speeches, **Magic** cards, or development articles. **Magic** is not a reading game or a memory game, nor does it seek to test the limits of human comprehension. Simplicity in a game is a good thing (as long as it's not at the expense of fun and depth of game play).

2.  **This card doesn't do anything.**

Actually, we've never printed a **Magic** card that does absolutely nothing (heh, I just got an idea for a new card we could print). So every **Magic** card does *something*.

Creatures have intrinsic abilities (and thusly inherent complexity) because **Magic**'s game rules make it so. A ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) mana cost allows the card to be played, etc. (I'm sure you can figure the rest out.)

To better illustrate just what the "do-nothing" [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) can and can't do, let's compare her to an analogous DuelMasters card, Burning Mane:

![Burning Mane vs. Cylian Elf](http://wizards.com//mtg/images/daily/ld/ld8_comparison.jpg)  

If you consult the rules for both games, you'll find that the differences include:

*   [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) can block; Burning Mane can't block.
*   Burning Mane can be a played as a mana source; [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) can't.
*   Burning Mane can directly attack your opponent's tapped creatures; [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) can attack your opponent.

Being a vanilla 2/2 creature in **Magic** actually gifts you with more "abilities" than you can fit into the text box. [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) would have considerably fewer abilities and game-play options if, for example, it was a 0/2 with "[Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) can't block."

3.  **This card is bad.**

While it would behoove you to read [When Good Cards Go Bad](https://web.archive.org/web/20081017000000/https://magic.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr5), the simple fact remains that cards can't be good without other cards being bad. Happiness can't be measured without sadness and beauty doesn't exist without ugliness.

"Why print it if it's bad?" is its own conundrum. Why do poker decks have 2s in them? Since deuces are the worst cards in the deck, how about not printing them? Doing that makes 3s the worst cards in the deck, etc. All this logic does is effectively decrease the power level gamut of cards. More on this later.

4.  **No one would ever play with this card.**

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=One+with+Nothing)](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=One+with+Nothing)

I saw a foil [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) attacking and blocking at the *Shards of Alara* Prerelease. For everyone out there who doesn't have access to **Magic Online** casual room data: every card gets played. All of them. Unless we go so far as to make a card that instructs you to sever a finger before you can play it (putting the basic human preservation instinct below playing the card), there are too many players across the world making too many decks for any card to not "see play."

Now, there's a valid argument that a certain number of players need to enjoy a particular card to justify printing it. However, if your quest is to design a card that absolutely no player will want to play, you will ultimately fail, because there exists a player niche (Über-Johnny) that enjoys a card precisely because no one else will play with it.

"No one would ever play with this card." is simply a way of hiding the more selfish statement that "I would never play with this card." That's actually an important part of **Magic**—identifying what cards are for you and which aren't for you. This spawns the entire "trading" part of **Magic**.

Now, the combination of "this card is bad" and "no one would ever play with this card" leads to a behavior that plays directly into the core of **Magic**'s business model.

**Magic**'s fantastic mana system ensures that cards are only truly in competition with other cards of the same mana cost. When [Shadowmage Infiltrator](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shadowmage+Infiltrator) was fighting [Psychatog](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychatog) for deck slots during *Odyssey* Standard, [Psychatog](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychatog) won. Later, [Shadowmage Infiltrator](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shadowmage+Infiltrator) got its chance to shine in the *Time Spiral* "timeshifted" set when [Psychatog](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychatog) wasn't around.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shadowmage+Infiltrator"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Shadowmage+Infiltrator"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychatog"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Psychatog"></a></div></div></td></tr></tbody></table>

It stands to reason that with twenty-three different green creatures that cost ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), competition between them could be avoided. But creating a competition with obvious winners and losers can be a *good* thing. For example, which creature would you rather attack with?

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Gray+Ogre"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Uthden+Troll"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Uthden+Troll"></a></div></div></td></tr><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedge+Troll"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Sedge+Troll"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Granite+Gargoyle"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Granite+Gargoyle"></a></div></div></td></tr></tbody></table>

While the winner might not be obvious, we can all agree that [Gray Ogre](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre) trudges across this finish line in last place. This particular competition is interesting because all these cards were printed in Alpha, Beta, *Unlimited*, and *Revised*. Many "mistakes" were fixed across these four printings, but the four ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) 2/2 creatures were not among the "mistakes" that needed correcting. You may start with [Gray Ogre](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre) due to availability, but a big step forward in your **Magic** career is replacing a card in your deck with another card you believe to be superior.

As another exercise, consider all these potential four-drops for your new Bant exalted deck:

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Outrider+of+Jhess"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Outrider+of+Jhess"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rhox+Charger"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Rhox+Charger"></a></div></div></td></tr><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angelic+Benediction"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Angelic+Benediction"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ranger+of+Eos"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Ranger+of+Eos"></a></div></div></td></tr><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stoic+Angel"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Stoic+Angel"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rafiq+of+the+Many"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Rafiq+of+the+Many"></a></div></div></td></tr></tbody></table>

With this many cards to choose from, deck-builders have plenty of options just from *Shards of Alara* alone. 

When you replace an [Outrider of Jhess](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Outrider+of+Jhess) in your Bant exalted deck with a [Rafiq of the Many](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rafiq+of+the+Many), it's almost like your deck "leveled up," if you're willing to stretch the metaphor a little. As a **Magic** player, you almost subconsciously make decisions like this all the time while maximizing fun, power level, or some other variables.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gempalm+Strider"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Gempalm+Strider"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stonewood+Invoker"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Stonewood+Invoker"></a></div></div></td></tr><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bramblewood+Paragon"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Bramblewood+Paragon"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wolf-Skull+Shaman"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Wolf-Skull+Shaman"></a></div></div></td></tr></tbody></table>

The fact that you can be confident in your choice in comparison to [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) gives players a sense of accomplishment, and tons of games use that phenomenon to their advantage.

To put it another way, in any role-playing game you've played, you can find a sword with bonus +1 damage. I guarantee you that any game with a +1 damage sword also has a +2 damage sword. Why? Because unequipping your +1 damage Sword for a strictly better +2 damage sword feels great! It's what players want—it's absolutely the correct play, and you feel (and are) more powerful within the rules of the game.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wild+Nacatl)](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Nacatl)

Now, it *is* possible to design games without "strictly betters," where every player choice fits inside an intricate puzzle of "maybes" with tons of rock-paper-scissors involved. The possible choices would be closer to something like:

*   Sword of +1 damage
*   Shield of +2 defense, -1 speed
*   Dagger of +2 speed, -1 defense

But in the end, the player satisfaction gained from replacing a +1 damage sword with a strictly better +2 damage sword far outweigh the unjustified derision of "strictly betters" existing. In effect, [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf), acting as the +1 damage sword, does her part by "spreading more awesome" on the sword of +2 damage (say, [Gempalm Strider](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gempalm+Strider)). Tons of games do it, and so does **Magic**—but **Magic** does it less than most.

Before I get an avalanche of hate mail claiming that "rarity = power level," I've designed quite a few **Magic** cards, and the most powerful one of all is the mighty common [Wild Nacatl](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Nacatl). We are more than happy to spread power level across all rarities (you end up with a better set that way).

5.  **This card has been printed before.**

There once was a time when our Nayan friend [Druid of the Anima](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Druid+of+the+Anima) would get a cock-eyed sideways glance for graduating with worse grades from Mana Elf University than her cousin [Skyshroud Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skyshroud+Elf).

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skyshroud+Elf"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Skyshroud+Elf"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Druid+of+the+Anima"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Druid+of+the+Anima"></a></div></div></td></tr></tbody></table>

The goal of **Magic** design and development isn't to plot every **Magic** card on a graph so that no two cards overlap each other perfectly for cost, effect, power level, format, sideboard, and metagame axis. No strictly-betters, no obsoletions—just filling in the points on the multi-dimensional graph that haven't been filled yet. That's more like a piece of art rather than an actual game capitalizing on the allure of strictly-betters.

And for the record, [Oblivion Ring](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring), [Cancel](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel), [Infest](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infest), [Goblin Mountaineer](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Mountaineer), and [Naturalize](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize) are not "a cycle of reprints" as conspiracy theorists contend—each card cleanly performs a function that the set needs. A huge goal of a **Magic** set is to "play fun," not "be a collection of cards slightly different from the previous 10,000 cards."

Conclusion

And that's about all I have to say about [Cylian Elf](https://web.archive.org/web/20081017000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf). I hope you understand better why she exists in all her vanilla glory, and I hope you feel her selflessness at work as you enjoy her strictly-betters.
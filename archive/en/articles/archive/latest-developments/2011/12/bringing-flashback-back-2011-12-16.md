
---
[Link to Wayback Machine](https://web.archive.org/web/20210122224641/https://magic.wizards.com/en/articles/archive/latest-developments/bringing-flashback-back-2011-12-16)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "Welcome to Flashback Week!"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "644611"
[_metadata_:publish_date]:- "2011-12-16"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Bringing Flashback Back"
[_metadata_:wayback_capture_timestamp]:- "2021-01-22 22:46:41"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210122224641id_/https://magic.wizards.com/en/articles/archive/latest-developments/bringing-flashback-back-2011-12-16"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/bringing-flashback-back-2011-12-16"
---


Bringing Flashback Back
=======================



 Posted in **Latest Developments**
 on December 16, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 






Welcome to Flashback Week!


I'm sort of overcome with options right now. I could flash back to the *original* Flashback Week, and write an article in the style of *that* Latest Developments... until I realized that somehow there was no previous Flashback Week. I could discuss the (many) reasons behind why we don't intend to bring the card [Flash](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash) back. I could pontificate about the card [Sentinels of Glen Elendra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sentinels+of+Glen+Elendra), which has "flash" and whose playtest name was originally Faerie Defensive Back. Man, this Development column thing is so open-ended!


::breathes::


Restrictions breed creativity. Restrictions breed creativity.


Let's see. Let's see.


...oh yeah! I could talk about how we develop cards that have flashback!


Brilliant and original.


### The (Lack of) Luck of the Draw


Year after year of **Magic** releases have shown time and time again that players *love* any mechanic that lets them get more than one use out of their spells. Replicate, flashback, buyback, and persist have all rated amongst the most popular **Magic** mechanics ever. There's something inherently cool about breaking one of **Magic**'s fundamental rules, which is that you're playing a game where cards represent spells, and so each card normally represents one spell you can cast one time. Another part of this is that mechanics that break this rule tend to be *really powerful—*so powerful, in fact, that Development got a lot of them wrong in the beginning.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld173_grasp.jpg)[Grasp of Phantoms](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grasp+of+Phantoms) | Art by [Izzy](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Izzy%22%5D)


Lots of games promise a fun experience where you do a lot of really cool things that create cool interactions and allow you to tell cool stories. That promise of being able to do awesome and exciting stuff creates this intense desire within you to continue playing the game. When you start actually playing that game, however, you learn quickly that what you should be doing when you want to win is throwing all of that stuff out the window and figuring out how to generate raw resource advantage. In a strategy game, instead of building that first unit that goes out and fights things, you should probably build more units that harvest minerals. In an action-adventure game or an RPG, instead of advancing the storyline and exploring the world, you should first probably farm all the creeps in the area. In a deck building game, instead of taking advantage of sweet cards that create interesting game play, you should probably buy more gold and silver or whatever. This isn't always true, but is true enough of the time that if I'm playing a new game I've never seen before, I can frequently just employ this heuristic and play the game at something like 80% efficacy.


Similarly, in **Magic**, the structure of the game (drawing one card per turn from an initial state of equilibrium) mandates that accruing raw resource advantage in the form of cards is very strong. In the mid 90s, the concept of "card advantage" revolutionized competitive deck building and has only become more relevant in the fifteen-plus years since. If I can trade one card of mine for two cards of my opponent's, or one card of mine for access to two more cards of mine, I am *way* ahead—way more ahead than it might intuitively seem at first.


That one additional card—specifically, arriving at the point in the game-state where you have access to one card and your opponent has access to zero—is so deceptively powerful that it's difficult to comprehend. I myself struggle with it nowadays. I came into R&D right off the Pro Tour in the middle of what might be considered to be the best season of my career. At that point in time, I didn't even have to think about how many cards I was ahead in a given game, who played and who drew first, which cards I had cast that had generated advantage, which cards my opponent had cast that had done so, etc. That "count" informed my entire game play strategy on a given turn and in a given game—frequently I'd choose decks whose *entire purpose* was to leave myself with access to a single card, no matter how innocuous-seeming that card might be, while my opponent had access to none. Now, though, without the intense pressure of having to compete at the highest level for the last several years, I'm just way worse at doing that than I used to be. And I'll find myself losing games that I would have never lost before just because I get careless and throw away a card here and there. As it's happening, I don't really think about it.


One of the reasons **Magic** has been so successful as of late, I believe, is because R&D realized that winning and losing games this way isn't all that satisfying. It reduces **Magic** to a kind of counting contest, and unless you're trained to think about games in this way it becomes very difficult to improve in a way that's viscerally rewarding. I have played in twenty-something Pro Tours and have won a lot of games with [Exclude](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exclude)s, [Dismiss](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss)es, [Blightning](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightning)s, [Flametongue Kavu](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flametongue+Kavu)s, and [Cryptic Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Command)s—but never once was I like, "WHOA DUDE, THAT WAS TOTALLY AWESOME, I NEUTRALIZED ONE OF MY OPPONENT'S SPELLS WITHOUT SACRIFICING ONE OF MY OWN!!!!!!!!!!!!!!!11111111oneone."


It's not that people don't "get" it—we're not *dumbing down the game*. It's not that players don't understand what's powerful. It's that when you say to somebody, "Oh, if you want to win, you shouldn't summon that awesome Demon Angel Dragon or cast that awesome spell that makes your guys 27/27 or assemble that awesome combination that deals 62 damage to each opponent for every Squirrel Penguin Cat Lord you have in play; instead, you should cast [Mind Rot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Rot)," they say, "That's nice, and I understand—but why in the world would I ever want to do that?" And that's a natural reaction, because they've just been lied to. They have been tempted by the game designer with tremendously appealing possibilities, only to have those possibilities shot down by the very structure of the game inside which those possibilities exist.


We've made it a lot easier to win with the kinds of things most people want to win with, and a lot more difficult to win the game with [Force Spike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+Spike) into [Whispers of the Muse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whispers+of+the+Muse). That's good. But it's not good if the *only* thing a player can do is summon creatures and send them mindlessly bashing into one another, either. **Magic** is fun because there are a lot of strategies you can use to play **Magic** and win at **Magic** in a way that's satisfying to you. It's just that because raw resource advantage is so much more fundamentally powerful than everything else, it requires a lot of diligence to balance it effectively.


Flashback is, at its core, nothing but raw resource advantage. It has a place in the game. It is very popular and very fun. It just has to be handled with care.


### Hungry Like The (Were)Wolf


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld173_ancient.jpg)[Ancient Grudge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancient+Grudge) | Art by [Ryan Yee](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Ryan+Yee%22%5D)


Why is flashback nothing but raw resource advantage?


Here is the actual text of the flashback mechanic, with all the rules baggage removed. Are you ready for this? You are about to get a glimpse into a mind-blowing fundamental secret. You are about to peel back the layers and discover something essentially *true*. All flashback says is:



> Draw a card.
> 
> 


This is not a metaphor, by the way. I am not about to explain how getting to re-buy your spell is so similar to drawing another card that for all intents and purposes it might as well say "draw a card" or whatever. I mean literally that every card with flashback has no other text than the actual line "draw a card" on it. When you cast [Firebolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firebolt), you are casting "![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif); Sorcery; Deal 2 damage to target creature or player. Draw a card."


![Firebolt](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Firebolt)  
That's an insanely powerful spell that we would never print. How, then, did we print [Firebolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firebolt) (which, by the way, we would never print at common nowadays)?


The trick is that the card you're drawing off [Firebolt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firebolt) just happens to always be the following spell: "![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif); Sorcery; Deal 2 damage to target creature or player."


Look man. Beggars can't be choosers, alright. I'm letting you [Shock](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) and draw a card for one mana, and all you can do is complain to me that the additional card you drew off that [Shock](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) is so mediocre. *You're killing me, Smalls.* It's like complaining during the holidays that your grandma "only" gave you a $10 gift card.


Cope.


Seriously, though, I hope it's beginning to make sense why flashback is such a difficult mechanic to develop. It looks so underwhelming on its surface but is actually just a massive, massive beating, because when you play a flashback card you're just playing a two-for-one *every single time*. Yet the resource-advantage is so well-hidden that its power doesn't become evident. This issue came to a head in *Innistrad* development, where lead developer Erik Lauer had to re-envision almost every single flashback spell.


The card that precipitated all of these changes was a reprint from *Odyssey*: [Morbid Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morbid+Hunger).


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld173_morbid.jpg)[Morbid Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morbid+Hunger) | Art by [Eric Peterson](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Eric+Peterson%22%5D)


[Morbid Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morbid+Hunger) was originally in the file for a number of reasons. The name and theme fit very well with *Innistrad's* Gothic horror motif. Most sets want a cheap efficient black removal spell and another ponderous yet more powerful black removal spell at a higher mana cost. [Morbid Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morbid+Hunger) fit the latter role admirably, and we thought it would be a neat throwback for people who remembered *Odyssey* Limited, as the card was a staple of that format. The problem was that most people didn't even *play* it in Draft or Sealed. 


![Morbid Hunger](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Morbid+Hunger)  
When you look at [Morbid Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morbid+Hunger), it's just very awkward. It costs six mana for an effect ([Essence Drain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Drain)) that's typically *splashable* at five mana. The reward for this extra cost? Eventually, for the low, low price of nine mana, you might get to cast that underwhelming spell yet again.


That reasoning sounds very plausible and is also totally, totally wrong. [Morbid Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morbid+Hunger) is an incredibly powerful spell in Limited and was probably the best or second-best black common in *Odyssey* Limited. Neutralizing two of your opponent's threats with a single card is just that good. Moreover, the life-gain aspect of the card actually allows you to get to the game state where you might use its flashback, so the card kind of combos with itself.


What kept happening was that the developers with Pro Tour experience kept slaughtering everyone else with our late-pick [Morbid Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morbid+Hunger)s when no one else was taking or even playing with them, and it just wasn't satisfying. I am a giant Spike. I love to win a game of **Magic: The Gathering**. But I derive no enjoyment when the reason I keep winning is not because of any aspect of myself or my ability to play the game, but because my opponent keeps evincing the same systemic lack of understanding over and over again. It's not a question of skill at that point; it's a question of information access. It can and will be remedied at some point, but that point hasn't happened yet. It's why I never felt powerful because I knew how to say "damage on the stack" when my opponent didn't.


It's like you're at a party, and your friend is telling a story, but you know the punch line already and so you're just not really listening. Everyone else laughs, but they aren't going to laugh when they hear the story the fourth time, and it's not really funny that fourth time either. It's kind of annoying and tedious and sad. "Oh, I get what's about to happen," you say to yourself, and you tune out. You've seen this interaction before.




|  |  |
| --- | --- |
| Silent Departure | Travel Preparations |

What Erik realized was that, inasmuch as it was possible, the flashback cards needed to consist of effects that were possible to cost in a way that was appealing. We didn't need a bunch of [Dark Banishing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing)s that you could cast again. This led us to cards like [Silent Departure](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Departure) and [Travel Preparations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Travel+Preparations) that, while very powerful, weren't rote, point-and-click two-for-ones. They still did things, and they did them well. But they had costs that made it evident why you'd want to play them, as opposed to requiring some kind of understanding of the inner-workings of game mechanics that force you to peek unpleasantly behind the curtain.


I hope this provides some insight into how we made an appealing mechanic appealing by giving ourselves the option to make it appealing. Join me next year when I talk about... things I can't talk about until next year!


Thanks for flashing back to flashback.


  







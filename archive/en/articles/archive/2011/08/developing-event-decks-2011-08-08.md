
---
[Link to Wayback Machine](https://web.archive.org/web/20220924154722/https://magic.wizards.com/en/articles/archive/developing-event-decks-2011-08-08)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "Magic is super fun. Yay! Awesome! Let's go play some Magic! Unfortunately, Magic is also super hard. Gah, jeez! I knew there was a catch! It's astounding how much of my job as a Magic: The Gathering game designer/developer can be summed up in these two facts. They're at the core of everything we do. Once people start to play Magic, overwhelmingly it becomes one of their"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "680801"
[_metadata_:publish_date]:- "2011-08-08"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Event Decks"
[_metadata_:wayback_capture_timestamp]:- "2022-09-24 15:47:22"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220924154722id_/https://magic.wizards.com/en/articles/archive/developing-event-decks-2011-08-08"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/developing-event-decks-2011-08-08"
---


Developing Event Decks
======================



 Posted in **Feature**
 on August 8, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 







M**agic** is super fun. Yay! Awesome! Let's go play some **Magic**!


Unfortunately, **Magic** is also super hard. Gah, jeez! I knew there was a catch!


It's astounding how much of my job as a **Magic: The Gathering** game designer/developer can be summed up in these two facts. They're at the core of everything we do.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/feature155_logo.jpg)Once people start to play **Magic**, overwhelmingly it becomes one of their favorite games—one of their favorite pastimes altogether, in fact. People that play **Magic** frequently identify as "**Magic** players" and devote a huge portion of their free time to understanding, learning about, and participating in our game. It's clear that once you get involved, the payoff is worth it. On the other hand, getting to that point isn't easy. **Magic** is complicated. There are hundreds of rules to memorize and thousands of cards to learn. There are single-player games, multiplayer games, Limited formats, Constructed formats, banned cards, restricted cards, cards that rotate in, cards that rotate out, and cards that aren't banned and haven't rotated but will still get you slapped by your friends if you choose to play them.


(I'm looking at you, Aaron Forsythe, and your [Plow Under](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plow+Under)s / [Smokestack](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smokestack)s / [Crucibles of Worlds](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crucible+of+Worlds) / [Sundering Titan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sundering+Titan)s.)


Point being, we have to pay a lot of attention to a) making sure that **Magic** remains fun once you play it, and b) giving you a reason to play **Magic** in the first place.


To make matters worse, a lot of the things that make **Magic** fun are things that make it harder to understand initially. This is true of basically every rule in every complex system ever, but **Magic** compounds this problem because its core mechanic involves cards whose very function is to break the rules you've been taught to obey. Draw one card per turn... unless you've cast [Divination](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination). Play one land per turn...unless you've cast [Exploration](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exploration) (or [Rampant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampant+Growth), or [Asuza, Lost but Seeking](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Asuza%2C+Lost+but+Seeking), or [Sakura-Tribe Scout](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Scout), or...)


Like I said, it's super hard.


But wait, there's more.


So you've figured out how to play **Magic**. Heck, you've done more than figure it out—you're the best player at your kitchen table. You know "the stack" is more than just a pile of pancakes. You can recite the text of a thousand cards like a teacher rattling off attendance. You make perfect attacks and effective blocks, and you can tell what cards your opponents are holding in their hands before they cast them. Maybe, you're thinking, I should branch out a little bit and test my skills against someone other than my three best friends.


Sounds awesome, right?


Okay, great. Where do I play?


Well, there's a store down the street and they host something called "Friday Night **Magic**." That's cool—I was going to chill with you guys this Friday anyway, so how about we just head up there instead of having to deal with the smell of Mike's cat and that irritating fluorescent light in the kitchen that sort of sputters when you're not looking at it in a manner eerily reminiscent of those Boo ghosts from Mario Brothers?


Awesome.


But what do I play?


Well, it says the format's "Standard," which I Googled and realized was the last two years' worth of cards. So I guess if we take Chad's black-red discard deck and cut the [Hypnotic Specter](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hypnotic+Specter)s we're good to go... for one of us. But we should all play. Not just Chad. I just... yeah, those [Mana Leak](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak)s from *Stronghold* I definitely know were reprinted, but that [Dismiss](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismiss) I'm not too sure about. [Cancel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) I am pretty sure is always around, but now that you mention it I'm not really sure how many lands I should be playing if we can't draw up to seven cards whenever we mulligan, and I read something about [Lightning Bolt](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) not coming back, so, right, um. I'm kind of confused.


And what on *Earth* is this business about "*sideboarding*?"


**Magic** is super hard.


 

We talk a lot on this website about how complexity, accessibility, and intuitive top-down resonance affect **Magic** set design. What we talk about a little less is how those attributes affect more than just the cards themselves. Our job as designers is to create an *experience* for the player, a meaningful interplay of game mechanics, creative expression, and play environment. We're constantly striving to improve that experience along every axis conceivable. Oftentimes, the way to do that is to create an entire product.


In this case, that product is the **Magic** Event Deck.


  
[![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_M12Decks.jpg)](/en/articles/archive/magic-2012-event-decks-2011-08-01)
[Click here for full deck lists](/en/articles/archive/magic-2012-event-decks-2011-08-01).


Event Decks were created to make it as easy as possible for someone to show up at Friday Night **Magic** and play in a tournament. And when I say "play," I don't just mean "register a legal deck." I mean have an actual game experience that communicates what it's like to really participate fully in FNM. Competitive cards. Competitive strategies. Competitive tactics, theories, and ideas. The concept behind the product was to remove every conceivable barrier possible to Friday Night **Magic** participation by allowing someone to show up empty-handed and, with a minimal amount of background knowledge, be participating in an event within ten minutes of arriving at the store. Are they going to automatically be wielding the best deck there? Probably not, but they are going to have something decent to start out with. And they'll figure out what works, and they'll decide if anything doesn't, and they'll have a direction to take their deck once they've logged a few rounds of game play under their belt.


Most importantly—we hope—they'll be having fun.


 [![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_NPHDecks.jpg)](/en/articles/archive/new-phyrexia-event-decks-deck-lists-2011-05-19)
[Click here for full deck lists](/en/articles/archive/new-phyrexia-event-decks-deck-lists-2011-05-19).


 

This article is about how we develop Event Decks, and why they look the way they do. As the guy who developed the *New Phyrexia* and ***Magic** 2012* Event Decks, I have some insight into this process. The other key player is Erik "The Mad Genius" Lauer, my colleague in R&D and one of the greatest Pro Tour deckbuilders of all time, who spearheaded the *Mirrodin Beseiged* Event Decks and guided the overall vision of the project. A lot of the principles I'm going to talk about arose from Erik's conception of what the product should be. If an idea sounds good, he probably came up with it.


 [![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_MBSDecks.jpg)](/en/articles/archive/mirrodin-besieged-event-decks-deck-lists-2011-02-16)
[Click here for full deck lists](/en/articles/archive/mirrodin-besieged-event-decks-deck-lists-2011-02-16).


### FNM


As stated before, the purpose of an Event Deck is to make it as easy as possible for someone to show up at FNM and play in a tournament. Why Friday Night **Magic**? We've found in our research that FNM is a great place for people who want to compete in a friendly environment without being overwhelmed by a ruthless, cutthroat, unforgiving gaming culture. It's natural to want to branch out into a bigger world, to test your skills and creativity against other people—or, more generally, to meet new friends inside the comfort of structured activity. To participate in a community.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_fnm.jpg)Point being, FNM is awesome, and we wanted to figure out a way to help people share in that experience. A lot of obstacles arise, though, that make that difficult.


For one thing, people don't like to be bad at things. This is a problem because **Magic**, even in a casual environment, is inherently competitive—the game terminates when a player wins or loses, so there's no way to get away from the fact that at some point you're going to have to battle the other people in the room. Competition establishes implicit social hierarchies, and it feels bad to lose over and over and over again. But **Magic** is difficult enough that you're not going to start winning unless you lose a bunch and learn from it. It's an unfortunate paradox—unless you have a little help.


### #winning


We knew it would be bad for everyone if Event Decks were the best decks in the format out of the box. People work very hard to innovate, to remain on the cutting edge of deck design, and if all of that effort was obliterated every time a new Event Deck came out, there'd be no point in doing it at all. More importantly, we would be doing something very wrong in R&D if the nine or so playtesters in our Standard "Future Future League" were able to perfectly predict metagames a year ahead of time (when these Event Decks are designed). Environments ought to be more robust than that. Even if Event Decks *were* the best possible decks in a given format, the metagame would adapt such that they weren't viable anymore—they would be, after all, a very easy target to hit—which would defeat the purpose of the product existing in the first place.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_M12Cards.jpg)So we knew the product couldn't be a microscopically tuned, impeccably engineered tournament crushing machine. We also knew, though, that they had to be tournament viable—that, in any given game, you had to have a decent chance of winning. This was very controversial at first, because we don't like to give the impression that we at Wizards of the Coast are building the players' decks for them. The thing is, though, nobody wants to be the person who shows up to a tournament with a deck that's just embarrassing. That feels bad, and when what we're selling is the idea that showing up at FNM is awesome and cool, there's no way that could work. Moreover, we knew that for this product to succeed, store owners and other players would have to be comfortable recommending Event Decks to newer players. We had to amp up the juice.


Every Event Deck you've seen, and every Event Deck in the pipeline, has been designed by someone whose decks have made Top 8 at Pro Tours. They understand how **Magic** deckbuilding works. Every Event Deck you've seen, and every Event Deck in the pipeline, is molded after decks that have seen either real-world or Future Future League success. Finally, every single Event Deck is rigorously playtested against a gauntlet of real-world and FFL archetypes, as well as against the other Event Decks.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_NPHCards.jpg)Now, FFL environments are designed to replicate high-level competitive play, and the real-world archetypes we playtest with are drawn from the Top 8s of Grand Prix, Pro Tours, and high-end independent tournament circuits. Friday Night **Magic** events aren't—and shouldn't be—that competitive. Still, because we want Event Decks to stand a chance in all Standard environments, we aim for them to win about 25% of games against our gauntlet of decks—bearing in mind that the gauntlet averages 50% of wins against itself by definition. This ensures that players get a real game-play experience, while a) allowing flexibility in deck customization should the players want to take their Event Deck in a new direction and b) not placing undue constraints on the environment.


At FNM? That 25% is going to be a lot higher, and we hear stories all the time of Event Decks winning store-level events with minimal modifications made to them. To that we say: keep up the good work!


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_MBSCards.jpg)A final detail: we don't want those 25% of game wins to come about because someone happens to play like an absolute master and is able to eke out advantage over the course of thirty turns, whereas the other 75% of losses emerge because the deck's five-part combo just fails to come together most of the time. We want the games to feel like games, which is to say we want to make sure that players are doing stuff, and we want the decks to win when the decks successfully do their thing. This is why a lot of our decks wind up being aggro decks: we don't expect everyone who opens one of these up to automatically be able to resolve [Gifts Ungiven](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven) perfectly every time they cast it. That requires a lot of time and energy and practice.


That said, there's a lot of sophistication to these bad boys. Properly managing [Pawn of Ulamog](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pawn+of+Ulamog) and [Bloodghast](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloodghast), or [Corpse Cur](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Corpse+Cur) recursion, or the perfect timing of a [Carrion Call](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carrion+Call), isn't easy. But you get better with practice.


### I'm Board


If **Magic** is super hard, sideboarding is super weird.


"So you have these decks... but you also have these cards that aren't in the decks. But they are in the decks because you can swap them into the decks between games. As long as you swap out other cards. So they're sort of in the decks. The idea is that they're good against certain decks and bad against others. They're good enough to play sometimes under the right conditions is what I'm saying. No, you can't play them in the first game ever. Even if you know what your opponent is playing. Oh, and don't forget to make sure you take them out of your deck after the match..."


Nevertheless, sideboarding is an essential element of tournament play. It allows skilled deck designers to accumulate massive edges from match-up to match-up, and ensures that a much wider variety of card types will be Constructed-viable every year.


Event Decks are designed with sideboards that are adaptable against a wide range of possible deck types, ensuring that you always have at least some tools at your disposal no matter what you face. They contain descriptions of sideboarding strategies and explanations of why you might want certain cards for certain matchups. They don't do all the work for you—the art of sideboarding involves paying careful attention to what you bring in and what you take out—but they should take a lot of the edge off how to make high-impact, and high-stress, last-minute cuts and additions.


### Medium Well


Maybe the easiest thing to notice about our Event Decks when compared to our other fixed-deck products is that they're packed full of really powerful rares!


When we were given the green light in R&D to include copies of the format's most potent tournament-level cards in these decks, we were a little taken aback. Were we really going to be allowed to do this? The entire point of creating Event Decks was to ensure that players could walk into a game store, buy a product, and play. If all we did was pack that product full of hotness, it couldn't possibly achieve its goal. Why not? Because it wouldn't just be appealing to the prospective FNM-er—it'd be the juiciest target for everybody! This would be great for us at Wizards—we'd have product flying off the shelf—but would be really bad for the person we're trying to reach with this product. Event Decks would never be in stock!


Because of that, we knew that we had to be judicious with how many format-defining rares we put in these products. Still, though, we wanted to push the limits. The *New Phyrexia* "War of Attrition" Event Deck—which approximates the [Puresteel Paladin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puresteel+Paladin) decks that are performing very well in Standard and Block Constructed right now—contains two copies of [Stoneforge Mystic](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stoneforge+Mystic), a card so powerful we banned it in Standard. Without revealing too much, I can say that our *Innistrad* and *Dark Ascension* event decks also contain cards we consider to be amongst the most powerful in their respective formats. These decks need to win games, and to do that, they require some of the best cards Standard has to offer.


### Strategy, Schmategy


So how do we decide which strategies to choose for a particular set's Event Decks?


One of the constraints a two-product release schedule per set places on us is that we chew up a lot of design space. That's eight Event Decks per calendar year. To put it in perspective, a lot of the time it's difficult to build eight viable Standard decks at any given moment with an unlimited card pool and no secondary constraints (i.e. in the real world it's totally okay to build a [Squadron Hawk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk) deck splashing black and a [Squadron Hawk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squadron+Hawk) deck splashing blue and call them different decks, but I would feel pretty bad releasing two of those and calling them different products). That's one of the reasons we take advantage of format rotation—of the reality that every single Event Deck is designed to be played inside a given three-month format, and when rotation happens you either a) modify your deck accordingly or b) pick up a new Event Deck.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_vamp.jpg)[Vampire Outcasts](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampire+Outcasts) | Art by [Clint Cearley](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Clint+Cearley%22%5D)


That's also one of the reasons that the contents of a given set's Event Decks vary widely in terms of how many cards they actually use of that particular set. With ***Magic** 2012*, I knew I wanted to take advantage of a lot of cool *Zendikar* block Vampires before they rotated out of Standard, since Event Decks weren't around during *Zendikar*'s release. That meant, though, that a lot of the deck wouldn't be legal after the release of *Innistrad*. To compensate for that, I knew I wanted for most of the blue deck to be legal after the rotation, and to take advantage of a lot of M12-specific cards. *New Phyrexia's* Event Decks, meanwhile, were much more evenly spaced when it comes to the frequency of *Zendikar* block versus *Scars* block cards.


As a general rule, then, we tend to prefer at least one linear, mostly aggressive strategy whose manabase can be made to work with minimal effort. The other strategy will likely be more set-specific and try to play up some interesting block themes. As formats get close to rotating, we're more likely to try and get one last hurrah out of the previous block's Constructed All-Star list, whereas earlier in a set's lifespan we're more likely to explore themes that have the opportunity to grow more robust with each release.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feature155_illusion.jpg)[Lord of the Unreal](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+the+Unreal) | Art by [Jason Chan](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Jason+Chan%22%5D)


Most importantly, though, we want our decks to be capable of winning games, and we want them to be fun. That's why you're likely to see fewer thematic or set-specific tie-ins with this product than with others. When *Betrayers of Kamigawa* is released (for example), it doesn't necessarily follow that Standard will be defined by *Betrayers of Kamigawa* cards—and the same is true for our Event Decks. Think of them more as decks we believe will be interesting to play when they're released.


### Y'all Come Back Now, Y'hear!


Hopefully, this article has given you an interesting look into the creative process behind Event Deck design and development. If you're stroking your chin, gazing at your computer screen through a monocle, and murmuring, "Mmhmm, mmhmm," then I hope it's given your brain something to gnaw on. Please post on the forums with your insights, analyses, critical appraisals of our playtest methodologies, and musings on Kripkean semantics as viewed through the lens of predicate logic.


If, though, you're someone who's itching to play **Magic**, I hope this encourages you to get out and battle. And if you're new to FNM—maybe you've heard of it, seen an ad for it somewhere, have been a little nervous about actually attending yourself—go ahead and pick up an Event Deck. Play some games. I bet you'll have at least a single smidgen of fun.










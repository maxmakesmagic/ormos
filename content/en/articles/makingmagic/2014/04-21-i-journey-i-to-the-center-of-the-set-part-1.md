---
id: x5xhaem9
kind: article
lang: en
path: /en/articles/makingmagic/2014/04-21-i-journey-i-to-the-center-of-the-set-part-1
title: <i>Journey</i> to the Center of the Set, Part 1
published: '2014-04-21'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
    lang_detected: en
    capture_id: 221284
    url: https://magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
    captured_at: '2024-05-18 03:36:26+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
    lang_detected: en
    capture_id: 221284
    url: https://magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
    captured_at: '2024-05-18 03:36:26+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
    lang_detected: en
    capture_id: 221284
    url: https://magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
    captured_at: '2024-05-18 03:36:26+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
    lang_detected: en
    capture_id: 221284
    url: https://magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
    captured_at: '2024-05-18 03:36:26+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: x5xhaem9
  url: https://magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
  page_key: magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:36:26+00'
  capture_id: 221284
  wayback_url: https://web.archive.org/web/20240518033626id_/https://magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: x5xhaem9
  capture_id: 221284
  url: https://magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
  wayback_url: https://web.archive.org/web/20240518033626id_/https://magic.wizards.com/en/news/making-magic/journey-center-set-part-1-2014-04-21-0
  captured_at: '2024-05-18 03:36:26+00'
  template: contentful
  sha256: 7b41ecfcc1ad8a23e569aa37ab971d97baa4d671c4cf6c6bd77567c3d56121b3
render_recovery: []
---
After preview weeks, I like to spend an article or two (it's going to be two in this case) talking about design stories of individual cards and cycles. As I have a lot of stories to get to, let's not waste a lot of time with my thesis paragraph.

![](https://i.ormos.uk/50/b7/50b7949bc8b10f37396f23873feecdaaee4e9a0387a24cb8f2937413ba6418c2.jpg)

This card will probably confuse some people when they first see it. Hexproof on a white card. Isn't hexproof a green and blue thing? It is. Well, what's it doing on a white card? For starters, it's not normal hexproof. The creature doesn't have hexproof. It gives hexproof... to you, its controller.

Most creature abilities cannot be given to players (I actually try from time to time and most often I'm told no) so this was a weird case. Here's how it works when design teams or development teams make something that's a little off the beaten color pie path: they tend to come to me as the color-pie guru and ask my advice on what color they should be. Sometimes, they have a color in mind and they're seeing if I agree with them. Sometimes, they have a card and are just trying to figure what color to make it.

I believe this discussion went a little something like this:

> **Them**: Mark, can you tell me what color this is?  
> **Me**: Sure.  
> **Them**: A creature that grants hexproof to you, the player.  
> **Me**: You're giving hexproof to a player?  
> **Them**: Yes.  
> **Me**: That's white. The precedent is [Ivory Mask](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ivory+Mask), last seen in *Ninth Edition*, which gave you, the player, shroud. Basically the same thing, flavorwise.  
> **Them**: So white?  
> **Me**: Yep, white.  
> **Them**: Thank you.

![](https://i.ormos.uk/9e/55/9e55161371a7b7f7bec5861a6552aa2bab9caa000795d4533071aa63398af499.jpg)

The plan had always been from pretty early on that Ajani was going to show up in the third act of the story, which means the third set. The fact that the leonin are on *Theros* (and, as many people have pointed, out they are one of the few things not from Greek mythology) was partly because we liked that *Theros* had a lot of qualities that would make Ajani feel somewhat at home.

Ajani marks the tenth and final two-color combination to show up on a Planeswalker. I'm sure a lot of people are curious if he was made green-white specifically because we didn't have one yet. The answer is "sort of." Let me walk you through what happened. We knew we wanted Ajani. We also knew the protagonist was going to be Elspeth.

While the creative team chooses which characters are going to be represented as Planeswalkers, they have to work with development to make sure there is a good color balance. The existence of a mono-white Elspeth—and the creative team really wanted her mono-white (in general, it's nice if the protagonist is monocolor to help him or her get more visibility by showing up in a greater number of decks)—meant it was awkward if a second Planeswalker was mono-white. Note that it is something we could do if we have to but it did raise some red flags.

As the team started looking at options for a two-color Ajani, there weren't a lot that made sense. Also, the team was aware that green-white was going to be the last combination ([Kiora, the Crashing Wave](https://web.archive.org/web/20140421000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Kiora%252C%2Bthe%2BCrashing%2BWave) was the second-to-last, fulfilling the green-blue void) to appear on a Planeswalker, and green-white fit the flavor well. This meant that green-white solved our problems while also allowing us to deliver something we know players had been asking for.

![](https://i.ormos.uk/bb/c5/bbc5ab4b05ff0a5af0ee05be3a97f7ce9b18ac48627e8decce17f71715f0a1d7.jpg)

*Arabian Nights*, the first **Magic** expansion, had the following card in it:

![924](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=924)

The flavor of the card was that you locked a creature away in a jail and it stayed locked away until someone destroyed the cell. I'm not quite sure why it was an enchantment or why it was black, but it was one of my favorite cards from the set.

Years later, while working on the design of *Lorwyn*, I felt it was time to finally redo the card but in the color it was always meant to be in, white. Black doesn't lock things away. Black just kills things. White, the color with the strong moral center, is the one that doesn't want to kill if it doesn't have to. Also, I'm a huge fan of white being the color that has answers with answers. Anyway, it turned out as this card:

![139414](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=139414)

The card hit in a good spot and for many years we kept reprinting it. Unfortunately, it had one small issue. You see, the way the card technically works, it has an "enters the battlefield" trigger and a "leaves the battlefield" trigger. The first trigger removes the nonland permanent and the second one returns it. So if you play [Oblivion Ring](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) and then immediately destroy it, you can make it such that the leaves-play trigger happens before the enters-the-battlefield trigger. All of this is a fancy way of saying, if you manipulate things, you can make it such that the nonland permanent exiled never returns.

This is very non-intuitive and not at all the intent of the card. We tried playing around with the rules but we couldn't find a way to close up that loophole without causing other problems, so the solution was to come up with a new template and then just make a new version of [Oblivion Ring](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring). Well, here we are. [Oblivion Ring](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) 2.0.

![](https://i.ormos.uk/43/54/4354b2f45aaae32d602a96d4c79bbbbeb7702b16f124a7c0b36d2fce89fdf030.jpg)

Atlas was one of the titans that Zeus and company managed to overthrow in their coup of Olympus. As a punishment, Atlas was forced to hold up the celestial sphere (i.e., the world). If you've ever seen a Greek mythological person with the Earth on his shoulders, that's Atlas. And yes, the word "atlas" is named after him.

Anyway, how could we do a Greek set without making an Atlas card? We tried a couple of different versions throughout *Theros* and *Born of the Gods* and *Journey into Nyx* but this is the one that made it to print. I really do like the flavor that if something happens to "Atlas," the whole world comes tumbling down.

![](https://i.ormos.uk/f4/ed/f4ed4761db2bd64d5308b76a619c246f6d3aa030dd597c23ce532d69d0d66c48.jpg)  
*Crystalline Nautilus, Sightless Brawler, Gnarled Scarhide, Mogis's Warhound, Spirespine*

One of the things we try to do as a block advances is take mechanics unique to that block and evolve them. Bestow is probably the showiest mechanic in the block, so we got a lot of players asking for us to do different things with it. The most popular request was to make some bestow creatures you might want to put on your opponent's creature. It turns out this is a little trickier than you might think.

Advanced planning had stumbled across the idea of bestow creatures you put onto your opponent's creatures. As the third set was going to be a battle between the gods and the denizens, saving the bestow for opponents for the last set where the gods would be actively trying to stop the denizens felt right. All *Journey into Nyx* had to do was design a few.

Here was the first problem. All of the bestow cards in *Theros* and *Born of the Gods* grant power and toughness boosts that match the power and toughness of the bestow creature. It was going to be difficult to make things you were willing to bestow on your opponent's creatures if it gave them stat boosts. So, the first version we made didn't give stat boosts, but whenever we playtested the cards we kept getting the same feedback. Why were these bestow creatures different from the rest?

We finally decided the only way to do them was to give the stat bonuses but have them come with some negatives substantial enough that you would still be willing to do it. The key was to create a balance, so you would sometimes put them on your creature and sometimes put them on the opponent's. That meant that there tended to be two abilities, a significant power/toughness boost and a drawback.

Crystalline Nexus is a good example of this model: +4/+4 is a substantial boost, so you are tempted to put it on your creature, but the "illusion ability" (formerly known as the "skulking ability"—the creature is sacrificed when targeted) would tempt you to put it onto your opponent's creature when you have the means to kill it.

These five cards are a five-card cycle at uncommon.

![](https://i.ormos.uk/cc/e9/cce9259fe499490e5d1518938bff0eb4d656519f5a2e5b3a25649bdb0749ada7.jpg)

We do plenty of top-down designs, but Deicide is a little different than most. This was a top-down story moment. (I'll leave you all to piece together what exactly is going on in this card.) It started because we knew we wanted to show a particular story moment in the illustration of a card. That card concept is where we started the design.

From the card concept, we got the name Deicide, and then we designed a card to mechanically do exactly that—kill a God. As the Gods are all indestructible enchantment creatures, we chose to make it a card that exiled enchantments. Then to hit home the theme, we added a [Lobotomy](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lobotomy) rider if you happen to kill a god ([Lobotomy](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lobotomy) was a card from *Tempest* that removes a card and then also removes all copies of it from the game.)

Development likes to make sure that every strategy has a counter strategy, so it was nice that we could create an answer for Gods while also creating a very memorable card to highlight a key story moment.

![](https://i.ormos.uk/32/aa/32aa3fbe9679446b996c583bb37fc9d6f26516ae7bd4f27bc1339518a6498f59.jpg)

One of the things that's interesting to watch is how design and development evolve over the years. Here's the pattern: We experiment and try something new. If that something new works, we do it again. With continued success, we start to build it into our process.

This card is an example of how we've rethought our approach to Draft archetypes. Back in the day, we'd create themes and kind of let them loose, crisscrossing in whatever ways they did. With time, we realized Draft was better if we baked the Draft archetypes into the design. Part of doing this was helping create cards that would give direction. A simple way to do this, as most Draft archetypes are two colors, is to make multicolor cards, usually at uncommon, that point in the direction of the archetype.

For example, in *Theros* Block Draft, we made red and white the aggro heroic deck. In *Journey into Nyx*, as we started segmenting the gods and the denizens, we enabled players to get even more aggressive, going either all-god or all-denizen. In red and white, this meant finding a way to enhance the already draftable red-white aggro heroic deck.

Desperate Stand was created as a card specifically to point red-white down this path. If you take this card as your first pick, it gives you a very clear direction of what deck you might want to build. The twist with *Journey into Nyx* is that there are now more cards that allow a strategy of drafting numerous heroic creatures. Before *Journey into Nyx*, the deck only needed a few heroic creatures, as the deck was limited in how many ways it could target creatures. With the introduction of strive, the deck now can justify a higher percentage of heroic creatures.

The lesson is the importance of guidance cards, often in both colors of the deck archetype, that can help solidify a strategy early in the first pack.

![](https://i.ormos.uk/ad/2d/ad2d7214acb100df519dbec7b35ff78381dca023df02fbb09b4e84bd2a0a5e2d.jpg)  
*Dictate of Heliod, Dictate of Kruphix, Dictate of Erebos, Dictate of the Twin Gods, Dictate of Karametra*

*Journey into Nyx* is the first set of the *Theros* block to have noncreature, non-Aura enchantments. These five cards are a rare cycle making use of these global enchantments. Each of them is a classic enchantment effect with the extra twist of having flash. Different enchantments make use of the flash differently.

Dictate of Heliod uses its flash to surprise the opponent, usually mid-combat, buffing your entire team.

Dictate of Kruphix uses the flash to offset the global effect by allowing you to cast it on your opponent's turn, letting you draw the first card.

Dictate of Erebos uses its flash to allow you to respond to the effect that is about to kill a creature so you can get the enchantment on the battlefield in time to trigger.

Dictate of the Twin Gods uses flash to allow you play the enchantment after your opponent has committed, or not committed, to blocking.

Dictate of Karametra is similar to Dictate of Kruphix in that it creates a global effect that flash allows you to access first.

I really enjoy how this cycle takes very simple, basic enchantment effects and, just by adding one small element—one word even—makes them play very differently.

![](https://i.ormos.uk/3c/62/3c6275c8d9a2a764c7a9f74525ce9fa2555d457f71a16a9e410c1f696f7d4398.jpg)

About two seconds after I accepted that we were going to finally do an enchantment block, the first thought in my mind was, "Hmm, what's our enchantress going to be?" For those unfamiliar, let me show you this card from Alpha:

![178](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=178)

Richard Garfield made it clear from day one that green liked enchantments. The [Verduran Enchantress](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Verduran+Enchantress) was so popular that it created a mini-archetype for **Magic**, the green creature that loves enchantments.

<table><tbody><tr><td><div><div><img alt="Argothian Enchantress" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Argothian+Enchantress"></div></div></td><td><div><div><img alt="Yavimaya Enchantress" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Yavimaya+Enchantress"></div></div></td></tr></tbody></table>

Of all the effects, the one players enjoyed the most was the card drawing. It was simple, powerful, and full of flavor. Once I knew we were going to have enchantment creatures, I realized that we could make an even better enchantress because we could make one that was also an enchantment. This allowed you to overcome the one previous weakness, which was that having to play enchantresses in your deck kept you from making your entire deck enchantments.

The "enchantress" went through many iterations but it was always an enchantment creature that allowed you to draw cards when you played enchantments. I believe the first one even predated the constellation mechanic, although once that was added to the set, it was clear that the card had to make use of the mechanic.

Throughout the block, I got a lot of complaints from players who had expected an "enchantment matters" theme. The very reason we held it back was because we knew it was going to be a pent-up demand that we could fulfill in the third set, but that meant I had to answer a lot of questions that basically started with, "Where's the enchantment-matter cards?"

While answering these questions, I just kept thinking about the Eidolon of Blossoms and said to myself that one day you'd be happy. That is, by the way, why I led with this card as [my first preview](/en/articles/makingmagic/2014/04-07-the-incredible-journey-part-1) on the first day of showing off *Journey into Nyx*. I hope many decks get built around it.

![](https://i.ormos.uk/0a/17/0a170339433e67527d1b611a8e80e956d5ef87d22c07b1b58dbe7fcf664e3592.jpg)

This was the very first card in the set. I, in fact, made it before *Journey into Nyx* design even started. I knew two things. One, there was going to be a battle between the gods and the denizens of the world and, two, we were saving "enchantment matters" for the last set. With that in mind, I designed the following card.

> Wrath of the Gods  
> 4WW  
> Sorcery  
> Destroy all nonenchantment creatures.

I'm pretty sure it all started with the name. I loved that name. Deep in my heart, I was hoping that there was some way I could convince everyone that we should keep it. I knew its chances were small. We tend not to make card names too similar to one another, but I really liked it.

So what would a Wrath of the Gods do? Well, [Wrath of God](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) destroyed all the creatures, so that was a start. But these "Gods" were the gods of *Theros*. The spell had to reflect that. Well, what if they only went after the denizens and not their own creations? Mechanically that would be easy, as every god-related creature was an enchantment creature. Okay, destroy all creatures except the enchantment creatures.

I gave the card to Ethan and I believe he made the *Journey into Nyx* file in Multiverse (our card database) just to have somewhere to put it. Wrath of the Gods stayed as is for the complete duration of the design. During development, it was decided that the card would do more good in black so it was moved. Once the card was no longer in white, the name parallel made less sense (not that it was going to stay anyway) and it received a new name.

I'm happy the card made it to print and, as far as I'm concerned, its nickname is Wrath of the Gods.

![](https://i.ormos.uk/32/73/32735d0132361e8720050d717ea365d1e2bf805f10263b276748fdff259a6aa9.jpg)

One of our goals for *Theros* block was to support a Minotaur tribal theme. To accomplish this, we did a few things. First we put Minotaurs into a second color (black, chosen by the creative team because they wanted the Minotaurs to have more of a cruel streak). Second, we made sure the block would have a whole bunch of Minotaurs. Third, we made a number of Minotaur tribal cards, a number of which were lords (that is, creatures that granted abilities to all your Minotaurs).

Earlier in the block, we gave you lords that buffed your team's stats and allowed you to attack aggressively. Felhide Petrifier is just us giving you a different kind of Minotaur lord. Granting deathtouch can be useful but in a new way. It's by giving players a bunch of different options we allow players to have more choices in how to play their Minotaurs.

![](https://i.ormos.uk/b7/b2/b7b2cea431ec84e1b68c4c6ec5c73bf036ddc9ce79023f92bf9869e2051fbf47.jpg)

This set uses enchantments in a bunch of different ways. One new thing (for *Theros* block, anyway) is the use of what we call seals. [Seals](https://web.archive.org/web/20140421000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+%5BSeal%5D+%5Bof%5D) are essentially instants that you can pay for up front and then use at your leisure by sacrificing them. They are particularly useful in this set because of the "enchantment matters" theme. For example, Font of Fortunes is essentially a [Divination](https://web.archive.org/web/20140421000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination) but with more utility in *Journey into Nyx*.

One of the big debates is that R&D is a bit mixed about the use of seals. A big part of having instants and sorceries is to add hidden information to the game and seals take away a lot of that game play, but the "enchantment matters" theme was so key to the set that we decided we could make an exception and include some seals.

![](https://i.ormos.uk/12/e4/12e456fd5714628e7c5a9a3bebd484784d8f93c9701c19e8f36ff2a7ea7f05fc.jpg)

There are a few cards that show off the design point I want to make, but only one of them is an Octopus (by the way, please read all the flavor text in this set—[Kiora, the Crashing Wave](https://web.archive.org/web/20140421000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Kiora%252C%2Bthe%2BCrashing%2BWave) is a hoot). Originally, this card could only attack if your opponent controlled an enchantment. Always on the lookout to find ways to make Auras better, especially in this block, I suggested we add one more possibility. What if the creature could also attack if your opponent controlled an enchanted permanent?

This way, you had some control of your destiny. Without this rider, you were at the mercy of your opponent playing an enchantment. True, it's hard to avoid playing enchantments in *Theros* Block Limited but people might also want to play this card in other, most-likely casual, formats. The rider now gives you a reason to want to play enchantments in your deck and that felt like a nice upgrade for only adding four words.

![](https://i.ormos.uk/56/16/5616d43dbe231b9297b747e47ebca4f7467ef4456fcaecc1bed5bfd0971bbe1c.jpg)

So it was decided that Elspeth needed a weapon, and a very potent one at that. The weapon came from Heliod, so it had to be white. It needed to seem powerful, so we gave it a big power/toughness boost. It had to be capable of killing a God, so we gave it an ability that exiled any creature blocking or blocked by the equipped creature. Finally, as the card was already exiling creatures, we added one more ability to make sure things killed by the Godsend stayed dead. Hopefully, some of you will know the true rush of wielding Godsend.

### The End of the *Journey*

That's all the time we have for today. I hope you enjoyed my romp through some of the cards from *Journey into Nyx*. As I stopped at G, I'll be back in two weeks with Part 2 of my card-by-card stories. As always, I'm eager to hear your thoughts on my thoughts. You can reply through the email link at the bottom of the page, respond in the thread to this column, or contact me through one of my many social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro#)).

Join me next week when my head will be in the stars.

  

* * *

  

### Drive to Work #114 & 115  
20 Things That Were Going to Kill Magic, Parts 1 & 2

For 20th Anniversary Week last year, [I wrote an article](/en/articles/makingmagic/2013/08-05-twenty-things-that-were-going-to-kill-magic) that examined twenty of the biggest controversies in **Magic**'s history. In a two-podcast series, I examine in detail those twenty events.

  

*   [**Episode 115**](https://media.ormos.uk/68/22/68229b67c1516b27d2607d4a2acff8feb107685a1b3b389c897e27d9b3e18890.mp3) : *20 Things That Were Going to Kill Magic, Part 2* (22.8 MB)
*   [**Episode 114**](https://media.ormos.uk/7e/c8/7ec8ebc8acadfeafe6f24d4aef4e744083b63b63fd583a5e6f20becec7f193d9.mp3) : *20 Things That Were Going to Kill Magic, Part 1* (20.8 MB)
*   [**Episode 113**](https://media.ormos.uk/e2/70/e270e00033927a7c50cd4174c481484105e76f9a61d2af716064866fcce00efe.mp3) : *Day in the Life* (14.7 MB)
*   [**Episode 112**](https://media.ormos.uk/fc/3e/fc3ebcd61496483f6caab03107fc490845ff858ba41d11ecc1ce6f73faa95cb7.mp3) : *1998* (13.3 MB)
*   [**Episode 111**](https://media.ormos.uk/03/b0/03b0e447f681f0eb27f8cc8f7ab109cfd4215acf91440dab08f93475765758a5.mp3) : *Judgment, Part 3* (13.6 MB)  

*   [**Complete Drive To Work Podcast Archive**](/en/articles/makingmagic/undated/drive-to-work-podcast-archive)
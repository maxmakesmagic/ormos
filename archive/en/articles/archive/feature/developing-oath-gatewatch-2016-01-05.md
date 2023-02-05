
---
[Link to Wayback Machine](https://web.archive.org/web/20160108202332/http://magic.wizards.com/en/articles/archive/feature/developing-oath-gatewatch-2016-01-05)

[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/developing-oath-gatewatch-2016-01-05"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160108202332id_/http://magic.wizards.com/en/articles/archive/feature/developing-oath-gatewatch-2016-01-05"
[_metadata_:wayback_capture_timestamp]:- "2016-01-08 20:23:32+00:00"
[_metadata_:description]:- "Ian's team overcame many challenges while developing Oath of the Gatewatch, and he's here to share a few cards that adversity inspired."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Developing Oath of the Gatewatch
================================



 Posted in **Feature**
 on January 5, 2016 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_ianduke.jpg)
By Ian Duke




Ian Duke is a developer in Magic R&D and has been with Wizards of the Coast since 2012. A gift of an Ice Age starter deck in 1995 sparked Ian's lifelong passion for Magic. He also enjoys math, physics, board games, and puzzles. To the surprise of few, his favorite guild is Azorius. 






Hello everyone, Ian Duke here! In addition to moonlighting as a Pro Tour commentator, my main job here at Wizards is as a senior game designer on the development team for *Magic* R&D. All the members of the development team work on every *Magic* set in some capacity, but *Oath of the Gatewatch* is very special to me, as it marks the first Standard-legal main booster release for which I led the development of the set. If you enjoyed some of my previous work on *Commander (2014 Edition)*, *Vintage Masters*, and *Tempest Remastered*, you can expect more great things coming your way from this new set.


*Magic* R&D's development group is responsible for the final design and balance design of each set. We receive a handoff from the design group (for this set, led by Ethan Fleischer) that includes a fully populated card file, a general set structure, mechanics, and a vision for the set, and then we go to work iterating on it, polishing it, balancing it, and generally making it as fun to play as possible.


Developing a set is a lot more than just changing numbers and casting costs. While a design handoff always includes a tremendous number of awesome ideas and exciting card designs, as we iterate more on the set we find things that aren't working as originally envisioned or simply need more fleshing out. Sometimes individual card designs or entire strategies need to be redesigned or rethought. Today I'll share with you some of the challenges my team and I went up against in developing *Oath of the Gatewatch*, and you'll get to see three new preview cards that emerged from conquering those challenges.


Colorless Mana
==============


Without a doubt, the biggest challenge in working on *Oath of the Gatewatch* was the new colorless mana mechanic, by which I mean casting costs and ability costs that require colorless mana to use. Ethan and I had discussed the mechanic early in the predesign stage (before the actual set design began), and we both agreed that the mechanic was ambitious and would be challenging to execute on, but would ultimately be worth it. It's not often that a mechanic comes up that makes you sit up and say "What!? Wow!" but is also relatively easy to understand and is backward- and forward-compatible with the rest of *Magic*.


So why was colorless mana going to be so hard? There are several reasons, but they basically boil down to getting the mechanic to play well in Limited, and then separately making cool Constructed-level designs that inspire players to build new decks that work well and are at the right power level. Let's think about those together, one at a time.


Limited Access
==============


In Limited, meaning Sealed Deck and Booster Draft, the trouble all stems from mana bases. A typical Limited deck is two colors and plays a 9-8 split of the two corresponding basic land types. Occasionally, if you have a powerful card or two in a third color, you might "splash" it and play an 8-7-2 land split. However, even a minor splash like that has a huge impact on the consistency of your deck, and you'll start to lose some games simply from drawing the wrong lands to match your spells. Adding cards that cost colorless mana to cast is a lot like splashing a third color in your deck. We worried that, without us taking proper care, mana bases would be too difficult to build or simply wouldn't work.


![](https://media.wizards.com/2015/images/daily/cardart_OGW_Unknown-Shores.jpg)


[Unknown Shores](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unknown+Shores) | Art by [Jung Park](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Jung+Park%22%5D)


Ethan's big innovation was to make most of the colorless mana costs at the common/uncommon level on activated abilities of colored creatures. As an example, imagine a 3/2 creature that costs 2B to cast and has an activated ability for C to give it some temporary boost. This card plays perfectly fine in a deck with only a few colorless mana sources (or even none). It won't be stuck in your hand waiting for you to draw your one [Blighted Fen](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blighted+Fen). You can simply cast it on turn three, and if you find access to colorless mana at some point in the game, it's all upside.


Through that piece of design technology, it meant we were asking a lot less of you for adding colorless mana costs to your deck. You could simply play these cards in an otherwise normal deck with a few incidental sources of colorless mana and things would work just fine.


On the flip side of the rarity spectrum, we could design uncommons, rares, and mythic rares that *required* you to have colorless mana to cast them, but that were powerful and exciting and actually worth compromising your mana base to cast. (Feel free to scroll down for a peek at one if you can't help yourself!)


Meanwhile, we also infused the set with a number of nonland colorless mana sources to help you in "splashing" colorless into your deck. Some are creatures, focused primarily in black and blue (the main colors that pair with colorless mana). Others are artifacts. Green takes advantage of Wastes being a basic land, with cards that can search your library to find it. And of course, Eldrazi Scions can also produce colorless mana in a pinch.


By the end of the process, we were pretty happy with the amount of colorless mana production and how "free" it was to include in your deck. I do hope that players enjoy the deck-building challenge of finding the right amount and the right kinds of colorless mana sources for their decks, and I think it makes for a really exciting and unique Booster Draft experience.


As an aside, I'd like to answer one of the most popular questions I've been asked about the format. Why decide not to allow players to add any number of Wastes to their decks? Why limit players to what they open in their sealed pool or pick in a draft?


First, the decision wasn't clear-cut, and it was something I strongly considered. But there are a number of reasons not to do it that way. Taken all together, it was compelling to try to avoid that solution if possible, and I think we were able to. Here are some of the reasons not to allow players to add any number of Wastes to their decks.


1. Logistics. We'd have to ensure that there were always enough to go around. It wouldn't be fair to say players can add an unlimited number of Wastes and then have them run out. This is particularly tricky at the store level, where it would mean replacing land stations or sending supplementary Wastes packs to every local game store in the world. If they didn't arrive on time, or they ran out, or a store misjudged how many they needed, they wouldn't be able to hold any more *OGW* drafts. That would be sad. Would it have been possible to do this? Yes, but it's not an ideal solution.
2. Wastes aren't the only colorless mana sources in the format. Not even close. Not only is it not necessary to have several Wastes in your deck, it wouldn't even be correct to do that if you could. You're much better off building your deck with a couple lands that produce colorless mana, maybe that also have special abilities, and rounding things out with some creatures, artifacts, and Eldrazi Scions as your other colorless sources.
3. To that end, we were worried inexperienced players could be led astray in how they build their mana bases. By limiting the number of colorless lands to what you open in a draft, we prevent a situation where an inexperienced player adds, say, six or seven Wastes to their deck and then gets color hosed every round. We actually saw behavior lean in this direction in internal playtesting, so even if you think, "Well, I would never do that!" maybe the player next to you would, and that wouldn't be a great experience. Remember that we can control the math of how many sources of colorless mana are opened in a draft (on average) by tuning up and down the number of sources and their rarities. Dialing that number to just the right level helps ensure that players don't overdo it to their own detriment.
4. Colorless cards could be stronger. By asking players to make some sacrifices and correctly prioritize colorless sources in Draft, it let us make the colorless cards stronger and more exciting.
5. It helped differentiate the experience from simply splashing a color in your deck. There's something way cooler about sacrificing that key Eldrazi Scion to cast Kozilek on the crucial turn than adding some Plains and a couple white cards to your deck.
6. It's fun! Having to draft colorless sources is a fun challenge, and something unlike what most Booster Draft formats offer. While it's not something we would want to do for every set, *Magic* is an ever-changing experience, and I think it added a lot of unique texture and depth to the format.

An Overstuffed Pie
==================


So how about Constructed? In a similar way, we wanted to make sure that adding colorless mana cards to a deck was worth it, as far as constructing a mana base was concerned. We got a lot of help here from the pain lands in *Magic Origins*, and in fact, knowing that colorless mana was going to be a major theme of *Oath of the Gatewatch* was a big reason why we chose to reprint them there. We didn't want "mono-colorless" to be the only deck that used colorless mana cards, and so just like for Limited we made sure to include some powerful colored cards with colorless mana abilities.


But what about the cards with colorless mana in their actual casting costs? Surely these incentivize players to build very colorless-heavy decks, and we wanted to make sure to deliver on this promise. To that end, we have a number of powerful colorless-producing lands and a variety of powerful colorless mana cards to support more dedicated colorless decks. Check this one out:


![](https://media.wizards.com/2015/ogw_239nCi30ks3/en_vCqQtH2Nnr.png)


This Eldrazi is no joke! I like to think of this one as part [Thundermaw Hellkite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thundermaw+Hellkite), part [Thunderbreak Regent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thunderbreak+Regent), and part [Blightning](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightning). As a five-mana 5/5 with haste and evasion (fun fact: R&D considers trample to be in the category of evasion abilities, which I never thought about before coming here but makes perfect sense), this Eldrazi hits hard and fast. To top it off, its protective ability ensures that you'll usually get a two-for-one even if your opponent already has a removal spell. Plus, if your opponent's hand is empty, not even a topdecked removal spell will do the trick!


So what's with that wacky discard-if-you-target-me ability? Well, one of the challenges with making Constructed-level colorless cards is that we didn't want them to feel like they could have been any single color. It turns out this is tough, because *Magic*'s five colors have pretty neatly parceled out the game's design space. It's not like we were saving a hidden area of card design for 20 years just in case we decided to add a new non-color to the game! With that challenge in mind, we tried to design powerful colorless cards that did unique things—things that couldn't easily be matched up with what any one color would do.


The other tricky thing with colorless mana is that if we wanted it to be in an interesting spot for Constructed play, we needed the (relatively) small number of cards with colorless costs in *Oath of the Gatewatch* to be competitive with the 200-ish cards each of the five colors has access to in Standard. That meant every colorless design counted in terms of pushing the theme to a competitive Constructed level. My hope is that you'll find a lot of interesting Constructed shots in the set at a variety of different casting costs. I'm excited to see what cool decks you all can brew up!


A Different Kind of Planeswalker
================================


Designing planeswalker cards is one of my favorite things to do here in *Magic* R&D. They are always some of the most important cards in each set, and there's a lot of pressure to hit the right level of "Wow!" factor. It's an awesome challenge.


The behind-the-scenes side of creating planeswalkers is an immense linear algebra–style puzzle. With six sets in Standard at once, we need to make sure we're not overlapping too much in color, casting cost, ability suites, or unique characters. After all, there's only room in most decks for three to six planeswalker cards or so. If we have multiple cards sitting on top of one another (for example, two four-casting-cost mono-red planeswalkers), chances are one will bully the other out of seeing Standard play. When choices about what planeswalker to play are clear-cut direct comparisons, the decisions are less interesting and there's less for players to explore.


With *Oath of the Gatewatch*, I set out to do something a little different with the set's planeswalker cards. I wanted them to fill holes that weren't already being filled and also weren't likely to compete with future planeswalkers we'd want to make in upcoming sets. In particular, I was really intrigued with the idea of making a "big red" planeswalker. The only high-mana-cost red planeswalkers we'd attempted before were [Sarkhan, the Dragonspeaker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sarkhan%2C+the+Dragonspeaker) and [Chandra Ablaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Ablaze). While I think Sarkhan ended up in a good spot for Standard, as a player I found [Chandra Ablaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Ablaze) interesting but ultimately disappointing in power level.


Within R&D, red's role in the color pie is a frequently debated topic. In an effort to make red feel passionate, impulsive, and aggressive, the color often ends up gravitating toward a singular strategy of all-in rush-down. The problem is that red cards don't lend themselves toward playing a long game, so once you start putting red cards in your deck you just want more red cards, and then you end up nearly mono-red. Traditionally, there hasn't been much reason for adding red to midrange or control decks, aside from maybe a few efficient creature-removal burn spells or maybe a multicolored spell.


That is, until now.


![](https://media.wizards.com/2015/ogw_239nCi30ks3/en_l9Z8PERHSF.png)


Say hello to your new win-condition, red decks. Chandra encapsulates everything red is about—dealing damage, impulsively throwing away your hand for new random cards, and, well, dealing more damage! But it does so in a way that doesn't force you to go all in on burning your opponent out and doesn't preclude you from playing other colors in your deck.


Let's check out her abilities. Her -X ability can get you out of a heap of trouble, sometimes sweeping the board of opposing creatures and leaving you with a six-mana planeswalker still alive. From there, you have the option of card selection and card advantage with her second ability, or simply ending the game very quickly with a +1 ability that deals 6 damage. What other planeswalker has had a *plus* to deal *6 damage*! She's also great at taking down other planeswalkers; because her plus creates two tokens, the damage can't be easily chump-blocked, and she gets to go up in loyalty while knocking opposing planeswalkers down.


If you're not sure what deck you want to add Chandra to just yet, don't worry! That's part of the point. Like I said, my goal was to create a card that lends itself to a strategy unlike what traditional red decks have done, while still playing in a very red way. I hope you enjoy brewing around this powerful planeswalker as much as we did.


Taking the Oath
===============


As much as *Oath of the Gatewatch* is about building on *Battle for Zendikar*, with the emergence of Kozilek and his brood, more cool and bizarre Eldrazi, and the new colorless mana mechanic, it is also a set very much about teamwork. *Oath of the Gatewatch* marks a major story moment, where the Zendikari people band together with a team of powerful Planeswalkers to attempt to finally end the Eldrazi threat once and for all. Ethan and his team sought to infuse the set with the feeling of banding together to defeat a common enemy.


To that end, you'll find a very special group of cards in this set called the Oaths. Each Oath is a legendary enchantment that represents a powerful Planeswalker committing him or herself to your cause. From a mechanical standpoint, each Oath has a spell-like enters-the-battlefield effect, and then gives a lasting bonus relating to planeswalker cards. Let's introduce one of them, and then I'll talk about how they came to be.


![](https://media.wizards.com/2015/ogw_239nCi30ks3/en_2sIH5M9IAk.png)


At base level, Chandra's oath is like a 1R burn spell that deals 3 damage to a creature. A very solid effect, but maybe not quite a powerhouse on its own. However, with a few planeswalkers in your deck, over the course of a game it can get up to [Searing Blaze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Blaze) levels or better—and that card is one of the strongest burn spells in Modern!


Our goal with the Oaths is to straddle the line between being awesome in a super friends–style planeswalker-heavy deck but also being strong enough in a more typical Constructed deck that plays three to five planeswalker cards. To that end, we put a healthy amount of power into the enters-the-battlefield abilities, so each Oath is already pretty useful even if you haven't drawn a planeswalker yet. But over the course of a few turns, if you deploy one or two planeswalkers, they'll end up adding a lot of value to your strategy.


Until Next Time
===============


I hope you enjoyed this tour through just a few of the challenges and decisions that went into making *Oath of the Gatewatch*. This is an ambitious set, and it brings a lot of new content to explore. As it's my first Standard-legal set, I'm really interested to see how players enjoy it and get feedback on what worked well and what didn't. My goal is to continue to make *Magic* as awesome of an experience as I can for you all, so definitely let me know [on Twitter](http://www.twitter.com/mtg_ianduke) what you do and don't like about the set.


Be sure to check out coverage of Pro Tour *Oath of the Gatewatch* in Atlanta, Georgia, February 5–7. You'll see some of the strongest players in the world take a crack at solving *Oath of the Gatewatch* Limited and playing Modern. As always, I'll be there doing commentary for our broadcast on [twitch.tv/magic](http://www.twitch.tv/magic). For now, it's time for me to get back to the future, making next year's *Magic* even more awesome than this one's. Thanks for joining me!








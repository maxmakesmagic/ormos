---
id: ym81axqs
kind: article
lang: en
path: /en/articles/makingmagic/2013/10-14-drawing-attention
title: Drawing Attention
published: '2013-10-14'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
    lang_detected: en
    capture_id: 215052
    url: https://magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
    captured_at: '2024-05-18 03:44:39+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
    lang_detected: en
    capture_id: 215052
    url: https://magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
    captured_at: '2024-05-18 03:44:39+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
    lang_detected: en
    capture_id: 215052
    url: https://magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
    captured_at: '2024-05-18 03:44:39+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
    lang_detected: en
    capture_id: 215052
    url: https://magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
    captured_at: '2024-05-18 03:44:39+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: ym81axqs
  url: https://magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
  page_key: magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:44:39+00'
  capture_id: 215052
  wayback_url: https://web.archive.org/web/20240518034439id_/https://magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
- document_id: ym81axqs
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/269
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/269
  lang: en
  template: aspx
  captured_at: '2014-02-19 06:21:34+00'
  capture_id: 652104
  wayback_url: https://web.archive.org/web/20140219062134id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/269
- document_id: ym81axqs
  url: https://magic.wizards.com/en/articles/archive/making-magic/drawing-attention-2013-10-10
  page_key: magic.wizards.com/en/articles/archive/making-magic/drawing-attention-2013-10-10
  lang: en
  template: drupal
  captured_at: '2022-10-03 10:39:10+00'
  capture_id: 877331
  wayback_url: https://web.archive.org/web/20221003103910id_/https://magic.wizards.com/en/articles/archive/making-magic/drawing-attention-2013-10-10
- document_id: ym81axqs
  url: https://magic.wizards.com/en/articles/archive/making-magic/drawing-attention-2013-10-14
  page_key: magic.wizards.com/en/articles/archive/making-magic/drawing-attention-2013-10-14
  lang: en
  template: drupal
  captured_at: '2022-01-28 23:06:24+00'
  capture_id: 877343
  wayback_url: https://web.archive.org/web/20220128230624id_/https://magic.wizards.com/en/articles/archive/making-magic/drawing-attention-2013-10-14
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ym81axqs
  capture_id: 215052
  url: https://magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
  wayback_url: https://web.archive.org/web/20240518034439id_/https://magic.wizards.com/en/news/making-magic/drawing-attention-2013-10-14
  captured_at: '2024-05-18 03:44:39+00'
  template: contentful
  sha256: 810210ba66911fb7cf9975695ad2bf6439522513a843bb93023f4a08f64cdedc
render_recovery: []
---
Today's article came from an interesting place. I have a preview card to show off from the upcoming *Commander* (2013 Edition) and while looking at it to figure out what I wanted to say about it, I got an idea for a column. The column, though, has nothing to do with *Commander* (2013 Edition). The card just got me thinking about a topic that I've been meaning to write about for years.

So, I'm going to start by showing you the card and then I'm going to veer off in what I hope is an interesting direction. Note that two weeks from now is Commander Week, and I promise, during that article, I'll talk about the design of *Commander* (2013 Edition) and introduce you to the design team. Without any further ado, let's get to the preview card.

World, I would like to introduce you to Baleful Force:

\>> Click to Show

![](https://i.ormos.uk/e2/9d/e29d5d1668b2fce933143866c434babc2d9f0d97fa66d6356d88dbd1bf5a9c70.jpg)

So what topic did this preview card inspire me to write about? A mechanic that's about as basic as it gets—card drawing. I want to explore what role it plays in the game and how we use it in design. I will walk us through its place in the color wheel and talk about the positives and negatives it brings to design. Hopefully, by article's end you'll think about card drawing in a slightly different light.

![](https://i.ormos.uk/7e/11/7e11fcd9bb1cbae5ac4036df6b17ed90fef077a9c1338451d877b9e5603bc16b.png)

### Luck of the Draw

At its core, **Magic** is a game of resources, of which you start with two: life and cards. Your life is frontloaded, you get it all up front, but cards get doled out to you over the course of the game. Why is that? Why is life given out all at once but cards are not? Understanding this is key to grasping the role that cards have on the game.

**#1: Cards Are the Lifeblood of the Game**

![](https://i.ormos.uk/04/dd/04dd4ffc671739c5d43bfbeb78f03f7805d91476a5eb8f89b2a2bff56a504c3b.png)

Life and cards have two different functions. Life serves as the win condition of the game. It exists so the players have a goal. (See my column on "[Ten Things Every Game Needs](https://web.archive.org/web/20131014000000/https://magic.wizards.com/en/node/654461)" for more on why you need a goal.) Cards, on the other hand, are the access to all the other resources in the game. Cards provide lands, which provide mana, which is the costing system. Cards also provide spells, which are the means to accomplish the goal.

Because the cards are the lifeblood of the game, they are doled out to make sure that something new has the potential to happen each turn. The card draw happens early in the turn because you want to frontload the information of what is new to allow it to have maximum impact on the turn.

**#2: Options Need to be Controlled**

![](https://i.ormos.uk/07/3e/073e23647b8d71a317e42d5e2a5528f83970a02440886b4b645aa1a7f65d5a99.png)

I'm often asked why the game starts with a seven-card hand. Enough people inquired that a number of years ago I posed the question to Richard Garfield. Richard replied that finding the right number was a question of balancing getting enough cards to provide interesting game decisions with limiting information as to not cause decision paralysis.

The idea was that you want the game to start out with fewer decisions to help the first few turns go quickly and then branch out as the game progresses. Seven was a logically place to start, as it's one of the more common starting hand sizes in card games. Richard said he tried other numbers but seven always felt the best.

This then begets the next question: Why does **Magic** draw one card per turn? I also asked Richard this. His answer was twofold. First, most card games have you draw a single card a turn, so it plays into player's expectations. Second, he felt it provided the right amount of card flow. Much like the opening hand, you want enough to make sure that each turn gets new material to affect game play without creating too much complexity.

**#3: It Helps Define the Turn**

![](https://i.ormos.uk/59/86/5986eaa0e746380d603e95d80d34bd07854234a398f48a02ac127fe872f48867.png)

I like to talk about how the human brain works. The brain likes to break down information into small bits and then link them together into connected strands. The end result of this is that people are happiest when any process is broken down into small, regular chunks. When you study the act of creating, you learn that there is a structure followed to provide comfort for the user. In games, this tends to be the turn.

Card drawing does a good job of helping define the turn and make each turn feel like a piece of the whole. In fact, when teaching the game, new players like to grasp onto the parts of the turn because it is something orderly for them to focus on. An important part of this is that the start of the turn (and, yes, technically, there are a few things that come before this) is the card draw. It's a nice, clean action that delineates the end of one person's turn with the beginning of the next person's.

**#4: It Keeps a Steady Stream of Surprise**

![](https://i.ormos.uk/3f/a3/3fa32862b3132529f604cb832935584a60a3a557d2de516533b9e5d0ca4ea5b4.png)

In [my article on communications theory](/en/articles/makingmagic/2013/06-03-communications-theory), I talked about how people need comfort, surprise, and completion. In games, this means that the players need to have things that are familiar and know the parameters of what they need to win. It also means that there needs to be some information that they are not aware of. (I even list surprise as one of [the ten things every games needs](https://web.archive.org/web/20131014000000/https://magic.wizards.com/en/node/654461) in my article on the topic.)

One of the ways to guarantee that there is hidden information is to constantly provide a flow of new cards. This is importance in two ways. First, it just gives the players new options, which will allow the game to shift in different directions. Second, because a player does not know what he or she is going to draw, it adds a dynamic to game play where players have to make assumptions on what could come next, which leads to cool moments.

**#5: It Adds Excitement**

![](https://i.ormos.uk/af/1f/af1fb071c9cb602678d176d0c025d2ff6353003016dfaa2623d801b66c71f80f.png)

The unknown is exciting because it has the potential to be whatever you want it to be. A big part of creating fun (and remember, that's the end goal for a game designer—making the game something enjoyable for the people playing it) is doing things that lead to emotional highs and lows. The card drawing encapsulates this concept perfectly. You always need something, so each draw comes with the promise of something wonderful. When you get it, you are very happy. When you don't, there is an equal emotional rush. This ensures that each turn has a moment of drama.

### Mmm... Color Pie

![](https://i.ormos.uk/49/6a/496a636813bfd2f142590fd73df02af43cec9362c3cecdd472bdff4b539107b4.png)

Now that I've explained why card drawing is so important to the game, let's examine how, as a mechanic, it is actually used. Because the core of the game is the color pie, I thought the best way to examine this is to look at how each color makes use of card drawing.

**All Colors**

Some things are so fundamental to the game that we allow each color to have some access to it. The tool we've provided to all the colors is what we call a cantrip. First introduced in [*Ice Age*](https://web.archive.org/web/20131014000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=+%5B%22Ice+Age%22%5D&text=+%5Bdraw%5D+%5Bcard%5D+%5Bupkeep%5D) (although those versions delayed the draw to the start of the next turn), the cantrip is the attaching of a card draw onto a spell effect. Most often, cantrips are used as a costing method to make effects normally too small to work on cards. They have many other uses, though. For example, sometimes a set wants more card flow to allow a higher volume of spells to get cast or to get more cards into the graveyard. Cantrips are available to every color in whatever volume they need.

**Blue**

![](https://i.ormos.uk/44/84/44840109b0b2900c8606d560b20766741c53731562f297d5f66c6529a3144c9d.png)

I'm starting with blue because blue is king of card drawing. The hand and the library are a metaphor for knowledge (the former being what you currently are thinking of while the latter is the entirety of what you know) so card drawing is a perfect fit. Here are the various card-drawing abilities we give to blue:

**Card drawing:** This is straight-up, take some number of cards from your library and put them into your hand.

**Card filtering:** This is a variant on card drawing where you draw more cards but only get to choose to keep a subset of them. The remaining cards usually are either put into the graveyard are put onto the bottom of the library.

**"Looting":** This is drawing some number of cards, although usually one, and then discarding a number equal to what you drew. Looting almost always goes to the graveyard.

**"Curiosity":** This is a creature ability where you draw a card when the creature deals combat damage to another player. There is a variant of this ability we do at high rarities where you get to draw a card for each point of combat damage that creature deals.

**Death-trigger draw:** This is a creature ability that draws you a card when the creature dies.

**Tutoring:** This is when you go into your library and get a particular card. Sometimes, the choice of the card is restricted. There are also variants where you pick a larger number of cards and interact with your opponent in a way where you end up with less than all the cards.

**Regrowing:** This is when you return a card from your graveyard to your hand. In blue, this usually gets you back instants and sometimes sorceries.

**Green**

![](https://i.ormos.uk/5d/4f/5d4fcf252560d0efdba1b7ea4112afb7b2d8c8aaac84938f078430f56688cfbc.png)

The color with the next most access to card drawing is green. Green uses card drawing as a metaphor for growth. Usually, green's card drawing is tied to its creatures. Here are the various card drawing cards for green:

**"Curiosity":** Blue is primary in this ability and green is secondary.

**Card drawing:** Most green card drawing ties directly into one or more of its creatures. Usually, the amount of cards drawn is tied to a power or toughness of one of your creatures or the total number of all, or sometimes a particular subset, of your creatures.

**Land fetching:** Green has the ability to go into the library to specifically get lands. Sometimes they go to the hand and sometimes they go onto the battlefield.

**Creature cantrips:** While all colors get cantrips and all colors can have creature cantrips, this is something done much more in green than any other color.

**Regrowing:** Green is primary in the ability to get back any type of card from the graveyard. It tends to do this at higher rarities, occasionally at uncommon.

**Creature tutoring:** Other than lands (see above), green tutors but only specifically for creature cards. Some variants of this ability will put the creature directly onto the battlefield instead of into the hand.

**Black**

![](https://i.ormos.uk/25/cd/25cd50ebd36345aba175a1dfea2ccd7c4568f47883c8cdc5724bfcc27365e988.png)

Black is third in card drawing. Here is the various ways it draws cards:

**Card drawing:** Black's card drawing always comes with a payment of some kind in addition to the mana. The most common payment is life, but black will sacrifice things from time to time instead.

**Tutoring:** Black, along with blue, is the color that can tutor for any card from the library.

**Regrowing:** Black has the ability to put creature cards from its graveyard into its hand. It can sometimes instead put the creature onto the battlefield. This latter ability is known as reanimating. There are also some black creatures that have the ability to return themselves from the graveyard to the battlefield.

**Death-trigger draw:** This ability is primary in blue, but black dips its toe into it occasionally.

**Red**

![](https://i.ormos.uk/02/8e/028e7b801f6f5f0f77722ef7dcdce7cdc64c666114bf0f71297744296fec0879.png)

Red is number four in this category, although it doesn't do a lot.

**"Looting":** Red has its own form of looting, what R&D calls "red looting" and many players call "rummaging," where it discards before it draws. Every once in a while, these cards are templated such that you can draw cards, and gain card advantage, on an empty hand.

**"Impulsive draw":** This is an ability we've started doing in red, where red gets to draw cards (technically, it exiles them) but only has access to cast them for the rest of the turn. The cards that are not cast remain lost in exile. R&D sometimes refer to this as the "Elkin ability," referring to the cards [Elkin Bottle](https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Bottle) and [Elkin Lair](https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Lair) with this ability.

**Regrowing:** There are three types of cards red can get back from the graveyard. First, it's allowed to regrow sorceries. This isn't used often, and is mainly kept for sets that care about the graveyard or sorceries. Second, some direct-damage spells have conditions by which you can get them back from the graveyard. Third, red has [Phoenixes that can return themselves](https://web.archive.org/web/20131014000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+%5BPhoenix%5D&color=+%5BR%5D&text=+%5Bgraveyard%5D)—often requiring mana. The phoenixes sometimes return to the hand and sometimes return to the battlefield.

**White**

![](https://i.ormos.uk/db/b4/dbb4322b99fc839eac5d57055517a744a872eff21565831121d24e053d52b46f.png)

White is the low color on the card-drawing totem pole. It does even less than red:

**Regrowing:** White can get back artifacts and enchantments from the graveyard to its hand. On rare occasion, it can put them onto the battlefield. It can also regrow small creatures, usually defined as converted mana cost of 2 or less, but every once in a while it's defined by a low power level.

**Tutoring:** White can occasionally tutor for enchantments and less often for artifacts, usually Equipment.

This, of course, begs the question, why is white worst at card drawing? The answer is that white is the color that has the most answers, so one of its weaknesses is that it has the worst card flow. If it could too easily draw cards, it would be able to answer every problem. One of the way white's enemies can get ahead of it is through card advantage.

### On the Draw

So, card drawing does much good for the game and we've managed to weave it through all of the color pie. What's holding R&D back from using it as much as we can? To answer this question, I present the restricted list from [Vintage](https://web.archive.org/web/20140517160307/http://www.wizards.com/Magic/Magazine/Article.aspx?x=judge/resources/sfrvintage). These are cards that are problematic in the format where you can use every card in **Magic** (minus a few bothersome ante, subgame, and physical-dexterity cards).

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall">Ancestral Recall</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotus+Petal">Lotus Petal</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strip+Mine">Strip Mine</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance">Balance</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Crypt">Mana Crypt</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thirst+for+Knowledge">Thirst for Knowledge</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Lotus">Black Lotus</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Vault">Mana Vault</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Vault">Time Vault</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm">Brainstorm</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memory+Jar">Memory Jar</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk">Time Walk</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Channel">Channel</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll">Merchant Scroll</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Timetwister">Timetwister</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Consultation">Demonic Consultation</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind%27s+Desire">Mind's Desire</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tinker">Tinker</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Tutor">Demonic Tutor</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Emerald">Mox Emerald</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolarian+Academy">Tolarian Academy</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fastbond">Fastbond</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Jet">Mox Jet</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinisphere">Trinisphere</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash">Flash</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Pearl">Mox Pearl</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampiric+Tutor">Vampiric Tutor</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven">Gifts Ungiven</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Ruby">Mox Ruby</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wheel+of+Fortune">Wheel of Fortune</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imperial+Seal">Imperial Seal</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mox+Sapphire">Mox Sapphire</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Windfall">Windfall</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Library+of+Alexandria">Library of Alexandria</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Tutor">Mystical Tutor</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Bargain">Yawgmoth's Bargain</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lion%27s+Eye+Diamond">Lion's Eye Diamond</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence">Necropotence</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Will">Yawgmoth's Will</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder">Ponder</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sol+Ring">Sol Ring</a></td><td> </td></tr></tbody></table>

Let's start by removing the cards that allow you to get mana quickly (fifteen cards in all), leaving us with this:

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall">Ancestral Recall</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder">Ponder</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance">Balance</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strip+Mine">Strip Mine</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm">Brainstorm</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thirst+for+Knowledge">Thirst for Knowledge</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Consultation">Demonic Consultation</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Vault">Time Vault</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Tutor">Demonic Tutor</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk">Time Walk</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash">Flash</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Timetwister">Timetwister</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven">Gifts Ungiven</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tinker">Tinker</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imperial+Seal">Imperial Seal</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trinisphere">Trinisphere</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Library+of+Alexandria">Library of Alexandria</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampiric+Tutor">Vampiric Tutor</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memory+Jar">Memory Jar</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wheel+of+Fortune">Wheel of Fortune</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll">Merchant Scroll</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Windfall">Windfall</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind%27s+Desire">Mind's Desire</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Bargain">Yawgmoth's Bargain</a></td></tr><tr><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence">Necropotence</a></td><td><a href="https://web.archive.org/web/20131014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Will">Yawgmoth's Will</a></td></tr></tbody></table>

What remains is twenty-six cards. *Twenty-two* of them essentially draw you cards. That's the problem. Card drawing is so vital to the game that a little too much of it can break the game. In fact, one of the most common notes I get in "devign" (the overlap period between design and development) is "Too much card drawing."

What this means is that you have to be careful with how you use card drawing in design because it is a resource that you have to allocate. Note, by the way, that not all card drawing is the same. Cards that draw cards but cannot net the player card advantage (i.e., allow them to end up with more cards than they started with) are nowhere near as dangerous and thus can be used more liberally.

The keys I have found to deal with card drawing in design is twofold.

First, we have learned to be more aware of what is and isn't card drawing. As I demonstrated above, there are a lot of things that actually are card drawing but might not seem like it at first glance. Second, we try to make sure that we spread around the card drawing into different places so that it's diffused. Sometimes this is done with color, and sometimes it is done with functionality. The former works because the mana system makes it hard to play too many colors. The latter works by making cards that have different functionalities and thus want to go into different kinds of decks.

The other thing we've learned to do in design is to better understand what role card drawing plays in the current design. While card drawing is obviously always useful, it actually plays different roles in different blocks. For example, in *Innistrad*, there was a milling subtheme, so we had to be aware that certain card-drawing cards would occasionally double as tools to finish off an opponent or to fill up your graveyard.

In *Theros*, by contrast, the block has what we call a Voltron subtheme—that is, we encourage players to take creatures and build them up into larger threats. We provided a lot of synergy but we needed the card flow to ensure that the combinations would come up. This is why scry got added to the environment, to make sure players were drawing the things they needed to make the synergies work.

The reason this topic is relevant is because even after eighteen years of doing this job, understanding card draw in design is still something I'm learning. For instance, the scry example from above wasn't done by design, but by development. It's a complex topic but something I find fascinating.

### Draw to a Conclusion

![](https://i.ormos.uk/b5/cb/b5cb5c503755e1133eb31eadabe433e4e71fc7bf9062219bba7463bda0f3f81e.png)

I hope you enjoyed today's article. Sometimes, to understand how things work, you have to dig in and look at the tiniest components. If you have any thoughts about the topic you would like to share with me, feel free to email me through the link below, respond to the thread of this column, or contact me through any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts)).

Join me next week when I get heroic.

Until then, may you realize that there is still a lot left to learn.

### Drive to Work #60 – Comfort and #61 – Surprise

As I still haven't caught up, I decided to keep posting two podcasts a week for the month of October.

This week's two podcasts are Parts 1 and 2 of my podcast on Communications Theory, something I wrote about in [an article earlier this year](/en/articles/makingmagic/2013/06-03-communications-theory).

*   [**Episode 61**](https://media.ormos.uk/57/93/5793202daffbd93e084011f034bcee06baaf62a75c42fdd9157a0832393b4ab5.mp3) : *Surprise* (10.2 MB)
*   [**Episode 60**](https://media.ormos.uk/2f/b6/2fb61a14ecb9458ad81bd7d4f31343d437697b774ed04ccb3e79f3b2473142b2.mp3) : *Comfort* (13.4 MB)
*   [**Episode 59**](https://media.ormos.uk/1a/6d/1a6d8ef40d37f572fc9710c429c6d2b586e2b38579b44b6454efcfecd50296c4.mp3) : *Champions of Kamigawa, Part 3* (14.5 MB)
*   [**Episode 58**](https://media.ormos.uk/20/d3/20d358251b1e78f0bcf820e36100464858c140e71786bc8c757f08e9bb998512.mp3) : *Champions of Kamigawa, Part 2* (10.7 MB)
*   [**Episode 57**](https://media.ormos.uk/5b/91/5b91d6e550007959a1a4de7aab71ce7d8cb6e6d6bb443880ef288144a433be85.mp3) : *Champions of Kamigawa, Part 1* (14.5 MB)  

*   [**Complete Drive To Work Podcast Archive**](/en/articles/makingmagic/undated/drive-to-work-podcast-archive)
---
id: 5nyky1nt
kind: article
lang: en
path: /en/articles/makingmagic/2002/11-04-to-infinity-and-beyond
title: To Infinity and Beyond
published: '2002-11-04'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
    lang_detected: en
    capture_id: 221157
    url: https://magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
    captured_at: '2024-05-20 04:59:28+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
    lang_detected: en
    capture_id: 221157
    url: https://magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
    captured_at: '2024-05-20 04:59:28+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
    lang_detected: en
    capture_id: 221157
    url: https://magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
    captured_at: '2024-05-20 04:59:28+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
    lang_detected: en
    capture_id: 221157
    url: https://magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
    captured_at: '2024-05-20 04:59:28+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 5nyky1nt
  url: https://magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
  page_key: magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
  lang: en
  template: contentful
  captured_at: '2024-05-20 04:59:28+00'
  capture_id: 221157
  wayback_url: https://web.archive.org/web/20240520045928id_/https://magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
- document_id: 5nyky1nt
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr45
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr45
  lang: en
  template: aspx
  captured_at: '2013-02-12 05:47:21+00'
  capture_id: 803700
  wayback_url: https://web.archive.org/web/20130212054721id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr45
- document_id: 5nyky1nt
  url: https://magic.wizards.com/en/articles/archive/making-magic/infinity-and-beyond-2002-11-04-0
  page_key: magic.wizards.com/en/articles/archive/making-magic/infinity-and-beyond-2002-11-04-0
  lang: en
  template: drupal
  captured_at: '2022-10-07 23:12:49+00'
  capture_id: 890346
  wayback_url: https://web.archive.org/web/20221007231249id_/https://magic.wizards.com/en/articles/archive/making-magic/infinity-and-beyond-2002-11-04-0
- document_id: 5nyky1nt
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr45
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr45
  lang: en
  template: classic_asp
  captured_at: '2005-04-05 00:53:50+00'
  capture_id: 1978540
  wayback_url: https://web.archive.org/web/20050405005350id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr45
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 5nyky1nt
  capture_id: 221157
  url: https://magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
  wayback_url: https://web.archive.org/web/20240520045928id_/https://magic.wizards.com/en/news/making-magic/infinity-and-beyond-2002-11-04-0
  captured_at: '2024-05-20 04:59:28+00'
  template: contentful
  sha256: 654f6021e170f862b4e812060f4d18499f3fdc2cde863e4a53eb8ef0f3cf3c56
render_recovery: []
---
Welcometo Mana Engine Week! This week we’ll be exploring card combinations that allow you to create an endless amount of mana. As many of our other writers will explore this week, there’s quite a number of such combos. As for me, I thought I’d use my column to answer a number of common design questions connected to "infinite" mana engines.

<table><tbody><tr><td><br><i><a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Power+Artifact">Power Artifact</a>/<a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grim+Monolith">Grim Monolith</a>: One of the easiest mana engines to play.</i></td></tr></tbody></table>

### Question #1 – Why do you create infinite combos?

First, let me state that I can only talk about how I design cards, but I do feel that my answers will give insight into the overall design process. So, while I’m using “I” there is a hint of “we” behind it.

The answer is that I don’t create infinite combos. At least not in the way that most of you think. Design is about creating open-ended cards. I focus more on the individual cards that the card combinations. The best way to explain this is to use a metaphor (and as long time readers will attest, I do love my metaphors). I like to think of designers as tool-makers. Our job is to make interesting and useful tools. Our job isn’t to use the tools. That’s the job of craftsmen (a.k.a. all of you). It’s important that we understand what the craftsmen want so that we can maximize the usefulness of our tools, but in the end we focus our energy in making the better hammer rather than thinking of new ways to use the hammer.

As a designer, my responsibility to combos lies in the word “open-ended.” What do I mean by that? It means that I design cards to have synergy with other cards. Not specific cards but general types of cards. I want our tools to click together with other tools. But I do not sit around thinking what exact tools each new tool will click together with. In fact, part of the excitement for the designers is to see what the world will do with their cards when they get their hands on them.

A good example is the card [Hand to Hand](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hand+to+Hand) from *Tempest* (click on the words “Hand to Hand” if you don’t know what it does). I designed the card to be a “don’t mess with my guys in combat” card. In tournament play though, it got used as a sideboard card in red decks that was brought in against certain white decks. Since abilities couldn’t be activated during combat it kept players from activating their [Circle of Protection: Red](https://web.archive.org/web/20021104000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Circle%2Bof%2BProtection%253A%2BRed). Did I have this idea in mind when I created the card? No. Did I mind the shift in usage? Absolutely not. I was actually pleased that the public found a way to use the card that I had never thought of.

Design, by nature, is just not deck-oriented. The reason for this is the modular design of trading card games. Trading card games live and die by the ability for the cards to intermix in interesting combinations. In order to maximize this, it’s important that the designers create cards that have maximum interactivity. Thus, when I create a card, I don’t spend a great deal of time figuring out what deck will use the card. I just make generally useful cards and assume that players will find uses for them. This doesn’t mean every card will find a tournament-worthy use. And as I’ve explained in my bad card article (“[When Cards Go Bad](https://web.archive.org/web/20021104000000/http://archive.wizards.com/default.asp?x=mtgcom/daily/mr5)”), not every card will find a deck. But open-ended design increases the flexibility of the cards.

In summary, I (as a designer) am responsible for combos in that I make cards that work well with other cards, but I don’t generally design two cards specifically to combo together.

### Question #2 – Do you like infinite combos? Are you happy they exist?

The answer to this question varies a bit in R&D, so I’ll give you my take. I like infinite combos… in moderation. As I’ve explained before, **Magic** is broken up into different types of players (“[Timmy, Johnny, and Spike](/en/articles/makingmagic/2002/03-11-timmy-johnny-and-spike)”). I believe infinite combos are good for Johnny and bad for Spike. Johnny has fun seeing what he can do with a **Magic** deck. Spike merely wants to win. Infinite combos provide Johnny with the ability to do bizarre and cool things. Infinite combos in Spike’s hands can cause problems. Let me explain.

There are two types of combo decks: what I’ll call fast combo and slow combo. Fast combo decks win by getting the combo off quicker than the opponent can do anything about it. As such, it turns **Magic** into a game of solitaire. **Magic** is supposed to have player interaction, so when fast combos get played, the game gets less fun. The best example of this was a period in 1998 called “Combo Winter.” Certain degenerate cards in the *Urza’s Saga* block created an environment where games could be won in one or two turns. (One of the most famous stories of that time involved Brian Hacker playing only a [Gustha's Scepter](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gustha%27s+Scepter) on the first turn, and winning the game on the second turn.) The joke at the time was the **Magic** game had shifted. The early game was the flipping of the coin to see who would go first. The mid-game was drawing your opening hand and deciding whether to mulligan. And the end game was the first turn.

Slow combos work very much like permission decks. Players have to gain control of the game. Once they do, they use the combo to win. I think slow combos can be fun and they don’t take the interactive element away from the game. The only problem with certain slow combos is that they take too long to win. What this means is that infinite combos, with a few exceptions listed above, are generally a problem when aimed at Spike. Thus, R&D tends to focus these types of cards more at Johnny and less at Spike. Occasionally, Spike will find uses for them, but when they do, they’re costed non-aggressively enough that they become slow combos and not fast combos.

<table><tbody><tr><td><br><i>A nice slow combo: <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carnival+of+Souls">Carnival of Souls</a>, <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Contemplation">Contemplation</a>, <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tortured+Existence">Tortured Existence</a>, <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashnod%27s+Altar">Ashnod's Altar</a>, <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Initiates+of+the+Ebon+Hand">Initiates of the Ebon Hand</a>, <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter">Ornithopter</a>, and <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Basking+Rootwalla">Basking Rootwalla</a>. Talk amongst yourselves.</i></td></tr></tbody></table>

### Question #3 – How do you design infinite combo cards?

While we don’t specifically set out to design combo cards, we do design cards that are what I would call “combo enablers.” These are cards that have an increased chance of creating combos. I’ll break up the cards into four categories:

**Engine Cards**

Engine cards are cards that allow you to convert one resource into another. More often than not, engine cards are permanents, but not always. Some past examples of engine cards:

*   [Channel](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Channel) – trades life for mana
*   [Necroptence](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necroptence) – trades life for cards
*   [Cadaverous Bloom](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cadaverous+Bloom) – trades cards for mana
*   [Treasure Trove](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treasure+Trove) – trades mana for cards
*   [Peace of Mind](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Peace+of+Mind) – trades cards (and mana) for life
*   [Dream Halls](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dream+Halls) – trades cards for, well, just about anything
*   [Earthcraft](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earthcraft) – trades creature utility for mana
*   [Mind over Matter](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+over+Matter) – trades cards for mana/utility
*   [Squandered Resources](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squandered+Resources) – trades long term mana for greater short term mana

<table><tbody><tr><td><br><i>Three powerful &quot;engine&quot; cards: <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cadaverous+Bloom">Cadaverous Bloom</a>, <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earthcraft">Earthcraft</a>, and <a href="https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+over+Matter">Mind over Matter</a>.</i></td></tr></tbody></table>

The reason engine cards are combo enablers is that they tend to feed off one another. Many infinite combos are created by exchanging the same resources back and forth netting some bonus in the exchange. As a designer, I have a particular affinity for engine cards and as thus have made more than my share.

**Tutors**

Tutors are cards that allow you to search your library for a particular card. They are important to infinite combos (and combos in general) because the allow players to collect all the pieces for their combo. Examples of past tutors: (most of which have Tutor in their name)

*   [Demonic Tutor](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Tutor)
*   [Mystical Tutor](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Tutor)
*   [Enlightened Tutor](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enlightened+Tutor)
*   [Merchant Scroll](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll)
*   [Crop Rotation](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crop+Rotation)

**Card Drawing Cards**

These cards are sort of a cross between engine cards and tutor cards. They allow you to convert mana into cards (the engine part) in order to get access to your combo pieces (the tutor part). Examples of past card drawers:

*   [Ancestral Recall](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall)
*   [Braingeyser](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Braingeyser)
*   [Prosperity](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prosperity)
*   [Stroke of Genius](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stroke+of+Genius)
*   [Jayemdae Tome](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jayemdae+Tome)

**Mana Generators**

These are cards that help you speed up your mana. They enable combos as they let you get out expensive engine cards and card drawers earlier than normal. Some past examples of mana accelerators:

*   [Black Lotus](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Lotus)
*   [Mana Vault](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Vault)
*   [Dark Ritual](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual)
*   [Priest of Titania](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Priest+of+Titania)
*   [Tolarian Academy](https://web.archive.org/web/20021104000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolarian+Academy)

The lesson of the *Urza’s Saga* block was that we have to be careful with these types of cards. While we still make plenty of engine cards, we now are much more conservative in the way we price them. We’ve cut back on tutor cards. We’ve weakened our card drawers. And we’re very cautious about the mana generators we make.

Combo card lovers need not completely fear. In recent years, you’ve seen R&D respond to the combo craziness of *Urza’s Saga* block. As such, we’ve been extra cautious with combo enablers. But as time elapses, we’re beginning to loosen up. While there’s no fear of a second “Combo Winter,” I do believe you will see combo oriented decks start to peek their head into the tournament scene from time to time in the years to come.

### Question #4 – So how does infinity work in Magic?

I guess I should begin by breaking the bad news, there is no infinity in **Magic**. So when you hear the term "infinite mana," it really means "a finite but very large amount of mana." Not as catchy, huh? So, what happens when you have a combination of cards that create an effect that could be done hypothetically an infinite number of times?

Luckily, The **Magic** Comprehensive Rules actually has an entire section dedicated to handling infinite loops:

> 421\. Handling “Infinite” Loops
> 
> 421.1. Occasionally the game can get into a state in which a set of actions could be repeated forever. The “infinity rule” governs how to break such loops.
> 
> 421.2. If the loop contains one or more optional actions and one player controls them all, that player chooses a number. The loop is treated as repeating that many times or until the other player intervenes, whichever comes first.
> 
> 421.3. If the loop contains at least one optional action controlled by each player and actions by both players are required to continue the loop, the active player chooses a number. The nonactive player then has two choices. He or she can choose a lower number, in which case the loop continues that number of times plus whatever fraction is necessary for the active player to “have the last word.” Or he or she can agree to the number the active player chose, in which case the loop continues that number of times plus whatever fraction is necessary for the nonactive player to “have the last word.” (Note that either fraction may be zero.)
> 
> *Example: One player controls a creature with the ability “![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): \[This creature\] gains flying.” Another player controls a permanent with the ability “![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless0.gif): Target creature loses flying.” The “infinity rule” ensures that regardless of which player initiated the gain/lose flying ability, the nonactive player will always have the final choice and therefore be able to determine whether the creature has flying. (Note that this assumes that the first player attempted to give the creature flying at least once.)*
> 
> 421.4. If the loop contains only mandatory actions, the game ends in a draw. (See rule 102.6.)
> 
> 421.5. If the loop contains at least one optional action controlled by each player and these actions don’t depend on one another, the active player chooses a number. The nonactive player can either agree to that number or choose a higher number. Note that this rule applies even if the actions could exist in separate loops rather than in a single loop.

### And the Beat Goes On

Hopefully this week’s column will give you a little insight into how R&D (well, at least how I) see infinite combos.

Join me next week, when I admit I make mistakes (expect some fun in the article thread).

Until then, may you know the joy of dealing over a million damage to your opponent’s head.

Mark Rosewater

Normally, my article would have ended, but I couldn’t resist the concept of having an infinite article about infinite combos. If this idea sounds interesting to you, click [here](#begin).

*Mark may be reached at makingmagic@wizards.com.*
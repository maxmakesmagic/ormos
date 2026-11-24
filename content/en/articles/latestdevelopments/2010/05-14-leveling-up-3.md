---
id: w6crrfb8
kind: article
lang: en
path: /en/articles/latestdevelopments/2010/05-14-leveling-up-3
title: Leveling Up
published: '2010-05-14'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
    lang_detected: en
    capture_id: 726598
    url: https://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
    captured_at: '2021-12-05 03:08:13+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
    lang_detected: en
    capture_id: 726598
    url: https://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
    captured_at: '2021-12-05 03:08:13+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
    lang_detected: en
    capture_id: 726598
    url: https://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
    captured_at: '2021-12-05 03:08:13+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
    lang_detected: en
    capture_id: 726598
    url: https://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
    captured_at: '2021-12-05 03:08:13+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: w6crrfb8
  url: https://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
  lang: en
  template: drupal
  captured_at: '2021-12-05 03:08:13+00'
  capture_id: 726598
  wayback_url: https://web.archive.org/web/20211205030813id_/https://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
- document_id: w6crrfb8
  url: http://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-13
  page_key: magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-13
  lang: en
  template: drupal
  captured_at: '2017-08-16 20:15:37+00'
  capture_id: 726584
  wayback_url: https://web.archive.org/web/20170816201537id_/http://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-13
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: w6crrfb8
  capture_id: 726598
  url: https://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
  wayback_url: https://web.archive.org/web/20211205030813id_/https://magic.wizards.com/en/articles/archive/latest-developments/leveling-2010-05-14
  captured_at: '2021-12-05 03:08:13+00'
  template: drupal
  sha256: e8f3fe63064635e3fb279f71f480f4efbdaa7aa47caefc5fe1c15b4219f6a77a
render_recovery: []
---
This is the end of Level Up Week on DailyMTG.com. Today I'll talk about two parts of the design and development process that the level up creatures went through.

**Magic** is a game of decisions. Most players who have played **Magic** for a while like staying active in a game by making decisions. Limited games that go on for a long time can make players feel that their decisions don't matter anymore. *Rise of the Eldrazi* games were going to go longer than most games. This risked making it feel too non-interactive. Brian Tinsman patterned the level up mechanic after his popular card [Figure of Destiny](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny). We, the developers, liked how level up kept players engaged through long games. We chose to put it in the common rarity to ensure that level up cards were in Limited decks.

The level up ability can be played only when you could cast a sorcery. Some players have expressed disappointment about this. **Magic** is a great game because it is challenging to play. We don't think that challenge should come from difficulty processing what the cards on the board do. Level up creatures that leveled at instant speed would have been very hard to process in combat because they change in unpredictable ways. We print some creatures that change size in combat already. We print them in ways that make them easy to process. We also try to print them in small quantities. Putting level up creatures at common with instant-speed leveling would have made board states harder to process than we like. This is why level up is a sorcery-speed ability.

![](https://i.ormos.uk/86/54/865470560a72643fbed1e865131c0e0603f847cf904648dac5c4173a33e3fa6a.png)

This is the end of Level Up Week on DailyMTG.com. Today I'll talk about two parts of the design and development process that the level up creatures went through.

Games that remain fun for repeated plays tend to give players meaningful decisions to make, and experienced **Magic** players love that **Magic** gives them lots of choices. Limited games that go long, though, often lead to both players running out of cards. When both players are playing off the top of their decks on a stalled board, that feeling of choice is greatly reduced. The important thing isn't which player plays better, it's who is luckier. Reducing a game that is often so skill-based to luck is a bit of a letdown.

![](https://i.ormos.uk/15/c8/15c82d2c6c4883e09c178e6ee794a4fb180e48014770023e81a867b6e393c715.jpg)

That feeling of a lack of control was exacerbated in *Rise of the Eldrazi* Limited by the increased length of games. For Eldrazi to matter, games needed to go long, but players also needed something fun to do while they waited for the Eldrazi to happen. Inspired by [Figure of Destiny](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny), Brian Tinsman chose level up mechanic to give players a thing to do in the intervening turns.

Later on in development, the team had to choose whether level up would appear in the common rarity or not. My fellow developers and I could have gone either way on this. It's obvious that in the end we chose to use it at common, and one of the considerations that led us to this was that we wanted players to have enough things to do during long games. Putting level up only at uncommon would have given players fewer outlets for all the extra mana that they would have sitting around, and that sounded worse than having them easily accessible.

![](https://i.ormos.uk/54/47/54470d8fb798cb269566f793625218a0dc9545201f91512ac188689a13f6d437.png)

One of the initial reactions to levelers from players was frustration that the level up ability could be played only as a sorcery. Hearing that feedback was challenging for us. **Magic** will never be a simple game, but as developers we do our best to put the complexity where complexity is fun. In our experience, trying to make strategic decisions is fun, but board states that are so tricky to understand that it's hard to get the the strategic level are less fun. Designers and developers both found that creatures with level up that leveled at instant speed often created the latter situation. The exchange of mana for size was different on different level up creatures. A pile of open mana accompanying a creature with level up could be tricky to process; a pile of open mana accompanying multiple creatures with level up could be bewildering.

We sometimes make creatures that can be bigger than they say they are. A splash of this is fine, because **Magic** should challenge you in different ways from game to game. However, we didn't want to put players in the position of having to read, process, and act on complicated boards that could change at instant speed in game after game of *Rise of the Eldrazi* Limited. Rather than do that, we chose to have the level up ability work at sorcery speed.

![](https://i.ormos.uk/f9/58/f95874bab43fe0cf640f5c09e1d0a92b41b6458568bb7c11d6f43b1544e4cc4e.png)

This is the end of Level Up Week on DailyMTG.com. Today, I'll take an increasingly deep look at two threads of the design and development process that the level up creatures went through. My intention is that you leave this article with a better understanding of the decisions we made around the mechanic.

### Common Decisions

I've played a lot of tournament **Magic**, and in particular I have played in a lot of Pro Tour Qualifiers. Limited format qualifiers use the Sealed Deck format for the Swiss rounds before the Top 8, and because of this I have played quite a lot of Sealed Deck. The most frustrating element of sealed deck play, for me, was when games would stall out and neither me nor my opponent would be able to break through. We would sit for turn after turn, with hands full of lands, each waiting to draw something that would let us do something. We were playing for a long time, but we weren't really making any meaningful decisions. What mattered wasn't who played smarter, but instead who drew a breakthrough card first.

We develop modern sets to avoid this situation as much as we can. However, *Rise of the Eldrazi* is a special case. Due to its "huge creature" theme, games were going to take a while. This meant that it was more likely than ever that games could go on indeterminately, with neither player feeling like they had done anything that mattered. **Magic** isn't as much fun when the players don't control much of what's going on, so we were concerned about this. Early *Rise of the Eldrazi* playtests showed that our concern was warranted. The Eldrazi creatures mattered, but much of the action that took place between the beginning of the game and the arrival of the Eldrazi felt unimportant. Developers involved with early playtesting requested that lead designer Brian Tinsman add something to make the intervening play more engaging.

![](https://i.ormos.uk/78/69/786911418efe04fecc7e0d329e3085760d41432dbcc0782e106d31b5ca4214d9.png)

The designers agreed with that feedback, and had largely come to the same conclusion—at the same time the developers did. Brian's solution was to add level up, which was inspired by his design for *Eventide*'s [Figure of Destiny](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny). That did exactly what the developers hoped it would do: it gave us things to do that mattered through more of the game.

Later in development we had a decision to make about how level up would be used. Some mechanics that require new frame treatments, like Kamigawa block's flip cards, live only at uncommon and higher. Others go at all rarities. Level up could have been either of these things. There were many factors that went into this decision, but one of them was that having level up creatures not be common meant that fewer cards were helping with the task of giving players meaningful decisions during board stalls. That helped push us to include level up at common.

### Instant Gratification

One of the initial reactions to levelers from players was frustration that the level up ability could be played only as a sorcery. This response was also frustrating to us as developers. Developers are responsible for managing cards' power level, but it's also important that we keep the game fun as well as balanced. Part of keeping the game fun is keeping it simple enough that players can process the cards on the table and make informed decisions. It was quite clear to us, after only a little bit of playing, that the level up ability being playable at instant speed would make games tough to process, because it would often not be clear how big creatures on the board could be by the time combat was over.

![](https://i.ormos.uk/6d/6a/6d6ab70255a9ee0e8da1c7fadf6ab790f7b140467b18847a48bc01eaa0919120.png)

Suppose I attack you with an [Ikiral Outrider](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ikiral+Outrider), a [Caravan Escort](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Caravan+Escort), and a [Kabira Vindicator](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kabira+Vindicator). The Irikal Outrider has two level counters, the [Caravan Escort](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Caravan+Escort) has four level counters, and the [Kabira Vindicator](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kabira+Vindicator) has two level counters. I have ten [Plains](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) untapped. If I can activate level up at instant speed, you have a pretty wild blocking puzzle to figure out. If you pile blockers onto my [Ikiral Outrider](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ikiral+Outrider), I can level it up twice to survive a ton of damage. Doing this also gives me enough mana to level up my [Caravan Escort](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Caravan+Escort) to a 5/5 first striker. Alternatively, I could level up the [Kabira Vindicator](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kabira+Vindicator) three times to pump both of my creatures. No matter what set of creatures you have, finding a set of blocks that doesn't have unfortunate consequences due to either of these scenarios takes a little thinking.

It's important that **Magic** have some variety from game to game in what can happen, and it's important that the game sometimes put you in a position where it isn't clear exactly what is going to happen. In the case of being unsure of the size of an attacking creature, we have a class of cards that put you in that position that we put at common over and over again: shades.

![](https://i.ormos.uk/30/12/30126673e219afcda8e0331d61ddf2aba51557fa792c77f0ed084a56f63a47bf.png)

When someone attacks you with one of these guys, you don't know how big it's going to get by the time combat is over. You can count how much mana they have, and in the case of [Looming Shade](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Looming+Shade) and [Crypt Ripper](https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crypt+Ripper) all you have to do is count the number of black sources they have. The math on these is easier than it is for levelers, as the trade between mana and increased size comes at the same rate every time. Because of this, it's clear how big these shades could get, even though it isn't clear how big they will get. Also, we tend to put only one shade at common in any given set, which limits how often you will run into them and be put in this position.

Levelers in *Rise of the Eldrazi* are a different story. We knew that there would be plenty of them in the set, and plenty of them at common. In the end, there are eight commons with level up, and sixteen more level up creatures at higher rarities. That meant that quite often, you could be attacked by multiple creatures with the mechanic, which would cause a decent amount of processing. With that density of level up creatures, having the level up mechanic work at instant speed would have created too much of a brain drain during play.

### The Last Level

I'm glad you took the time to level this article up all the way. *Rise of the Eldrazi*'s level up creatures are best when you give them time to grow, and I hope that this article has rewarded you just as much for giving it that time.

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>Which of the <i>Rise of the Eldrazi</i> mythic rares is your favorite? </b></th>&#10;		</tr></thead><tbody><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gideon+Jura">Gideon Jura</a></td>&#10;			<td>1674</td>&#10;			<td>18.6%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Emrakul%2C+the+Aeons+Torn">Emrakul, the Aeons Torn</a></td>&#10;			<td>1160</td>&#10;			<td>12.9%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vengevine">Vengevine</a></td>&#10;			<td>992</td>&#10;			<td>11.0%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=All+Is+Dust">All Is Dust</a></td>&#10;			<td>832</td>&#10;			<td>9.2%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Linvala%2C+Keeper+of+Silence">Linvala, Keeper of Silence</a></td>&#10;			<td>641</td>&#10;			<td>7.1%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sarkhan+the+Mad">Sarkhan the Mad</a></td>&#10;			<td>548</td>&#10;			<td>6.1%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lighthouse+Chronologist">Lighthouse Chronologist</a></td>&#10;			<td>485</td>&#10;			<td>5.4%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Transcendent+Master">Transcendent Master</a></td>&#10;			<td>473</td>&#10;			<td>5.3%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kargan+Dragonlord">Kargan Dragonlord</a></td>&#10;			<td>411</td>&#10;			<td>4.6%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Khalni+Hydra">Khalni Hydra</a></td>&#10;			<td>355</td>&#10;			<td>3.9%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nirkana+Revenant">Nirkana Revenant</a></td>&#10;			<td>345</td>&#10;			<td>3.8%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hellcarver+Demon">Hellcarver Demon</a></td>&#10;			<td>308</td>&#10;			<td>3.4%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulamog%2C+the+Infinite+Gyre">Ulamog, the Infinite Gyre</a></td>&#10;			<td>302</td>&#10;			<td>3.4%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kozilek%2C+Butcher+of+Truth">Kozilek, Butcher of Truth</a></td>&#10;			<td>298</td>&#10;			<td>3.3%</td>&#10;		</tr><tr><td><a href="https://web.archive.org/web/20100514000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cast+Through+Time">Cast Through Time</a></td>&#10;			<td>184</td>&#10;			<td>2.0%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>9008</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>
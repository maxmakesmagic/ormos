---
id: w0fbbkrr
kind: article
lang: en
path: /en/articles/feature/2002/12-17-before-the-storm
title: Before the Storm
published: '2002-12-17'
column_slug: feature
column: Feature
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
    lang_detected: en
    capture_id: 682419
    url: https://magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
    captured_at: '2021-09-11 09:30:49+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
    lang_detected: en
    capture_id: 682419
    url: https://magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
    captured_at: '2021-09-11 09:30:49+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
    lang_detected: en
    capture_id: 682419
    url: https://magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
    captured_at: '2021-09-11 09:30:49+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
    lang_detected: en
    capture_id: 682419
    url: https://magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
    captured_at: '2021-09-11 09:30:49+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: w0fbbkrr
  url: https://magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
  page_key: magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
  lang: en
  template: drupal
  captured_at: '2021-09-11 09:30:49+00'
  capture_id: 682419
  wayback_url: https://web.archive.org/web/20210911093049id_/https://magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
- document_id: w0fbbkrr
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/112
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/112
  lang: en
  template: aspx
  captured_at: '2012-02-29 19:40:59+00'
  capture_id: 808666
  wayback_url: https://web.archive.org/web/20120229194059id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/112
- document_id: w0fbbkrr
  url: http://www.wizards.com/default.asp?x=mtgcom/feature/112,,pt
  page_key: wizards.com/default.asp?x=mtgcom/feature/112
  lang: en
  template: classic_asp
  captured_at: '2005-04-20 21:49:23+00'
  capture_id: 2006594
  wayback_url: https://web.archive.org/web/20050420214923id_/http://www.wizards.com/default.asp?x=mtgcom/feature/112,,pt
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: w0fbbkrr
  capture_id: 682419
  url: https://magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
  wayback_url: https://web.archive.org/web/20210911093049id_/https://magic.wizards.com/en/articles/archive/feature/storm-2002-12-17
  captured_at: '2021-09-11 09:30:49+00'
  template: drupal
  sha256: 4f85ac9c78abb99254e47314a25a67ae53fd5f26b95d2a266e8845d0fa4053bb
render_recovery: []
---
*This article originally appeared in* The Duelist *#20, July 1997. It is presented here in its entirety.*

To most **Magic** players, card development is a big mystery. Everyone knows that someone makes the cards, but few know how it all happens. As the lead designer on *Tempest*, I'll take this opportunity to walk through both design and development in order to explain how a **Magic** expansion is created.

### In the Beginning

In my mind, *Tempest* began during an R&D ski trip in February of 1996 when Richard Garfield and I spent some time talking about new game mechanics. Richard had not actively worked on **Magic** since *Arabian Nights* and was interested in being part of the design process. Just a few weeks earlier, I had learned from Joel Mick, **Magic**’s lead designer, that a stand-alone expansion was scheduled for the fall of 1997. I had been at the company for just under half a year and was itching to work on design. I was enthusiastic about working with Richard, and managed to convince Joel (also on the trip) to let me manage the Design team.

To round out the team, I chose two R&D members I had worked with on previous projects: Mike Elliott and Charlie Catino (both names you might recognize as *Duelist* authors). The Design team scheduled time away from the office during early August to work on the initial design for the card, codenamed "Bogavhati." Richard volunteered his parents' house in Portland for the week. I then asked the team to brainstorm both new card mechanics and random card ideas to bring along. Mike and I went on a bit of a creative tear and by the time we were ready to leave for Portland, we had compiled over one hundred pages of card ideas.

### Razors, We Don’t Need No Stinkin' Razors

We chose to start the design process by examining our new card mechanics. With over twenty different ideas on paper, we needed to whittle the number down. After some discussion, we chose fifteen mechanics to include in our initial design. The number was high, as we wanted to test as many variations as possible in the playtest stage. Also, in a show of solidarity, we agreed not to shave until we had completed the first version of the set.

Let me explain the state of the four mechanics that ended up in *Tempest* as they were initially conceived.

*   **Shadow:** *(This creature can block or be blocked only by creatures with shadow.)* Shadow was originally designed by Mike to create a third front (after ground and air) which would add complexity in creature play. Initially, the ability was given to all five colors.
*   **Buyback:** *(You may pay some additional cost when you play this spell. If you do, put it into your hand instead of your graveyard as part of the spell’s effect.)* Richard and I created buyback as an interesting twist to casting spells. Initially, buybacks returned to the player's hand at the end of the turn.
*   **Slivers:** Slivers were designed by Mike while looking at a [Plague Rats](https://web.archive.org/web/20021217000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Plague%2BRats) one day. What if there were creatures like [Plague Rats](https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats), thought Mike, that shared other abilities with creatures of their own kind. Slivers were originally envisioned as pieces of a large creature that had been split apart. For this reason, the original Slivers were all named after body parts. There were eleven in all, five of which were common.
*   **Licids:** Originally called Lice, Licids had an interesting evolution. I created cards that could be cast as either creatures or creature enchantments. This inspired Mike to create creatures that could turn into creature enchantments and then back into creatures. The team was split on which version to include, but in the end we decided to try Mike's.

After working on the mechanics, we spent the next two days looking through individual card ideas. If two or more of us didn’t like a card, it was removed from the list. By the end of our first pass, we had whittled the list down to four to five hundred.

The next step was then to start organizing card ideas into a rough outline of the set. The outline had been created by taking the parameters of the set, such as color, rarity, and card type, and filling in all the necessary holes. For example, in a set of 330 cards (not counting basic lands), we decided to break down the rarities so that each color had twenty-three commons, nineteen uncommons, and fifteen rares with extra cards in each commonality going to multicolor, artifacts, and lands. We then committed to a certain number of spell types in each color.

Although we had more card ideas than we needed, we found certain areas were lacking material. We were then forced to brainstorm to fill these empty slots. By the end of the week we managed to finish the first version of the set (which was a good thing, as all of us needed a good shave).

<table><tbody><tr><td><img alt="Shadow creatures" src="https://i.ormos.uk/83/9f/839fce458b7a78fa9a3e242f9d35aeaa123d25670c06418d7d5763720bd693cc.jpg"><br><i>Shadow cards: <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soltari+Guerrillas">Soltari Guerrillas</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soltari+Priest">Soltari Priest</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dauthi+Slayer">Dauthi Slayer</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thalakos+Mistfolk">Thalakos Mistfolk</a>.</i></td></tr></tbody></table>

### Play It Like You Mean It

We took our first version and printed playtest cards. Now came the tough job: playing with them. Following Richard’s suggestions, we got a feel for the set by spending the first two weeks playing sealed games with just the common cards. Several things became apparent immediately. First, we realized that buyback had a lot of potential. This is when many of the basic buybacks such as [Searing Touch](https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Touch) (originally known as Poke) were first created.

Second, we realized that creatures with shadow made the game very aggressive, as they influenced players to attack. To reduce the severity of this phenomenon, we decided to restrict shadow to three colors. We chose black, blue, and white, as they seemed appropriate for integrating the mechanic. Also, as "shadow" seemed out of flavor for white creatures, we changed the name of the ability to "astral."

After two weeks, we mixed the uncommon cards into the playtest, and then a week later, the rare cards. We playtested for two months in all, playing several hours every day. The hundreds of cumulative hours taught us much about the burgeoning *Tempest* environment. For starters, it was fast. Real fast. Mike and I had actually had a five-game series that took only ten minutes. We learned what mechanics were working and replaced those that seemed extraneous. Many of these replacements were defensive cards that we felt would help slow down Bogavhati’s breakneck pace. Both Slivers and Licids proved to have high play value. After a little tweaking, we handed in the final design version of Bogavhati. It was time for development.

<table><tbody><tr><td><img alt="Licids" src="https://i.ormos.uk/30/19/30194272476d87ec1ddeee62a2e1955475ac4be16990aa7a32830cd9c23f9fd7.jpg"><br><i>Licid cards: <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enraging+Licid">Enraging Licid</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stinging+Licid">Stinging Licid</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nuturing+Licid">Nuturing Licid</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Quickening+Licid">Quickening Licid</a>.</i></td></tr></tbody></table>

### But It Goes to Eleven

Once the design file was officially handed in, Joel picked the Bogavhati development team: Henry Stern, Bill Rose, William Jockusch, Mike, and me. The idea was for the Development team to include some designers in order to represent the intentions of the design team, and some new eyes to give the cards a fresh perspective.

The Development team began by sitting down and going through the expansion card by card. The initial reaction was that the set had too many things going on at once. Four of the eleven submitted mechanics were weeded out, and the remaining mechanics were then dissected.

We changed the buyback mechanic so that buyback spells returned to the player's hand immediately upon resolution. This allowed the cards to be used multiple times during the same turn. The development team agreed that buybacks were one of the most interesting new mechanics and decided to further up the number in the set.

Next we turned our attention to the astral creatures. To differentiate them from other creatures and to avoid stalemate on the third front, we decided to make the astral creatures very offensive. They were given higher powers and, with only a few exceptions, toughness of 1. This ensured that defense would prove problematic. Since we were making them more aggressive, we decided to change one of the colors for astral from blue to red, as red is rife with aggressive creatures. This decision was short lived, however, and astral returned to blue. Finally, due to the existence of “astral” cards in the MicroProse **Magic** game for the PC, we changed the word astral to “etheric.”

Our playtesting led us to believe that the Slivers were powerful and would be extremely popular. To offset their power we chose to equalize their number over all five colors, forcing Sliver decks to use a variety of colors. We removed the rare Slivers and replaced them with a cycle (one in each color) of uncommons to go with the cycle of commons.

Although a little fooling was done with the Licids to see what would happen if the creatures came back from their enchantment state tapped, the Licids were primarily left alone. The remaining two mechanics were developed, but it was eventually decided that buybacks, etheric, Slivers, and Licids offered plenty for the Bogavhati player. One of the two extra mechanics was moved to the first Bogavhati expansion (although we left one card in as a taste of things to come)\* while the other is tentatively scheduled for next year’s stand-alone set.\*\*

<table><tbody><tr><td><img alt="Slivers" src="https://i.ormos.uk/c5/d6/c5d672aedf44279d282fd4963bf1b811217da1bac3aa25d507fd8f179d077629.jpg"><br><i>Sliver cards: <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindwhip+Sliver">Mindwhip Sliver</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winged+Sliver">Winged Sliver</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Muscle+Sliver">Muscle Sliver</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barbed+Sliver">Barbed Sliver</a>.</i></td></tr></tbody></table>

### This Is Only a Playtest

After the Development team spent a month or two making the initial fixes, the cards were sent to outside playtesters. Depending on the size of the set, the playtest stage can run anywhere from one to several months. Before playest cards were sent out, the naming team did its initial pass to make presentable names for each card. Poke, for example, was changed to Flame Touch (and later to [Searing Touch](https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Touch)).

The playtesters each received an envelope of stickers to be stuck on old **Magic** commons and lands. The playtesters were asked to play the cards in both sealed and constructed play. If a card was thought to be broken, the playtesters were asked to prove it by building a deck with the card in question. The development team concurrently did its own testing, and any problem cards were either removed or altered.

During the playtest stage, the development team came to some more conclusions. Buybacks, originally priced using cantrips as models, were deemed undercosted. [Searing Touch](https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Touch)’s buyback cost was raised from 2 to 3. As a test, [Whispers of the Muse](https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whispers+of+the+Muse)’s buyback cost was radically changed from 3 to 6.

To increase the impact of etherics on the sealed environment, the number of etherics was raised. To compensate, a number of etheric hosers were included in the set to help players deal with the etheric threat in a sealed game.

As the set began to solidfify, each card was given a name and an art description based on its function and flavor. This is generally done mid-way through the development process to insure that the artists have completed their work by the time the cards go into production. At this point that the flavor text team began their work.

<table><tbody><tr><td><img alt="Buyback spells" src="https://i.ormos.uk/6a/f7/6af71262b16e6e8523a14642de0eefed5692ac2b7e83e09e564eabc066fb1e5e.jpg"><br><i>Buyback cards: <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Touch">Searing Touch</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Fury">Elvish Fury</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whispers+of+the+Muse">Whispers of the Muse</a>, <a href="https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evincar%27s+Justice">Evincar's Justice</a>.</i></td></tr></tbody></table>

### Game, Set, Match

Playtest eventually came to an end and the Development team enterted the final stages of development. This involves making sure all the pieces are coming together in a cohesive fashion. Cards are templated, insuring that the wording matches proper **Magic** phrasing and terminology. The card names, art, and flavor text are checked to make sure that they fit the card power.

At this point. the lead developer also works with representatives of other parts of the company to make sure the project advances smoothly. For instance, while the set is being developed, the Art department is busy commissioning the art, Editing is making sure all the language is effective and accurate, international is preparing to translate the card set into other languages, and production is buying supplies and arranging time at the printers to ensure that the cards get printed on time. All these parts must work together to meet the final deadline.

As development was wrapping up, a few last adjustments were made. We decided to raise [Searing Touch](https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Touch)’s buyback cost from 3 to 4, while [Whispers of the Muse](https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whispers+of+the+Muse)’s cost was dropped down to 5. Editing alerted the development team that the word “etheric” does not work grammatically as a name for a creature ability, as it is an adjective and not a noun. A special meeting is called to come up with another name for etheric. In the end, the top choice, ironically enough, was "shadow." The name had come full circle.

Finally, R&D handed the final lists off to Editing. The set was still six months from being released, but all that time was needed for layout, production, printing, and distribution. At that point R&D started to work on *Tempest*’s first expansion. All that remained for them was to proof layout sheets before they were sent to the printers.

The entire process took fourteen months and resulted in the expansion that, hopefully, you now own. And that, faithful readers, is how an expansion is made.

\*: This refers to the Spikes that populate *Stronghold*. [Spike Drone](https://web.archive.org/web/20021217000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spike+Drone) was included in *Tempest* as a teaser.  
 \*\*: This actually refers to two mechanics, cycling and echo. Cycling was originally known as "sliding," and echo was fist called "planeshift." Both were designed for *Tempest* and then held off until *Urza's Saga.*

*Send questions and comments to editor@wizards.com.*
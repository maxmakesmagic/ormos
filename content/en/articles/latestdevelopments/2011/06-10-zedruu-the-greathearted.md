---
id: rjp7x6qx
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/06-10-zedruu-the-greathearted
title: Zedruu the Greathearted
published: '2011-06-10'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: mark-globus-23d2ab4c
  name: Mark Globus
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
    lang_detected: en
    capture_id: 736405
    url: https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
    captured_at: '2022-09-30 01:25:21+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
    lang_detected: en
    capture_id: 736405
    url: https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
    captured_at: '2022-09-30 01:25:21+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
    lang_detected: en
    capture_id: 736405
    url: https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
    captured_at: '2022-09-30 01:25:21+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
    lang_detected: en
    capture_id: 736405
    url: https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
    captured_at: '2022-09-30 01:25:21+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: rjp7x6qx
  url: https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
  page_key: magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
  lang: en
  template: drupal
  captured_at: '2022-09-30 01:25:21+00'
  capture_id: 736405
  wayback_url: https://web.archive.org/web/20220930012521id_/https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
- document_id: rjp7x6qx
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/146
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/146
  lang: en
  template: aspx
  captured_at: '2013-07-02 03:09:22+00'
  capture_id: 613312
  wayback_url: https://web.archive.org/web/20130702030922id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/146
- document_id: rjp7x6qx
  url: https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-09
  page_key: magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-09
  lang: en
  template: drupal
  captured_at: '2022-07-01 17:10:15+00'
  capture_id: 736398
  wayback_url: https://web.archive.org/web/20220701171015id_/https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-09
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: rjp7x6qx
  capture_id: 736405
  url: https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
  wayback_url: https://web.archive.org/web/20220930012521id_/https://magic.wizards.com/en/articles/archive/latest-developments/zedruu-greathearted-2011-06-10
  captured_at: '2022-09-30 01:25:21+00'
  template: drupal
  sha256: 0b429af13d7c18ca5c130923103e44c45fcee98f14ee6fbd1a0ba52ec117c4d9
render_recovery: []
---
Hello! I am filling in for Tom LaPille while he cavorts around Japan, spellslinging at Pro Tour Nagoya and doing some sightseeing. Today, I'll be sharing with you our experiences with developing ***Magic: The Gathering** Commander*.

Let me start off by introducing my crack development team.

**Mark Globus**

![](https://i.ormos.uk/92/ce/92ceeab73eb3a7f33920535b070768559eb14c5b512cccee052bbb624575be15.jpg)

I joined Wizards of the Coast about four and half years ago at the conclusion of the original [Great Designer Search](https://web.archive.org/web/20110610000000/https://magic.wizards.com/en/articles/archive/great-designer-search-2006-10-31), when I tied for fourth. I bounced around digital for a couple of years doing everything from crushing bugs on **Magic Online** to being the lead technical producer for [**Dungeons & Dragons** Insider](https://web.archive.org/web/20110610000000/http://www.wizards.com/dnd/Tools.aspx). Then, two and half years ago, I joined **Magic** R&D as the Senior Producer. What's that? Well, I make sure that everything is running smoothly within **Magic** R&D. I get new products off the ground and clear roadblocks from projects in flight. Occasionally, I jump on a design or development team as well, including ***Magic** 2011*, *Worldwake*, and *Scars of Mirrodin* design and *Zendikar*, *Rise of the Eldrazi*, and "Roll" development. This was my first development lead, and you'll see the fruits of my first design lead soon: ***Magic** 2012*.

**Peter Knudson**

![](https://i.ormos.uk/10/61/106179afed98c7e9410ce1b36c1c1aff48bdaf4397f320a8724b69cee7a367ff.jpg)

Peter has interned for us in **Magic** R&D twice, and on this second stint I asked him to be a part of this development team. He was a great addition, bringing us his enthusiasm, passion, and strong work ethic. "Political Puppets" was the deck in the roughest shape coming out of design, and I had Peter spearhead our efforts in making this a fun, exciting deck. Peter was unable to join us in R&D this summer, but I look forward to having the opportunity to work with him again in the future.

**Erik Lauer**

![](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg)

Erik's assistance on Commander development was invaluable, and I couldn't have gotten through this without his experience backing me up. He is the most tenured member of the Magic Development team and I greatly appreciated the perspective that his experience brought. Erik was my strong second on the team and I found his counsel to be wise. What was his number one piece of advice? Playtest, playtest, playtest.

**Ryan Miller**

![](https://i.ormos.uk/1b/e6/1be6726c717240b1a5368e24c38654f8b62141c4eb54a6d557ef3610cd66b2aa.jpg)

Ryan is an awesome designer who focuses more on non-**Magic** games here at Wizards. He's been on quite a tear lately with them, as he has led the design for \[REDACTED\] and came up with the idea for \[REDACTED\]. Hmmm... that wasn't fair! Here—how about this? Ryan recently took on the mantle as lead designer for **Duel Masters**, our Japanese TCG. Congratulations, Ryan! Occasionally, we get to borrow him for **Magic** projects as well and he was our representative on the development team from Ken Nagle's design team. His insights into the design vision helped us stay on track and kept us focused on keeping this product fun and not just "interesting."

**Lee Sharpe**

![](https://i.ormos.uk/55/c1/55c15279e289f2a4f448f07024ec45a6a6749744d19701e7536c7c0341c8de91.jpg)

Lee's day job is working in the finance department here at Wizards, but he has been an avid Commander player for years. Thus, I was excited to steal him away from his numbers for while to help out on this product. Lee's perspective on the Commander scene helped up focus on what makes Commander fun and make sure that we didn't stray from our target audience.

### By the Numbers

This is **Magic**'s first product to feature new cards outside of a booster release, and as such presented some interesting challenges. The first thing that we had to consider was how we were going to sell the cards! While we quickly settled on five decks, there were many discussions in the pit regarding what colors should be featured in those decks. Design settled on wedges (two allied colors and their common enemy, like white and blue with red), though four color decks were considered strongly. Wedges had the advantage that three-color decks have more cohesion than four and that there is not a significant amount of difference between a four-color deck and a five-color deck. We did talk about four-color decks in development, but we liked what we saw coming from design and saw no need to change things.

![](https://i.ormos.uk/60/18/6018aa670ed35054773c4634cd1bc2198d7790d5895b6c168419f670301ca59c.gif)  

The next thing to consider was how many new cards were supposed to be in the five decks. Design handed off five decks, with ten new cards in each deck. All of the new cards in each deck were unique, with no overlap in the new cards between the decks. Unfortunately, this didn't work very well in our initial development playtests. We really wanted people to get excited about the new cards, and too frequently people didn't have even one in their opening hands. Some games were played in which no new cards were seen from a deck, and that was definitely a letdown. Furthermore, we wanted to ensure that everyone felt like they were getting a good value from their purchase. Even though we were packing the decks with exciting reprints, it was important to us that the decks felt new.

The tricky part was that we didn't want to increase the number of cards. We liked having around fifty new cards; this product is significantly smaller than a booster release, and we didn't want to overshadow either *New Phyrexia* or ***Magic** 2012*. On the other hand, fifteen new cards seemed to be a lot better than ten—people would usually have a new card in their opening hand. Could we get there? I started to play with some numbers... What if a few of the cards overlapped between the decks? Could we keep the number of new cards at fifty while increasing the number of new cards per deck to fifteen?

Almost. We identified ten mono-color cards that could each go in three decks. These were previously in just one deck each, so we ended up with an additional four cards in each deck. This gave us fourteen. Aha! How about increasing the size of the set of new cards by just one and putting this into every deck! This gave us our fifty-one-card set and fifteen cards in each deck.

One of our goals was to ensure that this product had cards that were primarily for multiplayer games, including political cards. Most **Magic** sets have very little room for such cards as they are required to behave nicely in a two player game. Now we had a place to print more of these cards. For example, you may have already seen Death by Dragons, which Aaron Forsythe introduced in [his article](/en/articles/feature/2010/12-02-magic-the-gathering-commander) about ***Magic: The Gathering** Commander*. This is a fairly straightforward political card: you tick me off by attacking me, so I retaliate by giving everyone but you a 5/5 flying dragon! However, the design team wanted to go further than this and handed to development a deck that was completely political in nature.

Without further ado, let me introduce...

![](https://i.ormos.uk/a2/eb/a2eb91dfb0d3f57342b9ab811873150964c504f9ffa48f32a155302a318e6b06.jpg)  

Zedruu is the commander of the "Political Puppets" deck. At first blush, this card may seem pointless or weak, but we found Zedruu to be one of the most subtly powerful commanders in the set. Typically, we'd see people interact with Zedruu something like the following:

**Playtest 1:** "Zedruu's deck is really weak! I don't know why I would want to give away any of my stuff anyway. Can I play another commander?"

**Playtest 2:** "Haha—I cast [Wall of Omens](https://web.archive.org/web/20110610000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Omens) and after I drew my card, I gave it to my opponent. I drew a card off my Wall every turn!"

**Playtest 3:** "That game was awesome! I bribed my opponents to attack each other by giving them creatures and land. I also gave away my [Howling Mine](https://web.archive.org/web/20110610000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howling+Mine)! Before they knew it, I was drawing more cards than everyone else at the table put together and my life total was over 60. I cruised to victory!"

Here is a card that we wouldn't make in a normal **Magic** set, but that feels right at home here. This card only required minor tweaks as it came in from design. Originally, it was a 2/5 that only counted the number of *players* who controlled permanents that you owned, rather than counting the actual number of donated permanents. However, despite the fact that everyone who came into contact with this card read it multiple times, no one read it correctly! We changed it to meet player expectations and balanced this out by reducing the toughness of the card from 5 to 4.

![](https://i.ormos.uk/25/19/251978f236f9a46effb41e53236c9e48aef4d8d681e0278350727dd3c1dfdb6f.jpg)

Zedruu the Greathearted | Illustration by [Mark Zug](https://web.archive.org/web/20110610000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Mark+Zug%22%5D)

Further testing of Zedruu showed it to be in a great spot. Masters of diplomacy worked wonders with this commander. Some opponents loved being showered with gifts, while others feared receiving them and did everything possible to kill off Zedruu—repeatedly. While Zedruu certainly isn't for everyone, I believe she'll be well loved by many. I hope you have as much with Zedruu as I have!

Two weeks from now, Tom LaPille returns to Latest Developments. However, in the meantime, I have a question for all of you...

  
  
[![](https://i.ormos.uk/ec/eb/eceb257f1070ba6e35c980e983966e5de8cbbe188fc3bdce076cadbd4b7cabd7.jpg)](/en/events/2009/gameday-facts/world-wide-game-day)
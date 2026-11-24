---
id: 1gynp35g
kind: article
lang: en
path: /en/articles/makingmagic/2018/07-23-planeswalking-down-memory-lane
title: Planeswalking Down Memory Lane
published: '2018-07-23'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
    lang_detected: en
    capture_id: 228551
    url: https://magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
    captured_at: '2024-05-18 02:37:32+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
    lang_detected: en
    capture_id: 228551
    url: https://magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
    captured_at: '2024-05-18 02:37:32+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
    lang_detected: en
    capture_id: 228551
    url: https://magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
    captured_at: '2024-05-18 02:37:32+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
    lang_detected: en
    capture_id: 228551
    url: https://magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
    captured_at: '2024-05-18 02:37:32+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 1gynp35g
  url: https://magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
  page_key: magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
  lang: en
  template: contentful
  captured_at: '2024-05-18 02:37:32+00'
  capture_id: 228551
  wayback_url: https://web.archive.org/web/20240518023732id_/https://magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
- document_id: 1gynp35g
  url: https://magic.wizards.com/en/articles/archive/making-magic/planeswalking-down-memory-lane-2018-07-23
  page_key: magic.wizards.com/en/articles/archive/making-magic/planeswalking-down-memory-lane-2018-07-23
  lang: en
  template: drupal
  captured_at: '2022-09-30 10:23:18+00'
  capture_id: 904523
  wayback_url: https://web.archive.org/web/20220930102318id_/https://magic.wizards.com/en/articles/archive/making-magic/planeswalking-down-memory-lane-2018-07-23
- document_id: 1gynp35g
  url: https://magic.wizards.com/en/articles/archive/making-magic/planeswalking-down-memory-lane-2018-07-23?yde
  page_key: magic.wizards.com/en/articles/archive/making-magic/planeswalking-down-memory-lane-2018-07-23?yde
  lang: en
  template: drupal
  captured_at: '2022-09-30 10:22:25+00'
  capture_id: 904527
  wayback_url: https://web.archive.org/web/20220930102225id_/https://magic.wizards.com/en/articles/archive/making-magic/planeswalking-down-memory-lane-2018-07-23?yde
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 1gynp35g
  capture_id: 228551
  url: https://magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
  wayback_url: https://web.archive.org/web/20240518023732id_/https://magic.wizards.com/en/news/making-magic/planeswalking-down-memory-lane-2018-07-23
  captured_at: '2024-05-18 02:37:32+00'
  template: contentful
  sha256: e72e80241bde9f7c0dfb608b2c7b9cb65064fe3a6f1d3dc70628f7204b41dc1c
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email me
  occurrences: 1
---
Welcome to *Commander (2018 Edition)* Week. This week, we're showing off one deck per day, and today, we start with the blue-red artifact-themed deck. While I will be showing off preview cards from that deck, I decided to take my *Commander 2018* article in a slightly different direction. Tomorrow, Gavin Verhey will be writing about *Commander 2018*'s design and introduce the design team, so instead of doing that, I'm going to talk a bit about planeswalkers and how they've changed over time. (For those unaware, each of the *Commander 2018* decks have a planeswalker that can be played as a commander—and yes, you'll see the commander for the blue-red deck before this column is over.)

Back in 2007, when *Lorwyn* came out, I wrote a two-part article about the design of planeswalkers. I went in great detail about why we decided to make them and the steps we went through to design the new card type. (If you haven't read those articles yet, be sure to check out parts [one](/en/articles/makingmagic/2007/11-05-planeswalk-on-the-wild-side-part-i) and [two](/en/articles/makingmagic/2007/11-12-planeswalk-on-the-wild-side-part-ii).)

While I will briefly touch on their creation in this column, this article is more about how the planeswalker card type has evolved mechanically over the years.

# Planeswalk On

The idea all began in *Future Sight* design when design team member Matt Cavotta approached me with the idea for making planeswalkers a new card type. *Time Spiral* block's storyline had us revamping the power level of the Planeswalkers to allow us to make them a bit more approachable (characters with god-like powers were hard to relate to), and *Future Sight* was about peeking into the mechanical future of *Magic*. There had never been a more perfect time, Matt thought, to introduce planeswalker cards. As you see in the article linked above, the design team, including myself, was a bit skeptical at first—we tend not to make new card types very often—but Matt stayed strong and managed to convince us why we needed to do it.

We made a separate mini-team (Matt Cavotta, Mark Gottlieb, Brandon Bozzi, and myself) to work on designing planeswalkers to be introduced on the futureshifted sheet of *Future Sight*, but the versions we ended up with were a bit too robotic. There were three abilities that you rotated through each turn. Interestingly, this abandoned version of planeswalkers would be the inspiration for Sagas during *Dominaria* design.

We decided to push planeswalkers back until we had a design we liked, which ended up being in *Lorwyn*. ([Tarmogoyf](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)'s reminder text in *Future Sight* did hint that the card type was coming.) The core of the *Lorwyn* design team (Aaron Forsythe, Paul Sottosanti, and myself) did the majority of the second half of planeswalker design. For far greater detail, you can read the two-part article about planeswalker design that I linked to above.

*   [![140205](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=140205)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=140205)
*   [![140176](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=140176)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=140176)
*   [![140233](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=140233)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=140233)
*   [![140212](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=140212)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=140212)
*   [![140222](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=140222)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=140222)

The first five planeswalkers to be printed are known as the *Lorwyn* Five: Ajani, Jace, Liliana, Chandra, and Garruk. We decided to start with a cycle of five monocolored planeswalkers that hit square center for each color. We wanted these first five planeswalkers to be iconic representatives of their color. Each of the *Lorwyn* Five had the same template. They had a +1 ability that did a smaller effect, a minus ability that did a larger effect (something they had enough loyalty to do when cast), and a bigger minus effect, what we call an "ultimate," that they had to build up to use. The one other innovation was Chandra, which was the first to have a -X loyalty ability. We had actually talked about pushing it off, but it played so well and was such a perfect character fit that we decided to leave it. The *Lorwyn* Five are the only planeswalkers to appear at rare, but that's only because mythic rare didn't exist yet as a rarity.

The original plan for planeswalkers was that they were going to be something special that didn't show up all the time. *Lorwyn* introduced the first five planeswalkers, then the next three sets (*Morningtide*, *Shadowmoor*, and *Eventide*) had zero planeswalkers in them.

*   [![174852](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=174852)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=174852)
*   [![174859](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=174859)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=174859)
*   [![174983](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=174983)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=174983)
*   [![174912](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=174912)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=174912)

Planeswalkers next showed up in *Shards of Alara*. This time the planeswalkers weren't a cycle (although, between *Shards of Alara* and *Conflux*, we did have one planeswalker per shard). Two of them, Ajani and Sarkhan, were two-color. Ajani was the first planeswalker to get a second card and the first to change colors. Elspeth was the first planeswalker with two plus abilities. Tezzeret was the first planeswalker with a more niche ability, only playable in an artifact-heavy deck. There was a lot of talk at the time about whether we wanted to do that, and Tezzeret was made as a test.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=179441)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=179441)

The next set, *Conflux*, brought Nicol Bolas, which accomplished a couple firsts. He was the first three-color planeswalker, he was the first eight-mana planeswalker (we chose to make him powerful but expensive), and he was the first planeswalker that previously existed as a legendary creature card. (Jaya Ballard, Karn, Narset, Ob Nixilis, Teferi, Urza, Venser, and Xenagos all also exist as planeswalker cards and separately as legendary creature cards.)

*Magic 2010* was the first core set to feature planeswalkers, but those cards were simply reprints of the *Lorwyn* Five.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Chandra+Ablaze)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Ablaze)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nissa+Revane)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa+Revane)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=195403)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=195403)

Starting with *Zendikar*, we begin making planeswalkers an every-set occurrence. They were popular out of the gate, but we work two years ahead, so it wasn't until *Zendikar* that we could readjust to make sure that every set had at least one planeswalker. These three planeswalkers aren't particularly innovative, they just expand upon changes we'd already made: other versions of existing characters, narrower thematic focuses, etc.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=195297)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=195297)

*Worldwake* introduced [Jace, the Mind Sculptor](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+the+Mind+Sculptor), not only one of the most powerful planeswalkers ever made, but also the first to feature four loyalty abilities. When we originally designed the planeswalker frame, I'd also asked for them to build a four-loyalty-ability version because I wanted to have it in our back pocket. Jace had established himself as the most popular of the early planeswalkers, so we allowed him to be the first four-loyalty-ability planeswalker. Jace is also the first planeswalker to feature a 0-loyalty ability.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=192218)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=192218)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sarkhan+the+Mad)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sarkhan+the+Mad)

*Rise of the Eldrazi* only had two planeswalkers, but each paved new mechanical space. Gideon was the first planeswalker to turn into a creature. Sarkhan was the first planeswalker with no plus loyalty abilities. (This led to a lot of discussions in R&D at the time.)

From here on, I'm only going to reference planeswalkers when they do something new. The core sets continued to have a cycle of monocolored planeswalkers that mostly remained the *Lorwyn* Five but got tweaked every once in a while. Nissa would eventually swap in for Garruk, and Gideon replaced Ajani.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=214350)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=214350)

*New Phyrexia* brought [Karn Liberated](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Karn+Liberated), which was the first colorless planeswalker, requiring only generic mana to cast. He also has the largest minus for a loyalty cost. We talked a lot about whether Karn was also supposed to be an artifact but decided that for developmental reasons, we didn't want that (too many shenanigans with artifacts); we decided that planeswalker-ness overrides other qualities. It's also why Ajani is not a Cat, for example. (The one exception for subtypes is planeswalkers that turn into creatures gain a subtype while a creature.)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=245250&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=245250)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=245251&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=245251)

*Innistrad* introduced [Garruk Relentless](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Relentless), which represents a bunch of firsts. He's the first double-faced planeswalker and the first that transforms. He's the first planeswalker that changes color within the card. He's the first planeswalker with five loyalty abilities (and six overall abilities). He's the first planeswalker with a static ability.

A quick aside about the static ability: Planeswalker has become the most popular card type. It is also the card type with the least amount of design space, so in my role as head designer, one of the things I've championed has been slowing down the evolution of planeswalkers to make sure we're "squeezing all the toothpaste out of the tube." Because of this, the static ability on [Garruk Relentless](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Relentless) was a bit contentious. I've been trying to hold back on planeswalker static abilities, as it's something I didn't want us rushing into too quickly. After much discussion, we decided it was okay on Garruk because it was so tied to his transformation, which felt unique to a double-faced planeswalker.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=249985)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=249985)

[Sorin, Lord of Innistrad](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Lord+of+Innistrad) from *Dark Ascension* was the first printed planeswalker to produce an emblem. Emblems are an enchantment-like ability that sits in the command zone. Emblems have no color, name, or card type and currently have no way to be destroyed. (And it's not something we have any immediate plans to do; emblems require so much work to make, we don't want to make them easy to deal with.) The first emblem was actually made retroactively for [Elspeth, Knight-Errant](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elspeth%2C+Knight-Errant) from *Shards of Alara* as a rules fix for the card. Emblems are used solely for planeswalker cards and are printed on cards like tokens, but usually at low frequency as they are created only by planeswalkers (which show up at mythic rare).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tamiyo%2C+the+Moon+Sage)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tamiyo%2C+the+Moon+Sage)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=276497)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=276497)

Tamiyo was the first time we obviously introduced a planeswalker from a known plane (she's from Kamigawa) who was a visitor to the plane we were on. There are characters that we later revealed to be from known worlds (such as Liliana being from Dominaria), but it wasn't a known thing when they were introduced. Tibalt was our first attempt at a two-mana planeswalker, considered developmentally to be a big miss, as we were timid about pushing such a cheap planeswalker.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gideon%2C+Champion+of+Justice)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gideon%2C+Champion+of+Justice)

While -X loyalty costs existed since *Lorwyn*, [Gideon, Champion of Justice](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gideon%2C+Champion+of+Justice) was the first planeswalker to have essentially a variable positive loyalty ability where he could gain a different amount of loyalty depending on how many creatures the opponent controls.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ajani+Steadfast)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Steadfast)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Garruk%2C+Apex+Predator)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%2C+Apex+Predator)

In *Magic 2015*, [Ajani Steadfast](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Steadfast) became the first planeswalker capable of putting loyalty counters on other planeswalkers. Garruk became the second four-loyalty-ability planeswalker.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=382244)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=382244)

[Dack Fayden](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dack+Fayden) was the first planeswalker to show up as a new card outside of a Standard-legal set. *Commander (2014 Edition)* would be quick on its heels, later that year, with five more.

*   [![389530](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=389530)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=389530)
*   [![389478](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=389478)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=389478)
*   [![389612](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=389612)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=389612)
*   [![389618](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=389618)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=389618)
*   [![389712](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=389712)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=389712)

Each deck in *Commander 2014* was led by a planeswalker that had the ability to be a commander. This cycle of five cards is the second case of planeswalkers having a static ability (interestingly, listed at the bottom on these cards). These cards had a couple firsts. One, they were the first planeswalkers you could play as commanders. Two, Freyalise was the first dead character to show up on a planeswalker card. (The fates of both Nahiri and Teferi were unknown at the time, but we've since learned they're alive.) This opened up the door for future planeswalkers of dead characters in supplemental sets (one of which you'll see later this week). Teferi is the first card to allow planeswalkers to use more than one loyalty ability in a turn.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398438&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398438)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398432&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398432)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398428&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398428)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398429&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398429)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398434&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398434)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398435&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398435)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398422&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398422)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398423&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398423)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398441&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398441)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=398442&type=card "")](https://web.archive.org/web/20180723000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=398442)

*Magic Origins* introduced the first cards that can turn into planeswalkers. These monocolor double-faced cards were legendary creatures that could transform into planeswalkers. Kytheon was (sort of) the first one-drop planeswalker. These planeswalkers, due to their legendary status on front, could serve as commanders in the Commander format.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Chandra%2C+Pyrogenius)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra%2C+Pyrogenius)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nissa%2C+Nature%27s+Artisan)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%2C+Nature%27s+Artisan)

With the release of *Kaladesh*, we introduced Planeswalker Packs, a new tweak on preconstructed decks aimed at newer players. While we've made new content for preconstructed decks before, this was the first time we made new planeswalker cards. These cards were created at higher mana costs and were designed to not be relevant in Standard (as all the cards in the deck are Standard-legal). Both Chandra and Nissa had alternate versions of planeswalker cards in *Kaladesh* itself. The Planeswalker Packs only come with one copy of the planeswalker, but they also have a card that has an effect and then lets you [tutor](/en/articles/play-design/2017/07-14-the-m-files-hour-of-devastation-part-1#tutor) for the planeswalker (get it out of your library and put it into your hand) to essentially give you a second chance at drawing it.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nissa%2C+Genesis+Mage)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%2C+Genesis+Mage)

One of the Planeswalker Packs for H*our of Devastation* features Nissa. This was the first time a planeswalker appeared in the Planeswalker Pack but not the corresponding set.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Urza%2C+Academy+Headmaster)](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%2C+Academy+Headmaster)

*Unstable*'s [Urza, Academy Headmaster](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%2C+Academy+Headmaster) has a couple firsts. It's the first five-color planeswalker. It's the first silver-bordered planeswalker. It's the first planeswalker with variable abilities (you have to look up online to see what happens each time you activate it). And it's the first Urza, a character players have been asking for in planeswalker form since the card type first premiered.

Which brings us to the planeswalkers of *Commander (2018 Edition)*. Two of them are brand-new characters. One is a dead Planeswalker from long ago. And the final one is a new incarnation of a known Planeswalker. (That's the one I'm going to show off today.) All but today's are three-colored.

Now that I've revealed that today's planeswalker is a known Planeswalker, you should be able to figure out who. I said up front that today's *Commander 2018* deck is a blue-red artifact-themed deck. Who better to lead it than. . .

## Click to reveal

![Saheeli, the Gifted](https://media.wizards.com/2018/c18/en_6FqeR1wjYE.png)

Saheeli. Like the original [Saheeli Rai](https://web.archive.org/web/20180723000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saheeli+Rai), Saheeli, the Gifted is designed to be played in an artifact deck. In fact, if you remember back when *Kaladesh* came out, many players expected a blue-red artifact-themed legendary creature, but instead got a blue-red artifact-themed planeswalker. Jhoira eventually filled that slot in *Dominaria*, but Saheeli came back to also fill the slot she knocked out of the set the first time around.

But wait, there's more. How can I preview an artifact-themed deck without showing off an artifact? Here is an artifact designed to play nicely with Saheeli, the Gifted.

## Click here to see Retrofitter Foundry

![Retrofitter Foundry](https://media.wizards.com/2018/c18/en_yTEiTVLVtY.png)

This artifact allows you to keep upgrading your artifact creatures, including the Servos made by Saheeli.

# Planeswalk into the Sunset

I hope you had fun looking through the history of planeswalker innovations. A lot of neat stuff has happened, but a lot of cool stuff is still waiting in the wings. Speaking of new stuff, stick around all week as we show off a new deck each day—including the planeswalker that commands it.

As always, I'm interested in any feedback. You can email me or contact me through any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro)). Let me know what you thought of today's column and what you like most about planeswalkers.

Join me next week for my mailbag column on *Core Set 2019*.

Until then, may you dream of cool new planeswalker innovations.

* * *

 

##### #555: Unstable Cards, Part 3

##### #555: Unstable Cards, Part 3

42:26

This podcast is part three of a six-part series on the design of each and every non-Contraption card in *Unstable*.

[Download MP3 Format](https://media.wizards.com/2018/podcasts/magic/drivetowork555_unstablecardspart3_s43dF40s.mp3)

  

 

##### #556: Video with Richard & Peter

##### #556: Video with Richard & Peter

49:38

For the 25th Anniversary Grand Prix, I recorded a video with Richard Garfield and Peter Adkison. This podcast is all about the day I spent shooting that video. I also talk quite a bit about the early days of *Magic*.

[Download MP3 Format](https://media.wizards.com/2018/podcasts/magic/drivetowork556_videowithrichardandpeter_5ifJ30jJ.mp3)

*   [**Episode 554**](https://media.wizards.com/2018/podcasts/magic/drivetowork554_unstablecardspart2_G3ku9oOl.mp3) *Unstable* Cards, Part 2
*   [**Episode 553**](https://media.wizards.com/2018/podcasts/magic/drivetowork553_unstablecardspart1_lEr34eLL.mp3) *Unstable* Cards, Part 1
*   [**Episode 552**](https://media.wizards.com/2018/podcasts/magic/drivetowork552_whentokeyword_7uYi90oz.mp3) When to Keyword
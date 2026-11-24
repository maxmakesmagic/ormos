---
id: j1ds89qt
kind: article
lang: en
path: /en/articles/magiconline/2018/02-12-improving-our-approach-to-magic-online-data
title: Improving Our Approach to Magic Online Data
published: '2018-02-12'
column_slug: magiconline
column: Magic Online
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
    lang_detected: en
    capture_id: 764358
    url: https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
    captured_at: '2022-08-14 05:49:53+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
    lang_detected: en
    capture_id: 764358
    url: https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
    captured_at: '2022-08-14 05:49:53+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
    lang_detected: en
    capture_id: 764358
    url: https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
    captured_at: '2022-08-14 05:49:53+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
    lang_detected: en
    capture_id: 764358
    url: https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
    captured_at: '2022-08-14 05:49:53+00'
    rule: url.article_section
sources:
- document_id: j1ds89qt
  url: https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
  page_key: magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
  lang: en
  template: drupal
  captured_at: '2022-08-14 05:49:53+00'
  capture_id: 764358
  wayback_url: https://web.archive.org/web/20220814054953id_/https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
- document_id: j1ds89qt
  url: https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12?&partner=CardsRealm&medium=cardsrealm&utm_source=CardsRealm&utm_medium=affiliate&utm_campaign=CardsRealm
  page_key: magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12?medium=cardsrealm&partner=CardsRealm
  lang: en
  template: drupal
  captured_at: '2021-04-19 23:01:41+00'
  capture_id: 764360
  wayback_url: https://web.archive.org/web/20210419230141id_/https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12?&partner=CardsRealm&medium=cardsrealm&utm_source=CardsRealm&utm_medium=affiliate&utm_campaign=CardsRealm
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: j1ds89qt
  capture_id: 764358
  url: https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
  wayback_url: https://web.archive.org/web/20220814054953id_/https://magic.wizards.com/en/articles/archive/magic-digital/improving-our-approach-magic-online-data-2018-02-12
  captured_at: '2022-08-14 05:49:53+00'
  template: drupal
  sha256: f11849e230ddc0f1d526f95bd45dc9223559c6dc52b5b9de8c68e0ca9132c952
render_recovery: []
---
For some time now, we've been tinkering with what data from *Magic Online* we show, and how and when, usually—much to the distaste of the community—erring on the side of showing less data rather than more. Starting this weekend, we'll be changing the decklist data we show in a way that we hope addresses some of the complaints we've heard from the community.

Before we get to the how, when, and what of the data we'll be showing, let's talk a bit about what we're trying to accomplish with this change:

**Our goal is to use *Magic Online* decklist data to show you what is *possible*, not necessarily to show you what is *most played*.** We do want to show you a ton of cool, successful decks that let you explore new strategies. We don't necessarily want to provide data that reinforces more adoption of the already most-played deck. It can be a vicious cycle—whether or not the most-played deck is also the winningest deck.

To that end, the new system we're implementing will show every 5-0 deck that is significantly different from any other. We're searching for a suitable midpoint between those in the community who want all of the *Magic Online* play data—or at least a good chunk of it—and some data on our end that indicates there is a tipping point where too much information can create unhealthy or unfun play environments.

Second, we do realize that we have likely undershot with how much data we've been sharing. This new system attempts to address that. We don't necessarily believe we've found the sweet spot just yet, but we do believe this new system will be closer—and more useful—than the current system. In our eyes, this is a substantial improvement over the current system, but one that still leaves room for the exploration and unknowns that can make *Magic* interesting.

Given all of that, here's how the new system will work:

*   We're changing what we mean by "distinct" decklists. Currently, *distinct* is defined as having at least ten cards different between lists, and we list five different distinct decklists per day. We have found that ten-card differences often didn't create enough archetype differentiation. Initial testing at 20 seems to be leading to better diversity, showing a wider spread of the metagame, so we're moving the definition of *distinct* to 20-card differentiation.
*   Twice a week for Modern and Standard, and once a week for other less-played formats, we will be sharing an uncapped number of distinct 5-0 decklists from Competitive Leagues. Currently we show 35 per week. At the current rates of play and format diversity, the new system should be showing 50–80 decklists per week for Standard and Modern.

In other words, *we are attempting to show an example decklist of every single distinct archetype since the previous publication.*

This approach is mostly the result of some fine-tuning and initial testing. For example, using this new set of rules, we expect the first set of Standard lists will likely contain 25 or more decklists for each of the two publications in a given week. We expect that number to dip as the format matures, but it's a sign that this system (and Standard's diversity) is much improved.

The schedule for daily decklists will start out like this:

*   Monday – Standard
*   Tuesday – Modern
*   Wednesday – Pauper
*   Thursday – Standard
*   Friday – Modern
*   Saturday – Legacy
*   Sunday – Commander and Vintage

The amount of *Magic Online* data we share with the community has been a hot topic of debate on social media recently. The core of many—though not all—players' arguments in wanting more data is about inspiration for deck building and innovation. This change will result in us showing more data in a way that better meets that goal.

While there will always be a segment of players asking for more and more data to be shared, it is important that the amount of data and the way it is presented are consistent with *Magic*'s appeal as a creative deck-building game. By choosing to share data in a way that highlights and inspires innovative deck building, we hope to create an environment that is longer lasting and more enjoyable for players who enjoy the most creative elements of the game.
---
id: t576n9aq
kind: article
lang: en
path: /en/articles/uncategorised/2019/10-16-squashing-bugs-in-companion
title: Squashing Bugs in Companion
published: '2019-10-16'
column_slug: uncategorised
column: uncategorised
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
    lang_detected: en
    capture_id: 763242
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
    captured_at: '2022-06-25 08:01:25+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
    lang_detected: en
    capture_id: 763242
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
    captured_at: '2022-06-25 08:01:25+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
    lang_detected: en
    capture_id: 763242
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
    captured_at: '2022-06-25 08:01:25+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
    lang_detected: en
    capture_id: 763242
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
    captured_at: '2022-06-25 08:01:25+00'
    rule: url.article_section
sources:
- document_id: t576n9aq
  url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
  page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
  lang: en
  template: drupal
  captured_at: '2022-06-25 08:01:25+00'
  capture_id: 763242
  wayback_url: https://web.archive.org/web/20220625080125id_/https://magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: t576n9aq
  capture_id: 763242
  url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
  wayback_url: https://web.archive.org/web/20220625080125id_/https://magic.wizards.com/en/articles/archive/magic-companion-updates/squashing-bugs-companion-2019-10-16
  captured_at: '2022-06-25 08:01:25+00'
  template: drupal
  sha256: 54ea7bcedd7346ba53e87c689b25def91244c6e25e919aac82714b8c5327240c
render_recovery: []
---
It's bug week here for the *Magic: The Gathering Companion* team! This sprint we spent time cleaning up several bugs—many of them found and reported by you, the players, via the in-app email contact. Thanks for taking the time to help make *Companion* the best it can be. Here's a rundown of the items you helped us find.

**Event Failures on Certain iPhones**

After our last update, we introduced an issue that caused events to fail to run successfully in certain types of iPhones. Impacted users could start an event, but Round 2 would frequently disappear and the event could not continue. The fix ensures all supported iPhones now work properly.

**Double Byes**

Getting two byes is great at a Grand Prix, but when they're awarded randomly in an event no player should ever receive more than one. You helped us track down an issue that was causing players to get multiple free wins in an event, and we've fixed the service that pairs players for matches to make sure this doesn't happen in the future.

**Random Byes**

A few *Companion* fans astutely pointed out in an event with an odd number of players the player who was registered in the event last was the one who always received the first-round bye. This bug is ripe for abuse, as you can imagine, so we wanted to make sure it was fixed in this release to provide the best user experience possible and prevent anyone from abusing who gets the bye in Round 1. Now the bye is awarded at random, just as it should be!

As always, thanks to all the passionate *Magic: The Gathering Companion* Open Beta testers who have taken the time to help us track down bugs in the app. Additionally, a special thanks to Yael, the dev who hammered away at these fixes during this sprint. The app wouldn't be what it is without her!
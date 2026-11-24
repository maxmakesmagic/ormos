---
id: 523ds3bf
kind: article
lang: en
path: /en/articles/uncategorised/2020/07-22-new-features-and-improvements-in-companion
title: New Features and Improvements in Companion
published: '2020-07-22'
column_slug: uncategorised
column: uncategorised
authors:
- slug: billstark
  name: Bill Stark
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
    lang_detected: en
    capture_id: 763191
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
    captured_at: '2021-12-05 02:59:26+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
    lang_detected: en
    capture_id: 763191
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
    captured_at: '2021-12-05 02:59:26+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
    lang_detected: en
    capture_id: 763191
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
    captured_at: '2021-12-05 02:59:26+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
    lang_detected: en
    capture_id: 763191
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
    captured_at: '2021-12-05 02:59:26+00'
    rule: url.article_section
sources:
- document_id: 523ds3bf
  url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
  page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
  lang: en
  template: drupal
  captured_at: '2021-12-05 02:59:26+00'
  capture_id: 763191
  wayback_url: https://web.archive.org/web/20211205025926id_/https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 523ds3bf
  capture_id: 763191
  url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
  wayback_url: https://web.archive.org/web/20211205025926id_/https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-features-and-improvements-companion-2020-07-22
  captured_at: '2021-12-05 02:59:26+00'
  template: drupal
  sha256: e8fcf9ee4d0cfdd23824c8ea82a07fb79a73b373d37222c63698904bdfc601ff
render_recovery: []
---
Download *Companion* for iOS [here](https://apps.apple.com/us/app/magic-the-gathering-companion/id1455161962?src=app_page).

Download *Companion* for Android [here](https://play.google.com/store/apps/details?id=com.wizards.winter_orb&src=product_page).

Another sprint of work has gone by, which means the *Companion* team has new updates for the app! A week after our launch, we're excited to be taking your feedback and rolling out improvements and new features already. Let's cover what's new in this release!

# Improved EventLink Integration

EventLink is our new event management software for Wizards Play Network (WPN) stores. It's currently in open beta in regions where playing in events is safe. *Companion* works with EventLink to make the player's experience in an event as smooth as it can be, and recent improvements to EventLink warranted some work on the *Companion* side to ensure a high-quality experience for all. With the introduction of the "round rollback" feature, your WPN store owner can correct a mistake in their event by "rolling" the round back to the previous round. If that happens, *Companion* will notify you and give you new pairing or standings information once they're available.

# Fixing Commander Damage

Users noticed a bug with reporting Commander damage that was intricate enough that we missed it in our test cases. *Companion* automatically handles reducing your primary life total in-game when you adjust a Commander damage total, but what was unexpected was that if you undo Commander damage, your primary life total treats it as regular damage. That's a big "whoops" on our part, and we've rushed a fix to make sure your Commander experience is as smooth as it can be.

It was players who reached out to us that caught this issue, and if you notice an issue with *Companion*, you can send that feedback to us using the "Submit Feedback" option from the dropdown menu in the app. While we may not have time to personally reply to every message, we *do* read every single item that comes in.

# Player Eliminated Bug

In rare circumstances, Android users of *Companion* report that they receive a notification that they've been eliminated as soon as round 1 of their event starts. We are investigating a solution for this issue. If you're an Android user who experiences this, there is a simple fix: log out of *Companion*, then log back in with your Wizards Account. Have no fear: you're not actually eliminated as the message is simply an error. No progress in your event will be lost, and you're able to play normally. After you log back in, you can pick up where you left off by clicking on the open event in your event lobby. We hope to have that issue fixed in an upcoming release soon.

That's it for this release! We're hard at work on our next round of features and updates (Pauper players, we heard you—we'll add Pauper!). Thanks for making the *Companion* launch a huge success.
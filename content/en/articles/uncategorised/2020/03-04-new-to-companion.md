---
id: 7j68t660
kind: article
lang: en
path: /en/articles/uncategorised/2020/03-04-new-to-companion
title: New to Companion
published: '2020-03-04'
column_slug: uncategorised
column: uncategorised
authors:
- slug: billstark
  name: Bill Stark
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
    lang_detected: en
    capture_id: 763182
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
    captured_at: '2022-05-29 05:43:01+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
    lang_detected: en
    capture_id: 763182
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
    captured_at: '2022-05-29 05:43:01+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
    lang_detected: en
    capture_id: 763182
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
    captured_at: '2022-05-29 05:43:01+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
    lang_detected: en
    capture_id: 763182
    url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
    captured_at: '2022-05-29 05:43:01+00'
    rule: url.article_section
sources:
- document_id: 7j68t660
  url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
  page_key: magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
  lang: en
  template: drupal
  captured_at: '2022-05-29 05:43:01+00'
  capture_id: 763182
  wayback_url: https://web.archive.org/web/20220529054301id_/https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 7j68t660
  capture_id: 763182
  url: https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
  wayback_url: https://web.archive.org/web/20220529054301id_/https://magic.wizards.com/en/articles/archive/magic-companion-updates/new-companion-2020-03-04
  captured_at: '2022-05-29 05:43:01+00'
  template: drupal
  sha256: f911d63887f07f89ced0791d6138c7e97df56780504e63e9df4af688d232d0a4
render_recovery: []
---
Join the open beta playtest and download *Magic: The Gathering Companion* on [iOS](https://testflight.apple.com/join/sjZRvrZW) or [Android](https://play.google.com/apps/testing/com.wizards.winter_orb).

In the latest update to *Magic: The Gathering Companion*, we fixed a host of bugs reported by our users, increased who can access *Companion*, and began live-testing of the app in conjunction with our new event-reporting software. It's an exciting release, although, all the backend work may not be as flashy to you, our front-end users. Let's dive into what we've been working on.

# Who can use *Companion*?

A few users have been asking what devices are supported by *Companion*. The answer to that is lengthy and unsustainable, so a better answer is which operating systems are currently supported. Prior to this release, you had to have a device that could access the following operating systems:

8.0.0 and up for Android  
 12.1 and up for iOS

User feedback and data revealed that there was a not insignificant portion of users who were on older Android devices that couldn't use *Companion*. The devs spent time fixing this to roll access out to older devices, and I'm happy to announce that with this release, Android users on 6.0.0 operating systems or higher can use the app. If you tried downloading it before but were unable to do so because of your operating system, you should be able to do so now.

# Bug Fixes

As I've discussed before, building software involves rigorous efforts to minimize the likelihood that bugs go out in any given release. Despite that rigor, even seasoned development teams like the one we've got working on *Companion* won't catch everything. Our QA and QE teams help shore up what we miss, and users like you let us know about items that got by all of us. In our latest release, we tackled a whole bunch of them. Here are the biggest ones that will no longer be impacting you:

*   iOS users reported a 501 error when they removed a player from an event; this has been fixed.
*   There were a number of users who were reporting issues with visual displays on iOS and Android, meaning either they couldn't scroll to take actions or the visuals displayed improperly. Not anymore!
*   Android users will notice some user-experience improvements to the standings pages that help bring that part of the app in alignment with the iOS experience.
*   In rare circumstances, the leaderboard screens could crash, but the edge case that caused that has been addressed.

# *Companion* and Tournament Play

Many of our beta testers have been using *Companion* to run events at home. That's a key part of the features on offer presently, but the plan has always been to use *Companion* to support in-store play as well. For the past few months, we've been building a new event-reporting software to help our Wizards Play Network retailers offer the best, smoothest tournaments they can for players. Since December, we've been testing that software in conjunction with *Companion* at *Magic* tournaments here at Wizards of the Coast. This past week, we broke new ground: the first public tournaments in Wizards history using the new event-reporting software and *Companion* together took place.

For now, the testing we're doing with those events is relatively small and isolated to several stores in Washington and Florida. I'll have more to say about rollout plans for spreading those playtests out more widely in later installments of this blog. Meanwhile, we're going to continue taking feedback from those events and adjusting our work to ensure we're hitting all the key marks we need to create a fantastic experience for both tournament organizers and players. You'll see some features to support that effort in *Companion*, including in this release. As of the latest build, *Companion* supports more formats to ensure it can handle supporting the new event-reporting software. I'm excited about how smoothly that testing has gone so far, however, we still have a lot of ground to cover before we're ready to put it in people's hands on a wide scale.
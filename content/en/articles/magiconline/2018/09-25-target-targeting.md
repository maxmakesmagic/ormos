---
id: 9vp9fyf8
kind: article
lang: en
path: /en/articles/magiconline/2018/09-25-target-targeting
title: 'Target: Targeting'
published: '2018-09-25'
column_slug: magiconline
column: Magic Online
authors:
- slug: christopher-bellach-36e01f58
  name: Christopher Bellach
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
    lang_detected: en
    capture_id: 827443
    url: https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
    captured_at: '2021-12-08 04:45:16+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
    lang_detected: en
    capture_id: 827443
    url: https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
    captured_at: '2021-12-08 04:45:16+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
    lang_detected: en
    capture_id: 827443
    url: https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
    captured_at: '2021-12-08 04:45:16+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
    lang_detected: en
    capture_id: 827443
    url: https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
    captured_at: '2021-12-08 04:45:16+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 9vp9fyf8
  url: https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
  page_key: magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
  lang: en
  template: drupal
  captured_at: '2021-12-08 04:45:16+00'
  capture_id: 827443
  wayback_url: https://web.archive.org/web/20211208044516id_/https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9vp9fyf8
  capture_id: 827443
  url: https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
  wayback_url: https://web.archive.org/web/20211208044516id_/https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25
  captured_at: '2021-12-08 04:45:16+00'
  template: drupal
  sha256: 032721a5e4d2992371e3cc2a894d5b36fff78687ba7325bda81b0a3a84ff77d9
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:MagicOnlineFeedback@wizards.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - MagicOnlineFeedback@wizards.com
  occurrences: 1
---
Welcome back, fellow Planeswalkers and fans of *Magic Online*. This is Christopher Bellach again, client developer, and I have another exciting upgrade for *Magic Online* to share with you all. First, a little context as to why we decided to make this change.

Have you ever been in Game 3 of a match and you just need to draw your [Aurelia's Fury](https://web.archive.org/web/20180925000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aurelia%27s+Fury) to burn your opponent out? Miraculously, your next draw is that very card, and you snap-play it as fast as you can. But your opponent only takes 1 damage because the *Magic Online* targeting indicators covered up a critical part of the interface that should have allowed you to choose how much damage the spell would do to your opponent? Well players, rejoice, as we have worked diligently to design a new targeting indicator system to make sure this problem will be a thing of the past.

Before we get to what the new targeting looks like, I want to take you through the iterations we made before coming to the design that made it to release. While the player targeting was the most problematic, we wanted to use consistent iconography to relay targeting information when targeting cards in all zones. Our first iteration was inspired by the iconography that map apps use to point to specific locations.

Round 1

![](https://media.wizards.com/2018/images/daily/npOw3ylfav.png)![](https://media.wizards.com/2018/images/daily/8dm6yOgIpZ.png)

There was some confusion about which icon meant targeting and which icon meant being targeted, and our color-blind testers were having trouble seeing the icons. Our next iteration updated the coloring to be more friendly to common forms of color-blindness and used different symbols within each indicator.

Round 2

![](https://media.wizards.com/2018/images/daily/lKBrFFRVrJ.png)![](https://media.wizards.com/2018/images/daily/otvQMid3Qh.png)

The new icons helped show what each indictor was trying to relay to the player. The new coloring also was much clearer to our color-blind testers, but the design of the icon still wasn't very grokkable at first take. For the next iteration, we tried a couple of different designs, putting them through some A/B testing.

Round 3

![](https://media.wizards.com/2018/images/daily/8Cw9c8nxUH.png)![](https://media.wizards.com/2018/images/daily/efA70nIG5C.png)![](https://media.wizards.com/2018/images/daily/aH0JIIp3Sj.png)![](https://media.wizards.com/2018/images/daily/IkgFmpbPql.png)

After testing these new icons, the arrow design ended up being the most successful at clearly indicating the game state to the player. However, some playtesters commented that the icons felt out of place, especially when side by side with the [new counter icons](/en/articles/magiconline/2018/09-05-counter-development). We also heard that the icons were hard to notice. Also, when something was targeting itself, having both the outward targeting icon and the inward targeting icon on the same card took up a lot of space. For our last iteration, we increased the size of the icons significantly and added white and black borders around the icons. Then, to keep the display simpler, we created a special icon to indicate when something is targeting itself instead of showing two separate icons.

Final

![](https://media.wizards.com/2018/images/daily/zNFKoo8MrB.png)![](https://media.wizards.com/2018/images/daily/TmcWOtxy6K.png)![](https://media.wizards.com/2018/images/daily/GoEJAgoMZy.png)

These are the icons you will see in the next update to *Magic Online.* The sky blue up arrow indicates that this thing is targeting something, and the vermillion down arrow indicates what is being targeted. The merged icon is used to indicate when something is targeting itself.

Here are some examples of what the icons look like in the *Magic Online* client:

![](https://media.wizards.com/2018/images/daily/hhPdJyOyPU.jpg)

The next time your only out is that [Aurelia's Fury](https://web.archive.org/web/20180925000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aurelia%27s+Fury), this is what the interface on *Magic Online* will look like. The vermillion down arrow indicates that the player is being targeted and the damage spinner is no longer being covered up. It will be much easier to let *Magic Online* know that you want to deal that 20 damage to your opponent, instead of the default 1.

Here is what it looks like when you target yourself with your [Ancestral Recall](https://web.archive.org/web/20180925000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall):

![](https://media.wizards.com/2018/images/daily/sLwxB2ar0d.jpg)

On the battlefield, the icons will be large on the card and will always point up/down regardless of the tapped state of the card.

![](https://media.wizards.com/2018/images/daily/iVMRgYAcQn.jpg)

That's all I have for this update. Thanks for reading, and I'm excited for you all to get a chance to use the new targeting system. Feel free to send your feedback to MagicOnlineFeedback@wizards.com, and I look forward to hearing what you all think of these changes. See you next time, and may all of your packs have epic foils!
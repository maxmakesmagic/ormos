---
id: pca98d8t
kind: article
lang: en
path: /en/articles/latestdevelopments/2002/01-18-altering-the-environment
title: Altering the Environment
published: '2002-01-18'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
    lang_detected: en
    capture_id: 717897
    url: https://magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
    captured_at: '2022-01-24 06:05:04+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
    lang_detected: en
    capture_id: 717897
    url: https://magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
    captured_at: '2022-01-24 06:05:04+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
    lang_detected: en
    capture_id: 717897
    url: https://magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
    captured_at: '2022-01-24 06:05:04+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
    lang_detected: en
    capture_id: 717897
    url: https://magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
    captured_at: '2022-01-24 06:05:04+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: pca98d8t
  url: https://magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
  page_key: magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
  lang: en
  template: drupal
  captured_at: '2022-01-24 06:05:04+00'
  capture_id: 717897
  wayback_url: https://web.archive.org/web/20220124060504id_/https://magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
- document_id: pca98d8t
  url: https://magic.wizards.com/en/articles/archive/altering-environment-2002-01-18
  page_key: magic.wizards.com/en/articles/archive/altering-environment-2002-01-18
  lang: en
  template: drupal
  captured_at: '2021-10-23 08:14:23+00'
  capture_id: 142041
  wayback_url: https://web.archive.org/web/20211023081423id_/https://magic.wizards.com/en/articles/archive/altering-environment-2002-01-18
- document_id: pca98d8t
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/rb3,,ja,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/rb3
  lang: en
  template: classic_asp
  captured_at: '2005-01-05 02:25:48+00'
  capture_id: 1988793
  wayback_url: https://web.archive.org/web/20050105022548id_/http://www.wizards.com/default.asp?x=mtgcom/daily/rb3,,ja,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: pca98d8t
  capture_id: 717897
  url: https://magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
  wayback_url: https://web.archive.org/web/20220124060504id_/https://magic.wizards.com/en/articles/archive/latest-developments/altering-environment-2002-01-18
  captured_at: '2022-01-24 06:05:04+00'
  template: drupal
  sha256: f0ffa273570185fc5435a4856647d3e40dd14b0ebf57fd934ae2e907ad02d357
render_recovery: []
---
One of the things a **Magic** development team does when working on a set is to try to figure out the impact of the set on Constructed tournaments. For years now, one of R&D’s missions has been to get people to play multi-color decks. Well, the *Invasion*-block finally accomplished that. Big time. Then with *Odyssey* we felt the rotation out of [Rishadan Port](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rishadan+Port) plus the introduction of another cycle of decent dual-lands (the [Sungrass Prairie](https://web.archive.org/web/20020118000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Sungrass%2BPrairie)) would make Standard even more multi-colored than it had been with *Mercadian Masques* plus *Invasion*.

![](https://i.ormos.uk/83/99/839908343f91c93fdc34eccfe2ccd1b8462759eecc2739d2837cebbc93b9f578.jpg)*A typical R&D scene: Buehler battles Barclay in a Future Future match.*

We in R&D also like **Magic** to stay fresh and we like **Magic** environments to constantly change, so it probably comes as no surprise that with *Torment* the pendulum is starting to swing back in the other direction. For the first time since I started working at Wizards, we actively decided to encourage a mono-color deck. In addition to our desire to keep things changing, we also knew that we had pushed multi-color black decks pretty aggressively in *Apocalypse*. We knew [Spiritmonger](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spiritmonger) and [Pernicious Deed](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pernicious+Deed) would make green-black pretty good and one of our own best test decks was a black/white [Phyrexian Arena](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Arena) deck with [Vindicate](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vindicate), [Death Grasp](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Grasp), [Gerrard's Verdict](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gerrard%27s+Verdict), etc. Black/blue (especially [Shadowmage Infiltrator](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shadowmage+Infiltrator)) isn’t half bad either.

Anyway, we were sitting around trying to figure out how to print a set with a bunch of really good black cards without making the existing black decks (especially black/white) too much better and that’s when it occurred to us: we could print cards that are good in mono-black but not good in black/X. Black already has cards that reward you for having lots and lots of swamps in play, like [Nightmare](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare), [Looming Shade](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Looming+Shade), and especially [Corrupt](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Corrupt) (all in *7th Edition*). Multi-color black decks don’t tend to have that many swamps so we figured if we made more cards like that, we might be able to introduce a whole new archetype to Standard. That way we could print a bunch of new and powerful cards without messing up the competitive balance too much.

![](https://i.ormos.uk/a1/2e/a12e939b1cf96cc156ebc2824d0a3474e8a0ba97690931b1043e024c8f1ecf4e.jpg)

We then looked at black’s two biggest themes -- discard and creature removal -- and realized each allowed for a nice simple spell that could trigger off the number of swamps you had in play. Thus were born [Mind Sludge](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Sludge) and [Mutilate](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutilate). It’s a bit unusual for a development team to think up brand new cards because that’s normally what design teams are supposed to do. However, since it’s the development team’s responsibility to think about how a set is going to impact Constructed, especially Standard, it often happens that a development team will be forced to improvise when the design doesn’t have the sorts of cards that development thinks will be good for the environment. That’s exactly what happened in this case.

When the *Torment* team studied the environment it was inheriting from the previous four sets, there was one unmistakable fact: blue was king. The *Invasion* block has lots of good cards in it, but we suspected that blue got more than its fair share. This isn’t all that surprising if you think about it -- the natural foil to blue has always been weenie decks. But it’s hard to build a really good weenie deck if your best cards require two different colors of mana. There are inherent problems with building a consistent mana-base and that’s why the best weenie decks, historically, have always been mono-color. Without aggressive weenie decks running around to keep it in check, is it any surprise that blue prospered? It’s possible that we shouldn’t have printed [Fact or Fiction](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction) in the gold set, but we didn’t figure all this out until *Apocalypse* (which is why we pushed green-black and black-white much more than the enemy color combinations that include blue). Certainly by the time we were working on the *Odyssey* block it was way too late to change anything. The *Torment* team thought through all this logic and decided we wanted to add a couple good weenies to the environment. We certainly didn’t want to return to the days of *Tempest* when [Jackal Pups](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jackal+Pups) roamed the earth and all decks were of the mono-color weenie variety, but a few carefully thought-out weenies seemed called for. In particular, we were ideally interested in weenies that would be good against control decks, without being all that exciting against colors other than blue.

![](https://i.ormos.uk/d1/68/d1683b5dd2e2a9572ef0bccb6e0044ee646aa84ac20afcee3adbe4c91e271e3c.jpg)

Enter [Basking Rootwalla](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Basking+Rootwalla) and [Nantuko Shade](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Shade). Each creature comes down fast, usually before an opponent can get up [Counterspell](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) mana, and if your opponent doesn’t react, you can just keeping pumping mana into them until your opponent is dead.

The Shade, of course, also fit in perfectly with our mono-black idea. It’s the third card the development team added to *Torment* and is, without a doubt, the best shade ever. We took [Frozen Shade](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frozen+Shade) (a card that was been in the base from *Alpha* through *Sixth Edition*) and added two power to its base stats. Then we cut a mana from its mana cost. It’s ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) to play now, but any deck that wants to run shades can probably come up with that initial cost without any problems. Basically, we knew that [Frozen Shade](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frozen+Shade) (and variants like [Hoar Shade](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hoar+Shade), [Whispering Shade](https://web.archive.org/web/20020118000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whispering+Shade), etc.) weren’t good enough for Constructed, but we thought it would be cool to have a shade in Constructed (for the two reasons I’ve explained), and voila.

Only time will tell what the true impact of *Torment* will be. That said, I think it’s safe to conclude one thing already: Black is back. Deal with it.

*Randy may be reached at latestdevelopments@wizards.com.*
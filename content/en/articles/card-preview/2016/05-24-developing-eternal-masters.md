---
id: keet2zm0
kind: article
lang: en
path: /en/articles/card-preview/2016/05-24-developing-eternal-masters
title: Developing Eternal Masters
published: '2016-05-24'
column_slug: card-preview
column: Card Preview
authors:
- slug: adam-prosak-76cf4169
  name: Adam Prosak
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
    lang_detected: en
    capture_id: 256053
    url: https://magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
    captured_at: '2022-08-26 18:33:19+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
    lang_detected: en
    capture_id: 256053
    url: https://magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
    captured_at: '2022-08-26 18:33:19+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
    lang_detected: en
    capture_id: 256053
    url: https://magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
    captured_at: '2022-08-26 18:33:19+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
    lang_detected: en
    capture_id: 256053
    url: https://magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
    captured_at: '2022-08-26 18:33:19+00'
    rule: url.article_section
sources:
- document_id: keet2zm0
  url: https://magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
  page_key: magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
  lang: en
  template: drupal
  captured_at: '2022-08-26 18:33:19+00'
  capture_id: 256053
  wayback_url: https://web.archive.org/web/20220826183319id_/https://magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: keet2zm0
  capture_id: 256053
  url: https://magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
  wayback_url: https://web.archive.org/web/20220826183319id_/https://magic.wizards.com/en/articles/archive/card-preview/developing-eternal-masters-2016-05-24
  captured_at: '2022-08-26 18:33:19+00'
  template: drupal
  sha256: 7dae9aa163688e3384df870f0bf3a18dc9790bf595e36ab08ab3b491ae1f3d1b
render_recovery: []
---
Hello, fellow magicians!

I'm Adam Prosak, I work in *Magic* R&D, and I was the lead developer on *Eternal Masters*. Nearly all of our sets have a design team and a development team. The design team is typically tasked with coming up with a vision for the set and creating the initial card file, while the development team takes that card file, refines it, and creates a fun experience for everyone to enjoy.

Mark Rosewater introduced the design team for *Eternal Masters* [here](/en/articles/makingmagic/2016/05-23-eternal-formats-of-the-spotless-mind), and I believe that they did an excellent job creating the structure of the set. One of their biggest challenges was to figure out what card pool to use. In general, we try to restrict what sets we can draw our reprints from—that way each product feels different. The design team's first instinct was to only use cards that are not Modern legal. However, *Vintage Masters* (for *Magic Online*) had that exact restriction, and if we were to reuse it, then *Eternal Masters* would look too much like *Vintage Masters*. What we ended up with was not a hard and fast rule, but simply a guideline.

*   Create Limited archetypes that need both Modern-legal cards *and* non-Modern-legal cards to create a unique experience that could not happen otherwise.
*   When choosing cards, try and choose a non-Modern-legal card. Use Modern-legal cards to help bridge gaps in strategies.

We didn't want to make either another *Vintage Masters* or another *Modern Masters*, so these guidelines helped the design and development team choose cards that would make *Eternal Masters* a unique experience.

# The Development Team

![](http://media.wizards.com/2016/images/daily/desdev_EMA_Prosak.png)

**Adam Prosak**—That's me! I work on the development team, mainly contributing to the Future Future League (where we playtest future Standard). Previously, I've worked on *Vintage Masters* and *Modern Masters (2015 Edition)*, and I really enjoy working on *Masters* sets. I love finding new ways to play with old cards. I think that one of the strengths of *Magic* is that there is a near-endless combination of things to do, and the *Masters* sets highlight much of what I love about *Magic*.

![](http://media.wizards.com/2016/images/daily/desdev_EMA_Hawley.png)

**Bryan Hawley**—Like myself, Bryan works on the development team. His main roles are with the FFL team and *Magic Duels*, and he was also on the development team for the upcoming *Eldritch Moon*. Bryan carried over from the *Eternal Masters* design team, and did excellent work helping us keep the design vision intact.

![](http://media.wizards.com/2016/images/daily/desdev_EMA_Stoddard.png)

**Sam Stoddard**—Sam writes our [Latest Developments column](/en/articles/columns/undated/latest-developments), in addition to being one of my favorite people in the entire world. He was also the most experienced person on the *Eternal Masters* development team, having led *Magic Origins* and the upcoming *Eldritch Moon*.

# Balancing for Balance

One of the most important tasks that the Development team has is balancing a set, such that one strategy isn't dominant over the others...

![](http://media.wizards.com/2016/adhfianalodifdj2_EMA/en_H5wUclVmHl.png)

...Oh, there's a preview card! [Balance](https://web.archive.org/web/20160524000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance) is one of the most iconic white spells of all time. When creating a set, both the design and development teams include many iconic cards, then try to build an environment around them. When creating *Eternal Masters*, cards like [Balance](https://web.archive.org/web/20160524000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance), [Force of Will](https://web.archive.org/web/20160524000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will), and Wasteland were among the first cards to be included.

The only unfortunate thing about [Balance](https://web.archive.org/web/20160524000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance) is that it is not very...balanced. It is one of the strongest cards that exists in *Magic*, and can potentially make a Limited environment much less fun. However, at mythic rare, it shows up less often and contributes less to the overall power of white. Additionally, [Balance](https://web.archive.org/web/20160524000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance) has a splashy effect that is unique in *Magic*, which makes it a good candidate to be a mythic rare.

Finding mythic rares for sets like *Eternal Masters* can often be difficult, since many of the cards we want to use come from sets without mythic rares. Cards like [Balance](https://web.archive.org/web/20160524000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance) make things a bit easier, as the combination of Limited power level and splashy effect make for a perfect mythic rare.

![](http://media.wizards.com/2016/images/daily/c4rd4r7_tfJj97SD3M.jpg)

[Balance](https://web.archive.org/web/20160524000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance) | Art by [Kev Walker](https://web.archive.org/web/20160524000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Kev+Walker%22%5d)

# Balancing for Limited

When developing *Eternal Masters*, we wanted to do a strategy for each color pair like we do with the majority of our sets. So *Eternal Masters* has green-white enchantments and blue-black reanimator as two of the ten primary strategies. However, we also wanted there to be overlap between the strategies. This meant finding strategies that can have some amount of overlap. If we want blue-black to be a reanimator strategy, then green-blue can be a threshold strategy. This allows the blue cards that fill up your graveyard to work in multiple strategies while enabling different things.

Another good example comes from using cards to bridge strategies that may not appear to have much in common. Green-white enchantments and red-green fast aggro don't appear to have much in common, but a strong Aura can help your small creatures break through in a red-green deck while triggering the enchantment rewards in your green-white deck.

Another cool benefit of these overlaps is now you have some additional flexibility when drafting. You can overlap two strategies, or even do strategies that aren't in the colors they were intended. You might get some cool red-green threshold decks, or white-black reanimator decks. While the format is still built around ten color pairs, there are definitely more things to explore.

Finding these strategies that have a significant amount of overlap was difficult, but also one of the most rewarding parts of working on *Eternal Masters*. One of these challenges had to do with finding the right amount of tribal for the set. Tribal strategies are really cool, and one of the best ways to link "Eternal" cards and "Modern" cards. However, it can be difficult to link up tribal strategies with each other. The first *Modern Masters* did this with changeling cards, but we did not want to repeat this. The design handoff had lots of tribal strategies, but in the end, only Elves survived. The competitive success of Elves in Eternal formats helped inform our decision to keep them, as well.

All in all, I believe that *Eternal Masters* is a great set. It has an excellent mix of nostalgia, great gameplay, and exciting cards. I hope you get the chance to draft it at least once, whether it's with your friends, at your local store, or on *Magic Online*.

—Adam
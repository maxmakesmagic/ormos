---
id: w5f1s7x1
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/06-07-dragons-maze-multiverse
title: Dragon's Maze Multiverse
published: '2013-06-07'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
    lang_detected: en
    capture_id: 721232
    url: https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
    captured_at: '2022-08-13 04:08:02+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
    lang_detected: en
    capture_id: 721232
    url: https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
    captured_at: '2022-08-13 04:08:02+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
    lang_detected: en
    capture_id: 721232
    url: https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
    captured_at: '2022-08-13 04:08:02+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
    lang_detected: en
    capture_id: 721232
    url: https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
    captured_at: '2022-08-13 04:08:02+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: w5f1s7x1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
  page_key: magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
  lang: en
  template: drupal
  captured_at: '2022-08-13 04:08:02+00'
  capture_id: 721232
  wayback_url: https://web.archive.org/web/20220813040802id_/https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
- document_id: w5f1s7x1
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/250
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/250
  lang: en
  template: aspx
  captured_at: '2014-04-29 14:55:28+00'
  capture_id: 620401
  wayback_url: https://web.archive.org/web/20140429145528id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/250
- document_id: w5f1s7x1
  url: https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-04
  page_key: magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-04
  lang: en
  template: drupal
  captured_at: '2021-10-17 13:58:07+00'
  capture_id: 721230
  wayback_url: https://web.archive.org/web/20211017135807id_/https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-04
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: w5f1s7x1
  capture_id: 721232
  url: https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
  wayback_url: https://web.archive.org/web/20220813040802id_/https://magic.wizards.com/en/articles/archive/latest-developments/dragons-maze-multiverse-2013-06-07
  captured_at: '2022-08-13 04:08:02+00'
  template: drupal
  sha256: caeef7cb9326d9b0b5be21f3805e892474f786478d280e1db89cb4f742ce1f2a
render_recovery: []
---
It's time once again to take a jaunt through the records of Multiverse, the database we use to store and work on the card files, and see what people were thinking about during the design and development of *Dragon's Maze*. Some comments will be insightful, some will be snarky, but I hope they are all entertaining.

But first, the cast:

![](https://i.ormos.uk/cc/88/cc886ad1801d000e9f8ccad3e73a31d571306e9ce45cdc656ac198f23d06f9f0.jpg)

**AF**—[Aaron Forsythe](https://web.archive.org/web/20140509102153/http://www.wizards.com/magic/magazine/archive.aspx?author=Aaron%20Forsythe)

![](https://i.ormos.uk/a3/b8/a3b88e7d7f0d7e9bc111f4e1149c808d9a8720ad945e30ef48046e924f760e83.jpg)

**DB**—[Doug Beyer](https://web.archive.org/web/20140518165222/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Doug%20Beyer)

![](https://i.ormos.uk/a9/0c/a90c93246e1c543ad1616b44e6648d77c13eeeea6364f3d3e7fbe09ed759b875.jpg)

**DEL**—Del Laugel

![](https://i.ormos.uk/89/be/89be87cd13e85cdfa6301f157dc41afff82903d838483860ee14e4361d9d5e30.jpg)

**GSV**—[Gavin Verhey](https://web.archive.org/web/20130619105806/http://www.wizards.com/magic/magazine/archive.aspx?author=Gavin%20Verhey)

![](https://i.ormos.uk/e0/0c/e00c2900e4532fed44efdbc0223f486ee1518c0cf594bb289867319eeda0f043.jpg)

**KD**—[Kelly Digges](https://web.archive.org/web/20130927013638/https://www.wizards.com/Magic/Magazine/Archive.aspx?author=Kelly%20Digges)

![](https://i.ormos.uk/73/dc/73dc2c209bef80978eea09781f3075d348fa6472480299108af0945ff889dce7.jpg)

**KEN**—[Ken Nagle](https://web.archive.org/web/20140327225845/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ken%20Nagle)

![](https://i.ormos.uk/2c/91/2c91c356c244bac703be5454524033ba3e82399c4aa0766ca588b15370ade280.jpg)

**Mago**—[Mark Gottlieb](https://web.archive.org/web/20130719134822/http://www.wizards.com/magic/magazine/archive.aspx?author=Mark%20Gottlieb)

![](https://i.ormos.uk/36/2b/362b9b8902548d4692f09924d01f0429d5ba1494d3c33b8acce1eeff05988df7.jpg)

**Max**—[Max McCall](https://web.archive.org/web/20140508203101/http://www.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)

![](https://i.ormos.uk/b4/9a/b49a97d847733a73985c5d85979f9c0df999dfc0380369be66282a7035d6c565.jpg)

**MJ**—Mons Johnson

![](https://i.ormos.uk/92/ce/92ceeab73eb3a7f33920535b070768559eb14c5b512cccee052bbb624575be15.jpg)

**MJG**—[Mark Globus](https://web.archive.org/web/20130706022422/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Globus)

![](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg)

**MR**—[Mark Rosewater](https://web.archive.org/web/20140501120753/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater)

![](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg)

**SPS**—[That's-a-me](https://web.archive.org/web/20130927012952/http://www.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard)

 

![](https://i.ormos.uk/98/ff/98ff84c36158a8091193fe55e8d3028e6e766bb343fd8e5051e08a78fcb62548.jpg)

**ZH**—[Zac Hill](https://web.archive.org/web/20140510005846/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Zac%20Hill)

 

And onto the file:

![Aetherling](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Aetherling)

 

 

> ZH 4/2: Now [Morphling](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) variant.  
>  AF 4/23: I can either give this -1/+1 or I can give it "infinite virtual toughness" by flickering it.  
>  ZH 4/23: Not if you want to deal damage.  
>  KD 4/24: Should this return under its owner's control or under your control?  
>  ZH 4/25: Owner's I think.  
>  MJG 4/30/12: I like this guy.  
>  Mago 4/30: I was looking forward to seeing the white & black [Morphling](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling)s before we got back around to blue. This guy seems scary/neat.  
>  ZH 6/11: Hump wanted a finisher that didn't die to Wrath. Trying an updated [Flicker](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flicker) ability now. Also adding a point of toughness to push for Constructed, and because most of our 'flowstone' guys aren't even-statted.  
>  KD 6/12: Previous 'lings have all had three colored-mana abilities and square stats.  
>  MR 6/26/12: A [Morphling](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) variant really needs to follow [Morphling](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling). I can handle not having square stats, but it really has to have five abilities.  
>  SPS 6/29/12 Is there a minor U ability we can throw on? Untapping seems too good, and untargetable, and flying both don't make a lot of sense.  
>  ZH 7/5: I added a new Gottlieb ability. Unsure if it fits.  
>  ZH 7/10: New new Gottlieb ability.  
>  Mago 7/10: The third ability could become "U: CARDNAME becomes all colors until end of turn" to save space.  
>  KD 8/22: Deleted color-changing trinket-text ability. Now looks less like [Morphling](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling), fits on card.

Text size is one of the hardest things for us to get around as a team. We are bound to having cards that can actually be read and actually fit on cards. While there was a desire to get Ætherling to better line up with the other [Morphling](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) variants, we couldn't do it and keep the text above our minimum-text-size requirements.

![Blood Baron of Vizkopa](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Blood+Baron+of+Vizkopa)

 

 

> DB 6/7/2012: Conditional flying can be sucky to concept. Can this have flying always or never?  
>  ZH 6/18: I reeeeeeeeeeeally would not like this to have a gargoyle concept. I reeeeeeeeeeally would like this to be a vampiric angel. I don't know if that is possible but I think it could be and I would hope it is.  
>  ZH 7/19: No more First Strike; killing words.  
>  SPS 9/4/12: I would like to change the pro white and black to activated abilities at B: pro white, W: pro black.  
>  KD 9/11: Changed numbers for DH. +1/+1 baseline, -1/-1 when pumped, costs 1 more.

As Doug mentioned, one of the issues with **Magic** is that we only get to show a card in one still frame. Cards that change dramatically can end up being very weird on the card, since you have to either show it in its first or final state. Still, Zac really pushed for the card, so that aspect of it didn't change.

In terms of strength, this was much stronger as a 3/3 for four and would often shut out heavy-white-based decks or Zombies pretty quickly, and first strike made it a pretty powerful blocker (who would sometimes awkwardly level up in the middle of combat, only to level back down after non-first-strike damage was dealt). We decided to make the change pretty late in development to the current stats, making it a bit beefier but giving other decks a better chance of having an established board before it came down.

![Deputy of Acquittals](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Deputy+of+Acquittals)

 

 

> ZH 4/17: Changed 'permanent' to 'creature'. Keeps most Jail stuff, dodges O-Ring tricks, is much simpler.  
>  ZH 4/23: "Another" to avoid Extort loops.  
>  Mago 4/30: It took me 2 minutes to figure out why this isn't strictly worse than [Whitemane Lion](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whitemane+Lion), but I eventually did. I like it.  
>  Max 5/22/12: Not too NWO friendly  
>  MR 6/26/12: Being "may" helps the NWO issue. Still confusing to new guy but he can simply not do it.  
>  Del 8/17: I don't see a good reason why that other creature isn't targeted. ([Whitemane Lion](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whitemane+Lion) was a weirdo PLC card that was meant to be perceived as having the "gating" mechanic, which hadn't targeted.)  
>  KD 9/17: Per DH, now targets.

Developers often template using old cards to get the words pretty close to right. Sometimes, especially when the card you are looking at is from *Time Spiral* block, this ends up with wordings we wouldn't use today. Luckily, editing is there to fix the problems.

![Fatal Fumes](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fatal+Fumes)

 

 

> Mago 4/30: 5 CMC is way over the top. Compare [Wring Flesh](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wring+Flesh), [Pull Under](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pull+Under), [Last Gasp](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Last+Gasp), [Grasp of Darkness](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grasp+of+Darkness)... This isn't strictly worse than any specific precedent, but it's ugly.  
>  ZH 6/18: After much complaining, I moved my favorite card in the set from 4B to 3B.

Zac Hill loved [Fatal Fumes](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fatal+Fumes) in a way that many other developers simply couldn't understand. Some believe it is because the 4 and 2 reminded him of a [Pillarfield Ox](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox). Others believed he liked ponderous removal. Yet others believed it had something to do with [Pillarfield Ox](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox) as well. But why, really? The world may never know.

![Melek, Izzet Paragon](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Melek%2C+Izzet+Paragon)

 

 

> ZH 4/20: Changed to 2/3 so I could add a cool, potentially bananas copy ability.  
>  Max 5/8: lol "potentially"  
>  ZH 6/6: 1/4 now because of the 2/3 in Hook  
>  GSV 6/11: Might be my favorite card in the set. My Johnny/Timmy cube senses are tingling.  
>  ZH 6/18: Shifted to 1/3 at Gavin's request.  
>  ZH 6/26: To six mana to distance from Ral and the RTR guy. Back to [Pillarfield Ox](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox). Moo.

Zac Hill loved himself a [Pillarfield Ox](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox).

![Ruric Thar, the Unbowed](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ruric+Thar%2C+the+Unbowed)

 

 

> KD 7/9: Art has two heads. Card doesn't have any two-headed mechanic. OK?  
>  Del 8/21: Trostani also has multiple heads. Must be something in the water on Ravnica.

While creatures are allowed to have as many heads as they want to without having a mechanical reinforcement (who are we to tell them how to live their lives?), we do have a long-established history of creatures with two heads either being harder to block or blocking better. It's always good that someone is looking out for these kinds of flavor issues and bringing them up to development.

![Savageborn Hydra](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Savageborn+Hydra)

 

 

> KEN 3/15/2012: [RoooooSHEEN!!](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=RoooooSHEEN%21%21) ZH 4/2: Now with trample!  
>  ZH 4/12: Now without trample. Big numbers are awesome!  
>  Mago 4/16: Sweet. I like the new ability more than trample here.  
>  ZH 6/4: Now as a sorcery.  
>  Del 6/4: Do you love it as much if one set of Xs needs to become Ys?  
>  MJ 6/14: I like this guy, but the activated ability might need to be toned down a bit.  
>  ZH 6/21: X twice didn't work. Using hybrid on suggestion from the team. Set has extort still, so we believe it's okay.

A little backstory on this. First off, yes, trample was pretty good. Originally, the Hydra was an XRG 0/0 double striker that entered the battlefield with X +1/+1 counters and had the ability: XRG: Put X +1/+1 counters on [Savageborn Hydra](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savageborn+Hydra). The **Magic** rules handle X well enough. It's pretty easy to figure out what to do when it appears on instants and sorceries. But permanents get a little weirder. You see, by choosing a value for X in the activated ability, you're choosing a value for \*all\* the Xs. Yep, the one in the corner, too. So, it turns out you can't use X like that. It's a time loop thing, I think. Like [*Back to the Future*](http://en.wikipedia.org/wiki/Back_to_the_Future). While it is easy for humans to parse what it intended, there are many cards in the past that have taken a similar approach and ended in disaster years later for **Magic Online** programmers or for rules managers trying to get them to work. I'm looking at you, [Illusionary Mask](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusionary+Mask).

![Trostani's Summoner](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Trostani%27s+Summoner)

 

 

> ZH 5/4: To Rhino to go up rather than down the chain.  
>  AF 5/10: Dust off your [Reveillark](https://web.archive.org/web/20130607000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reveillark)s!

The original version of this card was a 4/4 and made a 3/3, a 2/2, and two 1/1 birds. The current configuration was deemed to be more interesting. Aaron, in the way he likes to, immediately pointed out the busted thing this would allow. I don't think it's going to break Modern, but I would love to accomplish it in Cube or Commander.

![Vorel of the Hull Clade](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vorel+of+the+Hull+Clade)

 

 

> MJ 6/14: This guy's interaction with Planeswalkers might be a bit much.  
>  ZH 6/18: No longer works with Planeswalkers.  
>  Gideon 9/10: No longer works with what, exactly?

Awwwwkward.

 

* * *

 

That's it for this week's Multiverse wrap-up. As the summer approaches, there are lots of open weeks of columns for me and I'm interested in hearing what you all would like to read about. If you have any development-related questions or topics that you'd like to see me write about, use the email author link at the top of this article and send them to me. I can't guarantee that I can hit all of them, but I will try to do as many as a I can.

Sam
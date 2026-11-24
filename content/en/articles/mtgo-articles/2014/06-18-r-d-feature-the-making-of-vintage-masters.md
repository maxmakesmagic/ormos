---
id: 7188xsxb
kind: article
lang: en
path: /en/articles/mtgo-articles/2014/06-18-r-d-feature-the-making-of-vintage-masters
title: 'R&D Feature: The Making of Vintage Masters'
published: '2014-06-18'
column_slug: mtgo-articles
column: MTGO Articles
authors:
- slug: ian-duke-4e99a22e
  name: Ian Duke
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
    lang_detected: en
    capture_id: 948431
    url: http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
    captured_at: '2015-04-10 05:10:40+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
    lang_detected: en
    capture_id: 948431
    url: http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
    captured_at: '2015-04-10 05:10:40+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
    lang_detected: en
    capture_id: 948431
    url: http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
    captured_at: '2015-04-10 05:10:40+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
    lang_detected: en
    capture_id: 948431
    url: http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
    captured_at: '2015-04-10 05:10:40+00'
    rule: url.article_section
sources:
- document_id: 7188xsxb
  url: http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
  page_key: magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
  lang: en
  template: drupal
  captured_at: '2015-04-10 05:10:40+00'
  capture_id: 948431
  wayback_url: https://web.archive.org/web/20150410051040id_/http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
- document_id: 7188xsxb
  url: http://magic.wizards.com/en/articles/archive/rd-feature-making-vintage-masters-2014-06-18
  page_key: magic.wizards.com/en/articles/archive/rd-feature-making-vintage-masters-2014-06-18
  lang: en
  template: drupal
  captured_at: '2014-06-22 11:52:29+00'
  capture_id: 1146247
  wayback_url: https://web.archive.org/web/20140622115229id_/http://magic.wizards.com/en/articles/archive/rd-feature-making-vintage-masters-2014-06-18
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 7188xsxb
  capture_id: 948431
  url: http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
  wayback_url: https://web.archive.org/web/20150410051040id_/http://magic.wizards.com/en/articles/archive/mtgo-articles/rd-feature-making-vintage-masters-2014-06-18
  captured_at: '2015-04-10 05:10:40+00'
  template: drupal
  sha256: 1eaad38810f462ea8018333096e0933aa2b26ef2809387f1677b82a66bfc08e7
render_recovery: []
---
![](https://i.ormos.uk/27/d3/27d3ec1824e5a06d640da530a39d3a3e13d7b9b4f9750d39fcd58a9750365811.jpg)

![](https://i.ormos.uk/7b/6e/7b6e229fef727f7c9d6511da69d06064f1810f171e7994fa2e50d58c6921f1dc.png)

[Download ******Magic** Online****](https://web.archive.org/web/20140618000000/https://accounts.onlinegaming.wizards.com/) 

Welcome back for another inside look at *Vintage Masters*! Today, I'll be building on some things that I talked about in my earlier preview article. If you didn't get a chance to check that out, you can do so [here](/en/articles/makingmagic/2014/05-12-developing-vintage-masters). The last time you joined me was during preview period, so I could only talk about a narrow slice of what the set has to offer. Today, we can lift off the hood and get a much deeper look at what makes *Vintage Masters* tick and what it was like to work on.

Before we get ahead of ourselves, let's meet the teams!

Design Team

**Lead Designer – Max McCall**

![](https://i.ormos.uk/36/2b/362b9b8902548d4692f09924d01f0429d5ba1494d3c33b8acce1eeff05988df7.jpg)

At the time of *Vintage Masters's* design, Max McCall was part of R&D's digital team, which functions as a liaison between those of us who work on the design of **Magic**'s gameplay and those who implement our ideas on **Magic Online**. Max spearheaded the vision behind releasing the Power Nine cards on **Magic Online**. When we decided to include that release as part of a fully draftable experience, Max led the initial design for the *Vintage Masters* card file. As a long-time player and an avid fan of Eternal formats, Max was the perfect person for the job. Following his work on *Vintage Masters*, Max has since moved on to other projects. R&D wishes him the best of luck in his future pursuits.

**Designer – Ethan Fleischer**

![](https://i.ormos.uk/71/7e/717ec8ea013fe26416594283aa203c8c086fe7db5bfeb02641f7c432994f20bb.jpg)

Ethan is one of R&D's core designers. He recently led the design of *Journey Into Nyx*, and was part of the *Gatecrash*, *Theros*, *Born of the Gods*, and *Commander* (2013 Edition) teams. A **Magic** player since 1993, Ethan is the designer who is most in tune with eternal formats, and he keeps up with Vintage forums and metagame trends on a frequent basis. One of Ethan's not-so-secret agendas is getting **Magic** cards that don't currently exist in digital form onto **Magic Online** for the first time. He played a key role in *Vintage Masters's* design by identifying several such cards that would be useful for Constructed play and getting them into the set.

Development Team

**Lead Developer – Ian Duke**

![](https://i.ormos.uk/82/2b/822b917034ff4543ec86ea9e0a479c80f7232f507471856a098422ca9b0c809b.jpg)

That's me! I joined Wizards of the Coast in 2012 as a development intern, during which time I focused on Future Future League playtesting, balancing and tuning both individual cards and Constructed and Limited formats, and giving feedback to set leads. Since becoming a core developer I have had the opportunity to lead some projects of my own. *Vintage Masters* is the second set I led the development of, but it is the first to be released. I've been playing **Magic** since 1995, and consider competitive Legacy and Vintage my personal favorite Constructed formats.

**Developer – Adam Prosak**

![](https://i.ormos.uk/c0/a9/c0a94240f34bb8dddfba6ac5e334cbf89cb606c22e021336d1e084422d82ffe9.jpg)

A long-time tournament player, deck builder, and columnist, Adam joined Wizards in 2013 and progressed through the same development internship process that I had earlier. Recently, he has been inducted as a **Magic** core developer. *Vintage Masters* was one of Adam's first opportunities to show his development chops, and I can say he was a true asset to the team. Adam's encyclopedic knowledge of **Magic**'s early history and Constructed formats helped us to capture that vintage **Magic** feel.

**Developer – Max McCall**

![](https://i.ormos.uk/36/2b/362b9b8902548d4692f09924d01f0429d5ba1494d3c33b8acce1eeff05988df7.jpg)

Max carried over as the third official member of the development team. Having a continuity of vision from design through development is something we actively try to do for every **Magic** set, so Max was invaluable in that respect.

  
**Editor – Tim Aten**

![](https://i.ormos.uk/79/aa/79aa3f6b0ec8239d064b1235bef8d373790b129748e7bd8799b2a49b5c5581d8.jpg)

Tim was our editor for *Vintage Masters*, and I'd like to give him a special call out for his contributions to the set. In addition to maintaining the card file and all of his other editorial duties, Tim was an active participant in our playtests and helped us through many snags by poring over old set lists and finding just the right card to solve the problems we were facing. Like Adam, Tim has a truly astounding pool of knowledge about **Magic**'s history, and the team made sure to tap into that whenever possible.

Designing the Set

Designing *Vintage Masters* from the ground up was a daunting task. With more than twenty years' worth of card sets, the possibilities seemed endless. As I mentioned in my last article, in order to give the set some focus and to capture the nostalgic feel of **Magic**'s early era, we decided to restrict our focus to the set of cards that aren't currently Modern legal.

Even with that narrowing of scope, we still had some nine years' worth of cards to choose from! In order to make sure the set was doing its job, we had to set down what our goals were.

![](https://i.ormos.uk/d3/50/d35041aa949a49037d76188610ba5104533a33338060a8a6d77271082a65519c.png)

*   **Release the Power Nine on Magic Online**—This one was straightforward. Players have been clamoring for access to these cards for years, so we wanted to do it right.

  

<table><tbody><tr><td>&#10;			<ul><li><img src="http://www.wizards.com/mtg/images/digital/magiconline/spread_nature_cruel_dack.png"></li>&#10;				<li>&#10;				<p><a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nature%27s+Ruin">Nature's Ruin</a>, <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cruel+Bargain">Cruel Bargain</a>, and <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dack+Fayden">Dack Fayden</a></p>&#10;				</li>&#10;			</ul></td>&#10;		</tr></tbody></table>

*   **Bring the Vintage format online**—Previously, the Classic format was as close as players could get to playing Vintage on **Magic Online**. But beyond even the Power Nine, several other Constructed-relevant Vintage cards were not available in online Classic. We wanted to bring many of those cards online for the first time. This includes cards from older supplemental sets like *Portal* and *Starter 1999* and also many new cards from *Conspiracy*. Even after *Vintage Masters*, there will still be cards that don't yet exist in digital format, but we plan to continue working on those bit by bit (especially if Ethan has anything to say about it!)

  

<table><tbody><tr><td>&#10;			<ul><li><img src="https://i.ormos.uk/36/be/36beeed68eba48bf057676b9385c7ea3c7b3cf210fff55296e6ab7c49f1ffb54.png"></li>&#10;				<li>&#10;				<p><a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will">Force of Will</a>, <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop">Mishra's Workshop</a>, and <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Vault">Time Vault</a></p>&#10;				</li>&#10;			</ul></td>&#10;		</tr></tbody></table>

*   **Rerelease many cards essential to Vintage play**—Many of the cards players will need to play Vintage come from sets that weren't heavily drafted or haven't been available in a while, like *Mirage*, *Tempest*, and the *Masters Editions*. We wanted to give players another opportunity to access the cards, while still being respectful to those who already own them in their collections. Please understand that with the huge card pool of Vintage, not every card that sees play in that format will appear in the set. No matter how many we included, there will always be more on the list! All in all, I'm pleased with the number of exciting tournament cards we were able to fit into the set. If you're disappointed not to see one of your favorite cards, chances are high that we didn't simply overlook it. We plan on continuing to support the **Magic Online** eternal community through a variety of means.

  

<table><tbody><tr><td>&#10;			<ul><li><img src="http://www.wizards.com/mtg/images/digital/magiconline/spread_swords_counterspell_chain.png"></li>&#10;				<li>&#10;				<p><a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swords+to+Plowshares">Swords to Plowshares</a>, <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell">Counterspell</a>, and <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chain+Lightning">Chain Lightning</a></p>&#10;				</li>&#10;			</ul></td>&#10;		</tr></tbody></table>

*   **Create an awesome, nostalgic Limited format**—We know that many players add to their collections by playing Booster Draft, so we wanted to make sure that the experience of playing with the *Vintage Masters* set was as fun as possible. By capturing the feel of early **Magic**, we could provide a window into that era for newer players and a walk down memory lane for the old-timers. Our goal was to let you play with your favorite cards from **Magic**'s past in a format where we apply modern development principles, balance and polish.

With those goals in mind, the design team set to work populating the file with awesome, old-school **Magic** cards. If you like how the set turned out, don't forget to give the design team a shout out on the forums or social media at [@wizards\_magic](https://twitter.com/wizards_magic) or [@MagicOnline](https://twitter.com/MagicOnline). Max and Ethan did a great job laying the foundation for this awesome set.

First Playtests

In between the design and development phases for a set, we have a crossover period we (cleverly!) refer to as "devign." During this time, the development team checks in with design to get a sneak peak of how the set is looking and to give feedback in time for design to make necessary big-picture changes.

  

<table><tbody><tr><td>&#10;			<ul><li><img src="https://i.ormos.uk/e3/0a/e30aacd92673e22fad49418c9e2b561ac6f5defd6891c7b7efa548bfa3de4c26.png"></li>&#10;				<li>&#10;				<p><a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall">Ancestral Recall</a>, <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Bargain">Yawgmoth's Bargain</a>, and <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Survival+of+the+Fittest">Survival of the Fittest</a></p>&#10;				</li>&#10;			</ul></td>&#10;		</tr></tbody></table>

Our first devign playtest was super exciting. Hoots and hollers rang throughout the pit as players cracked open exciting cards like [Ancestral Recall](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall), [Yawgmoth's Bargain](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Bargain), and [Survival of the Fittest](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Survival+of+the+Fittest) (Hey, even playtest stickers of these cards are exciting!). The packs whisked around the table in a flurry, and when the dust settled there were a bunch of cool decks.

Unfortunately, when it came time to battle, a few of the strategies really weren't working. Design had tried inserting a couple ambitious strategies, including Slivers (focused in BR) and Onslaught's Birds (focused in WU). While the UG madness and UB storm decks were working right off the bat, these weaker tribal strategies were struggling to compete with powerful individual cards.

  

<table><tbody><tr><td>&#10;			<ul><li><img src="https://i.ormos.uk/22/86/22862ae48f49d705bc56910cae808739e080d661dcad304bbc732c3776920129.png"></li>&#10;				<li>&#10;				<p>Examples of cards that were cut from the set.</p>&#10;				</li>&#10;			</ul></td>&#10;		</tr></tbody></table>

The big takeaway for me was that we wanted to create more of those exciting moments of opening a powerful rare card or assembling a sweet combo. The players who were able to do so had a great time, but the players who weren't so lucky felt left out of the fun. The team set a goal of making sure that by the end of the development process, every person in a *Vintage Masters* draft would get to feel awesome by drafting powerful cards and ending up with a synergistic deck.

Entering Development

Our major tasks from the outset of development were rethinking some of the color-pair strategies, balancing the colors, and infusing the set with more fun and powerful cards and combinations.

In modern-day set development, we like to make sure that, at baseline, the ten two-color pairs have unique and viable strategies. That doesn't mean we want to prescribe exactly what each pair must do—we don't want to set players on fixed rails where they don't have meaningful decisions and creative choices. Instead, we just want to make sure that there aren't color combinations that don't work at all.

Often, when developing a set, if certain color combinations aren't working, it's worth going back and looking at what each color does individually, and then finding what strategies emerge organically when you combine them together. In the case of *Vintage Masters*, we looked to early Constructed decks to get inspiration for what each color was all about. By restructuring a few color pairs into more natural strategies, we not only got those decks to work, but actually allowed players to draft reasonable facsimiles of many real Constructed decks from throughout **Magic**'s history.

Marshall Sutcliffe's [earlier article](/en/articles/limitedinformation/2014/05-14-vintage-masters-archetype-breakdown) covered some of the basic strategies for each color pair. Once we were satisfied by this baseline gameplay, we sought to add further excitement and depth to the format by layering in additional combos and what we call sideways strategies. Some examples of sideways strategies from recent **Magic** sets include [Raid Bombardment](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raid+Bombardment) in *Rise of the Eldrazi*, [Furnace Celebration](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furnace+Celebration) in *Scars of Mirrodin*, and [Burning Vengeance](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Vengeance) or [Spider Spawning](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spider+Spawning) in *Innistrad*. If you enjoy those types of offbeat decks, you'll find them aplenty in *Vintage Masters*.

Here are a few examples of strategies and combos that came up during playtesting. We also left things open-ended enough that I'm sure you all will surprise us with your own unique decks and discoveries!

  

<table><tbody><tr><td>&#10;			<ul><li><img src="https://i.ormos.uk/be/28/be284f627dbd51ab150c4b24a4160e04c938e3009db7dec4fd0c62ca29999247.png"></li>&#10;				<li>&#10;				<p><a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrid+Imp">Putrid Imp</a>, <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Symbiotic+Wurm">Symbiotic Wurm</a>, and <a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Animate+Dead">Animate Dead</a></p>&#10;				</li>&#10;			</ul></td>&#10;		</tr></tbody></table>

*   RW cycling with [Astral Slide](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide) and [Lightning Rift](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Rift)
*   BG Reanimator ([Putrid Imp](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrid+Imp) + [Symbiotic Wurm](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Symbiotic+Wurm) + [Animate Dead](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Animate+Dead), anyone?)
*   [Saproling Burst](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saproling+Burst) and [Fires of Yavimaya](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fires+of+Yavimaya)
*   [Survival of the Fittest](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Survival+of+the+Fittest) with madness
*   [Battle Screech](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle+Screech), [Beetleback Chief](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beetleback+Chief), and [Rites of Initiation](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rites+of+Initiation)
*   [Upheaval](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Upheaval) and [Psychatog](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychatog)
*   Full Storm Combo with [Yawgmoth's Bargain](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Bargain), [Skirge Familiar](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skirge+Familiar), [Mind's Desire](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind%27s+Desire), and [Tendrils of Agony](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tendrils+of+Agony)

One particular playtest story I'd like to share with you came up during a game against Nik Davidson. Our game had gone long and it looked like Nik was starting to take control, but my UB deck had him down to 12 with some flying and shadow creatures backed up by [Man-o'-War](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War). I knew I had to act soon before I got locked out of the game. A [Brainstorm](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm), a [Dark Ritual](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual), and a [Yawgmoth's Will](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yawgmoth%27s+Will) later, I smiled as I showed Nik a 12-point [Tendrils of Agony](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tendrils+of+Agony) that would finish him off. Nik smiled back as he [Counterspelled](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspelled) one of the [Tendrils of Agony](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tendrils+of+Agony) copies and [Brain Freezed](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brain+Freezed) me for the rest of my library. Ouch!

We look forward to watching you all create your own exciting stories when the set hits **Magic Online**.

Guiding Rares

While we hammered on color balance and depth at the common and uncommon level, we also worked on the rares and mythic rares in the set. The issue we ran into was that we had a tremendous number of high-profile Constructed cards in the set, but not all of them played well in Limited. [Sphere of Resistance](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphere+of+Resistance) and [Flusterstorm](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flusterstorm) aren't exactly Limited all-stars, and while we tried to make an artifact deck work, ultimately there weren't many good options to support cards like [Tolarian Academy](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolarian+Academy) and [Mishra's Workshop](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop).

This meant that some players were opening sweet cards like [Survival of the Fittest](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Survival+of+the+Fittest) and fist-pumping their way into an awesome UG madness deck, while others didn't get any cool playable cards that would help them find an archetype. Our solution was to increase the number of rares in the set. Our solution was to increase the number of rares in the set. This let us infuse the set with more cool build-arounds to keep Limited exciting, without removing cards that are important for Constructed play. Without these additional rares aimed at Limited play, too many of the decks and synergies would be common-uncommon driven, leading to more repetitive gameplay.

<table><tbody><tr><td>&#10;			<ul><li><img src="https://i.ormos.uk/d4/26/d42695e3a965b731f2c7f0840476c7fd5c55d3b61ba627f5149b4bfc19fbdbbb.png"></li>&#10;				<li>&#10;				<p><a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare">Recurring Nightmare</a></p>&#10;				</li>&#10;			</ul></td>&#10;			<td>&#10;			<ul><li><img src="https://i.ormos.uk/c9/60/c960383dd4ae33d48c4fc6b0385627cabb69eef6622edf1fbb9f4402b84a113f.png"></li>&#10;				<li>&#10;				<p><a href="https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Decree+of+Justice">Decree of Justice</a></p>&#10;				</li>&#10;			</ul></td>&#10;		</tr></tbody></table>

Many of the cards we added in this pass are what we call "guiding rares"—powerful cards with unique effects that lead you down a specific path. In keeping with the nostalgic feel of the set, you’ll encounter some exciting cards that once saw high-profile Constructed play, like [Recurring Nightmare](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare) and [Decree of Justice](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Decree+of+Justice). We found these guiding rares to be one of the most fun parts of playing *Vintage Masters*. Since you see different ones each time, it makes every draft a unique experience. You don't need to open powerful rares to be successful in *Vintage Masters* Limited, but for players who need a little help finding a deck to draft, or simply want to do something cool and special, they are there to help.

Bon Voyage

While I could go on and on about what *Vintage Masters* has in store, it looks like we're just about out of time. That means it's time to turn the story over to you! What cards do you hope to open in your first *Vintage Masters* draft? What combos are you looking to assemble? Do you have a favorite deck from **Magic**'s past that you're looking to revisit in Limited form? Let me know on the forums or via email.

Until next time! May all your opening hands contain [Sol Ring](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sol+Ring), and your [Mind's Desire](https://web.archive.org/web/20140618000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind%27s+Desire) flips strike true.
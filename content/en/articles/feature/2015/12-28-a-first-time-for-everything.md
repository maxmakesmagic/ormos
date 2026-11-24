---
id: 4heh4pdk
kind: article
lang: en
path: /en/articles/feature/2015/12-28-a-first-time-for-everything
title: A First Time for Everything
published: '2015-12-28'
column_slug: feature
column: Feature
authors:
- slug: ethan-fleischer-9ff0be68
  name: Ethan Fleischer
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
    lang_detected: en
    capture_id: 626946
    url: https://magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
    captured_at: '2022-10-07 21:53:41+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
    lang_detected: en
    capture_id: 626946
    url: https://magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
    captured_at: '2022-10-07 21:53:41+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
    lang_detected: en
    capture_id: 626946
    url: https://magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
    captured_at: '2022-10-07 21:53:41+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
    lang_detected: en
    capture_id: 626946
    url: https://magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
    captured_at: '2022-10-07 21:53:41+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: 4heh4pdk
  url: https://magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
  page_key: magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
  lang: en
  template: drupal
  captured_at: '2022-10-07 21:53:41+00'
  capture_id: 626946
  wayback_url: https://web.archive.org/web/20221007215341id_/https://magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 4heh4pdk
  capture_id: 626946
  url: https://magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
  wayback_url: https://web.archive.org/web/20221007215341id_/https://magic.wizards.com/en/articles/archive/feature/first-time-everything-2015-12-28
  captured_at: '2022-10-07 21:53:41+00'
  template: drupal
  sha256: 2f898d1126b7461e2b064a35411c4ebf717679b80ae03d11d32a3b23c9e6547e
render_recovery: []
---
Hi! I'm Ethan Fleischer, lead designer of the latest *Magic* set, *Oath of the Gatewatch*. Today I'm going to talk about the nitty-gritty of how we made the set. Mark Rosewater laid out *what* we did in [his preview article](/en/articles/makingmagic/2015/12-29-a-solemn-oath-part-1). I'll talk about *how* we did it. I recommend you read Maro's article first, as it lays out the broad overview. Don't worry, I'll wait.

I'm waiting.

I'm waiting.

Jeez, it's not *that* long of an article! You went and got a sandwich, didn't you? Okay, let's do this!

# I C What You Did There

Where do ideas come from? Sometimes creative folks think them up from scratch, but far more often they adapt or combine other people's concepts to work in a new context. One of the most exciting and radical designs in *Oath of the Gatewatch* (*OGW*) shook out of the Great Designer Search 2. That was a huge online *Magic* design contest held five years ago. I won it, but my friend [Jon Loucks was a finalist](/en/articles/feature/2010/12-08-the-great-designer-search-2-finalists-jonathon-loucks), and some of his work for the contest really grabbed my interest. Jon pitched the idea of a new mana symbol, to appear in costs, that could only be paid with colorless mana, and a new basic land that produced colorless mana to go along with it. How radical! How exciting! A pseudo "sixth color," hiding in plain sight since *Limited Edition (Alpha)*!

Very early in *OGW* design, we attempted to nail down the signature mechanic for Kozilek's brood lineage of Eldrazi. We wanted it to feel distinct from Ulamog's ingest mechanic. We came up with lots of interesting ideas that felt appropriate to Kozilek's physics-warping nature, but none of them were deep enough to put on many cards and have those cards still feel distinct from each other. I decided that we could simply use all of them, and tie them together with the "C" mana symbol. Kozilek wouldn't have a keyword mechanic; he would have a slice of the "color" pie. This is a natural extension of the Eldrazi theme from *Battle for Zendikar*: the devoid mechanic, cards that care about casting colorless spells or controlling colorless creatures. It plays into the idea that all of the Eldrazi of a brood lineage are connected together pandimensionally by allowing Eldrazi Scions to circulate mana to the larger Eldrazi.

Players would need other sources of colorless mana besides Eldrazi Scions. I liked the idea that the Eldrazi were sucking the color out of Zendikar's mana as they rampaged over the plane. We quickly added a basic land to the set. Ari Levitch, the creative rep on the design team, suggested putting two versions of the land, which I dubbed "Wastes," into the set: one depicting Kozilek's distinctive trail of destruction, and one showing Ulamog's chalky ruins. We sprinkled in some nonbasic lands that could generate colorless mana as well.

![](http://media.wizards.com/2015/ogw_239nCi30ks3/en_Ju7JrU0QSJ.png)

Crumbling Vestige is a great enabler for Limited decks. The turn you play it, you can cast a card with devoid, then on subsequent turns you can activate the colorless-mana-activated abilities of that card.

In general, the places where we put colorless mana costs were different on lower-rarity cards than they were for higher-rarity cards. We knew that players would have to draft their colorless mana sources in Limited, so we put most of the colorless costs in activated abilities of Eldrazi creatures with devoid. These are similar in design to cards like [Boreal Centaur](https://web.archive.org/web/20151228000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boreal+Centaur) from *Coldsnap*. This would allow players to cast their creatures right away using the normal basic lands from the land box, and then activate their abilities once they'd drawn one of the colorless sources they'd drafted.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Boreal+Centaur)](https://web.archive.org/web/20151228000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boreal+Centaur)

We put most of the cards with colorless casting costs at rare or mythic rare, where they wouldn't impact Limited games as often. In Constructed, we knew players could put as many Wastes as they wanted into their decks, along with the pain lands from *Magic Origins* and the many colorless mana sources we'd included in *Battle for Zendikar* block. This would make it simple enough for them to reliably cast such monstrosities as Endbringer.

![](http://media.wizards.com/2015/ogw_239nCi30ks3/en_tQugbhcIXX.png)

As you can see, this eldritch abomination is quite hungry for colorless mana, but the power it represents makes it well worth crafting a special mana base for its deck!

Implementing colorless mana costs presented some big challenges to the design team. In many ways, those challenges were even greater for the teams downstream of us. Of particular note, the *Magic Online* and *Magic Duels* teams had to go through heroic efforts to implement colorless mana costs digitally, going so far as to completely refactor the mana systems of their respective games. They had to carve out time well in advance of when they would normally have started working on *OGW*, so massive props to the digital developers for all of their hard work!

# A Set by Any Other Name

Sometimes lining up the design of a set and its name and themes can be challenging. For example, my first lead design was *Journey into Nyx* (code named "Countrymen"), but the set we had initially designed was all about a war between the mortals and the gods, the *Iliad* to *Theros*'s *Odyssey*. When we decided instead to make the set's name about Elspeth's hero's journey, it meant that the name and mechanical themes were a bit out of alignment.

So for this lead design, I started nudging others about the name earlier. Note: the following exchange has been drastically altered for dramatic effect.

"Hey," I said, "I've started on 'Sweat,' a set that looks like it could be all about Kozilek, but I wanted to make sure to touch base about halfway through design to make sure we're on the same page."

"Oh! I'm so glad you got in touch with us so early!" they said. "As you know, 'Sweat' is part of a multi-set storyline. The most important event in 'Sweat,' in the overarching story, is that our heroes form a team of Planeswalkers. We'd like the name of the set to reflect that, though we know Kozilek plays a big role."

I paused for a moment, rolling the set so far over in my mind. Kozilek had a lot of really cool design space around him, but, you know what, so did teaming up to fight Kozilek.

"Actually," I said, "that's a really cool idea! Let's try it!"

I'm about to reveal one of my weaknesses as a designer. I only stretch to find new and exciting things if a problem demands that I do so. The non-Eldrazi parts of "Sweat" were pretty humdrum in comparison with Kozilek's stuff. This other perspective was just what I needed to motivate me to make something new. Something better.

I worked with my design team to figure out how we could express "Planeswalkers forming a team" with game mechanics. We found two satisfying angles of approach, and used them both in the set: cards that encouraged you to use of multiple planeswalker cards, and cards that rewarded you for having a teammate. This second category plays into the central metaphor of *Magic: The Gathering*—that "You are a Planeswalker."

So we made surge, a mechanic that refers to your teammates—your allied players in Two-Headed Giant, Emperor, and certain other multiplayer *Magic* formats. We (and the development team, of course!) balanced the mechanic such that the cards could be powerful in two-player games as well. Here's an example of a card with the surge mechanic:

![](http://media.wizards.com/2015/ogw_239nCi30ks3/en_XyMR5zIdDK.png)

As you can see, this card is both cheaper and more powerful if it's been set up with another spell. You can do this yourself, or your teammate can help you in a multiplayer game.

You'll also notice that the triggered ability only gives a bonus to your own creatures, not to your teammate's. This might seem to be at odds with the idea of teaming up. We playtested the cards in the Two-Headed Giant Draft format, and tried to balance them such that maximum fun was achieved. This meant, rather than adding as much power as possible to the cards in 2HG, we instead were able to find the most appropriate power level for the best gameplay, given the number of hours we were able to devote to 2HG playtests.

# TIL about BBA

I knew that *OGW* would, as the first small set in the new [two-blocks-per-year paradigm](/en/articles/feature/2015/08-24-metamorphosis-redux), set a lot of precedents. This caused me to question a lot of the ways we had done things in the past, as, if we were going to make a change, this would be a natural time to do so.

A lot of our players were a bit frustrated that, when drafting the second set of a block, they drafted only one booster pack of the small set (Set B) and two sets of the large set (Set A). Naturally, they would prefer to open more packs of Set B; that's where they could get the newest cards! The sets were designed and balanced to be most fun drafted this way (BAA), but I wondered if it would be possible to make a set that would be as fun (or at least *nearly* as fun) when drafted BBA.

One of the things that I quickly realized was that moving from a BAA system to a BBA system would allow us to have a more radical change in either the creative treatment or the mechanics (or both!) from the first set to the second set. This would help to keep things fresher for our most-dedicated drafters. Instead of a small, incremental change, they would experience a bigger shift in how things felt when playing with the new cards. This was an exciting prospect for me, and as you'll see, I changed things a *lot* from *Battle for Zendikar* to *Oath of the Gatewatch*.

One of the problems we've encountered in the past when drafting multiple packs of a small set is that there isn't much variety. You don't have as many different options when you open your first pack as you do with a large set. After some calculations, some discussion, and a lot of playtesting, we decided to increase the default set size of our small sets to accommodate BBA drafting. We added ten more common cards, and a few more rare and mythic rare cards as well. The commons would help to add a little more variety from draft to draft. The higher-rarity cards would add more from draft to draft, as well as giving our players more cool cards to collect.

Another problem that can crop up when drafting multiple boosters of a small set is that you see the same cards drafted last a lot. This problem is exacerbated when there's a low-powered cycle, such as the Runemark cycle from *Fate Reforged*. Then the last several picks all look more or less the same.

![](http://media.wizards.com/2015/images/daily/FEAT20151228_Runemarks.png)

We decided to avoid cycles entirely at common for *OGW*. Some future sets will be structured in such a way that common cycles will be important, and those will have to be designed with great care, but *OGW* wasn't that kind of set.

For more details about how we optimized *OGW* for BBA drafting, see [Sam Stoddard's article](/en/articles/latestdevelopments/2015/12-04-double-small-set-drafting) from last month.

# There's No "I" in Gatewatch

There have been teams of Planeswalkers who banded together against threats to the Multiverse in the past.

**The Nine Titans**

*   Urza
*   Bo Levar
*   Daria
*   Freyalise
*   Commodore Guff
*   Kristina of the Woods
*   Taysir
*   Tevesh Szat
*   Lord Windgrace

![](http://media.wizards.com/2015/images/daily/cardart_AP_False-Dawn.jpg)

[False Dawn](https://web.archive.org/web/20151228000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=False+Dawn) | Art by [Dave Dorman](https://web.archive.org/web/20151228000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Dave+Dorman%22%5D)

These Planeswalkers teamed up to thwart the Phyrexian invasion of Dominaria. It was a fractured alliance, and only a few members of the team survived the *Invasion* block storyline. Then they went their separate ways.

**The Three**

*   [Ugin](https://web.archive.org/web/20151228000000/http://magic.wizards.com/en/story/planeswalkers/ugin-spirit-dragon)
*   [Nahiri](https://web.archive.org/web/20151228000000/http://magic.wizards.com/en/story/planeswalkers/nahiri-lithomancer)
*   [Sorin Markov](https://web.archive.org/web/20151228000000/http://magic.wizards.com/story/planeswalkers/sorin-markov)

![](http://media.wizards.com/2015/images/daily/3PW_storyshot.jpg)

Art by [Igor Kieryluk](https://web.archive.org/web/20151228000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Igor+Kieryluk%22%5D)

Six thousand years ago, these Planeswalkers trapped the Eldrazi on the plane of Zendikar. Afterward, Ugin was sorely wounded by Nicol Bolas, and Nahiri's whereabouts are unknown. Ugin sent Sorin to bring Nahiri to Zendikar, but the vampire Planeswalker hasn't shown up since. For whatever reason, this team is no longer functioning to deal with the Eldrazi.

**The Gatewatch**

*   [Gideon Jura](https://web.archive.org/web/20151228000000/http://magic.wizards.com/story/planeswalkers/gideon-jura)
*   [Chandra Nalaar](https://web.archive.org/web/20151228000000/http://magic.wizards.com/story/planeswalkers/chandra-nalaar)
*   [Jace Beleren](https://web.archive.org/web/20151228000000/http://magic.wizards.com/story/planeswalkers/jace-beleren)
*   [Nissa Revane](https://web.archive.org/web/20151228000000/http://magic.wizards.com/story/planeswalkers/nissa-revane)

![](http://media.wizards.com/2015/ogw_239nCi30ks3/2ZSCPxatyF.jpg)

Art by [Yefim Kligerman](https://web.archive.org/web/20151228000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Yefim+Kligerman%22%5D)

*Magic*'s newest Planeswalker team-up is something new. This isn't a single-serving friendship, but a lasting commitment to protect the people of the Multiverse from threats that no one else can handle. This team will endure beyond *Battle for Zendikar* block and into the future of *Magic*'s storyline.

*Oath of the Gatewatch* is a new kind of *Magic* set, representing an unprecedented fusion of storyline and gameplay. I've been very excited to see it progress from my initial design to its final form as a *Magic* set. I hope that the ideas that formed the basis of that design will bear fruit in the form of novel and thrilling gameplay for you and your friends.
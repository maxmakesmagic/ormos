---
id: 0baddfvw
kind: article
lang: en
path: /en/articles/feature/2008/11-03-jace-vs-chandra
title: Jace vs. Chandra
published: '2008-11-03'
column_slug: feature
column: Feature
authors:
- slug: ken-nagle-1c7b6b00
  name: Ken Nagle
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
    lang_detected: en
    capture_id: 636803
    url: https://magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
    captured_at: '2021-05-01 04:23:03+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
    lang_detected: en
    capture_id: 636803
    url: https://magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
    captured_at: '2021-05-01 04:23:03+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
    lang_detected: en
    capture_id: 636803
    url: https://magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
    captured_at: '2021-05-01 04:23:03+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
    lang_detected: en
    capture_id: 636803
    url: https://magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
    captured_at: '2021-05-01 04:23:03+00'
    rule: url.article_section
    registry_match: registry.explicit
  duplicate_sources:
  - t1c9hs4s
sources:
- document_id: 0baddfvw
  url: https://magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
  page_key: magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
  lang: en
  template: drupal
  captured_at: '2021-05-01 04:23:03+00'
  capture_id: 636803
  wayback_url: https://web.archive.org/web/20210501042303id_/https://magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
- document_id: t1c9hs4s
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/11
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/11
  lang: en
  template: aspx
  captured_at: '2013-05-20 10:06:33+00'
  capture_id: 426885
  wayback_url: https://web.archive.org/web/20130520100633id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/11
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 0baddfvw
  capture_id: 636803
  url: https://magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
  wayback_url: https://web.archive.org/web/20210501042303id_/https://magic.wizards.com/en/articles/archive/feature/jace-vs-chandra-2008-11-03
  captured_at: '2021-05-01 04:23:03+00'
  template: drupal
  sha256: 21bfa14ee6226b0669fda533fd5f57d86ddd4023a247c7a3c3813a77f4b76cba
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 2
---
[![](https://i.ormos.uk/84/ee/84eefbb0b3644c2cadde0468f833d4cd8c1c024f09c60bc0eee5a19d1aa71ca6.jpg)](https://web.archive.org/web/20081103000000/http://archive.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/jacevschandra/productinfo)

Two humans stand opposed. Two eyes squint and glow. The other's eyes are covered.

The air vibrates bluish around one. The other's hair flares and ignites. Suddenly, energies collide and catastrophes scar the landscape.

Wait—they're no mere humans, are they?

Salutations and welcome to *Jace vs. Chandra* Week! Or, at least, my *Jace vs. Chandra* article—it's actually Naya Week, but *Jace vs. Chandra* releases this Friday. I've been asked to share with you a behind-the-scenes account of the **Magic** R&D process that went into creating *Duel Decks: Jace vs. Chandra*.

### In the Beginning

While I was a Wizards of the Coast design intern during the first half of 2007, the development of *Duel Decks: Elves vs. Goblins* by Devin Low and Noah Weil happened right beside me. Lots of real and fake Elf and Goblin cards could be found strewn across the marble-lacquered, depleted-uranium tables that the collective hive mind of **Magic** R&D uses to test **Magic** cards that are far too dangerous for the civilian public.

Fast-forward to nearly a year later, and I'm sitting in my own float pod amidst a galactic senate full of ambassadors from across the **Magic** spectrum (still) far more important and influential than myself.

The givens of codename "Duel Decks 2: The Sequel" were many:

*   *Duel Decks: Elves vs. Goblins* was a success, and we wanted to do another (also successful) one.
*   It would follow the soon-to-be-familiar "EntityA vs. EntityB" paradigm.
*   The packaging would be similar along with all that entails, with two showcased foil cards, etc.
*   The product would use only existing card designs. (This is usually a given, but it never hurts to ask!)

The crack team assigned to "Duel Decks 2" included:

*   Designer Kenneth Nagle
*   Developer Erik Lauer
*   Editor Del Laugel
*   Creative Director Brady Dommermuth
*   Art Director Jeremy Jarvis

### Brainstorming the Theme

For your own good, I'm going to skip this part. The only thing that matters is that we eventually chose *Jace vs. Chandra* for the product name and theme. The two premium foil cards would be [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren) and [Chandra Nalaar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar).

### Creative

[![Demonfire](https://i.ormos.uk/f4/bc/f4bcd00093855115b9540602c90f08bf75ae3a2c57f00998c8398a130dc0fa80.jpg)](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Demonfire)

Working directly with the creative team on projects is a social experiment on its own. Planeswalkers are our central, recurring storyline characters, traveling to different planes (a storytelling vehicle not too unlike *Star Trek*). **Magic** cards appearing in a random distribution, having no guarantee of how few or many a customer with encounter, and having a single frame of illustration with tiny, uniformly typeset flavorfully equates to quite an ineffective storytelling device.

That said, a "Jace deck" and a "Chandra deck" might execute flavor better. We slated an early specification of two additional Jace alternate-art cards and two additional Chandra alternate-art cards.

The download from Creative specified and extremely easy deck theme for Chandra: Fire. Anything and everything Fire-themed would work, and coming from someone who has researched every red card in **Magic** with a fire in it, there are a *lot*—so many, in fact, that Creative Director Brady Dommermuth postulates that his final minutes working at Wizards of the Coast will be spent staring at a Multiverse record labeled "Yet Another Red Burn Spell" just before he snaps, driven insane by having to concept one too many spells that burn something.

Jace was a different story. While I'm sure an "ice" theme has leapt into your mind, [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren) is more adept with illusion and mental magic. This was not a happy thing for me as the designer to hear from Creative, but considering the Chandra deck theme was going to be a complete cakewalk, I decided to count my blessings.

### Design

There were considerable deck-building constraints for *Jace vs. Chandra*, including:

*   Maximizing fun
*   Ensuring back-and-forth game play
*   Choosing an appropriate power level
*   Choosing an appropriate complexity level (i.e. "keyword vocabulary")
*   Allowing "the planeswalker cards to be stars"
*   Choosing which cards to be alternate art
*   Catering to the flavor-driven player
*   Catering to the lapsed player
*   Catering to the casual player
*   Catering to the "bling bling" player (I'm one of these.)
*   Catering to the new player
*   Adhering to the Reserve List
*   Adhering to Extended legality rules

That last one really goosed my gander. It's a carry-over criterion from *Elves vs. Goblins* that I frankly don't see any upside in. I've played more than my fair share of casual **Magic** games (it's a valuable viewpoint I contribute to the collective **Magic** R&D hive mind), and *not once* can I recall an Extended-legality check from our games. The unwritten rules from my casual groups were:

*   You can't play more than 4 of one card except basic lands. (The basic deckbuilding rule of Magic that promotes variance.)
*   You can't play with a card that the group has collectively banned (frequently [Armageddon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armageddon) and its ilk).

Based on this, I appealed the legality requirement. The verdict came down from the heavens in favor, and that's why *Jace vs. Chandra* isn't Extended-legal.

The alternate arts were tackled early due to art commissioning requirements. As for the exact cards, we tried to leave ourselves leeway. The team settled on [Incinerate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate) and [Seal of Fire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seal+of+Fire) for Chandra, locking in [Seal of Fire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seal+of+Fire) because the art would depict an actual "seal" like its previous artworks. Jace was a left a bit more open-ended, with "a card drawing spell" and "a counterspell" locked in.

### Playtesting

I began playtesting with prototype *Jace vs. Chandra* decks. The panging thought in my brain was always, "If I were [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren) and I knew [Chandra Nalaar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar) was trying to kill me, what creatures would I summon? What spells would I cast?"

Jace would summon and cast:

*   [Narwhal](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Narwhal)
*   [Blue Elemental Blast](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blue+Elemental+Blast)
*   [Ether Well](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ether+Well)

Chandra answered the question similarly:

*   [Guma](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Guma)
*   [Red Elemental Blast](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Red+Elemental+Blast)
*   [Parch](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parch)

**Magic** is filled with these kinds of cards, and "metagaming" is the natural inclination for anyone who knows what their opponent will bring to the table. See *Jace vs. Chandra* developer Erik "Evil" Lauer's article [The Role of Hate](https://web.archive.org/web/20081103000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/10), which discusses color hosers in detail. Note that we would never put [Chill](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chill) or [Boil](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boil) into these decks, as those two cards are far more powerful in this matchup than Jace or Chandra could ever hope to be, even more powerful than every other card in the game. In fact, the only usable hosers I found were [Ether Well](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ether+Well) and [Parch](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Parch).

<table><tbody><tr><td><div><div><img alt="Narwhal" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Narwhal"></div></div></td><td><div><div><img alt="Guma" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Guma"></div></div></td></tr></tbody></table>

However, playtesting revealed that even [Guma](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Guma) and [Narwhal](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Narwhal) were invincible, unstoppable clocks that would require [Bottle Gnomes](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bottle+Gnomes) or [Moonglove Extract](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moonglove+Extract)s in both decks as answers.

The intermediate decklists for *Jace vs. Chandra* are almost unrecognizable. Here's a few of the more whimsical cards that were cut in playtesting:

**Jace**

*   [Belltower Sphinx](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Belltower+Sphinx)
*   [Millstone](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Millstone)
*   [Elixir of Vitality](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elixir+of+Vitality)

**Chandra**

*   [Searing Touch](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Touch)
*   [Firecat Blitz](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firecat+Blitz)

I found these cards fantastically fun, but they were ultimately purged during "The Great Powering Up" of both the Jace deck and the Chandra deck. (What can I do, The Pit is full of spikes!) Jace received a smattering of morph creatures like [Wall of Deceit](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Deceit) to convey his illusion magic and a complement in secret red hoser [Spire Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spire+Golem). Chandra's got a raw power-level upgrade with [Flametongue Kavu](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flametongue+Kavu) as well as her own sideways blue hoser in [Flamekin Brawler](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flamekin+Brawler). All in all, Erik Lauer did an exceptional job developing the back-and-forth game play of these decks even at their increased power level.

The Chandra deck ultimately crossed the finish line as "the attack deck."

#### Chandra's Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (1)

1 [Chandra Nalaar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChandra%5D+%5BNalaar%5D) 

##### Creature (20)

2 [Flamekin Brawler](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamekin%5D+%5BBrawler%5D) 1 [Fireslinger](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireslinger%5D) 2 [Soulbright Flamekin](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulbright%5D+%5BFlamekin%5D) 1 [Pyre Charger](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyre%5D+%5BCharger%5D) 2 [Slith Firewalker](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BFirewalker%5D) 1 [Flamewave Invoker](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamewave%5D+%5BInvoker%5D) 2 [Inner-Flame Acolyte](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInner-Flame%5D+%5BAcolyte%5D) 1 [Flametongue Kavu](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlametongue%5D+%5BKavu%5D) 2 [Furnace Whelp](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFurnace%5D+%5BWhelp%5D) 1 [Rakdos Pit Dragon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BPit%5D+%5BDragon%5D) 1 [Ingot Chewer](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIngot%5D+%5BChewer%5D) 2 [Oxidda Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidda%5D+%5BGolem%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Hostility](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHostility%5D) 

##### Sorcery (6)

2 [Firebolt](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirebolt%5D) 1 [Cone of Flame](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCone%5D+%5Bof%5D+%5BFlame%5D) 2 [Fireball](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireball%5D) 1 [Demonfire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonfire%5D) 

##### Instant (6)

2 [Incinerate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIncinerate%5D) 1 [Magma Jet](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagma%5D+%5BJet%5D) 1 [Flame Javelin](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlame%5D+%5BJavelin%5D) 2 [Fireblast](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireblast%5D) 

##### Enchantment (2)

2 [Seal of Fire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BFire%5D) 

##### Land (25)

1 [Keldon Megaliths](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeldon%5D+%5BMegaliths%5D) 24 [Mountain](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

60 Cards 

##### Red (33)

2 [Flamekin Brawler](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamekin%5D+%5BBrawler%5D) 1 [Fireslinger](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireslinger%5D) 2 [Soulbright Flamekin](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulbright%5D+%5BFlamekin%5D) 1 [Pyre Charger](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyre%5D+%5BCharger%5D) 2 [Slith Firewalker](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BFirewalker%5D) 1 [Flamewave Invoker](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamewave%5D+%5BInvoker%5D) 2 [Inner-Flame Acolyte](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInner-Flame%5D+%5BAcolyte%5D) 1 [Flametongue Kavu](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlametongue%5D+%5BKavu%5D) 2 [Furnace Whelp](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFurnace%5D+%5BWhelp%5D) 1 [Rakdos Pit Dragon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BPit%5D+%5BDragon%5D) 1 [Ingot Chewer](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIngot%5D+%5BChewer%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Hostility](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHostility%5D) 1 [Chandra Nalaar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChandra%5D+%5BNalaar%5D) 2 [Firebolt](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirebolt%5D) 2 [Seal of Fire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BFire%5D) 2 [Incinerate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIncinerate%5D) 1 [Magma Jet](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagma%5D+%5BJet%5D) 1 [Flame Javelin](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlame%5D+%5BJavelin%5D) 1 [Cone of Flame](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCone%5D+%5Bof%5D+%5BFlame%5D) 2 [Fireblast](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireblast%5D) 2 [Fireball](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireball%5D) 1 [Demonfire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonfire%5D) 

##### Colorless (27)

1 [Keldon Megaliths](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeldon%5D+%5BMegaliths%5D) 24 [Mountain](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Oxidda Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidda%5D+%5BGolem%5D) 

60 Cards 

##### 1 (9)

2 [Flamekin Brawler](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamekin%5D+%5BBrawler%5D) 2 [Firebolt](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirebolt%5D) 2 [Seal of Fire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BFire%5D) 2 [Fireball](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireball%5D) 1 [Demonfire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonfire%5D) 

##### 2 (9)

1 [Fireslinger](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireslinger%5D) 2 [Soulbright Flamekin](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulbright%5D+%5BFlamekin%5D) 1 [Pyre Charger](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyre%5D+%5BCharger%5D) 2 [Slith Firewalker](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BFirewalker%5D) 2 [Incinerate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIncinerate%5D) 1 [Magma Jet](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagma%5D+%5BJet%5D) 

##### 3 (3)

1 [Flamewave Invoker](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamewave%5D+%5BInvoker%5D) 2 [Inner-Flame Acolyte](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInner-Flame%5D+%5BAcolyte%5D) 

##### 4 (4)

1 [Flametongue Kavu](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlametongue%5D+%5BKavu%5D) 2 [Furnace Whelp](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFurnace%5D+%5BWhelp%5D) 1 [Rakdos Pit Dragon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BPit%5D+%5BDragon%5D) 

##### 5 (3)

1 [Ingot Chewer](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIngot%5D+%5BChewer%5D) 1 [Chandra Nalaar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChandra%5D+%5BNalaar%5D) 1 [Cone of Flame](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCone%5D+%5Bof%5D+%5BFlame%5D) 

##### 6 (7)

2 [Oxidda Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidda%5D+%5BGolem%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Hostility](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHostility%5D) 1 [Flame Javelin](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlame%5D+%5BJavelin%5D) 2 [Fireblast](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireblast%5D) 

35 Cards 

##### Common (39)

24 [Mountain](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Flamekin Brawler](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamekin%5D+%5BBrawler%5D) 1 [Fireslinger](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireslinger%5D) 2 [Soulbright Flamekin](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoulbright%5D+%5BFlamekin%5D) 2 [Inner-Flame Acolyte](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInner-Flame%5D+%5BAcolyte%5D) 1 [Ingot Chewer](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIngot%5D+%5BChewer%5D) 2 [Oxidda Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOxidda%5D+%5BGolem%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 2 [Seal of Fire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeal%5D+%5Bof%5D+%5BFire%5D) 2 [Incinerate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIncinerate%5D) 

##### Uncommon (17)

1 [Keldon Megaliths](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKeldon%5D+%5BMegaliths%5D) 1 [Pyre Charger](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyre%5D+%5BCharger%5D) 2 [Slith Firewalker](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BFirewalker%5D) 1 [Flamewave Invoker](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlamewave%5D+%5BInvoker%5D) 1 [Flametongue Kavu](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlametongue%5D+%5BKavu%5D) 2 [Furnace Whelp](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFurnace%5D+%5BWhelp%5D) 2 [Firebolt](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFirebolt%5D) 1 [Magma Jet](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagma%5D+%5BJet%5D) 1 [Flame Javelin](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlame%5D+%5BJavelin%5D) 1 [Cone of Flame](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCone%5D+%5Bof%5D+%5BFlame%5D) 2 [Fireblast](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireblast%5D) 2 [Fireball](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFireball%5D) 

##### Rare (3)

1 [Rakdos Pit Dragon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRakdos%5D+%5BPit%5D+%5BDragon%5D) 1 [Hostility](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHostility%5D) 1 [Demonfire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonfire%5D) 

##### Mythic (1)

1 [Chandra Nalaar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChandra%5D+%5BNalaar%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Keldon+Megaliths)

[Deal Another Hand](https://web.archive.org/web/20081103000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Firebolt)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flamekin+Brawler)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fireball)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Inner-Flame+Acolyte)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flametongue+Kavu)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fireblast)

a:26:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Keldon Megaliths";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"24";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Flamekin Brawler";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Fireslinger";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Soulbright Flamekin";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Pyre Charger";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Slith Firewalker";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Flamewave Invoker";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Inner-Flame Acolyte";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Flametongue Kavu";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Furnace Whelp";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Rakdos Pit Dragon";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Ingot Chewer";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Oxidda Golem";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Chartooth Cougar";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Hostility";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Chandra Nalaar";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Firebolt";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Seal of Fire";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Incinerate";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Magma Jet";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Flame Javelin";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Cone of Flame";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Fireblast";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Fireball";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Demonfire";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Chandra's creatures are the better attackers mostly because of their "[Firebreathing](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firebreathing)" abilities ("![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif): This creature gets +1/+0 until end of turn."), making each of them individually dangerous. Coupled with a high curve, Chandra is more than capable of utilizing six or more [Mountain](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s of mana each turn for good effect. Chandra also has the largest blowout potential with [Hostility](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hostility) into Fireblast, creating 18 power of haste combat damage out of nowhere. Her [Keldon Megaliths](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keldon+Megaliths) is an intentional unsolvable threat. [Chandra Nalaar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar) herself is a very dangerous board controller that will quickly take over the game (my personal favorite planeswalker design).

By contrast, the Jace deck ended up being "the defense deck."

#### Jace's Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (1)

1 [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 

##### Creature (23)

1 [Martyr of Frost](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartyr%5D+%5Bof%5D+%5BFrost%5D) 2 [Fathom Seer](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFathom%5D+%5BSeer%5D) 1 [Voidmage Apprentice](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidmage%5D+%5BApprentice%5D) 2 [Wall of Deceit](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDeceit%5D) 1 [Willbender](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWillbender%5D) 1 [Bottle Gnomes](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 2 [Man-o'-War](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMan-o%27-War%5D) 1 [Ophidian](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOphidian%5D) 1 [Fledgling Mawcor](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFledgling%5D+%5BMawcor%5D) 1 [Waterspout Djinn](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWaterspout%5D+%5BDjinn%5D) 2 [Mulldrifter](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D) 1 [Air Elemental](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAir%5D+%5BElemental%5D) 1 [Guile](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGuile%5D) 1 [Riftwing Cloudskate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D) 2 [Spire Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BGolem%5D) 1 [Brine Elemental](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D) 1 [Quicksilver Dragon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuicksilver%5D+%5BDragon%5D) 1 [Errant Ephemeron](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErrant%5D+%5BEphemeron%5D) 

##### Sorcery (1)

1 [Ancestral Vision](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncestral%5D+%5BVision%5D) 

##### Instant (9)

1 [Daze](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDaze%5D) 2 [Counterspell](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCounterspell%5D) 2 [Repulse](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepulse%5D) 1 [Fact or Fiction](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFact%5D+%5Bor%5D+%5BFiction%5D) 1 [Gush](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGush%5D) 2 [Condescend](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCondescend%5D) 

##### Artifact (1)

1 [Mind Stone](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D) 

##### Land (24)

1 [Terrain Generator](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerrain%5D+%5BGenerator%5D) 23 [Island](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

##### Other (1)

1 Aethersnipe 

60 Cards 

##### Blue (31)

1 [Martyr of Frost](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartyr%5D+%5Bof%5D+%5BFrost%5D) 2 [Fathom Seer](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFathom%5D+%5BSeer%5D) 1 [Voidmage Apprentice](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidmage%5D+%5BApprentice%5D) 2 [Wall of Deceit](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDeceit%5D) 1 [Willbender](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWillbender%5D) 2 [Man-o'-War](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMan-o%27-War%5D) 1 [Ophidian](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOphidian%5D) 1 [Fledgling Mawcor](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFledgling%5D+%5BMawcor%5D) 1 [Waterspout Djinn](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWaterspout%5D+%5BDjinn%5D) 2 [Mulldrifter](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D) 1 [Air Elemental](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAir%5D+%5BElemental%5D) 1 [Guile](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGuile%5D) 1 [Riftwing Cloudskate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D) 1 [Brine Elemental](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D) 1 [Quicksilver Dragon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuicksilver%5D+%5BDragon%5D) 1 [Errant Ephemeron](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErrant%5D+%5BEphemeron%5D) 1 [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 1 [Ancestral Vision](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncestral%5D+%5BVision%5D) 1 [Daze](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDaze%5D) 2 [Counterspell](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCounterspell%5D) 2 [Repulse](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepulse%5D) 1 [Fact or Fiction](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFact%5D+%5Bor%5D+%5BFiction%5D) 1 [Gush](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGush%5D) 2 [Condescend](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCondescend%5D) 

##### Colorless (29)

1 [Terrain Generator](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerrain%5D+%5BGenerator%5D) 23 [Island](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 Aethersnipe 1 [Bottle Gnomes](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 2 [Spire Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BGolem%5D) 1 [Mind Stone](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D) 

60 Cards 

##### 1 (3)

1 [Martyr of Frost](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartyr%5D+%5Bof%5D+%5BFrost%5D) 2 [Condescend](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCondescend%5D) 

##### 2 (10)

2 [Fathom Seer](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFathom%5D+%5BSeer%5D) 1 [Voidmage Apprentice](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidmage%5D+%5BApprentice%5D) 2 [Wall of Deceit](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDeceit%5D) 1 [Willbender](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWillbender%5D) 1 [Mind Stone](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D) 1 [Daze](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDaze%5D) 2 [Counterspell](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCounterspell%5D) 

##### 3 (7)

1 [Bottle Gnomes](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 2 [Man-o'-War](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMan-o%27-War%5D) 1 [Ophidian](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOphidian%5D) 1 [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 2 [Repulse](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepulse%5D) 

##### 4 (3)

1 [Fledgling Mawcor](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFledgling%5D+%5BMawcor%5D) 1 [Waterspout Djinn](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWaterspout%5D+%5BDjinn%5D) 1 [Fact or Fiction](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFact%5D+%5Bor%5D+%5BFiction%5D) 

##### 5 (5)

2 [Mulldrifter](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D) 1 [Air Elemental](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAir%5D+%5BElemental%5D) 1 [Riftwing Cloudskate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D) 1 [Gush](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGush%5D) 

##### 6 (5)

1 [Guile](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGuile%5D) 2 [Spire Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BGolem%5D) 1 [Brine Elemental](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D) 1 [Quicksilver Dragon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuicksilver%5D+%5BDragon%5D) 

##### 7 (1)

1 [Errant Ephemeron](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErrant%5D+%5BEphemeron%5D) 

34 Cards 

##### Common (40)

23 [Island](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 Aethersnipe 1 [Martyr of Frost](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartyr%5D+%5Bof%5D+%5BFrost%5D) 2 [Fathom Seer](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFathom%5D+%5BSeer%5D) 1 [Voidmage Apprentice](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVoidmage%5D+%5BApprentice%5D) 1 [Bottle Gnomes](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 2 [Man-o'-War](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMan-o%27-War%5D) 1 [Ophidian](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOphidian%5D) 2 [Mulldrifter](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMulldrifter%5D) 2 [Spire Golem](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BGolem%5D) 1 [Errant Ephemeron](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BErrant%5D+%5BEphemeron%5D) 1 [Daze](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDaze%5D) 2 [Repulse](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRepulse%5D) 

##### Uncommon (14)

1 [Terrain Generator](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerrain%5D+%5BGenerator%5D) 2 [Wall of Deceit](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDeceit%5D) 1 [Willbender](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWillbender%5D) 1 [Fledgling Mawcor](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFledgling%5D+%5BMawcor%5D) 1 [Waterspout Djinn](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWaterspout%5D+%5BDjinn%5D) 1 [Air Elemental](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAir%5D+%5BElemental%5D) 1 [Riftwing Cloudskate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRiftwing%5D+%5BCloudskate%5D) 1 [Brine Elemental](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D) 1 [Mind Stone](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMind%5D+%5BStone%5D) 1 [Fact or Fiction](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFact%5D+%5Bor%5D+%5BFiction%5D) 1 [Gush](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGush%5D) 2 [Condescend](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCondescend%5D) 

##### Rare (4)

1 [Guile](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGuile%5D) 1 [Quicksilver Dragon](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuicksilver%5D+%5BDragon%5D) 2 [Counterspell](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCounterspell%5D) 

##### Mythic (2)

1 [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace%5D+%5BBeleren%5D) 1 [Ancestral Vision](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncestral%5D+%5BVision%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Terrain+Generator)

[Deal Another Hand](https://web.archive.org/web/20081103000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mind+Stone)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Waterspout+Djinn)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bottle+Gnomes)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Voidmage+Apprentice)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Condescend)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Repulse)

a:30:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Terrain Generator";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"23";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Martyr of Frost";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Fathom Seer";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Voidmage Apprentice";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Wall of Deceit";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Willbender";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Bottle Gnomes";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Man-o'-War";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Ophidian";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Fledgling Mawcor";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Waterspout Djinn";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Mulldrifter";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Air Elemental";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Guile";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Riftwing Cloudskate";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Spire Golem";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Brine Elemental";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Quicksilver Dragon";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Errant Ephemeron";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Jace Beleren";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Ancestral Vision";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Mind Stone";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:4:"Daze";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Counterspell";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Repulse";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Fact or Fiction";s:22:"field\_card\_image\_front";a:0:{}}}i:28;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:4:"Gush";s:22:"field\_card\_image\_front";a:0:{}}}i:29;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Condescend";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

Jace's creatures are the better defenders by miles. Jace's game play against Chandra largely consists of fortifying a stable defense then electing a solitary flyer or [Guile](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Guile) to play offense before a stray [Fireball](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball) or [Cone of Flame](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cone+of+Flame) fries your best-laid plans. Card drawing is in your favor but you are burdened with the necessity of finding suitable answers for Chandra's questions, or else a seemingly innocuous [Flamekin Brawler](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flamekin+Brawler) will melt your life total. [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren) himself is about as meek as he could be against Chandra's burn suite, but I've used his +2 ability first to good effect to pull him out of burn range.

### Alternate Art

*Jace vs. Chandra* comes with six new illustrations from **Magic** artists Kev Walker, Jason Chan, Matt Cavotta, Steve Prescott, and Christopher Moeller.

Here we see [Jace Beleren](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren) the planeswalker, uncowled and illusion-ready:

![](https://i.ormos.uk/5a/c9/5ac9a2fd51f5d4715e7a74a6166f1a4de1c411fb3164b6f159f43481f245fe15.jpg)*Art by Kev Walker*  

Next is [Chandra Nalaar](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chandra+Nalaar) with her signature fire-imbued gauntlets, goggles, and crimson locks:

![](https://i.ormos.uk/0e/43/0e430cd44e86da2a839e6616acf45f0a9cfbf39fc38fa0fa8ab20d2015fe6869.jpg)*Art by Kev Walker*  

The final resting place for the "Jace drawing cards" alternate art was [Fact or Fiction](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction):

![](https://i.ormos.uk/7c/ae/7caea6c14519cbeda376fe7b0f84e2a5942a756db61c1c58530ab9147220e7d0.jpg)*Yes, Matt Cavotta is being groan-inducingly funny.*  

As promised, here was see Chandra laying down a [Seal of Fire](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seal+of+Fire) for Jace to walk into:

![](https://i.ormos.uk/9b/21/9b21e6abe3b37ddb637b6a90da2c6f953f42dcded0b0bd4cd88c79cd5b6a8120.jpg)*Art by Christopher Moeller*  

And finally here they are fighting with [Incinerate](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incinerate) and [Counterspell](https://web.archive.org/web/20081103000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell), respectively, in a semi-connected panoramic action shot. You actually get two of each of these in *Jace vs. Chandra* (a blessing from Erik Lauer).

![](https://i.ormos.uk/e8/5b/e85bb337c75d94d43621402159f6032683d78f60c1e625d86d38990c1cad1da3.jpg)*Incinerate Art by Steve Prescott, Counterspell Art by Jason Chan*  

### Conclusion

And that's how *Duel Decks: Jace vs. Chandra* came into being. If you weren't a fan of Jace or Chandra before, I can only hope that my reminiscing and primitive salesmanship skills have at least given you second thoughts. As a "bling bling matters" player, I've already put these promotional alternate art cards into my Elder Dragon Highlander decks.

Not to give anything away, but *Jace vs. Chandra* is evidence that we could do more planeswalker-themed *Duel Decks* in the future. Maybe someday Chandra will fight an ice-themed planeswalker, and my ultimate wish will come true: a Fire in Chandra's deck and an Ice in the other.

![](https://i.ormos.uk/85/a8/85a87c1be96da00770e34f41a26cd734bff01dccc3a2c3f29d1ebb3ce1b1fb6b.jpg)
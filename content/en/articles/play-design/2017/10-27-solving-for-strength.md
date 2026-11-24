---
id: 26g2wzj5
kind: article
lang: en
path: /en/articles/play-design/2017/10-27-solving-for-strength
title: Solving for Strength
published: '2017-10-27'
column_slug: play-design
column: Play Design
authors:
- slug: adam-prosak-76cf4169
  name: Adam Prosak
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
    lang_detected: en
    capture_id: 1140807
    url: https://magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
    captured_at: '2019-04-22 20:29:33+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
    lang_detected: en
    capture_id: 1140807
    url: https://magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
    captured_at: '2019-04-22 20:29:33+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
    lang_detected: en
    capture_id: 1140807
    url: https://magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
    captured_at: '2019-04-22 20:29:33+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
    lang_detected: en
    capture_id: 1140807
    url: https://magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
    captured_at: '2019-04-22 20:29:33+00'
    rule: url.article_section
sources:
- document_id: 26g2wzj5
  url: https://magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
  page_key: magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
  lang: en
  template: drupal
  captured_at: '2019-04-22 20:29:33+00'
  capture_id: 1140807
  wayback_url: https://web.archive.org/web/20190422202933id_/https://magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 26g2wzj5
  capture_id: 1140807
  url: https://magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
  wayback_url: https://web.archive.org/web/20190422202933id_/https://magic.wizards.com/en/articles/archive/play-design/solving-strength-2017-10-27
  captured_at: '2019-04-22 20:29:33+00'
  template: drupal
  sha256: 8a89a05a9cf1c7588c3d2198826e0305e637ea0bda4fee7ffba9afac11167604
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 2
---
Before we begin, I want to direct your attention to [Mark Rosewater's article](/en/articles/makingmagic/2017/10-23-vision-design-set-design-and-play-design) from Monday. If you are interested in a behind-the-scenes look inside Wizards R&D, Mark explains a bit about how things are changing. I'm very excited for the future of *Magic* R&D and Play Design's role within R&D!

Today's article is a little different than most of our articles. Today, I'm going to talk about an interesting question, and the implications it has for how Play Design works on *Magic* sets.

Play Design operates mostly with incomplete information. We typically work three to four sets ahead of the real world. While you are all enjoying *Ixalan* (I hope!), Play Design is working diligently on Spaghetti, the 2018 fall set. The current overlap between our [Future Future League](/en/articles/play-design/2017/07-07-designing-hour-of-devastation-cards-to-meet-ffl-goals) and the real world is exactly one set: *Ixalan*. This means that the majority of the environment that we are attempting to figure out is very unknown. Although we can't look at (very much) real-world data, Play Design uses a variety of tactics to help guide us. We look at historical trends in *Magic* quite a bit. We look at past *Magic* environments and analyze what went right and what went wrong. We also do quite a bit of theorycrafting, and asking questions that are difficult (or even impossible) to answer can often help guide us toward useful information. Some such questions are . . .

# How often is the strongest deck found before the environment rotates?

If you're looking for a concrete answer, I'm afraid I can't help you. However, talking through this question (and many like it!) is important for Play Design to craft great play environments. This question leads to many other questions, which provide very useful insights throughout the Play Design process.

# What classifies a deck as the strongest?

Like many exercises, it's important to set parameters. For this exercise, I am going to classify "the strongest deck" as the following:

*   A Standard deck from the modern era. Non-rotating formats always have a process of deck discovery, usually due to new card releases. I want to focus on recent Standard environments, as many of our early Standard environments weren't played in large numbers, and there were rarely multiple tournaments for the *Magic* community to refine decks.
*   A deck that is more likely to win a tournament than any other. Examples include Faeries, Abzan Reanimator, Caw-Blade, and White-Blue Delver. If you were preparing for a tournament, choosing this deck would give you the best chance at winning the tournament. Sometimes, the strongest deck is also the most-played deck, but this exercise is not about popularity, only deck strength. This leads to the question, "What makes a deck strong?" but that's a topic for another article.
*   Any given Standard environment has exactly one best deck. Theoretically, there is only one true answer, but in our opinion, good Standard environments have disagreement on what the best deck is. It is possible (and desirable!) for the best deck to be weak to many different strategies.

# How would you find out about a strong deck after rotation?

**Our FFL Decks Are Stronger**  
  
 In theory, it is possible that our FFL decks are stronger than the real world. Whatever strongest deck we have built could be stronger than anything that is played in high-level tournaments. However, it is nearly impossible for that to be the case, for two reasons:

1.  Millions are better than dozens. There are millions of you, and only dozens of us within R&D. Those of us within R&D can't come close to the amount of exploration that all of you do once a set is released. One of my favorite things about working within R&D is seeing all the cool stuff that you come up with that we didn't even consider.
2.  During our playtesting, if every member of Play Design can agree on which deck is the best, we will likely change some cards so that we are uncertain about which deck is the strongest. Again, if a small number of play designers can discover what the strongest deck is, then it won't take very long for all of you to figure it out. If that happens, the process of exploration is lost, and the environment becomes staler, faster.

**Late-Season Discovery**

Oftentimes, the best deck is not found immediately. Two examples come to mind. The first is one of the most famous decks in the history of *Magic*, and in contention for one of the strongest decks ever. While it technically breaks the rules I outlined above (it is an old deck, and it is from the now-defunct Extended format), I can't help but share this deck.

#### Necro Donate, aka "Trix"

##### 

 ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Sorcery (8)

4 [Donate](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDonate%5D) 4 [Duress](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 

##### Instant (18)

4 [Dark Ritual](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BRitual%5D) 4 [Demonic Consultation](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonic%5D+%5BConsultation%5D) 4 [Force of Will](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForce%5D+%5Bof%5D+%5BWill%5D) 2 [Hoodwink](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHoodwink%5D) 4 [Vampiric Tutor](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BTutor%5D) 

##### Artifact (4)

4 [Mana Vault](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BVault%5D) 

##### Enchantment (8)

4 [Necropotence](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNecropotence%5D) 4 [Illusions of Grandeur](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIllusions%5D+%5Bof%5D+%5BGrandeur%5D) 

##### Land (22)

4 [Badlands](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBadlands%5D) 2 [City of Brass](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCity%5D+%5Bof%5D+%5BBrass%5D) 4 [Gemstone Mine](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGemstone%5D+%5BMine%5D) 4 [Underground River](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 4 [Underground Sea](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BSea%5D) 4 [Volcanic Island](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolcanic%5D+%5BIsland%5D) 

60 Cards 

##### Blue (14)

4 [Donate](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDonate%5D) 4 [Force of Will](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForce%5D+%5Bof%5D+%5BWill%5D) 2 [Hoodwink](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHoodwink%5D) 4 [Illusions of Grandeur](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIllusions%5D+%5Bof%5D+%5BGrandeur%5D) 

##### Black (20)

4 [Necropotence](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNecropotence%5D) 4 [Dark Ritual](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BRitual%5D) 4 [Demonic Consultation](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonic%5D+%5BConsultation%5D) 4 [Duress](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 4 [Vampiric Tutor](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BTutor%5D) 

##### Colorless (26)

4 [Badlands](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBadlands%5D) 2 [City of Brass](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCity%5D+%5Bof%5D+%5BBrass%5D) 4 [Gemstone Mine](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGemstone%5D+%5BMine%5D) 4 [Underground River](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 4 [Underground Sea](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BSea%5D) 4 [Volcanic Island](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolcanic%5D+%5BIsland%5D) 4 [Mana Vault](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BVault%5D) 

60 Cards 

##### 1 (20)

4 [Dark Ritual](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BRitual%5D) 4 [Demonic Consultation](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonic%5D+%5BConsultation%5D) 4 [Duress](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 4 [Vampiric Tutor](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BTutor%5D) 4 [Mana Vault](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BVault%5D) 

##### 2 (2)

2 [Hoodwink](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHoodwink%5D) 

##### 3 (8)

4 [Necropotence](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNecropotence%5D) 4 [Donate](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDonate%5D) 

##### 4 (4)

4 [Illusions of Grandeur](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIllusions%5D+%5Bof%5D+%5BGrandeur%5D) 

##### 5 (4)

4 [Force of Will](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForce%5D+%5Bof%5D+%5BWill%5D) 

38 Cards 

##### Common (14)

4 [Gemstone Mine](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGemstone%5D+%5BMine%5D) 4 [Dark Ritual](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDark%5D+%5BRitual%5D) 4 [Duress](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDuress%5D) 2 [Hoodwink](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHoodwink%5D) 

##### Uncommon (4)

4 [Demonic Consultation](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemonic%5D+%5BConsultation%5D) 

##### Rare (38)

4 [Badlands](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBadlands%5D) 2 [City of Brass](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCity%5D+%5Bof%5D+%5BBrass%5D) 4 [Underground River](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BRiver%5D) 4 [Underground Sea](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderground%5D+%5BSea%5D) 4 [Volcanic Island](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolcanic%5D+%5BIsland%5D) 4 [Donate](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDonate%5D) 4 [Force of Will](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForce%5D+%5Bof%5D+%5BWill%5D) 4 [Vampiric Tutor](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BTutor%5D) 4 [Illusions of Grandeur](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIllusions%5D+%5Bof%5D+%5BGrandeur%5D) 4 [Mana Vault](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMana%5D+%5BVault%5D) 

##### Mythic (4)

4 [Necropotence](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNecropotence%5D) 

60 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Necropotence)

[Deal Another Hand](https://web.archive.org/web/20171027000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Demonic+Consultation)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Duress)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=City+of+Brass)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Underground+Sea)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mana+Vault)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mana+Vault)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Volcanic+Island)

a:16:{i:0;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Necropotence";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Badlands";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"City of Brass";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Gemstone Mine";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Underground River";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Underground Sea";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Volcanic Island";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Dark Ritual";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Demonic Consultation";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Donate";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Duress";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Force of Will";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Hoodwink";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Vampiric Tutor";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Illusions of Grandeur";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Mana Vault";s:22:"field\_card\_image\_front";a:0:{}}}} 

Played by our current World Champion, William Jensen, at Grand Prix Philadelphia in 2000, this deck was packed with cards that currently find themselves on the Legacy banned and restricted list! Using [Vampiric Tutor](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampiric+Tutor) and [Demonic Consultation](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Consultation) to provide incredible consistency, the goal is to play a [Necropotence](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) early in the game. Fill up your hand via [Necropotence](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence), use [Illusions of Grandeur](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusions+of+Grandeur) to gain 20 life, then [Donate](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Donate) it to your opponent, who will lose 20 life once they can't pay for the cumulative upkeep.

The other example I have is from a recent Standard season. At [Pro Tour *Battle for Zendikar*](/en/articles/event-coverage/undated/pro-tour-battle-for-zendikar), Matt Nass finished well with the following deck that few other people played at the time.

#### Matt Nass's Four-Color Company

##### 

 ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (27)

3 [Sidisi's Faithful](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSidisi%5D+%5BFaithful%5D) 4 [Elvish Visionary](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BVisionary%5D) 4 [Jace, Vryn's Prodigy](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BVryn%5D+%5BProdigy%5D) 4 [Zulaport Cutthroat](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZulaport%5D+%5BCutthroat%5D) 4 [Catacomb Sifter](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCatacomb%5D+%5BSifter%5D) 4 [Nantuko Husk](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNantuko%5D+%5BHusk%5D) 4 [Grim Haruspex](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHaruspex%5D) 

##### Instant (8)

4 [Collected Company](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollected%5D+%5BCompany%5D) 4 [Rally the Ancestors](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRally%5D+%5Bthe%5D+%5BAncestors%5D) 

##### Land (25)

1 [Prairie Stream](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrairie%5D+%5BStream%5D) 2 [Sunken Hollow](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BHollow%5D) 2 [Canopy Vista](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCanopy%5D+%5BVista%5D) 4 [Evolving Wilds](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEvolving%5D+%5BWilds%5D) 4 [Polluted Delta](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolluted%5D+%5BDelta%5D) 4 [Flooded Strand](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlooded%5D+%5BStrand%5D) 4 [Windswept Heath](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindswept%5D+%5BHeath%5D) 1 [Forest](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 1 [Island](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Plains](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Swamp](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

60 Cards 

##### Sideboard (15)

4 [Dispel](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDispel%5D) 3 [Murderous Cut](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMurderous%5D+%5BCut%5D) 2 [Fleshbag Marauder](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFleshbag%5D+%5BMarauder%5D) 4 [Jaddi Offshoot](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaddi%5D+%5BOffshoot%5D) 2 [Anafenza, the Foremost](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnafenza,%5D+%5Bthe%5D+%5BForemost%5D) 

##### White (4)

4 [Rally the Ancestors](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRally%5D+%5Bthe%5D+%5BAncestors%5D) 

##### Blue (11)

3 [Sidisi's Faithful](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSidisi%5D+%5BFaithful%5D) 4 [Jace, Vryn's Prodigy](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BVryn%5D+%5BProdigy%5D) 4 [Dispel](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDispel%5D) 

##### Black (17)

4 [Zulaport Cutthroat](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZulaport%5D+%5BCutthroat%5D) 4 [Nantuko Husk](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNantuko%5D+%5BHusk%5D) 4 [Grim Haruspex](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHaruspex%5D) 3 [Murderous Cut](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMurderous%5D+%5BCut%5D) 2 [Fleshbag Marauder](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFleshbag%5D+%5BMarauder%5D) 

##### Green (12)

4 [Elvish Visionary](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BVisionary%5D) 4 [Collected Company](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollected%5D+%5BCompany%5D) 4 [Jaddi Offshoot](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaddi%5D+%5BOffshoot%5D) 

##### Multi colored (2)

2 [Anafenza, the Foremost](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnafenza,%5D+%5Bthe%5D+%5BForemost%5D) 

##### Colorless (29)

4 [Catacomb Sifter](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCatacomb%5D+%5BSifter%5D) 1 [Prairie Stream](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrairie%5D+%5BStream%5D) 2 [Sunken Hollow](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BHollow%5D) 2 [Canopy Vista](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCanopy%5D+%5BVista%5D) 4 [Evolving Wilds](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEvolving%5D+%5BWilds%5D) 4 [Polluted Delta](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolluted%5D+%5BDelta%5D) 4 [Flooded Strand](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlooded%5D+%5BStrand%5D) 4 [Windswept Heath](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindswept%5D+%5BHeath%5D) 1 [Forest](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 1 [Island](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Plains](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Swamp](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

75 Cards 

##### 1 (11)

3 [Sidisi's Faithful](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSidisi%5D+%5BFaithful%5D) 4 [Dispel](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDispel%5D) 4 [Jaddi Offshoot](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaddi%5D+%5BOffshoot%5D) 

##### 2 (16)

4 [Elvish Visionary](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BVisionary%5D) 4 [Jace, Vryn's Prodigy](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BVryn%5D+%5BProdigy%5D) 4 [Zulaport Cutthroat](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZulaport%5D+%5BCutthroat%5D) 4 [Rally the Ancestors](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRally%5D+%5Bthe%5D+%5BAncestors%5D) 

##### 3 (16)

4 [Catacomb Sifter](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCatacomb%5D+%5BSifter%5D) 4 [Nantuko Husk](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNantuko%5D+%5BHusk%5D) 4 [Grim Haruspex](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHaruspex%5D) 2 [Fleshbag Marauder](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFleshbag%5D+%5BMarauder%5D) 2 [Anafenza, the Foremost](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnafenza,%5D+%5Bthe%5D+%5BForemost%5D) 

##### 4 (4)

4 [Collected Company](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollected%5D+%5BCompany%5D) 

##### 5 (3)

3 [Murderous Cut](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMurderous%5D+%5BCut%5D) 

50 Cards 

##### Common (23)

3 [Sidisi's Faithful](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSidisi%5D+%5BFaithful%5D) 4 [Elvish Visionary](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BElvish%5D+%5BVisionary%5D) 4 [Nantuko Husk](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNantuko%5D+%5BHusk%5D) 4 [Evolving Wilds](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEvolving%5D+%5BWilds%5D) 1 [Forest](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 1 [Island](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 1 [Plains](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Swamp](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 4 [Dispel](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDispel%5D) 

##### Uncommon (17)

4 [Zulaport Cutthroat](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BZulaport%5D+%5BCutthroat%5D) 4 [Catacomb Sifter](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCatacomb%5D+%5BSifter%5D) 3 [Murderous Cut](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMurderous%5D+%5BCut%5D) 2 [Fleshbag Marauder](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFleshbag%5D+%5BMarauder%5D) 4 [Jaddi Offshoot](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaddi%5D+%5BOffshoot%5D) 

##### Rare (12)

4 [Grim Haruspex](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGrim%5D+%5BHaruspex%5D) 4 [Collected Company](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCollected%5D+%5BCompany%5D) 4 [Rally the Ancestors](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRally%5D+%5Bthe%5D+%5BAncestors%5D) 

##### Mythic (23)

4 [Jace, Vryn's Prodigy](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJace,%5D+%5BVryn%5D+%5BProdigy%5D) 1 [Prairie Stream](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrairie%5D+%5BStream%5D) 2 [Sunken Hollow](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunken%5D+%5BHollow%5D) 2 [Canopy Vista](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCanopy%5D+%5BVista%5D) 4 [Polluted Delta](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPolluted%5D+%5BDelta%5D) 4 [Flooded Strand](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlooded%5D+%5BStrand%5D) 4 [Windswept Heath](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindswept%5D+%5BHeath%5D) 2 [Anafenza, the Foremost](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnafenza,%5D+%5Bthe%5D+%5BForemost%5D) 

75 Cards 

![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sidisi%27s+Faithful)

[Deal Another Hand](https://web.archive.org/web/20171027000000/https://magic.wizards.com/en)

*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rally+the+Ancestors)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sidisi%27s+Faithful)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Canopy+Vista)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sunken+Hollow)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Evolving+Wilds)
*   ![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Catacomb+Sifter)

a:25:{i:0;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Sidisi's Faithful";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Elvish Visionary";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Jace, Vryn's Prodigy";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Zulaport Cutthroat";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Catacomb Sifter";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Nantuko Husk";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Grim Haruspex";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Collected Company";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Rally the Ancestors";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Prairie Stream";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sunken Hollow";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Canopy Vista";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Evolving Wilds";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Polluted Delta";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Flooded Strand";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Windswept Heath";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Dispel";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Murderous Cut";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Fleshbag Marauder";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Jaddi Offshoot";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Anafenza, the Foremost";s:22:"field\_card\_image\_front";a:0:{}}}} 

Despite being almost a complete no-show at Pro Tour *Battle for Zendikar*, this deck went on to dominate the Grand Prix circuit, firmly establishing itself as the strongest deck from that season. In theory, it could take longer than the entirety of that Standard season for a deck like this to be discovered. What if Matt Nass was interested in other decks? What if he was abducted by aliens? Would this deck ever get discovered?  
  
 Decks like [Rally the Ancestors](https://web.archive.org/web/20171027000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rally+the+Ancestors) give me some amount of confidence that we've gone entire Standard seasons without the strongest deck being discovered. However, I believe that among the millions of *Magic* players, the strongest deck is discovered a clear majority of the time. It's foolish to try to prove that something doesn't exist, so I can't really answer the original question with 100% confidence. In Play Design, we ask many questions like this. We work with lots of unknown variables, and must make educated guesses about the *Magic* environments we are creating. Our goal is to create environments that are fun and engaging, even if we can't fully solve them ourselves.

I hope you enjoyed this look at the kinds of questions Play Design seeks to answer as we balance strong decks in new environments. Melissa will be back next week with more Play Design insights!

—Adam
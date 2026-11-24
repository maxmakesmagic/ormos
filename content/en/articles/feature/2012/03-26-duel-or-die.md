---
id: 57g5bpf1
kind: article
lang: en
path: /en/articles/feature/2012/03-26-duel-or-die
title: Duel or Die
published: '2012-03-26'
column_slug: feature
column: Feature
authors:
- slug: markgottlieb
  name: Mark Gottlieb
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
    lang_detected: en
    capture_id: 621691
    url: https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
    captured_at: '2022-01-23 21:16:42+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
    lang_detected: en
    capture_id: 621691
    url: https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
    captured_at: '2022-01-23 21:16:42+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
    lang_detected: en
    capture_id: 621691
    url: https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
    captured_at: '2022-01-23 21:16:42+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
    lang_detected: en
    capture_id: 621691
    url: https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
    captured_at: '2022-01-23 21:16:42+00'
    rule: url.article_section
    registry_match: registry.explicit
  duplicate_sources:
  - r5n5s6gx
sources:
- document_id: 57g5bpf1
  url: https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
  page_key: magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
  lang: en
  template: drupal
  captured_at: '2022-01-23 21:16:42+00'
  capture_id: 621691
  wayback_url: https://web.archive.org/web/20220123211642id_/https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
- document_id: 57g5bpf1
  url: https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26
  page_key: magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26
  lang: en
  template: drupal
  captured_at: '2021-12-09 04:36:29+00'
  capture_id: 621536
  wayback_url: https://web.archive.org/web/20211209043629id_/https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26
- document_id: r5n5s6gx
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/188
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/188
  lang: en
  template: aspx
  captured_at: '2013-07-02 23:04:16+00'
  capture_id: 590057
  wayback_url: https://web.archive.org/web/20130702230416id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/188
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 57g5bpf1
  capture_id: 621691
  url: https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
  wayback_url: https://web.archive.org/web/20220123211642id_/https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26-0
  captured_at: '2022-01-23 21:16:42+00'
  template: drupal
  sha256: 3fb339cf4470885be51779a2416a5c081114880a3e2f8a80c02763f69420e813
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 6
---
Hello to everyone in Internetlandia! I haven't written anything for the **Magic** website in many a moon. Let's just say I was on an... extended vacation. But my parole officer is encouraging me to make a "good-faith attempt to re-enter society" (whatever *that* means), so here I am, back at my old stomping grounds. Today I'll be taking you behind the scenes of the creation of *[Duel Decks: Venser vs. Koth](https://web.archive.org/web/20120326000000/https://magic.wizards.com/en/articles/archive/announcing-duel-decks-venser-vs-koth-2011-08-18)*.

![](https://i.ormos.uk/9e/33/9e3322329d805cf573e9b478b0bbaf784fb1a5d6d34ad8bec4969b0eddd8e1ed.jpg)  

Leading a guided tour through *Duel Decks: Venser vs. Koth* is an exciting prospect for me. I was the primary developer who worked on this product, and I love love *love* the way it turned out. This is a super-fun matchup that features dynamic game play, big swings, appeal to different player types, unusual cards that turn out to be surprisingly good, and tons of flavor. And we'll get to all that. But those of you who remember [my stint](https://web.archive.org/web/20131214002535/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Gottlieb) as the writer of [House of Cards](https://web.archive.org/web/20130507084935/http://www.wizards.com/magic/magazine/archive.aspx?tag=house%20of%20cards&description=house%20of%20cards) (a Johnny-oriented wacky deck column) or my run as the writer of mtg.combos know that I tend to treat **Magic** articles less as opportunities to educate and more as excuses for works of short fiction. Sure, there's probably some **Magic** content in there somewhere, but we all know what the real attraction is. I'd never worked with our new content manager, [Trick](https://web.archive.org/web/20140325203011/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Trick%20Jarrett), before, though, so I didn't know if my flights of fancy would fly. I asked him if I could frame the piece within the madcap antics of some very lost conquistadors who wound up looking for gold in Antarctica. He said "No." I asked him if I could write the article from the perspective of the plush cactus toy that sits on [Mark Rosewater](https://web.archive.org/web/20140415025705/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20rosewater)'s desk. He said "Not this time." I asked him if I could make up a paragraph in which I pitched him dumb story ideas and he rejected them. He said "Yes," then he told me to get to the dang Duel Decks. Works for me.

### Theme Main Event

Let's start out by asking the most basic question. "*Venser vs. Koth*: Whaaaaa?" (Or, more loquaciously stated, "Why Planeswalkers... and why *these* Planeswalkers?")

![](https://i.ormos.uk/e5/a0/e5a0ffaa45352fbe0cb1707c73c3d3b2fe078d8057dff33647c6503b84266f2a.jpg)

[Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venser%2C+the+Sojourner) and [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Koth+of+the+Hammer) | Art by [Eric Dechamps](https://web.archive.org/web/20120326000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Eric+Dechamps%22%5D)

The most recent Duel Decks was Ajani vs. Nicol Bolas, which was a Planeswalker battle. This fit the pattern: the late-year Duel Decks featured Planeswalkers (such as Elspeth vs. Tezzeret), and the early-year Duel Decks featured thematic faction fights (such as Knights vs. Dragons). Starting this year, we've switched their order, resulting in two Planeswalker battles in a row. To understand why, let's take a trip through history. Do you remember... 2010?

In 2010, the early-year Duel Decks were Phyrexia vs. The Coalition. The theme was chosen as a primer/reminder/hype vehicle for the return of Phyrexia within the *Scars of Mirrodin* set later that year. But six months was way too long a lead time for this to have any significant impact or synergy. Then, in the Duel Decks of Elspeth vs. Tezzeret, we previewed a couple of *Scars of Mirrodin* cards. Rather than being a splashy tidbit, these previews dominated the conversation, overshadowing the Planeswalkers themselves. And now we've switched things up. Hmmmm. I'll let you draw your own conclusions... 

Now that we knew we'd feature Planeswalkers in this matchup, the question of which ones to shine a spotlight on fell to Director of **Magic** R&D Aaron Forsythe and **Magic** Creative Director Brady Dommermuth. 

Then they flipped coins. 

Kidding! They chose Venser and Koth because they're recent and relevant (as opposed to the more archaic [Ajani Vengeant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Vengeant) and Nicol Bolas, for example), they're different colors that enable different play styles, and they actually do fight one another in the storyline (briefly, before teaming up, but still). All in all, it's a cool, sexy matchup.

### I Feel a Draft

Now that we knew what the decks were about, it was time to make a first draft of the two decklists. And for that, the powers that be naturally turned to an ex-House of Cards columnist, someone who has proven himself to be a creative, wily, imaginative deck builder with his finger on the pulse of funtastical innovations: Mark Got Chris Millar???!?!??!

![](https://i.ormos.uk/a4/2a/a42a1ed8db9969993f4d12929d6c193f17b23af61ef2fe5e8be2ac5c33e2268d.jpg)  

Sorry, I meant "Chris Millar!!!" That's right, it takes not one but *two* former House of Cards columnists to create Duel Decks! Chris dove right into the project and came up with a couple of nifty decks that showcased each Planeswalker's personal styles, played well against one another, and, most crucially, *felt* right. Although fewer than half of the individual cards in the original decks made it through to the final product, these drafts did two very important jobs:

> *   They set the tone and themes of the decks.
> *   They provided the basis for choosing cards to give alternative art.

What are these themes? Venser's deck was built around his first two abilities. He likes to "blink" things (exile them, then return them to the battlefield), so the deck features cards that want to get blunk (such as those with "enters the battlefield" effects). Of course, that lends itself to including more blinking and self-bouncing effects to interact with them. Similarly, Venser likes to make things unblockable, so the deck features "saboteur" abilities (abilities that trigger when a creature deals combat damage to an opponent), and that lends itself to including more unblockability effects. Plus, since Venser is a tricky-smart white-blue mage, scry was included as an additional theme.

Koth is an earth mage. He has deep affinity for [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s, so the deck is focused on that: Getting more [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s onto the battlefield and taking advantage of those [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s. This includes a landfall theme, but it also includes cards that count [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s, and some that just check for [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s in other ways. The deck has a bit of a Bloodfire creature theme, and it also (at the time) had a Flowstone creature theme.

Here are the final decks, filled in with just the individual cards that were in that first draft.

#### Venser's Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (1)

1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Creature (7)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 

##### Sorcery (2)

2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 

##### Instant (3)

2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 

##### Enchantment (1)

1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 

##### Land (23)

1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

##### Other (1)

1 ??? 

38 Cards 

##### White (2)

1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 

##### Blue (7)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 

##### Multi colored (5)

1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Colorless (24)

1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 ??? 

38 Cards 

##### 1 (3)

1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 

##### 2 (4)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 

##### 3 (4)

1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 

##### 4 (1)

1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 

##### 5 (2)

1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

14 Cards 

##### Common (29)

1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 1 ??? 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 

##### Uncommon (7)

1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 

##### Rare (1)

1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 

##### Mythic (1)

1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

38 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flood+Plain)

[Deal Another Hand](https://web.archive.org/web/20120326000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scroll+Thief)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Venser%2C+the+Sojourner)

a:18:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Flood Plain";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"New Benalia";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sejiri Refuge";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Soaring Seacliff";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"11";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Augury Owl";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Cryptic Annelid";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Mistmeadow Witch";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Neurok Invisimancer";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Scroll Thief";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Windreaver";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:13;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Oblivion Ring";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Overrule";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Path to Exile";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Preordain";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Venser, the Sojourner";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

#### Koth's Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (1)

1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### Creature (10)

1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 

##### Sorcery (1)

1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 

##### Artifact (3)

1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### Land (25)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

##### Other (1)

1 ??? 

41 Cards 

##### Red (10)

1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### Colorless (31)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 1 ??? 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

41 Cards 

##### 1 (2)

2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### 2 (2)

2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 

##### 3 (3)

2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 

##### 4 (3)

1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### 5 (3)

1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 

##### 6 (1)

1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 

##### 8 (1)

1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 

15 Cards 

##### Common (33)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 ??? 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### Uncommon (5)

1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 

##### Rare (2)

1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 

##### Mythic (1)

1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

41 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

[Deal Another Hand](https://web.archive.org/web/20120326000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bloodfire+Kavu)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Torchling)

a:14:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"25";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Anger";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Bloodfire Colossus";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Bloodfire Kavu";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Earth Servant";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Geyser Glider";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Pilgrim's Eye";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Plated Geopede";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Torchling";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:10;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Spire Barrage";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Vulshok Battlegear";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Wayfarer's Bauble";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Koth of the Hammer";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

One of the most beautiful aspects of these decks, which survived intact all the way through development, is the "quasi-mirror" (in Chris's words) of [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Windreaver) vs. [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling). Love it!

![](https://i.ormos.uk/43/09/430926bec869d0168c667c1f9e755a2546d22399cc64c73cd14448e55606c4ed.jpg)  

### Heart to Art

At this relatively early stage, the creative team is looped in so we can coordinate our efforts in creating a deck experience that looks and feels as best as it can.

![](https://i.ormos.uk/80/6d/806d210327c38e7117a4f14bac077b2bb47ebf75a2c08a513605f898697388a6.jpg)  

One aspect of this is that we choose two cards per deck (besides the Planeswalkers) to get a new art treatment. These cards need to warrant this honor by being significantly appealing, by making sense with relation to the Planeswalker, and (in at least some cases) by having upgradable art. The cards we chose here were [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anger), [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plated+Geopede), [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Path+to+Exile), and [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Preordain).

![](https://i.ormos.uk/c5/79/c5793b67623f059b51dd6d6422c12bcdf99b0550c114216ec92720a5b5abc114.jpg)  

In addition, we run these decks by Brady Dommermuth and **Magic** Art Director Jeremy Jarvis for their feedback and comments. Typically, Brady will point out when cards don't make flavor sense, and Jeremy will point out when cards have art that, by modern standards, is not up to snuff. I'm too polite to mention any specifics, but while these reviews sometimes frustrate me (it's tough beats to take out a card I've become smitten with for its mechanics), this expert guidance is crucial in crafting a rich and immersive experience.

![](https://i.ormos.uk/13/25/13259d2c4018ab87f08d032414bf503763f79d8f003f141616cf52f86c052076.jpg)

[Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Preordain) | Art by [Scott Chou](https://web.archive.org/web/20120326000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Scott+Chou%22%5D)

### Refine and Dandy

At this stage, we do what we do best in R&D: playtest and refine. Over and over and over. We swap cards in and out. We speculatively try some cards just to see what they do (and often, what they do is come right back out of the decks). We balance the decks with one another so neither one is an auto-win. (And yes, if you think I'm trying to rub your nose in the fact that my job description includes "Play lots of **Magic**," I am. Nyaaaah.)

A few things jumped out right away, and a few things took time to come to the surface. I don't have a chronological log of each testing session, but here's what I focused on.

**\* Venser's deck was too strong.**

It just couldn't lose. A lot of the coarse early refinement was spent balancing the decks. In Chris's own words, one of the original "themes" of Venser's deck was "infinite 2-for-1s." Powerful? Yes. A recipe for good, dynamic game play? No. Some of the raw card advantage was removed.

![](https://i.ormos.uk/c9/72/c97287fb2d5df0e0aca42c2dbca8e1b6bed59b27773df6c0cec29d4fc875a11e.jpg)

[Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Path+to+Exile) | Art by [Erica Yang](https://web.archive.org/web/20120326000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Erica+Yang%22%5D)

**\* The search for saboteurs.**

White and blue aren't the most conducive colors for saboteur abilities, and a couple of the ones that started out in the deck ([Mask of Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mask+of+Memory) and [Augury Adept](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Augury+Adept)) were pretty much impossible to beat if they ever hit. This is some of that raw card advantage that needed to be stripped out. This was on top of [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scroll+Thief), which remained in the deck. Did these colors have any saboteurs that weren't straight-up card-drawing effects? At this point, [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slith+Strider) and [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sigil+of+Sleep) made it into the deck.

![](https://i.ormos.uk/ef/bf/efbf072fa8ff92b27e9726d99e9acf8495961b90ef92406e2dacf50260b0b5b4.jpg)  

**\* Venser's deck needed more opportunities to be clever.**

This deck spends some of its efforts removing and returning its creatures to the battlefield. When those creatures provide the same benefit each time (like gaining 4 life or scrying 3), that's fine, and useful. But when you have a different, interesting choice to make each time, the deck's depth is deepened. Chris's original draft had [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptic+Annelid), which is a perfect (and oddball) example of this line of thinking. I wanted more of that. To that end, I added in [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone), [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Plasma), and [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sawtooth+Loon). I also tried to broaden the range of effects a white-blue deck could create, which is how [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kor+Cartographer) got in there. (Coral Fighters showed up in a later draft for the same reason.)

![](https://i.ormos.uk/ab/29/ab29c573fdd2b53e697425264a75f67309f3822c5292e2c4c5e778be792e2caf.jpg)  

**\* Koth is Vulshok.**

Chris tipped his hat to this flavorful theme by including [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vulshok+Battlegear). I upped the theme with [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vulshok+Morningstar), [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vulshok+Berserker), and [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vulshok+Sorcerer). After all, Koth is Vulshok!

![](https://i.ormos.uk/2d/83/2d83c8e6ce72b0ae625539f59bf2e722227b8b5f87e20ad6b3122d90d5706b45.jpg)

[Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anger) | Art by [Svetlin Velinov](https://web.archive.org/web/20120326000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Svetlin+Velinov%22%5D)

**\* More Mountains!**

Chris's first draft counted [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s. Okay, but... I wanted to COUNT MOUNTAINS. [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wayfarer%27s+Bauble) and [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pilgrim%27s+Eye) were supplemented with [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Journeyer%27s+Kite), [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chartooth+Cougar), and [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armillary+Sphere). [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spire+Barrage) and [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earth+Servant) were supplemented with [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Downhill+Charge), [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jaws+of+Stone), [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seismic+Strike), and [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lithophage). We debated these changes. [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armillary+Sphere), [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jaws+of+Stone), and [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seismic+Strike) were just in the mono-red Dragons deck (of Knights vs. Dragons). However, since these cards are the only overlaps between the two decks, and they really make this deck hum, I decided they made too much sense not to include. Of course Koth, deals damage based on the number of [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s you control! [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lithophage) feels a bit counterintuitive, as it eats the [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s you've worked so hard to collect, but if any deck has the spare [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s needed to feed it, this is the one. Go go, 7/7 fatty! On the same "put your [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s to work" theme, I added another forgotten rare: [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volley+of+Boulders). Mana cost {8R} and flashback cost {RRRRRR}? *That* is some earth magic, and *this* is the deck that can pull that off.

![](https://i.ormos.uk/92/39/9239762602c7cef67e93e254cde45674e8d0a214247e05eb94c3121ef3c055b0.jpg)  

**\* More landfall!**

In a similar vein, the landfall theme felt perfect in Koth's [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)ous deck, so I turned up the amplitude a bit. [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cosi%27s+Ravager) showed up, as did [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Searing+Blaze). Koth's deck had always had a burn suite, but now its card selection in this area was strongly tied into its mechanical and flavorful themes.

![](https://i.ormos.uk/92/98/9298bbc67bb86215250ad0da0c09a95ff14d9717da87619c8a6462a7e536dbe1.jpg)

[Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plated+Geopede) | Art by [Johann Bodin](https://web.archive.org/web/20120326000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Johann+Bodin%22%5D)

**\* OMG emblems!**

Emblems were a technological innovation created late in *Scars of Mirrodin* development to allow Venser and Koth's ultimate abilities to work the way we ideally wanted them to. (You can think of an emblem like an enchantment that can't possibly be removed, except it's not technically an enchantment and it lives out in the command zone rather than the battlefield. You can think of the command zone as the place where rainbows and smiley faces are born.) We didn't print physical representations of those emblems in *Scars of Mirrodin*, but we had the opportunity to do so here! The creative team came up with an emblem treatment, and this Duel Decks was all set to be the world premiere of printed emblems... until [Sorin, Lord of Innistrad](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorin%2C+Lord+of+Innistrad) stole our thunder because *Dark Ascension* came out first. But now you know who's riding whose coattails. Anyway, since each deck would come with an emblem, we didn't have room on the press sheets to print any tokens, so I decided not to have any token-producing cards in these decks. It seemed cleaner that way.

![](https://i.ormos.uk/c4/60/c46086862a8d913ad8839e34be869d41ab52f84c873139ce0dd2257457abee72.jpg)  

After a couple months of testing, changing, and testing again, here's how the decks stood.

#### Venser's Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (1)

1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Creature (16)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Galepowder Mage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D) 1 [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 1 [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D) 1 [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 2 [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D) 1 [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D) 1 [Whitemane Lion](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 

##### Sorcery (2)

2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 

##### Instant (5)

2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 1 [Safe Passage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D) 1 [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D) 

##### Enchantment (3)

1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 

##### Land (24)

1 [Azorius Chancery](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

##### Other (1)

1 ??? 

52 Cards 

##### White (6)

1 [Galepowder Mage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D) 1 [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D) 1 [Whitemane Lion](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 1 [Safe Passage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D) 

##### Blue (12)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 1 [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 2 [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 1 [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D) 

##### Multi colored (9)

1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D) 1 [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 1 [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D) 1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Colorless (25)

1 [Azorius Chancery](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 ??? 

52 Cards 

##### 1 (4)

1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 1 [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D) 

##### 2 (5)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Whitemane Lion](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D) 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 

##### 3 (9)

1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 2 [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D) 1 [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Safe Passage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 

##### 4 (7)

1 [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Galepowder Mage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D) 1 [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D) 1 [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D) 1 [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D) 1 [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D) 

##### 5 (2)

1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

27 Cards 

##### Common (35)

1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 1 [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 1 [Whitemane Lion](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D) 1 ??? 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 1 [Safe Passage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D) 1 [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 

##### Uncommon (13)

1 [Azorius Chancery](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D) 2 [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D) 1 [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D) 

##### Rare (3)

1 [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D) 1 [Galepowder Mage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 

##### Mythic (1)

1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

52 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Chancery)

[Deal Another Hand](https://web.archive.org/web/20120326000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Overrule)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Slith+Strider)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Preordain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Augury+Owl)

a:31:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Azorius Chancery";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Flood Plain";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"New Benalia";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sejiri Refuge";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Soaring Seacliff";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"11";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Augury Owl";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Clone";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Cryptic Annelid";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Galepowder Mage";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Kor Cartographer";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Mistmeadow Witch";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Neurok Invisimancer";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Primal Plasma";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sawtooth Loon";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Scroll Thief";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Slith Strider";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Wall of Denial";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Whitemane Lion";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Windreaver";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:22;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Oblivion Ring";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Overrule";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Path to Exile";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Preordain";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Safe Passage";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Sigil of Sleep";s:22:"field\_card\_image\_front";a:0:{}}}i:28;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Steel of the Godhead";s:22:"field\_card\_image\_front";a:0:{}}}i:29;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Vanish into Memory";s:22:"field\_card\_image\_front";a:0:{}}}i:30;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Venser, the Sojourner";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

#### Koth's Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (1)

1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### Creature (16)

1 [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D) 1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D) 1 [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D) 

##### Sorcery (3)

1 [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 1 [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D) 

##### Instant (4)

1 [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D) 1 [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D) 2 [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D) 

##### Artifact (6)

1 [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D) 1 [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 1 [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### Land (25)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

##### Other (1)

1 ??? 

56 Cards 

##### Red (22)

1 [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D) 1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D) 1 [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D) 1 [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D) 1 [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D) 1 [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D) 2 [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 1 [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D) 1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### Colorless (34)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 1 ??? 1 [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D) 1 [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 1 [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

56 Cards 

##### 1 (2)

2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### 2 (6)

2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D) 1 [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D) 1 [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D) 1 [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D) 

##### 3 (8)

1 [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 1 [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D) 1 [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D) 2 [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 

##### 4 (5)

1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D) 1 [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D) 1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### 5 (4)

1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 

##### 6 (3)

1 [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D) 

##### 8 (1)

1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 

##### 9 (1)

1 [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D) 

30 Cards 

##### Common (42)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D) 1 [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D) 1 ??? 1 [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D) 1 [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D) 1 [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D) 2 [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### Uncommon (8)

1 [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D) 1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 1 [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D) 

##### Rare (5)

1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D) 1 [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D) 

##### Mythic (1)

1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

56 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

[Deal Another Hand](https://web.archive.org/web/20120326000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bloodfire+Kavu)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Koth+of+the+Hammer)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Armillary+Sphere)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Journeyer%27s+Kite)

a:28:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"25";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Æther Membrane";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Anger";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Bloodfire Colossus";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Bloodfire Kavu";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Chartooth Cougar";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Cosi's Ravager";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Earth Servant";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Geyser Glider";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Lithophage";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Pilgrim's Eye";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Plated Geopede";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Torchling";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Vulshok Berserker";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Vulshok Sorcerer";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:5:"Other";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";N;s:22:"field\_card\_image\_front";N;}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Armillary Sphere";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Downhill Charge";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Jaws of Stone";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Journeyer's Kite";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Searing Blaze";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Seismic Strike";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Spire Barrage";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Volley of Boulders";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Vulshok Battlegear";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Vulshok Morningstar";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Wayfarer's Bauble";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Koth of the Hammer";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

### Finish Them!

As you can see, the decks were really rounding into shape, but there were still some crucial aspects that needed to be improved.

**\* Go with the Flowstone.**

Playtester extraordinaire Mons Johnson was the first to make this point. Koth's deck featured a number of Flowstone creatures, which are a flavorful execution of earth magic. However, it was frustrating that you'd have eight [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s on the battlefield, but you'd be unable to pump up [Flowstone Shambler](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flowstone+Shambler) more than once (because it'd die!) I was reluctant to replace these with straight-up firebreathers because it reminded me of Chandra's deck. Notably, Koth's deck is the fourth mono-red Duel Deck, after Goblins, Chandra, and Dragons, so it was important that this played differently than all of those. But by this point, I was convinced that it would, so in came a couple [Fiery Hellhound](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Hellhound)s and a [Pygmy Pyrosaur](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pygmy+Pyrosaur).

![](https://i.ormos.uk/c6/4f/c64fa2b876014d662e3f018c0c96015827453021b4b9ba22fa8c5434f4f16621.jpg)  

**\* It's Millar time.**

After a spate of testing and changing, I looped Chris back in for his analysis and feedback. He was pretty happy with the progression the decks had taken, and made some excellent suggestions. The best one was to add [Stone Giant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Giant) to Koth's deck. It's so simple, so flavorful, so brilliant! What a combo with the new firebreathers. That went in immediately... and it caused me to look for other earth-themed cards. Naturally, I found one of the goofiest cards in recent memory: [Greater Stone Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Stone+Spirit). This *Coldsnap* throwback mines nostalgia for cards no one actually remembers: It's like a Stone Spirit that can cast Stonehands! I added it to Koth's deck as a lark, but soon found that it is *amazing* in there. It's a stupendous mana sink for Koth's million [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s; goofy or not, this dude is a dangerous threat. I am unreasonably proud of myself for adding this card to the deck.

![](https://i.ormos.uk/7d/21/7d21e3d1d1e117ba33f52a77b8098316b4803c823d6cb619ad4359dccaf94262.jpg)  

**\* The ping is the thing.**

One dismaying trend that we noticed in testing is that [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vulshok+Sorcerer) would dominate the battlefield if it showed up in a game. In a development note, I wrote that it kills seven of Venser's creatures outright, shutting down the deck and rendering many cards in the deck dead draws. On the other hand, it was a vital check to both [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Windreaver) and [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mistmeadow+Witch); I was concerned that if the Sorcerer was removed from the deck, *those* cards would become unstoppable. Rather than remove it, I opted to bend Venser's deck around fighting it to some extent. For example, the "When this enters the battlefield, you gain 4 life" card changed from [Lone Missionary](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lone+Missionary) to [Jedit's Dragoons](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jedit%27s+Dragoons). Plus, in another lightning strike of "perfect card, perfect time" similar to [Greater Stone Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Stone+Spirit), [Angelic Shield](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angelic+Shield) was added to Venser's deck. It's white-blue, it pumps up everything defensively to foil the Sorcerer and the damage-splitting spells, and it supports Venser's self-bounce/recast theme.

![](https://i.ormos.uk/f3/58/f3583af3709b0976eacd1af8d090c8521752bcba021654c996e7bd88fb760904.jpg)  

**\* Point/counterpoint.**

Let me expand on that last point for a bit. One of the most fun aspects of Duel Decks is that they're tuned to fight one another. That leads to opportunities for situational cards to shine like stars, or for cards that are normally amazingly good to maybe be a bit more balanced. For example, I added a pair of Walls into the decks earlier in development. Koth got the goofy card [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%C3%86ther+Membrane). It's fantastic flying defense in a mono-red deck... but Venser's deck *likes* to have many of its creatures bounced back to hand so they can be recast. Huh. Venser, meanwhile, got [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Denial), which Koth can't target at all... but which a pumped-up [Fiery Hellhound](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Hellhound) could take down without too much problem. However, if there's an 8/2 [Fiery Hellhound](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Hellhound) on the board, Venser's [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vanish+into+Memory) is a *stunning* card! It's good under normal circumstances, but when you're temporarily removing a threat from the board, drawing eight cards, and discarding only two? Like I said, stunning. [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrule) is also a fascinating card in this matchup. At first glance, it seems bad, because Koth's deck is so good at getting extra [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s out. But Koth's deck also casts plenty of gigantic spells, which are relatively easy to counter this way—while you gain some life to counteract Koth's burn.

![](https://i.ormos.uk/7e/7e/7e7e3a75ce7dbbe63d5769d9f1ff7b0853914b67e1598a6d9b52b8ae0a70404e.jpg)  

**\*Bomb Squad.**

I believe it was Erik Lauer who pointed out the last issue that we addressed. By now, Koth's deck was running like a dream. It would hold its own in the early game, staving off Venser's tricks and disruption while building its mana base... then, after a certain point, something would click and it'd start dropping haymakers. 4/10 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earth+Servant)! 9/1 [Pygmy Pyrosaur](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pygmy+Pyrosaur)! A couple of 6-damage [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Volley+of+Boulders) strikes! Venser's deck, on the other hand, could win through extremely careful tactics that generated incremental advantage over the course of the game, plus some small evasive attackers. Basically, things had to go perfectly, and you needed to play optimally. There was nearly no room for error. I had achieved the dichotomies of play styles that I wanted: Koth's deck for the brutal brawler, Venser's deck for the clever tactician. But Venser's deck needed some juice. Sometimes it needed the haymaker too. What was the point of all the scrying and [Looning](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sawtooth+Loon) if there wasn't anything specific to dig for? In came a couple of bomby rare win conditions: [Sunblast Angel](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunblast+Angel) and [Sphinx of Uthuun](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sphinx+of+Uthuun). If you want to attack with them for the win, great. If you want to blink them out and in for the win, great. The deck had been Venser than most... but now it was the Vensest.

![](https://i.ormos.uk/b0/43/b043f2af4ae0b2312e0581a4550d2de6403d1880881a287b167bd0ce744c62ab.jpg)  

#### Venser's Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (1)

1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Creature (23)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Cache Raiders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCache%5D+%5BRaiders%5D) 1 [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D) 1 [Coral Fighters](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoral%5D+%5BFighters%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Galepowder Mage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D) 1 [Jedit's Dragoons](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJedit%5D+%5BDragoons%5D) 1 [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D) 1 [Minamo Sightbender](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo%5D+%5BSightbender%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 1 [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D) 1 [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 1 [Sky Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BSpirit%5D) 2 [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D) 1 [Sphinx of Uthuun](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSphinx%5D+%5Bof%5D+%5BUthuun%5D) 1 [Sunblast Angel](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunblast%5D+%5BAngel%5D) 1 [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D) 1 [Whitemane Lion](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 

##### Sorcery (3)

2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 1 [Revoke Existence](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D) 

##### Instant (5)

2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 1 [Safe Passage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D) 1 [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D) 

##### Enchantment (4)

1 [Angelic Shield](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAngelic%5D+%5BShield%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 

##### Land (24)

1 [Azorius Chancery](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### White (9)

1 [Galepowder Mage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D) 1 [Jedit's Dragoons](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJedit%5D+%5BDragoons%5D) 1 [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D) 1 [Sunblast Angel](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunblast%5D+%5BAngel%5D) 1 [Whitemane Lion](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 1 [Revoke Existence](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D) 1 [Safe Passage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D) 

##### Blue (16)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Cache Raiders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCache%5D+%5BRaiders%5D) 1 [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D) 1 [Coral Fighters](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoral%5D+%5BFighters%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Minamo Sightbender](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo%5D+%5BSightbender%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 1 [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 2 [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D) 1 [Sphinx of Uthuun](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSphinx%5D+%5Bof%5D+%5BUthuun%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 1 [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D) 

##### Multi colored (11)

1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D) 1 [Sky Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BSpirit%5D) 1 [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 1 [Angelic Shield](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAngelic%5D+%5BShield%5D) 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 1 [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D) 1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### Colorless (24)

1 [Azorius Chancery](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### 1 (4)

1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 1 [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D) 

##### 2 (9)

1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Coral Fighters](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoral%5D+%5BFighters%5D) 1 [Minamo Sightbender](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo%5D+%5BSightbender%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Whitemane Lion](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D) 1 [Angelic Shield](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAngelic%5D+%5BShield%5D) 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Revoke Existence](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D) 

##### 3 (10)

1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 1 [Sky Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BSpirit%5D) 2 [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D) 1 [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Safe Passage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 

##### 4 (7)

1 [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Galepowder Mage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D) 1 [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D) 1 [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D) 1 [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D) 1 [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D) 

##### 5 (3)

1 [Cache Raiders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCache%5D+%5BRaiders%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

##### 6 (2)

1 [Jedit's Dragoons](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJedit%5D+%5BDragoons%5D) 1 [Sunblast Angel](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunblast%5D+%5BAngel%5D) 

##### 7 (1)

1 [Sphinx of Uthuun](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSphinx%5D+%5Bof%5D+%5BUthuun%5D) 

36 Cards 

##### Common (36)

1 [Soaring Seacliff](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D) 11 [Island](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 7 [Plains](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 1 [Augury Owl](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D) 1 [Jedit's Dragoons](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJedit%5D+%5BDragoons%5D) 1 [Kor Cartographer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D) 1 [Neurok Invisimancer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D) 1 [Primal Plasma](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D) 2 [Scroll Thief](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D) 1 [Whitemane Lion](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D) 2 [Overrule](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D) 1 [Path to Exile](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D) 2 [Preordain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D) 1 [Revoke Existence](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D) 1 [Safe Passage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D) 1 [Sigil of Sleep](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D) 1 [Steel of the Godhead](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D) 

##### Uncommon (18)

1 [Azorius Chancery](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 1 [Flood Plain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D) 1 [New Benalia](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D) 2 [Sejiri Refuge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D) 1 [Cache Raiders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCache%5D+%5BRaiders%5D) 1 [Coral Fighters](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoral%5D+%5BFighters%5D) 1 [Cryptic Annelid](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D) 1 [Minamo Sightbender](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo%5D+%5BSightbender%5D) 1 [Mistmeadow Witch](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D) 1 [Sawtooth Loon](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D) 1 [Sky Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BSpirit%5D) 2 [Slith Strider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D) 1 [Wall of Denial](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D) 1 [Angelic Shield](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAngelic%5D+%5BShield%5D) 1 [Oblivion Ring](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D) 1 [Vanish into Memory](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D) 

##### Rare (5)

1 [Clone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D) 1 [Galepowder Mage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D) 1 [Sphinx of Uthuun](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSphinx%5D+%5Bof%5D+%5BUthuun%5D) 1 [Sunblast Angel](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunblast%5D+%5BAngel%5D) 1 [Windreaver](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D) 

##### Mythic (1)

1 [Venser, the Sojourner](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D) 

60 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Chancery)

[Deal Another Hand](https://web.archive.org/web/20120326000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Overrule)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scroll+Thief)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scroll+Thief)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kor+Cartographer)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Galepowder+Mage)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Clone)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

a:39:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Azorius Chancery";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Flood Plain";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"New Benalia";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sejiri Refuge";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Soaring Seacliff";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"11";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Augury Owl";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Cache Raiders";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Clone";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Coral Fighters";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Cryptic Annelid";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Galepowder Mage";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Jedit's Dragoons";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Kor Cartographer";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Minamo Sightbender";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Mistmeadow Witch";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Neurok Invisimancer";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Primal Plasma";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sawtooth Loon";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Scroll Thief";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Sky Spirit";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Slith Strider";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Sphinx of Uthuun";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Sunblast Angel";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Wall of Denial";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Whitemane Lion";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Windreaver";s:22:"field\_card\_image\_front";a:0:{}}}i:28;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Angelic Shield";s:22:"field\_card\_image\_front";a:0:{}}}i:29;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Oblivion Ring";s:22:"field\_card\_image\_front";a:0:{}}}i:30;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Overrule";s:22:"field\_card\_image\_front";a:0:{}}}i:31;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Path to Exile";s:22:"field\_card\_image\_front";a:0:{}}}i:32;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Preordain";s:22:"field\_card\_image\_front";a:0:{}}}i:33;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Revoke Existence";s:22:"field\_card\_image\_front";a:0:{}}}i:34;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Safe Passage";s:22:"field\_card\_image\_front";a:0:{}}}i:35;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Sigil of Sleep";s:22:"field\_card\_image\_front";a:0:{}}}i:36;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Steel of the Godhead";s:22:"field\_card\_image\_front";a:0:{}}}i:37;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Vanish into Memory";s:22:"field\_card\_image\_front";a:0:{}}}i:38;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Venser, the Sojourner";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

#### Koth's Deck

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (1)

1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### Creature (21)

1 [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D) 1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 2 [Fiery Hellhound](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BHellhound%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Greater Stone Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BStone%5D+%5BSpirit%5D) 1 [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Pygmy Pyrosaur](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPygmy%5D+%5BPyrosaur%5D) 1 [Stone Giant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStone%5D+%5BGiant%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D) 1 [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D) 

##### Sorcery (3)

1 [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 1 [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D) 

##### Instant (4)

1 [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D) 1 [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D) 2 [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D) 

##### Artifact (6)

1 [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D) 1 [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 1 [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### Land (25)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 

60 Cards 

##### Red (27)

1 [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D) 1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 2 [Fiery Hellhound](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BHellhound%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Greater Stone Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BStone%5D+%5BSpirit%5D) 1 [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Pygmy Pyrosaur](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPygmy%5D+%5BPyrosaur%5D) 1 [Stone Giant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStone%5D+%5BGiant%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D) 1 [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D) 1 [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D) 1 [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D) 1 [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D) 2 [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 1 [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D) 1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### Colorless (33)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 1 [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D) 1 [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 1 [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

60 Cards 

##### 1 (2)

2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### 2 (7)

2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Pygmy Pyrosaur](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPygmy%5D+%5BPyrosaur%5D) 1 [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D) 1 [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D) 1 [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D) 1 [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D) 

##### 3 (10)

1 [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D) 2 [Fiery Hellhound](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BHellhound%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 1 [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D) 1 [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D) 2 [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 

##### 4 (6)

1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D) 1 [Stone Giant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStone%5D+%5BGiant%5D) 1 [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D) 1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

##### 5 (4)

1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 

##### 6 (4)

1 [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Greater Stone Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BStone%5D+%5BSpirit%5D) 1 [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D) 

##### 8 (1)

1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 

##### 9 (1)

1 [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D) 

35 Cards 

##### Common (44)

25 [Mountain](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 1 [Chartooth Cougar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D) 1 [Cosi's Ravager](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D) 2 [Fiery Hellhound](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BHellhound%5D) 2 [Pilgrim's Eye](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D) 2 [Plated Geopede](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D) 1 [Pygmy Pyrosaur](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPygmy%5D+%5BPyrosaur%5D) 1 [Vulshok Berserker](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D) 1 [Vulshok Sorcerer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D) 1 [Armillary Sphere](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D) 1 [Downhill Charge](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D) 1 [Searing Blaze](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D) 2 [Seismic Strike](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D) 1 [Spire Barrage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D) 2 [Wayfarer's Bauble](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D) 

##### Uncommon (10)

1 [Æther Membrane](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D) 1 [Anger](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D) 1 [Bloodfire Kavu](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D) 1 [Earth Servant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D) 1 [Geyser Glider](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D) 1 [Greater Stone Spirit](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BStone%5D+%5BSpirit%5D) 1 [Stone Giant](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStone%5D+%5BGiant%5D) 1 [Jaws of Stone](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D) 1 [Vulshok Battlegear](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D) 1 [Vulshok Morningstar](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D) 

##### Rare (5)

1 [Bloodfire Colossus](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D) 1 [Lithophage](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D) 1 [Torchling](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D) 1 [Journeyer's Kite](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D) 1 [Volley of Boulders](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D) 

##### Mythic (1)

1 [Koth of the Hammer](https://web.archive.org/web/20120326000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D) 

60 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

[Deal Another Hand](https://web.archive.org/web/20120326000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Armillary+Sphere)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pygmy+Pyrosaur)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fiery+Hellhound)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bloodfire+Kavu)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Earth+Servant)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Geyser+Glider)

a:31:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"25";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Æther Membrane";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Anger";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Bloodfire Colossus";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Bloodfire Kavu";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Chartooth Cougar";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Cosi's Ravager";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Earth Servant";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Fiery Hellhound";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Geyser Glider";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:20:"Greater Stone Spirit";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Lithophage";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Pilgrim's Eye";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Plated Geopede";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Pygmy Pyrosaur";s:22:"field\_card\_image\_front";a:0:{}}}i:15;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Stone Giant";s:22:"field\_card\_image\_front";a:0:{}}}i:16;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Torchling";s:22:"field\_card\_image\_front";a:0:{}}}i:17;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Vulshok Berserker";s:22:"field\_card\_image\_front";a:0:{}}}i:18;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Vulshok Sorcerer";s:22:"field\_card\_image\_front";a:0:{}}}i:19;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Armillary Sphere";s:22:"field\_card\_image\_front";a:0:{}}}i:20;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Downhill Charge";s:22:"field\_card\_image\_front";a:0:{}}}i:21;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Jaws of Stone";s:22:"field\_card\_image\_front";a:0:{}}}i:22;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Journeyer's Kite";s:22:"field\_card\_image\_front";a:0:{}}}i:23;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Searing Blaze";s:22:"field\_card\_image\_front";a:0:{}}}i:24;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Seismic Strike";s:22:"field\_card\_image\_front";a:0:{}}}i:25;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Spire Barrage";s:22:"field\_card\_image\_front";a:0:{}}}i:26;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Volley of Boulders";s:22:"field\_card\_image\_front";a:0:{}}}i:27;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Vulshok Battlegear";s:22:"field\_card\_image\_front";a:0:{}}}i:28;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Vulshok Morningstar";s:22:"field\_card\_image\_front";a:0:{}}}i:29;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Wayfarer's Bauble";s:22:"field\_card\_image\_front";a:0:{}}}i:30;O:8:"stdClass":3:{s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Koth of the Hammer";s:22:"field\_card\_image\_front";a:0:{}}}} 

  

### All Duel Respect

My mission complete, I could now head back to Antarctica, Mayan treasure map in hand. This was one of the most fun projects I've ever worked on, and I hope (and believe) that fun is imbued within the product. It's a blast to play, and I can't wait until you all get to experience it for yourselves.

Enjoy!

Mark

![](https://i.ormos.uk/6a/6d/6a6d1187ecbb7b0fb02b31c90d9ec42d21f374071108abde45885da1be5753f7.jpg)
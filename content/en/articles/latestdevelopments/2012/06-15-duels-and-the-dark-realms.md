---
id: 68egd0eh
kind: article
lang: en
path: /en/articles/latestdevelopments/2012/06-15-duels-and-the-dark-realms
title: Duels and the Dark Realms
published: '2012-06-15'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: zac-hill-263da3f4
  name: Zac Hill
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
    lang_detected: en
    capture_id: 721238
    url: https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
    captured_at: '2022-06-28 21:03:31+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
    lang_detected: en
    capture_id: 721238
    url: https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
    captured_at: '2022-06-28 21:03:31+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
    lang_detected: en
    capture_id: 721238
    url: https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
    captured_at: '2022-06-28 21:03:31+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
    lang_detected: en
    capture_id: 721238
    url: https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
    captured_at: '2022-06-28 21:03:31+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - q6wmqh26
  - wr9y1bxw
sources:
- document_id: 68egd0eh
  url: https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
  page_key: magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
  lang: en
  template: drupal
  captured_at: '2022-06-28 21:03:31+00'
  capture_id: 721238
  wayback_url: https://web.archive.org/web/20220628210331id_/https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
- document_id: q6wmqh26
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/199
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/199
  lang: en
  template: aspx
  captured_at: '2014-01-07 10:35:18+00'
  capture_id: 618522
  wayback_url: https://web.archive.org/web/20140107103518id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/199
- document_id: wr9y1bxw
  url: https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-15
  page_key: magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-15
  lang: en
  template: drupal
  captured_at: '2022-10-06 17:19:44+00'
  capture_id: 721242
  wayback_url: https://web.archive.org/web/20221006171944id_/https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-15
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 68egd0eh
  capture_id: 721238
  url: https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
  wayback_url: https://web.archive.org/web/20220628210331id_/https://magic.wizards.com/en/articles/archive/latest-developments/duels-and-dark-realms-2012-06-12
  captured_at: '2022-06-28 21:03:31+00'
  template: drupal
  sha256: a6122730503121bbdb15b8beb8f7320b3331eb96355591fc36919d4503e9d6fc
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 1
---
What it is, y'all.

  

This article is something of a two-parter for a two-parter. Today, I want to talk about (a) the **Magic** card Liliana of the Dark Realms and (b) the Liliana deck for **Duels of the Planeswalkers 2013**. Next week, I want to talk more broadly about **Duels of the Planeswalkers 2013**, **Duels** in general, and how we develop both **Duels** and the sets (like ***Magic** 2013—*my first lead!) that tie in with it.

That's a lot of chatter.

First, though, I should probably talk about what on Earth **Duels of the Planeswalkers** is in the first place.

Get Over Here and Play a Video Game

![](https://i.ormos.uk/77/7c/777ca579f5e413118cb625228bafa8837b33f7b1990b7a4f0cb13b5c3770032b.jpg)

**Duels of the Planeswalkers** is a collaborative effort between Wizards of the Coast and the awesome folks at Stainless Games. It's basically our attempt at creating a kind of "arcade game" experience using **Magic** cards and decks. What does that mean? It's streamlined, fast-paced, sleek, and intuitive, and is easy to play in five-minute or five-hour bursts. You don't just have to take my word for it, though. The **Duels** series has been a perennial Top-10 product on XBox live, and *PCGamer* magazine recently declared it to be one of the "Top 100 Games of All Time" and ranked it #4 on its "15 best games for your laptop" list.

If I sound kind of gushy, that's 'cause I am. In general I don't play all that much "e-**Magic**"—one too many misclick rage-quits for this guy—but I've played through every second of **Duels**. I was on both Challenges and deck design teams for **Duels2010** and **Duels2012** and spent a lot of time working to integrate ***Magic** 2013* with **Duels2013** as a cohesive experience. So I more or less love this product, is what I am trying to say.

Anyway. The deal is it's sort of like a fighting game with **Magic** cards. You play through a campaign ladder battling your deck against a bunch of rival opponents, unlocking cards along the way. There are some mini-games and side quests you can opt into and eventually you can tackle massive boss fights and an über-difficult Revenge Mode.

![](https://i.ormos.uk/a1/60/a160b2f494dc604d24c86dbcd17d3e070ff17b54f5c3ad37f62cf3bc8a9f89c4.jpg)

*Screenshot of Duels of the Planeswalkers 2013 for Xbox 360*

This is just the PvE (player vs. environment) experience, of course. **Duels** also features robust PvP (player vs. player) game play, if you're into that sort of thing. You've got your standard one-on-one battle, naturally, where you can play and customize any of the decks from the ladder (now boasting an unprecedented number of unlocks) against your friends. But because multiplayer is, well, multiplayer, you can also loop your friends into Two-Headed Giant and Planechase, featuring all-new plane cards from *Planechase* (2012 Edition).

I am sure someone on a marketing team somewhere has put together a far more robust explanation, which you can check out [here](https://web.archive.org/web/20120615000000/http://archive.wizards.com/Magic/Digital/DuelsOfThePlaneswalkers.aspx) if you're into that sort of thing. It probably has sleek graphics and slick trailers and polished advertising copy. I'm just a dude who writes stuff and makes games. What I can tell you is that it's just an absolute steal. Forty hours of game play is a *really* conservative estimate, and you're not just grinding quests for gold to buy a hammer that entire time. You're playing **Magic**, the best game in the world.

A Villainess

So what does all this have to do with Liliana?

***Magic** 2013* features five Planeswalkers and five "generals," legendary creatures whose abilities lend themselves to certain themes. All of them get their own decks in **Duels2013**, making for ten playable decks at release. The idea is that the **Duels** decklists should reflect the abilities of each "general" and each Planeswalker card, tying the two together in a visceral, coherent way.

What that means is that even though the Planeswalker decks don't actually contain their respective Planeswalker cards—**Duels** unfortunately doesn't support this functionality yet—the cards should feel organically like they'd make perfect sense in their respective decks.

Okay. So this deck is something like a natural extension of Liliana—her *essential expression* in sixty-card form.

Let's take a look at Liliana, then.

![](https://i.ormos.uk/87/d6/87d619a5e606b1208bda2825ca0714d54a139af55bfa82a0c7b3258bfc9e89b8.jpg)  

When I [previewed my last Planeswalker](https://web.archive.org/web/20120615000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/190), [Tibalt, the Fiend-Blooded](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tibalt%2C+the+Fiend-Blooded), I took it piecemeal. For Liliana, I want to be a bit more big-picture:

Girl likes herself some [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s.

![](https://i.ormos.uk/77/b6/77b6daa73fa1b0bca1b8dfb6e19c66549269b57f16a99888d00298f023515f5f.jpg)

Liliana of the Dark Realms | Art by [D. Alexander Gregory](https://web.archive.org/web/20120615000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22D.+Alexander+Gregory%22%5D)

The ability to +1 and be up a card isn't shabby. In fact, the last time we saw that was on [Tezzeret, Agent of Bolas](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tezzeret%2C+Agent+of+Bolas)—and with him, you missed sometimes. Before that, the last four-mana 'walker who netted you a card was [*Jace*](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+the+Mind+Sculptor).

Now, I'm not saying Land Granting for a [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) is Jace-level, because it's obviously not. What I will say is that if you are sitting there drawing an extra card every turn while fueling your big spells, it's going to be pretty hard to lose the game.

Your opponents, of course, aren't likely to twiddle their thumbs doing nothing while you gradually accumulate advantage. Fortunately, like Vanilla Ice, Lily here is perfectly willing to solve your problems. For the low, low cost of 3 loyalty, Ms. Vess is capable of killing almost any creature on the table. Don't get me wrong—if you want to do it immediately, she's not going to stick around real long. We can't all be winners all of the time. But if you can cast her into an empty board, maybe [using](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismember)[cards](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Go+for+the+Throat)[like](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Sun%27s+Zenith)[these](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade), she can take time out of her busy day to blunderbuss your opponents' biggest threats.

![](https://i.ormos.uk/04/4d/044dc23db78de36ca53ce5ed366dea712f01b998f70b57015ac498fdeb42880b.jpg)

[Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) | Art by [Mike Bierek](https://web.archive.org/web/20120615000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Mike+Bierek%22%5D)

That's not even the whole story, though. At some point, you need to get around to actually ending the game. I know, I know, that's the boring part. But after you've fetched out a [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) or four and need to start doming your opponent 8 points at a time, Liliana here is ready and willing to help you out. And if that damage is Infect damage? So much the better!

But there are times when you need mana, and there are times when you need *mana*.

Sure, a few [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s will get you ahead. But what if you're not looking to cast, say, [Grave Titan](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grave+Titan)s. What if your plans aim a little... higher? [Eldrazi-level](https://web.archive.org/web/20120615000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;subtype=+%5b%22Eldrazi%22%5d) higher. [Drain-Life-For-20+](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drain+Life) higher. Yet-To-Be-Spoiled-Totally-Bananas-Expensive-Spell higher? Look, Liliana bargained with some demons, okay! She's got herself some *power*, and I don't mean power like low-level county clerks have power. I mean El Presidente, You-Can-Have-Whatever-You-Like style Go-Big-Or-Go-Home *power*. Every [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) taps for four? Lake of the Dead, no drawback? Break out the dice—you're going to need them.

Oh, and savvy readers will note that she doesn't just get *basic*[Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s.

Though I'm not sure how that could ever matter, really. There aren't any other kinds of [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp) legal in Standard, and I can't see Snow coming back any time soon (it's currently pretty warm up here in lovely Renton, WA, and we're not exactly hankering to give ourselves the chills).

I'm just pointing that out for completeness' sake. Due diligence. Do it right or don't do it at all, etc., etc. I would be remiss if I didn't.

Paint It Black

So Liliana's deck, and her cards, should care a lot about [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s: getting them into play, using them effectively, and clearing out anything that might try to trump those plans.

Interesting, that.

Here's the list. I have no idea how many of these cards have been spoiled yet. So... if you know it, awesome! If you don't know it... speculate!

#### 139310 Zombie

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (10)

2 [Liliana's Specter](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BSpecter%5D) 2 [Warpath Ghoul](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWarpath%5D+%5BGhoul%5D) 2 [Blister Beetle](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlister%5D+%5BBeetle%5D) 2 [Fume Spitter](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFume%5D+%5BSpitter%5D) 1 [Rune-Scarred Demon](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRune-Scarred%5D+%5BDemon%5D) 1 [Vampire Nighthawk](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BNighthawk%5D) 

##### Sorcery (6)

2 [Sign in Blood](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSign%5D+%5Bin%5D+%5BBlood%5D) 1 [Corrupt](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D) 1 [Rise from the Grave](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRise%5D+%5Bfrom%5D+%5Bthe%5D+%5BGrave%5D) 1 [Mire's Toll](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMire%5D+%5BToll%5D) 1 [Innocent Blood](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D) 

##### Instant (2)

1 [Tendrils of Corruption](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D) 1 [Last Kiss](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLast%5D+%5BKiss%5D) 

##### Artifact (2)

2 [Jet Medallion](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJet%5D+%5BMedallion%5D) 

##### Enchantment (1)

1 [Underworld Dreams](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderworld%5D+%5BDreams%5D) 

##### Land (25)

25 [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 

46 Cards 

##### Black (19)

2 [Liliana's Specter](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BSpecter%5D) 2 [Warpath Ghoul](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWarpath%5D+%5BGhoul%5D) 2 [Blister Beetle](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlister%5D+%5BBeetle%5D) 2 [Fume Spitter](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFume%5D+%5BSpitter%5D) 1 [Rune-Scarred Demon](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRune-Scarred%5D+%5BDemon%5D) 1 [Vampire Nighthawk](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BNighthawk%5D) 1 [Tendrils of Corruption](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D) 1 [Underworld Dreams](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderworld%5D+%5BDreams%5D) 2 [Sign in Blood](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSign%5D+%5Bin%5D+%5BBlood%5D) 1 [Corrupt](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D) 1 [Last Kiss](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLast%5D+%5BKiss%5D) 1 [Rise from the Grave](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRise%5D+%5Bfrom%5D+%5Bthe%5D+%5BGrave%5D) 1 [Mire's Toll](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMire%5D+%5BToll%5D) 1 [Innocent Blood](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D) 

##### Colorless (27)

25 [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Jet Medallion](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJet%5D+%5BMedallion%5D) 

46 Cards 

##### 1 (4)

2 [Fume Spitter](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFume%5D+%5BSpitter%5D) 1 [Mire's Toll](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMire%5D+%5BToll%5D) 1 [Innocent Blood](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D) 

##### 2 (6)

2 [Blister Beetle](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlister%5D+%5BBeetle%5D) 2 [Sign in Blood](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSign%5D+%5Bin%5D+%5BBlood%5D) 2 [Jet Medallion](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJet%5D+%5BMedallion%5D) 

##### 3 (7)

2 [Liliana's Specter](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BSpecter%5D) 2 [Warpath Ghoul](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWarpath%5D+%5BGhoul%5D) 1 [Vampire Nighthawk](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BNighthawk%5D) 1 [Underworld Dreams](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderworld%5D+%5BDreams%5D) 1 [Last Kiss](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLast%5D+%5BKiss%5D) 

##### 4 (1)

1 [Tendrils of Corruption](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D) 

##### 5 (1)

1 [Rise from the Grave](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRise%5D+%5Bfrom%5D+%5Bthe%5D+%5BGrave%5D) 

##### 6 (1)

1 [Corrupt](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D) 

##### 7 (1)

1 [Rune-Scarred Demon](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRune-Scarred%5D+%5BDemon%5D) 

21 Cards 

##### Common (37)

25 [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D) 2 [Liliana's Specter](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLiliana%5D+%5BSpecter%5D) 2 [Warpath Ghoul](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWarpath%5D+%5BGhoul%5D) 2 [Blister Beetle](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlister%5D+%5BBeetle%5D) 2 [Fume Spitter](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFume%5D+%5BSpitter%5D) 1 [Tendrils of Corruption](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D) 1 [Last Kiss](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLast%5D+%5BKiss%5D) 1 [Mire's Toll](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMire%5D+%5BToll%5D) 1 [Innocent Blood](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D) 

##### Uncommon (4)

1 [Vampire Nighthawk](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampire%5D+%5BNighthawk%5D) 1 [Underworld Dreams](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUnderworld%5D+%5BDreams%5D) 1 [Corrupt](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D) 1 [Rise from the Grave](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRise%5D+%5Bfrom%5D+%5Bthe%5D+%5BGrave%5D) 

##### Rare (5)

1 [Rune-Scarred Demon](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRune-Scarred%5D+%5BDemon%5D) 2 [Sign in Blood](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSign%5D+%5Bin%5D+%5BBlood%5D) 2 [Jet Medallion](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJet%5D+%5BMedallion%5D) 

46 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)

[Deal Another Hand](https://web.archive.org/web/20120615000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vampire+Nighthawk)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)

a:16:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:5:"Swamp";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"25";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Liliana's Specter";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Warpath Ghoul";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Blister Beetle";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Fume Spitter";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Rune-Scarred Demon";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Vampire Nighthawk";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:22:"Tendrils of Corruption";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Underworld Dreams";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Sign in Blood";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"2";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:7:"Corrupt";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Last Kiss";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"1";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Rise from the Grave";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Jet Medallion";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"2";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Mire's Toll";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Innocent Blood";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"1";}} 

  

Some of those numbers look off? See any glaring omissions? Well, that's because what I *haven't* spoiled are the *thirty* unlocks you can earn over the course of playing games. So it's fair to say the deck can get quite a bit more powerful. I'm looking at a few different Demons, six or seven ways to kill things dead, and a *really* sweet piece of [rk post](https://web.archive.org/web/20120615000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5b%22rk+post%22%5d) artwork, just to name a few. But I'm not one to give away *all* my secrets, so as to exactly what all those unlocks are? I s'pose you'll have to find out...

Anyway, this is a mana-hungry, power-hungry, classically inclined mono-black midrange deck. The plan is simple: get about a billion [Swamp](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)s in play and tap out to cast spells until your opponent dies. You've got a lot of ways to kill stuff, a fair amount of direct damage, some Fatty Boom Boom monsters, and some solid recursive card advantage. Were Lily herself a part of Duels, she'd fit right in (give my [Vampire Nighthawk](https://web.archive.org/web/20120615000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampire+Nighthawk) +7/+7...).

As just a heads-up, you can expect something similar from the other Planeswalker decks in **Duels2013**. I'm going to talk more next week about how we go about designing these decks, but the idea is to create a fun, diverse play experience that captures the feel of **Magic**'s characters and color pie. The power level should be around that of an Intro Pack. We're not putting Delver and Wolf Run Ramp in here, because that's not the point. But we do want to capture the strategic definition that's a huge part of what makes **Magic** fun.

As to how we did that for **Duels2013** specifically?

Well, stay tuned for next week. :)

Zac ([@zdch](https://twitter.com/#!/zdch))

* * *

  

![](https://i.ormos.uk/d1/0e/d10ed9864085fe8c7a490a03738bb22ec464663708d1e5368fdc74be705e9755.jpg)[![](https://i.ormos.uk/d0/4f/d04f04e451637360d8afc1d5bcebbb90a71e40d5c78b31a3098a4cdbf65afab6.png)](http://store.steampowered.com/app/97330)
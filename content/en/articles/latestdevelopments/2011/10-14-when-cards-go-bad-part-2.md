---
id: 1cyb8eek
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/10-14-when-cards-go-bad-part-2
title: When Cards Go Bad, Part 2
published: '2011-10-14'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
    lang_detected: en
    capture_id: 736005
    url: https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
    captured_at: '2022-09-17 19:01:02+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
    lang_detected: en
    capture_id: 736005
    url: https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
    captured_at: '2022-09-17 19:01:02+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
    lang_detected: en
    capture_id: 736005
    url: https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
    captured_at: '2022-09-17 19:01:02+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
    lang_detected: en
    capture_id: 736005
    url: https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
    captured_at: '2022-09-17 19:01:02+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - 3f4g1wkn
  - t07gvq8g
sources:
- document_id: 1cyb8eek
  url: https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
  page_key: magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
  lang: en
  template: drupal
  captured_at: '2022-09-17 19:01:02+00'
  capture_id: 736005
  wayback_url: https://web.archive.org/web/20220917190102id_/https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
- document_id: 3f4g1wkn
  url: https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-14
  lang: en
  template: drupal
  captured_at: '2020-08-05 19:55:20+00'
  capture_id: 736016
  wayback_url: https://web.archive.org/web/20200805195520id_/https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-14
- document_id: t07gvq8g
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/164
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/164
  lang: en
  template: aspx
  captured_at: '2013-07-06 05:38:17+00'
  capture_id: 613935
  wayback_url: https://web.archive.org/web/20130706053817id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/164
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 1cyb8eek
  capture_id: 736005
  url: https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
  wayback_url: https://web.archive.org/web/20220917190102id_/https://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-12
  captured_at: '2022-09-17 19:01:02+00'
  template: drupal
  sha256: bb345dc4d045b45b37ebf3084316b878d1f976bafa36f412847ddd675bb5ca3e
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
A long time ago, Mark Rosewater wrote a column titled [When Cards Go Bad](https://web.archive.org/web/20111014000000/https://magic.wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr5) about why "bad cards" exist. While I agree with many of the things he said, he approached the problem from a design perspective.

I've been itching to write my own version of his article for a few months. Here are some reasons that developers make cards "bad."

Some cards aren't fun when they're good.

Consider the card [Scrambleverse](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scrambleverse)](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse)

  

Have you ever been part of a game in which this card resolved? What happened?

In a two-player game, you probably flipped a lot of coins, and then whatever board state existed before the card was cast was completely ruined. In a multiplayer game, you probably had to use dice, and there were likely a lot more permanents changing hands. In my experience, this card is a novelty the first time, but its welcome wears out quickly, as the act of resolving it is complicated and it invalidates all the work everyone put into the game before it resolved.

You might, then, be wondering why the card exists at all.

![](https://i.ormos.uk/26/01/2601c183322cd0cd0c44cb364531cad4ada0501c8a0ff935edf4148af1752dd8.jpg)  

Let me tell you about Nick Fang. Nick is a **Magic** judge who often serves as the scorekeeper at Pro Tours. Some of Nick's favorite cards are red chaos-inducing cards in the vein of [Confusion in the Ranks](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confusion+in+the+Ranks), [Wild Evocation](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Evocation), and [Warp World](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warp+World). Whenever I go to Pro Tours, Nick reminds me how much he likes those cards, and that we don't normally make very many of them. Nick's friendly reminders were on my mind while I was working on ***Magic** 2012*, especially because *Scars of Mirrodin* block didn't have any big and random red cards to speak of. I made [Scrambleverse](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse) to fill that need.

![](https://i.ormos.uk/8e/0c/8e0cc1d4e81d6ad0370cb35e9779eda7cc395e6fd51ad464e9b299cb8d5387de.jpg)  

While on the surface I made [Scrambleverse](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse) for Nick Fang, that's not what's actually going on here. Nick is not the only **Magic** player out there who likes big and random effects, as the Gatherer [rate-and-discuss page](https://web.archive.org/web/20111014000000/http://gatherer.wizards.com/Pages/Card/Discussion.aspx?multiverseid=220300) for [Scrambleverse](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse) demonstrates. We need to make cards to serve that audience every once in a while. However, a world in which a deck with four [Scrambleverse](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse)s wins a Pro Tour would be a terrible one indeed, as most players don't enjoy doing that sort of thing more than once every very long time. In order to give [Scrambleverse](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse) to the people who need it but keep it from annoying people who want to avoid it, we just make the card cost so much mana that only the people who really want to play with it will bother to.

![](https://i.ormos.uk/13/0f/130fd958e1d28a91514a382d5159a27c9947cb8c21ea0351082eadb740fd7568.jpg)  

Random red effects are not the only cards that we do this with. Cards like [Painful Quandary](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Painful+Quandary) that enable griefing and cards like [Shared Fate](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shared+Fate) that take an otherwise perfectly normal game and make it weirder both have their audiences, but can annoy the majority of **Magic** players if they become powerful. Our job is to make **Magic** the most fun for everyone, and we've found that we reach the best balance when cards like [Scrambleverse](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse), [Painful Quandary](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Painful+Quandary), and [Shared Fate](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shared+Fate) exist, but have a low enough power level that most players don't want to play with them.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Painful+Quandary"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Painful+Quandary"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shared+Fate"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Shared+Fate"></a></div></div></td></tr></tbody></table>

Limited needs to be balanced.

Most **Magic** players experience **Magic** on a card-by-card basis. While we understand that and do our best to make sure that cards make sense individually, **Magic** developers need to think about the larger picture. Limited is important to **Magic**; lots of people have their first interactions with a **Magic** set at a Sealed Deck event at a Prerelease, and as long as **Magic Online** is up, there will be people drafting twenty-four hours a day. All that Limited play needs to remain fun over time, and to achieve that, we would like the power levels of each color in each format to be balanced.

![](https://i.ormos.uk/68/77/687751b8ac82a8ca8e4c0055c297e94af04b51c825e62d25f0159a9b71ae32be.jpg)  

This often leads to some conversations in meetings that would look strange to outsiders. We had several of these during *New Phyrexia* development. In particular, there was a meeting when both blue and black were doing much better than we wanted in our playtests. Lead developer Aaron Forsythe decreed that we needed a weak blue card and a weak black card. None of us came up with a blue card that was weak enough, so Aaron created [Defensive Stance](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Defensive+Stance) to fill the hole. While I have seen [Defensive Stance](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Defensive+Stance) sideboarded in against [Plague Stinger](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Stinger)s and [Blighted Agent](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blighted+Agent)s, it is hardly a Limited all-star. That same meeting also resulted in [Evil Presence](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evil+Presence) entering the set. While [Evil Presence](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evil+Presence) was important in *Masters Edition III* for dealing with certain legendary lands, in *New Phyrexia* it is merely a weak black card with a flavorful name that we put in to balance the colors.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Defensive+Stance"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Defensive+Stance"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evil+Presence"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Evil+Presence"></a></div></div></td></tr></tbody></table>

I wouldn't be surprised if you drafted full *Scars of Mirrodin* block several times without having played either [Evil Presence](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evil+Presence) or [Defensive Stance](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Defensive+Stance), but I guarantee that those cards being the right power level for the set contributed to the fun you had.

Draft needs to be human-processable.

From a game design perspective, the most potentially confusion-inducing point in a booster draft is the moment you open your first pack. At that moment, you're looking at a fresh collection of fourteen or fifteen cards, and you don't have anything in your pile already to guide you. We include cards of varying power levels in the pack so that this moment is a little bit easier to deal with.

![](https://i.ormos.uk/4c/f6/4cf6fb999c732cbf9df42cc111a09152a1740c35d27547bf9ec8e249fb1d3a4e.jpg)  

Oddly, this is the opposite of many people's instincts about what makes for good Limited game play. Why, they ask, isn't every card almost equally playable? Wouldn't that be more balanced?

It might be a little bit more balanced, but that balance would come with significant costs. I have more experience than most playing Limited with flat power curves. Before I came to Wizards, I spent lots of time playing Cube Draft, a format very similar to Booster Draft in which the booster packs are replaced with a different set of cards preselected by the host. Usually, the selection of cards doesn't include any "bad cards," because who wants to play with those? Because of how often I used to draft Cubes, my Cube card evaluation skills are pretty sharp. However, due to the absence of the bad cards, the card power levels are much closer together than they are in a normal draft.

To illustrate this, here is a pack I just pulled from my Cube.

*   [Necropotence](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence)
*   [Phantom Centaur](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Centaur)
*   [Hero of Oxid Ridge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hero+of+Oxid+Ridge)
*   [Tarmogoyf](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)
*   [Chrome Mox](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chrome+Mox)
*   [Badlands](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Badlands)
*   [Eldrazi Monument](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eldrazi+Monument)
*   [Venser, Shaper Savant](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venser%2C+Shaper+Savant)
*   [Woolly Thoctar](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar)
*   [Pristine Angel](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pristine+Angel)
*   [Recurring Nightmare](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare)
*   [Counterspell](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell)
*   [Geist of Saint Traft](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft)
*   [Whipcorder](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whipcorder)
*   [Slagstorm](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slagstorm)

When most drafters I know open their first pack, the first thing they do is narrow down to a few cards they might be willing to first pick. On your first pass, how many of these cards seem first-pickable to you?

I narrowed it down to just [Chrome Mox](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chrome+Mox), [Necropotence](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence), and [Recurring Nightmare](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare). [Necropotence](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) and [Recurring Nightmare](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare) are both powerful build-around cards, and I think both are reasonable to pick first; I'd take the [Chrome Mox](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chrome+Mox) because it doesn't commit me to anything and I value mana acceleration highly.

![](https://i.ormos.uk/4b/bf/4bbf47518922bc47182a12219115b104203110749c1822fa28495c714250eb7e.jpg)  

Now, a second question. Which of these fifteen cards occurred to you as "bad cards" in context, if any? My "bad cards" in this pack are [Slagstorm](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slagstorm), [Whipcorder](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whipcorder), [Pristine Angel](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pristine+Angel), [Phantom Centaur](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Centaur), and [Woolly Thoctar](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar). I've played all of them in Cube decks before, but none of them are powerful enough to draw me into drafting a deck around them. Despite that, all five have been historically proven as reasonable Constructed cards! This is exactly the kind of card evaluation puzzle that bewilders most people during their first few Cube drafts.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slagstorm"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Slagstorm"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Woolly+Thoctar"></a></div></div></td></tr></tbody></table>

Drafting is a complex enough task already without every card being extremely close together in power, so we include plenty of cards of widely differing power levels so that the right answer can be a little bit less ambiguous. This doesn't simplify the task of correctly identifying those power levels—a challenging task in itself!—but it does make deciding between correctly-identified power levels a little bit easier.

As a side note, I was not much of a believer in this idea until early *Zendikar* development. One of the main problems with the *Zendikar* design handoff was how flat the power levels of the cards were. Most cards were very close to one another in power, so the only way you could get an edge was to draft a highly synergistic deck. One of the first things that *Zendikar* lead developer Henry Stern did to the set once he got his hands on it was de-flatten the power curve by adding one common to each color that you would be unambiguously happy to open and first pick. That made a big difference in lowering the stress level of the beginning of a *Zendikar* draft, and I've been a believer ever since.

Some "bad cards" aren't bad.

Finally, we get to my favorite answer. Often, when a card is previewed, people will post comments like "This should cost one less mana" or "needs trample" or some such. Often, those comments will be about cards that are the way they are for reasons previously enumerated in Mark Rosewater's article or this one, but occasionally, those comments are simply off base. The card is just fine and will have its day in the sun eventually. In these cases, there will inevitably be a moment of discovery when the card turns out to be powerful enough anyway.

![](https://i.ormos.uk/1c/24/1c24971cae778cf2f2f9aef81d12ae7ffbac2c0522e272b781d30fee2cd4e9cc.jpg)  

One such moment happened last weekend with the Wolf Run Ramp deck that Brian Sondag used to win the Star City Games Standard Open in Nashville.

#### Brian Sondag's Wolf Run Ramp

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Planeswalker (4)

4 [Garruk, Primal Hunter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BPrimal%5D+%5BHunter%5D) 

##### Creature (15)

3 [Solemn Simulacrum](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSolemn%5D+%5BSimulacrum%5D) 3 [Wurmcoil Engine](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D) 1 [Acidic Slime](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcidic%5D+%5BSlime%5D) 1 [Birds of Paradise](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D) 3 [Primeval Titan](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimeval%5D+%5BTitan%5D) 4 [Viridian Emissary](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BEmissary%5D) 

##### Sorcery (11)

4 [Green Sun's Zenith](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreen%5D+%5BSun%5D+%5BZenith%5D) 4 [Rampant Growth](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRampant%5D+%5BGrowth%5D) 3 [Slagstorm](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D) 

##### Instant (4)

4 [Beast Within](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeast%5D+%5BWithin%5D) 

##### Land (26)

9 [Forest](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 3 [Mountain](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Copperline Gorge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCopperline%5D+%5BGorge%5D) 4 [Inkmoth Nexus](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkmoth%5D+%5BNexus%5D) 2 [Kessig Wolf Run](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKessig%5D+%5BWolf%5D+%5BRun%5D) 4 [Rootbound Crag](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRootbound%5D+%5BCrag%5D) 

60 Cards 

##### Sideboard (15)

1 [Slagstorm](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D) 1 [Ratchet Bomb](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D) 3 [Sword of Feast and Famine](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BFeast%5D+%5Band%5D+%5BFamine%5D) 2 [Tree of Redemption](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BRedemption%5D) 1 [Viridian Corrupter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BCorrupter%5D) 4 [Ancient Grudge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D) 3 [Thrun, the Last Troll](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThrun,%5D+%5Bthe%5D+%5BLast%5D+%5BTroll%5D) 

##### Red (8)

4 [Slagstorm](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D) 4 [Ancient Grudge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D) 

##### Green (31)

1 [Acidic Slime](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcidic%5D+%5BSlime%5D) 1 [Birds of Paradise](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D) 3 [Primeval Titan](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimeval%5D+%5BTitan%5D) 4 [Viridian Emissary](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BEmissary%5D) 4 [Garruk, Primal Hunter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BPrimal%5D+%5BHunter%5D) 4 [Beast Within](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeast%5D+%5BWithin%5D) 4 [Green Sun's Zenith](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreen%5D+%5BSun%5D+%5BZenith%5D) 4 [Rampant Growth](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRampant%5D+%5BGrowth%5D) 2 [Tree of Redemption](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BRedemption%5D) 1 [Viridian Corrupter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BCorrupter%5D) 3 [Thrun, the Last Troll](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThrun,%5D+%5Bthe%5D+%5BLast%5D+%5BTroll%5D) 

##### Colorless (36)

9 [Forest](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 3 [Mountain](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 4 [Copperline Gorge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCopperline%5D+%5BGorge%5D) 4 [Inkmoth Nexus](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkmoth%5D+%5BNexus%5D) 2 [Kessig Wolf Run](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKessig%5D+%5BWolf%5D+%5BRun%5D) 4 [Rootbound Crag](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRootbound%5D+%5BCrag%5D) 3 [Solemn Simulacrum](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSolemn%5D+%5BSimulacrum%5D) 3 [Wurmcoil Engine](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D) 1 [Ratchet Bomb](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D) 3 [Sword of Feast and Famine](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BFeast%5D+%5Band%5D+%5BFamine%5D) 

75 Cards 

##### 1 (5)

1 [Birds of Paradise](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D) 4 [Green Sun's Zenith](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreen%5D+%5BSun%5D+%5BZenith%5D) 

##### 2 (13)

4 [Viridian Emissary](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BEmissary%5D) 4 [Rampant Growth](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRampant%5D+%5BGrowth%5D) 1 [Ratchet Bomb](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D) 4 [Ancient Grudge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D) 

##### 3 (12)

4 [Beast Within](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeast%5D+%5BWithin%5D) 4 [Slagstorm](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D) 3 [Sword of Feast and Famine](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BFeast%5D+%5Band%5D+%5BFamine%5D) 1 [Viridian Corrupter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BCorrupter%5D) 

##### 4 (8)

3 [Solemn Simulacrum](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSolemn%5D+%5BSimulacrum%5D) 2 [Tree of Redemption](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BRedemption%5D) 3 [Thrun, the Last Troll](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThrun,%5D+%5Bthe%5D+%5BLast%5D+%5BTroll%5D) 

##### 5 (5)

1 [Acidic Slime](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcidic%5D+%5BSlime%5D) 4 [Garruk, Primal Hunter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BPrimal%5D+%5BHunter%5D) 

##### 6 (6)

3 [Wurmcoil Engine](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D) 3 [Primeval Titan](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimeval%5D+%5BTitan%5D) 

49 Cards 

##### Common (27)

9 [Forest](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D) 3 [Mountain](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D) 3 [Primeval Titan](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimeval%5D+%5BTitan%5D) 4 [Viridian Emissary](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BEmissary%5D) 4 [Rampant Growth](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRampant%5D+%5BGrowth%5D) 4 [Ancient Grudge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D) 

##### Uncommon (6)

1 [Acidic Slime](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcidic%5D+%5BSlime%5D) 4 [Beast Within](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeast%5D+%5BWithin%5D) 1 [Viridian Corrupter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BCorrupter%5D) 

##### Rare (23)

4 [Inkmoth Nexus](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkmoth%5D+%5BNexus%5D) 2 [Kessig Wolf Run](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKessig%5D+%5BWolf%5D+%5BRun%5D) 4 [Rootbound Crag](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRootbound%5D+%5BCrag%5D) 3 [Solemn Simulacrum](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSolemn%5D+%5BSimulacrum%5D) 1 [Birds of Paradise](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D) 4 [Green Sun's Zenith](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreen%5D+%5BSun%5D+%5BZenith%5D) 4 [Slagstorm](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D) 1 [Ratchet Bomb](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D) 

##### Mythic (19)

4 [Copperline Gorge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCopperline%5D+%5BGorge%5D) 3 [Wurmcoil Engine](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D) 4 [Garruk, Primal Hunter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BPrimal%5D+%5BHunter%5D) 3 [Sword of Feast and Famine](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BFeast%5D+%5Band%5D+%5BFamine%5D) 2 [Tree of Redemption](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BRedemption%5D) 3 [Thrun, the Last Troll](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThrun,%5D+%5Bthe%5D+%5BLast%5D+%5BTroll%5D) 

75 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

[Deal Another Hand](https://web.archive.org/web/20111014000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rampant+Growth)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Garruk%2C+Primal+Hunter)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Viridian+Emissary)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Beast+Within)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rootbound+Crag)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Viridian+Emissary)

a:23:{i:0;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Forest";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";}i:1;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Mountain";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";}i:2;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Copperline Gorge";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:3;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Inkmoth Nexus";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:4;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Kessig Wolf Run";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";}i:5;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Rootbound Crag";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";}i:6;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Solemn Simulacrum";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:7;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Wurmcoil Engine";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:8;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Acidic Slime";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:9;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Birds of Paradise";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"1";}i:10;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Primeval Titan";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";}i:11;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Viridian Emissary";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";}i:12;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Garruk, Primal Hunter";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:12:"planeswalker";s:10:"deck\_count";s:1:"4";}i:13;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Beast Within";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";}i:14;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Green Sun's Zenith";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";}i:15;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Rampant Growth";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";}i:16;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Slagstorm";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"3";}i:17;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Ratchet Bomb";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";i:0;}i:18;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Sword of Feast and Famine";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"artifact";s:10:"deck\_count";i:0;}i:19;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Tree of Redemption";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:20;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Viridian Corrupter";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}i:21;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Ancient Grudge";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:7:"instant";s:10:"deck\_count";i:0;}i:22;O:8:"stdClass":3:{s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:21:"Thrun, the Last Troll";s:22:"field\_card\_image\_front";a:0:{}}s:4:"type";s:8:"creature";s:10:"deck\_count";i:0;}} 

  

I had a lot of people complain to me that [Garruk, Primal Hunter](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%2C+Primal+Hunter) was too weak to play in Constructed when it was previewed. My internal experience suggested that this was not the case once *Innistrad* rotated in, but as always I was open to being wrong. Happily, "big Garruk" is starting to show up. I look forward to seeing more of his work in the future.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Garruk%2C+Primal+Hunter)](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%2C+Primal+Hunter)

  

We try to design **Magic** sets so that cards can surprise you over time. If you could get everything right just by looking at individual cards, that wouldn't be much fun. We can't get it right by doing that either, so we have to do a lot of work to figure things out, but we think it's worth it in the end if we get a rich and changing tapestry to explore instead of a quickly solved static puzzle.

In the end, each individual card has to serve the greater good of **Magic**. Sometimes, that means not being as powerful as other cards. We hope you understand.

Last Week's Poll

<table><tbody><tr><td colspan="3"><b>Which of Magic's Werewolves is your favorite? </b></td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mayor+of+Avabruck">Mayor of Avabruck</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howlpack+Alpha">Howlpack Alpha</a></td><td>240</td><td>25.5%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reckless+Waif">Reckless Waif</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merciless+Predator">Merciless Predator</a></td><td>167</td><td>17.7%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kruin+Outlaw">Kruin Outlaw</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terror+of+Kruin+Pass">Terror of Kruin Pass</a></td><td>145</td><td>15.4%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Instigator+Gang">Instigator Gang</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildblood+Pack">Wildblood Pack</a></td><td>116</td><td>12.3%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Daybreak+Ranger">Daybreak Ranger</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightfall+Predator">Nightfall Predator</a></td><td>85</td><td>9.0%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gatstaf+Shepherd">Gatstaf Shepherd</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gatstaf+Howler">Gatstaf Howler</a></td><td>43</td><td>4.6%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Village+Ironsmith">Village Ironsmith</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironfang">Ironfang</a></td><td>28</td><td>3.0%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hanweir+Watchkeep">Hanweir Watchkeep</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bane+of+Hanweir">Bane of Hanweir</a></td><td>25</td><td>2.7%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulvenwald+Mystics">Ulvenwald Mystics</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulvenwald+Primordials">Ulvenwald Primordials</a></td><td>21</td><td>2.2%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lesser+Werewolf">Lesser Werewolf</a></td><td>20</td><td>2.1%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Villagers+of+Estwald">Villagers of Estwald</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howlpack+of+Estwald">Howlpack of Estwald</a></td><td>16</td><td>1.7%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Werewolf">Greater Werewolf</a></td><td>13</td><td>1.4%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tormented+Pariah">Tormented Pariah</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampaging+Werewolf">Rampaging Werewolf</a></td><td>9</td><td>1.0%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treacherous+Werewolf">Treacherous Werewolf</a></td><td>7</td><td>0.7%</td></tr><tr><td><a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzled+Outcasts">Grizzled Outcasts</a> / <a href="https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krallenhorde+Wantons">Krallenhorde Wantons</a></td><td>7</td><td>0.7%</td></tr><tr><td><b>Total</b></td><td><b>942</b></td><td><b>100.0%</b></td></tr></tbody></table>

  

This Week's Poll

**What would you first-pick out of the cube pack from the article?**[Necropotence](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence)[Phantom Centaur](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Centaur)[Hero of Oxid Ridge](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hero+of+Oxid+Ridge)[Tarmogoyf](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)[Chrome Mox](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chrome+Mox)[Badlands](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Badlands)[Eldrazi Monument](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eldrazi+Monument)[Venser, Shaper Savant](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venser%2C+Shaper+Savant)[Woolly Thoctar](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar)[Pristine Angel](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pristine+Angel)[Recurring Nightmare](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare)[Counterspell](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell)[Geist of Saint Traft](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft)[Whipcorder](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whipcorder)[Slagstorm](https://web.archive.org/web/20111014000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slagstorm)

  

* * *

  

![](https://i.ormos.uk/de/61/de610ee6bd6662eadd1ef84855886025655c4666aa92fa8c19549a455afab7a0.jpg)![](https://i.ormos.uk/21/0c/210c4f783ebb895a2393c23b6a553dd97ddb4846a029d152cca2e6c75ac13a54.jpg)[![](https://i.ormos.uk/41/3e/413eecb73f09eb7faeb80fd74dc4f80e135ee873e1be1a4eb5ecdd4defaf5643.jpg)](https://web.archive.org/web/20111014000000/http://staging.wizards.com/Magic/Digital/MagicOnline.aspx)
---
id: jx6185q3
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/03-27-fixing-the-environment
title: Fixing the Environment
published: '2009-03-27'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
    lang_detected: en
    capture_id: 722535
    url: https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
    captured_at: '2022-08-16 07:32:08+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
    lang_detected: en
    capture_id: 722535
    url: https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
    captured_at: '2022-08-16 07:32:08+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
    lang_detected: en
    capture_id: 722535
    url: https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
    captured_at: '2022-08-16 07:32:08+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
    lang_detected: en
    capture_id: 722535
    url: https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
    captured_at: '2022-08-16 07:32:08+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: jx6185q3
  url: https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
  page_key: magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
  lang: en
  template: drupal
  captured_at: '2022-08-16 07:32:08+00'
  capture_id: 722535
  wayback_url: https://web.archive.org/web/20220816073208id_/https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
- document_id: jx6185q3
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/31
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/31
  lang: en
  template: aspx
  captured_at: '2013-07-01 22:56:43+00'
  capture_id: 620870
  wayback_url: https://web.archive.org/web/20130701225643id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/31
- document_id: jx6185q3
  url: https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-26
  lang: en
  template: drupal
  captured_at: '2021-12-02 22:13:49+00'
  capture_id: 722530
  wayback_url: https://web.archive.org/web/20211202221349id_/https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-26
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: jx6185q3
  capture_id: 722535
  url: https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
  wayback_url: https://web.archive.org/web/20220816073208id_/https://magic.wizards.com/en/articles/archive/latest-developments/fixing-environment-2009-03-27
  captured_at: '2022-08-16 07:32:08+00'
  template: drupal
  sha256: cf63c222a6c060f14d8bd8943cbc0abe6e1f9cfc74e45ff78056fac8f9dc6e3e
render_recovery: []
---
Hello everyone, and welcome to the end of Mana Fixing Week. **Magic** developers like mana fixers. We know that it isn't any fun when you can't cast your spells, and mana-fixing cards let you cast spells of various colors much more reliably. On top of being fun, casting cards of many colors more consistently is also powerful, and the most powerful mana fixing cards are often played heavily. Different categories of mana fixing cards being powerful can have subtle but significant effects on environments, and **Magic** developers think about those effects while they build sets. Today I'll talk about the non-obvious effects that various kinds of mana fixing have on **Magic** environments and what we've learned from watching them play out in the real world.

One obvious thing we do to fix mana is to print two-color dual lands, and from set to set they tend to work in very similar ways. We avoid making them strictly better than basic lands to make sure that there are costs to playing multiple colors. One way we do this is making them come into play tapped some of the time, like *Lorwyn*'s tribal lands. Another is to put an extra cost on making each of the two colors the dual land produces, like *Tenth Edition*'s painlands. The last trick we use is to make lands that produce two colors of mana but don't simply tap for one mana of either color, like *Shadowmoor* and *Eventide*'s filter lands.

![](https://i.ormos.uk/ee/b2/eeb21a4efd772721c1bc3a07e155236b8afe2507ed9edd20f07459886600d8d6.jpg)

Different cycles of dual lands have slightly different effects; for example, *Lorwyn*'s dual lands encourage you to play tribal decks and *Shadowmoor* and *Eventide* filter lands make playing colorless lands more costly. However, their overall effect on Constructed **Magic** is very similar from cycle to cycle. They let you play two-color decks fairly effortlessly and let you think about playing three or more colors if you are willing to stretch. Because dual lands tend to work very similarly, they don't radically effect the environments they are in.

Dual lands are by no means the only tools that we give players to help fix their mana, and those other tools often have much more noticeable effects on **Magic** environments. Today I'll talk about three kinds of mana fixers we have printed. I'll cover why each of them is appealing as well as the subtle side effects they have.

### Mana Artifacts

![](https://i.ormos.uk/43/e6/43e64fc3d684c15f30fd2da12af7a76907116d5fdaf2872589a7a8ac6a46d10e.jpg)

On a very basic level, mana acceleration cards are fun because they let you play spells faster than you should be able to. We normally put this effect only in green as part of the mechanical definition of the colors. However, we also print artifacts that make mana, which lets every color get in on the fun. Some of these artifacts produce only colorless mana, and others make one or more colors. The most recent example of powerful mana artifacts are *Ravnica*'s signets. These did a fantastic job of letting players play all the exciting multicolored cards that *Ravnica* had to offer.

Efficient mana artifacts hurt green by taking away one of its strengths and giving it to every color. Part of green's color pie is efficient mana acceleration. Many green mana accelerators are creatures such as [Birds of Paradise](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise), but cards like [Rampant Growth](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampant+Growth), [Fertile Ground](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertile+Ground), and [Kodama's Reach](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kodama%27s+Reach) are still perfect for people who don't want the fragility that comes with mana-accelerating creatures. They also are perfect for decks that use mass removal spells like [Wrath of God](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) to defend themselves while ramping up to big spells. Those decks often go to green to get the mana acceleration they need. However, when there are efficient mana artifacts around, they can get the same ramping effect without having to add a color.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Azorius Signet" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Azorius+Signet"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Gruul Signet" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Gruul+Signet"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

![](https://i.ormos.uk/b6/5f/b65fd60200d0193ff37a531ff2e4baec1c79c8b0431408930e9e0f64c8d91a96.jpg)

This is very crushing for green. Decks that would have played green to get access to mana acceleration that also want other things green has to offer must consider if they would be better off just playing artifacts for mana acceleration instead and doing without the other green cards they wanted. Decks that only wanted green for mana acceleration can ignore green entirely and play artifacts. Decks that are based in green and use green's mana acceleration cards need a very compelling reason to stay green, or they might also be better off moving to other colors where they can get mana accelerators that are nearly as good as green's while having access to other colors' best cards too. Blue decks in particular love it when powerful artifact mana accelerators exist. Mana acceleration and card drawing are two of the most powerful mechanics in **Magic**, and good mana artifacts mean that blue gets access to both of them at the same time!

Another effect of efficient mana artifacts that produce colored mana is that they allow you to play many more colorless lands than you otherwise would be able to. Colorless lands normally hurt you by making it less likely that you can play your colored spells, but a deck that plays a bunch of mana artifacts in addition to lands can just use the artifacts to get the colored mana they need and play tons of interesting colorless lands too. For example, check out this mana base from the Top 8 of [the World Championships in 2006](https://web.archive.org/web/20090327000000/https://magic.wizards.com/en/events/coverage/mihara-dutch-crowned-world-champions).

4 [Urza's Tower](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Tower)  
 4 [Urza's Power Plant](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Power+Plant)  
 4 [Urza's Mine](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Mine)  
 1 [Urza's Factory](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Factory)  
 1 [Academy Ruins](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Academy+Ruins)  
 4 [Hallowed Fountain](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hallowed+Fountain)  
 4 [Adarkar Wastes](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adarkar+Wastes)  
 1 [Island](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)  
 4 [Azorius Signet](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Azorius+Signet)  
 3 [Dimir Signet](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dimir+Signet)

This mana base came from [a blue-white control deck](/en/articles/event-coverage/2006/12-01-decklists-the-top-8-decks). Only nine of its lands make blue mana, but thanks to the whopping seven Signets the deck will not often be lacking for blue mana despite playing fourteen lands that produce only colorless. Without the Signets, there's no way a blue control deck could get away with having over half its lands not produce any color of mana.

### Mana Creatures That Block Well

![](https://i.ormos.uk/20/25/2025a08ac49df4acf8028383eb095f8f15fd191b996b33c20dfdc7ac50a916b5.jpg)

We print lots of creatures that help you make mana. They are mostly green, and range from the humble [Llanowar Elves](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves) to flashy block-specific cards like [Noble Hierarch](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noble+Hierarch). Many of these creatures have tap abilities that make mana, which means that they can't make mana and block on the same turn. Most of these also have low toughness, so if they block early in the game they are in the graveyard and don't keep making you mana. You can always use them to chump-block later on but then they won't have protected you in the early game.

We sometimes print mana-accelerating creatures that can both block and accelerate mana. The most notable of these have been [Wall of Roots](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Roots), [Vine Trellis](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vine+Trellis), and [Sakura-Tribe Elder](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder). [Vine Trellis](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vine+Trellis) can't block if you just used it for mana, but it often doesn't die when it blocks. [Sakura-Tribe Elder](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder) will almost certainly die when it blocks, but it was always going to die eventually when it fetched you a land. [Wall of Roots](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Roots) is in the best of both of these worlds; it survives combat with most cheap creatures and lets you block even immediately after using it to make mana.

![](https://i.ormos.uk/cf/50/cf5099a0b63999c5cd049895792d8bfb572bedc6c18c6f94c2a07143c8da3752.jpg)

These cards do exactly what many midrange green-based decks want. Not only do they accelerate mana so that expensive spells can come down faster, but they also provide some defense against aggressive creature swarms. Without these cards, those decks would have had to include one set of cards to accelerate their mana and another set of cards to defend against early creature beatdown. With them, they get to skimp on early defense and crutch on their mana accelerators instead. Of course, that's also exactly why these cards are so appealing. Playing expensive and splashy spells is fun, and these cards both get you the mana you need to do it and keep you from dying before you get there.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Sylvan Scrying" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Sylvan+Scrying"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Reap and Sow" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Reap+and+Sow"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

Midrange green decks that have access to these cards can go surprisingly low on defensive cards without becoming weak to creature assaults. In the summer of 2005, I spent a lot of time playing a mono-green deck built around the Urza's lands. That deck used [Sylvan Scrying](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sylvan+Scrying) and [Reap and Sow](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reap+and+Sow) to assemble the Urzatron, then used big spells like [Tooth and Nail](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tooth+and+Nail) to put the opponent away. Almost everyone who played that deck used [Sakura-Tribe Elder](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder), and many players also used [Oblivion Stone](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Stone) to have defense against creature swarms. Someone suggested to me that I try adding [Vine Trellis](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vine+Trellis), and when I did I was shocked to find that I no longer needed [Oblivion Stone](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Stone) against creature swarms. My anti-creature package consisted only of four each of [Sakura-Tribe Elder](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder) and [Vine Trellis](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vine+Trellis) and a single [Duplicant](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duplicant), and that usually bought me enough time to cast [Tooth and Nail](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tooth+and+Nail) before dying.

This effect has also played out on a large scale in real-world tournament formats. One example is Kamigawa Block Constructed, which in many ways was dominated by [Sakura-Tribe Elder](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder). The Top 8 of Pro Tour Philadelphia contained seven midrange green decks that each had four Elders, and the qualifier season following it was dominated by green-based [Gifts Ungiven](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven) control decks, which used [Kagemaro, First to Suffer](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kagemaro%2C+First+to+Suffer) and [Sickening Shoal](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickening+Shoal) as their main creature removal. Both of these cards have problems; [Kagemaro, First to Suffer](https://web.archive.org/web/20090327000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Kagemaro%252C%2BFirst%2Bto%2BSuffer) costs six total mana to use, and [Sickening Shoal](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sickening+Shoal) is very expensive if it is not played with the alternate cost. [Sakura-Tribe Elder](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder)'s one-turn Fog effect was key to the Gifts deck's ability to survive early assaults from against mono-white and mono-black creature decks.

### Five-Color Mana

![](https://i.ormos.uk/b9/4c/b94c5b85acfde6b8060f7f5324fe3584345950949607a064972e784d05622816.jpg)

Two of the most fundamental things about how **Magic** works as a game are the mana system and the color pie. The mana system ensures that the player must make a choice of which color to play, and the color pie makes that choice meaningful. Mana fixers that help you play two colors don't undermine that feeling of choice because you still have to pick two of the five colors to play. Five-color mana fixers, however, let you avoid having to make a choice and instead play cards of any color. On the other hand, they are appealing exactly because they let you "break the rules." Playing all five colors feels like getting away with something, which is exciting. It's also fun to have the freedom to play any card you can think of putting in your deck.

![](https://i.ormos.uk/50/bc/50bc49471dc597d8937aa522c797ba02e8f419bce2a5b70627ecc4f846f1877a.jpg)

Devin Low wrote [an article](/en/articles/latestdevelopments/2007/05-25-the-dark-side-of-mana-fixers) about how *Time Spiral* block flirted with five-color mana after the *Time Spiral* Block Constructed [Pro Tour–Yokohama](/en/articles/event-coverage/undated/wafo-tapa-tops-them-all-2). He is absolutely right about how cards like [Terramorphic Expanse](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse) and [Prismatic Lens](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) let players play extra colors for little cost. However, I don't think that it's automatically a bad thing when colors bleed a little bit. I was still in the real world when Time Spiral block was new, and I had a lot of fun playing the multicolor blue control decks that Devin talks about in that article. It's not every day that you get to play [Bogardan Hellkite](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bogardan+Hellkite), [Damnation](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation), [Careful Consideration](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Consideration), and [Gaea's Blessing](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Blessing) in the same deck, and I really enjoyed the change of pace. I also felt that playing five colors had some serious consequences for my deck. Have a look at the mana base that I played in the *Time Spiral* block [Grand Prix–San Francisco](https://web.archive.org/web/20090327000000/https://magic.wizards.com/en/events/coverage/scott-vargas-repeats-golden-state).

4 [Prismatic Lens](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens)  
 4 [Coalition Relic](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coalition+Relic)  
 4 [River of Tears](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears)  
 4 [Tolaria West](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolaria+West)  
 4 [Terramorphic Expanse](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse)  
 3 [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth)  
 2 [Urza's Factory](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Factory)  
 1 [Academy Ruins](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Academy+Ruins)  
 1 [Dreadship Reef](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dreadship+Reef)  
 1 [Molten Slagheap](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Molten+Slagheap)  
 1 [Forest](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest)  
 1 [Mountain](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)  
 1 [Swamp](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swamp)  
 1 [Plains](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains)  
 3 [Island](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)

I don't think that it's automatically a bad thing when a mana base like this can function in a format. I enjoyed playing this deck a lot because it was markedly different from other blue control decks I had played. It also required me to make some serious sacrifices to get access to all five colors of mana. [Prismatic Lens](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) is nowhere near as powerful as the *Ravnica* Signets, and spending my third turn doing nothing but casting [Coalition Relic](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coalition+Relic) was often painful. [Terramorphic Expanse](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse) required that I put one of each basic land other than [Island](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island) in my deck, which introduced inconsistency because sometimes I would draw the [Forest](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest) and [Plains](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) and then have trouble casting [Damnation](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) and [Careful Consideration](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Consideration). Also take note of the fact that my mana base was 35 cards. That meant that I only had 25 other cards in my deck that could do other things. I had the ability to transmute [Tolaria West](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolaria+West) for [Slaughter Pact](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slaughter+Pact) and [Pact of Negation](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pact+of+Negation), but just as often I would search for [Urborg, Tomb of Yawgmoth](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth) and sometimes I would just play it as a land.

![](https://i.ormos.uk/1d/70/1d704df321dbb28b2215fb4cbd5357611cf7d81a2d8fdab0c371a8ac7a343e88.jpg)

All of these factors meant that the decision to play all five colors had some real consequences. I could have cut some of the extra colors and had a more consistent deck, but I chose not to. Amusingly, **Magic** developer Erik Lauer thinks that I made the wrong choice with that deck. His *Time Spiral* block blue decks didn't play [Terramorphic Expanse](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse) and instead had enough [Island](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Island)s to consistently suspend [Ancestral Vision](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Vision) on turn one. He also played [Cancel](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) because he had the ability to consistently cast [Careful Consideration](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Consideration) and still have two more blue mana open, which my list did not. He also played fewer total mana sources than I did because he only needed to support two colors most of the time, so he simply had more spells that did things in his deck. The fact that we could have that discussion and not be sure who is right at the end shows that the choice to seriously extend to five colors or not was interesting in that format.

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Vivid Creek" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Vivid+Creek"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Reflecting Pool" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Reflecting+Pool"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

On the other hand, I think that five-color mana fixing goes wrong when that discussion stops being interesting. Unfortunately, *Lorwyn*'s Vivid lands create a situation similar to that in Standard right now. Thanks to them and [Reflecting Pool](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reflecting+Pool), control decks in Standard can play all five colors very easily. In contrast to *Time Spiral* Block, where playing all five colors seriously impacted your mana base's consistency and made you play more mana sources than you might have otherwise wanted to, modern five-color control decks in standard get all the colors they need from their lands alone. The Vivid lands do come into play tapped, but control decks often don't do many things on their early turns so this is not a huge cost. We regret the Vivid lands because they do not create the same level of consequence for players who want to play all five colors as *Time Spiral* block's mana fixing did.

![](https://i.ormos.uk/2c/71/2c71f2c12d88453357c0962a9023ab72cb01def4c29b7de649b1d7e40b601542.jpg)

Today I discussed three kinds of mana-fixing cards we print and the effects they have on **Magic** environments. All three of the categories I talked about have been popular and are things we like to do. However, you might have read some of the effects I listed and wondered to yourself if they were actually reasons to not print them. For example, one could say that [Sakura-Tribe Elder](https://web.archive.org/web/20090327000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder) was a mistake because it hurt aggressive decks, or that *Ravnica*'s Signets were a mistake because they gave blue decks access to mana acceleration they shouldn't have had. While those cards did have those effects, that doesn't mean that we shouldn't have made them. **Magic** is a great game because it changes over time, and the mana fixers we print each year have different subtle effects. It's our job as developers to recognize exactly what those effects are, be responsible for their impact, and change them over time to keep the game fresh. I hope you enjoyed Mana Fixing Week!

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>How many colors does your favorite Magic deck play?</b></th>&#10;		</tr></thead><tbody><tr><td>0</td>&#10;			<td>99</td>&#10;			<td>1.3%</td>&#10;		</tr><tr><td>1</td>&#10;			<td>1146</td>&#10;			<td>15.1%</td>&#10;		</tr><tr><td>2</td>&#10;			<td>2950</td>&#10;			<td>38.8%</td>&#10;		</tr><tr><td>3</td>&#10;			<td>2173</td>&#10;			<td>28.6%</td>&#10;		</tr><tr><td>4</td>&#10;			<td>301</td>&#10;			<td>4.0%</td>&#10;		</tr><tr><td>5</td>&#10;			<td>925</td>&#10;			<td>12.2%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>7594</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>
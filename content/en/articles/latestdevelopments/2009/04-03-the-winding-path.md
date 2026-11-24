---
id: gbh5ndxd
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/04-03-the-winding-path
title: The Winding Path
published: '2009-04-03'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
    lang_detected: en
    capture_id: 736250
    url: https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
    captured_at: '2022-09-27 16:53:22+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
    lang_detected: en
    capture_id: 736250
    url: https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
    captured_at: '2022-09-27 16:53:22+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
    lang_detected: en
    capture_id: 736250
    url: https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
    captured_at: '2022-09-27 16:53:22+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
    lang_detected: en
    capture_id: 736250
    url: https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
    captured_at: '2022-09-27 16:53:22+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: gbh5ndxd
  url: https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
  page_key: magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
  lang: en
  template: drupal
  captured_at: '2022-09-27 16:53:22+00'
  capture_id: 736250
  wayback_url: https://web.archive.org/web/20220927165322id_/https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
- document_id: gbh5ndxd
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/32
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/32
  lang: en
  template: aspx
  captured_at: '2013-07-02 16:47:04+00'
  capture_id: 620884
  wayback_url: https://web.archive.org/web/20130702164704id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/32
- document_id: gbh5ndxd
  url: https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-02
  page_key: magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-02
  lang: en
  template: drupal
  captured_at: '2021-12-04 04:19:16+00'
  capture_id: 736247
  wayback_url: https://web.archive.org/web/20211204041916id_/https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-02
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: gbh5ndxd
  capture_id: 736250
  url: https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
  wayback_url: https://web.archive.org/web/20220927165322id_/https://magic.wizards.com/en/articles/archive/latest-developments/winding-path-2009-04-03
  captured_at: '2022-09-27 16:53:22+00'
  template: drupal
  sha256: 1983fb1161c4d208d1bc37a6b9e6e83da28f33e35c4053d04a425b7a93959526
render_recovery: []
---
![](https://i.ormos.uk/6e/6f/6e6f17795d0365f41606724c5d5677104f9935de618c3a919f93fca8614af1fa.jpg)

M**agic** developers treat the game of **Magic** with utmost respect. We choose to work on **Magic** rather than do other things because we love the game, and we do everything with its best interests in mind. Sometimes, the path that this takes us down leads to strange places, and we make decisions that we never thought we would when we began to attack a problem. Many of these interesting and odd decisions are hidden from those who do not work on the game, because only we see the winding path that cards, mechanics, and sets take as they make their way from design to print. Today I'll talk about two different choices **Magic** developers have made that both developers and players found strange, and talk about the reasons we made them.

### Thornling

![](https://i.ormos.uk/2c/c5/2cc501dc3d42a998e8b0689ddf45f464da2bc2dc50e5d86f91e96d32c9ccf57a.jpg)

[Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) is a throwback to [Morphling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling), a famously powerful **Magic** card that was referred to as "Superman" for many years. Players who recognized the reference asked me over and over at the Prerelease why [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) does not have the ability to untap itself like [Morphling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) and its *Planar Chaos* homage [Torchling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling) do. This was not a mistake. We knew that it looked strange; in fact, it looked strange to many of us as well. However, we were still willing to put that aside and print the most fun [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) we thought we could make.

Like all human beings, **Magic** designers enjoy completing patterns. [Torchling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling) hinted that [Morphling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling)s of other colors might be running around the Multiverse somewhere, so it wasn't a huge surprise when a green version showed up in a design file. The first version was exactly what many people thought [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) was supposed to be:

> Ultraling  
>  3GG  
>  Creature – Shapeshifter  
>  4/4  
>  G: CARDNAME gains trample until end of turn.  
>  G: CARDNAME is indestructible until end of turn.  
>  G: Untap CARDNAME.  
>  1: CARDNAME gets +1/-1 until end of turn.  
>  1: CARDNAME gets -1/+1 until end of turn.

I started working at Wizards about halfway through *Conflux* development, and Constructed playtesting usually becomes the focus at about that point in the development cycle. Being new meant that I had much to learn about how things were done at Wizards, but I was able to contribute immediately by building lots of Future Future League decks. For whatever reason [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) was one of the cards that appealed to me most as I went through the *Conflux* file, so I started building mana ramp decks that showed it off.

![](https://i.ormos.uk/59/56/5956cd43e8c13aff1a1e4293d0456a0e4b7760b5848786ecc4fc87e34a856d17.jpg)

I quickly realized that not only was [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) fun to read, it was also one of the most potent cards in my decks. I built them to have lots of mana quickly, and with a little mana [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) dominates the board against ground creature decks. Over and over again, I would attack with a [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) and invite my opponent to block it. I usually had enough mana to pump its power high enough to both kill any blocker and make [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) indestructible, so most of the time my opponents didn't block. I would then still have enough mana to both untap it and make it indestructible, which kept my opponent from attacking me back. Although [Morphling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) and [Torchling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling) do have the ability to untap, giving them enough toughness to survive combat with a high-power creature can be quite expensive. [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) requires only that you pay ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) to get the same effect.

<table><tbody><tr><td>&#10;					<div>&#10;						<div><img alt="Morphling" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Morphling"></div>&#10;					</div>&#10;				</td>&#10;				<td>&#10;					<div>&#10;						<div><img alt="Torchling" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Torchling"></div>&#10;					</div>&#10;				</td>&#10;			</tr></tbody></table>

More people began playing [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling)s when they saw how powerful it was against creature swarms in decks that had access to a lot of mana. This led to the realization that [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling)-on-[Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) fights were very annoying thanks to the untap ability. When a [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) blocked a [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling), what usually happened was both [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling)s became indestructible, the attacking [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) gained trample and went to 7/1, and the defending one went to 1/7. The next turn, the [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) that just blocked would attack, the other [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) would untap for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), then the process would repeat. This was very mathy and turned games into mana arms races, and it was even worse when there were multiple [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling)s on each side.

We grew unhappy with the untap ability, so we explored alternatives. Speaking abstractly, the original [Morphling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling)'s three abilities helped it race, gave it evasion, and protected it from harm. Evasion was already covered by trample and protection was covered by indestructible, so we looked for a different ability that could help it win a race. Vigilance was raised as a simple alternative that frontloaded the untapping cost, but that didn't solve the gameplay problems. Haste was the next suggestion, with the logic that it helps [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) race by letting it attack on the first turn.

![Thornling](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thornling)

 

I fell in love with the haste idea. It made the card better against control decks because I could attack immediately with it in the late game, and it made the card worse against creature swarm decks because it couldn't both attack and prevent the opponent from attacking. I also thought that [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) standoffs would be less miserable because the decision to attack with one would be more meaningful. I played it that way for a few days and discovered that not only was that logic correct on all counts, but it was also more fun in intangible ways. There was something viscerally awesome about attacking with it immediately, and I fought for the change until it found way into the file. That ability survived all the way to print despite the double-take many of us did every time we read it in the file.

I can't blame anyone familiar with [Morphling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) and [Torchling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torchling) for thinking that [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) looks strange next to its Shapeshifter brethren. We also found it a little odd, and the decision to take the untap ability away from [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) was contentious. However, I believe we ended up with a more fun **Magic** card because we were willing to let the oddness remain.

![](https://i.ormos.uk/a3/69/a369ceffc56fa0b4a76257d96b7afae58513744eb8c3370c29bdd2ad62c88258.jpg)

As a final note, [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) is my favorite *Conflux* card. I played four of it in the Standard deck that I used to gunsling at the *Conflux* Prerelease I attended, and I had tons of fun attacking for 7 over and over again. I hope that it will get a chance to shine at [Pro Tour–Honolulu](https://web.archive.org/web/20090403000000/https://magic.wizards.com/en/node/640716) or in this summer's Standard format Pro Tour–Austin qualifiers!

### Ponder

![](https://i.ormos.uk/5a/1e/5a1eb777f3a3ef0079e61cced40b194b182eba6ffb445772a2dd2e18b204bca3.jpg)

Vintage is the **Magic** tournament format that gives players the opportunity to play with the widest variety of cards. Only cards that are not legal in any tournament format and those that involve manual dexterity, ante, or subgames are banned. The worst fate that other cards can suffer is being placed on the restricted list, which means that only one copy can be played in a 60-card Vintage deck. We enjoy it when cards like [Tezzeret the Seeker](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tezzeret+the+Seeker) and [Inkwell Leviathan](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkwell+Leviathan) make a splash in Vintage, but we do not go out of our way to make cards for the format because only the most powerful cards in **Magic** thrive there, and it is impossible to compete with cards like the Moxes while keeping a reasonable power level in Standard. We use [the restricted list](https://web.archive.org/web/20090403000000/http://archive.wizards.com/Magic/TCG/Resources.aspx?x=judge/resources/sfrvintage) to keep the format fun while still allowing players to play with the largest variety of cards possible.

<table><tbody><tr><td>&#10;					<div>&#10;						<div><img alt="Tezzeret the Seeker" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Tezzeret+the+Seeker"></div>&#10;					</div>&#10;				</td>&#10;				<td>&#10;					<div>&#10;						<div><img alt="Inkwell Leviathan" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Inkwell+Leviathan"></div>&#10;					</div>&#10;				</td>&#10;			</tr></tbody></table>

Many restricted cards are famously powerful. However, the DCI does not create the restricted list by applying an objective measurement of power across all **Magic** cards and restricting all cards that are above a certain power level. Instead, the DCI uses the restricted list to sculpt an environment that is fun and diverse. **Magic** developers test standard to make sure there are lots of different reasonable decks to play that are enjoyable. We have the same goals for other formats, and we recommend changes to the DCI when we notice that one of them is becoming stagnant.

On June 1, 2008, the DCI announced the restriction of five cards in Vintage: [Flash](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash), [Gush](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush), [Merchant Scroll](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll), [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm), and [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder). The motivation for restricting the first three of those cards was clear at the time to most Vintage players, although not all agreed that it was strictly necessary. Using [Flash](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash) to put a [Protean Hulk](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Protean+Hulk) into play allowed players to immediately win the game if they had the right set of creatures in their library, and decks built to do just that could consistently win the game in the first two turns. Decks built around the [Fastbond](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fastbond)-[Gush](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush) mana engine were also winning tournaments left and right. [Merchant Scroll](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll) was a key piece of the decks built around both [Flash](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash) and [Gush](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush), and it was not a huge surprise when it eventually joined similar cards like [Mystical Tutor](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Tutor) and [Demonic Tutor](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonic+Tutor) on the restricted list.

<table><tbody><tr><td>&#10;					<div>&#10;						<div><img alt="Brainstorm" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Brainstorm"></div>&#10;					</div>&#10;				</td>&#10;				<td>&#10;					<div>&#10;						<div><img alt="Ponder" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Ponder"></div>&#10;					</div>&#10;				</td>&#10;			</tr></tbody></table>

The restrictions of [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) and [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder), however, confused many players. [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm)'s restriction was understandable, although somewhat surprising. A player who casts [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm), puts two useless cards on top of his or her library, and then shuffles his or her library is effectively up three cards, and Vintage has no shortage of cards that let a player shuffle his or her library. [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder)'s restriction was more difficult to explain. Some blue Vintage decks were playing both [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) and [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder), but some only played [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm). It was also difficult to compare [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) in a satisfying way to other previously restricted cards. Because of this, many players were rightfully confused about the DCI's choice to restrict it.

I was not a Wizards employee when I read the announcement of that restriction, and it confused me just as much as it did other **Magic** players. I have since learned the reasoning. I fully acknowledge that it looks strange on paper, but the **Magic** developers had good reasons for their decision. I was pleasantly surprised to learn them.

![](https://i.ormos.uk/82/7b/827b134a9facc8c628dedf254380893082a4ddb6e78edbbf2323dba0a26a4c8a.jpg)

Ever since *Future Sight* was released, the most powerful Vintage decks have revolved around one or more of [Dark Ritual](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual), [Force of Will](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will), [Bazaar of Baghdad](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bazaar+of+Baghdad), and [Mishra's Workshop](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop). These are some of the most powerful unrestricted cards in the format; in fact, some of them are more powerful than cards that are restricted! For example, [Dark Ritual](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual) is stronger than [Lotus Petal](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lotus+Petal), and [Mishra's Workshop](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop) is stronger than [Grim Monolith](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grim+Monolith).

We are happy despite that apparent inconsistency because each of the four cards I listed creates Vintage deck archetypes. [Dark Ritual](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual) fuels decks built around the Storm mechanic. [Force of Will](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) decks usually build around other unrestricted blue cards; [Mana Drain](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain) currently fills that role, but [Gush](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush), [Gifts Ungiven](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gifts+Ungiven), and [Fact or Fiction](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction) all spent time in that slot before their restrictions. [Bazaar of Baghdad](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bazaar+of+Baghdad) decks abuse *Ravnica*'s dredge mechanic to win the game out of the graveyard in the first three turns. [Mishra's Workshop](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop) decks cast artifacts quickly to lock their opponents out of the game. We acknowledge that these cards are overpowered. However, we value the existence of different decks in a Constructed format, and each of those cards fuels an entire archetype.

In early 2008, members of **Magic** R&D were not happy with the direction that tournament Vintage was going. There were two problems that needed to be solved. The first was that [Force of Will](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) decks were much, much stronger than decks built around [Mishra's Workshop](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Workshop), [Bazaar of Baghdad](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bazaar+of+Baghdad), and [Dark Ritual](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Ritual). The second issue was that [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) and [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) had a homogenizing effect on Vintage blue decks. Once you put four [Force of Will](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will), four [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm), four [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder), a bunch of restricted cards, and some mana sources in your deck, there simply isn't much room to put in anything else. This meant that the differences between different [Force of Will](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) decks were usually very small, and that hurt the format's variety.

![](https://i.ormos.uk/99/66/99669955594e6ea1755a082ada5dc1aa32bd7f2993e5afe0c4e0f06c67d8efcf.jpg)

The developers believed that restricting [Flash](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flash), [Gush](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush), and [Merchant Scroll](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merchant+Scroll) would mitigate the first problem because they were the key pieces to the most powerful [Force of Will](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) decks. They considered restricting only [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) to solve the second problem, but [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) was strong enough that many players who did not play [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) before would just replace their [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm)s with [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder)s and the situation would be similar. Therefore, they chose to restrict both cards instead despite how odd it felt to restrict a card as innocuous as [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder).

In the end, even though restricting [Brainstorm](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brainstorm) and [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) looked strange, it accomplished our goals for Vintage because it forced blue players to make meaningful decisions about what cards they would play with their [Force of Will](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will)s. Many players have chosen [Mana Drain](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain) and [Thirst for Knowledge](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thirst+for+Knowledge). Others have experimented with [Intuition](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Intuition+) and [Accumulated Knowledge](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Accumulated+Knowledge). Some players are willing to play four [Force of Will](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will)s with as few as seventeen blue cards in their deck and accept the inconsistency that this invites. Any of these decisions is meaningful, and the format is much more diverse even within the blue decks.

### Unexpected

<table><tbody><tr><td>&#10;					<div>&#10;						<div><img alt="Thirst for Knowledge" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Thirst+for+Knowledge"></div>&#10;					</div>&#10;				</td>&#10;				<td>&#10;					<div>&#10;						<div><img alt="Accumulated Knowledge" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Accumulated+Knowledge"></div>&#10;					</div>&#10;				</td>&#10;			</tr></tbody></table>

We never expected to make a [Morphling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) variant that had haste when [Thornling](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thornling) first arrived from **Magic**'s designers, and no one expected that [Ponder](https://web.archive.org/web/20090403000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ponder) would be restricted while *Lorwyn* was being developed. Despite that, we think that **Magic** is a better game because we were willing to do those things even though they looked strange. We don't make decisions that affect **Magic** lightly, we never lose sight of how cool it is that you like our game as much as we do, and we're glad you keep playing even if you occasionally disagree with us.

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>What is your favorite paper <b>Magic</b> Constructed format?</b></th>&#10;			</tr></thead><tbody><tr><td>Standard</td>&#10;				<td>3218</td>&#10;				<td>35.1%</td>&#10;			</tr><tr><td>Legacy</td>&#10;				<td>1335</td>&#10;				<td>14.5%</td>&#10;			</tr><tr><td>I don't worry about formats.</td>&#10;				<td>1321</td>&#10;				<td>14.4%</td>&#10;			</tr><tr><td>Extended</td>&#10;				<td>1245</td>&#10;				<td>13.6%</td>&#10;			</tr><tr><td>EDH/Commander</td>&#10;				<td>872</td>&#10;				<td>9.5%</td>&#10;			</tr><tr><td>Vintage</td>&#10;				<td>787</td>&#10;				<td>8.6%</td>&#10;			</tr><tr><td>Other</td>&#10;				<td>400</td>&#10;				<td>4.4%</td>&#10;			</tr><tr><td><b>Total</b></td>&#10;				<td><b>9178</b></td>&#10;				<td><b>100.0%</b></td>&#10;			</tr></tbody></table>
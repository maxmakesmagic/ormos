---
id: v224v6nx
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/01-14-how-to-make-a-time-machine
title: How to Make a Time Machine
published: '2011-01-14'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
    lang_detected: en
    capture_id: 723167
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
    captured_at: '2021-11-28 07:12:58+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
    lang_detected: en
    capture_id: 723167
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
    captured_at: '2021-11-28 07:12:58+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
    lang_detected: en
    capture_id: 723167
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
    captured_at: '2021-11-28 07:12:58+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
    lang_detected: en
    capture_id: 723167
    url: https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
    captured_at: '2021-11-28 07:12:58+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: v224v6nx
  url: https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
  page_key: magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
  lang: en
  template: drupal
  captured_at: '2021-11-28 07:12:58+00'
  capture_id: 723167
  wayback_url: https://web.archive.org/web/20211128071258id_/https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
- document_id: v224v6nx
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/125
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/125
  lang: en
  template: aspx
  captured_at: '2013-07-02 06:30:58+00'
  capture_id: 612958
  wayback_url: https://web.archive.org/web/20130702063058id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/125
- document_id: v224v6nx
  url: https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-14
  lang: en
  template: drupal
  captured_at: '2021-10-24 01:08:09+00'
  capture_id: 723168
  wayback_url: https://web.archive.org/web/20211024010809id_/https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-14
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: v224v6nx
  capture_id: 723167
  url: https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
  wayback_url: https://web.archive.org/web/20211128071258id_/https://magic.wizards.com/en/articles/archive/latest-developments/how-make-time-machine-2011-01-13
  captured_at: '2021-11-28 07:12:58+00'
  template: drupal
  sha256: f5870dfe50ead576bab1ae821d0913028e0ccaafdc26c96383b9460316e68cb1
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
M*asters Edition III* and *Masters Edition IV* are two of the more interesting projects I've ever worked on during my time at Wizards. Although I wrote preview articles for both sets, I have wanted for a while to write a crunchy development column about the *Masters* development process. This is that article.

When **Magic Online** was released, the most recent blocks were *Invasion* and *Odyssey*. Every paper set since *Invasion*, then, was released online. Later, we released *Mirage* online, and began moving forward from there. We are now all the way up to *Urza's Legacy*. We have not, however, released online any paper sets that came before *Mirage*. What gives?

![](http://media.wizards.com/images/magic/daily/ld/ld125_mastersArt.jpg)  

Let's talk for a moment about one of the realities of **Magic Online**. In paper **Magic**, many players buy packs and open them for cards. The **Magic Online** audience, however, prefers to get cards by playing Limited. That's not a huge surprise, as **Magic Online** is the perfect venue for drafting whenever you want and over and over again if desired. However, this puts some restrictions on what kind of sets we can release online.

Theoretically, we could have just released *The Dark* online. However, that would have been a poor idea. It's likely that most of you have never attempted to draft *The Dark*. I have. It was horrible. I can't blame the designers and developers of *The Dark* for this, as Booster Draft didn't exist as a popular format then, but it was really awful. I would not wish it on anyone. People I knew who tried drafting other pre-*Mirage* sets reported similar experiences.

At the time, I didn't bother to investigate why these drafts didn't work. Working on the *Masters* sets several years later showed me what was actually going on.

The Creatures in Old Sets All Suck

Modern Limited games all revolve around creature combat. That requires creatures in high enough power and quantity at low rarities that games play out normally. This was obviously not a concern to the people behind pre-*Mirage* sets; for example, in *Legends*, the only mono-red common creatures are Kobolds, Walls, and [Blazing Effigy](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blazing+Effigy). This is not a recipe for fun drafting. Even when there were enough creatures, though, they were much weaker than we make creatures now. 

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crimson+Kobolds"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Crimson+Kobolds"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blazing+Effigy"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Blazing+Effigy"></a></div></div></td></tr></tbody></table>

There Aren't Any Instants

I said just above that creature combat is one of the most important pieces of modern Limited. One of the keys to creature combat being fun is not knowing exactly how a given creature combat will go, and the key to surprises during combat is instants. We include tons of cards that can screw up a combat step so that surprises can happen, and we try to spread those cards around all the colors. For example, ***Magic** 2011* contains [Mighty Leap](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mighty+Leap), [Diminish](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diminish), [Stabbing Pain](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stabbing+Pain), [Thunder Strike](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thunder+Strike), and [Giant Growth](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth). Not all of these are strong enough that you play them in every deck, but I've lost combat steps to all five of them. Pre-*Mirage* sets just don't have very many cards like this, likely because no one was drafting.

![](http://media.wizards.com/images/magic/daily/ld/ld125_noInstants.jpg)  

White and Green Are Terrible

In modern sets, white and green tend to get the most strength from their creatures, and have somewhat weaker spells to compensate for that and keep colors balanced in power. As I already noted, though, creatures in old sets were uniformly less powerful, so the green and white creatures didn't pick up the slack. This meant that green and white were pretty much just worse. You'll also note that [Pacifism](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism), first printed in *Mirage*, hadn't been invented yet, and strong [Giant Growth](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) effects weren't included as a rule in sets. That takes away two of the most important effects that define white and green in modern sets. Without those cards and without creatures that compensate for the powerful spells that the other colors have, white and green were just worse.

The Rares Are Not Good Enough in Limited

Rares in Limited do two very important jobs. One of those jobs is giving players direction. On a basic level, when you open up a [Shivan Dragon](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shivan+Dragon), you want to play red. That will give you a different experience from the time you opened [Mahamoti Djinn](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mahamoti+Djinn), which made you want to play blue. Rares can also give you even more direction by encouraging you to build a unique deck. For example, [Overwhelming Stampede](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overwhelming+Stampede) is a powerful card that you would be hard pressed not to first pick.

![](http://media.wizards.com/images/magic/daily/ld/ld125_3Cards1.jpg)  

However, it encourages you to play tons of creatures in your deck, and starting with an [Overwhelming Stampede](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overwhelming+Stampede) may cause you to take [Sacred Wolf](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sacred+Wolf) over [Giant Growth](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) when you would otherwise have made the opposite pick. The last thing that rares can do is cause games to end. Often, when a game threatens to grind on forever, an enormous rare bomb will show up and put the game out of its misery. All three of these functions are important.

Although pre-*Mirage* sets are full of rares with unique and interesting effects, many of those cards are so goofy that they don't fit into an average Limited deck. That means that there aren't enough rares in decks to give the variety of experience that we've found that **Magic** players like.

As you can see, there are all kinds of problems with drafting those sets. Happily, Erik and I were able to compensate for them in *Masters Edition IV*. Here's how we did it.

Creatures

I said above that the creatures in old sets were quite bad, and it's true. Thankfully, that's not true about the *Portal* sets, which saved us here. Those sets are full of cards like [Ironhoof Ox](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironhoof+Ox), [Alaborn Musketeer](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alaborn+Musketeer), [Cloud Spirit](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloud+Spirit), [Goblin Firestarter](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Firestarter), and [Foul Spirit](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Foul+Spirit) that are the bread and butter of modern Limited. Cards like that can only do so much to provide character and uniqueness to a format, of course, but that's what we used the cards from Limited Edition Beta, *Arabian Nights*, and *Antiquities* for. We were missing the simple cards, and that was exactly what *Portal* had to offer.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironhoof+Ox"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Ironhoof+Ox"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Foul+Spirit"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Foul+Spirit"></a></div></div></td></tr></tbody></table>

Using *Portal* to fill in the common creature gaps often does some strange things to the creative feel of the set. For example, [Alaborn Musketeer](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alaborn+Musketeer)'s reach ability, quite strange for a white card these days, is justified by the enormous gun that he is holding. *Masters Edition III* was even more jarring, as heroic fantasy portraits like those on [Marhault Elsdragon](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marhault+Elsdragon) or [Riven Turnbull](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riven+Turnbull) lived next to realistic depictions of historical Chinese people from *Portal: Three Kingdoms*. 

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Southern+Elephant"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Southern+Elephant"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shu+Elite+Companions"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Shu+Elite+Companions"></a></div></div></td></tr></tbody></table>

I sometimes wonder what the designers and developers of the *Portal* sets would think if they saw a [Southern Elephant](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Southern+Elephant) being regenerated by an [Elephant Graveyard](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elephant+Graveyard) or a [Shu Elite Companions](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shu+Elite+Companions) sneaking past [Arcades Sabboth](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Arcades+Sabboth). However, that's what it takes to make a playable *Masters* set, and it gives those sets an anarchic and unique feel that I enjoy.

Instants

In contrast to the last problem, the *Portal* sets offer very little help here, as they were specifically designed to not have instants. We have since retrofitted several cards from the *Portal* sets with the instant type, as they actually functioned as such, but that only gave us a few cards in [False Summoning](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=False+Summoning) and [Just Fate](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Just+Fate). 

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=False+Summoning"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=False+Summoning"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Just+Fate"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Just+Fate"></a></div></div></td></tr></tbody></table>

For the rest of the instants, we had to look elsewhere. As it turns out, there were still instants to be found that we hadn't used in *Masters Editions I*, *II*, and *III*. [Crumble](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crumble), [Divine Offering](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divine+Offering), and [Terror](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terror) are all strong instant removal spells that rival the best spells in modern sets. [Gravebind](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravebind), [Sandstorm](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sandstorm), [Just Fate](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Just+Fate), [Howl From Beyond](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howl+From+Beyond), and [Fog](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog) can screw up combat steps. This group of cards isn't as strong as the equivalents I would include in a modern set, but it's what we had. I put literally every instant I found that had potential combat interactions in, all the way up to [Healing Salve](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Healing+Salve). My favorite contribution to the set was putting [Giant Growth](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in; there was no other available green creature pump spell, and although the card had been in all three previous *Masters Editions*, there was nothing before *Mirage* that I could include that did anything similar.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravebind"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Gravebind"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Healing+Salve"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Healing+Salve"></a></div></div></td></tr></tbody></table>

In the end, I feel that there are more than enough instants in the set for it to be fun to play. I would have liked to find even more so that some could be uncommon, meaning that they would show up less often and not be as correct to play around, but there simply weren't any more cards to include. As is, everything works just fine.

Green and White

The problem with making white and green strong enough was the hardest of the four problems to solve. In *Masters Edition IV*, white has a bad [Pacifism](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism) in [Serra Bestiary](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serra+Bestiary) and one of the strongest commons of the set in [Divine Offering](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divine+Offering), which is a filthy card when [Obsianus Golem](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Obsianus+Golem)s and [Clay Statue](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clay+Statue)s are running around. White also has an aggressive bent, supported by the common [Righteous Charge](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Righteous+Charge), which is a fine way to put away a game when you have lots of creatures on the table.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Righteous+Charge"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Righteous+Charge"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scavenger+Folk"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Scavenger+Folk"></a></div></div></td></tr></tbody></table>

Green was more challenging. [Crumble](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crumble) and [Scavenger Folk](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scavenger+Folk) are both strong removal cards, which helps. [Citanul Druid](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Citanul+Druid) and [Argothian Pixies](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Argothian+Pixies) are also strong against artifacts. [Ironhoof Ox](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironhoof+Ox), [Southern Elephant](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Southern+Elephant), and [War Mammoth](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Mammoth) are some of the more efficient big creatures in the format. However, if an opponent of a green player is low on artifacts, things can get a little rough. I would, however, encourage green players to look out for [Elephant Graveyard](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elephant+Graveyard), which can make those [War Mammoth](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Mammoth)s and [Southern Elephant](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Southern+Elephant)s much more intimidating.

Rares

Although finding exciting Constructed rares was no problem at all for *Masters Edition IV*, finding rares that mattered in Limited was harder. This was especially true due to cards like [In the Eye of Chaos](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=In+the+Eye+of+Chaos), [Leeches](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leeches), and [Naked Singularity](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naked+Singularity), that had to get into **Magic Online** somehow but were obviously unplayable in Limited. Those were blanks every time we opened them, and that's not a recipe for excitement.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloud+Dragon"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Cloud+Dragon"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dread+Reaper"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Dread+Reaper"></a></div></div></td></tr></tbody></table>

We had to reach deep into the bucket for cards that would matter in Limited. Once again, the *Portal* sets were our saviors. Every time I found a simple but huge card like [Cloud Dragon](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloud+Dragon), [Dread Reaper](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dread+Reaper), or [Thunder Dragon](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thunder+Dragon), I put it in, and over time the density of potentially game-ending rares got high enough. Although [Deathcoil Wurm](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deathcoil+Wurm) and [Minion of Tevesh Szat](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Minion+of+Tevesh+Szat) aren't the cards that make you excited about playing Legacy or Classic, I think you'll still be glad when you open them.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overwhelming+Forces"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Overwhelming+Forces"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Daggers"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Rain+of+Daggers"></a></div></div></td></tr></tbody></table>

The drive to put in Limited game-ending cards sometimes caused us to have two cards that feel very similar; for example, [Overwhelming Forces](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overwhelming+Forces) and [Rain of Daggers](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Daggers) are both big and dumb cards that can put a game away. We would avoid this in a paper set, but we couldn't make new cards here. Even so, these two cards push you in different directions. [Overwhelming Forces](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overwhelming+Forces) points you toward a control deck with lots of mana that stalls until you cast it, while [Rain of Daggers](https://web.archive.org/web/20110114000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Daggers)' life loss encourages you to lean a little more aggressively. This kind of subtle difference exists in many pairs of similar *Masters Edition IV*, and drafters would do well to adjust for them.

![](http://media.wizards.com/images/magic/daily/ld/ld125_me4Logo.jpg)  

Erik and I had a ton of fun working on *Masters Edition III* and *Masters Edition IV*. *Masters Edition IV* release events started two days ago, so there's still plenty of time to go and play. Next week, though, attention turns back to the broader as we begin *Mirrodin Besieged* previews. I hope you've enjoyed this little side trip, and I'll see you next Friday.

Last Week's Poll

<table><tbody><tr><td colspan="3"><b>Have you played Limited with <i>Masters Edition</i>, <i>Masters Edition II</i>, or <i>Masters Edition III</i>?</b></td></tr><tr><td>Yes, with all.</td><td>312</td><td>6.6%</td></tr><tr><td>Yes, with some.</td><td>437</td><td>9.2%</td></tr><tr><td>No.</td><td>3993</td><td>84.2%</td></tr><tr><td><b>Total</b></td><td><b>4742</b></td><td><b>100.0%</b></td></tr></tbody></table>

  
  

This Week's Poll

<table><tbody><tr><td><div><b>Which of last year's draft formats was your favorite?</b><i>Zendikar-Zendikar-Zendikar</i><i>Zendikar-Zendikar-Worldwake</i><i>Rise-Rise-Rise</i>M11-M11-M11I don't have an opinion.</div></td></tr></tbody></table>

  
[![](https://i.ormos.uk/54/ed/54ed8d6a757191146dd1acaaa063545c2cafd11510a4eb480a375e9a18152c3a.jpg)](https://web.archive.org/web/20110114000000/http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/prerelease-facts)
---
id: b69p4y6s
kind: article
lang: en
path: /en/articles/announcements/2023/04-19-march-of-the-machine-update-bulletin
title: March of the Machine Update Bulletin
published: '2023-04-19'
column_slug: announcements
column: Announcements
authors:
- slug: eliana-rabinowitz-2195a536
  name: Eliana Rabinowitz
- slug: jess-dunks-ac6aaab2
  name: Jess Dunks
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
    lang_detected: en
    capture_id: 136086
    url: https://magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
    captured_at: '2024-05-18 01:19:35+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
    lang_detected: en
    capture_id: 136086
    url: https://magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
    captured_at: '2024-05-18 01:19:35+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
    lang_detected: en
    capture_id: 136086
    url: https://magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
    captured_at: '2024-05-18 01:19:35+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
    lang_detected: en
    capture_id: 136086
    url: https://magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
    captured_at: '2024-05-18 01:19:35+00'
    rule: url.article_section
sources:
- document_id: b69p4y6s
  url: https://magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
  page_key: magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:19:35+00'
  capture_id: 136086
  wayback_url: https://web.archive.org/web/20240518011935id_/https://magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: b69p4y6s
  capture_id: 136086
  url: https://magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
  wayback_url: https://web.archive.org/web/20240518011935id_/https://magic.wizards.com/en/news/announcements/march-of-the-machine-update-bulletin
  captured_at: '2024-05-18 01:19:35+00'
  template: contentful
  sha256: aac394604d00845b20694301524ad31272aa50ec4b6882f933a1142c04205378
render_recovery: []
---
Hello, everyone!

The *March of the Machine* Update Bulletin is the place to find information about changes to the *Magic* Comprehensive Rules coming with the set's release and updates to the official text of some cards. This document is written while the rules and card text changes are still going through editing, so it's possible they'll be a little different from the final changes. When the rules are finalized, you'll be able to see them on the [rules page](https://web.archive.org/web/20230419000000/https://magic.wizards.com/en/game-info/gameplay/rules-and-formats/rules). Once the set is live, official Oracle card text for each card can be found at [Gatherer](https://web.archive.org/web/20230419000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=508148).

Alright. Let's dive in!

## *March of the Machine* Comprehensive Rules Changes

This is a summary of the rule changes planned for *Magic* with the release *March of the Machine*. The official rules are still under review at the time of this writing. When they are published, they can be found on our [rules page](https://web.archive.org/web/20230419000000/https://magic.wizards.com/en/game-info/gameplay/rules-and-formats/rules). If there should be a discrepancy between this summary and the official rules, the official rules take precedence.

### New and Updated rules

### Incubate

#### 701.51

![Incubator token](https://media.wizards.com/2023/mom/en_01bec8f863.png)

![Phyrexian token](https://media.wizards.com/2023/mom/en_c6e9ae10f0.png)

 

This new section covers incubate, a new keyword action that makes Incubator tokens with +1/+1 counters. These are transforming double-faced tokens that are artifacts on the front face but have the ability "{2}: Transform this artifact." The back face is a colorless 0/0 Phyrexian artifact creature. The rules previously allowed only cards to transform, not tokens. Now, transforming double-faced tokens can transform, too, including tokens that are copies of transforming double-faced permanents. That means that a token copy of an Incubator token will function just like a regular Incubator token (although it may be disappointing to transform it if it doesn't have any counters because it has no toughness on the back face and will probably die).

#### 111.10i

Incubator tokens join the list of predefined tokens.

### Backup

#### 702.160

This section defines backup, a new triggered ability that puts +1/+1 counters on target creature when a creature with backup enters the battlefield. If this ability targets another creature than the one with backup, the targeted creature also gets the ability printed below backup until end of turn. The abilities granted by backup are determined only when the ability goes on the stack, so losing abilities before the backup ability resolves won't change its effect. On the other hand, additional abilities a creature gains aren't considered to be printed on the card, so backup won't grant them.

### Battles

#### 310

This section (moved from 315 and no longer empty) defines battles, a brand-new card type. Battles are permanents, and a battle spell can be cast any time its controller has priority while the stack is empty. Each one has a defense value, and it gets counters equal to that defense value as it enters the battlefield. Battles can be dealt damage and attacked, like planeswalkers, and damage to them causes that many defense counters to be removed.

As a battle enters the battlefield, its controller must assign a protector for the battle. All battles printed so far have the subtype Siege, and a Siege's protector must be one of its controller's opponents. The battle's protector doesn't control it, but they can block creatures that are attacking the battle just like they can block attacks on planeswalkers they control. Any player, including a battle's controller, can attack the battle as long as the protector of that battle is a defending player. This also means that the protector of a battle cannot attack it. The protector is always considered the defending player for any effects that need to determine the defending player for a battle.

Sieges have an additional intrinsic ability. That ability is "when the last defense counter is removed from this permanent, exile it, then you may cast it transformed without paying its mana cost." This means that if for any reason a battle enters the battlefield without defense counters, it will be put into the graveyard and its controller will not get the chance to exile it.

For more information about battles and Sieges, please check the *[March of the Machine Release Notes](/en/articles/feature/2023/04-07-march-of-the-machine-release-notes)* or the [full comprehensive rules](https://web.archive.org/web/20230419000000/https://magic.wizards.com/en/rules).

#### 120

Objects that deal damage to "any target" can target battles. Damage dealt to battles causes that many defense counters to be removed, and battles dealt damage greater than their defense count as being dealt excess damage.

Various other rules throughout the document have also been updated to accommodate battles, including rules for combat, counters, types, state-based actions, and so on.

### Other rules changes

#### 208.3a

If an effect changes the power or toughness of a noncreature permanent, this rule says the effect is still created and will work if that permanent became a creature during the duration of that effect. This rule is now a little more explicit that effects that set a permanent's power or toughness are also still created and work the same way.

#### 311.7

Planes, nontraditional cards used in the Planechase variant, have triggered abilities that previously triggered when the chaos symbol was rolled on the planar die. Those abilities now trigger when "chaos ensues." This is mostly an aesthetic change; obviously, chaos ensues when the chaos symbol is rolled on the planar die. In addition, resolving spells or abilities can also state that chaos ensues. All previously printed plane cards have had an update to their Oracle text to accommodate this change.

#### 700.10

![Cut Short](https://media.wizards.com/2023/mom/en_85848ff4da.png)

The card Cut Short refers to a planeswalker that was activated this turn. This rule explains that a permanent "was activated" if it was the source of an ability that was activated this turn.

#### 701.19j

![Invasion of Arcavios](https://media.wizards.com/2023/mom/en_6fd8e8aab5.png)

![Invocation of the Founders](https://media.wizards.com/2023/mom/en_bd2b5b609a.png)

 

Invasion of Arcavios instructs a player to search for a card they own outside the game. The search rules have been expanded to explain that this means to choose a card you own from outside the game. You do not need to bring every card you own to the table and search through them all to resolve this effect (that means you, Jess).

#### 701.28

The transform rules now include transforming double-faced tokens and define a "transformed permanent." A permanent with its front face up is never considered transformed, even if it previously had its back face up.

#### 707.8a and 707.10g

Now that we have transforming double-faced tokens, the copy rules needed some updates. An effect that creates a token that is a copy of a transforming permanent will create a transforming double-faced token. If the permanent being copied has its back face up, the token copy will also have its back face up. These transforming double-faced tokens can transform just like the permanents they copy. Copying a transforming double-faced spell or card not on the battlefield works the same way. Note that this does not apply to permanents already on the battlefield that become a copy of a transforming permanent. It also doesn't apply to tokens with their own set of characteristics that enter the battlefield and copy a transforming permanent due to a replacement effect, like a Saproling token that enters as a copy of a transforming permanent due to a Mystic Reflection, or a token that is a copy of a Clone. Those copies still only have one face and cannot transform.

#### 712

A lot of players would be surprised to learn that meld cards aren't *technically* double-faced cards because their back face is, well, only half a card face. However, the fact that I just used the words "back face" to describe them (and so did the rules) kind of demonstrates how confusing this distinction can be. Now that some cards, like Overgrown Pest, reference double-faced cards in their rules text, we've officially let meld cards join the double-faced card family to avoid player confusion. While this means that section 713 got folded into section 712 (where double-faced cards live), there is no functional difference to this change other than allowing the aforementioned effects to find them. The back face of a meld card still doesn't have any characteristics, however. After all, it's still only half a card face.

#### 712.13a

This rule plugs a new corner-case rules hole that would sometimes cause a transforming double-faced spell with its front face up on the stack to enter the battlefield transformed even though the back face of that card is an instant or sorcery card. If that happens, it won't enter the battlefield and will instead be put into its owner's graveyard. Battles are the only new type of card that gets to be on the battlefield for now; instants and sorceries don't get to join that party.

### New Subtypes

Incubator  
 Siege  
 The Abyss  
 Amonkhet  
 Antausia  
 Arcavios  
 Capenna  
 Cridhe  
 Echoir  
 Eldraine  
 Fiora  
 Gargantikar  
 Bobakhan  
 Ikoria  
 Ixalan  
 Kaladesh  
 Kylem  
 Shenmeng  
 Tarkir  
 Theros  
 Zhalfir

### New Glossary Entries

Backup  
 Defense  
 Incubate  
 Incubator token  
 Protect  
 Protector  
 Siege

### Updated Glossary Entries

Battle  
 Chaos ability  
 Chaos symbol

## *March of the Machine* Oracle Changes

There are a few cards receiving errata to their Oracle text with the release of this set. You can find the official text of any card on [Gatherer](https://web.archive.org/web/20230419000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=508148).

### Large Templating Changes

#### Chaos Ensues

![Towashi](https://media.wizards.com/2023/mom/en_4dfd25f938.png)

Each plane card with a chaos ability is receiving an update to its rules text to use the new "whenever chaos ensues" triggered ability rather than the previous "whenever you roll \[CHAOS\]" triggered ability. Though this is technically a functional change that allows other effects to cause chaos abilities to trigger, chaos abilities and cards that care about them should play the same way they always did with older cards.

### Individual Card Changes

#### Ruxa, Patient Professor

![Ruxa, Patient Professor](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=518462)

The last ability of Ruxa, Patient Professor has received an update to make it clear that it is a choice you make for each creature you control with no abilities, not a choice you make once for all creatures with no abilities. Specifically, if you attack with more than one creature with no abilities, you may have some of them, none of them, or all of them assign their combat damage as though they weren't blocked. It isn't an all-or-nothing choice.

**Old Text**:

Whenever Ruxa, Patient Professor enters the battlefield or attacks, return target creature card with no abilities from your graveyard to your hand.  
 Creatures you control with no abilities get +1/+1.  
 You may have creatures you control with no abilities assign their combat damage as though they weren't blocked.

**New Text**:

Whenever Ruxa, Patient Professor enters the battlefield or attacks, return target creature card with no abilities from your graveyard to your hand.  
 Creatures you control with no abilities get +1/+1.  
 For each creature you control with no abilities, you may have that creature assign its combat damage as though it weren't blocked.

#### Druid of the Emerald Grove

![Druid of the Emerald Grove](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=563109&type=card)

*Unfinity* introduced cards that can increase the result of a die roll. For cards that instruct you to roll a d20 and have results tables telling you what that means, this can cause the die result to be higher than any of the results on the table. In most cases, this just causes nothing to happen. In the case of Druid of the Emerald Grove, however, this would mean that you search your library and then there would be no instruction telling you to shuffle. Druid of the Emerald Grove has received an update to its rules text so that the last entry in its results table accounts for results higher than 20. No other cards with results tables have been changed in this update.

**Old Text**:

When Druid of the Emerald Grove enters the battlefield, search your library for up to two basic land cards and reveal them, then roll a d20.  
 **1–9** | Put those cards into your hand, then shuffle.  
 **10–19** | Put one of those cards onto the battlefield tapped and the other into your hand, then shuffle.  
 **20** | Put those cards onto the battlefield tapped, then shuffle.

**New Text**:

When Druid of the Emerald Grove enters the battlefield, search your library for up to two basic land cards and reveal them, then roll a d20.  
 **1–9** | Put those cards into your hand, then shuffle.  
 **10–19** | Put one of those cards onto the battlefield tapped and the other into your hand, then shuffle.  
 **20+** | Put those cards onto the battlefield tapped, then shuffle.
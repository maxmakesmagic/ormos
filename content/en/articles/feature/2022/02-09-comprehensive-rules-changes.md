---
id: mn4ve4kj
kind: article
lang: en
path: /en/articles/feature/2022/02-09-comprehensive-rules-changes
title: Comprehensive Rules Changes
published: '2022-02-09'
column_slug: feature
column: Feature
authors:
- slug: jess-dunks-ac6aaab2
  name: Jess Dunks
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
    lang_detected: en
    capture_id: 127364
    url: https://magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
    captured_at: '2024-05-18 01:46:32+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
    lang_detected: en
    capture_id: 127364
    url: https://magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
    captured_at: '2024-05-18 01:46:32+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
    lang_detected: en
    capture_id: 127364
    url: https://magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
    captured_at: '2024-05-18 01:46:32+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2022-02-09
    lang_detected: en
    capture_id: 1095351
    url: https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2022-02-09
    captured_at: '2022-09-09 00:37:25+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: mn4ve4kj
  url: https://magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
  page_key: magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:46:32+00'
  capture_id: 127364
  wayback_url: https://web.archive.org/web/20240518014632id_/https://magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
- document_id: mn4ve4kj
  url: https://magic.wizards.com//en/articles/archive/news/comprehensive-rules-changes-2022-02-09
  page_key: magic.wizards.com//en/articles/archive/news/comprehensive-rules-changes-2022-02-09
  lang: en
  template: drupal
  captured_at: '2022-02-10 10:38:18+00'
  capture_id: 1095349
  wayback_url: https://web.archive.org/web/20220210103818id_/https://magic.wizards.com//en/articles/archive/news/comprehensive-rules-changes-2022-02-09
- document_id: mn4ve4kj
  url: https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2022-02-09
  page_key: magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2022-02-09
  lang: en
  template: drupal
  captured_at: '2022-09-09 00:37:25+00'
  capture_id: 1095351
  wayback_url: https://web.archive.org/web/20220909003725id_/https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2022-02-09
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: mn4ve4kj
  capture_id: 127364
  url: https://magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
  wayback_url: https://web.archive.org/web/20240518014632id_/https://magic.wizards.com/en/news/announcements/comprehensive-rules-changes-2-9-22
  captured_at: '2024-05-18 01:46:32+00'
  template: contentful
  sha256: b5f48441f4c057c2bb749361e191f70cba8436fb937205965cbe1bd8095c8c64
render_recovery: []
---
This is a summary of the rule changes planned for *Magic* with the release of *Kamigawa: Neon Dynasty*. The official rules are still under review at the time of this writing. When they are published, they can be found on our [rules page](https://web.archive.org/web/20220209000000/https://magic.wizards.com/en/game-info/gameplay/rules-and-formats/rules). If there should be a discrepancy between this summary and the official rules, the official rules take precedence.

# New and Updated rules

## Reconfigure

## 301.5c

This is the rule that says an Equipment that's also a creature can't equip a creature. Obviously, this needs to change for reconfigure to work correctly. Now, this rule has an exception for Equipment with reconfigure.

## 702.151

This rule and its subrules define the keyword ability reconfigure. The first subrule tells us that reconfigure represents two activated abilities. Reconfigure \[cost\] means "\[Cost\]: Attach this permanent to another target creature you control. Activate only as a sorcery," and "\[Cost\]: Unattach this permanent. Activate only if this permanent is attached to a creature and only as a sorcery."

The rest of the subrules in this section explain that when an effect attaches an Equipment with reconfigure to another creature, it also causes the Equipment to stop being a creature as long as its attached and that if it's still somehow a creature after that, it becomes unattached.

## Vehicles

## 702.122a

This is the rule for the crew ability. A lot of players may not have realized that Vehicles, once animated, could technically crew themselves. This is not only unintuitive but also pretty scary for people like me who don't trust self-driving cars. A one-word change to this rule now prevents players from being able to do this.

## 701.22d

Some Vehicles in this set, such as Mobilizer Mech, have abilities that trigger when they become crewed. This new rule tells us that "When this Vehicle becomes crewed" means "When a crew ability of this Vehicle resolves." This is notably different from a triggered ability that triggers when a creature crews a Vehicle, such as that found on Gearshift Ace. Those abilities trigger when you activate the crew ability rather than when it resolves. It's also worth noting that these abilities won't trigger if that Vehicle becomes a creature in any way other than its own crew ability.

## Compleated

## 107.4 and 107.4f

![Tamiyo, Compleated Sage](https://media.wizards.com/2021/neo/en_ub8fLyqE7L.png)

This is the rule that defines what the mana symbols are. Tamiyo, Compleated Sage uses a new hybrid Phyrexian mana symbol that needed to be added here. Even though no other cards have this symbol, the other nine hybrid Phyrexian symbols have been added here for compleateness.

## 702.150

This rule defines the replacement effect that the keyword ability compleated represents. Basically, for each time you pay life for a Phyrexian mana symbol in the cost of a planeswalker spell with compleated, if it would enter the battlefield with loyalty counters, it enters with that many counters minus two instead. It was very difficult to complete this rule with autocorrect on.

## Modified Creatures

## 700.9

A modified creature is one that has one or more counters on it, is equipped, or is enchanted by an Aura that's controlled by that creature's controller. This new rule explains that in very similar words to the last sentence and also explains that only creatures can be modified.

## Other rules changes

## 406.3

![The Dragon Kami Reborn](https://media.wizards.com/2021/neo/en_SeMA6kIpvn.png)

This is the rule that says that once a player has been allowed to look at cards in exile, that player may continue to look at those cards. As written, the rule only applied to cards that were exiled already when you were given permission to look at them. It didn't apply to situations where you look at a card *and then* exile it face down. Therefore, cards that do this also explicitly say you may look at those cards. When designing The Dragon-Kami Reborn, we challenged the need for this and decided to write this permission directly into the rules. Now, if an effect says to look at some cards and exile them face down, you may continue to look at those cards for as long as they are in exile. This is technically a functional change for one card (\[autocard\]Clone Shell\[/autocard\]), but my experience with that card is that most players already believed they could look at the exiled card again and were playing that way anyway.

## 508.3d-f

This is the section of rules that explains what abilities trigger when creatures attack. It has been updated to account for some newer trigger conditions. This does not functionally change any cards.

## 602.5f

Some rules tell you that certain words on older cards mean something different than what they say. For example, older cards that say "removed from the game" have been updated to say "exiled" instead. A rule exists to tell you that these are the same. When "Activate this ability only as a sorcery" was shortened to "Activate only as a sorcery" on many cards, a similar rule was added. However, since there is no functional difference or potential for confusion between the two templates, this rule is unnecessary and has been removed.

## 616.1d

*Kamigawa: Neon Dynasty* Sagas are transforming double-faced cards that exile themselves and return to the battlefield transformed as creatures. A new rule clarifying when to apply the "enters the battlefield transformed" replacement effect covers an odd corner case by preventing players from choosing to have them also enter with a lore counter when entering the battlefield transformed.

## 702.20b

When a card tells you to search your library for a particular card, shuffle, then put that card on top, the card is technically still in your library at the time you are shuffling. This rule is the one that says you don't shuffle that card along with it, which allows this template to work properly. However, it turns out that it wasn't quite broad enough to cover \[autocard\]Ecological Appreciation\[/autocard\], so it has now been updated to do so. This is not a functional change to any card unless you were playing \[autocard\]Ecological Appreciation\[/autocard\] in a very strange way.

## 707.8

This rule explains what happens if you copy a double-faced permanent. Since double-faced permanents come from double-faced spells, and we can also copy those, this rule was generalized to cover double-faced cards in all zones.

## 903.3a

![Shorikai, Genesis Engine](https://media.wizards.com/2021/neo/en_jJP7AFmr40.png)

Shorikai, Genesis Engine is a legendary Vehicle with an ability that says it can be your commander. The rule that supports this was given a minor tweak to make sure that ability functions properly on Vehicle cards.

## New Subtypes

Kaito was added to the list of planeswalker types.

## New Glossary Entries

Compleated, modified, reconfigure

* * *

[Introduction](/en/articles/feature/2022/02-09-kamigawa-neon-dynasty-update-bulletin)  
 Comprehensive Rules Changes  
 [Oracle Changes](/en/articles/feature/2022/02-09-oracle-changes)
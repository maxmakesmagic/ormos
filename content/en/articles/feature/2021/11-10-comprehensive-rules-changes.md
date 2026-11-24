---
id: ha9mhy3n
kind: article
lang: en
path: /en/articles/feature/2021/11-10-comprehensive-rules-changes
title: Comprehensive Rules Changes
published: '2021-11-10'
column_slug: feature
column: Feature
authors:
- slug: jess-dunks-ac6aaab2
  name: Jess Dunks
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
    lang_detected: en
    capture_id: 1095341
    url: https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
    captured_at: '2022-09-27 22:07:38+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
    lang_detected: en
    capture_id: 1095341
    url: https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
    captured_at: '2022-09-27 22:07:38+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
    lang_detected: en
    capture_id: 1095341
    url: https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
    captured_at: '2022-09-27 22:07:38+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
    lang_detected: en
    capture_id: 1095341
    url: https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
    captured_at: '2022-09-27 22:07:38+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: ha9mhy3n
  url: https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
  page_key: magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
  lang: en
  template: drupal
  captured_at: '2022-09-27 22:07:38+00'
  capture_id: 1095341
  wayback_url: https://web.archive.org/web/20220927220738id_/https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
- document_id: ha9mhy3n
  url: https://magic.wizards.com//en/articles/archive/news/comprehensive-rules-changes-2021-11-10
  page_key: magic.wizards.com//en/articles/archive/news/comprehensive-rules-changes-2021-11-10
  lang: en
  template: drupal
  captured_at: '2021-11-11 10:33:32+00'
  capture_id: 1095336
  wayback_url: https://web.archive.org/web/20211111103332id_/https://magic.wizards.com//en/articles/archive/news/comprehensive-rules-changes-2021-11-10
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ha9mhy3n
  capture_id: 1095341
  url: https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
  wayback_url: https://web.archive.org/web/20220927220738id_/https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2021-11-10
  captured_at: '2022-09-27 22:07:38+00'
  template: drupal
  sha256: 3512eace89b319b12a44335de4dd7905e47ed680c00cdf4124c14127a9ed8bd6
render_recovery: []
---
This is a summary of the rules changes planned for *Magic* with the release of [*Innistrad: Crimson Vow*](https://web.archive.org/web/20211110000000/https://magic.wizards.com/en/products/innistrad-crimson-vow). The official rules are still under review at the time of this writing. When they are published, they can be found on our [rules page](https://web.archive.org/web/20211110000000/https://magic.wizards.com/en/game-info/gameplay/rules-and-formats/rules). If there should be a discrepancy between this summary and the official rules, the official rules take precedence.

# New and Updated rules

## Blood Tokens

## 111.4

According to this rule, if a spell or ability created a token without specifying its name, the token's name was the same as its subtypes. For example, an effect which says "create a 2/2 Illusion creature token" would create a token whose name was Illusion. This had some uncommon but weird interactions with effects that let you choose the name of a card, such as those of [Pithing Needle](https://web.archive.org/web/20211110000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pithing+Needle) and [Runed Halo](https://web.archive.org/web/20211110000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runed+Halo). Since you can only choose names of printed cards for such effects, you usually can't choose the name of a token. Sometimes, however, the name of an unrelated card happens to overlap with the name of a token, such as the Illusion half of the split card [Illusion // Reality](https://web.archive.org/web/20211110000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusion+%2F%2F+Reality). In that case, choosing the name of the card would apply any relevant effects to tokens named Illusion.

With the creation of Blood tokens in *Innistrad: Crimson Vow*, this relatively obscure interaction had the potential to become significantly more common (see [Flesh // Blood](https://web.archive.org/web/20211110000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flesh+%2F%2F+Blood)). The fact that a player could stop Blood tokens with [Pithing Needle](https://web.archive.org/web/20211110000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pithing+Needle)'s effect but not Treasure, Food, or Clue tokens is inconsistent, and players shouldn't be expected to know which tokens share a name with a printed card, so we decided to change the rule. From now on, if a spell or ability is creating a token without specifying its name, the name will be the same as its subtypes plus the word "Token." For example, a "Goblin Scout creature token" is named "Goblin Scout Token." Similarly, the name of a Blood token created in the game is "Blood Token" and choosing the name "Blood" for an effect will not cause that effect to apply to Blood tokens.

Note that Blood token supplements found in *Innistrad: Crimson Vow* boosters will only have the word Blood on the name line. This does not affect gameplay. Also keep in mind that this rule change does not apply to a token that is a copy of another permanent or was created due to an ability that specified its name, such as that of [Llanowar Mentor](https://web.archive.org/web/20211110000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Mentor).

## 111.10g

This rule adds Blood tokens to the list of predefined tokens.

## 205.3g

This rule adds Blood to the list of artifact types.

## Alternate Names

## 201.5

The rule that covered secondary title bars for some versions of *Ikoria: Lair of Behemoths* cards has been generalized and expanded to make sure it includes cards from the *Innistrad: Crimson Vow* set and any future card with a secondary title bar and an alternate name.

## Day/Night and Daybound/Nightbound

## 502.2, 703.4b-d

Day/night didn't mention that it was a turn-based action in all the appropriate places. Now it is properly referenced in each place it should be.

## New Keyword Abilities

## Cleave

702.148 is the new rule that defines the cleave mechanic.

## Training

702.149 is the new rule that defines the training mechanic.

## New Glossary Entries

Alternate name, Blood token, cleave, flavor word, secondary title bar, training

* * *

[Introduction](/en/articles/feature/2021/11-10-innistrad-crimson-vow-update-bulletin)  
 Comprehensive Rules Changes  
[Oracle Changes](/en/articles/feature/2021/11-10-oracle-changes)
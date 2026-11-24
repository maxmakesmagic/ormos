---
id: v6veg7hn
kind: article
lang: en
path: /en/articles/feature/2002/01-24-rules-primer-madness
title: 'Rules Primer: Madness'
published: '2002-01-24'
column_slug: feature
column: Feature
authors:
- slug: paulbarclay
  name: Paul Barclay
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
    lang_detected: en
    capture_id: 191932
    url: https://magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
    captured_at: '2024-03-16 09:32:47+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
    lang_detected: en
    capture_id: 191932
    url: https://magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
    captured_at: '2024-03-16 09:32:47+00'
    rule: jsonld.date_published
  column:
    page_key: magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
    lang_detected: en
    capture_id: 191932
    url: https://magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
    captured_at: '2024-03-16 09:32:47+00'
    rule: url.article_section
    registry_match: registry.explicit
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/rules-primer-madness-2002-01-24
    lang_detected: en
    capture_id: 665746
    url: https://magic.wizards.com/en/articles/archive/feature/rules-primer-madness-2002-01-24
    captured_at: '2022-10-03 10:31:33+00'
    rule: drupal.div_author
sources:
- document_id: v6veg7hn
  url: https://magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
  page_key: magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
  lang: en
  template: contentful
  captured_at: '2024-03-16 09:32:47+00'
  capture_id: 191932
  wayback_url: https://web.archive.org/web/20240316093247id_/https://magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
- document_id: v6veg7hn
  url: https://magic.wizards.com/en/articles/archive/feature/rules-primer-madness-2002-01-24
  page_key: magic.wizards.com/en/articles/archive/feature/rules-primer-madness-2002-01-24
  lang: en
  template: drupal
  captured_at: '2022-10-03 10:31:33+00'
  capture_id: 665746
  wayback_url: https://web.archive.org/web/20221003103133id_/https://magic.wizards.com/en/articles/archive/feature/rules-primer-madness-2002-01-24
- document_id: v6veg7hn
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/7
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/feature/7
  lang: en
  template: aspx
  captured_at: '2009-07-10 03:39:15+00'
  capture_id: 815627
  wayback_url: https://web.archive.org/web/20090710033915id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/7
- document_id: v6veg7hn
  url: http://wizards.com/default.asp?x=mtgcom/feature/7,,fr
  page_key: wizards.com/default.asp?x=mtgcom/feature/7
  lang: en
  template: classic_asp
  captured_at: '2005-01-16 22:42:07+00'
  capture_id: 2022085
  wayback_url: https://web.archive.org/web/20050116224207id_/http://wizards.com/default.asp?x=mtgcom/feature/7,,fr
- document_id: v6veg7hn
  url: http://magic.wizards.com/en/node/634406
  page_key: magic.wizards.com/en/node/634406
  lang: en
  template: drupal
  captured_at: '2016-06-10 14:06:54+00'
  capture_id: 2523914
  wayback_url: https://web.archive.org/web/20160610140654id_/http://magic.wizards.com/en/node/634406
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: v6veg7hn
  capture_id: 191932
  url: https://magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
  wayback_url: https://web.archive.org/web/20240316093247id_/https://magic.wizards.com/en/news/feature/rules-primer-madness-2002-01-24
  captured_at: '2024-03-16 09:32:47+00'
  template: contentful
  sha256: 26d54eb07a22f6b0edd5d845f5dde4da466697b7d346af32892e96ba733b0025
render_recovery: []
---
Madness is one of the most complex abilities that the **Magic** R&D team has ever designed. Our task was to create an ability that would let you play a card whenever you discard it, allowed the spell to be countered, and didn’t let your opponent "mess" with the card you were going to play. To do this, we combined different types of effects into a single keyword ability.

<table><tbody><tr><td><br><i>The &quot;white board&quot; in R&amp;D during the design of madness</i></td></tr></tbody></table>

First, a replacement effect optionally removes the card from the game for a short time, keeping it safe from your opponent’s tricks. Then, a triggered ability lets you play the spell for its madness cost the next time you get a chance to play an instant. Finally, if you choose not to play the card after all, it’s put into your graveyard, so that it can count towards threshold.

Madness works no matter when or why you're discarding the card. You could discard to pay a cost, because a spell or ability tells you to, or even because you have too many cards in your hand at the end of your turn. In effect, madness gives you the opportunity to play creatures, enchantments, and sorceries when you would normally only be able to play instants. You can't discard a card with madness just because you want to, though.

To play a card with madness, say that you're playing the spell as soon as you discard it from your hand. Then, you get a chance to play instants and abilities (to generate the right kind of mana, for example). After that, playing a card with madness is just like playing an instant from your hand, except you pay the spell's madness cost instead of its mana cost. It goes on the stack like any other spell and it can be countered like any other spell. When it resolves, it goes into play (if it’s a creature or enchantment), or into your graveyard (if it’s an instant or sorcery).

When you play a card with madness, it still counts as being discarded, but it doesn't actually get to your graveyard before you play it. That means your opponent can't remove it "in response" to stop you from playing the spell with something like [Cremate](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cremate) or [Steamclaw](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steamclaw). Abilities such as [Megrim](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Megrim)'s and [Confessor](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confessor)'s that trigger on a card being discarded, however, will still trigger. If you choose not to play a card with madness when it's discarded, it goes to your graveyard. You don't get another chance to play it later.

Effects that cause you to pay more or less for a spell (such as [Nightscape Familiar](https://web.archive.org/web/20020124000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Nightscape%2BFamiliar) or [Feroz's Ban](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feroz%27s+Ban)) will cause you to pay that much more or less for its madness cost, too. That's because they affect the total cost of the spell, not just its mana cost.

### THE OFFICIAL WORD

For the brave, the official rules for the madness ability are as follows:

**502.24**. Madness

**502.24a** Madness represents two abilities. The first is a static ability of cards that functions while the card is in a player's hand. The second is a triggered ability that functions whenever the first ability is applied. The phrase "Madness \[cost\]" means "If a player would discard this card from his or her hand, that player discards it, but may remove it from the game instead of putting it into his or her graveyard," and "Whenever this card is removed from the game this way, until he or she passes next, he or she may play it any time he or she could play an instant as though it were in his or her hand by paying \[cost\] rather than paying its mana cost. When he or she passes next, he or she puts it into his or her graveyard."

**502.24b** Playing a spell using its madness ability follows the rules for paying alternative costs in rules 409.1b and 409.1f.

**502.24c** Any time you discard a card which has madness, you have the option to remove it from the game (to play it using its madness ability) or not. If you remove it from the game, the second part of the madness ability triggers. When this ability resolves, you have the option of playing the spell for its madness cost. You can only play it the very next time you could play an instant this turn. If it's an instant or sorcery, put it into your graveyard when it resolves. If it's an artifact, creature or enchantment, put it into play when it resolves.

### THE PLAY-BY-PLAY

For the very brave, let's go through a step-by-step example. This will be sort of a "slow-motion instant replay," and it is, I suspect, how **Magic** Online will handle the madness mechanic. This example is very complicated, and may confuse newer players or players without strong rules knowledge. To them I say this: Just remember to not put madness cards into the graveyard when you discard them. Hold on to them and say you are casting them with madness. Everyone should understand what you mean.

On with the example:

You have four cards in your hand – two copies of [Flametongue Kavu](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flametongue+Kavu) and two copies of [Fiery Temper](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Temper). You have one untapped [Mountain](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain) in play. Your opponent casts [Persecute](https://web.archive.org/web/20020124000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Persecute), targeting you.

You have no effects before Persecute resolves (since you can't cast anything), so it resolves, and your opponent chooses "red." Now you must discard all four of your cards.

The Flametongues do not have madness, so they go right into the graveyard. But Fiery Temper is a madness card, giving you the option (by rule 504.24c) to remove either or both from the game temporarily with a replacement effect. Regardless of whether you can actually cast the madness spells (or even if you want to), you can temporarily remove them from the game. If you choose not to, they go to the graveyard like the Flametongues did.

Let's say you remove both Fiery Tempers from the game. Now all four cards in your hand have been accounted for, and that's it for Persecute – it is considered fully resolved and should be placed in your opponent's graveyard. The next thing that happens is that the Fiery Tempers' madness triggered abilities go on the stack. Assuming no one has any effects once the triggers go on the stack, they will resolve.

The first time you get priority after a card's madness trigger resolves, you can cast the spell. This is, in fact, the only window you have to cast it. Once the first Fiery Temper trigger resolves, let's say you tap your Mountain and cast it for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) (its madness cost) at your opponent. The spell goes on the stack, then resolves, and your opponent takes three points of damage. That Fiery Temper goes to the graveyard like any normal instant.

Finally, the second Fiery Temper's madness trigger will resolve. You don't have the resources to cast it, so when you pass priority, it will also go to the graveyard.

Hopefully that makes sense! If you have further questions, feel free to ask the judges at your local prerelease this weekend.
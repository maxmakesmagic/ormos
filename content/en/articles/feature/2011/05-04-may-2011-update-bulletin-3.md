---
id: 841nsxbs
kind: article
lang: en
path: /en/articles/feature/2011/05-04-may-2011-update-bulletin-3
title: May 2011 Update Bulletin
published: '2011-05-04'
column_slug: feature
column: Feature
authors:
- slug: matt-tabak-25905907
  name: Matt Tabak
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?page=3&x=mtg/daily/feature/141a
    lang_detected: en
    capture_id: 173861
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/141a&page=3
    captured_at: '2011-08-10 02:49:34+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?page=3&x=mtg/daily/feature/141a
    lang_detected: en
    capture_id: 173861
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/141a&page=3
    captured_at: '2011-08-10 02:49:34+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?page=3&x=mtg/daily/feature/141a
    lang_detected: en
    capture_id: 173861
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/141a&page=3
    captured_at: '2011-08-10 02:49:34+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?page=3&x=mtg/daily/feature/141a
    lang_detected: en
    capture_id: 173861
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/141a&page=3
    captured_at: '2011-08-10 02:49:34+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: 841nsxbs
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/141a&page=3
  page_key: wizards.com/magic/magazine/article.aspx?page=3&x=mtg/daily/feature/141a
  lang: en
  template: aspx
  captured_at: '2011-08-10 02:49:34+00'
  capture_id: 173861
  wayback_url: https://web.archive.org/web/20110810024934id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/141a&page=3
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 841nsxbs
  capture_id: 173861
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/141a&page=3
  wayback_url: https://web.archive.org/web/20110810024934id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/141a&page=3
  captured_at: '2011-08-10 02:49:34+00'
  template: aspx
  sha256: eb629a303de593af15797551cab59cee68ca9b24a3850fc3b33fe7944d4deaea
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Liliana Vess
  - Goblin Caves
  - Goblin Shrine
  - Essence Leak
  - Lavamancer's Skill
  - Natural Selection
  - Portent
  - Crumbling Sanctuary
  - Bone Mask
  - Lightning Bolt
  - Skyshroud Forest
  - Star Compass
  - Fellwar Stone
  - Gloomwidow
  - Cloud Elemental
  - Leaping Lizard
  - Hyalopterous Lemure
  - Energy Storm
  - Delaying Shield
  - Nefarious Lich
  - Icy Prison
  - Oblivion Ring
  - Revelation
  - Wandering Eye
  - Defiant Stand
  - Veteran's Reflexes
  - Pure Intentions
  - Through the Breach
  - Gruesome Encore
  - Goblin Ringleader
  - Grave Defiler
  occurrences: 49
---
### Nonfunctional Oracle Changes

 **Liliana Vess**  
 Over the last few updates, we've been moving to the standard "from a graveyard" when talking about zone changes from a graveyard.

*New wording*  
 +1: Target player discards a card.  
 -2: Search your library for a card, then shuffle your library and put that card on top of it.  
 -8: Put all creature cards from all graveyards onto the battlefield under your control.

**Conditional effects: Goblin Caves, Goblin Shrine, Essence Leak, and Lavamancer's Skill**  
 If an ability continuously checks a condition to see whether it has a particular effect, we generally say "as long as" the condition is true. If the check is only performed at a specific time, such as whether a creature can attack or block, we still use "if."

*New Goblin Caves wording*  
 Enchant land  
 As long as enchanted land is a basic Mountain, Goblin creatures get +0/+2.

*New Goblin Shrine wording*  
 Enchant land  
 As long as enchanted land is a basic Mountain, Goblin creatures get +1/+0.  
 When Goblin Shrine leaves the battlefield, it deals 1 damage to each Goblin creature.

*New Essence Leak wording*  
 Enchant permanent  
 As long as enchanted permanent is red or green, it has "At the beginning of your upkeep, sacrifice this permanent unless you pay its mana cost."

*New Lavamancer's Skill wording*  
 Enchant creature  
 Enchanted creature has "{oT}: This creature deals 1 damage to target creature."  
 As long as enchanted creature is a Wizard, it has "{oT}: This creature deals 2 damage to target creature."

 **Natural Selection**  
 I thought it was im-Portent to line this up with Portent. Actually, that horrible pun reminds me to speak briefly about one reason to line up templates like this: it makes searching for certain rules text easier and more reliable. Oracle isn't always consistent about this, and we don't want to introduce needless functional changes, but it's worth it to tighten up when we can.

*New wording*  
 Look at the top three cards of target player's library, then put them back in any order. You may have that player shuffle his or her library.

**Simultaneous instructions: Crumbling Sanctuary & Bone Mask**  
 These two cards proved especially tricky. Here's the problem: let's say you control a Crumbling Sanctuary and your opponent cruelly aims a Lightning Bolt at your face. The Sanctuary prevents 3 damage, so you exile the top three cards of your library, right? Not exactly. The old wording could be interpreted such that there would be three instructions of "exile the top card of your library" being processed simultaneously. I believe this new wording clears up the functionality. If there are fewer cards in your library than the damage being prevented, you'll simply exile all the cards in your library.

*New Crumbling Sanctuary wording*  
 If damage would be dealt to a player, that player exiles that many cards from the top of his or her library instead.

*New Bone Mask wording*  
 {o2}, {oT}: The next time a source of your choice would deal damage to you this turn, prevent that damage. Exile cards from the top of your library equal to the damage prevented this way.

 **Skyshroud Forest**  
 The two mana symbols in the last ability were in the wrong order.

*New wording:*  
 Skyshroud Forest enters the battlefield tapped.  
 {oT}: Add {o1} to your mana pool.  
 {oT}: Add {oG} or {oU} to your mana pool. Skyshroud Forest deals 1 damage to you.

 **Star Compass**  
 This template was missing a "that" we use on several other cards, including Fellwar Stone.

*New wording*  
 Star Compass enters the battlefield tapped.  
 {oT}: Add to your mana pool one mana of any color that a basic land you control could produce.

 **Gloomwidow**  
 Gloomwidow has a blocking restriction, also seen on cards like Cloud Elemental, that is sometimes described as "high flying," so we opted not to use the same wording on the earthbound Gloomwidow. After consideration, we're going to line them up.

*New wording*  
 Reach  
 Gloomwidow can block only creatures with flying.

 **Leaping Lizard**  
 Several cards, including the adorable Hyalopterous Lemure, have a similar ability and reverse the order of the two bonuses, so Leaping Lizard should follow suit.

*New wording*  
 {o1oG}: Leaping Lizard gets -0/-1 and gains flying until end of turn.

 **Energy Storm**  
 When talking about the controller(s) of multiple creatures, we usually use the singular possessive if we can reasonably assume that the affected creatures will have the same controller. With cards like Energy Storm, it's more possible that multiple players will each control a creature with flying, so the plural possessive is used. There isn't a functional difference between the two (this is the nonfunctional changes section, after all).

*New wording*  
 Cumulative upkeep {o1} *(At the beginning of your upkeep, put an age counter on this permanent, then sacrifice it unless you pay its upkeep cost for each age counter on it.)*  
 Prevent all damage that would be dealt by instant and sorcery spells.  
 Creatures with flying don't untap during their controllers' untap steps.

 **Delaying Shield & Nefarious Lich**  
 These two cards both said "if you would be dealt damage," the only two cards to do so. We're adjusting it to the slightly more popular "if damage would be dealt to you."

*New Delaying Shield wording*  
 If damage would be dealt to you, put that many delay counters on Delaying Shield instead.  
 At the beginning of your upkeep, remove all delay counters from Delaying Shield. For each delay counter removed this way, you lose 1 life unless you pay {o1oW}.

*New Nefarious Lich wording*  
 If damage would be dealt to you, exile that many cards from your graveyard instead. If you can't, you lose the game.  
 If you would gain life, draw that many cards instead.  
 When Nefarious Lich leaves the battlefield, you lose the game.

 **Icy Prison**  
 The Oracle wording tried to return the "exiled creature" to the battlefield. It's not even a creature at that time. Weird. Let's try it Oblivion Ring-style:

*New wording*  
 When Icy Prison enters the battlefield, exile target creature.  
 At the beginning of your upkeep, sacrifice Icy Prison unless any player pays {o3}.  
 When Icy Prison leaves the battlefield, return the exiled card to the battlefield under its owner's control.

 **Revelation & Wandering Eye**  
 The use of "all" here seems unnecessary. The cards are very clear without it. Let the players play, player.

*New Revelation wording*  
 Players play with their hands revealed.

*New Wandering Eye wording*  
 Flying  
Players play with their hands revealed.

 **Defiant Stand**  
 *Portal* was trying to be helpful here, but checking to see if the creature was tapped before trying to untap it added unnecessary words to this card. Let's try the more modern template seen on Veteran's Reflexes.

*New wording*  
 Cast Defiant Stand only during the declare attackers step and only if you've been attacked this step.  
 Target creature gets +1/+3 until end of turn. Untap that creature.

 **Pure Intentions**  
 The second ability, which triggers off Pure Intentions itself being discarded, can only trigger once, so it should use "when."

*New wording*  
 Whenever a spell or ability an opponent controls causes you to discard cards this turn, return those cards from your graveyard to your hand.  
 When a spell or ability an opponent controls causes you to discard Pure Intentions, return Pure Intentions from your graveyard to your hand at the beginning of the next end step.

 **Through the Breach**  
 Like Gruesome Encore, this card should state that the creature gains haste, not just has it.

*New wording*  
 You may put a creature card from your hand onto the battlefield. That creature gains haste. Sacrifice that creature at the beginning of the next end step.  
 Splice onto Arcane {o2oRoR} *(As you cast an Arcane spell, you may reveal this card from your hand and pay its splice cost. If you do, add this card's effects to that spell.)*

 **Goblin Ringleader & Grave Defiler**  
 In a previous update, the other cards in this cycle from *Apocalypse* added a helpful "in any order" to the instruction to put cards on the bottom of your library. I'm not sure what these two cards were doing at the time, but they missed out. Fortunately, we have make-up day.

*New Goblin Ringleader wording*  
 Haste  
 When Goblin Ringleader enters the battlefield, reveal the top four cards of your library. Put all Goblin cards revealed this way into your hand and the rest on the bottom of your library in any order.

*New Grave Defiler wording*  
 When Grave Defiler enters the battlefield, reveal the top four cards of your library. Put all Zombie cards revealed this way into your hand and the rest on the bottom of your library in any order.  
 {o1oB}: Regenerate Grave Defiler.

* * *

> *   [Introduction](/en/articles/feature/2011/05-04-may-2011-update-bulletin-4)
> *   [Functional Oracle Changes](/en/articles/feature/2011/05-04-may-2011-update-bulletin)
> *   [Nonfunctional Oracle Changes](/en/articles/feature/2011/05-04-may-2011-update-bulletin-3)
> *   [Comprehensive Rulebook Changes](/en/articles/feature/2011/05-04-may-2011-update-bulletin-2)
---
id: anv069dr
kind: article
lang: en
path: /en/articles/faq/2004/01-22-darksteel-frequently-asked-questions
title: Darksteel Frequently Asked Questions
published: '2004-01-22'
column_slug: faq
column: FAQ
authors: []
detected_lang: en
unresolved_authors:
- FAQ
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/faq/darksteel
    lang_detected: en
    capture_id: 1817167
    url: http://www.wizards.com/default.asp?x=magic/faq/darksteel
    captured_at: '2005-03-25 09:23:02+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/faq/darksteel
    lang_detected: en
    capture_id: 1817167
    url: http://www.wizards.com/default.asp?x=magic/faq/darksteel
    captured_at: '2005-03-25 09:23:02+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/faq/darksteel
    lang_detected: en
    capture_id: 1817167
    url: http://www.wizards.com/default.asp?x=magic/faq/darksteel
    captured_at: '2005-03-25 09:23:02+00'
    rule: classic.byline
  column:
    page_key: wizards.com/default.asp?x=magic/faq/darksteel
    lang_detected: en
    capture_id: 1817167
    url: http://www.wizards.com/default.asp?x=magic/faq/darksteel
    captured_at: '2005-03-25 09:23:02+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: anv069dr
  url: http://www.wizards.com/default.asp?x=magic/faq/darksteel
  page_key: wizards.com/default.asp?x=magic/faq/darksteel
  lang: en
  template: classic_asp
  captured_at: '2005-03-25 09:23:02+00'
  capture_id: 1817167
  wayback_url: https://web.archive.org/web/20050325092302id_/http://www.wizards.com/default.asp?x=magic/faq/darksteel
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: anv069dr
  capture_id: 1817167
  url: http://www.wizards.com/default.asp?x=magic/faq/darksteel
  wayback_url: https://web.archive.org/web/20050325092302id_/http://www.wizards.com/default.asp?x=magic/faq/darksteel
  captured_at: '2005-03-25 09:23:02+00'
  template: classic_asp
  sha256: c9e6565ac94772a45f9c942b76836535c23444c1b0289300040e58415d8acca8
render_recovery: []
---
### Mechanics, rules, and card-specific discussions

* * *

*Compiled by Paul Barclay, David DeLaney, and Jeff Jordan*

[Darksteel FAQ in Rich Text format](https://web.archive.org/web/20040122000000/http://www.wizards.com/dci/downloads/DarksteelFAQ012204.rtf) (41k)

![](https://i.ormos.uk/51/91/5191b642b4e48c71fa3f59eaaa3aafa02adb759c44d7b300aeda11a85fa1cbd0.jpg)

This FAQ has two sections, each of which serves a different purpose.

The first section (["General Notes"](#general)) explains the new mechanics and concepts in the set. The second section (["Card-Specific Notes"](#cardspecific)) contains answers to the most important questions players might ask about a given card.

Items in the "Card-Specific Notes" section include full rules text for your reference. Not all cards in the set are listed.

* * *

### GENERAL NOTES

* * *

### Indestructible

"Indestructible" is not a keyword ability. It's just a word with a specific English meaning that's used as part of a permanent's abilities, like "unblockable." When an effect states that "\[this permanent\] is indestructible," it's stating a quality about that permanent, not giving it an ability. The official rules for indestructible (from the glossary of the Comprehensive Rules) are as follows:

Indestructible  
 If a permanent is indestructible, rules and effects can't destroy it. Such permanents are not destroyed by lethal damage and they ignore the lethal-damage state-based effect (see rule 420.5c). Rules or effects may cause the permanent to be sacrificed, put into a graveyard, or removed from the game.

**Darksteel Brute**  
![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)  
 Artifact  
 Darksteel Brute is indestructible. (*"Destroy" effects and lethal damage don't destroy it.*)  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif): Darksteel Brute becomes a 2/2 artifact creature until end of turn.

*   If an indestructible creature has 0 toughness, it will be put into its owner's graveyard. Being indestructible can't prevent this.
*   Damage accumulates on indestructible creatures, and that damage is removed during the cleanup step.
*   Lethal damage is defined as an amount of damage greater than or equal to a creature’s toughness. Even though an indestructible creature isn't destroyed by lethal damage, that definition is still used for things like assigning trample damage.
*   If a creature with lethal damage on it stops being indestructible, it's destroyed the next time state-based effects are checked.
*   Being indestructible stops only effects that would destroy the permanent, including destruction due to lethal damage and destruction that doesn't allow regeneration. An indestructible permanent can be removed from the game, returned to a player's hand, put into a graveyard, or sacrificed.
*   You can use a regeneration effect on an indestructible permanent, but since that permanent can't be destroyed, the effect will never apply.

* * *

### Modular

The modular ability applies at two times: as a creature with modular comes into play and when that creature leaves play. The official rules for modular (from the Comprehensive Rules) are as follows:

502.35. Modular

502.35a Modular represents both a static ability and a triggered ability. "Modular X" means "This permanent comes into play with X +1/+1 counters on it" and "When this permanent is put into a graveyard from play, you may put a +1/+1 counter on target artifact creature for each +1/+1 counter on this permanent."

502.35b If a creature has multiple instances of modular, each one works separately.

**Arcbound Bruiser**  
![5 Mana](https://i.ormos.uk/33/3c/333cbd82f68b5e306003b2955e517a94ffa7a3ea03087365c10afad540856dce.gif)  
 Artifact Creature  
 0/0  
 Modular 3 (*This comes into play with three +1/+1 counters on it. When it's put into a graveyard, you may put its +1/+1 counters on target artifact creature.*)

*   For the comes-into-play ability, the number of counters the permanent gets is equal to the number that follows "modular" on the card.
*   For the leaves-play ability, the number of counters on the permanent at the time it left play is what's relevant; the number after "modular" doesn't matter.
*   When a creature with modular leaves play, you may put the counters onto a single target artifact creature. You can't split them among two or more artifact creatures.

* * *

### Pulses

A cycle of five cards in the *Darksteel* set have the ability to return to a player's hand when they resolve if a stated condition is met. The Pulses are Pulse of the Dross, Pulse of the Fields, Pulse of the Forge, Pulse of the Grid, and Pulse of the Tangle.

**Pulse of the Dross**  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)  
 Sorcery  
 Target player reveals three cards from his or her hand and you choose one of them. That player discards that card. Then if that player has more cards in hand than you, return Pulse of the Dross to its owner's hand.

*   The condition is checked after all of the spell's other effects happen, so if the effect causes the condition to become false, the card won't return to its owner's hand.
*   The card returns to hand directly from the stack. It doesn't go to a graveyard at all.

* * *

### Echoing Spells

A cycle of five cards in the *Darksteel* set affect all permanents with the same name as their target. The Echoing cards are Echoing Calm, Echoing Courage, Echoing Decay, Echoing Ruin, and Echoing Truth.

**Echoing Calm**  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)  
 Instant  
 Destroy target enchantment and all other enchantments with the same name as that enchantment.

*   Four of the Echoing spells target a certain type of permanent and also affect all permanents \*of that type\* that have the same name as the target. Note that Echoing Truth is different: it targets a nonland permanent, but it affects all other permanents that have the same name, not just nonland permanents.
*   All of the permanents are affected at the same time.

* * *

### Imprint

The *Darksteel* set includes three cards with imprint abilities: Death-Mask Duplicant, Panoptic Mirror, and Spellbinder. Each of these cards has an entry in the "Card-Specific Notes" section of this FAQ. The official rules for imprint (from the Comprehensive Rules) are as follows:

502.34. Imprint

502.34a Imprint is a static ability, written "Imprint -- \[text\]." The phrase "Imprint -- \[ability\]" means "Cards in the removed-from-game zone that were removed from the game by this ability are imprinted on this permanent."

502.34b The phrase "imprinted \[type\] card" means the card of that type that's imprinted on the permanent. If a permanent has more than one card of that type imprinted on it, each of those cards is an "imprinted \[type\] card."

*   If you imprint a card on Panoptic Mirror or Spellbinder and that card has an additional cost, such as a kicker, buyback, or entwine cost, you can pay the additional costs for that card as you play it.
*   If you imprint a card on Panoptic Mirror or Spellbinder and that card has an alternative cost, such as "You may return an Island you control to its owner's hand rather than pay this spell's mana cost," you can't pay the alternative cost as you play the card, because you're already playing it without paying its mana cost.
*   If Panoptic Mirror or Spellbinder leaves play while its "play a copy of the imprinted card" ability is on the stack, its ability will use last known information to know what the imprinted card is. A copy of the card can be made, and it can be played as normal.
*   If the card imprinted on Panoptic Mirror or Spellbinder leaves the removed-from-game zone while the "play a copy of the imprinted card" ability is on the stack, there's no longer an imprinted card. A copy of the card can't be made in this case.

* * *

### Affinity

In addition to cards with affinity for artifacts, the *Darksteel* set includes a cycle of Golems with affinity for basic land types: Dross Golem, Oxidda Golem, Razor Golem, Spire Golem, and Tangle Golem.

**Dross Golem**  
![5 Mana](https://i.ormos.uk/33/3c/333cbd82f68b5e306003b2955e517a94ffa7a3ea03087365c10afad540856dce.gif)  
 Artifact Creature -- Golem  
 3/2  
 Affinity for Swamps (*This spell costs ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif) less to play for each Swamp you control.*)  
 Fear

See the [Mirrodin FAQ](/en/articles/faq/2003/09-23-mirrodin-frequently-asked-questions-2) for information about the affinity ability.

* * *

### Entwine

See the [Mirrodin FAQ](/en/articles/faq/2003/09-23-mirrodin-frequently-asked-questions-2) for information about the entwine ability.

* * *

### Equipment

See the [Mirrodin FAQ](/en/articles/faq/2003/09-23-mirrodin-frequently-asked-questions-2) for information about Equipment and the equip ability.

* * *

### CARD-SPECIFIC NOTES

* * *

**AEther Snap**  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)  
 Sorcery  
 Remove all counters from all permanents and remove all tokens from the game.

*   AEther Snap removes all counters from permanents, no matter what type they are. At the same time, it removes all tokens from the game.
*   Counters on objects that aren't permanents, such as delay counters on an Ertai's Meddling card that's removed from the game or poison counters on a player, are unaffected by AEther Snap.

* * *

**Arcbound Fiend**  
![6 Mana](https://i.ormos.uk/2d/12/2d12c8318f11a9188ce9fdd831b87ed97536df32e65841004ce583d399c4b454.gif)  
 Artifact Creature  
 0/0  
 Fear  
 At the beginning of your upkeep, you may move a +1/+1 counter from target creature onto Arcbound Fiend.  
 Modular 3 (*This comes into play with three +1/+1 counters on it. When it's put into a graveyard, you may put its +1/+1 counters on target artifact creature.*)

*   The creature that's targeted by Arcbound Fiend's middle ability doesn't have to have any +1/+1 counters on it. If it doesn't have a counter on it when the ability resolves, nothing happens.

* * *

Auriok Siege Sled {6} Artifact Creature 3/5 {1}: Target artifact creature blocks Auriok Siege Sled this turn if able. {1}: Target artifact creature can't block Auriok Siege Sled this turn.

*   Remember that in the **Magic**® game, an effect that says you "can't" do something overrides an effect that says you can or must do something. If you play both of Auriok Siege Sled's abilities on the same creature, that creature can't block Auriok Siege Sled this turn.

* * *

**Blinkmoth Nexus**  
 Land  
![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Add ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif) to your mana pool.  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif): Blinkmoth Nexus becomes a 1/1 Blinkmoth artifact creature with flying until end of turn. It's still a land.  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif), ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Target Blinkmoth gets +1/+1 until end of turn.

*   Blinkmoth Nexus gains the creature type "Blinkmoth" when it becomes a creature. This means that it ends up with three types (land, artifact, and creature), plus one creature subtype (Blinkmoth).
*   The "target Blinkmoth gets +1/+1" ability can target any creature with the creature type Blinkmoth.
*   If Blinkmoth Nexus is turned into a Forest after it's turned into a creature, it ends up with three types (artifact, land, and creature), plus one creature subtype (Blinkmoth) and one land subtype (Forest).

* * *

**Carry Away**  
![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)  
 Enchant Equipment  
 When Carry Away comes into play, unattach enchanted Equipment.  
 You control enchanted Equipment.

*   Carry Away is an enchant Equipment, which is a new subtype of local enchantments. An enchant Equipment can enchant only an Equipment (just as an enchant creature can enchant only a creature).
*   Normally, gaining control of an Equipment doesn't change what it's attached to. However, Carry Away has a triggered ability that unattaches the Equipment from whatever it's attached to. The Equipment's new controller can play its equip ability to move it onto a creature he or she controls.

* * *

**Death-Mask Duplicant**  
![7 Mana](https://i.ormos.uk/59/66/5966f494b39aae798102b737bdee28ed44a3bdfdaa8deb0f44fa798d7bf12603.gif)  
 Artifact Creature -- Shapeshifter  
 5/5  
 Imprint -- ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif): Remove target creature card in your graveyard from the game. (*The removed card is imprinted on this artifact.*)  
 As long as an imprinted creature card has flying, Death-Mask Duplicant has flying. The same is true for fear, first strike, double strike, haste, landwalk, protection, and trample.

*   Death-Mask Duplicant has an activated imprint ability. This ability can be played any number of times, so multiple creature cards can become imprinted on this creature.
*   Death-Mask Duplicant gains all landwalk and protection abilities of the imprinted creature cards. If Death-Mask Duplicant imprints a card with protection from red and a card with protection from creatures, it has protection from red and from creatures.

* * *

**Dismantle**  
![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)  
 Sorcery  
 Destroy target artifact. If that artifact had counters on it, put that many +1/+1 counters or charge counters on an artifact you control.

*   Dismantle targets only the artifact that will be destroyed. When Dismantle resolves, you choose which type of counters you want and choose an artifact you control to put them on.
*   It doesn't matter what kind of counters the destroyed artifact had on it, only how many. If an artifact had five bomb counters and two trap counters on it, that converts to seven +1/+1 counters or seven charge counters.
*   You can put +1/+1 counters on a noncreature artifact. They won't do anything unless the artifact becomes a creature, at which time they'll add to the creature's power and toughness.
*   If the artifact regenerates or is indestructible, it won't be destroyed, but you still put the appropriate number of counters onto an artifact you control.

* * *

**Fireball**  
![X Mana](https://i.ormos.uk/6b/b1/6bb1152b0a3305d0a7c2e2eb725b8ebd18620607efc62f6f38b0642b97c8501f.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)  
 Sorcery  
 Fireball deals X damage divided evenly, rounded down, among any number of target creatures and/or players.  
 As an additional cost to play Fireball, pay ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif) for each target beyond the first.

*   The additional cost is paid when you pay the rest of Fireball's costs, even though that text appears second on the card (to make the card easier to read). The additional cost doesn't count toward Fireball's converted mana cost.
*   If, for example, X is 5 and you choose three target creatures, Fireball has a total cost of {7}{R} and it deals 1 damage to each of those three creatures.

* * *

**Gemini Engine**  
![6 Mana](https://i.ormos.uk/2d/12/2d12c8318f11a9188ce9fdd831b87ed97536df32e65841004ce583d399c4b454.gif)  
 Artifact Creature  
 3/4  
 Whenever Gemini Engine attacks, put an attacking Twin artifact creature token into play. Its power is equal to Gemini Engine's power and its toughness is equal to Gemini Engine's toughness. Sacrifice the token at end of combat.

*   The Twin token comes into play as an untapped attacking creature. It's not subject to any costs to attack or restrictions on attacking.
*   The Twin token won't trigger any abilities that trigger "when \[a creature\] attacks."
*   The token's power and toughness are set equal to Gemini Engine's power and toughness. If there's a Glorious Anthem in play (which gives your creatures +1/+1), Gemini Engine is 4/5. The Twin token starts as a 4/5, and then the Anthem gives it +1/+1, making the Twin a 5/6 creature.
*   Once the token has been created, its power and toughness aren't dependent on Gemini Engine's power and toughness, and they won't change if Gemini Engine's power and toughness change.

* * *

**Heartseeker**  
![4 Mana](https://i.ormos.uk/36/29/3629288966daa042decf01d3752789ab6676fddd67c3679fa580cd3baecae158.gif)  
 Artifact -- Equipment  
 Equipped creature gets +2/+1 and has "![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif), Unattach Heartseeker: Destroy target creature."  
 Equip ![5 Mana](https://i.ormos.uk/33/3c/333cbd82f68b5e306003b2955e517a94ffa7a3ea03087365c10afad540856dce.gif) (*![5 Mana](https://i.ormos.uk/33/3c/333cbd82f68b5e306003b2955e517a94ffa7a3ea03087365c10afad540856dce.gif): Attach to target creature you control. Equip only as a sorcery. This card comes into play unattached and stays in play if the creature leaves play.*)

*   Heartseeker grants an ability to the equipped creature. The ability can target a creature with protection from artifacts (unless the equipped creature is an artifact creature).
*   The equipped creature's controller chooses whether or not to play the activated ability. It doesn't matter who controls Heartseeker.
*   "Unattach Heartseeker" means just that -- Heartseeker moves off the creature it was equipping and remains in play.

* * *

**Leonin Bola**  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)  
 Artifact -- Equipment  
 Equipped creature has "![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif), Unattach Leonin Bola: Tap target creature." Equip ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif) (*![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif): Attach to target creature you control. Equip only as a sorcery. This card comes into play unattached and stays in play if the creature leaves play.*)

*   Leonin Bola grants an ability to the equipped creature. The ability can target a creature with protection from artifacts (unless the equipped creature is an artifact creature).
*   The equipped creature's controller chooses whether or not to play the activated ability. It doesn't matter who controls Leonin Bola.
*   "Unattach Leonin Bola" means just that -- Leonin Bola moves off the creature it was equipping and remains in play.

* * *

**Leonin Shikari**  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)  
 Creature -- Cat Soldier  
 2/2  
 You may play equip abilities any time you could play an instant.

*   An equip ability uses the keyword ability "equip." Normally, equip abilities can be played only any time you could play a sorcery.
*   Leonin Shikari allows you to move your Equipment around during the combat phase or in response to a spell or ability. You're still subject to any other restrictions on playing equip abilities.

* * *

**Memnarch**  
![7 Mana](https://i.ormos.uk/59/66/5966f494b39aae798102b737bdee28ed44a3bdfdaa8deb0f44fa798d7bf12603.gif)  
 Artifact Creature -- Wizard Legend  
 4/5  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif): Target permanent becomes an artifact in addition to its other types. (*This effect doesn't end at end of turn.*)  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif): Gain control of target artifact. (*This effect doesn't end at end of turn.*)

*   The effects of Memnarch's abilities don't end at end of turn, and they don't end when Memnarch leaves play. Both effects last until the affected permanent leaves play.
*   You can use the first ability on a nonartifact permanent, wait for the ability to resolve, and then use the second ability on that permanent.

* * *

**Mycosynth Lattice**  
![6 Mana](https://i.ormos.uk/2d/12/2d12c8318f11a9188ce9fdd831b87ed97536df32e65841004ce583d399c4b454.gif)  
 Artifact  
 All permanents are artifacts in addition to their other types.  
 All cards that aren't in play, spells, and permanents are colorless.  
 Players may spend mana as though it were mana of any color.

*   Mycosynth Lattice turns all permanents in play into artifacts. Spells on the stack and cards in other zones aren't permanents, so those spells and cards don't become artifacts.
*   Mycosynth Lattice's second ability makes everything, in every zone of the game, colorless.
*   The Lattice's first ability causes local enchantments to become artifacts. Combined with March of the Machines from the Mirrodin set, this can then make those local enchantments become creatures. A local enchantment that's also a creature can't enchant anything. It's put into its owner's graveyard the next time state-based effects are checked.
*   The Lattice's third ability lets players spend even colorless mana as though it had a color. However, it doesn't remove restrictions on the mana. For example, Mycosynth Lattice doesn't allow mana from Vedalken Engineer to be used to play a nonartifact spell.

* * *

**Myr Landshaper**  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)  
 Artifact Creature -- Myr  
 1/1  
![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Target land becomes an artifact in addition to its other types until end of turn.

*   The land keeps all its other types, subtypes, and supertypes: If it was a basic land, it's still basic. If it was a Forest, it's still a Forest.

* * *

**Neurok Transmuter**  
![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif)  
 Creature -- Human Wizard  
 2/2  
![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif): Target creature becomes an artifact in addition to its other types until end of turn.  
![Blue Mana](https://i.ormos.uk/b7/5d/b75de4f4cec208d24e23ce112a4bb89540d55aa95fe1ef377d1c7c5d2b6bdb50.gif): Until end of turn, target artifact creature becomes blue and isn't an artifact.

*   Neurok Transmuter's second ability removes the type "artifact" -- and any artifact subtypes -- from the artifact creature it targets. It doesn't remove any other types or any subtypes of other types, and it doesn't remove supertypes. (If the artifact was legendary, it's still legendary, and the "Legend rule" applies normally.)
*   Equipment that stops being an artifact loses the subtype "Equipment." Permanents without the subtype Equipment can't equip creatures. (Of course, artifact creatures can't equip anything either.)
*   Neurok Transmuter's second ability interacts strangely with March of the Machines from the Mirrodin set. If an artifact is an artifact creature only because March of the Machines is in play and you then play Neurok Transmuter's second ability on that artifact creature, the result is a permanent with no types whatsoever. (Neurok Transmuter's ability removes the type "artifact." March of the Machines depends on knowing what is and isn't an artifact. The permanent won't be an artifact when March of the Machine's effect is applied and therefore it won't be turned into a creature.)

* * *

**Panoptic Mirror**  
![5 Mana](https://i.ormos.uk/33/3c/333cbd82f68b5e306003b2955e517a94ffa7a3ea03087365c10afad540856dce.gif)  
 Artifact  
 Imprint -- ![X Mana](https://i.ormos.uk/6b/b1/6bb1152b0a3305d0a7c2e2eb725b8ebd18620607efc62f6f38b0642b97c8501f.gif), ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): You may remove an instant or sorcery card with converted mana cost X in your hand from the game. (*That card is imprinted on this artifact.*)  
 At the beginning of your upkeep, you may copy an imprinted instant or sorcery card and play the copy without paying its mana cost.

*   As Panoptic Mirror's triggered ability resolves, it allows you to create a copy of one of the instant or sorcery cards imprinted on Panoptic Mirror in the removed-from-game zone (that's where the imprinted card is) and then play it without paying its mana cost.
*   You don't pay the spell's mana cost. If the spell has X in its mana cost, X is 0. You do pay any additional costs for that spell. You can't use any alternative costs.
*   The triggered ability triggers only once each upkeep, not once per imprinted card. If no cards are imprinted on Panoptic Mirror when the triggered ability resolves, it does nothing.
*   You may imprint a card on Panoptic Mirror in response to the upkeep-triggered ability. If you do, that card is available to copy when the triggered ability resolves.
*   Removing a card when the activated ability resolves is optional. If you choose to remove a card, you can remove only a card with converted mana cost equal to X.
*   To imprint a split card, you pay X equal to either side's converted mana cost. If the copied card is a split card, you choose which one side of it to play, but you can't play both sides. (You can choose the other side later in the game, though.)

* * *

**Rebuking Ceremony**  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif)  
 Sorcery  
 Put two target artifacts on top of their owners' libraries.

*   If both cards are owned by the same player, that player decides their order on top of his or her library.

* * *

**Savage Beating**  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)  
 Instant  
 Play Savage Beating only during your turn and only during combat.  
 Choose one -- Creatures you control gain double strike until end of turn; or untap all creatures you control and after this phase, there is an additional combat phase.  
 Entwine ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)

*   The additional combat phase is directly after the combat phase in which Savage Beating is played. There isn't a main phase between the two combat phases.

* * *

**Screams from Within**  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif)  
 Enchant Creature  
 Enchanted creature gets -1/-1.  
 When enchanted creature is put into a graveyard, return Screams from Within from your graveyard to play.

*   If Screams from Within returns to play from your graveyard, you choose the creature that Screams from Within enchants (just as you would for any local enchantment that you're putting into play without playing it). If your opponent doesn't control any creatures, you must choose one of your creatures. If there's nothing at all that Screams from Within can enchant, it remains in your graveyard.
*   If another player has gained control of Screams from Within, its triggered ability does nothing when it's put into a graveyard. Cards are always put into their owner's graveyard, but Screams from Within's ability looks for the card only in its controller's graveyard.

* * *

**Serum Powder**  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)  
 Artifact  
![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Add ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif) to your mana pool.  
 Any time you could mulligan and Serum Powder is in your hand, you may remove your hand from the game, then draw that many cards. (*You can do this in addition to taking mulligans.*)

*   You can use Serum Powder's second ability only while it's in your hand. If this card is in your hand, you can choose either to mulligan or to use Serum Powder's ability. Using the ability doesn't prevent you from taking further mulligans, and taking a mulligan doesn't prevent you from using a Serum Powder's ability if you happen to draw one.
*   Unlike a normal mulligan, Serum Power lets you draw the same number of cards that were in your hand, not one less. If you have already taken one mulligan and your hand contains six cards including a Serum Powder, you can choose to remove those six cards from the game and draw six new cards.
*   The hand is removed for the rest of the game; it isn't shuffled back into your library if you take another mulligan. (Cards removed from the game are always face up unless the effect that removed them says they aren't. Be sure to return those cards to your deck for your next game.)

* * *

**Slobad, Goblin Tinkerer**  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)  
 Creature -- Goblin Artificer Legend  
 1/2  
 Sacrifice an artifact: Target artifact becomes indestructible until end of turn. (*"Destroy" effects and lethal damage don't destroy that artifact.*)

*   Damage wears off simultaneously with this effect ending, so it does save an artifact creature from lethal damage.

* * *

**Spellbinder**  
 3  
 Artifact -- Equipment  
 Imprint -- When Spellbinder comes into play, you may remove an instant card in your hand from the game.  
 Whenever equipped creature deals combat damage to a player, you may copy the imprinted instant card and play the copy without paying its mana cost. Equip ![4 Mana](https://i.ormos.uk/36/29/3629288966daa042decf01d3752789ab6676fddd67c3679fa580cd3baecae158.gif)

*   Spellbinder's second ability allows you to create a copy of the imprinted instant card in the removed-from-game zone (that's where the imprinted instant card is) and then play it without paying its mana cost.
*   You don't pay the spell's mana cost. If the spell has X in its mana cost, X is 0. You do pay any additional costs for that spell. You can't use any alternative costs.
*   If the copied card is a split card, you choose which one side of it to play, but you can't play both sides. (You can choose the other side later in the game, though.)
*   Spellbinder imprints a card only once, when it comes into play. Attaching Spellbinder to a creature doesn't trigger its comes-into-play ability.

* * *

**Sundering Titan**  
![8 Mana](http://www.wizards.com/images/Symbols/Symbol_8_mana.gif)  
 Artifact Creature  
 7/10  
 When Sundering Titan comes into play, choose a land of each basic land type, then destroy those lands.  
 When Sundering Titan leaves play, choose a land of each basic land type, then destroy those lands.

*   Sundering Titan's two abilities aren't targeted. When one of the abilities resolves, the Titan's controller must choose one land for each basic land type (Plains, Island, Swamp, Mountain, and Forest).
*   If one of the basic land types isn't present, it isn't chosen. If the only land of a certain type is one you control, you must choose it.
*   If a land has more than one basic land type, it can be chosen more than once.
*   All the chosen lands are destroyed simultaneously.

* * *

**Surestrike Trident**  
![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)  
 Artifact -- Equipment  
 Equipped creature has first strike and "![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif), Unattach Surestrike Trident: This creature deals damage equal to its power to target player."  
 Equip ![4 Mana](https://i.ormos.uk/36/29/3629288966daa042decf01d3752789ab6676fddd67c3679fa580cd3baecae158.gif) (*![4 Mana](https://i.ormos.uk/36/29/3629288966daa042decf01d3752789ab6676fddd67c3679fa580cd3baecae158.gif): Attach to target creature you control. Equip only as a sorcery. This card comes into play unattached and stays in play if the creature leaves play.*)

*   Surestrike Trident grants an ability to the equipped creature.
*   The equipped creature's controller chooses whether or not to play the activated ability. It doesn't matter who controls Surestrike Trident.
*   "Unattach Surestrike Trident" means just that -- Surestrike Trident moves off the creature it was equipping and remains in play.

* * *

**Test of Faith**  
![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)  
 Instant  
 Prevent the next 3 damage that would be dealt to target creature this turn, and put a +1/+1 counter on that creature for each 1 damage prevented this way.

*   The +1/+1 counters are put onto the creature at the time the damage is prevented. If a 1/1 creature would be dealt 6 damage, 3 damage is prevented and three +1/+1 counters are put onto the creature. The creature is a 4/4 creature with 3 damage on it, so it won't be destroyed.

* * *

**Thought Dissector**  
![4 Mana](https://i.ormos.uk/36/29/3629288966daa042decf01d3752789ab6676fddd67c3679fa580cd3baecae158.gif)  
 Artifact  
![X Mana](https://i.ormos.uk/6b/b1/6bb1152b0a3305d0a7c2e2eb725b8ebd18620607efc62f6f38b0642b97c8501f.gif), ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Target opponent reveals cards from the top of his or her library until an artifact card or X cards are revealed, whichever comes first. If an artifact card is revealed this way, put it into play under your control and sacrifice Thought Dissector. Put the rest of the revealed cards into that player's graveyard.

*   You put the artifact card into play even if Thought Dissector has already left play and you can't sacrifice it.

* * *

**Thunderstaff**  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)  
 Artifact  
 If Thunderstaff is untapped and a creature would deal combat damage to you, prevent 1 of that damage.  
![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif), ![Tap](https://i.ormos.uk/bb/31/bb31ab0400c6bc497a5dfa0b4f8a1ccfb035016915dd04c1d5289fbc423245e5.gif): Attacking creatures get +1/+0 until end of turn.

*   If Thunderstaff is untapped, it prevents 1 damage from each creature, each time it would deal combat damage to you. So if three creatures with double strike attack you and aren't blocked, Thunderstaff will prevent a total of 6 damage.

* * *

**Trinisphere**  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)  
 Artifact  
 As long as Trinisphere is untapped, each spell that would cost less than three mana to play costs three mana to play. (*Additional mana in the cost may be paid with any color of mana or colorless mana. For example, a spell that would cost ![1 Mana](https://i.ormos.uk/6b/4c/6b4cf558eab279fb9414f146ebdd0e0705ec92984fec530597dd2a3bce43ce24.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif) to play costs ![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Black Mana](https://i.ormos.uk/e1/6b/e16bcf75cffdd1079b6ba1f9f43c9e6e7253bb89521acdf6b3e93d3c2e63dbb5.gif) to play instead.*)

*   Trinisphere's ability affects the total cost of the spell. It is applied *after* any other cost increasers or cost reducers are applied: First apply any cost increases. Next apply any cost reducers. Finally look at the amount of mana you have to pay. If it's less than three mana, you'll pay three mana.
*   Even with a cost reducer in play, spells can't cost less than three mana to play.
*   If a spell costs at least three mana due to additional costs, such as kicker costs, that's fine.
*   You still need to pay any additional nonmana costs the spell has, such as sacrificing a creature or discarding cards.
*   Playing a creature with morph face down already costs three mana, even though the converted mana cost of the face-down spell is zero, so Trinisphere normally doesn't modify the total cost of a face-down creature spell. However, if Dream Chisel is reducing that cost while Trinisphere is in play, you'll still have to pay three mana for the spell.

* * *

**Turn the Tables**  
![3 Mana](https://i.ormos.uk/7f/5d/7f5d2f1e55eaa9d19a9a23027b63bfbb5b39dbf8642160dda1a477a03df23a6a.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)  
 Instant  
 All combat damage that would be dealt to you this turn is dealt to target attacking creature instead.

*   If the targeted creature isn't in play when the combat damage would be dealt, the damage isn't redirected.
*   If the targeted creature has been removed from combat but is still in play, the damage will be redirected.

* * *

**Unforge**  
![2 Mana](https://i.ormos.uk/f9/cc/f9cc8a15b009997919d58ad79964384351495d1b6c9231f938316577453038a8.gif)![Red Mana](https://i.ormos.uk/86/2f/862ffc3d21299d18f0315a3f77721a10737fb394e147b0987204ef0496ce1060.gif)  
 Instant  
 Destroy target Equipment. If that Equipment was attached to a creature, Unforge deals 2 damage to that creature.

*   Unforge deals damage only to the creature that the Equipment was attached to when the Equipment was destroyed. It doesn't deal damage to creatures that the Equipment had previously equipped.

* * *

All trademarks, including character names, are property of Wizards of the Coast, Inc., in the U.S.A. and other countries. ©2004 Wizards.
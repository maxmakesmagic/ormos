---
id: vye6pgv7
kind: article
lang: en
path: /en/articles/feature/2008/09-24-september-2008-update-bulletin-5
title: September 2008 Update Bulletin
published: '2008-09-24'
column_slug: feature
column: Feature
authors:
- slug: markgottlieb
  name: Mark Gottlieb
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/other/092408
    lang_detected: en
    capture_id: 172332
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/092408&page=2&print=true
    captured_at: '2012-04-19 14:44:01+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/other/092408
    lang_detected: en
    capture_id: 172332
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/092408&page=2&print=true
    captured_at: '2012-04-19 14:44:01+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/other/092408
    lang_detected: en
    capture_id: 172332
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/092408&page=2&print=true
    captured_at: '2012-04-19 14:44:01+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/other/092408
    lang_detected: en
    capture_id: 172332
    url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/092408&page=2&print=true
    captured_at: '2012-04-19 14:44:01+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: vye6pgv7
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/092408&page=2&print=true
  page_key: wizards.com/magic/magazine/article.aspx?page=2&x=mtg/daily/other/092408
  lang: en
  template: aspx
  captured_at: '2012-04-19 14:44:01+00'
  capture_id: 172332
  wayback_url: https://web.archive.org/web/20120419144401id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/092408&page=2&print=true
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: vye6pgv7
  capture_id: 172332
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/092408&page=2&print=true
  wayback_url: https://web.archive.org/web/20120419144401id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/092408&page=2&print=true
  captured_at: '2012-04-19 14:44:01+00'
  template: aspx
  sha256: befdb80ad855fdc675dc2de1d6dec932e0feaad2d181ddb0b382b724f63b93cd
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Time Vault
  - Mana Vault
  - Fasting
  - Serra Avatar
  - Lake of the Dead
  - Master of Arms
  - Armor of Thorns
  - Goblin Welder
  - Cauldron Dance
  - Disharmony
  - Aurification
  - Freyalise's Winds
  - Temporal Distortion
  - Knowledge Vault
  - Triassic Egg
  - Hunting Pack
  - Krosan Vorine
  - Chartooth Cougar
  - Remove Enchantments
  - Cyclopean Tomb
  - Apocalypse Chime
  - City in a Bottle
  - Golgothian Sylex
  occurrences: 45
---
### Functional Oracle Changes

 **Time Vault**  
 The big one. Although its wording is superficially similar to Mana Vault, it's intended to work quite differently. If you decide to untap Time Vault during your untap step, you're supposed to skip *that turn*. The one you already started. Well, that doesn't work so well. There's sort of a rule that says you can't skip a turn you've already started. Not to mention all the other permanents that you didn't untap during the untap step in which you untapped Time Vault. But we know what it's supposed to do. It's supposed to let you funnel a turn into the Vault, which untaps it and saves that turn for later. How can we pull this off?

*New Oracle text:*  
 Time Vault comes into play tapped.  
 Time Vault doesn't untap during your untap step.  
 If you would begin your turn while Time Vault is tapped, you may skip that turn instead. If you do, untap Time Vault.  
 {oT}: Take an extra turn after this one.

This is... weird. Unprecedented. Scary. If I were the Rules Manager, I wouldn't let this go out the door. Hold on, I'm being informed that I am the Rules Manager. What I meant to say was that if I were sane, I wouldn't let this go out the door. Lucky for all of us, sanity is not an ailment that I suffer from. So we're going to give this a shot. This ability is getting a rule written specifically to support it: the untap is considered to be the first thing that happens during the next step that actually takes place (in case any triggered abilities or state-based effects care).

 **Fasting**  
 Let's look back to the printed wording. Here it is: "You may choose to skip your draw phase; if you do so, you gain 2 life. If you draw a card for any reason, Fasting is destroyed. During your upkeep, put a hunger counter on Fasting. When Fasting has five hunger counters on it, it is destroyed."

The printed wording said "destroy." The Oracle wording says "sacrifice." We can change it back. Also, the new Time Vault technology can get us closer to the original timing intent.

*New Oracle text:*  
 At the beginning of your upkeep, put a hunger counter on Fasting. Then destroy Fasting if it has five or more hunger counters on it.  
 If you would begin your draw step, you may skip that step instead. If you do, you gain 2 life.  
 When you draw a card, destroy Fasting.

 **Serra Avatar**  
 This card was printed with a triggered ability: "When Serra Avatar is put into a graveyard, shuffle Serra Avatar into owner's library." It currently has a replacement ability in Oracle: "If Serra Avatar would be put into a graveyard from anywhere, reveal Serra Avatar, then shuffle it into its owner's library instead." Why the switch? Because the replacement comes closest to matching the original functionality of the card. Under the rules system in place at the time Serra Avatar was printed, you couldn't respond to the triggered ability by playing another spell or ability that would remove Serra Avatar from the game or return it to play before it got shuffled in.

This is yet another case where original functionality faces off against printed wording. What's more important: preserving the way the card originally worked, or allowing the card to work as you'd expect if you simply picked it up and read it? It's a judgment call. In some cases (such as Lake of the Dead, Master of Arms, and Armor of Thorns), we place a premium on the original functionality because they'd be too overpowered, too underpowered, or too confusing if they worked as printed. In other cases, the printed wording works fine under the modern system and we're OK with letting the current rules gently sway how the cards work. We've decided that Serra Avatar falls into the latter category.

*New Oracle text:*  
 Serra Avatar's power and toughness are each equal to your life total.  
 When Serra Avatar is put into a graveyard from anywhere, shuffle it into its owner's library.

 **Goblin Welder**  
 Its current Oracle wording erroneously uses "the other artifact" to refer to an artifact *card* in a graveyard. Also, this card is trying to mimic an exchange, since its printed wording said to exchange a permanent with a card in a graveyard. This card won't be reverting to its printed wording, since an exchange shouldn't cause a permanent to go to the graveyard—it's not a sacrifice, it's not a destroy effect, and it's not a state-based effect. However, it may be able to get closer. Exchanges are simultaneous... so let's try that.

*New Oracle text:*  
 {oT}: Choose target artifact a player controls and target artifact card in that player's graveyard. If both targets are still legal as this ability resolves, that player simultaneously sacrifices the artifact and returns the artifact card to play.

 **Cauldron Dance**  
 I believe this is the only card that tells you to "put" a permanent into a graveyard. As discussed above, this is highly unorthodox. It's being changed to a sacrifice instead.

*New Oracle text:*  
 Play Cauldron Dance only during combat.  
 Return target creature card from your graveyard to play. That creature gains haste. Return it to your hand at end of turn.  
 You may put a creature card from your hand into play. That creature gains haste. Its controller sacrifices it at end of turn.

 **Disharmony**  
 This card's printed wording says "This creature is no longer considered to have attacked." That strongly implies that the creature should be removed from combat as part of the effect. If you target another player's creature, it's naturally removed from combat as part of the control-change effect. But if you target your own creature, Disharmony merely untaps it—it's still attacking! That needs to be fixed.

*New Oracle text:*  
 Play Disharmony only during combat before blockers are declared.  
 Untap target attacking creature and remove it from combat. Gain control of that creature until end of turn.

 **Aurification**  
 As printed, this card turned creatures into Walls, which rendered them unable to attack. Currently, it grants creatures defender, which renders them unable to attack. But there's no reason it can't *also* turn them into Walls, since that's what the card says it does.

*New Oracle text:*  
 Whenever a creature deals damage to you, put a gold counter on it.  
 Each creature with a gold counter on it is a Wall in addition to its other creature types and has defender. *(Those creatures can't attack.)*  
 When Aurification leaves play, remove all gold counters from all creatures.

 **Freyalise's Winds**  
 The printed wording of this card is "Whenever a permanent becomes tapped, put a wind counter on it. Permanents with any wind counters on them do not untap during their controller's untap phase; instead, remove all wind counters from those permanents." There are no line breaks... but *Ice Age* cards were real fuzzy with the line breaks. Because the second sentence references "permanents with any wind counters on them" (rather than referencing "that permanent" or the like), I think it's clear that the second sentence is a separate ability from the first sentence. Therefore, I don't think this card is supposed to grant abilities to permanents (as its current Oracle wording does); rather, I think this card is supposed to have the exact same wording as Temporal Distortion! (See the Nonfunctional Errata section for a minor update to Temporal Distortion's wording.)

*New Oracle text:*  
 Whenever a permanent becomes tapped, put a wind counter on it.  
 Permanents with wind counters on them don't untap during their controllers' untap steps.  
 At the beginning of each player's upkeep, remove all wind counters from permanents that player controls.

 **Knowledge Vault**  
 This card picked up an inexplicable "at end of turn" on its leaves-play ability that I tried to remove in the last Oracle update. It turns out that the addition was quite explicable: Without that addition, the card didn't work! Removing that text meant that sacrificing Knowledge Vault would cause the leaves-play trigger to put all the removed cards into the graveyard before the activated ability could put them into your hand.

I still don't like that "at end of turn," though, so I'm trying a different approach. Now, the sacrifice ability costs ![0 Mana](http://www.wizards.com/images/Symbols/Symbol_0_mana.gif), and you don't sacrifice Knowledge Vault until it resolves. However, that ability gives you the cards only if you actually sacrifice Knowledge Vault this way. You can't activate the ability, somehow return it to your hand (or otherwise make it leave play), and expect to get the cards. Also, if you activate the ability and someone tries to destroy Knowledge Vault in response (thus preventing you from being able to sacrifice it when the ability resolves), you can just activate the ability again in response. It costs ![0 Mana](http://www.wizards.com/images/Symbols/Symbol_0_mana.gif)! It's not exactly the same as intended, but it's really close—and, I believe, is closer than adding a delayed trigger to the other ability.

*New Oracle text:*  
 {o2}, {oT}: Remove the top card of your library from the game face down.  
 {o0}: Sacrifice Knowledge Vault. If you do, discard your hand, then put all cards removed from the game with Knowledge Vault into their owner's hand.  
 When Knowledge Vault leaves play, put all cards removed from the game with Knowledge Vault into their owner's graveyard.

 **Triassic Egg**  
 As originally printed in the *Legends* set, Triassic Egg didn't name what kind of counters to put on it. This was corrected when it was reprinted in *Chronicles* set; the card now instructed you to put hatchling counters on it. Somewhere along the way, this was changed in Oracle. The Oracle wording tells you to use incubation counters. These are pretty arbitrary names—no other card uses either hatchling counters or incubation counters—so I see no reason for the card not to match its printed functionality.

*New Oracle text:*  
 {o3}, {oT}: Put a hatchling counter on Triassic Egg.  
 Remove two hatchling counters from Triassic Egg, Sacrifice Triassic Egg: You may put a creature card from your hand or graveyard into play.

 **Hunting Pack**  
 In the creature type update, we changed this card so it produces Cat Beast tokens, because the art shows a Cat Beast and there are other Cat Beasts in *Onslaught* block (Krosan Vorine, Chartooth Cougar). But that was an unnecessary change. Hunting Pack itself doesn't stay in play, so its art doesn't need to be rigidly followed with regard to the creature type. This'll go back to producing Beast tokens, which is what the printed card says.

*New Oracle text:*  
 Put a 4/4 green Beast creature token into play.  
 Storm *(When you play this spell, copy it for each spell played before it this turn.)*

 **Remove Enchantments**  
 The printed card is bizarre, complex, and printed in tiny type. The Oracle wording is reasonably short, and quite simple. What's the secret? The Oracle wording ignores or changes half of what the card is supposed to do!

This is the result of the printed wording:

*   Enchantments you both own and control are put into your hand.
*   Auras that you own but don't control, and that are attached to permanents you control, are put into your hand.
*   Auras that you own but don't control, and that are attached to attacking creatures your opponents control, are put into your hand.
*   Auras that you don't own, but that are attached to permanents you control, are destroyed.
*   Auras that you don't own, but that are attached to attacking creatures your opponents control, are destroyed.
*   Enchantments you don't own but do control, and that haven't been covered by the last two bullet points, are destroyed.

This is the result of the Oracle wording:

*   Enchantments you both own and control are put into your hand. (Check!)
*   Auras that you own but don't control, and that are attached to permanents you control, are destroyed. (Wait, what? They're supposed to be returned to your hand!)
*   Auras that you own but don't control, and that are attached to attacking creatures you don't control, are destroyed. (Again, this should return them to your hand, and it shouldn't affect Auras attached to your teammate's attacking creatures.)
*   Auras that you don't own, but that are attached to permanents you control, are destroyed. (Check!)
*   Auras that you don't own, and that are attached to attacking creatures you don't control, are destroyed. (Not quite—this shouldn't affect Auras attached to your teammate's attacking creatures.)
*   Enchantments you don't own but do control, and that haven't been covered by the last two bullet points, are not affected. (And these are supposed to be destroyed.)

*New Oracle text:*  
 Return to your hand all enchantments you both own and control, all Auras you own attached to permanents you control, and all Auras you own attached to attacking creatures your opponents control. Then destroy all other enchantments you control, all other Auras attached to permanents you control, and all other Auras attached to attacking creatures your opponents control.

 **Cyclopean Tomb**  
 In the last update, Cyclopean Tomb got a new wording that allowed it to obey the rule that states that counters of the same name are indistinguishable. But it still had a problem. Once it leaves play, the upkeep triggers stick around forever. Say I play Cyclopean Tomb, put a mire counter on a land, then that Tomb is destroyed. During my next upkeep, I remove a mire counter from that land, so it's no longer a Swamp. Later, I play a different Cyclopean Tomb and put a mire counter on the same land (since it's hard to keep track of which land is which). During my next upkeep, the first Tomb's eternal triggered ability removes a mire counter from that land! Bad times. So this card is getting a tweak to its new wording. It's pretty brutal to read, but the upshot is that the card basically does what it says it does.

*New Oracle text:*  
 {o2}, {oT}: Put a mire counter on target non-Swamp land. That land is a Swamp as long as it has a mire counter on it. Play this ability only during your upkeep.  
 When Cyclopean Tomb is put into a graveyard from play, at the beginning of each of your upkeeps for the rest of the game, remove all mire counters from a land that a mire counter was put onto with Cyclopean Tomb but that a mire counter has not been removed from with Cyclopean Tomb.

 **Apocalypse Chime, City in a Bottle, Golgothian Sylex**  
 There are two issues with this trio.

1\. If a card's printed wording uses "cards" as a way to refer to permanents, we interpret that today as "nontoken permanents." (Tokens aren't cards.)

2\. City in a Bottle interprets the printed wording "discarded from play" as "sacrificed by its controller." Golgothian Sylex interprets the same printed wording as "destroy." The Sylex is being changed to match City in a Bottle's interpretation.

 *Apocalypse Chime's new Oracle text:*  
 {o2}, {oT}: Sacrifice Apocalypse Chime: Destroy all nontoken permanents from the Homelands expansion. They can't be regenerated.

 *City in a Bottle's new Oracle text:*  
 Whenever a nontoken permanent from the Arabian Nights expansion other than City in a Bottle is in play, its controller sacrifices it.  
 Players can't play cards from the Arabian Nights expansion.

 *Golgothian Sylex's new Oracle text:*  
 {o1}, {oT}: Each nontoken permanent from the Antiquities expansion is sacrificed by its controller.

[Introduction](/en/articles/feature/2008/09-24-september-2008-update-bulletin-3)  
 [Functional Oracle Changes](/en/articles/feature/2008/09-24-september-2008-update-bulletin-5)  
 [Nonfunctional Oracle Changes](/en/articles/feature/2008/09-24-september-2008-update-bulletin-4)  
 [Comprehensive Rules Changes](/en/articles/feature/2008/09-24-september-2008-update-bulletin-2)
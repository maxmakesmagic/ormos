---
id: jtx8ntr1
kind: article
lang: en
path: /en/articles/uncategorised/undated/magic-duels-patch-notes
title: Magic Duels Patch Notes
published: null
column_slug: uncategorised
column: uncategorised
authors: []
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/node/865031
    lang_detected: en
    capture_id: 2529987
    url: http://magic.wizards.com/en/node/865031
    captured_at: '2016-06-12 17:40:12+00'
    rule: meta.og_title
sources:
- document_id: jtx8ntr1
  url: http://magic.wizards.com/en/node/865031
  page_key: magic.wizards.com/en/node/865031
  lang: en
  template: drupal
  captured_at: '2016-06-12 17:40:12+00'
  capture_id: 2529987
  wayback_url: https://web.archive.org/web/20160612174012id_/http://magic.wizards.com/en/node/865031
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: jtx8ntr1
  capture_id: 2529987
  url: http://magic.wizards.com/en/node/865031
  wayback_url: https://web.archive.org/web/20160612174012id_/http://magic.wizards.com/en/node/865031
  captured_at: '2016-06-12 17:40:12+00'
  template: drupal
  sha256: 6f3c61148d8d83b15cf564f29d4aefca50c7e9aa9ebea9a8470918213dd611ae
render_recovery:
- code: broad_content_selector
---
## Magic Duels

# New Features

*   Awards for Two-Headed Giant

*   Player will receive coins for 2HG when defeating random opponents.

*   In versus Battle Mode, a player whose opponent concedes is awarded coins and rank immediately, and is informed via in-game message that their opponent has conceded. That player is then offered a choice:
    *   Win and end the duel, or
    *   Continue playing vs. AI
*   A global rollover time defined by a set 24-hour period is implemented. 12 a.m. UTC is the rollover time for everyone globally, and the countdown indicates that to the player via a countdown.
*   Deck selection defaults to the last-played or last-edited deck (if nothing has been played this session).
*   Improvements for targeting individual cards.
*   Stack moved off the battlefield to make targeting permanents easier.
*   Improvements for targeting correct land.
*   While browsing a selection of cards that can individually be zoomed, the user is able to move to the next or previous card in the selection while remaining in the zoom state.
*   On the Booster Purchase screen, there is an indicator displaying the percentage of owned cards for the set.
*   New highlight states for playing a card:
    *   Orange: The default highlight should trigger under the same circumstances as it currently does. It indicates that you can play this spell or use an activated ability—or more generally that you can do something with the card.
    *   Blue: Can be played in an unusual way. Typically this will be displayed when a card can be cast using an alternative cost (surge, awaken, or madness). Overrides the other highlights.
    *   White: The card is relevant to what you've got selected (e.g. this will be tapped for mana, or this has been chosen as a target). Overrides the other highlights.
*   Ability to minimize in-game windows for players to check the battlefield when making choices via dialogue boxes.

# General Bug Fixes

*   Fixed issue with AI playing similar decks on Hard.
*   Fixed issue with a card not being returned to the user's hand from the graveyard when using Greenwarden of Murasa's "on-death" ability.
*   Fixed issue with Ulamog, the Ceaseless Hunger's "on-attack" ability not triggering when you attack a planeswalker your opponent controls.
*   Fixed issue with users being unable to purchase boosters from the store.
*   Quests not updating every 24 hours for some users has been fixed.
*   Fixed issue with quests not being present.
*   Fixed issue where the game will crash and the user will be unable to reconnect if quotation marks (") are used in the name of a deck created with the deck builder.
*   Fixed issue when user opens a booster and the game crashes or disconnects, causing the user to spend coins but not receive cards.
*   Fixed issues with users seeing adverts appearing too often.
*   Fixed a crash in Nissa's Battle for Zendikar campaign story.
*   Fixed issue with the large vine attack animation displaying behind the avatar.
*   Fixed several Two-Headed Giant connectivity issues.
*   Fixed "Shadows of the Past" scry dialog appearing off screen when multiple cards are in play.
*   Fixed issue with Lys Alana Scarblade's activated ability counting ALL Elves in play and not just the Elves the player controls.
*   Fixed issue with the game asking you how many colors of mana you want to use to cast Skyrider Elf, but not asking how much mana you want to spend to cast it.
*   Fixed issue with the land being automatically played when a player zooms in on a land card during the Evolving Wilds selection phase.

# iOS Bug Fixes

*   Fixed issue with the client causing a multiplayer duel to crash when the user receives a phone call.
*   Fixed issue with user being unable to connect a second new Game Center account.

# All Current Known Issues

*   No animation is shown when earning coins by playing random Two-Headed Giant matches. Coins are still correctly awarded.
*   Priority is no longer held when the only cards and abilities a player can play are instant-speed. In this situation, the game skips to beginning of combat ("Attack") and the beginning of the end phase ("End").
*   Transformed double-faced cards are treated as having no mana cost and a converted mana cost of 0 instead of the cost of their front side, as they should per the Shadows over Innistrad rules update.
*   Awakened lands are able to attack without paying the appropriate mana cost when a player has Archangel of Tithes on the battlefield.
*   A user cannot cancel the mana cost prompt and is forced to pay twice when attacking a player who controls Archangel of Tithes and letting the turn timer run out.
*   Kalitas, Traitor of Ghet incorrectly creates a 2/2 Zombie token when an opponent's creature is exiled by Touch of the Void.
*   When blocking an attack against a Planeswalker then withdrawing the blocker, the attacking creature appears to be attacking the player instead. It still deals combat damage to the Planeswalker.
*   An unrecoverable desync occurs when a player lets the turn timer expire after choosing to attack an opponent, does not confirm the attack, has one Archangel of Tithes on the battlefield and no other creatures. The mana requirement to attack or block when an Archangel of Tithes is on the battlefield is paid automatically, and shortly after both devices enter an unrecoverable desync.
*   After minimizing the prompt of the Discard phase, an orange action line will be present on the battlefield.
*   The Mana Cycle prompt displays the opponent's avatar highlight instead of a card selection highlight.
*   Tapped land abilities cannot be activated by right-clicking on them. A 'System Busy' prompt appears even though it is the user's turn and the user can activate the ability legally.
*   If the user disconnects from a ranked duel and wins the duel offline, they will see they gained a rank until they reboot the title. Upon reboot, the user will again see the correct rank.
*   In Two-headed giant, after 25 cards are put into the right-hand player's graveyard, additional cards will start showing up in the left-hand player's graveyard.
*   Quest progress from the conceded duel is not updated and carries over into the next match played.
*   Quest progress is counted after a Solo Battle, but not immediately after a Campaign duel.
*   In very rare occasions, the AI will split damage between the user and their Planeswalker using multi-target damage spells.The damage is dealt to both the user and the user's Planeswalker.
*   After disconnecting a second controller, the dialogue prompt cannot be dismissed by the first player. Player 1 cannot dismiss the dialogue box and is forced to either kill the game or reconnect the second controller.
*   There is no 'More Info' entry for investigate.
*   Eldrazi Mimic does not change its power/toughness to equal the other creature's power and toughness if the power/toughness is changed due to other spells or abilities when Eldrazi Mimic's ability resolves. Eldrazi Mimic only gains the power/toughness of what is printed on the other creature card.
*   Ranked Versus messaging for Conceding/Opponent Conceding appears in Invite Versus matches.The prompts display information as if the duel was a ranked Versus Battle (Versus Battle with a Matched Opponent).
*   Matchmaking two local teammate teams will create unexpected results when conceding. When playing against an AI opponent that has replaced a random human opponent, coins are awarded only if the remaining team wins.
*   In the third node of the Nissa's Oath of the Gatewatch campaign, Coal Stoker produces three floating red mana when cast from the hand. If the user has an instant in hand that could be cast using this floating mana, the user is unable to cast the instant because the phase changes too quickly for the user to cast the spell or to stop the timer. This results in the mana disappearing unused.
*   Origin Creatures transforming into Planeswalkers do not trigger Oath of Chandra's ability.
*   Flameblade angel auto-resolve can result in a loop of 1 damage until a player dies.
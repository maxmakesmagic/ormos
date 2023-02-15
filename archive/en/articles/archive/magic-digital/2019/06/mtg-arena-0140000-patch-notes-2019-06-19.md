
---
[Link to Wayback Machine](https://web.archive.org/web/20201112043145/https://magic.wizards.com/en/articles/archive/magic-digital/mtg-arena-0140000-patch-notes-2019-06-19)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "War of the Spark All 264 cards from War of the Spark are now available in Magic: The Gathering Arena. This includes the buy-a-box promo as well as cards in the Jace and Gideon planeswalker decks. Redeem the code `PlayWarSpark` for three War of the Spark booster packs in-game!"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1437626"
[_metadata_:path_date]:- "2019-06-19"
[_metadata_:publish_date]:- "2019-04-25"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "MTG Arena: 0.14.00.00 Patch Notes"
[_metadata_:wayback_capture_timestamp]:- "2020-11-12 04:31:45"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201112043145id_/https://magic.wizards.com/en/articles/archive/magic-digital/mtg-arena-0140000-patch-notes-2019-06-19"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/magic-digital/mtg-arena-0140000-patch-notes-2019-06-19"
---


MTG Arena: 0.14.00.00 Patch Notes
=================================



 Posted in **Magic Digital**
 on April 25, 2019 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast












War of the Spark
================


* All 264 cards from *War of the Spark* are now available in Magic: The Gathering Arena. This includes the buy-a-box promo as well as cards in the [Jace and Gideon planeswalker decks](https://magic.wizards.com/en/articles/archive/card-preview/war-spark-planeswalker-deck-lists-2019-04-18).
* Redeem the code "PlayWarSpark" for three War of the Spark booster packs in-game!
	+ **IMPORTANT NOTE:** Please be sure to download the update before you try to redeem the code!
	+ MTG Arena Boosters (8-cards) are NOT guaranteed to have a planeswalker.
	+ MTG Arena Limited Boosters (14-cards in Draft/Sealed events) WILL each have a planeswalker.
* New War of the Spark themed battlefield, located on the top of Bolas's Citadel.
* New VFX have been added for each Mythic card in War of the Spark.
* New VFX for new mechanics Amass and Proliferate.
* For more information, please refer to our [War of the Spark MTG Arena Release Notes](https://forums.mtgarena.com/forums/threads/55090).

Twitch Prime Promotion
======================


* Beginning on April 25, 2019 at 11AM PT, Twitch Prime users can redeem a code for one (1) 60-card Boros Legion deck in Magic: The Gathering Arena ("MTG Arena").

Gameplay
========


Planeswalkers
-------------


* When selecting "Attack with All" with an opposing planeswalker on the field, you will now be prompted to select a target for all of the attackers rather than implicitly declaring them all as attacking the opponent.
* Planeswalkers now indicate whether they have an activation left for the turn.
* When selecting whether to attack a player or planeswalker, you can also select additional attackers to declare all of their attacks in a batch.
* When a Planeswalker has used all of their ability activations for the turn, their loyalty box will now grey out.
* Planeswalkers that become creatures (or other permanent types) will visually retain their loyalty counters. These are shown in the normal counter location and using the normal loyalty frame.

Auto-Tap
--------


* Auto-Tap should now be smarter when dealing with sources that can tap for colorless and have another mana ability
* AutoTap should now be smarter when calculating what actions it should leave mana available for (e.g. [Azcanta, the Sunken Ruin](https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=435226))
* AutoTap should now be smarter when tapping sources that produce mana with a spending restriction (e.g. [Unclaimed Territory](https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=435419), [Interplanar Beacon](https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=461174))
* We've added a new, fully optional way for AutoTap to help you pay for spells and abilities. Any time that you need to pay mana and AutoTap isn't handling it automatically (Convoking, sacrificing a treasure token, because you have AutoTap turned off, etc), there is now a new button for you to tell AutoTap to pay the cost for you.
	+ Hovering over this button will show what AutoTap will use, including any creatures tapped, treasure sacrificed, etc. Clicking the button will pay the cost, including doing things like sacrificing treasure (that AutoTap won't usually do)
	+ ![0392005b566d26a3e93018b1bd158b5136500c7c](https://s3.amazonaws.com/duxsite-mtgarena/0392005b566d26a3e93018b1bd158b5136500c7c370a99a985da5972a99d2984u46.png)

User Interface
--------------


* Cards that can't be countered are now shown with a flowing, red border while on the stack.
* When prompting for an optional action, the prompt will now be phrased as a question (e.g. "Discard a card?")
* When a card or effect allows 0 or more targets/selections, the "Submit" button is now blue when less than the maximum number of have been made, changing to orange when the max have been targeted/selected.
	+ Note: This doesn't change when you can legally submit, but should hopefully clarify when there are targets/selections left to make.
* When there is an effect on the stack that needs targets or selections, and there are valid selections beneath the stack, the stack now auto-collapses so players can clearly see all targets/selections.
	+ Note: You can still use the collapse/show button for the stack as normal to show and re-hide it.
* When players or planeswalkers are affected by damage prevention effects they now show this similarly to creatures; players have a glow around their life total, while planeswalkers have the glow around their loyalty counter.
* Cards affected by "can't activate" or "can't be activated" effects have a hanger indicating the effect and the source.
* Cards display a new badge for cards that care about the count or number of various objects that shows the appropriate count.
	+ For something like Dreadhorde Butcher ("When Dreadhorde Butcher dies, it deals damage equal to its power to any target.") the on-death trigger has a badge showing the Butcher's power when it dies.
	+ If a card that cares about instants or sorceries in your graveyard it shows the count of those.
	+ ![6d4393dab641ad8d7237d1c931e9a9dddc4596c6](https://s3.amazonaws.com/duxsite-mtgarena/6d4393dab641ad8d7237d1c931e9a9dddc4596c6c6031a9923077ec8d9d8f0aeu46.png)
* When there is a stack of creatures assigned as blockers and you are trying to target one of them, you can hover over the stack to fan it out, making it much easier to target the specific blocker you want in the stack. (With a stack of blockers, damage is dealt top-to-bottom.)
* When removing counters from a permanent (such as through Soul Diviner or Price of Betrayal), we show a new browser allowing the player to select the counter(s) they wish to remove.
	+ Click on a counter on the list to select it for removal.
	+ If the effect allows removing multiple counters, the counters that will be removed are move off to the left.
	+ If you change your mind, you can click on a counter on the left to cancel removing that one
* Cards that can't be played (due to effects like Experimental Frenzy or similar) now have a hanger in mouse-over that indicates that they can't be cast and lists the source.
	+ ![221f54e34197bc99c8029f3427438b5ec25879e3](https://s3.amazonaws.com/duxsite-mtgarena/221f54e34197bc99c8029f3427438b5ec25879e37eef383c7f27ac2620c2e582u46.png)
* We've changed the way we represent cards that "can be targeted as if they don't have hexproof"; now those cards will simply not show the hexproof VFX (though they will still show the Hexproof hanger on mouse over).
* When activating Blast Zone, we show the number of counters it had on it on the stack as well, so players know what CMC of permanents will be destroyed.
* When a permanent is copying another, we now show the original permanent as well in mouse-over, similar to how both sides are shown for a double-faced card.
* When you have exiled a card that you would normally be able to cast but can't due to its type (for example, you had to select a land with Thief of Sanity), it will no longer show up in your near-hand castables for you. (Your opponent will still see a cardback representing the possible cast, since they don't know what card you exiled.)

Events
======


* Special events (Momir, Pauper, Singleton, etc.) will now use matchmaking rating in addition to Win/Loss record.
	+ Win/Loss record is still the primary matchmaking criteria.
* The following cards are now banned in Ravnica Constructed:
	+ Gates Ablaze
* The following cards are now banned in Cascade Constructed:
	+ Lavinia, Azorius Renegade
	+ Nexus of Fate
	+ Teferi, Time Ravele
* Games in all Sealed and Draft events will use the battlefield associated with that set.
* Various updates to Draft bots

Cosmetics
=========


Card Styles
-----------


The following card styles are now available for direct purchase:




| Shivan Fire | DOM |
| Memorial to Genius | DOM |
| Nexus of Fate | M19 |
| Exclusion Mage | M19 |
| Surge Mare | M19 |
| Diamond Mare | M19 |
| Root Snare | M19 |
| Moment of Craving | RIX |
| Kaya's Wrath | RNA |
| Wilderness Reclamation | RNA |
| Hero of Precinct One | RNA |
| Drill Bit | RNA |
| Benthic Biomancer | RNA |
| Essence Capture | RNA |
| Cindervines | RNA |
| Dragonskull Summit | XLN |
| Sorcerous Spyglass | XLN |
| Kumena's Speaker | XLN |

Practice Matches
================


* Sparky will now comment on the board state and reply to player emotes

Miscellaneous
=============


* Updated the icon used for the MTGA Installer.

Bug Fixes
=========


* Hitting the "Escape" key now properly closes the Options menu.
* Card styles should no longer "jitter" when progressing through turn phases.
* Card sleeves should now correct display when you reconnect to a match.
* Players will no longer need to scroll to see the "Custom" option under Graphic → Quality Level.
* Simultaneously conceding a best-of-three match as you took lethal damage should no longer result in multiple game losses.
* Fixed some improper targeting that could occur when multiple permanents entered the battlefield simultaneously and one of them was an aura or a creature who enters as a copy.
* Fixed a rare bug that could cause the client to misrepresent the revealed cards in the opponent's hand, potentially hiding other, non-revealed cards
* Fixed a bug that could cause Ghalta to not properly update its casting cost when an opponent's copy is exiled face down and castable.







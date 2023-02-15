
---
[Link to Wayback Machine](https://web.archive.org/web/20150221074127/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-bug-blog-february-19-2015)

[_metadata_:author]:- "David Whitfield"
[_metadata_:description]:- "What Is the Magic Online Bug Blog?"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "draft"
[_metadata_:publish_date]:- "2015-02-19"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Magic Online Bug Blog February 19, 2015"
[_metadata_:wayback_capture_timestamp]:- "2015-02-21 07:41:27"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150221074127id_/http://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-bug-blog-february-19-2015"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-bug-blog-february-19-2015"
---


Magic Online Bug Blog February 19, 2015
=======================================



 Posted in **Magic Online**
 on February 19, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_davidwhitfield.jpg)
By David Whitfield










 



What Is the *Magic Online* Bug Blog?


While the [Known Issues List](http://magic.wizards.com/en/content/magic-online-known-issues) is simply that—a running list of issues we expect players to encounter most often—this accompanying “Bug Blog” is the list’s companion. Here you’ll find updates regarding emergent new issues, details around issue statuses when applicable, known issue workarounds, and a running tally of Known Issues List updates. The Bug Blog will be updated each week, in conjunction with the [Known Issues List](http://magic.wizards.com/en/content/magic-online-known-issues) on the same day.


**Quick Links**

[Download *****Magic Online*****](http://magic.wizards.com/en/content/download ) 

* [Known Issues List Updates](#updates)
* [Temporary Workarounds for Known Issues](#workarounds)



 




---

**Known Issues List Updates**


A cornucopia of fixes were deployed to *Magic Online* in the Wednesday, February 18 build! We've also added two new bugs, along with temporary workarounds, to the Known Issues List. Check out the list below for a break-down of what's new since last week's Bug Blog. Refer to the [Known Issues List](http://magic.wizards.com/en/content/magic-online-known-issues) for the most current *Magic Online* Known Issues.




---

**Newly Added Known Issues as of Thursday, February 19**


**Game Play**



* FRF | Archfiend of Depravity’s user interface needs to be updated


**Client**



* Duel Scene | Cancellation message appears if user does not return to play lobby after a duel has concluded




---

**Fixed during the Wednesday, February 18 *Magic Online* Client Update**


**Game Play**



* C13 | Marath, Will of the Wild can no longer be activated for 0
* C14 | Gideon Jura +2 ability no longer gives an illegal attack message preventing the game from continuing when Gideon is enchanted by Song of the Dryads
* C14 | If you make a copy of Stoneforged Blade, it no longer equips automatically when entering the battlefield
* FRF | "Cast with Dash" text should now appears when on stack but not once on battlefield
* FRF | If an attacking dragon is removed before Silumgar's trigger resolves, opponent's creatures now get -1/-1
* FRF | Lightform, and similar effects, now give blue rules text to all players indicating 'Flying' if the manifested creature already has flying on the face-down side
* FRF | Manifesting an aura with Write into Being prompts the user to attach auras properly. This no longer stops the game from proceeding
* General | A delayed triggered ability that targets a manifest/morph card will now display correct text while on the stack
* General | Advocates, such as Nullmage Advocate, that return multiple cards to opponent's hands can now be activated
* General | Cards with a trigger when opponent causes player to discard them, such as Guerilla Tactics, now properly trigger
* General | Chasm Skulker and Consecrated Sphinx's triggered abilities no longer believe themselves to be targeted effects
* General | Coalition Relic now allows a player to pick a color of mana when controlling another player's turn
* General | In the case where a creature has a negative power, Phthisis now properly adds negative power to the toughness of the destroyed creature to determine the life loss
* General | Manifest creatures now gain visual indication of new type or subtypes if they are granted
* General | Morphs on the stack are now revealed to opponents when the game ends
* General | Naming/choosing cards, such as with Pithing Needle, now correctly appears in game log
* General | Show and Tell's prompt is no longer able to be skipped with F2 to prevent players from accidentally missing their chance to put a card into play
* General | Sunburst cards with mana costs in activated abilities now display correctly when activated
* General | Targeting with Mind Bend and similar effects no longer causes the game to not continue
* General | We have cleaned up a number of corner cases around Spirespine (and other 'Must Block' creatures) giving illegal blocker error if it doesn't block
* General | You can no longer use both halves of split cards to pay a total of 2 mana for Delve costs
* JOU | Setessan Tactics' granted ability is no longer allowing creatures to target and fight themselves
* KTK | Crackling Doom now forces the sacrifice of a creature when the opponent's greatest power among creatures is negative
* KTK | Heart-Piercer Bow now deals damage if equipped creature is removed with trigger on stack
* KTK | Meandering Towershell no longer returns if exiled/destroyed in response to exile trigger
* KTK | Ride Down now properly grants trample if the blocking creature regenerates
* KTK | Villainous Wealth now properly works for cards which reference a creature an opponent controls
* M15 | Jace, the Living Guildpact no longer allows you to leave both cards on top of your library
* M15 | Xathrid Slyblade now loses Hexproof after activating its ability
* MMA | Kira, Great Glass Spinner now counts all spells and abilities, not just spells and abilities since you controlled the creature
* VMA | Carnophage now respects the choice made by its controller no longer causing its controller to lose 1 life regardless of option selected
* VMA | If two Volrath's Shapeshifters copies the same legend, the game no longer restarts and the client no longer crashes


**Card Look and Feel** 



* General | Copies of manifest token creatures now display proper artwork
* General | Eldrazi Spawn tokens now appear with correct frame and art
* General | Planeswalkers printed before Magic 2015 have had their numbers realigned in their loyalty ability boxes when zoomed in
* General | Suspended cards' time counters are now visible when covered by other exiled cards
* General | Two-colored lands' textbox backgrounds, such as Polluted Delta, now have the proper frame and color treatment
* General | When viewing Planeswalkers in the deck pane of the Collection scene while in Pile view, Planeswalkers which are not at the top of the pile now have their card name bolded


**Crash Fixes**



* Card View | The client no longer crashes when a pane set to Card View is reduced to its minimum vertical size and the User scrolls down
* Chat | Fixed an issue where profanity filter memory usage can cause crash
* Collection | A text search with 0 matches no longer causes a crash
* Collection | Adjusting panes and clicking the Options button no longer causes a crash
* Collection | Fixed several crashes in List View when trying to use keyboard commands
* Duel Scene | Fixed an intermittent crash that that occurred when trying to join a game
* Duel Scene | Fixed an issue that could cause a crash while adjusting damage spinners
* Duel Scene | Fixed an issue that could cause crash if the system thought there were two default buttons
* Duel Scene | Fixed an issues that could cause a crash while Magic Online is attempting to rebuild game state
* Duel Scene | Mogg Assassin's activated ability no longer restarts the game
* Duel Scene | When resolving Shamanic Revelation with no creatures in play the game no longer stops
* Limited Scene | Fixed an issue where the last row of the draft pool could be duplicated if the pane was reduced to minimum size and then cause a crash if one of those cards was added to Deck / Sideboard
* Play Lobby | Fixed an issue that could cause a crash if the system thought the game a player was playing did not exists
* Trade | Fixed an issue that could cause a crash in trade after updating a trade
* Trade | Fixed an issue where switching back and forth between large trade binders can cause crash
* Trade | The client no longer crashes after left clicking on a card in the "You Will Receive" pane while holding Shift key


**Collection Updates**



* Collection | Adding a selection of cards that includes cards in collection and cards not yet in collection (quantity 0) to a binder no longer fails silently and will instead add the cards that are available
* Collection | Converted mana cost column logic has been updated to better match player expectations and will respect original designation, even when cards of varying CMCs are added to the column
* Collection | Double-clicking sealed product no longer gives a deck-building prompt
* Collection | Show Versions Separately is now automatically selected when sorting by Set & Collector Number
* Collection | The default Collection Scene Sort is now Set & Collector Number with Show Versions Separately enabled
* Deckbuilding | Cards recently removed from the Sideboard pane are no longer displayed there after checking and unchecking the Sideboard's "Apply Filters" checkbox
* Deckbuilding | Closing a deck or binder now correctly updates the quantity display in the Matches pane
* Deckbuilding | When adding cards to a deck that are not yet in a play, they now remain dimmed in the Matches pane
* General | Updated the Pauper and the Standard Pauper filters to match the Banned lists
* Play Lobby | Right clicking on the drop down menu on Matches pane no longer displays the "Add deck" option


**Duel Scene and Event Updates**



* Duel Scene | Cards dragged to the right of a players hand no longer leave temporary card image
* Duel Scene | Cards inside Zone Windows now organize/scale similarly to Temporary Windows
* Duel Scene | Fixed a text issue on triggered abilities that decreased font size when the size of the Stack window increased
* Duel Scene | Fixed an issue that prevented the User from watching the replay of the first game after viewing the replay of the second game
* Duel Scene | Placing cards and effects on the stack happens automatically if they all are from the same source (this can create an issue where the player cannot stack triggers exactly as they like, which will be addressed in a future update)
* Duel Scene | Temporary Windows no longer place cards in separate piles once scroll arrows are present
* Duel Scene | Temporary windows now display all cards by default, which fixes the Thoughtseize problem
* Duel Scene | The graveyard has a mini display under the player box when the graveyard is closed
* Duel Scene | The host leaving a match now removes all players from the match queue
* Duel Scene | Undocked temporary zones, like Graveyard, no longer interfere with keyboard commands
* General | Player skill level filters now have proper spacing
* General | Updated the blue modified power/toughness on old frame cards to be more visible
* Limited Deckbuilding | Players can now drag and drop the cards from the draft pool into the sideboard during the draft


**Chat Updates**



* Chat | Chat Symbols now work in chat rooms
* Chat | Online buddies and offline buddies are now separated within the user’s Chat drop-down
* Chat | Opening the player list in chat no longer persists after making a selection
* Chat | The "Buddies" section of the Chat drop-down now organizes the user's buddies in alphabetical order


**Trade Updates**



* Trade | Accepting Trades from non-Trade scenes no longer force the player to the Trade Scene
* Trade | Sizing the lower pane of a trade to cover items in the matches pane no longer prevents those items from updating their visuals and quantities when they are removed from the "You Will Receive" pane
* Trade | Text searching for a username now returns results when filtering


**Other Updates**



* Account | Game History no longer contains the records of the matches the user watched but did not play
* Account | Prize Eligibility check boxes are no longer disabled after resizing window
* Play Lobby | Joined queues that are waiting to launch no longer show a start time of 12/31 11:59 PM
* Store | Users can no longer save addresses with blank required fields




---

 



**Temporary Workarounds for Known Issues**



We're hard at work on whittling down the Known Issues List. In the meantime, we've found temporary solutions that may help alleviate certain problems that players are experiencing. Refer to the table below to see if there is a suggested temporary workaround for an issue that you are experiencing.


**Game Play**




|  |  |
| --- | --- |
| **Issue Description** | **Temporary Workaround** |
| General | [Umezawa's Jitte](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa%27s+Jitte) counters are obscured by the equipped creature | Players can use card zoom or the preview pane to determine the number of counters |
| FRF | Archfiend of Depravity’s user interface needs to be updated | Archfiend of Depravity requires the player to select the two creatures to keep each turn. Make sure to select both creatures before hitting OK. |

**Client**




|  |  |
| --- | --- |
| **Issue Description** | **Temporary Workaround** |
| Collection | Dragging or adding a large number of cards to a deck or trade binder causes *Magic Online* to freeze while processing, resulting in a "Main Navigation is Not Responding" error | While the client is not responsive, waiting several minutes will allow the process to complete. Using the error dialog to close the client will cancel the transaction. |
| Duel Scene | Cancellation message appears if user does not return to play lobby after a duel has concluded. | When finished in an event, make sure to close your event details window. Within several minutes after an event ends, if the details window is left open in the background, the client will display this message: “The event has been canceled and your entry option has been returned to you. Please contact Game Support if you have additional questions or problems regarding this event. To do so, log in with your Wizards account at <http://www.wizards.com/customerservice>.” This message is in error. Your current event(s) is not affected. We are currently working on a fix for the inaccurate client message but, in the meantime, make sure to close your event details windows as the event finishes to avoid confusion. |
| Duel Scene | Land can visually appear tapped at the start of a turn if a player unmorphs a creature during their opponent's end step | The issue is visual only and clicking the tapped lands will add mana to the mana pool correctly |
| General | Players can experience memory leaks in some situations | Restarting the client can temporarily resolve these issues |
| Store | Updating billing and shipping information during the checkout process can have inconsistent results | Players who update from the Account Settings page should not have issues |

**Server**




|  |  |
| --- | --- |
| **Issue Description** | **Temporary Workaround** |
| Duel Scene | Both players show as waiting for opponent, one player times out | If you suspect this is happening to you, logging out and back in may resolve the problem |

 





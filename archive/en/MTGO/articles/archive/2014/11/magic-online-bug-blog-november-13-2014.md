
---
[Link to Wayback Machine](https://web.archive.org/web/20211022095933/https://magic.wizards.com/en/MTGO/articles/archive/magic-online-bug-blog-november-13-2014)

[_metadata_:author]:- "David Whitfield"
[_metadata_:description]:- "What Is the Magic Online Bug Blog? While the Known Issues List is simply that—a running list of issues we expect players to encounter most often—this accompanying “Bug Blog” is the list’s companion. Here you’ll find updates regarding emergent new issues, details around issue statuses when applicable, known issue workarounds, and a running tally of Known Issues List updates."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "297531"
[_metadata_:publish_date]:- "2014-11-14"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Magic Online Bug Blog November 13, 2014"
[_metadata_:wayback_capture_timestamp]:- "2021-10-22 09:59:33"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211022095933id_/https://magic.wizards.com/en/MTGO/articles/archive/magic-online-bug-blog-november-13-2014"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/MTGO/articles/archive/magic-online-bug-blog-november-13-2014"
---


Magic Online Bug Blog November 13, 2014
=======================================



 Posted in **Magic Online**
 on November 14, 2014 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_davidwhitfield.jpg)
By David Whitfield




 David works on the Magic community team as a content specialist. He spends his days writing about Magic Online and trying to play too many colors at once in Limited. 






 



What Is the *Magic Online* Bug Blog?
![](https://media.wizards.com/2015/mtgo/icon_bugblog.jpg)
While the [Known Issues List](http://magic.wizards.com/en/content/magic-online-known-issues) is simply that—a running list of issues we expect players to encounter most often—this accompanying “Bug Blog” is the list’s companion. Here you’ll find updates regarding emergent new issues, details around issue statuses when applicable, known issue workarounds, and a running tally of Known Issues List updates. The Bug Blog will be updated each Thursday, in conjunction with the [Known Issues List](http://magic.wizards.com/en/content/magic-online-known-issues) on the same day.


**Quick Links**

[Download *****Magic Online*****](http://magic.wizards.com/en/content/download%20) 

* [Addressing Memory Leak](#item1)
* [Known Issues List Updates](#updates)
* [Temporary Workarounds for Known Issues](#workarounds)



 



Addressing Memory Leak
After the inaugural edition of the Known Issues List, we got feedback from users that an issue many have experienced, client memory leak, was never mentioned. Rest assured, there's no conspiracy at work to sweep client memory leak under the rug; the explanation for its exclusion is fairly simple: from our end, we thought we'd covered it. We believe the memory issues that some users experience are caused, in part, by a collection of items that are already on the Known Issues List. That wasn't made clear to the community, however, so the confusion and concern are more than understandable.


This sparked a discussion amongst us here at Wizards HQ. How do we best serve the community with this list? First and foremost, communication is the main goal of the Known Issues List. Whether or not the root causes of memory leak were included on the Known Issues list is irrelevant if players don't know that correlation exists. We've included an item addressing memory leak in this week's update and will continue to update players in this Bug Blog as progress is made towards hammering out the kinks that, we believe, cause memory leak to occur. It was never our intent to hide or ignore this issue, it’s just not as straight forward as most items on the list. In the meantime, we appreciate your feedback and help in making these documents as helpful as they can be to *Magic Online* players.



 



Known Issues List Updates
Players won't see a lot of movement in the Fixed and Scheduled section this week while we gear up for our next fix deployment on Wednesday, December 3. We're evaluating what will be coming up in the next deployment and will update players as soon as we have a better idea of what will make the cut. The Client section, on the other hand, has received some updates, which can be found below.


**Newly Scheduled for the Wednesday, December 3 *Magic Online* Client Update**


**Client**



* Collection | Selecting different versions of a card and using the context menu to "Add 1 to Deck" only adds one card, not one of each version.
* Collection | Sorting columns in list view prevents quantity from being displayed correctly. Changing to card view will show correct quantities.
* Event Details | Row color does not always update to show completed matches correctly
* Events | Decks saved during limited deck building occasionally fail to load and deliver a "No decks available matching your pool." message.
* Events | In limited deckbuilding, decks sometimes fail to show all cards which can prevent deck submission.
* Events | Occasionally cards can become visually duplicated in your sideboard and prevent deck submission. Restarting the client should fix the issue.
* Events | Scheduled events that are not four rounds show up as Daily (4-round) in the Play Lobby


**Newly Added Known Issues as of Thursday, November 13**


**Game Play**



* General | [Cruel Ultimatum](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cruel+Ultimatum)'s resolution can crash the game, causing it to restart
* KTK | [Deflecting Palm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deflecting+Palm) and a damage-doubling effect do not allow you to deal quadruple damage to the player


**Client**



* Chat | The buddies list in the chat details does not sort properly, nor does it scroll properly
* Chat | The view location in the game log or chat can become stuck and requires players to manually scroll to see latest entries
* Collection | Selecting different versions of a card and using the context menu to "Add 1 to Deck" only adds one card, not one of each version
* Collection | Sorting columns in list view prevents quantity from being displayed correctly
* Duel Scene | Hotkeys for "always yes to this" and "always yield to this" don't work
* Duel Scene | The window for Thoughtsieze (and other spells or effects that allow selection from a subset of revealed cards) is not sized correctly to show all cards. Scrolling, resizing the window, or checking the game log will allow players to see all the cards revealed
* General | Players can experience memory leaks in some situations



 



Temporary Workarounds for Known Issues
We're hard at work on whittling down the Known Issues List. In the meantime, we've found temporary solutions that may help alleviate certain problems that players are experiencing. Refer to the table below to see if there is a suggested temporary workaround for an issue that you are experiencing.




|  |
| --- |
| **Server** |
| **Issue Description** | **Temporary Workaround** |
| Duel Scene | Both players show as waiting for opponent, one player times out | If you suspect this is happening to you, logging out and back in may resolve the problem |
| **Client** |
| **Issue Description** | **Temporary Workaround** |
| Collection | Dragging or adding a large number of cards to a deck or trade binder causes *Magic Online* to freeze while processing, resulting in a "Main Navigation is Not Responding" error | While the client is not responsive, waiting several minutes will allow the process to complete. Using the error dialog to close the client will cancel the transaction. |
| Collection | Sorting columns in list view prevents quantity from being displayed correctly | Changing to card view will show correct quantities |
| Duel Scene | Land can visually appear tapped at the start of a turn if a player unmorphs a creature during their opponent's end step | The issue is visual only and clicking the tapped lands will add mana to the mana pool correctly |
| Duel Scene | The window for [Thoughtsieze](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtsieze) (and other spells or effects that allow selection from a subset of revealed cards) is not sized correctly to show all cards | Scrolling, resizing the window, or checking the game log will allow players to see all the cards revealed |
| Events | Occasionally cards can become visually duplicated in your sideboard and prevent deck submission | Restarting the client should fix the issue |
| General | Players can experience memory leaks in some situations | Restarting the client can temporarily resolve these issues |
| Store | Updating billing and shipping information during the checkout process can have inconsistent results | Players who update from the Account Settings page should not have issues |









---
[Link to Wayback Machine](https://web.archive.org/web/20160831172459/http://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-ii-2001-11-03)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Matt Villamaino&#13; &#13; Part 2: Result entry problems continued and Ordered Pairing&#13; &#13; The last column dealt with correcting an incorrectly entered match result. This week will continue with a few variations on the same theme. Before doing so however I want to cover the ordered pairing window in a little more detail.&#13; &#13;"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "938876"
[_metadata_:publish_date]:- "2001-11-03"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "DCI Reporter: Beyond the Basics II"
[_metadata_:wayback_capture_timestamp]:- "2016-08-31 17:24:59"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160831172459id_/http://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-ii-2001-11-03"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-ii-2001-11-03"
---


DCI Reporter: Beyond the Basics II
==================================



 Posted in [ARTICLES](/en/articles)
 on November 3, 2001 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











*Matt Villamaino*


### Part 2: Result entry problems continued and Ordered Pairing


The last column dealt with correcting an incorrectly entered match result. This week will continue with a few variations on the same theme. Before doing so however I want to cover the ordered pairing window in a little more detail.


![](https://media.wizards.com/legacy/dci/judge/images/ordered2.jpg)


1. The round that is currently being edited. You can only edit the current round and only before you have entered any results for that round.
2. Free players area. This is the area of the window where all players not assigned to a match are listed.
3. Bye entry. To enter a bye (for example if one player is left after making the pairings), enter the player number of the player to receive the bye and click the [Enter Bye] button.
4. Table number: Before a match can be entered, it must be assigned a table. To do so, either enter the table number here (it must be a table without a match assigned to it) or click on the [First free table] button.
5. Players: When you double click on a player, his or her name will appear here. After filling both boxes with a name click the [Enter Pairing] button.
6. Pairings: the current pairings. By double clicking on the table number of a match you release the players in that match to the Free Player area.

### Buttons


[**Name**] and [**Pts**]: These buttons sort the names in the free players area by either name (last) or match points.


[**Top**]: Sets the table number as the lowest number (usually one)


[**First free table**]: Click on this button to select the lowest table number without a match being played at it.


[**Cancel**]: Cancels all changes made.


[**Release****Bye**]: Clicking this button releases the player who had the bye into the free player area.


[Delete all pairings]


[**Save pairings and Exit**]: When you have finished any changes click this to save the changes.


[**Enter Bye**]: After typing the player number who has received the bye in the bye area click this to enter it.


[**Enter Pairing**]: After selecting two players and a table click this button to enter the pairing.


\*\*\*


**ISSUE:**  
*The result is entered correctly but the wrong player is dropped.*


In this case, the fix is almost identical to the original problem you just skip the step where you change the match result.


**The Fix:**


1. Go to the Player: Data Entry window [**F2**] or **Edit => Players**.
2. Re-enter the player that was accidentally dropped.
3. Confirm with DCI Reporter that you will fix the re-entry in ordered pairing.
4. Drop the player that should have been dropped.  

 "A Match result for this player has not been entered. Continue?" [**OK**]  

 "Does this mean that the opponent wins by maximum points?" [**No**]  

 "Should the opponent drop out too?" [**No**]  

 "Ordered Bye?" [**OK**]
5. [**Save and Exit**]
6. Go to Perform => Ordered Pairing
7. Click [**Release bye**]
8. Click [**First free table**]
9. Double click on each players name so that it appears in the bottom area.
10. Click [**Enter pairing**]
11. [**Save pairings and exit**]
12. Print a result slip for that match

\*\*\*


**ISSUE:**  
*A player marked drop on the slip, but was not dropped.*


While this may happen, it is usually not brought up by the player who dropped. Before you enter the no-show results, check to see if the player had marked drop on the previous round's slip. If the player intended to drop and was not dropped, his or her DCI rating should not be penalized for it. The best solution in this case is to give the player who they had been paired against an ordered bye. That player still gets three match points (though they will not get DCI points) and the other player is not penalized for a scorekeeping error.


**The Fix:**


1. Go to the Player: Data Entry window [**F2**] or **Edit => Players.**
2. Drop the player who should have been dropped.  

 "A Match result for this player has not been entered. Continue?" [**OK**]  

 "Does this mean that the opponent wins by maximum points?" [**No**]  

 "Should the opponent drop out too?" [**No**]  

 "Ordered Bye?" [**OK**]
3. [**Save and Exit**]
4. Inform the player who was present for the match that they have an ordered bye for the round since their opponent should have been dropped.

\*\*\*


**ISSUE:**  
*The match slip was entered incorrectly, with neither player dropping.*


This problem is similar to the original problem. In this case the best solution is to simply swap the pairings of the matches of the players involved. When you correct this problem you skip the steps in the Player: Data window (Re-entering and dropping the correct player) and have an additional step in the Ordered Pairing window (the second match that must be fixed)


**The Fix:**


1. Go to the Results Entry Window [**F3**] or **Edit => Results Entry**.
2. Enter the number of the previous round.
3. Correct the match result.
4. [**Save and Exit**]
5. Go to **Perform => Ordered Pairing**
6. Double click on the table numbers of the two matches that need to be repaired. This will make their names appear in the window on the left.
7. Click [**First free table**] and double click two of the players who should be playing. (The easiest way to see this is to pair the players with the same number of match points together.)
8. Click [**Enter pairing**] and repeat for the other match.
9. [**Save pairings and exit**]
10. Print match slips for the two new matches.

\*\*\*


**ISSUE:**  
*Both players were accidentally dropped.*


There are two ways to fix this issue. The first is to randomly pick a match in which the players would be eligible to play against the dropped players and pair them against each other. The other option is to repair the round.


Make sure that the match result was entered correctly before re-entering the players and proceeding any further.


*Note: This case is very unlikely to happen by accident. In the event that it does happen the head judge should be the one who makes the decision about what option to use.*


**Option 1:** Pair them against players in another match.


In this example Mike Feuell (6pts) and Jeff Donais (6pts) were both accidentally dropped after their round three match.


![](https://media.wizards.com/legacy/dci/judge/images/pairings.jpg)


1. Re-enter both players into the tournament in the Player: Data window.
2. 2. Get a printed copy of the pairings and look for eligible matches. Here there are three matches that you could split to add Mike and Jeff in: Tables 1, 2, and 3.
3. Pick one of these matches randomly and check to see if the players involved have already played against the people that need to be added in. Using the **View => Player** Data option is probably the easiest way to do this. After checking, we find that Mike Feuell has played Mike Donais and Jeff Donais has played Paul Barclay so we will now pair Mike Feuell against Paul Barclay and Jeff Donais against Mike Donais.
4. Double click somewhere on the table two line to release the Mike Donais/Paul Barclay pairing. Their names should now appear in the free players area.
5. Click [**First free table**] and select Mike Feuell and Paul Barclay, then [**Enter Pairing**]
6. Repeat with Jeff Donais and Mike Donais.
7. [**Save and Exit**]
8. Print match slips

**Option 2:** Repair the round


1. Re-enter both players into the tournament in the Player: Data window.
2. Press [F7] or go to Perform => Pairing.
3. Confirm the deletion of the current pairings.
4. Click [Yes] then [Pair] to make the new pairings.
5. Print and post the new pairings.

Remember that most of these problems are avoidable by making sure that you enter the match slip correctly. If a slip has been filled out incorrectly, it is up to the head judge to decide to let the result stand or correct it.


Questions? If you have a question about DCI Reporter use, please send it to [MadMage682@aol.com](mailto:MadMage682@aol.com)








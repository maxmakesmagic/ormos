
---
[Link to Wayback Machine](https://web.archive.org/web/20210502062732/https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2001-10-13)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Matt Villamaino Introduction DCI Reporter: Beyond the Basics assumes that you know the basics of running a tournament with DCI Reporter. That is, creating a new event, entering players, pairing the round, printing pairings and match slips, and entering results will not be covered. The purpose of DCI Reporter: Beyond the Basics is to solve problems that arise during the event"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "938866"
[_metadata_:publish_date]:- "2001-10-13"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "DCI Reporter: Beyond the Basics"
[_metadata_:wayback_capture_timestamp]:- "2021-05-02 06:27:32"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210502062732id_/https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2001-10-13"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/dci-reporter-beyond-basics-2001-10-13"
---


DCI Reporter: Beyond the Basics
===============================



 Posted in [NEWS](/en/articles?source=MX_Nav2020)
 on October 13, 2001 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_author.jpg)
By Wizards of the Coast











*Matt Villamaino*


### Introduction


DCI Reporter: Beyond the Basics assumes that you know the basics of running a tournament with DCI Reporter. That is, creating a new event, entering players, pairing the round, printing pairings and match slips, and entering results will not be covered.


The purpose of DCI Reporter: Beyond the Basics is to solve problems that arise during the event either due to player or scorekeeper error. Some examples of what will be covered include dropping the wrong player, entering match results incorrectly, and forgetting to drop a player. Other features of DCI Reporter such as the Local player database will also be covered. In general, judging philosophy will not be discussed.


In some circumstances there is more than one way to fix a problem. When this is the case, I will list both methods along with which might be the better one to use.


Suggestions on problems to fix are also welcome. Please e-mail them and any other comments to [MadMage682@aol.com](mailto:MadMage682@aol.com).


I strongly recommend practicing all these problems before doing it in a tournament. Just set up a tournament, name it practice, enroll 8-16 players and go through the steps found here.


**Problem #1**  
*The Match Result of a match in the previous round was recorded incorrectly and the wrong player dropped.*


After pairings for round two have been posted Joe Scrub approaches you and tells you that he is not on the pairings list The first thing that you should do is checking the match result slip. Upon checking the slip, you discover that he beat Pro Player in the previous round and Pro Player has decided to drop. Players will sometimes mark the wrong spot on the match slip dropping their opponent instead of them, so it is important to check the match slip to see if this is the case.


![](https://media.wizards.com/legacy/dci/judge/images/result_slip.jpg)


In cases where a player marked the wrong spot you have two options. The first is to stick them to what the slip says and the second is to fix it to what it should be. Players are not supposed to sign the slip until they verify that everything on it is correct. On the other hand, if the player is handing it in to the scorekeeper he may change his mind and mark drop after his opponent has signed the slip. The decision of what option to use is best left to the head judge, so check with him or her before doing anything if the slip contains the error.


Remember this is only true if the discrepancy is over what player dropped. If the match result on the slip differs from what the player says it should be notify the head judge immediately.


Here the problem was in the data entry, so it should be corrected.


However, before you make any changes you will want to check the player information about the player in question in DCI Reporter. By doing this you can check both the status of the player (active or dropped out) and see the match result that was entered for the first round. To do this go to the Player Data window by either pressing [**F12**] or going to **View => Player Data**. Once there, double click on the player you want to see the information about.


![](https://media.wizards.com/legacy/dci/judge/images/playerdata.jpg)


Looking at this, you can see that he lost to Pro Player in round 1 and is currently dropped from the tournament. What likely happened then, is that the match slip was reversed when it was entered, giving Pro Player a 2-0 match win and dropping Joe Scrub instead of Joe Scrub winning 2-0 and Pro Player dropping.


There are now two options to fix this problem. After correcting the match result you can either repair the round or pair Joe Scrub against the player that Pro Player was paired against in round 2.


Regardless of which option you chose, you first need to enter the correct match result for the previous round. To do this you must go to the match result entry window [**F3**] or **Edit => Results Entry**. Click on the Previous Round radio box and enter the number of the previous round (in this case 1). Locate one of the players names in the section on the right and double click on it. Now enter the correct match result and click [**Save and Exit**]. Next go to the Edit Players window [**F2**] or **Edit => Players**. Click the Re-enter radio box, double click on the player who was accidentally dropped (in this case Joe Scrub) and click enter. DCI Reporter will ask you to confirm that you will fix the pairing in Ordered Pairing, click [**OK**]. Next, click the drop radio box, double click on the player who should have been dropped (in this case Pro Player) and press enter. DCI Reporter will now take you through several dialogue boxes:



> 
> "A Match result for this player has not been entered. Continue?" [**OK**]  
> 
> "Does this mean that the opponent wins by maximum points?" [**No**]  
> 
> "Should the opponent drop out too?" [**No**]  
> 
> "Ordered Bye?" [**OK**]
> 
> 
> 


![](https://media.wizards.com/legacy/dci/judge/images/data_entry.jpg)


Now save and exit out of the Players: Data Entry window.


If you decide to repair the round, you simply press [**F7**] or go to **Perform => Pairing**. DCI Reporter will ask you to confirm the deletion of pairings for that round (in this case 2). Click [**OK**] then click [**Yes**] followed by [**Pair**] to make the new pairings for the round.


The better option is to pair Joe Scrub against the player Pro Player was paired up against. This will minimize the disruption to the rest of the event and save time in the long run. The first thing that should be done in this case (ideally by a judge or other staff member so you can fix the problem on the computer) is look at the pairings to see who Pro Player was paired against. Call that player to the judge's station or go to the table where he or she is sitting. Explain that there was a problem with the pairings that they will be playing each other. The round should be started at this point if it has not been already.


To finish fixing the problem go to **Perform => Ordered** pairing. DCI Reporter will say that a new round has been paired, do you want to continue? Click [**YES**]. *Note that no other results for this round can have been entered*. In the top left of the window you should see the player who had been incorrectly dropped along with their correct number of match points. Click on the [**Release Bye**] button. The player with the ordered bye now appears in that window as well. Click on the [**First Free Table**] button. The table where they should be playing appears in the Table box. Remember this number. Next, double click on each players name so that it appears next to either Player 1 or Player 2. Click [**Enter Pairing**], then [**Save and Exit**].


![](https://media.wizards.com/legacy/dci/judge/images/ordered.jpg)


Assuming that you have already printed out the match slips for this round, you now want to print one for this match. If you have not, print them as normal, however if you need to print just that slip, go to **Print => Results Entry Slips**. Make sure that the round listed is the current round. In the First Table and Last Table boxes enter the table that you assigned to the match in Ordered Pairing. Click Print and give them the slip.


Fixing this problem once you know how to do it should only take a couple of minutes (if that). While it may appear easier to just repair the round, if you know what you are doing this option is much better and is also preferred by the players.


Problems with the incorrect entry of match results are probably the most common DCI Reporter error. Next week I will cover a few other problems on this issue.


*A note on the screenshots*: The tournament I set up to take the screenshots in was not created as a sanctioned tournament, therefore DCI numbers do not appear in the Player Data Entry Window. The criteria for getting into the tournament was being a recognizable figure (Level 4 judge, netrep, etc...). Wins were determined arbitrarily.








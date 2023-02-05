
---
[Link to Wayback Machine](https://web.archive.org/web/20200531085758/https://magic.wizards.com/en/articles/archive/feature/going-wide-2012-09-04)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/going-wide-2012-09-04"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200531085758id_/https://magic.wizards.com/en/articles/archive/feature/going-wide-2012-09-04"
[_metadata_:wayback_capture_timestamp]:- "2020-05-31 08:57:58+00:00"
[_metadata_:publish_date]:- "2012-09-04"
[_metadata_:description]:- "Greetings, Magic Online players! For those of you who took part in the Sneak Peek of the Magic Online beta client in July, thank you—and special thanks to those who took the time to send us feedback, whether in email, on Twitter, on the forums, or through surveys."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Going Wide
==========



 Posted in **Feature**
 on September 4, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_ryanspain.jpg)
By Ryan Spain




Ryan Spain has been a digital designer in R&D since 2011. He is involved in all things Magic Online, from new card sets to the new client and everything in between. He likely has more lifetime hours played on Magic Online than anyone at Wizards. 






Greetings, **Magic Online** players! For those of you who took part in the Sneak Peek of the **Magic Online** beta client in July, thank you—and special thanks to those who took the time to send us feedback, whether [in email](http://wizards.custhelp.com/), [on Twitter](/en/articles/archive/coming-soon-magic-online-2009-08-25), [on the forums](http://community.wizards.com/go/forum/view/75846/135046/Magic_Online_General), or through surveys. Input from our players is incredibly valuable as we work toward making the new **Magic Online** available.

The **Magic Online Beta Client:** Recent Changes at a Glance  
* "Always Open" option for the red zone
* "Big Card" view is back!
* Sticky settings between games and sessions
* Attack with all creatures or tap an entire pile of lands for mana with a single click
* Improved performance in Collection tab
* Improved Limited filters in Play Lobby
As described in [my Sneak Peek article](/en/articles/archive/meet-new-magic-online-2012-07-12), the second phase of releasing the new **Magic Online** client includes running a Wide Beta, where both versions of **Magic Online** are available on the live servers at the same time. I'm happy to announce that the Wide Beta has started! As of Tuesday, September 4, both versions of **Magic Online** are available for players, and they can play on either version with their normal **Magic Online** account. If you participated in the Sneak Peek, all you need to do is launch that version of **Magic Online** and it will automatically update to the current version. If you didn't play during the Sneak Peek, you can download the [new version here](/en/articles/archive/2011-10-17) and try it out.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat211b_mtgo.jpg)  
While we are in Wide Beta, we will continue to solicit feedback and make improvements until it is ready to be the one-and-only **Magic Online** client. Once it is ready, we will transition all players to the new version (with advance notice to players) and remove the beta tag.

The work to bring the new version to a state where it replaces the current version is on two tracks: a series of large "service pack" updates, each targeting a major area of the client, and ongoing smaller fixes and improvements. The schedule for service packs will depend on the work needed for each one, while the plan for smaller improvements is to release a new build every two weeks.

After the Sneak Peek ended, we first targeted areas based on your feedback that we could address quickly with low development risk, especially if they were not tied to an upcoming service pack effort. In addition, we pulled some highly requested changes out of their upcoming service packs and worked on them early. The result is a Wide Beta launch with a suite of improvements that many of you asked for.

### Seeing Red

One of the new features in the beta client is the red zone. When it's time for combat, a strip across the center of the screen opens up, and attacking and blocking creatures move into it, both to clarify which creatures are in combat and to show visually how blockers have been declared. While most people appreciated the red zone for the combat clarification, many people expressed a dislike for the opening and closing of the red zone each turn.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat211b_red_zone.jpg)  
We took two steps to address this concern. First, the red zone does not open until the Declare Attackers step, and if there are no legal attackers, **Magic Online** skips over this step. That means the red zone won't open unless combat is actually possible. For those who want to take it one step further, we also added an option to keep the red zone always open. You can find this setting in the "Options" menu in the game window, and in the "In-Duel Settings" on the Accounts tab.

### Getting Sticky

One of the most common requests of the beta client was to have the client remember various settings from one game or session to the next.

The client now remembers the customized sizes of all the adjustable panes, in the main window, the draft window, and each game window. It also remembers the customized size of the game and client windows between sessions. In the long term, we will broaden the "sticky settings" list to include how you have your game chat docked.

### We're Going to Need a Bigger Card

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat211b_card_preview.jpg)  
The "Card View" feature in the current **Magic Online** client is the window that shows whatever card you are mousing over, at whatever size you have made the window. Many **Magic Online** players let us know that this was an important feature to them. We've added it in this Wide Beta release by making it a free-floating window we are calling the Preview Pane. It can be toggled in the "View" or "Options" menu of any area in the beta client that displays cards, as well as in the Account tab.  
 Players who maximize a game window and attempt to use the Preview Pane during a duel will notice that it slips behind the game window when you take an action. This is a known bug, and will be fixed in an upcoming build.

### Going All In

Many **Magic** games end with an "alpha strike" in which one player sends all creatures that can legally attack into the red zone for (hopefully) lethal damage. Other times, an opposing player is tapped out without any creatures, and it's a no-brainer to attack with everything available. To make these attacks more streamlined, we have added "attack with all" functionality to the new client.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat211b_all_attack.jpg)  
During declare attackers, if you right-click on an empty spot on the battlefield, you will see a context menu containing an option to "Attack with all creatures." Selecting this option moves all your creatures into the red zone, but does not commit them to an attack until you move out of the Declare Attackers phase. This means that you can use this feature for clicking economy even when you want to attack with *most* of your creatures, but not all of them: choose "Attack with all creatures," then click on any creatures you want to hold back, and they will pull out of the red zone.

This feature also works on a single pile of creatures, so if you just want to send in the thirty-five Saproling tokens you made last turn, you can right-click on the pile of 1/1s and see the option to attack with all of them. If you are facing multiple opponents or an opponent controls a Planeswalker, these context menus will have a sub-menu to choose which person or Planeswalker to attack.

We also decided that as long as we were applying this functionality to creatures, we should apply the same tech to tapping a pile of identical lands for mana. Now, if you want to tap all the lands in a pile for the same colored mana, you can do it with a single right click instead of tapping each one individually. Further, if you want to cast, say, a [Canyon Minotaur](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Canyon+Minotaur) and you have twelve [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s in a pile, you can click on the Minotaur, then right-click on your [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain) pile and use the "All of these cards: add ![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)" function, and it will tap exactly four of them and cast the spell. You can use this for X spells like [Fireball](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball) to add an entire pile's worth of mana to the X as well.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat211b_tap_all_mana.jpg)  
### But Wait, There's More!

We've fixed and improved many other aspects of the beta client since the Sneak Peek that aren't as splashy as what I've covered so far, but are worth noting. For example, we've animated the transitions of the phase bar to make it clearer that the phase or step has changed. The number of responses we heard about people not noticing this transition increased the priority on this feature, and we are working on some other visual and audio communications about changes in the game state.

The chat field can now be expanded to show several rows of text, and performance is better in the Collection tab. In the Play Lobby, filters in Limited events now only show available formats, and we've also randomized the "Go to the Next Game" button in the Play Lobby so beta client users aren't inevitably paired with an absent host on the current client.

### The Road to One Client

![Parallel Thoughts](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Parallel+Thoughts)  
As we head into Wide Beta, I want to leave you with two thoughts: We know the new client is not done yet, and we are listening closely to our players as we finish it.

The Sneak Peek was a great success for us in that we were able to release the **Magic Online** beta client into the wild; take in the responses; and, wherever possible, adjust our priorities to match what we were hearing. As we continue to release updates on the way to removing the beta tag, I hope you continue to share your thoughts with us through the many avenues available. Not every great or often-received request is something we can turn around in a couple of weeks, but there will always be some that we can. The ones we can't are either part of the larger service packs to come or are part of the ongoing discussion about the future of **Magic Online**.

Thanks for taking the time to read about the latest changes to the **Magic Online** beta client, and I hope you take a look for yourself. Until next time, good luck and have fun!

—Ryan ([@RyanSpain](https://twitter.com/RyanSpain))

  







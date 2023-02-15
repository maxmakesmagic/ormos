
---
[Link to Wayback Machine](https://web.archive.org/web/20210502075045/https://magic.wizards.com/en/articles/archive/battlefield-battle-2012-12-19)

[_metadata_:author]:- "Ryan Spain"
[_metadata_:description]:- "Hello, digital Planeswalkers! On December 12, we released a build of the Magic Online beta client with some significant changes. Normally, this would be cause for one of my beta client update articles, but with Magic Online Week on DailyMTG.com right around the corner, we waited to include this overview of the latest updates to Magic Online as part of this theme week. I'm sure"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "682071"
[_metadata_:publish_date]:- "2012-12-19"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Battlefield Battle"
[_metadata_:wayback_capture_timestamp]:- "2021-05-02 07:50:45"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210502075045id_/https://magic.wizards.com/en/articles/archive/battlefield-battle-2012-12-19"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/battlefield-battle-2012-12-19"
---


The Battlefield Battle
======================



 Posted in **Feature**
 on December 19, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_ryanspain.jpg)
By Ryan Spain




Ryan Spain has been a digital designer in R&D since 2011. He is involved in all things Magic Online, from new card sets to the new client and everything in between. He likely has more lifetime hours played on Magic Online than anyone at Wizards. 







Hello, digital Planeswalkers! On December 12, we released a build of the **Magic Online** beta client with some significant changes. Normally, this would be cause for one of my beta client update articles, but with **Magic Online** Week on DailyMTG.com right around the corner, we waited to include this overview of the latest updates to **Magic Online** as part of this theme week.


I'm sure some of you have already discovered the latest changes on your own, but for those who haven't played the beta client recently, there are some nice improvements in the new build. For starters, we caught up on some features and fixed some issues in the Collection scene that didn't quite make it in time for the big Collection-focused update from October 31. The Collection scene now has quick-toggle color filters, .csv importing and exporting, and some revisions to the sorting logic for color and mana costs. We also made some additional performance improvements in Collection, where manipulating thousands of **Magic** cards can take its toll on a CPU.


[![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat226c_collectionsort_small.jpg)](http://media.wizards.com/images/magic/daily/features/feat226c_collectionsort_large.jpg)


*Click to expand*
Then, if you go to the Play Lobby, you'll see a bit of a facelift to the way you enter a game. The process for choosing your style of play is much clearer, and when you pick a deck in Constructed Open Play, the format is then auto-selected, allowing you to jump into a game with a minimal number of clicks.


[![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat226c_playlobby_partial.jpg)](http://media.wizards.com/images/magic/daily/features/feat226c_playlobby_full.jpg)


*Click to expand*
You can find a [complete changelist here](http://community.wizards.com/go/thread/view/75846/29466403/Wide_Beta_Changelist), but I'm going to spend the rest of this article on what I feel are the most significant changes to the beta client since it became publicly available, which center around how the beta client manages permanents on the battlefield.


### The Give and Take


The battlefield is the most important aspect of **Magic Online**—it is quite literally where the **Magic** happens—and it is also the most complex. Thousands of unique cards with an ever-growing list of mechanics must combine seamlessly on a digital battlefield of endless possibility, all in a way that makes it as clear as possible to all players exactly what is happening at all times. The edge cases alone are enough to keep **Magic Online** designers and developers up at night!


### Major Changes


A quick glance at the major changes in the latest version of the **Magic Online** beta client:


* Multiple changes to reduce movement of permanents on the battlefield during a game
* Cards form additional rows on the battlefield before scrolling happens
* Improved interface for joining events and matches
* Collection updates for better sorting, and the addition of quick-toggle color filters
* .CSV importing and exporting supported
* More streamlined creation of new decks
* Performance improvements in the Collection scene

Sometimes, in that effort to create the best user experience possible on **Magic Online**, design gets pulled in different directions by mutually exclusive design goals, all of which are extremely important to the overall product. Given the complexity of the battlefield in **Magic**, it was inevitable that we would encounter this kind of tension when redesigning the battlefield for the beta client. Finding the right balance point between conflicting design needs is a process requiring some iteration, and we have arrived at another stage of this process with this latest update.


Card size, game-state clarity, and board stability (the lack of positional change among permanents) are all important aspects of the battlefield, yet it is difficult to improve one area without making sacrifices in another. The current client, for example, prioritizes board stability highly. Except for basic lands, cards and tokens don't form piles, so each permanent occupies a full card's worth of space on the battlefield. In combat, attacking and blocking creatures do their thing from wherever they sit on the battlefield. Each new permanent that enters the battlefield stays put, except to make room for new permanents or to contract when an existing permanent leaves the battlefield.


[![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat226c_v3_small.jpg)](http://media.wizards.com/images/magic/daily/features/feat226c_v3_large.jpg)


*V3 Battlefield. Click to expand*
This high level of board stability is excellent for instances of serial clicking. When you are attacking with four of your seven creatures, or targeting three-of your opponent's twelve permanents, it's nice that they all sit still while you click them. However, game-state clarity takes a big hit in this world, as little of the organization that most players do naturally when playing with physical cards happens, such as signifying blocks by placing blockers across from attackers, or piling all of your centaur tokens together. Card size suffers also, as the lack of piling means cards shrink sooner to accommodate a permanent-heavy board.


In the beta client, we wanted to give game-state clarity and card size a boost. As those familiar with the beta client know, the red zone used for combat creates a very clear indication of which creatures are blocking which attackers. Piling identical permanents and shifting rows on the fly to make space as needed for tapping a permanent conserves maximum space on the battlefield so cards don't have to shrink as quickly.


While these changes were well intentioned, the resulting battlefield in the beta client took a significant hit to board stability. When you perform a series of clicks as part of a single act—like attacking with four of your seven creatures—you plot out the click locations in your head without even thinking about the act of clicking. If after clicking a permanent, the remaining permanents change position, your brain must recalculate the remaining click sequence. Instead of being able to make those four clicks quickly and confidently, you have to slow way down to track the card movement and update your mental targeting to avoid misclicks.


This was happening even on relatively sparse battlefields in the previous incarnation of the beta client. Because permanents always sat as close as possible to their neighbors to maximize the use of space, simply casting a three-mana creature with three unique lands on an otherwise-empty board caused a brain recalculation due to the unwanted movement among the lands with each click. This proved unacceptable, and we knew we had a problem to solve.


### The Stabilization Play


We've taken a few important steps in the latest build to address the movement issue. First, we've reserved the space to the right of each permanent or pile of permanents to accommodate tapping without having to make room on the fly. This sacrifices some use of space, but is essential to the reduction of card movement. Second, piled cards no longer split off into a separate new pile when they become tapped; instead, tapped permanents in a pile move to the back of the pile and into the space reserved for tapping. This causes no movement to the surrounding permanents, but still allows players to target a tapped permanent in a pile, and to click repeatedly on the top of a pile to tap several of the same permanent in quick succession.


Finally, we no longer center attackers; creatures simply move straight up into the red zone when attacking (except on a super-crowded battlefield, which I'll get to in a bit). Perfectly centered attackers were aesthetically pleasing once attackers were declared, but it simply wasn't worth the movement cost to get there. Currently, blockers still have to move to retain the combat-clarifying intentions of the red zone, but we are working on a change to address the movement of permanents around blockers that will be ready in the next build. Overall, though, the latest build is a vast improvement over the hokeypokey that frequently plagued the declaration of attackers to this point in the beta client.


[![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat226c_beta_small.jpg)](http://media.wizards.com/images/magic/daily/features/feat226c_beta_large.jpg)


*Beta Battlefield. Click to expand*
 


Some movement is inevitable, though. When a new permanent is added to the battlefield, the layout has to change to accommodate and there's nothing we can do about that. The red zone, which has proven to be a great tool for clarifying combat, requires that creatures move into it after declaring attackers and blockers, and back out again upon the transition to the second Main Phase. However, movement during the addition or destruction of permanents or the transition between phases is not disruptive to our brains the way that it is when movement happens during an interactive moment. The new build makes huge strides in reducing such movement.


 


### A Rows is a Rows


To this point, the beta client has kept all permanents in two rows—a creature row and a non-creature row—and introduced horizontal scrolling to handle lots of permanents while keeping cards at the largest possible size. By piling identical permanents and not reserving space for tapping, the need for scrolling the battlefield was thankfully more of an edge case on most monitors, but frankly it wasn't enough of one. When the game state required scrolling to contain all the cards in two rows, it was too frustrating to navigate to perform certain actions, and too easy to forget what permanents were off the edge of the screen.


Having cards appear as big as possible at all times looks great in a screen shot, but at the end of the day the top priorities have to be game-state clarity and board stability. The only solution that made sense was to bring back the creation of additional rows beyond the second. Now, if the permanents don't all fit on two rows, additional rows are created until cards reach a minimum size, and only then does scrolling kick in. I personally have yet to experience scrolling on this build, even on my small laptop screen.


As is common, though, solving one problem created another. Moving attackers straight up into the red zone instead of centering them was a big movement reducer, but now with the possibility of a third row, there could be instances where creatures would not have the red zone directly above them. In such cases, unwanted movement would be required to get the attacker into red zone. To keep disruptive movement from happening during that interactive moment, creatures in multiple rows don't move into the red zone until the active player finishes declaring attackers. Creatures clicked for attacking move up slightly in place to be identifiable, but not in a way that distracts the brain and forces a click recalibration. This has solved the movement problem while allowing for additional rows quite nicely.


### Gotta Keep Moving!


There is still a lot of give and take to work out, and we still have some tricky battlefield problems left to solve before we will consider dropping the beta tag and turning off the current client. This release is a big step in the right direction, though, and I hope if you were dissatisfied with the battlefield experience in the beta client before that you'll give it another try, and if you haven't checked it out at all yet, there's no better time than the present!


As always, [we'd love to hear your feedback](http://www.surveygizmo.com/s3/1112822/MTGO-Wide-Beta-Survey-2-December-11-2012) on the battlefield balance, and any other feature you care to try in the beta client. Player feedback has been and continues to be an important part of the development of this client. Until the next big update, good luck and have fun!


—Ryan Spain ([@RyanSpain](https://twitter.com/RyanSpain))










---
[Link to Wayback Machine](https://web.archive.org/web/20201108170849/https://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-leagues-update-2015-08-17)

[_metadata_:author]:- "Chris Kiritz"
[_metadata_:description]:- "Greetings Magic Online players, It's been too long since my last Leagues update and, as you may have noticed, the first half of 2015 is over and you are not currently playing in a League. That will change soon. While it has been a longer journey than any of us would have liked, I'm excited to share the current project status and what you can expect from Leagues in the near future."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "454506"
[_metadata_:publish_date]:- "2015-08-17"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Magic Online Leagues Update"
[_metadata_:wayback_capture_timestamp]:- "2020-11-08 17:08:49"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201108170849id_/https://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-leagues-update-2015-08-17"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/MTGO/articles/archive/magic-online/magic-online-leagues-update-2015-08-17"
---


Magic Online Leagues Update
===========================



 Posted in **Magic Online**
 on August 17, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/hero/wizardslogo_thumb.jpg)
By Chris Kiritz












Greetings *Magic Online* players,


It's been too long since my [last Leagues update](http://magic.wizards.com/en/MTGO/articles/archive/magic-online-leagues-update-2014-11-19_2) and, as you may have noticed, the first half of 2015 is over and you are not currently playing in a League. That will change soon. While it has been a longer journey than any of us would have liked, I'm excited to share the current project status and what you can expect from Leagues in the near future.


For more Leagues information, look for Lee Sharpe’s article at the end of August. He’ll be discussing entry options, prizes, scheduling, and the full details of what you can expect as we roll out Leagues to the public at large.


Let's jump right in and discuss when we're launching, what we're launching, and some of the reasons behind these decisions. If you're not familiar with what a League is, [check out the bottom of the article to learn more](#aboutleagues).




---

When We're Launching
====================


Soon! I know we've said that before, but we've passed our last few milestones and are currently doing final preparations for release to production right now! If all our final pre-production testing goes well (which we fully expect), we will be deploying the initial Leagues code to *Magic Online* on August 26, with first public access in mid-September.


Once deployed, we will need some additional testing on the live production servers to verify that everything is solid and the system is stable, so players won't be able to join a League right at launch. Once this initial testing is done, however, we'll slowly open the gates to the public until we reach our initial capacity levels. We expect this roll out process to take several weeks and plan to hit our initial capacity target in time for the *Battle for Zendikar* release.




---

What We're Launching
====================


On August 26, we will be releasing the infrastructure updates, administration tool updates, and client updates that allow us to support Constructed Leagues with an active player cap significantly higher than anything we've done on *Magic Online* in the past. So we're clear, let me repeat that. **On August 26, we will start the roll-out for Constructed Leagues only, with public access starting in mid-September.** 


After we've deployed, you'll notice a couple changes to the *Magic Online* client. First, a featured League section will show up on the Home Scene, letting you know which League or Leagues are available to join. At launch, this area may be empty or filled with a test League—but once we're up and running, you'll be able to open the featured League and join it right there without heading to the Play Lobby. If you've already joined a League or two, this section will switch to showing the Leagues you've joined instead.


![](https://media.wizards.com/2015/mtgo/8-17-2015_img_1.png)


Second, the Constructed Events and the Limited Events rooms in the Play Lobby get new Leagues options. Here you'll be able to check out all the available League options, not just the featured Leagues or the Leagues you've joined. Of course, the Limited Leagues room will be empty until we launch that feature, so make sure you're in the Constructed Leagues room when you're looking to join.


![](https://media.wizards.com/2015/mtgo/8-17-2015_img_2.png)


Our early Leagues will have a limit on the number of players who can join and will run for relatively short timeframes. If everything looks good as Leagues progress, we'll increase their caps. At the end of the roll-out period, we'll be able to support thousands of active League players in a single Constructed League or distributed amongst several smaller Leagues, each larger than any tournament we've run on *Magic Online*. Here's a rough look at what the current roll-out plan looks like, though the timing for the transitions and the exact player counts will be based on reaching specific milestones and may be different from what is listed below.


![](https://media.wizards.com/2015/mtgo/8-17-2015_img_3.png)


While we'll have the opportunity to run several Leagues simultaneously, we want to make sure we have a critical mass of players in each League, so we'll focus on the most popular formats at first: Standard and Modern. Similar to a tournament, you'll choose your deck as you join the League and you'll use that deck as-is for its duration. Since the experience is focused on a single deck, Constructed Leagues will be shorter so players can mix it up more often.


We'll discuss the roll-out plan in greater depth, including participation dates, entry and prize structures, and League durations in the next week or two, prior to the inaugural Standard League.




---

Why the Delay?
==============


The Leagues project includes several distinct elements, including the Leagues proper, the tools to manage those Leagues, and infrastructure updates to support all of the changes. Obviously, all of these changes need be thoroughly tested to ensure that we don't disrupt the current *Magic Online* experience. Over the course of this testing, we uncovered issues that needed to be addressed before we could release Leagues to the public. Certainly nothing new in the world of software development, but a handful of the issues we discovered just needed more time to fix than we originally allotted.


In an effort to get a quality Leagues experience delivered sooner, we changed course from the more complex Sealed Deck League to the simpler Constructed League. This allowed us to focus on key League functions and performance without worrying about deck building, adding cards to a deck mid-League, and running multiple stages that Sealed Deck Leagues include. This saved both development and testing time. It also allowed us to double down on load testing and make sure we can support the large number of players we want in each League.


While the delay is unfortunate, the work delivered has created a much better foundation upon which to build the future of Leagues. We've upgraded our testing capabilities, especially around load testing, so we can do more testing faster. We've refined the Leagues infrastructure to allow better scalability, so future releases should be easier. This all translates to a better Leagues experience for you out of the gate and as we deliver addition features and support.




---

What's Next
===========


We're currently all hands on deck prepping for launch. Our final Closed Beta is running now, so if you're one of our Closed Beta players, get on there and let us know what you think. If you want to sign up to be part of our Closed Beta team and help us find issues in future releases, you can do so [here](http://wizards.custhelp.com/app/answers/detail/a_id/2265/~/magic-online-closed-beta-requirements).


Hot on the heels of the Constructed Leagues release, *Battle for Zendikar* Prerelease Events start on October 9. Stay tuned to [MTGO.com](http://magic.wizards.com/en/game-info/products/magic-online) for news about the upcoming Prerelease and release events. We're also planning for some cool events around the holidays (did someone say Cube?), but more on that as we get closer.


Thanks for all your patience. It's been a long road, but Leagues are almost here and I can't wait to battle some of you in the Leagues queue. If you want to share your thoughts or feedback, feel free to email us at [MagicOnlineFeedback@wizards.com](mailto:MagicOnlineFeedback@wizards.com) or ping me directly on Twitter at [@ckiritz](https://twitter.com/CKiritz).


Have fun and good gaming,


Chris Kiritz  

Digital Product Manager  
*Magic: The Gathering*




---


What is a League?
=================


A League is an ongoing tournament that plays out over the course of days or weeks rather than hours. Leagues have two main goals: reduce the amount of time it takes to play competitive *Magic* and allow players to play on their own schedules.


With these goals in mind, Leagues do not follow the round structure of other tournaments. Instead, you'll be able to join any active League, even if it has been running for several weeks. Once joined, you'll have a set number of matches you can play over the duration of the League. Once you've finished all of your matches your course is over, you'll receive any prizes you've earned, and, if the League is still active, you can join again immediately.


After you've joined the League and are ready to battle, you'll queue up for a match and we'll pair you with an opponent as soon as we can. This pairing will include some matchmaking, but our primary goal is to find you a suitable opponent as quickly as possible and limit the amount of time spent waiting to play *Magic*.


Once you finish your match, you can queue up again if you have time, or save your matches for the future. This lets you participate at your own pace one match at a time. You can binge and play all your matches consecutively or play once or twice a week throughout the duration of the League. The choice is up to you and what you have time for.


[Return to Top](#top)








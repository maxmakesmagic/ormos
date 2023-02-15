
---
[Link to Wayback Machine](https://web.archive.org/web/20180926125207/https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25)

[_metadata_:author]:- "Christopher Bellach"
[_metadata_:description]:- "A change is coming to the targeting system on Magic Online, which should make it much easier to burn your opponents to cinders."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1337576"
[_metadata_:publish_date]:- "2018-09-25"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Target: Targeting"
[_metadata_:wayback_capture_timestamp]:- "2018-09-26 12:52:07"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20180926125207id_/https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/magic-online/target-targeting-2018-09-25"
---


Target: Targeting
=================



 Posted in **Magic Online**
 on September 25, 2018 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Christopher Bellach











Welcome back, fellow Planeswalkers and fans of *Magic Online*. This is Christopher Bellach again, client developer, and I have another exciting upgrade for *Magic Online* to share with you all. First, a little context as to why we decided to make this change.


Have you ever been in Game 3 of a match and you just need to draw your [Aurelia's Fury](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aurelia%27s+Fury) to burn your opponent out? Miraculously, your next draw is that very card, and you snap-play it as fast as you can. But your opponent only takes 1 damage because the *Magic Online* targeting indicators covered up a critical part of the interface that should have allowed you to choose how much damage the spell would do to your opponent? Well players, rejoice, as we have worked diligently to design a new targeting indicator system to make sure this problem will be a thing of the past.


Before we get to what the new targeting looks like, I want to take you through the iterations we made before coming to the design that made it to release. While the player targeting was the most problematic, we wanted to use consistent iconography to relay targeting information when targeting cards in all zones. Our first iteration was inspired by the iconography that map apps use to point to specific locations.


Round 1


![](https://media.wizards.com/2018/images/daily/npOw3ylfav.png)![](https://media.wizards.com/2018/images/daily/8dm6yOgIpZ.png)


There was some confusion about which icon meant targeting and which icon meant being targeted, and our color-blind testers were having trouble seeing the icons. Our next iteration updated the coloring to be more friendly to common forms of color-blindness and used different symbols within each indicator.


Round 2


![](https://media.wizards.com/2018/images/daily/lKBrFFRVrJ.png)![](https://media.wizards.com/2018/images/daily/otvQMid3Qh.png)


The new icons helped show what each indictor was trying to relay to the player. The new coloring also was much clearer to our color-blind testers, but the design of the icon still wasn't very grokkable at first take. For the next iteration, we tried a couple of different designs, putting them through some A/B testing.


Round 3


![](https://media.wizards.com/2018/images/daily/8Cw9c8nxUH.png)![](https://media.wizards.com/2018/images/daily/efA70nIG5C.png)![](https://media.wizards.com/2018/images/daily/aH0JIIp3Sj.png)![](https://media.wizards.com/2018/images/daily/IkgFmpbPql.png)


After testing these new icons, the arrow design ended up being the most successful at clearly indicating the game state to the player. However, some playtesters commented that the icons felt out of place, especially when side by side with the [new counter icons](https://magic.wizards.com/en/articles/archive/magic-online/counter-development-2018-09-05). We also heard that the icons were hard to notice. Also, when something was targeting itself, having both the outward targeting icon and the inward targeting icon on the same card took up a lot of space. For our last iteration, we increased the size of the icons significantly and added white and black borders around the icons. Then, to keep the display simpler, we created a special icon to indicate when something is targeting itself instead of showing two separate icons.


Final


![](https://media.wizards.com/2018/images/daily/zNFKoo8MrB.png)![](https://media.wizards.com/2018/images/daily/TmcWOtxy6K.png)![](https://media.wizards.com/2018/images/daily/GoEJAgoMZy.png)


These are the icons you will see in the next update to *Magic Online.* The sky blue up arrow indicates that this thing is targeting something, and the vermillion down arrow indicates what is being targeted. The merged icon is used to indicate when something is targeting itself.


Here are some examples of what the icons look like in the *Magic Online* client:


![](https://media.wizards.com/2018/images/daily/hhPdJyOyPU.jpg)


The next time your only out is that [Aurelia's Fury](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aurelia%27s+Fury), this is what the interface on *Magic Online* will look like. The vermillion down arrow indicates that the player is being targeted and the damage spinner is no longer being covered up. It will be much easier to let *Magic Online* know that you want to deal that 20 damage to your opponent, instead of the default 1.


Here is what it looks like when you target yourself with your [Ancestral Recall](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall):


![](https://media.wizards.com/2018/images/daily/sLwxB2ar0d.jpg)


On the battlefield, the icons will be large on the card and will always point up/down regardless of the tapped state of the card.


![](https://media.wizards.com/2018/images/daily/iVMRgYAcQn.jpg)


That's all I have for this update. Thanks for reading, and I'm excited for you all to get a chance to use the new targeting system. Feel free to send your feedback to [MagicOnlineFeedback@wizards.com](mailto:MagicOnlineFeedback@wizards.com), and I look forward to hearing what you all think of these changes. See you next time, and may all of your packs have epic foils!








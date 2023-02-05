
---
[Link to Wayback Machine](https://web.archive.org/web/20220117224342/https://magic.wizards.com/en/articles/archive/feature/born-digital-gods-2014-02-24)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/born-digital-gods-2014-02-24"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220117224342id_/https://magic.wizards.com/en/articles/archive/feature/born-digital-gods-2014-02-24"
[_metadata_:wayback_capture_timestamp]:- "2022-01-17 22:43:42+00:00"
[_metadata_:description]:- "Download Magic Online This is the story of how Born of the Gods went from physical cards to a digital release. A few months ago, I told a similar tale for Theros. Like Theros, Born of the Gods was full of adventure, progress, setbacks, and learnings. Let’s start by paying tribute to a new mechanic in Born of the Gods… This Is Just a Tribute Fanatic of Xenagos Tribute offers"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Born of the Digital Gods
========================



 Posted in **Feature**
 on February 24, 2014 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_jonloucks.jpg)
By Jon Loucks




 Jonathon Loucks is a digital designer in Wizards R&D. As a civilian, he enjoyed playing and writing about rogue decks. Later, he co-hosted the Limited Resources podcast. Now he works on the many facets of Magic Online.
 








![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/logo_bng_transparent_250.png)[Download ******Magic**  Online****](https://accounts.onlinegaming.wizards.com/) 

This is the story of how *Born of the Gods* went from physical cards to a digital release. A few months ago, I told [a similar tale for *Theros*](http://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/other/09292013/loucks). Like *Theros, Born of the Gods* was full of adventure, progress, setbacks, and learnings. Let’s start by [paying tribute](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=370606) to a new mechanic in *Born of the Gods*…


This Is Just a Tribute
----------------------




![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/card_fanaticofxenagos.png)  
*[Fanatic of Xenagos](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Xenagos)*


Tribute offers the players a choice: pay the tribute, or don’t pay the tribute. This choice is presented to the player in the "prompt box"—the area of the screen where the player is prompted to act. One of my big goals with new sets on **Magic Online**  is making sure that the prompt box text is both helpful and concise.


The completely concise version of the tribute choice would be "Pay the tribute?" with "Yes" and "No" buttons. I know that would frustrate me as a player because I would have to re-read the card every time to remember if "paying tribute" meant the +1/+1 counters or the effect.


The completely helpful version of the tribute choice would be "Pay the tribute and put a +1/+1 counter on [Fanatic of Xenagos](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Xenagos)? If you don’t pay the tribute, when [Fanatic of Xenagos](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Xenagos) enters the battlefield, it gets +1/+1 and gains haste until end of turn." While helpful, that’s a lot of text to read every time the tribute choice is presented. It also requires some extrapolation by **Magic Online**  to see what not paying the tribute means.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/tribute_prompt_box.png)  
*Tribute prompt box  

for Fanatic of Xenagos.*
As players become more familiar with cards, they start to remember the effects. I’ll start to remember [Fanatic of Xenagos](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fanatic+of+Xenagos)’s exact ability over time. In the meantime, I can read the card to remember exactly what it does; the prompt box shouldn’t be trying to replace that functionality. All that in mind, this is the prompt box you’ll see when asked to pay tribute.


The idea is to provide a helpful reminder to players about what paying tribute means, without going into complete detail about the ramifications of that choice.



Prompt Box Prose
----------------


Along with the goal of clear prompt box text, I’ve been on the lookout for spells with multiple and different targets. For example, check out [Acolyte’s Reward](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Acolyte%E2%80%99s+Reward).




![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/card_acolytesreward.png)  
*[Acolyte's Reward](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Acolyte%27s+Reward)*


Normally, the prompt box would say "choose first target," followed by "choose second target." While I don’t want to reiterate all of [Acolyte’s Reward](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Acolyte%E2%80%99s+Reward)’s text in the prompt box, I do want the player to be clear on which target he or she is choosing; I never want the player to have to read the card text to figure out which target is first and which target is second.


This results in the following prompt boxes:



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/acolytesreward_1.png)![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/acolytesreward_2.png)*Prompt boxes for Acolyte's Reward.*

  

While we achieved clarity here, there is room for improvement: Clicking the "OK" button has no effect; its existence is likely a carryover from shared code that we hope to clean up in the future. Next, the text for choosing the first target is missing the word "target," which speaks to a larger goal of sticking as close to technical **Magic**  language as possible. While the text "choose creature to prevent damage to" is clear, it's misleading in the context of a **Magic**  game. "Choose creature" and "choose target creature" are different effects, so we should be sticking to the correct wording.



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/scry_prompt_box.png)  
*Prompt box for scry.*
I want to expand on staying technically precise in the prompt box. Any normal text you see in the prompt box should be technically precise **Magic**  language. However, sometimes extra explanation for the sake of **Magic Online**  is necessary. **Magic**  already has a good convention for helpful-but-not-necessarily-technically-precise language, and that’s reminder text. I’m currently working to improve the consistency of our language in the prompt box, which includes clear reminder text when necessary. For example, consider the current prompt box for scry.


That’s relatively clear **Magic**  instruction, but how the player performs that action is fairly ambiguous—the player has to click on the cards themselves to make the choice. This is a case where we should be using **Magic Online**  reminder text. For example, the prompt box could say: "Put the cards on the top or bottom of your library in any order. (Click on each card to choose.)" This is the type of thing I look to improve with each set release.



A lot of the quality and consistency of a **Magic**  set comes from the strength of our editing team.
While digital R&D has many combined years of **Magic**  experience, editing consistency takes a level of expertise that we know we are lacking. So, with an eye toward improving the quality and consistency of **Magic Online**, the digital R&D team turned to the **Magic**  editing team.


A lot of the quality and consistency of a **Magic**  set comes from the strength of our editing team. I’m happy to announce that **Magic Online**  now has dedicated editing resources within the **Magic**  editing team! This help comes in the form of Allison Medwin. She’s a recruit to Wizards of the Coast from the **Magic**  Judge program, and recently moved from Game Support to an internship on the **Magic**  editing team. Part of her many duties includes helping **Magic Online**  with its editing needs. I’m really excited about bringing the same quality and consistency of our physical releases into the digital realm.


Fickle Fates
------------


Ye gods! Part of the digital team’s promise is to deliver every card with each set release. Unfortunately, not all cards are created equally. [Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates), for example, accounted for a large chunk of the set-coding effort.




![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/card_whimsofthefates.png)  
*[Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates)*



Part of the digital team’s promise is to deliver every card with each set release. Unfortunately, not all cards are created equally.
Why was [Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) especially difficult? It required special UI that didn’t exist. While we’ve done card piles before on **Magic Online**—[Fact or Fiction](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction), [Liliana of the Veil](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liliana+of+the+Veil)’s ultimate—they were always two card piles. Adding in a third pile requires additional UI creation, and creates new user flow. Where previously the user only had to move a card to the "other" pile, now there are two "other" piles. [Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) also required that all players create their piles with full knowledge of the piles created by other players before them—also new functionality. On top of all that, the coexistence of the Wide Beta Client and the current client essentially doubled the amount of work to get this already difficult card coded.


But never fear, [Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) works thanks to the coordinated efforts of the cardset team, the current client live team, and the team focusing on increasing the Wide Beta Client stability and performance.


While we weathered the [Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) storm, we want to make sure we’re more prepared for this kind of thing in the future. Personally, I want to make sure we’re always learning and improving, and that we never make the same mistake twice. To that end, we’ve created the "[Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) check" step in the set-coding process.


Digital R&D really doesn’t want to shackle what the rest of R&D can do. We’re not going to ask R&D to kill a difficult-to-implement mechanic.
Previously, digital R&D wouldn’t really see a card set until it was already final. We’ve now further integrated digital R&D into the set-creation process. Now, we do a sweep of the set before it’s locked down so that we can look at expensive-to-implement cards (like [Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates)) and work with the R&D developers to potentially change the card. Digital R&D really doesn’t want to shackle what the rest of R&D can do. We’re not going to ask R&D to kill a difficult-to-implement mechanic, and we’re more than willing to put extra work into a flagship card of the set, like a Planeswalker. However, if we catch goofball, non-flagship cards like [Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) early enough, we can work with the developers to potentially change it and free up card coding resources.


Luckily, [Whims of the Fates](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) has largely been an exception, and digital R&D hasn’t had to request any changes on future sets—yet.


Online Branded Play & Hero Cards
--------------------------------


One of the digital team’s goals with the release of *Theros*  was to embrace branded play. We were tasked with making a digital experience that would echo the Hero’s Path experience held at local stores.


To that end, we implemented on **Magic Online**  the same Hero Cards that players gained at their local Prerelease, Release, and Game Day events. We created the Hero’s Path Standard format, in which players could use their Hero Cards with a Standard-legal deck. Since we couldn’t implement on **Magic Online**  the Face the Hydra deck that would be used in stores, we created the **Magic Online**  Face the Hydra Challenge. We streamed the event, and I even wore a hydra costume:



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/loucks_hydra_1.jpg)
We always try to learn from everything we do on **Magic Online**, taking players' feedback, reviewing event performance, and making changes for the future—all with the goal of making **Magic Online**  the best it can be. Unfortunately, sometimes we learn that **Magic Online**  isn't yet ready for all the awesome things we want it to do. The Prerelease boxes (which started with *Return to Ravnica*) have been a great addition to the **Magic Online**  Prerelease experience that we’re going to continue to deliver. However, we dialed back additional branded play efforts for *Born of the Gods*  so that we could focus on delivering the highest quality on those experiences we did offer. The next time we expand the **Magic Online**  branded play offerings we will be able to deliver at the quality bar that R&D expects.


What this all means for *Born of the Gods*  is that we are still delivering the hero avatars, and you’ll earn them much the same way you earned the *Theros*  avatars—by playing in Prerelease and Release Events. However, while the *Born of the Gods*  avatars can still be used for your player avatar, they don't possess any abilities themselves. Finally, we retired the Hero's Path Standard format—the only format where the avatars' abilities came into play—as announced in the [**Magic Online**  Weekly Announcements](http://community.wizards.com/content/blog/4051771) on February 11. I encourage you to check out the [Twitch.tv archives](http://www.twitch.tv/magic/b/475633068) if you want to see what that format was like.


The Owner of My Controller Is My Friend
---------------------------------------


One of the improvements we were able implement with *Born of the Gods*  was blue text for ownership:



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/blue_text_owner.jpg)


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/card_perplexingchimera.png)  
*[Perplexing Chimera](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Perplexing+Chimera)*


Whenever a card is controlled by a player other than its owner, that card will now have blue text showing who the owner of that card is. Not only does this help clarify the game state in two-player games, but it also provides useful information that was previously invisible in multiplayer games.


This is a timely fix for *Born of the Gods* with the wacky control-switching-on-the-stack [Perplexing Chimera](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Perplexing+Chimera).


Whenever a card is controlled by a player other than its owner, that card will now have blue text showing who the owner of that card is.
Mindreaver
----------




![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/card_mindreaver.png)  
*[Mindreaver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindreaver)*


I tend to call out the extreme cases of implementation, but here’s a simpler one: [Mindreaver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindreaver).


[Mindreaver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindreaver) can be implemented using technology that we already have. Since [Mindreaver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindreaver) cares about the cards it has exiled, we show the exiled cards behind it on the battlefield, much like players are used to with [Oblivion Ring](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) effects.


My goal with the "show exiled on the battlefield" tool is to only show the relevant cards on the battlefield. Since [Mindreaver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindreaver) can be used to counter spells, it makes sense to put the non-spell cards (the land cards) in the exile zone. This keeps the battlefield clean and relevant. [Ashiok, Nightmare Weaver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashiok%2C+Nightmare+Weaver) was given a similar treatment with *Theros*. (Watch out for those cards that end in "eaver.")



![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/digital/magiconline/mindreaver_exile.png)  
*Mindreaver exile as displayed  

on the battlefield.*
In the short term, I’m making sure we use this tool intelligently going forward. In the long term, I’m hoping to polish past cards where this tool was used inappropriately. For example, [Puresight Merrow](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puresight+Merrow) shows all the cards it exiles with the "[Oblivion Ring](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) treatment," when it doesn’t actually care about the exiled card anymore.


Perploucksing Chimera
---------------------


As usual, here’s a disclaimer on the designs I talk about in this article: These ideas are not necessarily a promise of things to come. Instead, they serve to illustrate the design direction the team is working in. We're always trying new ideas, iterating on them, and reprioritizing the things we implement. Consider this a behind-the-scenes look into that process, not a preview of the end result. And as I've said before, any feature we implement means another feature that we don't implement. It's all about priority.


And that, my friends, is just one part of the journey that *Born of the Gods*  made from idea to **Magic Online**  set. I’m glad I get to share my part of the story with you. As usual, I love receiving feedback through Twitter, email, and the forums.


Thank you so much for reading,


-Jon












---
[Link to Wayback Machine](https://web.archive.org/web/20211021131203/https://magic.wizards.com/en/articles/archive/feature/state-magic-online-%E2%80%93-february-18-2009-2009-02-18)

[_metadata_:author]:- "Worth Wollpert"
[_metadata_:description]:- "Hi everyone. It's been a while since we've communicated our broader plans for the program in a forum like this, so I and a bunch of others thought it was time to update everyone on what we're currently working on, and what the plans are for the rest of the year. Gordon sent me a long list of his notes that he was considering posting (and of course we talk daily), and rather"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "682981"
[_metadata_:publish_date]:- "2009-02-18"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "State of Magic Online – February 18, 2009"
[_metadata_:wayback_capture_timestamp]:- "2021-10-21 13:12:03"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211021131203id_/https://magic.wizards.com/en/articles/archive/feature/state-magic-online-%E2%80%93-february-18-2009-2009-02-18"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/state-magic-online-%E2%80%93-february-18-2009-2009-02-18"
---


State of Magic Online – February 18, 2009
=========================================



 Posted in **Feature**
 on February 18, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/worth-wollpert.jpg)
By Worth Wollpert











Hi everyone. It's been a while since we've communicated our broader plans for the program in a forum like this, so I and a bunch of others thought it was time to update everyone on what we're currently working on, and what the plans are for the rest of the year. Gordon sent me a long list of his notes that he was considering posting (and of course we talk daily), and rather than do two separate posts, I've taken his stuff and consolidated it here with mine. 


For some of the folks not as familiar with the staff who I reference below, here is a cheat-sheet with some quick introductions!


Gordon Culp – Director of the **Magic Online** studio, responsible for most of the technical/dev stuff that we talk about.


Mike Gills – Community rep, tournament coordinator, MTGO organized play program manager type guy!


Adriana Moscatelli – UI specialist and the one who is responsible for overhauling **Magic Online**'s current UI.


On to the news ....


**Magic Online** has been doing well ... great, even. Our daily average concurrent user counts are definitely rising. New player counts are rising. Tournament entries are rising. Stickiness with the program is up, meaning actual time spent in client is up. Pretty much every metric we care about is up, even trading. For that, Gordon and I both want to thank you all, especially the folks out there who take their own time to evangelize for us and help out the influx of new players that I spoke of. I know I'm only mentioning a few of the many folks out there who deserve it, but I feel like bubba0077 and hamtastic in the main forums and MTGKaioshin and temepesteye in the bugs/tech help forum have really gone above and beyond and deserve some public praise. Thanks folks!


In Gordon's [last update](http://archive.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/other/101008) he mentioned that we were working mostly on problems with the current system and now that we're close to properly staffed up we've made some good progress on these things. Redemption is up and running well again, and we've also made some good progress cleaning up some further items on or list of architectural defects in **MOL** Version 3. We have reduced the memory usage of the game servers considerably, and *Conflux* will likely bring a rewritten Game Server Host server to the production system (pending successful testing, of course). *Conflux* beta users will note that they will see the game table immediately upon connecting to a game, regardless of whether their opponent has connected to the game yet or not. The client connection to game servers in general has been cleaned up and is far less likely to cause situations where the user really can't tell what is happening with their game table. There has also been some progress made on the client-side collection state issues that have continued to plague trading. If these fixes are validated in the *Conflux* beta, I believe users will see some significant increases in the usability of the current client.


We're pretty happy with the system's performance under the aforementioned steadily increasing user and activity loads. I see some particularly good signs from the **Magic Online** economy when I go over the data with our analysts. Our efforts to promote Constructed are definitely working, and overall card values are markedly up since even a few months ago. Lots of things happened to help here, redemption, pauper, 2 & 4 person queues, promos, more new players .... The list goes on. The tournament team that meets regularly to address these sorts of things has helped greatly, and Mike G. has done a great job of leading that team and listening to all of you. 


On our larger development projects (Leagues, UI, and collection server), we have been working diligently to do more and better specification and design work before digging into the development.


In the future, we will be able to give a rough idea of when users can expect all of these features to be complete and/or in beta. Gordon previously ruled out Q1 2009, we can also rule out Q2 at this point. Not the news everyone was hoping for, probably. We're in the same camp, but things have proven a bit harder than originally thought, and some of our specs were inadequate for the new philosophy, so revisiting all that has taken time. We are also still very much exploring the outsourcing of specific modules (like Leagues) to outside vendors and integrating their work into our system. It's important to keep in mind that a good portion of the total work in software development is the completely upfront creation of a concise and tight technical specification (a.k.a. spec or spec doc). One of our tech writers likes to quote that it takes (on average) about 15 minutes to fix a problem with a spec before code is written and two dozen *hours* to fix it after. Pretty crazy.


The collection server is still being spec'd and designed. This will be pretty major open-heart surgery on the system, and we simply have to have a very tight plan to get it right. With that in mind, we have and will continue to put more effort and priority into improving trading in the current client and escrow system with our upcoming set releases. We believe *Conflux* will bring some relief to the traders out there, big and small. Gordon is hoping to get some third-party trading bots operating in the *Conflux* beta so that we can work any issues directly with the bot developers before *Conflux* goes out. As of press time, we should have some bots running in the beta and generating data for us.


Our third major initiative is a significant upgrade to the client's usability. As with Leagues, we have been carefully documenting and spec'ing out this work, and we will soon be actively working on implementing the new design. We are talking a lot about how to balance an open communication plan with managing expectations. We want to build confidence in our UI design and dev capability in the community without painting Adriana's team into a corner by releasing screenshots of prototypes and such too soon. Mike G. and other community folks will be providing details about our plan to keep the community up to date and confident that we aren't going to deploy a sub-standard usability experience again.


The UI work is going to take awhile, so we will be continuing to apply minor improvements to the current client. Our plan right now is also to ship leagues in the current client. I promise that when we have something we're comfortable showing on the UI that we will, and with enough time to solicit and integrate feedback. We've already run multiple testing passes on actual **Magic Online** players to get things started, and without speaking for her too much, Adriana is very focused on community feedback. 


You may be wondering, "What am I going to see first of the three major initiatives?" It's still a little too early to tell, and we're just wrapping up specs on some of them. I don't really want to get into timelines anymore, since we all know how well my countdown timer went over. : ) I can promise two things for sure: we'll be hard at work until everything is finished, and the second they are, we'll let you know. As I said before, the UI specifically is something you guys should be able to see (and comment on) pieces of along the way. I'll try to wrangle Adriana into writing something up about the experience and status when she feels it's OK to start saying stuff. 


Please don't take the above as us resting until the three major features are ready. There should be continual updates, upgrades, improvements, bug fixes, and the like for the rest of time. The *Conflux* beta has a little something for everyone in this regard, and while I know nothing is quite as enticing as Leagues or a new UI, hopefully folks can find some enjoyment in at least a few of the new features in the mean time. Mike G. and company are in the final stages of preparing the rollout of the rewards program that ran into some roadblocks at the eleventh hour. He should have news on that relatively soon, so I won't scoop him too much ... but if you guys look at your promo tabs/binders you can see all the cards we've got the *ability* to give away, and there are more coming. Some pretty cool stuff in there, and it's not just for show! You folks will be able to get your hands on the coolest stuff in there soon enough.


That's all for now. I'll update any progress as information warrants, especially on the major features talked about above. Thanks again for making **Magic Online** great. We're riding some pretty impressive momentum right now, especially given the global economic climate, and that's all due to you folks. Until next time ....


Worth Wollpert  
 Sr. Business Manager, **Magic Online**








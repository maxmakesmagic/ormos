
---
[Link to Wayback Machine](https://web.archive.org/web/20210502074432/https://magic.wizards.com/en/articles/archive/making-magic/day-loucks-2013-06-05)

[_metadata_:author]:- "Jon Loucks"
[_metadata_:description]:- "Hey, I'm Jon Loucks! I'm a new digital designer in Wizards R&D. Some of you know me from the Limited Resources podcast. Not too long ago, I was in the Top 8 of the Great Designer Search 2. Years ago, I wrote strategy articles and enjoyed building rogue decks. I've spent the last few years working as a game designer at Microsoft and Amazon. Now I'm finally at Wizards of the"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "682601"
[_metadata_:publish_date]:- "2013-06-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "A Day in the Loucks"
[_metadata_:wayback_capture_timestamp]:- "2021-05-02 07:44:32"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210502074432id_/https://magic.wizards.com/en/articles/archive/making-magic/day-loucks-2013-06-05"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/day-loucks-2013-06-05"
---


A Day in the Loucks
===================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on June 5, 2013 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_jonloucks.jpg)
By Jon Loucks




 Jonathon Loucks is a digital designer in Wizards R&D. As a civilian, he enjoyed playing and writing about rogue decks. Later, he co-hosted the Limited Resources podcast. Now he works on the many facets of Magic Online.
 







Hey, I'm Jon Loucks! I'm a new digital designer in Wizards R&D. Some of you know me from the [Limited Resources](http://lrcast.com/) podcast. Not too long ago, I was in the Top 8 of the [Great Designer Search 2](/en/articles/archive/great-designer-search-2-2011-03-07-0). Years ago, I wrote strategy articles and enjoyed building rogue decks. I've spent the last few years working as a game designer at Microsoft and Amazon. Now I'm finally at Wizards of the Coast, and I'm working on **Magic Online**!


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat250a_choice.jpg)[Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations) | Art by [Tim Hildebrandt](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Tim%20Hildebrandt%22%5D)


I give **Magic** a lot of credit for shaping my life. **Magic Online** is a big part of that, too. It let me hone my skills so that one day I could play on the Pro Tour. It kept me connected with friends even when I was out of town for the summer. It let me connect with an entire community of people in an awesome way by streaming. It entertained me for more hours than any other videogame has, by far.


I love **Magic Online**, and I want it to be as good as it can be. It has done so much, yet it can do even more. That's why Wizards of the Coast hired me into a whole new position—the digital team is growing. A lot of smart and passionate people are working to take **Magic Online** to the next level, and I feel honored to be a part of it.


A question I frequently get from people interested in the game industry is, "What's your average day like?" It's such a weird industry, who knows what we do! Sometimes I wonder myself. The days can be very different depending on the current project, but I'll give you a run through of my "average" day.


### The Joy Loucks Club


I pull into work around 9 a.m. I grab some yogurt from the robo-convenience store (paying with my fingerprint) and then head to my desk, right next to [Shawn Main](http://www.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main). He eagerly says hello. I ignore him and boot up my computer. I'm greeted by this card open in my browser:



![Choice of Damnations](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Choice+of+Damnations)

 

For a moment, I'm very confused. Why is this here? What was I trying to tell myself?


So I boot up the **Magic Online** beta. ([Want to play on the open beta? Download here.](/en/articles/archive/2011-10-17)) I assume that if I go through the process of resolving the spell, I'll remember why I was looking at it. Time to use the Avatar of Congress! This is how we create all kinds of scenarios in order to test cards on **Magic Online**. I have a deck with sixty Mountains and an Avatar of Congress just for this purpose. I create a solitaire game, and I'm off!


(Did you know you can create solitaire games? On the beta client, it's in the play lobby under "Multiplayer Options," right at the top of the list. It treats you as your own opponent, which can cause some strange interactions, but it can be useful to get a feel for a deck before jumping into a tournament.)


Thanks to the AoC, I can do all kinds of things! Like...


* Create all manner of mana
* Search up any card from my library or my collection. (Luckily, I've got four of everything!)
* Give my creatures haste.
* Deal some damage.
* Draw some cards.
* DEPLOY BEARS!

Deploy Bears is how we quickly set up a complex board position. It puts a bunch of creatures on the battlefield, suspends a card, throws a flashback card in the graveyard, puts a split card in your hand, and more!


So why did I make a note of [Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations)? Let's find out. I deploy Bears to set up a board. Then I wish for a [Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations) and cast it using Avatar of Congress. I target myself, since I'm in solitaire. I have eighteen permanents, so I choose the number fifteen. "Have TesMonkey001 lose 15 life?" I click No. "Sacrifice three permanents."


Well that seems in order...but wait! There are buttons!


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat250a_truechoice.jpg)I click No, and nothing happens. I click Yes, and nothing happens! Somehow these Yes and No buttons got carried over into the implementation of [Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations), yet have no function. Time to log a bug!


### If I Didn't Have Bad Loucks, I'd Have No Loucks At All


As I open our bug tracking software, I reflect on how the heck I got here in the first place. Why was I looking at [Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations)? I was looking at Cube cards the other day, browsing to see if there's anything we should fix before the next Cube draft, but I know [Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations) isn't in the Cube. I open up the Cube list to look at my notes, and the last card I looked at was [Balance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Balance). That's right! I was exploring cards that asked you to choose a bunch of permanents, seeing if there was any way that could be improved. Exploring the Cube has led me down some strange paths indeed.


So I enter the bug into our system. I check to make sure nobody else has filed the bug, then I fill out as much detail as I can, attach a few screenshots, and fill in complete reproduction steps. It's important that I'm thorough and detailed so the developer can find the source of the bug. Also, once the bug has been fixed, QA (quality assurance) can use my reproduction steps to verify the fix and close the bug. I should emphasize this paragraph—if you get into digital gaming, filing bugs is an important part of your day.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/feat250a_filebug.jpg)(Want to tell us about a bug you found? Have any other feedback? [Check out our feedback form.](http://www.surveygizmo.com/s3/1028055/Magic-Online-Wide-Beta-Feedback-Form))


The next important (and hopefully illuminating) step in a bug's life cycle is the triage meeting. A select group of designers, developers, and QA meet multiple times a week to "triage" newly filed bugs. One by one, the room looks at a bug, maybe discusses how difficult it might be to fix, and ultimately decides how important it is. This lets us schedule the bug for a time to be fixed in the future.


There are multiple buckets we can toss a bug into during triage. Sometimes it's a "must fix now," and it gets assigned to be fixed in our next release. (If it's REALLY bad we'll do a hot fix.) Sometimes it gets tossed into the "low priority future fix"—we hope to fix it one day, but it's not important that it be fixed in the near future. It's still good to track bugs that we know aren't going to be fixed soon, since we don't want people logging the same bugs over and over again. If we're lucky, sometimes these bugs get picked up along with a more important fix if they're in the same area of the game.


So what's the fate of our [Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations)? "Low priority future fix." Well, damn!


Sometimes, that's just how it goes. [Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations) just isn't a particularly relevant card. It's not in any recently draftable set, and it's not a highly played card. And it technically works, there's just some noisy UI involved. As much as I want to be able to fix every bug right now, fixing one bug means not spending time to fix another. I hope it's not a shock to you, but we've got bigger fish to fry than [Choice of Damnations](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Choice+of+Damnations).


Later in that same triage meeting, I get a win! I gave *Modern Masters* a once-over looking for cards that could be improved, and I stumbled on [Incremental Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incremental+Growth). The prompt box simply said "select 1st/2nd/3rd target." So I created an issue to change the text to "Select target creature to get one/two/three +1/+1 counter(s)." This way the player could easily tell what he or she is doing with each target, in the same way we treat cards like [Martial Glory](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Martial+Glory). Since [Incremental Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Incremental+Growth) is in a big new release, and it's a relatively easy fix, it will be fixed in time to release with *Modern Masters*. Success!




|  |  |
| --- | --- |
| 
Martial Glory
 | 
Incremental Growth
 |

After triage, I head to the weekly "Card Crafting" meeting. As the invite itself says, it's the best meeting ever! Each week, we talk about whatever topic needs talking-to. Something like the legendary rules change might start in a Card Crafting meeting. Sometimes it's more philosophical. Either way, it's bound to be a fun meeting, so I try to make it when I can.


Lunch time! If you see a group of people moving slowly toward the elevators, latch on. They usually won't notice you tagged along until you're ordering food, and by then it's usually too late to kick you out. I use this time to get other R&D members' thoughts on **Magic Online**.


### Under Loucks and Key


Back at work, I've got an email about the upcoming fixes in **Magic Online**. There are more than 100 resolved issues, and I note a few of the highlights:


* A good number of crash fixes. As we move closer to a V3-off world, crash fixes are an increasingly high priority.
* The profanity filter is now set to default on.
* The Gideon theme becomes the only theme. We've had some time trying out all the themes, and Gideon is a clear standout. We're turning off the other themes until the day we can give the feature enough love so that every theme shines.
* Fixed an issue with collection quantity filters. Sometimes cards of 0 quantity would show up in the 1+ quantity filter due to different owned versions.
* Some of the context windows in the collection scene were slow to appear due to a fade-in animation. They now appear instantly. While a somewhat small issue, it speaks to our desire to increase the speed of the client. Sometimes that means speeding up load times, and sometimes that means tightening up UI reactions.
* Collection load times have been improved. As we move closer to V3-off, we have to be more careful with risky changes. We've mproved collection load times in the low-risk ways we can, and after V3 is off there are some higher-risk changes that will make collection loading even faster.
* We moved the quantity indicator for a stack of cards when they tap—that way it no longer covers up the power and toughness.
* Clicking F2 no longer selects "Yes" if the prompt box is presenting a Yes/No choice. This was leading to accidental Yes clicks as players tried to move through the turn quickly using F2. Now, F2 consistently only shortcuts the "ok" button.
* Right clicking on a stack of creatures now brings up an option to attack with every creature in that pile. This should speed up attacking with a bunch of tokens. (You can still right click on the battlefield during the declare attackers phase and choose "attack with all creatures.")
* There's now an option to disable animations during game play. This will give players with slower computers an option to help performance.

### Better Loucksy than Good


It's almost 2 p.m.! That means the weekly **Magic Online** test tournament is about to start. As is usual, I rush to find the email with the link to the most recent build and install it. I log in with my test account and join the tournament. Ten in the queue!


The event fires, and it's *Return to Ravnica* Block Sealed this week. I see a pool with a juicy combo, but it's in four different colors! Good thing I have all these Cluestones and Gates—it's time to build five-color surprise.


Eventually, I get paired against my boss, [Ryan Spain](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ryan%20Spain). He sits across from me. Playing **Magic Online** with somebody sitting directly across from you is what we call "battleshipping." I had yet to assemble my combo, but I had a good feeling about this round...


Turn-one [Dryad Militant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dryad+Militant) from Ryan. On the play. Uh oh.



![Dryad Militant](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dryad+Militant)

 

My first play is a Cluestone.


Then a [Haunter of Nightveil](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Haunter+of+Nightveil) stems the bleeding.


Then a [Zhur-Taa Ancient](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zhur-Taa+Ancient) comes down and powers out a [Pit Fight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pit+Fight).




|  |  |
| --- | --- |
| 
Zhur-Taa Ancient
 | 
Pit Fight
 |

Then I [Mind Grind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Grind) Ryan for eleven. Surprise! Ryan draws the last card in his library and concedes. I see a single tear slide down his cheek. True story.


Just another typical average completely normal day at the office in which I beat Ryan Spain at **Magic**.


Through playing in the tournament, I noticed a few issues to research. I track down the meaningful people, such as [Dave Marsee](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Dave%20Marsee), UI designer, or Peter Beckfield, card coder. Sometimes I find the answers I need and there's no issue, and sometimes a new bug gets created. It's important to the team that we keep playing **Magic Online** from the inside, so we can keep up with the changes, find any bugs, see the result of our hard work, and find the next area that most needs our help.


It's off to my last meeting of the day with the **Magic Online** business team with a face you may be familiar with: [Chris Kiritz](http://www.wizards.com/magic/magazine/archive.aspx?author=chris%20kiritz). (As much as I try, the name "Kiritz Top" won't stick.) I'm mostly an observer in these meetings, learning about prize structure and event scheduling and all kinds secret future things. I bring up this meeting because interfacing with other teams is an important part of my day.


At the end of the day I tend to have some open time to spend as I see fit. Usually I'm writing up a feature to pitch to the team later in the week. Or typing up loose ends created in emails throughout the day. Or exploring more Cube cards to look for improvements. Or peeking ahead at upcoming sets, both for my own curiosity and to prepare myself mentally for new mechanic implementation on **Magic Online**.


On this fictitious day, I use my free time to finish writing my article. I thank my audience for reading and look forward to the next time I get to write to them!


Goodnight, and good Loucks.










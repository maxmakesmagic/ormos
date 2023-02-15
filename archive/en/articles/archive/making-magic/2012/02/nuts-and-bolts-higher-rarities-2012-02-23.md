
---
[Link to Wayback Machine](https://web.archive.org/web/20170607050304/http://magic.wizards.com/en/articles/archive/making-magic/nuts-and-bolts-higher-rarities-2012-02-23)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "194086"
[_metadata_:path_date]:- "2012-02-23"
[_metadata_:publish_date]:- "2012-02-27"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Nuts and Bolts: Higher Rarities"
[_metadata_:wayback_capture_timestamp]:- "2017-06-07 05:03:04"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170607050304id_/http://magic.wizards.com/en/articles/archive/making-magic/nuts-and-bolts-higher-rarities-2012-02-23"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/nuts-and-bolts-higher-rarities-2012-02-23"
---


Nuts and Bolts: Higher Rarities
===============================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on February 27, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 







Three years ago, I wrote a little column called "[Nuts & Bolts](http://archive.wizards.com/Magic/magazine/Article.aspx?x=mtg/daily/mm/21)," where I intended to show off smaller technical issues the designers have to deal with every day. I started with card codes to explain how designers label and keep track of a file. Certain readers were very fascinated by the idea of a card file, so the following year I wrote an article explaining [the concept of the design skeleton](http://archive.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/mm/78), a tool used by designers to create the initial file.


![](https://media.wizards.com/images/magic/daily/mm/mm184_hacker.jpg)[Magical Hacker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magical+Hacker) | Art by [Doug Chaffee](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler)


It was clear that this subset of readers was very interested in how to make their own design skeletons, so the next year I wrote a column about [filling in the design skeleton](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/132). While the "Nuts & Bolts" columns have drifted slightly from my original intent, it's clear that having a series of "how we make card files" columns has enough support that I've chosen to write a new one every year. That means today's column continues with everything I talked about in the first three. If you haven't read them, I strongly urge you to, because this column will assume you have. Okay, let's continue making a card file.


* Previously, in Nuts & Bolts

[Last year](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/132), I talked about filling in the design skeleton at common. (And once again, if you haven't read the previous "Nuts & Bolts" columns, I strongly urge you to do so.) This year I'm going to add in a few more issues for common and then I'll talk about filling in the higher rarities.


![](https://media.wizards.com/images/magic/daily/mm/mm184_con.jpg)[Aesthetic Consultation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aesthetic+Consultation) | Art by [Dave Martin](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler)


The set in question is *Justice* from the *Truth*, *Justice,* and *The American Way* block. (All of this is 100% made up for this column.) It's a small set with 145 cards—60 commons, 40 uncommons, 35 rares, and 10 mythic rares. The set is a graveyard-themed set evolving the gravetwist mechanic from *Truth*.


Last column, I talked about filling in the commons in the design skeleton. My original plan was to start with uncommons today, but I realized something big happened in the last year that makes me need to talk a little more about filling in the commons.


* The Commons

The "something big" that happened is what R&D calls New World Order (NWO). I wrote [an entire article about it](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/172) last December. I'm going to talk about it a bit here but I suggest you read the column on it if you haven't already. (Yes, "Nuts & Bolts" columns have a lot of required reading.) New World Order was something R&D originally put into place to help lower the barrier to entry for new players but ended up also bringing clarity to the game. The end result for design is the NWO forces us to be more conscious about how much complexity is going on at common.


Here are some NWO questions you have to ask yourself while filling in the common slots:


1. How difficult is this card to understand? Can you read it and then understand what it does? We call this comprehension complexity. Cards that aren't very clear tend to be moved to higher rarities or even just removed altogether.
2. How much interaction does this card have with the other cards on the battlefield? Does having this one card make you have to reevaluate every other card on the battlefield? We call this board complexity. Cards that significantly raise the number of options available on permanents on the battlefield tend to be moved to higher rarities. Another way to think of it is this: If your card has the ability to affect numerous other permanents in play, unless that use is very restricted, we tend to push the card up to at least uncommon.
3. Does this card add extra strategic evaluation? Will a better player gain advantage from understanding how best to use it? We call this strategic complexity. As long as this card does not break either of the two previous rules, we like having this type of card at common. This helps add a layer for the advanced player without making the game any harder to learn.



|  |  |
| --- | --- |
|  |  |

Note that you do get to have some complexity at common but it's restricted. As such, you need to make sure the complex cards you do have are helping you advance the major themes of your set. A common card that is setting off red flags (what R&D calls common cards that are breaking a guideline, meaning they have to be checked over before they stay at common) but isn't a key part of your design needs to move up to higher rarities or be stricken from the set. Be aware that being in theme doesn't allow a card that's overly complex for common to stay in common.


Another common issue that NWO cares about is one of focus. Most new **Magic** sets will make players care about something they don't normally care about. That's okay, but to help keep the set from being too complex, you have to choose your key focus point and restrict yourself to that (at common). For example, *Zendikar* cared about your land drop. That's not something players normally care about, but for *Zendikar* it was okay because that was the focus. Notice that the set didn't also make you care about some other aspect.


The lesson here is that your set should have some focus but you need to limit yourself to that focus. In other words, don't have five cards care about Thing A, five care about Thing B, and five care about Thing C. Instead, have fifteen care about Thing A. Note that you can have variance within that focus. *Zendikar*, once again, made caring about lands matter in multiple ways but it stuck to land drops as being the focus.


I'm going to talk about uncommons in a second, but before I do, I need to stress one last time that it's important to complete your commons before advancing onto the uncommons. Your first playtest wants to be all common because it's the best way to make sure your themes and mechanics are loud enough and focused enough. The higher rarities will allow you to add more complexity (which is a good thing—New World Order isn't trying eliminate all complexity, just to contain it to fewer cards per booster opening) but that complexity can make it harder to ascertain what your set is doing.


![](https://media.wizards.com/images/magic/daily/mm/mm184_mystic.jpg)[Mystic Retrieval](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Retrieval) | Art by [Scott Chou](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler)


A good design maxim is "Don't advance beyond common until your commons are getting the job done."


* The Uncommons

It's not important to do your uncommon design skeleton until the commons are roughly done. The reason is, the act of doing the commons will most often inform what uncommons need. What I tend to like doing is making a blank uncommon skeleton and only fill it in with requirements that come up while doing commons. These tend to be:


1. Inevitably, when you make commons, you will discover you have cards that don't fit at common. Part of this will be because of the New World Order, but an equal part will simply be running out of room. When you start a set, you have lots of cool ideas, and what you find is that the commons get cramped very quickly. The key to solving this problem is figuring out what needs to stay at common and what can be addressed at uncommon or higher rarities.
2. While designing your commons, you will hit upon the major themes of your set. Once you figure out what those are, you need to continue those themes at the higher rarities—especially uncommon. Going up in rarity will not only allow you to hit the themes again but also explore those themes in ways that wouldn't mechanically work at common
3. Tied to the last point, when working on commons, often you will come up with ideas that are too complex for common. In fact, it's a running joke in design that one of the ways I get uncommon cards is to ask my design team to design commons. Commons are very hard to make, and it's quite easy when creating them to make cool cards that aren't really common. When I get cards I like but I know can't be common, I'll throw them into an uncommon slot to remind me that I'd like to work them in if I can.

Once I have a working set of commons and start working on my uncommons, I like to make a list of all the things I've accumulated that I want to consider for uncommon. These things will fall into three categories.


First will be things that are necessary because they follow up on things you've established in common. For instance, you will have chosen your major focus and you will want to continue it in uncommon. This first category is things you have to work in if at all possible.


![](https://media.wizards.com/images/magic/daily/mm/mm184_wish.jpg)[Make a Wish](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Make+a+Wish) | Art by [Howard Lyon](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler)


The second category is things that tie into what you are doing but aren't inherently part of the structure. An example of this would be a card that's very in-theme for the set but has no specific role. It's important to have a list of cards from this category because it will help inform you when you are making less clear-cut decisions.


The last category is things that are nice in a vacuum but don't particularly advance any element of the set. These things should in no way shape what the set becomes. Too often in early design, a designer will warp the set to fit in elements that are essentially superfluous. Be careful not to do that.


To recap, the first category should help shape your uncommons. The second category should help guide you when you are unsure which path to take. The third category should never guide you, as it will cause you to make concessions that should never be made. This isn't to say things from the third category cannot get into the set; they just shouldn't have any say in shaping it.




|  |  |
| --- | --- |
|  |  |

Now that you have sorted through the material created while making commons, it's time to start on your uncommon design skeleton. You want to do this just as you did your commons. Keep the creature-to-spell ratios the same, although you have a little more wiggle room if you need it. In the previous versions of this column, I actually mocked up the design skeleton, but as I haven't actually gone through the work of designing the commons, it's hard to accurately reflect how my uncommon design skeleton would look.


You will want to put the uncommon design skeleton together the same way as the common one. (See [the original design skeleton article](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/78) for how to do this.) The biggest difference will be that you are not starting with a blank slate. Remember that the first category items will help you inform decisions about what uncommon needs to have. As I explained last year, start with what is mandatory and work your way out from there.


![](https://media.wizards.com/images/magic/daily/mm/mm184_brim.jpg)[Brimstone Volley](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brimstone+Volley) | Art by [Eytan Zana](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler)


Here are a few very important things to understand about uncommons.


First, if you think commons got cramped, you haven't seen anything yet. Uncommons are famous among **Magic** designers for being the pinch point of the set. They get pushed up from common for complexity and down from rare to matter more in Limited, making for a very tight fit. Uncommons do just as much work as commons but in 66% the space (60% in large sets). What this means is that you have to be very careful with every card. Cards that aren't serving a specific purpose will get forced out.


Second, a lot of designers seem to misunderstand the impact of uncommons on Limited (and casual Constructed, where players don't buy a lot of booster packs). One of the best ways to explain this is to talk about a concept R&D calls "as-fan." As-fan talks about the chance of something showing up if you opened a random booster pack. Often, the lead designer (and later the lead developer), will pick a level the team is trying to hit for a certain aspect of the set. For instance, let's say we decide the new mechanic gravetwist is crucial to the feel of the set. To make sure it has the impact needed, we might set the as-fan at two. This means that, on average, two cards out of every booster pack will be gravetwist cards.


When calculating this number, uncommons are half the rate of commons. So let's say the math says you have to have twenty cards at common to hit the ratio you need. (Note that my example is on the high side for as-fan of a mechanic.) Every two cards at uncommon count as one common card. So instead of having twenty common cards, for example, you could have fifteen commons and ten uncommons. My point here is that, while commons do the lion share of your work, uncommons are still very relevant to ratios. (Sorry, but these "Nuts & Bolts" columns can get a little math-y.)


When putting together your uncommons, here are the major roles to keep in mind:



> 
> * **Filling In Your Theme**—Commons serve as a great boilerplate for your set. From them, you will start to figure out what your set is about. Whatever that is, it must also show up in uncommon. I always talk about how your theme has to show up in common. It also wants to be in uncommon as well.
> * **Upping the Size of Your Creatures and Spells—**I often talk about how commons are limited by complexity, but they are also restricted by size. Most colors don't have creatures with a power greater than 3 at common (blue usually has one and green has one or two). Also, common effects tend to be smaller in size. Uncommons allow the designer to step up the size of his creatures and spells.
> * **Providing Complexity—**When I talk about New World Order, I tend to stress getting complexity out of common. What I talk less about is making sure complexity does get put into the other rarities. NWO isn't about removing complexity from the game, but rather shifting where it sits. I firmly believe complexity serves the game, I just think it does so in smaller, less common chunks. Uncommon is important because this is where the crux of your Limited and casual Constructed complexity sits. When working on your uncommons, make sure you use it to add twists to your themes and mechanics.
> * **Helping Players Win—**One of the things you learn in all-common playtests is that **Magic** needs the ability for large turnovers to happen. Yes, the game can look like it's going your way, but to keep up the suspense there always has to be the chance for the opponent to come back. (This is also known as a "[catch-up feature](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/174).") This can come in the form of board sweepers that clear the battlefield. It can be large creatures that can turn the tide of battle. It can be sweeping effects that help you gain control of the game. The biggest of these come in rare and mythic rare, but you need to have a few in uncommon to make sure that every deck has some chance to turn the game around.
> * **Shaping Draft—**Another very important role is the one uncommons play in Limited. Rares and mythic rares happen at a low enough frequency that the designers can't use them to influence how Draft plays out. Uncommons, though, do show up enough that you can start weaving in Draft-relevant cards. One of the most frequent uses for uncommon is to create cards for players to draft around. Usually these cards are too focused for common but they work well at uncommon. The idea being that if a player opens this card in the first pack, that player can shape a draft around it. A few cards like this sprinkled through uncommon can add important depth to a Draft environment.
> 


As you can see, there's a lot going on in a very tiny space. Just as making commons gets you uncommons, so will making uncommons get you rares.


* Rares

It might not seem so at first glance, but rare is the rarity with the most breathing room. The main reason for this is that most of rare's responsibilities are providing excitement, not structure. Splashy cards take up less room than all the infrastructure common and uncommon need to make the game work.




|  |  |
| --- | --- |
|  |  |

The advice for making rares follows much of what was said about uncommons. You don't need to make your rare design skeleton until uncommon is done. Also, as you make rare cards while filling in uncommon, stick them into empty slots at rare. Another reason rare has more freedom is that you are less locked into creature percentages. Every color should have both creatures and spells, but the requirements are much looser at rare.


Does rare need any structure? A little. You will probably have at least two rare cycles. One following up on the themes of the set, usually with some new twist. The other being some splashy cycle that is more distant from your themes—something to excite players who might not be all that enamored of your main theme. Also, be aware that you might want a vertical cycle or two. That's when a cycle has a card in common, uncommon, and rare/mythic rare all in the same color.


So what responsibilities do rares have?


1. **Make Exciting Cards—**Commons make sets play well, but rares (and mythic rares) sell sets. The role of your rares is to make splashy cards players want to put into their decks. There are a few ways to do this:
	1. **Make The Card Big—**I talk about how many Timmys are drawn to the large creature or spell. This phenomenon is not limited to Timmys. Everyone enjoys casting a spell that has a huge impact on the game. It gets the blood pumping and leads to great stories. Most of all: it's fun!
	2. **Make the Card Efficient—**Big cards might make the splash, but efficient cards win games. The trick to making these cards rare is to pinpoint their effect. They don't do just anything, but they do the thing they're made to do very well.
	3. **Make the Card Flavorful—**We've learned that the cards that preview the best are ones that drip with flavor. Players can't always gauge power but they can instantly gauge coolness. Make the card resonate and players will flock to it.
	4. **Make the Card Unique—**Another surefire way to excite players is to do something they've never seen before. **Magic** is a game of exploration. Players always like to discover new things. Note that you shouldn't have too many totally unique rare cards in your set. A little goes a long way.
2. **Make Even Larger Creatures and Spells—**Just as uncommon steps it up from common, so too does rare step it up from uncommon. Rares are allowed to have giant size or huge effects. When a player plays a rare, the game is allowed to *feel* it.
3. **Win Games—**Uncommons help you win. Rares (and mythic rares) just win. **Magic** needs its bombs, and to keep from ruining Limited these bombs are kept to rare and mythic rare.
4. **Get Complex—The game of Magic** doesn't need a lot of cards you have to read twice to understand, but it gets to have some. These wordy creations live at rare. Note that we tend not to put the super complex cards at mythic rare because we like mythic rares to be a little more straightforward. That means rare is the sole home for the über-complicated cards.



|  |  |
| --- | --- |
|  |  |

One of the best tests for a set is to let a new player look at only the rares and mythic rares. If that bundle of cards doesn't excite them, you have a lot of work ahead.


* Mythic Rares

Of all the rarities, this one is the most about feel. The line I like is this: "Every mythic rare has to have the potential to be awesome."


That means that when players see a mythic rare, they have to be able to dream of something wonderful happening. The best-case scenario is one you'd tell stories about for years to come. This doesn't mean it has to always happen, just that the possibility is there.




|  |  |
| --- | --- |
|  |  |

This description is fuzzy, I know, and what is awesome to one player might not be awesome to another. The goal is to make sure the card excites its own audience. Players who don't love flavor, for example, might not care for every legendary creature, but that's okay. As long as each card has an admirer and each player has a mythic rare to lust after, you're doing your job at this highest rarity.


* Skeleton Complete

There's everything you need to finish filling in your skeleton. Please be aware that what I'm talking about today is very difficult. It takes a long time and many passes to fill in the skeleton, and even once you do your work of designing a set is just beginning. But hey, that's a topic for next year. I hope you enjoyed this year's "Nuts & Bolts" column. I'm curious to hear any feedback you might have. ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), my email, the thread to this column. You have lots of choices.)


Join me next week when I put you all in fate's hands.


Until then, may the cards flow.




---

 

![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_location_static.png)![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_go_active.png)![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_go_static.png)
![](https://web.archive.org/web/20121110024559id_/http://www.wizards.com/mtg/images/daily/features/banners/DKA_ArticleFooterBanner_FNM_Top.jpg)[![](https://web.archive.org/web/20121110024554id_/http://www.wizards.com/mtg/images/daily/features/banners/DKA_ArticleFooterBanner_FNM_Button01_Static.jpg)](http://staging.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/darkascension/productinfo)[![](https://web.archive.org/web/20121110024606id_/http://www.wizards.com/mtg/images/daily/features/banners/DKA_ArticleFooterBanner_FNM_Button02_Static.jpg)](http://gatherer.wizards.com/Pages/Search/Default.aspx?sort=color+)







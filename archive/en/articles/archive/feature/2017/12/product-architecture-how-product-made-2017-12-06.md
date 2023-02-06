
---
[Link to Wayback Machine](https://web.archive.org/web/20171207162657/https://magic.wizards.com/en/articles/archive/feature/product-architecture-how-product-made-2017-12-06)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/product-architecture-how-product-made-2017-12-06"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20171207162657id_/https://magic.wizards.com/en/articles/archive/feature/product-architecture-how-product-made-2017-12-06"
[_metadata_:wayback_capture_timestamp]:- "2017-12-07 16:26:57+00:00"
[_metadata_:publish_date]:- "2017-12-06"
[_metadata_:description]:- "Ever wondered how a Magic product is made, from start to finish? Product Architecture is your monthly look at our product architecture process."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Product Architecture: How a Product Is Made
===========================================



 Posted in **Feature**
 on December 6, 2017 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorPic_GavinVerhey.jpg)
By Gavin Verhey




 When Gavin Verhey was eleven, he dreamt of a job making Magic cards—and now as a Magic designer, he's living his dream! Gavin has been writing about Magic since 2005. 






Have you ever wondered how a product is made at Wizards, from start to finish?


Sure, if you're an avid DailyMTG reader you have probably seen a fair number of glimpses into how we design sets, thanks to Mark Rosewater. And articles on both development and play design have covered those aspects of things pretty well.


But there's so, so much more to product creation than that.


I'm on the Product Architecture team, a team I introduced a couple months back. Feel free to check out [that article](https://magic.wizards.com/en/articles/archive/feature/building-better-magic-set-2017-09-27) if you need a quick refresher. I received a lot of positive feedback on that one, and, after talking with esteemed DailyMTG editor Blake Rasmussen, we decided to try making this a monthly column! You can expect me to bring you monthly looks under the hood of *Magic*'s architecture once a month for as long as you keep enjoying it.


And today's topic is something I directly work on, day in and day out: building our products and helping make sure all aspects are as great as possible!


Today, we're going to be following along with the creation of what you all now know as *Explorers of Ixalan*!


![](https://media.wizards.com/2017/images/daily/yc05EKw2Qd.png)


This new experience combines *Magic* with a bit of a board-game element, as you uncover tiles for special effects. It's probably not like much you've seen before, and it's a good blueprint for what doing something new looks like. You can learn all about it [here](https://magic.wizards.com/en/products/explorers-ixalan). It may be worth taking a quick look at what's inside before going forward, if you don't already know.


Every process is a little bit different, and *s* is no exception. But enough preamble—let's get to the fun part!


Boot up your time machines, everybody. And while those warm up, let's have a bit of a prologue, shall we?


Prologue – The Vision Document
==============================


You might have heard from Mark Rosewater about the design handoff vision document. This is a much different thing—and happens a lot earlier.


Every Tuesday, we have a meeting called *Magic* Strike Force. This meeting gathers members from the major teams inside Wizards responsible for creating a product: R&D, Brand, Sales, Retail, Packaging Design, Graphic Design, and many, many more.


As the name implies, this is where a lot of major strike decisions are made—and where a product is first presented.


The vision document comes from Brand. Their goal is to shape the canvas R&D is going to try and paint on in the next step. It gives us the general description of what they are looking for.


Now, sometimes it's Brand coming up with a goal and asking R&D to create something new to fill it. Other times, R&D has a general idea of something new to do, they recommend it to Brand, and Brand writes up a vision document of what they are looking for to give us some specifications.


*Explorers of Ixalan* is a bit of a third kind of case, however.


How many of you have ever heard of Annex?


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Annex)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annex)
No, not the card [Annex](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annex)! The product line Annex.


Know that one? I'd be surprised if you did.


"Annex" is an internal code name used for a special line of products we started with *Amonkhet*. The idea is that they would be "complete experiences in a box" released after the set they were associated with.


We did one of these with *Amonkhet*. How many of you can guess what it was?


Here's your answer:


![](https://media.wizards.com/2017/images/daily/X4aEhWQxxy.png)


*Archenemy: Nicol Bolas* was the first product in the Annex lineup. *Explorers of Ixalan*—or, as it was known, "Ham Annex"—would be the second. ("Ham" being the code name for *Ixalan*.)


One important note on this: because Ham Annex was continuing an existing product line, Brand didn't need to re-present a vision document. The vision document was originally written for the entire line, and it still held true.


What did it look like? Well, I'm going to show you!


Before diving in, I want to note that this may appear a little formal and jargon-heavy. But considering the weight these presentations carry—they are the backbone of an entire product line—they need to be.


Ready? Take a look!




---

"HAM ANNEX"
===========


*I love the new settings that* Magic *introduces twice a year, and now there's a cool way for me to experience those planes in a completely new way each time!*


**SECTION 1 – VISION**


**What are the goals and business objectives of this project?**


The primary goal of this product is to highlight the key flavor and mechanical elements of the current block. It should resonate with themes in that plane to create a play experience that feels rooted in that plane.


With more and more of our specialty products being focused on booster products, there are few casual expressions of *Magic* that are available in ready-to-play formats. To that end, this product should be focused on play (rather than collectability). The product will need to allow players to play the product with or against each other.


**Who is the customer, and why does the customer need the product?**


Similar to *Duel Decks*, the primary customer for this product is the Interested *Magic* player. These players are engaged in the brand, but tend toward social "kitchen table" play over competitive play or playing in store events. The Lapsed player is very similar to the Interested player in the context of this product. Both player segments will value the "ready-to-play, just add players" nature of this product.


Since this product will explore the current plane in a deeper way than any other play product, this offers an opportunity to create a compelling game product that will appeal to the Vorthos player. It will offer this player a unique look at the world and story and how it plays out in the game.


While the focus of the product will be on Interested players, that is not to say that the product won't (or shouldn't) be appealing to more engaged and/or competitive players. This product should include cards that are appealing to a variety of player types. It will offer a great *Magic* experience that current players can use to play, expand their collection, or mine the contents to improve their own Constructed decks.


**Where, when, and how might we deliver this?**


This product should be considered part of the suite of products for each block, and is recommended for a release with one set of the block, not both. The specific release date is very flexible.


The shape and scope of this product will, by design, change with each block. The guidelines spelled out in the goals above require a setting-based, flavorful, ready-to-play experience. The product should include multiple versions, or offer multiplayer play options.


An example of what this could be: Zendikar might be a variety of Zendikar-themed decks and a "boss" Eldrazi deck to provide a challenge deck–type of experience. The product could leverage existing specialty product play experiences as appropriate. *E.g.*, *Archenemy*, *Planechase*, *Conspiracy*, *Challenge Decks*, etc.


To what degree it is possible, this product could highlight the key story beats of the block.


MSRP is flexible based on the specifics of any given release.


**How will we measure the success of this project?**


Sell-through and fan reaction will be the key metrics for measuring the success of this product. It will be critical to monitor fan reaction and apply those learnings to future products.


SECTION 2 – BUSINESS PRIORITIES
===============================


**Scope Includes**:


*Must Haves:*


* Ready-to-Play product
* Multiple versions and/or multiplayer options
* Play experience with strong connection to current block setting—both flavor and mechanics
* Casual, fun-focused play experience

*Nice to Haves:*


* New Art
* Use of classic/famous cards from past sets
* Use of non-booster block cards (i.e., those included in Sample Decks)
* Planeswalkers
* New Cards
* Preview cards
* Leverage existing specialty product play experiences
* Options for retailers to use product to engage Interested players in-store

*Scope Excludes:*


* Requirement to be legal in any specific format

**Notes for Project Management Organization.**


The vision document will be consistent from block to block, but will require a new request doc from R&D for each block. It will likely need to be greenlit each time, as the contents and quantity could vary from block to block.




---

So, in this case, the vision document was already in place. This is what R&D knew about.


And that means th—what's that? I think I hear your time machine dinging that it's ready!


Set your coordinates for January 2016! Here we gooooo!


January 19, 2016 – The Request Document
=======================================


Our story for this product actually starts a little in advance of this moment.


Since we knew that we were going to need something for Ham Annex, pre-work had been done in exploring what we could do here. About eight weeks in total were spent trying different iterations and investigating how this would work. There were some brainstorms about what kind of experience it should be. Shawn Main came up with some early iterations involving reaching achievements that were listed on board. All good starts.


But it was *Magic* designer Peter Lee who really cracked the nut of combining hexagonal tiles with mana payments and achievements. Once that system was discovered, the floodgates opened—and good thing, too, because it was about time to present the R&D request document to Strike Force!


![](https://media.wizards.com/2017/images/daily/F4Q6aLfHDR.png)


If the vision document provides the canvas for R&D to paint on, the R&D request document provides the paints. This serves as a guide to what is going to be in the product. And while removing things from the list is possible after this is presented, adding things can be much harder.


Why? Because, once it's approved, every team is building toward this list!


Structural Design is working on prototyping the box and components. Brand and Retail are figuring out marketing and sales strategies. R&D designers are working toward designing it. And so on.


Changing anything on this document after it is presented, discussed, and approved could cause other departments to change their work. While that does certainly happen from time to time (as you will see in a moment), we try to avoid it where possible.


So, what does this thing look like? I'm glad you asked!


Here's the R&D Request Document for "Ham Annex."




---

R&D Request Doc – Ham Annex
===========================


This is a boxed experience representing the four factions in the Ham world searching for the golden city.


### Details


The goal of this SKU is to deepen player engagement with story and provide players a unique play experience right out of the box.


Ideal contents of each unit:


* 4 60-card theme decks (a)
* 50 hex tiles (b)
* 1 game board (c)
* 1 insert (d)
* 4 spindown dice (e)
* 4 tuckboxes (f)
* Up to 35 tokens (g)

This should be priced at approximately $60.


### (a) 4 60-card theme decks


Four 60-card decks themed around the Ham factions. The decks would contain only reprints, including cards from Ham (approximately 50% of the nonland cards). Each would contain one premium foil card and approximately six to ten rares. Around 20 cards would have new art. A new expansion symbol will be needed.


### (b) 50 hex tiles


50 hexagonal cardboard tiles. The back sides would have one of three different pieces of map art. The fronts would contain rules text and three location tiles would have art. Approximately 1.25-inch sides.


### (c) 1 game board


A folding cardboard game board with map art and a hex grid to indicate how to lay out the tiles and rules reminder information in the corners. Roughly 20 inches square with one fold. Wrapped edges and a black back.


### (d) 1 insert


A product-specific insert that contains rules information and information about the decks and story.


### (e) 4 spindown dice


Four 20-sided spindown dice would be provided, with the expansion symbol replacing the 20.


### (f) 4 tuckboxes


Four boxes for the decks. These need to hold 60 cards, ideally either sleeved or unsleeved.


### (g) Up to 35 tokens


Up to 35 double-sided token cards. No new art.


### Packaging


The packaging should resemble a traditional board game and highlight the setting. It should look different from the Barrel Annex product and should conform to the Ham style guide.




---

As you can see, the core of the experience stayed the same: four decks and 50 tiles. These were the primary asks of Ham Annex, and were integral to make the product work.


Now, you might notice that's not exactly how it ended up. A few things changed!


Not to get too far ahead of ourselves here, but I do want to address this quickly. Once we started doing more playtesting, it became clear that a game board wasn't really needed; the tiles themselves served as a game board in and of themselves.


Additionally, the game used so many +1/+1 counters that it made sense to include them as components. So in the final version we were able to get 36 +1/+1 counters into the product, at the cost of the four d20s, which we thought players would likely have around or replace with other available ways to track their life totals.


![](https://media.wizards.com/2017/images/daily/HPoONba8NR.png)


And that's why what you see differs slightly from the original document.


Okay. So now that it's been presented, the group has talked about it in the meeting, and it's approved, what happens next?


Each team representative in Strike Force goes back to their respective team and informs them about what we're making. Meanwhile, project management is hard at work building out a schedule of how everything is going to come together.


Once that's done, we have some dates to work wit . . . and it's time to figure out when the design team will begin!


But first, a quick interlude.


Ongoing – Brand Discussions
===========================


Throughout this entire process, you can expect there to be many meetings and discussions with Brand.


Brand is a crucial stakeholder and partner in how the product turns out, as they help figure out the release window, price point, marketing, and, essentially, most aspects related to selling the product. Like a product architect, a Brand representative strives to make sure that all aspects of a product have the highest quality level possible. And while an architect sits more on the R&D side of that coin—making sure that, for example, game mechanics are represented—Brand sits on the other side, making sure that Brand values, topline set goals, and so on are all well represented.


It's absolutely crucial work, and conversations begin immediately after request document presentation and last all the way through the product's release. Additionally, Brand representatives are in most of the same meetings as the architect, weighing in on decisions.


Some discussion will happen with Brand here and there in the time after presentation, which will help inform R&D. But besides that, the next stage really kicks off a little bit later—let's travel a few months forward, into April!


April 1, 2016 – Design Begins
=============================


No fooling—April first is when this project kicked off in earnest.


The design team begins meeting a couple times each week to playtest, design new tiles and decks, and iterate on the core system. This looks much like the design process Mark Rosewater has utilized many times. It's all a matter of finding where the fun is, and preparing the product for a handoff.


What's the role of a product architect at this point? Mostly, to ensure the product stays on track and maintains its vision. For example, with Ham Annex, an architect should participate in occasional playtests to make sure that it's hitting all the presented goals.


What are some things to keep an eye on?


Well, it could be flavor based. For example, if the Dinosaur deck starts including Kithkin, that's a problem.


![](https://media.wizards.com/2017/images/daily/TwBHGJJOiA.png)


The goals of this product, remember, are in part to be thematic and to deepen the world of Ixalan. Kithkin don't exist here, and they aren't in the Sun Empire. Those are right out.


It could also be mechanics based. Imagine that you came out to a playtest and it turned out that the entire tile system had been scrapped entirely! That would be something other teams would desperately need to know—or more likely, a use for the tiles would need to be re-envisioned.


Now, those are two pretty crazy and extreme circumstances. A far more likely situation is that, for example, it seems 50 tiles is too few and the game needs more to operate. In which case, as an architect, you would go discuss with other teams and see if adding more was at all possible.


The architect should be checking in with the team regularly to see how they're doing.


But that's far from all the architect is doing, because it's around this point when plenty of other discussions begin to kick off. And things go from moving along a single, more linear track to orchestrating several moving pieces at once!


To make matters even crazier, once one of these pieces kicks off, it just keeps running in parallel with the others. Things begin to escalate quickly!


For example, about a month later . . .


May 4, 2016 – CAPS Kickoff
==========================


What is "CAPS," you may ask?


CAPS is a team inside of Wizards whose name stands for "Creative and Professional Services." It's a pretty wide catch-all term, and to be fair, they do a *lot* of things. But in this case, they're going to be working on pretty much all the structural and graphic design of the product. If it isn't on an actual card, this group of all-stars probably helped make it happen! From the box, to the deck boxes, to the tiles—CAPS is the band of geniuses behind it all.


There will be many, many meetings with CAPS over the course of this project. The kickoff is just the beginning!


Box shapes and designs will be reviewed. Art will be selected for display. The tiles will be iterated on—and so on.


It's up to the architect and the Brand representative to take a look at the incredible work that CAPS comes up with and provide suggestions for how to make sure it ties in with the product as well as possible. For example, making sure that the tribes are highlighted on the box in some way, or that the tiles have the elements needed to aid gameplay.


Meetings with CAPS will continue well into 2017.


August 8, 2016 – Creative Kickoff
=================================


In reality, Creative has been steadily guiding this product the entire time. We made sure to embed a member from the creative team on the design team so it would be a cohesive creative experience. Many discussions have been had about how the flavor will work and what some potential names are.


With all of that said, it is here where things really start moving into gear.


First, in August, toplines and art descriptions will begin being written. Over the course of the next few months, art will be commissioned for cards that need new art (such as reprints), names will be assigned to the tiles, an expansion symbol will be created, and another round of toplines and art descriptions will happen for any other reprints that need it. Graphic designs and art for the tiles will be commissioned. This all takes a lot of time and a careful hand to make sure it turns out as strong as possible.


Creative's work will run well into 2017, with the bulk of it happening in January and February.


October 19, 2016 – Development Begins
=====================================


Design ran for a couple months, then wrapped up. Why? Because *Ixalan* was being worked on in parallel! It needed to speed up to figure out how the Annex product was going to work, but once it had a good stable of tile designs, it was put on hold for a few months so *Ixalan* could develop more—and decks could be built using more final *Ixalan* cards. (This is especially important given that the decks needed to be thematic!)


When design resumes, we're in the "development" phase. (Known today as the set design or final design phase.) While the core system and mechanics have been figured out by this point, and there are decks and tiles to work with, this is where the decks and tiles are going to be hammered on for optimal balance and to make the experience as great as possible.


At this point, the architect is mostly keeping an eye out to make sure that feedback from playtesters is positive and the game is performing as well as possible. If anything is blocking the game from succeeding, it's on the architect to help the designer get what they need.


February 7, 2017 – Writing and Editing Begins
=============================================


The delta team is a crucial piece of the process of any set. Containing the editing and rules teams, among others, they and their detail-oriented eyes really make sure a product all comes together.


Delta not only edits the card set, for both functionality and grammar, but templates it, works on writing the inserts, helps proof the packaging, and so much more.


Editing helps make sure that many tiny (but important) details are there, which adds a true level of polish to our work.


In this case, the process kicks off in February by beginning explorations on the rules insert and what that should look like. Really, they've been working and consulting with the other teams the entire time—answering questions like whether a mechanic will work, whether certain text will fit on a card, and so on. But here's where their primary role begins.


Over the course of the next several months, the rules will be written and revised; the delta team will take a look at all of the writing in the product, including names and flavor text; and—perhaps most near and dear of all to our hearts—they will edit, template, and help make sure the cards are ready to send off to the next step.


March 7, 2017 – Imaging and Typesetting Begins
==============================================


Once delta has done the bulk of their work, a team begins actually making the cards in the product look like *Magic* cards! Using diligent and meticulous work ethic melded with high-tech processes, they get the art into frames, lay out the text on the cards, and, when applicable, do things like figure out how the foils are going to look.


During this process, other teams will review these cards to make sure that everything looks good here. Delta, for example, will want to confirm that all the text is right. Creative will want to make sure the art crops and foiling processes look good. And so on.


After all this time, there are a few bits and pieces to take care of at the end. Collation, production, shipping, and so on. Once that's done, the product safely sits in a warehouse until it's time to ship it out. And then—well, then you can go and pick it up for yourself!


At Your Store
=============


And *that's* the general life cycle of a product. There's a lot more in there than you may have thought—and remember, once a process starts, it generally keeps rolling for many more months afterward!


Now, as I noted earlier, every product is different and requires different considerations and work. Sometimes there will be other stages added. But this should give you a general idea of how something is made.


Hopefully you found this interesting and enlightening! Have any thoughts, questions, or comments? Feel free to [send me a tweet](http://www.twitter.com/gavinverhey), ask me a question on [my Tumblr](http://www.gavinverhey.tumblr.com/), or [email me](mailto:BeyondBasicsMagic@gmail.com).


Additionally, if you have any suggestions for article topics you'd like to hear about in future months, send those my way! I have some ideas . . . but I most want to write about what you want to hear about!


Talk with you again next time! Until then, may you try holding a product in your hands and thinking about all the time that went into it.


Gavin  
[@GavinVerhey](http://www.twitter.com/gavinverhey)  
[GavInsight](http://www.gavinverhey.tumblr.com/)








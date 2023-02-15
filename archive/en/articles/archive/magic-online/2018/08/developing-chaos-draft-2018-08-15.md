
---
[Link to Wayback Machine](https://web.archive.org/web/20180816181217/https://magic.wizards.com/en/articles/archive/magic-online/developing-chaos-draft-2018-08-15)

[_metadata_:author]:- "Damian Tedrow"
[_metadata_:description]:- "Software developer Damian Tedrow takes us behind the scenes on the coding and creation of Chaos Leagues."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1331821"
[_metadata_:publish_date]:- "2018-08-15"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing a Chaos Draft"
[_metadata_:wayback_capture_timestamp]:- "2018-08-16 18:12:17"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20180816181217id_/https://magic.wizards.com/en/articles/archive/magic-online/developing-chaos-draft-2018-08-15"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/magic-online/developing-chaos-draft-2018-08-15"
---


Developing a Chaos Draft
========================



 Posted in **Magic Online**
 on August 15, 2018 






![](https://media.magic.wizards.com/styles/auth_small/public/images/hero/wizardslogo_thumb.jpg)
By Damian Tedrow











The greatest thing about my job is making fun and exciting ways to play *Magic Online*. While I spend most of my time fixing bugs, sometimes I get to create something brand new. My name is Damian Tedrow, and I am a software developer for MTGO. I've been at this for the last three and a half years when I was hired on to help ship Leagues, but I'm also a customer. I created my MTGO account way back in November 2002, only a few months after it went live.


Recently, I was asked to bring a little controlled chaos into MTGO in the form of Draft and Sealed events with randomly selected boosters. This request involved changes to several areas of the back-end systems, some new art, and working with our Project and Release Management team to schedule its testing and production deployment. Working on a game as large and mature as MTGO is often challenging but comes with the benefit of many tried-and-true components that are powerful and easily reusable. My job was to configure and extend those components to provide the new features.


The first step was to create a "Chaos card set," reusing the already built-in Eternal card legality rules. We do this many times a year for normal card set releases and have custom tools to make this job relatively straightforward, but we did face a minor challenge: timing. In our release schedule, the high-level card set description for *Guilds of Ravnica* had already been created, assuming that Chaos would take about a month to build. However, the existing tools *Magic Online* has proved to be so well-suited to this project that as I got started, it became very clear that we could ship Chaos much sooner than previously expected.


And everyone wanted that.


The catch was that it would cost the *Guilds of Ravnica* team about a developer-day of work to account for this change in schedule. But if it meant we could get Chaos out the door early, we were committed to rebuilding the card set deployment scripts for *Guilds*.


Next, we had to create the new Chaos boosters in the digital object catalog database and tie them back to the card set created in step one. Like before, our custom tools made this easy, and again, *Guilds* deployment code would have to change to accommodate it. This time it would cost only a few hours—a small price to pay, we all agreed.


Then we linked the new boosters to our pack-opening collation engine, but instead of opening cards, it opened a real card set booster! We use this approach already for Treasure Chests, and it works the same for Chaos boosters. Essentially, the content of a Chaos booster is just another booster selected randomly.


![Chaos Boosters](https://media.wizards.com/2018/images/daily/Xgw18KgjqC.png)


But not *entirely* randomly. One of the requirements stated that a booster from a particular card set should not be duplicated in a Draft pod or Sealed pool, so if you open an *Apocalypse* booster, you can be sure that nobody else opened one. This ensures that you'll always be drafting cards from 24 different sets and is a lot like dealing cards from a shuffled deck. Of course, that's pretty much bread and butter around here. MTGO already knows how to do this for Cube drafts, and we were able to reuse that cube-draft feature for Chaos without changing a line of code.


The hardest part was modifying the Sealed pool generation and Draft podding code to recognize the new format and then open both the Chaos booster and the real booster inside it. We chose this approach since it was straightforward, isolated to this new format, and required the least amount of integration testing. We considered other options, for example creating a new type of booster that could automatically open both the outer booster and the one inside in a single step, but that would involve making more fundamental changes to the collation engine. We wanted to play and not to build perfect abstractions for a single-use case. We may revisit this someday, but for now, it all works. It's passed its testing, and I'm monitoring its deployment as I write this dev blog.


We did need help on a few things, notably the art for the Chaos boosters and the list of boosters to choose from. And of course, at Wizards there are plenty of amazing artists and sage historians of the game who stepped up to help, which is just awesome. We worked with the production team that handles printed packaging design to create the booster image, and asked R&D to pick the boosters based on what they thought would be most fun to play with together online. The results of this teamwork are truly magical.


Tomorrow, I will go back to fixing bugs in MTGO, but today I made Chaos events happen. It is my joy to build on the work of those who came before me and constructed the many components that make *Magic Online* a truly great game. It is a testament to the dedication of the world-class producers, designers, developers, artists, and architects who have come together and poured their hearts and souls into making a digital version of one of the most complicated games ever created. Chaos events celebrate the entire history of *Magic Online*. So, tell a friend and get a little Chaos in your spellcasting life when these Leagues open on August 22!








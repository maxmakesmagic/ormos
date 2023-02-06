
---
[Link to Wayback Machine](https://web.archive.org/web/20210502053621/https://magic.wizards.com/en/articles/archive/feature/level-headed-2010-05-10)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/level-headed-2010-05-10"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210502053621id_/https://magic.wizards.com/en/articles/archive/feature/level-headed-2010-05-10"
[_metadata_:wayback_capture_timestamp]:- "2021-05-02 05:36:21+00:00"
[_metadata_:description]:- "It's Level Up Week here at magicthegathering.com. This week will be dedicated to exploring and discussing the level up mechanic from Rise of the Eldrazi. During previews, I spent a little bit of time talking about how Brian Tinsman and his design team decided to use the level up mechanic, so today I was hoping to use levelers to explore a part of design and development that I"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:publish_date]:- "2010-05-10"
---


Level Headed
============



 Posted in **Feature**
 on May 10, 2010 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 







It's Level Up Week here at **magicthegathering.com**. This week will be dedicated to exploring and discussing the level up mechanic from *Rise of the Eldrazi*. [During previews](/en/articles/archive/rise-part-ii-2010-04-05), I spent a little bit of time talking about how Brian Tinsman and his design team decided to use the level up mechanic, so today I was hoping to use levelers to explore a part of design and development that I haven't spent as much time talking about. Along the way, you will get a chance to see all the different arguments level up created in the process of getting printed.


### The Other Game of Magic


One of the purposes of Making Magic is to help you all have a better understanding of what it is like to design and develop **Magic** cards. Today I wanted to bring to your attention something I haven't really talked about before. R&D doesn't play the same game of **Magic** that all of you do. It's similar, but it has one giant difference. You all are playing what I'll call stable **Magic**. To you, the cards are what they are. They don't change (okay, errata exists but errata infrequently changes the functionality of the cards). My point is that to the public the cards are a locked entity. They are what they are.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm90_playtest.jpg)R&D plays what I'll call fluid **Magic** (note that I'm talking about the play we do for our job. We too like to get out and play stable **Magic** when we can). With fluid **Magic**, cards can change. Something could cost three today and four tomorrow. A card can completely morph into a different card, perhaps of a different card type. Card power can fluctuate as text gets massaged. In the game of **Magic** that R&D plays, you can never assume anything will stay the same.


I bring this up because it has a huge impact in how R&D sees the game. When players play, they are not thinking about how they can change the game; they are thinking about how to use what exists. The cards are a constant. No so to R&D. I bring this up today because it's important to understand this vantage point as we talk about how level up was created. You all look at a level up card and say, "Well, that's how Wizards did it." We had to look at the card and say, "How should we do it?" To us, every option was on the table.


Part of the design and development process involves always having to talk through how to do things. For many cards the choice is obvious. **Magic** has so many precedents that most decisions have already been decided, but when you dive into virgin design space, nothing is a given. Today I'm going to talk about the many different issues that came up when trying to figure out how level up should work and how the card needed to be laid out to make sure that players got what was going on.


What I'm going to do is walk through the many forks that came in the path on our road to build the level up mechanic. Note that most of our issues on this mechanic were about how to visually represent what we wanted the mechanic to do. Each choice in presentation had mechanical ramifications, so what we were doing was an odd hybrid of mechanics and graphics. I should make note at this point that we have an awesome team of graphic designers that help us make everything look as good as it could. Concurrent to all the arguments I'm going to talk about, the graphic designers kept giving us different versions of the card frame to show how we could represent what we wanted with the best graphic design possible.


### To Start


Before I jump into all the arguments we had, let's start by talking about what we all agreed on. What was the core of the level up mechanic? The design team wanted the following:


Each card would be a creature with three different states. Most states would change power and/or toughness although not all. Some stages would add abilities. A few would remove some.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm90_leveledBottoms.jpg)The way each creature would advance stages would be through the paying of mana. This payment could change from creature to creature but would be the same for each payment made by a particular creature. If it costs ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif) to go from level 1 to level 2, then it would also cost ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif) to go from level 2 to level 3.


The different stages would be concurrent with different groupings of levels. The first stage would also be the level the creature starts at. The second stage would require at least one level up but possibly many more than one. The third stage always required leveling up higher than the second stage.


Creatures would never be able, through their own power, to go down in levels.


That's what we had to work with. Let the arguments begin!


### Level 0 vs. Level 1


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm90_dice.jpg)Everyone was on board with creatures "leveling up"—that is, the idea that these creatures would have a level and be able to advance up to higher levels, improving along the way. The idea of leveling is a pretty core gaming concept (I believe introduced by **Dungeons & Dragons**, but I could be wrong). As we were trying to tap into resonant areas of an adventure world, leveling seemed ideal.


Creatures would advance one level a time. The big question was at what level were they supposed to start at? There really are only two good answers. We could start them at level 0 or level 1, what I'll call the elevator conundrum. Is the bottom level of a building the first floor (assuming no basements) or is the first story up the first floor. The answer to this question varies depending on what country you live in. Anyway, there are two possible choices so, of course, this was one of the first issues that came up.


The level 0 camp argued that the mechanic came with some logistics and we wanted to create the simplest way for players to remember what level they were at. The easiest way was to use level counters to represent the level, but if we started at level 1 then the counter number would not match the level number (two counters would mean level 3 not level 2).


The level 1 camp argued that we were trying to be resonant and connect with what people already know and to do that we needed to start at level 1. Why? Because just about any game you could name (especially **Dungeons & Dragons**, which was the key inspiration for the mechanic) that used leveling started at level 1. Players would just assume creatures started at level 1 and making it level 0 would be counter-intuitive.


Both camps had strong points. In the end, it was decided that matching up the level counters to the level was more important and that we would have to do whatever it took to help override the intuitive belief that creatures started at level 1. One way we did this was to make sure that all common levelers went to the second stage at level 1. If stage two started at level 1 then by definition the creature couldn't start at level 1 leaving level 0 as the only other option. This spawned another issue, whether or not to mark the first stage as "level 0," which I'll get to down below.


### Progression Down vs. Progression Up


If the card was to have three stages, everyone agreed that the card had to clearly show those three stages. While we had liked [Figure of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny), we didn't like that the three stages weren't as clear as they could have been. If we were going to do level up, we wanted each stage to be clearly identified. Part of this meant having separate sections and power/toughness boxes for each stage.


So everyone was on board with having a section of the text box (remember that level up cards still only have one text box) for each stage including a unique power/toughness box. The argument that came up was what order should the stages be. Should the first stage be on top and each stage progress downwards or should the first stage be on the bottom and each stage progress upwards.




|  |  |
| --- | --- |
| 
Figure of Destiny
 | 
Lord of Shatterskull Pass
 |

The progression down camp argued that people read from top to bottom. If the card was going to progress it should progress in the order that people naturally read their cards.


The progression up camp argued that it was important for the bottom right corner to have the power/toughness of the original creature. That is where players have been taught to look and it made sense to keep it the same. Also, this camp argued, growth goes up. It seemed natural to have the first stage be the lowest and have each successive stage "grow" upwards.


One of the biggest factors in finding the correct answer was to mock up cards (again thanks to the graphic design team) and show them around to Wizards employees outside of R&D who played **Magic**. We were very interested in what **Magic** players would assume when faced with the different options. Downward progression proved easier for the players so that is the side that won. The one concession to the other side was to move the third stage power/toughness box so that it was tucked inside the third stage section of the text box rather than appearing lower on the card as it normally does. This slight movement helped players keep from assuming the lowest power/toughness box was the one to look at first.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm90_PTBoxes.jpg)### Additive vs. Replacement


The creature was going to change from stage to stage. This meant that it was going to gain abilities. How were we supposed to represent that the second stage had flying while the first did not? Also, how did we make sure that the player understood that stage three still had flying even if it had gained an additional ability? Once again, we had two basic choices. Each stage could be additive, meaning it just told you what new things the creature had that it didn't have before, or it could be a replacement, meaning that each stage told you everything that stage had.


The upside to additive was that it allowed you to have the fewest words. If you had to repeat everything multiple times, it could get pretty wordy. In addition, we had the problem of what to do with the level up mechanic. It had to exist at least on the first and second stage. If the abilities were additive, then we could just write it on the card once.


The upside to replacement was that it gave you the ability to remove things. A creature could have an ability in stage two that it didn't have in stage three.




|  |  |
| --- | --- |
| 
Student of Warfare
 | 
Enclave Cryptologist
 |

Sometimes this was good. It is cooler and less confusing for first strike to turn into double strike than to gain double strike in addition to first strike. Sometimes this is bad. [Enclave Cryptologist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enclave+Cryptologist) can no longer help you discard cards while in the third stage. We felt this was okay because the draw ability felt like an upgrade to the "looting" (or filtering) ability.


Another argument of the replacement crowd was that the power and toughness worked as a replacement. A creature that gained a power and toughness didn't have "+1/+1" written in their second stage power/toughness box, so why should the abilities work any different?


The real issue was: Which version did the most players correctly interpret when they saw it? Let's take [Knight of Cliffhaven](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+Cliffhaven) again as an example.



![Knight of Cliffhaven](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Knight+of+Cliffhaven)

  

 When the second stage said "Flying" and the third stage only said "Vigilance," most players assumed that it was a 2/3 flyer at stage two and a 4/4 creature with vigilance at stage three. We tried adding a plus before "Flying" and "Vigilance" to convey that the creature was now "up" this ability. It didn't help enough and most players we surveyed still got it wrong.


It seemed clear that the replacement version was clearer to people. There was just one problem. Writing the word level up again and again was kind of ugly. What if the first stage was represented differently than the second and third stages? The first stage, because it didn't have an arrow and went all the way across the card, would represent something that all stages had. To simplify it even further we decided to have all first stages only have one ability: level up. We felt that the existence of stage three made players believe that stage two still had the level up ability. Testing obviously showed this to be the case.


The replacement choice did come with a cost: we had to be much more concerned about space. This is why we chose to have [Enclave Cryptologist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Enclave+Cryptologist) lose its second stage ability when it gained its third stage one. We followed the philosophy that it was okay to lose things if what you were gaining felt like it was an upgrade to the thing you were losing.


### First Arrow vs. No First Arrow




|  |  |
| --- | --- |
| I should point out that all these arguments were happening at the same time. I'm presenting the arguments in the most logical order I can, as some decisions did affect others. Just be aware that the process was much more chaotic than how I am making it sound. |
|  | This issue stemmed back to the "level 0 vs. level 1" debate. Players weren't going to get that creatures started at level 1. The best way to help educate them was to have an arrow in the first stage spelling out "Level 0." That, the level 1 crowd said, was the best way to avoid confusion. This argument ran head first into the last one. To keep from having to repeat the words "level up" on all the stages, the layout had to communicate that the first stage had a different property than the later stages. To do this, it had to lose the arrow. |
|  | What if it was a smaller arrow? What if it had a different shape? What if we just bit the bullet and put the words "level up" on the second stage as well as the first? (The argument was that the third stage didn't need to have it.) In the end, the decision was to make the cards look as clean as they could and hope that the solution of making all commons go to stage two at the first level would be enough to carry the message of creatures starting at level 0. |

### The Word "Level" vs. No Word


One of the pressures that came from the graphic designers was that the less we put on the cards, the cleaner the graphic looked. As such, they discouraged us from using the word "level" on the arrow. Couldn't the numbers convey what had to be conveyed? Another knock against the word "level" is that it's an English word and we print cards in many languages. Using the word "level" would cause each language to change it or live with an English word on non-English cards.


As a result we tried versions without the word "level" and tested how the players responded. It turned out the word "level" really helped players get what was going on. It impacted the graphic design as the arrows had to be longer to fit the word, but we decided to do it as it was clear to us that it would help the players better understand how to play the card.


### Level Change vs. Level Grouping


A similar argument came down about the numbers. If a creature changed at level 2, could we write only a 2 on the first arrow? Did we have to write the full spectrum of numbers that the stage existed at? This was another area where testing showed that one way was just easier to understand than the other.


### "+" After the Number of the Third Stage vs. No "+"


I'm starting to get to the nitty-gritty, but I want to point out that R&D (and graphic design) have to worry about the nitty-gritty. The question here was whether or not the "+" was needed on the number in the third stage. If [Kargan Dragonlord](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kargan+Dragonlord) became an 8/8 flying, trampling, fire-breather at level 8, was it clear that it would always be that, even if it gained levels? The answer was "No, it wasn't clear." **Magic** players have learned to be precise, so if the card said "level 8" it would be taken to mean "exactly at level 8." The "+" was added.


![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/mm/mm90_muchoLeveled.jpg)### Type Lines vs. No Type Lines


Early in the process the design team entertained the idea that each stage would have its own type line. This proved infeasible for space issues, but also confused the issue of whether or not this was all one text box. In the end, there wasn't enough gain. The levelers were adventurers and little would change about them even if it could, other than a shift in class on a card or two.


### On the Level


My hope with today's column is that it can give you an insight into all the little details that R&D has to worry about and how each one leads to its own issues. I'm very happy with where the levelers ended up but it was definitely a rocky road to get to the solution.


Join me next week when I finish Part 2 of my look at [Dieter Rams's 10 Principles for Good Design](/en/articles/archive/ten-principles-good-design-part-1-2010-05-03).


Until then, may you learn to fight for the little things; they matter.


[![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/features/GameDay_ROE-Article-Banner-620-Wide-Template.jpg)](http://www.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/gameday-facts)






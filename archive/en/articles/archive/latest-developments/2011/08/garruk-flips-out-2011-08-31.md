
---
[Link to Wayback Machine](https://web.archive.org/web/20210429130306/https://magic.wizards.com/en/articles/archive/latest-developments/garruk-flips-out-2011-08-31)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Two weeks ago, Mark Rosewater gave his traditional pre-preview set tease by giving you a few out-of-context tidbits about the set. While there were many interesting tidbits among them, there was one in particular that sparked all kinds of discussion: `a planeswalker with five loyalty abilities.`We enjoyed watching all of you speculate about what this could possibly mean. Jace,"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "193001"
[_metadata_:path_date]:- "2011-08-31"
[_metadata_:publish_date]:- "2011-09-02"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Garruk Flips Out"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 13:03:06"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429130306id_/https://magic.wizards.com/en/articles/archive/latest-developments/garruk-flips-out-2011-08-31"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/garruk-flips-out-2011-08-31"
---


Garruk Flips Out
================



 Posted in **Latest Developments**
 on September 2, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






Two weeks ago, Mark Rosewater gave his traditional pre-preview set tease by giving you a few out-of-context tidbits about the set. While there were many interesting tidbits among them, there was one in particular that sparked all kinds of discussion: "a planeswalker with five loyalty abilities."

We enjoyed watching all of you speculate about what this could possibly mean. [Jace, the Mind Sculptor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+the+Mind+Sculptor) required a whole new frame to fit on a card and had a smaller art box than normal, and that only had four abilities! Did we print a card that had barely any room for art? Had we simply used tiny text? What was happening?

I was on the *Innistrad* development team, so I knew exactly what was happening, as well as how we got there. Speaking of the development team, we traditionally introduce everyone on the team during previews. I've got a big story for today, though, and a big card, so I'll be doing that next week. For now, let's go back in time to the beginning of development.

By this time, we were fairly certain that we were going to do double-faced cards. That made both lead developer Erik Lauer and lead designer Mark Rosewater want to make a double-faced planeswalker. Mark's original idea was to create a new werewolf Planeswalker character to match the idea of a transforming planeswalker. However, several people pointed out that we already had a Planeswalker who had gone through a transformation of sorts, unwilling as it may have been, and maybe we should just represent that instead.

[![](https://media.wizards.com/images/magic/daily/ld/ld158_comic1.jpg)](http://archive.wizards.com/Magic/Multiverse/Article.aspx?x=mtgcom/feature2/470a)[The Hunter and the Veil Part 3](http://archive.wizards.com/Magic/Multiverse/Article.aspx?x=mtgcom/feature2/470a) | Art by [Alex Horley-Orlandelli](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Alex+Horley-Orlandelli%22%5D)

While this is obviously a very cool idea, I had some trepidation about it. Planeswalker development already presents challenging problems. We have also found that those problems are more challenging when there are even more knobs on the card, and this would be more knobs than we've ever put on one planeswalker. There would potentially never be another opportunity to make a double-faced planeswalker, however, and Magic design resources can be scarce. When we see an opportunity to do something exciting in a spot that only exists this once, we should usually take it. I could tell we were going to do that here, so I braced myself and jumped in.

Spoiler warning: everything turned out fine. Here is the card:

</magic/flipcards/flipcard_big.html?ca=pl8kpaqt6oamp;cb=lgtxg8gphzamp;lang=en>[Double-Faced Card Rules](http://archive.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/innistrad/dfcrules)

Getting to this point, however, required answering a lot of tricky questions. Like, say, these questions.

What does Garruk look like?
We know one thing this Garruk would not look like, and that's a standard planeswalker card. Jace's four-ability frame was cute, but with two sides we wanted to leave plenty of room for the art that would sell Garruk's transformation. That left us room for three abilities on each face, but at least one ability on the front face and potentially one ability on the back face needed to govern the transformation.

![](https://media.wizards.com/images/magic/daily/ld/tyrszxcrytuhjkbhnsdukjfhnsjkld.jpg)Garruk Relentless | Art by [Eric Deschamps](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Eric+Deschamps%22%5D)

While one of the loyalty abilities could have induced the transformation, we thought it would be strange to do that here. Garruk won't actually want to transform, so having him "choose" to do so in a meta sense while you play the card would be rather odd. We also decided that he doesn't get to transform back to normal, as in the story (so far) he remains veil-cursed, without a way to solve the problem on his own.

Adding all that up meant that we needed a static trigger on the front face that transformed him, two loyalty abilities on the front face, and three loyalty abilities on the back face.

How does Garruk transform?
The narrative answer to this question is simple: he transforms when Liliana blasts him with creepy dark magic. That doesn't translate very well to a **Magic** card, though. "Whenever an opponent casts a card with Liliana in its name, transform CARDNAME" is cute, but referring to card names is bad for us now that **Magic** is printed in over ten languages, and we also don't want Garruk's transformation to depend on the opponent doing something from a very narrow category of actions. Players like to feel that they have control over what's going on with their cards.

![](https://media.wizards.com/images/magic/daily/ld/rtyfghjnmosjkfghndujkfmd.jpg)  
We've found that in modular game design the best way to do something is usually the simplest. We chose to have the transformation trigger when Garruk's loyalty is below a certain threshold, as that is the closest we could come to suggesting some kind of unhealthiness or vulnerability. That threshold, of course, needed to be less than his starting loyalty.

This induces another question.

How can Garruk lower his loyalty in a way that feels natural?
It would be pretty lame if Garruk could only transform when an opponent attacked him. Just as before, we want a player to have control over what happens to their cards. We needed to come up with an ability that let Garruk do something constructive, but also resulted in some lost loyalty, so that it felt natural to get him to transform.

Erik's idea was to let Garruk get down and dirty by fighting personally with opposing creatures. While green removing creatures is a little weird, we've gotten comfortable with allowing green creatures to fight opposing creatures, and this is very close to that. I could not help but observe that since Garruk's transformation, the comics have shown him doing a lot more of his own dirty work—moving piled-up rocks to get out of a cave, jumping through stained-glass windows, grabbing Jace by the throat and throttling him—as opposed to summoning bestial minions to do it for him. That was all the justification I needed.

What else can Garruk do?
For the rest of Garruk's abilities, we drew from a few well-established wells. Garruk's previous cards have made tokens, and this one does as well. [Heal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heal)thy Garruk gets to make Wolves this time; his less-healthy incarnation makes Wolves as well, but Erik chose to represent Garruk's curse in the change to the token that he makes. Erik suggested 1/1 Wolves with deathtouch, which I liked both for flavor and for game play. I have had times in games where a 2/2 is better than a 1/1 deathtouch, but there have also been plenty of situations where the opposite was true, and I think that makes for an interesting card.

![](https://media.wizards.com/images/magic/daily/ld/iuferdfgdhvsudjvrgdbuftykusuy.jpg)  
My favorite of Garruk's abilities is the middle one on his back face. In some ways, it is similar to the middle ability on [Garruk, Primal Hunter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%2C+Primal+Hunter); however, the requirement of a sacrificed creature gives it a somewhat darker tone, and it has quite different implications on deckbuilding. I find variety in **Magic** play to be quite important, and one way we can build variety into competitive play is by including tournament-level cards that allow you to search your deck for a category of things. While this often increases consistency, it can also induce players to include goofy one-of cards that they would not otherwise play, and if the tutoring functionality is either fragile or conditional enough, that can provide the variety that I enjoy so much.

![](https://media.wizards.com/images/magic/daily/ld/jhdtrghjkgdfgfgfg.jpg)  
Garruk is basically perfect for this. Getting to his middle back ability is hardly automatic, but the possibility for doing so is a great incentive to include a single copy of something like [Elesh Norn, Grand Cenobite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elesh+Norn%2C+Grand+Cenobite) or [Sheoldred, Whispering One](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sheoldred%2C+Whispering+One) just in case. When you do that, though, sometimes you randomly draw a Praetor and dump it on your unsuspecting opponent. That's one of my favorite feelings in the world.

![](https://media.wizards.com/images/magic/daily/ld/ydctnyjghdjfnmsghdnfkjkbdnmfdfd.jpg)  
I don't have much to say about the ultimate, which is just a darker twist on [Overrun](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun). I do, however, have a lot to say about developing a planeswalker with five abilities. We had a ton of knobs on this Garruk, with the mana cost, starting loyalty, transforming loyalty, and five loyalty ability costs. While our first goal was to make the card balanced and interesting to play with, our secondary goal was to build him so that all five abilities were valuable and worth thinking about. As you might expect, the latter goal is pretty challenging, and it required lots of tuning. To make the abilities on the back face matter, we had to make sure he could transform, and that meant no loyalty-gaining abilities on the front. That meant we had to add more power to the abilities on the back, as well as make a strange-looking "ultimate" that is only a -3. However, in the end, I'm quite pleased with where this card ended up, as we regularly use all five abilities in playtesting.

![](https://media.wizards.com/images/magic/daily/ld/nytdvcbyrtshghdfjbsvnegtndtyfgjhkjsd.jpg)Garruk, the Veil-Cursed | Art by [Eric Deschamps](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Eric+Deschamps%22%5D)

While *Innistrad* may have been the talk of the Internet this past week, there's other big news in the **Magic** world this weekend. As of Friday morning, the **Magic** Pro Tour has arrived in Philadelphia, and it will be the first high-level tournament to use the new Modern format. The Constructed results from this event will define what Modern looks like for its first few months of its life. If you're into that kind of thing, you might want to pay attention.

I'm particularly excited about this event because I made both of the formats it is using. I led ***Magic** 2012* development, and I also helped shepherd Modern through Wizards from idea to execution. This is "my" Pro Tour in a way that no other split-format Pro Tour has been any one person's, which I think is pretty cool. I look forward to seeing the Top 8 on Sunday, and I hope you will be right there with me.



---

  
Last Week's Polls


|  |
| --- |
|  **Have you built a Modern deck with physical cards?**  |
| Yes | 258 | 33.2% |
| No | 518 | 66.8% |
| **Total** | **776** | **100.0%** |

  


|  |
| --- |
| **Have you played a match of Modern on **Magic** Online?**  |
| Yes | 42 | 5.0% |
| No, and I play Magic Online | 157 | 18.7% |
| No, and I don't play Magic Online | 642 | 76.3% |
| **Total** | **841** | **100.0%** |

  
This Week's Poll
**What color do you most enjoy playing with?**WhiteBlueBlackRedGreen  


---

  
![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_location_static.png)![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_go_active.png)![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_go_static.png)![](https://web.archive.org/web/20131205111141im_/http://www.wizards.com/mtg/images/daily/features/banners/ISD_ArticleFooterBanner_Pre_Top.jpg)[![](https://web.archive.org/web/20131205130924im_/http://www.wizards.com/mtg/images/daily/features/banners/ISD_ArticleFooterBanner_Pre_Button01_Static.jpg)](http://archive.wizards.com/magic/tcg/Products.aspx?x=mtg/tcg/products/innistrad)






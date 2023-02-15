
---
[Link to Wayback Machine](https://web.archive.org/web/20170215195757/http://magic.wizards.com/en/articles/archive/making-magic/trigger-happy-2003-01-06)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Welcome to 2003! MagicTheGathering.com is now one year old. We have all sorts of cool things planned for this year, such as our normal set previews, a new `You Make The Card,` the big Magic tenth anniversary celebration, and a lot more! In addition, I'm happy to announce that we have a new columnist for our Wednesday column: Brian David-Marshall. You might recognize Brian from his `Deconstructing Famous Decks` articles."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "618201"
[_metadata_:publish_date]:- "2003-01-06"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Trigger Happy"
[_metadata_:wayback_capture_timestamp]:- "2017-02-15 19:57:57"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170215195757id_/http://magic.wizards.com/en/articles/archive/making-magic/trigger-happy-2003-01-06"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/trigger-happy-2003-01-06"
---


Trigger Happy
=============



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on January 6, 2003 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Welcome to 2003! MagicTheGathering.com is now one year old. We have all sorts of cool things planned for this year, such as our normal set previews, a new "You Make The Card," the big **Magic** tenth anniversary celebration, and a lot more! In addition, I'm happy to announce that we have a new columnist for our Wednesday column: Brian David-Marshall. You might recognize Brian from his "[Deconstructing Famous Decks](/en/articles/archive/magicthegatheringcom-author-archive-brian-david-marshall-2002-05-03)" articles. Brian will explore many of the basic tenets of the game to help you improve your play. Check in on Wednesday for his first article. 

Welcome to the *Legions* preview! During the next three weeks, you'll get a sneak peek at the newest **Magic** expansion. Mechanics, art, flavor -- we'll cover it all.

Welcome to Morph Trigger Week! This week we'll be talking about the newest twist to morph creatures. So what, you ask, is a "morph trigger"? Let me start my explanation by showing you a *Legions* card: 

![Shaleskin Plower](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shaleskin+Plower)A morph trigger is an ability that triggers when the creature it's on is turned face up. [Shaleskin Plower](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shaleskin+Plower), for example, destroys a land when turned face up. While turning a card face up doesn't go on the stack, these triggered abilities do (We'll have more on the specific rules later in the week). Now that you've seen the new ability, let's get down to the nuts and bolts of this article -- how morph triggers were designed. 

### The Morph the Merrier

Before I can begin explaining how morph triggers came to be, I have to first make sure you know how morph came to be. Thus, for the first time ever in "Making **Magic**" I'm writing an article with required reading. You know, like high school at the end of each summer. You had a list given to you at the beginning of the summer that you ignored until two or three days until school started. Something like that. 

Required reading: "[Wait, There's Morph](/en/articles/archive/making-magic/wait-theres-morph-2002-09-09-0)"

Now, I also know that many people don't actually read the required reading. I mean it's summer for goodness sake. Summer! So, what do these poor souls do? They read the shorter version. Yes, I'm talking about CliffsNotes. For those unfamiliar with CliffsNotes, let me explain. Long ago, a very smart person realized there was money to be made from other people's laziness. I'm assuming this guy was named Cliff, but that's pure speculation. Anyway Cliff (if his name wasn't actually Cliff I apologize ahead of time) took many of the classic books that were required reading in many high schools and colleges and condensed them into a much shorter and easier read. (For more information, visit the [CliffNotes](http://www.cliffsnotes.com/aboutcliffs/aboutcliff.html) website.) A book that might be 200+ pages was shortened to fifteen pages. 

As I'm a kind columnist and still young enough to remember my dislike of required summer reading, I am providing the MarksNotes (I don't want to get sued by Cliff) of my morph column: 


> Rosewater begins by explaining the creation of [Illusionary Mask](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusionary+Mask) by Richard Garfield. The card was the combination of two of Garfield's interests: creating a card that promoted bluffing and creating a card that gave the attacker the advantage in combat. Years later, the Rules team (consisting then of Paul Barclay, Elaine Chase, Brady Dommermuth, Mike Donais, Jeff Donais, and Collin Jackson) was given the task of updating the card (as well as the companion card [Camouflage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Camouflage)) to fit into *Sixth Edition* rules. 
> 
> 
> The team realized that the largest problem with [Illusionary Mask](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusionary+Mask) was that the card required unknown information on the part of one player. For example, a player would only know that a creature could not be affected by [Terror](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terror). He or she wasn't allowed to know why. The team's revolutionary solution was to give the face-down card have defined qualities. That way, all the players would know how cards interacted with it. 
> 
> 
> Meanwhile, the *Onslaught* design team (Mike Elliott and Mike Donais) was looking for a new mechanic to replace one they had gotten rid of. One day while Rosewater was talking to Elliott, the Rules team heard Rosewater's rather loud voice and came next door with their ideas of how to turn the [Illusionary Mask](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusionary+Mask) fix into a mechanic. Elliott didn't have a strong first impression, but Rosewater really liked it. 
> 
> 
> To demonstrate the mechanic, Rosewater designed twelve cards, split them between two two-color decks and started playing with various R&D members. Rosewater changed the morph creatures from 1/1 to 2/2 to give make them less fragile and more inclined to attack. The playtesting produced positive response (even with Elliott) so morph was added to the *Onslaught* set. 
> 
> 

### Morph, Part Deux

All caught up now? Good. Now, I get to tell you the full story. Last time we talked, it was for the *Onslaught* previews. Because morph triggers were delayed until the *Legions* set, I wasn't supposed to talk about them. That meant I left a few details out. Now, you get to hear the full story. You see, morph triggers go back to those original twelve playtest cards. 

I just got out of the meeting in which the Rules team pitched the early version of the morph mechanic. I knew that I wanted to make some cards that demonstrated what morph could do. I started by creating creatures that interacted well with morph. That meant that they needed to be creatures that you would want to play face down. The first obvious answer was creatures that were bigger and more expensive. With these creatures morph had an "echo" feel, as they let you pay off the creature over time. 

Next, we had creatures that were more fragile (usually with 1 toughness) but had some other advantage, such as an ability like first strike or flying. Third, we made creatures that got bigger but came with a drawback. Fourth, we had creatures for which surprise mattered. The best example of this is a creature with an effect that happens when the creature damages a player, such as the *Onslaught* card [Haunted Cadaver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Haunted+Cadaver). This creates an interesting tension as some morph creatures want to be blocked while others don't. 

### They're Not Dead Yet

All of this leads up to my discovery of morph triggers. To understand my next leap of logic, let me first talk a little about creative thought. To demonstrate this, I'll use a story from my favorite book, A *Whack on the Side of the Head: How You Can Be More Creative* by Roger von Oech (a must-read if the concept of creative thinking interests you at all). 

A long time ago, a deadly plague struck a small village in Lithuania. One of the most troubling aspects of the disease was that it often left people in a death-like state, which lead to the accidental burying of people who were still alive. 

The town came together to find a solution to the problem. The first group came up with the idea of putting a little bit of food and water into every coffin and then digging an air hole. This way, a living person could breathe and call for help. The food would make sure they survived until help arrived. 

The problem with this solution was that it was very expensive. A second group came up with a much cheaper alternative. Put a twelve-inch spike in each coffin lid that resided over the person's heart. That way no one buried would still be living. You see, the second group solved the problem by asking a different question than the first. 

The first group asked, "How can we make sure that a person buried alive doesn't die?" The second group asked, "How do we make sure that no one buried is still alive?" The different attack of the problem resulted in two very different answers. 

### The Morph You Know

During my first attempt at designing morph, I asked myself why players would play any particular card face down. What advantage did the face-down version of the creature have over the face-up version? Then I changed my question: How could I make a creature that players felt had to be morphed? 

With this question in mind, I went a completely different route. How could I force players to morph a card? First, I examined cards that couldn't be played normally but *had* to be played face down. This felt to me like it violated the essence of morph. Morph was about having a choice, and taking away the choice seemed wrong. That led me to my next line of thought: What if players want to morph the creature because the power of the card lay in the act of turning the card face up? 

The new line of thought had a lot of promise. The most obvious answer was to use the morph cost as a way to generate an effect. The easiest execution of this (and remember that many of the best designs follow the easiest execution) was to have the morph equivalent of a comes-into-play ability. The advantages of this mechanic are threefold. First, it makes the player want to play the card face down. Second, it adds a very interesting surprise element. And third, it opens up a large area of design space. 



|  |
| --- |
| *Two of the original morph trigger (then called "stealth") playtest cards that Mark used to convince the team the mechanic was viable.* |

### Viva la Difference

A very important part of any design is actually playing with the cards. You can think about an idea all you want, but nothing takes the place of simply using it. The morph triggers turned out to be not just interesting but surprisingly powerful. At first I had thought of morph triggers as a variant of comes-into-play abilities. But in actuality they played quite differently. 

There were a few reasons. The most important was the element of surprise. Comes-into-play abilities of creatures, with only a few exceptions, function like sorceries. Morph triggers act like instants. Also, the useful life of the creature with a comes-into-play ability comes after you get its effect. With a morph trigger, the creature sees some action before you get its morph trigger effect. (Morph triggers proved most interesting on smaller creatures because there was a more interesting tension if the creature got worse once the trigger went off.) Finally, the morph triggers tie into the larger framework of the morph mechanic. 

The end result was that we ended up with something cool. All the other R&D guys had a similar positive reaction to the morph triggers, so more were added to the mix. But if morph triggers existed in the *Onslaught* design file, why didn't you all see them until the *Legions* set? Mainly because we like to introduce aspects of a block's main mechanic slowly over time as opposed to all at once, but that's more of a development issue than a design one.

Join me next week when I introduce a creature that does something never done before in the **Magic** game. And it's even a Legend. 

Until then, may you learn to approach a problem from multiple sides.

*Mark may be reached at makingmagic@wizards.com.*






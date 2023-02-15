
---
[Link to Wayback Machine](https://web.archive.org/web/20190704173607/https://magic.wizards.com/en/articles/archive/making-magic/between-grok-and-hard-place-2006-10-16)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "We begin by removing a time counter from Suspend Week and…"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "616836"
[_metadata_:publish_date]:- "2006-10-16"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Between a Grok and a Hard Place"
[_metadata_:wayback_capture_timestamp]:- "2019-07-04 17:36:07"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20190704173607id_/https://magic.wizards.com/en/articles/archive/making-magic/between-grok-and-hard-place-2006-10-16"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/between-grok-and-hard-place-2006-10-16"
---


Between a Grok and a Hard Place
===============================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on October 16, 2006 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 







We begin by removing a time counter from Suspend Week and…


Welcome to Suspend Week! This week we’ll be exploring the largest new mechanic of *Time Spiral*. As is becoming a fine tradition for this column, the theme week about the mechanic comes several weeks after I explained how said mechanic was designed. (The column, “[Needing a Little Time](/en/articles/archive/making-magic/needing-little-time-2006-09-11),” was my column during the second week of previews.) This means that I have to find something different to say about the design of suspend. Luckily, there’s a juicy design nugget that I haven’t touched upon yet. In fact, the topic at hand is a much larger issue that I’ve wanted to talk about for some time. So for once, everything seems to be working out perfectly. (Foiled again, Mr. Editor-in-Chief – Note that Scott doesn’t actually try to trip me up by giving me theme weeks that I’ve already talked about; at least that’s *his* story.)


### Suspending Disbelief


Let’s begin by talking a look at the keyword along with its ever so lovely reminder text: (I’ve chosen [Errant Ephemeron](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Errant+Ephemeron) as my sample.)



The keyword along with its reminder text is seven lines long. Seven lines long! And that doesn’t even count the line that says “Flying.” How in the world did R&D come up with a mechanic designed for common that has more lines of rules text than most rares? And once we did, how did we ever decide to keep it at common? Good questions. This is the topic I’ll be covering today. How is suspend okay as a keyword mechanic that shows up in every rarity?


To answer this question, I have to pull back a bit to explain some larger issues about card design. In fact, I have to pull back farther than that. I have to pull back to the human brain. Yes, to understand why R&D decided to do suspend you have to hear about the human brain. That’s the fun of my column. No one does the pull-back like I do. You’re getting into the nitty-gritty of card templating, and the next thing you know you’re in Brain Anatomy 101. Actually, it’s more about perception than brain anatomy, but I like the idea that you think I might pull out a map of the brain at any moment.


This is going to seem like a bit of a non sequitur, but stick with me. If I asked you if you could memorize a thirty-digit number, what would you say? I assume most of you would be a bit hesitant to say yes. Instead, let me ask a similar question. Can you name in order the following three phone numbers with area code: your home phone number, your cell phone number, and your work phone number? Assuming you have all three, I bet the vast majority of you would answer that you could. That is a thirty-digit number. (For my non-American readers – the longer versions of American phone numbers are ten numbers long.)


If I asked you if you could memorize a thirty-digit number, what would you say?The biggest difference between a raw thirty-digit number and a string of three phone numbers is that the first is thought of as thirty separate units while the second is thought of as three. Thirty is an intimidating number to most people. Three is not. The trick to remembering longer things is to group them into chunks that are easier to remember. Most memory tricks stem from this technique. Roy G Biv sounds like a guy’s name. One guy. That’s simpler than remembering the seven colors of the rainbow (**R**ed-**O**range-**Y**ellow-**G**reen-**B**lue-**I**ndigo-**V**iolet).


What does this have to do with **Magic** design? A lot. Why? Because at a base level, designing **Magic** cards involves understanding how much people can comprehend. If you overstuff a card, the card becomes daunting, and daunting cards are a bad, bad thing. Yes, a few rares each set that require you to read them twice are one thing. Having multiple commons that do this are a death knell for a set.


### All Together Now


What is a **Magic** designer to do? He or she needs to have a firm grasp of a concept I call grouping. Grouping is the technique of making separate aspects of a card hang together to feel connected. When done properly, it makes the pieces feel like part of a larger picture. Thus, you turn multiple separate chunks into one connected idea. Huh. Let me walk you through some examples using existing **Magic** cards.


We’ll begin with Vicious Hunger. (Those of you who took “[The Test](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/365)” last week might be familiar with this card – look at question 19.)


 



![Vicious Hunger](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vicious+Hunger)

[Vicious Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vicious+Hunger) does two things:

1. It deals 2 damage to a creature. Basically, a more limited, sorcery version of [Shock](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock).
2. It gains its caster 2 life. This is a buybackless, sorcery version of [Reaping the Rewards](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaping+the+Rewards).

But does it really? No. It actually just does one thing. It drains 2 life from a creature. The two abilities join together in a way that clumps them. This makes the abilities on the card feel like one ability.


 

 



![Sift](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sift)

Let’s try a different card, [Sift](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sift).

[Sift](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sift) also does two things:


1. It makes you draw three cards. It’s a more expensive sorcery version of [Ancestral Recall](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall).
2. It makes you discard a card. It’s a weaker sorcery version of [One with Nothing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=One+with+Nothing).

Once again, it doesn’t really. The “draw three” and “discard one” are seen as one action. Note that it is possible with this card to draw three cards and then discard a fourth card already in your hand. The discard effect potentially could have nothing to do with the draw. It doesn’t matter. The overall effect (and don’t dismiss the importance of the name and flavor) is one that the player melds into a single concept.


What does this have to do with suspend and its seven lines of text? We’re moving in that direction; don’t worry. The lesson here is that design has to think of mechanics in a sense larger than the individual pieces. We have to examine how the audience groks them.


### Grok & Roll


Grok? Yes, vocabulary time. The word “grok” comes from science fiction author Robert Heinlein’s famous novel *Stranger in a Strange Land*. In the book the term is defined as such: “Grok means to understand so thoroughly that the observer becomes a part of the observed – to merge, blend, intermarry, lose identity in group experience. It means almost everything that we mean by religion, philosophy, and science – and it means as little to us (because we are from Earth) as color means to a blind man.”


Over time the word has come to mean several slightly different things. The usage that I’m most interested in is the idea that people understand something so intimately that they are not even conscious why they understand it. To grok something by this definition means that you understand it in a way that is more intuitive than intellectual. You get the essence of what it means, but mostly because it just feels right – not because you’ve been formally taught anything about it.

Grokking things is an important concept in understanding perception (and thus in card design). While people clearly can consciously learn things, much of what defines their comprehension comes from things that they aren’t consciously aware of. There are a number of reasons for this.



> 
> **#1) Aesthetics** – I’ve talked about this topic a few times before in “Making Magic” (the most thorough was in “[Zen and the Art of Cycle Maintenance](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr28)”) so I’ll just hit the highlights here. The human brain is hard wired to appreciate certain things. People like to think of things like beauty as subjective, but science has shown that across cultures and time certain attributes are found universally appealing (symmetry being an example). One of the major reasons that some things feel more natural is that the human brain is predisposed to certain qualities. Because this comes from such a non-conscious place, it is hard for most people to appreciate how it affects their perceptions.
> 
> 
> **#2) Pattern Setting** – Humans crave patterns. It’s just the way our brains work. They constantly struggle to find connectors between things. Why? There are a number of guesses, but my favorite is that connecting things together is one of the fundamental roles of intelligence (and creativity – but that’s for a whole other column). Humans think this way because it is how our brain learns. Once again, this phenomenon operates at a level below awareness so it is hard for humans to get how this affects their perception.
> 
> 
> ![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/making/mr250_lego.jpg)**#3 Comprehension** – To use an oversimplified metaphor, human comprehension is like a bunch of Legos. When it gets a new piece, it has to stick it to an old piece. The new piece cannot exist floating off by itself. For the brain to get it, it has to connect to something the brain already understands. This doesn’t mean that the association cannot move with time, but concepts cannot exist in a vacuum. The human brain comprehends by understanding the new data in relation to old data. This, for instance, is why metaphors are such a great tool in explaining new ideas. (Good metaphors, at least. The bunch of Legos is a little bit of a stretch.) It helps tie the new into the old. This is another reason that your brain might connect things in a way that you’re not conscious about. It’s just trying to understand, so it uses whatever reference tools it has available.
> 
> 
> 


The point of all this is that when you’re creating something new you need to have a basic understanding of how your new thing will be perceived. For card design, a large part of this is understanding grouping and grokking (sounds dirty, doesn’t it?). Why do people group the things together that they do? How will it affect how they see your card? What will they grok? What won’t they grok? Most importantly, how can you use this knowledge to make better cards? All fine questions. Let’s see which ones we can answer.


### Grouping and Grokking (still sounds dirty, doesn’t it?)


Now let’s take this idea and connect it back into card design. Many years ago I wrote a column called “[Design 101](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr68)” to help new designers recognize many of the early pitfalls to design. I listed five mistakes. Number two was: “The abilities on the card have no synergy.” While walking my readers through this mistake, I explained a common trend of new designers to overload their cards with abilities that have absolutely no synergy with one another. The underlying principle to this design rule is grouping and grokking (I’m going to stop bringing up this fact, but be aware it will sound dirty every time I mention it for the rest of the column).


Here’s the big design secret: Every card has to feel like it’s one thing. Yes, there are a few exceptions to this (split cards being a prime example), but the general idea is an important one to understand. Players want to grok cards. Grokkable cards are comforting. Non-grokkable cards are intimidating and generally uncomfortable. People play games for fun. Intimidating and uncomfortable are not so synonymous with fun. Cards with a single, unified design are much easier to grok.


So how does a designer make a card feel like one thing? By grouping the items on the card together. How does one do that? The most honest answer is that it comes from getting a good instinct for what feels right. But making sure it “feels right” is not so helpful a piece of advice, so let me walk you through a bunch of things that can put you on the right path:



> 
> **Synergy** – As I noted above, people’s brains want to connect things. One of the easiest ways to do this as a designer is to make the pieces of the card have mechanical relevance with one another. When the brain finds this connection it reinforces that everything feels right. This is why I urge designers to make sure that the separate pieces of their card work with one another.
> 
> 
> **Language** – If you notice on both [Vicious Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vicious+Hunger) and [Sift](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sift), the two abilities are written within a single sentence. You don’t do A and then later do B. You do A and B. “Do A and B” sounds like one thing. “Do A. Then do B” sounds like two. This might seem like a minor detail but in design there’s no such thing. All the pieces of the card have to work together to create the effect you want. Using the language to reinforce this is merely making effective use of your tools.
> 
> 
> **Flavor** – Another reason that [Vicious Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vicious+Hunger) and [Sift](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sift) work is that the overall flavor of the cards from the name to the art to the flavor text reinforces what the card is about. This is where card concepting becomes so important. If you want your direct damage and healing effects to feel linked, you have to create a feel for the card that interlinks the two.
> 
> 
> 


![Truth_or_Tale](https://web.archive.org/web/20100309150300im_/http://www.wizards.com/magic/images/cardart/TSP/Truth_or_Tale.jpg)![Truth_or_Tale](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/TSP/Truth_or_Tale.jpg)Today’s lesson is a simple but potent one. In design, as in all art, the whole has to be worth more than the sum of the parts. When you create a card, you have to make sure that each piece you add is contributing to the overall effect of the card. If it isn’t, cut it. It’s just mucking up your beautiful card. Save the cool idea for another card, one possibly where it might take center stage and have the elements built around it. If you try to connect things that players don’t want to connect, your card will seem disjointed and will (sometimes on a subconscious level) irritate them. This is why well-designed cards feel better: They are working with a player’s natural instincts instead of against them.


Which, of course, brings us back to suspend. How could R&D put a keyword mechanic that requires seven lines of text on common cards? Because suspend is very, very grokkable. Yes, it requires a lot of words to technically explain what has to happen, but the basic idea – you’re using time as a cost in exchange for needing less mana – is simple and elegant. And that… makes for a good design.


### Grok Me Amadeus


Probably not what you were expecting for Suspend Week, but then I always like to keep my readers on their toes. This column was a little more on design philosophy than my average column. If you like this kind of stuff and want to hear more of it, drop me a line. If you found it boring and want me to go back to the columns where I actually make jokes, also drop me a line. I’m very curious for your feedback as it will influence whether or not I do more columns like this in the future.


Join me next week, when pie is on the menu.


Until then, may you learn to continually add new Legos to your stash.


Mark Rosewater










---
[Link to Wayback Machine](https://web.archive.org/web/20201111230649/https://magic.wizards.com/en/articles/archive/making-magic/feeling-draft-2006-07-10)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Welcome to the first week of non-Coldsnap previews. Yes, today I have no preview card for you. That isn't to say I don't have a column all about Coldsnap. Come on, the set's due any day now, what else am I supposed to write about? Anyway, today's column is about a particular aspect of Coldsnap. Any rocket scientists reading (come on Henry, I know you are) will probably have deduced the topic (I knew naming my columns would come back to haunt me)."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "616661"
[_metadata_:publish_date]:- "2006-07-10"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Feeling a Draft"
[_metadata_:wayback_capture_timestamp]:- "2020-11-11 23:06:49"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201111230649id_/https://magic.wizards.com/en/articles/archive/making-magic/feeling-draft-2006-07-10"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/feeling-draft-2006-07-10"
---


Feeling a Draft
===============



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on July 10, 2006 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Welcome to the first week of non-*Coldsnap* previews. Yes, today I have no preview card for you. That isn't to say I don't have a column all about *Coldsnap*. Come on, the set's due any day now, what else am I supposed to write about? Anyway, today's column is about a particular aspect of *Coldsnap*. Any rocket scientists reading (come on Henry, I know you are) will probably have deduced the topic (I knew naming my columns would come back to haunt me). Yes, today I will talk about one of the greatest challenges of designing and developing *Coldsnap* – dealing with draft. Sound interesting? Keep on reading. If not, see you next week. (No really, you don't need to feel bad; not every week's for every reader.)

### Life Draft

*Coldsnap* is the very first tournament-legal set (yes, we retroactively have made sets like *Portal* tournament legal, but it wasn't designed as such) to be designed outside the block structure. As such, – 


> 
> We interrupt this paragraph to bring you the answer to a pressing question. Why is *Coldsnap* tournament legal? A number of readers seem very invested if finding out why. Being that this is the column that answers questions like this, I thought I'd take a quick moment to explain why. So, why? The shortest answer is because that is what we believe the majority of players want. Past experience with things such as *Portal* demonstrated that players got upset when we made cards that they wanted to play in their decks but couldn't. The *Un*-sets make sense as non-tournament legal as they break all sorts of taboos. Tournament players don't want that kind of craziness allowed. But if we made a set with interesting, normal cards and then told the public that they aren't allowed to play with them in any tournament, experience had shown us that we would get a lot of angry letters. Imagine having a card that perfectly complements your deck and wouldn't cause any disruption to the tournament scene, but you are told you not only cannot play the card now, but might never be able to play it, unless of course it gets reprinted in a tournament legal set. *That* is why the set is tournament-legal. We now return you to your regularly scheduled paragraph.
> 
> 
> 

- R&D had a challenge we had never faced before. Sets are always designed within the context of a block. Players have been taught exactly how to draft any set that might come out. The only exceptions are the base sets and the *Un*-sets. The base sets are drafted by themselves and the *Un*-sets are designed to be mixed into any draft pool. But *Coldsnap* had specific themes; themes that don't fit neatly into *Ravnica* block or *Time Spiral* block. This meant that *Coldsnap* couldn't easily be added to the end of the former or the start of the latter. The only choice would be that the set would have to be drafted by itself.

Anyone who has ever drafted three packs of a small set (like at a prerelease) can start to see the problems inherent in this set-up. A small set only has between 140 and 180 cards. (*Coldsnap* has 155.) This means that the repetition rate for cards (a.k.a. how many times you see a card per draft and between drafts) is quite high. This is problematic for two reasons that I will explain momentarily. If we (and by we, I mean both design and development – though to be fair, making draft work always falls more on the shoulders of development, as things like power level have a huge impact on how draft works) wanted to make an interesting draft environment, we had to solve both these problems.

### Art & Drafts

I often talk about how I design holistically. That is, I like to make choices while looking at the big picture. This means that whenever I have two or more problems, I like to examine them together because often the seeds of solving one problem rest in the other. To see how my mind works, I thought I'd walk you through these particular problems so you can see where we began to find our solutions.

### Problem #1 – Repetition in card evaluation is boring



|  |
| --- |
| *Repetition can be booooring.* |

The first time you see a card, you are intrigued (assuming the card's not a total dud). Does this card have anything to offer your drafting plan? You examine your options and your past choices and you decide either to take the card in question or to pass it. The second time you see the card, the choices are much less interesting. Very few cards warrant taking two of them. To make matters worse, the kind of cards you want to see two of seldom make it to you because other people also value them highly. When drafting solely from a small set, you are going to see the same cards a lot. A *lot*! 

All **Magic** booster packs (now at least) have fifteen cards, eleven of which are commons. A small set traditionally has between 55 and 60 commons. At 55 cards, that means you only have five packs worth of unique cards. You will see duplicate cards almost immediately. 

### Problem #2 – Repetition in card inclusion lessens play variance

The first problem involves the draft itself. The second problem is focused on the game play. What's the biggest problem with having a small card pool? You keep drafting the same cards. Why is this bad? Because it cuts into game variance. That is, having the same cards raises the chance the games play out similarly. For example, when you play two games with the exact same card pool (like say playing in a Constructed tournament), you have the highest chance of having two games feel identical. 

One of the biggest draws to Limited formats is that they shake things up more than Constructed. While two Constructed environments have some chance of feeling similar, most Limited formats shake things up much more. The biggest reason for this is the high variance of the cards and the fact that you only have access to one or two copies of any one card. This advantage of Limited is already lessened in draft because of the nature of how drafts work. This means repetition is most noticed in drafts.

I'll be honest that this issue was a daunting one for the designers and developers. The two problems listed above are real deal breakers. Luckily, R&D gets its most creative when backed into a corner (hmm, restrictions breed creativity…). Such is a case with *Coldsnap*. 

### Getting the Draft

Before I walk you through our various solutions, let me first explain what I call the non-negotiables. That is, these are the factors that design and development cannot change. Solutions have to come by working around these issues. Here are the relevant non-negotiables for *Coldsnap*:


> 
> **#A – The set cannot exceed 155 cards** – Because this is the first non-block tournament-legal expansion (and thus the first “fourth” set), we wanted to keep our set size on the lower side. 
> 
> 
> **#B – The set has to have normal rarity** – The common, uncommon, rare structure to our rarity is so engrained in our player base that changing it is plain foolishness.
> 
> 
> **#C – Draft had to be three packs of *Coldsnap*** – The set just doesn't play nicely with the themes of *Ravnica* block or *Time Spiral* block. (And for those out there that want to write in and quote last year's State of the Game column – yes, I'm working to making blocks work together. And the *Ravnica* and *Time Spiral* blocks do. You see, creating a set that had a theme that blended nicely between two sets that were already designed to have synergy without copying what was coming proved to be an impossible task.) This means that *Coldsnap*'s only option is a draft by its lonesome.
> 
> 
> 

Now comes the fun part. We have our straightjacket, our rope and our tank of sharks. Time to Houdini it up. Some designers are not fond of situations like this: you know, take these crazy conditions and make them work. Me? I thrive on this stuff. I used to do improv for fun because I loved the idea that I had no idea what I was going to do before I got up on the stage. Why have a creative job if you're never really going to give it a workout?

The first realization is to understand that no one solution is going to solve this problem. The key rests in finding a lot of little solutions. While the solutions I'm about to outline do have a purpose to their order, it was not necessarily the order in which we discovered them. As they make much more sense in this order, this is how I'm going to explain it.

### Solution #1 – Reconfigure the percentages of the rarities

How can you make the draft experience less random? Add more commons. This is the trick we use in the big sets (large sets have 120 commons while only having 80 uncommons and rares a.k.a. 120/80/80). But remember non-negotiable A. We can't add cards. Fine, let's borrow from Paul. After all Peter needs some loving. When this set started we had a normal distribution for a small set – 55/44/44. For those out there that can do math in their head, that adds up to 143. (I guess it adds up to 143 either way – the rest of you just had to wait for me to tell you the total.) 

There's a whole lot of math that goes into how many cards can exist of a certain rarity. It has to do with things like collation and “as fanned” percentages. You see, I studied words in college. I leave issues like this to the number guys. They come back and tell me what options are available. During design, the team stumbled upon the idea of helping out draft by increasing the number of commons. We asked the math guys what was the largest common size we could have and have the right balance of uncommons and rares and still stay at 155 or below. What came back was the 65/50/40 number.

### Solution #2 – Flatten the power band

How do you make sixty-five commons get as much mileage as possible in draft? Make them all relevant to Limited. That is, cut the bottom percentage; the part that never gets drafted. This, of course, leads to many letters saying, “You can do that? Why don't you do that to every set?”

The reason we don't do that is because it comes with a very high cost. Having a wide power band does all sorts of good things for the games. Because this is one of my technical columns, I'm going to briefly explain what I mean, but please be aware that each point below is worthy of an entire column so I'm just giving the sound bite version.

One, having a more stretched out, gentler slope allows trackable growth, meaning that it lets players get better and have the ability to track that they're getting better. This is a huge motivation to most players. Two, it creates more tonal variance. It shorthand, it makes the game feel more dynamic and creates more “exciting moments”. Three, it expands viable design space. Think of design as a finite resource. Stretching out the power band essentially increases that resource by a significant magnitude. Four, it makes skill matter more. This is an important one, so let me dedicate a whole paragraph to it.

Imagine a draft environment where every card had the same power level. What would separate the good drafters from the bad ones? Every player would get enough playable cards. They're all playable! Making the crucial twenty-third pick wouldn't be all that tough. You can't go too wrong. In addition, there is a lot of fun in figuring what cards other people are undervaluing. Players love finding the hidden gems. If there's no variance, there is a distinctive lessening of discovery. And as I've explained in “Making Magic” numerous times, the game is all about discovery.

So if the width of the power band is such an important thing, why are we messing with it? Because desperate times call for desperate measures. Our hands are very tied. Finding solutions rests in playing with areas we don't normally play with. This solution does create a new problem we have to solve. Trackable growth, tonal variance, viable design space are all important, but they can survive the changing of one set. The last, skill determination, isn't something we're willing to give up. This means that we have to find other ways to achieve this (and note that we didn't mash the power band completely, so the cards will lend themselves to some gradation).

### Solution #3 – Make repetition a positive

With 155 cards, even with 65 being common, players are going to see the same card over and over. How do we keep that from being a negative experience? As the header gives it away – we had to find a way to make repetition a positive. To do that we thought back to **Magic** cards of past that you were excited in a draft to see again and again. The simplest answer (and to all the future designers out there, here's probably the most important advice in this whole column – the simplest answer is the best answer the vast, vast majority of the time; don't ignore it) was cards whose power level grew through number – or in my lingo, self-referential linear cards - what I like to call the Plague Rat family.

![Plague Rats](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plague+Rats)I'm not sure if there exists a **Magic** card more influential than [Plague Rats](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Rats). Whole swaths of design space start with “I was trying to make a \_\_\_\_\_ that acted like a Plague Rat.” (Hello slivers.)Which leads us to the design team's first answer. I was sitting in the design meeting racking my brain for cards that you wanted to draft a lot of. What came to my mind was a card from my very first design team (*Tempest* for any new readers) – [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle) (a.k.a. Plague Bolt – it was my attempt to bring Plague Rat's joy to instants and sorceries). [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle) was the kind of card you loved seeing in your draft, the more times the better. What if *Coldsnap* had a cycle of [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle) cards?

Everyone liked the idea. The only stumbling block was the fact that the [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle) mechanic premiered years after *Ice Age*. In the end, we decided that the idea was so important to the set and that the [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle) mechanic wasn't keyworded, so it wouldn't feel too weird. Maybe it was where the *Tempest* designers got the idea in the first place. The set already has one card that premieres in *Coldsnap* that would later be “reprinted” in a later set. 

Design was happy with the [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle) cycle and stopped. This is where development picked up the ball. As they started drafting with the set, they saw the value of the [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle) cards. So much so, that they started adding more cards that made you want to collect as many of them as you could. They called these cards “collect me's”. With each development pass, another collect me was added. If my memory serves me, I think the final set ended up with eleven of them at common. And this isn't even counting all the cards with the new ripple mechanic (see [Aaron's column](/en/articles/archive/latest-developments/walk-through-cold-2006-07-07-0) last Friday for more info.) 

### Solution #4 – Include themes that players can choose to commit to

This next solution is another one where design put the seed of an idea in the file which development nurtured into a full-blown theme. When we talked about “snow matters” (a.k.a. snow-covered goodness), the team stressed that one of the things they disliked about the execution in *Ice Age* was that snow-coveredness always forced you to play all snow-covered lands or none. There just weren't any cards that encouraged a little amount of snow-covered lands. 

On a separate note, a few members of the design team remembered the organized play headache that was snow-covered land. As it was basic land, the floor rules at the time treated like all other basic lands. Players, for instance, could add as many snow-covered lands to their deck as they wanted. This made tournament organizers have to track down significant qualities of each of the snow-covered lands for use in Limited. It also made some deck registration headaches as it's very easy to forget to include the snow-coveredness of your lands if they're all the same. 

Add the two problems together and it was decided by the team that it would be much more interesting if snow lands were a resource that you had to focus on collecting. Instead of just being given access to it, you had to horde it. This allowed us a reason to put the snow lands in the set. It also allowed us to create cards that used snow lands without having them be busted in half. To make these cards powerful, you had to horde the snow lands. Meet collect me's number twelve through sixteen. 

This treatment of snow lands also allowed us to design a variety of snow matters cards. Some needed just one snow mana to do their thing. Others scale based on the amount of snow mana you have. The former only needs a little bit of snow, while the latter wants as much as you can get.

The other lesson that snow taught the development team was that it was interesting to have a theme that players commit to at different levels. This helps differentiate drafts. If each draft provides different path choices (that is, things that you really care about in some drafts and not care about at all in others), it helps make each draft more unique. This philosophy had a big impact on how the set was developed.

### Solution #5 – Avoid things that keep moving drafts in the same direction

Another discovery of development came from something design did incorrectly. In our quest to feel like the “lost” *Ice Age* set, the design team studied *Ice Age* and *Alliances*. We tried as much as possible to pick up as many themes as we could. One theme that we included was an “ally color” theme where cards encouraged allies to play together. As we were coming off the *Ravnica* block, the design team thought this might be a nice opportunity to provide some synergy between *Coldsnap* and the last block. Our fatal flaw? We forgot about draft (and we were doing so well with the [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle) cards).

The ally color theme made players draft ally colors, and there are only five choices. This greatly restricted draft options and made the drafts more repetitive. The only answer? Lose it. Development pulled the theme (well mostly – it's still there in small numbers) to help keep color options as open as possible for drafts.

### Skin Draft

While all of the above might seem simple in hindsight, it was a long and laborious process. The good news is that we accomplished our goal. *Coldsnap* is a very interesting (and I believe fun) set to draft. The decision tree is a bit steeper than normal and collecting affects the draft like never before. All I can say is try it, you'll like it. And either way, I'm interested to hear your opinion of *Coldsnap* draft. Love it or hate it, I'm eager to hear.

That's all I got this week. Join me next week when I trek through more snow. Uphill, both ways.

Until then, may you know the joy of the sixth [Kindle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kindle).

Mark Rosewater








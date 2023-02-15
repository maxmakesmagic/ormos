
---
[Link to Wayback Machine](https://web.archive.org/web/20170318214712/http://magic.wizards.com/en/articles/archive/making-magic/building-better-mousetrap-2014-06-09)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "657081"
[_metadata_:publish_date]:- "2014-06-09"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Building a Better Mousetrap"
[_metadata_:wayback_capture_timestamp]:- "2017-03-18 21:47:12"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170318214712id_/http://magic.wizards.com/en/articles/archive/making-magic/building-better-mousetrap-2014-06-09"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/building-better-mousetrap-2014-06-09"
---


Building a Better Mousetrap
===========================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on June 9, 2014 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 







Welcome to *Vintage Masters* Week. This week, we're going to be talking about the newest release for **Magic Online**, where players are going to have their chance to play a draft environment with cards from **Magic**'s distant past. As I wasn't on the design team for this product (the design team was Ethan Fleischer and Max McCall), I thought I'd pull back and talk about the topic from a slightly broader approach. How do you design an environment using only preexisting **Magic** cards? Cube, Duplicate Sealed, products like *Modern Masters* and *Vintage Masters*—how are the designed? Today, I am going to walk you through the basics. 

One quick caveat. Obviously, whatever format you are building toward will have a big impact on all the decisions below. Because I'm talking in general terms, I am not going to get format-specific.

### Step #1—Take Inventory of Your Card Pool

The first thing you have to do is figure out the card pool you are drawing from. Which cards are eligible? All cards? All black-border (and white-border) cards? All cards you own? All cards from particular blocks? All cards of a particular subset?

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/2014/mm_wk23_303_cardart_sicken.jpg)
[Sicken](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sicken) | Art by [Heather Hudson](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Heather%20Hudson%22%5D)


 The key to today's exercise is to figure out how to craft an environment. To do so, you have to know the tools available for you. Normally, I talk about how to design traditional **Magic** sets. While I'm allowed to use old cards as reprints, I have the luxury of making new cards, which means that I am able to have a much broader scope in setting my set's mood and themes. 

For this reason, I am able to start my designs not by asking what can be done but by what I want to do. When you are working with only preexisting cards, you don't always have this luxury. Your subset of cards is going to have a big impact on what is possible, so the first thing you have to do is take inventory so you understand what tools you are working with.

 Note that if you have a larger card pool (for instance, every card in **Magic**), you might need to do Step #2 before Step #1. 

Here are a few things you need to think about while doing this first inventory:


**Don't Dismiss Anything Immediately**


 Part of the process will be culling away the things that will not work, but it's important on your first pass to not make assumptions. For example, you will probably be aware of which cards were the better cards in the environments they were played. This doesn't necessarily mean the same cards will be the better cards in the environment you put together. Power can, at times, be situational, such that a card that shines in one environment might not even be playable in another. Also, you have a limited number of answers to your design problems. Dismissing cards early might prevent you from realizing later that they can be an answer to a problem, one you might not even be aware of when you do this first pass on your cards. 


**Take Lots of Notes (Especially on What Interests You)**


One of the biggest reasons to do this first inventory is to refresh in your mind what's available. The metaphor I'll use here is having a box of Legos. If you want to build something out of all your Legos, the first thing you want to do is empty your box and see what you have to work with. What unique pieces jump out at you? What colors do you have a lot of or few of? What size and scope is reasonable for your project? An important part of making a cool environment out of existing cards is to spend the time and energy understanding what you have to work with. I suggest taking a lot of notes, because when you're done with the inventory, you want to be able to see everything you've learned in one place.


**Figure Out the Strengths and Weaknesses of Your Card Pool**


Probably the most important thing you're learning while doing this inventory is understanding what your card pool is good and bad at doing. What can each color (and artifacts/multicolor/colorless/etc.—whatever else you care about) do well and what does it do poorly? What mechanics offer many choices and which ones offer few? (Note that, by mechanics, I am talking more about basic things like creature destruction than keyword mechanics.) Where are you going to have an embarrassment of riches, where you have lots of decisions, and where are you going to be scraping by to find answers? These strengths and weaknesses are going to be the defining elements in figuring out the structure of your set.


**See If a Theme Stands Out**


The next step is all about figuring out your theme. One of the reasons doing an inventory can be valuable is that sometimes a theme will jump out at you.

### Step #2—Figure Out Your Theme

 Many years back, I wrote a two-part article about my wedding ([Part 1](http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/8) and [Part 2](/en/articles/archive/cosmic-encounter-part-ii-2008-10-27)), where I talked about the importance of themes. In it, I explained that when you are putting together a creative endeavor, it helps to have some focus. As the head designer, I make sure that each block has a crystal-clear bull's-eye so everyone is working in the same direction and that bull's-eye is always tied directly to the set's/block's theme. 

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/2014/mm_wk23_303_cardart_etheriumhornsorcerer.jpg)
[Etherium-Horn Sorcerer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Etherium-Horn+Sorcerer) | Art by [Franz Vohwinkel](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Franz%20Vohwinkel%22%5D)


 Now that you've done your inventory, you need to figure out what theme calls to you. Note that you get to have subthemes working in conjunction with you major theme, but you want focus on one major theme. As an example, *Innistrad*'s graveyard and tribal themes were subsets to its Gothic horror theme, which meant that we used them to enhance the Gothic horror theme and not to be the factors that dictated the structure. The same has to happen to the set you are building. Something has to have priority. Something has to be the thing that you're going to use to focus what you're building. 

As I said above, if your card pool is very large (bigger than, let's say, a few thousand cards), you might need to start with your theme as a means to narrow down your card pool. But other than that, I feel it's important to do your inventory before choosing your theme.

When deciding your theme, here are some things to think about:


**Decision #1: Does Your Theme Want to Be Based on Mechanics or Flavor?**


 There are two basic ways to do **Magic** design, bottom-up (mechanics first) or top-down (flavor first). *Zendikar* and *Return to Ravnica* were designed as bottom-up blocks. *Innistrad* and *Theros* were designed as top-down blocks. Note that choosing mechanics or flavor does not mean the other won't be present or important. It just means that the key decision making will first be focused on one aspect. 


**Decision #2: Does Your Theme Have the Volume You Need?**


 One of my design maxims is, "If your theme is not at common, it isn't your theme." What this means is that, when designing a **Magic** set, you have to make sure that what you are doing can be played out in the portion of the set that is going to make up the majority of the cards. Now, when you are crafting your own environment, you are no longer tied down to commonality like we are. If you want rares and mythic rares to make up a larger amount of your set, you can, but be careful what impact that will have on your set. (More on this below.) 

The reason I bring up this issue here is that, when picking your theme, make sure you have enough cards that the theme can show up enough to be clearly seen as the theme. If you have 300 cards in your set and, for instance, only 20 of them are part of your theme, no one will be able to detect that your choice of theme is your theme. The way I like to think of it is to make sure your theme shows up on at least three cards per pack if you're drafting, which means that, at bare minimum, at least 20% of your set has to be strongly on theme. You most often will want more, but I wouldn't do any less. And yes, this will limit themes that you can choose.


 **Decision #3: Are You Trying to Do a Theme **Magic** Has Done Before or Not?** 


 At first blush, this might seem like an odd question. If we're only using existing cards, how could the theme be something **Magic** hasn't done? The answer is, "Pretty easily." Imagine a set built around *The Wizard of Oz* or around cards with titles starting with vowels. If you want to do many of the obvious things, then yes, it's going to be hard to avoid something **Magic** has touched in its last twenty-plus years (although far from impossible), but if you get creative, you can do all sorts of things **Magic** has yet to touch, specifically, in theme. 

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/2014/mm_wk23_303_cardart_thoughtboundprimoc.jpg)
[Thoughtbound Primoc](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thoughtbound+Primoc) | Art by [Jeff Miracola](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Jeff%20Miracola%22%5D)


### Step #3—Divide Your Card Pool

Once you have picked your theme, the next step is to divide your card pool into four categories:


**Category #1—In-Theme**


These are cards that work directly into what your overall theme is.


**Category #2—Theme Adjacent**


These are cards that aren't directly in your theme but play well with it.


**Category #3—Neutral**


These are cards that don't play with your theme but they don't play against it either.


**Category #4—Anti-Theme**


These are cards that directly work against your theme. Note that cards that are good against your theme (for instance, artifact destruction in an artifact theme) are in-theme, not anti-theme. An example of anti-theme might be cards that care about color in a set with a strong artifact theme. This pile could be tiny or large depending on your theme.

### Step #4—Start Building Your Set

Start by putting away Category #4. Barring very extenuating circumstances, you are not going to look at these cards again.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/2014/mm_wk23_303_cardart_necrologia.jpg)
[Necrologia](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necrologia) | Art by [Scott M. Fischer](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Scott%20M.%20Fischer%22%5D)


Next, divide up Category #1 into the following piles: For each color make a creature pile and a noncreature pile. Do the same with artifacts, land and colorless spells. For the multicolor spells, unless you have a multicolor theme, you can just put all the multicolor creatures in one pile and all the multicolor spells in another pile.

 A quick aside: When you are building your own environment, you have the freedom to do whatever you want, which includes off-balancing your colors or even not using all the colors. For today, I am going to assume you're balancing your colors (meaning you have the same number of each color at each rarity), because doing it any other way will have all sorts of pitfalls that I don't want to get into. Additionally, I am going to assume that you're going to stay roughly at the same rarity distribution. You clearly can shift what sits at what rarity, but if you deviate too much from normal **Magic**, you'll find yourself starting to have balance and complexity issues. 

Next, take each color and look through it, jotting down notes on what mechanics/subthemes are coming through in each color. One of the most important things you need to do is make sure that each color in your set has a strong identity. Eventually, you are going to think about how the colors interconnect, but for now you need to focus on what each color in your set is about.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/2014/mm_wk23_303_cardart_crueltutor.jpg)
[Cruel Tutor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cruel+Tutor) | Art by [Kev Walker](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Kev%20Walker%22%5D)


For each color, write down a few possible things that will tie together the color. Once you are done with that, take your notes and examine what other colors have cards that play into any of the themes you jotted down for another color. As you find overlaps in mechanics and subthemes, write them down. After this pass, take a look at all your notes to figure out the following two things:

1. What are your most promising connectors? What elements seem to work well together? What colors are they in?
2. What are your deficiencies? Where are the gaping holes in the first category of cards? What color or colors have the weakest support?

As an example, let's say I want to do a graveyard-themed set using only cards from the last two years. As I look through each color, this is what I see:


> 
> **White:** The major white theme with the graveyard is returning permanents from the graveyard to hand and to the battlefield. There is a smaller theme of removing cards from the graveyard.   
> **Blue:** The major graveyard theme in blue is milling.   
> **Black:** Black has a bunch of graveyard themes, including getting creature cards from the graveyard to hand and to play, milling (including a subset from *Gatecrash* that we called grinding), and graveyard removal.   
> **Red:** There are few mono-red cards that play into the graveyard theme.   
> **Green:** Green's major theme with the graveyard is using it as a resource, either by pulling things out of it or by caring about things in your graveyard. 

Let's now ask the two questions. What is our most promising connectors? Well, white, black, and green each care about having things in your graveyard, while blue and black have means to get cards into the graveyard. What are our deficiencies? Well, red is a huge problem. It's just not playing very well into our theme. These two factors are going to be the beginning of building our set's infrastructure.

Now it's time to do the same thing to the Category #2 cards that you did with the Category #1 cards. The one difference is that you are going to look at this batch through the lens of what you learned from the first category. You are going to look for things that synergize with your strengths and look for things that fill in your weaknesses.

 We know that, in our ongoing example, white, black, and green all care about cards in the graveyard. This means that we'll be on the lookout for other cards that can get cards into the graveyard. For instance, looting (drawing a card and discarding), cards with discarding as a cost, and cards that inadvertently get cards from the top of the library into the graveyard (for example, green cards that search for lands or creatures off the top of the library, such as [Commune with the Gods](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Commune+with+the+Gods)) all play nicely into the theme. 

Also, as we know red is lacking in the main theme, we have to start looking for things for red to do. The reason we want to look for that early is because of an important tenet of design. Early in design, you have a lot of flexibility, but as design evolves and things get set, it's harder and harder to make changes. This means that you have to prioritize what matters most and start there. Matching the core of your set's theme and filling in the main deficiencies are those early things you have to focus on before things start to settle.

Finish this step by doing the same with the Category #3 cards you did with the first two groups. On this pass, you are looking in particular for things to fill in the holes in your set. Remember, that part of filling in the structure is committing to the different subthemes.

### Step #5—Start Solidifying What Colors Do

Now that you've looked through all your cards, it's time to make a commitment as to what each color is doing in your set. Usually, part of figuring this out is committing to what mechanics you want in your set. Note, though, that mechanics are most often used in more than one color. This is done to give each mechanical theme some variance. If all the necessary cards are just sitting in one color, it threatens to drive down the replayability of your set.

Once you have a general idea of the subtheme for each color, you're going to want to pair up each of the ten-color combinations and ask yourself what those two colors are doing together. A lot of the definition of a set comes from these two-color interactions. Write down what you think each two-color combination is going to be about.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/2014/mm_wk23_303_cardart_cruelbargain.jpg)
[Cruel Bargain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cruel+Bargain) | Art by [Adrian Smith](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Adrian%20Smith%22%5D)


Let me jump in here to point out that you probably won't, at first, find focuses for all ten two-color combinations. That's okay, you'll figure some of it along the way. Also, you will come up with ideas that might seem great at first blush but, as you play with the cards, they will turn out not to work. This list is not final but, rather, a work-in-progress.

I should also point out that this is where mechanics start serving a higher purpose. Most of your mechanics will be used in two or more colors and will start being used when you are trying to identify the archetype for each color combination.

### Step #6—Find Your Crisscross Cards

I guess I should start by defining what a crisscross card is. It's a card that fits into two or more subthemes of your set. Crisscross cards are important because you want to make sure your cards have value to more than one archetype. This is key for Limited environments, Draft especially. The reason is that it's important that few cards in your set are only wanted by a single archetype. This tends to lead to stagnated deck building where the decks of an archetype all look very similar.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/2014/mm_wk23_303_cardart_morphling.jpg)
[Morphling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Morphling) | Art by [rk post](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22rk%20post%22%5D)


 When doing normal **Magic** design, you tend to design most of your crisscross cards from scratch, as they are hard to find. In an enclosed system, that means you have to make sure to think about the crisscross cards earlier, so you can find them and build the set around them if necessary. 

In the previous step, you wrote down your subthemes for each color. Now you need to start finding crisscross cards that overlap those subthemes. The trick is finding ones that feel like they naturally belong. The crisscross cards have to come early because they're going to influence how your set comes together.

 Once the crisscross cards are in, finish filling out your set. No matter what, make sure to create a full card set, even if you aren't completely happy with some of the choices. The reason ties back to advice I got in writing class: You have to finish the first draft, because no rewrite work can be done until you finish the first pass. **Magic** design is no different. Having something built will allow you to play and learn, making substitutions along the way. Which leads us to our next step: 

### Step #7—Iterate

Once you have a card set, the next step is playtesting. Make sure when playtesting to keep good notes as you play, as well as getting every playtester to give you feedback. With each playtest, you'll get a better sense of which cards are working and which ones are not. You'll also learn if entire subthemes are working. Hopefully, you can settle down on your subthemes in the first few playtests so you can focus more on mechanics and individual cards, but remember that any part of the set should be removed if it isn't contributing to the set as a whole.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/mm/2014/mm_wk23_303_cardart_goblinsharpshooter.jpg)
[Goblin Sharpshooter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Sharpshooter) | Art by [Wayne Reynolds](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Wayne%20Reynolds%22%5D)


The one thing I will caution you about is not changing too many things between iterations. The point of making changes is to track the differences, but if you change too much at one time, it becomes too hard to get a sense of what is and isn't working.

### Step #8—Enjoy

It takes a long time to build a strong set, so be patient. Also remember that the set will have to be bad before it can get to a point where it's good. Finally, what we are talking about is a complex project, so there are a lot more issues than I can easily cover in a single article. I tried to hit the high points today to help give you the basics of what you need to do.

 For those of you out there who are interested in a project like this, I'm curious if you found today's article to be helpful. Feel free to email me through the link at the bottom of this article, post in the article's thread, or contact me through any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro#)). 

Join me next week when I take a look at the bright side of life.

Until then, may you find the card you need to fill the gap you have.

  


---

  
### "Drive to Work # 128 & 129—Wordwake, Parts 2 & 3"

 Today's two podcasts are the second and third parts of a three-part series on the design of *Worldwake*. 

  



* [**Episode 129**](http://media.wizards.com/podcasts/magic/drivetowork129_worldwake3.mp3): *Worldwake, Part 3* (16.6 MB)
* [**Episode 128**](http://media.wizards.com/podcasts/magic/drivetowork128_worldwake2.mp3): *Worldwake, Part 2* (14.6 MB)
* [**Episode 127**](http://media.wizards.com/podcasts/magic/drivetowork127_worldwake1.mp3): *Worldwake, Part 1* (14.0 MB)
* [**Episode 126**](http://media.wizards.com/podcasts/magic/drivetowork126_lenticular2.mp3): *Lenticular Design, Part 2* (15.9 MB)
* [**Episode 125**](http://media.wizards.com/podcasts/magic/drivetowork125_lenticular1.mp3): *Lenticular Design, Part 1* (13.3 MB)
  
* [**Complete Drive To Work Podcast Archive**](http://www.wizards.com/Magic/magazine/Article.aspx?x=mtg/daily/mm/drivetowork)











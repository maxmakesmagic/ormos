
---
[Link to Wayback Machine](https://web.archive.org/web/20200921133529/https://magic.wizards.com/en/articles/archive/making-magic/utter-chaos-2007-01-15)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "616981"
[_metadata_:publish_date]:- "2007-01-15"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Utter Chaos"
[_metadata_:wayback_capture_timestamp]:- "2020-09-21 13:35:29"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200921133529id_/https://magic.wizards.com/en/articles/archive/making-magic/utter-chaos-2007-01-15"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/utter-chaos-2007-01-15"
---


Utter Chaos
===========



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on January 15, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 







Welcome to Week Two of *Planar Chaos* Previews! This week I’ll continue explaining how *Planar Chaos* was designed. (I really recommend checking out [last week’s column](/en/articles/archive/making-magic/chaos-theory-2007-01-08) if you haven’t done so, as this week’s column builds on things I talked about.) I’ll hit a few new issues (including one that [last week’s thread](http://boards1.wizards.com/showthread.php?t=766876) brought up). And I’ll even find time to throw in a preview card. (Why do most columnists just get one week of preview cards while I always get two? To paraphrase Mel Brook’s *History of the World, Part I* – “It’s good to be Head Designer.”)


### Preview To A Kill


Last week I made you wait until the very end for the preview card, so I figure it’s only fair today to start with it at the beginning. This card is going to set up the discussion of the day more than vice versa. As such, I need to begin by showing it to you.


Here you go.


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/making/mr262_6l71dm48y0jym8wt.jpg)
I know this card raises a number of questions, some of which I’m going to address today. I guess I should start with the most obvious: Vanishing? Hey, isn’t that just fading?


### Fade to Vanish


Yes. And no. You see, part of the design of *Planar Chaos’s* “alternate reality” theme was to examine how many different facets of **Magic** could have been different. This introspection included mechanics. In fact, the *Planar Chaos* team made a bold decision. The mechanics in *Planar Chaos* (and by mechanics I mean card elements that show up consistently over numerous cards, most of which are not keyworded) are reinterpreted old mechanics. As with everything else in the set, we take a “what if” approach to mechanics showing how those mechanics could have been done slightly differently. The biggest difference from other “what if” scenarios is that for the mechanics we chose to do things that we felt we either did incorrectly in the past or which had more design space than originally conceived.


 



![Blastoderm](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Blastoderm)

What does this have to do with fading? Simple: R&D believes we messed up with fading. The overall idea, spend less but only get the card for a limited duration, is awesome. The problem came with the execution. While designing fading, Mike Elliott (the design lead of *Nemesis* and the creator of the fading mechanic) made the decision to have the fading number match with the number of times a creature could attack. This way when you saw a fading 3 creature, you could do the simple math, multiply their power by three to figure out the damage potential. The problem with this execution is that it plays against expectation.

I’ve talked about this concept of design before, but let me walk you through the points once again. Design’s goal is to make playing the game as straight-forward as possible. We want the cards to do what you think they do. Because this is so important, we spend a lot of time trying to figure out how players will perceive something. Sometimes this process leads us to interesting discoveries.


A common occurrence is that everyone playing with a card consistently plays it incorrect. When this happens, do you know what we like to do? We change the card to match everyone’s intuition. Why? To quote a Jim Croce song “You don’t tug on Superman’s cape / You don’t spit into the wind / You don’t pull the mask off the old Lone Ranger/ And you don’t mess around with Jim.”


![Far_Wanderings](https://web.archive.org/web/20130605183632im_/http://www.wizards.com/magic/images/cardart/TOR/Far_Wanderings.jpg)![Far_Wanderings](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/TOR/Far_Wanderings.jpg)My point is this: Good game design plays into the intuitions of the players. If something feels natural, that means players will play the card correctly. If it doesn’t, you’ll be fighting with them constantly to play the card right. It’s a fight you can win, but most often at a cost that you don’t want to spend. The best games succeed because they play into player expectations. The games deliver because they give the players what they want. 


Let me take a quick example from my Hollywood writing days. I can write a romantic comedy where the two lovebirds destined to be together don’t end up together. I can craft a murder mystery that doesn’t get solved. I can create a soap opera where everyone gets along. But you know what? My chances for failure go way, way up. Why? Because people tune in to certain genres because they know what to expect. Romantic comedies end happily with the lovebirds getting together. Murder mysteries get solved. And soap opera characters hate each other (when they’re not in love with one another that is – and even then sometimes they still hate each other). Genres are what they are because essentially they tap into basic needs of the human experience.


Games are the same way. People play games because they create an experience that they can predict and enjoy. This doesn’t mean that there can’t be surprises. But the surprises need to be in places with comfortable surroundings.


### Um, Weren’t We Talking About Fading?


What this long-winded explanation is all about is this: Fading had a fundamental flaw. As a quick refresher, here’s how fading works. The permanent comes into play with N fade counters (where the mechanic is “Fading N”). At the beginning of each upkeep you remove a fade counter. When you are unable to remove a counter, the permanent is put into the graveyard. See the flaw?


Here it is: Players expect for something to happen when you run out of something. Not a turn later. This is why we made suspend “go off” when the last counter was removed. Anyway, when *Time Spiral* design started, we actually put suspend and fading into the set. They seemed like natural bookends, but we quickly found a problem – three problems, actually.


![Morphling](https://web.archive.org/web/20191104183625im_/http://www.wizards.com/magic/images/cardart/UZ/Morphling.jpg)![Morphling](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/UZ/Morphling.jpg)The first problem was that the two mechanics, while very similar, were not identical. Suspend triggered when the last counter was removed while fading triggered the turn after the last counter was removed. Having two things this close but not identical is bad design. Why? Because players will naturally assume that two similar mechanics work the same way. Why? Because players assume that games have an internal consistency. Once they learn how one thing works, it’s assumed that other elements will follow suit. And by the way, internal consistency is a hallmark of good game design.


The second problem was that fading uses fade counters while suspend uses time counters. Having different names meant we couldn’t make cards that could manipulate both cards with suspend and cards with fading (well, we could, but it would be clunky).


The third problem was that having two mechanics in the same set that forced you to put a card into play with counters increased confusion. Often we found ourselves thinking a suspended card had vanishing or vice versa. We started by solving the third problem. We moved the mechanic to *Planar Chaos*. We decided that once the players had some time with suspend under their belt, it would be easier for them to remember which is which.


We examined the idea of changing how fading worked and using Oracle to retroactively errata the old cards but we felt the need to raise the number on every card along with the fact that the change would functionally alter some of the cards (particularly the ones where you remove a fade counter to achieve some effect) went against our errata policy (yes, we have a policy about what can and cannot be errataed).


This, of course, led us to the next approach. We came up with a new keyword. That’s what vanishing is. It’s fading 2.0. It’s how we wish fading had always worked and it’s what we plan to move forward with in the future.


Real quickly, here’s how vanishing works. When a permanent with vanishing N comes into play you put N time counters on it. At the beginning of each upkeep, remove a time counter. When the last time counter is removed, sacrifice the permanent with vanishing. It works just like suspend except the zone change is from play to graveyard rather than from out of the game to play. Also, even though Chronozoa has a “put into the graveyard from play” trigger, not all vanishing creatures do. The more simple ones simply go away after N turns.


Once vanishing got put into *Planar Chaos*, we realized that the need to change the term actually played into our theme. In fact, reinventing old mechanics became a key component of what *Planar Chaos* was doing.


Yes, this means that *Planar Chaos* is not debuting any truly new mechanics. Yes, we will have individual cards that do things you’ve never seen before, but the mechanics themselves are all old mechanics. We’ve spiffed them up and done some things with them you haven’t seen, but in the end this set plays around with known quantities.


### What’s New?


Which is a nice segue into an issue that raised its head in [last week’s thread](http://boards1.wizards.com/showthread.php?t=766876). The debate revolves around whether or not the design of *Planar Chaos* is creative. But why paraphrase when I can go right to the horse’s mouth (at least one of the horses’ mouth – not that this means I’m calling him a horse)? The post was by margalis:



> 
> I have no problem with functional reprints being "timeshifted" cards, although it is a bit silly given that every set has functional reprints. Why wasn't [Heartbeat of Spring](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heartbeat+of+Spring) timeshifted?
> 
> 
> My problem is that all these timeshifted cards count against the total number of cards in the set, unlike the TSP cards that are extra.
> 
> 
> This set is going to have very few new cards in it. That is extremely lame and extremely uncreative.
> 
> 
> Giving an old card a new name and font color is the definition of uncreative. Again, as a supplement I am fine with that. Nearly all of PC is been there, done that. We are all familiar with Wrath, [Ball Lightning](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ball+Lightning), etc.
> 
> 
> I can appreciate the flavor but I think Kami proves that players prefer a fun environment over a flavorful one. It seems that Wizards has forgotten why many players buy new sets - to get new cards. Not rehashes.
> 
> 
> PC has some cool cards but the whole will be much less than the sum of it's parts. A black Wrath is cool, a green Ball is cool, etc, but put them all together and you have a crusty old set.
> 
> 
> How many genuinely new cards is PC going to have? 4?
> 
> 
> 


I will now say to margalis and any others with a similar viewpoint what I said to the design team. The role of design in **Magic** is to constantly take the game in new directions. We have to continually allow the player base to rediscover the game. Our job is to reinvent **Magic**, set after set. To do this, we have to embrace several important points:


1. **We have to be willing to change how we design**. If we want to surprise our audience, we have to approach design in different ways. There is no better way to become predictable than to keep doing things the same way year after year.
2. **We have to take risks**. If our task is to constantly evolve, then nothing will stop us quicker than an unwillingness to try untested things. To do the unthinkable, we have to be willing to embrace the unknown. If we don’t know our own limits, how can the players know them?
3. **We have to respect our audience**. Our players are very smart. We can do things that are complicated or subtle or tricky (although note that it is possible to get too complicated or too subtle or too tricky such that we lose most of our audience). We have to trust that our audience will spend as much time thinking about the set as they play it as we do as we design it.
4. **We have to let different parts of design shine**. There are many different aspects to good design. At any one time only a few can shine. That’s okay. One of the ways to get the variety we need is to allow ourselves to keep shifting our focus. This means that certain aspects will be a fundamental part of one design and mostly irrelevant to another.

![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/making/mr262_ptmekjzcmda29k6a.jpg)In short, I think the focus is on the wrong question. Is the design of *Planar Chaos* creative? I believe it’s almost emphatically so. We approached the design in a way we’ve never approached design before. We designed the set in a manner we’ve never designed before. The design is very “out of the box.” I think the real question is not about creativity but innovation. Is what we’re doing in *Planar Chaos* innovative? No. And yes.


I guess I need to start by defining what innovative means. Trusty **dictionary.com** defines it as “producing something like nothing done or experienced or created before.” Is a black [Wrath of God](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) innovative? No. Clearly it can’t be. It’s obviously very much like something created before. My question back to the thread is this: Does a design need to be innovative to be good? Personally, I don’t think so.


A **Magic** design has to be fun. It has to excite players. It has to stir discussion. It has to create new deckbuilding options. It has to push the game in a new direction. Do black Wrath (aka Damnation) and other cards of its ilk do these things? Plenty of the players online are eager to play with Damnation. Many are very excited for it to come out. Its preview spawned numerous threads and articles. Numerous players feel that it’s going to enable decks that aren’t good enough to play right now. And others are hypothesizing what the new world with a black Wrath will be like. So yes, Damnation is doing its job.


My point is that there are many facets of design and, as I point out above, you can’t focus on every one every time. True, *Planar Chaos* doesn’t put all its chips on the innovation square, but that doesn’t mean it’s a bad design. It means that we’ve chosen to focus on different aspects. (And for innovation lovers out there, let me stress that this block has just as much innovation as any block – probably more – we’re just saving the bulk of it for the last set.) It’s not laziness. It’s not desperation. Ironically, we’re trying something new. I guess in the end we are innovating, only this time in the very form of how we’re designing.


### But Wait, There’s More


![Mind_Bend](https://web.archive.org/web/20130605180856im_/http://www.wizards.com/magic/images/cardart/9ED/Mind_Bend.jpg)![Mind_Bend](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/9ED/Mind_Bend.jpg)For a set with nothing “new,” there’s a lot of stuff you’ve never seen before. Look for us to make twists with suspend (and to a lesser extent with split second and flash). Look for yet another old keyword mechanic making a return (hint: it starts with a “k” and rhymes with sticker). Look for a number of older mechanics to get a makeover (the people paying attention in *Time Spiral* should already be able to guess what we’re doing with echo). Look for “alternate reality” versions of popular spells from the past (changed in various ways – colorshifting is just the trick the timeshifted cards use). Look for some color pie exploration (once again, I will spend an upcoming week explaining why certain colors got certain abilities). 


Like *Time Spiral* (and *Future Sight* too), *Planar Chaos* is a set that has a lot packed into it. Much of the nuance will take time to see. When you open your packs at this weekend’s [prerelease tournaments](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/prerelease/planarchaos) (hint, hint), take the time to really look at the cards. There’s a lot going on.


That’s all I got for today. For anyone who wants to take the time, I’m curious to get your initial feedback on *Planar Chaos*. How do you feel about the set before seeing most of the cards? Do you like the high concept of this set? Are we playing around in areas that you think we should play in? What preview card has had the biggest impact? How do you feel about the set? I want to know.


Join me next week when I continue to dig into the design of *Planar Chaos.* Just like the set itself, the design had a lot of “what if” moments.


Until then, may you try tackling your problems with a solution you’ve never tried before.

 


Mark Rosewater









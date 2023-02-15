
---
[Link to Wayback Machine](https://web.archive.org/web/20220627054734/https://magic.wizards.com/en/articles/archive/latest-developments/sculpting-flow-and-fiero-2012-03-01)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "Occasionally, at some kind of conference or expo or gathering or what-have-you, somebody asks me to take off my goofy Magic-developer-dragon hat (you should check it out sometime?it's sorta like Mickey's in Fantasia, only `edgier,` in accordance with our style guide) and speak in broader strokes about game design as an intellectual discipline. Today, I want to do something"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "194126"
[_metadata_:path_date]:- "2012-03-01"
[_metadata_:publish_date]:- "2012-03-02"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Sculpting Flow and Fiero"
[_metadata_:wayback_capture_timestamp]:- "2022-06-27 05:47:34"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220627054734id_/https://magic.wizards.com/en/articles/archive/latest-developments/sculpting-flow-and-fiero-2012-03-01"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/sculpting-flow-and-fiero-2012-03-01"
---


Sculpting Flow and Fiero
========================



 Posted in **Latest Developments**
 on March 2, 2012 






![](https://web.archive.org/web/20211024110319im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By Zac Hill











Occasionally, at some kind of conference or expo or gathering or what-have-you, somebody asks me to take off my goofy **Magic**-developer-dragon hat (you should check it out sometime?it's sorta like Mickey's in Fantasia, only "edgier," in accordance with our style guide) and speak in broader strokes about game design as an intellectual discipline. Today, I want to do something similar.

Often here at DailyMTG.com, we talk about the process of making **Magic**. But we don't really say very much about game design more broadly. In truth, though, the field of game design is *exploding*. Recently I spoke at a high school career fair?*study hard, eat your vitamins, topdeck savagely*?and was absolutely floored to see the results of the survey where the principal asked the kids what they wanted to be when they grew up. Answer number one? Doctor, sure. Saving lives, yeah yeah yeah. But just below that?

Game designer.

![ld184_rich.jpg](https://media.wizards.com/legacy/mtg/images/daily/ld/ld184_rich.jpg)  
We've come a long way from sixteen-pixel spaceships and line-dancing aliens. Nowadays, the principles of game design are being applied to fields as diverse as policy analysis, applied biochemistry, developmental psychology, and education. In other words, the volume of information out there about game design is proliferating at an incredible rate. And we in Ramp;D do our best to keep our fingers on the pulse.

I'm often asked what are the best game design books I've ever read. There are several, obviously, and if you asked ten different people in Ramp;D you'd probably get ten different answers. Two of them, however, stand out especially to me: Jesse Schell's[*The Art of Game Design*](http://artofgamedesign.com/)and Jane McGonigal's [*Reality is Broken*](http://realityisbroken.org/).

![ld184_artreal.jpg](https://media.wizards.com/images/magic/daily/ld/ld184_artreal.jpg)  
Any summary I offer here of either of these books is going to fall wildly short of the mark, so I'm not going to even attempt to generalize what either is about. But I do want to examine a common takeaway from both: the idea that games are primarily valuable due to the emotional responses they evoke and the experiences they engender in their players. Today's article is going to draw heavily from both sources. Specifically, I want to take a look at the two responses that, I believe, games sculpt better than any other media. One is called *flow*, and the other, *fiero*.

What a Feeling
Before I dive into each of those experiences, though, I want to examine this notion of emotional engagement. It's not at all intuitive, after all, that how a player *feels* should be a central concern of a game's design. Aren't many games highly abstract, existing in a different dimension entirely than the primal, visceral, sense-engaging stimuli of most other modern media? Can't it even be argued that the absence of authorial control?*players* drive the narrative paths of games, after all?conflicts with the very idea that a game designer can create and share a core emotional experience with an audience?

Everyone has to agree, though, that people play games for *some* reason. After all, one of the defining attributes of any game is that it is, in a some sense, voluntary work. There is almost always a problem to resolve. Almost always, the resolution of that problem requires some kind of directed engagement?or at least the *illusion* of directed engagement, which is sometimes even more powerful. And coming up with the right way go about that engagement almost always requires effort. It is not at all easy to propel a ball in a high arc through a hoop ten feet off the ground, or to lob a grenade across the map into a sniper den while evading a hailstorm of gunfire, or to reduce an opponent from 20 life-points to 0 by (a) selecting sixty cards from a library of thousands and thousands to form a deck and then (b) memorizing hundreds of arcane rules that tell you how to deploy those cards.

![](https://media.wizards.com/legacy/mtg/images/daily/ld/ld184_jace.jpg)[Jace, Memory Adept](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace%2C+Memory+Adept)| Art by [D. Alexander Gregory](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22D.+Alexander+Gregory%22%5D)

When they do things that require effort, human beings require payoff in order to render that effort worth it. When you're doing something like going into work every day, that payoff comes in the form of money and benefits?and even then, the brain hates extrinsic rewards. But millions of people invest millions and millions of hours into games they have to *give* up money in order to play. Either we're all idiots or we're all getting something out of it!

What this means for you as a game designer is that if you're going to ask people to do voluntary work, you have got to make sure they're getting something out of it. The single biggest mistake I see from amateur game designers is that they create a system and then expect people to marvel at the cleverness of the system once they participate in it. But if that system isn't engendering an experience, you aren't doing your job.

Furthermore, you have to make sure the experience you're engendering plays into a strength the media you're working in does a good job of maximizing. As an example, I think one of the lessons we learned from the *Weatherlight* story is that card games aren't an effective vehicle for linear narrative. Conversely, as a literary author, I've taught a class at Richard Hugo House here in Seattle about the types of experiences fiction is good at conveying. Linear narrative is one of them, as are constructive introspection, empathic perception, and a whole host of other things. But?to get back on track?fiction is actually quite bad at relaying (for example) experiences of flow and moments of *fiero*. Games, by contrast, are excellent in those respects.

I'm not going to ignite a debate over whether games are, or are not, an art form. I am, however, going to observe that if the process of creating art involves the maximization of resonant experience in a given medium, there are certain experiences for which the medium of gaming excels at replicating. Flow and fiero are chief among those.

So, uh. What are they, exactly?

Get in the Zone
Most of the time, people don't talk about games using overly wrought language of "maximized resonant experience." They say they're *having fun*. But "having fun" is rooted in "play," for which my favorite description is "intense, optimistic engagement with the world around us."

It turns out that you can design "play" along something called an *engagement curve*, which basically means that (as a game designer) you present challenges to people in roughly the order they're equipped to handle them. In the moments where the challenges we face match up almost exactly with our ability to overcome them, we can be said to be in *flow*.

![](https://media.wizards.com/legacy/mtg/images/daily/ld/ld184_mih.jpg)The flow experience is one of the most universally euphoric experiences human beings enjoy. The psychologist [Mihaly Csikszentmihalyi](http://en.wikipedia.org/wiki/Mihaly_Csikszentmihalyi) defines it as "the satisfying, exhilarating feeling of creative accomplishment and heightened functioning." In fact, he dedicated almost a decade of his life to researching flow. Where can we find it? Why do we enjoy it so much? And what are the secrets to getting more of it?

Csikszentmihalyi found that central to the flow experience were three factors: clear goals, rigidly defined rules of engagement, and the potential for measured improvement in the context of those goals and rules.

![](https://media.wizards.com/legacy/mtg/images/daily/ld/ld184_hive.jpg)[Hive Mind](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hive+Mind)| Art by [Steve Argyle](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Steve+Argyle%22%5D)

Why does that work?

Inside that environment, we feel powerful?we feel capacitized as people. This is what we mean when we say we're in the zone. Quickly, we're able to overcome our weaknesses and learn from our mistakes, and we reap the rewards of that learning by triumphing over obstacles. Given that our ability to learn rapidly is one of our defining traits as a species?indeed, it might be the attribute most responsible for our ability to dominate the planet?it makes sense that the psychological reward for intensely rapid learning is so pronounced.

Pump the Fist
If flow represents the height of the human capacity to learn?and therefore to triumph?*fiero* is the payoff that happens once we do that.

According to [Dr. McGonigal](http://en.wikipedia.org/wiki/Jane_McGonigal), *fiero* is "possibly the most primal rush we can experience." It's the feeling we get when we conquer an obstacle that, for whatever reason, is emotionally important to us. It's the weird and surreal force that leads to touchdown dances, fist-pumps, and the compulsion to scream "GOOOOOOOOOOOOAAAAAAAAAAAAAAAAAAAAAAAALLLLLLLLLLLLLLLLLL" when someone scores in a Premier League football match.

The harder the challenge, the more severe the payoff. We love, after all, to confirm our own narratives of exceptionalism. But the obstacles we overcome must feel genuine. If I've just taught someone **Magic**, something is wrong with me if I just relish the opportunity to bash in that player's face by playing every match like it's the finals of the Pro Tour. On the other hand, a masterfully sculpted game like the recent [Kibler-Finkel semifinals](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/ptdka12/sf_2) feels like a well-choreographed dance, and the moments where we win such games feel viscerally like they mean something. The root of that meaning is the fiero impulse, which inspires optimism by evincing mastery?and mastery helps us feel capable of meeting the most intense challenges of our lives.

![](https://media.wizards.com/legacy/mtg/images/daily/ld/ld184_master.jpg)[Presence of the Master](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Presence+of+the+Master)| Art by [Ciruelo](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Ciruelo%22%5D)

When something pushes us to our limits, but we rise to face it, that victory feels fundamentally and inherently substantial. It's a powerful motivator; indeed, researchers at Stanford's Center for Interdisciplinary Brain Sciences have hypothesized that it's why we ventured forth from the safe huddles of our caves to go out and conquer the world!

Emotion Engines
Flow and *fiero*, then, are two emotional responses that games are extremely good at creating. But how does **Magic** engage them?

Let's take them one at a time.

As mentioned before, flow depends upon three things: goals, rules, and improvement. The more straightforward and clearly defined each of these are, the more conducive to flow the overall experience becomes. Moreover?due to the engagement curve we talked about earlier?each of these variables needs to be robust; that is, as your investment into the game deepens, the challenges put forth to you should rise correspondingly in proportion to your burgeoning understanding.

In terms of goals, then, it's clear that **Magic** succeeds. At its most basic level, you need to accomplish one thing: reduce the opponent's life total from 20 to 0. That's it. Now, the game provides you an endless potential of ways you can do that, but the goal remains very clear. Eventually, as you play more and more, your goals evolve. You learn you can run opponents out of cards or poison them ten times. You learn about card advantage, and how it's a goal in and of itself, and you start to keep a count of who is up by how many cards at any given time. You learn about the mana curve, and develop yet another goal of deploying a threat on every turn of the game. The goals emerge in proportion to the extent of your understanding of the game.

![](https://media.wizards.com/legacy/mtg/images/daily/ld/ld184_inc.jpg)[Increasing Ambition](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Increasing+Ambition)| Art by [Volkan Baga](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Volkan+Baga%22%5D)

You'll see a similar pattern in the rigidity of **Magic's** rules. Like many popular, dynamic games, **Magic's** rules are very complicated. But embedded into that complexity is a kind of confidence: there is *always* a correct answer to any interaction, however bizarre. So you're always aware of the system inside which you operate, what you can and cannot do. That's vital to create flow. In real life, we're not always confident about how we can act to affect our environment, and that makes us feel lost and helpless. In a system of clearly defined rules of interaction, we feel capacitized and imbued with agency. Again, as you grow to understand **Magic** more, your understanding of its "rules" moves beyond the set of legal game actions. Systems like the color pie become more and more important?you learn the limits of a strategy or color combination, and you learn to test those limits. You develop heuristics about when to attack and when to block, loose sets of "rules" that you learn to bend and modify when situations change. That learning experience, again, is powerful. It helps us feel like we're always moving forward.

That last example alludes, finally, to the need to improve. Yet again, on a very basic level, the initial complexity of **Magic** means that in the beginning almost every situation that arises improves some understanding you have of the game. "Oh, that's what an instant does." "Oh, that's why flying is powerful." Deck building contributes very powerfully to this sense. "Wow, this [Walking Corpse](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse) is a lot better than this [Mindless Null](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindless+Null)." "Wow, this [Doom Blade](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade) is awesome?I should definitely play four copies of it in my deck." As you improve in skill, your enhanced understanding is met with new opportunities to maximize value. "I should trade 3 damage for 4 damage here because my creature has evasion, and it's far more likely that I'll draw a chump-blocker or removal spell that can interact with my opponent's creature than it is she'll draw one to interact with mine." "I should play a single copy of [Revoke Existence](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Revoke+Existence) because my Delver/Snapcaster deck looks at a lot of cards, and the marginal value of having access to an effect is huge relative to the real-estate it occupies in the decklist." And even more arcane sentences than that! It spirals deeper as you dive into the rabbit-hole.

*Fiero* moments are harder to quantify. McGonigal describes it as "a craving for challenges we can overcome, battles we can win, and dangers we can vanquish." Obviously, every time an opponent summons a [Craw Wurm](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Craw+Wurm), it's a little mini-quest to embark upon. And the entire framework of a game of **Magic** is constructed as an embedded series of battles, strings of small victories that culminate in a conquest.

![](https://media.wizards.com/legacy/mtg/images/daily/ld/ld184_pledge.jpg)[Conqueror's Pledge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conqueror%27s+Pledge) Art by [Kev Walker](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Kev+Walker%22%5D)

Really, though, I feel like the *fiero* impulse is rooted in the same reason that so many **Magic** players fall into the "Timmy" category. It's not just about challenges, battles, and conquests, after all?it's about meaningful *challenges*, battles, and conquests. *Fiero*, to me, is driven by the desire to participate in something epic, something imbued with narrative significance. And **Magic** might be the best vehicle to regularly experience narrative events on the planet. Every time I meet players, I'm overwhelmed by epic story after epic story, all brought upon through their game experiences. The crazy combos. The all-out attacks. The 50,000 Saprolings and the 216,000/216,000 [Chameleon Colossus](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chameleon+Colossus). Every [Rite of Replication](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rite+of+Replication) ever cast and kicked. It all comes together in a kind of victorious symphony, a testament to superlative experiences. Everyone has their *fiero* story?oftentimes entire collections of them. Few other experiences produce so many, so quickly, so regularly. They're epic, they're genuine, and they're real.

A lot of non-gamers approach games with a kind of confusion, a deep perplexity as to why so many people would spend so much time on experiences that are so totally artificial and so totally constructed. That's a natural response. As I've spent more and more time working on games, though, I've realized that they're popular precisely because they address real human needs. They evoke real human emotions in ways other art forms address, but occasionally cannot touch. Flow and fiero are two of the most straightforward of those.

Zac Hill,[@zdch](https://twitter.com/#!/zdch)



---

  
![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_location_static.png)![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_go_active.png)![](https://media.wizards.com/legacy//mtg/images/daily/features/en_storelocatorbutton_go_static.png)![](https://web.archive.org/web/20121110024559id_/http://www.wizards.com/mtg/images/daily/features/banners/DKA_ArticleFooterBanner_FNM_Top.jpg)[![](https://web.archive.org/web/20121110024554id_/http://www.wizards.com/mtg/images/daily/features/banners/DKA_ArticleFooterBanner_FNM_Button01_Static.jpg)](http://staging.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/darkascension/productinfo)[![](https://web.archive.org/web/20121110024606id_/http://www.wizards.com/mtg/images/daily/features/banners/DKA_ArticleFooterBanner_FNM_Button02_Static.jpg)](http://gatherer.wizards.com/Pages/Search/Default.aspx?sort=color+amp;output=spoileramp;method=visualamp;action=advancedamp;set=%20%5B%22Dark+Ascension%22%5D)






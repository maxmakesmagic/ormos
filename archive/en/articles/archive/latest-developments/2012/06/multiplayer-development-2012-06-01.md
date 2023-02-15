
---
[Link to Wayback Machine](https://web.archive.org/web/20200809211301/https://magic.wizards.com/en/articles/archive/latest-developments/multiplayer-development-2012-06-01)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "Last week, I talked a little bit about Planechase, how and why we designed it, and how and why we make new cards for it. Today, I want to take a step back and talk about how we develop multiplayer products generally. What's different about multiplayer from two-player Magic? Is it a fundamentally different experience, or a subset of the same overall game? What kinds of cards prove to be successful multiplayer designs, and what usually doesn't tend to work out as well?"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "645091"
[_metadata_:publish_date]:- "2012-06-01"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Multiplayer Development"
[_metadata_:wayback_capture_timestamp]:- "2020-08-09 21:13:01"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200809211301id_/https://magic.wizards.com/en/articles/archive/latest-developments/multiplayer-development-2012-06-01"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/multiplayer-development-2012-06-01"
---


Multiplayer Development
=======================



 Posted in **Latest Developments**
 on June 1, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 






Last week, I talked a little bit about *Planechase,* how and why we designed it, and how and why we make new cards for it. Today, I want to take a step back and talk about how we develop multiplayer products generally. What's different about multiplayer from two-player **Magic?** Is it a fundamentally different experience, or a subset of the same overall game? What kinds of cards prove to be successful multiplayer designs, and what usually *doesn't* tend to work out as well?

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld197_kil.jpg)[Kilnspire District](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kilnspire+District) | Art by [John Avon](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22John+Avon%22%5D)

I can tell right now this is going to be a more theory-crafting type of article—which makes sense, as every lead developer needs to have an understanding of these principles, because every set has cards that are tailored for multiplayer games. So much of the artistry involved in making **Magic** requires the lead developer to wield finesse, to create cards that every kind of player can enjoy. We don't have a quota—you know, "aiight, Dave, we're running low on rolls at the Emperor Two-Headed-Giant Grab Bag crowd, so make sure we give them at least three surefire hits this time around," or whatever. What we have to try and do is understand the different needs of different types of players. And the way to do that is to break down how the games themselves are played. From there, we as developers can figure out how to build tools for those environments.

Note, of course, that my examples are going to be *way* oversimplified. The way these kinds of exercises work is that you have to figure out what the level-one incentives are, not stuff like "Well, my [Geist of Saint Traft](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft) dodges the 'committing a threat is bad' heuristic because it comes out early and is hard to answer with value," or whatever. The reason all, or even most, games probably don't play out exactly like the hypothetical situations we're going to describe is that play-groups advance past the baseline, and **Magic** offers a lot of tools to people who understand its inner-workings. But when we're developing sets, we're making those tools. And they have to take into account the way the world works before they come into being. So if I say something like, "When I press a picture frame up against the wall, it falls to the ground," I'm not saying "...because I haven't figured out how to hammer a nail into that wall." I'm saying, "This is how the world works without nails—and this is how we build nails for people to hammer."

Thank you for putting up with that analogy, which I haven't found to be totally ridiculous yet but probably will by the time this article goes live on Friday.

### Inertia Creeps

The most fundamental difference between a two-player game of **Magic** and a multiplayer game is that, in a duel, everything is zero-sum. What's good for you is bad for your opponent. When you kill one of your opponent's creatures, you're getting that much farther ahead yourself. Answers to threats tend to be quick and efficient, since usually you want to deal with a problematic card at minimum expense to yourself. The less disruptive to your own overall strategy that answer is, the quicker you can set about executing your own game plan again.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld197_doo.jpg)[Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade) | Art by [Chippy](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22FIRST+LAST%22%5D)

Multiplayer games don't work this way. If you play a [Centaur Courser](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Centaur+Courser) in a duel and I [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade) it, we're both down a card and I've saved a single mana. In aggregate, that tends to be good for me. In a five-player game, though, if the same exact situation occurs it's *really* bad for me. You and I are both down a card, which puts us behind the three other players. Moreover, I've now committed my removal spell to a threat that wasn't necessarily even affecting me. In this game, from my perspective, my removal needs to do *four times* the work it does in a duel, because there are four times the number of threats. Aah! Scary! Now, the reality is that the game in total (all things being equal) has a comparable number of threats relative to answers, but the game's other players aren't looking out for my interests. They're looking out for Numero Uno.

![247322](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=247322)  
When that [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade) is in my hand, it's capable of answering anything that comes my way. That makes me kind of want to sit back and hold it until somebody, you know, looks at me the wrong way or whatever. Or sends a giant baddie into the red zone at my face. The second I commit, I'm (a) behind the other players and (b) very vulnerable suddenly.

What this tends to mean is that it's very costly in a multiplayer game to *do anything*. Usually you're okay if you start generating raw resource advantage, which is why so many decks tend to focus around drawing cards, ramping mana, and casting high-impact creatures and spells. But committing to the board? Bah. I don't really want to be the person answering a threat—I want someone else to answer it. Similarly, even though in a duel the advantage tends to be in the hands of the attacker (who has access usually to more available mana and more available cards, despite the rules of the game favoring the defender), in a multiplayer game attacking carries a very high cost. Just like the [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade) in your hand can answer *any* threat that comes your way—well, as long as that threat isn't black—your untapped creatures serve as deterrents to the entire table. Now, opponents can just use one of their [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade)s on your blocker, of course, but they put themselves into the very situation we've just been talking about.

So there are huge incentives for the entire table to just keep it real and not do a whole lot until everyone starts to launch nuclear weapons at one another. This effect is magnified in formats like Commander where you have six zillion life to begin with and basically always have access to (at least) one card. But it's not *exclusive* to Commander by any means. On the other hand, formats like Two-Headed Giant and *Archenemy* actually *are* zero-sum, only with much bigger systems to take into account. So a lot of what I've been talking about doesn't apply as much there.

### Okay. So?

**Magic** players, being human beings and all, respond to incentives. So what does the world I just described look like in practice, and how does that affect the play pattern?

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld197_day.jpg)[Day of Judgment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment) | Art by [Vincent Proce](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Vincent+Proce%22%5D)

The first thing is that mass removal is *really* good in multiplayer. ***Really***good. Remember all that stuff I said about zero-sum, not doing anything, raw resource advantage, etc? A card like [Day of Judgment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment) gets around all of that. Not only does it allow you to spend your first few turns generating advantage, it allows you to remove problematic threats without shooting yourself in the foot relative to the rest of the table.

![Day of Judgment](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Day+of+Judgment)  
What that means is that your everyday level-one aggro deck is really bad, too. Because it's so powerful for everybody to be packing sweepers, it's just incredibly likely that someone is going to have one in the early turns. But because you've had to commit a threat to the board every turn of the game, you get *even more* punished by the sweeper effect than the rest of the table. Furthermore, even if you somehow miraculously manage to have all your threats survive, you have the other problem of needing to kill four other opponents. In a duel, aggressive decks cede late-game topdecks for early-game advantage. But the way they usually win is that they play a fast enough curve to threaten the opponent's life total, then play a couple of removal or disruption spells to deal with a single threat or two from the slower deck. What that entails for multiplayer is that while you might be able to deal with one player's defenses, it's just very unlikely that you beat the table's.

Now, what you might expect to happen is that players don't need to deal with aggro decks' defenses in the early game, so they play fewer and fewer sweeper effects. Therefore, it ought to be possible to catch people off guard with an aggro deck and get 'em where it hurts. The problem is that every deck, sooner or later, is still going to have to play a suite of answers to threats. If everybody is playing aggro decks, [Day of Judgment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment) is good for all the reasons we've described. If everybody's going Big Poppa, though, [Day of Judgment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Day+of+Judgment) is *still* good because it answers six-mana threats for four mana—and usually has "draw two or so cards" tacked on to it because of the incidental value you get out of the rest of the table.

The net result of all of this is that it really pays off to accumulate raw resources, and either cast *über*-high-impact threats, or assemble some kind of combo that finishes off a lot of opponents at once.

### Don't Just Stand There. Do Something!

So what does all this mean for us?

The first takeaway is that if you want to make aggressive cards good, you have to recoup all the disadvantages that come with committing a ton of threats to the board. One way to do that is to print, you know, [Living Death](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Living+Death), so that you just get all your guys back while dealing with your opponents' first wave of boom-booms. That's the kind of card that only comes along so often, though, obviously. So we love doing stuff like [Edric, Spymaster of Trest](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Edric%2C+Spymaster+of+Trest) that can recoup a lot of the disadvantage you eat in the early game by flooding the board, or cards like [Scavenging Ooze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scavenging+Ooze) that are very powerful at any stage, or [Shardless Agent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shardless+Agent) (which I previewed last week) that can create armies by themselves. Put together two creatures and an Equipment and suddenly you can end games quickly without just eating it to a sweeper effect.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld197_cul.jpg)[Cultivate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cultivate) | Art by [Anthony Palumbo](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Anthony+Palumbo%22%5D)

A lot of the time, though, you don't fight inertia. The fact is, most multiplayer formats revolve around big spells and big effects, and a lot of players play those formats precisely *because* they enjoy those effects. So it's our job to make sure y'all keep getting new toys! These can come in the form of multiplayer-directed products like *Commander* and *Planechase*, or through expansion sets with cycles like the Praetors, *Avacyn Restored*'s legendary Angels, and (yes) the Titans. As well as a *lot* of stuff in the pipeline you'll be seeing more of later this year. We can also gear up ramp and advantage in a way that isn't destructive in Standard, but is exactly the kind of thing people like to do in multiplayer. A classic example of this was our putting [Cultivate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cultivate) in ***Magic** 2011*, which we did due to the popularity of [Kodama's Reach](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kodama%27s+Reach). If y'all want to do a thing, we want to make sure you have at least the rudimentary equipment to do it.



|  |  |
| --- | --- |
| Cultivate | Negate |

Finally—we do have to include stop-gaps. **Magic** is a game of interaction. We spend a lot of time talking in our public-facing outlets about how we like creatures, attack phases, big mana, and swingy effects. We say it so much that I know it's frustrating to hear over and over again. But what we mean is that for most of **Magic's** history, it has tended to reward spells, draw steps, efficient incrementation, and marginal advantage. So we have to do a lot of work to balance those tensions out, and that's where we focus most of our effort. But **Magic** would be a bad game if all that went away, and we realize that. It just doesn't require as much *work* on our end to make sure that [Preordain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Preordain) and [Path to Exile](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Path+to+Exile) are good.

I say all of that to reiterate that, yes, an essential component of developing for multiplayer is ensuring that players aren't just sitting there getting hit by shotgun blasts. While the momentum certainly doesn't *favor* a [Doom Blade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Doom+Blade), plenty of players use cards like [Putrefy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrefy), [Mortify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mortify), [Maelstrom Pulse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maelstrom+Pulse), [Dissipate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dissipate), [Hinder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hinder), and [Condemn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Condemn) to make sure they can deal with problems in a pinch. Versatility is at a premium in multiplayer, because you can't be a surgical as you can be in a duel. I love a card like [Negate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Negate) for precisely that reason—it doesn't stop everything, but it stops (say) the combo you're most scared of facing. And, when possible, we've begun to move a lot of "target opponent" effects to "each opponent" to eliminate some of the asymmetry inherent in a lot of offensively-minded cards. This also has the important side effect of saving clicks in **Magic Online—**which, as online play expands, has become much more of a concern for us.

### Parappa the Wrapper-Upper

So yeah. What I've realized is that thinking about how multiplayer tends to work is kind of a microcosm for **Magic** development, generally speaking. We think about what the pressures exerted on a format are, and we think about how to work around them. I know this content was kind of dense, but I hope it's given you a better understanding into our process, the outcomes, and how we hope to send some love in the direction of multiplayer aficionados everywhere.

Of course, we don't know everything. What else would you like to see? What do you wish we did more of? What do you think we do *too* much of, multiplayer-wise? Let me know, aiight?

Thanks, y'all.

Zac ([@zdch](https://twitter.com/#!/zdch))








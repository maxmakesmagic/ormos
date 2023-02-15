
---
[Link to Wayback Machine](https://web.archive.org/web/20160729033950/http://magic.wizards.com/en/articles/archive/latest-developments/blurring-edges-mana-cost-2012-03-16)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "Here on DailyMTG.com, we often talk about different elements of design, development, and creative as though they exist in their own particular `camps.` The format of our columns contributes to this, of course."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "644826"
[_metadata_:publish_date]:- "2012-03-16"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Blurring the Edges: Mana Cost"
[_metadata_:wayback_capture_timestamp]:- "2016-07-29 03:39:50"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160729033950id_/http://magic.wizards.com/en/articles/archive/latest-developments/blurring-edges-mana-cost-2012-03-16"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/blurring-edges-mana-cost-2012-03-16"
---


Blurring the Edges: Mana Cost
=============================



 Posted in **Latest Developments**
 on March 16, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 






Here on **DailyMTG.com**, we often talk about different elements of design, development, and creative as though they exist in their own particular "camps." The format of our columns contributes to this, of course. We talk about design in [Making Magic](http://www.wizards.com/Magic/Magazine/Archive.aspx?tag=Making%20Magic&description=Making%20Magic), about development in [Latest Developments](http://www.wizards.com/Magic/Magazine/Archive.aspx?tag=Latest%20Developments&description=Latest%20Developments), and about creative in [Savor the Flavor](http://www.wizards.com/Magic/Magazine/Archive.aspx?tag=SavortheFlavor&description=Taste%20the%20Magic), so the issues we present naturally seem to kind of be part of our respective domains.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld186_three.jpg)[Three Dreams](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Three+Dreams) | Art by [Shishizaru](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Shishizaru%22%5D)

In truth, however, the processes aren't always as distinct. Design thinks about how mechanics will play in Limited and about what their cards represent inside the game world. Development thinks up totally new cards from scratch and matches later-stage revisions to pieces of art that already exist. And creative gets to assign creature types—especially relevant to game play in tribal sets—while also enjoying the final say on power and toughness (we don't want any 2/1 Giants, after all—unless we're in [Segovia](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Segovian+Leviathan)!).

These points of intersection are interesting to me. They play out on an individual level, too. When we talk about one of (newest R&D hire—yay!) Shawn Main's über-fun mechanics or one of [Erik Lauer](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Erik%20Lauer)'s awesome dragons or one of [Richard Whitters](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Richard%20Whitters)'s super-sweet pieces of concept art, a lot more people are usually involved than just the stars of the show. That's one of the cool parts of working in R&D—it's an intensely collaborative environment. But we don't get to dissect those minutiae on our website all the time—which makes sense, as that would be confusing and would take forever. So, from time to time, I want to spend a column exploring one of those topics that, at first glance, falls squarely under the umbrella of a single department. There might just be a rabbit hole to dive down...

### Expense Reporting

Today, the issue I want to tackle is mana cost.

*Clearly* a development issue, right? 

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld186_count.jpg)[Counterbalance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterbalance) | Art by [John Zeleznik](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22John+Zeleznik%22%5D)

After all, a huge part of the reason development even exists is to balance cards, and one of the most important balance-knobs in the game is how much a card costs. Moreover, beyond mere issues of balance, cost is one of the central determinants of the game-play experience. The more expensive cards naturally come up later in the game, which allows you to design a narrative whereby certain bigger effects only come up after an initial period of early-game positioning. You could very easily *balance*, for example, a huge number of one-and-two-mana Werewolves, but the gimmick is way less cool when you have to take into account the reality that a lot of decks don't ever intend to cast spells on the first turn of the game. So the tool of mana cost, it seems, sits squarely in development's camp.

That's *mostly* true.

It turns out, though, that the relationship between cost and effect isn't simply a one-way street. That is, there doesn't exist some list descended from the heavens that details how much, in a perfect world, a certain effect "should" cost. There is frequently a gradient, an array of choices, that would work without unbalancing the game, and it's a design choice to think about where you want the card to fall in that array. Moreover, designers don't create cards as much as they do create *files—*since, after all, the exact composition of a set is left to the developers, but its overall tone, feel, and mechanical definition are up to design. As such, a good design file should contain a diversity of play styles and effects—and they can only be diverse if they suitably match up to a wide variety of costs.

### The Whole Shebang

![](https://media.magic.wizards.com/image_legacy_migration/mtg/images/daily/ld/ld186_card.jpg)  
...what?

That card makes no sense. Even assuming it has some kind of sensible creative treatment, that card makes no sense. Nothing about it is legendary! White gets 1W 2/2 creatures all the time—often with upside! So why give this utterly mundane card the legendary drawback (and assume the burden of an involved creative treatment) when it communicates nothing whatsoever? It's change for change's sake, which is usually a hallmark of bad design—and let's not get started on the amateur flavor text!

Contrast that, however, to the following card:

![Isamaru, Hound of Konda](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Isamaru%2C+Hound+of+Konda)  
Ignoring obvious superiority of kitties to—ahem—*hounds*, this [Isamaru](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Isamaru) guy is a far superior design. It's coherent, and it's coherent entirely because of the mana cost. No color in **Magic** gets C 2/2 creatures, full stop, no drawback. So the fact that you're getting away with something, the fact that you're cued into some kind of real abnormality, a "limited time offer; act now!" type of situation—all of that renders the legendary supertype sensible on this card. Yet superficially, independent of cost, it's the exact same "design" as the first one.

What's the difference?

The key is that when you design a **Magic** card, you're really designing a play pattern. You're not simply writing rules text on a piece of paper. [Essence Drain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Drain) and [Lightning Helix](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Helix) are not the same design. [Elite Vanguard](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elite+Vanguard) and [Coral Eel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coral+Eel) are not the same design. [Ancestral Recall](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancestral+Recall) and [Concentrate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Concentrate) are *certainly* not the same design. A lot of new designers make this mistake—they create a bunch of effects and assume someone will cost them correctly later. But to approach it from this angle ignores the power of cost in sculpting the game-play experience.

This is one of the reasons—and I realize this statement is controversial—that I'm glad we made [Baneslayer Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baneslayer+Angel) 3WW. It's a card a lot of people love and a lot of people hate, but by pushing it to the level we did, we made the statement that we were okay with tournament **Magic** being about this kind of effect. It's designed to be played in a certain kind of environment. It's a statement of implicit sanction. It says, "We want people to do this." At (say) 5WW, it does none of those things. It's not [Baneslayer Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Baneslayer+Angel). It's not the same design. It doesn't inspire passion, one way or another. It doesn't inspire *anything.* It's just another woman with wings.

### Independent Misses

What I've hoped I've managed to convey is that cost and effect are not independent variables. This has profound implications for a design file.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld186_prim.jpg)[Primeval Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primeval+Titan) | Art by [Aleksi Bricolt](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Aleksi+Bricolt%22%5D)

One of the strengths designers have is their ability to create totally awesome **Magic** cards. As a developer, I like to think I have a sweet one up my sleeve once in awhile, but if you're having a Commander-card-design battle to the death, I promise that you want Nagle on your side and not me. What this means is that, generally, **Magic** sets are better if you have designers creating sweet rares.

Imagine, though, that the following cards (having never been printed before) are in some hypothetical green design file rare-slots:


> 
> [Terastodon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terastodon)  
> [Woodfall Primus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woodfall+Primus)  
> [Tooth and Nail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tooth+and+Nail)  
> [Primeval Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primeval+Titan)  
> [Vorinclex, Voice of Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vorinclex%2C+Voice+of+Hunger)  
> [Gaea's Revenge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaea%27s+Revenge)  
> [Mana Reflection](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Reflection)  
> [Genesis Wave](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Genesis+Wave)  
> [Asceticism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Asceticism)  
> [Primal Command](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Command)  
> [Epic Proportions](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Epic+Proportions)
> 
> 
> 

Now, I happen to be a huge fan of all these cards. Moreover, in our little hypothetical universe, their mana costs can change because the file hasn't even entered development yet. So what's wrong with putting all of them in the same file?

The problem is that certain effects are suitable for certain mana costs. I cannot print a three-mana [Tooth and Nail](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tooth+and+Nail). But in order to function in Limited, as well as to provide enough appeal for a broad enough array of players, you have to diversify the mana costs of your commons, uncommons, rares, and mythic rares. The fourth 4GGG card you see has diminishing returns, even if it's totally awesome, and would better serve a later set. With a handoff like the one above, even though all of the cards are super-sweet, I have to set like half of them on fire and start over. There's just no way to realistically cost enough of them below five mana. This winds up making the set worse, because then I as a developer have to start designing a bunch of cards late in the game and have less time to work on them.

Because of this, a good designer has to have a ballpark estimate of what certain effects cost. That way, the designer can populate the file with a broad array of effects that occupy each point on the mana curve. Correspondingly, a good developer has to have an eye for a file that might prove problematic in this regard down the line, and kick those cards back to design in time to elicit cool submissions. It's very much a back-and-forth.

### You Gotta Keep 'Em Separated

We've separated design and development in **Magic** R&D for a reason: specific people have specific sets of skills. But I was surprised, when I got here, at the extent to which those skillsets overlapped and, in many cases, depended upon one another. The ability to cost cards appropriately is just one example of a "development skill" that proves vital in an entirely different department. That's one of many reasons why we put creative people on design teams and designers on development teams *et cetera*. At the end of the day, we all have to be capable of doing just a little bit of everything.

Zac  [(@zdch)](https://twitter.com/#!/zdch)

  







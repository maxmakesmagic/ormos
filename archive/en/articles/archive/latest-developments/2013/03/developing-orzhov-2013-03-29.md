
---
[Link to Wayback Machine](https://web.archive.org/web/20170321192943/http://magic.wizards.com/en/articles/archive/latest-developments/developing-orzhov-2013-03-29)

[_metadata_:author]:- "Billy Moreno"
[_metadata_:description]:- "&#13;"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "645801"
[_metadata_:publish_date]:- "2013-03-29"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Orzhov"
[_metadata_:wayback_capture_timestamp]:- "2017-03-21 19:29:43"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170321192943id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-orzhov-2013-03-29"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/developing-orzhov-2013-03-29"
---


Developing Orzhov
=================



 Posted in **Latest Developments**
 on March 29, 2013 






![](http://magic.wizards.com/sites/mtg/files/styles/auth_small/public/images/person/authorpic_BillyMoreno.jpg?itok=a1IiPCGz)
By Billy Moreno












Today's article marks the end of Latest Development's exploration of the *Gatecrash* guilds, and we're wrapping up this exercise in the only way that really makes sense, by paying all due respects to the Orzhov guild and its patriarch, [Obzedat, Ghost Council](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Obzedat%2C+Ghost+Council). If there is a real pecking order among the guilds, then the Azorius Senate and Boros Legion, as the architects of the law and its martial enforcers, respectively, have meaningful and legitimate claims to the top spot. The Orzhov Syndicate scoffs at legitimacy—power belongs to those who possess it. While every merchant enjoys the protection of the syndicate enforcers, while every citizen pays blind obedience (and tithes actual money) to the syndics at the church of deals, and while its army of lawyers profitably mediate nearly every contract dispute, you'd be hard-pressed convincing the citizens of Ravnica that any other guild held nearly the same sway over their daily lives.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld240_ghostcouncil.jpg)It might seem surprising that a guild led by a practically immortal ghost council made up of retired paragons would take such a strong (and strong-arming) interest in the day-to-day mundane. But the guild's profiteering banality is actually a direct result of its focus on the interminable, inevitable long game. Owing to impatient brilliance or frustrating marginalization, guilds like the Izzet League or the Gruul Clans are prone to fixating on the next big score. For the Orzhov, on the other hand, over a thousand centuries and through one thousand lashes, the pursuit of guild supremacy centers on a relatively straightforward game plan—it's all about the grind.


### "What's a little extortion among friends?"


[Earlier this week](http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/240), [Mark Rosewater](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Rosewater) discussed why extort is an ideal expression of Orzhov philosophy, and while we took a few swings to get there, the relationship is so neat and tight in hindsight that I don't really have a lot to add to it. Even though it was the last mechanic in *Gatecrash* to be pinned down, extort cards were relatively straightforward to develop. By and large, extort commons and uncommons (i.e., the ones that would define the guild's role in Limited) didn't change much once the design team got hold of the mechanic and put it on some cards. Extort works best on cheap creatures that can hit the battlefield before you start casting spells without the keyword. At common and uncommon, there are no extort cards that cost more than five mana and only two cost that much.




|  |  |
| --- | --- |
| 
Vizkopa Confessor
 | 
Thrull Parasite
 |

Mark briefly touched on how extort plays differently depending on whether it's paired up with Boros or Dimir cards, and I'd like to explore that thought some more, because it touches on two strategies the development teams applied while working on both *Return to Ravnica* and *Gatecrash*.


In the typical **Magic** set, the development team works to make sure there is coherent strategy for each of the ten color pairs, as well as a few "weird" Limited archetypes that revolve around specific card groupings. While we often refer to the natural congruity of allied pairs (white-blue, blue-black, black-red, red-green, and green-white) and the unnatural incongruity of enemy pairs (white-black, black-green, green-blue, blue-red, and red-white), it is actually just as easy to put Plains and Mountains in a deck together as it is Islands and Swamps, so long as we provide you with cards in each pairing that work well together. If you think back on your time playing ***Magic** 2013* or *Innistrad* Limited, there's a good chance you played all of the possible combinations roughly the same amount.


*Return to Ravnica* and *Gatecrash* are unique environments in that regard. In each set, we actually want you playing five of the ten color pairs most of the time. When your *Gatecrash* Limited games predominantly feature *Gatecrash* guilds, it goes a long way to reinforcing how important the guilds are and how much they define work and play on Ravnica. But we generally seed all ten color pairs because we've learned that successfully fleshing out that many archetypes leads to deeper and more rewarding drafting experiences. Some simple math led us to our first development strategy.


### Development Strategy #1: Each Guild Should Contain an Aggressive Archetype and a Control Archetype.


By doubling up on the archetypes for each of the five guilds, we hoped to get somewhere close to that magic number of ten. Earlier, I said the math was simple, but I was being optimistic and a little sneaky. Two times five is, in fact, ten. But it turns out, building two Limited archetypes into a single guild is not the easiest task. Since every Orzhov deck is powered by Plains and Swamps, we can't completely stop you from playing "aggressive" cards and "control" cards together. And since each guild should have a cohesive identity that feels right, we didn't want to make the "aggressive" and "control" cards so incompatible that you didn't want to play them together. So while [Syndic of Tithes](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Syndic+of+Tithes) is better at attacking and [Basilica Guards](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Basilica+Guards) is better at blocking, they work perfectly well together. In fact, you could put every Orzhov common and uncommon in a draft deck together and it would make sense; it would have a plan. That's where our second strategy comes in.




|  |  |
| --- | --- |
| 
Syndic of Tithes
 | 
Basilica Guards
 |

### Development Strategy #2: Each Guild Should Interact Well with Its Neighbors.


A guild's neighbors are the two guilds that share a color with it. In *Gatecrash*, Orzhov overlaps the hyper-aggressive Boros on the white side and the controlling Dimir on the black side. The stark difference between Orzhov's neighbors is important. Rosewater brushed on how extort plays opposite roles in Boros and Dimir decks. In the former, the Orzhov mechanic provides added reach with which to finish off a staggered opponent; in the latter, it pads your life total while you tighten the screws of control before ultimately winning the long game. That's all good and well, but Boros and Dimir were always going to be Different Decks (I probably can't trademark that concept but no one can stop me from capitalizing it... in my rough draft at least). What's really interesting is how battalion and cipher contribute to the different Orzhov decks we worked to build into the set.


While piloting a dedicated Boros deck defined by ample amounts of battalion, you will often face defenses that force you to wait for a solid all-in attack. But waiting as your opponent continues to evolve his or her defenses can be costly and nerve-wracking. In an Orzhov deck built around the extort mechanic, waiting can actually be winning. If your curve is filled out with reasonable and/or relentless attackers like [Basilica Screecher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Basilica+Screecher), [Dutiful Thrull](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dutiful+Thrull), [Kingpin's Pet](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kingpin%27s+Pet), [Knight of Obligation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+Obligation), and the aforementioned [Syndic of Tithes](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Syndic+of+Tithes), it's actually pretty easy to maintain pressure while assembling the critical mass of warm bodies needed to turn [Boros Elite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Elite) and [Daring Skyjek](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Daring+Skyjek) into high-octane threats. [Court Street Denizen](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Court+Street+Denizen) is pretty ineffective in a slower Orzhov deck, but when you're rounding out your forty cards with aggressive white battalion creatures, it turns each of them into a blocker-clearing tapper that also happens to drain a life or two from your opponent's dwindling total.




|  |  |
| --- | --- |
| 
Basilica Screecher
 | 
Boros Elite
 |

On the other hand, extorters like [Basilica Guards](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Basilica+Guards), [Syndicate Enforcer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Syndicate+Enforcer)s, and [Vizkopa Confessor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vizkopa+Confessor) tend to be better blockers than attackers. Backed by zone-controlling spells like [Executioner's Swing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Executioner%27s+Swing) and [Purge the Profane](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Purge+the+Profane), you might find your deck is leaning toward late-game domination. Removal like [Killing Glare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Killing+Glare) and [Grisly Spectacle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grisly+Spectacle) will already push your Orzhov deck toward its dark side, but those work equally well at whatever speed your looking to play. [Devour Flesh](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Devour+Flesh) and [Death's Approach](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death%27s+Approach), however, don't work that well in an aggressive Orzhov deck that's looking to continually whittle down the opponent's life total while maintaining battalion-level board presence.




|  |  |
| --- | --- |
| 
Syndicate Enforcer
 | 
Grisly Spectacle
 |

Traditionally, control decks feature a high number of defensive creatures—ones that are good at blocking, not necessarily ones with defender—that can hold the fort and a few evasive ones that can grind out the game while avoiding most interference. All-purpose all-stars like [Basilica Screecher](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Basilica+Screecher) and [Kingpin's Pet](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kingpin%27s+Pet) serve nicely here, especially when encoded by grindy attrition spells like [Midnight Recovery](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Midnight+Recovery) and [Mental Vapors](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mental+Vapors). Not only do these two cipher standouts provide a steady flow of card advantage (aka the lifeblood of control decks), they also repeatedly trigger extort, fending off your defeat with a constant drip of life.




|  |  |
| --- | --- |
| 
Kingpin's Pet
 | 
Mental Vapors
 |

Without our deliberate attempts to build aggressive and controlling Orzhov cards, the differences between Boros- and Dimir-leaning decks would be negligible. And *Gatecrash*'s replay value would suffer for it.


### "I made him an offer he couldn't refuse."


If you haven't watched the [Godfather](http://en.wikipedia.org/wiki/The_Godfather) recently enough (or \*gasp\* ever) for this quote to resonant with you on anything but an overplayed, caricature-of-a-"Bad-Man" level, I can't recommend revisiting it forcefully enough. The timeless excellence of that movie is in the nuance of its titular characters, [Michael and Vito Corleone](http://en.wikipedia.org/wiki/Corleone_family). Nowadays, when I hear someone talk about making a "godfather offer," that person is talking about a pitch that is so appealing it couldn't possibly be turned down. That's missing the whole point. Let me see if I can clear it up for you with some clever punctuation:


"I made him an offer. He couldn't refuse."


See it now? A [real godfather offer](http://en.wikipedia.org/wiki/Throffer) is one backed by immense power and the willingness to use it. Refusing one doesn't depend on the quality of the offer. The godfather defines the deal that works for him and it happens. Because he's the godfather.


As much as I respect the Corleone family, it would be demeaning to compare the Orzhov guild to a mere organized crime syndicate, because for all practical purposes Orzhov is the law in Ravnica. That said, the Orzhov excel at "godfather offers," and they start at the top.


[Obzedat, Ghost Council](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Obzedat%2C+Ghost+Council) would like 2 life now and it'll be back for 2 more tomorrow, if that's all right by you. And of course it is; these deals are non-negotiable.


And doesn't [Merciless Eviction](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merciless+Eviction) always seem to work out in favor of its Orzhov caster?




|  |  |
| --- | --- |
| 
Obzedat, Ghost Council
 | 
Merciless Eviction
 |

Oh, I see you're blocking my minions because you don't want to lose anymore life. [Vizkopa Guildmage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vizkopa+Guildmage) has ways of forcing the issue. Think you can turn the tables by attacking? Let's see how that works out for you.


*Gatecrash* lead developer, [Dave Humpherys](http://www.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humpherys), made cards like these a big part of the Orzhov identity, fighting for Obzedat and Eviction in particular because it is mortally important that all of you understand that when it comes down to it, you will pay up.










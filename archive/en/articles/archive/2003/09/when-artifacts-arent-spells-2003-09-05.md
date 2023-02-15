
---
[Link to Wayback Machine](https://web.archive.org/web/20150721233503/http://magic.wizards.com/en/articles/archive/when-artifacts-arent-spells-2003-09-05)

[_metadata_:description]:- "Mark Rosewater mentioned earlier this week that there are a few new types of cards in Mirrodin. You saw one of them on Tuesday when Paul Barclay introduced you to Equipment and now I get to preview the second: Artifact Land."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "288091"
[_metadata_:publish_date]:- "2003-09-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "When Artifacts Aren't Spells"
[_metadata_:wayback_capture_timestamp]:- "2015-07-21 23:35:03"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150721233503id_/http://magic.wizards.com/en/articles/archive/when-artifacts-arent-spells-2003-09-05"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/when-artifacts-arent-spells-2003-09-05"
---


When Artifacts Aren't Spells
============================



 Posted in [ARTICLES](/en/articles)
 on September 5, 2003 










Mark Rosewater mentioned [earlier this week](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr87) that there are a few new types of cards in *Mirrodin*. You saw one of them on Tuesday when Paul Barclay introduced you to Equipment and now I get to preview the second: Artifact Land.


![Tree of Tales, Ancient Den, Seat of the Synod](https://media.wizards.com/legacy/magic/images/mtgcom/articles/threeartifactlands.jpg)

For such seemingly simple cards, I actually have a remarkable number of almost unconnected stories I want to tell. I’m not sure where else to start so I’ll just start at the beginning.


### The Design


You have to go all the way back to *Tempest* to find a large expansion that does not include a cycle of [common lands](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=19642). Lands aren’t the most exciting aspect of the game, but everyone always has to include a bunch of them in every deck they build, so we like to give players options. In addition, for each of the last several blocks we’ve been able to find ways for the [common lands](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=19642) to fit into the [theme of the set](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=31762), and we’ve been pleased with the way those [land cycles](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=23237) have been relevant to Limited play in addition to [Constructed](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=41140).


Anyway, way back when *Mirrodin* was still called “Bacon,” the design team knew they wanted a cycle of lands at common, but they weren’t sure what to do. Their theme – artifacts – was already set, so they kept trying to come up with lands that interacted with artifacts somehow. For a while they had lands with activated abilities of each color, like “1W, T: Regenerate target artifact” but that had a couple of problems. First of all, we require all of our lands to tap for mana (otherwise, why are they lands instead of artifacts or enchantments?), but then if you add on the ability to tap for colored mana these are strictly better than basic lands. So they require a drawback, like coming into play tapped. Well the design team felt we have been making too many lands with this drawback in recent sets so they wanted to avoid using it again, plus they were just generally discontent with the way the cycle was working out.


At some point in this process Mark Rosewater had the brainstorm: Rather than interacting with artifacts, couldn't they just *be* artifacts?! The set was already chock full of cards that rewarded you for having artifacts in play so that might solve the puzzle perfectly. The design team immediately latched onto Mark’s idea and playtesting quickly showed that artifact lands were indeed quite interesting to play with.


![Vault of Whispers](https://media.wizards.com/legacy/magic/images/mtgcom/articles/vaultdewhispers.jpg)


### The Templating


Story number two begins when the development team took control of the set. One of the most important things we try to do is “break” the cards. Usually that refers to the power-level of the card and “breaking” a card consists of building a deck that abuses it in a way that we deem to be degenerate. However, that’s certainly not the only way a card be broken. Sometimes, the development team will point out situations where a card is too confusing, or where it’s not even clear how the card is supposed to work. In the case of the artifact lands, these circumstances kept coming up.


All the design team told us was that “they’re lands, but they also count as artifacts.” At first blush, that sounds like plenty of information, but it’s actually not nearly enough. Can you [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) an artifact land? Well you can’t counter lands, but you can counter artifacts. Do you draw a card from [Vedalken Archmage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vedalken+Archmage) when you play an artifact land? We kind of wanted the answer to be “yes” but much more important than that we wanted the answer to be unambiguous. Does playing an artifact land use the stack? We knew this one probably wouldn’t make a difference very often, but playing an artifact does use the stack while playing a land doesn’t so it was at least another point that required clarification.


The development team definitely liked the way these interacted with the rest of the set, so we wanted to do them, but we were worried for a while that we wouldn’t be able to solve all of these problems. Pretty early on in development, I called a meeting with everyone who works on card wordings to try to figure out if there was a way to do these. The first thing that emerged from those meetings was a very astute analysis of the problem: the rules for playing an artifact contradict the rules for playing a land. Most of the time it’s no problem for a card to be both a land and an artifact. You just merge the rules for being an artifact with the rules for being a land, similar to the way Artifact Creatures merge the rules for artifacts and creature. However, lands get from your hand into play in a way very different from artifacts. Artifacts go on the stack and your opponent has an opportunity to respond to them (including an opportunity to counter them). Artifacts also trigger effects that trigger whenever a spell is played. Lands, on the other hand, do not use the stack, and cannot be countered, and don’t count as spells, and can only be played once per turn.


What we realized was that the key to doing these cards was to clarify which set of rules applied when you played an artifact land. We definitely needed them to use up your land drop for the turn, and we didn’t really want to allow players to [Annul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Annul) their opponents’ artifact lands, so we decided that they should follow the rules for playing lands (and *not* the rules for playing artifacts).


Having decided the functionality we wanted, we still had to figure out how to communicate that functionality unambiguously on the cards. Many different sorts of reminder text were proposed, most of which attempted to list out answers to all of the potentially ambiguous or confusing situations. For quite a while what we had in the file was “CARDNAME follows the rules for playing a land.” It wasn’t very friendly, and we weren’t sure that everyone would understand exactly what that meant so we kept trying to come up with something better.


What we actually wound up with might be the most bizarre reminder text of all time, but I’m actually happy with how it turned out. All we really needed to communicate was that, when you were playing the card, you were supposed to ignore the fact that it’s an artifact and just play it like you would play any other land. “This is not a spell” is a surprisingly simple and friendly way of pointing out exactly what we needed to point out. There’s no problem when the card is in your hand or when the card is in play; the only potential problems come when the card is in between your hand and play. Well, if you just remember that you don’t play it like a spell (because it follows the rules for playing a land instead) then you’ll never go wrong.


Of course, our solution made everyone happy except for [Vedalken Archmage](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mg87). As the lands are not spells, he won't draw you a card when you play one.


### The Names


![Great Furnace](https://media.wizards.com/legacy/magic/images/mtgcom/articles/furnacegrande.jpg)


My third story has to do with the creative concepts that wound up on the cards and it begins long before anyone dreamed up these cards. With each new block, our creative team builds a world for the card set to take place in. They spend a lot of time making sure the world is coherent and consistent. Part of that process includes working out details about both the cosmology and geography of the world. So they invent all these interesting details about what cities are in the world, what the forest is like, where the goblins live, etc. However, in the past these locations wouldn’t usually get cards to represent them. Since these are specific places (as opposed to generic places like “Swamp” or “Lonely Sandbar”) they would most naturally go onto legendary lands, but we just don’t do nearly enough legendary lands to work all these cool locations into the set.


As Brady Dommermuth alluded to in a recent [Ask Wizards answer](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/asksearchablearchive), we’ve decided to change this policy. We’re now going to start depicting specific places on some of our nonbasic lands. The first lands to benefit from this new policy are the artifact lands. Each depicts one of the most important landmarks to the creatures of that color. You can read a lot more about these locations, and also about the plane of Mirrodin in general, if you pick up a copy of the *Mirrodin* “Fat Pack” in a couple of weeks. The Player’s Guide included in that product includes a nice spread on the way this world works. Additionally, Rei Nakazawa has an article on the same subject that will be running here on MagicTheGathering.com next week.


This new policy actually underwent a bit of development when we were working on *Mirrodin*. The names of the artifact lands initially included the specific names of the places in addition to a description, so they were things like “Tel-Jilad, the Tree of Tales” and “Taj-Nar, the First Den.” When we played with stickered-up versions of the cards with those names, they felt wrong. They were too grandiose for common – mostly because they were named using conventions that we only use on legendary permanents. We wound up dropping their proper names and then things felt much better. The proper names are still there, but we moved them into the flavor text.


At first I was nervous about previewing the artifact lands because they obviously depend on other cards before they actually do anything cool. In retrospect, however, I see that Aaron was right – there are lots of stories to tell about these lands. They’re pretty interesting even before you know what else is in the set. Plus this way we also get to tease you guys and let you speculate about all the different ways they might turn out to interact with the rest of the cards.




---


### Last Poll Results:




|  |
| --- |
| **How old are you?** |
| 0-10 | 43 | 0.3% |
| 11-12 | 337 | 2.7% |
| 13-14 | 1639 | 13.2% |
| 15-16 | 2532 | 20.3% |
| 17-18 | 2034 | 16.3% |
| 19-20 | 1397 | 11.2% |
| 20-21 | 907 | 7.3% |
| 22-23 | 703 | 5.6% |
| 24-26 | 1004 | 8.1% |
| 27-29 | 732 | 5.9% |
| 30-35 | 709 | 5.7% |
| 36-40 | 209 | 1.7% |
| 41+ | 199 | 1.6% |
| **Total** | **12445** | **100.0%** |




---

*Randy may be reached at latestdevelopments@wizards.com.*









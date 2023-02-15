
---
[Link to Wayback Machine](https://web.archive.org/web/20141223015307/http://magic.wizards.com/en/articles/archive/making-magic/new-world-order-2011-12-02)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "For those planning to hear me talk about flashback, you're going to have to wait a week. My teaser last week accidentally talked about the next theme week that doesn't happen until seven days from now. That means I have this week free to talk about anything I want. Luckily, Ethan provided me with a topic in his feature article last week when he broached an issue that I've been meaning to talk about for quite some time."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "193526"
[_metadata_:path_date]:- "2011-12-02"
[_metadata_:publish_date]:- "2011-12-01"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "New World Order"
[_metadata_:wayback_capture_timestamp]:- "2014-12-23 01:53:07"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20141223015307id_/http://magic.wizards.com/en/articles/archive/making-magic/new-world-order-2011-12-02"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/new-world-order-2011-12-02"
---


New World Order
===============



 Posted in **Making Magic**
 on December 1, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




Working for Magic R&D since October, 1995, Mark Rosewater is currently the head designer. His hobbies include spending time with his family, talking about Magic on every known medium (including a daily blog and a weekly podcast), and writing about himself in the third person. 





For those planning to hear me talk about flashback, you're going to have to wait a week. My teaser last week accidentally talked about the next theme week that doesn't happen until seven days from now. That means I have this week free to talk about anything I want. Luckily, Ethan provided me with a topic in [his feature article](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/171) last week when he broached an issue that I've been meaning to talk about for quite some time. So as long as I have a free week, let's talk about something R&D has been up to for over three years (and the work leading up to it for three more), a little something we call New World Order.


Today's column will introduce you to a big problem we had to solve, the solution that problem led to, and the realization that our solution not only solved our problem but made the game better overall. There's a lot to cover, so let's get started.


Problem Solving
===============


As our story is all about solving a problem, I believe the best place to begin is with the problem itself. To do this, we need to go back about six years. I often talk about how we track a lot of numbers. Part of running a business is understanding how things are going, and six years ago we had a big problem. One of our most important numbers, the number of people who play *Magic* , was going down. We did a lot of research and discovered the cause: our acquisition was on the decline. In other words, fewer people were learning to play *Magic* . The big question was: Why? What about *Magic* was keeping new players from wanting to play the game?


We studied the problem and found a culprit that I often talk about: complexity creep. Let me show you what I'm talking about.


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm172_graph.jpg)
The green line marks the complexity of the game over time. (Note that this chart is for explanation purposes and does not reflect any actual data.) *Magic* is a trading card game, which means each year we introduce new cards and new mechanics and new concepts and new themes. As we do that, complexity slowly creeps upward as the game keeps adding components.


The red line is the baseline. That represents where a new player approaches the game. The baseline never changes, because a new player is always in the same place, they know nothing. The space between the red line and the green line is what we in R&D call "the barrier to entry." The taller that gap, the harder it is to make the leap from nonplayer to player. This graph does a good job of showing our problem. Complexity creep was increasing our barrier to entry, making it harder and harder for new players to learn how to play. We were failing to get as many new players because the game was getting progressively harder to learn.


R&D understood that this was a giant threat to the game, something that if left unchecked would create an impact for all the players. It was a problem that had to be solved.


A Complex Problem
=================


This whole discovery happened during *Time Spiral* block. We looked around and realized that we were in the middle of making the most complex block we had ever made. There were almost as many named keyword mechanics in *Future Sight*, for example, as had existed in all of *Magic* up to *Future Sight*'s release. *Time Spiral* block, though, was too far along to change, so we focused on the next block, *Lorwyn*.


Our goal with *Lorwyn* was to make the cards more straightforward. We wanted the rules text to be very clear in what the cards did. We spent a lot of time making sure their intent was simple and understandable, but as the block played out we discovered that we hadn't gotten rid of the complexity; we had just moved it to a different area of the game. I'll explain.


What we learned was that there are three types of complexity in a game:


**Comprehension Complexity**


This type of complexity has to do with the players understanding what a card does. Quite bluntly, can the players read the card and know how it works in the game? This might sound silly, but *Magic* has definitely veered hard into this category in its history. For instance, let's take the suspend mechanic from *Time Spiral* block.


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Errant Ephemeron)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Errant Ephemeron)
It's a perfect example of a mechanic that seems easy if you get it but proved to be a major stumbling block for many players. Design pursued this mechanic because "paying time instead of mana" seemed like a cool and grokable idea, but the manipulation required along with the changing of zones and the lengthy and complicated text overwhelmed a lot of people.


This was the type of complexity *Lorwyn* went after.


Note that time has shown us a second facet of comprehension complexity, a subset I call intuitive comprehension. Here's an example:


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scornful Egotist)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scornful Egotist)
[Scornful Egotist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scornful+Egotist), from *Scourge*, isn't confusing in what it says. It's a 1/1 with morph for 7U. The problem is that many players didn't understand the eight-mana cost. For those unfamiliar with *Scourge*, it had a "converted mana cost matters" theme. [Scornful Egotist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scornful+Egotist)'s high converted mana cost was considered a bonus for the card (you got it into play using the morph). Unfortunately, this theme didn't draw as much attention to itself as it could and the card just ended up baffling many players because they couldn't comprehend why the card was doing what it did.


Intuitive comprehension is all about players understanding and accepting what they read. When the words don't make sense because of context, it can be just as confusing as when they don't make sense inherently. I'm not saying we shouldn't make these kinds of cards just stressing that we have to accept that they are more complex than one would realize at first glance.


**Board Complexity**


Here was the problem that reared its head during *Lorwyn* and *Morningtide*. This type of complexity isn't about what cards can do but rather about how they interact with one another while they are on the battlefield. This problem was most noticeable to R&D during the employee Prerelease for *Morningtide*. The casual players were quitting after one or two rounds and we kept watching people who stayed in suffer as they couldn't figure out what they had to do. There was just too much dependent interaction.


Another important lesson about board complexity was that it didn't take very many cards with this style of complexity to cause problems. Just one card, for example, can change the design tree from a few choices to a double-digit number of choices.


*Magic* is a game about interactions. This type of complexity stresses that too much interaction can be just as taxing mentally as cards that take multiple readings to comprehend.


**Strategic Complexity**


This type of complexity is about understanding how best to use your cards. One of the reasons *Magic* has the depth of play it does is because there is a lot of subtlety to how cards can best be used. Are you supposed to play a card as soon as you can or hold it until a more optimal situation arises? When do you sacrifice a resource to gain long-term advantage? Is a certain card optimal in a particular draft strategy? Questions like these are all examples of strategic complexity.


This complexity is all about maximizing a card's usefulness, about understanding [tempo and card advantage](http://www.starcitygames.com/magic/fundamentals/3690_Tempo_And_Card_Advantage.html), about knowing [who's the beatdown](http://www.starcitygames.com/magic/fundamentals/3692_Whos_The_Beatdown.html). This complexity is about understanding the intricacies of the game. It is what separates a pro player from an average Friday Night *Magic* player.


Common Knowledge
================


Sometimes it helps to lay out a problem when you're trying to solve it. Here's what we knew: We had to bring down the level of barrier to entry. It had simply gotten too high. The game was filled with all sorts of complexity, which was pushing it up. On the flip side, though, we had the established players. Much of what was creating the complexity stemmed from things that were important to keep our existing players. *Magic* has to keep adding new elements. Expansions have to have new mechanics and new keywords and new themes and new strategies. How could we possibly make all the parties happy?


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm172_common.jpg)
The solution ended up being a tool that trading card games had always had: rarity. How could we get things into the hands of the experienced players without overwhelming the less experienced players? We simply had to keep it out of common. We knew that beginning players buy fewer boosters. This means that the percentage of relevant cards they own that are common is simply much higher.


"Keep it out of common" is actually incorrect. The theory behind New World Order was this: we have to be very careful about what we put at common. We had to redraw the line for what level of complexity was acceptable. We were allowed some complexity at common, but less than we had used in the past, which meant it was a resource that had to be carefully managed.


To offset the shift of complexity, New World Order allowed higher rarities, especially uncommon, to tick up in complexity. The goal wasn't to remove complexity, but to shift where it was positioned in the game. The idea was that by moving where it sat, we lessened it for the players who needed it lessened and kept it there for the experienced players who wanted it.


Once we thought of complexity as a limited resource at common, it radically changed how we approached making commons. For instance, I often say "If your theme is not at common, it's not your theme." Because the theme by its nature tends to involve complexity (themes tend to require players caring about something you don't normally care about), it meant that we had to allocate a certain portion of our common complexity to supporting the theme.


I will stress again that common is allowed some complexity. The big shift of New World Order is that R&D is much more conscious about where and how it is used. If a common card is complex, it has to have a reason; it has to serve a purpose. And even then, there has to be a limit to how much complexity shows up at common. Each card has to be judged, and then all the common cards have to be judged together.


Another big jump was the realization that not all complexity is the same. Comprehension complexity and board complexity are a problem for beginners. Strategic complexity is not. Why? Because beginners can't see strategic complexity. It requires a certain amount of game knowledge before it's visible. This meant it was exempt from most of the complexity crackdown at common. The trick, though, was finding ways to put strategic complexity at common without also having comprehension and board complexity.


A Whole New World
=================


New World Order required a radically different way of looking at *Magic* expansions, but once R&D shifted our mindset, we found something even more exciting. When we started playing with the New World Order-shifted sets, we discovered that they were more fun. I'm not talking about for beginners; I'm talking about for R&D, a very established group of longtime *Magic* players. Why? Simply put, New World Order brought clarity to the game. (I termed this phrase because I believe strongly that you need language to guide behavior. If you can't talk about something it's hard to think about it. The term helped cement the concept for R&D.)


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm172_time.jpg)
To understand what was going on let's jump away from *Magic* design to design in general. Last year I wrote a two-part article talking about the Ten Principles of Design by a famous industrial designer named Dieter Rams ([Part 1](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/89), [Part 2](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/91)). Principle Number 10 was "Good design is as little design as possible."


The role of a designer is to only use what you absolutely have to. If a creation can exist without something, a good designer will take it away. For game design, this means that you want to only leave in the game what is necessary for the game to function. When we boiled down our commons to their bare essence, what we found was that we had made a cleaner game. Instead of focusing on lots of tiny elements that gave you little incremental advantages, you were able to focus on the key things that mattered.


Another way to think about is this: Simplifying the commons took away a lot of bookkeeping. By bookkeeping, I mean the requirement to pay attention to elements of the game that *could* matter but often don't. In general, bookkeeping is something you want to take out of games. Keeping track of a lot of information is actually an unfun activity, but gamers do it because they are doing their best to win.


I've talked about this before that players will do whatever the game incentivizes them to do whether or not that thing is fun. The goal of a game designer is to make the incentives move the players towards the parts of the game that *are* fun. Tracking lots of information is not what makes *Magic* fun, yet complexity applied to the wrong places can make that the focus. By stripping away the complexity at common, we were able to move the focus back to things like combat and spell casting.


For those that are worried that this is boring, I ask you to simply try the following experiment. Make two decks of just vanilla creatures and common sorceries. (This is very similar to a beginner product we made long ago named *Portal*.) Find a player of a similar skill level to your own and play the decks against each other. What you will find is that these games are actually quite interesting. It's easy to get caught up in all the complexity of *Magic* that you forget how much fun the base of the game is—and not just fun, skillful.


Be aware there still are a staggering amount of decisions in an average *Magic* game. New World Order didn't lessen the overall skill of the game. What it did was shift the focus on the ability to make the right decisions rather than keep track of excessive amounts of data. Chess, for example, doesn't get more skillful if you add in four new piece types and double the size of the board (nor, for that matter, does it get more fun).


*Magic* has had a huge amount of success in the last three years, and R&D believes strongly that New World Order has had a lot to do with it. It helped us refocus what mattered in the game. I also believe New World Order had another great impact. I've explained that Aaron was very influenced by *Alpha* in his creation of **Magic* 2010*, the product that pushed us down our current path of resonance. I believe that New World Order, and the refocusing that came with it, helped bring about the mental shift that brought Aaron back to *Alpha* as an influence.


New World Order has made all sorts of ripples through the game. As another example, I believe our current push toward making more cards Limited playable has come from our exploring ways to bring strategic complexity to common. Creating cards that are useful in one type of deck but poor in another makes commons that are strategically dynamic without being confusing for the newer player (high in strategic complexity, low in comprehension and board complexity).


In many ways, the excitement of New World Order for R&D has been the complete rethinking of how we use our resources, not just at common but throughout the game. Understanding what is complex and how has completely reshaped how we design and develop the game.


All Together Now
================


The real lesson of today's story hits another common theme of this column: the holistic nature of design. R&D set out to solve an acquisition problem and ended up with a way to refresh the essence of the game. Making the game better for one section of the audience led to making it better for all sections.


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm172_allied.jpg)
I encourage feedback on today's article. Write me an [email](mailto:making.magic@hotmail.com), send me a tweet (@[maro254](http://twitter.com/maro254)). Write to me on [Tumblr](http://markrosewater.tumblr.com/) or [Google+](https://plus.google.com/107824009487778543249/posts). Respond in the thread to this column. I'm curious to see what you think about the current state of *Magic* .


Join me next week when I finally get to talk about flashback.


Until then, may you try a little decluttering.








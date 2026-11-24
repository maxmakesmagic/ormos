---
id: wxfdkvh8
kind: article
lang: en
path: /en/articles/feature/2011/10-17-greetings-from-the-future-future
title: Greetings from the Future Future
published: '2011-10-17'
column_slug: feature
column: Feature
authors:
- slug: zac-hill-263da3f4
  name: Zac Hill
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
    lang_detected: en
    capture_id: 633421
    url: https://magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
    captured_at: '2022-10-05 12:02:04+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
    lang_detected: en
    capture_id: 633421
    url: https://magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
    captured_at: '2022-10-05 12:02:04+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
    lang_detected: en
    capture_id: 633421
    url: https://magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
    captured_at: '2022-10-05 12:02:04+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
    lang_detected: en
    capture_id: 633421
    url: https://magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
    captured_at: '2022-10-05 12:02:04+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: wxfdkvh8
  url: https://magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
  page_key: magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
  lang: en
  template: drupal
  captured_at: '2022-10-05 12:02:04+00'
  capture_id: 633421
  wayback_url: https://web.archive.org/web/20221005120204id_/https://magic.wizards.com/en/articles/archive/feature/greetings-future-future-2011-10-17
- document_id: wxfdkvh8
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/165
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/165
  lang: en
  template: aspx
  captured_at: '2013-09-27 01:29:08+00'
  capture_id: 584496
  wayback_url: https://web.archive.org/web/20130927012908id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/165
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: wxfdkvh8
  capture_id: 584496
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/165
  wayback_url: https://web.archive.org/web/20130927012908id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/165
  captured_at: '2013-09-27 01:29:08+00'
  template: aspx
  sha256: ed4cdfbc5c10c3f14bb71d7d94e1e18e3149fc6d68f14cdbae99b3da8f87aec2
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Null Rod
  - Steel Overseer
  - Ancient Grudge
  - Stony Silence
  occurrences: 7
---
Today I want to talk about the Future Future League. Which is different from the Future League. Which doesn't exist.

Make sense yet?

The Future Future League (FFL) is **Magic**'s internal Constructed playtest team. It's composed primarily of **Magic** developers and a few enthusiastic deck-brewers from other departments. This article will be about what the FFL does, why it exists, and how its efforts ensure that **Magic** continues to be the best game it can be. But before I start talking about what the point of the FFL is, it's important to clarify an even more fundamental question: What is the point of **Magic** development in the first place?

### Oh, So You Guys Like Tweak Numbers and Stuff?

We sometimes joke in R&D that people view development as the IT department of game design. We're supposed to make sure things run smoothly, the idea goes. We're supposed to ensure that nothing breaks, and when something does break we're supposed to fix it. Essentially, it's like design hands us this super cool excited energetic precious playful puppy, and we have to toss a leash around it, potty-train the thing, and make sure it doesn't get itself into too much trouble.

![](https://i.ormos.uk/28/e3/28e3e77ec07ecdb6106589a3b3a41fb1b0fb7aef88dbde949c0dd5f708d6a855.jpg) 

  

This is a totally coherent model and is also totally wrong.

A long time ago, R&D did operate kind of like this. The maxim went something like, "Design's in charge of making **Magic** *fun*, and Development's in charge of making **Magic** *balanced*." We've learned a lot since then, though. Specifically, we learned that sacrificing fun in the name of balance misses the point entirely. I promise you I can host a meticulously balanced, masterfully orchestrated staring-at-the-wall contest. That doesn't mean that anyone wants to participate in it.

Nowadays, both design and development are principally concerned with making **Magic** as fun as it can possibly be. The difference is that we use slightly different sets of tools, which reflect the fact that sets are at different stages of maturity when design and development get their hands on them. Design is focused on ensuring that a set's features, mechanics, and themes have the ability to be fun when executed properly. They're mining for gold, trying to make sure that the materials exist to create something awesome. Development, by contrast, focuses more on the game-play value of the specific cards themselves—that, as a set takes shape, the different pieces interact in a way that's satisfying. They take the gold handed to them by design and *shape* it into something awesome.

![](https://i.ormos.uk/90/9d/909d40200727ecc16c5b5e7268564a8e4651901002a676e57ef6efade27cceb2.jpg) 

  

Basically, design says, "Play with these toys. We think they're fun." Development takes those toys, plays with them, and makes sure they really are.

That does kind of beg a question, though.

### What We Talk About When We Talk About *Fun*

The idea of fun is subjective, of course.

It's tempting as a game designer to use that subjectivity as an excuse to create an experience that's cool for you, then pass it on to the players and blame those players for not liking your idea. "Oh, they just don't understand why this is cool," it's easy to say. "Well, the idea was good, they just don't get it," you might tell yourself.

If that's what you're doing when you design a game, though, you should work a little harder.

Taste is subjective, but there exist (for example) bad books and good books, and when I tell you, "This book is bad," you don't stare blankly at me as if that idea doesn't mean anything to you. Even if our tastes don't exactly line up with one another, certain traits are indicative of quality and other traits are not. A good book probably employs evocative imagery, showcases multifaceted characters in intriguing situations, and avoids needless repetition of clichéd ideas or values.

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <img src="https://i.ormos.uk/c1/73/c173c4daca9c17692e43c220beb6fdbc3f44a11ee57d7a73d9663a64e67e504f.jpg">&#10;        </div>&#10;        <div>&#10;          <i>That's a bad book.</i>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Similarly, a fun game-play experience may mean a lot of things to a lot of different people. After all, we talk at length about [Timmies, Johnnies, and Spikes](/en/articles/makingmagic/2006/03-20-timmy-johnny-and-spike-revisited-4)—their different wants and needs, the feelings they crave when they play a game. We know we need to hit a lot of different targets. A lot of those targets overlap, though. Everyone wants to cast their spells. Everyone wants the specific cards they choose to include in their deck to matter. And everyone, to some degree, wants to resolve an element of the unknown: Who is going to win? What cards am I going to draw? What will I learn that I didn't know before?

There are things that **Magic**, as a collectible card game, is excellent at doing—promises that, explicitly or otherwise, it makes to its players. When we tell you you can create a deck, it implies that the act of creating that deck is meaningful, that somehow such a deck will be different from other decks created by other people. When we tell you that deck should be composed of individual cards, it implies that the act of drawing those cards should be exciting, and that separate cards should create separate experiences from one another. And when we tell you to collect those cards, it implies that you should feel a sense of evolution, of progress, of goal-fulfillment, as the pieces of your deck come together.

When we fail to do that, we're failing to deliver on the promise that the structure of our game makes to the player. That feels bad and is bad in the way that being lied to both feels bad and is bad. As members of **Magic** R&D, then, we are obligated to ensure that the reality of our game experience parallels the promise that the idea of our game experience makes.

The FFL is the best way we have to do that.

### Standard Issues

Many players—though certainly not all—participate in **Magic** by playing the Standard format. It's got a lot of benefits: you don't have to own nearly twenty years' worth of cards, or remember what twenty years' worth of cards all do, or evaluate the cards in every single booster pack you open against every single other booster pack you've ever opened when trying to decide whether some cool new card can go into a deck. Consequently, we spend most of our time playtesting Standard.

Furthermore, we spend most of our time playtesting *competitive* Standard. It isn't necessarily intuitive that we'd do this, since most people don't actually engage with our game at the competitive level. It's important that we operate this way, though, because oppressive decks and strategies have a habit of percolating down to the casual level. If the metagame—the environment of decks and strategies that people choose to play—can remain robust when it's being strained to its maximum, it's likely that it can remain equally or more robust when its boundaries aren't being pushed as hard.

What do I mean when I say "oppressive decks and strategies," though?

![](https://i.ormos.uk/af/53/af535e7f7d89e5e4ca27ef7bd000a6408882fc42977f8e8d4888bf34213b7655.jpg) 

  

As mentioned earlier, an essential element of **Magic** involves the ability to create a deck and play it. Other people may create decks that are better than yours, that can defeat yours, but as you improve you should always be able to figure out a way to attack their strategy and get ahead. Furthermore, even if you're not as interested in cutthroat competition, you should still be able to do something you think is cool and have an interesting narrative pan out. When a certain deck is too powerful, or when certain unhealthy strategies become dominant, it threatens players' abilities to do the types of things that make **Magic** fun. Why go out and create your own deck when it doesn't stand a chance against the elephant in the room? What's the point of selecting between thousands of cool, unique cards when none of them really matter?

Any deck can become overly dominant, but we've noticed that certain kinds of strategies really damage game play at any level. These tend to be, in descending order of frustration:

*   "Prison" control decks, which aim to lock players out of the resources to cast their spells, while grinding out a slow, gradual long game
*   Land destruction decks that never let the opponent get off the ground
*   Lightning-fast combination decks that end the game as quickly, and noninteractively, as possible
*   "Draw-Go" style counterspell decks that do nothing except counter the opponent's spells
*   Resource-advantage decks that aim to make **Magic** a contest of raw attrition

All of these decks share a common root: they eliminate the dynamism and excitement that comes with constructive interaction between cards, largely because their goal is to ignore as much of the rules text on the opponent's cards as possible.

As you can see, the issue isn't simply one of game balance. If there's an environment where you can choose between numerous equally viable ways to blow up all your opponent's lands, you're still not going to be having a whole lot of fun.

The FFL allows us to hedge against these kinds of problems. If a certain deck, in our playtesting, starts to beat all of our other decks, we can make some of its key cards weaker or power up other cards to attack it. If a certain unfun strategy becomes dominant, we can alter the cards that promote that strategy. And if it doesn't seem like enough decks are doing something cool—if, in other words, there's not enough "spice" in the environment—we can print new, interesting, "build-a-deck-around-me" cards that take **Magic** into unfamiliar territory... assuming, of course, that those cards themselves don't become too dominant or unfun.

Sounds easy, right? Just identify all the problems, solve them, and voila! You're done!

### Building a Mystery

When we release a set, we're handing a key to millions of players that allows them to explore a new environment across millions and millions and millions of games. This environment should prove to be new and interesting, full of cool discoveries and interactions that spawn creative ideas and totally unique directions of play. This environment should remain fresh and intriguing for at least the several months until the next set's release, when the pattern resets itself anew.

At any given point there are between eight and ten people actively participating in the FFL.

I am fortunate to work with some amazing people. Under our roof are some of the most talented, capable deck designers in **Magic** history, including a number of Pro Tour Champions, Pro Tour Hall of Famers, and deckbuilding masterminds. But if we create an environment that can be solved by a handful of people—even very talented people—over the course of **Magic**'s development cycle, we have failed.

![](https://i.ormos.uk/87/9a/879a7abd7c654824e9cd4b1cd007a7452b4cdb5f11ea30e847c2fd5f7cb89815.jpg) 

  

I get asked a lot how certain cards or effects slip through the cracks. Certain strategies will be obviously too powerful, and certain environments will obviously exhibit fundamental problems. Sometimes, of course, we mess up. But it would be easy to envision a world where none of these problems emerge. I could create a totally predictable Standard metagame right now. Simply print twenty or thirty cards across all five colors that are obviously, flagrantly better than every other card in the environment, and all of a sudden the "real" pool of cards you have to work with is reduced dramatically. This is why Vintage decks can main-deck multiple copies of Null Rod even though the card literally does nothing against a giant percentage of the decks theoretically available in the Vintage format: a massive power differential allows you to focus only on what matters.

This world would be miserable, though, even though it would be very easy to balance effectively. The sense of discovery would dry up within days, and the sets of interactions between viable decks would be exhausted almost immediately.

Instead, what we try to do is create environments filled with a host of roughly comparable strategies. We try to have some idea of the best things to do within that environment, and we like to know what that format's defining cards and interactions will be. We realize, of course, that inevitably some strategies will rise to the top. Our goals are 1) to make sure those strategies are fun, and 2) to put mechanisms in place that ensure those strategies don't remain dominant for too long.

We accomplish this in a variety of different ways:

**1) Don't keep all the goodies in the same place.** 

In previous environments, we've been haunted by "block monsters": decks whose powerful cards all exist in the same set at the same time. Faeries, for example, was constructed almost entirely out of *Lorwyn* and *Morningtide* cards. This is a bad idea, because you have to live with that deck for as long as the problem set lives in Standard—in some cases, for years at a time.

What we try to do now is "seed" some cards for a format's likely strategies in earlier sets. This ensures that, when a rotation occurs, a lot of that format's most powerful archetypes are meaningfully affected. A great recent example of this was the inclusion of Steel Overseer in ***Magic** 2011*. We were pretty sure that, in the wake of *Scars of Mirrodin*, some kind of artifact creature deck would be a force to be reckoned with. By putting a powerful card for that strategy in an earlier rotation—and balancing around it—we were able to distribute the total power of that deck across multiple sets and rotations.

 ![Steel Overseer](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Steel%20Overseer&options=) 

  

**2) Let them kill your darlings.** 

If what you want to do going into a format is seed some potentially powerful strategies, you also want to give players tools to attack those strategies moving out of it. This once again prevents the metagame from becoming too stagnant. As cards become available to combat a format's existing archetypes, the players who choose to pilot those archetypes are forced to adapt to a different world. Either they decide to play new decks entirely—causing a shift in the environment—or they have to modify their decks to react to new hate cards, which simultaneously takes those decks in a new direction and tends to weaken them overall. Examples of this plan in action include the presence of both Ancient Grudge and Stony Silence in *Innistrad*, which fight the artifact-centric strategies of *Scars of Mirrodin* block and help keep the environment fresh.

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Ancient Grudge" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Ancient%20Grudge&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;      <td>&#10;        <div>&#10;          <div>&#10;            <a>&#10;              <img alt="Stony Silence" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Stony%20Silence&amp;options=">&#10;            </a>&#10;          </div>&#10;        </div>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

**3) Think small.** 

When you're lead developing a set, the temptation is to print as many massively powerful cards as possible. After all, don't players like to do powerful things? Don't you want your set to stand out above the rest? This seems intuitive but is actually disproved by our data, which shows that players universally respond better to weaker formats and weaker sets. Why is that?

![](https://i.ormos.uk/d9/03/d903fbeca10b3ee8634597043a103f00b980413616ef5190a5d324db3ba4d3f0.jpg) 

  

It's related to the thought experiment we talked about earlier, with the format comprised entirely of twenty or so superlatively powerful cards. There's just much less discovery there. What if I don't want to play with one of those twenty cards? What does the format have to offer me? And what if I'm sick with dealing with one of those twenty cards? What else can I do that competes with it?

When some cards in a format stand head and shoulders above the other ones, developers of subsequent sets have two options: either they can a) print cards with similar overall power levels to those overly-dominant cards, "creeping" the power of **Magic** to an unhealthy level, or b) accept the reality that their set will be weaker, ensuring that the same cards continue to dominate for even longer.

Both of these outcomes are bad. A responsible developer therefore aims to moderate the power of the cards in his or her set, ensuring that things remain at a more or less constant level across a given Standard format. The FFL, meanwhile, helps the developer know whether or not these attempts are actually succeeding!

**4) Playtest. A lot.** 

This, of course, is the most important part. It's not romantic, it isn't slick, and it doesn't make you sound smart when you write an article about it. But sometimes the best way to know what's happening with a given format is simply to play until you have enough data to make conclusions about it. We're never going to have perfect information, but the more we can get a feel for an environment's interactions, the more we understand what drives it, the better we're able to maintain a full, complete, holistic understanding of what's going on. And that affects everything we do.

### The Future of the League

The FFL is, at the end of the day, a tool in a toolbox. We're constantly refining how it operates and we're constantly rethinking what it can do. A lot of the ideas discussed in this article didn't apply five years ago, and a lot of them probably won't apply five years from now. What's important isn't that these processes remain exactly intact, or these techniques continue to produce exactly the same results. What's important is that **Magic** remains fun.

As a **Magic** designer/developer, I spend a huge chunk of my time playing the game. What's cool about that is that the better I do my job, the more fun I wind up having. Conversely, it also means I really feel the damage whenever I make a mistake, because I have to live with the results of that mistake day in and day out, just like you guys do. So if it ever seems like we're really passionate about our work, it might just be because we're really selfish, and don't want to slog through yet another wave of Cryptic Command mirror matches for the umpteenth week in a row. :)

I hope you've enjoyed this insight into how we work. Please feel free to email me with your thoughts using the link at the bottom of the page, or hit me up on Twitter: @[zdch](http://twitter.com/#!/zdch). Is Standard fun for you? Anything obvious you think we're missing? Any questions about things that have happened in the FFL? I'm all ears.

At least until I start talking, that is.

* * *

  

![](https://i.ormos.uk/de/61/de610ee6bd6662eadd1ef84855886025655c4666aa92fa8c19549a455afab7a0.jpg) ![](https://i.ormos.uk/21/0c/210c4f783ebb895a2393c23b6a553dd97ddb4846a029d152cca2e6c75ac13a54.jpg) [![](https://i.ormos.uk/41/3e/413eecb73f09eb7faeb80fd74dc4f80e135ee873e1be1a4eb5ecdd4defaf5643.jpg)](https://web.archive.org/web/20111017000000/http://staging.wizards.com/Magic/Digital/MagicOnline.aspx)
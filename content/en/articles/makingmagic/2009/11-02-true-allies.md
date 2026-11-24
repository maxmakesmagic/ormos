---
id: b51tk419
kind: article
lang: en
path: /en/articles/makingmagic/2009/11-02-true-allies
title: True Allies
published: '2009-11-02'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
    lang_detected: en
    capture_id: 931031
    url: https://magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
    captured_at: '2022-10-04 19:27:27+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
    lang_detected: en
    capture_id: 931031
    url: https://magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
    captured_at: '2022-10-04 19:27:27+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
    lang_detected: en
    capture_id: 931031
    url: https://magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
    captured_at: '2022-10-04 19:27:27+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
    lang_detected: en
    capture_id: 931031
    url: https://magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
    captured_at: '2022-10-04 19:27:27+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: b51tk419
  url: https://magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
  page_key: magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
  lang: en
  template: drupal
  captured_at: '2022-10-04 19:27:27+00'
  capture_id: 931031
  wayback_url: https://web.archive.org/web/20221004192727id_/https://magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-11-02
- document_id: b51tk419
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/mm/63
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/63
  lang: en
  template: aspx
  captured_at: '2013-07-02 07:07:56+00'
  capture_id: 653412
  wayback_url: https://web.archive.org/web/20130702070756id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/mm/63
- document_id: b51tk419
  url: https://magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-10-30
  page_key: magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-10-30
  lang: en
  template: drupal
  captured_at: '2022-05-17 12:35:22+00'
  capture_id: 931023
  wayback_url: https://web.archive.org/web/20220517123522id_/https://magic.wizards.com/en/articles/archive/making-magic/true-allies-2009-10-30
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: b51tk419
  capture_id: 653412
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/mm/63
  wayback_url: https://web.archive.org/web/20130702070756id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/mm/63
  captured_at: '2013-07-02 07:07:56+00'
  template: aspx
  sha256: 753cdd9bbc82682b8bf965ad6dbc17867414224f94999245df81c20f4f1ec357
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Goblin King
  - Naturalize
  - Harrow
  - Hill Giant
  - Muscle Sliver
  occurrences: 13
---
Welcome to Ally Week! This week we're going to be exploring the most linear of *Zendikar*'s mechanics. I'll walk you through their creation while interweaving the explanation of design's need for linear mechanics. I might even go into a little more detail into the origin of the ally mechanic.

### Allies My Mother Told Me

Before I jump into the story, I guess you probably want to read the Ally section of my [second *Zendikar* preview article](/en/articles/makingmagic/2009/09-14-achieving-zendikar-part-ii) if you haven't already. (It's under a section called "Chaps"—the article explains why.) That article explains the basic story of Allies' design, but because I was trying to talk about so many different things in one article, it was an abridged story. Today you get the unabridged version.

So, the Allies' story begins in two different places. The first part happens even before we realized that our setting was going to be an adventure world. The design team (Doug Beyer, Graeme Hopkins, Ken Nagle, Matt Place and myself) were still fiddling around with land mechanics, and we had recently added in kicker. Traps, quests, adventurer's Equipment—all that was off in the future. Matt came to me with an idea. It was becoming clear that the land mechanics were going to be more modular designs, and that the set didn't have a linear design yet. 

![](https://i.ormos.uk/2c/bb/2cbb967788f37b14b5e6534524083955209c74b0dcf67d1561d750cd93107553.jpg) 

  

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <img src="https://i.ormos.uk/ea/73/ea735b57f85dcb61eb1ce7d1872e15c479db35fd9ee4a803f1eb7cccad3ef204.jpg">&#10;      </div>&#10;      <div>&#10;        <i>The king of modular.</i>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

Let me quickly jump in with some definitions as I'm using as few words as if they're normal English instead of **Magic** design-ese. The terms are linear and modular. In design, linear refers to a mechanic or card that dictates the need for specific other cards to be used with it. A classic example of a linear card is Goblin King. You are not going to use it in a deck without adding Goblin cards. Modular refers to a mechanic or card that stands alone and doesn't need other things to make it work. The classic example of a modular card would be Naturalize. Other than green mana sources to cast it, the card requires no other cards to support it. I wrote an entire article ([Come Together](/en/articles/makingmagic/2003/10-06-come-together)) about this concept if you'd like to hear me explain the terms and impact on design in greater detail. Today's column is going to build on this knowledge so I will dub it "recommended reading."

Before I jump back into Allies, one more quick aside. (I seem to be in an aside mood today.) I've always thought of linear and modular as ends of a spectrum, so I assumed that a mechanic had to be either linear or modular but was incapable of being both. Then we designed landfall. The mechanic is linear in that it encourages you to play with certain styles of cards (Harrow, fetch lands, and the like; things that get more lands onto the battlefield) which in turn encourages you to play with more landfall cards, yet is modular in that you can throw any one landfall card into a deck and it will function just fine. What does this mean for the definition of linear and modular? Honestly, I don't know. It does show me, though, that in design nothing can be taken for granted. What seems like solid earth one day may shift tomorrow.

When last I wasn't making asides, Matt had come to me with a worry that *Zendikar* was lacking a linear mechanic. At the time we were playing with landfall, "spell" lands and kicker, all of which feel very modular (the linear-ness of landfall is less apparent at first glance). He had been playing around with something he wanted to show me, something he called Super Slivers.

Before we talk Super Slivers, let me first answer the question that this story brings up. Why must a set have a linear component? In my original article on linear and modular, I talk about how designs vacillate back and forth on the spectrum. (Or is it now a circle?) What I don't talk about is how it's important for all designs to have some of each. Why? The same reason that **Magic** is such a challenge to design for: **Magic** is a different game to different people.

One of **Magic**'s greatest strengths is its customizability. More so that just about any game I can think of, **Magic** gives its players the ability to determine what kind of game it is. Between selecting your deck, your format, and your opponent(s), **Magic** has a sweeping range of possibilities. The challenge for design is that every set has to speak to all the players even though what they want out of the game varies greatly. Another way to think of it is this: **Magic** is not one game but thousands of games. Each set has to be designed to work in each of those games.

The trick design uses to accomplish this task is the following: not every card has to be designed for every player. This also holds true for mechanics and themes. To make a player happy with a set we have to provide them something (and most often several somethings) they like. They don't have to like everything. The things they don't like (or more often don't care about) is the space where we get to make different types of players happy.

![](https://i.ormos.uk/c7/cf/c7cf6bc491648eba01a84fcf62e6d549333cfd1102252d7182ab61f745f1a8c5.jpg) 

  

The linear/modular discussion basically stems from this concept—that we need to make everyone like something but not everything. Some players crave linear mechanics because they add an important comfortableness. I will use my five-year-old twins to explain. (I mean as an example—I won't make them write a paragraph or anything.) Adam and Sarah both love drawing. Sarah likes coloring books. They have pictures of things she likes and it is fun to color them in. Adam prefers to have blank pieces of paper. He likes to draw his "own world." Neither is the correct or incorrect way to color.

Sarah's pictures are much neater and the average adult can tell what her pictures are. In addition, they get to connect into other things she cares about, such as popular media properties. Adam's pictures are more creative and allow additional self-expression. (Hmm, if Rachel, my oldest, could somehow strive to always draw the best pictures, we might have the making of a Rosewater psychographic parallel.) Each child is getting what he or she wants out of the drawing experience.

So what do linear mechanics offer? A few things:

**Comfort** – Some players have fun in figuring out how to do something rather than figuring out what to do. They like coming to a new set and say, "What cool new thing do you have for me to play with today?"

**Guidance –** Linear mechanics tend to spell out what they are looking for. Allies, as the perfect example, want other Allies. When looking through *Zendikar* cards, players can easily find the most obvious cards to consider for an Ally deck.

**Shared Experience –** Community is created through shared experiences. For instance, all of the readers of **magicthegathering.com** are brought together by their interest in **Magic**. It becomes very easy to talk in the forums because you all have a common interest. (For example, in my thread you can all share in your take on what I said wrong this week. :) ) Having linear themes to build around helps create conversation points. 

**Something to Measure Against –** When players are building their own versions of a linear theme, they have the ability to see what many others are doing. "Here's my Goblin deck. What do other people's Goblin decks look like? How does mine measure up?"

### Up, Up, and Away

All this talk about the importance of linear mechanics brings us back to Matt and the Super Slivers. Matt is a giant fan of Slivers, mostly because many of you are giant fans of Slivers. Slivers are definitely one of the most popular linear mechanics we've ever created. (Made by Mike Elliott prior to coming to work at Wizards and then put into Mike's first design team, *Tempest;* you can read more about it [here](/en/articles/feature/2008/11-24-before-the-storm).) As such, Matt is always on the lookout for more Sliver-like mechanics.

![](https://i.ormos.uk/e7/3d/e73d6bd96dd02608a8b7851090cfb967b5b246e8780cfa7fe9bf4d3dad83f55c.jpg) 

  

Super Slivers, though, weren't a Sliver-like mechanic as much as just an expanded Sliver mechanic. I don't remember that exact cards Matt showed me, but here is the gist:

> **Super Winged Sliver**  
>  2U  
>  Creature - Sliver  
>  1/1  
>  When CARDNAME enters the battlefield, put a +1/+1 counter on all Slivers in play.  
>  All slivers gain flying.

Yes, he was pitching Slivers that while doing what Slivers always do, in addition, put a +1/+1 counter on all other Slivers when they entered the battlefield. My comment to Matt was that while I liked the tweak, I didn't feel *Zendikar* was the right place to bring back Slivers. They had appeared in large numbers in *Time Spiral*, and bringing them back just three years later seemed too fast. So I said no to Super Slivers. I did agree with him, though, that the set wanted a tight linear mechanic.

### I Heard There Was a Party

Now we flash forward a few months. (I'm happy to report that none of the design team collapsed into unconsciousness for two minutes and seventeen seconds.) The creative team has pitched the idea of "adventure world," and the design team was trying to figure out what mechanical components we could add to help increase the "adventure world" feel. As I've talked about in other columns, one of the most familiar places R&D drifted to was the classic roleplaying game **Dungeons & Dragons** (made by some company I can't recall right now).

![](https://i.ormos.uk/51/b3/51b31a9d944d0007f8fd06b9de2a608a6895289d8fabdefd5d9f6d5ee1601caf.jpg) 

  

As one of our recent goals has been to increase the resonance of **Magic**, turning to the Mecca of medieval gaming fantasy for inspiration seemed like an obvious choice. It was through looking at our set through the lens of **D&D** that the team came to an obvious realization: we needed adventuring parties.

The first step in finding a mechanical execution is to figure out the flavor essence that you are trying to capture. What is at the center of an adventuring party? The adventurers, of course. We wanted fighters and wizards and clerics and thieves all working together (is my "I played **D&D** in the late 80s" showing?). Mechanically, this meant two things. One, we had to have creature cards of the appropriate classes, and two, we needed a mechanic that made them better in numbers thus encouraging you to want to play them together. 

In the preview article, I claimed the first version of the mechanic was called "adventurer." This isn't exactly correct. While the mechanic was eventually changed to the name "adventurer," the first version of the mechanic was called "teamwork." (This is the kind of thing that happens in abridged versions—you squash things together for the sake of brevity.) Teamwork worked very simply. Any creature with teamwork got a bonus when its controller controlled another creature with teamwork.

The idea was simple and it did a decent job of getting the flavor across. Only one problem: it wasn't simple. Let me explain. Imagine that the following card is the very first card you pull out of your very first *Zendikar* booster pack:

> Awesome Fighter  
>  3R  
>  Creature - Human Warrior  
>  3/3  
>  Teamwork  
>  CARDNAME gets +1/+1 if you control another creature with teamwork.

Here is the thought process that I believe the majority of players go through:

"Hmm, it's a Hill Giant with an ability. Oh, and if you have another creature with the same ability it becomes a 4/4. Sounds cool. Okay, what does teamwork do? There's no reminder text. Is this some ability that I'm supposed to already know? Did ***Magic** 2010* add a keyword that I just missed? It can't be a new ability. They would have put reminder text on the card. Whatever, let's see the next card."

The confusion doesn't stop there, though. As each creature has its stats change whenever another teamwork creature is in play (under their controller's control), there are often going to be numerous creatures with stats that are different than what is written on the card. To make matters worse, as some of those creatures leave the battlefield, that can affect the stats of others on the battlefield. This both creates memory issues and makes it much harder to assess the battlefield, increasing what we in R&D call board complexity.

 ![Muscle Sliver](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Muscle%20Sliver&options=) 

Design's next step was to try to solve both problems with one solution. If teamwork not doing anything caused confusion, then let's have it do something. In addition, if that something could be the thing that helped teammates help each other rather than relying on static power/toughness changes, that would be great.

This is the point where our two stories intersect. Matt came to me and suggested that we use Super Sliver technology to solve our Ally dilemma. What if teamwork meant that a creature put a +1/+1 counter on itself and all other creatures with teamwork when it entered the battlefield? It sounded like an interesting idea, so I added that change to the file. I think this is where "teamwork" was changed to "adventurer."

Before I explain what happened, can you spot the problem? For those of you familiar with Sliver history, you probably know what the best Sliver was when they premiered in *Tempest*. The Sliver was named Muscle Sliver, and it granted +1/+1 to all other Slivers. The adventurer mechanic turned every Sliver into a Muscle Sliver. Actually, it turned every Sliver into something better than a Muscle Sliver, because the bonus granted by Muscle Sliver at least went away if your opponent could get rid of the Sliver. Due to the +1/+1 counters, the bonus added by a creature with adventurer never went away.

This was around the time that the set was handed off from design to development. We hadn't quite cracked Allies yet, but there was some hope that a small tweak could solve the power-level issues. As development is very good with power level, design left the issue in development's hands. I went off to start working on the design of next fall's large set, "Lights."

One of the roles of a lead designer for a set is that you're supposed to keep abreast of what is going on in development to either help out with new designs needed or to give some notes if you feel some aspect is drifting too far away from its initial intent. As such, I kept my eye on *Zendikar* development. About a month or two into development, it became clear to everyone that Allies, as they were, were not working. Something had to change.

While development fiddled with some ideas, Matt and I got together to try to propose a new design for Allies. Because this mechanic was filling an important flavor task, we started by figuring out what we had to do mechanically to capture the feel we wanted. After some discussion here's what Matt and I agreed on:

**#1) Allies had to care about other Allies.** This first rule might seem obvious as the entire design of Allies stemmed from a desire to have a linear mechanic, but when spelling things out you should always state the obvious because it's amazing how easy the obvious is to miss when it isn't spelled out.

**#2) Allies had to grow in power the more Allies you had.** There are a number of ways for cards to care about each other. Because we were going for a Sliver feel, we wanted a mechanic that heartily encouraged you to play a deck full of Allies. To do this we needed to make each Ally matter. As such, we agreed that each card would grow stronger with each additional Ally.

**#3) Allies needed to not add board complexity.** Very simple cards can create intensely complex boards if they each make the player care about a different thing. We wanted Allies in number at common, and we wanted them to be relevant for Limited. That meant that we had to find a mechanic that didn't add too much board complication as you got more and more Allies onto the battlefield.

**#4) We needed the mechanic to support a variety of effects.** We wanted to have creatures that felt like characters you would have in an adventuring party—This meant that the mechanic had to allow enough variation for different creatures to feel like a party's fighter, wizard, cleric, thief, and so on.

### A Web of Allies

Of the four restrictions above, the thing we started on was #3, as it was the greatest restriction. How could we have Allies affect one another without creating complex memory issues? It seemed we had two obvious choices. We could make use of counters, most likely +1/+1 counters, or we could have effects that only lasted for a turn. In the end, we decided to try both.

![](https://i.ormos.uk/77/7d/777d2a8d1e858c830362e6749ca9fa39c05da54d4234508908b5c0f66c04e97d.jpg) 

  

We examined different "until end of turn" triggers. The one that seemed the simplest to remember was the "enter the battlefield" (ETB) trigger. It came up that landfall also had an ETB trigger. Rather than fight the similarity with landfall, we decided to embrace it. One of *Zendikar*'s themes would be ETB triggers. Once we decided to try an ETB trigger, we looked at our other restrictions to see how we could do this. After some searching, we came up with three ways that made sense:

First, we could generate an effect that scaled its size based on how many Allies you had on the battlefield. The more Allies you had, the bigger the effect. Because we work with scaling effects all the time, we were well aware how we could manipulate them to keep them from going crazy on the large end of the spectrum. For instance, a common trick with direct damage is to just have it hit creatures. Yes, scaling up can help the damage take out larger creatures, but there isn't much difference between 5 damage and 10 damage most of the time, making the top end scale manageable from a power level perspective.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Murasa Pyromancer" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Murasa%20Pyromancer&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Hagra Diabolist" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Hagra%20Diabolist&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

This effect felt very much like a giant spell being cast, so we sub-categorized them as "wizards." Note that our subcategorizing wasn't the definitive creative answer for each creature—a "wizard" didn't have to be concepted as a wizard, just someone who made sense creating the effect; for example, the discard Ally was concepted as a thief.

Second, we could generate an effect that affected all your Allies. This worked for #2, because the more Allies a player has, the more he or she can affect and thus the stronger the impact. This felt a lot to us like "buffing" in RPGs, and thus we dubbed this subclass the "clerics."

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Kazandu Blademaster" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Kazandu%20Blademaster&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Turntimber Ranger" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Turntimber%20Ranger&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

Finally, the last way we found to make this work was to use +1/+1 counters to permanently enhance Allies. To make it work, we flipped the adventurer mechanic around so that each creature got a +1/+1 counter whenever itself or another Ally entered the battlefield (controlled by the same controller). Unlike the last two effects, this effect would last beyond the turn the creature was played, but due to the +1/+1 counter, there wouldn't be any memory issues. We dubbed this last group the "fighters," as they got stronger the more teammates they had.

With our proposal in hand, we went to the development team and pitched them our version of Allies. I guess it should come as no surprise that they liked what we pitched and adopted it for the set.

### Allies, Damned Allies, and Statistics

Hopefully, today's column can show how something very simple on the surface can go through significant changes through the design and development process. I'm curious to hear what all you think of the ally mechanic. Please let me know in my email, in the thread, or on my Twitter account (@[maro254](http://twitter.com/maro254)).

Join me next week when I face my most brutal interview ever.

Until then, may your friends empower you.
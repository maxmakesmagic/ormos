---
id: x1r859mg
kind: article
lang: en
path: /en/articles/makingmagic/2024/01-08-why-so-many-restrictions
title: Why So Many Restrictions?
published: '2024-01-08'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/why-so-many-restrictions
    lang_detected: en
    capture_id: 234500
    url: https://magic.wizards.com/en/news/making-magic/why-so-many-restrictions
    captured_at: '2024-05-18 01:03:46+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/why-so-many-restrictions
    lang_detected: en
    capture_id: 234500
    url: https://magic.wizards.com/en/news/making-magic/why-so-many-restrictions
    captured_at: '2024-05-18 01:03:46+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/why-so-many-restrictions
    lang_detected: en
    capture_id: 234500
    url: https://magic.wizards.com/en/news/making-magic/why-so-many-restrictions
    captured_at: '2024-05-18 01:03:46+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/why-so-many-restrictions
    lang_detected: en
    capture_id: 234500
    url: https://magic.wizards.com/en/news/making-magic/why-so-many-restrictions
    captured_at: '2024-05-18 01:03:46+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: x1r859mg
  url: https://magic.wizards.com/en/news/making-magic/why-so-many-restrictions
  page_key: magic.wizards.com/en/news/making-magic/why-so-many-restrictions
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:03:46+00'
  capture_id: 234500
  wayback_url: https://web.archive.org/web/20240518010346id_/https://magic.wizards.com/en/news/making-magic/why-so-many-restrictions
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: x1r859mg
  capture_id: 234500
  url: https://magic.wizards.com/en/news/making-magic/why-so-many-restrictions
  wayback_url: https://web.archive.org/web/20240518010346id_/https://magic.wizards.com/en/news/making-magic/why-so-many-restrictions
  captured_at: '2024-05-18 01:03:46+00'
  template: contentful
  sha256: 79194a7cea563d93b951dd4bac68d4651e3cdc9a5619fbfc0ab1d82f8445cce6
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
I have [a blog on Tumblr called Blogatog](https://markrosewater.tumblr.com/) where I answer questions every day. Many questions I can answer with a blog post, but occasionally, I get a question with a long enough answer that I'll use my *Drive to Work* podcast to answer it. For today's column, I'm using a question I answered recently on the podcast. I liked it enough that I decided to turn it into an article. (Ah, the synergy of creating lots of content on different mediums.)

The question, which I got from numerous posters, could be summed up as follows:

**I've noticed that R&D is adding a lot more restrictions to cards these days with things like "can only be cast as a sorcery," "only use once per turn," "only use on your turn," etc. Why are you doing this?**

To answer this question, I'll first answer some supporting questions that lead up to it.

### Why even have restrictions?

To answer this question, let me talk a little about the role of a game designer. Many years ago, I wrote an article called "Ten Principles of a Good Design" ([Part 1](/en/articles/makingmagic/2010/05-03-the-ten-principles-for-good-design-part-1) and [Part 2](/en/articles/makingmagic/2010/05-17-the-ten-principles-for-good-design-part-2)) where I talked about the rules laid out for good design by Dieter Rams, a German industrial designer. Dieter Rams is considered to be the biggest influence on Jonathan Ive, the main industrial designer at Apple. The point of my article was about the universality of design. A man who made appliances and lamps created a series of design principles that were so relevant to *Magic* design that I was able to write a two-part article about it. But there was one point where we, as designers, deviated.

When Dieter Rams, or any industrial designer, creates a lamp, the goal of that lamp is to be as easy to use as possible. Turning it on, adjusting the light level, moving it such that you can shine light where you need it should all be intuitively obvious. The goal is to minimize the user having to think about how to use it. It should feel like a natural extension of the user. In contrast, let's say we made a game lamp. Turning it on wouldn't necessarily be easy because the goal of a game is to mentally challenge the user. Yes, we want players to intuit how to use the game pieces, but a core part of game design is that we, the game designers, are trying to challenge you, the player.

That's how game designers are different than most designers. Our main goal is to provide obstacles to the user. The thrill of a game is getting to mentally test yourself, to see if you have the skills to accomplish the goal of the game. That means restrictions aren't a by-product of a design, they're an important part of it.

Back in 2011, I wrote an article called "[Ten Things Every Game Needs](/en/articles/makingmagic/2011/12-19-ten-things-every-game-needs-part-1-part-2)" based on a talk I gave to my daughter's fifth-grade class about the core elements of making a good game. Among them are a goal or goals and rules about what you're allowed to do to meet those goals. To make a good game, the goal(s) can't be too easy and the rules have to provide significant obstacles. *Magic* wouldn't be a particularly fun game if the goal was "the first person to draw a card wins."

This gets into a topic I haven't yet written a whole article about: a concept in entertainment known as a "safe experience." There are many things we'd like to experience, but in real life, they come connected with dangerous activities. For example, being scared is problematic when there's the potential for actual jeopardy, so it's hard to enjoy being afraid in real life. But a horror film allows you to access those same emotions in the context of a safe space. One of the things entertainment can offer people is the ability to experience something without the threat of consequences.

Let's bring that around to games. Games offer you a chance to work on your ability to problem solve and do creative thinking but in a context where failure doesn't have real-world consequences. As such, it's important for games to test you. They need to be designed in such a way that the player is challenged at a level that matches their abilities. Part of this is usually playing against another person or people as their goal is usually counter to yours. If you chose players at a similar skill level, it can provide a good mental workout. On top of that, the game designers also want to make sure that you're properly engaged and tested, which means we have to build our goal(s) and rules such that they create an environment where players are challenged.

All of this is to say that first and foremost, restrictions are core to the game-design experience. So why do we add restrictions to the game? To make it a better game.

This leads us to the next question:

### Can't *Magic* be fun without restrictions?

The simple answer is no, but I think the better answer is this: *Magic*, from the very beginning, from *Limited Edition (Alpha)*, has always had restrictions built into it.

Let's walk through the restrictions that Richard Garfield built into the game from the beginning.

**Tapping**

![Llanowar Elves](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=166&type=card) ![Prodigal Sorcerer](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=121&type=card) ![Samite Healer](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=268&type=card)

The tap symbol didn't happen until *Revised Edition* (and it's changed several times over the years), but *Alpha* had tapping built into the game. Richard used it in a couple of key ways. First, there were some resources, mana being the biggest, that he only wanted players to access once per turn, and tapping was a way to demonstrate that a player used up the resource. Second, there were decisions that Richard wanted the player to make. For example, if you choose to attack with a creature, then you can't have it back to block for you (except creatures with vigilance, but that was only on one creature and sort of on one Aura in *Alpha*). Tapping as part of an activation on creatures was a cross between these two reasons. It limited its usage and made you choose how you wanted to use the creature each turn. Tapping for an ability came at the cost of being unable to attack (and possibly block, depending on when you needed to use it).

**The Mono Supertype**

![Black Lotus](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=3&type=card) ![Cyclopean Tomb](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=11&type=card) ![Disrupting Scepter](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=13&type=card)

Here's something Richard introduced in *Alpha* that quickly went away. Originally, there were different types of artifacts. A mono artifact could only be activated once per turn. A poly artifact could be activated as many times as you were able to pay the cost of the ability. A continuous artifact had an effect that was always "on." Artifact creatures were their own category. I bring this up because "only use once per turn" was so important to Richard that he executed on it in more than one way. Mono artifacts would later get a change to include a tap symbol.

**"Sorcery Speed"**

![Armageddon](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=233&type=card) ![Clockwork Beast](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=7&type=card) ![Animate Dead](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=48&type=card)

All the cards, save two card types (flash didn't exist yet, but interrupts were still a card type), could only be played on your turn. Even then, only during your main phase (multiple main phases would come later). Why did Richard do that? Because he wanted focus when players did things. This would help shape gameplay and provide strategic decisions. An important part of game design is creating the flow for the game, that is, the order in which things happen. You want to make it intuitive but also encourage the type of behavior that you think will lead to the best game experience. There's a reason that most game elements have a restriction built into them. Richard created the timing of things as he did because he wanted players to have a default for how a turn progressed. Note that he did make instants and had activated abilities mostly work at "instant speed" because he realized there were times when players should do things on an opponent's turn, but he wanted to minimize them.

**Casting Limitations**

![Siren's Call](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=125&type=card) ![Blaze of Glory](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=237&type=card) ![False Orders](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=195&type=card)

Even instants could have restrictions. Some spells needed to be instants because Richard wanted players to use them in combat, but he spelled out when and how they could use them. Richard understood that while flexibility had value, it was the game designer's job to be very exact on how game pieces were to be used.

**Activation Limitations**

![Dragon Whelp](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=189&type=card) ![Goblin Balloon Brigade](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=201&type=card) ![Nettling Imp](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=73&type=card)

Limitations don't stop with spells. Richard also realized he wanted to restrict how players used activations.

It's important to understand that restrictions have been a core part of *Magic* from the beginning. It's an integral part of what makes the game fun. But if you don't want to take my word for it, try the following test: Play a game of *Magic* where every card and every activated ability can be cast or played whenever an instant can be played. I think you'll find it both mentally taxing and less fun. It will also cause a lot of confusion because the rules aren't built to handle it.

### Okay, Richard built plenty of restrictions into the game. Why did R&D have to add more?

There are three different answers to this question. First, what *Magic* is today is very different than the game Richard invented and released back in 1993. This is no slight to Richard. I don't think anyone could have predicted then that *Magic* would become a phenomenon. Richard assumed the game would be like the scores of other games in the game store. You'd spend the amount of money you'd normally spend on a game and have a small amount of cards, no more than a few hundred. Then, occasionally, you'd maybe buy a booster or two to supplement your collection.

This is why the original rules for *Magic* had you build a 40-card deck and had a rule, known as ante (your eighth card would be put aside, and the winner of the game got to permanently keep their opponent's ante card), which would force card flow between players in a play group. There weren't any card restrictions because players wouldn't have that many of a particular card, save maybe commons, and many of those were designed to appear more often. Richard was also aware that some cards were significantly more powerful than others, but as they were mostly rares, there was no expectation that more than one or two copies would even exist in a single playgroup.

Richard was also very secretive about what the cards even were. There were no card lists, rarity wasn't written on the card, there was no official announcement of exactly how many cards there were (for *Limited Edition (Beta)*, they announced that the game had "over 300 cards"). Richard's vision was that players would discover new cards as they played with other people.

Here's a partial list of things that didn't exist when *Magic* first came out:

*   **Formats** (It was originally "use all the cards.")
*   **Limited play** (Richard and the playtesters were aware that the potential existed, but the early sets weren't designed or balanced for Limited play.)
*   **The four-card deck limit** (Cards like Plague Rats were specifically designed assuming you could have as many as you wanted.)
*   **Tournament play** (The DCI would start up in early 1994.)
*   **Modern rules** (The early rules system was a tangled mess, once mocked up as a rat maze in an issue of *The Duelist*—things like the stack wouldn't come about until the *Sixth Edition* rules.)
*   **Legendary cards** (They would premiere in *Legends*.)
*   **Multicolor cards** (They would also premiere in *Legends*.)
*   **Alternate types of mana** (Hybrid, twobrid, Phyrexian mana, snow mana, etc. were years away.)
*   **All the card types** (Interrupt would go away, and planeswalkers and battles were introduced.)
*   **Noncreature subtypes** (Equipment, Vehicles, Sagas, etc. were also many years away.)
*   **Nonevergreen keywords** (Named mechanics were originally things that were always in the game.)
*   **The modern color pie** (The five colors existed, but mechanical consistency took time to establish.)
*   **Much terminology** (Battlefield, exile, dies, etc.)

Second, one of the cornerstones of *Magic* is how the game evolves over time. Because we keep making new cards and how the players make use of the cards changes over time, the game is constantly reinventing itself. A perfect example of this would be the Commander format. It was created by the public and championed by the public. Wizards would eventually start making products for it, and it became the most played tabletop format. That, in turn, required *Magic* to adapt to the format. For instance, both white and red had inherent disadvantages in the format because their strengths were undone by Commander's structure (starting at 40 life, having multiple opponents, etc.). Such things required us to rethink how to design white and red cards and how to create new abilities that stayed true to the philosophy of each color.

This constant evolution is a huge strength of the game. One of my hypotheses about the success of *Magic* is something I call the "Crispy Hash Brown Theory." If you use the metaphor that games are like hash browns, the most exciting time to play a game is the very beginning, because the discovery process of a game is like the crispy outside of a hash brown. However, most games get to a point where players come to understand the nature of the game well enough that they move onto a new phase where they have to start learning what others have learned before them. This usually involves a lot of memorization. In chess, it's memorizing the opening moves. In *Scrabble*, it's learning all the legal two- and three-letter words.

The memorization portion of gaming is usually not as fun as the discovery process. Yes, the inside of the hash brown is still good, but it's not quite as good as the crispy outside. *Magic* is constantly regrowing its outer shell in that as it adapts, the game changes, and so the players are in a constant state of discovery. The crispy outer part keeps growing back. The game, by its very nature, adapts and changes.

Third, when creating something, you make use of what's known as an iterative loop. Here's what it looks like:

1.  You come up with an idea.
2.  You theory craft it, which means you use your experience to think through how best to execute on the idea.
3.  You turn the idea into an actual thing. For a game, that usually means making a game component, or possibly a new rule.
4.  You then experience it how the audience will experience it. For games, this means you playtest it. Often the playtests will involve other people for more perspectives.
5.  You get feedback from the playtest. You then use this feedback to return to the beginning of the loop, coming up with an adapted version of the idea, or maybe a whole new idea, considering what you learned from step four.

Each *Magic* set is made using iterative loops, but you can think of the game itself as being one giant ongoing iterative loop. We make a set. Millions of players play the set and give us feedback. We then use that feedback when making the next set. This means that the technology of designing *Magic* is forever improving as we learn more and more ways to better design it.

We've been making *Magic* for 30 years. That's a lot of iterative loops. The nature of how we design *Magic* changes because the mere act of making it and watching the public play it changes how we design the next set.

So, why have we added more restrictions? Because the nature of what the game is, how it's adapting, and what our iterative loops have taught us have moved us toward wanting more restrictions.

### But *Magic* has been fun for many years, so why the need for more restrictions now?

As I stated above, restrictions have always been a part of *Magic* design. The larger issue is one of where we're using the restrictions and how often. I think the biggest change is that we've become more willing to be blunt about the use of restrictions. In early *Magic*, we made use of a game design technique that I'll call "hiding the vegetables." When you make a game, there's a difference between what makes the game fun for an audience and what the audience appreciates on a surface level. Part of a game designer's job is maximizing the fun while minimizing things that the audience might bristle at. This concept obviously comes from the idea that, as a parent, what your kids need to eat and what they want to eat varies. Sometimes you have to sneak vegetables into other foods.

From a design standpoint, it means you make use of tools that accomplish your task that are less blunt about it. For ease of explanation, I'm going to use the restriction of only using an ability or card once per turn. Symbols are nice because they embody a concept in a way that doesn't have to spell it out in words. They also have the benefit of feeling more engrained in the core of the game. The issue with symbols is that they come at a high comprehension cost, meaning you need to be stingy with how many you use. The fact that tapping got a symbol shows how important this restriction is to the game.

In addition to a tap symbol, there are a bunch of tricks we use to do things once per turn without having to spell them out. Triggered abilities, at least ones that can only trigger once per turn, work well. The most popular are attack triggers, saboteur triggers (when this creature deals combat damage), and beginning-of-step/phase triggers. We also make effects that only functionally work once without stating so. Each activation can undo previous activations, or it creates an effect that doesn't stack. Some activations, mostly on creatures, can kill the creature if activated more than once. +N/-N effects are a good example of this. The point is that there are numerous ways for us to limit things to once a turn without having to say "once a turn."

*Legends* was the first set to give you an ability that restricted its use to once a turn.

![Dream Coat](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=1477&type=card)

Dream Coat is an Aura that grants you an ability to use once per turn. Interestingly, the actual terminology "once each turn" didn't show up until two cards in *Ice Age*.

![Grizzled Wolverine](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=2628&type=card) ![Walking Wall](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=2432&type=card)

These two cards showed a gap that we had. Creatures, at least those without vigilance, need to tap to attack, so if you wanted an ability that worked in combat that you needed to limit, you couldn't use a tap symbol. Neither of these two cards were particularly memorable, though. The card that brought this use front and center to me was the card Rootwalla:

![Rootwalla](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=4786&type=card)

This card came about because Mike Elliott and I independently designed the same card, I think using the same thought pattern. Wouldn't it be cool to have a green creature with a built-in Giant Growth effect. We didn't want it repeated for numerous reasons. One, other colors were "pumping" (i.e., had activated abilities you could use multiple times a turn to increase creatures' power and/or toughness), and we wanted this to feel more green. Two, strategically, it was a much more interesting card if you could only use it once.

I should note that *Tempest* had three cards that did one-time boosts, but Rootwalla has become so iconic that R&D uses it as a term to mean a green creature with a one-time Giant Growth effect.

![Crazed Armodon](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=4754&type=card) ![Plated Rootwalla](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=5201&type=card)

Our thought at the time was "it's okay to use 'once per turn' a little bit."

From there, we started making use of a tool that helped us do something that other tools couldn't. As we had success with this tool, we started using it more. We understood that it wasn't "hiding the vegetables," but we thought the gameplay was good enough to warrant it. Through iteration, we learned different advantages of using it:

**A single-use effect is easier to cost** – When we cost an ability, we have to cost it for its most abuseable use, even if that's what would happen a minority of the time. For example, if the Rootwalla ability wasn't limited, it couldn't cost 1G because of its abuse late game when you have a lot of mana.

**A single-use effect allows us more control when it gets used** – Once, the cost can be set toward the use we want, we can choose a cost that allows it at the time we want. A large part of game design is about trying to incentivize play, so the more tools we have that help push players toward what we feel is the most fun play pattern of the card, the better the gameplay.

**A single-use effect allows us access to larger effects** – If something can be used multiple times, it forces us to make the effect small to allow multiple uses. When we limit the activation, we have the freedom to choose how big we want the effect to be.

**A single-use effect allows access to more abilities** – With this freedom to shape when something happens, it also gives us more freedom to shape what happens. It opens design space.

I'm talking about single-use effects, but the same can be applied to other restrictions. In short, the more the designers have access to controlling when and how something happens, the better designs we can make. Restrictions have gone up over time because we've learned how valuable they are as a tool.

### Does it bother you that some of the new restrictions feel bad to read?

Now we get to the crux of the issue. We're not "hiding the vegetables" as well as we once did. They're a little more in your face. We're doing this consciously because we feel the increase in gameplay quality is worth a little reading discontent, but I am sympathetic to the note that players are responding to the increase of our bluntness when it comes to restrictions.

There are some potential answers to this. One has to do with templating. I've gotten the note many times that players wish they understood the restriction of an ability before they get to the ability. That's what the tap symbol and triggered abilities do. This isn't quite as easy to accomplish as one would hope, as there are many ways we use restrictions and templating is a complicated endeavor, but it is something we're looking at.

Two, the more we concentrate what restrictions we use, the easier it is for players to grok them. The poster child for this issue is first strike. We've found that we often want to use first strike only offensively, but we keep shifting how exactly we say that ("as long as it's your turn, CARDNAME has first strike," "at the beginning of combat, CARDNAME gains first strike," "when CARDNAME attacks, it gains first strike," "as long as CARDNAME is attacking, it has first strike"). We are working to better consolidate when and how we use particular restrictions.

Number three concerns better communication. It's why I recorded the podcast and wrote this article. I think the more players understand the reasoning behind the restrictions and why they lead to better gameplay, the easier it will be to accept them.

Four is familiarity. The more we do something, the more accustomed players get to it. There are things we do that created an uproar when we first did them but that have now become core to the game.

## "Class Dismissed"

That's all my time for today. I hope it's shed some light on why we're using more blunt restrictions. As always, I'm eager to hear your feedback on today's column. You can email me or contact me through any of my social media accounts ([X \[formerly Twitter\]](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week when I start my *Murders at Karlov Manor* card previews.

Until then, may a restriction cause some thought.
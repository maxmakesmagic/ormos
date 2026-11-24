---
id: b4q81fek
kind: article
lang: en
path: /en/articles/card-preview/2017/08-09-vampirism-101
title: Vampirism 101
published: '2017-08-09'
column_slug: card-preview
column: Card Preview
authors:
- slug: bryan-hawley-625cce85
  name: Bryan Hawley
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
    lang_detected: en
    capture_id: 266737
    url: https://magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
    captured_at: '2022-05-23 13:23:01+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
    lang_detected: en
    capture_id: 266737
    url: https://magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
    captured_at: '2022-05-23 13:23:01+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
    lang_detected: en
    capture_id: 266737
    url: https://magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
    captured_at: '2022-05-23 13:23:01+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
    lang_detected: en
    capture_id: 266737
    url: https://magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
    captured_at: '2022-05-23 13:23:01+00'
    rule: url.article_section
sources:
- document_id: b4q81fek
  url: https://magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
  page_key: magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
  lang: en
  template: drupal
  captured_at: '2022-05-23 13:23:01+00'
  capture_id: 266737
  wayback_url: https://web.archive.org/web/20220523132301id_/https://magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: b4q81fek
  capture_id: 266737
  url: https://magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
  wayback_url: https://web.archive.org/web/20220523132301id_/https://magic.wizards.com/en/articles/archive/card-preview/vampirism-101-2017-08-09
  captured_at: '2022-05-23 13:23:01+00'
  template: drupal
  sha256: 9e822e0591de8c9597a96a600a2a1c27767152d3bd2df7a2236148a085193a3f
render_recovery: []
---
Welcome to Vampire Day! As the lead developer of *Commander (2017 Edition)*, I wanted to tell a few of my favorite stories from the development process of the Vampire deck specifically and a bit from the set as a whole. First, though, let me introduce my team! I was extremely happy with all their contributions. In addition to being a team of strong designers, all three were incredibly well-versed in the Commander format across different styles of play.

**Bryan Hawley** (Lead)

![](http://media.wizards.com/2017/images/daily/CP20170809_Hawley.png)

That's me! At the time *Commander 2017* was in design, I was member of development, but with the inception of Play Design, I'm now working on that team. Gavin mentioned in his article earlier this week that he was fresh off lead designing *Archenemy: Nicol Bolas*. Coincidentally, I was fresh off lead developing *Archenemy: Nicol Bolas*! There was a period of about nine months where Gavin and I led design and development respectively of the same products, and Jules Robins was on all our teams.

For *Commander* products, we typically assign one deck to each team member to build, tune, and own. That person is also responsible for telling the lead what types of new designs their deck needs and suggesting cards to fill those roles. I owned Dragons, but as the set lead, I owned the file and was ultimately responsible for all the decks.

* * *

**Jules Robins**

![](http://media.wizards.com/2017/images/daily/CP20170809_Robbins.png)

At the time of this team, Jules was still a relatively recent addition to *Magic* R&D, and he was an incredibly awesome person to have around. He was the carryover from the design team, so aside from his usual contributions in designing sweet cards and helping build and rebuild decks, he was also someone who could speak to the context and the "why" of decisions the design team made. This sort of voice is very helpful because, while development does at times deviate from original intent or revise goals that aren't working out, it's important that we don't do that without realizing we're deviating.

Jules was the master of Vampires, so in addition to today being Vampires Day, you could also call it Jules Day!

* * *

**Glenn Jones**

![](http://media.wizards.com/2017/images/daily/CP20170809_Jones.png)

Glenn is one of our illustrious editors, and especially on this type of team I'm a huge proponent of having an editor on my teams whenever I can get one. Glenn is an avid Commander player and skilled deck builder, and he also has a keen eye for simplicity and clean designs. Aside from his excellent work designing and refining the Wizards deck, I leaned on Glenn heavily to guide me on whether there was a clean implementation of a card that did what I wanted. This type of input is especially valuable in multiplayer-pointed products because often the words needed to describe an effect become so nonsensical that it's not worth pursuing the idea—and knowing that ahead of time keeps designs on a good track throughout.

As a tricksy mage and lover of difficult problems, Glenn was our resident master of Wizards, which was probably the most challenging of the four decks for which to figure out the mechanical identity.

* * *

**Mark Globus**

![](http://media.wizards.com/2017/images/daily/CP20170809_Globus.png)

Mark Globus is a long-time veteran of *Magic* R&D, currently playing the part of a product architect and general-purpose font of wisdom. His day job is leading discussions about the macro-level direction for *Magic*, but he's also an avid Commander player and is particularly good at asking the right questions of design leads to make sure they're thinking about the right things, which is always an incredibly valuable asset to a team.

Throughout development, it was common to hear Mark reply (very enthusiastically), "I AM CAT LORD!" when asked which deck he owned.

# Tag Me In, Coach!

In design and most of the way through development, the eminence mechanic was called "coach." That changed as soon as creative looked at the set and collectively cringed. [Gavin's article](/en/articles/feature/2017/08-08-dragons-dragons-and-cat-dragons) goes into a lot on the design of eminence, but I wanted to talk a bit about the execution side of the mechanic.

Early on, I expanded on the design pillars for eminence that Gavin had come to, and came to these:

1.  Coaches should be deck-specific and care about cards of their tribe.
2.  Coaches should fill weaknesses in their tribes.
3.  Some of the power of the coach needs to come from them being cast.

Our main goal with this mechanic was to give these tribes a way to work cohesively in Commander in a way that was fun for the format. The biggest challenge is that there's no way to interact with cards that affect the game from the command zone, so we needed to be very careful with the types of effects we put on them.

The first requirement, that they should be deck-specific, is to address two issues. The first is to avoid cards like [Oloro, Ageless Ascetic](https://web.archive.org/web/20170809000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oloro%2C+Ageless+Ascetic) that shape the game and add significant power to their decks without being interactable. The second is that by caring about actually having cards of their tribes in your deck, it feels more like the Vampires or Wizards are doing the work as opposed to the commander. The feeling we aimed for was that the commander would enable the tribe, not that the tribe enabled the commander.

The second requirement was born from the overarching goal that this product supports tribal in a fun and satisfying way. For each tribe, we asked ourselves "What is this tribe missing?" and tried to fill on those weaknesses so that we'd wind up with well-rounded decks rather than one-trick ponies that either win or lose depending on matchup or variance in their draws.

The third goal came mostly from playing with versions of the mechanic where it wasn't true, and it just didn't feel right. Commanders on the battlefield are fun, and it was easy to come up with designs where you'd never want to cast them. We didn't have any particular goal for how often the commanders were cast, just that they were somewhat appealing to actually get into play.

Starting from there, it was just a long slew of designs, redesigns, tweaks, and tuning to get us to something like this:

## Click to reveal

![](http://media.wizards.com/2017/c17/en_41iZZBXhco.png)

 

Early on in design, Gavin worked with creative to figure out which characters would be awesome to show off here, and Edgar Markov was high on that list. Fortunately, as the progenitor of Vampires on Innistrad, he also fit perfectly with the mechanical needs of the Vampire deck!

One of the things we noticed relatively early on was that Vampires have had a wide variety of different strategies they could pursue, but they all pointed the deck toward being somewhat aggressive and cared about having lots of Vampires in play at the same time. Cards like [Kalastria Highborn](https://web.archive.org/web/20170809000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kalastria+Highborn), [Captivating Vampire](https://web.archive.org/web/20170809000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captivating+Vampire), and [Malakir Bloodwitch](https://web.archive.org/web/20170809000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Malakir+Bloodwitch) can have a hard time in a format full of sweepers where you might need to rebuild over and over, so we were looking for an eminence ability that would give some fuel for that type of effect.

After settling on this pattern for coaches, where they had two abilities on the battlefield and one in the command zone, Edgar was one of the first designs we came up with. Other than tweaking numbers, he didn't substantially change after that point. He's an excellent example of why we often talk about setting our goals for cards and mechanics first, then designing toward them. Once we knew what we were looking for and had a design that fit all our goals, we just needed to test and verify that the design was working out, but it was pretty smooth sailing once we knew the shape of the problem.

# Fitting a Round Cycle into a Square Set

*Commander 2017* is the first *Commander* product to feature four decks instead of five. We're moving to this model for a number of reasons, from narrowing our focus to questioning the additional value of the fifth deck to players being relatively small. It did, though, pose something of a challenge from a design perspective. It was important to us that each deck have the same number of new cards of various rarities, but we also wanted to have cycles of cards with similar effects when we came up with cool ideas for them. We explored a number of implementations from broken cycles to only multicolor cycles, but the answer we came to was just to give one deck two members of a cycle. It took a bit of wiggling the set skeleton—which is our term for a spreadsheet that lays out the set size, distribution of rarities, colors, slots dedicated to cycles, and so on that defines what we design toward—but it allowed us to do awesome things like this:

## Click to reveal

![](http://media.wizards.com/2017/c17/en_6Wodiy98KL.png)![](http://media.wizards.com/2017/c17/en_KSenKoRxe0.png)![](http://media.wizards.com/2017/c17/en_pyG4cDyMhX.png)

![](http://media.wizards.com/2017/c17/en_lkPgKvZSim.png)![](http://media.wizards.com/2017/c17/en_dHoqKl8Nuw.png)

 

These cards went through a wild ride on their way to these designs. It all started with an individual card that we loved that put bounties on your opponents to create a little minigame where people would incentivize their opponents to attack each other. We tried expanding that out into a full cycle and got a few designs we liked but a few that just were horribly complicated and impossible to keep track of. We narrowed down the effect on those cards, but after some refining, they felt like more complicated curses without many redeeming features, so we just turned them into Curses with a novel twist. Rather than just the player triggering the curse getting rewarded, the owner of the curse does as well!

# Before I Vanish in Smoke

Since I was the lead developer of the set, Blake (our content manager) is particularly vulnerable to puppy-dog eyes, and this card is in the Vampire deck, I have a special bonus preview card I get to sneak in at the end! This is a card that Gavin came up with early on to fill a hole in the file, and it's one of the rare cases where a card stays almost exactly the same through the entire process. I didn't even change the numbers; I loved it as soon as I saw it and the only thing to solve was how it was going to actually work.

It started like this:

Vanish in Smoke  
 2W  
 Instant  
 Exile all permanents you control. At the beginning of your next end step, return them all to the battlefield tapped. You gain protection from everything until end of turn.  
 Exile CARDNAME

And became this:

## Click to reveal

![](http://media.wizards.com/2017/c17/en_kkHomijBXx.png)

 

That's right. It's been just over 20 years since the last time we printed a card with phasing, but it's back. Enjoy it, but don't get used to it. It's every inch the same bizarre and not-very-fun mechanic it always was, but it did the job here.

# Phasing? Really?

So how'd we get to phasing?

Commander, and our other multiplayer-focused products, often have cards where there's something specific the designer wants to do but prioritizes a grokkable, intuitive card over having the edge cases work one specific way or another. There's a lot of back and forth with editing where editing tries to sound out what's important to the designer and what isn't to come up with a card that works the way people expect but preserves the intent of the design. Often the design changes to accommodate that to get 100% of the functionality, the card would need horrifying words nobody should ever read, but we can get 95% of the way there and have a pretty clean, appealing card.

Especially in cases where we need to handle situations with three-plus players making decisions or interacting with an effect in some way, it can get really complicated, and we often tweak designs or just throw them out if we can't come up with a way to express what we want the card to do.

In the case of this card, the conversation went something like this (with minor liberties on details):

Editor: What's important to you about how this card works?

Me: You're out of the game for a little while and nobody can mess with you. Also, that you can say "I'm out!" in an overly dramatic voice.

Editor: Is it important that it triggers [enters/leaves-the-battlefield](/en/articles/play-design/2017/07-14-the-m-files-hour-of-devastation-part-1#enters-the-battlefield-effects) abilities?

Me: No, it's actually probably better if it doesn't because that's a lot of extra power that's not key to what we're doing and we'd probably need to charge more for it, which I don't want to do.

Editor: How much do you care about things like [Exsanguinate](https://web.archive.org/web/20170809000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exsanguinate)?

Me: It'd be great if [Exsanguinate](https://web.archive.org/web/20170809000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exsanguinate) worked the same as [Earthquake](https://web.archive.org/web/20170809000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earthquake), but not vital.

Editor: How about [Fact or Fiction](https://web.archive.org/web/20170809000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fact+or+Fiction)?

Me: Whatever makes the cleanest card.

(This continues for a while . . .)

Editor: So basically you want you and everything you own to stop existing for a little while.

Me: Yeah.

Editor: So, that's phasing.

Me: Sounds great.

A week or so later, Aaron Forsythe enters the pit:

Aaron: Who put a card with phasing in their set?

Me: That'd be me.

Aaron, chuckling: Well, carry on then.

And that's how we did it.

I hope you enjoy vampirizing people as much as we did!

—Bryan
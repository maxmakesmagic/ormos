---
id: 8g3deb6d
kind: article
lang: en
path: /en/articles/makingmagic/2014/04-14-the-incredible-i-journey-i-part-2
title: The Incredible <i>Journey</i>, Part 2
published: '2014-04-14'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
    lang_detected: en
    capture_id: 221142
    url: https://magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
    captured_at: '2024-05-18 03:36:38+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
    lang_detected: en
    capture_id: 221142
    url: https://magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
    captured_at: '2024-05-18 03:36:38+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
    lang_detected: en
    capture_id: 221142
    url: https://magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
    captured_at: '2024-05-18 03:36:38+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
    lang_detected: en
    capture_id: 221142
    url: https://magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
    captured_at: '2024-05-18 03:36:38+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 8g3deb6d
  url: https://magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
  page_key: magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:36:38+00'
  capture_id: 221142
  wayback_url: https://web.archive.org/web/20240518033638id_/https://magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 8g3deb6d
  capture_id: 221142
  url: https://magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
  wayback_url: https://web.archive.org/web/20240518033638id_/https://magic.wizards.com/en/news/making-magic/incredible-journey-part-2-2014-04-14-0
  captured_at: '2024-05-18 03:36:38+00'
  template: contentful
  sha256: 0b0c2cbbe2b948c37d18156953863645bd7db4e41c44b21f9d8c280d87e733bc
render_recovery: []
---
Welcome to the second preview week for *Journey into Nyx*. As the "Part 2" in the tile might give away, this is the second (and final) article about the design of *Journey into Nyx*. Before I get to the second half of the story (along with a fun new preview card), I thought I would quickly recap [the first half](/en/articles/makingmagic/2014/04-07-the-incredible-journey-part-1) in a small play:

### The Gods Must Be Crazy

**(...In Love with How Awesome Their Theme Is)**  
A Very Short One-Act Play

**Design Team Member #1:** We need to design *Journey into Nyx*.

**Design Team Member #2:** The focus is on the gods versus the denizens of Theros.

**Design Team Member #3:** Let's start by focusing on the gods' side.

**Design Team Member #4:** Examining everything it seems clear that the gods are intrinsically linked to enchantments.

**Design Team Member #5:** Then let's make an enchantment-themed mechanic, something "enchantment matters" since we've been saving that for this last set.

**Design Team Member #1:** How about enchantmentfall *a la* landfall?

**Design Team Member #2:** Sure, but let's just do it on enchantments.

**Design Team Member #3:** Done.

And scene.

If you only looked at the gods' portion of the design, you might think that *Journey into Nyx*'s design was seamless and easy and there was no drama (well, other than that brilliantly constructed very short one-act play). It turns out there was another whole section, the denizen side of the conflict, and that part didn't go quite as easily. In fact, it's a much longer story and the focus of today's article. I will walk you through it all and even show off a new preview card with the other new mechanic in the set.

### Mortal Combat

Let me start by defining what I mean when I say the denizens of the world. Theros is a world inspired by Greek mythology. Obviously a focal point was the gods, but in addition to the gods, there was an entire world crafted. The denizens are everyone, minus the gods and the creations of the gods, who live on Theros. In design-speak, they were the Heroes and Monsters of the Gods, Heroes, and Monsters theme of *Theros*.

The gods' side was much easier to theme because the design of the block already gave it a strong definition through the use of enchantments. The denizen side was a little less focused. After studying the heroes and monsters, one thing did stand out. The hero mechanic was heroic, while the monster mechanics were monstrosity and tribute. All three had something in common—+1/+1 counters. What if *Journey into Nyx* had a mechanic that worked well with +1/+1 counters, such that it would help tie the other side together?

This idea came up during advanced design and the team started exploring what one could do to reward players for playing +1/+1 counters. Usually, when you are trying to figure something like this out, one of the things you do is look to the past to see if there is an existing mechanic already playing in a similar space. And luckily there was—proliferate.

![Thrummingbird](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thrummingbird)

 

For those who might not have played during *Scars of Mirrodin* block, proliferate was a mechanic that allowed its caster to choose any number of players or permanents with counters and add one more counter (of the same kind they already had) to each. The advanced planning team was interested in finding a similar but slightly different approach. Their inspiration came from a card I had made in *Dragon's Maze*.

![Vorel of the Hull Clade](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vorel+of+the+Hull+Clade)

 

The Simic had a strong counter theme in *Return to Ravnica* block, and I do so love doubling things, so I gave the Simic Maze Runner a counter-doubling ability. That felt like a riff on proliferate, but instead of making everything a little bigger, it made one thing a lot bigger. Vorel only affected artifacts, creatures, and lands, which worked perfectly because affecting Planeswalkers would cause developmental concerns and affecting enchantments would not separate it enough from the gods' side of the quarrel. We dubbed the ability enhance and tagged it as a potential new mechanic for *Journey into Nyx*.

When Journey design started up, we spent a little time talking about an "enchantment matters" mechanic but chose to leave enhance alone and just put it into the set. Erik Lauer, the development representative on the design team, let us know that a mechanic that doubles things was a little risky, but we knew that we could always dial back the effect to adding a set number of counters rather than doubling. We prefer to let design start with an aggressive approach because we'd rather get a feel for what the more extreme version would play like. Sometimes, the thing that seems a little crazy turns out not to be so bad. Other times, it proves to be exactly what you think it might, but that's when you can scale back. The big thing about design is not to let potential risk keep you from exploring the ideal version.

Because we only wanted to have two new mechanics, we filled in the monster space with individual +1/+1-countering cards so the new mechanic would be able to interact with them. We also chose to push the +1/+1-counter gaining in heroic to all five colors rather than keep it just in white and green, as it had mostly been done in *Theros* and *Born of the Gods*.

And so, in early design, we played with enhance and it was fun. Doubling things is exciting and we found that big, crazy things would often happen when we played. At first, it seemed like maybe it would work out, but playtesting soon revealed exactly what Erik had warned about the first time we'd talked about the mechanic. Doubling was safe much of the time, but when it wasn't, it really wasn't, so we dialed back the mechanic. The next version of the mechanic had a number, such as enhance 2 or enhance 3. When you played it on an artifact, creature, or land with counters, it would add that many counters to the permanent. At first, we had a lot of enhance 3 but with playtesting most of those dropped to enhance 2.

We talked about enhance 1, but at that point we were just making a mechanic strictly weaker than proliferate. This, of course, led us to discuss the idea that maybe we should just use proliferate, but that mechanic still was relatively recent. The design team wasn't quite sure what to do. This, by the way, was around the time the set was about to be handed off from design to development.

### Let's See What Develops

During the tail end of "devign" (the space between design and development when design still has control of the file but starts getting feedback from the development team), the design team realized that enhance wasn't going to work, so we started trying to find a replacement. Up until that time, we thought of +1/+1 counters as being the thing to link the heroes and monsters together, but as we examined the problem we realized we needed to try a different approach.

![](https://i.ormos.uk/85/a8/85a831d635da8e7fa3f36e9cc27e3223c9aae021bd6bc5fc4e86fa067b3f4ebb.jpg)

Art by [Chase Stone](https://web.archive.org/web/20140414000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Chase%20Stone%22%5D)

Instead of looking to see what mechanically connected the denizens we started thinking about what linked them together flavorfully. The gods were obviously very centered around enchantments, as those represented the touch of the gods upon the world. The denizens, on the other hand, seemed very focus on building themselves up. The +1/+1 counters were one way to build up but not the only way (Auras, for instance, were another way). As we examined more, we came to the conclusion that the mechanical center of the denizens was the heroic mechanic. Perhaps there was a different way to help enable it.

The design team wrote all the issues on the board:

*   We wanted a mechanic that worked well with heroic.
*   We wanted a mechanic that could go on instants and sorceries, as the previous block mechanics we were carrying over were almost all on creatures.
*   It would be nice if the mechanic helped players use their extra mana, as we like to have a mana-sink mechanic in every set.

With all the restrictions in place, we got creative and came up with a new mechanic called resupply. Here's how it worked.

> Ajani's Presence  
> W  
> Instant  
> Target creature gets +2/+2 until end of turn.  
> Resupply 2 *(Whenever a creature enters the battlefield under your control, you may pay 2. If you do, return CARDNAME from your graveyard to your hand.)*

It was at this point that devign ended, so we officially handed over the file to development. Dave Humpherys and his team (Ian Duke, Tom Jenkot, Erik Lauer, and Ken Nagle) did a bunch of playtests with resupply. While it was accomplishing a lot of the tasks it was created to accomplish, it turned out to be a little more complex than they liked. It also wasn't doing a great job of encouraging players to play a number of heroic cards in their deck (more on this in a minute).

The note we kept getting back from development was that they were hoping for a mechanic that played a little more like buyback, something else that would allow players to have something to do with their extra mana and combo well with heroic. One day, the development team decided that they knew a good mechanic like buyback—buyback.

![](https://i.ormos.uk/5f/41/5f414db9b5b03abba5608a46d868a3dab80650f778d15a1b8b1ff72bb6e76bec.jpg)

For those unaware of the buyback mechanic, let me give you a quick history lesson. During *Tempest* design, Richard Garfield came up with a few spells that allowed you to pay extra mana to have the spell go back to your hand when it resolved instead of going to the graveyard. I liked the mechanic so much that I made the call that it was going to be one of our two major keyword mechanics (the other was shadow).

Buyback proved to be both powerful and popular (those two are often interlinked) but it had some issues, the biggest of which was the repetition-of-play problem. Once you were able to pay for a spell with buyback, you tended to cast the same spell turn after turn. The other problem was that there weren't a lot of answers to buyback, especially not ones the average player easily understood. (The best way to stop a buyback spell, for example, was to fizzle the spell by removing the target. Yes, killing your own creatures was often the key to stopping buyback. Not something lower-experienced players were ever going to stumble across.)

Development brought buyback into the file with their eyes wide open. They knew it was problematic but they felt it did such a good job of buffing heroic creatures that it was worth trying to make it work. They did a lot of experimenting with buyback. They limited what kinds of spells had buyback. They tried to build in limitations. They tried to design some new answers. In the end, though, it wasn't quite working.

### Time To Rally

Dave Humpherys was taking paternity leave for the birth of his first child so he handed the reins over to Erik Lauer to lead the set while he was away. Erik knew that buyback wasn't working, so while Dave was off, he decided to go and try to find its replacement. Erik had the same restrictions the design team had worked with and came up with another option, a mechanic he called rally. Here was the original version:

> Ajani's Presence  
> W  
> Instant  
> Rally 2W *(You may pay an additional 2W any number of times as you cast this spell.)* Target creature gets +2/+2 until end of turn. For each time you rallied, another target creature gets +2/+2 until end of turn.

[Rally](https://web.archive.org/web/20140414000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rally) basically allows a spell to get additional targets by paying extra mana. The key is that it only allows you to target each creature once. This was important, because it was Erik's goal to find a way to make this mechanic encourage playing not with a single heroic creature, which both resupply and buyback had done, but rather play with a team of heroic creatures. This would help encourage players using the denizens to be able "go wide" and treat heroic a little more like a linear mechanic.

Erik played with rally and found that it was doing what he wanted. Dave returned to learn that Erik had completely swapped out buyback for a new mechanic but he liked what he saw and so rally (later called strive) stayed in the set.

I have a few more things in the set to talk about, but before I move on from strive, I do have one last thing to do. My preview card today is a strive card and a fun one at that, so let me take a moment to introduce you all to Twinflame.

![](https://i.ormos.uk/9d/72/9d722e25d123bf10f58422c92635fc6036d255891c90d6b59a3be61c4a083b1c.jpg)

I was very excited that I got to have this card as my preview because it's the kind of card I love as a player, as it gets your mind racing, trying to think of all the fun things you can do with it. I hope you all have a blast playing with it.

### But Wait, There's More

I've talked about constellation and the "enchantment matters" theme. I've talked about strive and the denizens of the world. But that's not all. There are a few things in *Journey into Nyx* left to talk about.

<table><tbody><tr><td><img src="https://i.ormos.uk/ce/1d/ce1db5ba7293188cb8f48d889f7d626d1b4381a2b82fde6fc44c0274ec93f79d.jpg"></td><td><img src="https://i.ormos.uk/89/b4/89b4a06c3abeee8dee9875b72908d2d3177582bf37d4cda8dd57e3b5e5b78ac7.jpg"></td></tr></tbody></table>

### Oh Gods

*Journey into Nyx* has the third and final cycle of gods, this time the enemy-colored ones. We spent some time considering if we wanted the enemy-colored gods to be different than the ally-colored gods, but in the end we decided we liked the basic design and kept the formula the same. As with the ally-colored gods, the enemy-colored gods do not have an artifact enchantment weapon cycle.

### I'll Second That Devotion

Other than the five gods, you will notice that there is no devotion in *Journey into Nyx*. The reason for this stems back to why devotion was put into the block in the first place. As the block evolves, the denizens of the world start losing faith in the gods and this discontent leads to the conflict in the set. Knowing this was how the block was going to evolve, I felt it was important to find a way to show the break between the denizens and their gods. To do this, I needed a way to show the connection between the two.

That's where the idea to do devotion came from. We wanted a mechanic that played up the tie between the gods and the denizens. The chroma mechanic from *Eventide* seemed like a perfect fit. This meant, though, that as the block evolved, devotion would have to trail off as the denizens started questioning their gods. Because we knew that players would have devotion decks, we did make an effort to include a few permanents with mana costs that would play well in them.

### Monstrous Inc.

For most of Journey intoNyx's design, the plan was to make one-of monsters designs that made different uses of +1/+1 counters. We would then use the enhance mechanic to double their counters. As the mechanic shifted to resupply to buyback to strive, it became clear that there was less focus on what the monsters were going to do, mechanically. Dave Humpherys and his development team realized they needed to do something to tie the monsters together.

![](https://i.ormos.uk/fd/5d/fd5dce984382f3aee1f7a52e8fae6eb2b7a9be713a28335821ccb3d43c0b6313.jpg)

Hydra Broodmaster | Art by [Steve Prescott](https://web.archive.org/web/20140414000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Steve%20Prescott%22%5D)

They didn't want to make another new mechanic, as the set already had two, yet they really wanted the monsters to have some cohesion. Then one day, somebody innocently asked, "How about monstrous?" We had removed it from *Born of the Gods* to make room for tribute, but the mechanic still had plenty of design space left. The five mechanics of *Return to Ravnica* went away for the second set and then all returned in the third set. What if monstrous did the same thing?

The team started designing new monstrous cards and the mechanic fit right back in, as it had in *Theros*. And that is why monstrous is back.

### Enchanted

Here's something that has not yet appeared in *Theros* block but premieres in *Journey into Nyx*—noncreature, non-Aura enchantments. Yes, Journey of the Nyx introduces not just an "enchantment matters" theme but also plain old enchantments. There had been a lot of talk of their absence in *Theros* and *Born of the Gods*. The reasons were simple. There was a lot going on with enchantment creatures and it ate up all the available space. *Journey into Nyx*, though, needed a certain threshold of enchantments for the "enchantment matters" theme to work, so finally, there was some space for some good old basic enchantments.

### Enjoy the *Journey*

As you can see there is a lot for you all to explore at the Prerelease [next weekend](/en/articles/event-coverage/undated/magic-the-gathering-prereleases-3). We tried hard for *Journey into Nyx* to supplement what came before it while also adding a few new twists. I hope you enjoy it and I am eager to hear your feedback on the set. Drop me an email through the link below, write a post in this article's thread, or just talk to me through any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro#)).

Join me next week for some card-by-card design stories from *Journey into Nyx*.

Until then, may your Journey be a pleasant one.

 

* * *

 

### "Drive to Work #112—1998"

My first podcast today is another in my series "20 Years in 20 Podcasts." Today is all about the year 1998.

### "Drive to Work #113—A Day in the Life"

One of the most common questions I get is, "What is an average day in R&D like?" For my second podcast today, I answer that question.

 

 

*   [**Episode 113**](https://media.ormos.uk/e2/70/e270e00033927a7c50cd4174c481484105e76f9a61d2af716064866fcce00efe.mp3) : *Day in the Life* (14.7 MB)
*   [**Episode 112**](https://media.ormos.uk/fc/3e/fc3ebcd61496483f6caab03107fc490845ff858ba41d11ecc1ce6f73faa95cb7.mp3) : *1998* (13.3 MB)
*   [**Episode 111**](https://media.ormos.uk/03/b0/03b0e447f681f0eb27f8cc8f7ab109cfd4215acf91440dab08f93475765758a5.mp3) : *Judgment, Part 3* (13.6 MB)
*   [**Episode 110**](https://media.ormos.uk/76/cc/76cc57798bd37fb99fdd278a235891a0b63ac6c364a0f9f08486cd379e6c25d4.mp3) : *Judgment, Part 2* (14.3 MB)
*   [**Episode 109**](https://media.ormos.uk/a7/d2/a7d288cf216a4307d726b64477796f957717d60e64f1a5992962f1a278465caa.mp3) : *Judgment, Part 1* (13.1 MB)  

*   [**Complete Drive To Work Podcast Archive**](/en/articles/makingmagic/undated/drive-to-work-podcast-archive)

 

 
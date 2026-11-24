---
id: 1yb4szb4
kind: article
lang: en
path: /en/articles/makingmagic/2023/06-19-lessons-learned-part-4
title: Lessons Learned, Part 4
published: '2023-06-19'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-4
    lang_detected: en
    capture_id: 222555
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-4
    captured_at: '2024-05-18 01:21:52+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-4
    lang_detected: en
    capture_id: 222555
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-4
    captured_at: '2024-05-18 01:21:52+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-4
    lang_detected: en
    capture_id: 222555
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-4
    captured_at: '2024-05-18 01:21:52+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-4
    lang_detected: en
    capture_id: 222555
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-4
    captured_at: '2024-05-18 01:21:52+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 1yb4szb4
  url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-4
  page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-4
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:21:52+00'
  capture_id: 222555
  wayback_url: https://web.archive.org/web/20240518012152id_/https://magic.wizards.com/en/news/making-magic/lessons-learned-part-4
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 1yb4szb4
  capture_id: 222555
  url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-4
  wayback_url: https://web.archive.org/web/20240518012152id_/https://magic.wizards.com/en/news/making-magic/lessons-learned-part-4
  captured_at: '2024-05-18 01:21:52+00'
  template: contentful
  sha256: e1bec7c57e4bab41698e14ade4e9742e7fd6dc7dc3d0ea56778ee74616547c50
render_recovery:
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/35c7d774/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/a4d5bc04/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/da6b12ab/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/532ad11f/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/9fd43405/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
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
In my ongoing "Lessons Learned" series, I walk through every set for which I've led or co-led design and talk about what I learned. Here are my previous three articles:

*   [Part 1](/en/articles/makingmagic/2023/03-14-lessons-learned-part-1)
*   [Part 2](/en/articles/makingmagic/2023/03-20-lessons-learned-part-2)
*   [Part 3](/en/articles/makingmagic/2023/05-22-lessons-learned-part-3)

Last time, I got through original *Theros*, which means I'm up to *Khans of Tarkir*.

## *Khans of Tarkir*

**Lesson: "Let the set become what it wants to become."**

For many years, *Magic* had what we called blocks. The first set in the *Magic* "year" would come out in September or October and be a large set. In January or February, we'd have a small set that took place on the same plane and made use of the mechanics from the large set that preceded it. Early on, this small set wouldn't add any new named mechanics, but that would change. Finally, in April or May, there would be a third set, also small. It, too, would be set on the same plane as the large set and make use of the mechanics from the sets before it. All the sets would be drafted together, though the order they were drafted in would change.

We continued to play around with this structure. The *Lorwyn*–*Shadowmoor* block had four sets that made up two mini-blocks that were each one large set and one small set. Original *Zendikar* block was large-small-large, the last set meant to stand alone. The *Scars of Mirrodin* block had its third set more medium size than small. Original *Innistrad* block copied *Zendikar* block, except there were a little bit of mechanics stretched across the full block. *Return to Ravnica* block went large-large-small. This brings us to *Khans of Tarkir* block. It was scheduled to be a large-small-large set where the third set would deviate and be drafted by itself, but I asked if we could do something different.

My plan was to have the middle small set draft with each large set. This meant when the first large set came out, the draft would be three boosters of that. Then, you'd draft with two boosters of the larger sets (the first and third sets) and one pack of the smaller middle set. Exploratory design was all about figuring out how to make that flavorfully make sense.

In the end, we chose a time-travel theme. This was Tarkir, home to Sarkhan Vol. It was a plane once lush with dragons that had since been eradicated by the warlord clans. Sarkhan would travel back to the past, represented by the second small set to change history and save the dragons. Once he did, the third large set would represent the new timeline where dragons thrive. Each way of drafting would represent a different timeline.

When I set out to make *Khans of Tarkir*, I knew the set was going to be a faction plane with some number of clans. To make it feel different, I chose to have four clans. Originally, two of the clans had two colors, while the others had three colors, representing each color twice. (While it wouldn't get used in *Khans of Tarkir*, it did get repurposed for original *Ixalan*. More on that below.) A few months into design, Brady Dommermuth, who ran the Creative team, came to me to say that his team had a fifth clan they really liked and wanted to include. (To keep people from having to bug me on social media—it was Sultai).

The interesting thing was that I knew what was going to happen if I made the change. I'd been making *Magic* sets long enough that I could see where inertia was going to take us. Five factions would heavily pull us toward having each faction be the same number of colors. From there, I would have five choices:

*   Monocolor
*   Ally two-color
*   Enemy two-color
*   Arc three-color (a color and its two allies)
*   Wedge three-color (a color and its two enemies)

(Four-color wasn't a viable choice as it's structurally too hard to make.)

We'd done four of these before. The fifth, wedge three-color, was something players had been asking about forever. The lesson here is not to fight inertia. Sets will often want to go in a certain direction. Let them. Sometimes the easiest path won't be the right call, but it's always the right choice to examine and understand it. An important part of any set is that it matches player intuition, that way, it delivers on what they expect. That's not to say you can never subvert expectations, but it should be done with purpose and cause. Most of the time, delivering what players expect is the right call.

For *Khans of Tarkir*, it pushed the set in a very different direction than we had originally planned, but looking back, doing so was clearly the right call.

## *Battle for Zendikar*

**Lesson: "There are ideas that don't make a good *Magic* set."**

When original *Zendikar* block was in the earliest stages of being planned, the first large set and the first small set were going to be on Zendikar, and the last large set was going to be on its own plane. The reason for this was the last set was going to have completely different mechanics, so we felt that justified a change in location. The Creative team, at the time, had limited resources, so they pitched the idea that maybe something big enough happens on Zendikar that it justifies the third set being completely different.

That big "third act" event ended up being the release of the Eldrazi. The set mostly focused on them being out of their prison, and no time about how this affected Zendikar. We'd inadvertently created a giant cliffhanger (pun intended). So, when we came back, I felt obligated to pick up the story where we left it. The Eldrazi were free. What was the impact on the plane?

This resulted in the return to Zendikar being radically different from our first visit. The Eldrazi, creatures that hadn't even appeared in the first two sets, were now a huge percentage of the creatures in the set. That meant we had to dedicate significant mechanical resources defining what the Eldrazi were. To make matters extra difficult, many of our choices for *Rise of the Eldrazi* were unpopular, forcing us to find new answers. We then had to spend another chunk of mechanical resources referencing the war. The result of all this is that we spent a lot less time doing the things that had mechanically made Zendikar popular the first time we'd been there.

In my last "[Lessons Learned](/en/articles/makingmagic/2023/05-22-lessons-learned-part-3)" article, I talked about my experiences making *Scars of Mirrodin* block. I was lost in its design until I realized I was making the wrong set. *Battle for Zendikar* is kind of the same story with a less happy outcome. I didn't figure out I was making the wrong set until after it was too late to change it. In hindsight, what I wish I'd done was find a way to tell the story of Zendikar where the Eldrazi played a smaller role, or maybe no role. There needed to be consequences for the Eldrazi having been freed, but it didn't need to be an all-out war against incomprehensible giant alien beings. It just didn't lead us to a place where we were doing our best designs.

That's the lesson of *Battle for Zendikar*. The key to making a good *Magic* set is making sure you're setting yourself up to do so. Whenever I start making a set now, I always ask myself: "Does this idea have the component pieces to make a compelling *Magic* set?" And if not, I must figure out why and change it to reflect that issue. One of the keys to creating an outstanding *Magic* set is making sure you're setting yourself up for success, that you're lining things up that would make fun cards and mechanics and themes. One of the biggest obstacles a designer can face is not taking the time to ensure what is being asked of them can be done well.

## *Kaladesh*

**Lesson: "Every mechanic can find a home."**

This story begins in original *Mirrodin* design. We were looking for artifacts from the past to inspire new artifact designs, as Mirrodin was mechanically an artifact-themed block. One of the ones I chose was from *Homelands*:

![Serrated Arrows](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=2909&type=card)

I'd always enjoyed that Serrated Arrows got three uses. It seemed like a neat resource, so I made a bunch of artifact designs that came with charge counters. Then it dawned on me: It might be fun if a card with a charge counter could make use of charge counters from other cards. The charges on one artifact could be used on itself or another artifact. We advanced this execution to its natural end-point and ended up with counters that you, the player, got and could spend however you wished. We dubbed this new mechanic energy.

When I handed off my design file to development, I got a note back from Bill Rose, the head designer at the time, which said there was too much going on in the set. Energy was the least interconnected mechanic, so I just reverted to the charge-counter versions of the cards. I liked energy, though, so I wanted to find it a home. I put it aside, knowing that we'd make more *Magic* sets and I'd find a place for it one day.

*Kaladesh* would come out thirteen years after *Mirrodin*. During that time, I'd looked to find a home for energy, but it was never a perfect fit. That is, until *Kaladesh*. It was a steampunk set with an artifact theme that played into invention. It was obvious from the very first day of exploratory design that it was an ideal fit. So much so, that the Creative team did a lot of the worldbuilding around it. The lesson here is that *Magic* is a hungry monster and that good ideas will eventually find a home. We shouldn't push mechanics where they don't belong but rather take a long-range approach. If we make something good, there will eventually be a home for it. We must be patient. I find this an especially hard lesson for younger designers. The desire to put the cool thing you just made into the latest set is strong, but it doesn't lead to the best *Magic* design.

I do want to point out that I co-led *Kaladesh* design with Shawn Main. This was the beginning of the two-set block period, and I would co-lead each large set along with another designer. I would start the design and hand over the reins midway through.

## *Amonkhet*

**Lesson: "Nuance is tricky."** 

I co-led *Amonkhet* with Ethan Fleischer. We'd talked about doing an Egyptian plane for a long time (it was the runner-up theme for our first top-down block, *Champions of Kamigawa*). For story reasons, the ancient Egypt-inspired set got very entwined with the character of Nicol Bolas. In the story, Bolas needed an army for his plans to steal the sparks from a lot of Planeswalkers (i.e., War of the Spark), and Amonkhet was the place where he did this. Bolas had positioned himself as the head god and created a series of challenges that resulted in him creating an elite zombie army, known as the Eternals.

When building Amonkhet, we wanted the plane to have a sense of ancient Egypt and an influence of Bolas. We used a feeling of dissonance to achieve this. Dissonance is when discomfort is created because what you see doesn't match what you feel. This sense of dissonance came from the story. The Gatewatch (Gideon, Jace, Liliana, Chandra, and Nissa) show up to stop Nicol Bolas in his plans only to find a plane that seems enamored of him. On the surface, everything seems perfect, but the Gatewatch can tell something's wrong. That's the dissonance we were trying to capture.

The idea we came up with was that the creative of the plane would be shiny and positive, indicated through art, names, and flavor text, but the mechanics would suggest the opposite. For example, we had a -1/-1 counter theme, which by its nature feels harsh. We had a graveyard theme (with embalm and aftermath). We had a mechanic called exert, which is all about pushing yourself to gain an extra ability but at the cost of not untapping. The goal was the play of the game would feel different than the creative and that would create a sense of dissonance.

The lesson here is that we didn't realize the problem of not being loud about our theme. Usually, whatever we do, we lean into that theme with the creative so that the creative and the mechanics are telling the same story. Since this is a tricky medium, we're often blunt when doing this. In *Amonkhet*, we weren't as blunt as normal, and what we found was the message was more muddled than we'd hoped. While it worked for fans invested in the story, it was a miss for most players. It taught us that we must be careful where and how we use nuance. Not that there isn't a place for it, but not as the main theme of a set.

## *Ixalan*

**Lesson: "Sets need glue"**

Before I jump into the story, I want to note that I co-led this set with Ken Nagle, again doing the first half and handing over the reins for the second half.

Part of the process of choosing what sets to do is looking ahead and planning out the next two to three years of sets. When we do that, I'm responsible for choosing a rough estimation of how I think each set will function mechanically. It's not yet at the point where we're figuring out mechanics. I'm just spit-balling on a larger mechanical theme. For *Ixalan*, the idea for the plane came from the Creative team, and it originally was a two-sided conflict (between the invading vampires and the natives of the plane).

One of the ideas I was interested in was the idea of a mechanical fight for resources. In *Vampire: The Eternal Struggle* (another trading card game made by Wizards of the Coast under Richard Garfield), there was a mechanic called "the edge" that players fought over. I liked the idea of *Magic* having a plane that fought over a resource like this. To help this theme and make the plane feel a bit different, I asked the Creative team to add a third group to the mix, which ended up being pirates.

During the design for *Conspiracy: Take the Crown*, Shawn Main, the set's lead designer, came to me and said that they were interested in an edge-like mechanic, now the beloved monarch. He knew *Ixalan* had planned to do such a thing, but he wanted to know if his team would experiment with it. I told him he and his team could try it out, but they should also get a back-up mechanic ready just in case. I would start *Ixalan* exploratory design early and test out if an edge-like mechanic worked in two-player play.

Both *Ixalan* and *Conspiracy: Take the Crown* created edge-like mechanics that performed well. I told Shawn that he needed to use his back-up mechanic because I thought *Ixalan* could use the edge-like mechanic, but they never got a back-up mechanic that they liked. Shawn ended up appealing to Aaron Forsythe, my boss, and Aaron said that *Ixalan* had more time to find another answer and felt the mechanic worked best in multiplayer play, so *Conspiracy: Take the Crown* could keep the monarch mechanic. That meant *Ixalan* design started not knowing what its mechanical heart was.

Working with the Creative team, I realized that the two most exciting elements of the plane were two new creature types, Dinosaurs and Pirates. Dinosaurs were in past sets but hadn't been fully supported mechanically as a creature type. There had been a few Pirates, but only a handful, and they were never given any mechanical cohesion. I ended up making the call to have four factions, each with its own typal reward. (We've stopped using the word "tribal" in R&D as numerous consultants have stressed that it carries negative connotations, so we now use "typal" to mean "creature type mattering mechanically.") I added a fourth faction because I felt three creature types weren't enough to carry a typal theme. The Creative team came up with the idea of merfolk. I then made use of the four-factor structure we'd originally used in *Khans of Tarkir* where two of the factions were two-color and two were three-color. We decided the three-color factions should be the most exciting, so we made those Dinosaurs and Pirates.

As we started working with the set, it became apparent early on that we needed some way to tie the various creature types together mechanically. It was important that different drafters might want to draft the same cards. It's what we refer to as "glue" in R&D. Typal sets, more than any other theme, need glue. As an example, it's why we added changeling to the *Lorwyn* block. The low-hanging fruit was to have cards that were multiple creature types (ones that mechanically mattered). Could we have a Merfolk Pirate or a Vampire Dinosaur? The Creative team came back saying it wasn't supported by the creative and asked if we could avoid doing so. I'd already made the Creative team make numerous big changes (going from two factions to three and then from three to four) that I felt it was wrong to push on this point.

And thus, we get to the lesson of this design. I needed glue. If I didn't want to do things the Creative team didn't want to do, then I had to look elsewhere. Part of doing early design is solving the problems for the teams down river. I'd created a huge design problem and didn't offer any tools to fix the issue. In the end, *Ixalan* had several mechanical issues, but I feel the biggest one was the lack of glue, and that rests squarely on me never having solved the issue structurally in the first place. *Ixalan* failed in many regards, and I had to own up that I was responsible for many of those problems because I didn't do my job early on making sure the set was structurally sound.

## Learning the Hard Way

I hope you've enjoyed these introspective looks at previous designs. It's an important part of my own personal process of improving and something I'm happy to share. As always, I'm curious to hear your thoughts on today's column and/or any of the lessons. You can email me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for part two of my card design stories from *The Lord of the Rings: Tales of Middle-earth*.

Until then, may your life be full of lessons.
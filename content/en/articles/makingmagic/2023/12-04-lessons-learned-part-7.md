---
id: 1tvvc0sz
kind: article
lang: en
path: /en/articles/makingmagic/2023/12-04-lessons-learned-part-7
title: Lessons Learned, Part 7
published: '2023-12-04'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-7
    lang_detected: en
    capture_id: 222575
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7
    captured_at: '2024-05-18 01:04:29+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-7
    lang_detected: en
    capture_id: 222575
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7
    captured_at: '2024-05-18 01:04:29+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-7
    lang_detected: en
    capture_id: 222575
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7
    captured_at: '2024-05-18 01:04:29+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-7
    lang_detected: en
    capture_id: 222575
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7
    captured_at: '2024-05-18 01:04:29+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 1tvvc0sz
  url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7
  page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-7
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:04:29+00'
  capture_id: 222575
  wayback_url: https://web.archive.org/web/20240518010429id_/https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 1tvvc0sz
  capture_id: 222575
  url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7
  wayback_url: https://web.archive.org/web/20240518010429id_/https://magic.wizards.com/en/news/making-magic/lessons-learned-part-7
  captured_at: '2024-05-18 01:04:29+00'
  template: contentful
  sha256: 3b032c996d408cd9627746e89888b4c20190f7d18c1e11919d09b3628943b6bd
render_recovery:
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/bb99d5d7?color=FFFFFF&background=30343C
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/36645cd4?color=FFFFFF&background=30343C
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/a6fc6646?color=FFFFFF&background=30343C
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
Every week after I sign off, I post links to my podcast [*Drive to Work*](https://open.spotify.com/show/2I6wfhTMkpoN1WZzAxhMz8). If you've never listened to it, I record it on my drive to work, and I talk about various *Magic* design issues. (Most podcasts are only 30 minutes—the length of my drive to work—so it's an easy podcast to sample to see if you like it.) A recurring series from *Drive to Work* is one I call "Lessons Learned," where I go through every set for which I've led or co-led the design and talk about what I learned from the experience. Starting earlier this year, I've been doing written versions of this series, complete with links to the podcast where I go into greater detail. Here are the previous six "Lessons Learned" articles:

*   [Part 1](/en/articles/makingmagic/2023/03-14-lessons-learned-part-1)
*   [Part 2](/en/articles/makingmagic/2023/03-20-lessons-learned-part-2)
*   [Part 3](/en/articles/makingmagic/2023/05-22-lessons-learned-part-3)
*   [Part 4](/en/articles/makingmagic/2023/06-19-lessons-learned-part-4)
*   [Part 5](/en/articles/makingmagic/2023/08-07-lessons-learned-part-5)
*   [Part 6](/en/articles/makingmagic/2023/10-09-lessons-learned-part-6)

Last time, I got to *Strixhaven: School of Mages*, so I'm up to *Innistrad: Crimson Vow*.

## *Innistrad: Crimson Vow*

**Lesson: "There's not always the perfect solution."**

*Innistrad: Crimson Vow* was not originally on the schedule. The codenames are a big tip-off. *Innistrad: Midnight Hunt* was codenamed "Golf," and *Kamigawa: Neon Dynasty* was codenamed "Hockey." (*Innistrad: Crimson Vow*'s codename is "Clubs" to go with "Golf.") In fact, the design for *Kamigawa: Neon Dynasty* started before the design of *Innistrad: Crimson Vow*. Here's what happened. We'd stopped making core sets, then we brought them back, but it was a struggle. We decided to theme the next core set with *Dungeons & Dragons* to give it some extra flair, but the more we worked on the set, the more it was clear it should be a regular *Magic* set rather than a core set.

Once that core set went away, we realized that maybe we just wanted to return to four non-core premier sets a year. And when we were rethinking that, we started rethinking our schedule in general (note: I'm using northern hemisphere seasons) and decided that we'd rather put other products out during the summer. If we moved up our fall set, we'd have space to put out a second one closer to the end of the year. But we figured this out while we were doing vision design on *Kamigawa: Neon Dynasty*, the early winter set of the next year. If we were going to add a set in between *Innistrad: Midnight Hunt* and *Kamigawa: Neon Dynasty*, we had to move fast.

There was a little bit of wiggle room in the schedule to push back the rest of *Kamigawa: Neon Dynasty* vision design by a few months, meaning we could give the new set the full allotment of vision design, set design, and play design. However, we wouldn't have any time for exploratory design. That meant that the Creative team wouldn't have any time for exploratory worldbuilding, which meant creating a new plane was off the table. Even adapting an existing plane for a new set would be challenging in that time frame. What if we just stayed on Innistrad for a second set? We like to occasionally remain on the same plane for consecutive sets. That would require the least amount of worldbuilding. The Creative team would have enough time to adapt a new theme to it.

Remember, *Innistrad: Midnight Hunt* wasn't designed to be the first set of a two-set stay on Innistrad, so we had to look at what we were doing to see if there was a natural way to pivot to a second theme. The main mechanic was day/night, which, while applicable to all the monsters on Innistrad, pointed the most to Werewolves. As a result, we'd put a little more focus on Werewolves than the other creature types. If we leaned into that in set design, we could make the set a "Werewolf set" and then choose a second creature type to lean into flavorfully for *Innistrad: Crimson Vow*.

We chose Vampires and Zombies. While Spirits helped us fill out our ally creature type theme, they didn't have quite as much cache as the other three monster creature types, and Humans show up in most sets, so focusing on them didn't seem right. The Vision Design team designed mechanics for Zombies and mechanics for Vampires. Meanwhile, the Creative team met to figure out possible themes. The Vision Design team was leaning toward Zombies, as we'd made the decayed mechanic and really liked it but were open to either choice. However, the Creative team came up with the idea of a Vampire wedding, and we knew that was too awesome to pass up, so Vampires became our theme. Decayed would end up getting moved to *Innistrad: Midnight Hunt*.

We came up with Blood tokens for Vampires. *Magic* had a bunch of success with artifact tokens, which had a basic game function that you could make in volume and then use as a game resource (Treasure, Food, Clues, etc.), meaning there would be designs that would give the tokens other uses. Vampires require blood, so the idea that you could feed your Vampires to empower them and give them extra stats or abilities was very flavorful. But what should Blood tokens do?

A quick aside, because it comes up whenever we discuss Blood tokens: Did we ever discuss it being a token other than an artifact? We did. However, the only real choice was artifacts or enchantments, and we use artifacts to represent tangible things and enchantments to represent intangible things. Things like hope or faith make sense as enchantment tokens, but blood clearly is a tangible thing, so we felt it should be an artifact. Couldn't it have no card type? We don't like doing that for several reasons. One, it makes it less interactive with the rest of the game. There are less synergies and less answers to it. Two, it causes confusion. What exactly is it? Three, there are rules implications that can be problematic. The rules assume things are a known card type, so you end up with a lot of weird corner cases. Four, there are play balance issues. This ties back into the first reason. If the token is a thing, there are answers to it naturally built into the set.

Both Clues and Treasure came about because we wanted a certain functionality for a token and then named it appropriately. Food started with its flavor (pun, as always, intended), but there was an obvious low-hanging mechanic—life gain. Blood, as a creative concept, was a lot trickier. What exactly does blood do? It transports oxygen. It helps regulate a body. It provides protection from disease. It just doesn't have a clear and simple function.

First, we thought to have it create a +1/+1 counter. That's generally a useful effect, and you could think of it as empowering someone. The play pattern for it was wrong, though. We didn't want Vampires playing too similarly to Werewolves, as they're the creatures that tend to build up over time. It was more powerful than we wanted, it created complex board states, and we didn't want it interacting with combat. We also wanted the alternate of Blood to be temporally empowering Vampires, so we wanted the token to do something different.

In the end, we found the effect that played best was rummaging (i.e., discarding and drawing). It helped smooth draws. It was a small enough effect that players were willing to feed it to their Vampires. It had synergies with our other themes (all Innistrad sets have a graveyard component). But it didn't feel super bloody. I should note that we tried lots of different effects, and none did. I'm not sure there's even such a thing as a mechanic that's a slam dunk for Blood in terms of flavor.

These were the calls I had to make:

1.  Abandon the mechanic.
2.  Call the token something different.
3.  Leave it as is.

It was playing well and was acting as the glue tying the whole set together, so I didn't want to do A. We talked about doing B, but there just wasn't another good word. Also, while the token didn't have the best flavor, the flavor of the cards creating and using Blood tokens was great.

![Grisly Ritual](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=540964&type=card) ![Blood Fountain](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=540939&type=card)  
 ![Belligerent Guest](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=540999) ![Ceremonial Knife](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=541129&type=card)

So, I settled for C. With 20/20 hindsight, it was clearly the right call given where the set was at, but part of me wonders whether I was supposed to have abandoned the Blood token idea once it was clear that we couldn't score a slam dunk for flavor. Design requires leaning into what's playing best and assuming you'll find the right flavor along the way. The flip side of the argument is that it doesn't enable awesome card flavor. Is that enough? Does every artifact token itself need perfect flavor? There are definitely effects that could make good tokens but might not have great accompanying flavor. For example, rummaging plays well. Is there a flavor slam dunk for rummaging?

The point of this lesson is that not every design challenge has a perfect answer. Sometimes to get one element you really like, you must accept something you like a little less. Yes, you can always strive to improve the set, but at some point, you have to be done. Are Blood tokens a perfect design? No. The lack of ideal flavor will annoy me to the end of time. Are Blood tokens good enough that we should have made them? I think so, but there are doubts. There are members of R&D who think we shouldn't have made them.

I think players like to think of game design as having answers that are clearly correct or clearly wrong, but the reality is, *Magic* design isn't always black and white. There are often shades of gray and subjective calls to make. Blood tokens offer a good example of this.

## *Kamigawa: Neon Dynasty*

**Lesson: "Harness your greatest weakness."**

We put *Kamigawa: Neon Dynasty* on the schedule because we were interested in a plane inspired by Japanese pop culture. We had ideas of a plane more modern than the one we'd done so far. For those unaware, I have [a blog on Tumblr known as Blogatog](https://markrosewater.tumblr.com/), where I answer questions every day from *Magic* players. My blog audience consists of mostly enfranchised players, as one would expect in a blog from the head designer of a game, and there's a lot of back-and-forth between getting questions and notes and me responding to them. (I've had my blog 11 years and I've answered close to 150,000 questions.) From my blog, I knew that there was a portion of the playerbase that really wanted to return to Kamigawa.

The *Champions of Kamigawa* block came out in 2004 and 2005. It was a top-down design based on Japanese mythology. The set did poorly on just about every metric we track: sales were down, play was down, it scored the worst in market research of any set for both mechanics and plane for any world we've ever tracked. Players asked for us to return to Kamigawa so often on my blog, it became a running joke. I always replied the same way: it's just a real hard sell to my bosses. We have so many popular planes, why not return to any of them? In my heart, I knew there was an enfranchised audience who really, really wanted to go back to Kamigawa, and I wanted to make it happen if possible.

This meant I knew that I wanted "Hockey," as it was then codenamed, to be set on Kamigawa, but I wasn't 100% sure how to make that happen. First, during exploratory design, I had to get everybody on board with the following decision: Let's not decide yet whether the plane should be Kamigawa. Let's just build the world in a vacuum and decide later if calling Kamigawa makes sense. Then in design, my plan was to design a set that optimized the world we were building *and* mechanically had to be Kamigawa. How could we do that?

In design, we looked at all the mechanics from the *Champions of Kamigawa* block. The only popular one had been ninjutsu, and that was tied to Ninjas. We tried to see what was salvageable (trying things like splice onto instants), but in the end, the only other mechanic that seemed viable was channel (an ability word that lets you discard cards from your hand for an effect). Technically, we do things like channel all the time, and we normally don't label it, but it was generally a useful mechanic that would allow us to bring back a named ability word from the *Champions of Kamigawa* block.

But how do we take a modernized Japan and connect it to the Kamigawa from the *Champions of Kamigawa* block? We had one saving grace. The setting of the *Champions of Kamigawa* block was over 1,000 years in the past. The plane could realistically have changed quite radically, but if it changed too much, would it even feel like Kamigawa?

To tackle this problem, I borrowed a technique I learned in writing class. My teacher referred to it as "harnessing your greatest weakest." It works like this: When you get stuck writing a story, identify your biggest obstacle. What's getting in your way? Then, see if you can turn that negative into a positive. Basically, write your story around your weakness in such a way that it becomes a feature rather than a bug. It proved very helpful to me back in my writing days, so I decided to apply it to game design. Okay, what was our biggest weakness? We were designing two different worlds. One was modern, one was ancient. One was based on technology and the other on tradition. They were literary opposites of one another. Hmm.

When we create a world, we design something we call the conflict engine. *Magic* is a game about conflict, so it's important that there is some inherent conflict built into the world. (This also happens to be something important for story.) What if the conflict of the world was the conflict between these two halves? We then turned to our source material, Japanese pop culture. Are there conflicts with technology versus tradition? This happens to be one of the most popular themes of Japanese pop culture. Japan, as a country, values both technology and tradition, so that contrast has become a common theme in Japanese entertainment. Leaning into this mechanic would only reinforce the larger feel of the world.

Once this conflict was in place, it dictated the larger structure. Two-sided conflicts want to have two distinct sides such that each side of the conflict has its own mechanical definition, one that feels opposed to the other side in flavor but plays well together. We tend to use artifacts to convey technology, and enchantments felt good for representing tradition. Artifacts and enchantments work great as opposing themes. They feel opposite in flavor, but behind the scenes, they work almost identically. This allowed us to use a mechanic like modified that worked with either half but also together.

It's one of my favorite design stories in that it shows how what you see as the cause of your design problem can sometimes also be its solution.

## *Unfinity*

**Lesson: "Playing well isn't always enough."**

It's no secret that I'm a huge fan of the *Un-* sets (*Unglued*, *Unhinged*, *Unstable*, and *Unfinity*). I've led the design for all four of them, and for *Unfinity*, I got permission to lead the set from the very beginning to the very end, meaning it was the first set design team I'd ever led. We don't make a lot of *Un-* sets, so I try to savor them whenever I get a chance to make them.

The goal of an *Un-* set is threefold. One, it allows us to make cards that aren't tournament legal, which lets us create some designs we normally can't. Two, it has a lighter tone and a lot more humor than the average *Magic* set. Three, it's a place where we can push boundaries, try new things, some of which, like full-art basic lands or creature token cards, find their way to non-*Un-* sets.

When I started *Unfinity*, I had two major goals. One, I was interested in seeing if we could do anything with stickers. From time to time, we do something called a Hackathon where we spend a whole week going deep on new design ideas, usually products, but sometimes mechanics. In multiple Hackathons, stickers came up as a resource, and there were a lot of cool things done with them. *Un-* sets like to test new boundaries, and stickers showed a lot of promise.

Two, I liked the idea of each *Un-* set taking a different popular form of set design and applying it. *Unstable*, for example, showed us applying a faction set structure to *Un-* design. For *Unfinity*, I wanted to make a top-down set structure. I worked with Dawn Murin, my art director (she and I worked together on *Unstable* and *Unfinity*) to come up with a top-down topic that we didn't feel was anything we'd do soon elsewhere. I was interested in doing a circus or amusement park set, and Dawn was interested in a retro-futuristic space set, so we combined them. (And yes, "Volleyball" has a space theme, so that shows that we weren't as far away from normal *Magic* as we thought we were.)

For this lesson, I'm going to focus on the stickers, as that was one of the driving mechanical themes for the set. Our printing department had done stickers in other products but never in conjunction with a *Magic* set. They told me they could make stickers of any size or color combinations, as long as the sticker sheet fit inside a booster. I had two requests. My highest-priority request was that the stickers could peel off and wouldn't harm the card that was stickered. My second request was that the stickers could be reused. The idea was that you would use them for one game, take them off, and then use them for future games.

My design team spent a lot of time coming up with all the things you could do with stickers. In the end, we liked four things, all of which went on a *Magic* card: name stickers, art stickers, ability stickers, and power/toughness stickers. There was some discussion if we should do less things with stickers. What if we only did ability stickers? Or only did art stickers? One of the goals of an *Un-* set is to test things out and experiment, so I wanted to try all four. (I should note that we came up with much more than four uses. Only having four was cutting down.)

My thought process was that while there were a lot of different things you could do with stickers, we could mechanically get players to focus. For example, we made four different color pairs that each focused on a different kind of sticker. If you loved art stickers, you could play blue-red and focus on them.

I also made another decision when it came to stickers. I wanted to maximize variety. *Un-* sets are the most casual magic products we make, so we lean toward having a high variance, as high variance is very fun but less skill testing. The reason you play an *Un-* set isn't to be super competitive, so high variance seemed ideal. The printing allowed us to make 48 different stickers. I made the choice not to repeat any feature that I could avoid repeating, so the only stickers that show up multiple times are power/toughness stickers, as there literally weren't enough combinations not to repeat them.

In our early drafts, we drafted the sticker sheets but quickly realized it just made things too complicated to track, so we made rules that players must draft the sticker sheets they open. This also ensured a higher variance with them.

Due to numerous factors, *Unfinity* had a slightly longer design period than the average set. Stickers were in the very first file, and we iterated on them for over two years. I feel we got them to a really fun place that played well. In playtest feedback, stickers always got high marks. The general note we got again and again was, "These are really fun." I had high confidence in stickers as we officially handed off the file to production. But then *Unfinity* came out, and the response to stickers was very polarized. A good portion of the audience strongly disliked them. Why? Let's talk about the major reasons.

**1\. We put them into Eternal formats**: We decided late in set design to make every card that was playable under the rules, and wouldn't cause play balance issues in Eternal formats, Eternal legal. The idea being to let players who enjoy playing *Un-* cards not have to beg their play group to use them if they weren't causing rules and/or balance issues. Many players felt stickers, even though they worked in the rules, crossed the line. They didn't feel like they belonged. To make matters worse, we had tried hard to cost stickers so they wouldn't show up in competitive Eternal events. We missed on one.

![________ Goblin](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=580670&type=card)

With 20/20 hindsight, should we have made them Eternal legal? I'm a bit mixed on this. I do like that casual cards that work within the rules are accessible to Commander players. I'm less happy that the Legacy format has to deal with \_\_\_\_\_\_\_\_\_\_ Goblin. It's odd that one of our most casual formats and one of our most competitive formats use the same card list.

**2\. There were a lot of logistical issues**: How sticky should stickers be (what production calls tackiness)? Too sticky, and they wouldn't come off. Not sticky enough, and they wouldn't restick. Our goal was to be somewhere in the middle, although leaning slightly toward less sticky and not harming the cards was the primary goal. We got one test run with the stickers. We stickered them on cards. We took off the stickers. We put them back on. We tested them with specific cards that cared about stickers to see how well they worked with them. What we didn't do, and we should have in retrospect, was play a full tournament with them. Stickers are pretty good for the first couple games, but there comes a point where they just don't stick that well. And they didn't do a great job of sticking back on the sticker sheet after you used them. This resulted in players losing their stickers or stickers falling off mid-game and having to figure out where the sticker went. In short, the act of playing with stickers logistically, not what they did in game, just putting them on and off, and carrying them around between games, was suboptimal.

Looking at this problem with 20/20 hindsight, we should have done more testing with the one test run we had, but in general, it's just tough being the first set using brand-new printing technology, as very few actual playtests can use it. Yes, we played with actual stickers, but not the specific versions that were going to show up in boosters, as they literally didn't exist yet for most of the design. If I had to design the set over, I'd rethink how we use stickers, considering the logistical issues. Maybe the stickers are stickier but go on external card game pieces rather than the actual cards. I'm not 100 percent about what I'd change, but I would rethink the whole way stickers are used. I've also considered exchanging stickers for punch-out cards that work mostly the same. This would help with the reusability issue. I don't think I would abandon the larger concept, though, as I do see a lot of potential in them for fun gameplay.

**3\. They did too much**: This is the one that hurts the most. We were trying to show off what stickers could do, so we did several different things with them, not just in the type of sticker, but in how cards interacted with them. This card wants small stickers. This card wants big stickers. This card wants words that start with the same letter. This card wants hat stickers. The variety of stickers plus the variety of ways to use them made a matrix that was too complex for many players. While any one sticker and sticker card might be fun in a vacuum, all together they could be overwhelming, and that's not even getting into other themes of the set.

Of the three problems I listed, this was the one that, with 20/20 hindsight, the design team is most responsible for, and specifically me as lead designer of the set. Name stickers are the thing I'd remove if we were doing this again. They were the hardest to design around and the most confusing to use. I'd also pull up the as-fan of much of our one-of sticker use cards. I think having some rare cards that care in specific ways was fine, but we put too many at uncommon.

The lesson here is that gameplay is important, but it doesn't live in a vacuum. Format concerns, logistical issues, comprehension, and numerous other factors I didn't get into here all impact the reaction players have to a mechanic. Game design doesn't only have to focus on how cards play but how players will interact with and use the cards. A corollary to this is that it's important to play, as much as possible, in the same way that your players will play. This is why we playtest double-faced cards as actual double-faced cards and mock up play aides.

## "Class Dismissed"

I started my "Lessons Learned" columns earlier this year and have caught up to where I am in my podcasts. (I have led or co-led three sets that I haven't talked about yet—*Phyrexia: All Will Be One*, *March of the Machine*, and *The Lost Caverns of Ixalan*, but I haven't recorded "Lessons Learned" podcasts for them yet.) I assume I'll do an eighth "Lessons Learned" column sometime next year and future ones when enough sets I've designed have come out.

As always, if you have any feedback on today's column, any of my lessons, or on any of the sets I talked about, feel free to email me or contact me through any of my social media accounts ([X \[formerly Twitter\]](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week when I talk all about the innovations of the original *Ravnica* block.
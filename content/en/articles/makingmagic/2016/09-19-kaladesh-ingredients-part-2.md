---
id: 34873zxt
kind: article
lang: en
path: /en/articles/makingmagic/2016/09-19-kaladesh-ingredients-part-2
title: Kaladesh Ingredients, Part 2
published: '2016-09-19'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
    lang_detected: en
    capture_id: 222349
    url: https://magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
    captured_at: '2024-05-18 02:58:13+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
    lang_detected: en
    capture_id: 222349
    url: https://magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
    captured_at: '2024-05-18 02:58:13+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
    lang_detected: en
    capture_id: 222349
    url: https://magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
    captured_at: '2024-05-18 02:58:13+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
    lang_detected: en
    capture_id: 222349
    url: https://magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
    captured_at: '2024-05-18 02:58:13+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 34873zxt
  url: https://magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
  page_key: magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
  lang: en
  template: contentful
  captured_at: '2024-05-18 02:58:13+00'
  capture_id: 222349
  wayback_url: https://web.archive.org/web/20240518025813id_/https://magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
- document_id: 34873zxt
  url: https://magic.wizards.com/en/articles/archive/making-magic/kaladesh-ingredients-part-2-2016-09-19
  page_key: magic.wizards.com/en/articles/archive/making-magic/kaladesh-ingredients-part-2-2016-09-19
  lang: en
  template: drupal
  captured_at: '2022-05-25 01:46:54+00'
  capture_id: 891098
  wayback_url: https://web.archive.org/web/20220525014654id_/https://magic.wizards.com/en/articles/archive/making-magic/kaladesh-ingredients-part-2-2016-09-19
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 34873zxt
  capture_id: 222349
  url: https://magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
  wayback_url: https://web.archive.org/web/20240518025813id_/https://magic.wizards.com/en/news/making-magic/kaladesh-ingredients-part-2-2016-09-19
  captured_at: '2024-05-18 02:58:13+00'
  template: contentful
  sha256: 2b13ed7faceb2f3f7e0da95c51790a51d6e218e54ac7696632729e0eb064c2d7
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - my email
  occurrences: 1
---
[Two weeks ago](/en/articles/makingmagic/2016/09-05-kaladesh-ingredients-part-1), I began telling you the story of *Kaladesh*'s design. I took a week off to [introduce you to *Kaladesh Inventions*](/en/articles/makingmagic/2016/09-12-masterpiece-series) and the whole *Masterpiece Series*, but I'm back to finish the story. As we left it, I had introduced you to the design team and talked all about how energy first came about and how it eventually ended up in *Kaladesh*. So we're going to pick up where I left off—in exploratory design.

# Can You Give Me a Lift?

The very first thing we did in exploratory design was figure out how to make energy work. Once we were done with that task, I asked my team what they thought players were going to expect in *Kaladesh*. We had teased the world in *Magic Origins*, so you all had a hint of what was to come. We talked through numerous ideas. At one point, I suggested we take a look at the work the creative team had done on Kaladesh for *Magic Origins*. That's when we saw this:

![](http://media.wizards.com/2016/images/daily/MM20160919_26.jpg)

Kaladesh (the plane) was going to have large flying skyships as well as numerous other vehicles. As part of my job as spokesperson, I interact a lot with the fan base to ensure I have a good sense of what kinds of things you all want to see. Whenever you make suggestions, I make a note. One thing that's come up again and again for years is the request to make vehicles. We've never acted on it, because designing vehicles would be tricky and we never really had a world where it seemed right to introduce them. Well, that was clearly about to change. Kaladesh was going to very loudly have vehicles. So I charged my exploratory design team (Shawn Main, Doug Beyer, Adam Prosak, Dan Emmons, and myself) with finding a way to make Vehicles (the card type) work. I didn't know if we were going to end up with a solution, but I felt like we at least had to try.

![](http://media.wizards.com/2016/images/daily/MM20160919_27.jpg)

We started by asking ourselves, what all was a Vehicle supposed to do? Well, for starters, creatures had to be able to "get in" Vehicles and "drive" them. We also liked the idea of the Vehicle having some relevance to combat. With this in mind, the team started trying to crack the problem.

The first thing we tried was having Vehicles act kind of like Equipment—but instead of the artifact equipping to your creature, you equip your creatures to the Vehicle. We called it boarding. The idea was that while a creature was boarded to a Vehicle, the Vehicle provided some ability or abilities. A hot-air balloon, for example, would grant your creatures flying. Boarding had a mana cost, but there was no limit to how many creatures could board a single Vehicle. If everyone on your team wanted to climb into the hot air balloon, no problem.

It only took one playtest to understand the problems in this design. Let's say I have a 1/1 and a 2/2 and Hot-Air Balloon (a Vehicle that grants boarded creatures flying). You pay four (two for each creature) and board the 1/1 and 2/2. Now they each have flying. Let's say your opponent has a 1/2 flier so you only want to attack with your 2/2. What happens? Can the 2/2 attack alone and the 1/1 stay behind? They're in the same Hot Air Balloon. Are they forced to attack or block together? Or if my 2/2 attacks in the Hot Air Balloon but my 1/1 stays behind, is the 1/1 now forced to leave the Hot Air Balloon? Or does it stay in and we wave away the flavor inconsistency?

And the above example was just a vanilla 1/1 and 2/2 with no other card interactions. The more we explored how Vehicles would work in this configuration, the more we realized there wasn't any way to make it play well while making the flavor work out correctly. So we tried something different.

War Balloon had us exploring the idea of Vehicles being creatures. What if you could attack or block with them, but only if a creature had boarded them? War Balloon's power was the combination of the power of all the creatures boarding it. This version solved some of the old problems but created some new ones. I pay three and board my 3/3 to my War Balloon. If it attacks, what happens with the creature? Could I attack with my War Balloon and then, on my opponent's turn, block with my 3/3? The flavor of that seemed wrong. Wasn't my 3/3 in the War Balloon?

We hadn't quite cracked Vehicles by the end of exploratory design, but we had discovered enough potential that I was more than willing to let the design team (I introduced you to this team [last week](/en/articles/makingmagic/2016/09-12-masterpiece-series)) take a crack at it. I started by setting the following parameters:

1.  I wanted Vehicles to be artifacts.
2.  I wanted Vehicles to be able to attack and block in combat.
3.  I wanted creatures to be able to board Vehicles and have that matter.
4.  I wanted Vehicles to feel different than Equipment.

The design team latched onto the idea that a creature gets into a Vehicle and "turns it on." I think the earliest version in design had the Vehicles being artifact creatures, but they couldn't attack or block unless they had the proper crew. After a bunch of playtesting, we ended up with the idea that creatures would board Vehicles and then, once boarded, the Vehicle could attack or block until the creature(s) de-boarded. At that point, boarding still had a mana cost associated with it. We also added a restriction for how many creatures had to board a Vehicle for it to be able to attack or block.

I'll give an example. I have a 1/1 and a 2/2. I have a Vehicle called Big Tank that is a 5/5 artifact creature with trample. It costs two to board and has a crew requirement of two. For four mana, I could board my two creatures onto the Big Tank. (We would put the cards underneath.) For as long as those creatures were boarded, you had a 5/5 trampler you could attack or block with. While your creatures were boarded, they could still be targeted by spells and effects, so one of the best answer to Vehicles was to destroy the crew.

With playtesting, we came to realize a few things. First, we didn't like that creatures permanently boarded the Vehicle. Second, we were interested in finding a way to remove the mana cost for boarding. Third, people kept using their creatures for activated abilities while they were boarded to Vehicles, which felt weird flavor-wise.

Our solution was to change the mana requirement to a tapping requirement. To board you now had to tap the proper number of creatures. This then allowed you to attack or block that turn. That meant Big Tank would now just say "Board 2," which meant in order to attack or block with the 5/5 trampler you had to first tap two untapped creatures you controlled.

![](http://media.wizards.com/2016/images/daily/MM20160919_28.jpg)

# Driving the Vehicles

This is how Vehicles worked at the handoff from design to development. Development fiddled around with numbers. The creative team asked if the Vehicles could only be creatures when boarded, as it was odd to have empty Vehicles perform tasks that only creatures could. This also solved the problem of tapping one Vehicle to board another Vehicle. (This is still technically possible, but there are very few mechanical reasons now to want to do it.) The term "board" was also changed to "crew."

Development played with Vehicles for many weeks and started to see a problem. The reliance on having a certain number of creatures heavily rewarded you for having a lot of small creatures, especially tokens (this ties into the last mechanic, fabricate, which I will get to in a bit). Because the Vehicles worked so efficiently with tokens, development had to cost the Vehicles assuming you had tokens, and then they ended up being too expensive to work with anything *but* a token strategy.

Meanwhile, I was busy designing Ham, the fall (northern hemisphere) set of 2017. At the halfway point of *Kaladesh* design, I handed the reins of the set over to Shawn Main so I could start working on the design for *Amonkhet*, the large set of the next block. And then halfway through *Amonkhet* design, I handed the reins over to Ethan Fleischer so I could work on Ham. In Ham, we were working on a new mechanic that I was worried felt too much like Vehicles because it required having a certain number of creatures to activate it. To try and distance my mechanic from Vehicles, I changed it so instead of caring about how many creatures you had, it cared about the total power of the creatures you had. We tested with it and I really liked how it played.

From time to time I poke my head back into sets that I had previously handed off. *Kaladesh* was in development, so I talked with Ian Duke and Erik Lauer, the co-leads for *Kaladesh* development. They explained that they were having a problem with Vehicles. As they walked through their problem, it dawned on me that my solution for the Ham mechanic might actually work in *Kaladesh*. Instead of "crew 5" meaning you have to tap five creatures, it would mean you have to tap any number of creatures whose power added up to 5 or more.

The developers thought the idea was interesting and tried it out. It turned out to be a wonderful solution, because a high crew number no longer meant you had to have a deck with a whole bunch of tokens. Now, you could just play a deck with bigger creatures and not have any tokens. And that is how we got this.

![](http://media.wizards.com/2016/bVvMNuiu2i_KLD/en_xhHIG0S1uab.png)

One final note on Vehicles: while we definitely wanted players to be able to build a Vehicle deck, we designed the Vehicles such that they covered a range of different play styles—so that every player had the option of including a Vehicle or two in their deck if they so desired.

# Fabricating Fabricate

One of the goals of design was trying to capture the feel of the world. Early on, to help differentiate the kind of artifact set we were making, I came up with this line: on Kaladesh, artifacts are technology, not biology. Our last artifact world was Mirrodin and, on Mirrodin, many things were artifacts because it was a world made of metal and the creatures of the world were all, in some way or another, infused with that metal.

*Kaladesh* isn't a metal world, but rather a world of invention. I wanted the artifacts to be seen as a form of technology. The inhabitants of Kaladesh are enhanced not because they have metal woven into their biology, but rather because they have use of technology. They have gadgets and tools and vehicles and automatons. This feeling wouldn't stay isolated to the artifacts, though. The idea of technology had to inhabit all the colors as well.

To do this, we looked at what *Magic* tools could help capture this flavor. Creatures have technology and it makes them stronger or faster or smarter. It makes them better. In *Magic*, we often show this kind of improvement with +1/+1 counters. Also, we wanted to be able to show that the denizens of Kaladesh have the ability to create mechanical life. The Thopters, for example, were a big part of the sneak peak of Kaladesh in *Magic Origins*. The artificially made creatures could be represented through artifact creatures and artifact creature tokens.

Once we knew we wanted to use +1/+1 counters, we started weaving mechanical themes around them. The same was true for tokens, which could be rewarded either for being creatures or for being artifacts. As such, the set built up a +1/+1 counter theme and a token theme (as well as an artifact theme). Our biggest problem was the two weren't intersecting as much as we liked. Hmmm. What if we could make a mechanic that bridged the two themes?

That led us to think of Standsteppe Outcast from *Fate Reforged*:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=SANDSTEPPE+OUTCAST)](https://web.archive.org/web/20160919000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=SANDSTEPPE+OUTCAST)

When it entered the battlefield, it gave you a choice. You could enhance your creature with a +1/+1 counter or you could instead get a token. What if we built an entire mechanic around this option? It would allow players to care about both themes and would allow them to mix and match them in the same deck, because the fabricate (the name of the bridging mechanic) cards would work with both.

When we originally started, inspired by [Sandsteppe Outcast](https://web.archive.org/web/20160919000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sandsteppe+Outcast), we imagined the token being a 1/1 creature with no other abilities—well other than being an artifact. This was Kaladesh, after all. We did entertain the idea of the token creature being a 1/1 flying Thopter, but we were already having the problem that players were too often choosing the creature token. Making it fly took away almost all of the decision-making.

Even as a 1/1 non-flier though, players were choosing the tokens more often than the +1/+1 counter. (Remember, at this point Vehicles cared about how many creatures you tapped to crew them, so tokens mattered even more.) We had made the choice in the beginning to give fabricate a single number, meaning that the choice was always between the same number of +1/+1 counters or artifact creature tokens. We talked about disconnecting the two numbers, but it made the card more complex and a lot harder to easily track.

Our solution was to (often) put abilities on the fabricate creatures that scaled well with power. That way there was extra synergy if you chose the +1/+1 counter(s). When Vehicles were changed, it ratcheted down the power of choosing artifact creature tokens a little (although they still allow you to crew Vehicles without over-crewing them, aka tapping more power than needed) and made the two a bit easier to balance.

# Three Shall Be the Number

During design, we created a number of other mechanics. At one point we had five different mechanics in the set, but energy and Vehicles really wanted to fill a lot of space and were a bit more mentally taxing than the average mechanic, so we decided to drop down to just three mechanics. As I've mentioned in this year's "[State of Design](/en/articles/makingmagic/2016/12-27-state-of-design-2016)," I believe we've been overstuffing the sets for the last few years, so I liked the idea of pulling back a little. There's was still plenty going on, so I was happy to see the two other mechanics go. (I did like them both, so I'm sure we'll see them again one day.)

Another important thing was that the vision of making the player feel like an inventor transcended just the mechanics. I wanted lots of interesting choices that would increase the variance of play and cards that allowed players to build around them (more than we normally do). I wanted *Kaladesh* to be a set where players felt clever and were constantly discovering new things to try.

As I mentioned above, we made sure the set had a number of different themes, and we worked hard to create them in such a way that players could mix and match the themes, allowing them to invent as they built their decks—and again when they played with the cards. There are lots of fun stories about all the cool design things we did along the way, but you'll have to wait, as I'll use the new few weeks to talk about this when I do my card-by-card stories.

I just want to end today by stressing how excited I am for *Kaladesh*. There's something about this world that spoke to me and I had a blast, as did the rest of my design team, creating the set. There's so much cool stuff here, and the set has a very modular design to allow you to mix and match it in fun and interesting ways. I'm dying to get a chance to see you all start playing it.

That's it for today. I'm always excited for feedback, but as *Kaladesh* is so near and dear to my heart, I'm more eager than normal for feedback (constructively critical as well as positive). You can write to me through my email or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254),[Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and[Instagram](http://instagram.com/mtgmaro)).

Join me next week for the start of the *Kaladesh* card-by-card stories.

Until then, may you invent wondrous things.

* * *

**"[Drive to Work #366—Ravnica Showdown](http://media.wizards.com/2016/podcasts/magic/drivetowork366_ravnicashowdown.mp3)"**

This podcast starts a new series called "Showdown," where I pit two designs against one another. For this podcast, I am pitting the guild mechanics of original *Ravnica* block versus the guild mechanics of *Return to Ravnica* block. Who will win?

**"[Drive to Work #367—Flux](http://media.wizards.com/2016/podcasts/magic/drivetowork367_flux.mp3)"**

*Magic* is an ever-changing, ever-evolving game. In this podcast, I talk about the impact of flux on design.

*   [**Episode 365** ](http://media.wizards.com/2016/podcasts/magic/drivetowork365_urzaslegacypart2.mp3)Urza's Legacy, Part 2 (25.5 MB)
*   [**Episode 364**](http://media.wizards.com/2016/podcasts/magic/drivetowork364_urzaslegacypart1.mp3) Urza's Legacy, Part 1 (26.5 MB)
*   [**Episode 363**](http://media.wizards.com/2016/podcasts/magic/drivetowork363_packaging.mp3) Packaging (31.9 MB)

*   **[Complete Drive to Work Podcast Archive](/en/articles/media/undated/podcasts-media-articles)**
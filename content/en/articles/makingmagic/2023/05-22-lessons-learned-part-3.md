---
id: mdxmb1mw
kind: article
lang: en
path: /en/articles/makingmagic/2023/05-22-lessons-learned-part-3
title: Lessons Learned, Part 3
published: '2023-05-22'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-3
    lang_detected: en
    capture_id: 222549
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-3
    captured_at: '2024-05-18 01:17:53+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-3
    lang_detected: en
    capture_id: 222549
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-3
    captured_at: '2024-05-18 01:17:53+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-3
    lang_detected: en
    capture_id: 222549
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-3
    captured_at: '2024-05-18 01:17:53+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-3
    lang_detected: en
    capture_id: 222549
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-3
    captured_at: '2024-05-18 01:17:53+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: mdxmb1mw
  url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-3
  page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-3
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:17:53+00'
  capture_id: 222549
  wayback_url: https://web.archive.org/web/20240518011753id_/https://magic.wizards.com/en/news/making-magic/lessons-learned-part-3
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: mdxmb1mw
  capture_id: 222549
  url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-3
  wayback_url: https://web.archive.org/web/20240518011753id_/https://magic.wizards.com/en/news/making-magic/lessons-learned-part-3
  captured_at: '2024-05-18 01:17:53+00'
  template: contentful
  sha256: c79abc3337236c167c091d9221d46ddc7b6c19145f6cd61873cede3979daef2c
render_recovery:
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/9afa304e/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/38188cb9/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/de0b67ad/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/28a6346a/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/a8cdacdf/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/c828a671/dark
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
Back in March, I started a new article series called "Lessons Learned" based on a series from my *Drive to Work* podcast where I go through every set for which I've led or co-led the design and talk about what I learned from the experience ([Part 1](/en/articles/makingmagic/2023/03-14-lessons-learned-part-1) and [Part 2](/en/articles/makingmagic/2023/03-20-lessons-learned-part-2)). Last time, I got to original *Zendikar*, which means I'm up to *Scars of Mirrodin*.

## *Scars of Mirrodin*

**Lesson: "Don't skip the best part."**

Of all the design teams I've ever led, I think my lowest point came during *Scars of Mirrodin*. It was the only time I've ever been threatened to have a design taken away from me. Here's what happened.

When we visited Mirrodin for the first time, we subtly included a story element that we'd planned to come back to when we returned there. That story element was the return of the Phyrexians.

The Phyrexians were first introduced during *Antiquities*, *Magic*'s second-ever expansion, as part of the Brothers' War story. They would then go on to be the main villain for the *Weatherlight* Saga. At the end of that story, thanks to actions taken by Urza and the *Weatherlight* crew, the Phyrexians were wiped from the Multiverse.

But they were an awesome villain, so we knew one day, we'd like for them to return. The idea of Karn accidentally spreading Phyrexian oil to Mirrodin came about as we were building out the plane of Mirrodin. We made a few slight hints at it and then left it alone for over a decade.

The original plan for the *Scars of Mirrodin* block was that the first set was going to be New Phyrexia. Look, Phyrexia is somehow back, and we don't know how. Then the third set in the block would have a reveal, much like the ending of the original *Planet of the Apes*, that New Phyrexia was in fact Mirrodin but had been taken over by the Phyrexians.

I loved the Phyrexians as villains and was excited to have them return. I'd taken over as head designer as of the original *Ravnica* block, and every block since that had a clear block plan, but I struggled to figure out what the New Phyrexia block was supposed to be about. We came up with mechanics to represent the Phyrexians, but there was just something missing, and I didn't know what.

Things got so bad that Bill Rose stepped in. He gave me a deadline and told me that if I didn't solve the problem by then, he was going to assign the set to someone else. The design team also changed around its composition. In that meeting, Bill gave me the most rousing speech he'd ever given me about how I could solve this problem, as I was a strong *Magic* designer who exceled at this type of issue.

I spent a lot of time thinking through the problem I was having and eventually had a big breakthrough. I went back to Bill and said, "We're making the wrong block." We have this cool story to tell, and we've completely skipped over it. Last time we were on Mirrodin, it was (almost) 100% Mirrodin. We're back, and it's (almost) 100% New Phyrexia. How did it get from one state to the other. That was the story. Why were we skipping it?

I pitched a new block. We would start on Mirrodin. It's the plane as we remember it, except there's a little something going on, and the Mirrans don't quite understand what it is. Set two, the Phyrexians have escalated things, and it's an all-out war. Set three would take place on New Phyrexia, where we see the Phyrexians triumphant. It was in this meeting that Bill suggested that we don't tell the audience who wins until the third set comes out. We advertise it as either "Mirrodin Pure" or *New Phyrexia*, and the players don't know the outcome of the war until they're at the store buying it.

The big lesson of this design is about not seeing the forest for the trees. I was so focused on how to tell a particular story that I couldn't take a step back and ask, "Is this the right story to tell?" I was stuck because I kept trying to figure out how to do something that I fundamentally didn't want to do, but when I was able to take a step back and understand what story I did want to tell, the design came pouring out. Once the block was about the Phyrexian takeover of Mirrodin, the whole block plan spelled itself out.

## *Innistrad*

**Lesson: "Top-down design is about capturing the emotion."**

*Innistrad* is one of my designs that I'm most proud of. It came about because when we made *Odyssey*, Brady Dommermuth and I talked about how its mechanics were an odd fit for the creative it was given. (Back in the day, we would make a *Magic* set, and after it was done, the Creative team would give it a creative treatment. This was before Brady was on the Creative team.) Brady felt like a graveyard-focused set should be paired with a gothic horror plane. I agreed and spent years trying to make such a set a reality. It took a while, but finally, I was given the green light to make a set based on the horror genre.

*Magic* had tried a top-down block with *Champions of Kamigawa*, but it hadn't been considered a success, so I was hoping to use *Innistrad* to demonstrate how to do a top-down design. The key, I felt, was to have playing the set elicit the same emotions that watching a horror film or reading a horror novel elicited. The core emotion was fear. How do you make a game of *Magic* generate fear?

There were a couple ways. One was transformation. What if creatures could turn into scarier versions of themselves? That way the whole time they're on the battlefield, the opponent must worry about what they could become. Two was about making the normal unpredictable. What if there were things that normally happened in *Magic* that, in this set, might escalate things? We ended up choosing death as our "thing that normally happens in *Magic*," as it felt thematic. We combined this with a structure built around monsters and created a set that captured the feel we wanted.

We also leaned into a long list of tropes associated with the genre and designed cards to capture those tropes. We designed a lot of cards where we started with the name and designed the mechanics of that card to capture that name. The more evocative we got with the designs, the better the response we'd get in playtesting, and later from the audience. So much so, that emotional resonance became our guiding light for the set, and fundamentally, became the template for how we made future top-down sets.

## *Dark Ascension*

**Lesson: "Make the theme fun."** 

Back in the day, I normally did the first large set of the *Magic* year (the "fall" set), but the next large set was *Return to Ravnica*, and I thought it would be a good first large set for Ken Nagle to run, as returns are a bit easier to design than new planes (a lot of the structural issues and themes have already been worked out). This allowed me the opportunity to lead a small set, which wasn't something I had a lot of opportunity to do. In fact, I believe *Dark Ascension* is the only small "winter" set for which I've ever led the design.

The theme for *Dark Ascension* was that the humans were on the brink of extinction. Things had been bad in original *Innistrad*, but we needed to make things even worse to set up the third set in the block, *Avacyn Restored* (if the name didn't give it away, Avacyn is freed from the Helvault and returns to save the humans).

In early design, I spent a lot of time focusing on the plight of the humans. I made mechanics like fateful hour that played up how dire things were. Note that this was back when we had a design and development system, as opposed to the current vision design, set design, and play design structure. For the last two months of design, we had this period called "devign" where we would get feedback from the development team, and it allowed us to make changes to accommodate their issues.

Tom LaPille was the lead developer for *Dark Ascension*. His main note about the design was that it was "kind of depressing." We spent a lot of the set's resources on showing off the dire situation of the humans. But what about all the monsters? From their perspective, it's going great. They're getting more powerful and on the verge of accomplishing one of their biggest goals. Where is the excitement for the monsters?

Tom's comments really hit home for me. When a player plays a set, they're experiencing whatever it is they're playing. The fun of playing *Dark Ascension*, and *Innistrad*, was that you got to play the role of the monster. We needed to make that fun. The goal of the design wasn't to make you feel bad for what you were doing but rather let you enjoy it, to let you experience the visceral thrill of being a monster. That meant, for example, that I needed a splashy monster mechanic (which ended up being undying) and needed to play up the monster themes of the set. I did all that before the handoff to development, and it made the set much, much better.

I feel this was a very important lesson, and it's become a lens that I use on all new sets. Who are you, the player, becoming when you play the set, and how can we make that experience as exciting and as flavorful as we can?

## *Gatecrash*

**Lesson: "Make use of mechanics from other sources."**

The *Return to Ravnica* block ended up being a good year to help train some of my designers, so I let Ken Nagle lead the design for *Return to Ravnica* and then co-led the design for *Gatecrash* with Mark Gottlieb.

The biggest shift between the original *Ravnica* block and the *Return to Ravnica* block was that we changed how the block was structured and how we divvied up the guilds. The original *Ravnica* block consisted of one large set and two small sets, with four guilds in the large set and three guilds in each of the small sets. For the *Return to Ravnica* block, we shifted to a large-large-small block structure (although one could argue that the small one became a medium set), two with five guilds and one with ten. *Return to Ravnica* would have five guilds. *Gatecrash* would have the other five guilds. And *Dragon's Maze* would make use of all ten guilds.

Just before we began designing the *Return to Ravnica* block, I ran *Great Designer* *Search 2* (GDS2). For those unfamiliar with it, I was asked many years ago by Randy Buehler, my boss at the time, about how to find new design talent, and I came up with an out-of-the-box idea: what if we ran a design competition, like a *Magic* version of *Project Runway* or *Top Chef*? We'd let anyone who met certain basic requirements apply, and then we'd narrow them down to a small number of candidates who would participate in the event.

Each week, we'd give them a design assignment. Judges would then review those assignments, and one person would be eliminated. In the end, we'd have three finalists that would be brought to Wizards of the Coast for a series of interviews and a final live challenge. Five of the competitors from the first *Great Designer Search* would go on to get internships, four of which turned into full-time jobs at Wizards. The top two, Alexis Janson and Ken Nagle, each went on to lead the design of a set in the *Return to Ravnica* block (Ken led *Return to Ravnica*, and Alexis led *Dragon's Maze*).

For *Great Designer Search 2*, we changed how it worked. We asked each contestant for a plane idea, and then the challenges were about building up elements of that set. This would become important for *Gatecrash* design, because I used two mechanics that had been created during GDS2.

The first mechanic we used was evolve. Ethan Fleischer, who would go on to win *Great Designer Search 2*, was creating a prehistoric plane. He wanted a mechanic that showed evolution. The mechanic went on creatures that got +1/+1 counters if larger creatures entered the battlefield under your control. One of the five guilds in *Gatecrash* was the Simic, the green-blue guild. The Simic experiment with nature and had a +1/+1 counter theme on their first visit. Evolve seemed like a perfect fit. The *Gatecrash* design team tweaked how evolve worked (letting larger toughness trigger the counter as well as larger power), and the mechanic not only made it to print but even kept its name.

The second mechanic was battalion. In GDS2, runner-up Shawn Main designed a plane on the brink of extinction. He created a mechanic called assault, a creature mechanic that rewarded you for attacking with three or more creatures. *Gatecrash* had the red-white guild Boros, and it was a perfect fit. The *Gatecrash* design team again tweaked it (the creature it was on had to be one of the three creatures attacking), but the mechanic made it all the way to print.

Interestingly, there was a third guild mechanic also based on a GDS design, although this one wasn't in *Gatecrash*. Ken Nagle used his dispersion mechanic design from the first GDS to create overload, the Izzet mechanic in *Return to Ravnica*.

The lesson here is that mechanics (or cards, or themes) can come from anywhere. Yes, many things are created specifically for a certain set during design, but there must be a willingness to make use of the best idea regardless of where it comes from. An important part of any design is taking inventory of all the ideas we've come up with, including ones we haven't used, to see if one of them is a good mechanical fit for the current set.

## *Theros*

**Lesson: "Execution matters on a mechanic."**

The idea of a Greek mythology–inspired block went back to the early days of *Magic*. *Arabian Nights* was our first expansion, and its mere existence had R&D constantly talking about doing another set based on real-world stories. Greek mythology being the inspiration for a lot of *Alpha* was high on the list of choices. It became this theme we kept talking about but never did. That is, until a block idea we had got rejected late in the process.

The original plan for the *Theros* block "year" was to make a prehistoric world for the first set, a Middle Ages world for the second set, and a present-day world for the third set. The Creative team rejected this idea, as it would force them to build three different planes, and we were not well staffed at the time to do something like this. (We are now.)

As a result of this late change, we opted to do a theme we'd long talked about but never got to: Greek mythology. We committed early on to having an enchantment theme, and I loved the idea that the enchantments represented the influence of the gods. But how do we show the people's devotion to their gods? We felt this was an important part of the world, and thanks to the lesson above, we set out to explore what we'd done in the past before creating something new. Was there any mechanic that captured a sense of devotion? One of the suggestions was chroma.

The chroma mechanic came about during *Fifth Dawn* design. Aaron Forsythe pitched a card that cared about how many mana symbols were on cards in your hand. I thought it was a cool enough mechanic that it was worthy of being more than an isolated card and something we could do in volume. I ended up not putting the card into the set but held onto the design for future use. In *Future Sight*, I made a futureshifted card called Phosphorescent Feast that teased this mechanic.

![Phosphorescent Feast](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=126160&type=card) ![Phosphorescent Feast](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=151113&type=card)

I found a home for the mechanic, which ended up being an ability word called chroma, in a set a year later, *Eventide*. We even made sure to put the card Phosphorescent Feast in the set. *Eventide* had nine cards with chroma in the set. In market research, the mechanic fared poorly. Players were just unexcited by it.

This is why chroma being called out many years later was so interesting. It was a mechanic that we'd had such high hopes for but had failed miserably. Instead of just writing it off and assuming that its failure in *Eventide* was the sign of a bad mechanic, we were open to the idea that maybe we could do it better.

We made two main changes. One, we gave it a more concrete flavor—devotion. Two, we focused it to only look at permanents you control on the battlefield. Chroma had cards looking in different places (battlefield, hand, graveyard, etc.), and we felt that lack of focus kept you from building around it. Once devotion had a single focus, you could build on it as a theme.

Devotion would go on to be a giant hit that led to the big lesson of *Theros*: execution matters. You can take a good idea and squander it in how you make cards, in how you flavor it, in how you make it work with itself. A key part to constantly designing new material is to gain a critical eye for what shows potential, even if that thing's first outing didn't maximize it. What are the diamonds in the rough that *Magic* didn't execute well on but can redo and make memorable? This is true not just for mechanics, but themes, planes, and characters. We'll always make mistakes, but we must be careful not to throw out the proverbial baby with the bathwater.

## Live and Learn

That's all the time I have for today. I will continue doing this series when I find opportunities to do them, but they won't be right away. As always, I'm curious to hear your thoughts on today's column and any of the lessons. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for the start of *The Lord of the Rings: Tales of Middle-earth™* previews.

Until then, may your life be full of lessons.
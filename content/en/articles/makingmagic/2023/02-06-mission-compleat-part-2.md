---
id: ardh11jg
kind: article
lang: en
path: /en/articles/makingmagic/2023/02-06-mission-compleat-part-2
title: Mission Compleat, Part 2
published: '2023-02-06'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-2
    lang_detected: en
    capture_id: 223248
    url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-2
    captured_at: '2024-05-18 01:27:10+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-2
    lang_detected: en
    capture_id: 223248
    url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-2
    captured_at: '2024-05-18 01:27:10+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-2
    lang_detected: en
    capture_id: 223248
    url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-2
    captured_at: '2024-05-18 01:27:10+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-2
    lang_detected: en
    capture_id: 223248
    url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-2
    captured_at: '2024-05-18 01:27:10+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: ardh11jg
  url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-2
  page_key: magic.wizards.com/en/news/making-magic/mission-compleat-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:27:10+00'
  capture_id: 223248
  wayback_url: https://web.archive.org/web/20240518012710id_/https://magic.wizards.com/en/news/making-magic/mission-compleat-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ardh11jg
  capture_id: 223248
  url: https://magic.wizards.com/en/news/making-magic/mission-compleat-part-2
  wayback_url: https://web.archive.org/web/20240518012710id_/https://magic.wizards.com/en/news/making-magic/mission-compleat-part-2
  captured_at: '2024-05-18 01:27:10+00'
  template: contentful
  sha256: 388542d8005e4379009d5193673356f1817f4373ee2c3c4723975ba9f50fcf96
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
[Last week](/en/articles/makingmagic/2023/01-30-mission-compleat-part-1), I shared some card-by-card design stories from *Phyrexia: All Will Be One*. I'd gotten some feedback that my stories tend to focus on the higher rarity cards, so I wrote only about common cards in Part 1. Today, I'll tell some more card design stories but while addressing a different note from readers. I've been spending a lot of time showing the evolution of each card's design, and I got some feedback that people liked when I told stories that gave larger historical context for cards, so today's column is going to take that approach.

## The Compleated Planeswalkers

![](https://media.wizards.com/2023/one/en_b42628a03a.png) ![](https://media.wizards.com/2023/one/en_80b2b1b967.png) ![](https://media.wizards.com/2023/one/en_ea864f6cdf.png)

![](https://media.wizards.com/2023/one/en_d3095c961a.png) ![](https://media.wizards.com/2023/one/en_191f540645.png)

Planeswalkers first came about because Matt Cavotta swung by my desk to say, "I have an idea." Matt was on the *Future Sight* design team and at the time was part of the Creative team. They were working on the story for the *Time Spiral* block, an event called the Mending, which was created to allow us to power down the Planeswalkers as it was hard to relate to characters with godlike powers. Matt felt that we were doing so much to support having Planeswalkers that we should make them a card type.

I agreed, and we set out to see if we could make one. First, the *Future Sight* team worked on it with the idea that we'd have three of them on the futureshifted sheet, but it was clear by the time design ended that we weren't close enough. We decided to take the time to do it right and put them in whatever set made sense. We did, though, hint at them in the reminder text for Tarmogoyf.

I then put together and led a Planeswalker mini team. The team's earliest version was the design that we later adapted for Sagas. Eventually, we settled on a design, and planeswalker cards were introduced in *Lorwyn*.

I realized that planeswalker cards had a limited design space, so I was careful to have us slowly roll out additions to it. For instance, I didn't allow them to have static abilities (save some double-faced card shenanigans) until *War of the Spark*. This story begins when I was leading the vision design for *Kamigawa: Neon Dynasty*.

We'd outlined the Phyrexian storyline, and we knew Tamiyo was going to be Phyrexianized in *Kamigawa: Neon Dynasty*, Ajani in *Dominaria United*, and five other Planeswalkers (that hadn't been nailed down yet) in *Phyrexia: All Will Be One*. I was assigned the task of figuring out what it meant to be a Phyrexianized planeswalker card.

My first idea—the one I was most excited by—was Phyrexian loyalty, which let you spend life in place of loyalty. Play Design told me that this was inherently broken. I ended up producing a document that suggested five other possible ways to do it, each with several tweaks. For the first time ever, here were my five suggestions, along with my sub-suggestions:

#### Suggestion #1: Make Use of Poison

The Phyrexians are associated with poison, so I designed a bunch of versions that used poison as a restriction.

*   All loyalty abilities grant you poison.
*   Some abilities, mostly plus loyalty abilities, grant you poison.
*   Forced proliferate grants a little poison.
*   Loyalty abilities that can grant you poison if you choose to push them.
*   Loyalty abilities that sometimes grant you poison (based on certain things happening).
*   Granting poison as a static ability to stop you from keeping them for long.

#### Suggestion #2: Make Use of Life Loss

In *Scars of Mirrodin* block, we associated the Phyrexians with life loss, so that was another theme we explored. Most of the themes were the same ones we tried with poison.

#### Suggestion #3: Make Use of Sacrifice

Sacrifice was another Phyrexian theme in *Scars of Mirrodin* block, so we also experimented with using that as a cost. Again, structured similarly to how we did poison.

#### Suggestion #4: Make Use of Proliferate

Proliferate (along with poison and Phyrexian mana, the three P's of Phyrexia) was strongly associated the Phyrexians, so we explored this as a theme.

*   Every planeswalker has +0: Proliferate.
*   Every planeswalker references a kind of counter, and proliferate is on at least one ability.
*   Proliferate forces you to proliferate your own poison counter; some could come with one.

#### Suggestion #5: Make Use of the Library as a Resource

The library is not as associated with the Phyrexians, but it was a resource that you tend to have more of, so it gave us additional flexibility in costing. All these versions exiled cards from your library and usually gave you some way to use some of them.

All these ideas were explored, but in the end, none of them were used. Instead, they found a version that let them use Phyrexian mana by adding an additional cost (giving up loyalty). I like to use this as a good example of how some ideas require a lot of time and attention to find the proper answer. I am happy with how they ended up.

## The Mites

![](https://media.wizards.com/2023/one/en_4f99e651ee.png) ![](https://media.wizards.com/2023/one/en_ef3854b73c.png) ![](https://media.wizards.com/2023/one/en_441139231a.png)

![](https://media.wizards.com/2023/one/en_b3d1a4252b.png) ![](https://media.wizards.com/2023/one/en_d20e41ba8d.png) ![](https://media.wizards.com/2023/one/en_0caa9cbecf.png)

![](https://media.wizards.com/2023/one/en_acc3e52c76.png) ![](https://media.wizards.com/2023/one/en_71adbaba56.png) ![](https://media.wizards.com/2023/one/en_ca3a1d712d.png)

![](https://media.wizards.com/2023/one/en_2beab85e6f.png) ![](https://media.wizards.com/2023/one/en_c289509670.png)

When *Alpha* came out, the internet was young. The World Wide Web was just gaining ground, and most talk online was through a thing called the Usenet (kind of like a bulletin board). In addition, Richard Garfield's original vision was that players would discover what cards existed through playing with other people. As part of this in the early years, Wizards of the Coast did not publicly print card lists or show decklists from events. This meant that what was most popular in *Alpha* early on were cards that just excited people, regardless of their power level, as most players didn't yet have the skills to judge what was strong and there were no public expert opinions.

There was one card I really wanted, but no one would trade it away, so the only way to get one was to open it in a booster (which I excitedly did). What was that card? Take a guess and then click below to see the answer.

## Click here for the answer

![The Hive](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=43&type=card)

Yes, believe it or not, one of the hottest cards in the early days of *Magic* was The Hive. My best guess as to why is that this was a top-down design and the use of creature tokens was the only way Richard could think to make it. The reason I think players were drawn to it is that creature tokens are cool. Plus, it was one card capable of making many creatures, something no other *Alpha* card could do. Richard would make two more cards that made creature tokens in *Arabian Nights* (Rukh Egg and Bottle of Suleiman), and the ball just started rolling from there. Creature tokens became evergreen.

*Fallen Empires* was the first set to use creature tokens as part of a larger mechanical theme, of which Saprolings were a part (a creature type that to this day we only make on creature tokens). There were so many tokens and counters in the set that Wizards of the Coast made a punch-out sheet with all of them and put it into an issue of *The Duelist* (*Magic*'s magazine from back in the day).

*Apocalypse* made the penumbra mechanic (unnamed) where several green creatures created black creature tokens of their size when they died. *Odyssey* block made extensive use of creature tokens to make flashback spells that functioned a lot like creatures. *Onslaught* made a handful of symbiotic creatures that died into a number of 1/1 tokens equal to their power/toughness (all square).

Creature tokens started becoming a larger mechanical theme that we could tie into. For example, the mono-green theme in the original *Ravnica* (each color had a theme that overlapped its two colors) was token making. *Unglued* introduced creature token cards, and they started showing up in boosters by *Tenth Edition*.

In *Rise of the Eldrazi*, we were trying to make "battlecruiser *Magic*" where giant creatures could fight each other on the battlefield. To pull this off, we needed a way to help ramp mana while helping you cast your Eldrazi and not just any spell.

One of the answers to this problem was to design a creature token with a special function. These became Eldrazi Spawn tokens, which had the ability "Sacrifice this creature: Add <>." The idea of making unique creature tokens to support a set theme became another tool in our design toolbox. *Battle for Zendikar* had Eldrazi Scion tokens. *Strixhaven: School of Mages* had Pest tokens.

However, we noticed a problem with our desire to make creature tokens as larger themes. Tokens gummed up the board, making them more efficient defensively than offensively. *Theros Beyond Death* had 1/1 red Satyr tokens, and we found that they were causing problems, so the solution was to give all Satyr tokens "can't block." This helped focus them as being an offensive threat. We encountered a similar issue when making the Zombie tokens for *Innistrad: Midnight Hunt*. We gave them "can't block" and created a new decayed mechanic that required players to sacrifice them at the end of combat after attacking.

This brings us to *Phyrexia: All Will Be One*. We wanted white to have a swarm poison strategy, but there simply weren't enough 1/1 creatures. Creature tokens were the solution to that problem because they allow one card to generate more than one creature. They obviously needed toxic 1, as they were core to a poison strategy, but we weren't sure at first whether they needed "can't block." After all, wasn't toxic enough of an incentive to save your creature for an attack?

So, we had a playtest to see if that would hold true, and it didn't. Using your 1/1 token creatures as a disincentive for your opponent attacking and chump blocking big attackers just proved to be too efficient, so we added on "can't block."

We then looked for various ways to create a number of Mite creature tokens, like when a creature enters the battlefield or dies. It could be after an attack trigger or an upkeep trigger, or by using spells that made more than one. In combination, they did exactly what we wanted and gave white an amazing tool to allow a very specific kind of threat, one I hope you all get to experience firsthand on your side of the table.

## The Myr

![](https://media.wizards.com/2023/one/en_7c12a3108e.png) ![](https://media.wizards.com/2023/one/en_d651eb31ee.png)

![](https://media.wizards.com/2023/one/en_440bb7a7fc.png) ![](https://media.wizards.com/2023/one/en_11e879baac.png)

When I started designing original *Mirrodin*, one of the first things I created was the cycle of mana Myrs (Gold Myr, Silver Myr, Leaden Myr, Iron Myr, and Copper Myr). I liked the idea that on this artifact-themed plane, the common mana stones would be on creatures. This allowed me to make them at two mana, as being creatures would give them extra vulnerability.

For their creature type, I chose Gnome. Why Gnomes? Gnomes had oddly become an artifact creature type and were used on a bunch of small artifact creatures in the early years of *Magic*, and the public, myself included, found them endearing.

Then one day, Brady Dommermuth came to visit me. Brady would later go on to become the creative director of the Creative team, but this was before that happened. Here, with a bunch of dramatic license, was our conversation:

**Brady**: Gnomes?!  
 **Me**: What about them?  
 **Brady**: You have Gnomes in the set?  
 **Me**: Yes.  
 **Brady**: Why?  
 **Me**: Because they're adorable, and players like them.  
 **Brady**: So, when this artificial plane was created, someone said, "You know what we need? Gnomes."  
 **Me**: I take you don't like it being Gnomes.  
 **Brady**: It just doesn't make any sense from a story perspective. Why do you want it to be Gnomes?  
 **Me**: I just wanted a little softness, something players could find lovable.  
 **Brady**: Okay, what if I make a brand-new artifact creature that's lovable? Something new to this plane. Would that be okay?  
 **Me**: Sure.

Brady then went away and came back a month or so later with the earliest design of the Myrs. I believe they were influenced by the Myrmidons from Greek mythology, so Brady called them Myrs. (It rhymes with "deer.") I thought they were great. So much so that we added a bunch more to the file. *Mirrodin* came out, and Myrs were a huge hit.

After *Mirrodin* block was done, the Myrs went away as they're specifically from Mirrodin. The next time one would appear would be Sarcomite Myr in *Future Sight*. It was one of the futureshifted cards that showed potential futures of *Magic*.

![Sarcomite Myr](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=136212&type=card)

The card was meant as a big hint of what was going to happen when we returned to Mirrodin. We had subtly set up the Phyrexian invasion in our first visit (for example, Memnarch literally encounters a strange oil in the beginning of the book), and Sarcomite Myr was a hint of what was coming. Interestingly, it's the first monocolor artifact, as I expected to make use of monocolor artifacts as a main mechanical theme when we returned, but the idea ended up getting used first on the shard of Esper in *Shards of Alara* block.

The Myr returned in *Scars of Mirrodin* block. Like many of the denizens of Mirrodin, we watched some of them fall to the Phyrexians. A few showed up in *Modern Horizons 2* on cards set on New Phyrexia. Which brings us to *Phyrexia: All Will Be One*.

We were returning to New Phyrexia, formerly Mirrodin, the only plane where the Myrs exist, so we knew we wanted some new ones. The set had a lot going on, so in the end, there was only room for three in the main set and one in a Commander deck. We did make sure the Commander card was a Myr build-around with a five-color identity. All four Myrs were made colorless, with only one being a Phyrexian. We wanted to show that while many Myrs had fallen to the Phyrexians, not all of them had.

We tied the one Phyrexian Myr, Myr Convert, to the toxic mechanic with a second ability that was a throwback to the original mana Myr cycle, although with a life payment to make it feel more Phyrexian. Myr Custodian was made to help with deck smoothing, something all decks could use. Myr Kinsmith was made to interact with Myrs, giving it a little utility in Limited but a much more powerful effect in larger formats where you have access to more Myrs.

Looking back, I'm so glad Brady steered me away from making Gnomes.

## The Spheres

![](https://media.wizards.com/2023/one/en_bbaa347c47.png) ![](https://media.wizards.com/2023/one/en_89cef29691.png) ![](https://media.wizards.com/2023/one/en_436167f14a.png)

![](https://media.wizards.com/2023/one/en_7f3f266b81.png) ![](https://media.wizards.com/2023/one/en_c289509670.png) ![](https://media.wizards.com/2023/one/en_33108288ee.png)

![](https://media.wizards.com/2023/one/en_c754d6e960.png) ![](https://media.wizards.com/2023/one/en_2f469ea9c0.png) ![](https://media.wizards.com/2023/one/en_f6b7c3ebee.png)

The story of the Spheres begins with the design of *Return to Ravnica* back in 2012. We were going back to Ravnica, so we went back and looked at the original *Ravnica* to figure out what we could improve upon. The number-one answer was the color fixing. Ravnica had been revolutionary in many ways, but it came up short because it was often hard to play three-color decks, something the *Ravnica* block encouraged, especially in Draft when you added the second and third sets of the block.

We decided that we wanted it (and *Gatecrash*) to have a cycle of common dual lands and a cycle of rare dual lands. The best option for the common dual lands were the tap lands (dual lands that enter the battlefield tapped; they first appeared in *Invasion* block), and the best option for the rare dual lands were the shock lands (dual lands that enter the battlefield tapped unless you pay 2 life; they first appeared in the original *Ravnica* block). The problem was that the rare duals were "strictly better" than the common lands—that is, they did what the common dual lands did, but with a bonus. We're fine making strictly better cycles, but we tend to avoid making them in the same set.

This raised the question: could we tweak the tap lands? They were a bit on the weak side, so we had room to add some additional ability. What did that ability want to be? Also, could it be something that felt like it specifically belonged in Ravnica?

The answer came from the Creative team. They'd been building out the plane, as we do on returns, and came up with a concept of each guild having a gate. It was going to play a role in the larger story. What if we flavored each dual land as a Gate?

The next question: how do we make them different mechanically. We explored a lot of options but landed on the idea of doing a land subtype. In the beginning, land subtypes were just the five basic land subtypes, but over time, we started making more use of them. They began appearing on card type lines in *Eighth Edition* to solve some rules issues. We also went back on things like the Urzatron to use subtypes to help the cards mechanically function. We used them sporadically but usually to make cards work individually and not simply as a marker (although Desert retroactively became one).

The plan was to have the common dual lands be subtype Gate and have a handful of cards that cared about Gates so the cards would have some extra functionality. This was a bit controversial at the time, but it seemed like the cleanest execution, so we got everyone on board. Gates went on to be a success.

![](https://media.wizards.com/2022/images/daily/aYEJyRGKk0.jpg)

Phyrexian Atlas | Art by: [Illustranesia](https://web.archive.org/web/20230206000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&artist=+[%22Illustranesia%22])

Flash forward to *Phyrexia: All Will Be One* design. New Phyrexia, in trying to reflect old Phyrexia, created nine spheres. It was an important story point, so we wanted to reflect it in the set if possible. That raised the question: how exactly do we communicate that New Phyrexia has nine Spheres? Yeah, we could mention it in flavor text or a card title, but neither of those seemed grand enough. The solution was to borrow the same trick we used with Gates.

Phyrexia has nine lands representing the nine Spheres of the plane. We then had one card, Monument to Perfection, mechanically reference them. Five of them became part of a common cycle that was used to add some card flow in the late game. Each one represented one of the five colors. This was done by looking at the nine available Spheres and picking the one that felt like it captured the aspect of one of the five colors most. The remaining four were then designed top down and put at rare.

## Compleat Success

That's all the time I have today. I hope you enjoyed my stories. As always, I'm eager for any feedback. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for the *Phyrexia: All Will Be One* vision design handoff document.

Until then, may you visit all nine spheres of New Phyrexia.
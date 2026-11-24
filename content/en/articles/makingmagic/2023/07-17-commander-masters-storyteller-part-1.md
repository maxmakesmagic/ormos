---
id: txjrjkm6
kind: article
lang: en
path: /en/articles/makingmagic/2023/07-17-commander-masters-storyteller-part-1
title: Commander Masters Storyteller, Part 1
published: '2023-07-17'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
    lang_detected: en
    capture_id: 214384
    url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
    captured_at: '2024-06-04 05:33:23+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
    lang_detected: en
    capture_id: 214384
    url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
    captured_at: '2024-06-04 05:33:23+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
    lang_detected: en
    capture_id: 214384
    url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
    captured_at: '2024-06-04 05:33:23+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
    lang_detected: en
    capture_id: 214384
    url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
    captured_at: '2024-06-04 05:33:23+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: txjrjkm6
  url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
  page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
  lang: en
  template: contentful
  captured_at: '2024-06-04 05:33:23+00'
  capture_id: 214384
  wayback_url: https://web.archive.org/web/20240604053323id_/https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: txjrjkm6
  capture_id: 214384
  url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
  wayback_url: https://web.archive.org/web/20240604053323id_/https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-1
  captured_at: '2024-06-04 05:33:23+00'
  template: contentful
  sha256: efcd940c08b0a43d6d940645add2611f00d9f24b74923dfac9b0d3cb5d9a5de2
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email me
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
[Last week](/en/articles/makingmagic/2023/07-11-chain-of-commander-masters), I talked about the vision design and set design of *Commander Masters*. This week and next, I'll be telling some card design stories from the set.

**Avacyn, Angel of Hope**

![Avacyn, Angel of Hope](https://media.wizards.com/2023/cmm/en_17250e478e.png)

**Avacyn, Angel of Hope**

![Foil-Etched Avacyn, Angel of Hope](https://media.wizards.com/2023/cmm/en_f3f8126905.png)

**Foil-Etched Avacyn, Angel of Hope**

The initial plan for the original *Innistrad* block was to have two sets, a large and a small, that take place on one plane, share mechanics, and draft well together. The third set in the block would be large, take place on a different plane, have a new set of mechanics, and be drafted by itself. Originally, that final third set was going to take place on Innistrad. Brady Dommermuth and I had been pushing to do a top-down gothic horror set for years. Finally, Bill Rose, the VP of *Magic*, gave in and gave us one large set to do it in.

For the other two sets, R&D would run a company-wide contest to come up with a new plane. Tons of people submitted ideas, and the winner was a plane created by Brian Tinsman. Then, right before the fall set design was about to begin, Mark Globus brought up to Bill that it was weird to have a gothic horror set not release in October, near Halloween. Bill came to me and asked if there would be enough material to move *Innistrad* from May to October. I said the genre of horror was vast and popular, and we'd have plenty of material, so it was moved. The spring set would now become the plane that Brian pitched.

Brady Dommermuth, who led the Creative team at the time, didn't feel they were staffed up to design two new planes (we are now). Just as he had done with the *Zendikar* block two years earlier, he pitched having an event big enough to happen on the plane that justified new mechanics without having to go to a whole new plane. Brady's pitch was to have the first two sets be about the monsters attacking humans and humans being on the brink of extinction. The third set would be about something that turned things around and put the monsters on the back foot.

That something would end up being the Archangel Avacyn. Sorin had created her to keep the humans alive so that the vampires wouldn't lose their food source. Avacyn had been tricked by the demon Griselbrand and trapped in something called the Helvault. The events of the block ended up forcing Thalia to open the Helvault, releasing both Griselbrand and Avacyn. It's Avacyn being freed (restored) that sets everything in motion.

This meant that the card design for Avacyn had to be something spectacular. It was the linchpin of the whole set, so much so that her name was in it. Here's what we knew she had to be:

*   An Angel
*   A mythic rare
*   A creature with a high mana value
*   A creature with flying and vigilance
*   A savior

Here was my first pitch:

**Avacyn**  
 4WWW  
 Legendary Creature — Angel  
 7/7  
 Flying, vigilance, trample  
 Prevent all damage dealt to CARDNAME and any other creature you control.

She's daunting, protects your stuff, and can single-handedly win the game. I thought it was a great design. Brian Tinsman, who was the lead designer of the set, wanted to explore other options. The big mechanic we were playing with in design was called forbidden. Forbidden cards couldn't be put into your deck. You had to play specific cards that shuffled them in. Because there was such a large hoop to jump through, we could under-cost the cards. For example, we thought we might be able to make a forbidden version of Ancestral Recall (it costs a single blue mana to draw you three cards).

We went through many iterations of Avacyn designs that used forbidden. Little by little, she started becoming less defensive in flavor and more offensive. She began boosting your team and made Angel creature tokens. Eventually, development put their foot down on the forbidden mechanic and we removed it from design. (It was one of the things that influenced the design of Lessons and learn in *Strixhaven: School of Mages*.) The next batch of designs saw Avacyn getting even more aggressive, with such abilities as destroying other creatures.

I felt we were moving in the wrong direction. To me, Avacyn was supposed to represent the opposite of the monsters. Instead of destruction, she should represent salvation. If she acted too much like the monsters, I felt like the theme of the set would be darker than we wanted. So, I pitched we go back to my very first design. We did make one major change: instead of preventing the damage, we made her have and grant indestructible. We felt that it played similarly and just read a lot more exciting.

Development fiddled with her mana value, power, and toughness (and removed trample) but otherwise kept the design as we'd turned it in.

**Body Double**

![Body Double](https://media.wizards.com/2023/cmm/en_87e71a3e00.png)

**Body Double**

To become a good game designer, you need to enjoy playing games, so it shouldn't come as a surprise that game designers like to make little games out of designing. Body Double is a great example of one of these little games. Each color has its own slice of the color pie, a list of effects that it's allowed to do. (Here's a link to [my latest version of the "Mechanical Color Pie" article that spells out what all these abilities are](/en/articles/makingmagic/2021/10-18-mechanical-color-pie-2021).) By combining things in color, you can often design cards that are out of color.

The classic example of this is a green creature with the following text:

**Surprise Snake**  
 1G  
 Creature — Snake  
 1/1  
 Flash  
 Deathtouch  
 When CARDNAME enters the battlefield, it fights target creature.

Green is secondary in both flash and deathtouch and primary in fight, but one of its weaknesses is that it's bad at pinpoint creature destruction. If green wants to destroy an opponent's creature, it must use its own creature to do that. Technically, this spell does that but in a way that grants green a spell that is too much like a black creature kill spell. For example, if you had an empty board, you could use this spell to kill any one creature on the battlefield. That shouldn't be something green can do. What this means is even though the card can technically be assembled in color pie, the totality of it is out of color pie and thus isn't something we should print.

Nonetheless, it's fun to design cards that allow one color to mimic another color's abilities. We don't often print them, but we do design them for fun. Body Double is a perfect example. One day, it dawned on me that I could use copying to basically make a reanimation spell in blue. I had nowhere to put it because blue isn't supposed to be able to reanimate creatures from the graveyard, but I was tickled by the design.

Then came *Planar Chaos*, the middle set in the *Time Spiral* block. The block had a past, present, and future theme. Past and future were obvious themes, but I struggled a bit with what "present" meant as a theme. Wasn't almost every expansion set in the present? Eventually, I came up with the idea of an "alternate reality present" where we could see *Magic* if it had made different choices. We redid the color pie and leaned into the weirdness this little game played into.

This made *Planar Chaos* a home for cards that dipped into the mechanical spaces of other colors. I finally had a set for Body Double. Looking back, especially in a world of Eternal play where cards never leave the system, I now believe *Planar Chaos*, at least the color-twisting aspect of it, was a mistake, but it did allow cards like Body Double to see print.

**Chainer, Dementia Master**

![Chainer, Dementia Master](https://media.wizards.com/2023/cmm/en_c868c2c3b3.png)

**Chainer, Dementia Master**

![Foil-Etched Chainer, Dementia Master](https://media.wizards.com/2023/cmm/en_21326238ab.png)

**Foil-Etched Chainer, Dementia Master**

At the time that this card was designed (in *Torment*, part of the *Odyssey* block), the story was told in novels written by freelance writers. During design, we'd get a simple outline of what the story would be as it hadn't been written yet. Chainer was a character scheduled to appear in the book *Odyssey*, which told the story of the set *Odyssey*, and was planned to be the protagonist in the second book *Chainer's Torment*. Because we knew he was going to be the main character in the second book, we saved his card, Chainer, Dementia Summoner for the second set, *Torment*.

Chainer was what was known as a dementia summoner, meaning he had the power to pull literal nightmares into reality. Okay, how exactly does a card convey that mechanically? We knew we wanted him to create Nightmares. Maybe they could be creature tokens? At the time creature tokens were mostly vanilla creatures (flying was the only keyword we regularly used on creature tokens), so it didn't quite feel scary enough.

We then explored the idea that he could get creature cards onto the battlefield and grant them the Nightmare creature type. This was a mono-black card, so there was only one option to move cards from a zone onto the battlefield—reanimation. We made it cost a bunch of black mana, as it felt particularly black, and then added in a life payment because it captured the personal cost of dementia summoning. Next, to balance the card, we made it such that the Nightmares would leave play if Chainer did. This would allow the opponent to have an answer to all the Nightmares. We ended up making it exile, so a second copy of Chainer couldn't bring back the same creatures.

Interestingly, the ability that caused all the conversation was the first one on the card, granting +1/+1 to all Nightmares. (This was at a point in design where typal designs affected all creatures of that type, not just the ones you control.) One of the mechanics in the set, which was unnamed on the cards, was dubbed the nightmare mechanic in all our marketing. In *Torment*, it went on black and red creatures, all of which were creature type Nightmare. The black Nightmares removed something of the opponent's (a creature, cards in hand, life, etc.) until it left the battlefield. The red Nightmares removed something of yours but were cheaper.

At the time, our policy was to not put set mechanics on legendary creatures. Remember, this is before Commander existed as a format and legendary creatures were significantly smaller in number. There was worry that referencing Nightmares was breaking our rule. There were many conversations about whether an unnamed mechanic even counted as a mechanic for this rule. (It was deemed that it did.) It turned out that referencing Nightmares was the only way to make the last ability work, so the card had to do it. Once we realized that, we decided that it was okay to reference it twice on the card if we were already doing it once. Eventually, we would make the realization that legendary creatures wanted the set mechanics where appropriate as it helped make them feel more tied to the set and allowed players more access to them.

**Fact or Fiction**

![Fact or Fiction](https://media.wizards.com/2023/cmm/en_09841a2d3b.png)

**Fact or Fiction**

![Borderless Fact or Fiction](https://media.wizards.com/2023/cmm/en_606a162bf8.png)

**Borderless Fact or Fiction**

When I was initially hired into R&D, it was not as a designer but as a developer. I was upfront from the beginning that adjusting power level was not my area of expertise. I relied on other members to do that. Things imploded power-wise during *Urza's Saga* block, so much so that for the first and only time in my 28 years at Wizards, R&D was called before the CEO and chewed out.

I went to Bill, then head designer, and suggested that there was a great resource for finding new R&D members, specifically ones that could better judge power level. That source was the Pro Tour. I'd been involved with it since its beginning and was, at the time, attending them all. My first suggestion for an employee to hire was Randy Buehler. I'd gotten to know Randy from the Pro Tour and thought he'd be a good fit for R&D, and he was eventually hired.

The first set Randy worked on was *Invasion* as part of the development team. While I wasn't the lead of the development team, I was on the team, and I was constantly encouraging Randy to find spells that we could push that would lead to fun tournament play. The card he latched onto most was Fact or Fiction.

One of the themes in *Invasion* was a mechanic we nicknamed "divvy." The way divvy worked was that one player would divide some number of cards into two piles, then the other player would choose one pile. Where the cards came from, what you did with them after, who made the piles, and who chose a pile—all of that varied from card to card.

The version that ended up being the coolest was the blue one that drew cards. Randy really liked it because the power level of the card was very dependent on the skill level of the two players. It was super Spike friendly. Also, at its worst, it was just a card-draw spell. Even if it was a little on the strong side, Randy felt the potential downside was curbed. The card wouldn't win games by itself, but it would let the more skilled player have an edge, and Randy thought that was great.

Fact or Fiction became the card Randy rallied around about how to push cards in a way that would excite the Spikes of the world without causing the game to break. He fought very hard to be aggressive with the costing. In the end, it did exactly what Randy wanted. It was a powerful but fun card that showed up in tournament formats yet never inherently caused major problems.

**Hanna, Ship's Navigator**

![Hanna, Ship's Navigator](https://media.wizards.com/2023/cmm/en_45f1ad97da.png)

**Hanna, Ship's Navigator**

![Foil-Etched Hanna, Ship's Navigator](https://media.wizards.com/2023/cmm/en_b3a583b211.png)

**Foil-Etched Hanna, Ship's Navigator**

All *Magic* players have pet cards, and that includes the designers. The big difference about being a *Magic* designer is that you can use old favorites to inspire new designs. Hanna, Ship's Navigator is one such design. I took two old-time favorite cards of mine and smashed them together.

![Argivian Archaeologist](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=159743&type=card) ![Skull of Orm](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=1721&type=card)

Let's now go back to my time before working at Wizards. I was living in Los Angeles and was a Johnny who enjoyed making weird decks that won in strange and fun ways. One of my favorite tools was getting permanents back out of the graveyard. One-shot spells were okay, but I preferred having permanents that could do it repeatedly. I tended to enjoy designing decks that built up as the game progressed.

I was excited by Argivian Archaeologist the first time I saw it. *Antiquities* had an artifact theme, which was exciting to me, so having a way to constantly get back my artifacts was an instant draw. I built so many different artifact-themed decks, and most of them included the Argivian Archaeologist.

When *The Dark* came out, I had the same reaction to Skull of Orm. It was more expensive to use than the Archaeologist, but there really wasn't any other repeatable way to get enchantments back from the graveyard, so I used what I had to work with. Again, a lot of fun decks were made. A few even used both, although usually my decks were themed to use artifacts or enchantments.

Flash forward a couple of years. Michael Ryan and I pitched the *Weatherlight* Saga. I was careful to slowly dole out the crew members across sets. Finally, it was time to make a card for Hanna. She was the engineer of the crew, specializing in magical objects (much to her father Barrin's dismay, as he wanted her to be a wizard). It dawned on me that this would be the perfect opportunity to make a new Argivian Archaeologist. It was a perfect flavor fit. I then realized that maybe I could go one better than *Antiquities* had done. Upkeeping the boat involved some magical spells, maybe I could also update the Skull of Orm. Perhaps both effects could be on a single card?

Hanna was a character that I had grown very fond of, and I wanted her to have a card that would excite players, so the idea of taking two pet cards that had meant so much to me and combining them into something better seemed like a golden opportunity. And that is how Hanna, Ship's Navigator got her ability.

**Mikaeus, the Unhallowed**

![Mikaeus, the Unhallowed](https://media.wizards.com/2023/cmm/en_e609c5a1e9.png)

**Mikaeus, the Unhallowed**

![Foil-Etched Mikaeus, the Unhallowed](https://media.wizards.com/2023/cmm/en_bda3a8a960.png)

**Foil-Etched Mikaeus, the Unhallowed**

![Borderless Profile Mikaeus, the Unhallowed](https://media.wizards.com/2023/cmm/en_8a553a6a2f.png)

**Borderless Profile Mikaeus, the Unhallowed**

![Textured Foil Borderless Profile Mikaeus, the Unhallowed](https://media.wizards.com/2023/cmm/en_1330ab21a4.png)

**Textured Foil Borderless Profile Mikaeus, the Unhallowed**

When *Innistrad* block design started, the story had only been loosely outlined. Here are my notes from the time:

"Shake" – Meet the monsters; humans are on brink of extinction.

"Rattle" – Things get worse for the humans.

As I mentioned in my section on Avacyn, the third set wasn't even set on Innistrad yet.

When planning blocks, I like to create some kind of progression in the cards. In *Mirrodin* block, we hinted at cards that hadn't been printed yet. In *Ravnica* block, we made ten-card cycles that we doled out a little each set. In *Scars of Mirrodin*, we watched a mechanic, infect, spread to new colors. What could we do in *Innistrad* block across multiple cards that could convey the plight of the humans? What could happen that would devastate the humans most?

Worldbuilding was in its early state, but the Creative team had come up with the idea of the humans having a religion that they leaned on for support. I don't believe Avacyn had even been created yet, as I think that was part of creating the event that justified staying on Innistrad but changing to new mechanics. Obviously, if there was a religion, there had to be a religious leader. What if we introduced him in *Innistrad* and then turned him into a monster in *Dark Ascension*? That seemed the perfect embodiment of the death of hope. Things have gotten so bad that the person they look to for guidance has fallen. I pitched the idea to the Creative team, and they liked it.

![Mikaeus, the Lunarch](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=247234&type=card)

To show contrast, we made the Human Mikaeus, the Lunarch mono-white. (Humans were primarily in white and green, and him being a religious leader made more sense in white). The key quality we wanted to play up was that he helped his people, so we gave him a mechanic that allowed him to turn a +1/+1 counter on himself into a +1/+1 counter on all your creatures. We talked about him only putting a +1/+1 counter on your Humans, but it felt a little too narrow.

Then in *Dark Ascension*, it was time to make the Zombie version. We wanted some mechanical parallel between the two cards so they felt like the same character. The obvious choice was to have him now boost the monsters. Undying was the keyworded monster mechanic in the set, so we had him grant that and added an extra +1/+1 because players like that on creature lords (creatures that grant typal rewards).

![Mikaeus, the Unhallowed](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=249896&type=card)

It was important that the card felt specifically anti-Human to help play up the transformation into monster. We ended up using the ability from the card No Mercy, although only for Humans. I should note this was more trinket text (text added more for flavor than mechanics). Finally, we gave him intimidate, partly for a feel, partly to play with his 5/5 body. I enjoy how the two cards ended up and love how the evolution did a great job of hinting at the larger story in an emotional way.

## "Storytime Is Over"

That's all the time I have for today. I hope you enjoyed my stories. If you have any feedback about today's column, any of the cards I talked about, or *Commander Masters* in general, you can email me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for part two.

Until then, may you make stories of your own with these cards.
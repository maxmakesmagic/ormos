---
id: wm1ebwm8
kind: article
lang: en
path: /en/articles/makingmagic/2023/07-24-commander-masters-storyteller-part-2
title: Commander Masters Storyteller, Part 2
published: '2023-07-24'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
    lang_detected: en
    capture_id: 214392
    url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
    captured_at: '2024-05-18 01:13:12+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
    lang_detected: en
    capture_id: 214392
    url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
    captured_at: '2024-05-18 01:13:12+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
    lang_detected: en
    capture_id: 214392
    url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
    captured_at: '2024-05-18 01:13:12+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
    lang_detected: en
    capture_id: 214392
    url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
    captured_at: '2024-05-18 01:13:12+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: wm1ebwm8
  url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
  page_key: magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:13:12+00'
  capture_id: 214392
  wayback_url: https://web.archive.org/web/20240518011312id_/https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: wm1ebwm8
  capture_id: 214392
  url: https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
  wayback_url: https://web.archive.org/web/20240518011312id_/https://magic.wizards.com/en/news/making-magic/commander-masters-storyteller-part-2
  captured_at: '2024-05-18 01:13:12+00'
  template: contentful
  sha256: ba8e6c0be1261af7a92620c42c86980688c9cb9c8e3d38c0b0f97e62fead0668
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
[Last week](/en/articles/makingmagic/2023/07-17-commander-masters-storyteller-part-1), I started telling card-by-card design stories from *Commander Masters*. I had so many stories to tell, I'm continuing today.

**Morophon, the Boundless**

![Morophon, the Boundless](https://media.wizards.com/2023/cmm/en_80d24fc5ee.png)

Part of my job is interacting with players. As such, I get a lot of design requests. One of the most popular requests of the last ten or so years is, "Can you make me a Commander for my (fill in the creature type) deck?"

Typal themes are very popular, *Magic* has many creature types, and we keep making new ones. While there are a bunch that have a legendary creature that mechanically rewards you for playing that creature type, a lot don't. And while we'll keep designing new ones, because players enjoy them so much, there are a lot of creature types that we haven't gotten to yet.

This story begins during the Hackathon for *Modern Horizons*. Ethan Fleischer and I had each pitched the idea of a supplemental set with a higher complexity that made use of *Magic*'s full history of mechanics. We had a week and a dedicated team to design enough cards to give the managers of R&D a sense of what we envisioned.

We designed a *lot* of cards that week. One of my inspirations was to design cards I'd always wanted to design, but never had the right place to put them. One of the items was a catch-all typal lord that would allow any player the opportunity to have a Commander for their pet creature type. For sake of historical accuracy, I'm not sure whether this card was designed at the Hackathon or in early vision. It got added to the file in early vision, but my memory is that I originally made it during the Hackathon, so it's possible the card got designed a bit before it got put in the file.

Here's what I knew the card needed going into the design:

*   **It needed to have a generic mana cost.**

In order for it to be useable with any creature type, it had to work in any deck. The cleanest and easiest way to do this was to give it a generic mana cost.

*   **It needed to have a five-color color identity.**

It can be tricky to build a Commander deck out of less popular creature types, so I wanted to make sure that you could include all the colors in the deck.

*   **It needed to let you pick a creature type.**

My goal wasn't to make a card that rewarded you for playing lots of creatures. It had to reward you for playing a specific creature type. Luckily, "choose a creature type" had been a tool in our toolbox for many years.

*   **It needed to be generally useful.**

The design had to be very flexible because it had to work with all creature types. That meant whatever bonus I gave had to work with basically any creature.

That's it. I only had four goals for the design. The problem was that they didn't necessarily play nicely with one another. For example, a generic cost makes it trickier to have a five-color identity, so I had to have the colored mana symbols in the text box.

I started by asking what would benefit all creature types? The best two answers I came up with were pumping them and making them cheaper. All creatures have a power, a toughness, and a mana cost. It was then that I realized the key to getting the colored mana symbols on the card: What if the cost reduction wasn't for generic mana but for colored mana? I could reduce one of each colored pip by reducing the mana cost by WUBRG. Writing it out would get me my five-color identity, hitting two different goals wwith the same ability.

![Morophon, the Boundless](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=463950&type=card)

That idea also freed up the card for one additional ability. This was *Modern Horizons*, and I had access to all the mechanics, so I liked the idea of giving it a changeling so that it would be whatever creature your deck cared about. This would be a bonus if you picked a creature type that we had other typal cards for. I was so fond of the card that I chose it to be my preview card for my first *Modern Horizons* preview column. It had a great reception, and I got a lot of letters thanking me for making their creature type deck finally work.

**The Medallions**

![Pearl Medallion](https://media.wizards.com/2023/cmm/en_2c46b2d99a.png) ![Sapphire Medallion](https://media.wizards.com/2023/cmm/en_9c6e0ececc.png) ![Jet Medallion](https://media.wizards.com/2023/cmm/en_5e228df8e3.png)

![Ruby Medallion](https://media.wizards.com/2023/cmm/en_8cde9cb140.png) ![Emerald Medallion](https://media.wizards.com/2023/cmm/en_247523f4a6.png)

As I explained last week, I was hired into R&D to be a developer. My goal though was to become a designer. The key to doing that was finding an opportunity to prove that I could design. That opportunity came about one day when I was talking to Richard Garfield.

Richard mentioned in passing that he might want to be on a *Magic* design team. (Richard had stepped away from *Magic* to design other games.) I went to Joel Mick, the then head designer, and asked if he'd be willing to let me lead a design if Richard was on the team. Joel said yes. Next thing you know, I'm in charge of designing *Tempest*.

The Medallions came about because we were trying to find our take on the Moxen. I'm sure some are asking, "Did you really have to make new Moxen?" It was my first design, and a lot was riding on it, so I had the design team lean in on things that I knew were popular. The plan obviously wasn't to make something as broken as the Moxen. We were doing a thing R&D did a little too much of in the early days, attempting a "fixed version."

I was also interested in changing it up a little. Part of having a design team was to show that we could tweak things in interesting ways. I didn't want to make exactly a Mox and just change the mana cost. The inspiration for the tweak we made with the Medallions was inspired by the "lucky charms" from *Alpha*.

![Ivory Cup](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=22&type=card) ![Crystal Rod](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=10&type=card) ![Throne of Bone](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=44&type=card)

![Iron Star](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=21&type=card) ![Wooden Sphere](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=44&type=card)

For those unaware, "lucky charms" was a nickname for a cycle of artifacts in *Alpha* (Ivory Cup, Crystal Rod, Throne of Bone, Iron Star, and Wooden Sphere) that gained you life whenever a player cast a certain spell. The "lucky charms" were popular even though they weren't particularly strong. I like how it gave you a little something every time you cast a spell of a certain color. So, when I was designing cards for *Tempest*, I liked the idea of making a new "lucky charms" cycle, but one that did something other than gain you life.

The Medallions came about while I was trying to design two different artifact cycles, and they converged. The first cycle was "fixed" Moxen. The second cycle was a tweak on the "lucky charms." It came about when I made a list of all the effects I could use for the "lucky charms" cycle. One of the abilities was to add one mana of the appropriate color, but then I realized it was only useful if you cast two spells on the same turn, which doesn't happen a lot, especially early in the game. That got me to the idea of the "effect" being one less mana. At that point I realized, I'd kind of created a Mox. In the end, it wasn't quite a Mox and it wasn't quite a "lucky charm," but they combined to make a cool artifact cycle.

**Squee, Goblin Nabob**

One day I went into a development meeting for vision design. I think it was the last meeting before we handed off the set to editing. I read the flavor text for Relentless Assault, and while I liked the premise of goblin nursery rhyme/war cry, I felt the actual text had room for improvement. Bill said he could change it, but he needed a better option before the meeting was over.

So, as the development meeting was going on, I wrote the flavor text. Bill liked it enough that he swapped it. (This is not how the current process works at all!) I'm not sure where I came up with the name Flog, but Squee was the most Goblin-sounding one-syllable name I could think up that rhymed with "tree."

![Relentless Assault](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=3698&type=card)

Flash forward less than a year, and Michael Ryan and I are creating the *Weatherlight* crew for our pitch to the *Magic* brand team. We knew we wanted comic relief and in *Magic*, especially at the time, that seemed like it wanted to be a Goblin. Michael asked me if I had a name for the Goblin. I said I did. "How about Squee?"

In the first act of the *Weatherlight* Saga story (the *Tempest* block story), Squee didn't have a lot to do, but we had one moment to let him shine. There was an artifact from The Legacy that Squee grew fond of, seen on the card Squee's Toy (which is a pun that many people seem to miss). It's the thing Squee is holding in the art of his card in this set.

![Squee's Toy](https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=4629&type=card)

When the *Weatherlight* goes through Death Pits of Rath (to sneak into Volrath's Stronghold) Squee gets in trouble, and Gerrard has to save him. Then Squee gets scared and squeezes his "toy," which ends up accidentally saving Gerrard from some Carrionette Skeletons. The artifact specifically prevents one damage so that it could have this story moment.

All of this is to lead up to the fact that one of the defining traits of Squee is his luck, so years later when I was designing his card in *Mercadian Masques*, I decided to play up his luckiness. The fact he couldn't die wasn't meant to imply he was immortal, but that fate seems to like him. Originally, the card just didn't let him die. It was a static ability that literally said, "Squee can't die." It didn't quite work out in the rules, so we came up with an answer inspired by Phoenixes and Hammer of Bogardan. He just keeps coming back from the graveyard. The card design would later inspire an author to literally make him immortal, which was never my intent but was funny nonetheless.

**Tooth and Nail**

When I turned in the design handoff for original *Mirrodin*, the design file had the energy mechanic. Bill Rose, who was then the head designer, felt that there was a little too much complexity in the set. My solution was to remove energy. It took up a lot of space and was easier to pull out as it was less intertwined with the rest of the set. (I would obviously find a home for it years later in *Kaladesh*.) When I pulled it out, I removed the only mechanic in the set that was being used on instants and sorceries (affinity, Equipment, and imprint, all went on permanents), so Bill asked me to find a mechanic for instants and sorceries.

Usually when we're missing our last mechanic, we look at our set and figure out the shape of what isn't there. What was the set missing? Here's what I observed:

*   **The mechanic had to go on instants and sorceries.**

That was my starting point.

*   **The mechanic wanted to be a mana sink if possible.**

A "mana sink" is any card that lets you spend extra mana. In the late game, players tend to have more mana than cards, so it's nice to provide ways to spend that extra mana. Equipment was filling a little of this void, but not enough.

*   **The mechanic wanted to have choice.**

Looking through the set, I noticed we were a bit light on choices, meaning places on cards where you had an option of what the card did.

*   **The mechanic wanted to be straightforward.**

Equipment was a brand-new thing, and it was tricky to balance. Affinity was a cost reduction mechanic, and those are notoriously dangerous. Imprint was cool but quirky. The last mechanic just wanted to be something easy to explain and understand.

Bill hadn't given me a lot of time to fix the issues. Development had to start soon on the set. I was wracking my brain trying to figure out the answer. I went home, had dinner, watched some television, and went to bed. I was exhausted as it had been a long day.

In my sleep, I had a dream. I was playing *Magic*. Not just any *Magic*, I was playing *Mirrodin*. I drew a card that I had never seen before. It had this mechanic on it called entwine. (It was literally called entwine in my dream.) I had never seen it before. I read it and thought it was a pretty cool mechanic. It was a modal mechanic where you could spend extra mana to get both modes.

I then had that moment you often have in dreams where you realize something isn't quite right. While entwine was cool, it wasn't in the set. Then it dawned on me that entwine could be in the set. It hit all the criteria I'd listed above. But who made entwine? I then realized I'd made entwine. That's when I figured out I was dreaming. I woke up in a cold sweat and immediately grabbed a piece of paper and wrote down everything I could remember about the mechanic. I then stayed up for the rest of the night designing entwine cards. I was so excited.

The next day, I went into the office and told Bill I'd solved the problem. I showed him my entwine designs, he loved them, and the mechanic went into the set that day. Which brings us to Tooth and Nail. This card came about because we wanted a rare green entwine card. The key to good entwine design was to make two effects that each had functionality by themselves but combined to do something synergistic. The tricky part is both abilities had to be in the same color. And with Tooth and Nail, both had to be rare green effects.

I wrote down every rare green effect I could think of and tried pairing them. I eventually found two effects that paired nicely. Green can tutor for creatures and green can put creatures from its hand on the battlefield. The problem was the combined effect is usually what we do at rare. We solved this problem by doubling it. Now, you can tutor for two creatures or put two creatures from your hand on the battlefield. Since the second ability avoided paying mana, you could get your two most expensive creatures. It all ended up working out and made a sweet card.

**Tragic Slip**

![Tragic Slip](https://media.wizards.com/2023/cmm/en_f42feba1c0.png)

When you're designing a card, you're very focused on the small decisions. Sometimes you make a decision for one reason, but it end up making the card better for other reasons. Tragic Slip is a great example. The earliest version of the card read something like this:

**Early Tragic Slip**  
 B  
 Target creature gets -1/-1 until end of turn.  
 Morbid — Instead, destroy that creature.

My issue with the card is that the two sides didn't feel as connected as I'd have liked. Yes, granting a creature -1/-1 was sort of like injuring it, which was a lesser version of killing it, but it felt a step removed. My suggested fix was to have both effects just be -N/-N effects. That way it felt like the effect got bigger rather than changing to a similar but different effect.

I was fine with the larger -N/-N effect being pretty big, as I was okay with it basically being a kill spell. Once we knew it was a larger number, what number it was became clear. Early in design, Jenna Helland had made a card called Into the Hellmouth (which eventually became Into the Maw of Hell) that destroyed a land and did damage to a creature. I think it was 9 damage (we now tend to cap red at 6 if it's not an X spell). I changed it to 13 as thirteen is an unlucky number in some cultures, and we were making a gothic horror set. It quickly became a theme and others leaned into using 13 in their designs. So, obviously this card should grant -13/-13.

Interestingly, the fact that the card shrunk the creature rather than destroyed it ended up having a bunch of positive impacts on the card (such as killing indestructible creatures). This allowed it to become a top-tier Constructed card. While that wasn't our goal, the change from "destroy target creature" to "target creature gets -13/-13" ended up being a massive boon to its design.

## "And That's the End!"

We've come to the end of today's column. I hope you've enjoyed these two weeks of design stories. If you have any feedback about today's column, any of the cards I talked about, or *Commander Masters* in general, you can email me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for this year's "State of Design" article.

Until then, may you have fun playing any or all the cards I talked about.
---
id: vvj8s1td
kind: article
lang: en
path: /en/articles/makingmagic/2024/06-10-expanding-your-horizons-energy
title: 'Expanding Your Horizons: Energy'
published: '2024-06-10'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
    lang_detected: en
    capture_id: 220339
    url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
    captured_at: '2024-06-11 04:59:57+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
    lang_detected: en
    capture_id: 220339
    url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
    captured_at: '2024-06-11 04:59:57+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
    lang_detected: en
    capture_id: 220339
    url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
    captured_at: '2024-06-11 04:59:57+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
    lang_detected: en
    capture_id: 220339
    url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
    captured_at: '2024-06-11 04:59:57+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: vvj8s1td
  url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
  page_key: magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
  lang: en
  template: contentful
  captured_at: '2024-06-11 04:59:57+00'
  capture_id: 220339
  wayback_url: https://web.archive.org/web/20240611045957id_/https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: vvj8s1td
  capture_id: 220339
  url: https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
  wayback_url: https://web.archive.org/web/20240611045957id_/https://magic.wizards.com/en/news/making-magic/expanding-your-horizons-energy
  captured_at: '2024-06-11 04:59:57+00'
  template: contentful
  sha256: ae4e7575e7593b511fedc8c5f11a7f0726defe81dd5b7eb25bb649d99a5f1563
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
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist?color=FFFFFF&background=30343C
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
[Last week](/en/articles/makingmagic/2024/06-03-expanding-your-horizons-eldrazi), I told card-by-card design stories about some Eldrazi cards inspired by older cards. For each card, I told the design story of the original card followed by the design story of the card from *Modern Horizons 3*. Today's article is similar, but this time, I will cover some cards concerned with energy.

**Chthonian Nightmare**

0083\_MTGMH3\_Main: Chthonian Nightmare 

Our first story starts before I began working at Wizards back in the summer of 1994. *Legends* was coming out, so I waited in line in front of my local game store and bought two boxes of boosters. I went home and opened them all, then turned around and went right back to the game store to buy two more boxes. Luckily for me, my game store went all in on *Legends*. One of the very first cards I opened was this card:

Hell's Caretaker 

As I talked about several years ago in an article titled "[My Favorite Things](/en/articles/makingmagic/2020/06-01-my-favorite-things)," I'm a huge fan of graveyard interactions. Many of my early decks involved reanimating creatures from my graveyard, so when I saw Hell's Caretaker for the first time, I was super excited. It was reusable reanimation. *Antiquities* had a card called Argivian Archaeologist that allows you to repeatably return artifacts from your graveyard to your hand, but there wasn't such a card for creatures. In addition, Hell's Caretaker put the creatures on the battlefield. Yeah, you had to sacrifice a creature to do so, but that was just a restriction for my inner Johnny to build around. I designed a lot of decks with Hell's Caretaker.

Flash forward to the design of *Exodus*. One of the joys of being a *Magic* designer is being able to take cards you enjoy and make new versions of them. I loved Hell's Caretaker, so I wanted a spiritual successor. To make it different from Hell's Caretaker, I made it an enchantment rather than a creature. Also, rather than it being a once-a-turn trigger, I added the cost of bouncing the enchantment when you activated it.

I honestly wasn't trying to make it more powerful, but I did. Enchantments are harder to remove than creatures, and the bouncing cost could be used as a positive to save the enchantment if an opponent tried to destroy it. Also, removing the once-a-turn trigger allowed Recurring Nightmare to be used more than once a turn. This all combined to make a powerful card that saw a lot of tournament play.

Which brings us to *Modern Horizons 3*. Here's the earliest version of Chthonian Nightmare:

**Cleric's Nightmare (version #1)**  
 2BBB  
 Creature — Demon  
 6/6  
 Menace  
 Whenever a Cleric enters the battlefield under your control, you may sacrifice it. When you do, return CARDNAME from your graveyard to the battlefield.  
 Knoweth 3C *(3C, Discard this card: Draw two cards.)*

The card started as a creature, a Demon specifically. It was 6/6 because we like using the number 6 on Demons (as its associated with the devil). It had a typal design where it enabled Clerics to reanimate it. The knoweth ability was basically supercycling (two cards instead of one). This one has a colorless cost, so my gut says Erik Lauer, the set's lead vision designer, was trying knoweth as an Eldrazi thing. I don't think it got very far before Erik pulled it.

**Cleric's Nightmare (version #2)**  
 2BB  
 Creature — Demon  
 6/6  
 At the beginning of your upkeep, sacrifice another creature. Whenever a Cleric enters the battlefield under your control, you may sacrifice it. When you do, return CARDNAME from your graveyard to the battlefield.

Take two was just a tweak on the first design. It lost menace and knoweth. Its cost dropped from 2BBB to 2BB to allow a flavorful drawback, a creature sacrifice which would tie thematically into the sacrificing Cleric reanimation ability.

**Cleric's Nightmare (version #3)**  
 3BB  
 Creature — Demon  
 6/4  
 Suspend 4  
 As long as CARDNAME is in your graveyard, whenever a Cleric enters the battlefield under your control, you may sacrifice it. When you do, exile CARDNAME with 2 time counters.

The next version played around with adding suspend. For those who might not remember this mechanic from *Time Spiral*, here's its reminder text:

Suspend N — {mana cost} *(Rather than cast this card from your hand, you may pay {mana cost} and exile it with N time counters on it. At the beginning of your upkeep, remove a time counter. When the last is removed, you may cast it without paying its mana cost.)*

The file didn't list the cost for suspending Cleric's Nightmare. I assume that was an oversight. My gut says it would be something like 1B. The Cleric typal still reanimated it but did so using suspend technology, which delays its return.

**Recurring Nightmare (version #4)**  
 3BB  
 Creature — Demon  
 6/4  
 Sacrifice a creature, Return Recurring Nightmare to its owner's hand: Return target creature card from your graveyard to the battlefield. Activate only as a sorcery.

During set design, the team got the idea to explore adding Recurring Nightmare to Modern. The rule for *Modern Horizons* sets is that all reprints (except for lands) can't be cards in the current Modern format. This means all reprints are new to Modern. Recurring Nightmare is a powerful card, so this just shows that they were willing to experiment with bold reprints.

**Frankenstein's Exchange (version #5)**  
 2B  
 Enchantment  
 When CARDNAME enters the battlefield, add EEEE.  
 Pay X E, Sacrifice a creature, Return CARDNAME to its owner's hand: Return target creature card with mana value X from your graveyard to the battlefield. Activate only as a sorcery.

The addition of Recurring Nightmare was seen as a low-percentage gamble, but Set Design does like to push boundaries and see what's possible. Sometimes a thing you think could never work in fact does. That wasn't the case with Recurring Nightmare, though. Playtesting showed it was too good, so Set Design shifted this slot over to something else they were doing, energy designs that were callbacks to popular, and powerful, older cards. The first shot at this was close to the final version. The printed card is one mana cheaper but gives you one less energy. My best guess is that playtesting showed four energy was a little too much, so they reduced it to three and dropped the mana cost accordingly.

Finally, here's the art description for the card:

**\*\*\*EXTENDED-ART TEMPLATE\*\*\***  
 **Setting**: Unspecified plane  
 **Color**: A spell associated with black mana  
 **Location**: Dark cave interior  
 **Intent**: This card is a reference to the old card Recurring Nightmare (see art reference).  
 **Action**: Show the interior of a dark, weirdly organic CAVE lined with TEETH and EYES. The teeth are dripping DARK OIL as though it is saliva. A small figure is huddled on the floor of the cave near the back, they are trapped in a nightmare and being coated in the oil dripping from the cave's teeth.  
 **Focus**: The organic cave  
 **Mood**: Nightmarish

**Inspired Inventor**

0032\_MTGMH3\_Main: Inspired Inventor 

This next story is about the creation of a whole mechanic rather than a single card. The mechanic in question is fabricate, which premiered in *Kaladesh*. Kaladesh the plane was our take on a steampunk world, and we were leaning into the idea of a world where technology was king. Artifacts are the main way we represent technology. We wove our energy mechanic and our new Vehicle artifact subtype into artifacts.

To give the set some extra depth, we also made use of +1/+1 counters and artifact creature tokens. The +1/+1 counters helped with the flavor of creatures getting more powerful due to technology. The artifact creature tokens represented technology made by the inventors of Kaladesh. Both the +1/+1 counters and the artifact creature tokens played into the larger themes, but they didn't criss-cross with one another well. It's important to have your themes overlap to make cards desirable and worth fighting over during drafts.

So, during a meeting, I asked the question, "How can we make +1/+1 counters and artifact creature tokens overlap?" This led to the question, "Is there something we can do that would be beneficial in both the decks that focus on +1/+1 counters and the decks that focus on artifact creatures?" We talked through several ideas. What if there was a mechanic that let you turn +1/+1 counters into artifact creatures and/or vice versa? Or maybe there was a mechanic that counted +1/+1 counters and artifact creatures? Or possibly a mechanic that generated both?

That last one got the attention of the room. Creating both seemed like a bit too much. What if we made a mechanic that created one or the other? A creature could get bigger or have some small buddies. We made cards for the mechanic before we left the meeting and played with them at the next playtest. It went well, so fabricate became part of the set. It was challenging in set design to make both options valid because, as it turns out, there aren't a lot of designs that hit that sweet spot, but there were enough to keep fabricate in the set.

Now, let's turn our attention to the fabricate-inspired design:

**Morning Priest (version #1)**  
 W  
 Creature — Human Cleric  
 3/3  
 Lifelink  
 At the beginning of your upkeep, sacrifice CARDNAME unless you pay 2W.

The slot started as a one-drop 3/3 with an upkeep cost. Richard Garfield had put a lot of creatures with upkeep costs in *Limited Edition (Alpha)*, which was copied by a lot of early designers, but over time, it's something we've pulled back on substantially, as players aren't super excited by them. *Modern Horizons* sets look back, though, so maybe a new upkeep creature could be cool?

**Transcendent Novice (version #2)**  
 W  
 Creature — Eldrazi Ceric  
 3/3  
 At the beginning of your upkeep, sacrifice CARDNAME unless you pay E.

The upkeep cost wasn't enough to make the card feel like a *Modern Horizons* card, so the design team changed the upkeep cost from mana to energy. Interestingly, the card doesn't produce any mana when played, which is unlike how we design most energy cards.

**Transcendent Novice (version #3)**  
 W  
 Creature — Eldrazi Ceric  
 3/3  
 At the beginning of your upkeep, sacrifice CARDNAME unless you pay 1WW.

Then, the card changed back to its mana version, although this time with the upkeep cost being 1WW instead of 2W. I assume this was to make this card less efficient in a deck with two or more colors.

**Death Tax (version #4)**  
 W  
 Enchantment  
 Whenever a creature you control dies, you gain E.  
 Pay X energy, sacrifice CARDNAME: Return target creature with mana value X from your graveyard to the battlefield. Activate this only when you could cast a sorcery.

The upkeep card just wasn't playing well, so they tried a completely new design, this time as an enchantment. The design went back to energy, but now as a more traditional energy card that allowed you to use your energy to reanimate creatures. The nature of the design made the card reanimate small creatures often, which white is known for.

**Party Leader (version #5)**  
 2W  
 Creature — Human Warrior  
 3/2  
 Whenever a creature you control attacks alone, you get E.  
 Pay X E, sacrifice CARDNAME: Return target creature with mana value X from your graveyard to the battlefield. Activate this only when you could cast a sorcery.

The next version converted the card into a creature, most likely to make it more vulnerable to removal. It also changed the trigger from a death trigger to an attack trigger. I assume the death trigger was discouraging attacking while attack triggers, by definition, encourage it.

**Party Leader (version #6)**  
 2W  
 Creature — Human Warrior  
 3/2  
 Whenever a creature you control attacks alone, it gets +X/+X until end of turn, where X is the number of creatures in your party.

The next version kept the size and attack trigger but removed the energy and reanimation aspects, tying it instead to the party mechanic from *Zendikar Rising*. I don't 100% know that this change was influenced by the card being called Party Leader, but my gut says it's likely.

**Modified Soldier (version #7)**  
 2W  
 Creature — Human Soldier  
 3/3  
 Whenever CARDNAME attacks, it gets +1/+1 until end of turn for each modified creature you control.

Party is a very structural mechanic, meaning the set must be built around it, making its chances of working in a set like *Modern Horizons 3* low. The new version kept the same basic shell of design but played into one of the bigger themes in the set, modified.

**Glint-Sleeve Refiner (version #8)**  
 2W  
 Creature — Dwarf Artificer Rebel  
 2/3  
 When CARDNAME enters the battlefield, choose one —  
 • You get {EEE} *(three energy counters)*.  
 • Put a +1/+1 counter on CARDNAME.  
 • Create a 1/1 colorless Servo artifact creature token.

This version finally arrived at the execution of the final card. It mixes and matches two of the mechanics from *Kaladesh*, energy and fabricate, although fabricate isn't specifically referenced by name. The printed card loses a toughness and goes from being a Dwarf Rebel to a Human.

Before I move onto the next card, here's the art description for Inspired Inventor:

**Plane**: Kaladesh  
 **Color**: A white-aligned creature  
 **Location**: A balcony high above a rural town, with snow-tipped mountains in the background (See pages 13–14 for Kaladesh mountains and page 42 for buildings.)  
 **Action**: Show a male human ARTIFICER critically inspecting an AETHER-POWERED SERVO clinging to his forearm like a GAUNTLET. Servos come in a variety of shapes—see attached references for examples but adapt it to look like it's capable of doubling as a gauntlet. The servo's body glows with blue aether, and it has a big eye-like globe to help us know that it's not just a gauntlet. The man is of South Asian ancestry, has a heavyset figure, and is roughly 40 years old. (See pages 49–54 for Kaladesh human costuming reference.)  
 **Focus**: The artificer  
 **Mood**: "Almost perfect, but not quite … just a few more adjustments."

**Volatile Stormdrake**

0079\_MTGMH3\_Main: Volatile Stormdrake 

This story also starts with the release of *Legends*, but it involves different cards. As I explained above, I've always been a Johnny deck builder. One of the things I enjoyed in early days of *Magic* was building a deck that had won in a way I'd never seen before. Now, as I talked about above, I loved reanimation. *Legends* had some cards that gave me a cool idea. Here were the key cards (half of which come from *Legends*) added to my new deck:

Force of Nature Animate Dead Spirit Link Juxtapose Gauntlets of Chaos

I would reanimate Force of Nature with Animate Dead, making it a 7/8 creature. I would then put Spirit Link on it. Anytime the card would damage me, I would gain life to offset it. When I dealt damage to the opponent, I would gain life. (Spirit Link was the precursor to the lifelink ability, but it gained you life even if you weren't the controller of the creature.) That wasn't enough, though, because I'd won by reanimating creatures before. The last step was to exchange my Spirit Linked Animated Dead Force of Nature for one of my opponent's creatures with either Juxtapose or Gauntlets of Chaos. My opponent had to spend four green mana to prevent taking 8 damage (and often they weren't even playing green). If they didn't, they would take 8 damage and I would gain 8 life. They could attack me with the Force of Nature, but the Spirit Link would offset any damage. I won a lot of games with this deck. It was one of my favorites.

I thought it was cool to steal interesting creatures from my opponents using this deck; getting to play with cards I didn't bring to the table was a lot of fun.

Flash forward to the design of *Urza's Saga*. Over the years, we've made several cards that steal opponent's creatures, but I was tickled by the idea of exchanging creatures rather than stealing them. I gave the creature a decent body, a 3/3 flyer, because I wanted the fact that you were giving away the creature to mean something. Again, the card ended up being a bit more powerful than I anticipated. (There's a reason I mostly work on the beginning part of design; gauging power level is not my strong suit.)

Now, let's talk about the card, which was inspired by Gilded Drake:

**Clockwork Hound (version #1)**  
 1  
 Artifact Creature — Dog  
 0/0  
 CARDNAME enters the battlefield with X +1/+1 counters on it. At end of combat, if CARDNAME attacked or blocked this combat, remove a +1/+1 counter from it.  
 X, T: Put a +1/+1 counter on CARDNAME, where X is the number of +1/+1 counters on CARDNAME.

This slot went through a lot of changes over the course of design. The earliest version was a riff on Clockwork creatures, which first showed up on the *Alpha* card Clockwork Beast. Basically, clockwork creatures are artifact creatures that wind down as they get into combat, either attacking or blocking. This winding down is usually represented by +1/+1 counters that get removed. There is then some mechanism to wind it up and get the +1/+1 counters back.

**Blip, Forgotten Creation (version #2)**  
 \<none>  
 Legendary Artifact Creature — Powerstone  
 2/2  
 2: Return CARDNAME from your graveyard to the battlefield. Activate this only as a sorcery (you can't cast CARDNAME).  
 1: Discard CARDNAME.  
 When CARDNAME dies, return it to its owner's hand.  
 T: Add C. You can't spend this mana to cast spells.

The next version stayed an artifact creature but went in a whole new direction. Past *Modern Horizons* sets (as well as some premier sets) have had fun making artifact creatures that also have a subtype famous for being an artifact token. We'd never done one with Powerstone before (seen in *The Brothers' War*), so this design was tackling that challenge. The quirkiest thing about this design was that it had no mana cost.

The first ability was the way to get the card onto the battlefield, but it only worked in the graveyard. The second ability gave you a way to get it into the graveyard. The triggered ability kept it from getting to the graveyard by dying. The last ability was the Powerstone ability. Our rule is that if the card has a subtype from a token artifact, it must do what the token artifact with the same subtype does (or close to it).

**Jade Scepter (version #3)**  
 3  
 Artifact Creature — Golem  
 3, T: Target opponent discards a card. If they can't, untap CARDNAME and it becomes a 3/6 Golem artifact creature until end of turn. Activate only when you could cast a sorcery.

The next version tried a completely different artifact design. This card was a cross between two noncreature artifact cards from *Alpha*:

Disrupting Scepter Jade Statue 

The card had the mana cost and activation of Disrupting Scepter and the "turn into a 3/6 Golem" aspect of Jade Statue.

**Rotate Time (version #4)**  
 4U  
 Sorcery  
 Suspend 4 — Each player shuffles their hand and graveyard into their library, then draws seven cards.

The next version is a riff on a different *Alpha* card, Timetwister. This version costs two more generic mana but has a suspend cost. The actual suspend cost wasn't written down, but my gut says it was 2U, mirroring the original card.

**Energy Drake (version #5)**  
 1U  
 Creature — Drake  
 3/3  
 Flying  
 When CARDNAME enters the battlefield, you get EE *(two energy counters)*, then you may pay X E.  
 Exchange CARDNAME and target creature with mana value X. If you don't make an exchange this way, sacrifice CARDNAME.

This version was the first stab at a Gilded Drake variant. Note that it started by having a 1U mana cost and being a 3/3 flying Drake, all borrowed from Gilded Drake. It wove in energy by making it the resource that determines what you can steal.

**Energy Drake (version #6)**  
 1U  
 Creature — Drake  
 3/3  
 Flying  
 When CARDNAME enters the battlefield, you get {EE} and exchange control of CARDNAME and target creature an opponent controls. That creature gains echo X {E}, where X is its mana value. *(At the beginning of your upkeep, if this came under your control since the beginning of your last upkeep, sacrifice it unless you pay its echo cost.)*

The Set Design team experimented with using echo on the card (a mechanic from the *Urza's Saga* block). I think they got to echo because the "pay a fee to keep the card" aspect felt similar to echo. Echo proved to be unnecessarily confusing, so they moved to a version where you just paid immediately after you exchanged the creatures. It was the echo experiment that got them to the idea that you could steal a creature of any mana value but only got to keep it if you were able to pay the energy cost.

The final printed version is mostly the same with a few small changes. It's a 3/2 rather than a 3/3. It has hexproof from activated and triggered abilities, and it grants you four energy counters rather than two. All these changes feel like adjustments made during play design to position the card where they wanted it for Constructed formats.

Lastly, here's the art description:

**\*\*\*EXTENDED-ART TEMPLATE\*\*\***  
 **Setting**: Non-specific plane  
 **Color**: A blue-aligned creature  
 **Location**: The sky during a lightning storm  
 **Action**: A drake is a draconic creature with two wings, two hind legs, and no forelimbs. Show us a DRAKE with its WINGS SPREAD WIDE. Maybe the Drake is CRACKLING with BLUE ELECTRIC ENERGY. Or maybe we see a BLUE GLOW between its scales as if from a fiery blue furnace burning within.  
 **Focus**: The drake  
 **Mood**: A drake powered by bioelectricity

## "I Like Your *Energy*"

That's all the time I have for today. I hope you enjoyed my look at some of the energy designs and the cards and/or mechanics that inspired them. As always, I'm eager for any feedback, be it on today's article, any of the cards or mechanics I talked about, or *Modern Horizons 3*. You can email me or contact me through any of my social media accounts ([X](https://twitter.com/maro254), [*Blogatog*](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Next Tuesday, look forward to my card preview article for the upcoming *Universes Beyond* release, *Magic: The Gathering® – Assassin's Creed®*.

Until then, may you have all the energy you need for a fun game of *Magic*.
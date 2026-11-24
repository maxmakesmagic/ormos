---
id: 4t12dj24
kind: article
lang: en
path: /en/articles/makingmagic/2024/02-05-only-murders-that-were-building-part-2
title: Only Murders That We're Building, Part 2
published: '2024-02-05'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
    lang_detected: en
    capture_id: 225260
    url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
    captured_at: '2024-05-18 00:59:48+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
    lang_detected: en
    capture_id: 225260
    url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
    captured_at: '2024-05-18 00:59:48+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
    lang_detected: en
    capture_id: 225260
    url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
    captured_at: '2024-05-18 00:59:48+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
    lang_detected: en
    capture_id: 225260
    url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
    captured_at: '2024-05-18 00:59:48+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 4t12dj24
  url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
  page_key: magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 00:59:48+00'
  capture_id: 225260
  wayback_url: https://web.archive.org/web/20240518005948id_/https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 4t12dj24
  capture_id: 225260
  url: https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
  wayback_url: https://web.archive.org/web/20240518005948id_/https://magic.wizards.com/en/news/making-magic/only-murders-that-were-building-part-2
  captured_at: '2024-05-18 00:59:48+00'
  template: contentful
  sha256: a1306c70afe11001e52a9c75ffd3b6e37466f2431beec58cec9f74762a98cafa
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
[Last week](/en/articles/makingmagic/2024/01-29-only-murders-that-were-building-part-1), I started telling card-by-card design stories about *Murders at Karlov Manor* cards selected by readers on my blog, [Blogatog](https://markrosewater.tumblr.com/). Today, I will tell more stories about more cards, so sit back and enjoy.

**Crime Novelist**

![Crime Novelist](https://media.wizards.com/2024/mkm/en_26bc32d9bc.png)

This card started with a simple purpose. It wanted to be a little red creature that had synergy with artifacts. Investigate was in the set, which makes Clue artifact tokens, and red is number one in sacrificing artifacts, so this card was playing into that theme.

**Goblin Fire Clerk (version 1)**  
 2R  
 Creature — Goblin Advisor  
 1/1  
 T, Discard a card or sacrifice a Clue: Draw a card.

The card started at common and as a Goblin. Many small red creatures start as Goblins, as that's the characteristic race for red, and Ravnica has Goblins. The card was basically a rummaging card (i.e., discard and draw) with sacrificing Clues as a secondary option. We didn't want it to have an activation cost for the tap, so that meant it needed to be a 1/1 for two and a red mana.

**Goblin Fire Clerk (version 2)**  
 2R  
 Creature — Goblin Advisor  
 1/1  
 Haste  
 T, Discard a card or sacrifice an artifact: Draw a card.

This card had only two changes. One, we gave it haste because the card had a little extra room and haste on a 1/1 doesn't cost much. Two, we made the sacrifice restriction a little broader, allowing you to sacrifice any artifact rather than only a Clue. We often like making cards a bit more general, when possible, for better synergy.

**Goblin Fire Clerk (version 3)**  
 2R  
 Creature — Goblin Advisor  
 2/2  
 T, Sacrifice an artifact: Add RR.  
 Whenever you sacrifice an artifact, put a +1/+1 counter on CARDNAME.

The next change came about because we wanted something a little different from the card. Rather than having an alternate means to use Clues, we wanted it to be a card that rewards you for using them. That meant it wanted a triggered ability that happened when you sacrificed an artifact. We chose to make the creature bigger using +1/+1 counters. We then added a second ability (the first one written on the card), which allowed the card to work in a vacuum. When making synergistic components, it's helpful if the card doesn't require a second card to function (what we call an A/B theme where one card provides A and a second card provides B). The first ability was also nice because you could sacrifice a Clue to it if needed, but the overall card synergy was still there if you crack a Clue for a card.

**Goblin Fire Clerk (version 4)**  
 1R  
 Creature — Goblin Advisor  
 1/3  
 Whenever you sacrifice an artifact, CARDNAME deals 1 damage to each opponent.

We liked the first card, but we felt there was a little too much going on to be a common, so we removed the sacrifice ability and changed the triggered ability to something that could help win the game a bit more directly.

**Goblin Fire Clerk (version 5)**  
 2R  
 Creature — Goblin Advisor  
 2/2  
 T, Sacrifice an artifact: Add RR.  
 Whenever you sacrifice an artifact, put a +1/+1 counter on CARDNAME.

We then realized that we made the wrong choice. Rather than adapt a card we liked to be a common, we just moved the design as is (or as it was in the previous version) to uncommon so it could stay as is.

**Goblin Fire Clerk (version 6)**  
 2R  
 Creature — Goblin! Advisor  
 2/2  
 Trample  
 Whenever you sacrifice an artifact, put a +1/+1 counter on CARDNAME and add R. Until end of turn, this mana doesn't empty as steps and phases end. This ability only triggers once per turn.

We then decided that we wanted to make the card more enticing to build around, so we put both the mana production and granting a +1/+1 counter on the triggered ability. We added an ability to keep the mana around but would remove that before moving it to print as it just made the card wordier without enough payoff. The printed card would also revert to a 1/3, so we removed trample. The exclamation point after the word Goblin is a sign from design to the Creative team that they mechanically need the card to stay a Goblin. The Creative team came up with the idea of this being a Crime Novelist, a great addition that added a lot of flavor, and probably the reason my blog readers asked me to talk about this card.

Finally, here's the art description:

**Setting**: "Polo" Ravnica  
 **Color**: Creature associated with red mana  
 **Location**: A study—see pages 17–20 and 150–151 for general Ravnican environments, but this place is pretty open to be yours to design. Ravnica is inspired by the architecture of medieval Prague. In the background decorating the room, we see the trappings of a person fascinated by crime: a skull in a glass case, a knife that was a murder weapon, newspaper clippings on the walls.  
 **Action**: Using page 56 as inspiration, show a female GOBLIN who's a BESTSELLING CRIME NOVELIST. Show her excitedly WRITING her next devious plot twist, using a pen that leaves glowing red trails of text in its wake.  
 **Focus**: The goblin crime novelist  
 **Mood**: "Ooh, the readers will never see this coming!"  
 **Notes**: See pages 77–78 for goblins and pages 74–76 for additional costuming inspiration.

**Persuasive Interrogators**

![Persuasive Interrogators](https://media.wizards.com/2024/mkm/en_cb3e157ace.png)

This was the card that surprised me most when I was putting together my teaser for *Murders at Karlov Manor*. I always work on vision design for premier sets, but after it gets handed off, I move on to other sets. Yeah, I'll peek my head in from time to time, but I'm not always aware of every card that's added to the file. So, imagine my surprise when I looked through the file and found a card that gave out poison counters. How exactly did this card make it into, and stay in, the set? We'll begin in vision design:

**Hired Cleaner (version 1)**  
 4B  
 Creature — Ogre Assassin  
 4/4  
 You may cast this spell as though it had flash during an opponent's end step.  
 When CARDNAME enters the battlefield, destroy target creature or planeswalker an opponent controls that was dealt damage this turn.

Some cards start with a specific role and stay that way throughout the life of the file, while others adapt and change along the way. This card is an example of the latter. It started as a mono-black uncommon Assassin. It's a murder mystery set. Someone had to be killing people, and mono-black is a great slot for an Assassin. The first ability was a limited version of flash. I assume this was because they didn't want it being a surprise blocker. That would add a lot of power to the card and force us to make it either more expensive or smaller.

The second ability is something we put on black spells from time to time. We have a wide range of black kill effects, and "kill something that's been damaged" is on the weak end of the scale. This was a top-down design, and the ability felt enough like something an assassin would do without being too strong. We added the limited flash so that you could block a larger creature with a smaller creature and then kill it as a surprise. In the end, at five mana, it was just unwieldy to use and rarely killed anyone.

**Rhino Detective (version 2)**  
 4B  
 Creature — Rhino Detective  
 4/5  
 Menace  
 Whenever CARDNAME attacks, you may collect evidence. If you do, another target attacking creature gets +2/+0 and gains menace until end of turn. (To collect evidence, exile cards with total mana value 6 or more from your graveyard.)

Other than staying a five-mana creature with a power of 4, everything changed about this card for its second incarnation. That's a sign that the design team wasn't sure quite what to do with the slot yet. After a playtest, you take a bunch of notes about things you want to change. This card wasn't doing a good job at what it was, so the team repurposed it to do something else. Black was, at the time, one of the collect evidence colors, as it both had a high synergy with the graveyard and was good at filling it up. This is the early period of collect evidence where it was locked at 6 rather than having a number that was adjustable. Because it was now a Detective (and a Rhino) rather than an Assassin, its ability was helpful rather than harmful.

**Ogre Detective (version 3)**  
 4B  
 Creature — Ogre Detective  
 4/4  
 Whenever CARDNAME attacks, you may collect evidence 4. When you do, target creature defending player controls gets -2/-2 until end of turn. (To collect evidence 4, exile cards with total mana value 4 or more from your graveyard.)

This version went back to being an Ogre but remained a Detective. My guess is that they wanted a collect evidence effect that was more negative, but they wanted collect evidence to be on Detectives, so they returned this to an Ogre to make it feel a little more nefarious. As you can see, collective evidence now has a number, which has been reduced to 4 on this card. It's now a repeatable kill, which was more useful.

**Shameless Shamus (version 4)**  
 4B  
 Creature — Ogre Detective  
 5/4  
 You may pay {1} and 1 life rather than paying the mana cost for Clue Equipment spells you cast. Whenever an Equipment card is put into your graveyard from anywhere, each opponent loses 2 life.

Black started doing less collect evidence, so the Set Design team decided to tie this card to a different theme, caring about Equipment. This card cared about Clue Equipment. Clue Equipment cards are an uncommon cycle of Equipment based on weapons in the game *Clue*, which are Clues in addition to being Equipment. The first ability specifically calls out Clue Equipment to encourage you to play with it, but the second ability is more general, working with any Equipment, to help the card play into the larger theme.

**Dexterous Detective (version 5)**  
 3BB  
 Creature — Ogre Detective Assassin  
 3/5  
 When CARDNAME enters the battlefield, investigate.  
 Whenever you sacrifice a Clue, target creature gets a poison counter.

The card shifts themes again, now focusing on creating synergy with Clues. Usually, a set will have ten two-color draft archetypes, meaning a monocolored card can care about one of four themes. Most of the cards usually will have mechanics that play well with at least two themes (you want different drafters to fight over the same card to ensure that there's variance from draft to draft). After each playtest, the design team will readjust cards to make sure that each theme has enough support. This card keeps changing because the team isn't 100 percent on what to do with it, so it keeps shifting between themes. Investigate is a good mechanic in that it helps "smooth" your draw (i.e., helps you draw the specific card you need), meaning it works in most decks.

Because this is an uncommon, the second ability often will give the drafter a little task. In this case, it says "draft a lot of cards that can make Clues." Black (and red) care the most about sacrificing artifacts, so giving it an input that triggers whenever you sacrifice a Clue feels at home here. It's also a theme that you can only do in a set with investigate, so it's mining design space not normally tapped. The output usually wants to be some kind of win condition, that is, something that either directly wins the game or helps you win the game. That's what encourages players to draft around it.

I'm not sure what inspired the output of poison. Generally, we usually use poison in a set where it's a theme, but a single card design can support itself if the card doing it can give ten poison counters over the course of the game. The card was an Assassin, and the flavor of poison in a murder mystery set was great. My gut says it started from a place of flavor and stuck around because it made for a complete quest. Do this ten times in a Limited game to win. That's not easy to do, so it gave you something to focus on in the draft: take a lot of cards that investigate. Briefly, they changed the input to when you draw your second card, but it didn't play as well, so they changed it back.

The biggest shift between the fifth version and the printed version is that the card went from a five-mana 3/5 that gives one poison counter to six-mana 5/6 that gives two poison counters. One poison counter was just too hard of a task. It never happened in a Limited game. Two poison counters put the task within reach, although a stretch, but a great place for this type of draft build-around. The issue now was that the card had potential to impact Commander, so that meant the Casual Play Design team needed to take a look.

Even though the life total of Commander starts at 40, the poison count to win remains at ten. I know the Rules Committee has had discussions about changing the poison total but decided against it because poison wasn't causing problems. Playtesting showed that the card being six mana made it such that it was possible to knock out one player with poison in a game but very hard to kill multiple players, as once you kill your first player, you become a target for the rest of the players, and generating enough Clues to kill everyone all at once was a daunting task but one we thought players might have fun trying. The Casual Play Design team gave a thumbs up to the six-mana version of the card, which made it to print. The Creative team made one last change to help tie the card to poison by making it a Gorgon Detective. It was enough that they felt they could remove Assassin as a creature type.

Finally, here's the art description for the card:

**Setting**: "Polo" Ravnica  
 **Color**: Creature associated with black mana  
 **Location**: Bane Alley (see pages 145–148)  
 **Action**: Show a pair of burly GORGONS who are unethical, ruthless black-aligned DETECTIVES. (See attached references for gorgons and page 30 for costuming but adjust to not be these exact costumes.) They're slyly cracking open their Agency BADGES, revealing secret compartments where they store some deadly green POISON. Maybe in the background, we see a worried-looking human thief. The gorgon detective will do anything it takes to get the truth out of him.  
 **Focus**: The gorgon detectives  
 **Mood**: There are no lines they won't cross to get to the truth.

**Red Herring**

![Red Herring](https://media.wizards.com/2024/mkm/en_fea2b07033.png)

This card knew its task from day one. A murder mystery set needs to have red herrings (i.e., clues that seem to lead in the right direction but end up leading elsewhere), so how could we not have a card called Red Herring?

Before I get into the card design, I'll discuss the elephant in the room. *Magic*, sort of, already has a card called Red Herring, one of the playtest cards from *Mystery Booster*.

![Red Herring (Mystery Booster)](https://media.wizards.com/2024/images/daily/en_g28nSWy5D321.png)

**Red Herring (*Mystery Booster*)**

There's a rule that every card name in English must be unique, meaning that if there's a card called \[Name\], only one card called \[Name\] can exist. The playtest cards live in an odd area. They aren't official in the way most cards are, and a lot of their designs were more about making jokes that were fun to read, and maybe play once, than about cards that stand up to the rigor of repeated play, so when it came time to name them, we had a decision to make. Do we name them like a normal card, meaning we'd have to be cautious about what name space they were taking up, or do we just say, "These aren't official, so they're not taking up a name, name them however you want"?

A lot of cards, like Red Herring, had names that were built around, meaning it was hard to change them, but weren't names we'd greenlight for just a playtest card if it would use up the name, so the decision was made that they didn't take up a name slot. Future cards could use the name. That was great news for Red Herring and Pick Your Poison, which would both end up getting a card in *Murders at Karlov Manor*.

When we started the design of Red Herring, we knew the following:

**It would be called Red Herring** – When you design top down from a name, keeping the name is important.

**It would be creature type Fish** – A herring is a fish. A Fish is a creature type, so the card needed to be a creature.

**It would be a Clue** – A red herring is a clue. Clues are an artifact subtype, so the card would have to be an artifact creature.

**It would be red** – We tend to avoid putting one of the five color words in a title if that card isn't that color. There are exceptions (especially with *Universes Beyond*), but this seemed like the type of card that wanted to play into expectations.

**It played into the concept of a red herring** – A red herring is a false clue that leads the detective astray. We hoped the design could hint at that flavor. For example, the key conceit of the play design card Red Herring matched this flavor. This is the one card quality we weren't sure we'd be able to follow through on but wanted to try.

The rarity was harder to pin down. As you will see, we tried this card at many rarities.

**Red Herring (version 1)**  
 1R  
 Artifact Creature — Fish Clue  
 1/1  
 When CARDNAME enters the battlefield, an opponent gains control of it. It becomes a suspect. *(It can't attack or block. As a sorcery, its controller may clear it by discarding a card or sacrificing a Clue.)*  
 As long as you control any untapped permanents, you can't activate abilities.  
 2, Sacrifice CARDNAME: Draw a card.

The card starts as an uncommon design. The idea behind it is that the card causes problems, much like a red herring. You give it to your opponent and, until they can get rid of it, it limits their ability to activate cards. That restriction was chosen because we wanted it to be hard to use as a Clue, otherwise, you'd just be giving the opponent a chump blocker that can turn into an extra card.

**Quiet Red Herring (version 2)**  
 1R  
 Artifact Creature — Fish Clue  
 2/2  
 If an opponent would investigate while CARDNAME is in your graveyard, that player puts CARDNAME onto the battlefield under their control instead. At the beginning of your end step, CARDNAME's owner gains control of it.  
 2, Sacrifice CARDNAME: Draw a card.

Playtesting showed the first version wasn't particularly fun. The restriction tended to vacillate between being too easy to work around and being almost impossible to work around, so the design team took another shot at it, this time at rare. This new version continued the flavor of the Red Herring causing problems for your opponent, but mostly because if they didn't work around the restriction (being able to use the Clue the same turn as investigating), you ended up with the card.

**Distracting Red Herring (version 3)**  
 R  
 Artifact Creature — Fish Clue  
 1/1  
 Haste  
 CARDNAME must be blocked if able.  
 2, Sacrifice CARDNAME: Draw a card. CARDNAME deals 2 damage to you.

As a rule of thumb, making cards that discourage people from playing a major mechanic in the set is a bad idea, and playtesting proved this out. The next idea was to make something simpler and put the card at common. Part of the joy of doing a top-down name is letting more people see it. The first stab was it being a 1/1 haste creature for one red mana. The "must be blocked" was for flavor, as a 1/1 will almost always be blocked if able.

**Distracting Red Herring (version 4)**  
 1R  
 Artifact Creature — Fish Clue  
 2/1  
 CARDNAME must be blocked by a Detective if able.  
 2, Sacrifice CARDNAME: Draw a card.

That version was too good. A 1/1 haste creature for one red mana has room for a little extra something, but drawing a card is too much. The design team upped it to two mana, changed it from a 1/1 to a 2/1, and tweaked the restriction to add some more flavor and lower the power of the "must be blocked" ability, as 2 power is significantly more relevant than 1.

**Distracting Red Herring (version 5)**  
 1R  
 Artifact Creature — Fish Clue  
 2/1  
 Whenever CARDNAME attacks, target Detective you don't control can't block this turn.  
 2, Sacrifice CARDNAME: Draw a card.

The "must be blocked" wasn't pulling its weight, so they tried a different flavorful ability. Red Herring now had an attack trigger that worked against Detectives, the creatures most flavorfully affected by red herrings. In the end, the design team decided the red herring flavor of causing problems wasn't providing enough gameplay value to be worth it. They added the must attack restriction, which then allowed them to change it from a 2/1 to a 2/2. They decided keeping it clean and simple made for a better final card.

Here's the art description for the card:

**Setting**: "Polo" Ravnica  
 **Color**: A red-aligned artifact creature  
 **Location**: A waterfall in Izzet turf (see pages 174–182)  
 **Action**: Show an Izzet-made CLOCKWORK FISH constructed of REDDISH-HUED METAL. It LEAPS out of the water, against the strong current of a waterfall. Maybe parts of this fish are exposed so we see the clockwork innards.  
 **Focus**: The clockwork fish  
 **Mood**: A fish crafted by skilled Izzet inventors

## Sometimes, Crime Does Pay

That's all the time I have for today. I hope you enjoyed my card-by-card design stories from *Murders at Karlov Manor*. If you have feedback on the column, any of the cards I talked about, or the set itself, feel free to email me or contact me through any of my social media accounts ([X \[formerly Twitter\]](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week when I explore the history of hybrid mana.

Until then, may you solve the mysteries of many *Murders at Karlov Manor* games.
---
id: m2mkfm3q
kind: article
lang: en
path: /en/articles/card-preview/2023/04-04-a-battle-for-the-ages-leading-march-of-the-machine-set-design
title: 'A Battle for the Ages: Leading March of the Machine Set Design'
published: '2023-04-04'
column_slug: card-preview
column: Card Preview
authors:
- slug: dave-humpherys-4a7b522e
  name: Dave Humpherys
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
    lang_detected: en
    capture_id: 160585
    url: https://magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
    captured_at: '2024-05-18 01:23:22+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
    lang_detected: en
    capture_id: 160585
    url: https://magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
    captured_at: '2024-05-18 01:23:22+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
    lang_detected: en
    capture_id: 160585
    url: https://magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
    captured_at: '2024-05-18 01:23:22+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
    lang_detected: en
    capture_id: 160585
    url: https://magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
    captured_at: '2024-05-18 01:23:22+00'
    rule: url.article_section
sources:
- document_id: m2mkfm3q
  url: https://magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
  page_key: magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:23:22+00'
  capture_id: 160585
  wayback_url: https://web.archive.org/web/20240518012322id_/https://magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: m2mkfm3q
  capture_id: 160585
  url: https://magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
  wayback_url: https://web.archive.org/web/20240518012322id_/https://magic.wizards.com/en/news/card-preview/a-battle-for-the-ages-leading-march-of-the-machine-set-design
  captured_at: '2024-05-18 01:23:22+00'
  template: contentful
  sha256: fa517154c88be4399066143be9560e6b1d64b36eb2c0e87a4155a5e6906e10c4
render_recovery: []
---
Mark Rosewater has covered much of the goals and mechanics of *March of the Machine* in his past two articles (you can read those [here](/en/articles/makingmagic/2023/03-29-march-of-the-machine-learning-part-1) and [here](/en/articles/makingmagic/2023/04-03-march-of-the-machine-learning-part-2)). I'll put most of my focus here on the goals and considerations going into making our new card type: battle. He'll later be going into detail on how each of the planes are represented by the various battles. I'll also end on some quick notes about some of the other mechanics and a few previews.

One of the primary goals of the set was to represent the interplanar nature of *March of the Machine* and this epic war. Vision Design had handed off lands that could be envisioned like portals that you could spend mana to transform into more powerful lands that represented the various planes. I suspected we could reach a more exciting and novel way of conveying these goals. In short, with these lands, I was also concerned with complexity added into the resource system. Rather than delve into that model, I'll focus on what I like about where we ended up and provide some of the pathing that got us there.

Much of our early focus during set design included brainstorming new ideas for how we might tackle this conceptual space differently. We were only a couple of weeks into meeting as a Set Design team when we started to synthesize the elements that we wanted and went down a new path. There was a lot of collaboration in this process. Ari Nieh ultimately detailed and suggested the primary pitch, pulling several ideas together. She suggested using transforming double-faced cards that could be attackable by the player and could transform into multiple card types. She credited Ken Nagle in that pitch for the goal of attack-to-flip and Jadine Klomparens with the multiple card types on the back face. She noted that the flavor on the front would be a plane under Phyrexian assault and the back would be the "plane fighting back," which were notes that helped address Mark Rosewater's creative goals for this mechanic's role in the set.

## Gameplay

One of the scary things about making a new card type is potentially the lack of points of interaction with it. These would be permanents, so many cards would interact with them, but still quite a few other cards spell out specific types of permanents and would often fail to interact with battles. We were steady through almost all the process in not wanting cards that said "destroy target permanent" to solve these. They could get rid of them, but that's all. We didn't like having such cards be a design constraint, and the flavor of it felt off anyway. We were on board with opening things up beyond combat damage to include direct damage and other ways to remove counters though, basically anything that could bring the defense counters on them down to zero.

![Beast Within](https://media.wizards.com/2023/one/en_547354cf80.png) ![Red cross-out mark](https://media.wizards.com/2023/images/daily/redx.png)

![Render Inert](https://media.wizards.com/2023/mom/en_abf6439d49.png)

 

*Magic*'s combat engine would naturally allow for interaction with these cards via attacking and blocking. The reverse faces of the cards would be cast as normal, as usual card types where they could be interacted with in ways our game usually supports. In this fashion, we expected them to fit rather naturally into gameplay. Early playtesting with these felt promising and fun! Having them be attackable felt flavorful to a battle without adding extra rules. I personally love the idea of structuring their rules like planeswalkers enough so that if you understood that card type it would be easier to learn how these played too in blocking, attacking, and in how they could lose counters.

We realized we needed to balance and design around some concerns, though. The nature of the mechanic could lead to a feeling that games started to snowball board advantage. If you were ahead on board, you could pull further ahead on board. In and of itself, this isn't particularly how we'd want a mechanic to play. We made some specific adjustments and, for example, increased the mana values of some of the battle cards that were otherwise removing blockers in the early game and then allowing you flip themselves or other battles.

![Invasion of Muraganda](https://media.wizards.com/2023/mom/en_c9cb6e69be.png)

![Primordial Plasm](https://media.wizards.com/2023/mom/en_042d61044b.png)

**Invasion of Muraganda // Primordial Plasm**

 

We also played around with different styles of cards on the reverse faces that would still allow for comebacks for an opponent in ways you might typically see in Limited or Constructed.

The battles didn't necessarily help you close out a game and were working against the on-board snowball. They are balanced so that you'd get a large fraction of a card's worth of strength from the enters-the-battlefield effect on the front but would need to flip them for more than the average strength of a card. We were trying to strike the balancing point of normal strength based on how often you can leverage the extra value of the reverse face of the card. Once the defense counters on the battle remaining are above an opponent's life total, at least in two-player games, and, barring some exceptions, there's not much reason to attack them, so you're getting less power than usual in closing out a game. This helped facilitate certain types of comebacks at game endings for battle-heavy decks, which is something we do endeavor for in mechanics.

There are some parallels to various board games here. Battles can help build infrastructure but are at times at odds with points of victory or conditions. I'd expect some players to gravitate more to battles if they are more the build-up style of player than the more aggressively victory point–oriented player.

Another gameplay pattern we kept an eye on was that there was suddenly caution about attacking. What if I attack and my opponent plays a battle and I don't have anyone back to defend it? There's a fair amount of strategy around trying to time playing battles on turns that you can try to immediately defeat them. This play pattern is common enough that we at times considered trying to create a delay to being able to attack them built into their rules. Ultimately, though, they just felt too challenging to win in that delayed model and didn't look appealing as a card type. We continued ahead and kept adjusting defense numbers and effects to strike the most fun balancing points we could find. There will be times you might want to be more cautious, but it's still mostly correct to attack in situations where you usually would. The exceptions to this will be part of the learning curve. This set, more than most, will reward those who try their hand at the set early and learn how to navigate deploying and defending battles, how many battle cards are best to include, and what cards are overperformers on the warfront.

While battles have some similarities to planeswalkers, one very notable difference is how the challenges are being presented. Planeswalkers require certain types of interaction that not all decks are built to handle, and they usually accrue advantage each and every turn. Battles on the other hand have a one-shot effect, and even assuming you are able to cast them transformed on the same turn, they typically present a threat that is more likely to be something most decks are equipped to deal with. On average, it's felt that they don't have quite the same urgency to answer that many players at times don't enjoy in this space.

Beyond the above, there are plenty of scenarios that feel novel where you are making an unusual attack to defeat a battle at the cost of an attacker, scenarios that otherwise don't come up in quite the same way in previous *Magic* experiences.

## Who's in Control Here?

In the original pitch, the battles went under an opponent's control. In terms of rules, it made the most sense to enter under your control to get the enters-the-battlefield effect, then move to an opponent's control. We felt like this was perhaps the most intuitive way to handle this card type.

One of the latest big functional changes was to have them stay under your control instead. As we tested more, we were worried that cards like Rite of Oblivion, which was a major force in the real-world Standard as we were testing, might easily limit the popularity of battles if they just fueled your opponent with sacrifice fodder. We were also eager to open more ways for you to interact with cards like you'd usually be able to do, like bouncing them or using "flickering" or "sliding" effects that exile these cards and return them to the battlefield for their entering effects.

Rite of Oblivion Flickerwisp 

## What Do We Call Them?

Originally, we called these planes. We considered hijacking that name from Planechase, at least until that became a major theme for the Commander product. We realized that a name like this wouldn't translate well to most future settings. As a new card type, we wanted these to be reusable in future settings, and "battle" felt like the best word for that while hitting our other major goals. It was only four months into set design before we changed these to the battle card type. As part of this change, we agreed that each card name would directly reference the plane where it was occurring so it would be very clear where the battles were taking place. Beyond that, there was still much debate about the other words we wanted to use in the card titles. Through most of playtesting, they were the name of the planes followed by the word "Besieged." There was also temptation for Battle for Zendikar or other phrases that were callbacks to set names. In the end, we and the Creative team were most happy aligning these as "Invasion of \_\_\_\_\_." I was tempted to have their counters be loyalty counters so you might know what best to compare them to, but I think folks correctly told me that lacked flavor, so we landed on defense counters.

## Why Double-Faced Cards? Whose Side of the Fight Am I Enacting with These?

Double-faced cards (DFCs) come with some complexity. We even went to two DFCs per booster. I believe that complexity was well spent here. I also believe it goes a long way in telling the stories of these planes and making for exciting game pieces to own. I'm not sure we'll see so many DFCs in a set again, so I hope you enjoy our foray into cards that care about transformation, such as being a theme for the blue-green color pair in Limited.

The initial pitch, and what we stayed the course on, was that these would be depicting you, the denizens of the plane trying to liberate their plane from the Phyrexian invasion. The reverse face of the card would depict a pivotal character, creature type, or event to the resistance. Many of the reverse faces originated from very specific story asks from the Creative team, like in the case of Ephara being a key character in Theros. Similarly, there were also asks to depict the zombies of Innistrad and the faeries of Eldraine.

![Invasion of Theros](https://media.wizards.com/2023/mom/en_6a09338144.png)

![Ephara, Ever-Sheltering](https://media.wizards.com/2023/mom/en_a331c8d6fb.png)

**Invasion of Theros // Ephara, Ever-Sheltering**

 

There were a couple of oddball battles that we eventually narrowed down to only one, the Invasion of New Phyrexia, where the resistance were the aggressors, but we still showed a heroic Teferi as a key figure.

![Invasion of New Phyrexia](https://media.wizards.com/2023/mom/en_54d5057db0.png)

![Teferi Akosa of Zhalfir](https://media.wizards.com/2023/mom/en_a54964477a.png)

**Invasion of New Phyrexia // Teferi Akosa of Zhalfir**

 

Since this story focuses more on the denizens of the Multiverse overcoming the Phyrexian invasion than the last set, we felt this was the best presentation for the shape of these cards and players including them in their decks. For someone running a deck full of Phyrexian cards, the creative deployment on these cards is a bit more of a stretch, but I believe we still showed plausibly what was at stake and that it wasn't hard to imagine that you were taking the reverse faces of these cards into your compleated forces.

## Why Are They All Subtype Siege?

Battles weren't going to have a subtype at all until later in the process. As design progressed, other future design teams started exploring variants on battles. We wanted to make sure we had rules that would encompass those designs, too. We'd briefly explored variants, especially for Invasion of New Phyrexia, but ultimately, I wanted these all to work the same as much as possible for ease in learning. There was talk that maybe we could have the battles with permanents on their backs simply transform and the other card types cast. I believe we just wanted to have all the battles work the same way even though they had a variety of card types on the reverse face. I felt like we didn't need to innovate more in this space, much in ways I'd argued for consistency on Sagas all being straightforward three-chapter cards in the past when leading *Dominaria*.

## I've Never Heard of This Plane

I had a ton of fun looking through all the Planechase cards to look for obscure planes to fill out needed slots. I spent a fair bit of time looking at the art, names, and mechanics to try to take a best guess on what color(s) and designs best spoke to these planes that we knew so little about. We also took inspiration from stories, especially planes known to be the homeworlds of Planeswalkers. Hopefully, we see more of these planes someday. The hope is that these lesser-known planes would show the grand scope of the Phyrexian invasion of the Multiverse. It was a joy to see what artists did in expanding on this exploration. As I noted at the start, expect more details to come from Mark Rosewater on these planes.

![Invasion of Xerex](https://media.wizards.com/2023/mom/en_0a344c4fb7.png)

![Vertex Paladin](https://media.wizards.com/2023/mom/en_639e102d4e.png)

**Invasion of Xerex // Vertex Paladin**

 

## Other Mechanics

### Incubate

We've been deploying several noncreature artifact tokens in recent sets. As with many of these, this is a mana sink mechanic. It felt quite flavorful that these hatched over time into creatures with a vibe familiar to alien invasion tropes. They fed into the transformation theme. We decided these could flip at instant speed since they were generally simple creatures, unlike the transforming double-faced cards. In Constructed, I like the options these give against sweeper effects. They are great fodder for the sacrifice effects in the set.

![Incubator](https://media.wizards.com/2023/mom/en_01bec8f863.png)

![Phyrexian](https://media.wizards.com/2023/mom/en_c6e9ae10f0.png)

**Incubator // Phyrexian token**

 

### Double-Faced Cards That Become Phyrexian

Much of the justification for these was simply in being able to show the before and after of iconic creatures from many planes. The artists delivered here. We had fun trying to represent the bending of the color pie as these creatures picked up new abilities in their compleated form after you spent Phyrexian mana, in a fun callback to that mechanic, fashioned as easier to balance in an activated ability.

![Blightreaper Thallid](https://media.wizards.com/2023/mom/en_ef23dd039d.png)

![Blightsower Thallid](https://media.wizards.com/2023/mom/en_e5d1599faf.png)

**Blightreaper Thallid // Blightsower Thallid**

 

### Praetors

I loved the idea of Sagas here for a new twist on cycles of cards. We've executed on these cards so well in the past that it felt hard to top without going truly as big as we could in effects. I envisioned these as akin to planeswalker ultimates that if they were able to lurk around for a while on your board, they could spin up an ability that would usher in a very likely win for your game.

![Sheoldred](https://media.wizards.com/2023/mom/en_d8449de05a.png)

![The True Scriptures](https://media.wizards.com/2023/mom/en_ff20430f1c.png)

**Sheoldred // The True Scriptures**

![Sheoldred](https://media.wizards.com/2023/mom/en_0b6689cce9.png)

![The True Scriptures](https://media.wizards.com/2023/mom/en_b6e8552c75.png)

**Planar Booster Fun**

 

### Backup

I love combining mechanics and keywords. See my set lead on mutate in *Ikoria: Lair of Behemoths*. Backup was just a particularly lovable mechanic in Limited, and I'm hopeful we have some cards that will play roles elsewhere. Trying to optimize where you put your counters and how to make a fierce attack to threaten defeat on a battle are all a part of the fun.

![Voldaren Thrillseeker](https://media.wizards.com/2023/mom/en_fbfa8be61b.png)

**Voldaren Thrillseeker**

![Extended-Art Voldaren Thrillseeker](https://media.wizards.com/2023/mom/en_e801817f8c.png)

**Extended Art**

### Convoke

We were eager to try out convoke in colors the mechanic has been less explored. This, like backup, was another opportunity to highlight folks working together to fend off the Phyrexians. Because blue and red are traditionally light on creatures, we wanted to make sure they had extra support in having cards that make multiple creatures at once, sometimes in the form of creature tokens. Take a look at Ral's Reinforcements:

![Ral's Reinforcements](https://media.wizards.com/2023/mom/en_f46c367d2f.png)

**Ral's Reinforcements**

We very intentionally created a new card here rather than a reprint so that we could have the tokens be two colors to more flexibly fuel the color requirements of convoke spells.

And what better way to explore convoke in blue than in seeing what our traditional four-mana, draw-two instants look like when they don't necessarily require four mana. I'm very curious to see what Meeting of Minds is capable of.

![Meeting of Minds](https://media.wizards.com/2023/mom/en_4b0e29a264.png)

**Meeting of Minds**

## Legendary Team-Ups and Delivering on an Event Set

The team-ups between two legends were so much fun to work on and an unexpected high point for the set. They were amongst the most rewarding cards to design that I've ever worked on. I hope they bring as much happiness to our players as they did internally in playtests.

![Borborygmos and Fblthp](https://media.wizards.com/2023/mom/en_a20187da10.png)

**Borborygmos and Fblthp**

![Borborygmos and Fblthp](https://media.wizards.com/2023/mom/en_6c42214342.png)

**Planar Booster Fun**

Much of the fun of making *March of the Machine* was also in helping share a story through cards. I had the pleasure of leading *War of the Spark* design and loved leading another "event set" to bring a story arc to its culmination again here. On that note, I leave you with the final preview card of the article, a heartfelt Seed of Hope.

![Seed of Hope](https://media.wizards.com/2023/mom/en_f42f156cd4.png)

**Seed of Hope**
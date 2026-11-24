---
id: b87rqxmw
kind: article
lang: en
path: /en/articles/makingmagic/2023/05-15-march-of-the-machine-vision-design-handoff-document-part-2
title: March of the Machine Vision Design Handoff Document, Part 2
published: '2023-05-15'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 223009
    url: https://magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 01:16:49+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 223009
    url: https://magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 01:16:49+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 223009
    url: https://magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 01:16:49+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 223009
    url: https://magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 01:16:49+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: b87rqxmw
  url: https://magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
  page_key: magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:16:49+00'
  capture_id: 223009
  wayback_url: https://web.archive.org/web/20240518011649id_/https://magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: b87rqxmw
  capture_id: 223009
  url: https://magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
  wayback_url: https://web.archive.org/web/20240518011649id_/https://magic.wizards.com/en/news/making-magic/march-of-the-machine-vision-design-handoff-document-part-2
  captured_at: '2024-05-18 01:16:49+00'
  template: contentful
  sha256: 56528c88ab6de390be4b317e8af5eeca43e3abbea8059ecd070acc2a2096df9d
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
[Last week](/en/articles/makingmagic/2023/05-08-march-of-the-machine-vision-design-handoff-document-part-1), I shared the first half of my *March of the Machine* vision design handoff document. Today's article includes the second half. Most of the text below consists of the actual document as it was turned in, with my notes in boxes for greater explanation and context.

## Coalition (Actual Name of This Group TBD)

The Phyrexians are a singular race, so it's much easier to create a cohesive mechanical feel for them. The coalition are only defined by not being Phyrexians. They represent almost every creative thing we've ever done in any set for the last 28 years.

The key to capturing the defenders cohesively was twofold. First, we leaned on parallel design—that is, we showed how different planes all do the same thing. The coalition are all different, yet in some ways they are very alike. Second, we leaned on a theme of teaming up. The defenders are desperate to save their respective planes, so they're willing to work with whomever to do that, even if that someone is normally an enemy.

**Planes (maybe new card type, maybe new subtype)**

**Portal to Amonkhet**  
 Land — Desert  
 CARDNAME enters the battlefield tapped.  
 T: Add B.  
 2B, T: Exile CARDNAME and return it to the battlefield transformed. Then planeswalk to CARDNAME. It loses non-mana abilities once it has no loyalty. Activate only as a sorcery.  
 /////  
 **Amonkhet, the Plane**  
 Land — Desert Plane  
 T: Add B.  
 Whenever a creature you control becomes blocked, defending player loses 1 life.  
 4B, T: Planeswalk to CARDNAME.  
 Whenever you planeswalk here, create a 2/2 white Zombie creature token.  
 Loyalty 2

**Portal to Innistrad**  
 Land  
 CARDNAME enters the battlefield tapped.  
 T: Add B.  
 3B, T: Exile CARDNAME and return it to the battlefield transformed. Then planeswalk to CARDNAME. It loses non-mana abilities once it has no loyalty. Activate only as a sorcery.  
 /////  
 **Innistrad, the Plane**  
 Land — Plane  
 T: Add B.  
 Whenever a creature card leaves your graveyard, you gain 2 life.  
 5B, T: Planeswalk to CARDNAME.  
 Whenever you planeswalk here, return target creature card from your graveyard to the battlefield.  
 Loyalty 1

We started approaching the defenders by pulling way back. I said above that we wanted to look at every aspect of the set through the lens of the planes, so why not think of the defenders collectively as the planes they defend?

Part of accomplishing this was finding a way to create a mechanical component that highlighted the planes in a loud, visceral way. *Planechase* had done this, but it deviated in a few ways from what we wanted here. First, the plane cards are oversized cards such that we couldn't put them in booster packs (well, not easily) or in decks.

Second, they represent places on each plane. We were interested in capturing the entire essence of a whole plane on one card. For example, we wanted players to be able to collect the planes or have plane names come up in gameplay.

Third, the *Planechase* plane cards treat the planes under the old cosmology. You could only ever interact with planes one at a time, and they never interacted with one another. The story in "Marathon" (with the Phyrexians changing the nature of the World Tree) is creating a new cosmology where planes can interact with one another. We wanted this mechanic to help capture this new reality.

Most of what I say here ended up being true in the finished product. This paragraph is a great example of an important function of this document. I don't just need to explain what we're doing but also why. Battles, for instance, changed greatly from where we handed them over, but being clear on why we wanted them to exist helped Set Design figure out what they should be.

Planes are double-faced cards with a land on the front. Other than the transformation ability, the land just produces mana, and currently, all of them enter the battlefield tapped. (Set Design can experiment with lands that require life to enter untapped.) Each card has a transformation cost to transform to the other face. This face represents the plane. Currently, the back face is also a land with a subtype (we're currently using "plane," but that will probably have to change). It's possible the back wants to be its own card type, possibly a combination of land and plane (whatever we call it).

We knew from the beginning that the *Planechase* cards being card type plane was going to cause problems with us calling these "plane," but it was the word that best captured the feel we needed, so we used it with the acknowledgement that we'll eventually have to find another word.

The back face has four elements. First, it taps for the same colors as the front face of the card. We experimented with players losing the mana when they transform to the plane, but Play Design had concerns with it, so we added the mana.

Second, it has a static ability. This ability becomes active as soon as the card is transformed.

Third, it has an activated ability. Most require mana, but some just require a tap. When you transform the card, it always duplicates the tap ability from the back face. For example, when you transform Portal to Amonkhet to Amonkhet, you get a white 2/2 Zombie creature token.

Fourth, it has a loyalty (that word could easily change). Planes can be attacked by creatures and lose loyalty just like a planeswalker. When a plane loses all its loyalty, it loses all abilities save the mana production. The assumption is that we'll have a frame that makes it clear what gets lost when the plane "falls to invaders."

It's interesting to note that the one aspect that carried through (other than the larger "totality of the plane" feel) was that they were attackable items.

Of all the components in the design, this is the one that still needs the most work. It is, by far, the most ambitious part of the design, but because it's so core to the identity of the set, we feel its inclusion is crucial. We got a lot of good notes from Play Design about the mechanic. The card has many knobs, so we're hopeful Set Design can find the right mix to make these work. As I said above, the plan is for every booster to have a plane.

I knew when I wrote this document that we hadn't solved this problem, which is why I spent a lot of time talking about it. The Vision Design team tries to solve as many design problems as they can, but there's always something we didn't get to, or didn't solve in the optimal way, which is why looking back at these documents is always informative.

For the numbers to work out to have one plane per booster, we're going to need somewhere from 30 to 40 plane cards. To help with this, Vision Design made a list of plane buckets. Bucket 1 includes planes that we've visited before that have a style guide. Bucket 2 includes planes that we think players are generally familiar with but don't meet the requirements of Bucket 1. Bucket 3 includes every plane that has ever been referenced in any official source that's not in Bucket 1 or 2. Here's the list:

We ended up with 36 battles, so my general sense of what we needed was pretty spot on.

### Bucket 1: Major Planes

Alara  
 Amonkhet  
 Arcavios (Strixhaven)  
 Dominaria\*  
 Eldraine  
 Ikoria  
 Innistrad  
 Ixalan  
 Kaladesh  
 Kaldheim  
 Kamigawa  
 Lorwyn/Shadowmoor  
 New Celesta  
 New Phyrexia\*  
 Ravnica  
 Tarkir  
 Theros  
 Zendikar

Everything from this list made it onto a battle. There was some talk about whether New Phyrexia was supposed to be included (that's why there's an asterisk), as it was the one plane not being invaded by the Phyrexians. Ideally, we wanted it included, and I'm happy Set Design and the Creative teams found a solution to let it be.

I'm not sure why Dominaria has an asterisk. Maybe because it's had multiple different style guides over the years.

### Bucket 2: Minor Planes

Bolas's Prison Realm  
 Fiora  
 Kylem  
 Mercadia  
 Muraganda  
 Rabiah  
 Regatha  
 Segovia  
 Shandalar  
 Ulgrotha  
 Vryn

Every plane on this list save Bolas's Prison Realm and Rabiah ended up making it onto a battle (and I know Rabiah was on a battle for a while in design).

### Bucket 3: All Other Planes

Not listed here, as it's a long list.

Ari made this list, and it was surprisingly long (which is why I didn't list it in the document). It was posted online along with our meeting notes. I believe all the other planes to make it onto battles were on this list.

Our plan is to have plane cards from all of Bucket 1 and most of Bucket 2, with maybe a smattering from Bucket 3. Also, these didn't go in a bucket, but we have new upcoming planes. We might want to do a few new planes here as a throw-forward to them.

I was pretty accurate in my guess as to how we'd use the buckets. As to upcoming planes, let me talk about that for a second. We work two to three years ahead. In that time, we have several new planes coming. We did examine the idea of doing a few "throw ahead" planes where we introduce a plane that we've never referenced before and then pay them off in the upcoming years when we visit there. So why didn't we do this?

One, it's a lot of work to do planes ahead of time. We know this from *Magic Origins* when we previewed Kaladesh. Basically, you have to front-load some of the early worldbuilding work, and it takes extra time and resources. *March of the Machine* already had scope issues, so the idea of doing even more things felt a little too overwhelming.

Two, if we showed off a plane we'd never mentioned while every other plane had been mentioned somewhere before, we felt we'd be making a pretty large announcement of "we're visiting this plane soon," and we didn't want that to pull focus from *March of the Machine*. We wanted the audience more focused on the planes they knew rather than the one(s) they didn't.

**Boost (new mechanic)**

**Kitesail Guide ZEN**  
 4U  
 Creature — Merfolk Rogue  
 2/2  
 Flying  
 Boost 1 (When CARDNAME enters the battlefield, put a +1/+1 counter on target creature. That creature gains all of CARDNAME's abilities until end of turn.)

**Naya Blademate ALA**  
 3R  
 Creature — Cat Warrior  
 1/1  
 Double strike  
 Boost 1 (When CARDNAME enters the battlefield, put a +1/+1 counter on target creature. That creature gains all of CARDNAME's abilities until end of turn.)

Boost is a new mechanic representing the defenders working together. When a creature with boost enters the battlefield, you choose target creature (which can be itself), and then it gets N +1/+1 counters (where N is the boost number) and gains all abilities of the boost creature until end of turn. For example, you play Kitesail Guide with a Grizzly Bears under your control on the battlefield. You can choose to give your Kitesail Guide a +1/+1 counter, or you can give it to your Grizzly Bears and it will gain flying until end of turn. The boost creatures are designed with abilities that you'd want to grant to other creatures to create interesting choices when you cast them.

I'm surprised the samples don't have a boost higher than 1. Usually when there's a variable, we do that to show off how the variable might work. It's also cool that both sample cards ended up making it into the set, although with numbers changed, and Kitesail Guide moving to white.

**Convoke (returning mechanic)**

**Regisaur's Charge XLN**  
 1R  
 Sorcery  
 Convoke  
 Target creature gets +4/+2 and gains trample until end of turn.

**Second Sun's Dawn AKH**  
 5WW  
 Sorcery  
 Convoke  
 Destroy all creatures. For each creature you control destroyed in this way, create a 1/1 white Spirit creature token with flying.

We were looking for a mechanic that both conveyed a sense of teamwork and could go on instants and sorceries (as most of the other mechanics are very permanent-centric). Convoke was an existing mechanic that felt like a perfect fit, so we added it to the set. The Vision Design team did experiment with fun and flavorful ways to use it.

When I started to write this article, I believed the idea of pushing it into blue and red, the two colors that had least used it before, came up during set design. As you'll see in a second, I just remembered wrong.

**Team-up legends**

**Zurgo and Anafenza DTK**  
 RW  
 Legendary Creature — Orc Spirit  
 2/2  
 Haste  
 Whenever another nontoken creature enters the battlefield under your control, put a +1/+1 counter on target creature.  
 1W: Return another target creature you control to its owner's hand.

**Sram and Gonti KLD**  
 1WB  
 Legendary Creature — Dwarf Aetherborn  
 2/3  
 Whenever you cast an artifact spell, exile the top three cards of target opponent's library. You may play one of them this turn. If it's a spell card, you may spend mana as though it were any color to cast it. This ability may not target the same opponent more than once each turn.

We liked the idea that this war forced enemies to work together. A cool way to do this was to create legendary creatures that represented two creatures on a single card. Currently, the set has a rare enemy-color cycle that does this.

This idea exploded once it got to set design. The file, when handed over, had five. The finished set had fifteen, and then there were even more in other related products. I think legendary team-ups is going to be a tool in our toolbox we make a lot more use of. It allows us to make cards for characters we've made before, but with a twist that makes them feel different.

**Superweapons**

**Strixhaven's Grand Rite STX**  
 5UUU  
 Sorcery  
 Convoke  
 Return all nonland permanents target player controls to their owner's hand.  
 Untap all nonland permanents you control.

**Falkenrath Vengeance ISD**  
 2BBB  
 Enchantment — Aura Curse  
 Enchant player  
 Whenever enchanted player is attacked, attacking player mills three cards and may return a creature card from their graveyard to the battlefield with a vengeance counter on it. If that creature would leave the battlefield, exile it instead of putting it anywhere else.

How does each of the planes react to the Phyrexian invasion? This rare cycle shows off the "super weapons" five of the planes put together from a giant spell on Arcavios to make a huge, potent curse on Innistrad.

This was a cool cycle (Ari came up with the core idea) that ended up not making the set. Elements of this did show up in the story, but it wasn't done as a mechanical cycle.

**Cross-plane cycles (cycle theme)**

Both the team-up legendary creatures and the super weapons show a valuable tool for communicating the coalition's similarities. "Marathon" can have cycles where each member of the cycle is from a different plane. This allows us to show parallel stories where we can see how the planes are both similar in their response while still being slightly different. I believe these cross-planar cycles can show up at every rarity and can be everything from very tight cycles to very loose ones.

This is something that was done, but a bit more subtly than I expected. *Magic* sets need cycles, and this seemed like a cool way to play into the theme. The execution that didn't happen (that was in the vision design handoff file) was something like a cycle of Knights that showed off how five different planes had very different knights. I liked the idea that the structure of cycles could be used to demonstrate how different planes had similar elements that were fundamentally different in certain ways. ("On this plane, knights ride giant cats.") I do think if there had been watermarks, this might have been a little louder.

**Bonus sheet**

This isn't officially in the file right now but is an idea the Vision Design team talked a bit about. One of the ways we could show off the breadth of the defenders fighting off the Phyrexians is to have a bonus sheet of cards in the set that shows off elements from all the different planes fighting. We believe the cards selected for the bonus sheet should be things iconically from specific planes. We even talked about restricting the list to cards with proper names in their titles. I'm not sure this component is necessary, but it would be a cool and thematic addition to the set.

The Set Design team ended up being even a bit more focused than our suggestion on how to do the bonus sheet. I do like how the bonus sheet ended up.

Finally, as I mentioned above, we do think it's important that each card have some way of identifying what plane it occurs on. We feel this detail will help reinforce the gravity and size of the war.

Booster fun did take this idea and run with it, but I do wish there had been some way to help communicate this on the normal cards.

## Both Sides

While most of the set falls on one side or the other in the conflict, we do think it's possible to have some cards in the set represent the totality of the conflict. Here's the example currently in the file:

**Battle enchantments**

**Battle of Malakir ZEN**  
 1BB  
 Enchantment  
 Whenever you play a land or attack, put a war counter on CARDNAME. When the third war counter is put on CARDNAME, sacrifice it and choose coalition or Phyrexia.  
 \* Coalition — Return target creature card from your graveyard to the battlefield.  
 \* Phyrexia — Target player discards two cards. You draw two cards.

**Battle of Sokenzan NEO**  
 1R  
 Enchantment  
 Whenever you play a land or attack, put a war counter on CARDNAME. When the third war counter is put on CARDNAME, sacrifice it and choose coalition or Phyrexia.  
 \* Coalition — Exile the top four cards of your library. You may play them until the end of your next turn.  
 \* Phyrexia — CARDNAME deals 3 damage to up to two targets.

This is a rare cycle, set on five different planes, using anchor words (like *Fate Reforged*) where the player gets to choose which side is winning to help determine the effect of the enchantment.

This was another cycle that didn't end up seeing the light of day. I think that battles end up being the place that showed the direct fight between the Phyrexians and the natives of that plane, which didn't give this cycle an identity. I am a fan of anchor words, especially when they can play up a core conflict in the set.

## Draft Archetypes

The Vision Design team was able to spend some time on the draft archetypes for the ten two-color pairs. Here's where they currently stand:

**White-Blue**: This is a tempo deck with a Knight tribal component that represents the good guys teaming up to fight back.

This one mostly stayed.

**Blue-Black**: This is the "transformation matters" color combination that represents the Phyrexians assimilating everything.

This moved to green-blue. It ended up taking black-green's graveyard theme.

**Black-Red**: This is a deck built around sacrificing permanents. It represents both sides doing what it takes to win the conflict.

This one stayed, although black-red doing a sacrifice theme is as run of the mill as it gets.

**Red-Green**: This is a midrange deck that cares about having creatures with power 4 or greater. It represents the wilder parts of the planes fighting back.

This archetype ended up being about battles, which weren't a thing yet when this document was made.

**Green-White**: This color cares about +1/+1 counters and thus interacts with the boost mechanic. It represents the good guys building up their forces.

This theme stayed.

**White-Black**: This is the Phyrexian tribal archetype, as black is the color most associated with the Phyrexians and white is the color of their leader, Elesh Norn.

This was the theme I was happiest to see make it all the way through. I played this at the Prerelease and had a lot of fun.

**Blue-Red**: This is the archetype that plays the best with convoke. It represents the good guys working together.

Hmm, I always thought of convoke being in blue and red as a set design thing, but I guess it had its seeds in vision design.

**Black-Green**: This is a graveyard-based recursion deck. Like black-red, it probably represents aspects of both sides.

Blue-black ended up being the archetype that cared about the graveyard, so this archetype ended up being more about incubate and ramping into bigger creatures.

**Red-White**: This is the aggro deck of the ten. It has an affinity for Equipment and Vehicles. It also represents the defenders.

Red-white stayed aggro because, well, it's red-white, and it was still focused on the planar defenders, but everything else about this archetype changed. It ended up becoming a lot more about boost.

**Green-Blue**: This is a ramping deck designed to play nicely with planes. This is another deck representing the good guys.

Green-blue's archetype is either ramp or "care about the set theme," and often both. As the lands turned into battles, that theme moved to red-green, so green-blue stole blue-black's theme.

## In Conclusion

I'm proud of all the work the Exploratory Design and Vision Design teams did (along with the Creative team) to help create the blueprint for this very ambitious set. I'm excited to see what Set Design does with it. If you have any questions about anything said (or not said) in this document, please come talk to me.

Thanks,

Mark Rosewater

I'm very proud of how *March of the Machine* turned out. I think this document and all the work of the Exploratory Design and Vision Design teams had a big impact on the set. I want to thank Dave Humpherys and his Set Design team for taking all the ideas in this document and making them even better. Also, a nod to all the other hard-working teams downstream of us that did stellar work to make *March of the Machine* shine as much as it did.

And that, in slightly over 7,000 words, is the annotated version of the *March of the Machine* vision design handoff document. I hope you all enjoyed seeing it, and as always, I'm eager for any feedback on the article, the document, or *March of the Machine* itself. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week when I share another article in my "Lessons Learned" series.

Until then, may you have the chance to see your vision become reality.
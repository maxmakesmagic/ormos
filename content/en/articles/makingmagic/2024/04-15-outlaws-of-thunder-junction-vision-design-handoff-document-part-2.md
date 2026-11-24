---
id: apbn4p0n
kind: article
lang: en
path: /en/articles/makingmagic/2024/04-15-outlaws-of-thunder-junction-vision-design-handoff-document-part-2
title: Outlaws of Thunder Junction Vision Design Handoff Document, Part 2
published: '2024-04-15'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 225320
    url: https://magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 00:57:22+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 225320
    url: https://magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 00:57:22+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 225320
    url: https://magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 00:57:22+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
    lang_detected: en
    capture_id: 225320
    url: https://magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
    captured_at: '2024-05-18 00:57:22+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: apbn4p0n
  url: https://magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
  page_key: magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 00:57:22+00'
  capture_id: 225320
  wayback_url: https://web.archive.org/web/20240518005722id_/https://magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: apbn4p0n
  capture_id: 225320
  url: https://magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
  wayback_url: https://web.archive.org/web/20240518005722id_/https://magic.wizards.com/en/news/making-magic/outlaws-of-thunder-junction-vision-design-handoff-document-part-2
  captured_at: '2024-05-18 00:57:22+00'
  template: contentful
  sha256: 462a205f1ca6934d5e89187ab4e9ff6dab77c9dded38cab4251d08915012923d
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
[Last week](/en/articles/makingmagic/2024/04-08-outlaws-of-thunder-junction-vision-design-handoff-document-part-1), I showed you the first half of the actual document I handed off when *Outlaws of Thunder Junction* moved from the vision design process to the set design process. Today is the second half. All the text is the actual text from the actual document, except for the text in boxes, which is my commentary.

**Mission (Pay these additional costs to choose one or more)**

**Bank Robbery**  
 R  
 Sorcery — Mission  
 Pay these additional costs to choose one or more —  
 • {o1} Crack the Safe — Destroy target artifact. CARDNAME deals 2 damage to its controller.  
 • {o2} Pocket the Goods — Exile the top two cards of your library. Until the end of your next turn, you may play those cards.

**Escape Plan**  
 W  
 Instant — Mission  
 Pay these additional costs to choose one or more —  
 • {o1} Distract — Exile target creature. At the beginning of the next end step, return that card to the battlefield under its owner's control.  
 • {o3} Knock Out — Destroy target creature with the most power or tied for the most power.

**Stampede Into Town**  
 GG  
 Sorcery — Mission  
 Pay these additional costs to choose one or more —  
 • {o1} Ready to Ride – Put three +1/+1 counters on target creature you control.  
 • {o2} Hire Muscle – Draw cards equal to the greatest power among creatures you control.  
 • {o6} Charge! – You may put any number of green creatures from your hand onto the battlefield.

Escape Plan, with a few tweaks, made it to the set as Getaway Glamer.

Mission is our spell mechanic. It technically is an instant and sorcery subtype. Mission spells have a base cost and then a few modes, usually two or three, each with its own cost. The caster must choose one mode but is allowed to choose as many modes as they can pay. (We did discuss letting you choose zero modes to cast a spell that does nothing, other than counting as a spell, but decided against it. The team could relook at this decision.) Mission spells with two modes have three options (A or B or both A and B) while Mission spells with three modes have seven options (A, B, or C, A and B, A and C, B and C, or A, B, and C). We mostly used generic mana for the mode costs but also use colored mana on occasion. Currently in the file, we only used mana costs for the modes. I believe non-mana costs could have some significant impacts on digital if we're interested in them.

Missions became bonanza and ultimately spree. The finished version is close to what we turned over. The two biggest changes were: the Set Design team ended up using more colored mana costs for the modes than what we handed off; I talk about the second change below. I only mention it in passing above, but the Vision Design team did spend some time exploring whether it was okay to cast zero modes. In the end, there weren't enough things to do with it and it made the template a little less clear. I don't think the Set Design team explored non-mana costs for the modes.

For flavor reasons, we're treating Mission like anchor words where each mode has a flavor word or phrase associated with it. This gives the spells a larger sense of villainy as it represents the planning of illegal activities.

In the version we handed off (as you can see in the card examples above), each mode had a flavor word. The Vision Design team thought it added a lot of charm and helped capture the flavor better. It turns out that spree cards are already wordy and the flavor words weren't worth the space they took up.

**Outlaw *(Outlaws are Rogues, Assassins, Warlocks, and Mercenaries.)*** 

**Blink Bandit**  
 2B  
 Creature — Human Assassin  
 2/2  
 Flash  
 When CARDNAME enters the battlefield, target attacking outlaw gains deathtouch until end of turn. *(Outlaws are Rogues, Assassins, Warlocks, and Mercenaries.)*

**Shoot-Out**  
 4R  
 Instant  
 CARDNAME deals 5 damage to target creature. CARDNAME deals X damage to that creature's controller where X is the number of outlaws you control. *(Outlaws are Rogues, Assassins, Warlocks, and Mercenaries.)* 

**Baron of Evil**  
 2BR  
 Creature — Devil Warlock  
 3/2  
 Whenever CARDNAME or another outlaw enters the battlefield under your control, CARDNAME deals 1 damage to each opponent. *(Outlaws are Rogues, Assassins, Warlocks, and Mercenaries.)* 

Baron of Evil, with a few tweaks, went to print as Vial Smasher, Gleeful Grenadier.

Outlaws are a batch of creature types that currently includes Rogues, Assassins, Warlocks, and Mercenaries. These four were included because they have the right sense of feel, capture enough colors historically (focused in black, but hitting a lot of blue and red and a little white and green), and enable the Creative team to concept anything Set Design needs to mechanically be an outlaw. Rogues are doing the lion's share of the work with color. Mercenaries are the new token type I explain below. (Mercenary is an existing creature type, but used infrequently, and only appears on the tokens in this set.) Warlock helps us cover the spell casters and is a creature type we've been trying to make feel a bit more villainous. Assassin was a perfect flavor fit.

The plan, as handed off, was that Mercenary would only be used on the new creature token. It turns out that a lot of cards wanted to be outlaws for mechanical reasons, and the other three creature types didn't always make sense, so Mercenary ended up being used on a lot of cards. There weren't any cards that specifically interacted with the Mercenary tokens (as those cards just referenced outlaws), so the token type overlapping with creature types on cards wasn't a big deal.

Other creature types we considered that can be reexamined by the Set Design team: Barbarian, Berserker, Minion, Ninja, Pirate, and Rebel. We also talked about Warrior but realized it's used too often for "good guys." We normally batch with two to four creature types, but a fifth one isn't necessarily off limits if it makes sense appearing in this set in enough number. Like crimes, outlaws are a means to get a flavorful word in rules text and create a new deck-building challenge that is backwards compatible and thus usable in larger formats.

When we batch, our loose rule is to use two to five items. The sweet spot is three, but sometimes we need different numbers. When we were putting together the outlaw batch, we knew there were more than five creature types that could be used, so we prioritized what the set needed. Four felt right, but we wanted the Set Design team to be aware of other options. While we did do a check for how often those four appeared in sets leading up to *Outlaws of Thunder Junction*, we didn't do a pass on the runner-up list. The fact that *The Lost Caverns of Ixalan* introduced a bunch of new Pirates to Standard was a big motivation for Set Design to add it to the batch.

**Mercenary (1/1 red Mercenary token with "T: Target creature you control gets +1/+0 until end of turn. Activate only as a sorcery.")**

**Disposable Grunt**  
 R  
 Creature — Goblin Rogue  
 1/1  
 When CARDNAME dies, create a 1/1 red Mercenary token with "T: Target creature you control gets +1/+0 until end of turn. Activate only as a sorcery."

**Untouchable Politician**  
 4W  
 Creature — Human Noble  
 3/4  
 When CARDNAME enters the battlefield, create a 1/1 red Mercenary creature token with "T: Target creature you control gets +1/+0 until end of turn. Activate only as a sorcery."  
 Sacrifice a Mercenary: CARDNAME gains hexproof and indestructible until end of turn. Tap it.

**Scofflaw Boss**  
 2RW  
 Creature — Human Warlock  
 2/3  
 When CARDNAME enters the battlefield, create a 1/1 red Mercenary creature token with "T: Target creature you control gets +1/+0 until end of turn. Activate only as a sorcery."  
 Your Mercenary tokens have haste and tap for an additional +1/+0 when using their ability.

Untouchable Politician, with some tweaks, was printed as Prosperity Tycoon. Scofflaw Boss, with even more tweaks, was printed as Ertha Jo, Frontier Mentor.

Mercenary is a new creature token, one designed to capture the feel of henchmen. They do more support than anything else. The creature token has played well and is currently focused in red and white with a smattering in green.

When we first made the token, we toyed with them being Minion, but Doug, the creative liaison, preferred Mercenary. (We don't really use Minion much these days.) This creature ability was the first thing we tried; we liked it and never looked back. The token stayed in red and white, but the third color ended up being black, not green.

**Mount** ***(Pay COST to put this creature under target unmounted creature you control or remove it from a mounted creature. Mount only as a sorcery. While mounted, that creature gains this creature's other abilities and if it would be destroyed, instead an opponent chooses which card is put into its owner's graveyard.)***

**Saddled Porcupine**  
 1R  
 Creature — Beast  
 3/2  
 Menace  
 Mount 2 *(Pay 2 to put this creature under target unmounted creature you control or remove it from a mounted creature. Mount only as a sorcery. While mounted, that creature gains this creature's other abilities and if it would be destroyed, instead an opponent chooses which card is put into its owner's graveyard.)*

**Brushwaggon**  
 G  
 Creature — Brushwagg  
 1/1  
 CARDNAME gets +1/+1 while attacking.  
 Mount 2 *(Pay 2 to put this creature under target unmounted creature you control or remove it from a mounted creature. Mount only as a sorcery. While mounted, that creature gains this creature's other abilities and if it would be destroyed, instead an opponent chooses which card is put into its owner's graveyard.)*

**Hippogriff for Hire**  
 5W  
 Creature — Hippogriff  
 3/3  
 Flying, first strike, lifelink  
 Mount 4 *(Pay 4 to put this creature under target unmounted creature you control or remove it from a mounted creature. Mount only as a sorcery. While mounted, that creature gains this creature's other abilities and if it would be destroyed, instead an opponent chooses which card is put into its owner's graveyard.)*

**Consulate Mountie**  
 1W  
 Creature — Dwarf Soldier  
 3/1  
 CARDNAME has flying if it has a mount.

The idea of mounts, creatures that a humanoid can ride, has been a player ask for many years. Much like how *Kaladesh* felt it had to deliver on Vehicles (another common player desire), "Quilting," with its Western-inspired setting, feels like it's obligated to finally bring mounts to the game. While some of these can be horses, this is a fantasy game, so we can have all sorts of cool creatures to ride, from giant animals to Dragons.

We've talked about doing a mount mechanic for many years, but it never felt like the right set. That is until *Outlaws of Thunder Junction*. Everyone just assumed it was a given that we were going to do it.

Mount is an activated ability that allows you to put your creature, the rider, on top of the mounted creature and have the stack function similarly to how a mutate stack works (i.e., it's one unified creature). The top card, the rider, designates everything about the card but has the bottom card's abilities. You may pay the mount cost to separate the mount from the rider and make them two creatures again. Also, if the unified mount and rider ever die, you choose an opponent to decide whether the rider or mount is put into the graveyard. The other remains on the battlefield.

While the final set has saddle and the concept stayed in the set, this is the one mechanic that was handed off from the Vision Design team that didn't make it to print. We went down the path of a mutate variant because we were a little too enamored by the idea that the rider literally sat on top of the mount and that the two were treated as a singular creature.

This is currently the most complex mechanic rules-wise. Mount is trying to make use of mutate technology to capture the rider being on the mount and the two being a single entity. Mechanically, it has played well, but we understand that the Set Design team might need to simplify it. The two qualities we care most about is the rider being physically on top of the mount and the two being a single creature. If the current execution proves untenable, the Set Design team could look at doing a riff on reconfigure to capture the flavor of mount (meaning the mount is attached rather than a part of the rider).

Looking back, I can see the denial. I knew that we were asking for a complicated solution to something that had simpler answers. Interestingly, even my fallback, a reconfigure variant, was probably more complicated than we wanted. The design was solved by a different design team (which I was on) that had approached the same problem from a different vantage point. That team asked: what was the closest thing to mount that existed in the game? Vehicles, being the closest, gave us the direction we needed for the mechanic.

**Deserts**

**Cactus Field**  
 Land — Desert  
 CARDNAME enters the battlefield tapped.  
 When CARDNAME enters the battlefield, it deals 1 damage to target player.  
 {T}: Add {R} or {G}.

**Lost to the Desert**  
 1U  
 Instant  
 Return target nonland permanent to its owner's hand. If you control a Desert, opponents can't cast spells with the same name as that card until end of turn.

**Vulture's Snack**  
 1B  
 Instant  
 Target creature gets -2/-2. It gets an additional -1/-1 for each Desert you control.

Two of these cards were printed (mostly) as is. Vulture's Snack became Desert's Due (except templated correctly—"until end of turn" was implied). Cactus Field became Bristling Backwoods. The common dual land cycle was designed as a mirror of the "life gain lands" from *Zendikar* and *Khans of Tarkir* where the dual lands come into play tapped and give you 1 life. The 1 damage felt rougher, to match the tone of the plane, and counted as a crime for cards that cared about committing crimes. From their first design, they were Deserts. I'm always happy when cards we handed over from the vision design make it into the printed product unchanged.

We have one other nod to Westerns mechanically. We're bringing back the Desert subtype. The file includes some lands with the subtype, including a common dual land cycle, and numerous cards that mechanically care about Deserts.

We knew from pretty early on that we wanted the Desert subtype on a few lands, but the team spent some time figuring out if we wanted any "Deserts matter" cards. Inspired by Gates from *Return to Ravnica*, we said yes.

## Draft Archetypes

Vision Design didn't get to spend a lot of time on draft archetypes, but here's what we have at handoff:

I'm surprised how close we got on a lot of these.

**White-Blue**: This color combination uses plot support for a slower control deck.

This archetype didn't stray too far from this. It has a theme of rewarding you for not playing spells on your turn, which plot helps you do.

**Blue-Black**: This is a slower manipulative crime-centered deck.

This archetype also stayed roughly the same.

**Black-Red**: This is the outlaw archetype with crime support.

Three in a row that stuck close to what we handed off.

**Red-Green**: This is a slower ramping deck with Mission and Treasure support.

This archetype is still about ramping but now rewards you more for having creatures with power 4 or greater.

**Green-White**: This is a midrange deck that has synergy with mounts.

While the mount mechanic changed completely, this archetype is still about focusing on Mounts (and the saddle mechanic).

**White-Black**: This is a token-sacrifice deck.

This archetype is still a token-sacrifice deck.

**Blue-Red**: This is a more tempo-y crimes deck.

This is one of the bigger changes. This archetype is now about casting two spells a turn and takes advantage of cheap spells and plot.

**Black-Green**: This is a slower deck that focuses on things not in your hand (graveyard and plot).

This archetype shifted away from its "not in your hand" theme to more just caring about the graveyard and bringing things back from it.

**Red-White**: This is an aggro deck that uses Mercenaries.

When handed off, red and white had the cheapest creatures and the most Mercenary creature tokens. None of that changed, so the archetype remained the same as well.

**Green-Blue**: This deck cares about casting second spells using plot for support.

This archetype still makes use of plot but leans into the "second spells matter" theme added by Set Design (also seen in the blue-red archetype).

I'm proud of all the work done by the Exploratory Design, Vision Design, and Worldbuilding teams to help create this set and plane. I can't wait to see what the Set Design team does with it. If you have any questions about anything in this document (or anything not in this document), please contact me.

Thanks,

Mark Rosewater

Some sets change a lot from the handoff, and some change only a little. *Outlaws of Thunder Junction* was mostly the latter (with the change of the mount mechanic being the biggest change). I want to thank Dave Humpherys and his Set Design team for finding the best execution of the vision design my team and I created.

## "Git a Long, Little Doggie"

That finishes our look at the document. I hope you enjoyed this behind-the-scenes look at the middle part of the design process. As always, I'm eager for any feedback, either on the article, handoff doc, or *Outlaws of Thunder Junction* itself. You can email me or contact me through any of my social media accounts ([X](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for *Outlaws of Thunder Junction* card-by-card design stories.

Until then, may you have a good time plotting and scheming.
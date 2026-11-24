---
id: vz8ts8p1
kind: article
lang: en
path: /en/articles/mtg-arena/2023/07-10-the-ring-tempts-you-on-mtg-arena
title: The Ring Tempts You on MTG Arena
published: '2023-07-10'
column_slug: mtg-arena
column: MTG Arena
authors:
- slug: ian-adams-1d137168
  name: Ian Adams
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
    lang_detected: en
    capture_id: 243647
    url: https://magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
    captured_at: '2024-05-20 18:14:56+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
    lang_detected: en
    capture_id: 243647
    url: https://magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
    captured_at: '2024-05-20 18:14:56+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
    lang_detected: en
    capture_id: 243647
    url: https://magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
    captured_at: '2024-05-20 18:14:56+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
    lang_detected: en
    capture_id: 243647
    url: https://magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
    captured_at: '2024-05-20 18:14:56+00'
    rule: url.article_section
sources:
- document_id: vz8ts8p1
  url: https://magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
  page_key: magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
  lang: en
  template: contentful
  captured_at: '2024-05-20 18:14:56+00'
  capture_id: 243647
  wayback_url: https://web.archive.org/web/20240520181456id_/https://magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: vz8ts8p1
  capture_id: 243647
  url: https://magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
  wayback_url: https://web.archive.org/web/20240520181456id_/https://magic.wizards.com/en/news/mtg-arena/the-ring-tempts-you-on-mtg-arena
  captured_at: '2024-05-20 18:14:56+00'
  template: contentful
  sha256: 381f242e97ffa5ec9766fa408f6f55e27d25e92b54c2cfbe1658afab7f736e65
render_recovery: []
---
***(Editor's Note: Join Ian Adams in a [](https://discord.gg/wizards-magic)*[Magic *Discord Q&A*](https://discord.gg/wizards-magic) *on Tuesday, July 11, beginning at 1 p.m. PT / 20:00 UTC.)***

Design on *MTG Arena* is a constant tightrope walk. *Magic* is a very complicated game, and it is regularly increasing in complexity. Take the Defiler cycle in *Dominaria United*, such as Defiler of Vigor. We present the ability on those cards using Phyrexian mana symbols. We do this because it effectively and efficiently communicates the interaction to the player and doesn't create a new, different UI for performing what is more or less the same action. But, of course, it's not the same action. You aren't paying Phyrexian mana. You aren't actually paying that mana at all. Instead you’re discounting the cost. At the end of the day, the call was made that the clarity provided for the majority of players and interactions was worth the cost of the UI being slightly misleading about the underlying rules.

![The Lord of the Rings: Tales of Middle-earth logo and Magic: The Gathering Universes Beyond logo](https://images.ctfassets.net/s5n2t79q9icq/6CD9PhihniOG1WoBZyHJfS/5e40415cdc58b9b43871cfd82bd58328/LTR_-_Universes_Beyond_EN.png?w=660&fm=webp) 

This brings us to *The Lord of the Rings: Tales of Middle-earth*™ and specifically the Ring tempts you mechanic. In gameplay, this ability is straightforward. But behind the scenes, the rules that make it work are novel and presented a real challenge to represent correctly on *MTG Arena*. Altogether, the ability does a handful of different things.

# It Creates an Emblem, but Differently

Emblems have existed in *Magic* for over a decade.

*\*Pause to allow a subset of* Magic *players, myself included, to rapidly age like that* Saving Private Ryan *gif.\**

In all that time, they have only been created by planeswalkers (yes, that counts Teferi's Talent, because the planeswalker is ultimately the source of the ability that creates the emblem). For the first time, we've got an emblem that isn't. It's created by all kinds of card types. What's more, it only ever creates the emblem once. People familiar with Chandra, Awakened Inferno know very well that normal emblem creation stacks.

It is reasonable at this point to ask the question, "Then why is it an emblem at all?" Obviously, I asked this as well, and frustratingly, there are a number of good answers around it. The design of the Ring tempts you wants the progress made to persist regardless of the survival of individual permanents on the battlefield. We have a handful of methods for doing that (cards like dungeons, for example), but emblems are by far the cleanest solution.

![Screenshot showing the Ring helper card, the Ring emblem on the left of the battlefield, and in the center the Frodo Baggins card as the Ring-bearer](https://media.wizards.com/2023/images/daily/maqu3hevipow.jpg) 

Unfortunately, presentation needs here are fundamentally different. Every other emblem has all the rules it will ever have up front. When a player mouses over them, they see the abilities it *has*. With the Ring tempts you, players on both sides of the battlefield also want to know what abilities it *will* have.

# It Makes Non-Legendary Creatures Legendary

This is fine actually. We already support this. There's some VFX on it to call extra attention to the Ring-bearer designation, but this was zero additional work, so I'm just going to hang out in this paragraph for a second. Just chill with Tom Bombadil for a spell.

![Tom Bombadil card art](https://media.wizards.com/2023/images/daily/1920x1080_LTR_Tom%20Bombadil.jpg)

Tom Bombadil | Art by [Dmitry Burmak](https://web.archive.org/web/20230710000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&artist=+%3C%22Dmitry%20Burmak%22%3E)

# It Grants Abilities but Not Really

The rules reasons here are complicated, but it's important to understand that while the Ring tempts you has abilities that modify the behavior of your Ring-bearer, that creature never actually *gains* those abilities. Those abilities live on the emblem and modify game rules as they relate to the Ring-bearer. This means two important things:

1.  If your Ring-bearer loses all their abilities somehow (for example, by a Witness Protection), all the effects of the emblem created by the Ring tempts you remain. The creature itself never had those abilities in the first place.
2.  The code in *MTG Arena* that puts gained abilities onto cards in blue text didn't add anything to Ring-bearers by default, because, again, they never actually gained any abilities.

![Battlefield with Frodo Baggins as the Ring-bearer and the ability](https://media.wizards.com/2023/images/daily/chem2crubiro.jpg) 

So now we're back to the topic from the top of this: How do we balance necessary accuracy versus usable clarity? We recognized from the start that we'd need to do bespoke work to have the emblem display upcoming effects. But for the Ring-bearer, we initially seriously underestimated how aggressively we'd need to communicate the state of the emblem.

Most obviously, we've gone ahead and added text to the card that calls out the impact of the emblem. We went with gold text here rather than the normal blue because we didn't want to imply these were abilities the creature had gained. During initial internal discussion, this was controversial, as several people believed that, like the Phyrexian mana example from the opening, it was close enough that it was better to use blue text to avoid confusing players with a new text color. At the end of the day, the presence of Barrow-Blade in Limited made us decide that even if the gold text wasn't immediately clear to every player, looking at the board state after a Ring-bearer has lost its abilities would be clearer with gold text than the alternative.

![](https://media.wizards.com/2023/images/daily/yuyesog3xita.jpg) 

So how did it go? Did we make the right calls? Did we balance things in a way that was helpful to you as a player? Let me know! I'll be jumping on the *Magic* Discord Tuesday, July 11, at 1 p.m. PT to check in with folks and do some Q&A about *MTG Arena* generally. I hope to see you there!
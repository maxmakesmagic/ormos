---
id: zmd4w5zt
kind: article
lang: en
path: /en/articles/makingmagic/2018/09-17-guild-to-order-part-2
title: Guild to Order, Part 2
published: '2018-09-17'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
    lang_detected: en
    capture_id: 220838
    url: https://magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
    captured_at: '2024-05-18 02:37:12+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
    lang_detected: en
    capture_id: 220838
    url: https://magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
    captured_at: '2024-05-18 02:37:12+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
    lang_detected: en
    capture_id: 220838
    url: https://magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
    captured_at: '2024-05-18 02:37:12+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
    lang_detected: en
    capture_id: 220838
    url: https://magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
    captured_at: '2024-05-18 02:37:12+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: zmd4w5zt
  url: https://magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
  page_key: magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
  lang: en
  template: contentful
  captured_at: '2024-05-18 02:37:12+00'
  capture_id: 220838
  wayback_url: https://web.archive.org/web/20240518023712id_/https://magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
- document_id: zmd4w5zt
  url: https://magic.wizards.com/en/articles/archive/making-magic/guild-order-part-2-2018-09-17
  page_key: magic.wizards.com/en/articles/archive/making-magic/guild-order-part-2-2018-09-17
  lang: en
  template: drupal
  captured_at: '2022-01-18 12:54:58+00'
  capture_id: 889386
  wayback_url: https://web.archive.org/web/20220118125458id_/https://magic.wizards.com/en/articles/archive/making-magic/guild-order-part-2-2018-09-17
- document_id: zmd4w5zt
  url: https://magic.wizards.com/en/articles/archive/making-magic/guild-order-part-2-2018-09-17?c
  page_key: magic.wizards.com/en/articles/archive/making-magic/guild-order-part-2-2018-09-17?c
  lang: en
  template: drupal
  captured_at: '2022-10-25 12:35:48+00'
  capture_id: 889389
  wayback_url: https://web.archive.org/web/20221025123548id_/https://magic.wizards.com/en/articles/archive/making-magic/guild-order-part-2-2018-09-17?c
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: zmd4w5zt
  capture_id: 220838
  url: https://magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
  wayback_url: https://web.archive.org/web/20240518023712id_/https://magic.wizards.com/en/news/making-magic/guild-order-part-2-2018-09-17
  captured_at: '2024-05-18 02:37:12+00'
  template: contentful
  sha256: b542e383577b9cc0ce4ecd5cc154b132a820bf3f18f81ef6af1eb0a613cbcea8
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:Beyondbasicsmagic@gmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email
  occurrences: 1
---
Hello, everyone! [Last week](/en/articles/makingmagic/2018/09-10-guild-to-order-part-1), I started talking about how *Guilds of Ravnica* was designed and introduced you to the Vision Design team. I only got to one of the four guilds, so I'm back today to finish the story. Also, I have another cool preview card to show off. That said, let's jump back in. We left with me talking about Izzet, so let's move onto Dimir (I'm following the path of colors that overlap between guilds).

# Dimir

Dimir has had the least success with its past guild mechanics in two regards. One, neither was something we've wanted to bring back, and two, neither did a great job of capturing Dimir's feel. Transmute was a [tutoring](/en/articles/play-design/2017/07-14-the-m-files-hour-of-devastation-part-1#tutor) mechanic that interacted with the library. *Transmute \[cost\] ((cost), Discard this card: Search your library for a card with the same converted mana cost as this card, reveal it, and put it into your hand. Then shuffle your library. Transmute only as a sorcery).*

Cipher turned spells in saboteur effects, aka effects that trigger when you deal combat damage to an opponent. *(After casting the spell) you may exile this spell card encoded on a creature you control. Whenever that creature deals combat damage to a player, its controller may cast a copy of this card without paying its mana cost.)* While both captured an aspect of the Dimir, neither did a great job of giving the guild a strong mechanical feel. Dimir also had the problem that its mechanics haven't been particularly synergistic with the adjacent mechanics in color. In short, we knew going in that Dimir was probably going to be one of the hardest guilds to design for.

Vision Design struggled a lot with the Dimir mechanic. I believe it was the final mechanic, of all ten (we were working on both *Guilds of Ravnica* and *Ravnica Allegiance* at the same time), that we settled on. The mechanic we handed off from design was called "disguise," and it was a ninjutsu variant. The basic idea was that it was ninjutsu except the creature with disguise was swapping with the attacking creature, meaning that anything connected to it (enchantments enchanting it, equipment equipped to it, counters on it, etc.) were still attached to the new creature as it was treated as the same object.

Disguise was definitely fun, but it was both a little complex (with five mechanics in the set, we were trying to tone down the complexity of any individual mechanic) and not as synergistic with the mechanics around it. Vision Design had tried to adjust this with some smaller themes in the guild, but Erik Lauer (*Guild of Ravnica*'s set design lead) correctly felt that it wasn't doing the work it needed to do.

Erik looked at both the connected mechanics, Izzet's jump-start mechanic and Golgari's undergrowth mechanic (I'll get to this next), and realized that they both wanted help getting things into the graveyard. Connect that to Dimir's desire to play around with knowledge and/or the library, and Erik and his team came up with surveil, a library filter that allowed you to fill up your graveyard (basically a scry variant where the cards go to the graveyard instead of the bottom of the library).

Surveil is a great example of the trickiness of overlapping various guild mechanics in a way that allowed each guild to make use of shared keywords. There was some talk if the mechanic wanted to be a little splashier, but in the end, we decided that a subtle mechanic that helped you win in ways that were not so overtly obvious felt like the perfect Dimir mechanic.

# Golgari

Golgari is one of the guilds with the strongest identities, one where the philosophy and mechanics cleanly overlap. It's the "cycle of life" guild, which mechanically makes use of the graveyard, both by caring about it and by returning things to the hand or battlefield from it. Both Golgari's previous mechanics, dredge *(If you would draw a card, instead you may put exactly N cards from the top of your library into your graveyard. If you do, return this card from your graveyard to your hand. Otherwise, draw a card.)* and scavenge, *(Exile this card from your graveyard: Put a number of +1/+1 counters equal to this card's power on target creature. Scavenge only as a sorcery.)* were popular and flavorful (although dredge is probably the most broken guild mechanic in terms of power). The goal of the Vision Design team was simple: find another mechanic that fits this mold (pun, as always, intended).

The problem we ran into was that Golgari is so defined that everything we looked at just felt like a twist on things Golgari had already done. We talked about maybe bringing back one of the many graveyard mechanics from the past. I believe we had a whole meeting examining the prospect of bringing unearth back (the Grixis mechanic from *Shards of Alara*). In the end, the solution to our problem came from outside the team, from none other than Erik Lauer.

Erik's idea was to focus on a mechanic that cared about the graveyard rather than bringing things back from it. I'm not sure what exactly his inspiration was, but I always assumed it was [Lhurgoyf](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lhurgoyf) (from *Ice Age*). The mechanic was originally called "necrobloom" in vision design but is now called undergrowth. The idea was that the mechanic always cares about how many creature cards you have in your graveyard. The more you have, the larger the effect.

Erik's one caveat with the mechanic was that he didn't want to make players have to constantly check their graveyard, so all the undergrowth cards have an effect when you cast them or they [enter the battlefield](/en/articles/play-design/2017/07-14-the-m-files-hour-of-devastation-part-1#enters-the-battlefield-effects), which requires you to check your graveyard just once. Erik liked the synergy between Golgari and its connected guilds because Dimir had various ways to get cards into your graveyard (its surveil mechanic, milling, and discard-as-cost effects), while Selesnya had a lot of creatures, many of which would die as the guild did its thing. Undergrowth would be one of the two guild keywords turned in by Vision Design to make it to print.

# Selesnya

Of all the guilds, Selesnya has the best track record with guild mechanics. Convoke *(Your creatures can help cast this spell. Each creature you tap while casting this spell pays for one mana of that creature's color.)* was already brought back in a core set, and populate *(Create a token that's a copy of a creature token you control.)* is a mechanic that I believe will also return one day. Both mechanics are very popular with the players. Selesnya is all about playing a lot of creatures and overrunning the opponent either through a large number of small creatures or a small number of large creatures. We knew coming in that what we wanted was a creature-focused mechanic, one that encouraged you playing a lot of creatures.

We tried a number of different mechanics but ended up with one that we've tried in a number of sets—"creaturefall." Much like landfall or constellation, creaturefall comprises effects that triggered whenever a creature you controlled entered the battlefield. Many individual cards have done this over the years, but it's never been keyworded. Selesnya seemed like the right guild for which to finally do this.

The mechanic ended up getting killed in set design, but probably not for the reason you'd think. It ended up being too synergistic with Boros's mechanic (mentor, I'll get to it next). But wait, I keep talking about the need for synergy. Why would too much synergy be a problem? It stems into what we in R&D call the "Naya problem." Selesnya and Boros tend to have themes that naturally overlap with one another. Both guilds focus on a [go-wide](/en/articles/top-decks/2017/07-25-what-to-expect-at-pro-tour-hour-of-devastation#go-wide) strategy playing with a lot of creatures that attack with regularity. The reason this is a problem is that you want drafts to be open, wherein players have interesting choices. If two guilds are too synergistic, it means that those two guilds will constantly be drafted together and the number of unique strategies goes down.

Mentor was the more innovative and flavorful mechanic, so Erik opted to keep mentor and replace the Selesnya mechanic. He explored several new mechanics (including trying affinity for creatures, but only on activations), but also looked at some returning options. As I said last week, in past Ravnica sets we made returning mechanics off limits, but decided for the third time around to allow them. The more that Erik played around with the other mechanics, the more he realized that the perfect mechanic for Selesnya was convoke. It required creatures in a way that worked with Boros, but not too efficiently. There was some talk about if it was okay to bring back a guild mechanic (as opposed with bringing back something that hadn't been used in a guild before), but convoke was such a perfect fit, Set Design decided to use it.

Before we move along to Boros, it's time for me to show off my preview card as it's from Selesnya (in spirit at least, if not watermarked). Anyone who's read my stuff for any length of time knows I'm a big fan of creature tokens, and if you are too, you should enjoy my preview.

So, without further ado, click below to see Divine Visitation.

## Click here to reveal Divine Visitation

![Divine Visitation](https://media.wizards.com/2018/grn/en_Co3HGiNQzd.png)

This is one of those designs that when I first saw it, I said to myself, "How is it we haven't made this card yet?" Hopefully, many of you will have lots of fun with it.

# Boros

Boros is another guild that has a very focused theme, one that connects flavor and mechanics well. It's the aggro guild, the one that plays a lot of cheap creatures and attacks. It's the fastest of the ten guilds. Boros had one of the least flavorful mechanics with radiance *(Target creature and each other creature that shares a color with it. . .)* and one of the most flavorful with battalion *(Whenever this card and at least two other creatures attack,. . .)*. Vision Design was interested in seeing if we could find a mechanic that plays into the theme of Boros but added a little twist.

This resulted in my favorite of the *Guilds of Ravnica* mechanics, mentor *(Whenever this creature attacks, put a +1/+1 counter on target attacking creature with less power*). The mechanic always had the mentor name, and I loved how it used its flavor to help make a somewhat complicated mechanic feel much less complicated. I also like how it plays, in that it encourages you to think about your attackers in a different way than normal.

Mentor was the other mechanic that came in during vision design and made it all the way through to print. I know it was a mechanic that required a lot of work from Set Design to create the cards that played interestingly. Its synergy with Selesnya was straightforward in that small creatures play well with mentor. The Boros/Izzet synergy proved a bit more difficult. The Set Design team solved this by making red cards with jump-start that play well into Boros's strategies, either by helping boost creatures to aid with mentor or by removing blockers allowing smaller creatures to attack.

I'm eager to hear feedback from all of you once you've had a chance to play with mentor.

# And the Rest

Now that I've talked about the guilds, let me hit upon a few other minor themes.

**Shock Lands**

*   [![89066](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=89066)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=89066)
*   [![89072](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=89072)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=89072)
*   [![89093](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=89093)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=89093)
*   [![96923](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=96923)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=96923)
*   [![83731](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=83731)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=83731)

*   [![366439](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=366439)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=366439)
*   [![253680](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=253680)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=253680)
*   [![253681](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=253681)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=253681)
*   [![253682](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=253682)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=253682)
*   [![366335](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=366335)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=366335)

![Temple Garden](https://media.wizards.com/2018/grn/en_5gF9cjVAp8.png)![Steam Vents](https://media.wizards.com/2018/grn/en_fX1qglWknx.png)

When we planned to return to Ravnica for the third time, we'd always planned on bringing back the shock lands—interestingly though, not in the Ravnica sets themselves. The original plan was for the shock lands to be in the large sets the year before *Guilds of Ravnica*. A combination of logistics and not finding the right dual lands to put into the Ravnica sets made us change our minds and put the shock lands back. (It's an internal R&D joke that we specifically named the shock lands so they can fit into any world, and then we keep putting them on Ravnica.)

**Guildgates**

*   [![366390](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=366390)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=366390)
*   [![270964](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=270964)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=270964)
*   [![271099](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=271099)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=271099)
*   [![270961](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=270961)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=270961)
*   [![366313](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=366313)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=366313)

![Selesnya Guildgate](https://media.wizards.com/2018/grn/en_wbx89RoQfv.png)![Izzet Guildgate](https://media.wizards.com/2018/grn/en_o0bXOMWwcH.png)

Guildgates were created in *Return to Ravnica* block as a means to make common dual lands. The concern was that plain "enters the battlefield tapped" dual lands would feel too much like strictly worse shock lands, so the Gate subtype was added to give them extra functionality. The Guildgates are back, this time with a slight uptick on cards that care about the Gate subtype.

**Hybrid Mana and Split Cards**

*   [![Privileged Position](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Privileged+Position)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Privileged+Position)
*   [![97197](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=97197)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=97197)
*   [![366385](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=366385)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=366385)
*   [![290529](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=290529)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=290529)
*   [![[Odds] [//] [Ends]](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Odds+%2F%2F+Ends)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%5BOdds%5D+%5B%2F%2F%5D+%5BEnds%5D)
*   [![[Alive] [//] [Well]](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Alive+%2F%2F+Well)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%5BAlive%5D+%5B%2F%2F%5D+%5BWell%5D)

![Whisper Agent](https://media.wizards.com/2018/grn/en_xNSBDqrc5Z.png)

![Integrity // Intervention](https://media.wizards.com/2018/grn/en_PKkBktGxTP_side.png)

Original *Ravnica* introduced hybrid mana to the game. It has shown up in every Ravnica set since then, usually in a vertical cycle (on a common, uncommon, and a rare). The final set of each of the previous Ravnica blocks (*Dissension* and *Dragon's Maze*) had split cards as a means to get extra multicolor cards into the mix. *Guilds of Ravnica* and *Ravnica Allegiance* bring both these two elements back but combine them for the first time. There is a cycle of common hybrid cards. Then there is an uncommon and rare cycle of split cards. Each split card has one cheaper hybrid card and one higher-costed traditional multicolor card. There is also a cycle of common artifact mana fixers that make use of a hybrid activation.

**Guildmages**

*   [![87918](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=87918)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=87918)
*   [![83838](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=83838)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=83838)
*   [![87988](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=87988)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=87988)
*   [![96966](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=96966)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=96966)
*   [![87990](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=87990)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=87990)

*   [![366429](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=366429)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=366429)
*   [![270364](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=270364)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=270364)
*   [![Vitu-Ghazi Guildmage](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vitu-Ghazi+Guildmage)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vitu-Ghazi+Guildmage)
*   [![270366](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=270366)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=270366)
*   [![366328](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=366328)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=366328)

![Conclave Guildmage](https://media.wizards.com/2018/grn/en_5yycaYOOga.png)![Swarm Guildmage](https://media.wizards.com/2018/grn/en_wJChOjsUfS.png)

We always knew we were going to have Guildmages. The big question was how did we want to design them this time? Original *Ravnica* block has them as two-drop hybrid creatures that had two activations, one with each color. The idea with these was that you could play them in either color deck, but to optimize them, you had to have both colors. *Return to Ravnica* block had two-drop traditional multicolor cards with two activations which each required both colors of mana. The new Guildmages are a combination of the first two. They are two-drop traditional multicolored creatures, but they have two abilities, each one activated by a different color. The one new twist is that these activated abilities require a tap, so they can only be used once per turn.

**Guild Leaders**

*   [![89061](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=89061)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=89061)
*   [![Savra, Queen of the Golgari](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Savra%2C+Queen+of+the+Golgari)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savra%2C+Queen+of+the+Golgari)
*   [![Tolsimir Wolfblood](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tolsimir+Wolfblood)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tolsimir+Wolfblood)
*   [![96952](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=96952)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=96952)
*   [![89092](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=89092)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=89092)

*   [![366448](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=366448)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=366448)
*   [![290534](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=290534)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=290534)
*   [![Trostani, Selesnya's Voice](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Trostani%2C+Selesnya%27s+Voice)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Trostani%2C+Selesnya%27s+Voice)
*   [![253626](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=253626)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=253626)
*   [![Lazav, Dimir Mastermind](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lazav%2C+Dimir+Mastermind)](https://web.archive.org/web/20180917000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lazav%2C+Dimir+Mastermind)

![Lazav, the Multifarious](https://media.wizards.com/2018/grn/en_kVHUPiVjH0.png)![Aurelia, Exemplar of Justice](https://media.wizards.com/2018/grn/en_Ulg8LdPLjA.png)

In both *Ravnica* and *Return to Ravnica* blocks, there was a ten-card multicolor cycle of guild leaders and a second ten-card multicolor cycle of guild champions. *Guilds of Ravnica* and *Ravnica Allegiance* tweak this slightly. The five Bolas-leaning guilds have planeswalkers as their leaders. The resistance guilds have legendary creatures as their leaders. Then all guilds have one other cycle of legendary creatures. Who exactly these represent varies a bit from guild to guild, but they're always characters from that guild.

**Watermarks**

![](https://media.wizards.com/2018/images/daily/kyoKXWJ4HT.png)![](https://media.wizards.com/2018/images/daily/WZu1WgzNvf.png)![](https://media.wizards.com/2018/images/daily/yhXiE4tfyX.png)

![](https://media.wizards.com/2018/images/daily/CLOjkEoqvG.png)![](https://media.wizards.com/2018/images/daily/eUNmP8vxnF.png)

Another old component coming back are guild watermarks. Guild watermarks show up on any card with either both colors of the guild, the guild mechanic, or that requires both colors to optimize the card. (*Guilds of Ravnica* and *Ravnica Allegiance* don't have any cards with off-color activations.)

# Guilding a Better Future

That's all the time I have for today. I hope you all are as excited for Ravnica to return as I am. If you have any comments on today's article, *Guilds of Ravnica*, or any of the guilds, please feel free to drop me an email or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro)).

Join me next week when I share some card-by-card design stories from *Guilds of Ravnica*.

Until then, may you not fall to Bolas's influence.

* * *

 

##### #571: Color Talk - Black Speaks

##### #571: Color Talk - Black Speaks

39:11

I turn over my podcast to the color black, which explains in its own words what it believes. This is part three of a five-part series I'm calling "Color Talk."

[Download MP3 Format](https://media.wizards.com/2018/podcasts/magic/drivetowork571_blackspeaks_u8SdiP21.mp3)

  

 

##### #572: Bad Cards

##### #572: Bad Cards

45:23

I revisit two of my old articles ("[When Cards Go Bad](/en/articles/makingmagic/2002/01-28-when-cards-go-bad)" and the follow-up "[When Cards Go Bad Revisited](/en/articles/makingmagic/2012/10-22-when-cards-go-bad-revisited)") to talk about why R&D makes bad cards.

[Download MP3 Format](https://media.wizards.com/2018/podcasts/magic/drivetowork572_badcards_iJSr99oI.mp3)

*   [**Episode 570**](https://media.wizards.com/2018/podcasts/magic/drivetowork570_bluespeaks_hIl3e0D1.mp3) Color Talk - Blue Speaks
*   [**Episode 569**](https://media.wizards.com/2018/podcasts/magic/drivetowork569_whitespeaks_dI94DjeR.mp3) Color Talk - White Speaks
*   [**Episode 568**](https://media.wizards.com/2018/podcasts/magic/drivetowork568_throwingparties_4hj2Eo94.mp3) Throwing Parties
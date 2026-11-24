---
id: 7vbv602a
kind: article
lang: en
path: /en/articles/makingmagic/2024/05-27-third-times-the-charm-part-2
title: Third Time's the Charm, Part 2
published: '2024-05-27'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
    lang_detected: en
    capture_id: 230996
    url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
    captured_at: '2024-07-13 00:10:09+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
    lang_detected: en
    capture_id: 230996
    url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
    captured_at: '2024-07-13 00:10:09+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
    lang_detected: en
    capture_id: 230996
    url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
    captured_at: '2024-07-13 00:10:09+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
    lang_detected: en
    capture_id: 230996
    url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
    captured_at: '2024-07-13 00:10:09+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 7vbv602a
  url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
  page_key: magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
  lang: en
  template: contentful
  captured_at: '2024-07-13 00:10:09+00'
  capture_id: 230996
  wayback_url: https://web.archive.org/web/20240713001009id_/https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 7vbv602a
  capture_id: 230996
  url: https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
  wayback_url: https://web.archive.org/web/20240713001009id_/https://magic.wizards.com/en/news/making-magic/third-times-the-charm-part-2
  captured_at: '2024-07-13 00:10:09+00'
  template: contentful
  sha256: a4a7ebb735e6ce48ba39063d06ec8dc7759f285a25b8d31a9de2539b5721cc3c
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
Welcome to the second week of *Modern Horizons 3* previews. [Last week](/en/articles/makingmagic/2024/05-21-third-times-the-charm-part-1), I introduced the Vision Design team, showed off a preview card, and began the story of the set's design. Today, I will introduce you to some other design teams, show off two new preview cards, and finish the story of the set's design, including looking back at the history of the set's major mechanics.

## *Modern* Masters

As always, before I get into my design story, I want to introduce you to some of the people who made the set. Last week, I introduced the Vision Design team. Today, it's the Set Design team's turn. The introductions (even his own bio) were written by Michael Majors, *Modern Horizons 3*'s lead set designer.

## Click here to meet the *Modern Horizons 3* Set Design team

 

**Michael Majors (Set Design Lead)**

Michael joined Wizards of the Coast shortly before the hackathon that led to the conception of the original *Modern Horizons*. With his extensive background playing and writing about Modern in the competitive landscape, he was a natural fit to work on the project. He led final development for both *Modern Horizons* and *Modern Horizons 2*, and *Modern Horizons 3* was his first set lead. He placed an early emphasis on making *Modern Horizons 3* exciting for all lovers of *Magic* and *Magic*'s history.

**Carmen Klomparens (Vision Design, Set Design, and Final Development)**

Carmen was instrumental to the design team throughout the design process. Her love and knowledge of *Magic* and her strength as a designer can be felt throughout the product. She delivered countless references, fun *Time* *Spiral*-esque in-jokes, and ultimately participated in the final balancing of the cards alongside our contracted Future Future League team (pro players Brad Nelson, Brian Braun-Duin, and Mason Clark).

**Eliana Rabinowitz (Set Design, Digital, and Rules Liasson)**

One of the biggest challenges of making a *Modern Horizons* product is the need to mix and match mechanics from *Magic*'s history in exciting and sometimes unprecedented ways. On top of that, *Modern Horizons 3* is the first product of its kind to be featured on *MTG Arena*. Eliana was an invaluable source of rules knowledge for gut-checking our loftiest designs and ensuring a smooth transition to digital.

**Megan Smith (Set Design, Commander Play Design)**

Although *Modern* *Horizons*'s primary focus is on the Modern Constructed format, I also wanted to make sure it was exciting for everyone who plays *Magic*. A large part of making a set awesome for everyone is making sure Commander players love it. Megan's passion for both Modern and Commander made her an easy include on the team, and she helped ensure that we satisfied as many audiences as we possibly could.

**Michael Hinderaker (Set Design, Final Limited Balanced)**

Michael was a late add to the Set Design team as we approached the final stages and began entering development. His role as a play designer was to lead *Modern Horizons 3*'s final Limited balance, no easy feat with the wealth of both mechanics and mechanical complexity that exists in the product. He not only did a great job but also provided additional perspective on the set as it entered final development.

**Dan Musser (Final Development Lead)**

Dan's responsibility was late in the process, but an important one. In the past, I've been the development lead for the *Modern Horizons* products and even co-led with Dan on *Modern Horizons 2*, but as the set lead, we want to divvy up responsibilities to better ensure a system of checks and balances. Dan made sure that our team kept on track throughout the final balancing phase, making sure that the cards were both fun and powerful and that every card in the file was vetted properly and ultimately made for someone to love.

With this set, I'm going to start to do something I haven't done before. I'm going to introduce you to the Commander deck design team. They also work hard and deserve some recognition. These bios are written by Ethan Fleischer, the lead designer for the Commander decks.

## Click here to meet the *Modern Horizons 3* Commander deck design team

 

**Glenn Jones (Lead)**

Glenn distinguished himself as the technical lead for our Commander products and our *Universes Beyond* products and has a deep well of knowledge for *Magic*'s history and its lore. Glenn led the *Modern Horizons 3* Commander deck design team for a mere month before he left Wizards for another opportunity, but in that month, he identified compelling themes for each of the decks, setting up the next lead designer for success\[nbsp\]…

**Ethan Fleischer (Lead)**

Ethan's experience as the lead designer for *Modern Horizons* and *Modern Horizons 2*'s Vision Design teams meant that no time needed to be wasted getting him up to speed on what *Modern Horizons* was all about. He also took up Glenn's task of establishing best design practices for *Universes Beyond* products. Ethan led the design team for most of the design period, turning the rough ideas for the deck themes into full-fledged decks with cool card designs before handing the set off to\[nbsp\]…

**Reggie Valk**

Reggie has served on many design teams and quickly established himself a reputation as a valuable addition to the design group. He had recently completed design of the charming *Ravnica: Clue Edition*. Once the *Modern Horizons 3* Commander deck design team stopped meeting, Reggie took up the task of shepherding the set through final polish, redesigning several cards and improving cards in response to feedback.

**Daniel Holt**

Daniel arrived at Wizards as a *Magic* player who preferred competitive tournaments and was hired as a graphic designer. We've slowly corrupted him, assigning him to more and more design teams. He's now officially a senior game designer, a bona fide filthy casual Commander player, and has led design teams for upcoming products.

**Eric Engelhard**

Eric is a veteran of the tabletop games industry with a fascination with the history of *Magic*'s land cards. This made him the ideal choice for a design team making a strange land-themed deck. Eric is also an expert in the arcane knowledge of collation and is even now leading a design team for an upcoming product.

**Henry Davis**

Henry's main job at Wizards was as a user-experience designer, but he served on several design teams during his tenure with the company. His passion for game design, and especially Commander design, made him a great contributor to the team.

## A *Modern* Sensibility

When Erik Lauer handed the vision design file to the Set Design team, there were two main mechanical themes (colorless/Eldrazi and energy) and one new tool (double-faced cards). Michael and his team kept all three components and added one more mechanical theme (modified). These four components were the crux of the set's structure. I talked about DFCs last week, so let's dive into the history of the set's three mechanical themes.

### Colorless Mana

Colorless mana goes back to the very beginning of the game.

Basalt Monolith Mana Vault 

Sol Ring Channel 

Richard Garfield had created the five colors, but he liked the idea that some spells would be accessible to everyone. These would end up being artifacts in *Limited Edition (Alpha)*. Also, using only mana with a color would be too unwieldy for mana costs. To solve these two problems, he made what we now call generic mana. That's a cost with a number in a mana bubble. Generic costs can be paid by any color.

Because there were generic costs to be paid, Richard came up with the idea of colorless mana. Colorless mana couldn't be used to pay for colored mana costs, but it could be used for generic mana costs. Since there were a significant number of generic costs, Richard ended up making four cards that added colorless mana to your mana pool. At the time, it was just written out "add two colorless mana to your mana pool."

Rasputin Dreamweaver Sunastian Falconer 

Then in *Legends*, *Magic*'s third expansion, we started expressing colorless mana using the same symbol we use for generic mana, a number in a mana bubble. I assume it was done because that's how we represent colored mana in rules text. If I tap to add {oR} ![Red mana symbol](https://media.wizards.com/2023/images/daily/r.png), I can then use it to pay for any cost requiring {oR} ![Red mana symbol](https://media.wizards.com/2023/images/daily/r.png) or any generic cost. That's kind of true for two colorless mana. If I tap to add {o2}, I can use that to pay for any generic cost that requires {o2} ![Two generic mana symbol](https://media.wizards.com/2023/images/daily/2.png), but it's not limited to that. Also, it conflates two things, generic mana and colorless mana, as the same when they're not.

None of this was a problem until we got to *Oath of the Gatewatch*. Trying to find a novel way to capture the colorlessness and oddness of the Eldrazi, the *Oath of the Gatewatch* design team came up with the idea to use colorless mana as a cost. It was novel and a clever way to make a new kind of mana cost that was still backwards compatible. There was just one problem. The second you put generic costs in a mana cost, things get confusing. {o1}{oW} ![One generic mana symbol](https://media.wizards.com/2023/images/daily/1.png)![White mana symbol](https://media.wizards.com/2023/images/daily/w.png) could now mean either one generic mana and one white mana or one colorless mana and one white mana.

The only reason the overlap lasted so long was context told you which type of symbol it was. Once we put a colorless mana symbol in places that a generic mana symbol could go, we'd created ambiguity.

Kozilek, the Great Distortion Endbringer Matter Reshaper 

The solution was to give colorless mana a new mana symbol. We spent a lot of time on it and ended up with this: {oC} ![Colorless mana symbol](https://media.wizards.com/2023/images/daily/c.png). We then retroactively changed all the old cards that created colorless mana to use this symbol.

Colorless mana proved to be difficult to design for on two fronts. First, we have a well-crafted color pie where each ability is carefully assigned to one or more colors. Colorless isn't a color (as I like to say on my blog, "barefoot is not a type of shoe"), but it still needed some identity. We spent a lot of time talking about what colorless could and couldn't do.

Second, colorless mana in costs created a lot more structural requirements than we realized at first. Much like adding a new color would require access to cards that can produce it, colorless mana requires a set to be properly set up for it.

These two things combined make it hard to splash colorless mana costs. In addition, the colorless mana costs have become closely associated with the Eldrazi. I do think we can overcome this last part if we start it using elsewhere, but it's another factor that currently makes it tough to splash.

Since *Oath of the Gatewatch*, we've only used colorless mana on new cards once, in the Eldrazi Unbound *Commander Masters* deck. *The Brothers' War* vision design did toy with the idea of bringing it back there, even going so far as examining the idea of creating fifteen draft archetypes, the normal ten plus each color paired with colorless, but it was pulling the mechanical center of the set too far away from the nostalgia that was its focus.

I do think a premier set will use colorless mana in costs again, but I believe two things will be true when we do. One, it will be a large part of the set, something we can focus a lot of resources on. Two, my gut is it will be for something other than the Eldrazi. The longer we tie it exclusively to one creative connection, the harder it is to use freely elsewhere, and I do believe colorless mana costs are something we want to have as a tool.

Colorless mana costs were a great fit for *Modern Horizons 3*, as it's a theme that shows up a bit in Modern, but could use more cards. While I want new uses to explore other creative options, *Modern Horizons* sets are about nostalgia, so tying into the Eldrazi again allowed us to make a bunch of flavorful cards. The Eldrazi theme is tied to blue, red, and green, which I will get to below when I talk about draft archetypes.

### Energy

Energy was first designed during the original *Mirrodin* design.

Serrated Arrows 

The set was going to have a lot of artifacts, so we were trying to find some mechanical executions that captured artifacts. One of the cards we were inspired by was Serrated Arrows from *Homelands*. The card came with three counters, allowing you to use the artifact three times. We liked the idea that artifacts only had so many charges. That's how objects work in a lot of video games, and we thought it was a fruitful space to explore.

To help solidify things, we made all the counters that went on noncreature artifacts charge counters. This then led us to our next big idea. What if instead of removing a charge counter from this specific card, we could remove a charge counter from any of our cards. If we had Card A and Card B, which each came with three charge counters, that would mean we got six uses between the two, but not necessarily three and three. If Card A's ability was situationally more important, we could use it more times.

After a few playtests, we realized that charge counters had basically become a new resource, and we questioned if there was a cleaner way to execute on the resource. Putting the counters on our cards created a lot of logistical complexity. For example, we were encouraged to spread around our usage of the counters, so any one spell that destroyed an artifact didn't wipe out all our resources. In addition, if we used counters on creatures, we couldn't use +1/+1 counters (it's standard practice to use one main counter on creatures in a set so that in Limited you can tell what the counters on the creature signify), and an artifact-themed set really wanted +1/+1 counters for a bunch of cool flavor executions.

That's when we came up with the idea of a counter that went to the player. This had all the upside of the resource while removing a lot of the logistical complexity. We eventually realized it worked best with a symbol. We used E to represent it. We played with it a bunch, and it was a lot of fun.

So, what happened? My team and I simply designed too much stuff. In my early design leads, I tended to overdesign and make too many mechanical components. Bill Rose, then head designer, told me that there was too much stuff and something had to go. Energy was the least connected to the rest of the set, so I pulled it. As I like to say, *Magic* is a hungry monster. I had confidence we'd find a home for it one day. I mentioned it in passing in an article, calling it "Mechanic E," which caused players to inquire about it for years.

We tried it as the key mechanic for the Esper shard (white-blue-black) in *Shards of Alara*, but it wasn't a great fit. It wouldn't be until *Kaladesh*, thirteen years after original *Mirrodin*, that we'd find a home for energy.

Aetherworks Marvel Demon of Dark Schemes Aether Hub 

This time, we built the set around it mechanically and creatively. We made the energy symbol {oE} ![Energy symbol](https://media.wizards.com/2024/images/daily/e.png) and built a whole energy economy for the set. It ended up being stronger than we expected and warped multiple formats, leading us to ban some cards. Like colorless mana costs, it wasn't something we'd revisit for a while.

Longtusk Stalker Glimmer of Genius 

Energy had a cameo card in *Jumpstart: Historic Horizons* and showed up as the main mechanic in the Science! Commander deck from *Magic: The Gathering® – Fallout®*. Energy is another theme that players have been asking us to revisit. It was also a second-tier deck in Modern that we'd hoped we could give a boost. Energy was centered in white, blue, and red.

### Modified

For the *Magic* year that was *Zendikar Rising*, *Kaldheim*, and *Strixhaven: School of Mages*, I tried an experiment where I ran a mechanical element, modal double-faced cards (MDFCs), through all three sets. To get a sense of what that would look like, Aaron Forsythe, my boss, asked me to mock up three decks, one for each set. Only *Zendikar Rising* was in design, so I just extrapolated from what I knew about each set to make each deck feel appropriate.

I decided to give *Kaldheim* and *Strixhaven* a new mechanic in addition to the MDFCs to give them a little flavor and make them feel like something new. The mechanic I designed for the *Kaldheim* deck was modified (well, it just referred to Auras and Equipment). We'd experimented with themes that tried to cross Auras with Equipment in the past, but we never found something we liked. My idea here was to make it a keyword, inspired by the historic batch we'd done in *Dominaria*.

Halvar, God of Battle // Sword of the Realms 

When we finally got to *Kaldheim* design, I suggested modified, and it was added to the set. Over time, it was nibbled down to the point where it only existed on a handful of cards and the keyword was removed.

Kodama of the West Tree Goro-Goro, Disciple of Ryusei Invigorating Hot Spring 

Flash forward to *Kamigawa: Neon Dynasty* where we had an artifact and enchantment theme. We wanted some strategies that crossed between the two, and modified fit the bill perfectly. This is where counters were added to the definition.

Mirror-Style Master Ian the Reckless 

Other than showing up on a couple one-off designs, modified also fell into the camp of a mechanic that players had said they wanted more, something that Modern could use. Michael and his Set Design team added it because it did such a good job of shaping draft archetypes. Modified shows up mainly in white, black, and green.

Which brings us to the ten draft archetypes (with the text borrowed from the archetype write-up):

**White-Blue Energy Fliers**

Play flying creatures that get stronger the more energy you have. Use them to attack your opponent or otherwise find tricky ways to get past your opponent's blockers.

**Blue-Black Card Draw**

This classic blue-black control archetype employs a variety of ways to draw extra cards, then leverages them for additional effects to dominate the battlefield.

**Black-Red Artifacts**

Start small and go big. This black-red archetype uses a variety of artifact synergies, including the infamous affinity, to summon powerhouses from *Magic*'s past and future.

**Red-Green Eldrazi Spawn**

Even the smallest Eldrazi are worthy of fear. Overwhelm your opponent with your terrifying Eldrazi horde, aided by Eldrazi Spawn tokens, in this red-green archetype.

**Green-White Modified Bestow**

Bestow gives you the versatility to play creatures or use them as Auras to buff others. Go tall and then dare your opponent to stop you from going wide if they can weather the storm first.

**White-Black Modified Dies**

In this unique take on a white-black sacrifice archetype, you're going to be modifying your creatures with counters, Equipment, and Auras for long-term advantages.

**Blue-Red Energy Midrange**

Embrace your inner mad scientist! Blue-red energy gives you plenty of ways to manage different types of engine-like permanents to generate overwhelming advantage over your opponents.

**Black-Green Modified Adapt**

This black-green adapt archetype uses +1/+1 counters to great effect, giving creatures additional spell-like triggers to dominate the battlefield.

**Red-White Energy Aggro**

There's no point hoarding your excess energy here, so spend it and smash! This aggressive red-white archetype will do whatever it takes with energy to keep attacking turn after turn.

**Green-Blue Eldrazi Ramp**

In this green-blue archetype, generate Eldrazi Spawn and then use them to summon their much larger kin—and proceed to devour the Multiverse.

* * *

Finally, before I wrap up for today, I have two previews for you. One is a new card, and one is a reprint new to Modern. I'll start with the latter.

I designed this card many years ago. For some fun, I will tell you some facts about it and see if you can guess what card it is before I show you.

1.  The card was in a set where I was the only member of the design team.
2.  The card in Oracle uses an evergreen keyword action, but not one that existed at the time of its original design. It was introduced in *Magic 2012*.
3.  This card is of a card type that changed the color of its frame in *Eighth Edition*.
4.  This card causes another card to change zones.
5.  The first of the two words in this card's title is the nickname for a black-green-white deck that used to be played in the extended format.
6.  The second of the two words in this card's title is one letter short of the card with this rules text: "Change the target of target spell with a single target unless that spell's controller pays {o2}."
7.  The card's flavor text is: *Garbage in, treasure out.*

## Click here to see if you figured it out correctly

 

0293\_MTGMH3\_Bonus: Junk Diver 

Here are the answers to the clues:

1.  *Urza's Destiny* was the one design team where I was the only team member.
2.  The keyword in question was "dies." Death triggers were a small theme of *Urza's Destiny*.
3.  The card type was artifact. It was brown before the *Eighth Edition* card change made it silver (to differentiate it more from the land frame).
4.  The card moves an artifact from the graveyard to your hand.
5.  Junk is the name of the deck.
6.  Divert is the card with that rules text.
7.  The flavor text stayed for *Modern Horizons 3*.

I've always been a fan of artifacts, combo decks, and graveyard interactions, so I designed this card as a combination of all three.

My next card preview makes use of a mechanic that was introduced in *Scourge* that I named a whole scale around.

## Click here to see Amphibian Downpour

 

0051\_MTGMH3\_Main: Amphibian Downpour 0449\_MTGMH3\_ExtRM: Amphibian Downpour 

I like to refer to *Modern Horizons* sets as "decadent designs" as you get to design with almost no filters (save color pie and an appropriate power level for Modern). This card takes the storm mechanic and attaches it to the card Turn to Frog. In what other set could you do that?

## *Modern* Times

That finishes our look back at the major components of *Modern Horizons 3*. As always, I'm eager for any feedback on today's column or *Modern Horizons 3* itself. You can email me or contact me through any of my social media accounts ([X](https://twitter.com/maro254), [*Blogatog*](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)).

Until next time, may your gameplay be as decadent as our designs.
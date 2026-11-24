---
id: v3dga084
kind: article
lang: en
path: /en/articles/makingmagic/2023/08-15-wilds-story-part-1
title: Wilds Story, Part 1
published: '2023-08-15'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/wilds-story-part-1
    lang_detected: en
    capture_id: 234579
    url: https://magic.wizards.com/en/news/making-magic/wilds-story-part-1
    captured_at: '2024-05-18 01:13:36+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/wilds-story-part-1
    lang_detected: en
    capture_id: 234579
    url: https://magic.wizards.com/en/news/making-magic/wilds-story-part-1
    captured_at: '2024-05-18 01:13:36+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/wilds-story-part-1
    lang_detected: en
    capture_id: 234579
    url: https://magic.wizards.com/en/news/making-magic/wilds-story-part-1
    captured_at: '2024-05-18 01:13:36+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/wilds-story-part-1
    lang_detected: en
    capture_id: 234579
    url: https://magic.wizards.com/en/news/making-magic/wilds-story-part-1
    captured_at: '2024-05-18 01:13:36+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: v3dga084
  url: https://magic.wizards.com/en/news/making-magic/wilds-story-part-1
  page_key: magic.wizards.com/en/news/making-magic/wilds-story-part-1
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:13:36+00'
  capture_id: 234579
  wayback_url: https://web.archive.org/web/20240518011336id_/https://magic.wizards.com/en/news/making-magic/wilds-story-part-1
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: v3dga084
  capture_id: 234579
  url: https://magic.wizards.com/en/news/making-magic/wilds-story-part-1
  wayback_url: https://web.archive.org/web/20240518011336id_/https://magic.wizards.com/en/news/making-magic/wilds-story-part-1
  captured_at: '2024-05-18 01:13:36+00'
  template: contentful
  sha256: eec1b9dff0e6c6c888477700cdeea4fdf31fd9ad3f92cf797d284e359f155154
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
Welcome to the first week of [*Wilds of Eldraine*](https://web.archive.org/web/20230815000000/https://magic.wizards.com/products/wilds-of-eldraine) previews. This week, I'm going to introduce the Exploratory and Vision Design teams, walk through the set's exploratory design and vision design, and show off two cool preview cards.

## In the *Wilds*

Before I can tell you the story of the set's early design, I need to first introduce you to the teams that made it. I'll have Lead Vision Designer Chris Mooney introduce their team.

## Meet the *Wilds of Eldraine*  Exploratory and Vision Design teams

 

**Chris Mooney**

Back in 2018, before I started working at Wizards, I flew up to the office to participate in the final round of the *Great Designer Search 3*. Afterward, us three contestants were treated to a special event: we got to draft an early version of *Throne of Eldraine*. We had no idea what to expect going in, and I instantly fell in love with the flavor of the set. (Not only that, but I also won the draft!) Since then, Eldraine has held a special place in my heart. I even got a chance to write the [Planeswalker's Guide to Eldraine](/en/articles/feature/2019/10-31-planeswalkers-guide-to-eldraine) article many months later. It was an honor to lead the Vision Design team for *Wilds of Eldraine*, especially as my first official team lead position.

**Mark Rosewater**

Because *Wilds of Eldraine* was my first time leading a vision design, they wanted to pair me with someone more experienced, and nobody's more experienced in vision design than Mark Rosewater! Mark and I worked together closely on *Unfinity*, where he helped teach me the vision process. Mark's experience and passion for the original set and general love of top-down design made him a great strong second to support me.

**Erik Lauer**

Erik played a large part in the development of the original *Throne of Eldraine*, so I spoke with him many times about the set and was excited to work with him directly. In contrast to Mark, Erik knew almost nothing about fairy tales! It was useful (and often humorous) to hear his perspective as someone with deep knowledge of *Magic* design but not much knowledge of the source material. Erik's experience and intuition helped to guide many mechanics and themes that ended up in the final product.

**Jenna Helland**

Jenna was heavily involved in the original *Throne of Eldraine* on the creative side and was a valuable resource for the first half of our vision process. She had a great read on which parts of *Throne of Eldraine* worked and which we wanted to improve or focus on less.

**Doug Beyer**

As creative director, Doug sits in on many Vision Design teams to guide creative alignment. Doug was an important part of finding the structure of *Wilds of Eldraine*, focusing on and choosing our ten fairy-tale archetypes (which I'm sure Mark will tell you about soon).

**Dan Musser**

Dan was our play design representative on this team. Together with Erik, he helped to make sure our mechanics and themes were viable for Play Design to work with.

**Annie Sardelis**

Annie and I were the most junior team members. Annie excels at brainstorming ideas for mechanics, and on a team with so many tenured designers, she brought a fresh perspective to source material. We worked together on *Unfinity* and again on multiple future projects.

## Eld*rain* e Drops Keep Falling on My Head

When I was working on the original *Innistrad*, I became enamored with working on a top-down set based on genre tropes. After it was over, I started thinking about what other genres we could work with that felt fantasy adjacent. The most obvious one to me was fairy tales. With their need for castles, kingdoms, witches, and magical beasts, they fell squarely in fantasy territory. They also were quite well known. I used the stat that, during their life, the average American sees ten movies that are essentially the story of Cinderella. (I believe this is also true for many non-Americans, but that was the stat I was quoting.) It seemed like a slam dunk, so I was surprised that it was poorly received when first pitched.

There were worries it was "too juvenile," "too soft," or "too off brand." I stressed that the source material was a lot more mature than much of the media inspired by it. If we wanted to go darker or edgier, the source material could handle it. For years, I continued pitching a fairy tale–inspired plane, but never with much success.

Several years later, Shawn Main, probably best known for being runner-up in the second *Great Designer Search*, pitched a plane inspired by Camelot and Arthurian legend. This one got a lot of traction, enough so that we were considering adding it to the upcoming multi-year plan. That's when I saw my opportunity.

I went to Aaron Forsythe, my boss, and said that I didn't think Camelot had enough material to fill up an entire set. I'd done an informal poll where I made a list of many characters, objects, places, and events from Camelot to see how much general recognition they had. My list went about ten items deep before most people stopped recognizing them.

My pitch to Aaron was this: we'd supplement it with fairy tales. The Arthurian legends were, in many ways, English fairy tales. We could match them up with the ones from continental Europe (most of what people know of fairy tales come from Germany, France, and Italy). I thought it would feel cohesive and give us enough source material to work with. Aaron gave me his blessing, and finally, I had a chance to make my fairy-tale set, just mixed with Camelot.

*Throne of Eldraine* ended up having two main components: a structured half that represented the five courts and a more top-down half that allowed you to mix and match fairy-tale tropes. As expected, the Camelot portion of the set served as the meat and potatoes of the set but didn't provide as much excitement as the fairy-tale portion. Mostly this was because *Magic* has done many sets that incorporated high-fantasy kingdoms filled with knights (*Alpha* had White Knight and Black Knight, for example). It just wasn't novel. In contrast, other than a little in *Lorwyn*, we hadn't touched upon fairy-tale tropes, so they seemed much newer. I communicated this to the Marketing team, who'd go on to lean into highlighting the fairy-tale aspect of the set. The trailer, for example, featured two gingerbread creatures.

*Throne of Eldraine* came out and was a massive success. As predicted, the fairy-tale portion was what captured the lion's share of the attention. I had high hopes that we'd get a chance to return one day.

A few years later, we were planning out the schedule past what we called internally the Parallax Arc, what you all know as the Phyrexian Arc. We needed a plane that could give us a break from a large capstone event set. Last time we needed one, we turned to Eldraine (after *War of the Spark*). Maybe we could do that again. Chris was a huge fan of original *Throne of Eldraine*, and return sets are usually the best venue for someone to lead their first premier set design, so Chris was made the lead vision designer for the set.

## *Wild* est Dreams

The first thing we do when designing a return is list everything from the original set to see what elements we might want to bring back. Here's a list of everything we did in *Throne of Eldraine*:

**Adamant** – This was an ability word that granted a spell or permanent either an additional ability or an enhanced effect if you spent three or more mana of the same color when casting it. The mechanic was tied to the monocolor courts. This mechanic fared the worst of the named mechanics in market testing. We were skeptical it would come back.

**Adventures** – Adventure cards were all creatures that had an instant or sorcery spell attached to them. If you cast the spell first, you could then cast the creature from exile. In contrast to adamant, Adventures got the best scores in market research. Also, while *Throne of Eldraine* only had creatures with Adventure, the mechanic allowed any permanent to have it, something *Commander Legends: Battle for Baldur's Gate* explored. This was the mechanic we were most confident in returning. The big question: did we want to tweak it in any way or just redo what *Throne of Eldraine* had done?

**Artifacts and Enchantments Matter** – This was a smaller theme in the set, rewarding you for controlling both an artifact and an enchantment. This theme didn't get a lot of attention and didn't feel as endemic of Eldraine as other mechanics. We thought we'd flesh out the set and see if artifacts and enchantments naturally showed up in enough volume that this was a theme we wanted to revisit.

**Food Tokens** – These are artifact tokens you can trade in for life. While they are thematically very tied to Eldraine, they did cause some problems in Limited and Constructed formats. Our initial thoughts were to only do Food in small amounts, not large enough to be a draft archetype, but once again, fairy tales do love involving food. This would be apparent when one of our draft archetypes revolved around Hansel and Gretel.

**Knight Typal** – Knights showed up in all five colors but were focused in white, black, and red. We knew the return would have some Arthurian-inspired cards, but probably not at the volume they'd been in the first set. The set would have plenty of Knights, but we didn't think we'd do much Knight typal. As you will see, we chose to lean toward fairy tales for our draft archetypes.

**Non-Human Typal** – We used this in *Throne of Eldraine* to capture most of the fairy-tale creatures. As we were planning to raise the volume of them in this set, we felt non-Human would hit too many creatures.

**Top-Down Designs** – Being a top-down set, there was a lot of focus on hitting known Arthurian and fairy-tale characters, objects, places, and events. These individual designs had gone over very well, so we knew we'd be doing a lot more. We understood the fairy-tale well was much deeper than the Arthurian well.

When the dust settled, we decided we'd use Adventures, Food tokens, top-down Arthurian and fairy-tale designs, and possibly have artifacts and/or enchantments matter in some way.

Here were our thoughts on what to do with each of these:

**Adventures** – We explored a number of tweaks but decided we didn't need to do anything too drastic. When we handed over the file, we had two things. First, we had spells where the Adventure was in another color. These cards would be usable in one color but better in two. Set Design kept some of these in the set. Our second suggestion: Adventures on enchantments. As you will see, the set started pushing toward being more about enchantments, so this seemed like a simple way to expand Adventures. (*Commander Legends: Battle for Baldur's Gate* had expanded to artifacts.)

**Food Tokens** – Vision Design proposed only having a small dose of Food creators. Set Design would add a bunch and make it part of some draft archetypes.

**Top-Down Designs** – We made extensive lists of what *Throne of Eldraine* had not done. We also decided that we'd be willing to redo things we had done if we had an interesting new design.

**Artifacts and Enchantments Matter** – We knew there was potential here, but we weren't quite sure what to do with it. As you will see, it would lead us down the path to two of our new mechanics.

## Running *Wild*

One of the things the Vision Design team enjoyed about *Throne of Eldraine* was the way in which you could mix and match different fairy-tale and Arthurian elements to make up brand-new stories. Sure, Cinderella could crew the Pumpkin Carriage, but could Pinocchio? Was there any new way to play in this space? We tried a few different things, but Roles got the most traction.

The idea of a Role was that a creature could take on a specific title that would tap into a trope from fairy tales. For example, your creature could become a Princess or a Beast. Doing so meant that they gained a certain line of rules text. We explored various ways to do this. Maybe it'd be a label, a counter, or an emblem. In the end, the idea we liked best was that Roles were Aura tokens.

We make creature tokens every set and have started making a lot more artifact tokens. We've even made a few enchantment tokens, but far less frequently. Auras did a great job of capturing the feel and mechanical execution we liked. Enchantments have answers and can synergize with other cards. At the handoff, we had ten Roles: Princess, Young Hero, Beast, Wicked, Frog, Animated, Knight, Faerie, Wizard, and Woodsman.

Set Design would whittle the list from ten to six (seven if you count the Virtuous Role token from *Wilds of Eldraine* Commander). The names of four of the six would change. Princess became Royal, Beast became Monster, Frog became Cursed, Wizard became Sorcerer, and Young Hero and Wicked kept their names. I'll talk a little more next week about how Roles were adapted in set design. Here's the final list: Royal, Young Hero, Monster, Sorcerer, Wicked, and Cursed.

Besides adding a lot of flavor, Roles allowed us to interact with Auras and enchantments in ways we hadn't before. Normally, it's hard to do small Aura effects because they're not worth a card, but because Roles could be a by-product of other cards, it allowed us freedom to make them. This allowed us to care about enchantments in various ways, including counting and sacrificing them.

Roles would lead us to make two mechanics, one a keyword and the other an ability word. The keyword we called bargain allows you to sacrifice an artifact, enchantment, or token to boost a spell. I think the mechanic started with Auras but extended to enchantments, then added later to artifacts. Finally, tokens were added, so you could sacrifice token creatures, a feature important for the black-red Rat archetype.

The ability word is celebration. In the handoff, it was just a theme that ran through a number of cards, but Set Design would decide to give it a name. Celebration gives you a reward if two or more nonland permanents entered the battlefield this turn. Cards generating Roles allowed you to meet this requirement with a single card.

## *Wild* at Heart

Chris pitched the last big element of the design early in vision design. What if we built our ten two-color draft archetypes around popular fairy tales? As I said above, the ability to mix and match fairy-tale elements had been a popular theme in *Throne of Eldraine*, so we wanted to double down on it. Building each draft archetype around a story allowed us to give the set a unique feel that played into our key theme. Note that we were using the story as a jumping-off point and were doing our twist on it rather than just straight up repeating the story.

Here are the ten we chose when we handed off the set from design, all of which made it to print:

**White-Blue: The Snow Queen**

This story obviously dealt with cold and ice, so blue seemed like a shoo-in. White seemed like the best color pair, as the effects white gave us worked best with the type of effects we wanted for the story.

**Blue-Black: Sleeping Beauty**

This story had to involve sleeping, which we've traditionally done in blue. It has a dark edge to it, so that made black feel like a good color to pair it with.

**Black-Red: Pied Piper**

Rats are black, and the Pied Piper controlling people with music felt blue or red. We already had a blue-black story we liked, and the archetype wanted to make a lot of Rat tokens, which felt more red than blue.

**Red-Green: Little Red Riding Hood**

The wolf, the huntsman, and the forest setting all felt very green. The second color wanted to be either black or red, and we liked black-green more for Hansel and Gretel.

**Green-White: Beauty and the Beast**

This was the color pair we had the hardest time with. It went through several changes, but we liked how green and white captured the wild and controlled elements of the story.

**White-Black: Snow White**

We knew we wanted our version of Snow White and the Evil Queen, so that put us squarely in white-black.

**Blue-Red: The Sorcerer's Apprentice**

This was another hard color pair to find the right story for. Blue-red wanted to deal with spells, so we had to find a story where magic went awry, and the Sorcerer's Apprentice was the best fit.

**Black-Green: Hansel and Gretel**

The hungry kids and forest setting felt green. The witch felt black. This was one of the first stories we settled on.

**Red-White: Cinderella**

We knew we wanted to do Cinderella, and it got moved all over. I think we ended up in red-white because we felt we could make it work there, and no other story seemed to fit as well.

**Green-Blue: Jack and the Beanstalk**

This is another one we struggled with. Green made perfect sense because of the beanstalk. Stealing everything from the giant felt blue.

Interestingly, all ten stories made it all the way to print. Next week, I'll talk about what went into making each draft archetype.

## *Wild* About You

Before I sign off for today, I want to show you my two preview cards, one of which lets me talk about a final aspect we added to the set during vision design.

## Click here to learn about The Huntsman's Redemption

 

![The Huntsman's Redemption](https://media.wizards.com/2023/woe/en_201093de37.png)

**The Huntsman's Redemption**

When we made *Throne of Eldraine*, we talked about including Sagas. Sagas work best when the audience knows the story, and fairy tales are about as well known as stories get. We ended up not using them because *Theros Beyond Death* wanted them and, at the time, Sagas weren't yet deciduous enough for us to do them in back-to-back sets. This time, we knew we wanted to use them. We explored a bunch of tweaks but decided to keep them simple. Our handoff in vision design suggested we have a ten-card, two-color rare cycle telling the ten stories of our archetypes. Set Design would de-cycle them and make them monocolor.

My second preview card is a bookend to the card I previewed when *Throne of Eldraine* came out, Once Upon a Time.

Once Upon a Time

## Click here to see The End

 

![The End](https://media.wizards.com/2023/woe/en_10b2f8f342.png)

**The End**

![The End (Extended Art)](https://media.wizards.com/2023/woe/en_c1d30a9992.png)

**The End (Extended Art)**

This card blends an effect R&D refers to as a lobotomy effect with a constraint first seen in the mechanic fateful hour in *Dark Ascension*.

## *Wild* Times

Well, that's all the time I have for today. I hope you enjoyed hearing about the vision design of *Wilds of Eldraine*. As always, I'm eager for any feedback on today's column, on any of the mechanics I talked about, or on *Wilds of Eldraine* as a whole. You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next time when I walk through *Wilds of* *Eldraine*'s set design.

Until then, may you have fun mixing and matching.
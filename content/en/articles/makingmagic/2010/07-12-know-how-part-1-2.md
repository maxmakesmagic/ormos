---
id: y3g43hf0
kind: article
lang: en
path: /en/articles/makingmagic/2010/07-12-know-how-part-1-2
title: Know How, Part 1
published: '2010-07-12'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
    lang_detected: en
    capture_id: 222458
    url: https://magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
    captured_at: '2024-05-18 04:03:31+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
    lang_detected: en
    capture_id: 222458
    url: https://magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
    captured_at: '2024-05-18 04:03:31+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
    lang_detected: en
    capture_id: 222458
    url: https://magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
    captured_at: '2024-05-18 04:03:31+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
    lang_detected: en
    capture_id: 222458
    url: https://magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
    captured_at: '2024-05-18 04:03:31+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: y3g43hf0
  url: https://magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
  page_key: magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
  lang: en
  template: contentful
  captured_at: '2024-05-18 04:03:31+00'
  capture_id: 222458
  wayback_url: https://web.archive.org/web/20240518040331id_/https://magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
- document_id: y3g43hf0
  url: https://magic.wizards.com/en/articles/archive/making-magic/know-how-part-1-2010-07-12
  page_key: magic.wizards.com/en/articles/archive/making-magic/know-how-part-1-2010-07-12
  lang: en
  template: drupal
  captured_at: '2022-09-26 03:28:03+00'
  capture_id: 891472
  wayback_url: https://web.archive.org/web/20220926032803id_/https://magic.wizards.com/en/articles/archive/making-magic/know-how-part-1-2010-07-12
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: y3g43hf0
  capture_id: 222458
  url: https://magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
  wayback_url: https://web.archive.org/web/20240518040331id_/https://magic.wizards.com/en/news/making-magic/know-how-part-1-2010-07-12
  captured_at: '2024-05-18 04:03:31+00'
  template: contentful
  sha256: 0f7676b00eff143261fb693f4df8b9436eee400c6d99affe2008747a9da0c886
render_recovery: []
---
It's Living Weapon Week. [Four weeks ago](https://web.archive.org/web/20100712000000/https://magic.wizards.com/en/articles/archive/fight-club-part-1-2011-02-07) we talked about the Mirran mechanic from *Mirrodin Besieged*, battle cry. This week we discuss the Phyrexian one. For my column today I've decided to try something a little different. I've been writing Making **Magic** for over nine years (my five hundredth week happens at the end of the summer). I've written numerous mechanic columns and many mailbag columns, but until today I've never combined them.

![](https://i.ormos.uk/08/b2/08b20f7618f2b801b4d45af77bc9e60edc9ef2204e70b0ed015d4b83c3c26a9f.jpg)  

Here's what's going to happen today. I went on my Twitter feed and had people tweet me questions about the living weapon mechanic. My column today will answer some of your questions about the mechanic. (Note that multiple people asked the majority of the questions, but I've chosen one representative in each case to be the person asking.) I'm very curious to see how this column goes.

All right, on with the questions:

> ![](https://i.ormos.uk/df/75/df7564f32ea890456ce84e41275623f9ff0a9c11d053d4e3e4fedd5000683404.jpg)
> 
> [asmor](http://www.twitter.com/asmor) @maro254 Were germs always 0/0?

I'll start with your question, asmor, as you asked the most popular question.

Let's begin by talking about the tokens being 0/0. When the cards were first created in *Scars of Mirrodin* design (yes, living weapon was created by the *Scars of Mirrodin* design team: Mark Globus, Mark Gottlieb, Nate Heiss, Alexis Janson, Erik Lauer, Matt Place and myself; more on how it got moved in a bit), they created 0/0 creature tokens. The design team really liked the 0/0 tokens because a) they captured the flavor of the weapons being inhabited and coming alive, b) it allowed us to put all the value onto the Equipment, and c) 0/0 felt novel and different.

During devign (the time between the end of design and the beginning of development), Mike Turian, the lead developer of *Scars of Mirrodin*, made a note that he'd like us to try out living weapon with a 1/1 token. His major notes were that his felt 0/0 forced a lot of restrictions (the Equipment, for example, had to all provide toughness) and was unintuitive. What does a 0/0 creature token even mean?

![](https://i.ormos.uk/ed/a7/eda73ddf937eacab8a63a4c41b60ba8d955f3f343cf7be373b412c2757c70851.jpg)  

As we always do during devign, when development brings up an issue, design looks into it. We changed over from 0/0 tokens to 1/1 tokens. As design played with them we found a few problems. First, we were surprised how much of your mana went to paying for the 1/1, both for the fact that you were making a creature viable without the Equipment and for the boost in power. The cards just had to cost more, and they looked worse because of it.

The second big strike against the 1/1 token was that it lost a lot of the feel that the 0/0 tokens had created. Yes, there was some confusion, but it also made the mechanic feel more unique. You weren't just summoning an Equipment along with a guy; you were summoning a living weapon.

We then tried a 0/1 version, figuring it might split the difference. We thought that 0/0 tokens might allow us to avoid having to grant toughness without making us pay for power. This playtest showed off something that R&D has long known about: It is harder to track changes on a creature where the power and toughness are different. It's very easy to just say "whatever," but let me take a moment to explain a very important design concept: stickiness.

The concept of stickiness is defined as such. Some thing are naturally easy to remember or figure out, and some aren't. It has to do with how the brain processes information. For example, people can group numbers in threes and fours, so telephone numbers in America are broken up into three sections: a three-digit number in parentheses (the area code), a three-digit number followed by a hyphen, and then a four-digit number. American Social Security numbers are also broken down into groupings of three and four digits.

Information is sticky or it's not. You cannot train the brain to easily remember things that do not map to the way it thinks (well, at least not easily). I often talk about how game design has to adapt to human behavior rather than fight it. Tracking changes between power and toughness, we've learned, is a stickiness issue. If power and toughness are the same, it's sticky—even, by the way, when the numbers added to power and toughness aren't the same. This is why whenever we have a mechanic that changes power and toughness we tend to keep the creatures N/N as much as we can especially at lower rarities. And when we do altar the power of a creature with a different power and toughness we tend to increase it by the same number. Note that we make exceptions but usually on a case-by-case basis and not when making a decision that affects numerous cards.

![](https://i.ormos.uk/25/12/25122e55ffae71a4c6f8e515b3a3b310a49c61e8fb075f38d37747976bb953bc.jpg)  

The big problem with the 0/1 version was that it wasn't sticky. The way you can tell this, for those that are interested, is when in playtest you find yourself unable to remember something. A good example of something from **Magic**'s past that wasn't sticky was the names from the *Champions of Kamigawa* block. Those playing back then remember how much harder they were to learn than names from other blocks. When playtesting, if you keep having to ask how something is working or what a creature's stats are, it's a good indicator that you're probably dealing with a stickiness issue.

Anyway, we started with 0/0, tried the other options, and ended back where we started.

> ![](https://i.ormos.uk/8e/06/8e06ce8ae3fcd9a6f7dc4c878c76d1931f56c41f698c8117ebf83a09e586ae8b.jpg)
> 
> [coien](http://www.twitter.com/coien) @maro254 why black germs, and does that mean it's never coming back in the future?

Now, the second and third most asked questions: why black and why Germ? In design the creature token was an artifact as we thought it both made the most sense flavorwise and allowed neat interaction with other aspects of the set, metalcraft being the biggest one. (I should point out, though, that living weapon was created during the period where affinity for artifacts was still in the set, before we had ever considered metalcraft.)

While we messed around with the size of the creature token in devign, we never changed its color (or technically lack of color) or its card types (artifact creature). Development, though, had concerns Design didn't. Design, for example, wanted interaction. Development frowns on interaction if it makes some aspect of the game play too strong. Having a single card that produced two artifacts was just too much with metalcraft being set at three artifacts. The development team had two choices: change the artifact creature token, or change metalcraft from three to four. The former seemed like the better move.

Once it was decided it couldn't be an artifact, the development team had to figure out what to make it. The reason it wasn't colorless was that we try to avoid having nonartifact colorless permanents and artifact colorless permanents comingle. That's why, for example, *Rise of Eldrazi* had very few artifacts (only twelve in a large set).

If it couldn't be colorless, then it had to be one of the five colors. Green and black seemed like the likely choices as they were the two colors most affiliated with Phyrexia in *Scars of Mirrodin*. Black had the added bonus that it's the color hardest to kill, as some black creature destruction spells don't work on black creatures. It also fits Phyrexia's traditional association with black.

As to why Germs? That was a decision made by the creative team. If the creature type doesn't have mechanically relevant function, it is the purview of the creative team.

Does the token being a black Germ limit our ability to bring the mechanic back? Maybe a little, but not too much.

> ![](https://i.ormos.uk/38/a7/38a775f1659759cad7296551633fa0666519c01a23e87b8e6d26cf17e7c580ae.jpg)
> 
> [EliShffrn](http://www.twitter.com/EliShffrn) @maro254 Why not Phyrexian Newts?

The creative team's first idea was to call them Newts, as that lines up with the established ecology of the Phyrexians. The problem was that all the players who didn't know that (which I'll guess is over 99.9% of the audience) would read "Newt" as the Earth-based animal, which makes no flavor sense.

> ![](https://i.ormos.uk/2c/ea/2cea9349f64b1eeb375cbe03e7da8c2cca9a724b8fd00cd62150fcb02e3c7d4c.jpg)
> 
> [DemonSmallZ](http://www.twitter.com/DemonSmallZ) @maro254 : Well, why the introduction of a new creature type?

When we first designed living weapon, we gave the tokens the Spirit creature type as we liked the flavor that some essence was inhabiting the weapon. Once creative moved away from that flavor, it seemed best to give a creature token as unique as a 0/0 its own unique creature type.

> ![](https://i.ormos.uk/6d/36/6d3622dd6af3071f0bda5295a8bd05f66eb4b137fa02971fc51d84814128ad3a.jpg)
> 
> [AlexEvangelou](http://www.twitter.com/AlexEvangelou) @maro254 How long has it been thrown around in R&D? Did you consider it for aura's first or possibly before equipment even existed?

The general idea has been around a long time, long before Equipment. In fact, in the very first set I ever designed, *Tempest*, I created cards that can be thought of one of the earliest precursors to living weapon. Interestingly enough, they were my attempts at making something similar to a [Licid](https://web.archive.org/web/20100712000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?type=+%5Blicid%5D%7C%7Csubtype=+%5Blicid%5D).

My series of cards were all auras that could be discarded (along with a mana cost) to create a token creature that incorporated the abilities granted by the aura. For example, I had a [Flight](https://web.archive.org/web/20100712000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flight) (enchanted creature gains flying) for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) that could also make a 1/1 flying creature token. The idea was that if this Aura got stuck in your hand, you still had a way to use it.

My pseudo-Licid, though, is a bit far away from the space mined by living weapon. The earliest version that is a direct descendant was a cycle of Auras that you could pay extra mana to provide a creature token (a 1/1 if I remember correctly) to play it on. I think the first version of this mechanic came up during *Urza's Saga* block. Remember that the Urza block did have a strong enchantment theme.

> ![](https://i.ormos.uk/cf/1a/cf1a745199f852405d57f708e2fa00ed64d533012057c2d2ccc3f92701efe8af.jpg)
> 
> [Verno5x](http://www.twitter.com/Verno5x) @maro254 Why did it take so long to do? It's such a great idea and seems so simple/intuitive to play with.

A lot of people seem to think that an idea being good is what gets it made. That's not quite right, though. What gets an idea made is it being good and us finding the right place to use it. Burning up good ideas in sets that cannot maximize them just wastes a valuable resource. I have plenty of unused ideas that I consider good, but it's important for me to be patient and use them were they are best served. My fifteen-year trek to make poison a major component of a set is the most recent example of this idea at work.

> ![](https://i.ormos.uk/58/fa/58fa5d0134c092c7d84ddf2dbe702d5479c87055b3633c62e7ee058062918cde.jpg)
> 
> [DASeals](http://www.twitter.com/DASeals) @maro254 Also, why equipment instead of Enchantment-Aura, which are having a tougher time finding their place in modern Magic?

As I explained above, we've played around with this idea with Auras. We opted to put it on Equipment rather than Auras as the mechanic just works better on Equipment. On an Aura, the mechanic simply turns an Aura into a creature. On an Equipment, the mechanic allows you to start with a creature but once it dies, the Equipment still gets to get used as Equipment.

<table><tbody><tr><td><div><div><img alt="Bonehoard" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Bonehoard"></div></div></td><td><div><div><img alt="Bear Umbra" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Bear+Umbra"></div></div></td></tr></tbody></table>

Note that when we get a mechanic we stick it where it works best, not where it's needed most. Remember that mechanics are considered tools by design. When we create something, we think long term. We want to build things we'll be able to use again and again. This means we have to make choices with mechanics that optimize their reusability.

> ![](https://i.ormos.uk/ed/bd/edbd1d32ae7d6777aaf4bc85c9fd73dc3ae9e3d71429e56597a62e9990e98f64.jpg)
> 
> [wahonez](http://www.twitter.com/wahonez) @maro254 when can we expect living auras?

Another big change we've made in recent years is not allowing choices in the past to stop choices in the future. If we make some future block where living Auras make sense, it's clearly on the table. True, having done it first as living weapon increases the chance of it coming back on Equipment, but I wouldn't say Auras are automatically eliminated as a future evolution of the living weapon mechanic.

> ![](https://i.ormos.uk/75/f2/75f227caeaff48073f12d8919bb22334b12e69538e383b80b057b2baeb32abb4.jpg)
> 
> [j\_ram\_f](http://www.twitter.com/j_ram_f) @maro254 How much design space is left for living weapon?

There are a lot of living weapon designs that didn't see the light of day. I think the development team was frugal with living weapon because a little bit went a long way. There are only four in the set, not because there couldn't have been more but rather that there didn't have to be more. There's plenty of design space remaining for living weapon.

> ![](https://i.ormos.uk/53/eb/53eb9a25231a809b4c8442f254b4c20a4a8b8484e619b3530eb82eb5acc00ceb.jpg)
> 
> [timpskowski](http://www.twitter.com/timpskowski) @maro254 At any point were there Living Weapons in the file that gave Infect? Is so, what happened to them. If not, why?

Of course there were. Numerous designers made one. It was an obvious choice, especially as we knew living weapon was going to be a Phyrexian thing. Why didn't it end up in *Mirrodin Besieged*? I don't know. I guess that's a question for the set's lead developer, Erik Lauer.

> ![](https://i.ormos.uk/f5/6a/f56abdcb21244842f10bc61daaa0f8da8378e80a1dfd773460f786dfbf2f3110.jpg)
> 
> [EthanFleischer](http://www.twitter.com/EthanFleischer) @maro254 Did you think that Scars block, as a sequel to the first block with Equipment, needed a "twist" on Equipment?

Why yes we did. I talked about how living weapon was designed during *Scars of Mirrodin* design. The reason is that the team was very drawn to the idea of Phyrexia corrupting Mirrodin, and Equipment played such a strong role in the original *Mirrodin* block that it seemed like an easy target.

> ![](https://i.ormos.uk/9a/c3/9ac33fac2689420e7d1096211bb6975c2d74a0601e47a2eae337801e85d4ab41.jpg)
> 
> [MikeXIV](http://www.twitter.com/MikeXIV) @maro254 how did you convince the rest of the team that this was worth the (very high, but mostly intuitive) rules complexity?

Living weapon wasn't actually a hard sell to R&D. There was some debate about the size of the token and discussions about whether or not the token should be an artifact, but no one ever wanted to kill the mechanic. I think the reason is that although it has a lot of moving parts, the basics of it are very intuitive (save the 0/0). The mechanic works the way you think it would. In addition, it has a lot of flavor. All in all, it did a good job of selling itself in the Pit.

> ![](https://i.ormos.uk/13/a5/13a5f61caed30eb230a713c77d388becb5c94b0b9a278a9748089c77836b9229.jpg)
> 
> [gamertheorist](http://www.twitter.com/gamertheorist) @maro254 Why didn't you have Phyrexia corrupt iconic Mirran Equipment? Living Bonesplitter, Phyrexian Warhammer?

We tried hard in *Mirrodin Besieged* (and *Scars* block in general) to keep a tight rein on what I will call the homage cards (the cards that are direct riffs off of *Mirrodin*). We designed a bunch of homage living weapon cards but none of them quite had the impact we wanted so we cut them from the file.

> ![](https://i.ormos.uk/4a/36/4a3664a7eba121db1cdfa550d103b2ff1e245e32505d1c1dd7aa770f30d1de0e.jpg)
> 
> [ThreeLawsSafe](http://www.twitter.com/ThreeLawsSafe) @maro254 Why Phyrexian? The Mirrans seem more inclined to create artifacts that can be both a creature and a weapon.

When you are defining two sides in a conflict you have to make the two sides distinct from one another. Phyrexia was corrupting Mirrodin, so we had a theme of change that ran through the Phyrexian cards. As such, living weapon felt like a change to Equipment and thus fell into the Phyrexian end of the flavor.

![](https://i.ormos.uk/36/94/369425e6e4b2b5e94508625af86e9e83a7074a64b0e8da40dd51bc1f7507e7b8.jpg)  

If we had simply come back to Mirrodin and the Phyrexians weren't involved, I do believe we could have flavored living weapon as an offshoot of Mirrodin's evolution.

> ![](https://i.ormos.uk/93/04/93046576153f3497848f65230c871d4070fe98b2f8b4d7533159367bb8a62f21.jpg)
> 
> [nickhayes](http://www.twitter.com/nickhayes) @maro254 RoE had Totem Armor, and MBS has Living Weapon. Can we expect to see more mechanics that make auras and equipment more competitive?

Of course you can. Auras and Equipment are beloved by the players but have some built-in disadvantages (especially Auras). Design loves to try and create ways to offset disadvantages, so the attraction to make mechanics that help out Auras and Equipment is very high.

> ![](https://i.ormos.uk/4d/47/4d4704a33e1d81925dcc43102c962ae09ac310d3f7b161228b96f0aa6ee7e597.jpg)
> 
> [chjacobsen\_se](http://www.twitter.com/chjacobsen_se) @maro254 Is it the type of mechanic you consider a regular, or is it more likely to be a block-specific creation?

Living weapon is not an evergreen mechanic, a mechanic that design is free to use in any set. It's fun and flavorful, but it's also complicated and narrow. I definitely see it coming back some day, but it just isn't the kind of thing we want to have around all the time.

> ![](https://i.ormos.uk/7e/43/7e4326081c0ab16d4ea4700f07c014ba3f90efedd2804e31d394e49c4e266133.jpg)
> 
> [RegentCid33](http://www.twitter.com/RegentCid33) @maro254 Is this a mechanic you see showing up in future sets, or only relegated to Phyrexia?

I don't feel like living weapon is going to be forever linked with Phyrexia. I'm pretty sure the next time you see living weapon it will be in a non-Phyrexian context.

> ![](https://i.ormos.uk/86/b5/86b5b6b03e68764820a802473a6b7e688fef2eb489d14f44692d456d3886ceea.jpg)[hoopst](http://www.twitter.com/hoopst) @maro254 were u surprised that a lot of the GDS2 candidates had similar ideas for Living Weapon?

This is something we've been messing around with forever in design so it didn't surprise me to see so many Great Designer Search 2 candidates exploring this area. What did surprise me was how close Top 8 finalist Jonathan Woodward got with his mechanic incarnate. It was exactly living weapon (complete with 0/0 token), except on Auras instead of Equipment.

Remember that *Mirrodin Besieged* had already been printed by the time I saw Jonathan's first incarnate card. The first time I read it, I remember yelling out to the Pit, "Someone just made living weapon!" That, by the way, was not the first GDS2 submitted mechanic similar to something already in the pipeline.

> ![](https://i.ormos.uk/f5/f8/f5f87761e585c5b81a95baa98cba709e2a111a0124e1b05ca27faccc0f3f343e.jpg)
> 
> [KwagaToan](http://www.twitter.com/KwagaToan) @maro254 was any thought given to making a germ "lord" when living weapon was made?

We talked about it. The idea of 0/0 creature tokens definitely pulled focus, making us think a lot about them in design. One of the ideas floated was a card that gave all Germs +0/+1 so that they'd survive having the Equipment moved off of them. I also designed a card that made 0/0 creature tokens which immediately attached an Equipment on the battlefield to itself. In the end, with only four cards making Germ creature tokens, it didn't feel worth it.

### It's a Living Weapon

That's all I got for today. I hope today's column has answered some of the questions all of you had about living weapon. I had a blast answering your many questions.

I'm curious how all of you found the mailbag format for a mechanics article. Is this something you'd want to see again? Let me know by email, on Twitter (@[maro254](http://twitter.com/#!/maro254)), or using the Discuss link below.

Join me next week when I hang with the Conners.

Until then, may all your questions find answers.
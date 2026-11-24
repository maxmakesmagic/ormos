---
id: pyqyy4c3
kind: article
lang: en
path: /en/articles/makingmagic/2020/04-20-ikoria-of-the-beholder-part-1
title: Ikoria of the Beholder, Part 1
published: '2020-04-20'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
    lang_detected: en
    capture_id: 221078
    url: https://magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
    captured_at: '2024-05-18 02:21:49+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
    lang_detected: en
    capture_id: 221078
    url: https://magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
    captured_at: '2024-05-18 02:21:49+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
    lang_detected: en
    capture_id: 221078
    url: https://magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
    captured_at: '2024-05-18 02:21:49+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
    lang_detected: en
    capture_id: 221078
    url: https://magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
    captured_at: '2024-05-18 02:21:49+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: pyqyy4c3
  url: https://magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
  page_key: magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
  lang: en
  template: contentful
  captured_at: '2024-05-18 02:21:49+00'
  capture_id: 221078
  wayback_url: https://web.archive.org/web/20240518022149id_/https://magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
- document_id: pyqyy4c3
  url: https://magic.wizards.com/en/articles/archive/making-magic/ikoria-beholder-part-1-2020-04-20
  page_key: magic.wizards.com/en/articles/archive/making-magic/ikoria-beholder-part-1-2020-04-20
  lang: en
  template: drupal
  captured_at: '2022-05-25 04:57:35+00'
  capture_id: 890052
  wayback_url: https://web.archive.org/web/20220525045735id_/https://magic.wizards.com/en/articles/archive/making-magic/ikoria-beholder-part-1-2020-04-20
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: pyqyy4c3
  capture_id: 221078
  url: https://magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
  wayback_url: https://web.archive.org/web/20240518022149id_/https://magic.wizards.com/en/news/making-magic/ikoria-beholder-part-1-2020-04-20
  captured_at: '2024-05-18 02:21:49+00'
  template: contentful
  sha256: 8cfb53b8b56b02c2bfde9e40fb11c41e9caaf203953c205b929e1f984e7f2dee
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email me
  occurrences: 1
---
During the last two weeks, I talked about how *Ikoria: Lair of Behemoths* got created ([Part 1](/en/articles/makingmagic/2020/04-06-more-than-meets-the-ikoria) and [Part 2](https://web.archive.org/web/20211206183550/https://magic.wizards.com/en/articles/archive/making-magic/twinkle-someones-ikoria-2020-04-20)). Today and next week, I'm going to dive into some stories about how individual cards, cycles, or themes got designed.

**Colossification**

![Colossification](https://media.wizards.com/2020/iko/en_3aCQMoMLO7.png)

This card started off innocently enough. We wanted an aura that made something feel monstrous. We began by thinking of a reprint of [Mythic Proportions](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mythic+Proportions) (+8/+8 and trample) from *Onslaught*, but that didn't seem like enough. We'd already printed [Eldrazi Conscription](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eldrazi+Conscription) from *Rise of the Eldrazi* which was +10/+10. We had to do better than that. How about +12/+12? Still felt too close. How about +15/+15? Maybe. Then someone suggested +20/+20. Could we do that? Is that going to cause any problems? We talked to Play Design. As long as it didn't have trample, they thought it was probably okay. After some playtesting, we had it tap the creature when it entered the battlefield to give the opponent a turn to try and find an answer for your now "probably big enough to kill them if it hit them" creature. With the one tweak, this ended up being a "brain to print" card.

**Crystalline Giant**

![Crystalline Giant](https://media.wizards.com/2020/iko/en_uR9RL2zGb5.png)

A lot of our design with keyword counters was figuring out the most basic ways to execute on them. We liked how intuitive they were (a flying counter grants flying), so we were eager to find as many clean and simple executions as we could. That said, a *Magic* designer's mind will wander, and you'll start thinking about more advanced things you can do with keyword counters. What's a complex design that could only exist with keyword counters as a tool?

Crystalline Giant was one such design. Normally, permanently granting abilities is tricky because there's memory issues. Keyword counters offset that. Okay, so if you can permanently grant abilities, what's the next level? How about granting them randomly? Wouldn't it be cool to have a creature that evolves differently every time you cast it? We put together every kind of keyword counter we had (in the main set—the Commander decks introduce double strike and indestructible counters) as well as +1/+1 counters and then limited the random selection to counters that haven't yet been chosen. What we ended up with is a very cool design that couldn't exist anywhere but in *Ikoria*. The fact that it plays into the larger mutation theme (creatively, that is) was just icing on the cake.

**Gyruda, Doom of Depths; Obosh, the Preypiercer; Extinction Event; and Lavabrink Venturer**

![Gyruda, Doom of Depths](https://media.wizards.com/2020/iko/en_YNq9oMPbex.png)![Obosh, the Preypiercer](https://media.wizards.com/2020/iko/en_REQdj6yW4b.png)

![Extinction Event](https://media.wizards.com/2020/iko/en_VSc3WC5pbS.png)![Lavabrink Venturer](https://media.wizards.com/2020/iko/en_U4PLhEtA8A.png)

*Magic* has over 20,000 unique cards in existence, yet very few make reference to things being even or odd. Before *Ikoria*, there have only been three black-bordered cards and four silver-bordered cards that cared.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Chaos+Lord)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chaos+Lord)

The first card that cared showed up in *Ice Age* all the way back in 1994. The designers were trying to make a creature that embodied the feeling of chaos. To do this, they designed a creature that changed control under a weird circumstance. The weird circumstance was there being an even number of permanents on the battlefield. As each player has the ability to add or subtract permanents, it was something they had some control over, but not complete control. I also believe that "evenness" felt like a strange thing to track, so it added to the novelty of the design.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ashling%27s+Prerogative)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashling%27s+Prerogative)

The next card that cared didn't show up until thirteen years later in 2007 in the set *Lorwyn*. Again, it was a red card that was trying to create a sense of chaos. Ashling was an [Elemental Shaman](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elemental+Shaman), and the card was trying to communicate Ashling's quirky nature. For the first time, you got to choose which quality you cared about, and it applied to the converted mana costs (CMCs) of your creatures. Creatures matching that quality got haste, and the ones that didn't entered the battlefield tapped (the two abilities were meant to be opposites, as one was fast and one was slow). This was the first card to encourage you to build a deck of all even or all odd converted mana cost creatures.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Void+Winnower)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Void+Winnower)

The next card took another eight years to see print in the set *Battle for Zendikar*. The set was all about the Eldrazi, and we were trying to find designs that helped them feel alien. We liked the idea that they cared about things that normal creatures didn't care about. [Void Winnower](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Void+Winnower) was designed as a card that hosed what felt like a strange quality, the converted mana cost's evenness or oddness. Unlike [Ashling's Prerogative](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashling%27s+Prerogative), which only cared about your cards, [Void Winnower](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Void+Winnower) only affected your opponent's cards. We chose to hose even converted mana costs because we liked that Eldrazi cared about "odd" things.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=439625)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=439625)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=439627)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=439627)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Oddly+Uneven)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oddly+Uneven)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=439638)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=439638)

*Unstable* latched onto evenness and oddness by making four cards that cared. First was two different versions of [Knight of the Kitchen Sink](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Knight+of+the+Kitchen+Sink). Every version had a unique protection. Two of them had protection from collector numbers, one evens and one odds. [Oddly Uneven](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oddly+Uneven) was a [Wrath of God](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) variant that let you choose even or odd as it applied to the number of words in the cards' names. [Ineffable Blessing](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ineffable+Blessing) was another card that let you choose even or odd (each version of [Ineffable Blessing](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ineffable+Blessing) let you make a different modular choice), also caring about collector numbers.

Which brings us to *Ikoria*. The first two cards designed that cared about evens and odds was the two companion creatures. We were looking for qualities you could build a deck around that was easy for the opponent to monitor. The easiest grouping were things where every card shared some quality. That way, if a card without the quality showed up, the opponent would realize you didn't follow the guidelines. We came up with even and odd converted mana costs pretty early. Their designs were straightforward. It itself had to be of the correct even or odd number, and it had to have an effect that rewarded that quality.

Gyruda, being blue-black hybrid, played into self-milling space followed up by a reanimation of milled even CMC creatures. Reanimating milled cards is new design space, so we decided to put it into the two milling colors. (Blue-black is already the two-color combination with the least amount of mechanical overlap.) Obosh, being in black-red, the two colors that mess around with damage most, doubled damage of odd CMC creatures. Gyruda was given an even CMC while Obosh was given an odd one. Note that the power and toughness of each were also even and odd, accordingly. (Interestingly, Gyruda has an odd collector number and Obosh an even one—a nod to collector numbers being rebels.)

The other two designs happened in set design. My guess is the companion creatures just put evenness and oddness into the designers' psyches. Interestingly, the two designs mirror *Unstable* cards, granting protection and creature sweeping but caring about the thing black border can care about: CMC. In both cases, the designs let the players care about which quality they want, allowing the player to build around it.

**Flame Spill and Ram Through**

![Flame Spill](https://media.wizards.com/2020/iko/en_LVNm8tbOqv.png)![Ram Through](https://media.wizards.com/2020/iko/en_jlncXYvhO4.png)

Back in *Odyssey*, I designed a direct-damage spell that dealt 5 damage but had trample (much like a creature with trample will deal its excess damage to the creature's controller, so too would the direct-damage spell). Here's what it ended up being printed as:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Liquid+Fire)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liquid+Fire)

Over the years, I tried other versions of trample direct-damage spells, but like [Liquid Fire](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Liquid+Fire), they ended up a bit messier than what I was hoping for. Eventually, I gave up and printed this card in *Unstable*:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=439486)](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=439486)

It appears though I gave up prematurely. Dave Humpherys, the set's lead set designer, found a way to print [Super-Duper Death Ray](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Super-Duper+Death+Ray) in *Ikoria*. Okay, technically it doesn't have trample, but it's functionally identical, and with only three lines of text. ([Super-Duper Death Ray](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Super-Duper+Death+Ray) had three lines of text.) But Dave didn't stop there. He even made a bite spell (like fight but just one-way) with the "trample" text as well.

Maybe I need to get some tips from Dave.

**Frondland Felidar, Keensight Mentor, and Solid Footing**

![Frondland Felidar](https://media.wizards.com/2020/iko/en_3w1jiwiA6X.png)![Keensight Mentor](https://media.wizards.com/2020/iko/en_flzcCzPcE7.png)![Solid Footing](https://media.wizards.com/2020/iko/en_NvztrLJb3t.png)

One of the most common requests I get is for an ability that I'll call "keywords matter." That is, cards that mechanically care about creatures that have a certain evergreen keyword. The answer I always give is that there usually isn't enough density with any evergreen keyword, save flying, to exist in a high enough as-fan to matter. (As-fan is short for "as-fanned" and talks about how much of something shows up in an average booster. It's an R&D term that talks about density of an item in a set.) *Ikoria* changes up the math in two ways. One, because of mutate, we just made more creatures that have the evergreen keywords. Two, because of keyword counters, we have the ability to grant keywords in a permanent way at a much higher percentage (most sets can only so it with auras or equipment). What these two things mean is that we finally have enough density to actually do it.

For example, the three cards I show above all care about vigilance. Frondland Felidar grants an additional ability to every creature with vigilance. Keensight Mentor puts +1/+1 counters on creatures with vigilance. Solid Footing has an extra effect if the creature it enchants has vigilance. So, for all of you out there who have been bugging me for years to do this, I'm happy to say we finally found a set where it worked out. Enjoy!

**Helica Glider**

![Helica Glider](https://media.wizards.com/2020/iko/en_T53em8nJnz.png)

Let's start with a trivia question. How many creatures are there in the history of *Magic* with creature type Squirrel? Before *Ikoria*, the answer to that question was seven, five of which are silver-bordered and have been printed within the last three years. The remaining two are from *Odyssey* way back in 2001. In fact, the last Standard-legal set to even make Squirrel creature tokens was *Torment* (the second set in the *Odyssey* block). Helica Glider is the first Squirrel in a Standard-legal set in nineteen years. How exactly did that happen?

I blame myself. You see, I'm a huge fan of Squirrels. I'm responsible for the design of most of the Squirrel cards in *Magic*. ([Here's an article from Squirrel Week that I wrote in 2002](/en/articles/makingmagic/2002/07-22-squirrel-of-my-dreams).) Way back in *Urza's Legacy*, I made a card called [Deranged Hermit](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deranged+Hermit). It was good. In fact, it helped Aaron Forsythe make it onto the US Nationals team where he and his teammates won the World Team Championship. It unfortunately put a spotlight on the card which the brand team at the time didn't like, as they felt Squirrels were a bit too silly for *Magic*.

A year later, I was put in charge of the names, flavor text, and creature types of *Odyssey*, as well as the set's design, where I made Squirrel the default 1/1 green creature token. That pushed it over the edge, and the brand team asked us to remove Squirrels from *Magic*. They were officially banned. I did what I could to keep the spirit of Squirrels alive. I stuck them into every silver-bordered set I made, but my real hope was to find a way to get them back to black-bordered *Magic*.

Over the years, I found like-minded individuals in R&D. My biggest ally was Mark Purvis (yes, of the Council of Marks that helped make *Unstable* a reality). We were determined to turn the tide of Squirrel opinion in R&D. Little by little, the Squirrel haters left and the Squirrel fans grew in number. We managed to get Squirrel cards in supplemental sets ([Acorn Catapult](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Acorn+Catapult) in *Commander 2011* and [Deep Forest Hermit](https://web.archive.org/web/20200420000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deep+Forest+Hermit) in *Modern Horizons*). *Ikoria* was the set where all our hard work finally paid off. Yes, it's just a common, little 2/2 creature, but once you've breached the barrier, it means more will be able to follow. Rejoice Squirrel lovers. We've been held down for many years, but Squirrels are back in Standard-legal sets!

**Huntmaster Liger, Archipelagore, Insatiable Hemophage, Porcuparrot, and Auspicious Starrix**

![Huntmaster Liger](https://media.wizards.com/2020/iko/en_keaQ2hXONE.png)![Archipelagore](https://media.wizards.com/2020/iko/en_Mvy2W929V6.png)![Insatiable Hemophage](https://media.wizards.com/2020/iko/en_bpRQNRpOOr.png)

![Porcuparrot](https://media.wizards.com/2020/iko/en_ELQgsqxCGI.png)![Auspicious Starrix](https://media.wizards.com/2020/iko/en_fYyvD9RuIC.png)

The goal of the mutate mechanic was to encourage players to make their own monsters. The problem we ran into was a problem we have whenever we make cards that go onto other cards—card disadvantage. For instance, if I play an aura onto a creature, you have the ability to destroy both my creature and my aura by destroying my creature because when my creature goes away, so too does my aura. This is an ongoing problem in *Magic* design, as building things up is a lot of fun, but we don't want to lead players down a path where the fun is bad strategic play. We don't want you losing the game because you chose to do the fun thing. That means we always have to be vigilant to make sure that doing what's fun is also the right way to play.

There are two major ways we did this with mutate. First, we made it such that if the creature you're mutating is destroyed in response to your mutating it, that the creature with mutate will still enter the battlefield as a creature. With an aura, the aura would also go to the graveyard as it no longer has a target, but mutate creatures can exist without a creature to mutate. (In fact, you can just cast a mutate creature without mutating it.) Second, the vast majority of the mutate cards have a trigger when you mutate it. This guarantees that you get some value out of the card even if your opponent destroys it two seconds later.

The above cycle was not only designed to encourage you to mutate a creature once but to continue to mutate the same creature. Why? Because constantly mutating the same creature is a lot of fun. The way this cycle accomplishes this is by making mutate effects that scale based on how many times the creature has been mutated. This makes the effect get larger and larger as you mutate the same creature more and more times. Remember, you get every mutate trigger from a creature in your mutate stack, not just when it is first mutating.

The trick with this design was to find scaling effects with enough payoff to encourage players to do what the designers knew players wanted to do, continually mutate. For white, we did team pump, as that's something that scales well. For blue, we chose to scale how many creatures you get to freeze. For black, we have you drain the opponent. For red, we chose direct damage to any target. For green, you get to get permanents from off the top of your library onto the battlefield. Each of these effects helps encourage aggression, allowing you to use the creature you just mutated yet again. This cycle was first made in vision design, but the scaling effects were changed in set design.

**Kaheera, the Orphanguard**

![Kaheera, the Orphanguard](https://media.wizards.com/2020/iko/en_T3fi5CsPjs.png)

One of the roles of the Vision Design team is to work with the Creative team to make sure that the world building matches the needs of the design. As I explained in my preview article, in vision design, the set had a strong tribal component, as mutate cared about creature type as one of the two restrictions for mutations (with keywords being the other). As part of that, we established a tribe for each color to be the backbone of that creature's monsters. Then when you started seeing colors come together, you would see the intersection of those colors' creature types. While mutate changed, each color having a creature type stuck around. I thought I'd take a little time to talk about how we chose each of the creatures.

The goal of the creature types was as follows:

1.  It had to be a creature that felt natural in that color. That meant it needed some backwards compatibility, meaning we wanted there to be enough creatures of that creature already in the color to mechanically interact with.
2.  It had to be a creature that had enough visual flexibility that the artists could draw a lot of different creatures. A Wolf would be tricky, for example, because how many different wolves can you draw.
3.  It had to make sense in the context of a monster world.

Some of the creatures came very naturally. White being Cat and red being Dinosaur were in the very first pitch of the creature types from the Creative team. It helped that Cat and Dinosaur were both broad terms for a whole bunch of different kinds of animals. Elemental came next. The idea that they could be many different shapes using numerous elements helped give it some extra visual growth. Beast had the variety. We were worried it was a little too unfocused but decided that was less important than the other criteria. Black was the sticking point. At one point, the Vision Design team was pushing for Insect, but the Creative team felt it wasn't "cuddly" enough. We wanted monsters that looked scary, but also kind of lovable, and insects creep a lot of people out. We talked about black making up a new creature type, but then it lacked any backwards compatibility. In the end, we went with Nightmare, which was a little vague, but allowed us to give it a unique visual identity.

Kaheera, I believe, is the only card that remains that mechanically cares about these tribes. If you were puzzled why these five tribes are listed on the card, that's why.

# Seeing Eye to *Ikoria*

That's all the time I have for today. As always, I'm interested to hear your feedback on today's column, any of the cards I talked about, or *Ikoria* in general. You can email me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).

Join me next week for part two of my card-by-card design stories from *Ikoria*.

Until then, may you make a lot of monsters.

 

##### #731: Aaron Forsythe

##### #731: Aaron Forsythe

30:23

In this podcast, I'm interviewing my boss and longtime *Magic* collaborator, Aaron Forsythe.

[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork731_aaronforsythe_Jsn28yg6.mp3)

  

 

##### #732: Annie Sardelis

##### #732: Annie Sardelis

30:19

In this podcast, I'm interviewing Annie Sardelis, one of the members of the Creative team.

[Download MP3 Format](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork732_anniesardelis_akU32Hsd.mp3)

*   [**Episode 730**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork730_michaelryanp2_Hujs77yY.mp3) Michael Ryan, Part 2
*   [**Episode 729**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork729_michaelryanp1_82Hyeh76.mp3) Michael Ryan, Part 1
*   [**Episode 728**](http://dts.podtrac.com/redirect.mp3/media.wizards.com/2020/podcasts/magic/drivetowork728_thbpart5_jdj7Y29I.mp3) *Theros Beyond Death* Cards, Part 5
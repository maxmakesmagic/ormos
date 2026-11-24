---
id: ggkw9b12
kind: article
lang: en
path: /en/articles/makingmagic/2012/10-01-designing-for-selesnya
title: Designing for Selesnya
published: '2012-10-01'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
    lang_detected: en
    capture_id: 214825
    url: https://magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
    captured_at: '2024-05-18 03:50:34+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
    lang_detected: en
    capture_id: 214825
    url: https://magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
    captured_at: '2024-05-18 03:50:34+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
    lang_detected: en
    capture_id: 214825
    url: https://magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
    captured_at: '2024-05-18 03:50:34+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
    lang_detected: en
    capture_id: 214825
    url: https://magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
    captured_at: '2024-05-18 03:50:34+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: ggkw9b12
  url: https://magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
  page_key: magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:50:34+00'
  capture_id: 214825
  wayback_url: https://web.archive.org/web/20240518035034id_/https://magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
- document_id: ggkw9b12
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/215
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/215
  lang: en
  template: aspx
  captured_at: '2013-06-28 23:22:43+00'
  capture_id: 649914
  wayback_url: https://web.archive.org/web/20130628232243id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/215
- document_id: ggkw9b12
  url: https://magic.wizards.com/en/articles/archive/making-magic/designing-selesnya-2012-09-28
  page_key: magic.wizards.com/en/articles/archive/making-magic/designing-selesnya-2012-09-28
  lang: en
  template: drupal
  captured_at: '2017-11-23 09:28:22+00'
  capture_id: 875575
  wayback_url: https://web.archive.org/web/20171123092822id_/https://magic.wizards.com/en/articles/archive/making-magic/designing-selesnya-2012-09-28
- document_id: ggkw9b12
  url: https://magic.wizards.com/en/articles/archive/making-magic/designing-selesnya-2012-10-01
  page_key: magic.wizards.com/en/articles/archive/making-magic/designing-selesnya-2012-10-01
  lang: en
  template: drupal
  captured_at: '2022-10-01 06:18:25+00'
  capture_id: 875624
  wayback_url: https://web.archive.org/web/20221001061825id_/https://magic.wizards.com/en/articles/archive/making-magic/designing-selesnya-2012-10-01
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ggkw9b12
  capture_id: 214825
  url: https://magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
  wayback_url: https://web.archive.org/web/20240518035034id_/https://magic.wizards.com/en/news/making-magic/designing-selesnya-2012-10-01
  captured_at: '2024-05-18 03:50:34+00'
  template: contentful
  sha256: 7d9a938d787696cfb84f4d2e6953f110483ffd87005bf5be3c0aaf2150298a28
render_recovery: []
---
Welcome to Selesnya Week. For those keeping count, this is actually the second Selesnya Week. During the original *Ravnica* block, we had ten guild theme weeks and for *Return to Ravnica* block, we're doing it again. It's always a challenge to revisit theme weeks, because I already wrote the first article that came to my mind the last time we had the theme week. But I'm always up for a challenge. You can see all ten guild weeks along with my articles on color philosophy [here](https://web.archive.org/web/20121001000000/http://archive.wizards.com/Magic/Magazine/Features.aspx?tag=Color%20Pie). (My guild theme week articles were about the color philosophy of the two colors in question, along with the philosophy of the guild itself.)

As I spent the last batch of guild theme weeks talking about color philosophy, I thought I would spend the theme weeks this time talking about guild design. Today, for example, I am going to talk about how to design for green-white in the abstract and Selesnya in particular. I'll also look at the two guild mechanics (from original *Ravnica* block and *Return to Ravnica* block) to go a little more in depth as to how they were designed and what needs the mechanics had. Hopefully, that sounds like fun.

To keep things orderly (I will be doing this for ten weeks, after all), I thought I would structure these columns by asking the same sets of questions for each guild/color pairing.

![](https://i.ormos.uk/cc/2f/cc2f5285d37d42a1ae9e75c7adff3797164f3d4579b12a49bfd4bf7cc58eb00a.jpg)

[Selesnya Guildgate](https://web.archive.org/web/20121001000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Selesnya+Guildgate) | Art by [Howard Lyon](https://web.archive.org/web/20121001000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Howard%20Lyon%22%5D)

### What's the Easiest Thing About This Color Pairing?

For green-white, the answer is that the colors blend together easily. Of all the colors in the game, the green-white color pairing is the closest. Green and white, for example, are the two most creature-centric colors. This means they are #1 and #2 (white, then green) as far as who gets the most creatures. The two share lifegain, creature boosting, enchantment (and, to a lesser extent for white, artifact) removal, vigilance, damage prevention (with green's being [Fog](https://web.archive.org/web/20121001000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog) effects), adding +1/+1 counters, untapping creatures, and other small effects.

Green and white are not only the closest colors mechanically but also philosophically. Selesnya, for example, plays into the fact that these two colors are the colors of community. They both like to form large bands of creatures and overrun their enemies. Yes, white is more the army color, hitting fast with small creatures working together, while green ramps up its mana to get a horde of larger creatures onto the battlefield, but the two have a similar feel.

Also, in future weeks I'll talk about how certain color pairings are close in one area but distant in another. Green and white, in contrast, are similar to one another through almost every card type.

### What's the Hardest Thing About This Color Pairing?

One of my favorite sayings is "Your greatest weakness is just your greatest strength pushed too far." This similarity between green and white is good in finding synergies but also causes problems because it's harder to find multicolor cards that truly feel like they are green *and* white, rather than being green *or* white. In other words, green-white is the king of hybrid design where you're looking for overlap, but is problematic when you want strong definition to mix and match.

R&D has spent a lot of time making fine-tuned adjustments between what green gets and what white gets. As an example, white gets lesser creature boosts (+2/+2 and smaller), while green gets greater creature boosts (+3/+3 and larger). The fact that we've spent so much time splitting hairs between the colors means it's harder for each color to have clear color identity. For example, you can't make the white part of a green-white card grant a +2/+2 boost, because even though it's technically white it feels too close to green.

![](https://i.ormos.uk/9b/12/9b1224289dd0c14203fbae2111d515342ffc1efbae6474980bac27463949e8db.jpg)

[Vitu-Ghazi Guildmage](https://web.archive.org/web/20121001000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vitu-Ghazi+Guildmage) | Art by [Jason Chan](https://web.archive.org/web/20121001000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Jason%20Chan%22%5D)

### What's the Mechanical Heart of This Color Pair?

To answer this question, I must first define my terms. A mechanical heart is at the center of a design. It's the thing that defines what must be built around. For example, the mechanical heart of the original *Ravnica* design was the guilds. At every point, we used the emphasis on the guilds to create the framework for the design. It led to how the colors were used. It led to how the keywords were defined. It led to all the key decisions of the design.

Now, when I talk about the mechanical design of a color pair, I'm referring to what is the one mechanical element that most defines the interrelation between the two colors. For green and white, this is creatures. Both colors are focused on creatures and both colors define much of their philosophy and mechanics around supporting creatures.

If creatures are the mechanical heart, that means that the definition of green-white (and extra so in Selesnya) has to be found in the creatures. In other words, the guild keyword, which is going to be the strongest marker for the guild's mechanical feel, has to be on and about creatures.

### What's the Focus of This Color Pair?

The mechanical heart is about which part of the design has to be the build-around component. For green-white, that's creatures. The focus is more about what the color combination wants to do to win. Okay, green-white is focused on creatures. Wonderful. Now how is it going to use its creatures to win?

The answer was hinted at above. Green and white are both about overwhelming the opponent with creatures. White does it quicker than green, but both have a similar play style. This means the focus of green-white is a creature-based attack strategy that relies on having a number of creatures. The focus is another thing that has to play into the guild keyword. If green-white is about attacking with creatures, then its guild mechanic has to help in that goal.

### Convoke

![](https://i.ormos.uk/f6/2a/f62a31fbb7f7b87ef45b01ca64d709e2c4cae194f9e3eedc910ad6dbb6a50be4.jpg)

We'll begin with Selesnya's first guild mechanic, convoke. Convoke was designed by [Richard Garfield](https://web.archive.org/web/20121001000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Richard%20Garfield), interestingly enough, for the Boros guild. Richard felt that it conveyed the sense of the army working together to strengthen the unit. Richard called it crittercast. I enjoyed crittercast but told Richard I thought he had put it into the wrong guild. I'd been looking for a creature-centered mechanic for Selesnya and crittercast fit the bill perfectly.

For starters, convoke is a mechanic that requires creatures yet doesn't only go on creatures. In addition, it greatly rewards players having a lot of creatures. That is very much the identity we wanted with Selesnya. In addition, it lines up beautifully with the philosophy of the guild, as green and white's overlap is very much about the value of community. Selesnya's strength in the story is that it is the most selfless of the guilds. Its guild members consider each other equals and want to work together.

Convoke did a wonderful job of conveying a sense of closeness between the creatures because they have to work together to cast spells. Also, it did a good job of helping green-white get out bigger creatures faster to help their route to victory. Remember that the cost reduction wasn't solely about getting out big creatures. It also allowed a player from Selesnya to cast spells without requiring mana. These types of spells tended to be cheap, to maximize the amount of times they can be used for "free."

Early plotting is all well and good, but at some point you have to actually make the cards with the mechanic. It's at this point that you start to explore how much design space a mechanic can support. Let me quickly explain what you're looking for in this area:

**1.** **How many different card types can this mechanic go on?**

For each additional card type a mechanic can be used on, you're opening up more space.

**2.** **Does it require any restrictions?**

One of the biggest limiters of design space is simply self-limitations by the mechanic itself. Does the mechanic require targeting? Does it require a variable number? Does it require an ability that can be tweaked? Many mechanics get locked down because there is simply a small list of things that fit the card's mechanical requirements.

**3.** **Does the mechanic fight with itself for space?**

Another big problem is when a mechanic fights for a resource with other cards with the same mechanic. For example, we've been trying to find a home for [delve from *Future Sight*](https://web.archive.org/web/20121001000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+%5bdelve%5d&set=+%5b%22Future+Sight%22%5d)*.* One of delve's biggest issues is that it's hard to put too many in your deck because each one wants to eat up your graveyard, leaving no food for future delve cards. When this happens, it forces the designers to lessen how many cards they make with the mechanic.

One of convoke's greatest strengths was that it didn't cause any of these problems. It could go on any card type, it didn't have any real restrictions, and it didn't fight with itself. In fact, with the last issue it went the opposite way. The enablers for convoke worked well with all convoke cards, often encouraging you to play with more convoke.

Of the original ten *Ravnica* guild mechanics, I believe convoke was the strongest design with the most potential for future use.

![](https://i.ormos.uk/60/ca/60ca0a2660b7aac9c4031158820888856dd2ef0d80231b39cd1a8129a573b1ed.jpg)

[Coursers' Accord](https://web.archive.org/web/20121001000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Coursers%27+Accord) | Art by [Nils Hamm](https://web.archive.org/web/20121001000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Nils%20Hamm%22%5D)

### Populate

One of the things we tried with the new guild keywords in *Return to Ravnica* was to find ways to make a new keyword that wasn't simply retreading what the first guild mechanic had done. Convoke did a wonderful job, but we needed to find a different way to attack the problem. Obviously, the mechanic had to be creature-centered, but other than that we were free to explore any design space.

I felt like in *Ravnica*, Selesnya had explored the idea of creatures helping one another. I was interested in focusing more on the explosive nature of creatures in green-white. Selesnya's victory plan is to overwhelm the opponent with creatures. What if the new Selesnya guild mechanic helped with this explosion?

The first place my mind went was this card:

![Doubling Chant](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Doubling+Chant)

 

Could we make a mechanic out of this? No, it was a little too much. Could we tone it down? That's when I stumbled upon the idea of a proliferate for creature tokens. [As I've explained](https://web.archive.org/web/20121001000000/https://magic.wizards.com/en/node/656276), the first version was pretty much just that—it made a copy of each type of token. If you had two 1/1s, a 2/2, and two 3/3s, the spell would make a new 1/1, a new 2/2, and a new 3/3. I believe that version lasted for one playtest before it got changed to its current version. It was both too strong and created a weird incentive for deck building—you wanted to have as many different types of tokens as possible.

The interesting thing about populate is that, even though we cracked the mechanic during the first few weeks of design, populate caused a lot of headaches because it's what I call a two-tier mechanic. Let me explain. Some mechanics live on their own. That is, they don't require the interaction of any other card, or, if they do, what is being asked is something that **Magic** regularly provides.

A two-tier mechanic, though, requires some other element to exist in the set. In the case of populate, that second tier is token creatures. As second-tiers go, this one isn't too bad. The game naturally has tokens and green and white are the two colors that tend to create the most tokens. (Mass token generation used to be primary green and secondary white, but that got swapped when we decided to push harder on white being the army color—this is also when we changed it so white got the most creatures at common.)

Usually, the second tier has to be able to stand on its own, otherwise it becomes what we call parasitic (i.e., it only works with other things from the same set). Selesnya required us to up the overall number of tokens, but as they work fine in isolation we felt comfortable ramping it up. We felt that it would give Selesnya a stronger feel without severely handicapping the set. (Note that this did mean we had to be a little more cautious with the cards that are the natural enemies of token creatures—bounce spells, I'm looking at you.)

Populate ended up having two major problems. One, the populate part of the two-tier system was parasitic. It didn't mean anything without the other piece. Luckily, tokens are a strong part of **Magic**'s past, so although populate is parasitic it was at least parasitic with a lot of already-existing cards. Two, common populate cards had the problem of stranding players with populate cards without tokens.

The first problem we knew we had to suck up but the second one had some work-arounds. The most common trick we did was to make the populate cards themselves create tokens, ensuring there was always something to populate. The other common trick was to use populate as a rider. That way, if you didn't have a token in play, the card still had a function.

The end result of all this is that populate ended up having less design space than convoke. That's not a bad thing, as one of the biggest advantages of the guild system is that we can make use of mechanics that aren't quite big enough to be a showcase mechanic (a major high-focus mechanic of a set). Because we had fewer populate cards overall, we made sure to have a bunch of the higher rarity ones be repeatable. This would help increase the amount of populating going on during a game.

Populate was definitely a bigger pain to design, and design around, than convoke, but I'm very happy with how it turned out. Selesnya, due in a big part to populate, is my favorite guild to play in *Return to Ravnica*. (It's not my favorite in the block, but we'll get there soon enough.)

![](https://i.ormos.uk/41/e2/41e23608241c40b49af4d32dcb8b5097f588d3a8ee2249c0cb7b788f2f271a7b.jpg)

[Common Bond](https://web.archive.org/web/20121001000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Common+Bond) | Art by [Raymond Swanland](https://web.archive.org/web/20121001000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Raymond%20Swanland%22%5D)

### Any Final Thoughts?

The joy of designing guilds is capturing the purity of the guild's message. I'm very happy how we managed to make Selesnya creature-centric in *Return to Ravnica* but in a way different from the original *Ravnica*. I've mentioned how one of our goals was to make sure the new version of the guild felt unique but still blended nicely with what was done before.

I like how convoke and populate hit different notes but are still working toward the same goal. This means when you mix the watermarks from original Selesnya with the new Selesnya, you get a combination of cards that work together and create a unified feel.

### Love and Compassion

I'm happy I started with Selesnya because its design was much like the guild itself—pleasant and non-threatening. In future weeks, I'll get to some guilds that aren't quite as easygoing and have a lot less in common between their two colors. But I'm getting ahead of myself.

I hope you enjoyed today's peek at Selesnya, and as always, I'm curious to hear any feedback (my email, this thread, [Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Google+](https://plus.google.com/107824009487778543249/posts)).

Join me next week when I answer your questions about the design of *Return to Ravnica*.

Until then, may you find a collection of people who care about your welfare.
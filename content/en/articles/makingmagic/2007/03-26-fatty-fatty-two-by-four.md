---
id: vf0kxawh
kind: article
lang: en
path: /en/articles/makingmagic/2007/03-26-fatty-fatty-two-by-four
title: Fatty, Fatty, Two By Four
published: '2007-03-26'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
    lang_detected: en
    capture_id: 220370
    url: https://magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
    captured_at: '2024-05-18 04:14:45+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
    lang_detected: en
    capture_id: 220370
    url: https://magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
    captured_at: '2024-05-18 04:14:45+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
    lang_detected: en
    capture_id: 220370
    url: https://magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
    captured_at: '2024-05-18 04:14:45+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
    lang_detected: en
    capture_id: 220370
    url: https://magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
    captured_at: '2024-05-18 04:14:45+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: vf0kxawh
  url: https://magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
  page_key: magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
  lang: en
  template: contentful
  captured_at: '2024-05-18 04:14:45+00'
  capture_id: 220370
  wayback_url: https://web.archive.org/web/20240518041445id_/https://magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
- document_id: vf0kxawh
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr272
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr272
  lang: en
  template: aspx
  captured_at: '2012-11-11 21:41:10+00'
  capture_id: 800278
  wayback_url: https://web.archive.org/web/20121111214110id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr272
- document_id: vf0kxawh
  url: https://magic.wizards.com/en/articles/archive/making-magic/fatty-fatty-two-four-2007-03-26
  page_key: magic.wizards.com/en/articles/archive/making-magic/fatty-fatty-two-four-2007-03-26
  lang: en
  template: drupal
  captured_at: '2022-10-27 08:53:53+00'
  capture_id: 879544
  wayback_url: https://web.archive.org/web/20221027085353id_/https://magic.wizards.com/en/articles/archive/making-magic/fatty-fatty-two-four-2007-03-26
- document_id: vf0kxawh
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr272
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr272
  lang: en
  template: classic_asp
  captured_at: '2008-06-16 21:59:53+00'
  capture_id: 1975391
  wayback_url: https://web.archive.org/web/20080616215953id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr272
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: vf0kxawh
  capture_id: 220370
  url: https://magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
  wayback_url: https://web.archive.org/web/20240518041445id_/https://magic.wizards.com/en/news/making-magic/fatty-fatty-two-four-2007-03-26
  captured_at: '2024-05-18 04:14:45+00'
  template: contentful
  sha256: a081f061e729a9eb01148310f05a3a009c30a092683080f54d3a52ba41077a00
render_recovery: []
---
Welcome to Fatty Week! For those unfamiliar with the term, it is a piece of **Magic** slang meaning a large creature usually with five or more power and three or more toughness. (And there's even some debate whether creatures with toughness less than five should count – I just find it sad to not think of [Juggernaut](https://web.archive.org/web/20070326000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Juggernaut) as a fatty.) As it's Fatty Week and I always write in theme, I'll be talking about designing fatties.

While I started putting together the column, I realized that it touched upon a point that I've been meaning to write about but hadn't yet gotten the chance. You see, I've talked numerous times about Timmy, Johnny and Spike, the three psychographics that R&D uses to help define the players (most notably in my columns "[Timmy, Johnny, and Spike](/en/articles/makingmagic/2002/03-11-timmy-johnny-and-spike)" and "[Timmy, Johnny, and Spike Revisited](/en/articles/makingmagic/2006/03-20-timmy-johnny-and-spike-revisited-3)"). But I've never really spent much time talking about how design for each of the three differs from one another.

Then while putting together my column on designing fatties I realized that it just so happens that the designs for fatties can be split up among psychographic lines. This means that I can both give you an insight into how we design fatties and I can demonstrate how each group requires different criteria. Sound like fun? I sure hope so because if not the rest of the column's just downhill from here.

Here's how it's going to work. I'll start each section by showing you some cards that are examples of the section I'm a bout to talk about. Then I will explain what qualities those cards have that define them for the specific psychographic. One quick note before I begin: The psychographics are very complex. There are many facets to each group and each subgroup can require unique design challenges. Unfortunately, that article would be "War and Peace" long, and I only have several thousand words. So, I'm going to be talking in generalities. For each psychographic I'm going to focus on the qualities that cast the widest net and most separate from the other two psychographics. That said, let's talk psychographic design.

### Timmy

![Visara the Dreadful](https://i.ormos.uk/42/31/423182919565f099682aa8f6adbd3e5aff6a3044930937283770f819cf604e67.jpg)

![Borborygmos](https://i.ormos.uk/14/b0/14b03501180e8824fbce090a266aa1b9c403bfd302d7a53bb77cc080dd0ba34e.jpg)

![Sol'kanar the Swamp King](https://i.ormos.uk/24/3b/243b131777b2bc3bbdcaee752901a4dba18f269a7eba3d800ad6093dd86a8b06.jpg)

So what does Timmy look for in a fatty? To answer this, let's recap what Timmy looks for in a game of **Magic**. Timmy wants to experience something. Timmy is in it for the visceral thrills. Timmy wants to have fun. For Timmy, it's all about whether the game was enjoyable not necessarily the outcome. Yes, Timmy tries to win and yes winning is fun, but to Timmy winning in a boring game is not as much fun as barely losing in an exciting one.

**Timmy Fatty Rule #1 – The creature must look impressive.** First off, Timmy needs to have a creature that's impressive. The joy of a fatty to Timmy is the thrill of harnessing something awesome. They want to see their opponents' faces as they slam it on the table. They want to yell something out as they turn it sideways for the attack. They want their fatty to make a big impression on the game. Timmy is in the game for the rush. He wants to do things that excite him. Plunking down an intimidating fatty qualifies. Timmy fatties are on average bigger than most other fatties because, more than any other psychographic, Timmy appreciates size. Also, Timmy appreciates abilities. Many popular Timmy fatties have a number of abilities. While I'm talking about mechanics here, please note that it's also important for the Creative to create a dramatic and positive impression.

**Timmy Fatty Rule #2 – Avoid the drawbacks.** Timmy wants his fatty to seem as cool as possible. When he brings it out, he wants it to be clear how good it is. For this reason, Timmy fatties tend not to have drawbacks. Once they make it to the table, they're all upside. Yes, there are a few exceptions to this. Usually the downside is something that either doesn't seem too severe or even seems like it possibly could be an upside. Also, the bigger the creature, the more willing Timmy is to try and make it work.

**Timmy Fatty Rule #3 – The creature is expensive.** The second rule leads directly into this one. Timmy wants big, impressive creatures. Timmy doesn't want drawbacks. This leads us to the Triangle Rule of Design. Cards can only ever have two of the following three – be big, have no drawbacks, be cheap. You can have big and cheap if you have a drawback. You can have no drawbacks and be cheap but then you get a small creature. And you can have big and no drawback but then it isn't cheap. Timmy prefers the last category because the previous two rules lock out any other option. The easiest way to think of this is that Timmy fatties should be all upside. Once you get a Timmy fatty out, you're golden. Getting there is the only sticking point. This, by the way, is why few Timmy fatties make tournament play and then they mostly show up in decks that don't "cast" them traditionally (such as reanimation). Timmy wants and gets a lot for his fatties; he just has to pay for it.

**Timmy Fatty Rule #4 – The creature needs to be active.** Not only does Timmy want jaws to drop when he gets his fatty out, he also wants it to do something impressive. This means that Timmy fatties must either encourage attack or make something significant happen each turn. In general this means that you have to be very careful with tap abilities on Timmy fatties. Remember that when designing Timmy fatties, designers are trying to impress Timmy. They want the first impression to be memorable because it tells Timmy that he can recreate that feeling in every game he plays.

What does all this mean for designers? It means that designing Timmy fatties is very much about accentuating the positive. The hook between mechanics and creative is vital. The designer's goal is to impress Timmy much as Timmy wants to impress himself and everyone he plays with. Most importantly, Timmy fatties have to be fun to play with. When Timmy gets a fatty out, he wants to be talking about it the next day.

### Johnny

![Eater of Days](https://i.ormos.uk/e1/71/e1711eaa7c435206c809fe2655e14d25653b581f949d72c1d22731d59b4a65b1.jpg)

![Rakdos the Defiler](https://i.ormos.uk/b1/2b/b12b32bc5a2e79bc44c0c2613bac57dedf4b3b671ddad513534674c956447612.jpg)

![Sky Swallower](https://i.ormos.uk/03/46/034618fdb84e4445b79a7509eb97aca99729ab4ca23d0904198eae65ca146bae.jpg)

Let's begin by examining what Johnny wants out of a game. He wants to express something. For Johnny, deck building is a canvas for him to do his art. He uses the game as a means to show how he can take it in new and interesting directions. Johnny loves that **Magic** lets him show off his creative side. Johnny plays to win, but he plays to win with style (and on his own terms). Winning isn't an issue of quantity but quality. Johnnies constantly handicap themselves by playing suboptimal cards. Why does Johnny do this? Because he wants to show that he can do things that other players dare not try.

**Johnny Fatty Rule #1 – The creature needs to have a puzzle element.** Johnny isn't as straight-forward about his fatties as Timmy. Johnny is more attracted to fatties that provide a challenge. To do this, design takes two basic paths. First is what I'll call the puzzler. This is a creature that is usually cheap and powerful but comes with a strange drawback. Not something the player can just live with (we'll get to these in a moment when we get to Spike), but rather a drawback that forces the player to construct his deck around it. The second path, what I call the mystifier, is to make a fatty that has some positive effect that is offbeat enough that Johnny has fun figuring out how best to use the strange ability. In either case, a Johnny fatty presents Johnny with a puzzle: Find a way to craft a deck that can make use of it.

**Johnny Fatty Rule #2 – The creature has to be worth it.** This rule applies to the puzzlers. If you're going to make Johnny jump through a bunch of hoops (and Johnny likes hoops better than anyone) then the payoff needs to be worth it. This is why most of the puzzlers are quite big.

**Johnny Fatty Rule #3 – The creature has to create an interesting environment.** This rule applies to the mystifiers. If the designer's going to make Johnny work to use of the creature, then he or she needs to make sure that the game state it is creating is fun. What this means is that puzzlers are a lot easier to design than mystfiers. Usually you can tell pretty quickly if a handicap is interesting, but making sure a quirky environment changer is doing its job takes a bit more research. And yes, by the way, design does take a lot of playtesting. I know we mostly talk about it in regards to development, but design has the responsibility of figuring out if certain cards and mechanics are fun to play. The best way to do this is to make some cards and actually experience them first hand.

**Johnny Fatty Rule #4 – The creature requires thought.** This final rule is really a summation of the first three rules but it's important enough that I thought I'd restate it. Timmy is looking for a visceral thrill in his fatties. Johnny is looking for mental stimulation. This means that Timmy needs to understand that his fatties rock almost instantaneously. Johnny enjoys fatties that he doesn't know right off if they're good or not. The thrill for Johnny is to find a way to make his fatty work. To accomplish this, the designers have to make cards that aren't clear cut from first blush.

What does this mean to designers? Johnny fatties require more work than the other psychographic fatties. They have subtleties built into them that the other fatties (especially the Timmy ones) don't. Johnny fatties are made to encourage exploration. They throw down the gauntlet to Johnny to see if he can rise to the challenge. This means that the best Johnny fatties aren't always obvious but when Johnny does figure it out, the thrill is just as high for him as Timmy is when he's beating down with his giant monster.

### Spike

![Juzam Djinn](https://i.ormos.uk/82/24/8224b00bac6033ce32d54391ee46aed3e28b27fcb700316c5253d3346034449b.jpg)

![Calciderm](https://i.ormos.uk/45/31/4531366acbcfde0f6b271de8d897c0269dcf7864dbef5366540cf714a34c77d2.jpg)

![Phyrexian Negator](https://i.ormos.uk/cf/ac/cfacd63a626da4b47b958dc616a15d7ab28175164d3268957cbd0afd137f18fd.jpg)

What does Spike want out of a game of **Magic**? Spike wants to prove something. For Spike, **Magic** is the ultimate test. His goal is to maximize his wins. The more he wins, the better he fares on the test. Because of this Spike takes great pride in understanding the game as well as possible. He enjoys "breaking" cards to figure out which ones are the most powerful. Fatties are the hardest sell to Spike because he is the most sensitive to mana cost. Spike is the bargain shopper, always looking for the most he can get while spending the least.

**Spike Fatty Rule #1 – The creature must be cost efficient.** Both Timmy and Johnny are willing to pay extra for something that excites them. Not Spike. Spike, more than any other psychgraphic, cares about mana. Spike understands that **Magic** is at its heart a game about resource management. Spike is the one that watches his mana curve and carefully chooses his land mix. What this means for Spike fatties is that they don't tend to cost all that much. (There is one exception which I get to below in Timmy/Spike.)

**Spike Fatty Rule #2 – The creature must be powerful.** At the same time, Spike very much cares about power level. He will only play cards that reach a certain tournament threshold. This means that if a fatty doesn't deliver – that is, if it can't single-handedly win games – Spike isn't interested.

**Spike Fatty Rule #3 – The creature has a drawback.** Above I talked about the Triangle of Design. I said that you can get any two pieces at the cost of the third. Since the first two rules make cheapness and power non-negotiables, this means that Spike has to learn to live with drawbacks. He's okay with this, because Spike understands that something has to give.

**Spike Fatty Rule #4 – The drawback must be something that can be dealt with, not built around.** The drawbacks on a Spike fatty are very different than those on a Johnny fatty. Johnny likes drawbacks that force him to build around them. Spike prefers his drawbacks to be cards that he can just live with. Yes, he might make slight tweaks to his deck, but in general a Spike fatty has to be something that Spike is willing to just throw in one of his existing decks. The easiest way to separate the two is to think of whether or not "worthless" cards (a.k.a cards that wouldn't be played solely on their own merit) have to be used to help balance the drawback. If they do, it's a Johnny fatty. If not, it's a Spike one.

What does this mean to designers? It means that Spike fatties are harder to make in volume. Spike likes big, intimidating creatures as much as the next player. Where Spike differs is that he's not willing to make any allowances for it. If a fatty can't live up to the quality of the other cards in the deck, it simply won't make the cut. Like Johnny, Spike cannot immediately tell if a fatty is to his liking. And like Johnny, Spike enjoys the search. Spike likes finding the diamonds in the rough. Similar to Johnny fatties, Spike fatties require a little extra work from the designer. The key is finding drawbacks that make Spike wince, but not so much that he's unwilling to try it out in a deck.

### Timmy/Spike

![Akroma, Angel of Wrath](https://i.ormos.uk/36/aa/36aa028be364dfd24f908fb71982ec654c255f720a1db6a3cd5ef69eb0ee4021.jpg)

![Bogardan Hellkite](https://i.ormos.uk/e9/ce/e9cea74bdd84f190830bb2b227d8a979ae7ce4c401bb0018540d82d96fbfb995.jpg)

![Simic Sky Swallower](https://i.ormos.uk/1f/74/1f74023c57456893fed9cc0e6692871057c8dd903628dbfb76f725918a9d8f00.jpg)

Now that I've walked through the three demographics, it's time to start talking about the hybrids. I'm not going to spend as much time on them as they are more niche than the three base psychographics. So we begin with Timmy/Spike. I said that Timmy wants straight-forward fatties without any downside. Spike wants the most efficient fatties he can have and as such they tend to have drawbacks. Where's the overlap?

It turns out that there is a way to make efficient, all upside fatties. You need to get aggressive with their costing. The reason this isn't done all that much is that the game can only take so much pushing of power at any one time. The most common ways to push costing is to mess with mana either by including more colored mana or by making the card multicolored (and thus also pushing colored mana). Another trick used sometimes is to make the card a legend, as the slight drawback of being a legend can sometimes can eke out another chopping off of mana.

Finally, designers can push fatties towards both Timmy and Spike by creating cards elsewhere in the environment. First, they can create cards that make it easier to play larger creatures. A good example of this would be an aggressively costed reanimation spell which forces Spike to find big upside (aka Timmy fatties) to target. Second, the environment can favor a certain subset, raising the value of certain Timmy fatties. This can be seen, for instance, in a tribal environment such as *Onslaught* where certain creature types' value is higher than normal.

The key to this hybrid is finding a way to attract Spike through a means other than a cheap cost and a drawback.

### Timmy/Johnny

![Phyrexian Dreadnought](https://i.ormos.uk/70/9d/709ddd69808c34a9e8b7c866f9f560c1504c92505c2c9c8f0b1b17b174129533.jpg)

![Lord of the Pit](https://i.ormos.uk/93/f6/93f673ebc842f55304c7e5b063f33419c3db174b70e929e869c7f21bb9b80e76.jpg)

![The Unspeakable](https://i.ormos.uk/2e/10/2e10a9ac00f861da21fb598f8b123c4f3a4e09d635318b2aeb7268ef4d8aaffc.jpg)

The trick to designing to this hybrid is to find a way to make fatties that are both exciting but require some thought to build around. There are a number of tricks to do this. First, you can make the overall payoff so exciting that Timmy is willing to jump through Johnny's hoop. The simplest way to do this is through raw size. As I said above, Timmy is much more willing to look past things if the creature is tempting enough.

The next trick is to use a drawback that Timmy doesn't perceive as very serious. This is one of the most important tricks in a designer's bag – understanding what costs are and aren't perceived as threats to the players. This isn't a well that designers can go to too often, but many a popular Timmy/Johnny fatty was created with this plan in mind.

The final trick is to make a weird environment changer that sounds exciting. This way, the creature gets perceived as all upside by the Timmy half and exciting to build around by the Johnny half.

### Johnny/Spike

![Greater Gargadon](https://i.ormos.uk/d0/2d/d02d00adfda35d7438e81509645b0e8c5003e4a3ba9c12a8c4aa87c4caddf514.jpg)

![Sundering Titan](https://i.ormos.uk/96/4f/964feed616df46d370510f91f9334becfed5e458792ea1a5767a615552ff52ac.jpg)

![Terravore](https://i.ormos.uk/d9/84/d984fbaead921b65d981ffa11c953075f737b7568397e44611970cc2564633e5.jpg)

This hybrid requires the designer to find interesting concepts that can be pushed in power level. The most common example is fatties that double as engines (cards that allow players to turn one resource into another). Engine fatties have the advantage of being both powerful and interesting.

Another trick is to create fatties with drawbacks that can be built around using tournament level cards. To do this the designer needs to look at what resources Spike has in a given environment and then create a Johnny fatty that taps into that vein. For example, let's say the environment has a lot of strong card drawing spells. A designer can create a fatty whose drawback is balanced through card advantage. Essentially, Johnny is given access to Spike-level cards to craft his deck.

The final way to build this hybrid is to push the power level of a straight Johnny fatty. Once the fatty becomes efficient enough it justifies using other resources to get it into play. Like with the Spike/Timmy fatties, this avenue needs to be used sparingly if the designers/developers want to keep the overall power level in check.

### Timmy/Johnny/Spike

![Verdant Force](https://i.ormos.uk/45/e6/45e692ab90fb47132781cf3e176b4fbbab2f29cd1e99d845932d70a5a5b29a6f.jpg)

![Gleancrawler](https://i.ormos.uk/49/c4/49c46e1b28920d8bfeb268068592bcb782e560e50286bb7a62f5d1f3397b1e56.jpg)

![Serra Avatar](https://i.ormos.uk/3a/bb/3abbd5ea3a7e9e26c4b3e15fcd82aa7dc4d9ad22c21a0070fb94ed3af95e2878.jpg)

As I've mentioned before, R&D calls any card that appeals to all three psychographics "hat tricks." Making hat tricks is incredibly hard. Making hat trick fatties – even harder. Basically the way this is done is by taking what is essentially a Timmy/Johnny card and pushing either the card itself or the environment around it. Basically, the card has to have a solid body and then have an effect that excites Timmy, enthralls Johnny and taunts Spike. While hard to come by, hat trick fatties are truly exciting for a designer when you stumble upon one.

### Chewing the Fatties

I hope today's column both gave you an interesting insight into the process of designing fatties as well as how each psychographic requires different design needs. I'd be interested to hear what fatties excite all of you. (Also let me know what psyographic you are – both through self-identification and the results of the test from "[Timmy, Johnny and Spike Revisited](/en/articles/makingmagic/2006/03-20-timmy-johnny-and-spike-revisited-3).")

Join me next week when I explore a topic that's excited me for most of my life (and yes, it's actually connected to card design).

Until then, may you find the fatty that allows you to experience, express, and/or prove something.

Mark Rosewater
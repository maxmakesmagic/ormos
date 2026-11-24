---
id: 9jas1fbp
kind: article
lang: en
path: /en/articles/makingmagic/2002/04-01-tweak-in-review
title: Tweak in Review
published: '2002-04-01'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
    lang_detected: en
    capture_id: 233288
    url: https://magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
    captured_at: '2023-12-07 02:35:03+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
    lang_detected: en
    capture_id: 233288
    url: https://magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
    captured_at: '2023-12-07 02:35:03+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
    lang_detected: en
    capture_id: 233288
    url: https://magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
    captured_at: '2023-12-07 02:35:03+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
    lang_detected: en
    capture_id: 233288
    url: https://magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
    captured_at: '2023-12-07 02:35:03+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 9jas1fbp
  url: https://magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
  page_key: magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
  lang: en
  template: contentful
  captured_at: '2023-12-07 02:35:03+00'
  capture_id: 233288
  wayback_url: https://web.archive.org/web/20231207023503id_/https://magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
- document_id: 9jas1fbp
  url: https://magic.wizards.com/en/articles/archive/making-magic/tweak-review-2002-04-01
  page_key: magic.wizards.com/en/articles/archive/making-magic/tweak-review-2002-04-01
  lang: en
  template: drupal
  captured_at: '2022-01-28 17:48:28+00'
  capture_id: 931194
  wayback_url: https://web.archive.org/web/20220128174828id_/https://magic.wizards.com/en/articles/archive/making-magic/tweak-review-2002-04-01
- document_id: 9jas1fbp
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr14b,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr14b
  lang: en
  template: classic_asp
  captured_at: '2005-03-02 23:25:00+00'
  capture_id: 1972247
  wayback_url: https://web.archive.org/web/20050302232500id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr14b,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9jas1fbp
  capture_id: 233288
  url: https://magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
  wayback_url: https://web.archive.org/web/20231207023503id_/https://magic.wizards.com/en/news/making-magic/tweak-review-2002-04-01
  captured_at: '2023-12-07 02:35:03+00'
  template: contentful
  sha256: 2aa3c084344959822c14a8df558250695a2d636eb550d64f91597261406e6b2b
render_recovery: []
---
Welcome to Land Destruction Week! This week we’ll be taking a look at one of the game’s oldest archetypes. R&D has a very interesting perspective when it comes to land destruction and I was planning to take my column this week to explain how this outlook influences how we design and develop land destruction cards. But I discovered that Randy was planning to write the exact same article. So, if you’re interested in that topic, make sure to take a peek at “Latest Developments” (Randy’s column) this Friday. Instead I thought I’d take today’s column to discuss an overlooked aspect of design.

### Pun for the Road

Before I start this week’s column, I wanted to update you all on the results of my poll last week about whether puns should continue in flavor text. The vote was closer than most of our polls and ended up:

<table><thead><tr><th colspan="3"><b>Do groaner puns have a place in Magic?</b></th></tr></thead><tbody><tr><td>Yes</td><td>1792</td><td>58%</td></tr><tr><td>No</td><td>1277</td><td>42%</td></tr><tr><td>Total</td><td>3069</td><td>100%</td></tr></tbody></table>

So what does this mean? It’s a complicated topic that the Creative Director and his team are putting some attention towards. Look forward to future sets to see the outcome.

Now, on with today’s column.

### Day-to-Day

How many of you have seen the movie “Backdraft?” Remember the scene where Kurt Russel runs out of a burning room with a child tucked under his arm? Seconds after he makes it to the hall, a ball of flame explodes from the room behind him. That image represents how the average person sees the job of a firefighter: they’re running in burning buildings saving orphans. The truth is the average firefighter probably runs into a burning building only a handful of times each year. This is not meant as a knock to firefighters; I respect anyone whose willing to run into a burning building even once. My point is that a firefighter’s day-to-day job is more about mundane activities, like say upkeep of the firetruck, than heroic rescues.

The same goes for **Magic** designers. Designers do spend some of their time coming up with radical new cards with interesting, offbeat abilities. But a lot more of our time is spent making the basics work. Rares are fun, but a set lives or dies on its commons. So what does this have to do with land destruction? (As a quick aside, do you notice how many of my columns require me to assure you that I’ll eventually get to the assigned topic?) Well, land destruction is one of the basic abilities we include in every expansion. As such, it’s a perfect example to explore a time-tested R&D staple -- the tweak.

### Tweak in the Knees

A tweak is a card that does exactly what a previously printed card does except with one tiny change. As an example, [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) is a red sorcery that destroys a land. It was designed by Richard Garfield and appeared in Alpha. Examples of tweaks of [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) would be:

*   [Raze](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raze) (from *Urza’s Saga*) – it’s cheaper but destroys one of your lands
*   [Lay Waste](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lay+Waste) (from *Urza’s Saga*) – it also cycles
*   [Devastate](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Devastate) (from *Prophecy*) – it also deals a point of damage everything
*   [Dwarven Landslide](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dwarven+Landslide) (from *Apocalypse*) – if kicked it can destroy a second land
*   [Earth Rift](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earth+Rift) (from *Odyssey*) – it has flashback

The purpose of a tweak is to capture the essence of the old spell but still have some element that makes the card seem new. Ironically, this is one area where my Hollywood skills come into play. Hollywood is all about rehashing the old in a new, improved form. One of the more entertaining aspects of this is in something known in Hollwywood as the “three-beat.” A three-beat is where you take a new idea and sell it by condensing it down to a cross section of two old ideas. For example, *Spy Kids* would be pitched in Hollywood as *James Bond* meets *The Goonies*. *Smallville* is *Superman* meets *Dawson’s Creek*. And *A Beautiful Mind* is *Good Will Hunting* meets *Sybil*.

**Magic** design, believe it or not, is actually quite similar. A designer sits down to create his commons. Early in the process, the designer has to create cards that fill some of the basic staples of the game (creature destruction, card drawing, combat tricks, etc.) but in a new way. Thus begins the “tweak” process.

### #1) Block Mechanics

The first place the designers look for tweaks is the mechanics of the block. The designers need cards using the new mechanics anyway, so it’s a perfect fit. Let’s take *Odyssey* as an example. The new mechanics were flashback and threshold. [Earth Rift](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earth+Rift) was an obvious marriage. [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) meets flashback. The design team also fiddled around with a threshold [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain), but none ever saw print as we didn’t find a version we liked.

### #2) Additional Effects

Sometimes the best way to tweak a card is to recreate the effect and add a little something extra. [Devastate](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Devastate), from *Prophecy*, is a good example. It’s [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) meets [Tremor](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tremor). The hard part of this kind of tweak is the two abilities have to have some sort of synergy either playwise or flavorwise, ideally both. [Devastate](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Devastate), for instance, fits both bills as it gives land destruction decks a way to deal with weenie creatures and it has a nice "earthquake" flavor.

### #3) Drawbacks

Another popular technique is to make the effect cheaper but with a drawback. [Raze](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raze) (from *Urza’s Saga*) is a good example of this category. “Stone Rain you” meets “Stone Rain me.” [Raze](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raze) knocks off two mana from [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) in exchange for sacrificing one of your own lands. This makes a more aggressive version that requires deck builders to be a little more creative to offset the drawback.

### #4) Limit the Effect

This tweak is related to the last one. In this category a designer takes a basic effect and then limits what the effect can do. In exchange, the spell becomes cheaper. [Lava Blister](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Blister) (from *Odyssey*) falls into this category (although it’s not a clean example since it uses the “punisher” mechanic) as the card only destroys nonbasic lands. [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) meets [Ruination](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ruination).

### #5) Change the Speed

Another popular tweak R&D will do is to change the speed of the spell by turning instants into sorceries or sorceries into instants. [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) is actually a bad example of this as R&D has chosen to keep land destruction effects a sorcery (for more on this see Randy’s Friday article). The one example I was able to come up with was [Rith's Charm](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rith%27s+Charm) (from *Planeshift*), but I’m not sure how much it counts as a tweak. [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) meets random instant.

### #6) Repeats

The final answer is, of course, to simply repeat a card. I guess technically this isn’t a tweak, but it is often the best answer to fulfilling certain voids. A question I’m often asked is why we reprint cards. This topic is big enough for its own column, but in a nutshell (last time I said this, I opened quite the can of worms) repeats do the thing they do more eloquently than anything else. In the case of [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain), it’s hard to beat the simplicity of “Destroy target land.” [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) meets [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain).

That said, R&D does try to mix up the repeats. Sometimes we’ll repeat the basic card and sometimes we’ll do a tweak. [Stone Rain](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) is a good example of this. (Although I should note that early on it was our most-repeated card.)

Alpha: The Original Real-Deal  
*Ice Age*: repeat  
*Mirage*: repeat  
*Tempest*: repeat  
*Urza’s Saga*: tweak ([Lay Waste](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lay+Waste))  
*Mercadian Masques*: repeat  
*Invasion*: tweak ([Plague Spores](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Spores), [Frenzied Tilling](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frenzied+Tilling))  
*Odyssey*: tweak ([Earth Rift](https://web.archive.org/web/20020401000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earth+Rift))

The best parallel for this category is that of the cliché. Sometimes you want to state your idea in a fresh manner and sometimes the cliché just does it better than any other version can.

### Take This Job and Love It

The key to being a good designer is to find joy in the subtlety of design. Commons aren’t drudge work, but rather an opportunity to meld creativity with simplicity. “Making Magic” is a weekly glimpse into the life of a **Magic** designer. Hopefully, this column will give you insight into one of the more mundane (but far from boring) tasks we deal with every day.

Next week, I’ll take a look at the work all of you did as designers.

Until then, may you have plenty of land in hand against the land destruction deck.

Mark Rosewater

*Mark may be reached at makingmagic@wizards.com.*
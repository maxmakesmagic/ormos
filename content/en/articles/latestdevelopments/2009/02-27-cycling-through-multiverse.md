---
id: zmr3tr2m
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/02-27-cycling-through-multiverse
title: Cycling through Multiverse
published: '2009-02-27'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
    lang_detected: en
    capture_id: 720135
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
    captured_at: '2021-12-02 13:56:53+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
    lang_detected: en
    capture_id: 720135
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
    captured_at: '2021-12-02 13:56:53+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
    lang_detected: en
    capture_id: 720135
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
    captured_at: '2021-12-02 13:56:53+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
    lang_detected: en
    capture_id: 720135
    url: https://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
    captured_at: '2021-12-02 13:56:53+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: zmr3tr2m
  url: https://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
  lang: en
  template: drupal
  captured_at: '2021-12-02 13:56:53+00'
  capture_id: 720135
  wayback_url: https://web.archive.org/web/20211202135653id_/https://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
- document_id: zmr3tr2m
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/27
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/27
  lang: en
  template: aspx
  captured_at: '2013-07-07 18:25:58+00'
  capture_id: 620655
  wayback_url: https://web.archive.org/web/20130707182558id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/27
- document_id: zmr3tr2m
  url: http://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-27
  page_key: magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-27
  lang: en
  template: drupal
  captured_at: '2017-08-27 08:26:42+00'
  capture_id: 720141
  wayback_url: https://web.archive.org/web/20170827082642id_/http://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-27
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: zmr3tr2m
  capture_id: 720135
  url: https://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
  wayback_url: https://web.archive.org/web/20211202135653id_/https://magic.wizards.com/en/articles/archive/latest-developments/cycling-through-multiverse-2009-02-26
  captured_at: '2021-12-02 13:56:53+00'
  template: drupal
  sha256: c6101911983aba14fbb579ff511b4c28fbedde8b98e5edbf62a7920aeee789bb
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
Cycling is a mechanic that we have used in many, many blocks. Mark Rosewater's column on Monday talked about how the designers have used it in different ways in each of the four blocks that have featured it. It would be difficult for me to give a similar internal picture of the rich history that cycling has had; I joined **Magic** Ramp;D in June of last year, which was after all of *Conflux*'s cycling cards had been nailed down. Instead, I decided to go crawling through Multiverse in search of interesting comments on cycling cards from the past. I interacted with these cards as a player before I got here, so I'll be switching intermittently between my player hat and my developer hat.

[Akroma's Blessing](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Akroma%27s+Blessing)](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing)

  

The simplest way to execute the cycling mechanic is to put it on a situational utility card. This lets you put the card in your deck without fearing that it will sit useless in your hand. When you don't have anything to use it on, you can toss the card for another random card and feel good that you protected yourself from something. The most obvious way to do this is to have things like [Scrap](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrap) and [Clear](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clear), but situational tricks are also natural places to put cycling. If my opponent is never going to try to block or target my creatures, I can just cycle my [Akroma's Blessing](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing) instead. However, Randy Buehler's comment shows that the card used to be much more expensive to cycle:

> RB 2/14: dropped cycling cost from 3 to W to make it constructed tempting

My first instinct when I looked at this card in October of 2002 was that [Akroma's Blessing](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing) was a situational trick I would be thrilled play in Limited. Then, it was part of Osyp Lebedowicz's [Pro Tour–Venice](https://web.archive.org/web/20090227000000/https://magic.wizards.com/Magic/Magazine/Article.aspx?x=sideboard/events/ptven03)–winning deck. Of course, when [Lightning Rift](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Rift) and [Astral Slide](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide) combine to form the one of the best strategies in a format it doesn't take much to make a cheap cycling card worth playing.

<table><tbody><tr><td><div><div><a href="https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Rift"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Lightning+Rift"></a></div></div></td><td><div><div><a href="https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Astral+Slide"><img alt="" src="https://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Astral+Slide"></a></div></div></td></tr></tbody></table>

What I didn't expect was that I would eventually consider playing this card in decks that had no cycling interactions at all. When *Scourge* came out, there was a mono-white control deck in *Onslaught* Block Constructed. Barring random quick knockouts, the mirror match revolved around [Eternal Dragon](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eternal+Dragon) and [Temple of the False God](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Temple+of+the+False+God) creating huge reserves of mana that fuelled enormous Decrees of Justice. There was a short period of time where that seemed like the best deck, and my response to that was to main-deck a few [Akroma's Blessing](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing)s. The plan was to cycle a big [Decree of Justice](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Decree+of+Justice) in my opponent's end step, then give all my tokens protection from white so that my opponent couldn't block them with another [Decree of Justice](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Decree+of+Justice). Thanks to the low cycling cost, I could include that plan in my main deck while sacrificing very little edge against beatdown decks.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Decree+of+Justice)](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Decree+of+Justice)

  

What I learned from that is how little a card that cycles for one mana needs to do to be playable. The cost during play of drawing a situational card that cycles for one mana is very low, and the value from randomly having it at the right time can far outweigh the costs. There are, however, real costs. When I commit to playing only 60 cards and include something like [Akroma's Blessing](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing) in my deck with the intention of cycling it often, I have less space for cards that actively further my deck's strategy. It is also more difficult to evaluate opening hands when making mulligan decisions if I know that I will be cycling an [Akroma's Blessing](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing) for a random card. If you're willing to give up the deck space and the knowledge, however, there's not a lot in the way of you playing these cards.

![](http://wizards.com//mtg/images/daily/ld/ld27_akromaSplash.jpg)  

Players very clearly demonstrated their willingness to play cards that cycle for one mana when they adopted the five *Onslaught* cycling lands. It amuses me somewhat that when you look at what cards people played in Constructed, you can't help but conclude that a land that comes into play tapped is much more powerful than giving all your creatures protection from a color at instant speed for three mana. The instant feels so much more viscerally impactful, but [Secluded Steppe](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Secluded+Steppe) has seen tons of Constructed play, while [Akroma's Blessing](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing) was a niche Block Constructed card. Which of those cards feels more powerful to you?

[Death Pulse](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Pulse)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Death+Pulse)](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Pulse)

[Death Pulse](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Pulse) is one of a number of cards in *Onslaught* that have cycling triggers that perform a small version of the card's normal effect. Other examples are [Primal Boost](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Boost) and [Solar Blast](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Solar+Blast). Ken Nagle often says that a card "reads like a poem" to mean that it is obviously an elegant and complete whole package, and these cards read like poems to me. However, [Death Pulse](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Death+Pulse) almost didn't read that nicely, as you can see from these comments from Randy Buehler:

> RB 1/17: should the base effect be -5/-5 so the cycling part is more cleanly a smaller version of the base effect. -6/-6?  
>  RB 1/25: team says yes, changed from banish to -4/-4

The card's main effect used to be "Destroy target nonblack creature." However the connection between "destroy target nonblack creature" and "target creature gets -1/-1 until end of turn" is rather hidden, and that the card didn't read very poetically that way. I'm very glad the *Onslaught* team made that change. If they hadn't, I probably would never have noticed the mechanical connection to the other cards built in this mold.

![](http://wizards.com//mtg/images/daily/ld/ld27_deathSplash.jpg)  

On a side note, it often frustrates me as a developer that many of the things we do are thought to be aspects of design by people out in the world. This is an example of the sort of change that I feel is often attributed incorrectly. Quite regularly, design hands off cards with notes in the file like "We want this slot to be a creature kill spell that has a cycling trigger for a small version of a creature kill spell." It's the developers' job to figure out how to best implement that, and we are not afraid to change words or mechanics to make sure that the designers' big ideas are expressed in the most fun way possible. Developers do so much more than change numbers and costs, and I often wish that we were publicly perceived less as soulless number crunching machines and more as staunch guardians of fun in **Magic**, competitive or otherwise.

[Undead Gladiator](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undead+Gladiator)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Undead+Gladiator)](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undead+Gladiator)

Now we hear from Randy again, with a guest appearance by prolific designer Mike Elliot.

> RB 12/17: MElliot feels this is out of flavor for black. I think it's fine. Other opinions?  
>  RB 1/25: Tuesday meeting decision was: this is fine in black

I was puzzled when I read this comment. On the surface, [Undead Gladiator](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undead+Gladiator) seems totally black. He's a little beater who isn't very tough, but keeps on coming back for more fighting every time he dies. That sounded very zombie-like to me, so I was generally satisfied with it.

Later that day, I tried thinking about it on the assumption that [Undead Gladiator](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undead+Gladiator) was infringing on another color's slice of the color pie, and attempted to identify which color it would be. The best I could come up with was blue. In actual competitive play, the card was best used as a card selection engine for black control decks. It was very strong in *Torment*-based mono-black control decks, since [Cabal Coffers](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cabal+Coffers) made tons of mana that could be used to filter through lots of cards all at once. [Undead Gladiator](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undead+Gladiator) also made guest appearances in black-white control decks. In both of those decks, it filled the role of card drawing and card selection, which are both traditionally blue things. When you can play [Undead Gladiator](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undead+Gladiator) to accomplish that goal, who needs to play blue? This was not a great argument, but it was the best I found.

After coming to that conclusion on my own, I spoke to Mark Rosewater, who both attended and remembered the Tuesday meeting Randy was talking about in that comment. Amusingly, Mike felt that our zombie friend was infringing on red's and white's space. Black's "back from the dead" effects were most likely to return things to play with a reanimation flavor. White and red, on the other hand, have effects that return things to players' hands from the graveyard. White gets to return creatures to its hand with a resurrection flavor, while red gets to cast spells over again with things like [Hammer of Bogardan](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hammer+of+Bogardan). Mike thought that if we made black cards that do that, we would hurt the definition of the colors, and he felt so strong about it that they had a whole Tuesday meeting about it.

I personally find Mike's concern kind of strange, but it's great for **Magic** that we have people looking at sets from many different perspectives. To me, if anything is horribly wrong with [Undead Gladiator](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undead+Gladiator), it's that the creature is totally incidental to the card when it is used in the most powerful way. It would certainly be worse in Constructed if it were an enchantment with exactly the same text box and no power and toughness, but it wouldn't play that differently in many situations. Given that, I would rather the card just scream at you that it is supposed to be a card selection engine and not try to trick you with the attached 3/1 creature.

![](http://wizards.com//mtg/images/daily/ld/ld27_undeadSplash.jpg)  

All this discussion about Tuesday meetings might have made you curious. The story behind that is that on Tuesdays we have a big meeting where everyone in **Magic** Ramp;D is expected to attend, and anyone outside Ramp;D who is involved in **Magic** is also welcome. The Tuesday meeting is occasionally used to pass on important corporate information, but most of the time we just talk about random **Magic**-related issues. When Ramp;D members go to big events like Prereleases or Pro Tours, we use that meeting to talk about what we got out of the trip. Sometimes, as this entry shows, one set, mechanic, or even card creates enough controversy within the department that we have an entire meeting about it. Apparently [Undead Gladiator](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Undead+Gladiator) was one such card.

We recently had a Tuesday meeting whose topic was spawned by controversy over one card. It would amuse greatly me if seven years from now another developer was writing Latest Developments, found that card's Multiverse entry, wondered why it was such a problem, and shared that conversation with the world.

[Street Wraith](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Street+Wraith)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Street+Wraith)](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Street+Wraith)

This is a strange little card. It's obviously an extremely inefficient creature, so the card's value clearly comes from the "free" cycling. However, in many ways paying life to cycle is a much heavier cost than paying one mana. The following Multiverse thread between Steve Warner, Devin Low, and Aaron Forsythe shows that that we were confused by our own card in early development:

> SW 6/22: I don't see this ever being in play, I see it lots in decks that will just cycle it immediately to cut down their deck or feed Oversold \[Cemetery\].  
>  DAL 7/3: Annoying that this is basically not a creature - just "0, Instant, Pay 2 life, draw a card."  
>  AF 7/12: Not sure what to think about this.

The question that [Street Wraith](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Street+Wraith) asks us is essentially how much we are willing to pay to play with a deck that effectively has less than 60 cards. The costs to do so are very similar to the [Akroma's Blessing](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroma%27s+Blessing) example; we have less information when we are evaluating opening hands that contain a [Street Wraith](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Street+Wraith), and we must pay 2 life to move to the next card. Zero mana is an appealing price, however, and the now commonly accepted knowledge that playing the minimum deck size is most powerful made this card read appealing to some people. We ended up deciding that it was usually wrong to play this card in decks that had no positive interactions with it, but that we thought that as an open-ended enabler it would make enough people happy that it was worth printing.

![](http://wizards.com//mtg/images/daily/ld/ld27_streetSplash.jpg)  

In the end, we were right on both sides. Some players experimented with playing it in lots of decks, but eventually that stopped as they decided that 2 life was too much to pay for the reduced deck size. Also, the card ended up being most powerful in decks that got much more value out of drawing a card than most decks do by abusing the dredge mechanic. Dredge-based decks in Standard used it along with [Magus of the Bazaar](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magus+of+the+Bazaar), [Merfolk Looter](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Looter), [Drowned Rusalka](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drowned+Rusalka), and other similar cards as ways to quickly get cards into the graveyard. The card gave even more value to dredge decks in Extended, Legacy, and Vintage because it is a black creature for [Ichorid](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ichorid) to consume! In the end, [Street Wraith](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Street+Wraith) did exactly what we thought it would. 

[Viscera Dragger](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viscera+Dragger)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Viscera+Dragger)](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viscera+Dragger)

  

Many people who are neither developers nor designers use Multiverse to track changes to card sets. The creative team uses it to track card concepts and art, and editors use it to track templating and typesetting changes. We tend not to show you comments by those people, but they do exist in the system and are frequently amusing. For example, here's one from **Magic** editor Del Laugel: 

> Del 3/13: Must remember not to do passes on Grixis right after lunch.

This was the most interesting comment about [Viscera Dragger](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viscera+Dragger). My guess is that it made it into the file early, people liked what it did, and it survived all the way to print. Hooray for [Viscera Dragger](https://web.archive.org/web/20090227000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viscera+Dragger)!

![](http://wizards.com//mtg/images/daily/ld/ld27_visceraSplash.jpg)  

Conclusion

I hope you enjoyed this walk into Multiverse. I joined Wizards very recently compared to some of my coworkers, and I enjoy seeing what designers and developers went through on the way to making cards that I only experienced as a player. I hope that you also enjoy the windows into the process that we can provide.

[![](http://wizards.com//mtg/images/daily/td/td27_kyotoCta.jpg)](https://web.archive.org/web/20090227000000/https://magic.wizards.com/magic/tcg/events.aspx?x=mtgcom/protour/kyoto09)  

The best **Magic** players in the world are converging in Japan this weekend as the Pro Tour travels to Kyoto. The tournament may even already have begun as you read this! I'll talk about the aftermath of that event next week, as well as a special Latest Developments field trip!

Last Week's Poll

<table><tbody><tr><td colspan="3"><b>How do you feel about <i>Shards of Alara</i> draft with <i>Conflux</i> compared to drafting only <i>Shards of Alara</i>?</b></td></tr><tr><td>I like <i>Shards of Alara</i> / <i>Conflux</i> draft more.</td><td>707</td><td>41.2%</td></tr><tr><td>I like them both equally.</td><td>171</td><td>10.0%</td></tr><tr><td>I like triple-Shards draft more.</td><td>171</td><td>10.0%</td></tr><tr><td>I have only drafted <i>Shards of Alara</i> with <i>Conflux</i>.</td><td>64</td><td>3.7%</td></tr><tr><td>I have only drafted <i>Shards of Alara</i> by itself.</td><td>252</td><td>14.7%</td></tr><tr><td>I have never drafted <i>Shards of Alara</i> block cards.</td><td>353</td><td>20.5%</td></tr><tr><td><b>Total</b></td><td><b>1718</b></td><td><b>100.0%</b></td></tr></tbody></table>

  
![](http://wizards.com//mtg/images/daily/ld/ld27_landCycling.jpg)  

We had an early issue with the poll that got fixed later, so not every vote was counted. Happily, we got a nice sample size anyway, and I was happy to see that most people thought that *Conflux* improved the format. I strongly believe that the addition of *Conflux*'s very strong common mana fixing makes drafting much more fun, and it seems that for whatever reason the majority opinion agrees with me. I'm glad you're all having fun.

This Week's Poll

<table><tbody><tr><td><div><b>How many Pro Tour Qualifier tournaments have you played in?</b>012 or 34, 5, or 67, 8, 9, or 1011 or more</div></td></tr></tbody></table>

[![](http://wizards.com//mtg/images/daily/ads/GS620.jpg)](http://wizards.custhelp.com/cgi-bin/wizards.cfg/php/enduser/std_adp.php?p_faqid=489)
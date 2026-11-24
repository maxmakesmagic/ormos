---
id: 77psk732
kind: article
lang: en
path: /en/articles/limitedinformation/2015/09-23-ingest-and-process
title: Ingest and Process
published: '2015-09-23'
column_slug: limitedinformation
column: Limited Information
authors:
- slug: marshall-sutcliffe-2971aa66
  name: Marshall Sutcliffe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
    lang_detected: en
    capture_id: 749640
    url: http://magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
    captured_at: '2016-08-29 02:31:54+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
    lang_detected: en
    capture_id: 749640
    url: http://magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
    captured_at: '2016-08-29 02:31:54+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
    lang_detected: en
    capture_id: 749640
    url: http://magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
    captured_at: '2016-08-29 02:31:54+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
    lang_detected: en
    capture_id: 749640
    url: http://magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
    captured_at: '2016-08-29 02:31:54+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 77psk732
  url: http://magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
  page_key: magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
  lang: en
  template: drupal
  captured_at: '2016-08-29 02:31:54+00'
  capture_id: 749640
  wayback_url: https://web.archive.org/web/20160829023154id_/http://magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 77psk732
  capture_id: 749640
  url: http://magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
  wayback_url: https://web.archive.org/web/20160829023154id_/http://magic.wizards.com/en/articles/archive/limited-information/ingest-and-process-2015-09-23
  captured_at: '2016-08-29 02:31:54+00'
  template: drupal
  sha256: 74c8537099e43098facfabfec23de089841969b3714b5b92515a28697b114863
render_recovery: []
---
If you haven't noticed yet, *Battle for Zendikar* has been fully previewed in the [Card Image Gallery](/en/articles/card-image-gallery/2015/09-18-battle-for-zendikar). Some of the big flashy rares had been revealed before this last major rush, but this is where the big picture really starts to come into focus for us Limited enthusiasts.

As you know, it's the commons and uncommons that help shape how a format plays out from draft to draft. Yeah, the rares and mythic rares are cool and everything, but if you want to win more drafts and have more fun doing it, do as I do and pay attention to the little guys.

I had a chance to do commentary for the [Community Cup](https://web.archive.org/web/20150923000000/http://magic.wizards.com/en/content/2015-magic-community-cup) this year at Wizards of the Coast headquarters in Renton, WA. If you haven't watched the event before, it's pretty crazy. They did a Stipulation Draft of the Legacy Cube on *Magic Online* where they had to draft cards based on things like which card would make the best title of a romantic comedy, which letters the card names started with, if the converted mana cost of the card was even or odd, and even one where they had to play every single card they drafted but also got as many [Vivid lands](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&name=+%5BVivid%5D) as they wanted to build the mana base from.

As you can tell, it was a crazy event that played out in a crazy way.

But.

We also got to watch the valiant Community team battle the staunch Wizards team at good old fashioned "real" *Magic* as well. They did a *Battle for Zendikar* Sealed Deck and Booster Draft on Saturday and Sunday respectively.

My complete terror at barely knowing any of the cards aside, it was super fun to get such an early look at the new set. I asked many of the competitors from both sides to give me their early take on the Limited environment, and one subject kept coming up over and over again. . . .

**On Ingesting and Processing**

One of the big questions I have for this format is figuring out the balance between ingesters and Processors. You know, the creatures that have the ingest ability, and the ones that take advantage of all that ingesting.

Like these:

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mist+Intruder)](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mist+Intruder)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mind+Raker)](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Raker)

I love value creatures. Heck, I just love value in general, but when it comes to Limited, creatures are where it's at, so I really love a good value creature. Most creatures like this have some sort of condition where they enter the battlefield and a trigger happens or whatever. These Processors (the ones that ultimately net you some value) are kind of the easy part of the equation. You see, when they enter the battlefield you can (usually) "process" some of your opponent's exiled cards and net yourself something sweet. These effects are the payoff.

Making your opponent discard cards, returning a creature to their hand, gaining 5 life, and even looting are some of the abilities that the Processors bring to the table. So these are desirable creatures with desirable effects. Great. The real question we have to be wondering about is how often we actually get the bonus.

To that end we have to look at the creatures with ingest, as well as any other cards that exile our opponent's cards.

Here is a pile of examples:

![](http://media.wizards.com/2015/images/daily/Eight-Exile-Cards.png)

We have a broad sampling of different ways to get some processing fodder online. It seems like the most consistent way to get this chain going is by using creatures with ingest. Ideally, these are on the low end of the mana spectrum so that you can have the exiled cards all ready to go when you want to cast your payoff Processor.

It seems that not all of these creatures are created equal, however. [Mist Intruder](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mist+Intruder), for example, seems to be on the weaker end of the spectrum.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mist+Intruder)](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mist+Intruder)

For further explanation, imagine that ingest just wasn't a thing. How excited would you be to play a card like [Mist Intruder](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mist+Intruder)? A quick check of the French Vanilla Test reveals a fairly unexciting card, at 1/2 with flying for two mana. In fact, I don't think I'd be too happy running that card in my deck in almost any format. Now let's compare it to say, [Benthic Infiltrator](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benthic+Infiltrator).

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Benthic+Infiltrator)](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benthic+Infiltrator)

A 1/4 creature that can't be blocked for three mana? Sign me up. Not that it would be some kind of amazing all-star card or anything, but a creature with these stats would make the main deck in most builds. Add to that the fact that it can get a card ingested essentially at will (where the [Mist Intruder](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mist+Intruder) will be blocked sometimes) and you have a winner. This is the type of card that I want to help enable my processing power.

Let's throw another card in the mix: [Culling Drone](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Culling+Drone). Here we have what looks like a reasonable middle ground between the two previous examples. At 2/2 for two mana, this card holds its own without really excelling either. It attacks and blocks well for its mana cost, but lacks evasion. Again, as an experiment, lets take ingest off the table. Would we prefer [Culling Drone](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Culling+Drone) or [Mist Intruder](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mist+Intruder)? What if we include [Benthic Infiltrator](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benthic+Infiltrator)?

[Benthic Infiltrator](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benthic+Infiltrator) is a step above either of the two-drops from our example. But the difference between [Mist Intruder](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mist+Intruder) and [Culling Drone](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Culling+Drone) is much smaller. The real question here comes down to how important ingesting is. [Mist Intruder](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mist+Intruder) has a higher likelihood of actually ingesting some cards from our opponent, but [Culling Drone](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Culling+Drone) may be better in circumstances where ingesting doesn't factor in.

This will be one of the big questions we have to answer early on in the format. After all, if we are playing not-amazing creatures justified by the fact that they enable our actually-amazing creatures, the payoff has to be pretty huge! Remember, it's not just the Processor and the value that it creates that's important—the effort you put into getting to that point matters.

**Incidental Ingesters**

Even if ingest creatures are the most direct way to getting some cards exiled, they aren't the only way. It's easy to overlook the fact that Processors don't care *how* the card got exiled, just that it did. That means that you can exile your opponent's cards not just from the top of their library, but also from the battlefield.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Touch+of+the+Void)](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Touch+of+the+Void)

For example, [Touch of the Void](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Touch+of+the+Void) is a rock-solid burn spell that can hit creatures or players—and if a creature dealt damage by it dies, the creature gets exiled. Not a bad way to get some processing going. I really appreciate that this spell is only three mana as well, as it means you'll often get to your Processors right on curve, and for full value.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scour+from+Existence)](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scour+from+Existence)

If you'd like to take a more direct route to getting a card ready for processing, look no further than Scour from Existence. I love the simple rules text on this card. The downside here of course is that it's a whopping seven mana to cast, which means you will not be hitting your average Processors for value at the earliest convenience very often.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Unnatural+Aggression)](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unnatural+Aggression)

Similar to [Touch of the Void](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Touch+of+the+Void) but a bit more difficult to set up, [Unnatural Aggression](https://web.archive.org/web/20150923000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unnatural+Aggression) is an instant-speed "fight" card that has the additional clause of exiling an opposing creature that died as a result of this aggressive act. Again, this is a card you'll play anyway, and it has a nice bonus tacked on to help get your process works going.

**Questions**

We always have questions at the beginning of a new format. That's part of why it's such an exciting time. One of the big questions I have right now revolves around whether I need to dedicate real deck slots to cards that enable my Processors, or if I'll have enough of that just by running the removal spells and good ingest creatures.

Is getting one or two cards exiled during the course of a game good enough to do what I want, or do I need to have a steady stream of ingested cards at the ready in order to maximize on my Processor value train?

I don't know the answer today, but I suspect it won't take me too long to figure it out.

Have a great time at your Prerelease and remember to experiment a bit and learn what you can! We all have questions, and there's only one sure-fire way to get the answers: Try them for ourselves.

Until next week!

[@Marshall\_LR](http://www.twitter.com/Marshall_LR)
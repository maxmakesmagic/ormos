---
id: v8rhaq0k
kind: article
lang: en
path: /en/articles/makingmagic/2013/07-08-working-your-core
title: Working Your Core
published: '2013-07-08'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
    lang_detected: en
    capture_id: 234759
    url: https://magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
    captured_at: '2024-05-18 03:43:36+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
    lang_detected: en
    capture_id: 234759
    url: https://magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
    captured_at: '2024-05-18 03:43:36+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
    lang_detected: en
    capture_id: 234759
    url: https://magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
    captured_at: '2024-05-18 03:43:36+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
    lang_detected: en
    capture_id: 234759
    url: https://magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
    captured_at: '2024-05-18 03:43:36+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: v8rhaq0k
  url: https://magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
  page_key: magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:43:36+00'
  capture_id: 234759
  wayback_url: https://web.archive.org/web/20240518034336id_/https://magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
- document_id: v8rhaq0k
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/255
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/255
  lang: en
  template: aspx
  captured_at: '2014-02-19 09:09:26+00'
  capture_id: 651813
  wayback_url: https://web.archive.org/web/20140219090926id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/255
- document_id: v8rhaq0k
  url: https://magic.wizards.com/en/articles/archive/making-magic/working-your-core-2013-07-08
  page_key: magic.wizards.com/en/articles/archive/making-magic/working-your-core-2013-07-08
  lang: en
  template: drupal
  captured_at: '2022-01-16 11:07:50+00'
  capture_id: 938342
  wayback_url: https://web.archive.org/web/20220116110750id_/https://magic.wizards.com/en/articles/archive/making-magic/working-your-core-2013-07-08
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: v8rhaq0k
  capture_id: 234759
  url: https://magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
  wayback_url: https://web.archive.org/web/20240518034336id_/https://magic.wizards.com/en/news/making-magic/working-your-core-2013-07-08
  captured_at: '2024-05-18 03:43:36+00'
  template: contentful
  sha256: 9bada2206ecb7c0629345868ab114a8f77ca7415dfc71c0146ed064e6303db17
render_recovery: []
---
Often, when a set comes out, I walk through the card set and tell stories about individual cards. But as I just told stories a few weeks ago ("Modern Stories, [Part 1](/en/articles/makingmagic/2013/06-17-modern-tales-part-1)" and "[Part 2](/en/articles/makingmagic/2013/06-24-modern-tales-part-2)"), I thought I'd do something a little different with my card walkthrough today. I'm going to choose a handful of cards and examine why they're designed the way they are. For each card I examine, I am going to talk about why a certain design decision was made. Hopefully, this will be an insight into how we design.

![](https://i.ormos.uk/92/6e/926e04dec00ee38831c275b0d05450529327fdb323e1bf0339cc177a06d246ee.jpg)

 

### "Why is this a sorcery?"

For starters, if you never read my article on why sorceries exist at all ("Can't all the spells just be instants?"), you might want to take a peek at [my article from Sorcery Week](/en/articles/makingmagic/2004/04-19-slow-and-steady) back in 2004. For those who don't want to read it, it boils down to "Sorceries are an important game-design tool." This card is a good example.

Originally, this mechanic was in blue. The most famous example was a card called [Ray of Command](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command).

![2528](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=2528)

 

Stealing was firmly in blue's part of the color pie from the beginning, with cards like Control **Magic** and [Steal Artifact](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steal+Artifact) showing up in Alpha. [Ray of Command](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command) came about as a means to steal a creature temporarily. It was made an instant to allow blue to use it as a defensive trick, where it would steal an attacker to use as a blocker. This allowed one spell to remove two threats (if you did it correctly, you could have the two creatures destroy one another in combat). Interestingly, though, this ability didn't first show up in blue, but rather in red, with this card in *Legends*:

 

![1568](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=1568)

 

In fact, if you look back at early **Magic**, red was clearly number two when it came to stealing things. While blue was flavored as manipulation, red was flavored more as trickery. This all came to a head numerous years later when R&D was attempting to balance the color pie. Red was at the low end while blue was at the high end. I brought up that red had a history of stealing things and that perhaps we should consider moving [Ray of Command](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command) into red. That way, we would separate permanent stealing from temporary stealing. Blue the manipulator was better at permanently stealing something while red, with its ability to manipulate emotions, could control creatures for a shorter duration of time.

 

There was just one problem. [Ray of Command](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command) was much more valuable on defense than offense. Yes, sometimes you would use it to attack, but more often you would sit back and use it to wreck the opponent during an attack. Red is the least defensive color (in the fact that it doesn't focus on being defensive—its direct damage can serve as defense in a pinch) so there was some debate about letting red have [Ray of Command](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Command). The solution, I argued, was easy. If we want red to use it offensively we just had to make it a sorcery. Then that would be the only way to use it.

And that is why [Act of Treason](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Act+of+Treason) is a sorcery.

![](https://i.ormos.uk/d1/e4/d1e4fd751366719d37312459f90272cae0b3ea049f8ad98752288ce902749548.jpg)

 

 

### "Why can't Blood Bairn sacrifice itself to itself?"

Once upon a time, all creatures capable of sacrificing a creature were able to sacrifice themselves. It's just the way we did things. Then, one day, developer [Erik Lauer](https://web.archive.org/web/20140430170951/http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer) asked the following question: "Is it confusing that creatures could sacrifice themselves for an effect that could never happen?"

We'll take Blood Bairn as an example. The creature sacrifice gives Blood Bairn +2/+2. But that effect will never happen if the creature sacrificed itself. What then is the advantage of allowing it? Well, it allows the creature to destroy itself if somehow that is beneficial (for example, someone is trying to steal it). We decided the minimal upside in corner cases wasn't worth the confusion.

Why is this confusion a problem? Because focus testing has shown us that if a card does something that players don't understand, they start to question if they understand what the card actually does. "Why can I sacrifice a creature if doing so would keep it from being able to get the bonus? Okay, I must have read it wrong."

So R&D drew a line. If the creature can sacrifice itself and generate an effect, then it gets the ability to sacrifice itself, but if that ability is negated by the creature no longer being there (which most often means a bonus to the creature), it now says "sacrifice another creature."

![](https://i.ormos.uk/15/93/15936ee5f2ea72bfd7471424798f19416ef64d075a2e5f7442425660727c72a3.jpg)

 

 

### "Is that middle ability red?"

The short answer is "it is now."

The longer answer has to do with something known as [Blogatog](http://markrosewater.tumblr.com/). For those who might never visit Tumblr, Blogatog is my daily blog where I answer questions from players. One of the common occurrences on my blog is that players will raise issues which I will then turn back on my audience. One such issue was a concern that red's share of the color pie wasn't as big as the other colors. So I asked if there were things not in red that they felt should be in red.

The players (I call them Question Marks) responded in great volume. One of the ideas that got tossed around was giving red access to more abilities but restricting the duration of how long they could use it. In other words, red could generate effects but only ones that could be used here and now. Red was always in the moment.

I liked this idea because it would allow us to stretch red colorpiewise (I swear that's a word—at least it is now) without having red step on the toes of other colors. Red would get its own take on these effects. The one that came to me first was card drawing. Old timers might remember the card [Elkin Bottle](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Bottle).

![2403](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=2403)

 

I was always a huge fan of [Elkin Bottle](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Bottle) and as I was walking through the idea of short term effects, [Elkin Bottle](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elkin+Bottle) sprung up in my head. Meanwhile, as fates would have it, elsewhere it the pit some R&D folk were trying to figure out how to make Chandra better in **Magic** 2014. This was Chandra's fourth version and they really wanted to make her better than her previous attempts. Chandra has never had a top-tier planeswalker card and she was the face of **Magic** 2014, after all.

 

I made a suggestion of the "use it or lose it" card-drawing ability. I explained how I was trying to help red and everyone liked the suggestion, so in it went.

Is this the last we're going to see of this effect in red? Nope.

![](https://i.ormos.uk/68/5a/685a9923e08d31d23a42bcda7a234c0862c4de75bec730861be7ae88b8787a85.jpg)

 

 

### "Why doesn't this target players?"

If you want the long version, I would go read [this](https://web.archive.org/web/20130708000000/https://magic.wizards.com/en/node/654896) and [this](https://web.archive.org/web/20130708000000/https://magic.wizards.com/en/node/644866). The short version is this: Whenever we design a card for the core set we try to figure out what the simplest, easiest-to-[grok](http://www.merriam-webster.com/dictionary/grok) version of the card is. Note that when we design for expert expansions, how the card fits into the larger environment of the set takes precedence.

A big part of doing this is questioning every single word on the card and asking what value that word adds. So, of course, when this card was being design for **Magic** 2010, the words "Target player" was put under a microscope.

There was much debate as to whether the words added complexity. The anti-"Target player" contingent argued that "Draw two cards" is just simpler and easier to understand than "Target player draws two cards." The pro-"Target player" contingent argued that just as players got that "CARDNAME deals 3 damage to target creature or player" made sense so too did the card draw. The player, they argued (if you didn't read the linked article, I'm on this side) would assume the card did what you would want it to do—direct damage to the opponent and card draw for you.

In the end, the simplicity argument won and the card was made with three words of rules text rather than five.

![](https://i.ormos.uk/63/dc/63dc3de527af663c47f3f91d69ed932bf5a47819631027161ec2411ff6e079e3.jpg)

 

 

### "Why can you only activate this once?"

[Rootwalla](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootwalla) first showed up in *Tempest* design. It was created by [Mike Elliott](https://web.archive.org/web/20130714131709/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mike%20Elliott) and was called Chuckwalla—which, by the way, happens to be [an actual type of lizard](http://en.wikipedia.org/wiki/Chuckwalla). Interesting side note—the card was supposed to be called Chuckwalla but the artist assumed it was a made-up creature and thus didn't draw a chuckwalla. The name was then changed to [Rootwalla](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootwalla).

Mike was playing around with the idea of a creature with a built-in [Giant Growth](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth). He restricted it to one use because the creature wasn't supposed to be a shade or a firebreather (i.e., something that could be used repeatedly) but rather as something that was meant as a one-shot ability. The card did a nice job of giving green an ability that made use of mana to change size in a way that didn't step on the toes of any other color. It worked so well that the "[Rootwalla](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rootwalla) ability" became an evergreen, although unnamed, ability.

One of the most important roles of the color pie is to help the colors each have a delineated feel. That means that R&D spends a lot of time splitting hairs and making subtle divisions between the colors. White can pump its toughness (although it doesn't to it often these days), blue can get +N/-N or -N/+N, black can pump its shades (pumping power and toughness), red can have firebreathing, and green gets the rootwalla ability.

![](https://i.ormos.uk/cf/23/cf233c853768e708ce776e5ef843e1b35ccae6929dbf051dc8a985806305e4ba.jpg)

 

 

### "Why does this card specify 'non-Demon?'"

The whole "non-Demon" thing started in *Dissension* on a card called [Rakdos the Defiler](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakdos+the+Defiler).

![107438](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=107438)

 

Rakdos originally sacrificed half of your permanents when he attacked and made your opponent sacrifice half of his or her permanents when he dealt combat damage to him or her. The problem was that you were always behind because you always had to sacrifice your half of the permanents before your opponent—and that only happened if you managed to deal combat damage to him or her (well, it was a 7/6 flier with trample, so it did happen most of the time).

 

My solution to tip the scales was to have you sacrifice half of your "non-Demon" permanents. I felt it was flavorful, encouraged you to have other Demons in your deck, and solved the problem by only having to add one word to the rules text. The rest of the design team liked it and the change was made.

![Reaper from the Abyss](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Reaper+from+the+Abyss)

 

Flash forward to *Innistrad*. During a playtest, I play a [Reaper from the Abyss](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+from+the+Abyss). I attacked each turn, my opponent chump blocked (he had a lot of fliers), and then I killed a second creature. This happens until he had only one creature left. I attack, he blocked, and then the following dialogue occurred:

 

> **Him:** Kill your demon.  
> **Me:** What?  
> **Him:** My guy died so you have to kill a creature.  
> **Me:** Yeah, but why would a demon kill himself?  
> **Him:** I don't know. He's depressed there's no one left to kill.  
> **Me:** That doesn't make any sense.  
> **Him:** I don't care. It's what the card says.

I then take out my pen, remembering Rakdos, and wrote "non-Demon" on it.

> **Him:** You can't do that.  
> **Me:** I redesigned him while the effect was on the stack.

Which brings us to Shadowborn Demon. Once we in R&D learn a trick, we tend to repeat it, and the "non-Demon" rider has been well received and has played well, so once again it got used.

![](https://i.ormos.uk/55/bc/55bcf51c2fec9a98e41b9f5371aefd0c3cf2a5262d18fe029069d75b797fdceb.jpg)

 

 

### "Why aren't the three abilities closer in power?"

The easiest way to think about the power level of activated abilities is to figure out what each would cost if you simply cast it. A 3/3 token can be done for ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). Putting three +1/+1 counters on a creature costs somewhere between ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) and ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). Gaining 3 life is worth ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). Why the discrepancy?

The answer is twofold. First, one of the thing that makes cards with some randomness fun is that there is some variance. With Primeval Bounty in play, each draw becomes a moment of focus. Having a range of what you can expect heightens this suspense. Note that all the effects are good, so you are seeing how much goodness you get rather than fearing something bad happening. (I talk about this concept a lot more in my article on randomness ("[Kind Acts of Randomness](/en/articles/makingmagic/2009/05-04-kind-acts-of-randomness)").

Second is the importance of aesthetics. For those who have never heard of aesthetics, it is a scientific study of how the brain perceives things. I've heard it also called the "science of beauty." (For more on it, I talk about aesthetics in my article "[Zen and the Art of Cycle Maintenance](/en/articles/makingmagic/2002/07-08-zen-and-the-art-of-cycle-maintenance).") The human brain finds certain patterns pleasing and, using aesthetics, a designer can make a card more pleasing to the players in ways they might not even be conscious of. A common technique is to reuse the same number multiple times.

The three abilities of Primeval Bounty all use the number three. They might not match in power but the fact that each ability (and it helps that there are exactly three) uses three in some way makes the card more pleasing, subconsciously. Note that a lack of aesthetics will have the opposite effect. This card is the perfect example:

![Griselbrand](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Griselbrand)

 

The fact that [Griselbrand](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Griselbrand) has a converted mana cost of eight despite all the 7s in his rules text upset a lot of players.

 

![](https://i.ormos.uk/4b/84/4b84bcf56350616140044cc4c5f5009bfafc12e97dc12d470002a68c385e8d46.jpg)

 

 

### Why does Ratchet Bomb say "equal to" rather than "equal to or less?"

[Ratchet Bomb](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ratchet+Bomb) is a redone version of a card called [Powder Keg](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Powder+Keg) from *Urza's Destiny*.

![Powder Keg](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Powder+Keg)

 

This means the real question is why did [Powder Keg](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Powder+Keg) say "equal to" rather than "equal to or less?" The answer is the "equal to" creates better game play. Let's examine each version to see what happens. We'll start with the "equal to or less" text.

 

What do you do each turn? You add a counter. Why? Because adding a counter is strictly superior to not adding one. It merely allows you to destroy yet another subset of cards. This means there's never any decision to whether or not to add a counter.

Now let's look at the "equal to" text. What do you do each turn? Well, that depends on how many counters are on the [Powder Keg](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Powder+Keg) and what other permanents are in play. With this version, there's no automatic answer. It also allows your opponent some play as well, because if he or she can goad you into adding a counter, he or she can then play any item with a permanent with a lower converted mana cost.

It's interesting to note when I designed [Powder Keg](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Powder+Keg) in *Urza's Destiny*, I had this exact fight with another designer, Mike Elliott. Luckily, the development team agreed that my version led to more interesting game play.

![](https://i.ormos.uk/df/81/df818d340b2febc9f27eaf261dbbbb76b8cef6c9290c4d1ded8bcb6df90c7653.jpg)

 

 

### Why doesn't this Sliver grant abilities to other Slivers?

This card is a tweak of the card [Metallic Sliver](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Metallic+Sliver) from *Tempest*.

![4617](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=4617)

 

That card, by the way, was supposed to be called Silver Sliver, but the art came back and the creature was more of a bronze color than silver, so we had to change the name.

 

Anyway, the reason neither [Metallic Sliver](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Metallic+Sliver) nor Sliver Construct grant abilities to other Slivers is that they are not actually Slivers. Rather, they are both constructs built to resemble Slivers. (The one in *Tempest* was built by Volrath, for those who remember their **Magic** villains of days gone by.) This allows them to fool the Slivers and take abilities, but they are incapable of sharing with the Sliver hive mind.

![](https://i.ormos.uk/a1/d9/a1d90a9a104513e48cd6b844f69cb3e46bbce770d5e6ccd12cb404d3ddbd5172.jpg)

 

 

### Is this supposed to be a white ability or a blue ability?

White is the color of delay. Putting a creature on top of its owner's library is a nice simple way to remove the creature for the game for a full turn (and sometimes longer). Blue is the color of bounce (i.e., returning something back to its owner's hand). Putting a creature on top of the library is basically a super-[Unsummon](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon). Both feel right, but R&D was unhappy with the overlap. It wasn't the kind of ability used often enough to have it occur in two different colors. Thus, the topic was brought to Card Crafting.

Card Crafting is a weekly meeting where core designers, developers, and creative folk gather to talk technical issues. The fate of "put target creature on top of its owner's library" is exactly the type of topic we talk about each week.

The pro-white camp argued that blue already has [Unsummon](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon). Why don't we split up the effects (blue gets return to hand while white gets return to top of library) so that we can create more nuance with the effect?

The pro-blue camp said that the ability felt awkward in white and that the delaying flavor was simply less apparent than the super-[Unsummon](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon) flavor. The pro-blue camp also argued that white has numerous other ways to delay creatures and didn't need the mechanical space.

We spent Card Crafting working it out and in the end decided that we didn't want to chop up the effects and that "put target creature on top of its owner's library" simply felt more blue than white.

![](https://i.ormos.uk/07/48/07486ee6e7db9acffbb47da38fb9d464baa424035484892a34c6befa7e321568.jpg)

 

 

### Why does this round down instead of up?

I designed this card during *Odyssey*. The block had a strong graveyard theme, which tends to naturally push design to include a milling theme, as it helps get cards into graveyards. I was trying to make a super-milling card but I also wanted to make sure that the spell didn't make it too easy to mill out the opponent.

For those who don't know this, I'm a bit of a puzzle fan. [Traumatize](https://web.archive.org/web/20130708000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Traumatize) was inspired by a riddle. A scientist invents a radical new invention, a super car. You put in your end destination and in ten second it takes you exactly halfway. Assuming you are trying to travel 3,000 miles, how long will it take you?

I'll let you think about it for a second before giving you the answer.

See the answer

\>> Click to Show

The answer is an infinite amount of time because you'll never get there. As you keep going half way, you never complete the journey. This riddle gave me the solution to my problem. If I mill half of your deck, the spell is never going to mill you out. It will keep getting the player closer but by itself it cannot win.

That's why I made it round down—so that this card would never be the one that mills out your opponent. Your opponent will always have to draw the last card him- or herself.

 

### You're My Only Hope

 

Before I sign off for today, I have a personal request to make of all of you. Please watch the video below.

![](https://magic.wizards.com/sites/all/themes/wiz_mtg/img/interface/video-place-holder.png)[.](http://www.youtube.com/v/x7khnFuv66A&hl=en&fs=1&rel=0)

I appreciate any help you can provide me in my quest. Thanks.

### "Why? Because We Like You"

That's all the time I have for today. I hope you enjoyed this peek into some of the reasons behind how the cards work the way they do. As always, I'd love to hear your feedback through my email, the thread of this column or any of my social media ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Google+](https://plus.google.com/107824009487778543249/posts)).

Join me next week for the six-hundredth week of Making **Magic**.

Until then, may you take the time to think about why your cards work as they do.

  

* * *

  

### Drive to Work #41 – *Mirage*, Part 1

Today I start talking about the design and development (but more the development) of the first set of the very first modern block, *Mirage*.

  

*   [**Episode 41**](https://media.ormos.uk/8c/96/8c969d53f2b27f2fe56621197fb866cf0e9a050103fc2938dc31ff3afad546bc.mp3) : *Mirage, Part 1* (11.1 MB)
*   [**Episode 40**](https://media.ormos.uk/77/e9/77e9da096f613a2bf7c176cb0e2f526df5c38b6d42aeeeb6b6e3657ab1142869.mp3) : *Wizards of the Coast* (14.9 MB)
*   [**Episode 39**](http://media.wizards.com/podcasts/magic/http://media.wizards.com/podcasts/magic/drivetowork39randomness.mp3) : *Randomness* (13.9 MB)
*   [**Episode 38**](https://media.ormos.uk/4e/30/4e30a2b683e1f9863a6270dfb4a8e52de89fb34f7721e3b976d1ccacbcb86020.mp3) : *Unglued 2* (10.6 MB)
*   [**Episode 37**](https://media.ormos.uk/4e/50/4e500a8dba06584dc74e40ee672465d0d2e57b1f18fdf3e9934035b2934edf83.mp3) : *Lessons I've Learned, Part 3* (10.5 MB)

### So You Want To Work At Wizards

Many years ago I started posting job searches at the end of my column. You all liked the chance to see potential jobs at Wizards. We liked that it proved to be a good way to find qualified candidates, so I've chosen to keep doing them.

Today, we're looking for a senior coordinator for **Magic: The Gathering**. The requirements are:

*   Bachelors in Graphic Design or other visual communication field (or equivalent experience) highly desired.
*   Experience with Word, Excel preferred.
*   Experience with InDesign preferred.
*   Familiar with Adobe CS5 preferred (minimally Photoshop CS4)
*   Familiar with FileMaker Pro preferred.

And asks for the following knowledge, skills, and abilities:

*   Must be detail-oriented
*   Strong communication skills required
*   Print production knowledge highly desired
*   Able to adapt to quickly changing environment
*   Ability to work effectively with diverse groups of people
*   Ability to multitask
*   Participate in gaming environments

If you think that sounds like you, see the full job listing [here](https://web.archive.org/web/20130708000000/http://company.wizards.com/about/careers/sr-coordinator-art-administration-job-renton-wa-us?careers-view=1).
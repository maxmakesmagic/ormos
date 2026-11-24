---
id: rskkyn0e
kind: article
lang: en
path: /en/articles/latestdevelopments/2008/08-15-when-stone-rain-married-dark-banishing
title: When Stone Rain Married Dark Banishing
published: '2008-08-15'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: devinlow
  name: Devin Low
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
    lang_detected: en
    capture_id: 736060
    url: https://magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
    captured_at: '2022-01-16 22:50:06+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
    lang_detected: en
    capture_id: 736060
    url: https://magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
    captured_at: '2022-01-16 22:50:06+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
    lang_detected: en
    capture_id: 736060
    url: https://magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
    captured_at: '2022-01-16 22:50:06+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
    lang_detected: en
    capture_id: 736060
    url: https://magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
    captured_at: '2022-01-16 22:50:06+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: rskkyn0e
  url: https://magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
  page_key: magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
  lang: en
  template: drupal
  captured_at: '2022-01-16 22:50:06+00'
  capture_id: 736060
  wayback_url: https://web.archive.org/web/20220116225006id_/https://magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: rskkyn0e
  capture_id: 736060
  url: https://magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
  wayback_url: https://web.archive.org/web/20220116225006id_/https://magic.wizards.com/en/articles/archive/latest-developments/when-stone-rain-married-dark-banishing-2008-08-15
  captured_at: '2022-01-16 22:50:06+00'
  template: drupal
  sha256: 4f403d5f4f4b940a9c2a6ddc95600ff68dc135718a96c4125767bac53e876e0b
render_recovery: []
---
A theoretical card had been tossed around several design files near *Eventide*, though the card never made it to print in any of the sets:

> The Fountain  
>  1W  
>  Enchantment  
>  At the beginning of your upkeep, you may gain 1 life.

During *Eventide* development, one designer noted that *Eventide*'s 2W [Recumbent Bliss](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recumbent+Bliss) basically combined [Pacifism](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism) and "The Fountain" into one card. Since each of those cards cost 1W, the designer asked, and [Recumbent Bliss](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recumbent+Bliss) was essentially the sum of those two cards, shouldn't [Recumbent Bliss](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recumbent+Bliss) cost 2WW? Why was it so cheap?

![Pacifism + The Fountain = Recumbent Bliss](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation1.jpg "Pacifism + The Fountain = Recumbent Bliss")

1W + 1W = 2W?

This simple question set off vigorous debates in the R&D Pit and in our Multiverse database. If a new card combines the effects of an old card with mana cost A and an old card with mana cost B onto one card, should the mana cost of the new card be A+B? Or should the cost of the combined card be less than A+B? Or should it be more?

Proponents of each side had examples to back them up. And this question potentially goes far beyond [Recumbent Bliss](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recumbent+Bliss), to affect many other cards in the past and future. So what's the right answer? How do you cost "A+B" cards?

The answer is that you can't just follow a math formula. Sometimes the new card combining two old cards should cost exactly the sum of the old costs: A+B. Sometimes the new card needs to cost more, and sometimes it should cost less. There are two great ways to demonstrate this principle. First, let's look at some examples of combination cards from history that cost A+B, more than A+B, and less than A+B.

### Some Should Cost Exactly A+B

[**Rain of Salt**](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=+Rain+of+Salt+) 

![Stone Rain + Stone Rain = Rain of Salt](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation2.jpg "Stone Rain + Stone Rain = Rain of Salt")

2R + 2R = 4RR

The *Urza's Saga* uncommon [Rain of Salt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Salt) is a very elegant design. It's quite literally "double [Stone Rain](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain)" in every possible way. Is [Rain of Salt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Salt) better or worse a card than the original [Stone Rain](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain)?

The answer is that [Rain of Salt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Salt) is neither *strictly* better nor *strictly* worse. At the moment you play [Rain of Salt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Salt), it certainly has more raw power in the effect. But the ability to play [Stone Rain](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) on turn three—or turn two off of a [Birds of Paradise](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise) or [Llanowar Elves](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves)—can potentially be a lot more disruptive to your opponent than waiting until turn five or six to play [Rain of Salt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Salt).

And in fact, the best way to use [Rain of Salt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Salt) was often to start out with a few [Stone Rain](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain)s in the middle turns, then really bomb the opponent back to the stone age with [Rain of Salt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Salt) a couple of turns later.

[Rain of Salt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rain+of+Salt) is well-costed at 4RR, standing as a good example for the camp that says "Always cost a combination card at A+B."

**[Plague Spores](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Spores)** 

![Stone Rain + Dark Banishing = Plague Spores](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation3.jpg "Stone Rain + Dark Banishing = Plague Spores")

2R + 2B = 4BR

[Plague Spores](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Spores) is a classic, powerful gold common from *Invasion* that cost exactly 4BR . *Invasion* block contained a lot of elegant multicolored combination cards whose cost was chosen in exactly this way.

[Plague Spores](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Spores) combines [Stone Rain](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) and [Dark Banishing](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing) in every possible way. It's a powerful common, marrying land destruction, creature removal, and card advantage in a single package. But it's not so overpowering that it ruins the flow of a game. The net result is well costed at 4BR.

One thing to note here is that there are multiple ways to combine a pair of cards. [Stone Rain](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stone+Rain) is a sorcery and [Dark Banishing](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing) is an instant, so which card type is the combination of the two supposed to be? Is the no-regeneration clause of [Dark Banishing](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dark+Banishing) supposed to spread to cover both the land destruction and the creature destruction effects, or apply only to creature kill half?

There is a lot of latitude in such questions for the designers and developers. But the school of thought that says "always cost the combination at A+B" does not take into account the power level changes coming from these choices. [Plague Spores](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Spores) would have been a lot more powerful as an instant, but the "always cost the combination at A+B" advocates lock themselves into costing it at 4BR regardless of its card type.

**[Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake)** 

![Grizzly Bears + Counterspell = Mystic Snake](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation4.jpg "Grizzly Bears + Counterspell = Mystic Snake")

1G + UU = 1GUU

Back in *Apocalypse*, UU [Counterspell](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell) was the status quo. [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) is the exact combination of [Grizzly Bears](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) and [Counterspell](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell), so it was costed at 1GUU. There's something beautiful in that, and the mana cost being exactly equal to 1G + UU definitely adds to [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake)'s elegant design. [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) was popular and played on all levels in the days of *Apocalypse*, and 1GUU turned out to be a great cost for gameplay.

[Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) was so beloved, in fact, that we brought the mystical little buddy back among the *Time Spiral* "timeshifted" cards to be in Standard a second time. [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake)'s cost also feels very right by modern standards, and it still plays well today. The 1GUU cost has stood the test of time. It seems like that would bolster the case for "always cost the combination at A+B," but in fact, it introduces a flaw in the strictly additive philosophy.

After all, when *Time Spiral* brought back [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake), *Time Spiral* also included [Cancel](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel). And [Ashcoat Bear](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcoat+Bear). [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) is just as much the perfect combination of [Ashcoat Bear](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcoat+Bear) and [Cancel](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) as it is the perfect combination of [Grizzly Bears](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) and [Counterspell](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell). If anything, [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) is actually a little closer to [Ashcoat Bear](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcoat+Bear) and [Cancel](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel), since [Ashcoat Bear](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcoat+Bear) is a 2/2 with flash just like [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) is.

If the way to get an accurate cost for [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) comes from adding the mana costs of [Grizzly Bears](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) and [Counterspell](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell), then the way to get an accurate cost for [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake) should be to add the mana costs of [Ashcoat Bear](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ashcoat+Bear) and [Cancel](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) too. But [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake)'s mana cost can't equal both of those sums, because those sums are different.

![Ashcoat Bear + Cancel = Mystic Snake](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation5.jpg "Ashcoat Bear + Cancel = Mystic Snake")

1G + 1UU = 2GUU?

Even though 1UU is now the fair cost for "counter target spell," not UU, [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake)'s 1GUU mana cost feels as good and right now as it did in *Apocalypse*.

### Some Should Cost Less than A+B

**[Prophetic Bolt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophetic+Bolt)** 

[Prophetic Bolt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophetic+Bolt) is another classic enemy-colored gold card from *Apocalypse*. [Prophetic Bolt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophetic+Bolt) was played in tournaments almost as much as [Mystic Snake](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Snake), and often played in the same decks as that slithery, magical reptile, but [Prophetic Bolt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophetic+Bolt) never dominated tournament formats or was oppressive on them. That indicates that [Prophetic Bolt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophetic+Bolt) was costed pretty well.

[Prophetic Bolt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophetic+Bolt) is exactly, *exactly* the combination of [Lightning Blast](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Blast) and [Impulse](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Impulse). Let's see how the mana cost adds up

![Lightning Blast + Impulse = Prophetic Bolt](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation6.jpg "Lightning Blast + Impulse = Prophetic Bolt")

3R + 1U = 4UR

In this case, adding up the mana cost of [Prophetic Bolt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophetic+Bolt)'s components would indicate that it should cost 4UR. But instead the *Apocalypse* developers wisely chose to chop a mana off of [Prophetic Bolt](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prophetic+Bolt) to put in the perfect place. They were right to chop the mana off, and you can see here how it would have been a mistake to follow a strict formula of "always cost the combination at A+B."

**[Indrik Stomphowler](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Indrik+Stomphowler)** 

What does a vanilla green 4/4 cost? In the *Legends* expansion, [Durkwood Boars](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Durkwood+Boars) would grunt that the answer is 4G. Triangulating from cards in more recent sets like [Spined Wurm](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spined+Wurm), [Order of the Sacred Bell](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Order+of+the+Sacred+Bell), and a variety of 2GG 4/4s with abilities, the modern answer for what a vanilla green 4/4 costs is somewhere between 4G, 2GG, and 3G, not landing squarely on any of those exact mana costs. Call it 31/2G.

*Dissension* uncommon [Indrik Stomphowler](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Indrik+Stomphowler) is exactly the combination of a vanilla green 4/4 with a [Naturalize](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Naturalize) attached. The big Beast gets played a ton on *Magic Online* and in casual circles, and it even popped its head into tournament Constructed in events like [Pro Tour–Honolulu](https://web.archive.org/web/20080815000000/http://archive.wizards.com/Magic/Magazine/Events.aspx?x=mtgevent/pthon06/welcome). Again, the fact that it gets played so much, is loved so much, and yet is not oppressive or unbalancing indicates that its cost is pretty well chosen.

So how does [Indrik Stomphowler](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Indrik+Stomphowler)'s cost compare to the A+B costing method?

![Durkwood Boars + Naturalize = Indrik Stomphowler](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation7.jpg "Durkwood Boars + Naturalize = Indrik Stomphowler")

31/2G + 1G = 41/2GG?

Wow, that is quite a difference. The additive method says he should cost 41/2GG, but the actual cost played great at 4G. Again, this demonstrates the "Always cost the combination at A+B" philosophy breaking down.

### Some Should Cost More than A+B

**[Barter in Blood](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barter+in+Blood)** 

Nicolai Herzog used this *Mirrodin* uncommon to win two Pro Tour championships in back to back Limited Pro Tours. As long as you don't play out too many creatures yourself, killing two opposing creatures with one card for just four mana can be absolutely devastating. [Barter in Blood](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barter+in+Blood) was also played on the fringe level of tournament Constructed during some parts of its Standard life cycle. And I've seen casual players imprint [Barter in Blood](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barter+in+Blood) on [Panoptic Mirror](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Panoptic+Mirror) as a nasty recurring board sweeper. All in all, [Barter in Blood](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barter+in+Blood) is well-costed.

[Barter in Blood](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barter+in+Blood) received its name because it is literally the combination of two [Innocent Blood](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Innocent+Blood)s on one card. So let's compare it to the "Always cost the combination at A+B" method:

![Innocent Blood + Innocent Blood = Barter in Blood](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation8.jpg "Innocent Blood + Innocent Blood = Barter in Blood")

B+B=BB?

[Barter in Blood](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barter+in+Blood) performs all its roles so perfectly as a powerful, fun 2BB card that costing it at BB would have been crazy. I'm definitely glad we didn't use an "always cost the combination at A+B" philosophy on this card.

**[Lightning Blast](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Blast)** 

[Lightning Blast](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Blast) is just two [Shock](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock)s tacked together. If you assume all the damage has to go to the same target, then the deal 4 is actually significantly weaker than two consecutive [Shock](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock)s. Let's try the additive costing method for combination cards:

![Shock + Shock = Lightning Blast](http://archive.wizards.com/magic/images/mtgcom/fcpics/latest/dl50_equation9.jpg "Shock + Shock = Lightning Blast")

R+R=RR?

RR is clearly insane for an instant 4 damage burn spell with no rider or clauses. The additive costing method would also indicate that a "deal 6 damage" instant should cost RRR, and that a "deal 8 damage" instant should cost RRRR. But all of these cards are way too powerful. Additive costing is a big failure here.

### Why Doesn't Additive Costing Work?

There are three main reasons:

**1) Additive costing doesn't take number of cards used into account.**

[Shock](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock)'s mana cost is R, but it's real cost is "R *and a card from your hand.*" That's why RRR and a card from your hand isn't a fair cost to buy 6 damage to target creature or player. The fair cost for 6 damage to target creature or player is RRR and three cards from your hand (three [Shock](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock)s). Or 6R and a single [Blaze](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blaze) from your hand. Or RRRR and two cards from your hand if you use a [Shock](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) and a [Flame Javelin](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Javelin).

There are a lot of possible answers for how much mana and how many cards from your hand are a fair cost to deal 6 points of burn. But "RRR and a single card" is not one of them.

**2) Additive costing assumes that spending A+B is as easy spending A, then spending B.**

If 2GGGG is a fair cost for [Cloudthresher](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloudthresher), is 4GGGGGGGG a fair cost for a card that makes two [Cloudthresher](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloudthresher)s?

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="Cloudthresher" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Cloudthresher&amp;options="></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Cloudthresher" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Cloudthresher&amp;options="></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

Of course not. Twelve mana is way too expensive for two [Cloudthresher](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloudthresher)s, even though the burly Elemental duo would be quite powerful on the turn you somehow scrounged up twelve mana to summon them. That's because getting to twelve mana in a single turn is incredibly hard, far harder than spending six mana on one [Cloudthresher](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cloudthresher) on one turn, then spending another six mana on the following turn.

**3) Choosing mana costs isn't just a science. It's an art.**

If exact, strict rules could be put down for determining the mana costs of *Magic* cards, then computers could do the job instead of human developers. But creating strict rules and formulas for mana cost would inevitably make the game less fun. Because our goal is not to put each *Magic* card at some "exactly, scientifically fair" mana cost. Our goal is to weave a series of cards together to create a series of unique, interesting, and most of all *fun* play environments.

![Culling_Scales](https://i.ormos.uk/5f/79/5f79575961f1282af7c3954c230ba310a393dbc49abcf973d8fc69840d14ca25.jpg)If the mana costs were all "exactly, scientifically fair" year after year, and costed by computers, then there would be very little sense of discovery in *Magic*. There would be no more poring over set lists, trying to find the best combinations that your friends had not yet discovered. Because you would know before you started that all of the cards were "exactly, scientifically fair" and that none of the cards was more powerful than any of the others.

A lot of *Magic* cards *could* cost anywhere in a whole range of costs. Could [Recumbent Bliss](https://web.archive.org/web/20080815000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recumbent+Bliss) have cost 4W? Yes. Could it have cost 3W or WWW or 1WW or 2W or WW or 1W or theoretically even W? Sure. And many of the other hundreds of cards in Standard could have had different costs too. But we believe that the hundreds of costs we ended up selecting and printing have the best chance of making *Magic* as fun as it can be.

Choosing *Magic* cards' mana costs isn't just a formulaic procedure of mindlessly obeying costing equations. Choosing cards' mana costs is an art. And if we do our job right, it's one that lets you practice an even more important art: choosing the cards you want to build and play to make your decks your own in the most intriguing, enthralling, textured, and layered environments we can create.

### Last Week's Poll

<table><tbody><tr><td colspan="3"><b>Before you saw the answers, how many cards did you guess correctly? </b></td>&#10;		</tr><tr><td>6</td>&#10;			<td>597</td>&#10;			<td>8.4%</td>&#10;		</tr><tr><td>5</td>&#10;			<td>1333</td>&#10;			<td>18.7%</td>&#10;		</tr><tr><td>4</td>&#10;			<td>1264</td>&#10;			<td>17.7%</td>&#10;		</tr><tr><td>3</td>&#10;			<td>930</td>&#10;			<td>13.0%</td>&#10;		</tr><tr><td>2</td>&#10;			<td>590</td>&#10;			<td>8.3%</td>&#10;		</tr><tr><td>1</td>&#10;			<td>310</td>&#10;			<td>4.3%</td>&#10;		</tr><tr><td>0</td>&#10;			<td>105</td>&#10;			<td>1.5%</td>&#10;		</tr><tr><td>I didn't guess- I just clicked and revealed them.</td>&#10;			<td>2000</td>&#10;			<td>28.1%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>7129</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

About 72% of respondents played along [last week](https://web.archive.org/web/20080815000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/dl49) and guessed before they clicked the reveal buttons. The other 28% just clicked through, which makes a lot of sense too. Sometimes it's fun to do some mental detective work, and sometimes you just want to read an article. Of the people who responded, getting 5 out of 6 right or getting 4 out of 6 right were the most common results. What's funny is that the people who said they got 5 out of 6 right may have had their one wrong guess on totally different cards from one another. Though I think the sixth mystery is the hardest to get.
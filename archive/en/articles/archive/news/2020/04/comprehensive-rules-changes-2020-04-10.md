
---
[Link to Wayback Machine](https://web.archive.org/web/20200410153257/https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2020-04-10)

[_metadata_:author]:- "Eli Shiffrin"
[_metadata_:description]:- "103.1b It all begins with shuffling your deck to become your library. Except it doesn't. Before that, you have to deal with your sideboard and any cards in your deck that don't begin the game in your library. This new rule covers how companions fit into that: reveal them after setting aside your sideboard (if you have one) but before setting aside your commander (if you have one)."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1497112"
[_metadata_:publish_date]:- "2020-04-10"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Comprehensive Rules Changes"
[_metadata_:wayback_capture_timestamp]:- "2020-04-10 15:32:57"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20200410153257id_/https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2020-04-10"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/news/comprehensive-rules-changes-2020-04-10"
---


Comprehensive Rules Changes
===========================



 Posted in **News**
 on April 10, 2020 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_Eli-Shiffrin.jpg)
By Eli Shiffrin











103.1b
------


It all begins with shuffling your deck to become your library. Except it doesn't. Before that, you have to deal with your sideboard and any cards in your deck that don't begin the game in your library. This new rule covers how companions fit into that: reveal them after setting aside your sideboard (if you have one) but before setting aside your commander (if you have one).


120.4
-----


The rules on dealing damage have a new first step, making the damage-dealing process a four-step sequence instead of three. The new first step handles reportioning "excess damage" before looking at any replacement effects. This parallels how trample works, so if you think of this as "spell trample," you'll get it right. Well, if you already know how trample works with damage doubling and damage prevention, anyway.


As an aside, the reason this isn't simply trample is so that abilities can use it, too, and because it gives it some flexibility to work very slightly different under the hood when needed.


122.1b
------


Keyword counters! We've got a list here that defines what keywords get to be keyword counters. Sorry fuse.


122.8
-----


The Ozolith pioneers a new template: When we know that something's leaving the battlefield and therefore its counters cease to be, we can still reference putting "those counters" on something else. Those counters actually went poof, but this rule covers the gap to let us use words that encourage you to use that same pile of beads or dice or coins or kittens to represent them. It's much more user-friendly than the functionally identical words of "for each kind of counter that was on it, put the same number of that kind of counter on The Ozolith" or something.


201.5
-----


This rule won't answer the question of "Godzilla or Gojira?" but it does answer "Godzilla or Zilortha?" When a card has a second name in the little box below the normal title bar, that second name is its real name. The name in the title bar has no rules meaning and carries no weight.


205.3
-----


Here's where we have a bunch of lists of subtypes! Welcome to the creature subtype party, Shark and Otter. No, don't eat the Otter! Bad Shark, bad! Mooooving right along, Lukka joins the list of planeswalker subtypes.


607.5
-----


706.7a was a rule that talked about linked abilities where no choice was made for the first ability in the link. But wait, you might say, 706 is not the linked ability rules, those are 607. Actually, you probably don't say that because no one knows what rule numbers belong to which rules off the top of their head. This rule predates their current rule numbers, and it even predates linked abilities as a rules concept. It's always been something copy effects could get themselves into trouble with, so it lived with copy effects to begin with. However, it's really describing a truth of linked abilities, not just copy effects, so I've moved it up to the linked abilities section and made it slightly more generic.


613
---


For many players, the term "layers" fills their heart with dread, lurking in the shadows as a bizarre and arcane rules concept. In reality, the system of layers exists so that most of the time your best guess to how two effects interact will be correct, and we accept some weirdos like [Magus of the Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Magus+of+the+Moon) and [Humility](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humility). The rules for layers have changed remarkably little since they were introduced twenty-ish years ago, but here we go! There are four, FOUR changes!


613.1a
------


The very first layer is no longer simply copy effects. It's now *copiable* rules and effects. The new rule 613.2 expands on this: it includes traditional copy effects and mutate modifications in timestamp order (and theoretically also host and augment modifications if we allow silver-bordered cards into this discussion), followed by face-down status-modifying values. Mutate aside, this has always been true, and it's finally clear and explicit in the layers section of the rules.


613.1f
------


Layer six, the "abilities" layer, has been modified to include keyword counters.


613.3d
------


The sublayers for layer seven's power-and-toughness-modifying effects were 613.3, but they all got bumped to 613.4 with the addition of 613.2 for layer one's sublayers. This one rule, however, got chopped. It handled power-and-toughness counters separately from abilities that gave power-and-toughness pluses or minuses. Now there's just one sublayer of layer seven where we handle all plus and minus, whether they come from abilities or from counters. This changes exactly one interaction: a [Phyrexian Ingester](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Ingester) eating a Skullbriar that has a +1/+1 counter on it. This uses dependency (speaking of rules bugbears . . .) rather than layer ordering so that [Phyrexian Ingester](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Ingester) gets +2/+2 now rather than +1/+1.


613.7c
------


When dependency isn't involved (shoo, dependency, back under the bed), effects apply within each layer by timestamp order. But what's the timestamp on counters? Here is where we define this. The timestamp of a counter is the latest time that a counter of that kind was put on an object. It doesn't change if a counter is removed, and all counters of the same kind have the same timestamp because counters are interchangeable.


613.7k
------


What happens if two things want to get a timestamp at the same time? Previously, the active player chose relative timestamps for all the things. That gets a little weird because everything else in *Magic* uses active-nonactive player ordering, so as long as we're changing everything else about layers, this is changing, too.


702.138
-------


Here's the friendliest bunch of rules in the whole 241-page document: companion rules! Who's a good Demon Kraken? It's you! Yes, you are!


702.139 & 721
-------------


And here we have the rules for mutate and merging with permanents. I set up the merging section to be very flexible and freeform to allow for future shenanigans. Will this become hot new tech or a weirdo that lives in one set? Time will tell.


704.5g
------


A creature with damage marked on it greater than or equal to its toughness is destroyed. We all know that. But thanks to Zilortha, Strength Incarnate, there's an ambiguity: is 0 damage enough damage? We don't allow "0 damage" to mean anything elsewhere, so that's following suit here, and a creature must have damage marked on it at all for this state-based action to be processed.


903.11
------


In a Commander game, many playgroups use the rule that you can't bring cards in from outside the game, so anything that says you can get a card from outside the game just does nothing. In case your playgroup waives that rule and lets cards like [Burning Wish](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Wish) search a mini sideboard or something, you should still not be able to violate your color identity and you should still not be able to bring a duplicate card into the game. This rule establishes those as firmer rules than mere suggestions while also making sure that if you have a companion, it'll follow the rules. I mean, your playgroup can still decide to ignore this rule if you all want. I'm the rules manager, not the card police.




---

[Introduction](https://magic.wizards.com/en/articles/archive/news/ikoria-lair-behemoths-update-bulletin-2020-04-10)  

Comprehensive Rules Changes  
[Oracle Changes](https://magic.wizards.com/en/articles/archive/news/oracle-changes-2020-04-10)








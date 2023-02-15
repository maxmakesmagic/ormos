
---
[Link to Wayback Machine](https://web.archive.org/web/20160210072132/http://magic.wizards.com/en/articles/archive/layer-system-2009-11-05)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Layers are one of the more difficult parts of the Comprehensive Rules to learn (613). They are often a bane to both players and beginning judges, but why do we have them? What do they do?"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "936321"
[_metadata_:publish_date]:- "2009-11-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Layer System"
[_metadata_:wayback_capture_timestamp]:- "2016-02-10 07:21:32"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160210072132id_/http://magic.wizards.com/en/articles/archive/layer-system-2009-11-05"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/layer-system-2009-11-05"
---


The Layer System
================



 Posted in [ARTICLES](/en/articles)
 on November 5, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











Layers are one of the more difficult parts of the [Comprehensive Rules](http://magic.wizards.com/content/comprehensive-rules) to learn (613). They are often a bane to both players and beginning judges, but why do we have them? What do they do?


Magic is a very complex game, with literally thousands of cards that have continuous effects. When these continuous effects start to pile up, we need to know how they interact. The rules for layers give us a structure to make sure that when the same three cards end up in play at a tournament in Japan, the result is the same as when it happens in Italy, the U.S., and Brazil.


The interaction between [Bad Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bad+Moon) and [Darkest Hour](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darkest+Hour) is an example of both why layers are needed. If we only applied them in the order they came onto the battlefield the result can be very counterintuitive. For example, applying [Bad Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bad+Moon) first then [Darkest Hour](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darkest+Hour) would lead to only creatures that were already black getting +1/+1. The layers are ordered so we know we have to apply a color changing abilities before we can apply power//toughness changing abilities.


The layer system may seem difficult, but once you memorize the order and a few important rules, it will become far less daunting than you may have previously thought. We will first review what the layers are, give some example cards for each layer, go over some additional layer rules, quickly review the **M10** changes for layers, move into some memorization techniques, and lastly work through some example problems.


Before we can continue, we will need to define a few terms commonly used when talking about layers.


### Characteristic Defining Ability


A Characteristic Defining Ability (CDA) is an ability that defines a characteristic of a card or token. There are 3 specific rules that distinguish a CDA from other abilities.


1. A CDA can only define a characteristic of either the card or token it comes from.
2. A CDA can not be triggered, activated, or conditional.
3. A CDA must define a characteristic. Usually color, power and/or toughness, or sub-type.

### Timestamp Order


Each permanent receives a timestamp when it enters the battlefield. Each spell or ability receives a timestamp when it resolves. To apply multiple continuous effects (which apply in the same layer) in timestamp order, apply the effect with the oldest timestamp first, then apply the one with the next oldest, and so on and so forth.


### Dependency


Sometimes an effect can depend upon another effect. An effect can be said to depend upon another effect if:


* Both effects are applied in the same layer (or sub-layer).
* Applying one effect would change the text or existence of the other effect, how it applies, or what it applies to
* Neither effect is from a CDA.

If an effect is dependent on another effect, they will be applied in timestamp order unless the independent effect would be applied after the dependent one. If this is the case, the dependent effect is held until after the independent effect has been applied and then it is applied.


### What are the 7 layers & 5 sub-layers?




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| # |  | **Layer Name** | **Description** | **Examples** |
| **1** |  | Copy Effects | Any effect which would copy values onto the object you’re evaluating. If you can spot the word ‘Copy’ in the ability/spell text, then it’s fairly safe to say that the effect needs to live here. | * [Copy Enchantment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Copy+Enchantment)
* [Mirrorweave](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirrorweave)
 |
| **2** |  | Control-Changing Effects | Any effect which would change the controller of the object you’re evaluating. Any ability or spell that generates this type of effect should contain the word ‘Control.’ | * [Word of Seizing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Word+of+Seizing)
* [Confiscate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confiscate)
 |
| **3** |  | Text-Changing Effects | Any effect which would change the text of the object you’re evaluating. To be included in this layer, the effect has to specifically state that it’s changing text. Effects such as “Target creature loses all abilities” should be placed in Layer 6. | * [Swirl the Mists](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swirl+the+Mists)
* [Mind Bend](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Bend)
 |
| **4** |  | Type-Changing Effects | Any effect which would add, change or remove types, subtypes or supertypes from the object you’re evaluating. These should be easy to spot, but they’re often thrown in as part of a larger ability. | * [Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth)
* [Conspiracy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conspiracy)
 |
| **5** |  | Color Changing Effects | Any effect which would add, change or remove color from the object you’re evaluating. | * [Alchor's Tomb](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Alchor%27s+Tomb)
* [Moonlace](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moonlace)
 |
| **6** |  | Ability Adding or Removing Effects | Any effect which would add or remove abilities to an object you’re evaluating. | * [Fear](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fear)
* [Humble](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humble)
 |
| **7** | A | Effects from Power/Toughness affecting CDAs | All P/T CDAs. Other CDAs just apply first in their relevant layer. | * [Maro](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maro)
* [Tarmogoyf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)
 |
| B | Any Power/Toughness setting effects | All P/T effects that set either P/T or both to a specific number or value | * [March of the Machines](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=March+of+the+Machines)
* [Lignify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lignify)
 |
| C | Any Power/Toughness changing effect that doesn’t set | This covers all effects that modify Power/Toughness so long as they don’t set P/T to a specific value | * [Shared Triumph](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shared+Triumph)
* [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)
 |
| D | P/T changes from Counters | Any counters that affect P/T | * [Feral Hydra](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feral+Hydra)’s +1/+1 counters
* Any of [Frankenstein's Monster](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frankenstein%27s+Monster)’s counters
 |
| E | Effects that switch P/T | Any effect that switches power & toughness. | * [Inside Out](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inside+Out)
* [Merfolk Thaumaturgist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Thaumaturgist)
 |

 


### Important Rules to remember when using the Layer System:


1. If multiple continuous effects apply in the same layer, first apply CDAs and then apply each continuous effect in timestamp order. This order may be interrupted by dependencies.
2. If a continuous effect has started applying in an earlier layer, it will continue to apply in later layers even if the ability that created that effect has been removed.
3. Auras & equipment (along with fortifications) receive a new time stamp each time they become attached to a different permanent.

### *M10* Changes to the layer system


With the release of *Magic 2010*, the layers system has been greatly simplified to allow for better player (and judge) understanding. We have two primary changes.


First, the layer formerly known as layer 5 (all other effects), got split into 2 separate layers (the old layer 6 became 7). Layer 5 is now color changes and 6 is adding/losing abilities. By separating these 2 types of contunious effects the number of dependencies in the game has been greatly reduced.


Second, there has been a redefinition and rearrangement of sublayers B, C, and D. In the previous rules, temporary p/t effects like [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) could be overwritten by abilities like [Sorceress Queen](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sorceress+Queen), but at the same time abilities like [Glorious Anthem](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glorious+Anthem) would still get to effect the creature. This distinction made it difficult to explain to players, and was all-around confusing. The rules have been changed to go more in line with how Sorceress Queen's original text read; Power/Toughness setting abilities now only effect the actual numbers written on the bottom right of the card (or in the case of copy effects, what ever the copied value is) and then all other effects are added onto the top of that.


### Memorizing


While judging (or playing) we don't always have the [Comprehensive Rules](http://magic.wizards.com/content/comprehensive-rules) at arms reach. Because of this it very important to have the 7 layers, 5 sub layers, and their order memorized. You could commit this to memory or find a mnemonic, acronym, or some other helpful way to remember it. I personally use the mnemonic C.C.T.T.-CAP.


**C**opy  
**C**ontrol  
**T**ext  
**T**ype  
**C**olor  
**A**dding/Removing  
**P**ower and Toughness


While running a seminar on layers at Worlds 08, one judge in the audience told us how he remembered the order of the first two layers. He would think of a C.B. radio and say "Copy, Control."


Finding one that works for you may make memorizing the order a great deal easier.


### Examples of Using Layer System


**Simple Example**


Let's say you have [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears). You attack with it but before blockers are declared you cast [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) targeting your [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) to make him bigger. After the growth resolves, but still before blockers are chosen your opponent casts [Ovinize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ovinize) on your [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears). What does your bears look like?


![](https://web.archive.org/web/20150920111647im_/http://www.wizards.com/dci/judge/images/ja110509_SimpleExampleGraph.jpg)
 


![](https://web.archive.org/web/20150920065317im_/http://www.wizards.com/dci/judge/images/ja110509_SimpleExample.jpg)
 


**Complex Example**


In play there is a [Grizzly Bears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears) which has already been [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)ed, a [Bog Wraith](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bog+Wraith) enchanted by a [Lignify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lignify), and [Figure of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny) with its 3rd ability activated. I then cast a [Mirrorweave](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mirrorweave) targeting the [Figure of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny). What does each creature look like?


### Grizzly Bears


![](https://web.archive.org/web/20150920215020im_/http://www.wizards.com/dci/judge/images/ja110509_ComplexExampleBearsGraph.jpg)
 


![](https://web.archive.org/web/20150920060914im_/http://www.wizards.com/dci/judge/images/ja110509_ComplexExampleBears.jpg)
 


### Bog Wraith


![](https://web.archive.org/web/20150920115518im_/http://www.wizards.com/dci/judge/images/ja110509_ComplexExampeWraithgraph.jpg)
 


![](https://web.archive.org/web/20150920093845im_/http://www.wizards.com/dci/judge/images/ja110509_ComplexExampleWraith.jpg)
 


### Figure of Destiny


![](https://web.archive.org/web/20150920215001im_/http://www.wizards.com/dci/judge/images/ja110509_ComplexExampleFODGraph.jpg)
 


![](https://web.archive.org/web/20150920111659im_/http://www.wizards.com/dci/judge/images/ja110509_ComplexExampleFOD.jpg)
 


### Dependency


A dependent effect will usually affect either more or less objects if applied after the different effect it is dependent on. Here is a simple example of this.


Both [Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth) and [Blood Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Moon) are on the battlefield. What does my [Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth) look like?


If we try to apply [Blood Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Moon) before or after Urborg, [Blood Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Moon) will affect the same number of lands. However, if we apply Urborg after [Blood Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Moon), then Urborg loses its ability and affects no lands. That makes Urborg dependant on [Blood Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Moon), so [Blood Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Moon)'s effect has to be applied before Urborg no matter which has the older time stamp.


![](https://web.archive.org/web/20150920061358im_/http://www.wizards.com/dci/judge/images/ja110509_DependancyGraph.jpg)
 


![](https://web.archive.org/web/20150920215015im_/http://www.wizards.com/dci/judge/images/ja110509_Dependancy.jpg)
 


By comparison if we try removing Urborg's ability after it starts applying we get a very different result.


We have an [Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urborg%2C+Tomb+of+Yawgmoth) that had been hit by an [Animate Land](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Animate+Land) earlier in the turn I then [Ovinize](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ovinize) it. What does it look like?


![](https://web.archive.org/web/20150920065555im_/http://www.wizards.com/dci/judge/images/ja110509_2ndDependancyGraph.jpg)
 


![](https://web.archive.org/web/20150920215025im_/http://www.wizards.com/dci/judge/images/ja110509_2ndDependancy.jpg)
 


### Classic Layer Example


I have two copies of [Opalescence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Opalescence) and one [Humility](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humility). What does the [Humility](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humility) look like?


Ohhh whoops, to get this answer right we need to know which of these 3 has the newest time stamp. We will say [Humility](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humility) came into play last.


![](https://web.archive.org/web/20150920215029im_/http://www.wizards.com/dci/judge/images/ja110509_ClassicLayerExampleGraph.jpg)
 


![](https://web.archive.org/web/20150921140704im_/http://www.wizards.com/dci/judge/images/ja110509_ClassicLayerExample.jpg)
 


NOTE: In layer 6 all three enchantments lose their abilities. This does NOT create a paradox or infinite loop. All three enchantments started applying their abilities before they lost them, so they will continue to apply each part of their ability even though they no longer have them.


### So now that you know all this, let us test your knowledge.


**Question #1: CDAs**


Which of these 3 cards has a CDA? And for the two that are not CDAs, what about their ability makes it so they are NOT CDAs?


1. [Goblin King](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+King)
2. [Mystic Enforcer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Enforcer)
3. [Entropic Specter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Entropic+Specter)

**Question #2: Timestamp & Dependency**


Of these card combinations which are applied in time stamp order and which are applied in a dependency order? If applied in a dependency which of the two cards is dependant? Bonus question, which layer do they both apply in?


1. [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) & [Lignify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lignify)
2. [Conspiracy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conspiracy) & [Opalescence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Opalescence)
3. [Conspiracy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conspiracy) (set to goblins) & [Dralnu's Crusade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dralnu%27s+Crusade)
4. [Opalescence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Opalescence) & [Humility](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humility)

**Question #3: Basic Question**


Aiden has a [Battlegate Mimic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battlegate+Mimic) on the battlefield. Nick controls two [Wilderness Hypnotist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wilderness+Hypnotist)s. Aiden casts a [Scourge of the Nobilis](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scourge+of+the+Nobilis), targeting the Mimic; after that resolves Nick activates one of his Hypnotist's abilities, targeting the Mimic. Aiden attacks with the Mimic, and casts [Inside Out](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inside+Out) before the damage step. Once [Inside Out](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inside+Out) resolves, Nick activates the ability of his other Hypnotist. How much damage will the Mimic deal?


**Question #4: Advanced Question**


Alfred controls [Humility](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humility) which is the card with the newest timestamp on the battlefield, [Opalescence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Opalescence), [Copy Enchantment](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Copy+Enchantment) (which is copying [Opalescence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Opalescence)), [Swirl the Mists](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swirl+the+Mists) (set to Blue), Nigel's [Conspiracy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conspiracy) (set to goblins) that he stole using [Confiscate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confiscate), and of course the [Confiscate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confiscate) itself. Nigel controls [Shared Triumph](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shared+Triumph) set to goblins, [Night of Souls' Betrayal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Night+of+Souls%27+Betrayal), and [Dralnu's Crusade](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dralnu%27s+Crusade). What is going on HERE!?


### Acknowledgements:


* Many of the interactions were either fact checked or directly taken from Gavin Duggan on MTGRULES -L.
* The crazy enchantment question comes from Zammm on the Magicthegathering.com official message boards (I slightly altered it)
* Much of the material comes from Nick Sephton's judge article "[The Interaction of Continuous Effects](http://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26)"
* Carlos Ho & Graham White for their assistance

### Question 1 Answers:


1. is not a CDA because it affects other cards
2. is not a CDA because it is conditional.
3. is a CDA.

### Question 2 Answers:


1. These effects are applied in different layers, so neither time stamps nor dependency apply. [Lignify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lignify) is applied in layer 7b, and [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) in 7c.
2. Conspiracy is dependent on Opalescence. Both apply in layer 4.
3. Dralnu's Crusade is dependent on Conspiracy. Both apply in layer 4.
4. These effects are applied in time stamp order & both apply in layer 7b.

### Question 3 Answers:


![](https://web.archive.org/web/20150920061842im_/http://www.wizards.com/dci/judge/images/ja110509_Question3AnswerGraph.jpg)
 


![](https://web.archive.org/web/20150316072441im_/http://www.wizards.com/dci/judge/images/ja110509_Question3Answer.jpg)
 


Battlegate Mimic will assign 4 damage.


### Question 4 Answers:


![](https://media.wizards.com/legacy/dci/judge/images/ja110509_question4answergraph.jpg)
 


All enchantments other than Confiscate are 1/1 creatures. All of Alfred's creatures are blue goblin zombies.


Justin Hovdenes








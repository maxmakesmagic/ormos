
---
[Link to Wayback Machine](https://web.archive.org/web/20170411233450/http://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26)

[_metadata_:author]:- "Wizards of the Coast"
[_metadata_:description]:- "Introduction&#13; &#13; During my time as a DCI Judge, I've always found this topic challenging. Finally, in an attempt to defeat my demon, I decided to study the topic intricately and write an article that will hopefully be helpful to both judge and non-judge alike.&#13; &#13; Normally when I present the information below to a new or prospective judge, I am greeted by total disbelief. A common phrase at such an occasion is `This isn't in the rule book!` In fact, all of this can be found in the comp rules (rule 418.5), but in a vastly condensed form."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "936316"
[_metadata_:publish_date]:- "2007-11-26"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Interaction of Continuous Effects"
[_metadata_:wayback_capture_timestamp]:- "2017-04-11 23:34:50"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170411233450id_/http://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26"
---


The Interaction of Continuous Effects
=====================================



 Posted in [ARTICLES](/en/articles)
 on November 26, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Wizards of the Coast











### Introduction


During my time as a DCI Judge, I've always found this topic challenging. Finally, in an attempt to defeat my demon, I decided to study the topic intricately and write an article that will hopefully be helpful to both judge and non-judge alike.


Normally when I present the information below to a new or prospective judge, I am greeted by total disbelief. A common phrase at such an occasion is "This isn't in the rule book!" In fact, all of this can be found in the comp rules (rule 418.5), but in a vastly condensed form.


### Simplification is the key


A good way to look at managing continuous effects is to consider it like a mathematical equation. You have a starting value (your original object), a number of values to combine in some way (your effects) and hopefully at some point an answer. Your first task is to arrange your equation correctly, (either in your head, or on paper) because if you fail to do so, it will produce an incorrect answer.


![](https://media.wizards.com/legacy/dci/judge/images/20071126a_image1.jpg)


I'll talk more about a method to easily layout your equation later.


### Starting Concepts


Before we can correctly assign effects to layers, we've got to be able to understand a few basic concepts:



> 
> **Characteristic-Defining Abilities**
> 
> 
> A characteristic-defining ability is an ability that has the following qualities:
> 
> 
> * It is intrinsic to the object it's affecting (i.e. It was part of the object when it was created.)
> * It defines one or more of the following: colour, subtype, power or toughness.
> * It only affects the object it's on.
> 
> Any ability that has these three qualities is a Characteristic-Defining ability (CDA). These are important because they're applied before other abilities of a similar type.
> 
> 
> 




|  |  |  |
| --- | --- | --- |
| **Ability** | **Is it a CDA?** | **Reason** |
| *“Each land is a Swamp in addition to its other land types.”* | X | Affects objects other than itself |
| *“3BG: Until end of turn, Svogthos, the Restless Tomb becomes a black and green Plant Zombie creature with "This creature's power and toughness are each equal to the number of creature cards in your graveyard." It's still a land.”* | X | Isn’t intrinsic to the object it’s affecting.
 Defines Type as well as not Sub-type. |
| *“Nightmare's power and toughness are each equal to the number of Swamps you control.”* | √ | Affects only itself
 Is intrinsic
 Defines Power & Toughness |


> 
> **Timestamp Order**
> 
> 
> Each object has a timestamp, which marks the time it entered its current zone. When we talk about applying effects in 'timestamp order' we mean to apply the oldest effect first, then the next oldest and so on. There are a few special situations that can occur when determining timestamp order, as shown below:
> 
> 
> * The active player determines the timestamp of objects entering a zone at the same time.
> * If an Aura, Equipment or Fortification becomes attached to a different object, it gets a new timestamp.
> * Objects that phase out/in do not receive a new timestamp.
> 
> ***All effects within a layer are applied in timestamp order, with CDAs always being applied first.*** 
> 
> 
> 



> 
> **Dependency**
> 
> 
> Sometimes an effect can depend upon another effect. An effect can be said to depend upon another effect if:
> 
> 
> * Both effects are applied in the same layer (or sub-layer).
> * Applying the effect would change the text or existence of the other effect, how or what it applies to.
> * Neither effect is from a CDA.
> 



> 
> **Breaking up Effects**
> 
> 
> An effect that would apply in two or more different layers is broken into parts and each part applies in the relevant layer.
> 
> 
> 


### The Layer System


Shown below is the layers system, as described in the comprehensive rulebook. You'll notice that there are six layers and that the final layer (power and toughness effects) is split into five sub-layers.




|  |  |  |  |
| --- | --- | --- | --- |
| **#** |  | **Layer Name** | **Description** |
| 1 |  | Copy Effects | Any effect which would copy values onto the object you’re evaluating. If you can spot the word ‘Copy’ in the ability/spell text, then it’s fairly safe to say that the effect needs to live here. |
| 2 |  | Control-Changing Effects | Any effect which would change the controller of the object you’re evaluating. Any ability or spell that generates this type of effect should contain the word ‘Control’. |
| 3 |  | Text-Changing Effects | Any effect which would change the text of the object you’re evaluating. To be included in this layer, the effect has to specifically state that it’s changing text. Effects such as “Target creatures loses all abilities” should be placed in Layer 5. |
| 4 |  | Type-Changing Effects | Any effect which would add, change or remove types, subtypes or supertypes from the object you’re evaluating. These should be easy to spot, but they’re often thrown in as part of a larger ability. |
| 5 |  | All Other Effects not covered in 1,2,3,4 or 6 | Any effect which doesn’t fall under the other 5 layers. The place for the homeless! |
| 6 | **A** | Effects from Power/Toughness affecting CDAs | All P/T CDAs. Other CDAs just apply first in their relevant layer. |
| **B** | All other P/T Effects not covered in 6a, 6c, 6d or 6e | All P/T effects that aren’t covered in another sub-layer. This is mostly +X/+X, -X/-X and P/T setting effects. A very common mistake is to place effects here that should be placed in Layer 6d, or vice-versa. |
| **C** | P/T changes from Counters | Any counters that affect P/T |
| **D** | Effects from static abilities that modify power and/or toughness but don’t set power and/or toughness to a specific number or value | In order to be placed in 6d, an effect must originate from a static ability and modify but not set P/T. The effects from static abilities on objects that stay in play live in this layer *(Crusade, Bad Moon, Night of Soul’s Betrayal, etc…)* |
| **E** | Effects that switch P/T | Any effect that switches power & toughness. |

### Laying out the equation


While you're still learning the process above, it helps to have a way to layout the effects in a way to make them easy to visualize. I've also found these very useful to print out for attendees if you're planning on running a seminar on this topic.




|  |  |
| --- | --- |
| **Layer #** | **Effects in Timestamp Order** |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6a |  |
| 6b |  |
| 6c |  |
| 6d |  |
| 6e |  |

In order to use the above table, go through the effects that apply to an object you're examining in timestamp order (remembering that CDA's come first in each layer from 1-5).


Then, for each effect:


1. Determine which layer it should be assigned to.
2. Note it in the relevant box, to the right of any effect already present.

Once you've assigned each effect to a layer, read down the table applying each effect as you come to it.


### Examples


Below are some worked examples. If you're unfortunate enough to have sat through my seminar on this topic, these examples may seem familiar. Unless it says otherwise, all objects are face up and untapped.  
**Example 1**


The following effects are applied in chronological order to your [Benalish Cavalry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Cavalry)


* [Sudden Spoiling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sudden+Spoiling)
* [Moldervine Cloak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moldervine+Cloak)
* [Gather Courage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gather+Courage)
* [Omnibian](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Omnibian)'s ability

**Example 2**


The following effects are applied in chronological order to your [Gray Ogre](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre) with a +1/+1 counter on it


* [Ferocious Charge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ferocious+Charge)
* [Castle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Castle)
* [Humble](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humble)

**Example 3 (Warning: Beyond the realms of realism)**  

The following effects are applied in chronological order to your [Exalted Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exalted+Angel) with a +1/+1 counter on it. *(You have 6 swamps and 5 mountains, your opponent has 8 mountains and 4 plains)*


* Goblin King enters play under your control
* Cytoshape (copying a [Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare) onto the angel)
* [About Face](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=About+Face),
* [Mind Bend](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Bend) (changing swamp to mountain)
* [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)
* [Conspiracy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conspiracy) enters play under your control (choosing goblins)
* [Blood Lust](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Lust)
* Enchanted by an opponent's [Control Magic](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Control+Magic)
* [Bad Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bad+Moon) enters play
* [Purelace](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Purelace).

### Summary


In my opinion, this is the most complex rule in the book. Even after a fair amount of study, I still find myself tripped up occasionally, with sometimes disastrous consequences (Sorry JB!). If you have any questions about this topic or feedback on this article, I'd welcome it ([nick@dcijudge.co.uk](mailto:nick@dcijudge.co.uk)).


*Many thanks to Frank Wareman, Falko Goerres and Johanna Virtanen for Proof reading!*


### Worked Answers


**Answer 1**


To evaluate your [Benalish Cavalry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Cavalry) (known as **X** in the list below), go through the effects listed above in order and add them to the table. When you're done, simply read down the table to get the result.




|  |  |
| --- | --- |
| **Layer #** | **Effects in Timestamp Order** |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 | "**X** is a frog" |
| 5 | "**X** loses all abilities" |
| 6a |  |
| 6b | "**X** becomes 0/2", "**X** gets +2/+2" "**X** is 3/3" |
| 6c |  |
| 6d | "**X** gets +3/+3" |
| 6e |  |

*So:*   
[Benalish Cavalry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Cavalry) - Creature - Human Knight – Flanking – 2/2


*Becomes:*  
[Benalish Cavalry](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Cavalry) – Creature – Frog – 6/6


**Answer 2**




|  |  |
| --- | --- |
| **Layer #** | **Effects in Timestamp Order** |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 | "**X** loses all abilities" |
| 6a |  |
| 6b | "**X** gets +4/+4", "**X** is 0/1" |
| 6c | "**X** gets +1/+1" |
| 6d | "**X** gets +0/+2" |
| 6e |  |

*So:*   
[Gray Ogre](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre) - Creature – Ogre – 2/2


*Becomes:*  
[Gray Ogre](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre) – Creature – Ogre – 1/4


**Answer 3**


Note: Effects in red are those that do not apply because the creature doesn't fit the requirements at the time they would be applied.




|  |  |
| --- | --- |
| **Layer #** | **Effects in Timestamp Order** |
| 1 | "Copy of a [Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare)" |
| 2 | "Opponent gains control of **X**" |
| 3 | "Swamp becomes Mountain in the text of **X**" |
| 4 | "Creatures you control become Goblins [[Conspiracy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conspiracy)]" |
| 5 | "**X** is white", "Goblins gain Mountainwalk [Goblin King]" |
| 6a | "Set value of \*/\* (8/8)" |
| 6b | "**X** gets +3/+3", "**X** gets +4/-4" |
| 6c | "**X** gets +1/+1" |
| 6d | "**X** gets +1/+1 [Bad Moon]", "Goblins gets +1/+1 [Goblin King]" |
| 6e | "Switch **X**’s P/T" |

*So:*  
[Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare) (black) – Creature – Nightmare 6/6


*Becomes:*  
[Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare) (white) – Creature – Nightmare 8/16


Nick Sephton, L3








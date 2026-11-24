---
id: bqgfw70n
kind: article
lang: en
path: /en/articles/feature/2007/11-26-the-interaction-of-continuous-effects
title: The Interaction of Continuous Effects
published: '2007-11-26'
column_slug: feature
column: Feature
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
    lang_detected: en
    capture_id: 713395
    url: https://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
    captured_at: '2021-12-04 17:53:14+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
    lang_detected: en
    capture_id: 713395
    url: https://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
    captured_at: '2021-12-04 17:53:14+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
    lang_detected: en
    capture_id: 713395
    url: https://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
    captured_at: '2021-12-04 17:53:14+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
    lang_detected: en
    capture_id: 713395
    url: https://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
    captured_at: '2021-12-04 17:53:14+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: bqgfw70n
  url: https://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
  page_key: magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
  lang: en
  template: drupal
  captured_at: '2021-12-04 17:53:14+00'
  capture_id: 713395
  wayback_url: https://web.archive.org/web/20211204175314id_/https://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: bqgfw70n
  capture_id: 713395
  url: https://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
  wayback_url: https://web.archive.org/web/20211204175314id_/https://magic.wizards.com/en/articles/archive/interaction-continuous-effects-2007-11-26
  captured_at: '2021-12-04 17:53:14+00'
  template: drupal
  sha256: 805818fa9b12d3ff6c886238a28e33506b57c603f84b464aea36414ed1456dcd
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:nick@dcijudge.co.uk
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - nick@dcijudge.co.uk
  occurrences: 1
---
### Introduction

During my time as a DCI Judge, I've always found this topic challenging. Finally, in an attempt to defeat my demon, I decided to study the topic intricately and write an article that will hopefully be helpful to both judge and non-judge alike.

Normally when I present the information below to a new or prospective judge, I am greeted by total disbelief. A common phrase at such an occasion is "This isn't in the rule book!" In fact, all of this can be found in the comp rules (rule 418.5), but in a vastly condensed form.

### Simplification is the key

A good way to look at managing continuous effects is to consider it like a mathematical equation. You have a starting value (your original object), a number of values to combine in some way (your effects) and hopefully at some point an answer. Your first task is to arrange your equation correctly, (either in your head, or on paper) because if you fail to do so, it will produce an incorrect answer.

![](http://archive.wizards.com/dci/judge/images/20071126a_image1.jpg)

I'll talk more about a method to easily layout your equation later.

### Starting Concepts

Before we can correctly assign effects to layers, we've got to be able to understand a few basic concepts:

> **Characteristic-Defining Abilities**
> 
> A characteristic-defining ability is an ability that has the following qualities:
> 
> *   It is intrinsic to the object it's affecting (i.e. It was part of the object when it was created.)
> *   It defines one or more of the following: colour, subtype, power or toughness.
> *   It only affects the object it's on.
> 
> Any ability that has these three qualities is a Characteristic-Defining ability (CDA). These are important because they're applied before other abilities of a similar type.

<table><tbody><tr><td><b>Ability</b></td>&#10;			<td><b>Is it a CDA?</b></td>&#10;			<td><b>Reason</b></td>&#10;		</tr><tr><td><i>“Each land is a Swamp in addition to its other land types.”</i></td>&#10;			<td>X</td>&#10;			<td>Affects objects other than itself</td>&#10;		</tr><tr><td><i>“3BG: Until end of turn, Svogthos, the Restless Tomb becomes a black and green Plant Zombie creature with &quot;This creature's power and toughness are each equal to the number of creature cards in your graveyard.&quot; It's still a land.”</i></td>&#10;			<td>X</td>&#10;			<td>Isn’t intrinsic to the object it’s affecting.<br><br>&#10;			Defines Type as well as not Sub-type.</td>&#10;		</tr><tr><td><i>“Nightmare's power and toughness are each equal to the number of Swamps you control.”</i></td>&#10;			<td>√</td>&#10;			<td>Affects only itself<br><br>&#10;			Is intrinsic<br><br>&#10;			Defines Power &amp; Toughness</td>&#10;		</tr></tbody></table>

> **Timestamp Order**
> 
> Each object has a timestamp, which marks the time it entered its current zone. When we talk about applying effects in 'timestamp order' we mean to apply the oldest effect first, then the next oldest and so on. There are a few special situations that can occur when determining timestamp order, as shown below:
> 
> *   The active player determines the timestamp of objects entering a zone at the same time.
> *   If an Aura, Equipment or Fortification becomes attached to a different object, it gets a new timestamp.
> *   Objects that phase out/in do not receive a new timestamp.
> 
> ***All effects within a layer are applied in timestamp order, with CDAs always being applied first.***

> **Dependency**
> 
> Sometimes an effect can depend upon another effect. An effect can be said to depend upon another effect if:
> 
> *   Both effects are applied in the same layer (or sub-layer).
> *   Applying the effect would change the text or existence of the other effect, how or what it applies to.
> *   Neither effect is from a CDA.

> **Breaking up Effects**
> 
> An effect that would apply in two or more different layers is broken into parts and each part applies in the relevant layer.

### The Layer System

Shown below is the layers system, as described in the comprehensive rulebook. You'll notice that there are six layers and that the final layer (power and toughness effects) is split into five sub-layers.

<table><tbody><tr><td><b>#</b></td>&#10;			<td> </td>&#10;			<td><b>Layer Name</b></td>&#10;			<td><b>Description</b></td>&#10;		</tr><tr><td>&#10;			<h3>1</h3>&#10;			</td>&#10;			<td> </td>&#10;			<td>Copy Effects</td>&#10;			<td>Any effect which would copy values onto the object you’re evaluating. If you can spot the word ‘Copy’ in the ability/spell text, then it’s fairly safe to say that the effect needs to live here.</td>&#10;		</tr><tr><td>&#10;			<h3>2</h3>&#10;			</td>&#10;			<td> </td>&#10;			<td>Control-Changing Effects</td>&#10;			<td>Any effect which would change the controller of the object you’re evaluating. Any ability or spell that generates this type of effect should contain the word ‘Control’.</td>&#10;		</tr><tr><td>&#10;			<h3>3</h3>&#10;			</td>&#10;			<td> </td>&#10;			<td>Text-Changing Effects</td>&#10;			<td>Any effect which would change the text of the object you’re evaluating. To be included in this layer, the effect has to specifically state that it’s changing text. Effects such as “Target creatures loses all abilities” should be placed in Layer 5.</td>&#10;		</tr><tr><td>&#10;			<h3>4</h3>&#10;			</td>&#10;			<td> </td>&#10;			<td>Type-Changing Effects</td>&#10;			<td>Any effect which would add, change or remove types, subtypes or supertypes from the object you’re evaluating. These should be easy to spot, but they’re often thrown in as part of a larger ability.</td>&#10;		</tr><tr><td>&#10;			<h3>5</h3>&#10;			</td>&#10;			<td> </td>&#10;			<td>All Other Effects not covered in 1,2,3,4 or 6</td>&#10;			<td>Any effect which doesn’t fall under the other 5 layers. The place for the homeless!</td>&#10;		</tr><tr><td rowspan="5">&#10;			<h3>6</h3>&#10;			</td>&#10;			<td><b>A</b></td>&#10;			<td>Effects from Power/Toughness affecting CDAs</td>&#10;			<td>All P/T CDAs. Other CDAs just apply first in their relevant layer.</td>&#10;		</tr><tr><td><b>B</b></td>&#10;			<td>All other P/T Effects not covered in 6a, 6c, 6d or 6e</td>&#10;			<td>All P/T effects that aren’t covered in another sub-layer. This is mostly +X/+X, -X/-X and P/T setting effects. A very common mistake is to place effects here that should be placed in Layer 6d, or vice-versa.</td>&#10;		</tr><tr><td><b>C</b></td>&#10;			<td>P/T changes from Counters</td>&#10;			<td>Any counters that affect P/T</td>&#10;		</tr><tr><td><b>D</b></td>&#10;			<td>Effects from static abilities that modify power and/or toughness but don’t set power and/or toughness to a specific number or value</td>&#10;			<td>In order to be placed in 6d, an effect must originate from a static ability and modify but not set P/T. The effects from static abilities on objects that stay in play live in this layer<i> (Crusade, Bad Moon, Night of Soul’s Betrayal, etc…)</i></td>&#10;		</tr><tr><td><b>E</b></td>&#10;			<td>Effects that switch P/T</td>&#10;			<td>Any effect that switches power &amp; toughness.</td>&#10;		</tr></tbody></table>

### Laying out the equation

While you're still learning the process above, it helps to have a way to layout the effects in a way to make them easy to visualize. I've also found these very useful to print out for attendees if you're planning on running a seminar on this topic.

<table><tbody><tr><td><b>Layer #</b></td>&#10;			<td><b>Effects in Timestamp Order</b></td>&#10;		</tr><tr><td>&#10;			<h3>1</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>2</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>3</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>4</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>5</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>6a</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>6b</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>6c</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>6d</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>6e</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr></tbody></table>

In order to use the above table, go through the effects that apply to an object you're examining in timestamp order (remembering that CDA's come first in each layer from 1-5).

Then, for each effect:

1.  Determine which layer it should be assigned to.
2.  Note it in the relevant box, to the right of any effect already present.

Once you've assigned each effect to a layer, read down the table applying each effect as you come to it.

### Examples

Below are some worked examples. If you're unfortunate enough to have sat through my seminar on this topic, these examples may seem familiar. Unless it says otherwise, all objects are face up and untapped.  
**Example 1**

The following effects are applied in chronological order to your [Benalish Cavalry](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Cavalry)

*   [Sudden Spoiling](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sudden+Spoiling)
*   [Moldervine Cloak](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moldervine+Cloak)
*   [Gather Courage](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gather+Courage)
*   [Omnibian](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Omnibian)'s ability

**Example 2**

The following effects are applied in chronological order to your [Gray Ogre](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre) with a +1/+1 counter on it

*   [Ferocious Charge](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ferocious+Charge)
*   [Castle](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Castle)
*   [Humble](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Humble)

**Example 3 (Warning: Beyond the realms of realism)**  
 The following effects are applied in chronological order to your [Exalted Angel](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exalted+Angel) with a +1/+1 counter on it. *(You have 6 swamps and 5 mountains, your opponent has 8 mountains and 4 plains)*

*   Goblin King enters play under your control
*   Cytoshape (copying a [Nightmare](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare) onto the angel)
*   [About Face](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=About+Face),
*   [Mind Bend](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Bend) (changing swamp to mountain)
*   [Giant Growth](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)
*   [Conspiracy](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conspiracy) enters play under your control (choosing goblins)
*   [Blood Lust](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Lust)
*   Enchanted by an opponent's [Control Magic](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Control+Magic)
*   [Bad Moon](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bad+Moon) enters play
*   [Purelace](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Purelace).

### Summary

In my opinion, this is the most complex rule in the book. Even after a fair amount of study, I still find myself tripped up occasionally, with sometimes disastrous consequences (Sorry JB!). If you have any questions about this topic or feedback on this article, I'd welcome it (nick@dcijudge.co.uk).

*Many thanks to Frank Wareman, Falko Goerres and Johanna Virtanen for Proof reading!*

### Worked Answers

**Answer 1**

To evaluate your [Benalish Cavalry](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Cavalry) (known as **X** in the list below), go through the effects listed above in order and add them to the table. When you're done, simply read down the table to get the result.

<table><tbody><tr><td><b>Layer #</b></td>&#10;			<td><b>Effects in Timestamp Order</b></td>&#10;		</tr><tr><td>&#10;			<h3>1</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>2</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>3</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>4</h3>&#10;			</td>&#10;			<td>&quot;<b>X </b>is a frog&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>5</h3>&#10;			</td>&#10;			<td>&quot;<b>X </b>loses all abilities&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6a</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>6b</h3>&#10;			</td>&#10;			<td>&quot;<b>X</b> becomes 0/2&quot;, &quot;<b>X</b> gets +2/+2&quot; &quot;<b>X</b> is 3/3&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6c</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>6d</h3>&#10;			</td>&#10;			<td>&quot;<b>X</b> gets +3/+3&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6e</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr></tbody></table>

*So:*  
[Benalish Cavalry](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Cavalry) - Creature - Human Knight – Flanking – 2/2

*Becomes:*  
[Benalish Cavalry](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Benalish+Cavalry) – Creature – Frog – 6/6

**Answer 2**

<table><tbody><tr><td><b>Layer #</b></td>&#10;			<td><b>Effects in Timestamp Order</b></td>&#10;		</tr><tr><td>&#10;			<h3>1</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>2</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>3</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>4</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>5</h3>&#10;			</td>&#10;			<td>&quot;<b>X </b>loses all abilities&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6a</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr><tr><td>&#10;			<h3>6b</h3>&#10;			</td>&#10;			<td>&quot;<b>X</b> gets +4/+4&quot;, &quot;<b>X</b> is 0/1&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6c</h3>&#10;			</td>&#10;			<td>&quot;<b>X</b> gets +1/+1&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6d</h3>&#10;			</td>&#10;			<td>&quot;<b>X</b> gets +0/+2&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6e</h3>&#10;			</td>&#10;			<td> </td>&#10;		</tr></tbody></table>

*So:*  
[Gray Ogre](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre) - Creature – Ogre – 2/2

*Becomes:*  
[Gray Ogre](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre) – Creature – Ogre – 1/4

**Answer 3**

Note: Effects in red are those that do not apply because the creature doesn't fit the requirements at the time they would be applied.

<table><tbody><tr><td><b>Layer #</b></td>&#10;			<td><b>Effects in Timestamp Order</b></td>&#10;		</tr><tr><td>&#10;			<h3>1</h3>&#10;			</td>&#10;			<td>&quot;Copy of a <a href="https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare">Nightmare</a>&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>2</h3>&#10;			</td>&#10;			<td>&quot;Opponent gains control of <b>X</b>&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>3</h3>&#10;			</td>&#10;			<td>&quot;Swamp becomes Mountain in the text of <b>X</b>&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>4</h3>&#10;			</td>&#10;			<td>&quot;Creatures you control become Goblins [<a href="https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conspiracy">Conspiracy</a>]&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>5</h3>&#10;			</td>&#10;			<td>&quot;<b>X </b>is white&quot;, &quot;Goblins gain Mountainwalk [<a>Goblin King</a>]&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6a</h3>&#10;			</td>&#10;			<td>&quot;Set value of */* (8/8)&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6b</h3>&#10;			</td>&#10;			<td>&quot;<b>X</b> gets +3/+3&quot;, &quot;<b>X</b> gets +4/-4&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6c</h3>&#10;			</td>&#10;			<td>&quot;<b>X</b> gets +1/+1&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6d</h3>&#10;			</td>&#10;			<td>&quot;<b>X</b> gets +1/+1 [Bad Moon]&quot;, &quot;Goblins gets +1/+1 [Goblin King]&quot;</td>&#10;		</tr><tr><td>&#10;			<h3>6e</h3>&#10;			</td>&#10;			<td>&quot;Switch <b>X</b>’s P/T&quot;</td>&#10;		</tr></tbody></table>

*So:*  
[Nightmare](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare) (black) – Creature – Nightmare 6/6

*Becomes:*  
[Nightmare](https://web.archive.org/web/20071126000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightmare) (white) – Creature – Nightmare 8/16

Nick Sephton, L3
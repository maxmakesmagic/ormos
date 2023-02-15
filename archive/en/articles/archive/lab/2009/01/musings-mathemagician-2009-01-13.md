
---
[Link to Wayback Machine](https://web.archive.org/web/20211129050111/https://magic.wizards.com/en/articles/archive/lab/musings-mathemagician-2009-01-13)

[_metadata_:author]:- "Noel deCordova"
[_metadata_:description]:- "Hello all! Welcome back to the Lab, where I've cooked up some material that's a little off the beaten path for today. Now, anyone intimately familiar with playing Magic, whether it be through a computer or in person, is aware that most of the game play involves numbers. Whether it is 5 damage to the dome (Lava Axe), drawing 4 cards (Tidings), or creating 3 Saproling tokens"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "187011"
[_metadata_:path_date]:- "2009-01-13"
[_metadata_:publish_date]:- "2009-01-14"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Musings of a Mathemagician"
[_metadata_:wayback_capture_timestamp]:- "2021-11-29 05:01:11"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211129050111id_/https://magic.wizards.com/en/articles/archive/lab/musings-mathemagician-2009-01-13"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/lab/musings-mathemagician-2009-01-13"
---


Musings of a Mathemagician
==========================



 Posted in **From the Lab**
 on January 14, 2009 






![](https://web.archive.org/web/20211024110319im_/https://magic.wizards.com/sites/all/themes/wiz_mtg/images/global/generic-avatar-150.png)
By Noel deCordova











![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_numbercrunch.jpg)  
Hello all! Welcome back to the Lab, where I've cooked up some material that's a little off the beaten path for today. Now, anyone intimately familiar with playing **Magic**, whether it be through a computer or in person, is aware that most of the game play involves numbers. Whether it is 5 damage to the dome ([Lava Axe](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe)), drawing 4 cards ([Tidings](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tidings)), or creating 3 Saproling tokens ([Scatter the Seeds](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scatter+the+Seeds)), numbers are everywhere. But not only are numbers rampant in **Magic**, but patterns as well. For instance, those three card examples all have a converted mana cost of 5. Now, that might seem a tad cheesy, since I just created that pattern, but if you look hard enough, patterns of numbers lie in the game right before your eyes. (For instance, [Pattern of Rebirth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pattern+of+Rebirth) can be played upon a creature, only to be [Number Crunch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Number+Crunch)ed ... Okay, that one stinks.)

The Whole Melvin Yards
![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_sunset.jpg)  
So why am I using up a column to talk about numbers and patterns, when the latest expansion set, *Conflux*, looms on the horizon like the rising sun? Simple, really. To keep with today's miniature theme, let's look at it like a pattern:

From the Lab is a casual column aimed at Johnnies. Ergo, the author of From the Lab must be a Johnny. However, one should not completely alienate the other aspects of his or her psyche (namely, the Timmy, Spike, Vorthos, and Melvin sides.) It's like the whole idea behind *Shards of Alara*: Alara was split into five different entities, with each one getting ample screen time in From the Lab (the five theme weeks.) Concluding, since each aspect of myself as a **Magic** player has been at least mentioned so far besides Melvin, it's time for the quirky little guy to strut his stuff.

Whew, that was exhausting, was it not? In normal people speak (in case your Babelfish wasn't properly inside your ear) I'm flaunting my Melvin side today. Using a few spells from *Shards of Alara*, I'm going to attempt to demonstrate mathematics in **Magic** by examining converted mana costs, effects, and rarity levels. Hopefully this concept is bizarre enough; I am a mad scientist after all!

Disassembling Sangrite Surge
![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_surge.jpg)  
Let's eliminate the wordy intros now and get right to it. [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge), according to the Oracle rulings, costs ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). It is a sorcery, and it is uncommon. Its effect gives one target creature +3/+3 and double strike until the end of the turn. I begin with [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) because it is an easy place to start this exercise. It is a two-colored spell that gives two different upgrades to a creature.

Let's look at the benchmark costs for the two effects of [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge). [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) costs ![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), while [Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave) costs ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) (for the purposes of this exercise, I'm treating hybrid mana as whichever color I need).

Subtracting a normal [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) from [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) gives us a ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)[Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave). Likewise, subtracting a normal [Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave) from [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) gives us a ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)[Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth).

Now, if we add together these new costs for the spells, we wind up with a whopping ![](https://web.archive.org/web/20170424152843im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless7.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)[Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge). And you thought it was overcosted before! The difference between them now is an [Exile](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exile)d [Cathodion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cathodion): ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif). Remember that, because we're off to method number two.

Method # 2 is simple: We just look at the benchmarks and add them together (instead of subtracting) to "build" [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) out of spare parts. [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) + [Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave) (![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) + ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)) = A ridiculous ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)[Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge). If you'll notice, that's undercosted by ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif), the magic number we figured out before. Nifty! 

That would be the end of this experiment, but we've forgotten a key part of [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge): what creature you play it on.

Fortunately, a creature exists in Standard that can replicate one half of [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge)'s effect. [Hungry Spriggan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hungry+Spriggan) can attack for a free [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth). Since [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) gives +3/+3 already, we can eliminate the [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) ability. In clearer terms:

[Hungry Spriggan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hungry+Spriggan) costs ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) for a [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) every time it attacks. Thus, we can erase the ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) from [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge), giving us a "![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)[Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave)."

![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_surgeformula.jpg)  
Another example is with [Springjack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springjack+Knight), which brings us into even weirder territory. Excluding the clash ability for the moment, [Springjack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springjack+Knight) attacks for a free [Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave). Here's where the hybrid cost on [Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave) matters. Instead of thinking of it as ![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif), now we're shifting it to ![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif). Once again, in clearer terms:

[Springjack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springjack+Knight) costs ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) for a [Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave) every time it attacks (we'll get to the clash ability). Using [Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave)'s hybrid cost to conver ![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) to ![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif), we can subtract [Springjack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springjack+Knight) from [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) for a "![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)[Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)." 

However, we can't ignore that [Springjack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springjack+Knight) is hinged upon its clash trigger. Thus we have two possibilities:

1. We win the clash, and wind up with the ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)[Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) as described above.
2. We lose the clash. Thus, [Springjack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springjack+Knight) does not gain double strike. Since we are looking at double strike through the [Double Cleave](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Double+Cleave) lens (and dealing with white mana), we add ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) to the spell to get double strike, resulting in a ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)[Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge)! Weird!

Not enough? Let's try combining [Hungry Spriggan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hungry+Spriggan) with [Springjack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springjack+Knight).



|  |  |
| --- | --- |
|  |  |

This results in a 3/2 creature for ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) that can potentially play [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) on itself for free. Weirdly, this result is the equivalent of playing [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) on [Snapping Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapping+Drake)! Of course, the Drake has flying, so a simple [Flight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flight) on our [Hungry Spriggan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hungry+Spriggan)[jack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=jack+Knight) should even things up. Concluding in equation terms:

[Hungry Spriggan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hungry+Spriggan) + [Springjack Knight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springjack+Knight) + [Flight](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flight) = [Snapping Drake](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapping+Drake) + [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge)

Exhausting, eh? Personally, I find tinkering around like this a neat way to think inside the box. Let's do another!

Deconstructing Kiss of the Amesha
![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_kiss.jpg)  
This one is another relatively simple example. For creativity's sake, I'm going to look at [Kiss of the Amesha](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiss+of+the+Amesha) through a different thought process. Remember, I'm trying to be as Standard legal as possible, as **Magic** has evolved numerous times over its lifespan. 

[Kiss of the Amesha](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiss+of+the+Amesha) is a sorcery. It is uncommon. The effect gives you 7 life and draws you two cards. Finally, it costs ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif). Dividing by two, we once again get an even split, ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) and ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif).

Now I must match the effects with the new costs. Life gain and card draw have always been rooted in white and blue, respectively. So, that gives us "You gain 7 life" for ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif), and "You draw two cards" for ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif).

![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_kissformula.jpg)  
The next step is to use the benchmark costs for these effects and subtract from my created mana costs. [Counsel of the Soratami](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counsel+of+the+Soratami) is perfect as a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif), "Draw two cards." Unfortunately, there is no effect in Standard that results in a gain of 7 life outside of [Primal Command](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primal+Command), which is not only green but incredibly complicated in itself. Thus, we've reached our conclusion slightly more easily this time: According to Standard, [Kiss of the Amesha](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiss+of+the+Amesha) minus [Counsel of the Soratami](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counsel+of+the+Soratami) equals a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) spell that says, "You gain 7 life." Could it be an instant? Sure! [Kiss of the Amesha](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiss+of+the+Amesha) has a bigger effect, and thus is a sorcery, but I'm willing to create a "given" in this experiment, and that could be: instant + instant = sorcery. As you can infer, this given formula also applies to the [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) example above.

Rarity level has a similar formula: common + common = uncommon. This also works in the [Sangrite Surge](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sangrite+Surge) example.

![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_rarityformula.jpg)  
We can even create a name for our new life-gain card based on the two cards already in existence! Both cards have the same name formula ("blank of the blank"). Since [Kiss of the Amesha](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiss+of+the+Amesha) is the root card, and [Counsel of the Soratami](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counsel+of+the+Soratami) is kind of like a common factor, naming the ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 7-life gainer works like this:

"Kiss" minus "Counsel" equals Variable X.

"Amesha" minus "Soratami" equals Variable Y.

Our card would therefore be called Variable X of the Variable Y. Of course, it's figuring these variables out that makes this fun. ("Amesha," if you're wondering, is a rank of angel on Bant—or so the *Planeswalker's Guide to Alara* tells me.) To anyone interested, using this formula, what would you name this card? 

Ready to try this a different way? Take a look at [Reviving Dose](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reviving+Dose), the Oracle text of which is, "You gain 3 life. Draw a card," for ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif). A [Reviving Dose](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reviving+Dose) multiplied by 2 is thus, "You gain 6 life. Draw two cards," for ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif). Awfully close to [Kiss of the Amesha](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiss+of+the+Amesha), isn't it? The only difference is that the Kiss is ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif), and you gain 1 more life point. This leads to an incredibly odd conclusion: By adding blue to a spell, it can gain more life! Okay, only one more life point, but it's still a weird conclusion. And to think, you never would have known it if we hadn't torn apart [Kiss of the Amesha](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiss+of+the+Amesha).

To branch out even further, using this conclusion, our ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) "gain 7 life" card could be modified thusly: Target player gains 8 life for ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) or even ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif)! Now that seems *Planar Chaos*-ish, but logically, I derived these conclusions from the Standard environment!

Blowing Up Bull Cerodon
![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_cerodon.jpg)  
I bet you all have arrived at a conclusion of your own: This guy is the definition of nuts. At least, that's what Limited enthusiasts commonly say about [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon). Big, fast, and vigilant, it's a surefire bomb in Sealed Deck or *Shards of Alara* Booster Draft. 

Using [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) in this experiment introduces a brand-new lens to look through: power and toughness. Creature type is something I'm not going to worry about as much. Let's get the bull rolling!

[Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) costs ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif). It is uncommon, and it has power / toughness levels of 5/5. It has haste and vigilance. Dividing the cost in two gives us a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) cost and a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) cost. Colorwise, vigilance has dabbled in red, white, and green, but in today's Standard, it's mostly white. Haste has always called red home. So far, we have a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) haste creature and a ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) vigilance creature. 

I'll focus on the vigilance creature first. The most basic white creature with vigilance around right now is [Changeling Sentinel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Changeling+Sentinel). [Changeling Sentinel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Changeling+Sentinel) is a 3/2 creature, meaning that whatever haste guy we come up with has to be a 2/3. Our result: A ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) haste creature that's a 2/3. We'll call him Raging Cerodon.

Let's try beginning with haste this time. A longstanding benchmark of quick haste is [Raging Goblin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raging+Goblin). Subtracting a [Raging Goblin](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raging+Goblin) from [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) gives us a ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) vigilant guy that's a 4/4. We'll dub him Bull Sentinel.

![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_twocards.jpg)  
Now, [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon), the existing beatstick that he is, is a 5/5 hasty and vigilant creature for ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif). Adding together Raging Cerodon and Bull Sentinel, however, gives you a 6/7 hasty and vigilant creature for ![](https://web.archive.org/web/20170413132456im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless5.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif), which seems very good. Subtracting this ![](https://web.archive.org/web/20170413132456im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless5.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif) guy from the real [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) leaves us with a +1/+2 boost for ![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif). Hmm ... one white mana, +1/+2, testing everything in Standard ... Aha! All this figuring has led us to none other than [Holy Strength](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Holy+Strength). It just goes to show that one never knows what he or she will wind up with during this experimentation.

![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_day.jpg)  
Cult Following
Hi! Yeah, you—the one who skipped past the boring words in search of neat, Johnny-riffic decks! Don't worry, folks: in spite of my mad scientism, I'm still going to stick to the column's roots. However, I'm simultaneously going to stick with the running theme. Call it sticking up for my idea. Hey, stop moaning, you sticks in the mud!

(Apparently if From the Lab was a tree, it'd have a lot of sap.)

The following deck is all about getting out [Blood Cultist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Cultist) and wrecking havoc. This goal is stymied by the fact that [Blood Cultist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Cultist) is nowhere to be found! What to do? Here's the deck; see if you can figure it out first:







#### Cult Sliver


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (22)



4
[Metallic Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMetallic%5D+%5BSliver%5D)


4
[Sliversmith](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSliversmith%5D)


4
[Heart Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeart%5D+%5BSliver%5D)


3
[Sedge Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSedge%5D+%5BSliver%5D)


4
[Vampiric Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BSliver%5D)


2
[Homing Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHoming%5D+%5BSliver%5D)


1
[Fury Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFury%5D+%5BSliver%5D)



##### Instant (4)



4
[Fiery Temper](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BTemper%5D)



##### Enchantment (6)



4
[Power of Fire](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPower%5D+%5Bof%5D+%5BFire%5D)


2
[Vampiric Embrace](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BEmbrace%5D)



##### Land (24)



13
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


7
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Blood Crypt](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlood%5D+%5BCrypt%5D)



##### Tribal instant (4)



4
[Nameless Inversion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D)


60 Cards 



##### Black (10)



4
[Vampiric Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BSliver%5D)


4
[Nameless Inversion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D)


2
[Vampiric Embrace](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BEmbrace%5D)



##### Red (18)



4
[Heart Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeart%5D+%5BSliver%5D)


3
[Sedge Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSedge%5D+%5BSliver%5D)


2
[Homing Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHoming%5D+%5BSliver%5D)


1
[Fury Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFury%5D+%5BSliver%5D)


4
[Fiery Temper](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BTemper%5D)


4
[Power of Fire](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPower%5D+%5Bof%5D+%5BFire%5D)



##### Colorless (32)



13
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


7
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Blood Crypt](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlood%5D+%5BCrypt%5D)


4
[Metallic Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMetallic%5D+%5BSliver%5D)


4
[Sliversmith](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSliversmith%5D)


60 Cards 



##### 1 (4)



4
[Metallic Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMetallic%5D+%5BSliver%5D)



##### 2 (16)



4
[Sliversmith](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSliversmith%5D)


4
[Heart Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeart%5D+%5BSliver%5D)


4
[Power of Fire](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPower%5D+%5Bof%5D+%5BFire%5D)


4
[Nameless Inversion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D)



##### 3 (9)



3
[Sedge Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSedge%5D+%5BSliver%5D)


2
[Homing Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHoming%5D+%5BSliver%5D)


4
[Fiery Temper](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BTemper%5D)



##### 4 (6)



4
[Vampiric Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BSliver%5D)


2
[Vampiric Embrace](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BEmbrace%5D)



##### 6 (1)



1
[Fury Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFury%5D+%5BSliver%5D)


36 Cards 



##### Common (42)



13
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


7
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Metallic Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMetallic%5D+%5BSliver%5D)


4
[Heart Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHeart%5D+%5BSliver%5D)


2
[Homing Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHoming%5D+%5BSliver%5D)


4
[Fiery Temper](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BTemper%5D)


4
[Power of Fire](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPower%5D+%5Bof%5D+%5BFire%5D)


4
[Nameless Inversion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNameless%5D+%5BInversion%5D)



##### Uncommon (11)



4
[Sliversmith](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSliversmith%5D)


4
[Vampiric Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BSliver%5D)


1
[Fury Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFury%5D+%5BSliver%5D)


2
[Vampiric Embrace](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVampiric%5D+%5BEmbrace%5D)



##### Rare (7)



4
[Blood Crypt](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlood%5D+%5BCrypt%5D)


3
[Sedge Sliver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSedge%5D+%5BSliver%5D)


60 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

















  
Applying the same basic concept as from today's experiments, we must fiendishly mix together some creatures to result in a [Blood Cultist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Cultist). And what better tribe to customize than Slivers?

Enchant a 1/1 Sliver with [Power of Fire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Power+of+Fire) with a [Vampiric Sliver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampiric+Sliver) in play. Voila! One [Blood Cultist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Cultist), and yes, your opponent will have fires with that. There are 12 1/1 Slivers in the deck, so you have ample [Power of Fire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Power+of+Fire) targets. Try to discard [Fiery Temper](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fiery+Temper) to the [Sliversmith](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sliversmith) for even more fire and Slivers. Since over half my creature base can be Hurly-Burlied (you heard me) [Sedge Sliver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sedge+Sliver) steps in. [Homing Sliver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Homing+Sliver) can find your [Vampiric Sliver](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampiric+Sliver)s, as well as [Nameless Inversion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nameless+Inversion)s in a pinch. [Vampiric Embrace](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vampiric+Embrace), meanwhile, is an alternate way to Cultivate your Slivers.

Lesson's Over
I hope you appreciated this offbeat look at the mana cost of certain cards and the numbers and patterns that lie just under the surface of **Magic**. My mad scientist side has been screaming for attention lately, so I figured I'd indulge him. Next week, I'll officially take part in *Conflux* previews, so take that, New Year's Resolutions!

I wanted to cap off today with a hilarious email I received from Aaron Fernandez, who, in response to last week's article, informed me of the only [Realm Razer](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Realm+Razer) nickname that matters. Ready for this?

"In my opinion, the best nickname is clearly the Real Mr. Azer."

Aaron, you win numerous awesome points. See you all next week!

![](https://media.wizards.com/legacy//mtg/images/daily/ftl/ftl21_quote.jpg)  







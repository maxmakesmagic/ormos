
---
[Link to Wayback Machine](https://web.archive.org/web/20170628163014/http://magic.wizards.com/en/articles/archive/card-preview/overexertion-2017-06-20)

[_metadata_:author]:- "Ian Duke"
[_metadata_:description]:- "The development team pushed the exert mechanic to the next level in Hour of Devastation."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1164531"
[_metadata_:publish_date]:- "2017-06-20"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Overexertion"
[_metadata_:wayback_capture_timestamp]:- "2017-06-28 16:30:14"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170628163014id_/http://magic.wizards.com/en/articles/archive/card-preview/overexertion-2017-06-20"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/card-preview/overexertion-2017-06-20"
---


Overexertion
============



 Posted in **Card Preview**
 on June 20, 2017 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_ianduke_0.jpg)
By Ian Duke











Hello everyone! I'm Ian Duke, a senior game designer here in *Magic* R&D. I led the final design and development of *Hour of Devastation*. Our focus during this second half of a set's creation is to execute on the vision set forth by the initial design team, led by Shawn Main. The development team iterates on the set's mechanics, shapes the set themes for Limited and Constructed play, and usually ends up contributing about half of the final card designs.


Working on the second set in a block brings with it unique challenges. While we have a head start in some sense given the foundation of themes and mechanics created by the first set, it's often up to the second set to fully flesh out that design space and even take those themes to the next level. Much of the simple, straightforward design space is used in the first set. For example, *Amonkhet*'s [Sacred Cat](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sacred+Cat) and [Gust Walker](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gust+Walker) are two of the cleanest possible designs using the embalm and exert mechanics. [Splendid Agony](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Splendid+Agony) is a simple design that uses -1/-1 counters.


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sacred+Cat)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sacred+Cat) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gust+Walker)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gust+Walker) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Splendid+Agony)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Splendid+Agony)
We want every set to feel fresh and new and not just be a rehash of the same themes and mechanics but with different card designs. On the other hand, we always want some level of continuity between the two sets of a block. If the sets are too disconnected, they won't play well in Limited, and there won't be obvious upgrades for Constructed decks built on the themes of first set. And if we simply pile on a bunch of new mechanics *and* keep all the old ones, we risk overloading the set—both making it too complicated for new players and not having enough space to fully support each of the themes for more experienced players.


So with *Hour of Devastation*, we took the approach of riffing on the *Amonkhet* mechanics in new ways that the first set wasn't able to fully explore. The most obvious of these is embalm evolving into eternalize, which shares many mechanical similarities but plays much differently. Are you sure you want to attack into my 1/1 creature with eternalize? It might come back to haunt you! Cycling and -1/-1 counters also get several upgrades, including new build-arounds for both Limited and Constructed.


But the mechanic I'm most excited to talk to you about today is exert. In *Amonkhet*, creatures only exert when attacking, and most often the bonus for exerting a creature involves making it temporarily stronger in combat. This certainly makes a lot of sense from a flavor standpoint—the creature is physically overworking itself to make a daring attack or deliver a critical blow. Keeping those cards aligned both flavorfully and mechanically makes those cards easier to learn and process, which is a great design philosophy for the first set of the block.


By *Hour of Devastation*, we knew players would be looking for more variety in how and why creatures can exert. This is true both from the standpoint of reading and discovering novel cards, but also from a play-pattern standpoint of giving the mechanic some dimension outside of attacking. Shawn Main and his team decided to explore giving creatures activated abilities that allow them to exert for an extra-powerful effect. One of the first examples looked something like this:


Well Seeker  

2G  

Creature – Human Advisor  

1/1  

Overextend *(Whenever you activate this creature's abilities, you may choose not to untap it during the next untap step.)*  

T: Add G to your mana pool. If you over-extended Well Seeker, add GG to your mana pool instead.


Shawn's original idea was that each of these creatures with activated abilities that allow them to exert (then called "overextend") would have a baseline ability that got a direct upgrade when you chose to exert. Usually, the bonus would be doubling the regular effect.


Well Seeker did a really nice job of this as a "mana Elf" (as we in R&D often call them) that can either generate one mana every turn or a burst of two mana in a single turn at the expense of taking the following turn off. Sometimes this decision is clear—I play my big creature one turn ahead of schedule. Other times it leads to some fun decision-making. If I start the turn with three Forests and Well Seeker on the battlefield and have a Forest, two five-mana creatures and a six-mana creature in my hand, do I exert my Well Seeker to play the six-mana creature this turn, running the risk of not drawing a fifth land the following turn? Or do I take the conservative approach of guaranteeing I can play a five-mana creature both this turn and next?


However, the teams quickly found that there were fewer simple designs that played well and followed this pattern than we originally imagined. For example, a tapper (like [Fan Bearer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fan+Bearer)) that exerts to tap two creatures rarely exerts except to set up a lethal attack. A pinger (like [Prodigal Pyromancer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prodigal+Pyromancer)) that exerts to deal 2 damage is pretty frustrating to play against in Limited, and the choice of whether to exert or not was often obvious. As we explored this space more, we found ourselves wanting to deviate from the simple "exert to double the effect" structure.


Fortunately, as design of the set progressed, so too did our work on how we would write and implement the rules of mechanic. As you know, the placeholder mechanic name "overextend" ended up becoming "exert," and the templating changed somewhat. A version of this card that reads more like what we settled on would look like this:


Updated Well Seeker  

2G  

Creature – Human Advisor  

1/1  

T: Add G to your mana pool.  

T, Exert Updated Well Seeker: Add GG to your mana pool. *(An exerted creature won't untap during your next untap step.)*


Splitting up the activated abilities gave us significantly more freedom to balance the effects in ways that still felt mechanically and flavorfully connected but led to more fun game play patterns. For example, the pinger referenced above could do something like:


Hard-Working Pyromancer  

2R  

1/1  

T: Hard-working Pyromancer deals 1 damage to target player.  

T, Exert Hard-working Pyromancer: It deals 1 damage to target creature.


These two abilities still make sense appearing on the same card, but one is not a strict doubling of the other. And we wouldn't have been able to do this easily with both effects tied to the same ability.


We were even able to explore designs that have only one activated ability that always requires exerting the creature. There, the decision is whether to leave the creature unable to attack or block for an additional turn in exchange for its ability.


During development of the set, my team explored some additional ways to use the exert design space. One of the coolest ideas came from Ken Nagle, who suggested the idea of "What if you as the player could exert yourself to cast an awesome spell?" What would a design that represents that look like? Ken pitched a cycle of spells that do something awesome, but leave your lands tapped afterward. After looking at some example designs, the team was sold.


Now you might be asking, why would I want my lands to stay tapped after cast a spell? What do I get in return! Well . . .


![](https://media.wizards.com/2017/hou/en_5SY97pBWjQ.png)


The secret is we get to give you a ton of power for very little mana up front. How about a full-fledged, bona fide [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation), on turn three? I'll let that sink in.


Now yes, it's true that in some sense you'll end up "spending" a total of at least six mana over two turns, but if you're getting run over by a horde of Zombies, Dwarves, or Snakes, you just might want your sweeper online as soon as possible. Next turn might be the least of your worries!


[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lord+of+the+Accursed)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lord+of+the+Accursed) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Toolcraft+Exemplar)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Toolcraft+Exemplar) [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Winding+Constrictor)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Winding+Constrictor)
And in my experience, the strategic decisions of when to leave your "shields down" or throw off your mana curve for a turn make these cards a lot of fun to play with. Designing these cards was a blast, as there was always plenty of disagreement initially on how powerful they were. In the end, I think we got them to a really fun power level.


I hope you all enjoy the fun and high-impact decisions that exert brings to *Hour of Devastation* Limited and to Standard and especially the new exert designs that fit into less aggressive decks and play styles. Just remember to take some breaks in between your booster drafts and not to overdo it. We wouldn't want you to . . . well, never mind.








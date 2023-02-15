
---
[Link to Wayback Machine](https://web.archive.org/web/20191103152247/https://magic.wizards.com/en/articles/archive/latest-developments/five-fighting-2007-01-05-0)

[_metadata_:author]:- "Aaron Forsythe"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "612351"
[_metadata_:publish_date]:- "2007-01-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Five for Fighting"
[_metadata_:wayback_capture_timestamp]:- "2019-11-03 15:22:47"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20191103152247id_/https://magic.wizards.com/en/articles/archive/latest-developments/five-fighting-2007-01-05-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/five-fighting-2007-01-05-0"
---


Five for Fighting
=================



 Posted in **Latest Developments**
 on January 5, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_aaronforsythe.jpg)
By Aaron Forsythe












A new year, and with it the promise of a new set. *Planar Chaos* previews begin in earnest next Monday, but those of you who are plugged in have already gotten a taste of the new set. Perhaps you saw our New Year's Damnation [preview](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magic/expansion/planarchaos). Perhaps the [Minisite](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magic/planarchaos/home) has caught your eye. Or perhaps you've gotten your hands on one of the several industry magazines that tease some of the set's many goodies.


We'll have *plenty* to talk about when the time comes, trust me. *Planar Chaos* really taxed us as developers, as we had to answer a lot of hard questions pertaining to how the set was going to impact play environments for the rest of time, not just during the set's Standard lifespan.


But we aren't there yet; I don't want to steal anyone's thunder for next week. There's still lots to talk about regarding *Time Spiral!* To show just how much thought and tinkering go into each card we produce, I've chosen five cards from *Time Spiral* that have been poking their heads into constructed play lately and talk about how they came to be in gory detail.


Indented text has been lifted straight from our internal Multiverse database. Here's a great look at how we think and communicate here in R&D.


### Momentary Blink


 



![Momentary Blink](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Momentary+Blink)

[Momentary Blink](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Momentary+Blink) began life as a totally different card, as part of a cycle that had a completely different identity. Early in *Time Spiral* design, hybrid was a significant part of the set, and we crafted a cycle of hybrid flashback cards. Here's the original white-blue one:


> 
> Lend a Cloak  
> 
> 1{w/u}  
> 
> Instant  
> 
> Move target aura from one permanent you control to another permanent you control. Flashback {w/u}
> 
> 
> 


Hybrid didn't last long (*Ravnica* wanted in back), so we simply changed the hybrid symbols into two different colored symbols (after all, if we were willing to let either color play the spell in hybrid form, both colors could do it via flashback no problem).



> 
> AF 5/17: Might be better served as a cycle of well-known cards with flashback added. Of course, white no longer has any well-known spells.
> 
> 
> 


The original design card wasn't very useful, so we came up with a different white-blue card that was potentially more impactful:



> 
> Atalya's Blessing  
> 
> W  
> 
> Instant  
> 
> You and creatures you control can't be the target of spells or abilities this turn.  
> 
> Flashback 1U (You may play this card from your graveyard for its flashback cost. Then remove it from the game.)
> 
> 
> bs 10/13: works with r/w sword.  
> 
> MP 10/14: Decent hellball solution.  
> 
> AF 10/17: This could be the anti-delay card as well.  
> 
> bs 10/23: this card concerns me. with sunforger, it could get pretty annoying.  
> 
> bs 11/2: killed "counter target spell that targets me or a creature i control," adding a flicker in its place.
> 
> 
> 


 



![Flicker](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flicker)

While Matt Place enjoyed that the new card was a way to effectively stop a hellbent [Demonfire](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demonfire), Brian Schneider was incredibly annoyed with how good the card was in [Sunforger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunforger) decks (“r/w sword”). The Blessing was removed from the set partially due to Brian's concerns, but more as part of a movement to make “flickering” a decent-sized theme in white. The current [Momentary Blink](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Momentary+Blink) ability was tossed into the file, except it could target opponents' creatures as well, and it cost ![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) and ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif). We flip-flopped between having it be an instant and a sorcery.


> 
> PB 11/7: This doesn't seem right somehow, especially as a common sorcery.  
> 
> MP 11/9: Back to instant.  
> 
> RB 11/14: Do we really want both Flashback and Buyback? That might be one recursive mechanic too many. I vastly prefer to keep buyback and cut flashback if we do cut one.  
> 
> MP 11/14: Now only targets your own creatures. Team needs to talk about how all the flickers should work.  
> 
> MP 11/15: Flashback from 1U to 3U.  
> 
> RB 11/20: (We decided all Flicker should only target your own stuff)  
> 
> bs 11/30: upped from W to 1W. too many white commons costed w.  
> 
> sw 12/7: Very strong with aethermage's touch in keeping the creature around, and getting cip effects again.
> 
> 
> 


Randy Buehler's comments on flashback and buyback in the set went largely unheeded (both had their fans, and we felt that they played differently enough). Eventually, all the set's “Flicker” effects were changed to affect only your creatures, and over time the costs of the spell crept up and up. It is testimony to the card's power that even at the ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)/![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif) cost – which we figured probably made it a long shot for Constructed play – [Momentary Blink](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Momentary+Blink) still spawned a reasonably powerful Standard archetype.


Random notes: Of the other four cards in the cycle, [Mystical Teachings](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Teachings), [Strangling Soot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strangling+Soot), and [Thrill of the Hunt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thrill+of+the+Hunt) were printed in very similar incarnations to the original design file hybrid cards; [Ancient Grudge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancient+Grudge) was added later as an homage to [Ray of Revelation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ray+of+Revelation), a popular flashback card from *Judgment*. Steve Warner's note on Blink's potential use with *Dissension's* [Aethermage's Touch](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aethermage%27s+Touch) hints at R&D's paranoia that the latter card was potentially too good to print – unfounded for sure. (You may remember Zvi Mowshowitz's [preview article](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/zm40) of the Touch: “Every so often, a card should have enough potential that you want to run out, buy four copies and start breaking formats.”) Lastly, because tokens cease to exist as a state-based effect, token creatures can be Blinked out and *will* return because there is no time for state-based effects to be checked during resolution. There is some ambiguity on this point in Rule 216.3, and this issue will likely be revisited at some point in the future.


### Brine Elemental


 



![Brine Elemental](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Brine+Elemental)

Here's a card that appeared in the *Time Spiral* design file – one that played into the very prevalent “time matters theme” that the set's earliest incarnations already contained:


> 
> Vapor Elemental  
> 
> 4U  
> 
> Creature – Elemental  
> 
> 3/3  
> 
> When CARDNAME comes into play, lands controlled by target player don't untap during his or her next untap step.
> 
> 
> DAL 7/25: vs. Anchor. (btw Mana Vapors is a very unmemorable card that does this.)  
> 
> BT 7/28: A tricky yet simple card. Cool.  
> 
> bs 8/30: this guy is retarded as a common.  
> 
> HS 9/30 nice  
> 
> ZM 10/4: Mark of Eviction issues, will test.  
> 
> ZM 10/6: Looks reasonably hard to pull off.  
> 
> Del 10/10: Another confusing use of "this turn" -- confirm that this was your intent?  
> 
> bs 10/10: looks good.  
> 
> AF 10/17: Could be scary with Mark or Flickerform. Might want to be easier to kill, like 3/1.  
> 
> bs 10/19: lowered toughness from 3 to 1.  
> 
> HS 11/04 With Father of runes = Stasis for my opponents lands  
> 
> PB 11/7: Plenty of other cards in the set that can do the same trick.
> 
> 
> 


Devin Low's initial comment links the card's abilities to the forgettable *Prophecy* card [Mana Vapors](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Vapors), but also hints at something called “Anchor” – a keyword that was removed from the set pretty early on. The Anchor ability was another “time matters” mechanic, and, while incredibly boring, had enough interesting play implications that we might try it again some day. We lowered his toughness by two to make any kind of recursive combos easier to break up with damage, but there was still some abusive potential (I wrote about Father of Runes – the card Henry Stern mentions in his comment – in my “[The Themes of *Time Spiral*](/en/articles/archive/latest-developments/themes-time-spiral-2006-10-27-0)” article).


As Brian Schneider mentioned early in the comments, this card's status as a common was dubious at best, so when a hole opened up in blue rare, we beefed it up, tweaked it a bit, and moved it up:



> 
> Brine Elemental  
> 
> 5UU  
> 
> Creature – Elemental  
> 
> 5/4  
> 
> When CARDNAME comes into play, each opponent skips his or her next untap step.
> 
> 
> 


 



![Water Elemental](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Water+Elemental)

I'll confess to being the one responsible for the creature's power and toughness; I have some sort of unnatural love for the Alpha card [Water Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Water%2BElemental). As a newer player, I was enamored with the abnormal size of this blue creature, and I have had a soft spot in my heart for it ever since (the goofy art, with its focus on the guy in the boat as opposed to the barely-noticeable elemental in the corner, probably added to the card's appeal for me). In fact, I tried for a long time to convince my cohorts that [Water Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Water+Elemental) would have been a great card to timeshift, but no one agreed with me. So I tried working it in on this particular card. And, as you'll see later, I never gave up.


> 
> MP 11/15: Now a rare that makes them skip all untaps instead of just land. Also P/T matches water elemental.  
> 
> bs 11/21: this is a horrid-looking rare. exhaustion + water elemental is not exciting.
> 
> 
> 


Okay, so Schneider didn't like the card as a rare. Something else was bound to change, and it just so happened that about this same time, morph was winding its way into the set as a theme of blue. All of the blue morphs with “turn face up” triggers were made to mimic existing spells, like [Twiddle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Twiddle) and [Dream Cache](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dream+Cache) (which was later changed to [Gush](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gush)… and yes, as you may have seen on Card of the Day back in October, the coins in the art of [Fathom Seer](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fathom+Seer) are a lost reference to its original [Dream Cache](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dream+Cache) ability). Here is the “Exhaustion” morph, put in the file as an uncommon:



> 
> Brine Elemental  
> 
> 3U  
> 
> Creature – Elemental  
> 
> 3/1  
> 
> When CARDNAME is turned face up, each opponent skips his or her next untap step. Morph 2U (You may play this face down as a 2/2 creature for 3. Turn it face up any time for its morph cost.)
> 
> 
> bs 11/27: fixed recursion issues, added morph, moved to uncommon.  
> 
> ZM 11/29: I think we've fixed them, but I'm not positive just yet.  
> 
> AF 12/6: Having these "cast spells" doesn't seem worth it. I'd rather have a guy or two that wins fights. (Imagine if this guy was 5/4.) We made the spellshapers "cast spells" and we weren't always happy with the results. Making cards that play well has got to be better that having weird little Easter eggs that no one will catch.  
> 
> RB 12/19: I agree with Aaron  
> 
> AF 1/18: This guy needed to be worse... now he's a Water Elemental.  
> 
> MP 1/18: Cost down by 1, morph up by 2. Hopefully this makes the morph clone combo "fair".
> 
> 
> 


The card was really, really good because of the design constraint that the morph cost match the original spell exactly. Because all the power of the morphs was in their triggers, none of them had substantial bodies, so your opponents knew they could almost always safely block your morph creatures as none of them were able to turn into anything sizeable. I suggested that we break up the symmetry to get some size onto a morph, hoping that it could go back to being a [Water Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Water+Elemental) again. And one day, when Brian Schneider was out of the office, it did!


We had always known that [Vesuvan Shapeshifter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuvan+Shapeshifter), with its aggressive morph cost, was going to be the number-one choice to combo with the morph Exhaustion creature. Later on the day we made it into a 5/4, our testing forced up to up the Elemental's morph cost to a whopping seven. Because of the potential Shapeshifter abuse, both numbers on the [Brine Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Brine+Elemental) had to be high, but even with his hefty costs, Briney has still shown up in some very impressive Standard decks.


### Empty the Warrens


 



![Empty the Warrens](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Empty+the+Warrens)

Storm was always part of red's identity in *Time Spiral* – initially as just a vertical three-card cycle. Here was the common from that cycle:


> 
> Goblintide  
> 
> 1R  
> 
> Sorcery  
> 
> Put a red 1/1 Goblin creature token with haste into play.  
> 
> Storm
> 
> 
> Storm vertical cycle  
> 
> MP 9/27: Can this be an instant, I find storm cards that my opponent helps enable are fun.  
> 
> ZM 9/29: Certainly could use some help, right now it feels like bad Raise the Alarm.  
> 
> BB 10/18: Isn't this the kind of card we'd do in Pop?  
> 
> bs 10/23: why? goblins + storm? or because it's risky and it shouldn't be around for more than 16 months?
> 
> 
> 


As you can see from Brian's response to Brandon Bozzi's cryptic comment, there was always a significant worry surrounding the printing of any storm cards. That said, “Goblintide” was underperforming, even under the best circumstances. So we changed it to something closer to the current printed version:



> 
> [Goblin Horde]  
> 
> 2R  
> 
> Sorcery  
> 
> Put two 1/1 red Goblin creature tokens into play.  
> 
> Storm
> 
> 
> MP 11/15: Upped cost by 1, now creatures 2 guys instead of 1 guy with haste.  
> 
> MT 11/22: Made 6 dudes on turn 4. Oh and killed two creatures with the Ember Shot Storm card on the same turn. Should be 3R.  
> 
> ZM 11/23: Even at 3R this card is quite strong.
> 
> 
> 


Obviously the card didn't last long at three mana. At four, it certainly *looked* unwieldy, but both Mike Turian and Zvi Mowshowitz recognized that it would certainly still be very good.


When Matt Place asked early on if the card could be an instant, we knew pretty decisively that the answer was “no.” Many of Scourge's storm cards were instants, and it was so easy to get the count above one that there often was no deckbuilding or gameplay challenge at all. We wanted the ability to interact with suspend and to encourage people to find ways to abuse them themselves, as opposed to simply piggybacking off of what the opponent has done. And the results speak for themselves: Empty the Warrens is even seeing play in Extended, where all sorts of near-broken things are occurring.


### Scryb Ranger


 



![Scryb Ranger](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scryb+Ranger)

This little wunderkind first came to exist in development; we wanted a green flier that could help smooth out mana problems. Here was our first attempt, a common:


> 
> Tree Sprite  
> 
> 1G  
> 
> Creature – Faerie  
> 
> 1/1  
> 
> Flying  
> 
> 1, T: Add one mana of any color to your mana pool.
> 
> 
> bs 10/6: changed to a sprite. was spectral boars.  
> 
> Del 10/10: Makes my heart sink because it looks like a nerfed BoP replacement.  
> 
> bs 10/10: could be more fire sprite like.  
> 
> bs 10/23: is this the right card for this slot?
> 
> 
> 


The card the Faerie replaced, “Spectral Boars,” was later resurrected in a larger, more ridiculous form as [Spectral Force](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spectral+Force).


What we were trying to riff of with this particular card was a somewhat obscure *Legends* common called [Fire Sprites](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fire+Sprites) that had charm in its day. Tree Sprite was significantly less quirky, and its functionality was eventually stolen by [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens). So we went back to the drawing board.



> 
> [Quirion Sprite]  
> 
> 1G  
> 
> Creature – Faerie  
> 
> 1/1  
> 
> Flying  
> 
> Return a Forest you control to its owner's hand: Untap target creature. Play this ability only once per turn.
> 
> 
> bs 10/24: added quirion text.  
> 
> ZM 11/3: I feel like we lost the magic somehow.  
> 
> PB 11/7: This card is not fun to play against in limited - too many easy things to combo it with.  
> 
> RB 11/14: Probably yet another common that really belongs at uncommon. If it comes up less often then people will feel clever when they use it.  
> 
> MP 11/15: Unc now, added pro-blue.  
> 
> bs 12/2: took off pro:blue, added surprise.  
> 
> AF 12/8: Pro blue could help in constructed vs. skies.  
> 
> MP 12/14: I liked the random pro blue.  
> 
> bs 12/19: added pro blue back.  
> 
> MT 2/14: Totally awesome. Will be interested how good this is in constructed. My guess is pretty good.  
> 
> JT: 10/3: Baby Green Akroma.
> 
> 
> 


As you can see, this version of the card started off without many bells and whistles. There were a ton of things that comboed with it at common, as Paul Barclay noted, and we eventually moved it up to uncommon at Randy's urging.


If you look closely at the entire *Ravnica* block, you'll notice that there isn't a single creature therein that has protection from a particular color (the closest would be [Hunted Horror](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hunted+Horror)'s pro-black Centaur buddies). The lack of that ability was intentional – in *Ravnica*, colors were not enemies of specific other colors. Because protection tends to play well in well-metered doses, we wanted to crank up the number of pro-color creatures in *Time Spiral* to get protection back into the Standard environment. The Ranger was one of the beneficiaries of that pass, getting protection from blue.


There was a subsequent pass through *Time Spiral* to make sure that flash (then “surprise”) was important enough to the set and that it was showing up on the right cards. The Ranger was a perfect candidate for flash, as it had an ability that was great to ambush opponent's with – play the Ranger, untap my biggest guy, block! So it gained that keyword and lost protection… for a couple of weeks. The pro blue ability was well-liked among the developers and eventually found its way back onto the card on top of everything else, hence the “Baby Green Akroma” comment from Jake Theis. There certainly is quite a bit of goodness packed onto that little 1/1 frame.


The “skies” deck I talked about? It was a blue/white concoction featuring such unsung heroes as [Pride of the Clouds](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pride+of+the+Clouds), [Vexing Sphinx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vexing+Sphinx), and the long-departed [Serendib Efreet](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Serendib+Efreet), once a timeshifted candidate. The deck was quite saucy!


### Vesuva


 



![Vesuva](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vesuva)

Mark Rosewater and I both independently came up with the idea of a “Clone Land,” and it found its way into the original *Time Spiral* design:


> 
> [Clone Land]  
> 
> Land  
> 
> As CARDNAME comes into play, you may choose a land in play. If you do, CARDNAME comes into play as a copy of that land.
> 
> 
> 


Neat card, but it didn't have much to do with *Time Spiral* – it had no time-affecting mechanic and there was very little nostalgic about it. At one point we did a pass during design to remove any cool, unrelated cards from the set to save for later expansions, and this card disappeared.


A few nights later I was hit with the inspiration to call the card “Vesuva” as a nod to the original [Vesuvan Doppelganger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuvan+Doppelganger). [Vesuva](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuva) had to be a place, right? I talked to Brady Dommermuth about it, and he was reasonably sure that Vesuva had been mentioned somewhere in **Magic** literature, so I pleaded that the card be reinstated. It was, and was made legendary for flavor reasons.



> 
> BT 4/7: Love it.  
> 
> DAL 4/29: WOW me too.  
> 
> BB 5/5: nice!  
> 
> DAL 7/20: Name a perfect match.  
> 
> loved  
> 
> anywhere
> 
> 
> 


A hit! As development began, Brian decided to take off Legendary, as Legendary Lands have significant baggage associated with them that makes for bad game play. Who wants a land that you only want one of in your deck? But without that check in place, the real power of [Vesuva](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuva) began to show itself in the FFL. Soon most decks had the maximum four copies, and it became impossible to tell what lands were in play in any given game.



> 
> bs 9/23: took off legendary.  
> 
> MP 9/27: 4 of in nearly every deck.  
> 
> bs 9/27: it makes me smile.  
> 
> HS 10/5 nice  
> 
> NH 10/13: Can this have the sakashima rule so it can copy legendary things?  
> 
> MP 10/14: Fan of this card, too. Good with maze of ith.  
> 
> BB 12/12: Legendary? It could keep its name.  
> 
> MP 12/21: This could CIP sac me and search for a copy of a land in play. This version is so powerful that they are often too many of this in play to keep straight.  
> 
> MJ 12/21: I used to like this a lot, but have changed my mind. In playing the memory issue comes up time and again, particularly with multiples. GREAT card, but not one i would like to see a lot of in constructed.
> 
> 
> 


 



![Maze of Ith](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Maze+of+Ith)

Yes, [Maze of Ith](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maze+of+Ith) was a potential timeshifted card for a bit; it didn't last much longer after Matt's comment (and very annoying deck).

As a group we were divided as to what to do with [Vesuva](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuva). Some of us thought the card was so cool that the memory issues would be worth the trouble. Others felt that games involving multiple [Vesuva](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuva)s (and Karoos, which often bounced [Vesuva](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuva)s to reset them) were so miserable that printing the card as-is was out of the question. Mons Johnson was one of the loudest voices against the card's powerful version, and his common-sense approach won out. The development team eventually gave in.



> 
> bs 1/5: CN comes into play tapped.  
> 
> Del 2/28: Moved the CIPT info into the copy ability to make this work sensibly.
> 
> 
> 


In retrospect, the change was perfect. The card still has lots of appeal and enables some really cool things, and it is showing up at *just* the right amount in constructed – one copy here, one four-of deck there. The nightmare games of six or seven [Vesuva](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vesuva)s are few and far between.


### Wrapping Up


And that, folks, is why I love my job. Three thousand words on five cards! So many small but meaningful decisions, so many memories of meetings, games, and arguments, so many stories to tell.


And to think, next week begins another chapter in **Magic: The Gathering** history, with 165 new cards to talk about.


Stay tuned!


### Last Week's Poll




| **Who will win The Great Designer Search?**  |
| Alexis Janson | 4135 | 84.6% |
| Kenneth Nagle | 423 | 8.7% |
| Graeme Hopkins | 329 | 6.7% |
| **Total** | **4887** | **100.0%** |

Alexis voters rejoice! But all of them will be here this month, so in actuality there are lots and lots of winners.









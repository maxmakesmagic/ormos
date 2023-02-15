
---
[Link to Wayback Machine](https://web.archive.org/web/20141223193818/http://magic.wizards.com/en/articles/archive/latest-developments/guildpact-twenty-questions-2006-01-27)

[_metadata_:author]:- "Aaron Forsythe"
[_metadata_:description]:- "I got lots of email last week and from it I chose (pretty haphazardly) twenty questions about the development of Guildpact cards. If this article proves satisfactory, I may go back and find twenty more two weeks from now."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "289786"
[_metadata_:publish_date]:- "2006-01-27"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Guildpact: Twenty Questions"
[_metadata_:wayback_capture_timestamp]:- "2014-12-23 19:38:18"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20141223193818id_/http://magic.wizards.com/en/articles/archive/latest-developments/guildpact-twenty-questions-2006-01-27"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/guildpact-twenty-questions-2006-01-27"
---


Guildpact: Twenty Questions
===========================



 Posted in **Latest Developments**
 on January 27, 2006 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_aaronforsythe.jpg)
By Aaron Forsythe










I got lots of email last week and from it I chose (pretty haphazardly) twenty questions about the development of *Guildpact* cards. If this article proves satisfactory, I may go back and find twenty more two weeks from now.


A lot of these questions come down to “Why isn't Card X more awesome?” Valid questions, and I'll do my best to explain why. But I want to reiterate who we are and what we're trying to do. Yes, developers have the unsavory task of making cards worse from time to time, but we do so out of love. All of us are grizzled veterans of the game—most devs have a decade of *Magic* behind them—and the reason we wound up in our positions is that *we love the game*. Please understand that a room full of people that love *Magic* working together on a card set have one goal—keeping the game as fun as possible. So when you hear that a card or a mechanic got worse, rest assured that the conversations leading up to the change usually contained something akin to the following:


“That game sucked.”  



By making individual pieces worse, we strive to make the whole package—Standard, casual, Limited, all of it—better. We are certainly not out to ruin anything or spoil anyone's fun, regardless of how you feel about a particular card.


On to the questions.



> 
> *Why do* Ravnica *guilds have 16 gold cards each and* Guildpact *guilds only have 15? Not that it makes a big difference, but the number should be the same.*
> 
> 
> *--Davide Azevedo*
> 
> 
> 


It makes a tiny bit of difference, Davide, and personally I wish the numbers were the same. When we crunched and re-crunched the number of gold cards that each guild could support in *Ravnica*, we did so with *Guildpact* (and *Dissension*) in mind—we wanted to keep the guilds the same size throughout the block and tried to adjust accordingly. We arrived at a number of gold rares (including hybrid) that we thought we could live with for each guild (7 in RAV).


When *Guildpact* was handed over from design, it also had seven gold rares per guild, plus the cycle of five Nephilim. The lead developer felt that there weren't enough single-colored rares in the set (as each guild also had a rare land and a rare artifact), and that the seventh gold rare in each guild was less important to the set than the Nephilim. So each guild is down a rare in this set.


We avoided this problem in *Dissension* by making the set 15 cards larger. Each guild has seven gold rares in that set.


![](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/af103_borborygmos.jpg)

> 
> *Why is [Borborygmos](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Borborygmos) a Cyclops? Why are [Pyromatics](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyromatics) and [Train of Thought](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Train+of+Thought) so grossly overcosted? Why doesn't [Hatching Plans](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hatching+Plans) come with a way to sacrifice it, and why is it rare?*
> 
> 
> 
> *--Jason Barber*
> 
> 
> 


In order: (1) Our creative team thinks Cyclops is a type worth supporting and that it was a mistake to get rid of it in the first place. I imagine we'll be seeing more Cyclops in the future. In fact, check the most recent Oracle update and you'll see that some old Cyclops have been “restored.”


(2): The “replicate cost” on replicate cards was added very late in development (so late, in fact, the set was practically in editing); in design, the mechanic meant simply “pay the card's mana cost multiple times.” There was never any consideration to being able to have higher or lower replicate costs than the mana costs, even though the way the mechanic ended up worded makes such differences possible. So we had to decide whether or not one damage should cost R or 1R, and whether “draw a card” should cost U or 1U. The cheaper costs made the cards far too good, so we settled for the more fair (and admittedly less sexy) two-mana versions. They are, after all, meant to be the simplest and most common execution of the mechanic.



![](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/af103_narrow.jpg)
(3) [Hatching Plans](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hatching+Plans)' point is that it presents a challenge of how to use it. Putting some gimpy out clause (like “4UU: Sacrifice Hatching Plans” or “Skip your next turn: Sacrifice Hatching Plans”) takes all the mystique away from the card. As for why it's rare—we tend to make very narrow cards rare, and this card is the poster child for narrow.




> 
> *(1) Was [Giant Solifuge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Solifuge) originally 2RG? It feels weird casting an untargetable creature for 2RR, or a haste creature for 2GG ([Yavimaya Ants](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Yavimaya+Ants) notwithstanding).*
> 
> 
> *(2) Why does [Ogre Savant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ogre+Savant) compare so horribly to [Man-o'-War](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War)? Was it designed to be bad, did it lose out during limited pointing, or is [Man-o'-War](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War) now considered too good?*
> 
> 
> *Mark S. Cipolone*
> 
> 
> 


(1) Yes, indeed it was. Its playtest name was “Christmas Ants,” and its hybrid status was the result of some eleventh-hour changes. [Burning-Tree Shaman](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning-Tree+Shaman) was a late creation of the development team's, and it used the art of another uncommon card that was kicked out off the set. To make room for the Shaman at rare, [Feral Animist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Feral+Animist) (the original Gruul rare hybrid card) was moved from rare to uncommon. Because Gruul then needed a rare hybrid card, the Solifuge's cost was swapped from 2RG to 2(R/G)(R/G) and nothing else about the card changed. The card is a bit of a stretch as far as the color pie goes, as Green only rarely gets haste and Red never before had untargetability. But the team was comfortable blurring the boundaries a little for the sake of making a cooler card. Don't expect that to happen very often.



[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Man-o'-War)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o'-War)
(2) [Man-o'-War](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Man-o%27-War) is considered above the curve for a Blue creature, a fact that should be obvious once you realize how simple and iconic the card is, yet we've never opted to reprint it in ten years. Instead you get five-mana versions like [Kiri-Onna](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kiri-Onna) and [Ogre Recluse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ogre+Recluse). I can imagine us one day bringing back the original Jellyfish, or maybe something close, but the environment would have to be just right for that to happen.




> 
> *You asked for card-by-card questions, so here it is:*
> 
> 
> *Let's take the basic counter - [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell).*
> 
> 
> *Add a drawback - Non-blue spell.*
> 
> 
> *According to Mark Rosewater's article "[Counter Intelligence](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr169)", if you add drawbacks, it should cost less, but in this case we see a greater mana cost with a smaller effect. What happened?*
> 
> 
> *--Y.*
> 
> 
> 




![](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/af103_counterspell.jpg)
Your error comes in thinking that “good ol' UU Counterspell” is the baseline we use for making permission spells these days. In actuality, the current group of developers sees 1UU as the “fair” cost for “counter anything, period.” As far as “more expensive” is concerned, one costing trick we use a lot is that one colored mana symbol can usually be freely exchanged with 2 colorless. GG is a fair cost for a 2/3, as is 2G. [Boomerang](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boomerang) is UU, [Regress](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Regress) is 2U. [Vicious Hunger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vicious+Hunger) was BB, [Douse in Gloom](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Douse+in+Gloom) 2B (and an instant to compensate). So on the “fairness” meter, 1UU and 3U are pretty darn close. That said, we don't like the idea of making hard counters splashable—we want players to commit to heavy Blue to have reliable permission. So even at 3U, “counter any spell” is not something we're willing to print, which is why [Frazzle](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frazzle) has a situational drawback.





> 
> *You asked to send in questions about the development of* Guildpact *cards and there is something I'd like to know. Was [Conjurer's Ban](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Conjurer%27s+Ban) intentionally made into a sorcery (although similar cards like [Orim's Chant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Orim%27s+Chant) have been Instants before) to not fit the [Isochron Scepter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Isochron+Scepter)?*
> 
> 
> *--chaosof99*
> 
> 
> 


No, the Scepter never entered into the equation. The reason it is a sorcery is to prevent people from playing it “in response” to an opponent announcing a spell. That's a trick that doesn't actually work (the spell would have already been played, so it would be too late to say it couldn't be), but many, many players get such interactions wrong, as evidenced by the sheer number of rules issues surrounding cards like [Orim's Chant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Orim%27s+Chant). We like to circumvent those sticking points wherever we can.


![](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/af103_hypervolt.jpg)

> 
> 
> *I noticed on the* Guildpact *card [Hypervolt Grasp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hypervolt+Grasp) that it has the Gruul clan symbol in its text box, when it is obviously an Izzet card. Is this a misprint or was it put there on purpose?*
> 
> *--Alex McHardy*
> 
> 
> 


Yeah, that one was an error. Those darn Multiverse gremlins.



> 
> *At the prerelease, in the Sealed deck tourney, I played Izzet/Gruul. I pulled a [Killer Instinct](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Killer+Instinct), and got a [Wee Dragonauts](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wee+Dragonauts) with it. I then [Gigadrowse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gigadrowse)d my opponent with 4 (count 'em four) replications of the spell, and pretty much beat him down with my Dragonauts. Did you mean for this to happen when you designed either spell?*
> 
> 
> *--Patrik Martin*
> 
> 
> 


No we didn't, because that trick doesn't actually work. Replicated copies of spells aren't “played,” and don't trigger effects like those on [Wee Dragonauts](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wee+Dragonauts) and [Gelectrode](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gelectrode). Each replicate spells only counts as one spell played, regardless of how many times you replicate it.



> 
> *Why can [Wurmweaver Coil](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wurmweaver+Coil) only enchant green creatures?*
> 
> 
> *--Julian Vermund*
> 
> 
> 


Funny story. When we decided to print [Auratouched Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Auratouched+Mage) in *Ravnica*, the development agreed that we'd have to restrain ourselves from printing Auras that made the Mage “too easy,” like [Mythic Proportions](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mythic+Proportions) from *Onslaught*. “No problem,” I thought, “we only do Auras like that every few years.” So of course the *Guildpact* development team insists that we make a giant Aura in Green. Not wanting to make the Mage “too easy” (and this is not necessarily a high-level Standard issue, mind you), we restricted what the Coil could enchant.



> 
> 
> [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Leyline of the Void)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline of the Void)
> *How did you decide on the rarity of [Seize the Soul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seize+the+Soul)?*
> 
> *and*
> 
> 
> *Was [Leyline of the Void](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leyline+of+the+Void) created to intentionally destroy 'Tog decks and [Ichorid](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ichorid) decks?*
> 
> 
> *Darrin Katz*
> 
> 
> 


[Seize the Soul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seize+the+Soul) was uncommon for a bit, but when it was pointed out that the haunt reminder text didn't fit on it, we swapped it to rare for [Cryptwailing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cryptwailing) (a fine swap in any event). We don't like leaving reminder text off of non-rares, as we want people's first encounter with new mechanics to have reminder text. As is stands, [Seize the Soul](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seize+the+Soul) is a fine rare as it's effect is a bit narrow, but totally over the top (like [Hex](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hex)).


The Black Leyline was finalized long before Friggorid reared its head, but it was created, in a way, to destroy it. Development had fears that dredge was going to “break” somewhere, and that we needed a “panic button” available should our fears bear out. And they did.



> 
> 
> [![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hazezon Tamar)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hazezon Tamar)
> *Why on Earth does [Dune-Brood Nephilim](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dune-Brood+Nephilim) make Sand tokens?*
> 
> *It's bad enough that it's a legitimate creature type thanks to [Hazezon Tamar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hazezon+Tamar), but did you really have to go and remind everyone?*
> 
> 
> *--Cody Watts*
> 
> 
> 


Yes, we had to remind everyone. Quirky stuff like the “Sand” creature type amuses far more people than it offends, and I love it when we do little throwbacks like that.



> 
> *Why do the leylines cost so much? Even at the free cost, they seem very narrow. Were they too powerful at 1GG or 1UU?*
> 
> 
> *--Mark*
> 
> 
> 


While they may be “fair” at three, we wanted the “start the game in play” mechanic to actually mean something. The cheaper the cards' actual mana costs were, the less it would feel like you were getting away with something if you put them into play for free.



> 
> *Ok, then. How about some sort of explanation for [Shattering Spree](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shattering+Spree)? To my mind this is ridiculously cheap and so much better than most artifact removal, it renders much of it obsolete.*
> 
> 
> *--Andrew Currall*
> 
> 
> 



[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shattering Spree)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shattering Spree)
Most developers believe [Shatter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shatter) should have cost




R all along, as its effect just isn't worth two mana, especially in a color that is supposedly *good* at destroying artifacts. We may never actually make a one-mana vanilla [Shatter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shatter), though, because the card [Shatter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shatter) still does a fine job of being a baseline effect with a snappy name that we can use in Core Sets every time. But that doesn't preclude us from making other cards with the insight that [Shatter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shatter) is a fair card at R. Granted, even with that bit of knowledge, [Shattering Spree](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shattering+Spree) seems undercosted compared to [Train of Thought](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Train+of+Thought) and [Pyromatics](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyromatics) (as “draw a card” and “deal one damage” are also one-mana effects).


The card is intentionally powerful to be sure. Artifact destruction seemed like a place where we could offer a replicate card to older formats (like Extended and Vintage) without making a card that would turn Standard on its ear. All that said, [Shattering Spree](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shattering+Spree) is not “strictly better” than other playable Red artifact destruction, even though it may be the more correct choice most of the time.



> 
> *Why did you make some of them [Nephilim] 2/2? How awful.*
> 
> 
> *--phodos*
> 
> 
> 


The Nephilim started out pretty darned ridiculous. One iteration that I can remember included an 8/8 with protection from white for UBRG. After all, casting a creature with four colors has to be difficult, right?


In any block other than *Ravnica*, I imagine we could have gotten away with making the Nephilim a lot more powerful, but they fell victim of being in an environment that enables them far too easily. Between [Birds of Paradise](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birds+of+Paradise), [Farseek](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Farseek), [Sakura-Tribe Elder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sakura-Tribe+Elder), and any number of Signets and dual lands, playing a four-color card on turn 3 is easier than it has ever been in Standard, so we had to account for that.


Development's two goals for the cycle were (a) they had to cost “CDEF,” as anything else would not be cool. A mana cost of WUBR is much more attractive than 3WUBR or WWUUBBRR. And (b) the abilities needed to be the cool part, not the size. After all, if all you're after is fat, you can get it elsewhere. So once we had costs and abilities we liked, we set out to tweak power and toughness to where the cards were interesting but not absurd. Ideally, the Nephilim would be an interesting and fun diversion that might show up in tournaments occasionally. (We'd like to keep the focus on the guilds, after all.) So are their stats underwhelming? Yeah, I can see that. But casting them is super easy, and their abilities are all potentially really powerful. I wouldn't write them off just yet.


![](https://media.wizards.com/legacy/magic/images/mtgcom/fcpics/latest/af103_orzhov.jpg)  
*Sometimes the simplest option conveys the message the best.*

> 
> *Out of all of the possible White/Black options for the guildmage, why did you choose one as predictable and easy as how it is now?*
> 
> 
> *--Ed*
> 
> 
> 


Sometimes the simplest option conveys the message the best. Black-White has a theme of “bleeding” your opponent to death, as evidenced on cards like [Pillory of the Sleepless](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillory+of+the+Sleepless), [Blind Hunter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blind+Hunter), [Mourning Thrull](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mourning+Thrull), and [Agent of Masks](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agent+of+Masks). The Guildmage gave us another way to hammer home that theme, just as the [Gruul Guildmage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gruul+Guildmage) forces damage through and the [Izzet Guildmage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Izzet+Guildmage) enables instants and sorceries.



> 
> *1) Why is [Order of the Stars](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Order+of+the+Stars) a defender, rather than costing a bit more and enabling it to attack? I doubt 1W for a 1/1 with protection from the color of your choice is broken.*
> 
> 
> *2) Why was [Repeal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Repeal) printed? Bounce is usually used by spending some mana to make your opponent spend more. (e.g. [Boomerang](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boomerang)ing a 3cc creature means that that you spent 2 mana to make them spend 3. You spent less than them.)*
> 
> 
> *3) Several mechanics seemed as if they were not fully explored. Are you actually planning on revisiting these mechanics, or are they to be left unexplored? (I still want an ability with convoke, a land with transmute, and now I want fancy replicate costs, similar to the [Horobi's Whisper](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Horobi%27s+Whisper) cycle from back in BoK and haunt effects similar to auras (haunted creature gets +1/+1).)*
> 
> 
> *--nepence*
> 
> 
> 



[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Order of the Stars)](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Order of the Stars)
(1) Development is not a matter of finding the broken execution of each card and then pulling back one notch. Sure, one day we might be able to print a 1/1 pro-color-of-your-choice creature for 1W. That card would be darned good—[Beloved Chaplain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Beloved+Chaplain) has seen tournament play, and your suggestion is probably significantly better than that in a large majority of situations. [Order of the Stars](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Order+of+the+Stars) was designed to be a defensive card, and it does a fine job of that.


(2) Bounce normally costs you a card for a bit of tempo—and that's ok judging by this rule you seem to have created about what makes bounce playable. But [Repeal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Repeal) is a different animal completely, as the cost of the card no longer exists. Is it still good? Absolutely. I expect it to be played pretty darned heavily in Standard and Block, and maybe in other formats as well. Hopefully it'll make you rethink your rules.


(3) We intentionally didn't mine all of these mechanics in this block because we didn't have to. With fewer than fifteen cards with each keyword, we felt we could do lots of “baseline effects” that were all still interesting, saving the really big tweaks for the day we revisit them.









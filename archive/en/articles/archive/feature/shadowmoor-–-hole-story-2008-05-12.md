
---
[Link to Wayback Machine](https://web.archive.org/web/20201020022135/https://magic.wizards.com/en/articles/archive/feature/shadowmoor-%E2%80%93-hole-story-2008-05-12)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/shadowmoor-%E2%80%93-hole-story-2008-05-12"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201020022135id_/https://magic.wizards.com/en/articles/archive/feature/shadowmoor-%E2%80%93-hole-story-2008-05-12"
[_metadata_:wayback_capture_timestamp]:- "2020-10-20 02:21:35+00:00"
[_metadata_:description]:- "When I first joined the Shadowmoor development team (codenamed `Jelly` at the time), I wasn't sure what to expect. I had already put in some time on the `Doughnut` (now Eventide) design team, but this was my first development team. I was eager to try my hand at the development side of R&D, if for no other reason than to learn what exactly goes on during a set's development. I was somewhat surprised to learn that much of development is really just a different type of design, wherein many of the same skills get used."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


*Shadowmoor* – The Hole Story
=============================



 Posted in **Feature**
 on May 12, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_AlexisJanson.jpg)
By Alexis Janson




 Alexis Janson is the winner of the original Great Designer Search. After a six-month internship, she moved on to the technology team at Wizards of the Coast but continued to moonlight as a contributing member of Magic R&D. She currently works as a developer on the Magic Online client team. 






When I first joined the *Shadowmoor* development team (codenamed "Jelly" at the time), I wasn't sure what to expect. I had already put in some time on the "Doughnut" (now *Eventide*) design team, but this was my first development team. I was eager to try my hand at the development side of R&D, if for no other reason than to learn what exactly goes on during a set's development. I was somewhat surprised to learn that much of development is really just a different type of design, wherein many of the same skills get used.

To be fair, a lot of the development process is making sure that the power levels of a set are balanced, ensuring each color has a proper mana curve, and adjusting cards that prove to be too strong in FFL play. Yet all of these adjustments are a form of design. Adding one mana to a card's cost may make it fair, but it's not always the best tweak to make, nor is it an automatic decision. Sometimes subtly redesigning an ability is better; other times, balancing power, toughness, or other stats is correct. It takes development skills to recognize that a change needs to be made, but it takes design skills to properly craft a change. A lot of aesthetics go into tweaking cards en route to our desired power and mana curves.

And then, of course, there are times when part or all of a card needs to be completely redesigned.

### Abort, Retry, Improve?

[![Deathmark](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/10E/Deathmark.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Deathmark)Sometimes they are called holes; other times, the cards are marked as CQI, an acronym meaning "Continuous Quality Improvement." Regardless of the term, the card has been marked for death. Although both terms denote a card that needs replacing, CQI is used when where we want to retain some element of the existing card. A card within a cycle, or the only enchantment-removal card at common, or a rare legend representing a major storyline character—these will be marked CQI as a reminder to use parts of the current card as a template for a new card.

The actual reasons for killing a card are as varied as the cards themselves:


> 
> **Power Level** – Sometimes a card proves too powerful in testing, and the card will no longer be interesting at a ‘fair' power level. (such as with an increased mana cost.) A lot of times this decision hinges on who we perceive as the target audience for a card. Increase the cost on a Johnny or Timmy effect, and the card will still be played and enjoyed by many players. Increase the cost on a Spike effect too high, and the intended audience will just scoff at the card's existence.
> 
> 
> There are also effects that we've determined are inherently unbalanced at any cost. **Magic** has enough ways to skip paying a mana cost that even [Gleemax](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Gleemax) would see play if it had a powerful enough effect. Those effects tend to get killed in development.
> 
> 
> **Not Fun** – A lot of development's job is about balancing power level, but this is merely a subset of the true goal: making sure the gameplay is *fun*. Power level is simply one thing we tweak along the way. If playtesters simply aren't enjoying a card, it often gets replaced with something more interesting.
> 
> 
> **Role Playing** – A set can only contain a certain number of cards that say "counter target spell" or "draw N cards." If there are too many cards trying to do the same thing, some of them will be removed to make room for other cards.
> 
> 
> At the other end of the spectrum, there may be a dearth of cards to fill a particular role, and unrelated cards are killed to make room for cards to fill that role.
> 
> 
> This also includes cards that are trying to fill a certain role, but are failing to do it properly. If a card was added to the set to solve a problem (for example, "be a good answer to combo decks") and testing shows it is not doing its job (combo decks are still tearing up the FFL) we will look for a better card to fill that role.
> 
> 
> 

[![Chainbreaker](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/SHM/Chainbreaker.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Chainbreaker)Basically, the development team's goal is to make sure every card is pulling its individual weight as well as fitting into the set as a whole. Sometimes the reason for CQIing a card is subtle. Consider the following group of cards:


> 
> Kithkin Elder  
>  3W  
>  Creature – Kithkin Cleric  
>  2/2  
>  W, T: Prevent the next one damage that would be dealt to target creature or player.  
>  Put a -1/-1 counter on CARDNAME: Untap CARDNAME.
> 
> 
> Goblin Elder  
>  2B  
>  Creature – Goblin Shaman  
>  2/2  
>  T: Target creature gains fear until end of turn.  
>  Put a -1/-1 counter on CARDNAME: Untap CARDNAME.
> 
> 
> Lay Elder  
>  2G  
>  Creature – Elf Druid  
>  1/2  
>  T: Untap target land.  
>  Put a -1/-1 counter on CARDNAME: Untap CARDNAME.
> 
> 
> 

During an early development pass, the black card of this group was CQI'd to find a new ability. Understanding why this was done first requires understanding what purpose the cards were serving. These cards were referred to as "overheaters" because they allowed you to force them beyond their limit in order to get additional uses of their abilities- the cost being a form of permanent damage, like when you overheat an engine. The most interesting gameplay resulted when you would sometimes use their effects normally, and sometimes be tempted into overheating. To achieve this, the decision on when to overheat had to be nontrivial.

See the problem yet? The only time the black overheater would "overheat" was when its ability would (likely) win the game that turn. The decision was trivial—and hence the ability was CQI'd. Subtle design decisions like this are constantly causing cards to be tweaked or even replaced throughout design and development, with the goal of making the set as fun and interesting as possible.

![Cinderhaze Wretch](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Cinderhaze+Wretch)### Swiss Cheese

Development isn't afraid to poke as many holes as necessary in a set in order to get it to where it needs to be. For example, take this early playtest card:


> 
> Quake-icane  
>  (r/g)(r/g)(r/g)  
>  Sorcery  
>  For each R spent to play CARDNAME, it deals 1 damage to each creature without flying.  
>  For each G spent to play CARDNAME, it deals 1 damage to each creature with flying.
> 
> 
> 

Initially, this was a single card attempting to play around in some new design space. The design team quickly turned it into a full cycle, but development found the other four cards in the cycle difficult to keep balanced. Making spells that basically cost ![](https://web.archive.org/web/20160829100442im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/x.gif)Y—scaling in two directions with no additional cost—was proving nearly impossible.

Rather than print a cycle containing one stellar card and four duds, we fell back on a template that was on / off rather than scaled, giving us more knobs to turn and therefore more room for interesting effects. We kept the card above (which you know as [Firespout](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Firespout)) but immediately opened up four holes, leading to a much better cycle of five unique and interesting cards.

![Firespout](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Firespout)### WTB Common White Instant

Now that the holes are created, how do we decide upon cards to fill them? First, we must determine what sort of card should fill the slot. Sometimes this is trivial—we kill a card within a cycle, and we want the new card to fit right back into the cycle. Other times, it's early enough in set development that we just need "a green uncommon." But before settling on just "any red common" or "any rare blue enchantment," development needs to first take a step back and decide if the set has any greater needs to satisfy.

![Shield of the Oversoul](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shield+of+the+Oversoul)To give an example, I need to sidetrack for a second. A lot of *Shadowmoor*‘s gameplay centers around color. This theme was present all the way back to the initial design, including a number of cycles that specifically made two colors matter. The poster child for this motif was [the common Aura cycle](http://archive.wizards.com/%20http://ww2.wizards.com/Gatherer/index.aspx?term=as%20long%20as&Field_Rules=on&setfilter=Shadowmoor&colorfilter=Multi-Color&typefilter=Enchantments). Development loved how these cards pushed you to play lots of hybrid cards, and they were also simply tons of fun to play.Since the Auras would often win the game unanswered, we wanted to make sure there were enough common solutions for them. Note that this cycle of Auras was in the set in addition to an extremely strong uncommon in Armored Ascension and the standard Aura variants you would expect to see in a large set, such as [Pacifism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism) ([Prison Term](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prison+Term)), Control Magic ([Biting Tether](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Biting+Tether)), and [Dehydration](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dehydration) ([Curse of Chains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Curse+of+Chains)). A glance at the set revealed that there were no commons in white to deal with enchantments—a glaring hole, to be sure.

This led to the following description, a direct quote from Aaron Forsythe's hole request e-mail:


> 
> **CW13**  
>  Enchantment removal of some sort. Shouldn't cost one mana. Auras are quite powerful in this set, especially in limited, so something I wouldn't be embarrassed to maindeck once in a while would be nice.
> 
> 
> 

Can you guess what card this eventually led to? Click here.
![Strip Bare](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Strip+Bare)



### Calling All Cards

"But wait," you say. "Hole request e-mail? Tell me more!"

Often, a new card is designed on the spot by the team. Perhaps we've recently identified something the set needs, and we quickly come up with a card to fill this need. If nothing good is suggested, though, we send out for help. An e-mail is sent out to most of R&D, containing descriptions of all the cards we are looking for. The lead developer compiles the submissions into a large, anonymized document, and the development team convenes for a hole-filling meeting.

[![Revelsong_Horn](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/SHM/Revelsong_Horn.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Revelsong%2BHorn)Hole-filling leads to some of the most interesting meetings during development. A lot of great ideas go through what is probably the most rigorous process possible for a card to see print. Each hole typically has a page full of submissions, from which normally only a single card will see print. We usually start by culling this list of submissions down to [Cream of the Crop](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Cream%2Bof%2Bthe%2BCrop). Some common reasons a hole submission might get rejected:

* It's too similar to another card in the same set. You might be surprised how often this comes up—not only is it easy to accidentally step on another card when designing hole submissions, but almost any collision is almost immediately noted by at least one developer.
* It's too similar to another card in the same block or in the previous block (same Standard environment).
* It does something that enough cards in the set already do.
* It requires a problematic template. While card designers don't normally worry about templates, there are a number of standard card templates that we try to avoid because they are confusing or nonintuitive, or because they tend to lead to rules-lawyery situations where one player insists some subtle timing trick works in their favor and the other player has never even heard of the appropriate rules.
* It doesn't match the concept or art already allocated to the card.
* It doesn't match requirements for the hole, such as being part of a cycle, being a common or rare card, etc.
* It doesn't fit in with what the set is trying to do, or possibly actively goes against the set's themes.
* It's simple enough to fit in any set, and we'd rather have a card that fits in with the set's themes.

Once the submissions for a given card are culled to the best choices, there are usually still several highly inspired and unique submissions for each hole. Some of our best and most creative cards come from hole submissions. What typically follows is a flurry of debate, regarding not only which submission to use and why, but possible changes to address the concerns of other team members. Sometimes two or more cards get merged into one, or multiple submissions are so great that other cards are bumped from the set to make room. A great idea buried in a submission might become the inspiration for an entirely new card designed on the spot by the hole-filling team.

Let's look at a couple of final examples!

### Thinking Outside the Block

![Mercy Killing](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mercy+Killing)From the hole-request e-mail:


> 
> GW hybrid needs:  
>  [...]  
>  Another uncommon, preferably not a creature. Try to work some token-making into this card or the previous one.
> 
> 
> 

This card is part of one of my personal crusades. You see, I've always been bothered by how green is the only color that basically gets no removal. Red can burn things out of the way; black just kills them; blue counters, bounces, or steals them; white uses [Pacifism](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pacifism) or [Chastise](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chastise) effects. Green simply can't kill a creature that it can't get in a fight with. With that in mind, I keep trying new green-flavored ways to kill things whenever an appropriate hole comes up. [Mercy Killing](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mercy+Killing) is one such attempt—keep an eye out for more in upcoming sets. I'm not particularly concerned with finding a permanent addition to green's color pie—it's more about the journey, trying a bunch of different interesting and flavorful solutions to green's big weakness.

Hole-filling is often a good chance for one-of niche or "secret agenda" cards to sneak in. Every set has a certain quota of cards that don't have to closely follow the set themes, and those are perfect places to try one-ofs that are testing out new ideas. Since holes come from so many sources, it's no coincidence that many of these cards get into sets during hole filling.

In a related vein, sometimes the team gets [Tunnel Vision](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Tunnel%2BVision) and has trouble coming up with cards outside of the set's boundaries. Hole submitters bring a fresh perspective, designing cards that go in new and yet beautifully synergistic directions- or, in some cases, just submitting amazing unique ideas that have absolutely nothing to do with the set specifically.

### Putting It All Together

![Reaper King](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Reaper+King)From the hole-request e-mail:


> 
> Artifact needs:  
>  [...]  
>  A rare "Scarecrow Lord." Scarecrows are a new tribe, and they need a tribal card to bring them together. Many of them deal with color somehow--take a look at the artifact creatures in the set to see what they might need from a king.
> 
> 
> 

For this hole, a lot of the submissions played around with artifacts and colors. For those who are unfamiliar with the set, *Shadowmoor*'s [Scarecrows](http://archive.wizards.com/%20http://ww2.wizards.com/Gatherer/index.aspx?term=scarecrow&Field_Type=on&setfilter=Shadowmoor) are all artifact creatures; in addition, a lot of them [modify](http://archive.wizards.com/%20http://ww2.wizards.com/Gatherer/index.aspx?term=colors&Field_Rules=on&setfilter=Shadowmoor&typefilter=Artifacts&output=Spoiler) or [care about](http://archive.wizards.com/%20http://ww2.wizards.com/Gatherer/index.aspx?term=as%20long%20as&Field_Rules=on&setfilter=Shadowmoor&typefilter=Artifacts&output=Spoiler) the colors of permanents you control.

[![Lurebound_Scarecrow](https://media.magic.wizards.com/image_legacy_migration/magic/images/cardart/SHM/Lurebound_Scarecrow.jpg)](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Lurebound%2BScarecrow)Visually, the Scarecrows themselves are cobbled together from a variety of objects, so it is oddly appropriate that the [Reaper King](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reaper+King) was also cobbled together from no less than four ideas. Several submissions had the expected "Scarecrows get +1/+1" line, and that was deemed a good base. Ken Nagle's submission was off-the-wall as usual, with a crazy ![](https://web.archive.org/web/20210429201911im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2-white.gif)![](https://web.archive.org/web/20210430014203im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2-blue.gif)![](https://web.archive.org/web/20210426153733im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2-black.gif)![](https://web.archive.org/web/20210430014037im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2-red.gif)![](https://web.archive.org/web/20210430014203im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2-green.gif) mana cost, and it seemed so ridiculous that we had to try it. Other submissions had the "CARDNAME is all colors" text that allowed the lord to turn on all the "color matters" Scarecrows, but this mana cost accomplished that and more.

We needed a final ability, and we liked the idea (from yet another submission) of triggering off other Scarecrows coming into play—but the team wanted an effect with some impact. I jokingly shot out "[Vindicate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vindicate)," and Aaron Forsythe let out a devilish cackle, writing the final ability down with glee. The new card quickly became one of our favorite cards in the set. We hope you like it as much as we did.

### From Hole to Whole

And that's the whole story: how a bad card becomes a hole, and how a hole becomes a shiny new card, ready for playtesting. Now if you'll excuse me, "Scissors" just cut some holes in "Paper," and I have some work to do...








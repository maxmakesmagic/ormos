
---
[Link to Wayback Machine](https://web.archive.org/web/20150402060341/http://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-card-codes-2009-01-12)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Ninety-five percent of all crimes portrayed on television are felonies while five percent are misdemeanors. That happens to be almost exactly opposite of reality. So why does television do it? Because murder just makes for a more compelling story than jaywalking. The result of this, though, is that it skews people's image of the world. The world is a dangerous place, television teaches us; just look at all the serious crime going on."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "352836"
[_metadata_:publish_date]:- "2009-01-12"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Nuts & Bolts: Card Codes"
[_metadata_:wayback_capture_timestamp]:- "2015-04-02 06:03:41"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150402060341id_/http://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-card-codes-2009-01-12"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/making-magic/nuts-bolts-card-codes-2009-01-12"
---


Nuts & Bolts: Card Codes
========================



 Posted in [Making Magic](/en/articles/columns/making-magic-archive)
 on January 12, 2009 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 





Ninety-five percent of all crimes portrayed on television are felonies while five percent are misdemeanors. That happens to be almost exactly opposite of reality. So why does television do it? Because murder just makes for a more compelling story than jaywalking. The result of this, though, is that it skews people's image of the world. The world is a dangerous place, television teaches us; just look at all the serious crime going on.


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_guiltfeeder.jpg)


I bring this up because I feel Making Magic is equally guilty of such a misrepresentation. I spend the vast majority of my "behind the scenes" time talking about designing cards or discussing color philosophy. While this is essential to the process, it is actually the minority of what goes on in design. The majority of the time is spent on the little details, the nuts and bolts if you will. To use another metaphor: the architect spends far less time than the builders who have to come in and make the house happen. More time is spent painting walls or driving nails than is ever spent at the architect's drafting board. The same is true for card design.


This realization has inspired me to start a new feature that I'm calling "Nuts & Bolts." In these columns I'm going to take some little pesky detail which is essential to our process and walk you through all that it entails. The idea is to give you a glimpse of the importance of the little stuff. One of the steepest learning curves for new R&D members is absorbing all of the bits and pieces about what things have to happen to make the whole process work. For these articles I'm going to assume you know nothing, because I'm honestly not sure what parts you might have picked up versus which things you had no idea about.


### Cracking the Code


Today's topic is card codes. As I said above—mundane but essential to our process. So what is a card code? Many times in this column I've shown you a playtest card. For example:


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_playtest1.jpg)

See that sequence of letters and numbers?


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_playtest2.jpg)

This one. This is what I'm talking about. This is a card code. I guess we'll start at the very beginning.


### What Is a Card Code?


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_bingo.jpg)

A card code is a series of letters and numbers (specifically two letters followed by two numbers) that is used as a distinction for R&D, and other internal sections of the company, to identify a particular card.


### Why Do We Need It?


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_split.jpg)


In real life, players use the card title as a means to refer to a particular card. If the world wants to talk about the green instant that cost ![1 Mana](https://web.archive.org/web/20170413165508im_/http://archive.wizards.com/images/Symbols/Symbol_1_mana.gif)![Green Mana](https://media.wizards.com/legacy/images/symbols/green_mana.gif) and says "Destroy target artifact or enchantment," they get to use the label Naturalize. That works because printed cards are constants. Naturalize will always mean the same thing. (Well, there is the issue of errata, but let's skip that for now.) In design and development though, cards are in flux. The name constantly changes. Many cards go through various design names. Then the creative team tends to change it to a name suitable for sending out to the artist. Then comes the actual name which also can change once or twice depending on different factors.


You can even forget about the name. In design and development, more often than not the entire card changes, sometimes to a completely different card than what started. R&D cannot think in terms of a particular card. Instead we think about a slot. For example, a small set has sixty commons. Let's say there are only monocolor cards and no lands or artifacts at common. That means that each color would have twelve slots (sixty divided by five for those math impaired). As far as R&D is concerned, common white has twelve slots.


The point of the card code is that it labels not any one particular card but a particular slot. Cards can come and go but CW01 will always be the first card (collector numberwise at least).


### So what do the letters and numbers mean?


Let's break it down. Since I just used CW01 as an example, let's just use that:


CW01
====


This code has three distinctive pieces of information—


C — W — 01
==========


—the first letter, the second letter and the two digit number. I'm going to walk you through each one as well as fill you in on what options are available for each.


### First Letter


The first letter is the card's rarity. Rarity is important, because for production purposes, different rarities tend to end up in different places. (I'm not getting into how production makes cards, but how R&D handles the information.) Thus the first function of a card code is to let everyone know a card's rarity. So how many rarities does **Magic** have? Seriously, see if you can guess. Once you've made a guess, move on to the next paragraph.


Did you say three? Well then, you've forgotten about *Shards of Alara*'s introduction of mythic rares.


Did you say four? Well then, you've forgotten that large **Magic** sets actually have five rarities and not four. What's the fifth rarity? Basic land. They exist at a rarity more common than common.


Did you say five? Well, then you've forgotten that from time to time **Magic** adds other rarities such as with the *Time Spiral* "timeshifted" sheet.


Did you say six? Well then you've forgotten that there are cards in the booster pack with card frames and art other than tournament legal cards. Yes, the token cards. They have their own rarity. (In fact, token cards have various effective rarities, but for card code purposes they are listed as a single rarity.)


Yes, currently in Magic card codes there are seven options for the rarity field:


C – common


U – uncommon


R – rare


M – mythic rare


L – land (This refers only to basic lands; all other lands fit into one of the above four rarities.)


T – token


S – special (This includes things like the *Time Spiral* timeshifted sheet and Super Secret Tech from *Unhinged*; note that *Time Spiral* design originally used "B" for "bonus sheet"—we had no precedent so I just used a letter of my choosing—but that it was officially changed before the set was officially shipped off to production.)


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_rarities.jpg)
### Second Letter


So what does the second letter represent? Did you say color? Sorry, wrong. The second letter actually represents the card frame. Well, at least that's how the card code started. The second letter tells the production people what frame the card needs.


I should point out that card frames have become a lot more complicated since Alpha. Multicolored cards of exactly two colors now have distinctive looks, lands that produce one or two colors of mana have piping to remind you what color they produce, and *Ravnica* introduced things like guild watermarks. Production can no longer depend solely on the card code for the frame, but it is there to at least give a general hint.


Here are the current available letter codes for the second slot:


W – white


U – blue


B – black


R – red


G – green


Z – multicolor


X – split cards (That's split cards that aren't monocolored; the mono-red ones in *Planar Chaos*, for example, just used R.)


A – artifact (This is for traditional colorless artifacts; colored artifacts, except for Transguild Courier and Reaper King, use the appropriate color code.)


L – land


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_confused.jpg)


Before I move on, I want to talk about blue. Us old timers might have forgotten that it's weird that U means blue, but I know it throws new players for a loop the first time they see it. So why is blue U? For the card code to work, each letter had to be unique within each designation (although it's fine for the same letter to mean something different between the first and second letter—that's why U is both blue and uncommon and R is both rare and red). Blue and black both start with a "B." This meant that one of them had to choose a new letter.


The second letter for both colors is "L". As I showed above, "L" means land. The powers that be wanted to use the first letter whenever possible, so land got to keep "L." Black's third letter is "A." A is reserved for artifacts. This meant that Blue had "U" and "E" and Black had "C" and "K." (In the early days before Wizards spelled it out, incidentally, some players used "K" for black.) Why did we end up going with U? Basically because it was earlier in it's word than Black's "C" or "K."


One final note, the frames listed above are in the order that they are listed in the files. Monocolor (in WUBRG order—meaning white / blue / black / red / green and pronounced "wooberg" in R&D speak) comes before multicolor which comes before split cards which comes before artifacts which come before land.


### The Two-Digit Number


The rules for the number are pretty short:


**#1 – The digit is always two numbers.** The major reason for this rule is simple; it helps you know that no information is missing. If you see CW1, you don't know whether it is the first common white card or perhaps the tenth and the 0 was left off. With the current system you always know when you have all the information. The biggest ramification of the rule is that the first nine cards are always 0\_ such as 01 or 09.


**#2 – The numbering always starts at 01.** The key value of this number is to tell you how many slots exist within a certain rarity/frame combination. Whatever the highest number is lets you know how many cards exist in this subsection. This information is very handy and commonly referenced by design and development.


**#3 – The order, from a production standpoint, is arbitrary.** As long as common white has twelve cards, it doesn't matter which one is assigned to which card. Which is all well and good, except one thing: R&D has it's own little sub-rules about this:



> 
> **A – Creatures come before non-creatures.** One of the things that design and development is constantly checking is to see how many creatures are in a certain color in a particular commonality. To help us with this process, we always clump creatures together in the first part of the numbering.
> 
> 
> **B – Cycles get grouped at the same number.** To help find cycles, one of the tricks is to list them all at the same card number. For example, we have a cycle of 1/1s for C (that means one mana of the relevant color), so we put them all in the 01 slot. We're not always super vigilant about this rule, although we will always do it if able. Rule A above sometimes causes us headaches alongside this rule because the split between creatures and non-creatures varies between colors.
> 
> 
> 


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_cycle.jpg)


> 
> **C – Cards vying for the same slot get numbered the same.** One of the tricks R&D uses is to put multiple cards in the same card code slot as a way to say "These cards cannot both go into the set so we're trying them out." This keeps the lead designer from constantly getting comments that the cards are too close.
> 
> 
> **D – Cards are listed in their subsection (creature/non-creature) from cheapest to most expensive.** This is another one that isn't always done at any one time, but whenever a lead cleans up a file it's a nice way for the team to see how the set's curve is looking.
> 
> 
> **E – Cards in single-frame cycles (most often artifacts and lands) are put in consecutive order, always in WUBRG order.** Cycles that can be grouped together consecutively are listed as such meaning almost all artifact and land cycles are clumped consecutively. In addition, everything that can be is done in WUBRG order. When you are making a cycle of lands or color relevant artifacts, that doesn't change.
> 
> 
> 


When R&D hands off a file to editing, the card codes are always consecutive, but R&D has come up with a few two-digit codes that mean additional things. These codes are only used during design and development and are always gone before the file goes to anyone else. These codes are:


**99 –** This is the most commonly used code. It means that a card has been cut from the set but that we aren't convinced it might not come back in. "99ing a card" is actual R&D slang for something has been removed. ("Where's Fat Elf?" "99ed.")


**88 –** This means that a card is not yet officially in the file but that we are potentially looking for a place to put it. It differs from 99 in that an 88 is potentially on its way in rather than its way out.


**33, 44, 55, 66, 77 –** In design, I assign these codes to different designers on the team (one unique code per designer). When then input potential cards they use their code. That lets me know which team member submitted which card.


![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_designers.jpg)

**00 –** This code is used for general notes. Most often the code is CW00 such that it appears as the first thing in the file but on rare occasions, people have stuck in 00 notes before a particular section.


**10, 20, 30, 40, 50 –** This final creative use of numbering came from *Shadowmoor* design and development. When hybrid first showed up in *Ravnica*, the cards just used the Z code and all was well. After all, there were only twelve hybrid cards in the file. But when we started working on *Shadowmoor* we found we had a problem. When half the set is hybrid, that meant half of the set had a code of Z. How could design and development tell apart ![White or Blue Mana](https://web.archive.org/web/20150921022954im_/http://archive.wizards.com/images/Symbols/Symbol_WU_mana.gif) hybrid from ![Blue or Black Mana](https://web.archive.org/web/20150914235220im_/http://archive.wizards.com/images/Symbols/Symbol_UB_mana.gif) or ![Black or Red Mana](https://web.archive.org/web/20170413174345im_/http://archive.wizards.com/images/Symbols/Symbol_BR_mana.gif) or ![Red or Green Mana](https://media.wizards.com/legacy/images/symbols/symbol_rg_mana.gif) or ![Green or White Mana](https://web.archive.org/web/20150921045836im_/http://archive.wizards.com/images/Symbols/Symbol_GW_mana.gif)? As I explained above, having clear subsets is crucial for design and development to do our jobs. The solution was to have all ![White or Blue Mana](https://web.archive.org/web/20150921022954im_/http://archive.wizards.com/images/Symbols/Symbol_WU_mana.gif) cards have their card number in the 10s, ![Blue or Black Mana](https://web.archive.org/web/20150914235220im_/http://archive.wizards.com/images/Symbols/Symbol_UB_mana.gif) in the 20s, ![Black or Red Mana](https://web.archive.org/web/20170413174345im_/http://archive.wizards.com/images/Symbols/Symbol_BR_mana.gif) in the 30s, ![Red or Green Mana](https://media.wizards.com/legacy/images/symbols/symbol_rg_mana.gif) in the 40s, and ![Green or White Mana](https://web.archive.org/web/20150921045836im_/http://archive.wizards.com/images/Symbols/Symbol_GW_mana.gif) in the 50s. This way whenever a member of R&D looked at the *Shadowmoor* file, they could instantly know which hybrid combination they were looking at. The same system was then used in *Eventide* with the enemy hybrid combinations shifted in.


### Code Red (and White and Blue and Black and Green)


[![](https://media.wizards.com/legacy/mtg/images/daily/mm/mm21_orb.jpg)](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/arcana/98)


And that is everything there is to know about card codes.


My goal today was to demonstrate how a little dinky thing is actually a vital, important design and development tool—so much so that an entire structure and language has been built around the card codes.


Let me end today's column by asking this: did you like today's column? Do you enjoy hearing about the minutiae that makes the design behind the game tick? Or was it boring and not worthy of a column? Should I forget the jaywalking and stick to murder? I'm very curious, because I don't know whether this is the kind of thing people want to read about. I wrote it because I felt the only way to know was to create such an article and then see what kind of feedback I got. So time for feedback! Nuts & Bolts—stay or go as a recurring feature?


Join me next week when Conflux previews begin and we start giving you a taste test. If you can’t wait, I’ll point out that [the *Conflux* Orb of Insight](http://archive.wizards.com/magic/magazine/article.aspx?x=mtg/daily/arcana/98) is up and ready to play with.


Until next week, may you learn that little things mean a lot.








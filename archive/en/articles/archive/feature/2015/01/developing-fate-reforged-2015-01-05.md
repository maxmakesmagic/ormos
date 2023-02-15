
---
[Link to Wayback Machine](https://web.archive.org/web/20150107180953/http://magic.wizards.com/en/articles/archive/feature/developing-fate-reforged-2015-01-05)

[_metadata_:author]:- "Dave Humpherys"
[_metadata_:description]:- "Fate Reforged offered a unique challenge as a small set for development."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "322236"
[_metadata_:publish_date]:- "2015-01-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Developing Fate Reforged"
[_metadata_:wayback_capture_timestamp]:- "2015-01-07 18:09:53"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20150107180953id_/http://magic.wizards.com/en/articles/archive/feature/developing-fate-reforged-2015-01-05"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/feature/developing-fate-reforged-2015-01-05"
---


Developing Fate Reforged
========================



 Posted in **Feature**
 on January 5, 2015 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_davehumpherys.jpg)
By Dave Humpherys




Dave Humpherys has been managing the development team for Magic R&D since 2010. He led development for the Avacyn Restored and Gatecrash sets. He was inducted into the Magic Pro Tour Hall of Fame in 2006. 






 Let me start by introducing the *Fate Reforged* Development Team:




![](https://media.wizards.com/2014/ujehvsbfrf153/FEAT20150105_Dev_Humpherys.png)



**Dave Humpherys:** That's me. I manage the development team in *Magic* R&D. My team, along with Erik Lauer heading the technical side of our process, is ultimately responsible for the health of the Constructed and Limited formats. Someone on my team is generally in charge of leading a set's final design. I've personally led a number of sets recently and, once *Dragons of Tarkir* releases I'll have led (or co-led, in the case of *Dragons of Tarkir*) four of the past six paper booster releases, including *Journey into Nyx* and *Conspiracy.* I also previously led *Gatecrash* and *Avacyn Restored*.





---


![](https://media.wizards.com/2014/ujehvsbfrf153/FEAT20150105_Dev_Duke.png)



**Ian Duke:** If you enjoyed *Vintage Masters* on *Magic Online* this year, you can thank Ian for leading the development of that set. You've also seen Ian's work this year in the form of *Commander* (2014 Edition). Ian ran a mini-team during development for the Pledges, which would become known as the Sieges, which are enchantments where you choose to side with either Khans or Dragons. This cycle was especially challenging, given he had to dodge enchantments from an enchantment block and the Ascendancies in *Khans of Tarkir*. Ian's group provided a lot of great ideas for this cycle and I'm particular happy with how each of the Sieges turned out.





---


![](https://media.wizards.com/2014/ujehvsbfrf153/FEAT20150105_Dev_Gottlieb.png)



**Mark Gottlieb:** Mark is my counterpart on the design side of R&D, managing that team. Mark, an R&D veteran, has worn a few different hats (including rules manager) and he was briefly a developer on my team. Mark is on a lot of design teams, leading a number of them, most recently co-leading *Gatecrash* and leading *Dragons of Tarkir*. His knowledge of the set following *Fate Reforged* was particular invaluable in making this all come together. He's also been on quite a few development teams. Mark led a mini-team for the cards supporting the wedges in *Fate Reforged.* As with the other mini-teams, I'm very happy with how his team's work turned out. His team improved upon a number of designs and created new cards that polished up the two cycles of creatures with hybrid activations in *Fate Reforged*.





---


![](https://media.wizards.com/2014/ujehvsbfrf153/FEAT20150105_Dev_Hayes.png)



**Ben Hayes:** Ben is a relative newcomer to the development team. While R&D has been doing Future Future League (FFL) testing for ages, Ben helped me set up a process whereby we have a dedicated FFL team for each set. That process kicked off beginning with *Khans of Tarkir* and Ben led that inaugural team. You can thank him, in part, for the variety of decks appearing for each of the *Khans of Tarkir* clans, as well as a number of other decks that continue to pop up. He also helped Adam Prosak lead this FFL team for *Fate Reforged*. I'll also note here thanks to Tim Aten, Bryan Hawley, Gerry Thompson, and Gavin Verhey as others on the *Fate Reforged* FFL team that made this set possible. I think we've had some of our best FFL testing with the recent sets in large thanks to these guys.



Ben was in charge of a mini-team during development that focused on the design of the [Ugin Planeswalker in the set](/node/321776), and I relied very heavily on the work that mini-team produced for the card, in particular the mirroring of the ultimate on Nicol Bolas. And the basis for Ugin's equally splashy -X ability.




---


![](https://media.wizards.com/2014/ujehvsbfrf153/FEAT20150105_Dev_Spain.png)



**Ryan Spain:** Ryan manages the R&D side of *Magic Online*. Given his passion for Limited, as evidenced by his cofounding the [Limited Resources](http://lrcast.com/) podcast, I was happy to have Ryan helping out with the two draft formats that *Fate Reforged* shapes. Ryan has been on a couple of design and development teams, including *Modern Masters* development. Ryan tackled a mini-team that focused on ensuring our set delivered on satisfying designs for tropes related to that fact that we'd traveled back in time.





---

A Crossroads
============



*Fate Reforged* offered a unique challenge as a small set for development. It first needed to play well in Limited, in particular to draft well as Fate-Khans-Khans at launch, then later draft equally well with *Dragons of Tarkir* launch as a Dragons-Dragons-Fate draft. Developing the set to play well in both of these environments was daunting, and then on top of that we wanted to include many cards that would feel and play differently in each draft environment. We wanted cards that would be prioritized differently, that would have new significance, and that would interact with the evolving mechanics in novel ways. I felt it would be hard to get our players excited about this comparison, though, since when *Fate Reforged* releases there's only one draft experience and the payoff comes months later on a lot of the more subtle work we put into the set. So I also knew we had to immediately deliver well on the set itself.



And what did we need to do to achieve that? These were among my main goals:


* Evolve the metagame while building up the clan decks.
* Deliver a great *Khans of Tarkir/Fate Reforged* Limited experience.
* Play up ***choice*** and make sure that our cards involving choice were fun.
* Introduce exciting Dragons to support rather than step on the toes of the next set.
* Make an awesome and relevant Ugin.

Hybrid Vigor
============



 As *Fate Reforged* was taking shape, *Khans of Tarkir* development was going full speed, doing its best to do everything three-color "wedge" it could: charms, [Woolly Thoctar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar) variants, enchantments, lands, and splashy endgame cards like [Villainous Wealth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Villainous+Wealth) and [Duneblast](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Duneblast). Would we be able to find exciting, unexplored space for these decks without making three-color gold cards?




 In terms of building up clan decks, I was very excited when we started talking as a design team about using hybrid mana. Since [hybrid mana first appeared](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&text=+~[m/%28g\/w%29/]&set=+[%22Ravnica:%20City%20of%20Guilds%22]), I've always seen it as a great way to increase the number of decks a card might otherwise be played in without going all of the way to a generic effect or card. While colorless artifacts or lands with colorless activations certainly have their place in the game, there's always a very real danger that these become nearly ubiquitous. Take, for example, the many [Swords](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&type=+[artifact]&name=+[sword]) in *Magic*'s history, or [Mutavault](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mutavault). If there are too many competitive cards in this space, too many decks can start looking alike and playing alike. These cards act in a way that ignores the colors of *Magic* that we've all come to love. While hybrid is generally more complicated for newer players to understand than colorless mana, it dodges a number of the concerns I've listed here. My enjoyment of this mechanic was renewed when I led *Gatecrash* and saw the role and impact of cards like [Boros Reckoner](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boros+Reckoner) and, later, [Nightveil Specter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightveil+Specter) with the arrival of devotion.




![](https://media.wizards.com/2014/ujehvsbfrf153/40x9x0w4n5_cardart.jpg)



 Art by [Ryan Alexander Lee](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=[%22Ryan+Alexander+Lee%22])



I'll note here that we did explore using hybrid mana in the casting cost of spells. I was concerned, though, that there was already a lot going on in this block. Six mechanics with each set and the overall narrative of the block meant that I didn't want to introduce this complication unless we really needed to. And in the end I felt like the ten cards with hybrid mana activations were doing more than enough.


The designs with hybrid activation let us create a given card that was not only good in three-color clan deck but also in two different two-color decks. Consequently, these card designs lend themselves to more flexibility in which decks they can go in, and thus more options for deck building.


Because you can put these cards on the board for only one color, these cards also put less pressure on a player to immediately get all three colors of mana. The powerful cards in these two cycles lessen achieving optimal mana as a deciding factor in some number of games.


Since we are using hybrid mana activations on all of these, they also provide mana sinks for their respective clan decks. Not all of the clan decks had good ways to make use of excess mana in Constructed, especially since many of their cards' power are based on getting the correct mana early in the game.


Warden of the First Tree
========================



 It so happens that I was also on the [design team for *Fate Reforged*](/node/321031). My role on design teams ends up being less prolific in designing cards and more focused on nudging the ship's course so development will be able to reach its destination. There was one card, however, that I was particularly fond of that I designed during the design phase and that survived largely intact to the final file.




 By putting hybrid activations on a card with only one color in its casting cost, we could accomplish another thing I didn't mention above: We could make powerful clan cards with a gold feel that didn't need to cost three or more mana. [Three-color gold cards](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&set=[%22Khans+of+Tarkir%22]&cmc=+%3E=[3]&color=+^%28|[W]|[B]|[R]|[G]%29) in Khans all cost three or more mana by default. This left us with room to make one- or two-mana cards



My inspiration for the card we show you today was [Figure of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny). Yes, that [Figure of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny), the tournament powerhouse. I hope that alone already has you excited.


I was designing five cards, one for each of a cycle of cards with hybrid activations. First, I asked myself which of the clans would make most sense to have a card that levels up over time like [Figure of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny). The Abzan felt most fitting for a creature that was investing a lot of time and effort to become more and more powerful, so they are the lucky recipient of today's [Figure of Destiny](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Figure+of+Destiny) variant preview.


I submitted this card as a one-mana creature with four activated abilities that cost two, four, six, and eight mana total. I designed it so you could play these abilities in any order. The last of the four abilities was the only one that stacked with itself and it could be used any number of times. Testing of the card, however, suggested that tracking what the card had done thus far was too hard to remember and so we reworked the card to look even more like the card that inspired me.



![](https://media.wizards.com/2014/ujehvsbfrf153/en_cpyhzk81s2.png)


As always, thanks for reading,


Dave Humpherys

 





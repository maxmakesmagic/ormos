
---
[Link to Wayback Machine](https://web.archive.org/web/20221017164316/https://magic.wizards.com/en/articles/archive/making-magic/unfinity-gauntlet-part-3-2022-10-17)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Mark wraps up his card-by-card stories from the design of Unfinity."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1608122"
[_metadata_:publish_date]:- "2022-10-17"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Unfinity Gauntlet, Part 3"
[_metadata_:wayback_capture_timestamp]:- "2022-10-17 16:43:16"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20221017164316id_/https://magic.wizards.com/en/articles/archive/making-magic/unfinity-gauntlet-part-3-2022-10-17"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/unfinity-gauntlet-part-3-2022-10-17"
---


The Unfinity Gauntlet, Part 3
=============================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on October 17, 2022 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






[Last week](https://magic.wizards.com/en/articles/archive/making-magic/unfinity-gauntlet-part-2-2022-10-10) and [the week before that](https://magic.wizards.com/en/articles/archive/making-magic/unfinity-gauntlet-part-1-2022-10-03), I told card-by-card design stories about *Unfinity*. Today will be my third and final installment.


**Pair o' Dice Lost**


![Pair o' Dice Lost](https://media.wizards.com/2022/unf/en_c1z8YCjYsC.png)


In most *Magic* sets, we'll design some cards with a name in mind, but nothing is written in stone until the naming pass. *Un-* cards, because they're a little more holistic in nature and tend to have more fun with their names, will sometimes commit to a name early, which impacts how we choose to concept the card. Pair o' Dice Lost is a good example. I made this card early in vision design with this name. When we got to card concepting, I asked if we could concept to the name, which we did. So, we got back art focused on two abandoned fluffy dice (prizes from the park). When we got to naming, I said to Ari (Zirulnik, who led names and flavor text), "You can look for other names, but I think it's going to be hard to find something that works as well." Ari laughed and said, "Yeah, I don't think we're changing this name."


**Rat in the Hat**


![Rat in the Hat](https://media.wizards.com/2022/unf/en_CHRvXk30js.png)


The slot Rat in the Hat was designed to fill a common creature card for the white-black "hats matter" draft archetype. The first stab was a discard card, one that scaled based on how many hatted creatures you had:


**Rat in the Hat (version #1)**  

1B  

Creature — Rat  

1/1  

When CARDNAME enters the battlefield, target opponent reveals a number of cards from their hand equal to the number of creatures you control wearing a hat in their art. You choose one of those cards. That player discards that card.


Next, we tried one that drained life:


**Rat in the Hat (version #2)**  

1B  

Creature — Rat  

1/1  

When CARDNAME enters the battlefield, target opponent loses 1 life for each creature you control wearing a hat in its art.


The problem with both designs is that they got so much more powerful if you were playing a lot of hat-wearing creatures. That's usually fine for uncommon, but we tend to like our common cards to be more what R&D calls Threshold 1. Threshold 1 is a card that only needs one card of the group you're mechanically caring about to work. Having more of the group you're caring about allows you more options but doesn't significantly raise the power level of the card.


Also, we were starting to figure out the play pattern of the "hats matter" deck, and we realized we wanted it to have a graveyard-recursion element, so we changed Rat in the Hat to get a hatted creature back from the graveyard to your hand:


**Rat in the Hat (version #3)**  

1B  

Creature — Rat  

1/1  

{1B}, {T}, Sacrifice CARDNAME: Return target creature card wearing a hat from your graveyard to your hand.


Other than the change from "wearing a hat" to "has a hat" (a bunch of the art had characters holding hats but not wearing them), this card basically stayed the same for the rest of the design. That is, until we made one big shift. When we decided to make most of the sticker cards Eternal legal, we had to make them return to the sticker sheet if they went to the hand or library. The rules couldn't handle stickers staying on in non-public zones. This change only affected a handful of cards, but Rat in the Hat was one of them.


While many creatures naturally have hats in their art, we made stickering hats a big part of the "hats matter" strategy. Rat in the Hat would let you put a creature with a hat sticker from your graveyard into your hand, but the hat would then fall off, which worked against the largest strategy of the archetype. Was there a way to keep Rat in the Hat's basic function, but in a way that would work with the "hats matter" strategy?


It turns out there was. Instead of returning the hatted creature to your hand, it now let you cast that creature out of your graveyard, thus allowing you to keep its hat sticker. This now functioned similarly to putting it in your hand, assuming you cast it that turn. To help facilitate this, we took the mana activation cost off Rat in the Hat so you could spend your mana casting your hatted creature in the graveyard. We also changed it from a 1B 1/1 to a B 1/2.


**A Real Handful**


![A Real Handful](https://media.wizards.com/2022/unf/en_0eINeomunC.png)


This card is a great example of how one little change can make all the difference. Here's the first version:


**Meek Minion (version #1)**  

1BB  

Creature — Human Employee Minion  

1/1  

As long as a hand is touching your back, CARDNAME is a 3/3 creature.  

As long as two hands are touching your back, CARDNAME has menace.  

As long as three hands are touching your back, CARDNAME has lifelink.


You see, the first card required someone to be touching you instead of the card (your back specifically). This freaked numerous playtesters out. ("I don't want people touching me.") We spent a lot of time talking about if certain places were better for people to be touching. What if it was your shoulder? Or your head? Or your shoe?


In the end, this was the correct answer: don't make people have to touch you. We found we could capture the essence of the card by having a second person come help you (inspired by the success of *Unstable*'s [Handy Dandy Clone Machine](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Handy+Dandy+Clone+Machine)), which worked out just as fine if the thing being touched was the card itself. It just took us (and by us, I mean mostly me) way longer to come to that conclusion than it should have.


**Six-Sided Die**


![Six-Sided Die](https://media.wizards.com/2022/unf/en_qwuBphiOtv.png)


This card's design story is one of execution. George Fan made the card in exploratory design when we were brainstorming about die-rolling designs. The essence of the card, a black instant kill spell called Six Sided-Die where you rolled a die and it killed the creature six different ways, was there from George's very first incarnation. The challenge: what exactly does each die result do? Let's walk through this card's evolution in that regard.


**The Die Results (version #1)**  

1: Destroy it.  

2: Destroy it. It can't be regenerated.  

3: Exile it.  

4: CARDNAME deals 4 damage to it and you gain 4 life.  

5: It gets -5/-5 until the end of turn.  

6: Its controller sacrifices it.


You can see that George thought up four good ways to kill a creature (destroy it, exile it, drain it, and -N/-N it), one tweaked way (the opponent sacrifices it—normally when we do this, the controller chooses which creature they sacrifice), but struggled for the sixth one. "Destroy it and it can't be regenerated" hasn't been used since 2014 (in *Magic 2015*; with the one exception of [Damn](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damn) in *Modern Horizons 2*, but that was making a throwback to [Damnation](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation)). Regeneration itself was retired in 2016. This meant George needed a better option.


**The Die Results (version #2)**  

1: Destroy it.  

2: Exile it.  

3: Destroy it if it's tapped.  

4: CARDNAME deals 4 damage to it and you gain 4 life.  

5: It gets -5/-5 until the end of turn.  

6: Its controller sacrifices it.


Next, we tried "destroy it if it's tapped." It's a weaker kill ability, but one black occasionally uses.


**The Die Results (version #3)**  

1: Destroy it.  

2: Exile it.  

3: Put three -1/-1 counters on it.  

4: CARDNAME deals 4 damage to it and you gain 4 life.  

5: It gets -5/-5 until the end of turn.  

6: Its controller sacrifices it.


We then tried using -1/-1 counters. Normally, we don't mix +1/+1 counters and -1/-1 counters, but this is a quirky supplemental set, and Attempted Murder was already using them.


**The Die Results (version #4)**  

1: Destroy it.  

2: Exile it.  

3: Its controller sacrifices it.  

4: Put four -1/-1 counters on it.  

5: CARDNAME deals 5 damage to it and you gain 5 life.  

6: It gets -6/-6 until the end of turn.


This version has all the same kill effects but mixes them around a bit. -1/-1 goes to 4, drain to 5, and -N/-N to 6.


**The Die Results (version #5)**  

1: Its toughness becomes 1 until end of turn.  

2: Put two -1/-1 counters on it.  

3: CARDNAME deals 3 damage to it and you gain 3 life.  

4: It gets -4/-4 until end of turn.  

5: Destroy it.  

6: Exile it.


This last change did a couple things. First, it got rid of forced targeted sacrifice as that's not something we tend to do. Second, the card was proving a little too good in Limited, so we wanted to notch it down a little. Third, we wanted to have the card feel progressively better as you rolled higher. There are individual cards that care about different results (previous *Un-* sets tended to make rolling higher always better), but since the card cared about all six results, we wanted it to feel better as you rolled higher. Previous versions felt weird when you didn't want to roll a number in the middle.


This got us to put -1/-1 counters at 2, drain at 3, and -N/-N at 4. We liked destroy and exile being 5 and 6 as they were the best you could hope for. We then chose an effect for 1 that was the weakest and would sometimes not kill the creature (although you could play around it if you desired with what creature you targeted). Note we did our best to tie the effect to the number rolled with only 5 and 6 not making a reference.


**Sole Performer and Trigger Happy**


![Sole Performer](https://media.wizards.com/2022/unf/en_nFHQpbHt9l.png)![Trigger Happy](https://media.wizards.com/2022/unf/en_spoK3WqWaY.png)


Sole Performer and Trigger Happy have something in common that no other cards in *Unfinity* do. Both were not initially designed for *Unfinity* but rather were playtest cards for Mystery Booster. Gavin Verhey, who oversaw Mystery Booster, knew I was making *Unfinity*, so he had me look at the playtest cards and pull any that I thought would be appropriate for the next *Un-* set. I chose a handful of cards to put into the file, but these were the two that ended up making it to print.


**Souvenir T-Shirt**


![Souvenir T-Shirt](https://media.wizards.com/2022/unf/en_IvxW26AKwU.png)


Early on, we made a list of things you might get at a carnival or amusement park, and one of the items on the list was a t-shirt. That seemed like a cool piece of equipment that *Unfinity* could make that no one else would. The big question was, what would it do? Here was the first stab:


**Tee Shirt (version #1)**  

1  

Artifact — Equipment  

Equipped creature has haste and branding. (*It gets +1/+1 for each* Magic*-branded piece of clothing its controller is wearing*.)  

Equip {1}


Once we had the idea that it encouraged you to wear branded *Magic* clothing, we knew we found our hook. The big question: how do we execute this? This first version heavily encouraged you to wear as many *Magic*-branded items as possible, so much so that we'd have to cost it as if you did, which meant if you weren't wearing any or even just one or two pieces, the card wouldn't be powerful enough to play in your deck. Some of the design team thought that was cool, but I put my foot down and said, I didn't want to make a card that only a handful of people would play at the release event. I wanted to incorporate wearing *Magic*-branded items, but it had to be balanced in such a way that it was upside, not something you had to do. Also, I wanted people to feel good for having one *Magic* item on.


**Tee Shirt (version #2)**  

2  

Artifact — Equipment  

Equipped creature has haste and branding. (*Whenever it attacks, up to X attacking creatures you control each get +1/+1, where X is the number of* Magic*-branded clothing items you're wearing*.)  

Equip {1}


The next attempt gave you a bonus but ratcheted down how impactful it could be. It ended up not being impactful enough, and no one was playing it even if they did wear *Magic*-branded items.


**Tee Shirt (version #3)**  

2  

Artifact — Equipment  

Equipped creature gets +1/+1 and branding. (*Equipped creature can't be the target of* Magic *cards you don't own as long as you are wearing a* Magic: The Gathering-*branded clothing item*.)  

Equip {1}


The third version gave you a reward, basically hexproof, if you wore any items. The feedback we got on this was that it was too minimal of a bonus.


**Tee Shirt (version #4)**  

2  

Artifact — Equipment  

Equipped creature gets +1/+1 and branding. (As long as you are wearing a *Magic: The Gathering*-branded item, any creature with branding, and up to one without, can attack in a band. Bands are blocked as a group. If any creatures with branding you control are blocked by a creature, you divide that creature's combat damage, not its controller, among any of the creatures it's being blocked by.)  

Equip {o1}


The next version got a little crazier. What if branding gave you banding (spelled out, of course)? This tickled us to no end and stayed in the file longer than it probably should have. In the end, three things killed it. One, banding is quite confusing. Two, banding tends to gum up the board and stop attacks from happening (this is just a problem with banding and why enlist only works on attack). Three, it, like the last version, took away the dream of going to the release event loaded up with *Magic*-branded stuff.


For the final version, we decided having a second card inspired by [Elvish Impersonators](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Impersonators) was okay ([the first inspired card I talk about below](#elvish)). Allowing an extra die roll for each branded item made it matter, but in a way that was capped, so we could cost the card such that people without *Magic*-branded items would still play it.


**Standard Procedure**


![Standard Procedure](https://media.wizards.com/2022/unf/en_zQ5RQTyvWm.png)


In *Unglued 2*, I created a card called Shameless Plug (*The Duelist*, for those unaware, was the magazine Wizards used to make about the game):


**Shameless Plug**  

3  

Artifact  

Sacrifice Shameless Plug: Choose a *Magic* card pictured in the latest *Duelist*. Until end of turn, you may play as though that card were in your hand. Play this ability only if you have the latest copy of *The Duelist* with you.


The idea behind the card was that its utility would change over time. Its mechanical function was based on a subset of cards that shifted. *Unfinity* tried a different take on this idea, using the Standard format instead of *The Duelist*. Our first take functioned like a copy spell, essentially you could copy any cheap spell (defined originally as mana value two or less) in Standard. The first version of the spell was made blue because it was framed as a copy spell.


**Standard Spell (version #1)**  

3U  

Instant  

Name an instant or sorcery card currently legal in Standard with converted mana cost 2 or less. Cast a copy of it without paying its mana cost.


Even though we framed this as a copy spell, it felt a lot more like a tutor or wish, so we decided to make it black rather than blue. We also dropped the mana cost by one, as spending four mana to cast a two-mana spell felt wrong.


**Standard Spell (version #2)**  

2B  

Instant  

Name an instant or sorcery card currently legal in Standard with converted mana cost 2 or less. Cast a copy of it without paying its mana cost.


We enjoyed how this card was playing, but we had a big issue with it. It was breaking the color pie. For 2B, you could cast any small effect in any color. This led to us allowing you to cast the card rather than just casting it for free. This also meant it cost less to cast a cheaper spell. The card was fun in playtests, so we decided to open it up to all colors, changing it from black to colorless. Both factors had us drop the mana cost to 1. Finally, we decided to expand the pool of cards from mana value two or less to mana value three or less.


**Standard Spell (version #3)**  

1  

Instant  

Name an instant or sorcery card currently legal in Standard with converted mana cost 3 or less. You may cast a copy of that spell.


I generally liked how the card was playing, but I felt it was missing some potential to feel more different than a tutor or wish. That's when I proposed the idea that you didn't fetch the card but rather you turned this card into the card. We were already in acorn territory with caring about Standard, so it felt like a way to take the same effect and make it feel more different and splashier. It also allowed for some cool interactions because the card stays the copy of the card for the duration of the turn, so you can interact with it as the Standard card in various zones. (For example, you can make it a blue card to discard to [Force of Will](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) or make it an instant and remove it from the graveyard to pay for [Disciple of the Ring](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disciple+of+the+Ring).)


**Vedalken Squirrel-Whacker**


![Vedalken Squirrel-Whacker](https://media.wizards.com/2022/unf/en_OKbmKip1sq.png)


The first set to use die rolling was *Unglued*, and my favorite die-rolling card was [Elvish Impersonators](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Impersonators).


[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=9669)](https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=9669)
It was a perfect example of the fun of high variance with die rolling. You could get anything from a 1/1 to a 6/6 with 36 different outcomes. It played well, it had a great moment of suspense, and it was easy to understand. One day, it dawned on me, could we just reprint [Elvish Impersonators](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Impersonators) in *Unfinity*? Performer was literally a new creature type. We were reprinting the shock lands, but that felt different. We weren't reprinting any other former *Un*- cards in boosters. ([Water Gun Balloon Game](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Water+Gun+Balloon+Game) from *Unhinged* was the release promo.) Also, as creatures have gotten better, I was told that the card had room to do more at four mana.


I set out to make a new [Elvish Impersonators](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Impersonators). What else could I add to the card? It dawned on me that it might be fun if you could use the die rolls for some other function. What if you could swap them with another die roll. You could do this to either make the die roll better or make your creature better, and maybe on rare occasions, do both. (*Unfinity* has cards where rolling low is better.) The original card was a green-blue legendary creature, but we ended up making it mono-blue and taking away the legendary status, as we had other effects we wanted to put into the two green-blue legendary creature slots (Ambassador Blorpityblorpboop and It Came From Planet Glurg).


"And They All Lived Happily Ever After"
=======================================


I must wrap things up. I hope you enjoyed hearing all the *Unfinity* card design stories these last three weeks. As always, I'd love for any feedback on today's column, any of the cards I talked about, or about *Unfinity* itself. This product is near and dear to me, so I really want to hear your thoughts on it. You can [email](mailto:making.magic@hotmail.com) me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)).


Join me next week when *The Brothers' War* previews begin.


Until then, may you create your own *Unfinity* stories to tell.




 

##### 
 #975: UNF Names & Flavor Text with Ari Zirulnik






##### 
 #975: UNF Names & Flavor Text with Ari Zirulnik


43:20



I sit down with Ari Zirulnik to talk about overseeing the names and flavor text creation in *Unfinity*.

 



 Play
[Download MP3 Format](https://cdn.transistor.fm/file/transistor/m/shows/21454/37658c4dded0a5b03cae34583d221bd7.mp3)




  


 

##### 
 #976: Unfinity Design, Part 3






##### 
 #976: Unfinity Design, Part 3


34:31



This is part three of a four-part series on the design of *Unfinity*.

 



 Play
[Download MP3 Format](https://cdn.transistor.fm/file/transistor/m/shows/21454/8921828164fe2a313e2bd3c8748235be.mp3)





* [**Episode 974**](https://cdn.transistor.fm/file/transistor/m/shows/21454/8849600b6ee32e3ee9e9b7971e233e4b.mp3) *Unfinity* Design, Part 2
* [**Episode 973**](https://cdn.transistor.fm/file/transistor/m/shows/21454/2de5f6b12e79bea094aff6184454c481.mp3) UNF Card Concepting with Annie Sardelis
* [**Episode 972**](https://cdn.transistor.fm/file/transistor/m/shows/21454/45f870d9cd2491a08b3f422b7b73f27b.mp3) *Unfinity* Design, Part 1








---
[Link to Wayback Machine](https://web.archive.org/web/20160725070014/http://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-14)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "&#13; A long time ago, Mark Rosewater wrote a column titled When Cards Go Bad about why `bad cards` exist. While I agree with many of the things he said, he approached the problem from a design perspective.&#13; &#13; I've been itching to write my own version of his article for a few months. Here are some reasons that developers make cards `bad.`&#13; &#13; Some cards aren't fun when they're good.&#13; &#13; Consider the card Scrambleverse."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "644361"
[_metadata_:publish_date]:- "2011-10-14"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "When Cards Go Bad, Part 2"
[_metadata_:wayback_capture_timestamp]:- "2016-07-25 07:00:14"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20160725070014id_/http://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-14"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/when-cards-go-bad-part-2-2011-10-14"
---


When Cards Go Bad, Part 2
=========================



 Posted in **Latest Developments**
 on October 14, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_tomlapille.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 







A long time ago, Mark Rosewater wrote a column titled [When Cards Go Bad](/en/articles/archive/making-magic/when-cards-go-bad-2002-01-28) about why "bad cards" exist. While I agree with many of the things he said, he approached the problem from a design perspective.


I've been itching to write my own version of his article for a few months. Here are some reasons that developers make cards "bad."


### Some cards aren't fun when they're good.


Consider the card [Scrambleverse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse).



![Scrambleverse](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scrambleverse)

 

Have you ever been part of a game in which this card resolved? What happened?


In a two-player game, you probably flipped a lot of coins, and then whatever board state existed before the card was cast was completely ruined. In a multiplayer game, you probably had to use dice, and there were likely a lot more permanents changing hands. In my experience, this card is a novelty the first time, but its welcome wears out quickly, as the act of resolving it is complicated and it invalidates all the work everyone put into the game before it resolved.


You might, then, be wondering why the card exists at all.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld164_sramble.jpg)Let me tell you about Nick Fang. Nick is a **Magic** judge who often serves as the scorekeeper at Pro Tours. Some of Nick's favorite cards are red chaos-inducing cards in the vein of [Confusion in the Ranks](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Confusion+in+the+Ranks), [Wild Evocation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Evocation), and [Warp World](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Warp+World). Whenever I go to Pro Tours, Nick reminds me how much he likes those cards, and that we don't normally make very many of them. Nick's friendly reminders were on my mind while I was working on ***Magic** 2012*, especially because *Scars of Mirrodin* block didn't have any big and random red cards to speak of. I made [Scrambleverse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse) to fill that need.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld164_3Cards1.jpg)While on the surface I made [Scrambleverse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse) for Nick Fang, that's not what's actually going on here. Nick is not the only **Magic** player out there who likes big and random effects, as the Gatherer [rate-and-discuss page](http://gatherer.wizards.com/Pages/Card/Discussion.aspx?multiverseid=220300) for [Scrambleverse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse) demonstrates. We need to make cards to serve that audience every once in a while. However, a world in which a deck with four [Scrambleverse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse)s wins a Pro Tour would be a terrible one indeed, as most players don't enjoy doing that sort of thing more than once every very long time. In order to give [Scrambleverse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse) to the people who need it but keep it from annoying people who want to avoid it, we just make the card cost so much mana that only the people who really want to play with it will bother to.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld164_6rr.jpg)Random red effects are not the only cards that we do this with. Cards like [Painful Quandary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Painful+Quandary) that enable griefing and cards like [Shared Fate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shared+Fate) that take an otherwise perfectly normal game and make it weirder both have their audiences, but can annoy the majority of **Magic** players if they become powerful. Our job is to make **Magic** the most fun for everyone, and we've found that we reach the best balance when cards like [Scrambleverse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scrambleverse), [Painful Quandary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Painful+Quandary), and [Shared Fate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shared+Fate) exist, but have a low enough power level that most players don't want to play with them.


 




|  |  |
| --- | --- |
| 
Painful Quandary
 | 
Shared Fate
 |

### Limited needs to be balanced.


Most **Magic** players experience **Magic** on a card-by-card basis. While we understand that and do our best to make sure that cards make sense individually, **Magic** developers need to think about the larger picture. Limited is important to **Magic**; lots of people have their first interactions with a **Magic** set at a Sealed Deck event at a Prerelease, and as long as **Magic Online** is up, there will be people drafting twenty-four hours a day. All that Limited play needs to remain fun over time, and to achieve that, we would like the power levels of each color in each format to be balanced.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld164_cross1.jpg)This often leads to some conversations in meetings that would look strange to outsiders. We had several of these during *New Phyrexia* development. In particular, there was a meeting when both blue and black were doing much better than we wanted in our playtests. Lead developer Aaron Forsythe decreed that we needed a weak blue card and a weak black card. None of us came up with a blue card that was weak enough, so Aaron created [Defensive Stance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Defensive+Stance) to fill the hole. While I have seen [Defensive Stance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Defensive+Stance) sideboarded in against [Plague Stinger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Stinger)s and [Blighted Agent](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blighted+Agent)s, it is hardly a Limited all-star. That same meeting also resulted in [Evil Presence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evil+Presence) entering the set. While [Evil Presence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evil+Presence) was important in *Masters Edition III* for dealing with certain legendary lands, in *New Phyrexia* it is merely a weak black card with a flavorful name that we put in to balance the colors.


 




|  |  |
| --- | --- |
| 
Defensive Stance
 | 
Evil Presence
 |

I wouldn't be surprised if you drafted full *Scars of Mirrodin* block several times without having played either [Evil Presence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Evil+Presence) or [Defensive Stance](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Defensive+Stance), but I guarantee that those cards being the right power level for the set contributed to the fun you had.


### Draft needs to be human-processable.


From a game design perspective, the most potentially confusion-inducing point in a booster draft is the moment you open your first pack. At that moment, you're looking at a fresh collection of fourteen or fifteen cards, and you don't have anything in your pile already to guide you. We include cards of varying power levels in the pack so that this moment is a little bit easier to deal with.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld164_balance.jpg)Oddly, this is the opposite of many people's instincts about what makes for good Limited game play. Why, they ask, isn't every card almost equally playable? Wouldn't that be more balanced?


It might be a little bit more balanced, but that balance would come with significant costs. I have more experience than most playing Limited with flat power curves. Before I came to Wizards, I spent lots of time playing Cube Draft, a format very similar to Booster Draft in which the booster packs are replaced with a different set of cards preselected by the host. Usually, the selection of cards doesn't include any "bad cards," because who wants to play with those? Because of how often I used to draft Cubes, my Cube card evaluation skills are pretty sharp. However, due to the absence of the bad cards, the card power levels are much closer together than they are in a normal draft.


To illustrate this, here is a pack I just pulled from my Cube.


* [Necropotence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence)
* [Phantom Centaur](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Centaur)
* [Hero of Oxid Ridge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hero+of+Oxid+Ridge)
* [Tarmogoyf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tarmogoyf)
* [Chrome Mox](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chrome+Mox)
* [Badlands](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Badlands)
* [Eldrazi Monument](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eldrazi+Monument)
* [Venser, Shaper Savant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venser%2C+Shaper+Savant)
* [Woolly Thoctar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar)
* [Pristine Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pristine+Angel)
* [Recurring Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare)
* [Counterspell](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Counterspell)
* [Geist of Saint Traft](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft)
* [Whipcorder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whipcorder)
* [Slagstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slagstorm)

When most drafters I know open their first pack, the first thing they do is narrow down to a few cards they might be willing to first pick. On your first pass, how many of these cards seem first-pickable to you?


I narrowed it down to just [Chrome Mox](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chrome+Mox), [Necropotence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence), and [Recurring Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare). [Necropotence](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Necropotence) and [Recurring Nightmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recurring+Nightmare) are both powerful build-around cards, and I think both are reasonable to pick first; I'd take the [Chrome Mox](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chrome+Mox) because it doesn't commit me to anything and I value mana acceleration highly.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld164_3Cards2.jpg)Now, a second question. Which of these fifteen cards occurred to you as "bad cards" in context, if any? My "bad cards" in this pack are [Slagstorm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slagstorm), [Whipcorder](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whipcorder), [Pristine Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pristine+Angel), [Phantom Centaur](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantom+Centaur), and [Woolly Thoctar](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar). I've played all of them in Cube decks before, but none of them are powerful enough to draw me into drafting a deck around them. Despite that, all five have been historically proven as reasonable Constructed cards! This is exactly the kind of card evaluation puzzle that bewilders most people during their first few Cube drafts.


 




|  |  |
| --- | --- |
| 
Slagstorm
 | 
Woolly Thoctar
 |

Drafting is a complex enough task already without every card being extremely close together in power, so we include plenty of cards of widely differing power levels so that the right answer can be a little bit less ambiguous. This doesn't simplify the task of correctly identifying those power levels—a challenging task in itself!—but it does make deciding between correctly-identified power levels a little bit easier.


As a side note, I was not much of a believer in this idea until early *Zendikar* development. One of the main problems with the *Zendikar* design handoff was how flat the power levels of the cards were. Most cards were very close to one another in power, so the only way you could get an edge was to draft a highly synergistic deck. One of the first things that *Zendikar* lead developer Henry Stern did to the set once he got his hands on it was de-flatten the power curve by adding one common to each color that you would be unambiguously happy to open and first pick. That made a big difference in lowering the stress level of the beginning of a *Zendikar* draft, and I've been a believer ever since.


### Some "bad cards" aren't bad.


Finally, we get to my favorite answer. Often, when a card is previewed, people will post comments like "This should cost one less mana" or "needs trample" or some such. Often, those comments will be about cards that are the way they are for reasons previously enumerated in Mark Rosewater's article or this one, but occasionally, those comments are simply off base. The card is just fine and will have its day in the sun eventually. In these cases, there will inevitably be a moment of discovery when the card turns out to be powerful enough anyway.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld164_garruk.jpg)One such moment happened last weekend with the Wolf Run Ramp deck that Brian Sondag used to win the Star City Games Standard Open in Nashville.







#### Brian Sondag's Wolf Run Ramp


##### 






![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)





[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (4)



4
[Garruk, Primal Hunter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BPrimal%5D+%5BHunter%5D)



##### Creature (15)



3
[Solemn Simulacrum](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSolemn%5D+%5BSimulacrum%5D)


3
[Wurmcoil Engine](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D)


1
[Acidic Slime](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcidic%5D+%5BSlime%5D)


1
[Birds of Paradise](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D)


3
[Primeval Titan](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimeval%5D+%5BTitan%5D)


4
[Viridian Emissary](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BEmissary%5D)



##### Sorcery (11)



4
[Green Sun's Zenith](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreen%5D+%5BSun%5D+%5BZenith%5D)


4
[Rampant Growth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRampant%5D+%5BGrowth%5D)


3
[Slagstorm](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D)



##### Instant (4)



4
[Beast Within](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeast%5D+%5BWithin%5D)



##### Land (26)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


3
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Copperline Gorge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCopperline%5D+%5BGorge%5D)


4
[Inkmoth Nexus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkmoth%5D+%5BNexus%5D)


2
[Kessig Wolf Run](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKessig%5D+%5BWolf%5D+%5BRun%5D)


4
[Rootbound Crag](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRootbound%5D+%5BCrag%5D)


60 Cards 


##### Sideboard (15)



1
[Slagstorm](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D)


1
[Ratchet Bomb](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D)


3
[Sword of Feast and Famine](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BFeast%5D+%5Band%5D+%5BFamine%5D)


2
[Tree of Redemption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BRedemption%5D)


1
[Viridian Corrupter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BCorrupter%5D)


4
[Ancient Grudge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D)


3
[Thrun, the Last Troll](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThrun,%5D+%5Bthe%5D+%5BLast%5D+%5BTroll%5D)




##### Red (8)



4
[Slagstorm](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D)


4
[Ancient Grudge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D)



##### Green (31)



1
[Acidic Slime](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcidic%5D+%5BSlime%5D)


1
[Birds of Paradise](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D)


3
[Primeval Titan](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimeval%5D+%5BTitan%5D)


4
[Viridian Emissary](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BEmissary%5D)


4
[Garruk, Primal Hunter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BPrimal%5D+%5BHunter%5D)


4
[Beast Within](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeast%5D+%5BWithin%5D)


4
[Green Sun's Zenith](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreen%5D+%5BSun%5D+%5BZenith%5D)


4
[Rampant Growth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRampant%5D+%5BGrowth%5D)


2
[Tree of Redemption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BRedemption%5D)


1
[Viridian Corrupter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BCorrupter%5D)


3
[Thrun, the Last Troll](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThrun,%5D+%5Bthe%5D+%5BLast%5D+%5BTroll%5D)



##### Colorless (36)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


3
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Copperline Gorge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCopperline%5D+%5BGorge%5D)


4
[Inkmoth Nexus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkmoth%5D+%5BNexus%5D)


2
[Kessig Wolf Run](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKessig%5D+%5BWolf%5D+%5BRun%5D)


4
[Rootbound Crag](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRootbound%5D+%5BCrag%5D)


3
[Solemn Simulacrum](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSolemn%5D+%5BSimulacrum%5D)


3
[Wurmcoil Engine](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D)


1
[Ratchet Bomb](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D)


3
[Sword of Feast and Famine](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BFeast%5D+%5Band%5D+%5BFamine%5D)


75 Cards 



##### 1 (5)



1
[Birds of Paradise](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D)


4
[Green Sun's Zenith](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreen%5D+%5BSun%5D+%5BZenith%5D)



##### 2 (13)



4
[Viridian Emissary](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BEmissary%5D)


4
[Rampant Growth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRampant%5D+%5BGrowth%5D)


1
[Ratchet Bomb](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D)


4
[Ancient Grudge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D)



##### 3 (12)



4
[Beast Within](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeast%5D+%5BWithin%5D)


4
[Slagstorm](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D)


3
[Sword of Feast and Famine](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BFeast%5D+%5Band%5D+%5BFamine%5D)


1
[Viridian Corrupter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BCorrupter%5D)



##### 4 (8)



3
[Solemn Simulacrum](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSolemn%5D+%5BSimulacrum%5D)


2
[Tree of Redemption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BRedemption%5D)


3
[Thrun, the Last Troll](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThrun,%5D+%5Bthe%5D+%5BLast%5D+%5BTroll%5D)



##### 5 (5)



1
[Acidic Slime](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcidic%5D+%5BSlime%5D)


4
[Garruk, Primal Hunter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BPrimal%5D+%5BHunter%5D)



##### 6 (6)



3
[Wurmcoil Engine](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D)


3
[Primeval Titan](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimeval%5D+%5BTitan%5D)


49 Cards 



##### Common (24)



9
[Forest](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BForest%5D)


3
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Viridian Emissary](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BEmissary%5D)


4
[Rampant Growth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRampant%5D+%5BGrowth%5D)


4
[Ancient Grudge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D)



##### Uncommon (6)



1
[Acidic Slime](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcidic%5D+%5BSlime%5D)


4
[Beast Within](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBeast%5D+%5BWithin%5D)


1
[Viridian Corrupter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BViridian%5D+%5BCorrupter%5D)



##### Rare (23)



4
[Copperline Gorge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCopperline%5D+%5BGorge%5D)


4
[Inkmoth Nexus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInkmoth%5D+%5BNexus%5D)


2
[Kessig Wolf Run](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKessig%5D+%5BWolf%5D+%5BRun%5D)


4
[Rootbound Crag](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRootbound%5D+%5BCrag%5D)


3
[Solemn Simulacrum](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSolemn%5D+%5BSimulacrum%5D)


1
[Birds of Paradise](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBirds%5D+%5Bof%5D+%5BParadise%5D)


4
[Slagstorm](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlagstorm%5D)


1
[Ratchet Bomb](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRatchet%5D+%5BBomb%5D)



##### Mythic (22)



3
[Wurmcoil Engine](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWurmcoil%5D+%5BEngine%5D)


3
[Primeval Titan](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimeval%5D+%5BTitan%5D)


4
[Garruk, Primal Hunter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGarruk,%5D+%5BPrimal%5D+%5BHunter%5D)


4
[Green Sun's Zenith](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreen%5D+%5BSun%5D+%5BZenith%5D)


3
[Sword of Feast and Famine](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSword%5D+%5Bof%5D+%5BFeast%5D+%5Band%5D+%5BFamine%5D)


2
[Tree of Redemption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTree%5D+%5Bof%5D+%5BRedemption%5D)


3
[Thrun, the Last Troll](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThrun,%5D+%5Bthe%5D+%5BLast%5D+%5BTroll%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Forest)

















 

I had a lot of people complain to me that [Garruk, Primal Hunter](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk%2C+Primal+Hunter) was too weak to play in Constructed when it was previewed. My internal experience suggested that this was not the case once *Innistrad* rotated in, but as always I was open to being wrong. Happily, "big Garruk" is starting to show up. I look forward to seeing more of his work in the future.



![Garruk, Primal Hunter](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Garruk%2C+Primal+Hunter)

 

We try to design **Magic** sets so that cards can surprise you over time. If you could get everything right just by looking at individual cards, that wouldn't be much fun. We can't get it right by doing that either, so we have to do a lot of work to figure things out, but we think it's worth it in the end if we get a rich and changing tapestry to explore instead of a quickly solved static puzzle.


In the end, each individual card has to serve the greater good of **Magic**. Sometimes, that means not being as powerful as other cards. We hope you understand.


### Last Week's Poll




| **Which of Magic's Werewolves is your favorite?**  |
| --- |
| [Mayor of Avabruck](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mayor+of+Avabruck) / [Howlpack Alpha](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howlpack+Alpha) | 240 | 25.5% |
| [Reckless Waif](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reckless+Waif) / [Merciless Predator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merciless+Predator) | 167 | 17.7% |
| [Kruin Outlaw](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kruin+Outlaw) / [Terror of Kruin Pass](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terror+of+Kruin+Pass) | 145 | 15.4% |
| [Instigator Gang](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Instigator+Gang) / [Wildblood Pack](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildblood+Pack) | 116 | 12.3% |
| [Daybreak Ranger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Daybreak+Ranger) / [Nightfall Predator](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightfall+Predator) | 85 | 9.0% |
| [Gatstaf Shepherd](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gatstaf+Shepherd) / [Gatstaf Howler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gatstaf+Howler) | 43 | 4.6% |
| [Village Ironsmith](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Village+Ironsmith) / [Ironfang](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironfang) | 28 | 3.0% |
| [Hanweir Watchkeep](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hanweir+Watchkeep) / [Bane of Hanweir](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bane+of+Hanweir) | 25 | 2.7% |
| [Ulvenwald Mystics](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulvenwald+Mystics) / [Ulvenwald Primordials](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulvenwald+Primordials) | 21 | 2.2% |
| [Lesser Werewolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lesser+Werewolf) | 20 | 2.1% |
| [Villagers of Estwald](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Villagers+of+Estwald) / [Howlpack of Estwald](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howlpack+of+Estwald) | 16 | 1.7% |
| [Greater Werewolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Werewolf) | 13 | 1.4% |
| [Tormented Pariah](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tormented+Pariah) / [Rampaging Werewolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampaging+Werewolf) | 9 | 1.0% |
| [Treacherous Werewolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treacherous+Werewolf) | 7 | 0.7% |
| [Grizzled Outcasts](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzled+Outcasts) / [Krallenhorde Wantons](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krallenhorde+Wantons) | 7 | 0.7% |
| **Total** | **942** | **100.0%** |

  
  

 






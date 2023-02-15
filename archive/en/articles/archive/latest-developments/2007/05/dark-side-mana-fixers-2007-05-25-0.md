
---
[Link to Wayback Machine](https://web.archive.org/web/20170312010711/http://magic.wizards.com/en/articles/archive/latest-developments/dark-side-mana-fixers-2007-05-25-0)

[_metadata_:author]:- "Devin Low"
[_metadata_:description]:- "&#13;"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "612466"
[_metadata_:publish_date]:- "2007-05-25"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Dark Side of Mana Fixers"
[_metadata_:wayback_capture_timestamp]:- "2017-03-12 01:07:11"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170312010711id_/http://magic.wizards.com/en/articles/archive/latest-developments/dark-side-mana-fixers-2007-05-25-0"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/dark-side-mana-fixers-2007-05-25-0"
---


The Dark Side of Mana Fixers
============================



 Posted in **Latest Developments**
 on May 25, 2007 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DevinLow.jpg)
By Devin Low












Hello! This is **Magic** Head Developer Devin Low, guest writing Aaron's column this week to cover a topic I encountered at the recent [Pro Tour–Yokohama](/en/events/coverage/wafo-tapa-tops-them-all). With Aaron moving up to become Director of **Magic** R&D, I have advanced to become **Magic** Head Developer, following in the legacy of Randy Buehler, Brian Schneider, and Aaron himself. But enough of that. Today I'm here to talk about a very specific issue: The Dark Side of five-color mana fixers (Oooo...). We added *Time Spiral*'s five-color mana fixers with specific objectives that would make Limited more fun. Looking at the way Time Spiral Limited plays, I'm happy to say we accomplished the mission. But when I went to PT–Yokohama last month to analyze *Time Spiral / Planar Chaos* Block Constructed, I noticed that these cheerful little widgets had a dark side... a subtle, hurtful effect on Block Constructed that we never predicted. I'll lead you through the light and the dark, then describe how we fix this in *Future Sight*... and in the actual future.


### The Light Side


![Prismatic Lens, Terramorphic Expanse, and Chromatic Star](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/af172_cardfan.jpg)*Time Spiral* features three common colorless five-color mana fixers: [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens), [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse), and [Chromatic Star](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chromatic+Star). In a good article last October called [The State of Limited](/en/articles/archive/latest-developments/state-limited-2006-10-13-0), Aaron explained how much *Time Spiral* Limited benefits from the subtle influence of these humble smoothers. He concluded:



> *With those cards at common alongside green's normal slew of fixing and accelerating, plus a couple interesting uncommon cycles in the Totems and storage lands, players should have the ability to make mana bases that range from slickly consistent to downright weird and everything in between. And in drafts, mana can be prioritized or ignored at each player's discretion.*


I served on the *Time Spiral* development team, and we saw the colorless mana fixers as an experiment. We'd heard some sound arguments for why to add them, so we decided to try them out for a block and see where they took us. In addition to Aaron's points, here are some specific positive impacts that I feel the colorless mana fixers have on *Time Spiral* Block Limited:


***They help you play Time Spiral's mini-themes.***


Because *Time Spiral* doesn't have an overarching "mechanical heart" like *Odyssey* or *Onslaught*, the development team decided to build a selection of "mini-themes" across the colors. Besides just "playing powerful cards," you can build your Limited (or Constructed) decks around any of these *Time Spiral* mini-themes:


![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif): "White creatures matter" ([Gaze of Justice](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gaze+of+Justice), [Ivory Giant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ivory+Giant) etc.)  
![](https://web.archive.org/web/20161115194122im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/blue.gif): Morph  
![](https://web.archive.org/web/20161227195556im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif): Madness  
![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif): Storm  
![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif): Thallids  

All colors: Time counter manipulation or Slivers


The colorless mana fixers are the glue that pulls a lot of these themes and other *Time Spiral* mechanics together. Let's take a look:


**Slivers:** Midway through *Time Spiral* development, the easiest way to take advantage of five colors' worth of Slivers was to build around [Gemhide Sliver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gemhide+Sliver) and [Search for Tomorrow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Search+for+Tomorrow). But we found it a little stifling that Sliver decks would always have to be two-color Drafts, three-color Sealeds, or a heavy green base supporting four or five colors. If you pulled [Essence Sliver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Sliver), [Fury Sliver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fury+Sliver), and [Telekinetic Sliver](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Telekinetic+Sliver) in draft, it sucked that it was almost impossible to play them all together. The common five-color mana fixers do a great job of helping you play whatever crazy Sliver combination you want, whether you're green or not. Green is still clearly the best at supporting a four- or five-color deck, but you have the freedom to go whatever way you want.


**Flashback:** If you have a white-black draft deck with [Strangling Soot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strangling+Soot), you'll often be tempted to add a [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain) to have a shot at using its flashback. The colorless mana fixers make it a lot easier to get these off-color flashbacks to fire.


**Thallids:** Most Time Spiral Thallids are green, with [Deathspore Thallid](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Deathspore+Thallid) and [Thelon of Havenwood](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thelon+of+Havenwood) pulling you a little bit into black. But *Planar Chaos* adds [Pallid Mycoderm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pallid+Mycoderm) and [Mycologist](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mycologist) to tempt your Thallid decks into white. And maybe you want to max out your Thallids with the techy [Paradox Haze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Paradox+Haze), or more subtle combinations like [Fortify](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fortify), [Fallen Ideal](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fallen+Ideal), or [Greater Gargadon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Gargadon). You have much more freedom to build your G/b/w/u Thallid deck and have it actually work with the colorless mana fixers around than if they weren't.


**Morph:** Your blue-red Morph deck is losing the race, and you can't stop your opponent's two shadow creatures. With your own death on the stack, you unmorph... a random off-color [Weathered Bodyguards](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Weathered+Bodyguards). With your [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) on the board and no plains in your deck. "How lucky..." your opponent sulks.


***You choose whether to prioritize mana consistency or power.***


Aaron's article mentioned this. In *Champions of Kamigawa* Limited, if you hate losing to color-screw and you want to tighten up the color consistency of your blue-black deck, your available options are basically "Don't play [Wicked Akuba](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wicked+Akuba)." In *Time Spiral* Draft, when you see [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse) and [Spiketail Drakeling](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spiketail+Drakeling) staring out of the pack, you get to make the choice of which is more important to you—more power with the Spiketail or the more consistent colored mana of the Expanse.


***You get a lot of mileage out of fewer slots.***


 



![Geothermal Crevice](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Geothermal+Crevice)

In an effort to fix mana, *Invasion* spent five common slots on [Geothermal Crevice](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geothermal+Crevice) and its 4 friends. [Chromatic Sphere](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chromatic+Sphere) and [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) give more decks more fixing in fewer slots in the set, so you can get the mana fixing you need and still get more spells in your packs.

***More varied color options create more varied deckbuilding***


When you play W/U/r in *Time Spiral*, it feels different than just W/U. The mana fixers subtly help your game experience to feel different from week to week.


***They help players cast their spells.***


This is always an aspect of a mechanic that earns a lot of points from me when evaluating it on a development team. Nobody likes to sit there with [Vexing Sphinx](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vexing+Sphinx) and three swamps. Let players cast their spells.


*Time Spiral*'s three colorless five-color mana fixers do all these things invisibly, without calling any attention to themselves and without a lot of people ever noticing. That's a heck of a lot of value out of just three cards.


### The Dark Side


But despite all the benefits to Limited, these five-color mana fixers have some hurtful effects on *Time Spiral* / *Planar Chaos* Block Constructed. We didn't foresee these effects when we debated adding them on the development team, but as I watched 19 rounds at PT–Yokohama, I became pretty convinced that the little smoothers were causing some subtle problems we never even imagined.


Overall I was thrilled with the PT–Yokohama metagame. The most popular decks were Blue-Black Control, Mono-Red Aggro, Red-Green Midrange, White Weenie, Black-Red Control, and five-color Sliver / [Wild Pair](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wild+Pair) Combo. All five colors were popular and powerful. All deck speeds were popular and powerful, from aggro to midrange to board control to true control, with a splash of combo from the Slivers. Whatever kind of deck you enjoy playing, you could play it. And when White Weenie packed the Top 8s of **Magic Online** Block Constructed events leading into the PT, the pros reacted with hordes of [Sulfur Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sulfur+Elemental)s that beat White Weenie out of the top slots, showing some good reactive tools in the format that prevented things from getting unbalanced. I watched games for hours because they were fun to watch. Former **Magic** Head Developer Brian Schneider did a fantastic job crafting the metagame for *Ravnica* Block Constructed and Standard, and I'm pretty sure he did it again with *Time Spiral*.


The problem I saw caused by five-color mana fixers was very subtle, and usually went unnoticed. Here it is:


 



![Sulfur Elemental](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sulfur+Elemental)

Say you want to build a two-color *Time Spiral* Block Constructed deck that isn't fast aggro and isn't green. Black-red, blue-black, blue-red, white-red, whatever; midrange, board control, or true control. What are your top choices for color fixers? The answers are [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse), [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens), and the appropriate storage land, in that order. In fact it's very likely that you'll play 4, 4, and 2-4 of those. You only planned to play a two-color deck, but now you find you already have eight sources for a third color... and even a fourth color. All you have to do is add a single basic land of that color in the maindeck or sideboard for Expanse to fetch. Since you're planning the game to last a while, and you might also have card drawing or filtering, you'll eventually draw one of your nine sources of your third and fourth color to cast those key midgame and late game spells.

Now think about the specific example of blue-black control—the most successful class of control decks at Yokohama. Most of them revolved around [Mystical Teachings](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Teachings), which can fetch any instant or any creature while you have [Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teferi%2C+Mage+of+Zhalfir) out. This makes it incredibly easy for those decks to sideboard in 1 [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains), 1 [Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant), and 2 Pull from Eternities, and Teachings up any answer they need. Or a [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain), 2 [Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore), 2 [Ancient Grudge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancient+Grudge), and 4 [Sulfur Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sulfur+Elemental)s. Or maindeck one or both of those packages. What price did those blue-black decks pay for including those third and fourth colors? What sacrifices did they have to make to get access to two more whole colors of threats and answers? Just one [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) and one [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain) in the sideboard. This occurred constantly.


Let's look at the three most successful blue-black control decks at PT–Yokohama. Each is very different, but each of them makes heavy use of this automatic access to a third or fourth color.







#### Kazuya Mitamura


##### 






![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)





[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (14)



4
[Shadowmage Infiltrator](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D)


4
[Vesuvan Shapeshifter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVesuvan%5D+%5BShapeshifter%5D)


2
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Brine Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)



##### Sorcery (4)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)



##### Instant (12)



4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


2
[Strangling Soot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrangling%5D+%5BSoot%5D)


2
[Snapback](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnapback%5D)



##### Artifact (6)



2
[Phyrexian Totem](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BTotem%5D)


4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)



##### Land (24)



4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


1
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


5
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


9
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


60 Cards 


##### Sideboard (15)



2
[Brine Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D)


1
[Strangling Soot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrangling%5D+%5BSoot%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Sulfur Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSulfur%5D+%5BElemental%5D)


2
[Ancient Grudge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D)


2
[Serrated Arrows](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSerrated%5D+%5BArrows%5D)


2
[Willbender](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWillbender%5D)


1
[Dismal Failure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BFailure%5D)




##### Blue (25)



4
[Vesuvan Shapeshifter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVesuvan%5D+%5BShapeshifter%5D)


2
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


4
[Brine Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


2
[Snapback](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnapback%5D)


2
[Willbender](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWillbender%5D)


1
[Dismal Failure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BFailure%5D)



##### Black (7)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


3
[Strangling Soot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrangling%5D+%5BSoot%5D)



##### Red (6)



4
[Sulfur Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSulfur%5D+%5BElemental%5D)


2
[Ancient Grudge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D)



##### Multi colored (4)



4
[Shadowmage Infiltrator](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D)



##### Colorless (33)



4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


1
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


5
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


9
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


2
[Phyrexian Totem](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BTotem%5D)


4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


2
[Serrated Arrows](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSerrated%5D+%5BArrows%5D)


75 Cards 



##### 2 (10)



2
[Snapback](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnapback%5D)


4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


2
[Ancient Grudge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D)


2
[Willbender](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWillbender%5D)



##### 3 (17)



4
[Shadowmage Infiltrator](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


3
[Strangling Soot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrangling%5D+%5BSoot%5D)


2
[Phyrexian Totem](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BTotem%5D)


4
[Sulfur Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSulfur%5D+%5BElemental%5D)



##### 4 (11)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


2
[Serrated Arrows](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSerrated%5D+%5BArrows%5D)


1
[Dismal Failure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BFailure%5D)



##### 5 (6)



4
[Vesuvan Shapeshifter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVesuvan%5D+%5BShapeshifter%5D)


2
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)



##### 6 (6)



4
[Brine Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


50 Cards 



##### Common (36)



4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


5
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


9
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


3
[Strangling Soot](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStrangling%5D+%5BSoot%5D)


2
[Snapback](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnapback%5D)


4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


2
[Ancient Grudge](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAncient%5D+%5BGrudge%5D)


2
[Serrated Arrows](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSerrated%5D+%5BArrows%5D)



##### Uncommon (22)



4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


4
[Brine Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBrine%5D+%5BElemental%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


2
[Phyrexian Totem](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPhyrexian%5D+%5BTotem%5D)


4
[Sulfur Elemental](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSulfur%5D+%5BElemental%5D)


2
[Willbender](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWillbender%5D)


1
[Dismal Failure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BFailure%5D)



##### Rare (17)



1
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


4
[Shadowmage Infiltrator](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowmage%5D+%5BInfiltrator%5D)


4
[Vesuvan Shapeshifter](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVesuvan%5D+%5BShapeshifter%5D)


2
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dreadship+Reef)


















Except for the [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse) and [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) that every blue-black control deck played to get blue and black mana, Mitamura has no red mana in his maindeck, and only 1 [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain) in his sideboard. That tiny one-card nod to red mana is still enough to let him sideboard in a White Weenie–crushing 4 [Sulfur Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sulfur+Elemental)s, flashback his [Strangling Soot](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Strangling+Soot)s, and access [Ancient Grudge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancient+Grudge). I'll bet you a dollar he even flashbacked his [Ancient Grudge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ancient+Grudge)s for ![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) over the course of the weekend, without devoting *any* cards to producing green mana.







#### Guillaume Wafo-Tapa


##### 






![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)





[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (7)



2
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


1
[Triskelavus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTriskelavus%5D)



##### Sorcery (4)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)



##### Instant (19)



1
[Haunting Hymn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BHymn%5D)


2
[Think Twice](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


1
[Snapback](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnapback%5D)


2
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)



##### Artifact (4)



4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)



##### Land (26)



4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


4
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


10
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


1
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


1
[Molten Slagheap](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMolten%5D+%5BSlagheap%5D)


1
[Academy Ruins](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcademy%5D+%5BRuins%5D)


1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


60 Cards 


##### Sideboard (15)



1
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


1
[Fortune Thief](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFortune%5D+%5BThief%5D)


1
[Plains](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


1
[Disenchant](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisenchant%5D)


1
[Temporal Isolation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemporal%5D+%5BIsolation%5D)


2
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


3
[Premature Burial](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPremature%5D+%5BBurial%5D)


3
[Detritivore](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDetritivore%5D)




##### White (4)



1
[Disenchant](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisenchant%5D)


1
[Temporal Isolation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemporal%5D+%5BIsolation%5D)


2
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)



##### Blue (20)



2
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


2
[Think Twice](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


1
[Snapback](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnapback%5D)



##### Black (14)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


1
[Haunting Hymn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BHymn%5D)


3
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


3
[Premature Burial](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPremature%5D+%5BBurial%5D)



##### Red (4)



1
[Fortune Thief](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFortune%5D+%5BThief%5D)


3
[Detritivore](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDetritivore%5D)



##### Colorless (33)



4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


4
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


10
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


1
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


1
[Molten Slagheap](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMolten%5D+%5BSlagheap%5D)


1
[Academy Ruins](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcademy%5D+%5BRuins%5D)


1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


1
[Triskelavus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTriskelavus%5D)


4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


1
[Plains](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


75 Cards 



##### 1 (3)



2
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)



##### 2 (12)



4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


2
[Think Twice](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D)


1
[Snapback](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnapback%5D)


1
[Disenchant](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisenchant%5D)


1
[Temporal Isolation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemporal%5D+%5BIsolation%5D)


3
[Premature Burial](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPremature%5D+%5BBurial%5D)



##### 3 (7)



4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


3
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)



##### 4 (16)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


3
[Detritivore](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDetritivore%5D)



##### 5 (5)



2
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


1
[Fortune Thief](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFortune%5D+%5BThief%5D)



##### 6 (3)



2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


1
[Haunting Hymn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BHymn%5D)



##### 7 (1)



1
[Triskelavus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTriskelavus%5D)


47 Cards 



##### Common (35)



4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


10
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


1
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


2
[Think Twice](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThink%5D+%5BTwice%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


1
[Snapback](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnapback%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


1
[Plains](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


1
[Disenchant](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisenchant%5D)


1
[Temporal Isolation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemporal%5D+%5BIsolation%5D)



##### Uncommon (19)



4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


1
[Molten Slagheap](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMolten%5D+%5BSlagheap%5D)


1
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


1
[Haunting Hymn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BHymn%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


3
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


2
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)


3
[Premature Burial](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPremature%5D+%5BBurial%5D)



##### Rare (21)



4
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Academy Ruins](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAcademy%5D+%5BRuins%5D)


2
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


1
[Triskelavus](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTriskelavus%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


1
[Fortune Thief](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFortune%5D+%5BThief%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


3
[Detritivore](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDetritivore%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Terramorphic+Expanse)


















Pro Tour–Yokohama Champion Wafo-Tapa takes the strategy a step further by including both a red package ([Fortune Thief](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fortune+Thief), 3 [Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore), and a [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)) and a white package ([Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant), [Temporal Isolation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Temporal+Isolation), 2 [Pull from Eternity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pull+from+Eternity), and a [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains)) in his sideboard. You can see in his [Top 8 match](/en/articles/archive/event-coverage/semifinals-rally-caps-2007-04-22) against Mark Herberholz how crucial both packages were in winning the [Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore)-your-Urza's-Factories wars.







#### Mark Herberholz


##### 






![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)





[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Creature (5)



1
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


2
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)



##### Sorcery (4)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)



##### Instant (18)



1
[Haunting Hymn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BHymn%5D)


2
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


3
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


1
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)


1
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


1
[Disenchant](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisenchant%5D)


3
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)



##### Artifact (4)



4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)



##### Enchantment (2)



1
[Temporal Isolation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemporal%5D+%5BIsolation%5D)


1
[Teferi's Moat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi%5D+%5BMoat%5D)



##### Land (27)



8
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


3
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


3
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Plains](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


2
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


2
[Calciform Pools](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCalciform%5D+%5BPools%5D)


60 Cards 


##### Sideboard (15)



1
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


2
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


1
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


1
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)


2
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


1
[Teferi's Moat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi%5D+%5BMoat%5D)


1
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


1
[Dismal Failure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BFailure%5D)


2
[Magus of the Tabernacle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagus%5D+%5Bof%5D+%5Bthe%5D+%5BTabernacle%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


2
[Detritivore](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDetritivore%5D)




##### White (6)



1
[Temporal Isolation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemporal%5D+%5BIsolation%5D)


2
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)


1
[Disenchant](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisenchant%5D)


2
[Magus of the Tabernacle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagus%5D+%5Bof%5D+%5Bthe%5D+%5BTabernacle%5D)



##### Blue (18)



1
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


2
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


4
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


1
[Dismal Failure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BFailure%5D)



##### Black (14)



1
[Haunting Hymn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BHymn%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


2
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


4
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


3
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)



##### Red (2)



2
[Detritivore](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDetritivore%5D)



##### Multi colored (2)



2
[Teferi's Moat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi%5D+%5BMoat%5D)



##### Colorless (33)



8
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


3
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


4
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Plains](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


2
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


2
[Calciform Pools](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCalciform%5D+%5BPools%5D)


4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


75 Cards 



##### 1 (5)



2
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)


3
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)



##### 2 (6)



4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


1
[Temporal Isolation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemporal%5D+%5BIsolation%5D)


1
[Disenchant](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisenchant%5D)



##### 3 (6)



2
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)



##### 4 (21)



4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


4
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


4
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


1
[Dismal Failure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BFailure%5D)


2
[Magus of the Tabernacle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagus%5D+%5Bof%5D+%5Bthe%5D+%5BTabernacle%5D)


2
[Detritivore](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDetritivore%5D)



##### 5 (5)



1
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


2
[Teferi's Moat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi%5D+%5BMoat%5D)



##### 6 (3)



2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


1
[Haunting Hymn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BHymn%5D)


46 Cards 



##### Common (35)



8
[Island](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


3
[Swamp](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


4
[Terramorphic Expanse](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTerramorphic%5D+%5BExpanse%5D)


1
[Plains](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


4
[Prismatic Lens](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrismatic%5D+%5BLens%5D)


4
[Tendrils of Corruption](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTendrils%5D+%5Bof%5D+%5BCorruption%5D)


4
[Cancel](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCancel%5D)


4
[Mystical Teachings](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMystical%5D+%5BTeachings%5D)


1
[Temporal Isolation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTemporal%5D+%5BIsolation%5D)


1
[Disenchant](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisenchant%5D)


1
[Mountain](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)



##### Uncommon (18)



4
[Dreadship Reef](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDreadship%5D+%5BReef%5D)


2
[Urza's Factory](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrza%5D+%5BFactory%5D)


2
[Calciform Pools](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCalciform%5D+%5BPools%5D)


1
[Haunting Hymn](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BHymn%5D)


2
[Sudden Death](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSudden%5D+%5BDeath%5D)


2
[Pull from Eternity](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPull%5D+%5Bfrom%5D+%5BEternity%5D)


4
[Careful Consideration](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCareful%5D+%5BConsideration%5D)


1
[Dismal Failure](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDismal%5D+%5BFailure%5D)



##### Rare (22)



4
[Urborg, Tomb of Yawgmoth](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BUrborg,%5D+%5BTomb%5D+%5Bof%5D+%5BYawgmoth%5D)


1
[Teferi, Mage of Zhalfir](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi,%5D+%5BMage%5D+%5Bof%5D+%5BZhalfir%5D)


2
[Draining Whelk](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDraining%5D+%5BWhelk%5D)


2
[Aeon Chronicler](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAeon%5D+%5BChronicler%5D)


4
[Damnation](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDamnation%5D)


3
[Extirpate](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BExtirpate%5D)


2
[Teferi's Moat](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTeferi%5D+%5BMoat%5D)


2
[Magus of the Tabernacle](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagus%5D+%5Bof%5D+%5Bthe%5D+%5BTabernacle%5D)


2
[Detritivore](http://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDetritivore%5D)


75 Cards 




![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)


















Herberholz deployed a similar red sideboard package as Wafo-Tapa, then moved 4 white spells into his maindeck and increased his nod to white mana to 1 [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) and 2 [Calciform Pools](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Calciform+Pools).


***So Blue-Black Control gets to play some white and red spells. Why is that bad?***


I think this phenomenon hurts the format a bit. Here's why: There were tons of blue-black control decks. Some of them included red in the main deck or sideboard. Some included white in the maindeck or sideboard. Some did both. But they're all still fundamentally the same deck, usually built around a core of [Mystical Teachings](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Teachings), [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation), [Cancel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel), [Careful Consideration](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Careful+Consideration), [Aeon Chronicler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aeon+Chronicler), and [Draining Whelk](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Draining+Whelk), with a host of minor tweaks.


What if the format's best two-color fixers weren't [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) and [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse), but the ten *Ninth Edition* painlands instead? Then if a control deck builder wanted the power to stop [Aeon Chronicler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aeon+Chronicler) with [Pull from Eternity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pull+from+Eternity) and stop [Stormbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbind) with [Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant), he or she could build white-black, white-blue, or white-red control with the help of [Caves of Koilos](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Caves+of+Koilos), [Adarkar Wastes](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adarkar+Wastes), or [Battlefield Forge](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battlefield+Forge), and a handful of [Plains](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains). If he or she wanted the power to use [Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore), play [Void](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Void), threaten lethal [Disintegrate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disintegrate), kill Urza's factories, or flash out [Sulfur Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sulfur+Elemental), he or she could play red-black, red-blue, or red-white control deck with the appropriate painlands and [Mountain](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mountain)s.


If the best two-color mana fixers were not also five-color mana fixers, then there would be more of a distinction between blue-white true control, black-red true control, blue-black true control, and so on, each with its own strengths and vulnerabilities. It's good **Magic** when blue-white is awesome against [Stormbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbind) but has problems against [Urza's Factory](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Factory), while black-red true control is awesome against [Urza's Factory](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%27s+Factory) but has problems with [Stormbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbind). Then when you're playing blue-black and [Stormbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbind) is beating you up a lot, you think "Wow, maybe I should think about blue-white control instead, so I could beat [Stormbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbind)."


If blue-white, black-red, and blue-black control all became distinctly different decks, then the diversity of that format's metagame would increase. Players would get more choices of what decks to play. You would get to fight more varied opposing decks over the course of the tournament. And you could tune your deck to be more effective against the decks you most fear by including more of the cards that cause big problems for those tough opponents.


 




|  |
| --- |
| True Control Decks in Hypothetical *Time Spiral-Planar Chaos* Block Constructed with Painlands |
| **Colors** | **Pros** | **Vulnerabilities** |
|  /  | * Handles expensive spells by using countermagic
* Handles [Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore) and [Aeon Chronicler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aeon+Chronicler) by using [Pull from Eternity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pull+from+Eternity)
* Handles [Stormbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbind) & [Sacred Mesa](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sacred+Mesa) by using [Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant)
* Awesome card drawing
 | * Weenie hordes
* Burn
* [Urza’s Factory](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%E2%80%99s+Factory)
 |
|  /  | * Handles weenie hordes with [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation) and [Sulfur Elemental](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sulfur+Elemental)
* Handles [Urza’s Factory](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%E2%80%99s+Factory) with [Avalanche Riders](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Avalanche+Riders)
* Can use [Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore)
* Can threaten Lethal [Disintegrate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disintegrate)s
* [Stupor](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stupor), [Void](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Void), [Haunting Hymn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Haunting+Hymn)
* Life gain with Tendrils
 | * [Stormbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbind)
* Topdecked spells
* No card drawing
* [Aeon Chronicler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aeon+Chronicler)
* [Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore)
 |
|  /  | * Handles expensive spells by using countermagic
* Awesome card drawing
* Handles weenie hordes with [Damnation](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Damnation)
* Life gain with Tendrils
 | * [Stormbind](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stormbind)
* [Urza’s Factory](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Urza%E2%80%99s+Factory)
* [Aeon Chronicler](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aeon+Chronicler)
* [Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore)
 |

At the actual PT–Yokohama, almost all the true control decks were base blue-black decks that could use all the colors' strengths ([Detritivore](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Detritivore), [Teferi's Moat](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Teferi%27s+Moat), etc.), could cover every chink in the armor ([Pull from Eternity](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pull+from+Eternity), [Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant), [Avalanche Riders](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Avalanche+Riders), etc.) and had few vulnerabilities, without any mana commitment to other colors. Instead of playing a tournament where you face blue-white control in one round, then mono-red aggro, then black-red control, then white weenie, then blue-black control, then red-green midrange, each of the matchups very different, you were more likely to face three U/B/r/w control decks, one mono-red aggro, one white weenie, and one red-green midrange. I believe that the increased variety of matchups would be more strategic and more fun.


***Three-color and four-color decks can be great for metagames too.***


Don't get me wrong: I think it's great when blue-black deckbuilders say "I want [Disenchant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disenchant) so badly I'm going to go three-color to get it. I'll stretch my mana base to play white-blue lands and some more expensive five-color mana fixers instead of the normal blue-black mana fixers." For example, a *Ravnica*-era deck could stretch beyond the normal two-mana, two-color [Dimir Signet](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dimir+Signet) to play a clunkier three-mana, five-color [Spectral Searchlight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spectral+Searchlight). Then there is a difference between blue-black control and blue-black-white control. The straight blue-black deck has the advantage of faster mana acceleration or taking less damage by having fewer painlands. The problem at PT–Yokohama is that you didn't have to stretch at all or make any sacrifices to get to the extra colors in your mana base—they were already there.


### Looking to the Future... Sight


 



![River of Tears](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=River+of+Tears)

Fortunately for the *Time Spiral* Block Constructed format now in season everywhere, *Future Sight* fixes most of the problem by adding 5 very powerful two-color dual lands: [Graven Cairns](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Graven+Cairns), [Grove of the Burnwillows](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grove+of+the+Burnwillows), [Horizon Canopy](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Horizon+Canopy), [Nimbus Maze](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nimbus+Maze), and [River of Tears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears). These don't come into play tapped (like [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse)) and don't charge you extra mana to use (like [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens)). Many blue-black control players will certainly add [River of Tears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears), keep [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens) and [Terramorphic Expanse](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terramorphic+Expanse), and continue to splash red and white spells. But others will toss out the [Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens)es to focus on two-color decks with the increased speed and consistency of [Graven Cairns](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Graven+Cairns), [River of Tears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears), or [Grove of the Burnwillows](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grove+of+the+Burnwillows). The key is that with *Future Sight* added to the format, players who want to stay two colors get rewarded with more efficient mana fixers ([River of Tears](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=River+of+Tears)) than the players who want four colors of cards ([Prismatic Lens](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prismatic+Lens)). We're interested to see how the format evolves and how closely it matches our Block Constructed playtesting, and we'll be watching to see what happens.

Some of the sets even further down the road also have both two-color mana fixers and clunkier five-color mana fixers. When those sets' Block Constructed formats arrive, will the sleek speed of the two-color mana fixers take the forefront, or will the temptation of lots of colors lead control players people to go the four-color route? I'm betting on the former, and we'll see how it unfolds.


I had a lot of fun co-designing, playtesting and watching *Time Spiral*-*Planar Chaos*-*Future Sight* Block Constructed, and I hope you get a chance to give it a try! Let me know what you think about the format (or anything else you think R&D is doing right or wrong!) in the email link at the bottom.


Look for last week's poll results from Aaron next week.


### This Week's Poll:




|[The survey originally included in this article has been removed.]


|  |








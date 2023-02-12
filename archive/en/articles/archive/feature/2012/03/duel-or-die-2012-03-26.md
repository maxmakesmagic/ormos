
---
[Link to Wayback Machine](https://web.archive.org/web/20211209043629/https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26)

[_metadata_:author]:- "Mark Gottlieb"
[_metadata_:description]:- "Hello to everyone in Internetlandia! I haven't written anything for the Magic website in many a moon. Let's just say I was on an... extended vacation. But my parole officer is encouraging me to make a `good-faith attempt to re-enter society` (whatever that means), so here I am, back at my old stomping grounds. Today I'll be taking you behind the scenes of the creation of Duel"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "353521"
[_metadata_:publish_date]:- "2012-03-26"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Duel or Die"
[_metadata_:wayback_capture_timestamp]:- "2021-12-09 04:36:29"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211209043629id_/https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/duel-or-die-2012-03-26"
---


Duel or Die
===========



 Posted in **Feature**
 on March 26, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markgottlieb.jpg)
By Mark Gottlieb











Hello to everyone in Internetlandia! I haven't written anything for the **Magic** website in many a moon. Let's just say I was on an... extended vacation. But my parole officer is encouraging me to make a "good-faith attempt to re-enter society" (whatever *that* means), so here I am, back at my old stomping grounds. Today I'll be taking you behind the scenes of the creation of *[Duel Decks: Venser vs. Koth](http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/arcana/779)*.


![](https://web.archive.org/web/20150316071631im_/http://www.wizards.com/mtg/images/daily/features/feature188_vklogo.jpg)

Leading a guided tour through *Duel Decks: Venser vs. Koth* is an exciting prospect for me. I was the primary developer who worked on this product, and I love love *love* the way it turned out. This is a super-fun matchup that features dynamic game play, big swings, appeal to different player types, unusual cards that turn out to be surprisingly good, and tons of flavor. And we'll get to all that. But those of you who remember [my stint](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Mark%20Gottlieb) as the writer of [House of Cards](http://www.wizards.com/magic/magazine/archive.aspx?tag=house%20of%20cards&description=house%20of%20cards) (a Johnny-oriented wacky deck column) or my run as the writer of mtg.combos know that I tend to treat **Magic** articles less as opportunities to educate and more as excuses for works of short fiction. Sure, there's probably some**Magic** content in there somewhere, but we all know what the real attraction is. I'd never worked with our new content manager, [Trick](http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Trick%20Jarrett), before, though, so I didn't know if my flights of fancy would fly. I asked him if I could frame the piece within the madcap antics of some very lost conquistadors who wound up looking for gold in Antarctica. He said "No." I asked him if I could write the article from the perspective of the plush cactus toy that sits on [Mark Rosewater](http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20rosewater)'s desk. He said "Not this time." I asked him if I could make up a paragraph in which I pitched him dumb story ideas and he rejected them. He said "Yes," then he told me to get to the dang Duel Decks. Works for me.


### Theme Main Event


Let's start out by asking the most basic question. "*Venser vs. Koth*: Whaaaaa?" (Or, more loquaciously stated, "Why Planeswalkers... and why *these* Planeswalkers?")


![](https://web.archive.org/web/20130614025547id_/http://www.wizards.com/mtg/images/daily/features/feature188_venko.jpg)
Venser, the Sojourner and Koth of the Hammer | Art by [Eric Dechamps](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Eric+Dechamps%22%5D)


The most recent Duel Decks was Ajani vs. Nicol Bolas, which was a Planeswalker battle. This fit the pattern: the late-year Duel Decks featured Planeswalkers (such as Elspeth vs. Tezzeret), and the early-year Duel Decks featured thematic faction fights (such as Knights vs. Dragons). Starting this year, we've switched their order, resulting in two Planeswalker battles in a row. To understand why, let's take a trip through history. Do you remember... 2010?


In 2010, the early-year Duel Decks were Phyrexia vs. The Coalition. The theme was chosen as a primer/reminder/hype vehicle for the return of Phyrexia within the *Scars of Mirrodin* set later that year. But six months was way too long a lead time for this to have any significant impact or synergy. Then, in the Duel Decks of Elspeth vs. Tezzeret, we previewed a couple of *Scars of Mirrodin* cards. Rather than being a splashy tidbit, these previews dominated the conversation, overshadowing the Planeswalkers themselves. And now we've switched things up. Hmmmm. I'll let you draw your own conclusions...


Now that we knew we'd feature Planeswalkers in this matchup, the question of which ones to shine a spotlight on fell to Director of **Magic** R&D Aaron Forsythe and **Magic** Creative Director Brady Dommermuth.


Then they flipped coins.


Kidding! They chose Venser and Koth because they're recent and relevant (as opposed to the more archaic Ajani Vengeant and Nicol Bolas, for example), they're different colors that enable different play styles, and they actually do fight one another in the storyline (briefly, before teaming up, but still). All in all, it's a cool, sexy matchup.


### I Feel a Draft


Now that we knew what the decks were about, it was time to make a first draft of the two decklists. And for that, the powers that be naturally turned to an ex-House of Cards columnist, someone who has proven himself to be a creative, wily, imaginative deck builder with his finger on the pulse of funtastical innovations: ~~Mark Got~~ Chris Millar???!?!??!


![](https://web.archive.org/web/20150316071628im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards1.jpg)

Sorry, I meant "Chris Millar!!!" That's right, it takes not one but *two* former House of Cards columnists to create Duel Decks! Chris dove right into the project and came up with a couple of nifty decks that showcased each Planeswalker's personal styles, played well against one another, and, most crucially,*felt* right. Although fewer than half of the individual cards in the original decks made it through to the final product, these drafts did two very important jobs:



> 
> * They set the tone and themes of the decks.
> * They provided the basis for choosing cards to give alternative art.
> 


What are these themes? Venser's deck was built around his first two abilities. He likes to "blink" things (exile them, then return them to the battlefield), so the deck features cards that want to get blunk (such as those with "enters the battlefield" effects). Of course, that lends itself to including more blinking and self-bouncing effects to interact with them. Similarly, Venser likes to make things unblockable, so the deck features "saboteur" abilities (abilities that trigger when a creature deals combat damage to an opponent), and that lends itself to including more unblockability effects. Plus, since Venser is a tricky-smart white-blue mage, scry was included as an additional theme.


Koth is an earth mage. He has deep affinity for Mountains, so the deck is focused on that: Getting moreMountains onto the battlefield and taking advantage of those Mountains. This includes a landfall theme, but it also includes cards that count Mountains, and some that just check for Mountains in other ways. The deck has a bit of a Bloodfire creature theme, and it also (at the time) had a Flowstone creature theme.


Here are the final decks, filled in with just the individual cards that were in that first draft.


Venser's Deck  








#### 


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (1)



1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)



##### Creature (7)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)



##### Sorcery (2)



2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)



##### Instant (3)



2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)



##### Enchantment (1)



1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)



##### Land (23)



1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)



##### Other (1)



1
???


38 Cards 



##### White (2)



1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)



##### Blue (7)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)



##### Multi colored (5)



1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)



##### Colorless (24)



1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


1
???


38 Cards 



##### 1 (3)



1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)



##### 2 (4)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)



##### 3 (4)



1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)



##### 4 (1)



1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)



##### 5 (2)



1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)


1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)


14 Cards 



##### Common (29)



1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


1
???


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)



##### Uncommon (7)



1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)



##### Rare (1)



1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)



##### Mythic (1)



1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)


38 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flood+Plain)

















Koth's Deck  








#### 


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (1)



1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### Creature (10)



1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)



##### Sorcery (1)



1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)



##### Artifact (3)



1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### Land (25)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)



##### Other (1)



1
???


41 Cards 



##### Red (10)



1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)


1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### Colorless (31)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


1
???


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)


41 Cards 



##### 1 (2)



2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### 2 (2)



2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)



##### 3 (3)



2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)



##### 4 (3)



1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### 5 (3)



1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)



##### 6 (1)



1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)



##### 8 (1)



1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


15 Cards 



##### Common (33)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
???


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### Uncommon (5)



1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)



##### Rare (2)



1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)



##### Mythic (1)



1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)


41 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

















One of the most beautiful aspects of these decks, which survived intact all the way through development, is the "quasi-mirror" (in Chris's words) of Windreaver vs. Torchling. Love it!


![](https://web.archive.org/web/20150316071631im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards7.jpg)

### Heart to Art


At this relatively early stage, the creative team is looped in so we can coordinate our efforts in creating a deck experience that looks and feels as best as it can.


![](https://web.archive.org/web/20150316071629im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards2.jpg)

One aspect of this is that we choose two cards per deck (besides the Planeswalkers) to get a new art treatment. These cards need to warrant this honor by being significantly appealing, by making sense with relation to the Planeswalker, and (in at least some cases) by having upgradable art. The cards we chose here were Anger, Plated Geopede, Path to Exile, and Preordain.


![](https://web.archive.org/web/20150316071629im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards3.jpg)

In addition, we run these decks by Brady Dommermuth and **Magic** Art Director Jeremy Jarvis for their feedback and comments. Typically, Brady will point out when cards don't make flavor sense, and Jeremy will point out when cards have art that, by modern standards, is not up to snuff. I'm too polite to mention any specifics, but while these reviews sometimes frustrate me (it's tough beats to take out a card I've become smitten with for its mechanics), this expert guidance is crucial in crafting a rich and immersive experience.


![](https://web.archive.org/web/20150316071627im_/http://www.wizards.com/mtg/images/daily/features/feature188_preordain.jpg)
Preordain | Art by [Scott Chou](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Scott+Chou%22%5D)


### Refine and Dandy


At this stage, we do what we do best in R&D: playtest and refine. Over and over and over. We swap cards in and out. We speculatively try some cards just to see what they do (and often, what they do is come right back out of the decks). We balance the decks with one another so neither one is an auto-win. (And yes, if you think I'm trying to rub your nose in the fact that my job description includes "Play lots of **Magic**," I am. Nyaaaah.)


A few things jumped out right away, and a few things took time to come to the surface. I don't have a chronological log of each testing session, but here's what I focused on.


**\* Venser's deck was too strong.**


It just couldn't lose. A lot of the coarse early refinement was spent balancing the decks. In Chris's own words, one of the original "themes" of Venser's deck was "infinite 2-for-1s." Powerful? Yes. A recipe for good, dynamic game play? No. Some of the raw card advantage was removed.


![](https://web.archive.org/web/20150316071630im_/http://www.wizards.com/mtg/images/daily/features/feature188_path.jpg)
Path to Exile | Art by [Erica Yang](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Erica+Yang%22%5D)


**\* The search for saboteurs.**


White and blue aren't the most conducive colors for saboteur abilities, and a couple of the ones that started out in the deck (Mask of Memory and Augury Adept) were pretty much impossible to beat if they ever hit. This is some of that raw card advantage that needed to be stripped out. This was on top of Scroll Thief, which remained in the deck. Did these colors have any saboteurs that weren't straight-up card-drawing effects? At this point, Slith Strider and Sigil of Sleep made it into the deck.


![](https://web.archive.org/web/20150316071627im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards4.jpg)

**\* Venser's deck needed more opportunities to be clever.**


This deck spends some of its efforts removing and returning its creatures to the battlefield. When those creatures provide the same benefit each time (like gaining 4 life or scrying 3), that's fine, and useful. But when you have a different, interesting choice to make each time, the deck's depth is deepened. Chris's original draft had Cryptic Annelid, which is a perfect (and oddball) example of this line of thinking. I wanted more of that. To that end, I added in Clone, Primal Plasma, and Sawtooth Loon. I also tried to broaden the range of effects a white-blue deck could create, which is how Kor Cartographergot in there. (Coral Fighters showed up in a later draft for the same reason.)


![](https://web.archive.org/web/20150316071630im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards9.jpg)

**\* Koth is Vulshok.**


Chris tipped his hat to this flavorful theme by including Vulshok Battlegear. I upped the theme withVulshok Morningstar, Vulshok Berserker, and Vulshok Sorcerer. After all, Koth is Vulshok!


![](https://web.archive.org/web/20150316071628im_/http://www.wizards.com/mtg/images/daily/features/feature188_anger.jpg)
Anger | Art by [Svetlin Velinov](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Svetlin+Velinov%22%5D)


**\* More Mountains!**


Chris's first draft counted Mountains. Okay, but... I wanted to COUNT MOUNTAINS. Wayfarer's Baubleand Pilgrim's Eye were supplemented with Journeyer's Kite, Chartooth Cougar, and Armillary Sphere.Spire Barrage and Earth Servant were supplemented with Downhill Charge, Jaws of Stone, Seismic Strike, and Lithophage. We debated these changes. Armillary Sphere, Jaws of Stone, and Seismic Strikewere just in the mono-red Dragons deck (of Knights vs. Dragons). However, since these cards are the only overlaps between the two decks, and they really make this deck hum, I decided they made too much sense not to include. Of course Koth, deals damage based on the number of Mountains you control! Lithophage feels a bit counterintuitive, as it eats the Mountains you've worked so hard to collect, but if any deck has the spare Mountains needed to feed it, this is the one. Go go, 7/7 fatty! On the same "put your Mountains to work" theme, I added another forgotten rare: Volley of Boulders. Mana cost {8R} and flashback cost {RRRRRR}? *That* is some earth magic, and *this* is the deck that can pull that off.


![](https://web.archive.org/web/20150316071629im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards5.jpg)

**\* More landfall!**


In a similar vein, the landfall theme felt perfect in Koth's Mountainous deck, so I turned up the amplitude a bit. Cosi's Ravager showed up, as did Searing Blaze. Koth's deck had always had a burn suite, but now its card selection in this area was strongly tied into its mechanical and flavorful themes.


![](https://web.archive.org/web/20150316071628im_/http://www.wizards.com/mtg/images/daily/features/feature188_plated.jpg)
Plated Geopede | Art by [Johann Bodin](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Johann+Bodin%22%5D)


**\* OMG emblems!**


Emblems were a technological innovation created late in *Scars of Mirrodin* development to allow Venser and Koth's ultimate abilities to work the way we ideally wanted them to. (You can think of an emblem like an enchantment that can't possibly be removed, except it's not technically an enchantment and it lives out in the command zone rather than the battlefield. You can think of the command zone as the place where rainbows and smiley faces are born.) We didn't print physical representations of those emblems in *Scars of Mirrodin*, but we had the opportunity to do so here! The creative team came up with an emblem treatment, and this Duel Decks was all set to be the world premiere of printed emblems... until Sorin, Lord of Innistrad stole our thunder because *Dark Ascension* came out first. But now you know who's riding whose coattails. Anyway, since each deck would come with an emblem, we didn't have room on the press sheets to print any tokens, so I decided not to have any token-producing cards in these decks. It seemed cleaner that way.


![](https://web.archive.org/web/20150316071628im_/http://www.wizards.com/mtg/images/daily/features/feature188_emblems.jpg)

After a couple months of testing, changing, and testing again, here's how the decks stood.


Venser's Deck  








#### 


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (1)



1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)



##### Creature (16)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Clone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Galepowder Mage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D)


1
[Kor Cartographer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


1
[Primal Plasma](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D)


1
[Sawtooth Loon](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


2
[Slith Strider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D)


1
[Wall of Denial](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D)


1
[Whitemane Lion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)



##### Sorcery (2)



2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)



##### Instant (5)



2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


1
[Safe Passage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D)


1
[Vanish into Memory](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D)



##### Enchantment (3)



1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Sigil of Sleep](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D)


1
[Steel of the Godhead](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D)



##### Land (24)



1
[Azorius Chancery](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D)


1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)



##### Other (1)



1
???


52 Cards 



##### White (6)



1
[Galepowder Mage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D)


1
[Kor Cartographer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D)


1
[Whitemane Lion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


1
[Safe Passage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D)



##### Blue (12)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Clone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


1
[Primal Plasma](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


2
[Slith Strider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)


1
[Sigil of Sleep](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D)



##### Multi colored (9)



1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Sawtooth Loon](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D)


1
[Wall of Denial](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Steel of the Godhead](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D)


1
[Vanish into Memory](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D)


1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)



##### Colorless (25)



1
[Azorius Chancery](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D)


1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


1
???


52 Cards 



##### 1 (4)



1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)


1
[Sigil of Sleep](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D)



##### 2 (5)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Whitemane Lion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D)


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)



##### 3 (9)



1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


2
[Slith Strider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D)


1
[Wall of Denial](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Safe Passage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D)


1
[Steel of the Godhead](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D)



##### 4 (7)



1
[Clone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Galepowder Mage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D)


1
[Kor Cartographer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D)


1
[Primal Plasma](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D)


1
[Sawtooth Loon](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D)


1
[Vanish into Memory](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D)



##### 5 (2)



1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)


1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)


27 Cards 



##### Common (35)



1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Kor Cartographer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


1
[Primal Plasma](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


1
[Whitemane Lion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D)


1
???


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)


1
[Safe Passage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D)


1
[Sigil of Sleep](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D)


1
[Steel of the Godhead](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D)



##### Uncommon (13)



1
[Azorius Chancery](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D)


1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Sawtooth Loon](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D)


2
[Slith Strider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D)


1
[Wall of Denial](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Vanish into Memory](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D)



##### Rare (3)



1
[Clone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D)


1
[Galepowder Mage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)



##### Mythic (1)



1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)


52 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Chancery)

















Koth's Deck  








#### 


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (1)



1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### Creature (16)



1
[Æther Membrane](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D)


1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Chartooth Cougar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D)


1
[Cosi's Ravager](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Lithophage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Vulshok Berserker](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D)


1
[Vulshok Sorcerer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D)



##### Sorcery (3)



1
[Jaws of Stone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)


1
[Volley of Boulders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D)



##### Instant (4)



1
[Downhill Charge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D)


1
[Searing Blaze](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D)


2
[Seismic Strike](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D)



##### Artifact (6)



1
[Armillary Sphere](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D)


1
[Journeyer's Kite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)


1
[Vulshok Morningstar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### Land (25)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)



##### Other (1)



1
???


56 Cards 



##### Red (22)



1
[Æther Membrane](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D)


1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Chartooth Cougar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D)


1
[Cosi's Ravager](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Lithophage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Vulshok Berserker](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D)


1
[Vulshok Sorcerer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D)


1
[Downhill Charge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D)


1
[Jaws of Stone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D)


1
[Searing Blaze](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D)


2
[Seismic Strike](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)


1
[Volley of Boulders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D)


1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### Colorless (34)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


1
???


1
[Armillary Sphere](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D)


1
[Journeyer's Kite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)


1
[Vulshok Morningstar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)


56 Cards 



##### 1 (2)



2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### 2 (6)



2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Armillary Sphere](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D)


1
[Journeyer's Kite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D)


1
[Searing Blaze](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D)


1
[Vulshok Morningstar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D)



##### 3 (8)



1
[Æther Membrane](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


1
[Vulshok Sorcerer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D)


1
[Downhill Charge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D)


2
[Seismic Strike](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)



##### 4 (5)



1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Cosi's Ravager](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D)


1
[Vulshok Berserker](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D)


1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### 5 (4)



1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Lithophage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)



##### 6 (3)



1
[Chartooth Cougar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Jaws of Stone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D)



##### 8 (1)



1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)



##### 9 (1)



1
[Volley of Boulders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D)


30 Cards 



##### Common (42)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


1
[Chartooth Cougar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D)


1
[Cosi's Ravager](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Vulshok Berserker](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D)


1
[Vulshok Sorcerer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D)


1
???


1
[Armillary Sphere](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D)


1
[Downhill Charge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D)


1
[Searing Blaze](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D)


2
[Seismic Strike](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### Uncommon (8)



1
[Æther Membrane](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D)


1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Jaws of Stone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)


1
[Vulshok Morningstar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D)



##### Rare (5)



1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Lithophage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Journeyer's Kite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D)


1
[Volley of Boulders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D)



##### Mythic (1)



1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)


56 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)

















### Finish Them!


As you can see, the decks were really rounding into shape, but there were still some crucial aspects that needed to be improved.


**\* Go with the Flowstone.**


Playtester extraordinaire Mons Johnson was the first to make this point. Koth's deck featured a number of Flowstone creatures, which are a flavorful execution of earth magic. However, it was frustrating that you'd have eight Mountains on the battlefield, but you'd be unable to pump up Flowstone Shamblermore than once (because it'd die!) I was reluctant to replace these with straight-up firebreathers because it reminded me of Chandra's deck. Notably, Koth's deck is the fourth mono-red Duel Deck, after Goblins, Chandra, and Dragons, so it was important that this played differently than all of those. But by this point, I was convinced that it would, so in came a couple Fiery Hellhounds and a Pygmy Pyrosaur.


![](https://web.archive.org/web/20150316071631im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards6.jpg)

**\* It's Millar time.**


After a spate of testing and changing, I looped Chris back in for his analysis and feedback. He was pretty happy with the progression the decks had taken, and made some excellent suggestions. The best one was to add Stone Giant to Koth's deck. It's so simple, so flavorful, so brilliant! What a combo with the new firebreathers. That went in immediately... and it caused me to look for other earth-themed cards. Naturally, I found one of the goofiest cards in recent memory: Greater Stone Spirit. This *Coldsnap*throwback mines nostalgia for cards no one actually remembers: It's like a Stone Spirit that can cast Stonehands! I added it to Koth's deck as a lark, but soon found that it is *amazing* in there. It's a stupendous mana sink for Koth's million Mountains; goofy or not, this dude is a dangerous threat. I am unreasonably proud of myself for adding this card to the deck.


![](https://web.archive.org/web/20150316071630im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards8.jpg)

**\* The ping is the thing.**


One dismaying trend that we noticed in testing is that Vulshok Sorcerer would dominate the battlefield if it showed up in a game. In a development note, I wrote that it kills seven of Venser's creatures outright, shutting down the deck and rendering many cards in the deck dead draws. On the other hand, it was a vital check to both Windreaver and Mistmeadow Witch; I was concerned that if the Sorcerer was removed from the deck, *those* cards would become unstoppable. Rather than remove it, I opted to bend Venser's deck around fighting it to some extent. For example, the "When this enters the battlefield, you gain 4 life" card changed from Lone Missionary to Jedit's Dragoons. Plus, in another lightning strike of "perfect card, perfect time" similar to Greater Stone Spirit, Angelic Shield was added to Venser's deck. It's white-blue, it pumps up everything defensively to foil the Sorcerer and the damage-splitting spells, and it supports Venser's self-bounce/recast theme.


![](https://web.archive.org/web/20150316071629im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards10.jpg)

**\* Point/counterpoint.**


Let me expand on that last point for a bit. One of the most fun aspects of Duel Decks is that they're tuned to fight one another. That leads to opportunities for situational cards to shine like stars, or for cards that are normally amazingly good to maybe be a bit more balanced. For example, I added a pair of Walls into the decks earlier in development. Koth got the goofy card Æther Membrane. It's fantastic flying defense in a mono-red deck... but Venser's deck *likes* to have many of its creatures bounced back to hand so they can be recast. Huh. Venser, meanwhile, got Wall of Denial, which Koth can't target at all... but which a pumped-up Fiery Hellhound could take down without too much problem. However, if there's an 8/2 Fiery Hellhound on the board, Venser's Vanish into Memory is a *stunning* card! It's good under normal circumstances, but when you're temporarily removing a threat from the board, drawing eight cards, and discarding only two? Like I said, stunning. Overrule is also a fascinating card in this matchup. At first glance, it seems bad, because Koth's deck is so good at getting extra Mountains out. But Koth's deck also casts plenty of gigantic spells, which are relatively easy to counter this way—while you gain some life to counteract Koth's burn.


![](https://web.archive.org/web/20150316071630im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards11.jpg)

**\*Bomb Squad.**


I believe it was Erik Lauer who pointed out the last issue that we addressed. By now, Koth's deck was running like a dream. It would hold its own in the early game, staving off Venser's tricks and disruption while building its mana base... then, after a certain point, something would click and it'd start dropping haymakers. 4/10 Earth Servant! 9/1 Pygmy Pyrosaur! A couple of 6-damage Volley of Boulders strikes! Venser's deck, on the other hand, could win through extremely careful tactics that generated incremental advantage over the course of the game, plus some small evasive attackers. Basically, things had to go perfectly, and you needed to play optimally. There was nearly no room for error. I had achieved the dichotomies of play styles that I wanted: Koth's deck for the brutal brawler, Venser's deck for the clever tactician. But Venser's deck needed some juice. Sometimes it needed the haymaker too. What was the point of all the scrying and Looning if there wasn't anything specific to dig for? In came a couple of bomby rare win conditions: Sunblast Angel and Sphinx of Uthuun. If you want to attack with them for the win, great. If you want to blink them out and in for the win, great. The deck had been Venser than most... but now it was the Vensest.


![](https://web.archive.org/web/20150316071628im_/http://www.wizards.com/mtg/images/daily/features/feature188_2Cards12.jpg)

Venser's Deck  






#### 


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (1)



1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)



##### Creature (23)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Cache Raiders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCache%5D+%5BRaiders%5D)


1
[Clone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D)


1
[Coral Fighters](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoral%5D+%5BFighters%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Galepowder Mage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D)


1
[Jedit's Dragoons](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJedit%5D+%5BDragoons%5D)


1
[Kor Cartographer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D)


1
[Minamo Sightbender](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo%5D+%5BSightbender%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


1
[Primal Plasma](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D)


1
[Sawtooth Loon](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


1
[Sky Spirit](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BSpirit%5D)


2
[Slith Strider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D)


1
[Sphinx of Uthuun](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSphinx%5D+%5Bof%5D+%5BUthuun%5D)


1
[Sunblast Angel](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunblast%5D+%5BAngel%5D)


1
[Wall of Denial](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D)


1
[Whitemane Lion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)



##### Sorcery (3)



2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)


1
[Revoke Existence](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D)



##### Instant (5)



2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


1
[Safe Passage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D)


1
[Vanish into Memory](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D)



##### Enchantment (4)



1
[Angelic Shield](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAngelic%5D+%5BShield%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Sigil of Sleep](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D)


1
[Steel of the Godhead](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D)



##### Land (24)



1
[Azorius Chancery](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D)


1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


60 Cards 



##### White (9)



1
[Galepowder Mage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D)


1
[Jedit's Dragoons](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJedit%5D+%5BDragoons%5D)


1
[Kor Cartographer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D)


1
[Sunblast Angel](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunblast%5D+%5BAngel%5D)


1
[Whitemane Lion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


1
[Revoke Existence](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D)


1
[Safe Passage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D)



##### Blue (16)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Cache Raiders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCache%5D+%5BRaiders%5D)


1
[Clone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D)


1
[Coral Fighters](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoral%5D+%5BFighters%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Minamo Sightbender](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo%5D+%5BSightbender%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


1
[Primal Plasma](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


2
[Slith Strider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D)


1
[Sphinx of Uthuun](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSphinx%5D+%5Bof%5D+%5BUthuun%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)


1
[Sigil of Sleep](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D)



##### Multi colored (11)



1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Sawtooth Loon](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D)


1
[Sky Spirit](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BSpirit%5D)


1
[Wall of Denial](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)


1
[Angelic Shield](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAngelic%5D+%5BShield%5D)


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Steel of the Godhead](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D)


1
[Vanish into Memory](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D)


1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)



##### Colorless (24)



1
[Azorius Chancery](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D)


1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


60 Cards 



##### 1 (4)



1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)


1
[Sigil of Sleep](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D)



##### 2 (9)



1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Coral Fighters](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoral%5D+%5BFighters%5D)


1
[Minamo Sightbender](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo%5D+%5BSightbender%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Whitemane Lion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D)


1
[Angelic Shield](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAngelic%5D+%5BShield%5D)


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Revoke Existence](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D)



##### 3 (10)



1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


1
[Sky Spirit](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BSpirit%5D)


2
[Slith Strider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D)


1
[Wall of Denial](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Safe Passage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D)


1
[Steel of the Godhead](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D)



##### 4 (7)



1
[Clone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Galepowder Mage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D)


1
[Kor Cartographer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D)


1
[Primal Plasma](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D)


1
[Sawtooth Loon](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D)


1
[Vanish into Memory](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D)



##### 5 (3)



1
[Cache Raiders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCache%5D+%5BRaiders%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)


1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)



##### 6 (2)



1
[Jedit's Dragoons](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJedit%5D+%5BDragoons%5D)


1
[Sunblast Angel](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunblast%5D+%5BAngel%5D)



##### 7 (1)



1
[Sphinx of Uthuun](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSphinx%5D+%5Bof%5D+%5BUthuun%5D)


36 Cards 



##### Common (36)



1
[Soaring Seacliff](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoaring%5D+%5BSeacliff%5D)


11
[Island](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D)


7
[Plains](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D)


1
[Augury Owl](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAugury%5D+%5BOwl%5D)


1
[Jedit's Dragoons](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJedit%5D+%5BDragoons%5D)


1
[Kor Cartographer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKor%5D+%5BCartographer%5D)


1
[Neurok Invisimancer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNeurok%5D+%5BInvisimancer%5D)


1
[Primal Plasma](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPrimal%5D+%5BPlasma%5D)


2
[Scroll Thief](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScroll%5D+%5BThief%5D)


1
[Whitemane Lion](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWhitemane%5D+%5BLion%5D)


2
[Overrule](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOverrule%5D)


1
[Path to Exile](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPath%5D+%5Bto%5D+%5BExile%5D)


2
[Preordain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPreordain%5D)


1
[Revoke Existence](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRevoke%5D+%5BExistence%5D)


1
[Safe Passage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSafe%5D+%5BPassage%5D)


1
[Sigil of Sleep](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSigil%5D+%5Bof%5D+%5BSleep%5D)


1
[Steel of the Godhead](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSteel%5D+%5Bof%5D+%5Bthe%5D+%5BGodhead%5D)



##### Uncommon (18)



1
[Azorius Chancery](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D)


1
[Flood Plain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlood%5D+%5BPlain%5D)


1
[New Benalia](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BNew%5D+%5BBenalia%5D)


2
[Sejiri Refuge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSejiri%5D+%5BRefuge%5D)


1
[Cache Raiders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCache%5D+%5BRaiders%5D)


1
[Coral Fighters](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCoral%5D+%5BFighters%5D)


1
[Cryptic Annelid](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCryptic%5D+%5BAnnelid%5D)


1
[Minamo Sightbender](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo%5D+%5BSightbender%5D)


1
[Mistmeadow Witch](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMistmeadow%5D+%5BWitch%5D)


1
[Sawtooth Loon](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSawtooth%5D+%5BLoon%5D)


1
[Sky Spirit](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BSpirit%5D)


2
[Slith Strider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSlith%5D+%5BStrider%5D)


1
[Wall of Denial](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWall%5D+%5Bof%5D+%5BDenial%5D)


1
[Angelic Shield](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAngelic%5D+%5BShield%5D)


1
[Oblivion Ring](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOblivion%5D+%5BRing%5D)


1
[Vanish into Memory](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVanish%5D+%5Binto%5D+%5BMemory%5D)



##### Rare (5)



1
[Clone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BClone%5D)


1
[Galepowder Mage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGalepowder%5D+%5BMage%5D)


1
[Sphinx of Uthuun](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSphinx%5D+%5Bof%5D+%5BUthuun%5D)


1
[Sunblast Angel](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSunblast%5D+%5BAngel%5D)


1
[Windreaver](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWindreaver%5D)



##### Mythic (1)



1
[Venser, the Sojourner](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVenser,%5D+%5Bthe%5D+%5BSojourner%5D)


60 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Chancery)



















Koth's Deck  






#### 


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Planeswalker (1)



1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### Creature (21)



1
[Æther Membrane](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D)


1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Chartooth Cougar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D)


1
[Cosi's Ravager](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


2
[Fiery Hellhound](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BHellhound%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Greater Stone Spirit](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BStone%5D+%5BSpirit%5D)


1
[Lithophage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Pygmy Pyrosaur](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPygmy%5D+%5BPyrosaur%5D)


1
[Stone Giant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStone%5D+%5BGiant%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Vulshok Berserker](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D)


1
[Vulshok Sorcerer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D)



##### Sorcery (3)



1
[Jaws of Stone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)


1
[Volley of Boulders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D)



##### Instant (4)



1
[Downhill Charge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D)


1
[Searing Blaze](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D)


2
[Seismic Strike](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D)



##### Artifact (6)



1
[Armillary Sphere](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D)


1
[Journeyer's Kite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)


1
[Vulshok Morningstar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### Land (25)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


60 Cards 



##### Red (27)



1
[Æther Membrane](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D)


1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Chartooth Cougar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D)


1
[Cosi's Ravager](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


2
[Fiery Hellhound](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BHellhound%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Greater Stone Spirit](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BStone%5D+%5BSpirit%5D)


1
[Lithophage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Pygmy Pyrosaur](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPygmy%5D+%5BPyrosaur%5D)


1
[Stone Giant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStone%5D+%5BGiant%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Vulshok Berserker](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D)


1
[Vulshok Sorcerer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D)


1
[Downhill Charge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D)


1
[Jaws of Stone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D)


1
[Searing Blaze](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D)


2
[Seismic Strike](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)


1
[Volley of Boulders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D)


1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### Colorless (33)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


1
[Armillary Sphere](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D)


1
[Journeyer's Kite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)


1
[Vulshok Morningstar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)


60 Cards 



##### 1 (2)



2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### 2 (7)



2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Pygmy Pyrosaur](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPygmy%5D+%5BPyrosaur%5D)


1
[Armillary Sphere](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D)


1
[Journeyer's Kite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D)


1
[Searing Blaze](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D)


1
[Vulshok Morningstar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D)



##### 3 (10)



1
[Æther Membrane](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D)


2
[Fiery Hellhound](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BHellhound%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


1
[Vulshok Sorcerer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D)


1
[Downhill Charge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D)


2
[Seismic Strike](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)



##### 4 (6)



1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Cosi's Ravager](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D)


1
[Stone Giant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStone%5D+%5BGiant%5D)


1
[Vulshok Berserker](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D)


1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)



##### 5 (4)



1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Lithophage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)



##### 6 (4)



1
[Chartooth Cougar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Greater Stone Spirit](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BStone%5D+%5BSpirit%5D)


1
[Jaws of Stone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D)



##### 8 (1)



1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)



##### 9 (1)



1
[Volley of Boulders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D)


35 Cards 



##### Common (44)



25
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


1
[Chartooth Cougar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChartooth%5D+%5BCougar%5D)


1
[Cosi's Ravager](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCosi%5D+%5BRavager%5D)


2
[Fiery Hellhound](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFiery%5D+%5BHellhound%5D)


2
[Pilgrim's Eye](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPilgrim%5D+%5BEye%5D)


2
[Plated Geopede](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlated%5D+%5BGeopede%5D)


1
[Pygmy Pyrosaur](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPygmy%5D+%5BPyrosaur%5D)


1
[Vulshok Berserker](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBerserker%5D)


1
[Vulshok Sorcerer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BSorcerer%5D)


1
[Armillary Sphere](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArmillary%5D+%5BSphere%5D)


1
[Downhill Charge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDownhill%5D+%5BCharge%5D)


1
[Searing Blaze](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSearing%5D+%5BBlaze%5D)


2
[Seismic Strike](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeismic%5D+%5BStrike%5D)


1
[Spire Barrage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSpire%5D+%5BBarrage%5D)


2
[Wayfarer's Bauble](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWayfarer%5D+%5BBauble%5D)



##### Uncommon (10)



1
[Æther Membrane](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5B%C3%86ther%5D+%5BMembrane%5D)


1
[Anger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAnger%5D)


1
[Bloodfire Kavu](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BKavu%5D)


1
[Earth Servant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BServant%5D)


1
[Geyser Glider](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGeyser%5D+%5BGlider%5D)


1
[Greater Stone Spirit](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BStone%5D+%5BSpirit%5D)


1
[Stone Giant](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BStone%5D+%5BGiant%5D)


1
[Jaws of Stone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJaws%5D+%5Bof%5D+%5BStone%5D)


1
[Vulshok Battlegear](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BBattlegear%5D)


1
[Vulshok Morningstar](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVulshok%5D+%5BMorningstar%5D)



##### Rare (5)



1
[Bloodfire Colossus](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodfire%5D+%5BColossus%5D)


1
[Lithophage](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BLithophage%5D)


1
[Torchling](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTorchling%5D)


1
[Journeyer's Kite](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BJourneyer%5D+%5BKite%5D)


1
[Volley of Boulders](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVolley%5D+%5Bof%5D+%5BBoulders%5D)



##### Mythic (1)



1
[Koth of the Hammer](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKoth%5D+%5Bof%5D+%5Bthe%5D+%5BHammer%5D)


60 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mountain)





















### All Duel Respect


My mission complete, I could now head back to Antarctica, Mayan treasure map in hand. This was one of the most fun projects I've ever worked on, and I hope (and believe) that fun is imbued within the product. It's a blast to play, and I can't wait until you all get to experience it for yourselves.


Enjoy!


Mark


![](https://web.archive.org/web/20150316071631im_/http://www.wizards.com/mtg/images/daily/features/feature188_box.jpg)








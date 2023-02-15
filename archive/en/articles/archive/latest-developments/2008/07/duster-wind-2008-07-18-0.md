
---
[Link to Wayback Machine](https://web.archive.org/web/20220125160532/https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0)

[_metadata_:author]:- "Devin Low"
[_metadata_:description]:- "One little Kithkin who does its job and then some. Some cards are the ones that get all the buzz. The ones people can't stop talking about. The ones always popping up in decklists. The ones always getting traded back and forth. But while Magic development spends a lot of time on these high-profile cards, we also spend a huge amount of time developing even the most humble,"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "623711"
[_metadata_:publish_date]:- "2008-07-18"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Duster in the Wind"
[_metadata_:wayback_capture_timestamp]:- "2022-01-25 16:05:32"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220125160532id_/https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/duster-wind-2008-07-18-0"
---


Duster in the Wind
==================



 Posted in **Latest Developments**
 on July 18, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_DevinLow.jpg)
By Devin Low












One little Kithkin who does its job and then some.
--------------------------------------------------


Some cards are the ones that get all the buzz. The ones people can't stop talking about. The ones always popping up in decklists. The ones always getting traded back and forth. But while **Magic** development spends a lot of time on these high-profile cards, we also spend a huge amount of time developing even the most humble, low-profile cards in the set.


So today I'll take you through how much development can go into even one of the humblest, lowest-profile cards in all of *Eventide*. Today's honoree? The common, white, five-mana 2/3 flier: [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster). While he may not be the talk of the town, he's got several important jobs to do in *Eventide*, and he does them well. And I've got five different development stories to show you how.



![Kithkin Spellduster](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kithkin+Spellduster)

### Test of the Twins


There's a long history of white creatures dissolving enchantments, and *Morningtide* and *Eventide* each had one, until we noticed a problem between them. See if you can spot it:



> 
> CW03\_MOR  
> 
> Puff Pastry  
> 
> 3W  
> 
> Creature - Elemental  
> 
> 0/0  
> 
> Flying  
> 
> CARDNAME comes into play with two +1/+1 counters.  
> 
> 1W, Remove a +1/+1 counter from CARDNAME: Destroy target enchantment.
> 



> 
> CW02\_EVE  
> 
> Winged Demystifier  
> 
> 3W  
> 
> Creature - Kithkin Wizard  
> 
> 2/2  
> 
> Flying  
> 
> Persist (When this creature is put into a graveyard from play, if it had no -1/-1 counters on it, return it to play under its owner's control with a -1/-1 counter on it.)  
> 
> 1W, Sacrifice CARDNAME: Destroy target enchantment.
> 


What's the problem with these two cards? The problem is they're actually both the same card. Each one comes out as a ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 Flier, you can pay ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) and shrink your flier to 1/1 to destroy an enchantment, and then you can pay ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) and sacrifice your flier to destroy a second enchantment. Continuing the similarity, adding +1/+1 counters to either card lets you destroy more enchantments, whether by adding more +1/+1 counter ammunition to spend or by removing the -1/-1 counter from persist. The two versions interact differently against [Shock](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) or combat damage, but the overall role of the two cards is very much the same.


Both *Morningtide* and *Eventide* were in development at the time, and the two cards were too similar. Whether by changing numbers or changing abilities, one of them would have to move. The two cards edged into a tense staring contest. Each card was poised to attack, waiting for the other one to blink. It was so quiet you could hear a +1/+1 counter drop.


Suddenly a fierce hail of demystifying broke out, with enchantments being torn apart right and left! Or maybe that was some movie I saw. Oh right, I am getting it confused with the movie "*Hexhunter vs. [Wispmare](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wispmare): [Tempest of Light](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tempest+of+Light)."* In any case, The *Morningtide* team decided to move its card to ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) with one +1/+1 counter, largely to make room for *Morningtide*'s [Burrenton Bombardier](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burrenton+Bombardier) to change to ![](https://web.archive.org/web/20161225105850im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 flying, and for [Kithkin Zephyrnaut](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Zephyrnaut), [Order of the Golden Cricket](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Order+of+the+Golden+Cricket), and [Ballyrush Banneret](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ballyrush+Banneret) all to settle on 2 power at white common.




|  |  |
| --- | --- |
| [Elvish_Hexhunter](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Elvish%2BHexhunter) | [Wispmare](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Wispmare) |

By now you probably recognize the *Morningtide* and *Eventide* cards as [Shinewend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shinewend) and [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster). The cute part about [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) still being ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 at the time was that when the ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) died and persisted, it basically popped out a [Shinewend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shinewend). And when [Shinewend](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shinewend) got reinforced for 1, it basically popped into a [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster).



![Shinewend](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shinewend)

To smooth out the mana costs and power/toughness of the set, [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) eventually advanced to his final ![](https://web.archive.org/web/20160830042801im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/3 form. The ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227125855im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 2/2 flier slot, once so coveted by the two cards, ended up abandoned by both of them.


### The *Eventide* Style of Persist


Now the second story. Part of the key to block design is finding ways to link the sets in the block together, yet give each of the sets its own unique identity. Well-designed block plans perform this balancing act on a wide spectrum, from large and obvious to small and subtle.


The most obvious, global way that *Shadowmoor* and *Eventide* "compare and contrast" in this manner is that they're both hybrid sets, but one is allied-color and one is enemy-color. On the other end of the spectrum, one of the most subtle ways that *Eventide* is different from *Shadowmoor* is the way the two sets use persist.


*Shadowmoor* has six persist creatures with "comes into play" abilities: [Furystoke Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furystoke+Giant), [Kitchen Finks](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kitchen+Finks), [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), [Puppeteer Clique](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer+Clique), [Twilight Shepherd](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Twilight+Shepherd), and [Woodfall Primus](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woodfall+Primus). *Shadowmoor* has no Persist creatures with "sacrifice me" abilities.




|  |  |
| --- | --- |
| 
Woodfall Primus
 | 
Aerie Ouphes
 |

Conversely, *Eventide* has four Persist creatures with "sacrifice me" abilities: [Aerie Ouphes](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aerie+Ouphes), [Glen Elendra Archmage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage), [Grazing Kelpie](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grazing+Kelpie), and [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster). And *Eventide* has no persist creatures with "comes into play" abilities.


Persist allows you to get two uses of out of either a "comes into play" or a "sacrifice me" ability. But each set's persist creatures get two uses of out their abilities in their own way.


### "Creature — Kithkin"



![Rustic Clachan](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Rustic+Clachan)

Time for a third story. Fellow columnist and **Magic** R&D all-star Doug Beyer did the concepting work for *Eventide*. In addition to his role on the creative team, Doug had also worked on the development teams for *Lorwyn* and *Shadowmoor*, giving him considerable insight into the mechanics of the two blocks. During *Eventide* concepting, Doug used this mechanical knowledge to help set up flavor concepts and creature types that would intentionally flow well into the individual tribal themes of *Lorwyn* and *Morningtide*.


One example is [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster). Before writing out a full concept for the card, Doug wrote this note into Multiverse to show his creative team colleagues what he was leaning towards:



> 
> DB 8/14: Kithkin, to combo with kithkin Reinforce land?
> 


Doug's right. [Burrenton Bombardier](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burrenton+Bombardier), [Mosquito Guard](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosquito+Guard), and [Rustic Clachan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rustic+Clachan) are all Kithkin cards with reinforce, and reinforcing your persist creature to recharge it is a fun little combo. Reinforce cards like the [Pro Tour–winning](/en/articles/archive/event-coverage/top-8-decks-2008-02-16) card [Mosquito Guard](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosquito+Guard) already let you convert spells and lands into +1/+1 counters. Combining them with [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) lets you convert those spells and lands into extra [Demystify](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Demystify)s.


Doug Beyer and *Eventide* lead developer Matt Place also worked together to ensure that [Nettle Sentinel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nettle+Sentinel), [Twinblade Slasher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Twinblade+Slasher), [Talara's Battalion](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Talara%27s+Battalion), and [Bloom Tender](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bloom+Tender) were all Elves, that [Wake Thrasher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wake+Thrasher) was a Merfolk, and the other creatures were particular creature types, in order to open them up to mechanical synergies with *Lorwyn* and *Morningtide*.


### "Creature — Wizard"


Story number four: The "class" creature type is especially relevant on persist cards too. Developer Mons Johnson quickly found during *Shadowmoor* development that having the persist creature [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) be a Goblin Rogue, as the Redcap once was, was a particularly terrible idea.



![Oona's Blackguard](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Oona%27s+Blackguard)

Mons took advantage of the Redcap's creature type by building a deck with [Oona's Blackguard](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard), [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), and sacrifice outlets like [Greater Gargadon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Gargadon) and [Nantuko Husk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Husk). Mons would get [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) and [Oona's Blackguard](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard) into play, then start sacrificing the Redcap to his Husk or Gargadon.


Every time the [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) came back into play with a -1/-1 counter through Persist, [Oona's Blackguard](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard) put a +1/+1 counter on the Redcap because it was a Rogue. There's a rule that a +1/+1 counter and a -1/-1 counter on the same creature annihilate each other and disappear. So the Redcap would be back without any counters on it at all, dealing 2 damage to the opponent's face. Sacrifice the Redcap again, deal 2 more damage. Sacrifice it 8 more times, and, well, you get the idea.


This combo was a little too consistent, especially since one of the combo pieces had persist, and another of the combo pieces didn't even need to be in play (the [Greater Gargadon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Gargadon)). It was enough to get us to change the [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap)'s creature type to the even more flavorful Goblin *Assassin.*


Message to [Scarblade Elite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scarblade+Elite): You're welcome.


Tricky Mons built a similar deck using [Bramblewood Paragon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bramblewood+Paragon), [Nantuko Husk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Husk), and [Safehold Elite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite), who was at the time an Elf Warrior. Infinite sacrifices made the [Nantuko Husk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nantuko+Husk) immediately lethal, and he sometimes added an [Essence Warden](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Essence+Warden) to gain infinite life. [Safehold Elite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite) became an Elf Scout.


Mons had hit the nail on the head twice in a row, and it was enough to make us wonder: Should we just yank Rogue, Warrior, and Wizard—the three creature types with similar lords in *Morningtide*—off of all the persist creatures? This would damage some of the creative choices, since the concept of [Puppeteer Clique](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer+Clique) was very much a Wizard, and the concept of [Scuzzback Marauders](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scuzzback+Marauders) was very much a Warrior.


In the end, as we often decide with infinite win-the-game combos, we decided that these combos between persist and *Morningtide* class lords are actually pretty fun and good for **Magic**, as long as they're not too hyper-efficient. Our playtesting had suggested that that [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), [Oona's Blackguard](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oona%27s+Blackguard), [Safehold Elite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite), and [Bramblewood Paragon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bramblewood+Paragon) all had a shot to be powerful tournament contenders (as they have indeed turned out to be, at varying levels) even without creating infinite win-the-game combos between them.


But if people are willing to commit to their combos with a higher-mana-cost persist creature, instead of the two-mana [Safehold Elite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite) or the very powerful four-mana [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), we wanted to give them the chance to "go infinite" and win the game that way. So while [Safehold Elite](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Safehold+Elite) and [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap) became Scouts and Assassins, you can still go infinite with these combos with five-mana Persist Warriors, Wizards, and Rogues.


Possibilities include [Furystoke Giant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Furystoke+Giant), [Puppeteer Clique](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Puppeteer+Clique), and [Scuzzback Marauders](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scuzzback+Marauders) in *Shadowmoor*, all at five mana. Since [Glen Elendra Archmage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage) is less universal than [Murderous Redcap](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Murderous+Redcap), and doesn't have the Redcap's "comes into play" ability, we were ok with letting [Glen Elendra Archmage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage) and [Sage of Fables](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Fables) create infinite sacrifices, even though [Glen Elendra Archmage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage) matches the Redcap's four mana. Using the [Glen Elendra Archmage](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glen+Elendra+Archmage) in the combo with [Sage of Fables](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Fables) even lets you counter an infinite number of noncreature spells along the way.


![Sage of Fables, Glen Elendra Archmage, and Nantuko Husk](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/fcpics/latest/dl46_cardfan.jpg)


And what's the final *Eventide* card that creates infinite win-the-game sacrifice combos with *Morningtide* class lords? But of course: [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster).


### The Gift of Lockdown


And the final story. All ten [Steel of the Godhead](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steel+of+the+Godhead)–style hybrid Auras in Shadowmoor and Eventide can be totally devastating if they don't get stopped. Fortunately there are a variety of ways to stop them. One of the reasons [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) is so good at blowing up Auras is to put commons into *Shadowmoor* and *Eventide* that are good at blowing up the hybrid Auras before they get too out of hand. Another common that's fantastic at blowing up the Auras in *Eventide* is [Wickerbough Elder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder).



![Gift of the Deity](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gift+of+the+Deity)

But although [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) and [Wickerbough Elder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder) were intended to be able blow up the hybrid Auras, the black-green Aura [Gift of the Deity](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) didn't get the memo. Midway through *Eventide* development, [Gift of the Deity](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) cost ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20210208014640im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black-green.gif), giving [Lure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure), deathtouch, and +2/+2 to black-green creatures.


Many debates had already been waged about whether these ten hybrid Auras should be common or uncommon. The development team leads for *Shadowmoor* and *Eventide* had both concluded that the auras should be both common and very powerful—as long as they landed on the correctly colored creatures and didn't get disrupted by the opponent.


The chance of the Auras getting ruined by the opponent is a big part of why the Auras can be so powerful. When they work, they are awesome. But when you play a [Cerulean Wisps](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cerulean+Wisps) in the middle of combat to turn the opposing enchanted creature blue, turn off all of its Aura's color-based abilities, and kill both the enchanted creature and the Aura while drawing a card in the process, you can totally crush them.


The card "[Lure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure)" has always been a very powerful uncommon. [Lure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure) effects with a power/toughness bonus are even nastier, since you can lock down your opponent from ever building up creatures. For example, if you play [Gift of the Deity](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) on your Rendclaw Troll on turn four and attack, you can kill an opposing creature or two by forcing them to block, and stick your opponent with a nasty dilemma. If your opponent plays anything up to a 3/6, you just attack, force it to block, and kill it, losing nothing. If he or she doesn't play a creature, you just smash your opponent for 4 damage.


If your opponent plays the red-white Aura [Scourge of the Nobilis](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scourge+of+the+Nobilis), [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) and [Wickerbough Elder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder) are decent answers. You'll take some damage, then play your creature and destroy the Aura.



![Wickerbough Elder](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wickerbough+Elder)

But against a four-mana [Gift of the Deity](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity), [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) and [Wickerbough Elder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder) weren't able to answer the problem. If you played a turn-four [Wickerbough Elder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder), it would just get [Lure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure)d and destroyed before it could activate. If you played a turn-five Spellduster Kithkin, it would just get [Lure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure)d and destroyed as well.


On the face of it, [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) could persist back into play and blow the Aura up, and sometimes that would happen. But out of all ten color pairs, black-green has the most creatures with wither (including [Rendclaw Trow](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rendclaw+Trow), [Noxious Hatchling](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Noxious+Hatchling), and often [Woodlurker Mimic](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woodlurker+Mimic)), meaning that [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) could not even persist back into play.


In the end, the combination of [Lure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lure), power-pumping, toughness-pumping, and deathtouch in a four mana version of [Gift of the Deity](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) just locked down too many people too quickly during playtesting, stopping them from playing any more creatures too early. We still loved the thrill of power it gives when you play it, but five mana gives just a bit more breathing room before the pummeling starts.


And it gives you a little more time to play and activate your [Wickerbough Elder](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wickerbough+Elder) or [Kithkin Spellduster](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kithkin+Spellduster) without them getting bludgeoned to death by [Gift of the Deity](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gift+of+the+Deity) before they can activate to destroy it.


### Last Week's Poll




| **Are you going to the *Eventide* Prerelease?** |
| --- |
| Yes | 3736 | 44.4% |
| No | 3476 | 41.3% |
| Not Sure | 1196 | 14.2% |
| **Total** | **8408** | **100.0%** |

Wizards sent a huge contingent, over a dozen people, to the Seattle pre-release to gunsling and talk about *Eventide*. It's hard to resist the lure of playing with real **Magic** cards instead of playtest stickers! Mark Gottlieb happened to find himself in Denver that weekend, so of course he dropped in on the Denver prerelease to gunsling and have a good time.


Mark your calendars: Prereleases will occur all over the world for Shards of Alara on September 27. Many new prereleases will now be happening in local card stores, as well as many pre-releases happening in giant halls just like before.


### This Week's Poll




|  |
| --- |
| **Starting in *Lorwyn,* a sixteenth creature-token-card/rules-card was added to **Magic** packs. Was the change good or bad?** GoodBadIt's complicated |








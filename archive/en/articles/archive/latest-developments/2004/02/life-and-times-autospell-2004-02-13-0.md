
---
[Link to Wayback Machine](https://web.archive.org/web/20221005094642/https://magic.wizards.com/en/articles/archive/latest-developments/life-and-times-autospell-2004-02-13-0)

[_metadata_:author]:- "Aaron Forsythe"
[_metadata_:description]:- "My New Desk When I moved from the web team to R&D last fall, I was assigned Mike Donais’ old desk and expected to supply everyone with Altoids. I’m Aaron Forsythe, former modest Magic professional, former editor and Content Manager of this very website, and current Magic developer. I was recently assigned the somewhat daunting task of filling Randy Buehler’s capable shoes as"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "612046"
[_metadata_:publish_date]:- "2004-02-13"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Life and Times of Autospell"
[_metadata_:wayback_capture_timestamp]:- "2022-10-05 09:46:42"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20221005094642id_/https://magic.wizards.com/en/articles/archive/latest-developments/life-and-times-autospell-2004-02-13-0"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/life-and-times-autospell-2004-02-13-0"
---


The Life and Times of Autospell
===============================



 Posted in **Latest Developments**
 on February 13, 2004 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_aaronforsythe.jpg)
By Aaron Forsythe












### My New Desk


When I moved from the web team to R&D last fall, I was assigned Mike Donais’ old desk and expected to supply everyone with Altoids.


I’m Aaron Forsythe, former modest **Magic** professional, former editor and Content Manager of this very website, and current **Magic** developer. I was recently assigned the somewhat daunting task of filling Randy Buehler’s capable shoes as the “other voice of R&D” here on **magicthegathering.com**. (We all know Mark Rosewater is the lead vocalist; I can only hope to be Mike Mills to his Michael Stipe.) But I was talking about my new desk…


Poor Mike Donais. With his traitorous brother Jeff leaving Wizards for Upper Deck, the suits around here figured Mike was an immediate conflict-of-interest liability and gave him the axe. Rumor has it that they framed him by putting packs of Yu-Gi-Oh! cards in his desk drawers. I shed no tears, however, because that turn of events opened up a sweet desk in the middle of all the action in R&D.




|  |
| --- |
| *Altoid freak and **Magic** expatriate Mike Donais*  |

So I lied a little. Mike still works here; he simply moved from what we call “card-side R&D” to RPG (role-playing games) R&D to work on something called **Dungeons & Dragons**. **Dungeons & Dragons**, or **D&D** for short, is a weird game that I’m told is like EverQuest for people without computers. I can’t imagine it lasting. Anyway, Mike moved over there along with Andrew Finch, another long-time card-side guy, leaving two empty seats in **Magic** land.


I got one of them, the one which previously had something to do with Altoids. The other desk went to former Pro Tour great Matt Place. Matt is our main playtester for Magic expansions that are still in development, a position once held by a former teammate of mine, Pat Chapin, whose old desk has a new tenant as well—former Magic editor and current Thursday hack Mark Gottlieb. As you can see, the seating chart here is not exactly the portrait of stability.


I took Donais’ desk, Matt took Finch’s, and Gottlieb took Chapin’s, which was actually William Jockusch’s for many years. That isn’t all. The multi-talented Devin Low now occupies the seat abandoned when Dave Eckelberry took a job with a Boston software company. Paul Sottosanti has taken the coveted chair between Mark Rosewater and Randy Buehler long occupied by old-school crank Skaff Elias. And Mons Johnson made his triumphant return to Wizards of the Coast by wresting a cube from a very territorial box of *Legends* commons (which were given a corner office as compensation).


What I’m getting at is that I came to R&D as part of a wave of fresh blood. The department is certainly not in the throes another overhaul akin to the post-*Urza’s Saga* fiasco, but due to an increase in the workload for R&D, it has recently incorporated a cadre of real die-hard fun-loving gamers to an already proven core of talent (including Rosewater, Buehler, Brian Schneider, Henry Stern, Brian Tinsman, and many others). This column will be a look into the world of **Magic** development from my eyes—a new guy in the trenches still getting his feet wet, whose fingers are numb from shuffling and whose throat is hoarse from arguing. The current **Magic** group is nothing if not passionate, and we all know that passion often leads to some steamy little tales.


…But I’m not providing Altoids for everyone, sorry. Donais kept two industrial-sized steel canisters of the dusty mints—imagine metal pencil boxes stuffed with broken chalk—on his desk, free for the taking. Nice in theory, but I’m an insatiable snacker. I eat whatever’s in front of me. I can tell you from experience that after about 20 Altoids your breath smells wonderful, but your soft palate has all but dissolved and your stomach is a churning hole of Wintergreen froth. I refuse to expose myself to such hazardous working conditions. So, my lovely coworkers, I can promise you some fine playtesting results, but you ain’t getting any more Altoids. So stop asking.


Enough digression. Knowing that I am competing with [Nate Heiss](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/nh1) for your attention, I’ll stop with the personnel issues, bear down, and move onto some real **Magic** stuff.


### The Life and Times of Autospell


I’m going to take this opportunity to tie up some loose ends from articles that appeared on this site a few months ago. Must be my repressed editor personality struggling to break free. The required reading before we begin is Paul Barclay’s “[Talking About the Weather](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb74)” (especially the part about [Grip of Chaos](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grip+of+Chaos)) and Mark Rosewater’s “[Someday my Imprints Will Come](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr87).”


![](https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/authorpic_briantinsman.jpg)This story starts during the development of the *Scourge* set in the summer of 2002. Brian Tinsman had designed a card called “Blindness” that was driving the rules team insane. The card was a red enchantment that was meant to force all players to choose all their targets for spells and abilities at random. But no one could come up with acceptable wording for that effect, so the development team made the decision to pull the card from the set.


That change was made fairly late in the development cycle—so late, in fact, that art for the Blindness card was already finished. Any card designed to replace it in the set had to be able to use that art.


Brian Tinsman, being the fountain of wackiness that he is, came up with this doozy:


**[Autospell]**  
![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)![](https://web.archive.org/web/20161227130159im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/red.gif)  

Enchantment  

Remove the first instant or sorcery you resolve from the game. At the beginning of your upkeep, put a copy of that spell on the stack.


I. Loved. That. Card. I became fixated on it. It became my pet project for the Future Future League, and with it I built a black-red control deck based on one played by Brian Davis at US Nationals that year. Brian’s deck already got a lot of mileage out of spells with [Recoup](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Recoup), but Autospell made it even more of a card advantage machine.








#### Red-Black Autospell


##### 






![Download Arena Decklist](https://web.archive.org/web/20211024134741im_/https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png)
![](https://web.archive.org/web/20160726232508im_/http://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)






[Decklist](#none)
[Stats](#none)
[Sample Hand](#none)





Sort by:
OverviewColorCostRarity




##### Sorcery (31)



4
[Blackmail](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlackmail%5D)


3
[Innocent Blood](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D)


4
[Chainer's Edict](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChainer%5D+%5BEdict%5D)


4
[Vicious Hunger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVicious%5D+%5BHunger%5D)


3
[Recoup](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRecoup%5D)


4
[Diabolic Tutor](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDiabolic%5D+%5BTutor%5D)


2
[Persecute](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


2
[Haunting Echoes](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BEchoes%5D)


2
[Burning Wish](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning%5D+%5BWish%5D)


1
[Mutilate](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutilate%5D)


1
[Corrupt](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D)


1
[Pyroclasm](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D)



##### Artifact (3)



2
[Millstone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMillstone%5D)


1
[Ensnaring Bridge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnsnaring%5D+%5BBridge%5D)



##### Land (24)



12
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


2
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Bloodstained Mire](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodstained%5D+%5BMire%5D)


4
[Tainted Peak](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTainted%5D+%5BPeak%5D)


2
[Shadowblood Ridge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowblood%5D+%5BRidge%5D)



##### Other (2)



2
Autospell


60 Cards 


##### Sideboard (15)



1
[Innocent Blood](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D)


1
[Persecute](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


1
[Haunting Echoes](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BEchoes%5D)


1
[Mutilate](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutilate%5D)


1
[Ensnaring Bridge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnsnaring%5D+%5BBridge%5D)


1
[Corrupt](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D)


1
[Pyroclasm](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D)


2
[Magnivore](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagnivore%5D)


1
[Decree of Pain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDecree%5D+%5Bof%5D+%5BPain%5D)


1
[Earth Rift](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BRift%5D)


1
[Demolish](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemolish%5D)


1
[Soul Feast](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BFeast%5D)


1
[Flashfires](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfires%5D)


1
[Disrupting Scepter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisrupting%5D+%5BScepter%5D)




##### Black (32)



4
[Blackmail](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlackmail%5D)


4
[Innocent Blood](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D)


4
[Chainer's Edict](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChainer%5D+%5BEdict%5D)


4
[Vicious Hunger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVicious%5D+%5BHunger%5D)


4
[Diabolic Tutor](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDiabolic%5D+%5BTutor%5D)


3
[Persecute](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


3
[Haunting Echoes](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BEchoes%5D)


2
[Mutilate](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutilate%5D)


2
[Corrupt](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D)


1
[Decree of Pain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDecree%5D+%5Bof%5D+%5BPain%5D)


1
[Soul Feast](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BFeast%5D)



##### Red (12)



3
[Recoup](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRecoup%5D)


2
[Burning Wish](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning%5D+%5BWish%5D)


2
[Pyroclasm](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D)


2
[Magnivore](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagnivore%5D)


1
[Earth Rift](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BRift%5D)


1
[Demolish](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemolish%5D)


1
[Flashfires](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfires%5D)



##### Colorless (31)



12
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


2
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Bloodstained Mire](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodstained%5D+%5BMire%5D)


4
[Tainted Peak](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTainted%5D+%5BPeak%5D)


2
[Shadowblood Ridge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowblood%5D+%5BRidge%5D)


2
Autospell


2
[Millstone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMillstone%5D)


2
[Ensnaring Bridge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnsnaring%5D+%5BBridge%5D)


1
[Disrupting Scepter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisrupting%5D+%5BScepter%5D)


75 Cards 



##### 1 (8)



4
[Blackmail](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlackmail%5D)


4
[Innocent Blood](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D)



##### 2 (17)



4
[Chainer's Edict](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChainer%5D+%5BEdict%5D)


4
[Vicious Hunger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVicious%5D+%5BHunger%5D)


3
[Recoup](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRecoup%5D)


2
[Burning Wish](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning%5D+%5BWish%5D)


2
[Millstone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMillstone%5D)


2
[Pyroclasm](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D)



##### 3 (3)



2
[Ensnaring Bridge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnsnaring%5D+%5BBridge%5D)


1
[Disrupting Scepter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisrupting%5D+%5BScepter%5D)



##### 4 (14)



4
[Diabolic Tutor](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDiabolic%5D+%5BTutor%5D)


3
[Persecute](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


2
[Mutilate](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutilate%5D)


2
[Magnivore](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagnivore%5D)


1
[Earth Rift](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BRift%5D)


1
[Demolish](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemolish%5D)


1
[Flashfires](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfires%5D)



##### 5 (4)



3
[Haunting Echoes](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BEchoes%5D)


1
[Soul Feast](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BFeast%5D)



##### 6 (2)



2
[Corrupt](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D)



##### 8 (1)



1
[Decree of Pain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDecree%5D+%5Bof%5D+%5BPain%5D)


49 Cards 



##### Common (26)



12
[Swamp](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSwamp%5D)


2
[Mountain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMountain%5D)


4
[Innocent Blood](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BInnocent%5D+%5BBlood%5D)


4
[Vicious Hunger](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVicious%5D+%5BHunger%5D)


2
Autospell


1
[Earth Rift](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEarth%5D+%5BRift%5D)


1
[Demolish](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDemolish%5D)



##### Uncommon (27)



4
[Tainted Peak](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BTainted%5D+%5BPeak%5D)


4
[Blackmail](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBlackmail%5D)


4
[Chainer's Edict](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BChainer%5D+%5BEdict%5D)


3
[Recoup](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRecoup%5D)


4
[Diabolic Tutor](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDiabolic%5D+%5BTutor%5D)


2
[Millstone](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMillstone%5D)


2
[Corrupt](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCorrupt%5D)


2
[Pyroclasm](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPyroclasm%5D)


1
[Soul Feast](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BFeast%5D)


1
[Flashfires](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BFlashfires%5D)



##### Rare (16)



2
[Shadowblood Ridge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BShadowblood%5D+%5BRidge%5D)


3
[Persecute](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPersecute%5D)


3
[Haunting Echoes](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHaunting%5D+%5BEchoes%5D)


2
[Burning Wish](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBurning%5D+%5BWish%5D)


2
[Mutilate](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMutilate%5D)


2
[Magnivore](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMagnivore%5D)


1
[Decree of Pain](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDecree%5D+%5Bof%5D+%5BPain%5D)


1
[Disrupting Scepter](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDisrupting%5D+%5BScepter%5D)



##### Mythic (6)



4
[Bloodstained Mire](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBloodstained%5D+%5BMire%5D)


2
[Ensnaring Bridge](https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BEnsnaring%5D+%5BBridge%5D)


75 Cards 




![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp)


















If you’re wondering, [Corrupt](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Corrupt) was in fact in *Eighth Edition* for a long time during development.


The deck’s main plan was to use Autospell as a control element, getting free copies of an Edict or a Tutor each turn, eventually setting up a slow [Millstone](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Millstone) kill or a faster [Corrupt](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Corrupt)-on-the-other-copy-of-Autospell kill.


For the most part it worked very well. How can you lose with a free [Burning Wish](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Wish) every turn? Goblins were a main weakness, but I should have been able to compensate for that. But that’s neither here nor there.


Autospell, for all its redeeming qualities, was sadly short-lived in *Scourge*. One strike against it was that [Siege-Gang Commander](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege-Gang+Commander), [Goblin Warchief](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Warchief), and [Sulfuric Vortex](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sulfuric+Vortex) made red extremely powerful in the set, and the team was not keen on adding another potential powerhouse to an already loaded color. The other strike was that ol’ Rosewater had his eye on the card for *Mirrodin* design. I could only stand back and sniffle as my favorite deck was dismantled for good. Those jerks.


With little time left in *Scourge* development, Blindness went back in, got reasonable (if not perfect) wording and became [Grip of Chaos](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grip+of+Chaos), and Autospell was shuttled off to the primordial *Mirrodin* design file.


### From Red to Artifact


Mark had been holding onto a card called Clone Machine for many years, waiting for the right time to stick it into a set. It, like Autospell, allowed you to customize what it did by removing another card from the game. Clone Machine removed a creature card in your hand from the game and then would produce token copies of that creature, not unlike how Autospell gave you a copy of your removed spell each turn.


The two cards formed the basis of the imprint mechanic, which developed into one of the hallmarks of the *Mirrodin* set. Clone Machine, as I’m sure you all know, became [Soul Foundry](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Foundry), and Autospell turned into…


Not just yet. Autospell was put into the *Mirrodin* design file as a card called “Autospell Orb,” an artifact that looked like this:


**[Autospell Orb]**  
![](https://web.archive.org/web/20170413132456im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless5.gif)  

Artifact  

When CARDNAME comes into play, imprint the next instant or sorcery card you play that isn't countered. (To imprint a card, remove it from the game. As long as that card is removed from the game, it is linked to this card.)  

At the beginning of your upkeep, if all the imprinted card's targets can be chosen, put a copy of that card onto the stack. If it has X in its mana cost, X is 0.


Quite a mess, really. There's a lot of unnecessary text there, and no one really understood how the card had a triggered ability that removed a card from the game that hadn't been played yet. But the idea was a good one, so it stayed in the file.


Eventually it was switched to something more like its current incarnation:


**[Autospell Orb]**  
![](https://web.archive.org/web/20170413132456im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless5.gif)  

Artifact  

X, T: Put any card imprinted by CARDNAME into its owner's graveyard. Imprint a instant or sorcery card in your hand. X is that card's mana cost.  

At the beginning of your upkeep, if all the imprinted card's targets can be chosen, put a copy of that card onto the stack.


Although it didn't play quite the same, it was at least more understandable. At some point the *Mirrodin* design and development teams decided to split up the imprint cards into two groups. The cards that imprinted once at the time they came into play would all go into *Mirrodin*. Anything weirder than that (including equipment with imprint) would go into the other sets in the block. And so Autospell Orb was put into *Darksteel*.


It was met with some derision by the *Darksteel* development team. Here are the comments clipped from our database from Randy Buehler, Henry Stern, Brandon Bozzi, Brian Schneider, and editor Del Laugel:


RB 2/6: I liked this card significantly better when it was “the next ...” instead of activated. This version seems busy and it was cool that with the old version you were locked in forever  

HS 2/10 Team agrees.  

DL 2/17: Are you trying to pay the mana cost or the converted mana cost? Mana cost will be tough to template.  

RB 2/18: so the team agreed with half my comment (make it automatically fire) but not the other half (lock it in once and forever)?  

RB 2/21: cool card either way, can we trim a mana?  

DL 2/26: More importantly, can you trim text? There's no way that this fits on a card. (Put into the current MRD imprint template.)  

HS 3/1 Team wants to go back to “autospell orb” templating  

BB 3/10: Boy do I dislike trying to grock imprint cards. Is there anything we could do with the template to make these cards easier to understand?  

bs 3/12: i give up -- just shoot me. that’d be easier than trying to grock this.  

RB 3/25: Fix this please ... it was once very cool (inspired the whole Imprint mechanic in fact). I recommend:  

Autospell Orb  

5  

Artifact  

X, T: Remove from the game an instant or sorcery from your hand with converted mana cost X. (It is imprinted on CARDNAME)  

At the beginning of your upkeep, choose one of the cards imprinted on CARDNAME. You may copy that card and play the copy without paying its mana cost.  

HS 3/28 Team completely agrees. Del, can you please template the card so that it matches the above.


And thus was born [Panoptic Mirror](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Panoptic+Mirror), a splashy and powerful card indeed:




![Panoptic Mirror](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Panoptic+Mirror)


While it doesn't exactly capture the way the original Autospell worked, the essence is there; in fact, the ability to put more than one spell on it over time actually gives you more flexibility than Autospell did.


The very literate among you know that “panoptic” means “including everything visible in one view.” The flavor buffs out there should catch the reference to Panopticon, the name of Memnarch’s tower in the *Darksteel* story and the subject of the art on the [Darksteel Citadel](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darksteel+Citadel) card. If you are neither literate nor well versed in **Magic** lore, you should at least appreciate how shiny the card looks. Something for everyone!


### The Trick


In my experience with the Mirror in the FFL, I discovered a very cool trick. The key to the trick is that the Mirror’s triggered ability still goes on the stack even when there is no card imprinted on the Mirror. So you can drop the Mirror on turn five, its ability will go on the stack at the beginning of your next upkeep, and you are free to respond by activating the first ability and imprinting a card that will be copied immediately.


If you play right, your opponent can never 2-for-1 you with an artifact destruction card before you get at least one copy of your spell off. Assume that you activate an empty Mirror in response to it firing during your upkeep. In response to that, your opponent destroys it. You can choose to imprint nothing. Yes, you've wasted some mana, but at least you keep your Wrath or your [Time Walk](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk) or whatever in your hand. Many of the powerful imprint cards sacrifice card advantage in the short run with the promise of making it up later, and the Mirror is no exception. But if you play smart, you'll never end up down a card.


### Poll Position


One of the most popular features of Randy’s column was the weekly poll. I’ll be continuing that tradition.


### Last Week's Poll




| **What is your favorite color?** |
| --- |
| Black | 4834 | 31.4% |
| Blue | 3640 | 23.6% |
| Green | 2839 | 18.4% |
| White | 2061 | 13.4% |
| Red | 2024 | 13.1% |
| **Total** | **15398** | **100.0%** |

Is black's support due to the power of suggestion, or is it really the favorite? Personally, I believe that new players (which may be in the majority across all demographics) gravitate to red and green, but as you play for a while, the subtleties of black and blue become more appealing. As our web audience has a few years of gaming under their belts on average, it makes sense that black comes out ahead.


*Aaron may be reached at latestdevelopments@wizards.com.*









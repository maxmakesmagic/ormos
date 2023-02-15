
---
[Link to Wayback Machine](https://web.archive.org/web/20210429042502/https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "Erik Lauer recently gave me some wonderful advice about working on sets that get added to existing environments as opposed to being drafted on their own. As always, he said, I should try to make the set as good as possible for itself, but he suggested that I spend some time thinking about my least favorite parts of the previous environment. Every Magic developer was once a"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "643691"
[_metadata_:publish_date]:- "2011-02-04"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "A Better, Creepier World"
[_metadata_:wayback_capture_timestamp]:- "2021-04-29 04:25:02"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20210429042502id_/https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04"
---


A Better, Creepier World
========================



 Posted in **Latest Developments**
 on February 4, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






Erik Lauer recently gave me some wonderful advice about working on sets that get added to existing environments as opposed to being drafted on their own. As always, he said, I should try to make the set as good as possible for itself, but he suggested that I spend some time thinking about my least favorite parts of the previous environment. Every **Magic** developer was once a person who played tons of **Magic**. The things that I'm tired of after developing a large set are probably the same things that will annoy the most dedicated players by the time they've played with that set for three months. Doing things that solve my least favorite aspects about the big set preceding a small set will make those players happy.


He then blew my mind by telling me that this was the process he used while figuring out what to do with *Mirrodin Besieged*. I was on his development team, and yet I had no idea that this was going on inside his brain. In hindsight, though, it makes perfect sense, and I've put it into my bag of tricks for future development. It also explained the motivation behind several things that Erik did during *Mirrodin Besieged* development that I didn't understand at the time.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld128_hero.jpg)  
Before we begin, I should be clear that today's article is no slight against the *Scars of Mirrodin* development team. Mike Turian (who, by the way, has actually led the development of five **Magic** sets—I forgot *Worldwake* when [I introduced him](http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/126) two weeks ago!) is a metaphorical giant, and without standing on the collective shoulders of him and the rest of his development team, we would not have been able to create what we did in *Mirrodin Besieged*. Also, the *Mirrodin Besieged* team had much more time to develop hindsight on what we liked and didn't like about *Scars of Mirrodin*, and we would be doing a disservice to *Scars* if we didn't try to make playing with both sets together as much fun as possible.


With that in mind, let's talk about how *Mirrodin Besieged* changes things.


### The Rare Bombs Don't All Kill Things


[Sunblast Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunblast+Angel), [Hoard-Smelter Dragon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hoard-Smelter+Dragon), [Steel Hellkite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steel+Hellkite), and [Carnifex Demon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carnifex+Demon) are all *Scars of Mirrodin* rares that kill other creatures. [Contagion Engine](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Contagion+Engine), although not a creature, effectively kills all of your opponent's stuff in a few turns and many players consider it to be the strongest Limited rare in the set. I don't regret any of these as individual cards. [Sunblast Angel](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sunblast+Angel) has showed up in Extended, I have seen [Steel Hellkite](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steel+Hellkite)s cast off of Mishra's Workshop in Vintage, [Contagion Engine](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Contagion+Engine) is very popular in the **Magic Online** casual rooms, and the other two cards missing a little bit is fine when the hit rate on all of them together is so high. However, I do regret that collectively they make for a ton of rare bomb permanents that kill all your stuff in Sealed Deck and Draft.


In *Mirrodin Besieged*, we tried to avoid making the strongest Limited cards things that killed all your opponent's stuff with upside. I won't pretend that we didn't make any cards like that, but we carefully considered what kind of effects to do before we did. In the end, the cards in *Mirrodin Besieged* that do this are [Phyrexian Rebirth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Rebirth), which at least kills all but one of your own creatures, and [Massacre Wurm](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Massacre+Wurm), which only kills smaller creatures and shows up less often due to being mythic rare. [Black Sun's Zenith](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Sun%27s+Zenith) also exists, of course, but it doesn't leave your creatures unscathed.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld128_4cards1.jpg)  
This is not to say that there are no sweet rare creatures in the set, because there are. We just made sure that you have a little more time to kill these guys than the ones in *Scars of Mirrodin* before they wreck you completely.


### The Limited Format Slowed Down


One of the things that continually blows me away about **Magic** players is how smart they are. For example, at the *Mirrodin Besieged* Prerelease near my house, players spent much of the time talking about the environment discussing how much slower everything was going to be.


I was impressed to hear them identify this on their first day of playing with the set, as it's one of the more important things that we tried to do with the set. *Mirrodin Besieged* slows the format down. Both metalcraft and infect can result in decks that have the potential for massively powerful draws that put a game away very quickly. Those decks are exciting to build, but can be oppressive to play against, and we built the set so that the oppressively quick draws happen less often. While it's not exactly true that we made everything cost more mana, the distribution of cards is different. Your two-mana green creature in *Mirrodin Besieged*, rather than being [Carapace Forger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger), is now [Viridian Emissary](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Viridian+Emissary), which pushes games toward higher-mana cards instead of toward quick metalcraft-powered wins.


There's also something subtler at work. In *Scars of Mirrodin*, there are three packs full of two-mana mana Myr. *Mirrodin Besieged* replaces one of those packs with a pack that has no mana acceleration at common, and only two two-mana uncommons that accelerate your mana.




|  |  |
| --- | --- |
| Plague Myr | Sphere of the Suns |

Overall, games are going to take longer now, so you'll have some more time to get creative. I'm curious to see what you all will do with it.


### Limited Infect Decks Are Slower


This subcategory was one of my pet issues. My favorite kind of aggressive deck in **Magic** is the kind that can put on early pressure but has things it can do deep into the late game. Playing infect in *Scars of Mirrodin*, though, often felt to me like the more simple-minded blitz aggressive decks that I don't enjoy playing. There was such a mass of cheap creatures, and so few big bodies to follow them up with, that I felt obligated to go for an early assault that left me without much to do if it didn't work.


There's no reason, of course, for that to be true forever. Let's compare, then, the two-mana infect creatures from *Scars of Mirrodin* ...


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld128_4cards2.jpg)  
... with the ones from *Mirrodin Besieged*:




|  |  |
| --- | --- |
| Plague Myr | Flensermite |

The mass infect creatures in *Mirrodin Besieged* starts at three mana, not two, and they're much sturdier overall. [Priests of Norn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Priests+of+Norn) is literally sturdy with four toughness. [Rot Wolf](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rot+Wolf) is metaphorically sturdy, as it replaces itself with another card when it dies to keep your infect deck gassed up with cards. [Tine Shrike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tine+Shrike), [Blightwidow](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightwidow), and [Scourge Servant](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Scourge+Servant) are all common four-mana infect creatures that are either sizable or evasive. There's also more finishing power at lower rarities in *Mirrodin Besieged*, with [Flesh-Eater Imp](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flesh-Eater+Imp) and [Phyrexian Juggernaut](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Juggernaut) both easily able to crash through and put a game away.


![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld128_2Cards1.jpg)  
The net effect of all this is that infect decks will play a little differently. They'll be a bit slower, but significantly steadier. If you like drafting infect, look forward to some more staying power. If your opponents like drafting infect, you won't get out of the woods so quickly anymore.


### Infect Can Be a Normal Constructed Deck


One of the side effects of the focus on cheaper infect creatures in *Scars of Mirrodin* was that Constructed infect decks leaned toward being fast blitz decks without much ability to craft a late game. Erik likes his Constructed decks to have a little more staying power than that, and he knows that many strong competitive **Magic** players feel the same way. I agree with him. Even if a blitz infect deck is one of the strongest decks in a format, I would still not be likely to play it unless I absolutely had to.


Once again, there's no reason that this needs to be true forever. Although green is a perfect match for a blitz infect deck due to its mass of powerful [Giant Growth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) effects in Standard right now, that doesn't mean that black's infect deck can't be a little different.




|  |  |
| --- | --- |
| Phyrexian Vatmother | Phyrexian Crusader |

[Phyrexian Vatmother](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Vatmother) and [Phyrexian Crusader](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Crusader) are a little different than the *Scars of Mirrodin* rare infect creatures. They aren't worried about going directly to the opponent's face with poison counters, because they're resilient. Red and white removal spells can't touch [Phyrexian Crusader](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Crusader), and its first strike ability means that it's tough to kill in combat. [Phyrexian Vatmother](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Vatmother)'s 5 toughness is a huge deal, and not even Thrun can stand in its way.


![Inkmoth Nexus](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Inkmoth+Nexus)  
There are also the subtler support cards. [Plague Myr](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Myr) and [Inkmoth Nexus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkmoth+Nexus) are the sort of cards that you don't put on the movie poster, but do tons of work to get things going. [Plague Myr](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plague+Myr) can accelerate you into [Phyrexian Vatmother](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Vatmother)s and [Skithiryx, the Blight Dragon](http://gatherer.wizards.com/Pages/Card/Details.aspx?&name=Skithiryx%252C%2Bthe%2BBlight%2BDragon)es earlier than expected. [Inkmoth Nexus](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Inkmoth+Nexus) keeps the poison coming even after your actual creatures get stopped. Both of them are happy to be part of your mana base, then come crawling out to join the assault once they are no longer casting spells.


We have data that demonstrates infect's sizable popularity with just *Scars of Mirrodin*, but we also saw several people grousing about it. I sympathize with those who didn't love infect decks before *Mirrodin Besieged*, but these cards gave me an infect deck I could love. If you're like me, you might want to give it a try.


[![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/features/MBS_Launch_ArticleBaner.jpg)](http://www.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/release-facts)  
This weekend, *Mirrodin Besieged*
[Launch Parties](http://www.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/release-facts) will take place all across the country. That means that today is your first chance to buy cards, and that this weekend is your first chance to experience the full *Scars*-*Besieged* Limited format as we envisioned it. Things have changed, and as you can tell from this article, I think they've changed for the better.


### Last Week's Poll




|  |
| --- |
|  **Are you attending a Prerelease?**  |
| Yes, a large regional Pererelease. | 650 | 9.8% |
| Yes, a store Prerelease. | 4274 | 64.1% |
| Yes, one of each kind. | 170 | 2.6% |
| No. | 1571 | 23.6% |
| **Total** | **6665** | **100.0%** |

  
  
  








---
[Link to Wayback Machine](https://web.archive.org/web/20211025141850/https://magic.wizards.com/en/articles/archive/latest-developments/plays-thing-2011-10-06)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "From an internal perspective, the Innistrad preview season was a fascinating exercise in restraint. Magic players are full of opinions, and every time a new card is revealed, players share their opinions enthusiastically. A few of the things people said were interesting. Some seemed accurate. More did not. Most were fascinating. All, however, were uninformed.Prey Upon | Art by"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "193206"
[_metadata_:path_date]:- "2011-10-06"
[_metadata_:publish_date]:- "2011-10-07"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Play's the Thing"
[_metadata_:wayback_capture_timestamp]:- "2021-10-25 14:18:50"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211025141850id_/https://magic.wizards.com/en/articles/archive/latest-developments/plays-thing-2011-10-06"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/plays-thing-2011-10-06"
---


The Play's the Thing
====================



 Posted in **Latest Developments**
 on October 7, 2011 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






From an internal perspective, the *Innistrad* preview season was a fascinating exercise in restraint. **Magic** players are full of opinions, and every time a new card is revealed, players share their opinions enthusiastically. A few of the things people said were interesting. Some seemed accurate. More did not. Most were fascinating. All, however, were uninformed.

![](https://media.wizards.com/images/magic/daily/ld/ld163_preyUpon.jpg)[Prey Upon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prey+Upon) | Art by [Dave Kendall](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Dave+Kendall%22%5D)

In particular, people said all kinds of things about the Werewolves that I thought were wrong. Here is a sample:


> * The Werewolves will never transform.
> * The Werewolves will transform way too easily.
> * The Werewolves will make the format really fast.
> * Taking a turn off to transform a Werewolf will get you killed.
> * The Werewolves need more text to be interesting to play with.
> 

This frustrated me, because I knew that none of those commenters had played a single game with the cards.

</magic/flipcards/flipcard.html?ca=iuseybvnjtdhyfagshdsvamp;cb=utbnfm6x3y47nmgvha7ui3amp;lang=en></magic/flipcards/flipcard.html?ca=uiywrtgbenrmouviwyuejramp;cb=wvoeijhfr4bcnuaferdfgamp;lang=en>  
Here in Ramp;D, we're professional game designers who make **Magic** all the time. Before we played lots of games of **Magic** with double-faced cards, we didn't have a clue what they would be like either. If we didn't know before that, there's no way that the average **Magic** forum poster knew.

Let me pause for a moment and ask you a question. You're reading the development column on the official **Magic** website, so you probably spend a lot of time thinking about **Magic**, reading about **Magic**, talking about **Magic**, interacting with **Magic** cards, and actually playing **Magic**. If I were to pick a random time that you were doing one of those things, what is the probability that I picked a time that you were actually playing **Magic** as opposed to just interacting with or thinking about cards?

![](https://media.wizards.com/images/magic/daily/ld/ld163_thinkTwice.jpg)  
If you're a typical **Magic** player, it's not likely to be that high, and I say that from experience. While I was in college, I played a lot of **Magic**. During Pro Tour Qualifier seasons, I usually went to one Qualifier a weekend, and sometimes two if that was feasible. If that wasn't happening, it was usually because I had a Grand Prix instead. I also spent plenty of time practicing both on **Magic Online** and in person. Despite that, I'm still sure I spent much more time thinking about decklists, talking about **Magic** on the phone and on long drives, reading **Magic** articles, trading, building physical decks, and organizing cards than I did actually playing games. This seems unavoidable to me, as our brains constantly think about things we find interesting (and it takes some doing to keep a **Magic** collection in a state other than giant mess). It seems easy to conclude, then, that when measured by time, the average use case for a **Magic** card does not involve actually playing **Magic**.

This is an interesting realization, as we design and develop **Magic** cards to be maximally fun while being used to play games of **Magic**. When I put it that way, it sounds like there's something kind of insane going on. How many products are optimized for something other than their most common use case, let alone a particular fairly rare one?

That, however, is what we do here. We all love playing **Magic**, and we want to make sets that are as much fun for us and everyone else to play as we can make them.

This can sometimes cause some uncomfortable tension. Have a look at the card [Silent Departure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Departure).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Silent+Departure)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Departure)  
When this card was revealed, forum posters had some complaints. They were used to playing with [Unsummon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon), which does all kinds of cool tricks because it is an instant, but [Silent Departure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Departure) is a sorcery. They also thought that the flashback cost was way too high—who pays five mana for an [Unsummon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon) effect, especially at sorcery speed?

If we were maximizing the card's value for the first time when someone read it, we might have printed this card instead:

![](https://media.wizards.com/images/magic/daily/ld/ld163_TA.jpg)  
However, that's not what we're doing. We want **Magic** to be as fun to play as possible. This card is a sorcery because we have found that strongly board-affecting instants with flashback hiding in the graveyard are likely to cause feel-bad moments from forgotten cards. **Magic** has enough to remember without asking players to keep track of many things in the graveyard at all times, so we made as many of the flashback cards as we could into sorceries instead.

This card costs five mana the second time around because flashback is such a strong ability. Most players undervalue the ability to get a second use out of a spell. The fundamental resource of **Magic** is the card, and putting flashback on an instant or sorcery is a lot like writing "Draw an expensive version of this card" as a rider. It may be an expensive version of the card, but a card is still a card, and in a slower format like *Innistrad* that bonus card, even at a high cost, will often make a difference.

While Taciturn Abandonment is a stronger and more appealing individual card than [Silent Departure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Departure), we think that *Innistrad* is more fun with [Silent Departure](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Silent+Departure) than it would have been with Taciturn Abandonment.

Now, I'll ask you a different question. During which **Magic**-related activities do you learn the most about **Magic**? I bet it's not sorting cards or physically building decks. I also suspect it's not reading **Magic** articles or watching videos. No, I think the fastest way to learn about **Magic** is to play **Magic**. When you see the cards in action, you'll have leaps of insight that you could never have had while looking at a card in a vacuum.

I feel comfortable saying that because it happens to us inside **Magic** Ramp;D as well. We're all intelligent people, so we like to debate anything and everything that can have even a small amount of rigor applied to it. While the "Another Day of Ramp;D Productivity Lost" series in Mark Rosewater's "[Tales from the Pit](http://markrosewater.tumblr.com/tagged/Tales_from_the_Pit)" comic are all exaggerations, they are not gross exaggerations. We enjoy talking about goofy things, like who is the protagonist of *Jurassic Park*, whether dogs should be mechanically represented with loyalty counters, and what the correct average strength of a double-faced card in Limited is. Most of these arguments are frivolous, but some of them could be resolved if we just stopped talking and ran an experiment or two. Just like internet forum posters, though, we like talking a little too much, so I don't expect this pattern to change.

[![](https://media.wizards.com/images/magic/daily/ld/ld163_comic.jpg)](http://markrosewater.tumblr.com/tagged/Tales_from_the_Pit)  
**Magic** is hard, though, and we all know we aren't good enough to figure everything out inside our own heads. Just like you, we have to play games of **Magic**, and lots of them, to figure out the answers to questions. Our questions can be even more challenging than the questions you have to answer. Sometimes Design will create a mechanic that's a little out there, like the mechanic on the *Innistrad* Werewolves, and we'll start to argue about whether that mechanic is fun or not. The argument won't go anywhere, though, and we'll have to play games to find out.

Sometimes the argument is about a small tweak to a set's structure, which is even more difficult to resolve without playing games. For example, early in *Innistrad* development, Ken Nagle brought up how much fun he had with *Time Spiral*'s off-color flashback spells like [Mystical Teachings](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystical+Teachings) and [Momentary Blink](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Momentary+Blink), and suggested that we run the same gag. I loved that idea, and further suggested that we add some five-color mana fixing to allow people to "splash" flashback costs. Ken and I were excited about this, but there was another team member who wasn't, and who felt that this would distract people away from the set's focus and be tough to process. I thought that was a fair concern, but enough of us liked it that we tried putting it in the file anyway. After the first playtest, that team member immediately changed his mind, and those flashback cards made it to print.



|  |  |
| --- | --- |
|  |  |

Other times, someone will find a strong Constructed deck, claim that it's broken, and ask for a card to be changed. If we like the card, we might not want to believe them, and everything degenerates into another argument. The simplest way to resolve this? Grab a few other decks and run some games. After that, we'll know if something is too good, and as a kicker we'll have a better idea of what to change to fix it. This sometimes results in the original claimant being annoyed because he turns out to be wrong, but we know that is bound to happen sometimes.

</magic/flipcards/flipcard.html?ca=kjgbifnkbsuherygjhjamp;cb=uryatyturnjmvwoilekuyrjkmamp;lang=en></magic/flipcards/flipcard.html?ca=opisuyefn78iovatvertdyfghfdsafamp;cb=uasgencimovqlyuhwerbjvmy7useramp;lang=en>  
The Werewolves as a group are a perfect example of this kind of subject. [Steve Sadin's article](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/li/163) this week is the first time I've seen anyone start digging into the Werewolf-induced complexity that's hidden in *Innistrad*. The structure of **Magic** rewards you for using your mana efficiently, so most **Magic** players default to casting spells whenever they can. However, previous sets have not had an entire category of cards that worry about the number of spells played in a turn. As Steve points out, sometimes a card like [Traveler's Amulet](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Traveler%27s+Amulet) or [Blazing Torch](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blazing+Torch) that's held long past turn one can be the difference between an opposing [Krallenhorde Wantons](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krallenhorde+Wantons) smashing past your blockers and the same [Grizzled Outcasts](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzled+Outcasts) sitting back on defense. Steve also mentions the value of drafting and sideboarding in cheap cards that your deck might not otherwise need in order to assist you in messing with Werewolf transformations. For example, I don't normally play [Traveler's Amulet](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Traveler%27s+Amulet) in two-color decks, but against a deck with seven Werewolves I would happily board it in.



|  |  |
| --- | --- |
|  |  |

This stuff is all real. It's also only the beginning of what there is to learn about Werewolves, as we kept learning more things all the way up to the very last *Innistrad* playtest draft we did. It's also not something I saw anyone talk about during the preview season. And how could you have? No one was playing games yet.

We're going to keep making things as complex as the Werewolves. Like it or not, the only way you're going to figure them out is to play a lot of games. If you really want to know what's going on, get off the forums, go to your local store or get on **Magic Online**, and start playing.

I promise I won't be insulted. That's what we made the cards for anyway.

![](https://media.wizards.com/images/magic/daily/ld/ld163_moonmist.jpg)[Moonmist](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moonmist) | Art by [Ryan Yee](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Ryan+Yee%22%5D)

  


---

  
Last Week's Poll


|  |
| --- |
|  **How did you handle double-faced cards at the *Innistrad* Prerelease?**  |
| I played my double-faced cards in sleeves in my deck. | 445 | 45.5% |
| I didn't play in an *Innistrad* Prerelease event. | 225 | 23.0% |
| I played in sleeves with checklists. | 149 | 15.2% |
| I played unsleeved with checklists. | 121 | 12.4% |
| I didn't play any double-faced cards at the Prerelease. | 39 | 4.0% |
| **Total** | **979** | **100.0%** |

  
This Week's Poll
**Which of **Magic** Werewolf is your favorite?**[Greater Werewolf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Werewolf)[Lesser Werewolf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lesser+Werewolf)[Treacherous Werewolf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Treacherous+Werewolf)[Daybreak Ranger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Daybreak+Ranger) / [Nightfall Predator](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightfall+Predator)[Gatstaf Shepherd](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gatstaf+Shepherd) / [Gatstaf Howler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gatstaf+Howler)[Grizzled Outcasts](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzled+Outcasts) / [Krallenhorde Wantons](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krallenhorde+Wantons)[Hanweir Watchkeep](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hanweir+Watchkeep) / [Bane of Hanweir](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bane+of+Hanweir)[Instigator Gang](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Instigator+Gang) / [Wildblood Pack](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wildblood+Pack)[Kruin Outlaw](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kruin+Outlaw) / [Terror of Kruin Pass](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Terror+of+Kruin+Pass)[Mayor of Avabruck](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mayor+of+Avabruck) / [Howlpack Alpha](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howlpack+Alpha)[Reckless Waif](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reckless+Waif) / [Merciless Predator](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merciless+Predator)[Tormented Pariah](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tormented+Pariah) / [Rampaging Werewolf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rampaging+Werewolf)[Ulvenwald Mystics](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulvenwald+Mystics) / [Ulvenwald Primordials](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulvenwald+Primordials)[Village Ironsmith](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Village+Ironsmith) / [Ironfang](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ironfang)[Villagers of Estwald](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Villagers+of+Estwald) / [Howlpack of Estwald](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howlpack+of+Estwald)  


---

  
![](https://media.wizards.com/legacy//mtg/images/daily/features/banners/isd_articlefooterbanner_league_top.jpg)![](https://web.archive.org/web/20130923050335im_/http://www.wizards.com/mtg/images/daily/features/banners/ISD_ArticleFooterBanner_League_leftOfButton.jpg)[![](https://web.archive.org/web/20130923050331im_/http://www.wizards.com/mtg/images/daily/features/banners/ISD_ArticleFooterBanner_League_Button01_Static.jpg)](http://archive.wizards.com/Magic/TCG/Events.aspx?x=mtgcom/events/league-facts)






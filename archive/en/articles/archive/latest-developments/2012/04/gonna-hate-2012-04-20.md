
---
[Link to Wayback Machine](https://web.archive.org/web/20170214205303/http://magic.wizards.com/en/articles/archive/latest-developments/gonna-hate-2012-04-20)

[_metadata_:author]:- "Zac Hill"
[_metadata_:description]:- "I'm in a love/hate relationship with hate. There's not a lot to love. It's ugly. It's blunt. It (usually) means we made a mistake. But it solves problems. It smooths edges. It re-corrects. A well-positioned hate card can bring entire environments back into equilibrium. On the other hand, a poorly placed hate card creates more problems than it solves, and by its very presence imbalances an environment in unanticipated, dangerous ways."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "644911"
[_metadata_:publish_date]:- "2012-04-20"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Gonna Hate"
[_metadata_:wayback_capture_timestamp]:- "2017-02-14 20:53:03"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20170214205303id_/http://magic.wizards.com/en/articles/archive/latest-developments/gonna-hate-2012-04-20"
[_metadata_:wayback_url]:- "http://magic.wizards.com/en/articles/archive/latest-developments/gonna-hate-2012-04-20"
---


Gonna Hate
==========



 Posted in **Latest Developments**
 on April 20, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_zachill.jpg)
By Zac Hill




Zac is a former game designer/developer for Wizards of the Coast and was the lead developer for Dragon's Maze. His articles have appeared in The Huffington Post, The Believer, and on StarCityGames.com. Currently he serves as the chief operating officer of The Future Project, a nonprofit education initiative, and holds a position as a research affiliate in the MIT Game Lab. 






I'm in a love/hate relationship with hate. There's not a lot to love. It's ugly. It's blunt. It (usually) means we made a mistake. But it solves problems. It smooths edges. It re-corrects. A well-positioned hate card can bring entire environments back into equilibrium. On the other hand, a poorly placed hate card creates more problems than it solves, and by its very presence imbalances an environment in unanticipated, dangerous ways.

If you're a hater—well, at least if you're the kind of person who plays hate cards—today's gem is for you:

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/tcg/products/avr/h4ojgjs6dn_en.jpg)  
### o\_O

Alright. So this card fixes the mana in your creature decks and ensures that basically anything you cast can resolve if you want it to. We expect it to define almost every format in which it can be played. But this card is part of a bigger picture, as I'm sure you can tell. Specifically, there's one big question I'm sure is on your mind: Why does it have that last ability?

Well, I'm glad you asked!

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld191_snapcard.jpg)  
I'll be real with you. We messed up with [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage).

I'm not going to sit here and look you in the eye and tell you that [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage) is a fair **Magic** card. Nor am I going to blame any of my colleagues for the problem: I worked with Tiago Chan to design it, and by the time we realized exactly how powerful it was in concert with the abundance of one-mana cantrips in Standard, the card was already out the door. We knew it was something we were going to have to attack in order to keep Standard in check. The challenge was deciding how best to do that.

Now, before I dive into that process a little further, I want to spend a little bit of time talking about how we engineer cards that try to help put some reins on the environment. There are a couple of different kinds of hate cards. Some—like [Grafdigger's Cage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grafdigger%27s+Cage), [which I explored in detail here](/en/articles/archive/latest-developments/cage-match-2012-01-27)—are powerful, narrow, pinpoint answers to a specific card or subset of strategies. If something gets out of control, cards like Cage can come out of the arsenal to blast them powerfully and re-align the metagame. Other cards, though, are a little more subtle. They're main deckable. They're versatile. They have broader uses beyond straightforward, directed hate. I'd classify something like [Obstinate Baloth](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Obstinate+Baloth) in this camp—you can main deck it, you don't mind playing it against everything, but its utility grows exponentially when someone is (for example) casting [Blightning](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightning) against you.



|  |  |
| --- | --- |
| Grafdigger's Cage | Obstinate Baloth |

Each one of these card types has its advantages and disadvantages. With the first kind of card, it's a lot more likely that it'll actually accomplish the task it was intended to accomplish. That's because we can tailor exactly the effect we want, since versatility isn't an issue; we aggressively *don't* want the card to see play outside the context of what it's hating out, so we don't have to worry about that too much. The downside is that sometimes what it's hating out isn't actually a problem, so you waste a bunch of real estate and elegance creating a card that looks kind of dumb. The second kind of card avoids that problem to some degree, since it has some broader utility outside of its specific environmental purpose. Moreover, because these kinds of cards tend to go into main decks, they actually are *more* effective at sculpting a metagame when they work, since they're relevant in a greater percentage of games. The downside is that because they have to be more generally applicable, they can't serve their one specific purpose nearly as narrowly, so their consequences tend to be more far-reaching than we anticipate.

It's a balancing act.

### I Just Want Some Resolution

Alright. So we're getting tired of Snapcaster decks, and Snapcaster-enabled archetypes like UB Control and WU [Moorland Haunt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moorland+Haunt). But how does this card even address that problem? This card doesn't say anything about flashback whatsoever!

One of the challenges in attacking a card like [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage) is that it's card advantage, so you have to figure out a way to either net comparable advantage when you fight it or otherwise incur zero opportunity cost. If you don't, you might succeed at overcoming the problem, but you're going to ultimately create *more* problems for yourself than you solve. A card like [Grafdigger's Cage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grafdigger%27s+Cage), for example, *loudly hoses* [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage), but at the cost of being down a card. Therefore, if I'm the Snapcaster player, I'm still relatively happy when you cast it. You don't let me flash my cards back, but my Snapcaster has effectively made you mulligan before it's even on the battlefield.

Another difficulty when attacking this kind of card is how versatile it is by its very nature. If I'm trying to hose something like, say, Yawgmoth's Bargain—a card that's obviously a lot more bananas than [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage)—I know how I'm supposed to do that, because it only does one specific thing. With Snapcaster, you're just getting value along an axis. You might be [Unsummon](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unsummon)ing twice, or cantripping, or countering a spell, or flashing back [Dismember](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismember), or whatever. It's much more difficult to pinpoint your strategy.

What we had to do in order to attack the issue, then, was sit down and map out everything that Snapcaster was doing. What we came to realize very quickly was that [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) was almost as savage a culprit as good ol' Tiago himself.

![Mana Leak](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mana+Leak)  
One of the problems is that [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) is simply a much more powerful card than we would be comfortable printing under modern development rules. Similar to why the Swords are so powerful—their costs were locked in before people really understood how to price Equipment—[Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) is a relic of a bygone era.

Now, I get into arguments whenever I make a claim like this, because it's difficult to see. I can't tell you how many times I have been in a conversation of the following form:

"You guys are power creeping *so hard*."

"Hmm. I don't think we are. After all, there are all kinds of spells that we would never print nowadays that ran rampant in old environments, such as [Compulsive Research](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsive+Research), [Force Spike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+Spike), [Remand](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remand), '[Signets](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&name=+%5bSignet%5d),' etc."

"Well, sure, but creatures are getting a lot better, so it's a balance."

That argument makes sense on the surface, because it's true: we make creatures a lot better than we used to. But the reality (beyond the fact that you can prove mathematically that creatures were too weak for most of **Magic's** history, based on the number of turns it takes to resolve an average "goldfish" game state) is simply that *spells are much more inherently powerful than creatures*. Spells have haste, whereas creatures have "Suspend 1." Spells can only be interacted with for the moment they are on the stack, whereas creatures can be interacted with at sorcery speed. So you have to work a lot harder to make creatures relevant than you have to work to make spells relevant.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld191_gei.jpg)[Geist of Saint Traft](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft) | Art by [Igor Kieryluk](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Igor+Kieryluk%22%5D)

Anyway, the point of all that is that [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) turns out to be a huge portion of the power of [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage), as well as of a card like [Delver of Secrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Delver+of+Secrets) or [Geist of Saint Traft](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft). The reason is that those cards render it very easy to *achieve* "initiative"—a position in the game state that requires the opponent to take action—and [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) renders initiative very easy to *maintain*. If I cast [Geist of Saint Traft](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft) on the third turn, [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) forces you to deploy a threat onto the battlefield before I untap. When you do, though, all I need is something like a [Vapor Snag](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vapor+Snag) or a [Dismember](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dismember)—or even a two-mana mechanism of granting evasion, like [Spectral Flight](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spectral+Flight)—and suddenly it's just impossible to get back into that game.



|  |  |
| --- | --- |
| Geist of Saint Traft | </sites/all/modules/custom/wiz_legacy_migration/flipcard/flipcard.html?ca=jhfghionlmfhtytghdf777&cb=jcdbfuyugtehvursertrere&lang=en> |

It's tempting to blame the threats in this situation. But whether the card gaining initiative is [Delver of Secrets](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Delver+of+Secrets), [Geist of Saint Traft](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+of+Saint+Traft), [Midnight Haunting](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Midnight+Haunting), or [Moorland Haunt](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moorland+Haunt), or the threat of [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage) into a piece of Equipment like [Sword of War and Peace](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sword+of+War+and+Peace) or [Runechanter's Pike](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runechanter%27s+Pike), the common thread is the presence of [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) rendering it impossible to get ahead by casting a powerful, expensive spell. That spell is unlikely to resolve, and by tapping out to commit a threat to the table you're asking to get punished by any number of problematic cards.

To get back to the original point, though, one of the traditional ways of dealing with countermagic like [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) is to cast "test spells"—spells you don't care that much about resolving, but which your opponent nevertheless has to counter. Normally, the coast is clear once your opponent has "burned" a piece of countermagic. [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage), though, ensures that once your opponent has cast a single [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak), it's actually *more* likely for your next spell to get countered than your first one, because in addition to the three remaining [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak)s, there are four more [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage)s capable of "turning on" that [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) in the 'yard.

I can't tell you how many FFL matches were spent [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak)ing a spell, killing the next threat, and just sitting on [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) + [Snapcaster Mage](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Snapcaster+Mage) forever while casting flashback cards and activating nonbasic lands.

So we decided to nip that problem in the bud.

### I've got Soul; I'll name "Soldier"

One of the mistakes we made in *Rise of the Eldrazi* was not giving enough love to the themes that had been introduced in *Zendikar* and *Worldwake*. The departure was too stark. So we knew that *Avacyn Restored* should help out the tribal themes explored in *Innistrad* block in some way.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld191_kes.jpg)[Kessig Wolf Run](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kessig+Wolf+Run) | Art by [Eytan Zana](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Eytan+Zana%22%5D)

One of the things we found was that many of the tribal decks wanted to be aggressive, but the mana base was actually a bit of a pain to construct. The Werewolf deck, for example, could conceivably cast both [Wolfbitten Captive](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wolfbitten+Captive) and [Reckless Waif](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reckless+Waif) on the first turn, but had only a single Standard-legal dual land to help it out. Meanwhile, you've also got a deck like Zombies that really wants to cast [Geralf's Messenger](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geralf%27s+Messenger) but doesn't want to totally ignore all of its blue creatures in the process. We therefore decided we should make a land that could help these decks out. The land let you name a creature type, then tapped for either a colorless mana or a mana of any color that could be used to cast creatures of that type.

![Kessig Wolf Run](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kessig+Wolf+Run)  
We realized, though, that to solve our [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) problem we really wanted to print something like [Boseiju, Who Shelters All](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boseiju%2C+Who+Shelters+All)—some kind of land that everyone could play that would incidentally blow some hate in [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak)'s direction. So we decided to add "[Boseiju](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boseiju)" text to the card that became Cavern of Souls.

This radically changed the functionality of the card. It still met its "tribal" needs but now served as a kind of "insurance policy" in decks playing as few as four creatures, and as many as thirty. It also rewarded you for carefully constructing the sequence in which you played your threats. Some of the more popular creature types to name with Cavern of Souls in testing included:


> 
> * Human
> * Elf
> * Spirit
> * Zombie
> * Illusion
> * Shapeshifter
> * Troll (awkward every single time)
> * Wolf (hmm)
> * Dragon (!)
> * Giant
> * Sphinx
> * Praetor
> 

As you can imagine, the card led to a wild upsurge in the number of midrange and expensive creatures that were no longer embarrassing to play.

### Creature – Elephant-In-Room

There was one enormous consequence of printing this card, though, that could not be ignored: [Mana Leak](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Leak) was one of the forces keeping the Titans in check. Cavern of Souls is at its scariest inside some kind of [Primeval Titan](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Primeval+Titan) shell, since it's just so easy to kill an opponent after resolving that card.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld191_td5bk59e7u.jpg)Cavern of Souls | Art by [Cliff Childs](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5B%22Cliff+Childs%22%5D)

To be sure, the Titans demand a deliberate plan of attack in a world where they might not always get hit with a Leak or a [Dissipate](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dissipate). You can't just sit and ignore them. Personally, I've had a fair amount of success with cards like [Despise](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Despise) or {WARNING: unspoiled card}, since RG Ramp decks were so dependent upon resolving a single big threat. If I wanted to be more blunt, I could gut the culprit entirely with a [Memoricide](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memoricide), which gets proportionately more powerful in an environment with larger creatures since you're much more likely to catch a copy of a relevant card in your opponent's hand. We definitely played our fair share of [Unburial Rites](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unburial+Rites)-into-[Elesh Norn](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elesh+Norn%2C+Grand+Cenobite)/Griselbrand decks, and it's a pretty big beating to have all your fatty-boom-boom threats exiled forever after you've spent a couple turns setting up.



|  |  |
| --- | --- |
| Despise | Memoricide |

Still, we know Cavern of Souls will leave its mark on every format. It hates loudly on [Force of Will](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Force+of+Will) and [Spell Snare](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spell+Snare). It forces Faerie decks to lean far more heavily on [Vendilion Clique](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vendilion+Clique) to manage threats. It helps out every Commander. It does a *lot* of things. But we firmly believe that **Magic** tends to be more fun when you're confident, for the most part, that you can resolve your spells. Furthermore, the card has costs. The more you diversify your threats, the more often you're going to have a [Blasted Landscape](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blasted+Landscape) on the battlefield. It's not the kind of card you can mindlessly jam into every deck. But it is the kind of card that solves a problem—a very real problem—and the kind of card we hope will shake up Standard in the right ways.

May your creatures travel safely through the Æther all the way onto the kitchen table.

Zac ([@zdch](https://twitter.com/#!/zdch))

  







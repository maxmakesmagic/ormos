
---
[Link to Wayback Machine](https://web.archive.org/web/20220629122553/https://magic.wizards.com/en/articles/archive/making-magic/names-bond-soulbond-2012-05-11)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "I keep saying one of these weeks I'm going to talk about the design of soulbond. Well, it turns out this week is that week. Soulbond is a complex mechanic and it had an equally complex trip from idea to print. Today's column will examine some of the many issues we had to face designing (and developing) soulbond.Not So NewBrian Tinsman, lead designer for Avacyn Restored, is a"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "194711"
[_metadata_:path_date]:- "2012-05-11"
[_metadata_:publish_date]:- "2012-05-14"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Name's Bond, Soulbond"
[_metadata_:wayback_capture_timestamp]:- "2022-06-29 12:25:53"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220629122553id_/https://magic.wizards.com/en/articles/archive/making-magic/names-bond-soulbond-2012-05-11"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/names-bond-soulbond-2012-05-11"
---


The Name's Bond, Soulbond
=========================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on May 14, 2012 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






I keep saying one of these weeks I'm going to talk about the design of soulbond. Well, it turns out *this* week is that week. Soulbond is a complex mechanic and it had an equally complex trip from idea to print. Today's column will examine some of the many issues we had to face designing (and developing) soulbond.

Not So New
[Brian Tinsman](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Brian%20Tinsman), lead designer for *Avacyn Restored*, is a man who loves embracing a challenge. Some people will back away from things that have failed, but it only seems to fuel Brian to try and figure out how to make it work. I talked [a few weeks ago](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/190) about how Brian's determination to solve draw triggers led to him designing miracles. Soulbond has a similar path.

You see, *New Phyrexia* tried to solve a design problem we've been working on forever. How do you capture the flavor of two creatures working together? In Alpha, [Richard](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Richard%20Garfield) made banding.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=235)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=235)  
While banding works very differently mechanically from soulbond, it has its roots in the same flavor. The idea of two creatures working together has popped up again and again. It's just something that has such resonant flavor that every designer wants to see if he or she can crack it. *New Phyrexia* had a pretty radical take on it that [Ken Nagle](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Kenneth%20Nagle) and his design team ([Dave Guskin](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Dave%20Guskin), Joe Huber, [Matt Place](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Matt%20Place), and myself) spent a lot of time trying to make work. In the end, things weren't clicking so we went another direction, ultimately leading to Phyrexian mana.

Even though Brian wasn't on the *New Phyrexia* team, he was fascinated by the problem it was trying to solve. I'm not sure who first came up with soulbond, called bind when it was first created, but I do know that Brian quickly became its biggest champion. The idea behind soulbond was very simple. When a creature with the mechanic entered the battlefield, it was able to pair with another creature as long as that creature wasn't already paired with anyone else. The earliest version only worked when the creature with soulbond entered the battlefield. You had to make the connection then and there.

![](https://media.wizards.com/images/magic/daily/mm/mm195_spe.jpg)[Spectral Gateguards](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spectral+Gateguards) | Art by [Wayne England](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Wayne+England%22%5D)

But the biggest question when we first made the card wasn't even about the timing of pairing things. No, the focus of early design was trying to figure out what exactly being paired did for your creature and for the creature it was paired with. The earliest designs were all over the board. For example, some soulbond creatures granted abilities to the creatures they paired with. Others got abilities when they were paired. Still others granted abilities to themselves and the creatures they paired with.

To understand the confusion, let me introduce three sample cards.


> **Soulbond Angel**  
>  2WW  
>  Creature – Angel  
>  3/3  
>  Flying  
>  Soulbond  
>  Any creature paired with CARDNAME gains flying.
> 
> **Soulbond Warrior**  
>  2G  
>  Creature – Human Warrior  
>  2/2  
>  Trample  
>  Soulbond  
>  CARDNAME gets +2/+2 when paired with another creature.
> 
> **Soulbond Fighter**  
>  2RR  
>  Creature – Human Warrior  
>  3/3  
>  If paired, CARDNAME and any creature paired with it get +1/+1 and gain first strike.
> 
> 

Let's walk through what happens if these three cards pair with one another.


> Angel + Warrior = 3/3 Flying + 4/4 Flying, trample
> 
> Warrior + Fighter = 5/5 Trample, first strike + 4/4 First strike
> 
> Angel + Warrior = 4/4 Flying, first strike + 4/4 Flying, first strike
> 
> 

Normally, when I give an example like this, I will get back people who say, "That's not hard. I figured it out easily." What they are missing is that in the middle of a **Magic** game, you are most often keeping track of many other things. Having to exert attention to figure out what something's stats are is more taxing than it might first seem.

![](https://media.wizards.com/images/magic/daily/mm/mm195_sto.jpg)[Stonewright](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stonewright) | Art by [Wesley Burt](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Wesley+Burt%22%5D)

Second, when stats require a little extra mental energy to track it makes it much easier to forget what those stats are, meaning you spend a lot of time figuring things out multiple times. **Magic** simply has too many variables to make it easy to remember a number that isn't consistently created.

Third, one of the tenets of New World Order (and really good design when you get down to it) is that when we do something, especially at common—which NWO is focused on—we like to do it one consistent way. When a mechanic works differently on each card, it means that the player has to figure things out each and every time. Having the mechanic work the same on every card allows players to learn the mechanic and then apply the meta-rule rather than having to figure out how each card works individually. This meant that while we were trying out three versions, we really had to pick one.

Quick aside—so why do we do tests with multiple different versions if we know in the end we want only one? The main reason is that it's a timesaver. Playing once with mechanic A, then another time with mechanic B, and then another time with mechanic C, takes a lot longer than just playing with all the versions in one playtest. Yes, it makes it a little harder to focus but it helps us figure out quicker which versions are working.

Extrapolate to the Party
So we had three versions of soulbond. Let's do what we did and walk through how each version played out.

**Version A (The Angel)—Soulbond creatures grant abilities to the creatures they pair with**

In this version, soulbond creatures are never enhanced unless they pair with other soulbond creatures. This way isn't too hard to track but in many ways that's its biggest weakness. This version acts a lot like creature enchantments. A *lot* like creature enchantments. The goal of making a new mechanic is to have it feel different from what the game already does. True, this version means the enhancements are removed by creature destruction rather than enchantment destruction, but the overall feel is pretty close.

**Version B (The Warrior)—Soulbond creatures grant abilities to themselves when paired**

This version was harder to track but had a much bigger problem. Soulbond was supposed to represent the joining of the good guys to bring down the bad guys. Getting a bonus only for yourself flies in the face of this flavor. It feels selfish, not selfless.

![](https://media.wizards.com/images/magic/daily/mm/mm195_gei.jpg)[Geist Trappers](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Geist+Trappers) | Art by [Anthony Palumbo](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Anthony+Palumbo%22%5D)

**Version C (The Fighter)—Soulbond creatures grant abilities both to themselves and to the creatures they are paired with**

This version had a couple of things going for it. The flavor was great. Both creatures were better for the union. This version was pretty easy to track (they kind of feel Sliver-ish) and had a game play that felt very unique.

Once we crunched all of the above issues, the team realized we wanted to use version C, which, of course, led to the next issue.

The Next Issue
We thought we'd solved the problem. Soulbond was going to grant abilities to itself and the creature it paired with. What this meant, though, was the creature couldn't naturally have the ability. For example, if a soulbond creature granted vigilance when paired, it couldn't have vigilance until it was paired. This might not sound like a big deal, but it actually caused a few problems.

The first is the image problem. If soulbond creatures aren't upgraded until they're paired it meant the base version looked anemic. For example, look at [Druid's Familiar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Druid%27s+Familiar).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Druid%27s+Familiar)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Druid%27s+Familiar)  
Most players know that you get a bear (a 2/2 creature) for ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif), often with an extra bonus. [Druid's Familiar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Druid%27s+Familiar) costs ![](https://web.archive.org/web/20161227130050im_/http://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless3.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif). At first glance, this seems pretty bad. It's not until you understand not only how soulbond works but how soulbond creatures paired to each other work that you get that two [Druid's Familiar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Druid%27s+Familiar)s paired to one another are both 6/6 creatures. (In case you weren't aware, each [Druid's Familiar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Druid%27s+Familiar) grants +2/+2, meaning that together they grant +4/+4 to both creatures.)

The second issue is what I'll call the Angel issue. It's a set rule that all Angels fly, but soulbond creatures don't gain their ability until paired. This meant an Angel with soulbond can't exist because the two rules contradict. In a set all about Angels who supposedly are the forces bringing everyone together, the inability to have Angels with soulbond was a big deal.

![](https://media.wizards.com/images/magic/daily/mm/mm195_ang.jpg)[Angel of Jubilation](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Angel+of+Jubilation) | Art by [Terese Nielsen](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Terese+Nielsen%22%5D)

We tried versions where creatures had multiple abilities but only granted one (think of a Soulbond Angel that flies but grants vigilance when paired) and it just didn't work. The simplicity of each soulbond creature turning on and granting abilities short circuited when players had to start remembering which abilities were shared and which ones weren't.

In the end, we decided that we had to suck it up that the cards didn't look powerful at first glance. All **Magic** sets do some of this. We figured we would write articles to help players get how soulbond worked. We also decided that having no soulbond Angel was a price to pay to keep the mechanic as easy to grok as possible. We already knew the mechanic was a little complex (and would later get more complex in development), so if giving up an Angel helped lessen this problem, it was a price we had to pay.

Seeing Green
Having finally solved how the cards were going to work (or so we thought) we started down the next problem to solve. How were we going to use soulbond to help create color identity? One of the functions of mechanics in a set is to separate how the different colors play. Part of what makes **Magic** fun is that each color has its own philosophy and play style. This allows players to explore, because each color will give you access to a different facet of the set.

![](https://media.wizards.com/images/magic/daily/mm/mm195_dir.jpg)[Diregraf Escort](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Diregraf+Escort) | Art by [Ryan Pancoast](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22Ryan+Pancoast%22%5D)

Often, we solve this by only putting mechanics in certain colors. Sometimes, though, the flavor demands the mechanic show up in more colors, which means the definition is not limited by what color gets the mechanic but by how it's used by those colors.

Here are some of the major tools design gets to use to help focus a mechanic in a certain color or colors:

**Increase "As-Fan" in Certain Colors**

One of the things you learn early in designing a trading card game is the importance as what Ramp;D calls "as-fan." This term refers to how often one can expect a particular theme to show up percentage-wise ("as" it would happen to be "fanned" when opening a booster pack). The biggest two tools to affect as-fan are number and rarity.

If you want to increase as-fan, you either put more of that type of card in the set or you put more of that type of card at common. Often you do both. For soulbond, the number one color to get an increase of as-fan was green, with blue coming in second. What this meant was that we simply had more soulbond cards in green (and blue) and they also appeared at a lower rarity.

**Increase Power Level in Certain Colors**

If you want players to connect a particular color to a particular mechanic, another way to do this is with power level. Players remember the cards they play with. If the mechanic's best cards are in a certain color, that means players will get used to seeing that color with that mechanic. In *Avacyn Restored*, that meant we wanted to put the power level of soulbond with primary in green and secondary in blue. The simplest way to do this is straight-forward: make sure some of your best cards with the mechanic are in your primary color.



|  |  |
| --- | --- |
|  |  |

Another one of the tricks to help green is that we saved one of the most potent parts of soulbond solely for green—power and toughness pumping. The reason this is so good is that most abilities don't stack. If, for example, you have a soulbond creature that grants vigilance, that creature is weaker if it pairs with another copy of itself because having vigilance twice doesn't do anything. Power and toughness pumping, on the other hand, does stack, allowing good synergy when the creature is paired with itself.

**Increase Synergy in Certain Colors**

The final trick to help cement a creature as the primary color is to give it things that play well with the mechanic. Sometimes this is finding natural parts of the game that interact well. Other times, its designing cards that are made such that they would be bad normally but very good with the mechanic. This allows the player drafting a soulbond deck to get copies of these cards because nobody else wants them. [Flowering Lumberknot](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flowering+Lumberknot) is a good example of a card like this.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flowering+Lumberknot)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flowering+Lumberknot)  
So that's how we made green the soulbond color. Why did we choose green, though? As I explained during *Avacyn Restored* preview weeks, everything in the set gravitated toward white. As such, the design team worked hard to steer things to other colors whenever possible.

Soulbond was all about cooperation and teamwork. Two colors in **Magic** are about the value of the group over the individual: white and green (the two enemies of black, the color of putting the needs of the individual first). If we couldn't use white, green was the next logical choice. Power/toughness pumping, which was one of the strongest abilities for soulbond to grant, also felt most at home in green.

Another quick aside—in early playtests, every color was boosting power and toughness, but we found it was just too good in large numbers so we cut it down to just a few cards all in one color.

Coming and Going
If I'm telling the design story, it ends here. We figured out how we wanted soulbond to work. We chose the colors we wanted soulbond to lean toward. The cards were playing well and we handed over the file. Remember in this version, soulbond creatures only paired when they entered the battlefield. So what happened?

![](https://media.wizards.com/images/magic/daily/mm/mm195_nig.jpg)[Nightshade Peddler](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nightshade+Peddler) | Art by [John Stanko](http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoileramp;method=visualamp;action=advancedamp;artist=+%5B%22John+Stanko%22%5D)

In development playtest, many members of the development team got frustrated by soulbond. Having to pair when you cast the soulbond creature led to "feel bad" moments. First off, it was hard to make cheap soulbond creatures because the desire to pair them made players unwilling to play them early. Even later in the game, having to wait to have a creature to pair with often meant that players held back soulbond creatures.

The worse, though, was that once a creature paired with a soulbond creature was killed, the soulbond creature just became a low-powered vanilla creature. ("Vanilla creature" is what Ramp;D calls a creature with no other abilities.) Sometimes you could cast a new soulbond creature and pair it to the soulbond creature on the battlefield, but this happened infrequently enough that the power level concern was still valid.

So why didn't design make this change? I could say that design tends to like keeping things as simple as we can, but that's not the answer here (although we do). Why didn't we have soulbond creatures pair when other creatures entered the battlefield? Because we never thought of it. The cards were working well in design playtest (note that overall card balance is on a more even keel in design playtest so we can test all the cards, but this can sometimes keep us from seeing how certain elements react) so we didn't explore ways to improve upon them. I remember the first time [Dave Humpherys](http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Dave%20Humpherys) (*Avacyn Restored*'s lead developer) told me about [the tweak to soulbond](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/191) and my response was "that sounds kind of cool."

A Little Bit of Soulbond
And that is how soulbond went from design playtest card to final printed card. I hope you enjoyed the trip through the process of making this mechanic. As always, I'm interested to hear your feedback. What do all of you think of soulbond? You can let me know on [Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), and [Google+](https://plus.google.com/107824009487778543249/posts), in my email, or in the thread to this column. I'm interested in what you have to say.

Join me next week when we shift some planes.

Until then, may you learn the value of letting someone else help you.



---

  
![](http://wizards.com//mtg/images/daily/features/banners/AVR_ArticleFooterBanner_PTPOST_Top.jpg)![](https://media.wizards.com/legacy//mtg/images/daily/features/banners/avr_articlefooterbanner_ptpost_leftofbutton01.jpg)[![](https://media.wizards.com/legacy//mtg/images/daily/features/banners/avr_articlefooterbanner_ptpost_button01_static.jpg)](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/eventcoverage/ptavr12/welcome)






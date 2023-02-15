
---
[Link to Wayback Machine](https://web.archive.org/web/20220703213310/https://magic.wizards.com/en/articles/archive/making-magic/i-want-threshold-your-hand-or-possibly-my-artifacts-2010-10-15)

[_metadata_:author]:- "Mark Rosewater"
[_metadata_:description]:- "Welcome to Metalcraft Week! This week we'll be discussing one of the Mirran mechanics from Scars of Mirrodin. When a deadly plague-like force seeks to infect your whole plane, you have to pull out a few big guns. During the second week of Scars previews, I talked about the creation of metalcraft so I thought I'd use today's column to step back and look not at metalcraft"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "190991"
[_metadata_:path_date]:- "2010-10-15"
[_metadata_:publish_date]:- "2010-10-18"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "I Want to Threshold Your Hand (Or Possibly My Artifacts)"
[_metadata_:wayback_capture_timestamp]:- "2022-07-03 21:33:10"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220703213310id_/https://magic.wizards.com/en/articles/archive/making-magic/i-want-threshold-your-hand-or-possibly-my-artifacts-2010-10-15"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/making-magic/i-want-threshold-your-hand-or-possibly-my-artifacts-2010-10-15"
---


I Want to Threshold Your Hand (Or Possibly My Artifacts)
========================================================



 Posted in [Making Magic](/en/articles/columns/making-magic)
 on October 18, 2010 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/authorpic_markrosewater.jpg)
By Mark Rosewater




 Working in R&D since '95, Mark became Magic head designer in '03. His hobbies: spending time with family, writing about Magic in all mediums, and creating short bios. 






Welcome to Metalcraft Week! This week we'll be discussing one of the Mirran mechanics from *Scars of Mirrodin*. When a deadly plague-like force seeks to infect your whole plane, you have to pull out a few big guns. During the second week of [*Scars* previews](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/108), I talked about the creation of metalcraft so I thought I'd use today's column to step back and look not at metalcraft specifically but at the larger group of mechanics that metalcraft is a part of—something we refer to in Ramp;D as threshold mechanics.

Threshold Me Close
I guess I should begin by defining my terms. What exactly is a threshold mechanic? A threshold mechanic is a mechanic that allows a card to swap between various states based on some external criteria somewhere in the game. If thing X is true, then the card swaps from State A to State B (and possibly more states). Let's demonstrate with a threshold mechanic. In fact, we'll demonstrate *the* threshold mechanic—threshold. 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Springing_Tiger)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springing_Tiger)  
[Springing Tiger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springing+Tiger) is a 3/3 creature (State A). If you ever have seven or more cards in your graveyard, though, [Springing Tiger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springing+Tiger) turns into a 5/5 creature (State B).

Now let's look at a metalcraft card:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Carapace+Forger)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger)  
[Carapace Forger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger) is a 2/2 creature (State A). If though you ever have three or more artifacts on the battlefield, [Carapace Forger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger) turns into a 4/4 creature (State B). 

As you can see, threshold cards are structurally very similar. (Note that by "threshold cards," I mean the class I'm talking about, not cards with the *Odyssey* mechanic threshold. I'm using this word because it is the slang Ramp;D uses, but I agree it would be less confusing if the category wasn't named after a mechanic in the category. When I use the word "threshold" for the remainder of the article, unless I specify otherwise I'm talking about the class of cards.) The only real difference between them is what causes the swap from A to B. Luckily, this one difference is a pretty important one. For example, [Springing Tiger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Springing+Tiger) and [Carapace Forger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger) go into very different types of decks. The use of a threshold mechanic in one area does not impede on the use of it in another. As such, threshold mechanics have a considerable amount of design space.

Before we move on though, let's dig a little deeper into what exactly is a threshold mechanic. I'll begin with a very popular creature from **Magic**'s past.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kird+Ape)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kird+Ape)  
[Kird Ape](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kird+Ape) is a 1/1 creature (State A). If, though, you ever have a Forest on the battlefield, [Kird Ape](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kird+Ape) turns into a 2/3 (State B). I bring [Kird Ape](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kird+Ape) up because it is very easy to think of threshold as requiring a condition that involves some substantial work on behalf of the player. The condition can be very simple. What matters is that if the condition is met, no matter how simple it is, the state of the creature changes.

Now let's try a card from *Ravnica*:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Halcyon+Glaze)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Halcyon+Glaze)  
Is this a threshold card? [Halcyon Glaze](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Halcyon+Glaze) is an enchantment (State A). However, if you ever cast a creature spell, [Halcyon Glaze](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Halcyon+Glaze) turns into a 4/4 flying creature (State B). It sure seems like a threshold card. Note that this card does three things we haven't seen yet. One, the state change is a card type change. Two, the condition it is looking for is an event, it requires something to happen rather than something to just be. Three, the change is of a defined duration. You know when it turns on and when it's going to turn off. (So yes, for those that like to dwell of the minutiae, technically permanents with landfall that change state do fall into the overall threshold category.)

Let's look at another classic **Magic** card from days long ago:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mishras_Factory)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishras_Factory)  
Is this a threshold card? [Mishra's Factory](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mishra%27s+Factory) starts as a land that taps for one colorless mana (State A). If, though, you ever pay one mana, it turns into a 2/2 artifact creature (State B). This isn't a threshold card. The reason has to do with a word you might have missed in my description of what makes a threshold mechanic: A threshold mechanic is a mechanic that allows a card to swap between various states based on some **external** criteria somewhere in the game. 

Cards that can change themselves from state A to state B are not threshold cards. An important key to threshold cards is that something else causes them to change. Threshold cards have to care about something larger than themselves. (Hmm, a little hidden philosophy stuck away in a grouping of **Magic** mechanics?)

Let's take a look at a card from *Alpha*:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Keldon_Warlord)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keldon_Warlord)  
Is this a threshold card? Before we answer, let's take a look at a card I just made up:


> **Keldon Shoeshine Boy**  
>  1R  
>  Creature – Human Barbarian  
>  1/1  
>  If you ever control another creature, Keldon Shoeshine Boy gets +1/+1.
> 
> 

Clearly Keldon Shoeshine Boy is a threshold card, so why wouldn't [Keldon Warlord](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keldon+Warlord) be? It's just Keldon Shoeshine Boy with more possible states.

Note that in my definition of threshold I included "various" states rather than two. Why? Imagine this card:


> **Super-[Carapace Forger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger)**  
>  2G  
>  Creature – Elf Artificer  
>  Metalcraft – Super-[Carapace Forger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger) gets +2/+2 as long as you control three or more artifacts.  
>  Mega Metalcraft - Super-[Carapace Forger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger) gets +6/+6 as long as you control seven or more artifacts.
> 
> 

Is this card not a threshold card? Adding abilities to it doesn't remove it from the category. It still meets all the criteria. From this we know that threshold cards can have more than two states (well, that and I stated such above). Which brings us back to [Keldon Warlord](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keldon+Warlord). He is what we'd refer to in Ramp;D as a scaling threshold card. That is, he changes states based on external criteria but there are a large number of iterations. Usually this happens when you are counting the existence of something and each additional thing makes the card stronger.

What this means is that there is a spectrum of threshold cards. (By the way, Devin Low covered this topic in relation to tribal mechanics [back in 2007](http://archive.wizards.com/magic/magazine/Article.aspx?x=mtgcom/daily/dl10) if you want to see this discussion from a different vantage point.) On one end we have threshold one. These cards just need one single thing to create their change. [Kird Ape](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kird+Ape) is an example of this end of the spectrum. The other end of the spectrum is count-me threshold where the threshold has various stages each dependent on how many you have of a particular thing. [Keldon Warlord](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keldon+Warlord) is an example of this end of the spectrum.

Like any definition, there is definitely gray area. Take one of my all-time favorite cards:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Maro)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maro)  
Is [Maro](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maro) a threshold card? It has a lot of similarities to [Keldon Warlord](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keldon+Warlord). It's a \*/\* creature that looks at an external criteria to set various stage levels. It's criteria is oddly backwards from most threshold cards though in that it's the act of doing something that shrinks the creature, but there are threshold cards where the B state is worse than the A state. I believe [Maro](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Maro) barely squeaks in but it definitely starts to show how the definition can drift.

There are other subtleties that Ramp;D cares about when talking about threshold. For example, we have a concept we called threshold 0+. These are scaling threshold cards that meet the condition they are searching for. The most common place this happens is with tribal. Here's an example:

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Priest_of_Titania)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Priest_of_Titania)  
The [Priest of Titania](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Priest+of+Titania) always taps for ![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) because it counts itself, but the reason this card is considered a threshold card (because remember we require an external criteria in the definition) is because its strength comes from counting other Elves on the battlefield. The term threshold 0+ means that the card always has some function even if no external criteria is ever met. I'm trying not to dig too far down the rabbit hole as a lot of the small subtleties can get a little heady if you're not used to talking about them.

The reason I've spent so much defining threshold mechanics is that I wanted to spend today's column talking about designing them. I felt it was important to understand what we're talking about before we start actually talking about it.

Threshold Your Head High
Now we get to talk about designing threshold mechanics. What are the lessons, Ramp;D has learned over the years?

Lesson #1: Threshold Is All About the Tension Between the Variance
There are two big factors you have to keep in mind when looking at threshold creatures. Number one, what are the differences between the various states? And number two, how hard is the external criteria to meet? These two factors are important because it's the interaction of them that defines the feel of the mechanic.

![](https://media.wizards.com/images/magic/daily/mm/mm113_forger.jpg)  
For example, let's take metalcraft, as it's Metalcraft Week. How much a creature will change is tied to the difficulty of the change. Using [Carapace Forger](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carapace+Forger), let's examine what happens if we start fiddling with the requirement to cause the change. Our constant will be that we are starting with a ![](https://web.archive.org/web/20211201201921im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://web.archive.org/web/20220123123600im_/https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) 2/2 (because Ramp;D does love obsoleting [Grizzly Bears](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears), I mean [Runeclaw Bear](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runeclaw+Bear)). To help me with this exercise I asked developer Zac Hill to give me the proper numbers. Here's what we get as we turn the metalcraft dial:


> Change requires 1 artifact on the battlefield - 2/3  
>  Change requires 2 artifacts on the battlefield - 3/3  
>  Change requires 3 artifacts on the battlefield - 4/4  
>  Change requires 4 artifacts on the battlefield - 4/5  
>  Change requires 5 artifacts on the battlefield - 5/5  
>  Change requires 6 artifacts on the battlefield - 7/7  
>  Change requires 7 artifacts on the battlefield - 8/8  
>  Change requires 8 artifacts on the battlefield - 12/12  
>  Change requires 9 artifacts on the battlefield - 16/16  
>  Change requires 10 artifacts on the battlefield - 20/20
> 
> 

As you can see, as we change the requirements we change what you are able to get. The trick with threshold mechanics is figuring out the sweet spot. If the change is too easy, you often don't get much making the hoop jumping uninteresting. ("Now my 2/2 is a 2/3. Whoopee!") If you make the change too hard, you run the risk of annoying your players. (Getting a 20/20 one out of twenty games will frustrate just about everyone.) Players are willing to jump through hoops but there is only so much failure they will take before they abandon the mechanic.

The harder the change, the bigger the difference. This means the harder the change, the greater the variance. The more the creature changes, the greater the swinginess of the mechanic. As I've explained before, Timmy, in general is more accepting of wide variance mechanics while Spike is the least accepting. The unknown and wide swings are fun for many Timmies. Most Spikes, on the other hand, tend to appreciate consistency in their mechanics.

The offshoot of this is that threshold mechanics that are easier to meet tend to be more Spike-friendly while the ones that are harder to do tend to play better with Timmy. Interestingly, the hardest to accomplish are actually enjoyed greatest by Johnny who values solving the puzzle of how to make the change happen. What this all means is that there are threshold mechanics for each psychographic but who likes what is very determined by how hard the change is to create.

Lesson #2: There's A Sweet Spot
When we did threshold, we were asked why we didn't call it threshold 7 and people now are asking why we didn't call it metalcraft 3. The answer is that the numbers we reached are the sweet spot. When measuring the two factors against each other, it turns out that there is usually one combination that plays best. We don't add a number, because there's no reason to open up future design space that we won't use. 

![](https://media.wizards.com/images/magic/daily/mm/mm113_blast.jpg)  
A lot of people are fooled because threshold mechanics have the potential for range. They look at metalcraft and think to themselves there must be cards that could work with needing four artifacts on the battlefield. What they are missing is that there is some spot in game play where the tension is properly balanced. When we tried four artifacts on the playtesting we found that it was a little too hard to do. Yes, we could bribe players with a larger payoff, but design isn't about forcing players to do what you could make them do. Design is about figuring out what the players want to do and then making the game do that.

There's been a lot of talk on the boards about tension lately. Tom mentioned in an [article](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/110) a few weeks back how we changed the spellbombs in *Scars of Mirrodin* to lessen a certain tension. (Although I should add that it increases tension on a different axis—do I spend them before I can get the extra card?) This prompted a big discussion about the importance of tension for strategic play. Let me state for the record that Ramp;D isn't against tension. That said, all tensions are not made equal. Tension unto itself is not a positive thing. Forcing a player to make strategic choices can be good game play, but those choices have to empower the player not make him or her feel helpless.

Both complexity and tension are valuable tools when used in the right amount and in the right places. Used incorrectly though, both have the ability to lessen the fun of the game. The role of Ramp;D is to figure out when and where to use tension to maximize enjoyability. This is especially true on threshold mechanics because getting the right combination of factors is all about setting the tension level in the right place.

Lesson #3: Be Careful of Complexity
There's another reason we tend to keep threshold numbers locked to one number—not doing so causes endless complexity. As an example, early in design, we tried threshold (the *Odyssey* mechanic) at several numbers—3, 7, and 10 (you can think of it as mini-threshold, threshold, and maxi-threshold). The problem we quickly ran into was this: With just threshold, you have to remember the following:


>  1) Are there seven cards in my graveyard?  
>  2) Are there seven cards in my opponent's graveyard?  
>  3) If yes to either question, what is the change of each threshold permanent on the battlefield?
> 
> 

That's not an insignificant number of things to track. Now let's examine the world with the three different states:


>  1) Are there three cards in my graveyard?  
>  2) Are there seven cards in my graveyard?  
>  3) Are there ten cards in my graveyard?  
>  4) Are there three cards in my opponent's graveyard?  
>  5) Are there seven cards in my opponent's graveyard?  
>  6) Are there ten cards in my opponent's graveyard?  
>  7) Which cards with threshold care about having three cards in a graveyard?  
>  8) If yes to 1 or 4, what is the change of each of the relevant threshold cards?  
>  9) Which cards with threshold care about having seven cards in a graveyard?  
>  10) If yes to 2 or 5, what is the change of each of the relevant threshold cards?  
>  11) Which cards with threshold care about having ten cards in a graveyard?  
>  12) If yes to 3 or 6, what is the change of each of the relevant threshold cards?
> 
> 

Playtesting proved having three different versions to be brain melting. It was more information than someone could track without dedicating most of your mental resources to it. In design, we call this a "brain freeze." You see, there is a line where you overload the players so much that they are incapable of mentally processing enough to function. (And yes, this line varies from player to player.) Most players never have to think about concepts like brain freeze because Ramp;D never lets brain freeze-inducing sets out the door. (I'm sure there are those that would argue on this point.)

![](https://media.wizards.com/images/magic/daily/mm/mm113_stoic.jpg)  
When a playtest produces brain freeze it's a sign that there's too much going on. Through trial and error we've learned that not only do thresholds have a sweet spot, but also that one number tends to provide plenty of interaction. Multiple numbers don't add enough strategic gameplay to overcome the brain freeze concern so as a general rule threshold mechanics just use a single transformation, most often a single number.

Lesson #4: Beware of the Linear-ness of Threshold Mechanics
A quick refresher (hopefully those of you that took [The Great Designer Search 2](http://community.wizards.com/magicthegathering/wiki/labs:Gds) Multiple-Choice Test already knew this): a linear mechanic is a mechanic that encourages you to play with other specific cards. The example I've always used for linear cards is [Goblin King](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+King), but I should get with the times so I'll change my example to [Goblin Chieftain](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Chieftain).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Goblin+Chieftain)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Chieftain)  
The [Goblin Chieftain](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Goblin+Chieftain) says, "play with Goblins." If you aren't going to play with Goblins, there's really no reason to play with the Chieftain. That's what makes it a linear card. (For more on linear and its opposite modular, check out my column "[Come Together](http://archive.wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr92)") 

I bring up linear-ness because it's something designers have to think about with threshold mechanics. Basically, it boils down to this—to satisfy the condition of a card with a threshold mechanic, you have to build a deck that helps you do whatever condition you need to meet. Once you've done this, other threshold cards with the same condition become much more attractive. For example, once you've bothered to get three artifacts on the battlefield why wouldn't you want other cards that are also over the curve if this condition is met.

Threshold mechanics beget more of themselves because they share the same hoop. Note that the more the condition is a natural part of the game (such as the subset of landfall cards I talked about earlier) the more modular the cards become. 

The reason this becomes important for designers is that we try in sets to keep a balance between linear and modular mechanics. The pendulum will swing, but in general, we don't want all the mechanics in a set being linear or modular. (Ironically, I bring this up during one of the most linear sets [*Scars of Mirrodin*] that we've done in quite some time.) When you use a threshold mechanic, it usually means you want to start looking for a modular mechanic to help keep the balance.

Putting You On Threshold
That's all the time we've got for today. I hope this insight will show how much design has to think about different mechanical subsets. If you enjoyed today's column let me know and perhaps I'll take a look at another subset in a future column.

Join me next week when everyone will get to take the *Great Designer Search 2* Multiple-Choice Test. After you do, we'll give your score (and you'll see if you'd have made the cut) and then I'll walk through each question one by one providing not only the answer but the explanation behind it as well. 

Until then, may you get to State B.

[![](https://media.wizards.com/images/magic/daily/features/SOM_Article-banners_MTGO.jpg)](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/10062010e)  







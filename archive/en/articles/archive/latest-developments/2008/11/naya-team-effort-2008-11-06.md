
---
[Link to Wayback Machine](https://web.archive.org/web/20211209063019/https://magic.wizards.com/en/articles/archive/latest-developments/naya-team-effort-2008-11-06)

[_metadata_:author]:- "Tom LaPille"
[_metadata_:description]:- "As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on Magic development. Enjoy! –Kelly Digges, magicthegathering.com editor Hello there everyone! My name is Tom LaPille and I started developing Magic sets four months ago. The first Magic cards I bought were a two Tempest theme decks and the game"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "186611"
[_metadata_:path_date]:- "2008-11-06"
[_metadata_:publish_date]:- "2008-11-07"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Naya Is a Team Effort"
[_metadata_:wayback_capture_timestamp]:- "2021-12-09 06:30:19"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20211209063019id_/https://magic.wizards.com/en/articles/archive/latest-developments/naya-team-effort-2008-11-06"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/latest-developments/naya-team-effort-2008-11-06"
---


Naya Is a Team Effort
=====================



 Posted in **Latest Developments**
 on November 7, 2008 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/tom.jpg)
By Tom LaPille




Tom LaPille makes things. Some of the things he makes are card sets, like Dark Ascension and Born of the Gods. Sometimes he makes stories, too. Sometimes he makes unexpected things, like 16th-century Japanese clothing. He's probably making something right now. 






*As part of a special series, Latest Developments will be hosting a whole run of guest slots from some of the many people who work on **Magic** development. Enjoy!*  
 –Kelly Digges, **magicthegathering.com** editor 

Hello there everyone! My name is Tom LaPille and I started developing **Magic** sets four months ago. The first **Magic** cards I bought were a two *Tempest* theme decks and the game never let me go. Since then, **Magic** has taken me all over the continental USA, as well as to Hawaii, Canada, and Spain, and it's currently put me here in Seattle, Washington at what can only be described as a dream job. I fantasized about working here for many years and started seriously working toward that goal about a year ago, and now that I'm here it's every bit as awesome as I thought it would be. If you're ever on the fence about whether to pursue a lifelong dream, go for it. It'll be worth it, and you only get to live once!

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=%5Bcard%5D)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=%5Bcard%5D)Working in **Magic** Ramp;D is almost all fun and actually is all games, but one of the hidden realities of **Magic** is that there are lots of things that have to happen after we finish development on a set before you get to play with the awesome new cards we made. Editors and rules managers carefully check the text of cards to make sure they work and to avoid strange and unexpected interactions. Typesetters, graphic designers, and translators work to make the cards look as awesome as possible and so that people all around the world can play. Then, the cards are sent off to the printer. The net effect of this is that there are always many months worth of **Magic** cards that have been finalized but not yet released.

Internally, we refer to the sets that one neither played in the real world nor worked on as one's "black hole" because one does not have time to experience those sets at one's own pace, and instead must learn enormous amounts of cards very quickly. Due to the nature of human learning, this does not work as well as repeated experience over time, so most people here knows the sets in their black hole a little less well than the rest. I started work here at almost exactly the same time as the release of *Eventide*, and when I got here *Conflux* was still in development. That means that my black hole contains exactly one set, and that set happens to be *Shards of Alara*. 

This means I don't have any firsthand development stories to tell. However, I've picked up lots of juicy tidbits from talking to my fellow designers and developers. I've also divined many secrets from delving into Multiverse, Wizards' internal database. It contains card files as well as logs of comments about almost every aspect of the cards. **Magic** Ramp;D is filled with intelligent people, so going through those comments is an education in game development in itself. Many of those people are also very funny, which makes reading Multiverse a constant joy.

Given that this is Naya week, I'll be telling development stories about Naya cards. As I read through them in Multiverse it really struck me how much of a team effort **Magic** is. Everyone who works on **Magic** wants the cards to be as fun as they can be. Developers iron out mechanical kinks and problem interactions, but we can't make **Magic** awesome on our own. Without designers our cards wouldn't be exciting, without editors they would be indecipherable, and without rules experts they might not work at all! Walk with me and discover how the various parts of **Magic** Ramp;D work with development to make maximally awesome **Magic** cards.

Qasali Ambusher
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Qasali+Ambusher)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Qasali+Ambusher)The design behind this card is very cool. It's easy to imagine a stealthy and clever cat sentry who specializes in ambush tactics. What is not so easy is to translate that into game terms. **Magic**'s rules are carefully designed to parse logically and because of that we can't wave our hands and print something like "If you're being attacked, you can put this guy into play for free." Every **Magic** text box must be unambiguous. Given that, the developers had to find a template that stood up to rigorous analysis. Thankfully, we had the support of Del Laugel, a **Magic** editor and templating expert who presented various options that actually worked. Given those options, there now were decisions to be made.

It was immediately clear to the developers that there needed to be some kind of restriction on who could play the card for free. [Qasali Ambusher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Qasali+Ambusher) is a green and white gold card, and it would feel strange indeed if a black-red deck was allowed to summon it with no access to green or white mana. Therefore, some kind of color restriction clause was needed. The line "If a creature is attacking you, you may return a [Plains](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) or a [Forest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest) you control to your hand to play [Qasali Ambusher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Qasali+Ambusher) without paying its mana cost" was considered, but this would let mono-green or mono-white decks have access to the card. Eventually the current version that only requires a [Plains](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains) and a [Forest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest) in play was chosen because it was the simplest restriction that limited the card to true green-white decks.

The second question was whether [Qasali Ambusher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Qasali+Ambusher) should let you "play [Qasali Ambusher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Qasali+Ambusher) as though it has flash" or if it should let you "put [Qasali Ambusher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Qasali+Ambusher) into play." We went with the first template for a few reasons. One is that under the second template it is unclear whether anything ever goes on the stack and therefore if and when you can respond to it. The other reason is that we like it when **Magic** cards are able to interact with each other, and therefore we wanted counterspells to be able to stop a [Qasali Ambusher](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Qasali+Ambusher)'s ambush. This was not possible without having the Ambusher be "played."

Amusingly, the most natural way to write this card in my opinion is "When a creature attacks you and [some other condition], you may play this as though it had flash without paying its mana cost." However, this doesn't work because triggered abilities can't trigger from hidden zones. If something isn't public knowledge, it can't go on the stack!

The final version of this card is both an awesome Limited card and a potent Constructed surprise. Because it only requires that you control a [Forest](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forest) and a [Plains](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plains), you can satisfy the Ambusher's requirements with just a [Temple Garden](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Temple+Garden) or Savannah! I can tell you from personal experience that it feels really awesome when an angry cat comes out of nowhere to protect you from your opponent's first attack after you've played only one land.

Mosstodon
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Mosstodon)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon)Have you ever wondered why many of *Shards of Alara*'s "5 power matters" cards don't have static abilities? For example, why doesn't [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon) read "Creatures with power 5 or greater have trample."? The answer is that under **Magic**'s rules, that line of text has some very strange consequences. **Magic**'s rules include different groups of effects called layers, and the layers of effects are applied to the cards in a specific order. That order is:

1. Copy effects
2. Control-changing effects
3. Text-changing effects
4. Type-changing effects
5. All other continuous effects that do not change power or toughness
6. Continuous effects that change power and toughness

Let's assume that you had this card as your only creature in play:


> Design Mosstodon  
>  3GG  
>  Creature – Plant Elephant  
>  5/3  
>  Creatures with power 5 or greater have trample.

The static ability on this card is applied in layer 5. Because Design [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon) has 5 power at that time, it gains trample. This works just like you think it should. So far, so good.

Now imagine that you play a [Cylian Elf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) and then play [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth) on it. The [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon)'s ability is applied in layer 5, at which point the [Cylian Elf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) has 2 power. Therefore, the [Cylian Elf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) doesn't gain trample. Then, in layer 6, the [Giant Growth](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Growth)'s bonus is applied, making the [Cylian Elf](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cylian+Elf) into a 5/5 that does not have trample.

Now imagine that your opponent controls a [Night of Souls' Betrayal](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Night+of+Souls%27+Betrayal). Design [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon)'s static ability is still applied in layer 5, which gives the Design [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon) trample since it has 5 power at the time. Then, in layer 6, the [Night of Souls' Betrayal](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Night+of+Souls%27+Betrayal) ability is applied, leaving Design [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon) as a 4/2 with trample.

These interactions are very strange and counterintuitive. Most **Magic** Ramp;D members had no idea that this was how it would work, so it's only fair to assume that most of our audience wouldn't either! We believe that it isn't very fun to print cards that sound like they work one way but actually don't, so at the behest of our rules manager Mark Gottlieb, the "5 power matters" cards with static abilities were all given activated or triggered abilities instead.

I wasn't around when this happened, but in a happy coincidence I think it made for more fun **Magic** cards. I'm a huge fan of "shields down" moments in gaming. It generally isn't very fun when there is no way to deal with something inside of a game. It's also really fun to feel smart when you find the precise weakness in your opponent's defenses and exploit it! Imagine if [Drudge Skeletons](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drudge+Skeletons) didn't cost mana to regenerate. You would be annoyed that you couldn't ever kill it, and you would also never experience the joy of [Shock](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock)ing it when your opponent doesn't have a black mana free.

In my opinion, the big winner in terms of gained fun in this particular case is [Rakeclaw Gargantuan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakeclaw+Gargantuan). If that card always gave each of its 5-power friends first strike, you might not be able to attack into your opponent's team of multiple 5-power creatures even when he or she had no available mana. This comes up less with [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon) than with [Rakeclaw Gargantuan](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rakeclaw+Gargantuan), but it still does matter. In fact, just yesterday I was able to use a 1/1 Goblin token to block a sixth-turn [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) that my opponent had tapped out for while a [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon) looked on sadly. I didn't win that game, but I lost it one turn later than I would have if that [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) had the [Mosstodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mosstodon)'s help for free!

Bull Cerodon
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bull+Cerodon)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon)I want to talk about this card for two reasons. The first reason is this Multiverse exchange between Ken Nagle and Devin Low, which is a great example of the kind of Multiverse comments that make me smile.


> KEN 2/2: This guy's theme song is "Here Comes The BOOM", it plays when I cast him.  
>  DAL 2/7: Ken Nagle is awesome.
> 
> 

The second reason is that this is actually my favorite *Shards of Alara* card! I love cards that are simple, cards that make sense in a set, and I also like cards that are powerful. [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) delivers on all three categories. It's a pile of numbers with two keywords and it has 5 power in a shard where that matters. It's a bit less obvious how powerful it is, but a well-known Limited writer recently described the card as "an uncommon [Rorix Bladewing](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rorix+Bladewing)" and that description isn't far off. [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) hits hard and fast, it plays both offense and defense, and it's reasonably priced.

I became enamored with this card while I was gunslinging at a local Prerelease. My deck wanted to be black-red to take advantage of three [Blightning](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blightning)s and ten spot removal spells, but it was a little short on playables and big creatures. I determined that I was supposed to splash green for a few big monsters, but I still needed one more card and it was going to have to come from white because of what mana fixers I already had. My two options were [Ajani Vengeant](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ajani+Vengeant) and [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon). It pained me at first to leave Ajani on the bench, but I really wanted another big guy to finish off games, and Ajani would have just been an eleventh removal spell. That single inconspicuous [Bull Cerodon](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bull+Cerodon) was singlehandedly responsible for about two thirds of my game wins that day.

Woolly Thoctar
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Woolly+Thoctar)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar)Now that we've talked about a creature with a two-keyword text box, it's time to talk about one with no rules text at all. [Woolly Thoctar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar) was a surprise to the world, but it was as much a surprise to non-designers internally, as you can see here:


> KEN [Ken Nagle] 2/2: amp;gt;=O "Holy \*\*\*\*!" (- reaction of all Magic players.)  
>  DG [Dave Guskin] 2/4: "me: Holy \*\*\*\*!" to KD. I think KEN can read minds. \_  
>  SW [Steve Warner] 2/5: I believe Ken has my mind read.  
>  AF [Aaron Forsythe] 2/5: Hard to justify this historically. Feels like we've lost our minds.  
>  Del [Del Laugel] 3/15: The flavor text is in, so I finally got around to looking at this card. :)
> 
> 

However, even vanilla creatures must get developed. This card began life as a Cat Warrior, which caused dual problems. First, the art came in with only a single leonin in the frame, and one leonin is a stretch for a 5/4. Second, it did crazy things with [Obsidian Battle-Axe](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Obsidian+Battle-Axe)! Ken Nagle may not be a developer, but he does enjoy channeling his inner Timmy and equipping enormous monsters with big axes. His powerful Warrior deck that included both [Obsidian Battle-Axe](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Obsidian+Battle-Axe) and [Woolly Thoctar](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Woolly+Thoctar) reminded the developers that they had to be careful where they put class creature types. The best replacement art for the single-leonin piece was an illustration of a beast; this suited the developers just fine, because Beasts aren't smart enough to have a class!

Soul's Fire
[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Soul%27s+Fire)](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul%27s+Fire)This card is a Ken Nagle design that was inspired by one of the most iconic special moves from side-scrolling fighting games: the fireball! It's flavorful that a creature unleashing its inner strength at another creature would do damage based on its own power, and this also happens to play well with the Naya "high power matters" theme. All in all, this is an awesome top-down design that fits perfectly into its set. 

Based on all this, you would think that the card's journey through **Magic** Ramp;D would have been uneventful. However, you would be wrong, because there was little consensus about how to translate the fighting game fireball into **Magic** terms. Does a fighting game character tap when he uses a fireball attack? Does the creature itself deal the damage, or is it the fireball that deals the damage? One incarnation of this card had the creature performing the fireball tap as an additional cost, and another had [Soul's Fire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul%27s+Fire) itself dealing the damage and not the creature. If you had to choose from these options, which do you think expresses the concept of "my creature fireballs your creature" best?

I can only speak for me, since the Multiverse comments are somewhat cryptic, but I think we got as close as we could have gotten. A fighting game character who performs a fireball may be subject to a few recovery frames, but that hardly feels like tapping to me. If the spell itself did the damage instead of the creature, that would sound to me like a fire spell that drew from the power of a creature I controlled as opposed to the creature itself performing the fireball. It's not clear whether this kind of question is in the realm of design or development to me, since in this case the argument was about how to translate a concept into mechanics. Our final choice did have some development implications, because the printed version of [Soul's Fire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul%27s+Fire) does nothing if the creature that is about to perform the fireball gets killed before [Soul's Fire](https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul%27s+Fire) resolves, but it was more important to the developers that we match the concept as well as we could.

We All Work Together
Looking at **Magic** from the outside, you might think that there are massive splits between the different people who work on **Magic**. This is just not how it works. Developers are in some ways ultimately responsible for how fun a set is, but without design, editing, and rules support, we would never be able to consistently produce sets as awesome as we do. I hope you enjoyed this Naya-themed look into how development works with other parts of **Magic** Ramp;D, and I hope to write for you again soon!








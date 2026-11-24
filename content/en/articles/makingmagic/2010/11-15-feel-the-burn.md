---
id: ym4trvcz
kind: article
lang: en
path: /en/articles/makingmagic/2010/11-15-feel-the-burn
title: Feel the Burn
published: '2010-11-15'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
    lang_detected: en
    capture_id: 879336
    url: https://magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
    captured_at: '2022-06-25 23:12:17+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
    lang_detected: en
    capture_id: 879336
    url: https://magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
    captured_at: '2022-06-25 23:12:17+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
    lang_detected: en
    capture_id: 879336
    url: https://magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
    captured_at: '2022-06-25 23:12:17+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
    lang_detected: en
    capture_id: 879336
    url: https://magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
    captured_at: '2022-06-25 23:12:17+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: ym4trvcz
  url: https://magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
  page_key: magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
  lang: en
  template: drupal
  captured_at: '2022-06-25 23:12:17+00'
  capture_id: 879336
  wayback_url: https://web.archive.org/web/20220625231217id_/https://magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
- document_id: ym4trvcz
  url: https://magic.wizards.com/en/articles/archive/feature/feel-burn-2010-11-15
  page_key: magic.wizards.com/en/articles/archive/feature/feel-burn-2010-11-15
  lang: en
  template: drupal
  captured_at: '2022-01-21 13:54:19+00'
  capture_id: 626383
  wayback_url: https://web.archive.org/web/20220121135419id_/https://magic.wizards.com/en/articles/archive/feature/feel-burn-2010-11-15
- document_id: ym4trvcz
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/117
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/117
  lang: en
  template: aspx
  captured_at: '2013-07-04 00:13:08+00'
  capture_id: 639260
  wayback_url: https://web.archive.org/web/20130704001308id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/117
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ym4trvcz
  capture_id: 879336
  url: https://magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
  wayback_url: https://web.archive.org/web/20220625231217id_/https://magic.wizards.com/en/articles/archive/making-magic/feel-burn-2010-11-12
  captured_at: '2022-06-25 23:12:17+00'
  template: drupal
  sha256: ec554ad80882cc14bc8f1eb28f24d350bc20433bbd542b5bb8efef452e5df4a7
render_recovery:
- code: image_without_source
  element: img
  reason: The preview omitted the image because it had no usable source address.
  occurrences: 1
---
Welcome to Burn Week. In honor of the release of The Premium Deck Series' [Fire and Lightning](https://web.archive.org/web/20101115000000/http://archive.wizards.com/Magic/TCG/ProductArticle.aspx?x=mtg/tcg/pdsfirelightning/productinfo), we're spending this week talking about damage of a very direct kind. Today I'm going to examine the design of direct damage to demonstrate there is a lot more going on than one might realize at first glance.

Burn, Baby Burn

Ramp;D loves a juicy argument, so when I told them it was Burn Week and I was going to talk about the design of direct damage, I had no idea the can of worms I was unleashing. Is burn and direct damage synonymous? What exactly is burn? What exactly is direct damage? The discussion led to many interesting points but I'm going to leave that discussion for Tom on Friday. I'm going to focus today instead on the design of direct damage.

![](https://i.ormos.uk/bc/ab/bcabbe0710f7089f6af125b4568a9bfcd1c752bc933f0caedea290c75fc2d663.jpg)  

Before I can do that I guess I should start by defining what I mean by direct damage. Note that for the purposes of discussing design, I have an incentive to make my definition as broad as I can. Design is very focused on the nuances of different styles of effects, so we tend to like to clump large similar groupings of mechanics together. With that caveat out of the way, I'm going to define direct damage as "noncombat damage created by a spell or ability that produces damage which hits a creature or player." For purposes of my definition, I'm assuming that the spell or permanent with the effect is the source of that damage (a.k.a. it is dealt directly to the creature or player).

Of all of the mechanics in **Magic**, direct damage is one of the most flexible. The point of today's article is to show you many of the different options available to a designer when they want to use direct damage.

Now, let's examine the different ways direct damage can be used:

1\. Damage Dealt by an Instant or Sorcery Directly to a Creature or Player. Color: Red

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning+Bolt)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt)

  

When most people talk about direct damage, this is what they think of. This style of direct damage is found exclusively in red. There are a lot of variations that show up in other colors, and I'll get to those in a moment.

As the iconic form of direct damage this is the one we most commonly use when introducing a new mechanic. Want to show how red uses the "new thing" in the set, stick it on this style of direct damage spell.

2\. Damage Dealt by an Instant or Sorcery Directly to a Player. Color: Red

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lava+Axe)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lava+Axe)

  

One of the biggest tools available to a designer is restriction. Restrictions don't just breed creativity they also open up more design options. For example, this takes traditional direct damage and chops off one of the options. This subset is also found exclusively in red.

![](https://i.ormos.uk/db/94/db940122ecfd3335a3dd9c8acfbdfc5af165a1091fccdc03023bca82fbfd2897.jpg)  

More often than not this subset is put onto red sorceries, but every once in a while you'll find it on an instant. This style of direct damage helps educate players about how important the ability to hit creatures is on direct damage spells. This subset tends to pale compared to the other side of the coin:

3\. Damage Dealt by an Instant or Sorcery Directly to a Creature. Color: Red

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Heat+Ray)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heat+Ray)

  

If you can take away one restriction you can take away the other. This subset is still very popular in Limited because creature removal is valued so highly. The other nice thing about this subset is that Ramp;D can push it a little more because at best it just destroys a single creature. This subset like the last is found exclusively in red.

This is the category that [Hornet Sting](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hornet+Sting) falls into, but, as I feel strongly it isn't a green ability, I'm not listing green here. However, as [Hornet Sting](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hornet+Sting) has become associated with my dislike of it, I thought I'd use this column to make a quick aside about why I dislike it. There are some who believe that the way to show that a color is bad at something is to print it at a very weak power level. Do you want to know how bad green is at creature kill? Just compare [Hornet Sting](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hornet+Sting) to [Lightning Bolt](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt). I am not one of those people.

![](https://i.ormos.uk/95/1f/951f66eeb6e78ed99a4bee563e98860e822f04f8d94952aaddf41c281fb6db87.jpg)  

The way I like to demonstrate a color is bad at something is not let the color do it. I believe strongly that absence of an ability speaks louder. When you see a card in a vacuum: 

**A.** You might not be able to gauge its power level or  
**B.** You assume that if you see one card like it, others exist; and some of those cards might be stronger.

I don't mind green decks making use of artifacts to deal direct damage to creatures (obviously the power level needs to be far lower than what red gets). I just don't want the card with a green border as I feel it educates the player incorrectly. I believe the color pie is the backbone of all design. As such, I think it's crucial to keep weaknesses of the color clear. Okay, I'm done venting on this topic.

4\. Damage Dealt by an Instant or Sorcery Directly to Subset of Creatures on the Battlefield. Color: Red

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pyroclasm)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pyroclasm)

  

Of all my categories listed today, this is probably the one that the least number of other people would label direct damage but from a design standpoint, there is little difference between "CARDNAME deals 2 damage to target creature." and "CARDNAME deals 2 damage to all creatures."

One of the ways we divvy up direct damage effects is by tweaking various knobs. This particular knob determines how many creatures the direct damage hits. It could hit two, it could hit all the opponent's creatures, or it could hit all creatures. Most of the effects of this kind tend to be done at uncommon and higher rarities. The few exceptions are effects that deal 1 damage to the subset and effects that just hit two targets.

![](https://i.ormos.uk/e3/f4/e3f47482875676073ec37cc2da8685edaa6bb3090f051e54ba4fd0bf1e09c741.jpg)  

These effects are almost all done in red. Black does get -N/-N effects to all creatures such as [Infest](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infest), but as this isn't damage, it doesn't get counted here.

5\. Damage Dealt as a Side Effect of an Instant or Sorcery. Color: Red

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Melt+Terrain)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Melt+Terrain)

  

While the damage is usually not the major focus of these spells, the fact that the spell can be used for the damage makes it fall into the direct damage box from a design standpoint. The best of these effects make the damage a flavorful extension of the effect. Usually this means that something is destroyed and its destruction brings with it some pain for that permanent's controller.

![](https://i.ormos.uk/94/f1/94f17344956599840a2a332c335876579c45aecae8846e1f717f48749f5d5615.jpg)  

These effects are almost always red because black, the other color that tends to do this, is almost always done as loss of life.

6\. Damage Dealt by a Repeatable Effect of a Permanent, Usually an Activated Ability. Color: Red

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Prodigal+Pyromancer)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prodigal+Pyromancer)

  

As I talked about during [my answers](https://web.archive.org/web/20101115000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/114aamp;showme=true) to the GDS2 [multiple-choice test](https://web.archive.org/web/20101115000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/114a), we've chosen to move "repeatable kill" out of common. As such, this type of cards now tends to show up in uncommon (or higher rarities if the damage is large enough). The greatest majority of these cards are creatures capable of dealing damage. From time to time you'll see these types of effects on artifacts or enchantments.

In the beginning, this started on a very iconic blue creature, Prodigal Sorcerer. The ability was moved out of blue and into red during the big Color Pie Shuffle that Ramp;D did eight plus years ago. Blue had too many abilities and red not enough, so we decided to move the ability that didn't feel at all blue to the color where it was obviously at home.

Besides the activated ability, we occasionally will put direct damage on a triggered ability that occurs whenever a certain action happens. Depending on the frequency of the trigger event, we sometimes will put mana on the ability.

![](https://i.ormos.uk/90/ef/90ef42370ec64b8027bf5d835be54b93ff68c0f72fbd826654d4a7812ba7de2c.jpg)  

More often than not, these abilities will hit creatures or players—but from time to time you'll see the effect restricted to either just creatures or just players.

As a general rule of thumb, we tend to keep the damage dealt by these kinds of cards pretty low (usually just 1 or 2 damage) because creatures that do more damage than that are a little too efficient at killing creatures. (When we do design them they are done at rare or mythic rare.)

7\. Damage Dealt by an Effect of a Permanent, Usually a Triggered Ability. Color: Red

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flametongue+Kavu)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flametongue+Kavu)

  

When we want to use effects to do larger amounts of damage, we tend to make those effects one-shot. Some common ways you'll see it:

> *   on an "enters the battlefield" trigger (what Ramp;D now affectionately calls "ETB effects")
> *   on an "enters the graveyard from the battlefield" triggers (known as a "death trigger" in Ramp;D)
> *   On an activated ability that requires a sacrifice
> *   On a triggered ability that forces the permanent to be sacrificed to create the damage

More often than not, these effects will have some mana tied to them. Like all the abilities so far, this subset is found pretty exclusively in red.

![](https://i.ormos.uk/70/b6/70b691a17237af3862837dd20a385ee94d9151cf3c7579a68147d88389d46641.jpg)  

While the repeatable ability tends to let you target either creatures or players, we are more willing with this subset to hit just one or the other.

8\. Damage Dealt by a Spell or Effect that then Gains the Controller of That Spell or Permanent an Equal Amount of Life. Color: Black, Red-White

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Drain+Life)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drain+Life)

  

One of the things we do to separate black and red (the only two colors that overlap more are white and green), is that we have red deal damage where black causes loss of life. For example, imagine red and black each have a 1/1 with a tap ability that causes the opponent to go down 1 life. Red will get "CARDNAME deals 1 damage to target player" while black will get "Target player loses 1 life."

There is one big exception though and it is where black gets its most popular form of direct damage: the drain ability. Richard Garfield included [Drain Life](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drain+Life) in *Alpha* and the flavor of draining life was so perfect for black, the effect became a staple. Drain life effects in black always deal damage to the source and then gain the exact same amount of life (well, there are some weird [Drain Life](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drain+Life) variants where you can drain more than you deal but that isn't something we would do today). The reason that drain life is damage rather than life loss (and yes, I know damage generally causes life loss) is that we need the parallel of damage to life to make the effect feel right. 

![](https://i.ormos.uk/1b/58/1b582e1d10d3faa65673cac82df284b3a0a0f47138a3f0764ea2c29355961707.jpg)  

This ability also has the quirky quality that it can be used either on mono-black cards or on multicolor red-white cards. You see, if red brings direct damage to the table and white bring life gain, voila you get a drain effect. The only advantage red and white get is that together they are more efficient at it than mono-black, so red-white drain effects are cheaper.

The existence of the drain effects, by the way, was one of the reasons I felt so comfortable moving lifelink into black during the great *Future Sight* creature keyword expansion. (If you're not sure what I'm talking about, you can click [here](https://web.archive.org/web/20101115000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr284).)

9\. Damage Dealt by a Spell or Effect Dealt Directly to an Attacking and/or Blocking Creature. COLOR: White

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Heavy+Ballista)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heavy+Ballista)

  

While red can deal its damage to just about whomever it chooses, white isn't quite so liberated. You see, white has, what I call "the good guy weakness." That is, white doesn't deal damage unprovoked. White doesn't shoot first. The classic example of this in popular culture is the Federation on *Star Trek*. Sure, they won't back away from a fight, but they equally won't start one. White's the same way.

In order for white to pull out its direct damage, the creature in question has to be in combat. Attacking, blocking—usually it doesn't matter. As long as the creature is fighting yours or attacking you, you're free to zap it with some juice. 

![](https://i.ormos.uk/fb/0a/fb0a42809b479b2d6a64d82d53397228feead98ba73ba9f63a7a3a770ed1c0a0.jpg)  

This ability is seen both on spells and on creatures. The spells are always instants as they need be cast during combat. The creatures usually have a tap ability (what's known in Ramp;D as "range strike"), sometimes with some mana required. Like the "pingers" in red (slang for creatures that activate to deal 1 or 2 damage a.k.a. [Prodigal Pyromancer](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prodigal+Pyromancer)—see how much Ramp;D lingo you're learning today), the range-strike creatures have been moved out of common.

10\. Damage Dealt by a Spell or Ability to Flyers. Color: Green

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Leaf+Arrow)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leaf+Arrow)

  

Whenever I complain about [Hornet Sting](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hornet+Sting), I always have someone bring up the point that green does, in fact, have access to direct damage in its color pie—to flyers. This comes about because in *Alpha* Richard liked the idea that white, blue and black had more flyers but that red and green were the anti-flying colors. This is where cards like [Giant Spider](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Giant+Spider) and [Earthbind](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Earthbind) came from.

Over time, red's anti-flying flavor seeped away, but green's stayed. Most large sets will have what Ramp;D calls a "spider," a creature with reach and higher toughness than power and most often creature type Spider. (Some nicknames are more valuable than others.) Green also traditionally gets an uncommon spell (occasionally shifted down to common as in the case of [Leaf Arrow](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Leaf+Arrow)) that can hurt flyers. The means are all over the board. Sometimes it's a destruction effect; sometimes it's a –N/-N effect; and sometimes it's direct damage.

![](https://i.ormos.uk/78/23/7823054b72fea7beeb192ca5da3ab730814773415775e885eee3fc8f4e4ebd35.jpg)  

*Alpha*, by the way, also had the card [Hurricane](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hurricane), which not only allowed green to deal direct damage to flyers but also to players. While [Hurricane](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hurricane)-like effects continued for a few years after that, Ramp;D has pulled direct damage to players (even if it always hit all players) from green.

11\. Damage Dealt to a Creature by an Effect on a Creature that Also Causes the Other Creature to Deal Its Damage Back. Color: Green

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Tracker)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Tracker)

  

By the technical definition I'm using today, there is one other direct damage ability that shows up in green, what we in Ramp;D call the "tracker" ability named after 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=a+creature+from+The+Dark)](https://web.archive.org/web/20101115000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=a+creature+from+The+Dark)

that first had this ability. The flavor of this ability is that you can make two creatures "fight" with one another directly. As this damage is not technically combat damage it officially gets listed here.

Surveying the Direct Damage

As you can see direct damage sneaks its way onto a lot more types of cards than is obvious at first glance. Damage is a very important aspect of the game and thus design has chopped it up accordingly. I hope today's column gives you some sense of the nuance design has to use when it deals with large chunks of design space.

That's all I got for today. If you enjoy this kind of breakdown (of a particular mechanic), let me know, and perhaps I'll do it again. In addition, let me know what mechanic you'd like to see me breakdown next.

Join me next week when I finally see what's in the cards, as far as *Scars* is concerned.

Until then, may you know the joy of pointing your card at a creature or player.

  

[![](http://media.wizards.com/images/magic/daily/features/FireAndLightning-Article-Banner_left.jpg)](https://web.archive.org/web/20101115000000/http://archive.wizards.com/Magic/TCG/ProductArticle.aspx?x=mtg/tcg/pdsfirelightning/productinfo)[![](http://media.wizards.com/images/magic/daily/features/FireAndLightning-Article-Banner_right.jpg)](https://web.archive.org/web/20101115000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/arcana/576)
---
id: pvbgzy0s
kind: article
lang: en
path: /en/articles/feature/2012/09-03-on-the-origin-of-scavenge-and-overload
title: On the Origin of Scavenge and Overload
published: '2012-09-03'
column_slug: feature
column: Feature
authors:
- slug: ken-nagle-1c7b6b00
  name: Ken Nagle
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
    lang_detected: en
    capture_id: 651434
    url: https://magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
    captured_at: '2022-10-13 19:53:53+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
    lang_detected: en
    capture_id: 651434
    url: https://magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
    captured_at: '2022-10-13 19:53:53+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
    lang_detected: en
    capture_id: 651434
    url: https://magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
    captured_at: '2022-10-13 19:53:53+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
    lang_detected: en
    capture_id: 651434
    url: https://magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
    captured_at: '2022-10-13 19:53:53+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: pvbgzy0s
  url: https://magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
  page_key: magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
  lang: en
  template: drupal
  captured_at: '2022-10-13 19:53:53+00'
  capture_id: 651434
  wayback_url: https://web.archive.org/web/20221013195353id_/https://magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
- document_id: pvbgzy0s
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/211a
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/feature/211a
  lang: en
  template: aspx
  captured_at: '2013-07-07 20:28:20+00'
  capture_id: 591170
  wayback_url: https://web.archive.org/web/20130707202820id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/feature/211a
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: pvbgzy0s
  capture_id: 651434
  url: https://magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
  wayback_url: https://web.archive.org/web/20221013195353id_/https://magic.wizards.com/en/articles/archive/feature/origin-scavenge-and-overload-2012-09-03
  captured_at: '2022-10-13 19:53:53+00'
  template: drupal
  sha256: e6160a3791025038f71fdef62337586bccca6a438a8f08950af3f44bd775907f
render_recovery: []
---
R*eturn to Ravnica* is nearly upon us! The hustle and bustle of the city, the scheming of a [dracogenius](http://media.wizards.com/images/magic/daily/features/feat211_hidden_jz3lvi45ha.jpg), and the first-pick mana-fixers are nostalgic reminders for those of us who experienced Ravnica the first time. *Return to Ravnica* marks my third set as a lead designer, after *Worldwake* and *New Phyrexia* (so it definitely includes a fatty or two). But before I spoil a fatty in the set, let's go behind the scenes and into The Pit, more than a year ago, for a look at the play-by-play process for two new mechanics I designed for *Return to Ravnica*: Golgari's scavenge and Izzet's overload.

As we explore Golgari's scavenge and Izzet's overload mechanics, I'll review their previous keywords; show you initial playtest cards we made during design for the new mechanics, with typos and all (we don't copyedit playtest cards, after all); explain how and why the new mechanics changed; and, lastly, show the finished cards with glorious artwork.

![](https://i.ormos.uk/ea/47/ea4706cf7995e6a98c4122152269ac2dde9d9b7f18e02619f7601f4b73988a6b.jpg)

Art by [Slawomir Maniak](https://web.archive.org/web/20120903000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Slawomir%20Maniak%22%5D)

### Return of the Golgari

The Golgari are the necromancers of Ravnica, viewing death as just another way to grow in strength. Their previous mechanic was dredge, which works from and fuels the graveyard, allowing you to draw the same card over and over:

![Shambling Shell](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Shambling+Shell)

  

A large graveyard is the Golgari player's best friend. Now that we are returning to Ravnica, we wanted to keep the Golgari's large graveyard but design a new mechanic that's less repetitive.

***Digestable* to Scavenge**

The first playtest at the new Golgari mechanic was called "*digestable*" (notice that typo I was telling you about? I should have spelled it with an "I"—digestible):

![](https://i.ormos.uk/8c/74/8c7475ca148142c592a498e949d8db458a85997ed9921f5e56542f33cc85a2a8.jpg)  

The flavor is that the dead Greater Rotwurm is tasty enough for one of your other creatures to gobble up its corpse and gain its size and powers for a while. I wrote the *digestable* keyword reminder text this way for versatility so any creature could use it. However, the Golgari's *digestable* mechanic doesn't require such a large design space in the set—meaning we don't need to make forty *digestable* cards; what we need is more like a dozen *digestable* cards. Remember, the Golgari mechanic, along with the nine other guilds' mechanics, all must fit in *Return to Ravnica* and *Gatecrash* evenly because, at its core, Ravnica's guild system gives all ten color pairs equal treatment.

Onto our second playtest with *digestable*. This time, it gained a cost parameter and the reminder text plainly spelled out what happens:

![](https://i.ormos.uk/e8/ba/e8ba6708e36e8460df2a873a7c5b7510d62cb9a054dff6f756037455e0ce22c4.jpg)  

While the mechanic playtested fine, it unfortunately felt too fleeting and transient. We wanted to try a more permanent bonus. Instead of +1/+1 until end of turn, we wanted to try a +1/+1 counter. I named this updated version of the mechanic scavenge. This scavenge playtest card features the largest mana cost I've ever put on a common (because it's a fatty):

![](https://i.ormos.uk/f1/56/f156314887f298a0de20765e1f0debe901e6654cc3300551d807a21eabab2de5.jpg)  

This updated version of the mechanic made it to print, name and all. For those of you who don't know, I designed the card Scavenging Ooze and the devour mechanic, both of which are from older sets—you might see the connection that I love when my creatures eat each other.

Here is the final version of the Digestable Scorpion:

![Sluiceway Scorpion](https://i.ormos.uk/6d/53/6d5379026d6da81c194717a98c15da84d748768bc12fb9222d9613070bbc58cb.jpg)  

Thanks to scavenge, Golgari plays as the "large creature" guild in *Return to Ravnica*, trading to survive early and taking over the late game with a large graveyard filled with scavenge-able corpses. So keep an eye out when you return to Ravnica, because the Golgari will be scavenging the dead rather than digesting them—and now you'll know why.

![](https://i.ormos.uk/28/ef/28ef6a82fd2a55e1ffe68a508a0f298f7099c8dd328fbb4c7dfebde3b2fc81a9.jpg)

Art by [Noah Bradley](https://web.archive.org/web/20120903000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Noah%20Bradley%22%5D)

### Return of the Izzet

The Izzet guild is composed of the mad scientists from the Ravnican [ecumonopolis](http://en.wikipedia.org/wiki/Ecumonopolis). Their shocks of white hair come from over-thinking plans and laboratory blunders. Mechanically, the Izzet are a spell-based guild utilizing instants and sorceries. Their original guild mechanic, replicate, showcases their penchant for squeezing all the juice they can from their spells:

![Leap of Flame](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Leap+of+Flame)

  

**Disperse to Overload**

We wanted the new Izzet mechanic to also be an instant- and sorcery-based mechanic. The first thing we tried was "dispersion," a mechanic I submitted way back during [The Great Designer Search #1](https://web.archive.org/web/20120903000000/https://magic.wizards.com/en/articles/archive/episode-1-%E2%80%93-beginning-2006-10-26). This dispersion mechanic concept allowed cards to go from targeting just one thing to targeting all things. [Here's a look at my submission](https://web.archive.org/web/20120903000000/https://magic.wizards.com/en/articles/archive/great-designer-search-episode-2-%E2%80%93-%E2%80%9Cgimme-five%E2%80%9D-2006-11-02):

> Dispersive Silence (Common)  
>  W  
>  Sorcery  
>  Destroy target enchantment.  
>  Dispersion 4W (When you play this card, if you also paid the dispersion cost, target all enchantments.)
> 
> Dispersive Mold (Common)  
>  G  
>  Sorcery  
>  Destroy target artifact.  
>  Dispersion 4G (When you play this card, if you also paid the dispersion cost, target all artifacts.)
> 
> Dispersive Blast (Common)  
>  R  
>  Sorcery  
>  Dispersive Blast deals 2 damage to target creature or player.  
>  Dispersion 4R (When you play this card, if you also paid the dispersion cost, target all creatures and players.)
> 
> Dispersive Path (Common)  
>  U  
>  Sorcery  
>  Target creature is unblockable this turn.  
>  Dispersion 5U (When you play this card, if you also paid the dispersion cost, target all creatures.)
> 
> Dispersive Revival (Common)  
>  B  
>  Sorcery  
>  Return target creature card in your graveyard to your hand.  
>  Dispersion 6B (When you play this card, if you also paid the dispersion cost, target all creature cards in your graveyard.)

This mechanic emulates the card [Radiate](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Radiate), a red rare from *Torment*:

![Radiate](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Radiate)

  

The basic paradigm is to take any kind of single-targeted red or blue spell and turn it into its global version. Those Izzet will juice any spell to the max. Single-target burn, bounce, pump, and destruction are poised to be overloaded! The keyword "dispersion" was later changed to the better name "overload" by our creative team.

Here is the initial playtest card of my favorite overload card during design:

![](https://i.ormos.uk/cf/80/cf80361bcc789944a8d0649a5cc0e4baee424b50adf6b7face991df0cc0dbac3.jpg)  

This playtest card spelled out dispersion using the initial wording of [Radiate](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Radiate), which was the most workable solution during the first attempt at design. (Note that [Radiate](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Radiate)'s initial rules text prior to printing was "Change all the 'target' in target spell to 'each'," which was my desire for the disperse mechanic throughout design. Thanks, Rules Manager [Matt Tabak](https://web.archive.org/web/20120903000000/http://archive.wizards.com/Magic/Magazine/Archive.aspx?author=Matt%20Tabak), for the cool "target becomes each" implementation.)

Over time, the actual implementation of dispersion and Volcanic Hammer Time changed. All these are very different cards:

![](https://i.ormos.uk/6f/16/6f164a1403b297f4bd0a9e0ed6f3d039cd1b846b6d4541b5df8b3ec995e6b3cf.jpg)  

<table><tbody><tr><td><div><div><img alt="Flame Slash" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Flame+Slash"></div></div></td><td><div><div><img alt="5150" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;multiverseid=5150"></div></div></td></tr></tbody></table>

While it's easiest for me to envision the dispersing "Deal 4 damage to *target* creature or player" into "Deal 4 damage to *each* creature and player," other dispersion cards were not so clear. **Magic** has more cards like [Steam Blast](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steam+Blast) than like [Flame Wave](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Wave), but players are happier casting [Flame Wave](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Wave)s over [Steam Blast](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Steam+Blast). A more subtle problem is that dispersion doesn't change "creature or player" to "creature and player," yielding an unintended version of [Slagstorm](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Slagstorm).

Like Volcanic Hammer Time, other dispersion cards were wading into upside, downside, or somewhere in between. Most every card in **Magic** does one of two things:

*   Something good for me (like "Target creature gains first strike until end of turn").
*   Something bad for my opponent (like "Target creature loses flying until end of turn").

However, if we disperse "*target* creature gains first strike until end of turn" into "*each* creature gains first strike until end of turn," the card doesn't provide a proper balance of something good for me or something bad for my opponent. Similarly, "*target* creature loses flying until end of turn" dispersing into "*each* creature loses flying until end of turn" isn't showcasing the mechanic very well either.

### Fancy Targeting FTW

Our solution:

*   Target creature **you control** gains first strike until end of turn.
*   Target creature **you don't control** loses flying until end of turn.

This tweak works as intended when dispersed as "Each creature you control gains first strike until end of turn" and "Each creature you don't control loses flying until end of turn." For unified implementation and all-upside purposes, every overload card uses "you control" or "you don't control."

Here is the final version of Volcanic Hammer Time that you'll open in booster packs:

![Mizzium Mortars](https://i.ormos.uk/47/b4/47b4fa26a987395f20ca7d9e927a8bd0857ff23c3044273b517c7d401bf4894e.jpg)  

When you return to Ravnica, have fun with the Izzet guild overloading your spells. Your [Flame Slash](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Slash) could be the next [Flame Wave](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flame+Wave).

![](https://i.ormos.uk/f9/93/f99320a1fa52ce128eb041babb540ec13f03192b281288d0ee3344d44f8ea770.jpg)  

### Ravnica's Smartest Being

It's time for the fatty spoiler I promised.

Are you excited to see the...

*   Returning character
*   mythic rare
*   Legendary
*   multicolor
*   Izzet
*   Dragon who
*   deals damage,
*   draws cards,
*   ...and draws cards while dealing damage?

Everyone make way for Niv-Mizzet, Dracogenius!

![Niv-Mizzet, Dracogenius](https://i.ormos.uk/d6/53/d653baf7128415b23f04afbb0a34ce3f67da5358ba1724087ca34c249f41cd54.jpg)  

This design is reminiscent of the original and beloved [Niv-Mizzet, the Firemind](https://web.archive.org/web/20120903000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Niv-Mizzet%2C+the+Firemind), with a trigger reversal. Instead of dealing damage when you draw cards, now you draw cards when you deal damage. Niv-Mizzet has also grown in fattiness over the years; he's more likely to attack this time around.

![](https://i.ormos.uk/b5/35/b535be4fe55e7c169cbc751ec964a9ad55faacd923338e2d82684c169ae78356.jpg)

Niv-Mizzet, Dracogenius | Art by [Todd Lockwood](https://web.archive.org/web/20120903000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=%5B%22Todd%20Lockwood%22%5D)

As an added bonus, I've hidden a playtest card of my design for Niv-Mizzet inside this article. Can you find the dracogenius?

I hope you enjoy *Return to Ravnica* with as much delight and passion as I did designing it with my design team. A huge thank you to development, editing, creative, and the artists for their work on *Return to Ravnica*. I'm looking forward to the upcoming Prerelease to hear what players have to say about their experience. Feel free to share your thoughts with me using my email link at the bottom of this page, the forum thread, or on social media (and I'll sign any cards you snail mail me).

So whenever and wherever you experience *Return to Ravnica*, have fun scavenging your creatures and overloading your spells while Niv-Mizzet, Dracogenius looks on with much aplomb.
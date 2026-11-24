---
id: fxay8efa
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/09-12-developing-khans-of-tarkir
title: Developing Khans of Tarkir
published: '2014-09-12'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
    lang_detected: en
    capture_id: 737604
    url: http://magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
    captured_at: '2016-05-08 05:13:52+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
    lang_detected: en
    capture_id: 737604
    url: http://magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
    captured_at: '2016-05-08 05:13:52+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
    lang_detected: en
    capture_id: 737604
    url: http://magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
    captured_at: '2016-05-08 05:13:52+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
    lang_detected: en
    capture_id: 737604
    url: http://magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
    captured_at: '2016-05-08 05:13:52+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: fxay8efa
  url: http://magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
  page_key: magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
  lang: en
  template: drupal
  captured_at: '2016-05-08 05:13:52+00'
  capture_id: 737604
  wayback_url: https://web.archive.org/web/20160508051352id_/http://magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: fxay8efa
  capture_id: 737604
  url: http://magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
  wayback_url: https://web.archive.org/web/20160508051352id_/http://magic.wizards.com/en/articles/archive/ld/developing-khans-tarkir-2014-09-12
  captured_at: '2016-05-08 05:13:52+00'
  template: drupal
  sha256: 3df534fbb660148b3693d0f6abfa9081d7f87d7866a84c5d725d3efa45f85cd4
render_recovery: []
---
As we have done for the last few sets, the entire set of *Khans of Tarkir* is now up on our [Card Image Gallery](https://web.archive.org/web/20140912000000/http://magic.wizards.com/node/263136) on the second Friday of preview weeks. We're going to be discussing the set as a whole, so it might be helpful to take a look through it if you haven't already.

*Khans of Tarkir* is probably the most complex set we have released in quite a long time, with the wedge cards, morph, and five clan keywords. It's a lot to take in, so give yourself some time to review the set before attending your [local Prerelease](https://web.archive.org/web/20140912000000/http://locator.wizards.com/)—you'll be glad you did.

# Introducing the Development Team

First, I'll start off with the developers on this team. It is customary to have all of the lead developers of each set in a block work on the first set. This helps to make sure that the block has some consistency of theme and gameplay.

![](http://media.wizards.com/images/magic/daily/ld/2014/askl67dfue_lauer.jpg)

**Erik Lauer:** Erik is the most experienced developer working on *Magic*, and the head developer—sort of the corollary to Mark Rosewater's head of design. His previous sets include *Magic 2010*, *Magic 2011*, *Mirrodin Besieged*, *Innistrad*, *Return to Ravnica*, and *Theros*. He's also leading next year's fall set—codenamed "Blood."

![](http://media.wizards.com/images/magic/daily/ld/2014/askl67dfue_humpherys.jpg)

**David Humpherys:** Dave is a Pro Tour Hall of Famer, the development manager, and also the lead of *Gatecrash*, *Avacyn Restored*, *Journey into Nyx*, and another set in this block. Of all of the developers, Dave probably was the biggest fan of morph, and played hundreds of drafts of *Onslaught*-Block Draft on *Magic Online*.

![](http://media.wizards.com/images/magic/daily/ld/2014/askl67dfue_lapille.jpg)

**Tom LaPille:** Although Tom has recently moved from development to working on *Magic Online*, he is still a valuable part of the *Magic* R&D team. Tom has been the lead of several sets—*Magic 2012*, *Dark Ascension*, and *Born of the Gods*, as well as an unannounced set in this very block.

![](http://media.wizards.com/images/magic/daily/ld/2014/askl67dfue_main.jpg)

**Shawn Main:** It's important that the development team have both a designer on it (to help design cards and carry over design's philosophy) as well as a member of the design team who can explain the team's decisions and make sure the set is keeping those intact. In this case, Shawn Main played both roles. Shawn, who came to work at Wizards from the [Great Designer Search 2](https://web.archive.org/web/20140912000000/http://archive.wizards.com/Magic/magazine/article.aspx?x=mtg/daily/feature/133), led the design of *Conspiracy*.

![](http://media.wizards.com/images/magic/daily/ld/2014/askl67dfue_beyer.jpg)

**Doug Beyer:** Doug also has some experience as a designer, having led the design of *Magic 2013*, but his main role is as a senior designer for *Magic*'s creative team. Basically, Doug is one of the people in charge of *Magic*'s story, and having him for the development of *Khans of Tarkir* made sure the set would meet the creative vision for both the world and the clans.

![](http://media.wizards.com/images/magic/daily/ld/2014/askl67dfue_prozak.jpg)

**Adam Prosak:** One of the newest additions to the development team, Adam began working on *Khans of Tarkir* as an intern, getting his feet wet and learning how we develop sets. Adam brought to the table a combination of high-level tournament experience as well as a love for goofy and wacky gameplay. It was great to get his opinions on the set when he started, since it gave us a good baseline for how our target demographic would react to some of the crazier things the set was trying to accomplish. Like, you know, the largest returning mechanic of the set.

# The Return of The Morph

One of design's big-picture plans for *Khans of Tarkir* block was the return of morph. It helped design tell a story it wanted to tell, and Mark Rosewater felt like this was a mechanic we could make some big improvements on.

![](http://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_pu8esg2v7s.png)

I'll just say that this wasn't the least-contentious decision I've seen in my time in R&D. Morph had many supporters and detractors in both design and development, and there was a long period of time where it was less than clear if morph would even make it into the set. Ultimately, though, Mark Rosewater's vision for the set won out, and morph was locked in. From then, it was all about trying to execute on the cards to the best of our ability, and to try and solve some of the harder points of morph, like the complexity and individual card designs.

Quite a bit of the late design period for Khans was actually spent trying out some changes of morph based on development's concerns that [Gray Ogre](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Ogre)s just weren't what they used to be. We spent a pretty good amount of time trying out morphs as colorless 2/2s for two and seeing how close that could get the cards. The problem was that it was far too powerful for Limited, and we found you would play almost any morphs in your pool just as [Grizzly Bears](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Grizzly+Bears). It wasn't helping out the three-colorness of the set as much as it was making people who stumbled lose. Playing off-color morphs wasn't a sign of a bad deck—the only question was how many you had to play to get your curve to work.

Eventually, we decided that despite being pretty weak bodies, the original stats on morph were the correct ones to go with. This meant we were going to have to adjust what the front of the cards and the morph costs were to get players to play cards in both states.

Perhaps the most successful version of this method were the three-color morphs in the set, where morph is used as a kind of mana fixing. You can either play a pretty powerful five- or six-drop creature that costs CDF, or you can play it on turn three face down and get a huge advantage out of flipping it up on turn five. But, if you didn't have the mana to actually cast the card, you could also just play it face down and get some action on the board while you tried to draw out of your mana problems. In terms of getting a three-color set to work, morph goes a long way toward smoothing out draws enough to keep the games from coming down too much to being color hosed.

![](http://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_cv7yxupc0r.png)

![](http://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_aczdfgkg8r.png)

When working on morph, development took a hard look at the two blocks where the ability had already shown up—*Onslaught* and *Time Spiral*. Lead Developer Erik Lauer knew what he didn't want was a highly contentious debate about blocking versus not blocking with cards like [Battering Craghorn](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battering+Craghorn) and [Skirk Commando](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skirk+Commando) at common. Beyond the most obvious reason of not wanting games to come down to the decision to block or not block on turn three or four, the actual decision on whether to block or not was just solved.

If you look at *Onslaught* block, it's painfully obvious even before [Zombie Cutthroat](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombie+Cutthroat) that blocking a morph on turn three was a horrible play. Just too many of the morphs turned face up and won in combat, and the saboteurs could always just be blocked the next turn. While the community had a lot of interesting debate about what the strategies were the first time, I believe the sheer number of games and the increased *Magic Online* presence would have quickly made these decisions uninteresting.

*Time Spiral* alone took a different approach to morph. If you look at the morphs, none of the commons or uncommons are able to simply eat an opposing blocking morph on turn four. Okay, you could flip up a [Fathom Seer](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fathom+Seer) with damage on the stack (back when damage used the stack), but that would probably lead to you discarding a few cards that turn if it was on turn three or four. What we wanted to allow was for was easy blocking decisions for the first two turns of morph, and to allow for the interesting decisions to come up when one or both players could use combat tricks to fight each other's morphs rather than just the cost of turning them face up. For that reason, none of the morphs in *Khans of Tarkir* will simply "eat" an opposing morph creature for less than five mana. They can trade, or bounce, but they won't be simply card advantage until turn five. It wasn't always easy to obey this rule, but I think the set works better as a whole for us having had the tenacity to stick to it.

# To Stack or Not to Stack

Once it was decided that morph would be in the set, and that the morphs would be three-mana 2/2s, the final question came down to how morph would work. Morph is unlike almost every other ability we have in modern *Magic* in that it doesn't use the stack. Turning up a creature with morph can't be responded to, which is pretty unintuitive. It works like that because...well, getting a three-mana 2/2 vanilla to be playable is pretty difficult, and making them even worse against [Shock](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) wasn't seen as an option in 2002. Also, creatures have increased quite a bit since 2002, so we had further worries about just how far morphs would be from Constructed. Still, we could get morphs into Constructed with individual designs—[Exalted Angel](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exalted+Angel) sure did it the first time—so the question we needed to ask ourselves was how to get the best experience for the most people when using the cards. And one part of that was determining if we should change turning a card face up from a special action to an activated ability.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Exalted%20Angel)](https://web.archive.org/web/20140912000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Exalted%20Angel)

![](http://media.wizards.com/images/magic/tcg/products/ktk/8arg43u984398yf/en_9d4z0ycdiu.png)

Matt Tabak put in quite a few hours of research and rules tweaking to try and get morph to work under the proposed rules set. The issue was that you had to reveal the morph to turn it face up, but then had to turn it right back down again and wait for the ability to resolve. A lot of people did the thing that felt natural, and left it face up with the ability resolved, but that was kind of misrepresenting the game state since the card was simply a vanilla 2/2 when it was face down. The comprehensive rules state that when revealing a card and putting an ability on the stack, the card should remain revealed until that ability finishes resolving. Which meant that what the cards wanted to do was somehow reveal themselves briefly to get a cost to the creature face up as a special action, then have a cost to turn themselves face up spliced onto the blank part of the card...which was about as unintuitive as you could possibly imagine. Making *Magic* cards ain't easy.

I don't envy Matt Tabak's job some days, and the period of working on morph was a good highlight to how complicated being the rules manager is. Let's just say I won't be putting my hat into that arena anytime soon. Fortunately for everyone involved, most of development found that while morph using the stack had some advantages in consistency for the game, it felt that the gameplay wasn't enough of an improvement to warrant changing the rules.

That's it for this week. Next week, I'll take us through *Khans of Tarkir* in Multiverse with another M Files article.

Until next time,  
 Sam ([@samstod](https://twitter.com/samstod))
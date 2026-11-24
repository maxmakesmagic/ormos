---
id: cnbbrpry
kind: article
lang: en
path: /en/articles/play-design/2017/12-15-play-design-and-digital-magic
title: Play Design and Digital Magic
published: '2017-12-15'
column_slug: play-design
column: Play Design
authors:
- slug: melissa-detora-b431380a
  name: Melissa DeTora
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
    lang_detected: en
    capture_id: 1140628
    url: https://magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
    captured_at: '2022-08-12 23:08:59+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
    lang_detected: en
    capture_id: 1140628
    url: https://magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
    captured_at: '2022-08-12 23:08:59+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
    lang_detected: en
    capture_id: 1140628
    url: https://magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
    captured_at: '2022-08-12 23:08:59+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
    lang_detected: en
    capture_id: 1140628
    url: https://magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
    captured_at: '2022-08-12 23:08:59+00'
    rule: url.article_section
sources:
- document_id: cnbbrpry
  url: https://magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
  page_key: magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
  lang: en
  template: drupal
  captured_at: '2022-08-12 23:08:59+00'
  capture_id: 1140628
  wayback_url: https://web.archive.org/web/20220812230859id_/https://magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: cnbbrpry
  capture_id: 1140628
  url: https://magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
  wayback_url: https://web.archive.org/web/20220812230859id_/https://magic.wizards.com/en/articles/archive/play-design/play-design-and-digital-magic-2017-12-15
  captured_at: '2022-08-12 23:08:59+00'
  template: drupal
  sha256: 30b0d2a22a27b5ac65498ea91f8af0f1eb3c05a7be23e2d42c538db9077d4a5a
render_recovery: []
---
Haven't yet signed up for the *MTG Arena* Closed Beta, or interested in seeing how the next digital *Magic* game is progressing? [Click here](https://web.archive.org/web/20171215000000/https://magic.wizards.com/en/mtgarena) to learn more!

Welcome back to Play Design. For the last article of the year before the holiday break, and in honor of *Magic: The Gathering Arena* moving into the Closed Beta phase, this week I'm going to talk about how digital *Magic*—including *MTG Arena* and *Magic Online*—affects how we design and develop cards.

These days, *Magic* R&D works closely with both the *MTG Arena* and *Magic Online* devs and lets them know of any new mechanics that might require new code or extra development time, or anything else unusual coming up. The reason for this is that the *Magic* rules are very complex, and sometimes cards either need to be changed or require extra work and time. However, this has not always been the case.

Years ago, R&D didn't work with digital much at all. They just made their sets and then would ship them off to the *Magic Online* dev team when they were finished. R&D didn't know it at the time, but this process sometimes caused nightmares for the MTGO developers. Many of the issues players experienced with *Magic Online* back in the day started because of this significant process issue. Some cards were very difficult to code, some new cards caused bugs with existing cards, and all of this was done under deadlines that were very hard on the team. The nail in the coffin was a *Born of the Gods* card, [Whims of the Fates](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates).

[Whims of the Fates](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) did something that no *Magic* card had ever done before it: separate cards into three piles. Two piles had been done plenty of times, but *Magic Online* had never had a card that split cards into three piles. When the dev team started coding the set at their normal start time, this one card caused a ton of extra work. After the set was released on MTGO, R&D received feedback from the dev team about [Whims of the Fates](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) and the issues it caused. The funny thing about it was that [Whims of the Fates](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) was nothing more than a casual card, not aimed at competitive play and not a strong Limited card. Its effect could have easily been changed to something else.

![Whims of the Fates](https://media.wizards.com/2016/images/daily/cardart_BNG_Whims-of-the-Fates.jpg)

[Whims of the Fates](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) | Art by [Seb McKinnon](https://web.archive.org/web/20171215000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Seb+McKinnon%22%5d)

After the [Whims of the Fates](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Whims+of+the+Fates) issue, *Magic* R&D began working with the digital team much earlier in the process. They even hired a team of people known as "*Magic Online* R&D," whose job was to recommend digital implementations for cards and mechanics. Allison Medwin is our *Magic Online* and *MTG Arena* liaison, and she works with both digital teams daily and reports back to the design teams about any cards or mechanics that may cause issues in digital.

# Play Design's Input

R&D has been working with the *MTG Arena* team closely since they started development. We've developed a system and a list of dos and don'ts when designing cards with digital in mind. Since the Play Design team develops cards for Limited and Standard, the most popular formats on MTGO, we always have to think about how things affect digital when making changes to cards. Here are some things we consider.

**Click Counts**

If you are a MTGO player and have been drafting *Iconic Masters*, you may have recently played a card with suspend. I bet you've never thought about everything you have to do to play that card. Add mana, click on the card, click to put the trigger on the stack every turn, click to resolve the trigger, click to remove the final counter, and finally click to cast the card. All that just to play a [Search for Tomorrow](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Search+for+Tomorrow). Each card requiring a high number of clicks increases gameplay time, causes confusion, and overall makes the game less fun to play.

Now consider what it takes to play a suspend card in paper. Tap lands, put the card on the table, put a die or coins on the card, move die or a coin each turn, resolve the spell. We are taking fewer physical actions and spending less time to play this card in paper, and that's something we take for granted when we think about how we play it in a digital platform. As members of the Play Design team, when we look through our card files and playtest in [Future Future League](/en/articles/play-design/2017/07-07-designing-hour-of-devastation-cards-to-meet-ffl-goals), we think about ways cards can reduce clicks and make gameplay more enjoyable in digital.

**Reducing Unnecessary Targeting**

There are a number of things we look for to reduce click counts. One is reducing the amount of targeting when possible. One card that is harder to play in digital *Magic* than in paper is [Blood Artist](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Artist). [Blood Artist](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Artist)'s triggered ability targets any player. In paper, this trigger is easy to resolve. When a creature dies, you tell your opponent to lose 1 life. On MTGO, it's very unlikely that you'll want to target yourself with it, but MTGO will ask you to click on a player anyway. Compare that to [Zulaport Cutthroat](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zulaport+Cutthroat). These cards are functionally different, but in one-on-one paper *Magic*, you'd resolve this card the same way you'd resolve a [Blood Artist](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Artist)—tell your opponent to lose 1 when a creature dies. However, in one-on-one digital *Magic*, there are a lot fewer clicks you have to go through to resolve a [Zulaport Cutthroat](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zulaport+Cutthroat) trigger than that of a [Blood Artist](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Artist).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Blood+Artist)](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood+Artist)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Zulaport+Cutthroat)](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zulaport+Cutthroat)

**Reducing Triggered Abilities** 

I've talked about the templating of [Adanto Vanguard](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adanto+Vanguard) in a [previous article](/en/articles/play-design/2017/10-13-the-m-files-ixalan-edition-part-1), and this template was the start of reducing unnecessary triggers to make digital *Magic* easier and more enjoyable to play. If [Adanto Vanguard](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adanto+Vanguard) were worded as follows, "When [Adanto Vanguard](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adanto+Vanguard) attacks, it gets +2/+0 until end of turn," this would cause a stop in digital *Magic* that both players must click through. Most of the time, players aren't going to respond to this trigger, so the card would slow down gameplay turn after turn. If the opponent does want to respond to the trigger, maybe with a [Last Breath](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Last+Breath) or another spell that you couldn't cast once the creature got the bonus, there are other opportunities to cast it, like in the beginning of combat step. Going forward, you'll see more creatures templated like this. Note that if the ability has a target, such as that of [Battle-Rattle Shaman](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle-Rattle+Shaman), we can't make the ability static.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Adanto+Vanguard)](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adanto+Vanguard)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Battle-Rattle+Shaman)](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle-Rattle+Shaman)

Another example is the *Amonkhet* card [Nest of Scarabs](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nest+of+Scarabs). Consider these two wordings:

*Whenever you put one or more -1/-1 counters on a creature, create that many 1/1 black Insect creature tokens.*

versus

*Whenever you put a -1/-1 counter on a creature, create a 1/1 black Insect creature token.*

Both of these templates function in the exact same way, but the second one causes a lot more separate triggers. In paper, these separate triggers are invisible to the players, but in digital, you're going to have to put each trigger on the stack and then resolve them all individually. For obvious reasons, we printed the card with the former wording, keeping digital in mind.

Another way we reduce triggers in *Magic* is by changing "you may" to "you must." If the ability is optional, it takes extra time to resolve. Not only do you have to choose yes or no, but if you don't want to use the ability, you still have to go through the motions by putting the ability on the stack and choosing targets, only to decline to use it, a problem that paper *Magic* doesn't have. "May" triggered abilities cause confusion for many players when playing in digital: "Why is it making me target? I don't even want to use it!"

While we consider the things I described above and much more, gameplay is more important to the Play Design team than making cards work better in digital. Although we consider our options, we don't always execute on them. I'm going to use [Battle-Rattle Shaman](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle-Rattle+Shaman) as our example. It reads:

*At the beginning of combat on your turn, you may have target creature get +2/+0 until end of turn.*

If we were making this card again, the digital teams may have recommended that we remove "you may" from it. However, that makes gameplay with this card functionally different. With a forced target, if you cast this on an empty board, the [Battle-Rattle Shaman](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle-Rattle+Shaman) will automatically become a 4/2 in combat. This opens it up to be killed by spells like [Reprisal](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reprisal) or [Smite the Monstrous](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smite+the+Monstrous). If these cards were in the same Limited format together, it would mean that if you wanted to cast this on an empty board and your opponent had untapped mana, it would be correct to move past your combat step and cast this on your second main phase.

![Battle-Rattle Shaman](https://media.wizards.com/2017/images/daily/cardart_IMA_Battle-Rattle-Shaman.jpg)

[Battle-Rattle Shaman](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Battle-Rattle+Shaman) | Art by [Warren Mahy](https://web.archive.org/web/20171215000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Warren+Mahy%22%5d)

If Battle-Rattle wasn't a "may," you could have this scenario:

"Cast Battle-Rattle 2.0, go."

"End of turn, [Smite the Monstrous](https://web.archive.org/web/20171215000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smite+the+Monstrous) it."

"But it's a 2/2."

"It triggered in combat."

"But . . ."

If we made this card a "must" trigger, players would be recommended to specifically announce their second main phase when casting the spell on an empty board, which wouldn't be an intuitive or natural line of play. We always look for ways to improve digital *Magic*, but we aren't going to make changes to cards that make gameplay worse.

*MTG Arena* just entered Closed Beta, and all readers of this column are encouraged to [sign up](https://web.archive.org/web/20171215000000/https://magic.wizards.com/en/mtgarena). We want as many eyes on it as possible and are looking for all kinds of feedback. If you're not already in the Closed Beta, it's not too late. More information is available at this [link](/en/articles/mtg-arena/2017/11-21-mtg-arena-closed-beta-starts-december-4). I'll be playing over the holiday break and I hope to see you there!

Thanks for reading and Happy Holidays.

See you in 2018,

Melissa DeTora  
[@MelissaDeTora](http://www.twitter.com/melissadetora)
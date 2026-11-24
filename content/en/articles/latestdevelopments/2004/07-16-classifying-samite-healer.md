---
id: 1qcpjr9y
kind: article
lang: en
path: /en/articles/latestdevelopments/2004/07-16-classifying-samite-healer
title: Classifying Samite Healer
published: '2004-07-16'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: aaronforsythe
  name: Aaron Forsythe
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
    lang_detected: en
    capture_id: 719647
    url: https://magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
    captured_at: '2022-08-19 05:22:40+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
    lang_detected: en
    capture_id: 719647
    url: https://magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
    captured_at: '2022-08-19 05:22:40+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
    lang_detected: en
    capture_id: 719647
    url: https://magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
    captured_at: '2022-08-19 05:22:40+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
    lang_detected: en
    capture_id: 719647
    url: https://magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
    captured_at: '2022-08-19 05:22:40+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
  duplicate_sources:
  - s3n7fx8v
sources:
- document_id: 1qcpjr9y
  url: https://magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
  page_key: magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
  lang: en
  template: drupal
  captured_at: '2022-08-19 05:22:40+00'
  capture_id: 719647
  wayback_url: https://web.archive.org/web/20220819052240id_/https://magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
- document_id: s3n7fx8v
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/af23
  page_key: wizards.com/default.asp?x=mtgcom/daily/af23
  lang: en
  template: classic_asp
  captured_at: '2005-03-23 09:28:36+00'
  capture_id: 1927905
  wayback_url: https://web.archive.org/web/20050323092836id_/http://www.wizards.com/default.asp?x=mtgcom/daily/af23
- document_id: s3n7fx8v
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af23
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/af23
  lang: en
  template: aspx
  captured_at: '2009-08-31 13:55:25+00'
  capture_id: 780706
  wayback_url: https://web.archive.org/web/20090831135525id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/af23
source_selection: Kept this article's selected capture and recorded the matching captures.
archive_source:
  document_id: 1qcpjr9y
  capture_id: 719647
  url: https://magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
  wayback_url: https://web.archive.org/web/20220819052240id_/https://magic.wizards.com/en/articles/archive/latest-developments/classifying-samite-healer-2004-07-16
  captured_at: '2022-08-19 05:22:40+00'
  template: drupal
  sha256: c57c531600051671bd4056308d267194b29e1e821a2f8600a035b14f64e06fc7
render_recovery: []
---
Recently I've been spending a good chunk of my time helping put [Ninth Edition](https://web.archive.org/web/20040716000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/selecting9e/home) together, and it has been a blast. I was working "upstairs" on the Web Team two years ago when *Eighth Edition* was being assembled; even though I wasn't on the 8E team I made a couple sound suggestions (like reminding R&D that [Phyrexian Plaguelord](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phyrexian+Plaguelord) and [Plow Under](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Plow+Under) were not, in fact, on the [Reserve List](https://web.archive.org/web/20040716000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magic/products/ReprintPolicy)). After that little taste of Core Set cobbling, I was anxious to have a hand in Ninth.

Choosing and testing cards has been fun so far, but, as with every **Magic** set, there are these little "issues" that need to be addressed.

Creature types have long been a problem with the Core Set. With some cards, the lack of consistency is a problem: [Savannah Lions](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Savannah+Lions) is a Lion, whereas every new lion-like creature we've made is a Cat. Some cards have really random types that don't make a whole lot of sense and are unsupported: [Nekrataal](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nekrataal) is a Nekrataal and [Sage of Lat-Nam](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sage+of+Lat-Nam) is a Sage. But the issue that bugs me most right now is that of race-class.

For background: Randy Buehler wrote a pair of articles before *Mirrodin* came out about the possibility of adding the creature type Human to the game, to allow a more intuitive conventional method of giving types to sentient creatures. After all, why was [Aven Flock](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aven+Flock) a Bird Soldier and [Catapult Squad](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Catapult+Squad) just a Soldier? His articles, "[Debating Humantiy](https://web.archive.org/web/20040716000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb47)" and "[Human Nature](https://web.archive.org/web/20040716000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb48)" were testing the waters for the potential introduction of the type, and as you now know, we decided to pull the trigger and go forward with it in *Mirrodin*.

Randy ended his second column on the topic with this cryptic sentence: "We would not mess with the creature types of old cards except possibly when we reprint them." Well, with *Ninth Edition* in the works, it's time to reprint some cards.

### Two of a Kind?

Here's a sneak preview of two cards that are most likely going to be in the next Core Set:

<table><tbody><tr><td>&#10;			<div>&#10;			<div><img alt="samite healer" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=samite+healer"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Thought Courier" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Thought+Courier"></div>&#10;			</div>&#10;			</td>&#10;		</tr></tbody></table>

On the left, we have [Samite Healer](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Samite+Healer). "Sammy" is a Core Set stalwart, having been in every single one. He's a nice clean card with lots of history, and he's achieved "icon" status--many players refer to the ability to tap to prevent a point of damage as "Samite Healer," regardless of what card it's on. His creature type is simply Cleric, which is what's it has been since the beginning.

On the right is [Thought Courier](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thought+Courier) from *Fifth Dawn*. The card was created as a replacement for [Merfolk Looter](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Looter) once we decided to phase the Merfolk type out. Because he was made post-*Mirrodin*, his creature type follows the race-class model: Human Wizard.

Now, regardless of which method of "typing" you prefer, you have to admit that it's a little weird that they're different, especially considering that the Core Set's primary purpose is to teach new players the game. What kind of message do we send to people learning the game by having only a very small percentage of the creatures that are obviously humans actually have the type "Human"?

### What Can We Do?

The big question in my mind is, "What are we supposed to do about it?" I honestly don't know. It keeps me up at night.

There are three things we could do, in my opinion.

**1) Leave it alone and have the Core Set be an inconsistent mess of creature types for all time.**

That seems bad to me for obvious reasons. That decision weakens the set as a teaching tool, and the whole set starts to feel random and sloppy once you start paying attention to types.

**2) Make new versions of old cards and slide them into the Core Set.**

We made a new [Merfolk Looter](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Merfolk+Looter) because we no longer support merfolk. Does that mean we should make a new [Samite Healer](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Samite+Healer) just so it could have the type Human Cleric? We are talking about a lot of cards here. I'm not sure we'd want to clutter up expert-level expansions over the next few years with remakes of [Samite Healer](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Samite+Healer), [Crossbow Infantry](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crossbow+Infantry), [Fugitive Wizard](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fugitive+Wizard), [Venerable Monk](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venerable+Monk), and every other card that should have the Human type just for the Core Set. Plus we'd be throwing out all the history and nostalgia associated with those old cards, which is no small loss in my opinion. Plus, this fix would not be implemented in time for Ninth.

**3) Errata the cards.**

We could just say that [Samite Healer](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Samite+Healer) is a Human Cleric and print him that way in Ninth. Errata is bad times, though, as it causes confusing situations for people that play with older versions of cards. And this errata would affect lots of cards. Just looking at *Eighth Edition* white commons, there are seven cards that would need such errata ([Samite Healer](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Samite+Healer), [Venerable Monk](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Venerable+Monk), [Honor Guard](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Honor+Guard), [Master Decoy](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+Decoy), [Standing Troops](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Standing+Troops), [Crossbow Infantry](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crossbow+Infantry), and [Glory Seeker](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glory+Seeker)) plus [Eager Cadet](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eager+Cadet) in the Starter game.

Would we then also need to errata non-Human cards that are not race-class compilant? Should [Raging Goblin](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Raging+Goblin) be a Goblin Berserker? [Elvish Piper](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Elvish+Piper) an Elf Bard?

And what about old cards we aren't reprinting? If [Samite Healer](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Samite+Healer) is a Human Cleric, why wouldn't [Clergy en-Vec](https://web.archive.org/web/20040716000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clergy+en-Vec) and Femeref Healer be as well? They're the exact same card.

One bit of data that is swaying my opinion towards updating the cards we reprint is the results from a poll Mark Rosewater ran a while ago. In his article "[Getting in the Game](https://web.archive.org/web/20040716000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr48)" it was reported that almost 70% of his readers were in favor of updating old creature types with errata. I'm still not sure that's the best answer, and there are others in the department that want nothing to do with such changes.

The results of this poll come with no promises attached, but I'm sure they'll spark many hours of arguments here. If you have any better ideas than those I've listed, drop me a line by using the email link below.

In the meantime, continue participating in [Selecting Ninth Edition](https://web.archive.org/web/20040716000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/selecting9e/home). We have some saucy votes on the way!

### Last Week's Poll

<table><thead><tr><th colspan="3">Do you like the idea of cards designed to match art?</th>&#10;		</tr></thead><tbody><tr><td>Yes</td>&#10;			<td>9527</td>&#10;			<td>82.9%</td>&#10;		</tr><tr><td>No</td>&#10;			<td>1963</td>&#10;			<td>17.1%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>11490</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

I agree, actually. I believe that everyone involved in **Magic's** creative process deserves some degree of freedom. Our next block certainly bears that out!
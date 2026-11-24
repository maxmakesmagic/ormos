---
id: 0656k9g7
kind: article
lang: en
path: /en/articles/makingmagic/2016/07-04-over-the-moon-part-2
title: Over the Moon, Part 2
published: '2016-07-04'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
    lang_detected: en
    capture_id: 228117
    url: https://magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
    captured_at: '2024-05-18 03:00:31+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
    lang_detected: en
    capture_id: 228117
    url: https://magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
    captured_at: '2024-05-18 03:00:31+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
    lang_detected: en
    capture_id: 228117
    url: https://magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
    captured_at: '2024-05-18 03:00:31+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
    lang_detected: en
    capture_id: 228117
    url: https://magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
    captured_at: '2024-05-18 03:00:31+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 0656k9g7
  url: https://magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
  page_key: magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
  lang: en
  template: contentful
  captured_at: '2024-05-18 03:00:31+00'
  capture_id: 228117
  wayback_url: https://web.archive.org/web/20240518030031id_/https://magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
- document_id: 0656k9g7
  url: https://magic.wizards.com/en/articles/archive/making-magic/over-moon-part-2-2016-07-04
  page_key: magic.wizards.com/en/articles/archive/making-magic/over-moon-part-2-2016-07-04
  lang: en
  template: drupal
  captured_at: '2022-08-30 23:52:59+00'
  capture_id: 903682
  wayback_url: https://web.archive.org/web/20220830235259id_/https://magic.wizards.com/en/articles/archive/making-magic/over-moon-part-2-2016-07-04
- document_id: 0656k9g7
  url: http://magic.wizards.com/en/node/1032706
  page_key: magic.wizards.com/en/node/1032706
  lang: en
  template: drupal
  captured_at: '2016-07-11 06:38:35+00'
  capture_id: 2478569
  wayback_url: https://web.archive.org/web/20160711063835id_/http://magic.wizards.com/en/node/1032706
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 0656k9g7
  capture_id: 228117
  url: https://magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
  wayback_url: https://web.archive.org/web/20240518030031id_/https://magic.wizards.com/en/news/making-magic/over-moon-part-2-2016-07-04
  captured_at: '2024-05-18 03:00:31+00'
  template: contentful
  sha256: 9b9c52d8bb047a8525098ec8a9cf8e7d8724c81e5f84bf193646368efccb35d5
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - an email
  occurrences: 1
---
Welcome to the second *Eldritch Moon* Preview Week. [Last week](/en/articles/makingmagic/2016/06-27-over-the-moon-part-1), I talked about the new meld cards (the double-faced cards that transform into a card made up of two different cards—go check out last week's article if you don't know what I'm talking about). There was a lot of history behind the creation of the meld cards, so I used all of my column (other than the part where I introduced the design team) to talk about how meld came to be. *Eldritch Moon* has a lot of other things going on in it, though, so today I'm going to talk about the many other cool things in the set. I even have a new preview card, something that certain players have been wanting for a long time. (No, not the legendary Werewolf, [we previewed that last week](https://twitter.com/wizards_magic/status/744984664117485568).) Since I have a lot to talk about, let's get to it.

# To the *Moon* and Back

To understand what choices were made in *Eldritch* *Moon*'s design and development (I should note that both new mechanics I'm going to be talking about today were created during development), we first have to take a step back and look at what the set was responsible for.

*Shadows over Innistrad* found our protagonist, Jace, showing up on Innistrad in search of Sorin. He quickly realized that something was wrong with Innistrad—many of the denizens were going mad and slowly changing due to some unseen influence—and set out to solve the mystery of what was happening. With help of Tamiyo's journal and eventually Tamiyo herself, Jace came to believe that the cause of the madness was the angel Avacyn. Jace and Tamiyo were unable to defeat Avacyn, but Sorin showed up at the last minute and, with great regret, unmade his angelic creation. It turns out, though, that Avacyn was not only not the problem—she was, in fact, the one thing protecting Innistrad. And with her out of the way, something truly sinister was making its way to the plane.

That something sinister was Emrakul, who was drawn to Innistrad by Nahiri in her plan to get revenge on Sorin and his home plane. *Eldritch Moon* had to show the influence of what happens when Emrakul finally arrives. This was going to be tricky because the last block, *Battle for Zendikar*, had gone full throttle with the Eldrazi and we wanted to do something different.

To do that, we had a few rules:

1.  **Limit the number of colorless Eldrazi cards**—Obviously Emrakul would be colorless, and we could afford a few others, but we didn't want the as-fan of the set to be too high with colorless creatures. Innistrad is about Gothic horror; we didn't want the influence of Emrakul to overshadow that.
2.  **No devoid cards**—Devoid was a necessary byproduct of needing to have enough Eldrazi to feel as if they were dominant on the plane of Zendikar and that there was a real fight to be had by the Zendikari to win back their plane. If our goal was to not feel like a repeat of *Battle for Zendikar*, that meant we couldn't use the same tools. Therefore, the devoid cards were off limits as an answer.
3.  **Don't make colorless mana too much of a thing**—Just as we didn't want to use devoid, we didn't want the set to be too much about colorless/generic mana costs. *Eldritch Moon* needed to have a near-normal amount of color in it.
4.  **Show Innistrad mutated, not just Eldrazi**—The influence of Emrakul was not that she made a bunch of new Eldrazi, but rather that she mutated the creatures of Innistrad. The set had to demonstrate this.

Solving the puzzle of *Eldritch Moon*'s design was figuring out how to do what we needed to do while following the above rules. The first place we looked was double-faced cards. They had two big advantages. First, they had transformation built into their flavor, so they could do a good job of showing mutation. Second, they were something unique to Innistrad (fine, *Magic Origins* had five, but both Zendikar blocks had zero).

The theme of double-faced cards on Innistrad has always been what we called "dark transformation." The front side (usually) shows a more benign creature, and the back shows the darker version of it once it's been transformed. One way we could show the horror of Emrakul's presence was to start the double-faced cards on the "monster" side and then have their transformed side be a mutated version. See, things have gotten so bad that the benign front side is the *monster*.

![](http://media.wizards.com/2016/ouhtebrpjwxcnw5_EMN/en_R9ggIQ0tFc.png)

![](http://media.wizards.com/2016/ouhtebrpjwxcnw5_EMN/en_JsT3QOlaAQ.png)

This meant that the front side would be things we've seen before on Innistrad (and thus colored—artifacts and lands being the only exceptions), and the back would be colorless. Once mutated, the creature starts taking on Eldrazi attributes, which we could reinforce with the colorless Eldrazi frame. This also helped with rule number one, as it meant that most of the cards in your deck (assuming you play the front side face-up) would be colored.

This, of course, required us to change the symbols on the cards. Instead of a sun on the front and a crescent moon on the back, the fronts now have a full moon and the backs have an Eldrazi symbol. One double-faced card did keep the old sun/moon symbols, Ulrich of the Krallenhorde, the legendary Werewolf, but that's a story for my card-by-card article. (It's a good story.)

Most of our double-faced designs were very straightforward. Show an Innistrad thing on the front and then see the mutated, Eldrazified version on the back. Werewolves were a bit more problematic. In *Innistrad*, *Dark Ascension*, and *Shadows over Innistrad*, Werewolves all functioned exactly the same, with one condition to transform them from the sun side to the moon side and a different condition to transform them back.

We decided that we would start all Werewolves in their lupine form, and then have them transform into an Eldrazi version of a Werewolf. Neither of the previous transformation triggers seemed appropriate, so we opted to give them mana activations to transform them. This had the secondary advantage of working well with the other Werewolves, because it allows you to spend your mana in a way that will make your non–*Eldritch Moon* Werewolves turn to the Werewolf side. We chose with the Werewolves as well as all the double-faced mutations to make the transformation one-way. Once Emrakul has transformed you, there's no going back.

![](http://media.wizards.com/2016/ouhtebrpjwxcnw5_EMN/en_NnjsUYnaVy.png "")

![](http://media.wizards.com/2016/ouhtebrpjwxcnw5_EMN/en_fWg8kxUiHI.png "")

# A New Mechanic Emerges

The double-faced cards got us some colorless cards while still keeping the as-fan of colorless permanents down. We made an Emrakul card and tried a few other colorless Eldrazi. In the end, only Emrakul and one other true colorless Eldrazi, Eternal Scourge, stayed in the set.

It was also decided that we could use our tokens as a place to have colorless creatures. This allowed us to up the colorless creatures on the battlefield without having your hand filled with colorless cards. Neither the 0/1 Spawn of *Rise of the Eldrazi* nor the 1/1 Scions of *Battle for Zendikar* block worked well in the *Shadows over Innistrad* environment. It just wasn't about ramping into spells. After trying different combinations, development ended up making the token a 3/2 colorless creature. We called it an Eldrazi Horror, and it was used to represent what things mutated into.

![](http://media.wizards.com/2016/ouhtebrpjwxcnw5_EMN/en_r0E8h7Sx7s.png)

It was clear though that we were still missing something. If Emrakul's presence was a big part of the set, we wanted to have a mechanic that reflected it. But rules two and three put a lot of restrictions on what that mechanic could be. The cards needed to have a veneer of Eldrazi to them without circumventing the color pie. We didn't want every color to use every card with this mechanic. The inspiration to solve this problem turned out to be Ninjas.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ink-Eyes%2C+Servant+of+Oni)](https://web.archive.org/web/20160704000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ink-Eyes%2C+Servant+of+Oni)

More technically, the ninjutsu mechanic from *Betrayers of Kamigawa*. I designed ninjutsu as a mechanic to reflect the sneakiness of Ninjas. They're tricky masters of disguise (using magic, not an elephant suit, which was a popular joke at the time) such that you don't often see them coming when they attack. Sam Stoddard, the lead developer for *Eldritch Moon*, is a big fan of ninjutsu and thought that maybe it might hold the key to a solution. The new mechanic was called "emerge."

The first change he made was to add a sacrifice cost to the ability. (Ninjutsu, in contrast, returned the creature to your hand.) This gave it a bit of an *Alien* chestburster feel, that the mutated creature came forth out of the original creature. Originally, emerge worked like ninjutsu, as you could only use it on an attacking creature—but that ended up being a little too limiting. It was changed so that you could use the activation any time you could cast the creature.

The colored activation was the key to solving the "no devoid" problem. Each creature with emerge is colorless, but can be cast for one less total mana if you use colored mana and a sacrifice. This makes the cards playable in any deck but preferable in the proper color. The emerge ability only shows up in blue, black, and green.

# Time to Escalate the Issue

While Emrakul's influence is a big deal in *Eldritch Moon*, it's not the only thing the set had to convey. The Gatewatch have shown up to save the day, only to realize that they're not equipped to do so. They need help, and that means turning to an unlikely ally: Liliana. It just so happens that the only creatures unaffected by Emrakul are the Zombies, and guess which necromancer just happens to be on the plane?

The set needed a mechanic that reflected the unlikely alliances that come together to defeat Emrakul. This mechanic was interestingly also influenced by a mechanic I made many years ago, this time from original *Mirrodin* block.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=370432)](https://web.archive.org/web/20160704000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=370432)

I'm talking about entwine (the mechanic I explained [two weeks ago](/en/articles/makingmagic/2016/06-20-25-more-random-things-about-magic) that I literally dreamed up). Sam took entwine and mixed it with a combination of Charms and Commands. You most often get three options (a handful give you two), and you have the ability to pay extra to get not only the second option but also the third.

Escalate started out just showing up in white and black, with the escalate cost being the opposite color, but that execution ended up being too narrow. The development team changed the escalate costs to something the color could already pay (sometimes with color, sometimes with generic mana) and put the mechanic in three colors, adding red to white and black. Escalate also added a needed mana sink element to the set and a new tool for Standard to play with.

# Coming Back for More

I've talked about the new mechanics but haven't addressed the old mechanics (well, "old" as far as *Shadows over Innistrad block* goes). Let's walk through each.

**Double-Faced Cards**

This is the one I mostly covered last week and above. Double-faced cards shifted from "dark transformation" with sun/crescent moon symbols to "dark mutation" with a full moon/Eldrazi symbols. Three pairs of double-faced cards transform into the meld cards.

**Investigate**

The clue-gathering part of the story was over and the set needed to clear some space to make room for the new mechanics, so investigate was dropped.

**Madness**

Madness didn't change much. It stayed in the same colors (black and red) and was still tied heavily to the Vampires. Mostly, design and development just made new cards with the mechanic.

**Delirium**

In *Shadows over Innistrad*, design and development stayed away from having much power/toughness shifting, as it felt too close to what the double-faced cards were doing. With the double-faced cards moving to a new space, it was decided that delirium could move into their old space, so most delirium cards have the creatures growing as they become delirious. This also helps play into the theme of mutation.

**Tribal**

The five tribes (Humans, Spirits, Vampires, Werewolves, and Zombies) all remain and are all still in the same ally-color pairs. Werewolves, as mentioned above, change the most mechanically. We did work to make sure that we rounded out the various tribes to help them have a chance at seeing Constructed play.

**Color Pairs**

The ten two-color pairs for drafting all stayed mostly the same, with one exception. In *Shadows over Innistrad,* green-blue was focused on making investigate matter. For *Eldritch* *Moon*, green-blue interacts with the emerge mechanic.

# Preview from Your Seat

One last thing before I call it a day and wrap up my column. I have a preview card to show you! This is one I handpicked because it is something that players have been bothering me to make for a *long* time. Ever since Commander became a popular format, players write to me whenever there's a creature type they want to make a deck around that doesn't yet have a commander. The number one request I get is for a legendary Bear, but today's preview is my number two request.

So what is it? Go ahead and take a guess.

## Give up?

![](http://media.wizards.com/2016/ouhtebrpjwxcnw5_EMN/en_sbzUF2sxWO.png)

Yes, we've finally made a legendary Spider. I'm surprised it took us this long. Note that we gave it a black activation to make its color identity black-green, as that's usually what players ask for. (How can you not put [Spider Spawning](https://web.archive.org/web/20160704000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spider+Spawning) in your Spider deck?) The card makes Spider tokens and has Spider tribal, so you're welcome, Spider-loving Commander players.

# The Setting *Moon*

That, in two columns, is the story behind the design of *Eldritch Moon*. There was a lot to cover and I'm proud of the work the design and development teams did. Hopefully, you all will have a chance to play with it soon. As always, I'm eager to hear about your thoughts on the set and/or today's column. You can drop me an email or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Google+](https://plus.google.com/107824009487778543249/posts), and [Instagram](http://instagram.com/mtgmaro)).

Join me next week for some card-by-card design stories from *Eldritch Moon*.

Until then, may you get a chance to emerge *and* escalate.

* * *

**"Drive to Work #344—*Urza's Saga*, Part 4"**

This is the fourth and final podcast of my four-part series on the design of *Urza's Saga*.

**"Drive to Work #345—Twenty Lessons: Resonance"**

This is the third part of my 20-part series "Twenty Lessons, Twenty Podcasts" where I cover the 20 lessons from my speech "Twenty Years, Twenty Lessons," which covered what I've learned working on the same game for 20 years. (You can read my three-part article [here](/en/articles/makingmagic/2016/05-30-twenty-years-twenty-lessonspart-1), [here](/en/articles/makingmagic/2016/06-06-twenty-years-twenty-lessonspart-2), and [here](/en/articles/makingmagic/2016/06-13-twenty-years-twenty-lessonspart-3).)

*   [**Episode 345**](http://media.wizards.com/2016/podcasts/magic/drivetowork345_20lessons_resonance.mp3) Twenty Lessons: Resonance (15.4 MB)
*   [**Episode 344**](http://media.wizards.com/2016/podcasts/magic/drivetowork344_urzassagapart4.mp3) *Urza's Saga*, Part 4 (24.9 MB)
*   **[Episode 343](http://media.wizards.com/2016/podcasts/magic/drivetowork343_urzassagapart3.mp3)** *Urza's Saga*, Part 3 (16.7 MB)
*   **[Episode 342](http://media.wizards.com/2016/podcasts/magic/drivetowork342_urzassagapart2.mp3)** *Urza's Saga*, Part 2 (15.7 MB)
*   [**Episode 341**](http://media.wizards.com/2016/podcasts/magic/drivetowork341_urzassagapart1.mp3) *Urza's Saga*, Part 1 (17.7 MB)

*   **[Complete Drive to Work Podcast Archive](/en/articles/media/undated/podcasts-media-articles)**
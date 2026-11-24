---
id: gvkq4z0n
kind: article
lang: en
path: /en/articles/latestdevelopments/2012/02-03-a-planes-walk-through-the-multiverse
title: A (Planes?)Walk Through the Multiverse
published: '2012-02-03'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: zac-hill-263da3f4
  name: Zac Hill
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
    lang_detected: en
    capture_id: 729521
    url: https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
    captured_at: '2022-10-02 00:15:23+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
    lang_detected: en
    capture_id: 729521
    url: https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
    captured_at: '2022-10-02 00:15:23+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
    lang_detected: en
    capture_id: 729521
    url: https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
    captured_at: '2022-10-02 00:15:23+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
    lang_detected: en
    capture_id: 729521
    url: https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
    captured_at: '2022-10-02 00:15:23+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: gvkq4z0n
  url: https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
  page_key: magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
  lang: en
  template: drupal
  captured_at: '2022-10-02 00:15:23+00'
  capture_id: 729521
  wayback_url: https://web.archive.org/web/20221002001523id_/https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
- document_id: gvkq4z0n
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/180
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/180
  lang: en
  template: aspx
  captured_at: '2013-07-01 07:59:21+00'
  capture_id: 614945
  wayback_url: https://web.archive.org/web/20130701075921id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/180
- document_id: gvkq4z0n
  url: https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-02
  page_key: magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-02
  lang: en
  template: drupal
  captured_at: '2022-06-30 03:44:45+00'
  capture_id: 729520
  wayback_url: https://web.archive.org/web/20220630034445id_/https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-02
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: gvkq4z0n
  capture_id: 729521
  url: https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
  wayback_url: https://web.archive.org/web/20221002001523id_/https://magic.wizards.com/en/articles/archive/latest-developments/planeswalk-through-multiverse-2012-02-03
  captured_at: '2022-10-02 00:15:23+00'
  template: drupal
  sha256: 7fdf6ceec21f2cee8a3fd6b7e929d25405887772456daf988a90f5c5658d1553
render_recovery: []
---
Hey, y'all! I hope you've had a chance to play with *Dark Ascension* by now. If you went to a Prerelease, I hope you cracked some bombs, smashed some faces, and had a blast.

In honor of the set's public unveiling, I figured I'd give you a peek behind the curtain into some of DKA's Multiverse R&D back-and-forth. For those of you who haven't seen an article like this before, Multiverse is the cross-departmental database we use to keep track of our cards. It ensures that design, development, creative, and editing are all on the same page, and also allows us to track a set's progress across different stages of its evolution. While most of the work on a set happens offline in meetings and playtests, Multiverse serves as a useful space for card-specific comments that people know developers will see. Occasionally, it's also a place to poke a little bit of fun at someone or something, as you'll certainly notice by the end of this article.

Everyone with access to Multiverse can leave comments in the file. As such, we tend to gather a lot of input. To save space, we avoid writing out our full name in the "comments" section. In order for these comments to make sense, though, I've compiled a bit of a dossier for y'all so you can figure out who's who:

![](https://i.ormos.uk/2c/11/2c11e3c83c00b431c9ce63bd3fec77756dcb56c64267c66df8a0bdfce240983d.jpg)

**Tabak:** Matt Tabak, **Magic** editor, designer, developer, and resident giant.

![](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg)

**EVL:** Erik Lauer, deck builder extraordinaire and *de facto* head developer. Note that his middle name doesn't actually begin with "V." In fact, he doesn't have a middle name. But he likes that he gets to cackle because his name sort of looks like "evil." This is a 100% true story.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_dellaugel.jpg)

**Del:** Del Laugel, **Magic**'s senior editor. Probably has the highest ratio of "unbelievably important skillset vital for **Magic**'s health" to "visibility" in all of R&D. It's unclear how any of us function on the days when she's not in the office.

![](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg)

**MR:** Mark Rosewater, **Magic**'s head designer. Have you heard he wrote for *Roseanne*? Learn more by following his Twitter account, [@maro254](http://twitter.com/maro254)!

![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg)

**TML:** *Dark Ascension* Lead Developer Tom LaPille, who used to write this column.

![](https://i.ormos.uk/cc/88/cc886ad1801d000e9f8ccad3e73a31d571306e9ce45cdc656ac198f23d06f9f0.jpg)

**AF:** **Magic** R&D director and lord of all Commander griefers, Aaron Forsythe.

![](https://i.ormos.uk/b4/9a/b49a97d847733a73985c5d85979f9c0df999dfc0380369be66282a7035d6c565.jpg)

**MJ:** Mons Johnson, **Magic**/**Duel Masters** designer/developer/playtester and leader of [Goblin Raiders](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mons%27s+Goblin+Raider) everywhere.

![](https://i.ormos.uk/ef/72/ef720e25ac1b4ff1389d81c9977841b7deca7e5cf8d15df7528af1b3635b7ad0.jpg)

**DH:** **Magic** Hall of Famer Dave Humpherys, development manager, my boss, and all-around swell gentleman.

![](https://i.ormos.uk/71/7e/717ec8ea013fe26416594283aa203c8c086fe7db5bfeb02641f7c432994f20bb.jpg)

**EEF:** Great Designer Search 2 winner Ethan "The Butcher" Fleischer. He is good at everything. It's disgusting.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_max.jpg)

**Max:** **Magic** digital developer Max McCall, one of **Magic** R&D’s newest full-time hires and semi-professional curmudgeon. Probably has less fun utterly annihilating opponents with broken decks than anyone on Earth. Is the oldest member of R&D, clocking in at ninety-one years of age, but somehow possesses the nimble body and mind of a twenty-three-year-old. Don't be fooled, though. The speakeasy clothes and radio-villain voice are a dead giveaway: "He's coming around on the inside, see."

![](https://i.ormos.uk/73/dc/73dc2c209bef80978eea09781f3075d348fa6472480299108af0945ff889dce7.jpg)

**KEN:** Great Designer Search 1 finalist Ken Nagle. Lover of the fatties. Guru of kickboxing. [Squelch](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Squelch)er of fun.

![](https://i.ormos.uk/98/ff/98ff84c36158a8091193fe55e8d3028e6e766bb343fd8e5051e08a78fcb62548.jpg)

**ZH:** Some idiot. Poor guy.

Without further ado:

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card09a.jpg)

> Tabak 5/9: Meow.

This is a classic example of the immense profundity and carefully thought-through analysis that the dedicated members of **Magic** R&D put into every single card we create. We strive to inspire faith in our impassioned commitment to making this game great.

Also we make cat noises.

Incidentally, [Sanctuary Cat](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sanctuary+Cat) has dethroned the mighty [Might of Oaks](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Might+of+Oaks) for the hotly-contested title of **Magic** Developer Zac Hill's favorite **Magic** card. I'm now collecting as many unique versions of this guy as I can find.

"Why are you a 1/2? Heavily armed soldiers with swords and shields are mere 1/1s."

"...rreow!."

"But I don't understand! Is your hide magically reinforced? By virtue of living in the sanctuary, do you enjoy the divine blessings of Innistrad's mighty angelic protector Avacyn? What gives?"

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_cat.jpg)

"...purrrrrrrrrr..."

::[Sanctuary Cat](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sanctuary+Cat) walks over to Zach and nuzzles his face cutely, alleviating all concern::

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card05a.jpg)

> TML 1/13/2011: This isn't doing it quite right. We want incidental human-punishing, not pinpoint. I think?
> 
> DH 1/13/11: Prefer things specifically good at smashing humans not good at punishing players with humans.
> 
> TML 2/11/2011: I have grown to like this card, but I want it to let you gain life instead of punishing the opponent.
> 
> TML 2/15/2011: Now only one B in the cost.
> 
> TML 3/5/2011: Decided to go back on that.
> 
> TML 3/24/2011: To 4BB for Bill Rose.
> 
> TML 3/30/2011: I will change this in the stickers today.
> 
> TML 4/8/2011: Need better removal. 3BB.

One of the things that was most amazing to me when I arrived in R&D is exactly how much thought goes into what might seem to be basic, run-of-the-mill Limited commons and uncommons. This thread exemplifies that. The cost changed numerous times, the rider flipped back and forth, and VP Bill Rose of all people chimed in on what functioned the entire time as a relatively innocuous, relatively ponderous removal spell. It consistently amazes me what kinds of minutiae my co-workers have managed to pay attention to, and the game is better for it.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card07a.jpg)

> TML 3/11/2011: Now makes five humans.
> 
> Del 4/15: CW02 also makes five Humans. Theme or inadvertent overlap?
> 
> TML 4/18/2011: Theme!
> 
> TML 5/26/2011: Flashback to nine from eight.

As another example of this kind of attention to detail, you can see from Tom's comment here that playtesting demonstrated ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless6.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) to be too powerful for Standard play, but ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless7.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) was manageable. It's tempting, once you move past the lower mana costs, to view anything above (say) seven mana as kind of interchangeable—you know, "Well, what difference does it make? They'll either get there or they won't." But every point of mana is important, and increasing mana costs by one actually matters *more* at higher mana costs than lower ones when the important variable is *whether* the card gets cast, not *when* (because your draw steps are less likely to provide you the proper combination of (a) mana required to cast the card and (b) the tools to survive until you get there).

This string of comments is also a great example of the "feature or bug?" phenomenon, where you find wholly unintentional similarities midway through the testing process. We have to evaluate whether the emergent interaction is good or bad. Sometimes it's one, sometimes it's the other, but in this case Tom liked the idea of multiple spells across the set that could rally the townsfolk together against the encroaching monstrous hordes.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card10a.jpg)

> EEF 3/7/2011: Didn't we avoid Human tribal for so long specifically so we wouldn't print a card with "sacrifice a Human" on it?
> 
> TML 3/7/2011: Yes, but I think it's time. :)

I talked extensively about this guy [a couple weeks back](/en/articles/latestdevelopments/2012/01-20-hooked-on-a-feeling) but this card highlights the enormity of the discussion we had about Human tribal. It was a very contentious issue, as the comments on [Increasing Devotion](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Increasing+Devotion) touch upon briefly as well. Bringing Humans into the picture—calling them out by name, as opposed to leaving their type hidden in plain sight upon Human creature cards—evoked very eerie sensibilities in a lot of people. Sacrificing Humans is, well, scary. It feels brutal and gruesome. But getting across that tone—that visceral sense of dread and horror—was explicitly one of the goals of the Innistrad world. Sometimes, it's important to cross a bridge when it's time to cross a bridge.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card16a.jpg)

> AF 2/24: 3
> 
> KEN 3/9/2011: TROGDOOOOOOOR!!!
> 
> TML 4/1/2011: Was 4R.
> 
> TML 4/8/2011: Switching back.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_burn.jpg)

As you can see from both this card and the previous one, we certainly had no desire to hold back the grief being inflicted upon the Human race in this set. Incidentally, as you can maybe infer from the comments, this card's playtest name was "Burninating the Peasants." Yes, we like to have fun from time to time.

![](https://i.ormos.uk/66/42/6642685e50ec981b0325c0eee01bbfb75f4c01f1b1608c979add02ed8127035d.jpg)

> EVL 3/4: We are desperate; lets turtle up!

We're also just *so* punny. Fateful hour's playtest name was, of course, desperation.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card15a.jpg)

> MJ 2/22: 13 is bad luck! ... for your creature.

...and Mons continues the trend of proving exactly why only a *few* of us in R&D launched successful standup comedy careers...

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card03a.jpg)

> KEN 7/12/2010: I love these rare Curses! Grief and misery wrapped in a bow.

...while Nagle continues to reassure us he's the same fun-sapping griefer we all know and love!

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card04a.jpg)

> Del 3/10: Odd place to see a Werewolf helper.
> 
> MR 3/16/11: I would make this 3W (or 4W if need be) so that werewolf decks can splash it.
> 
> TML 3/24/2011: I don't want this card to be free to put in counterspell decks. :/

To me, this card is a perfect example of my favorite kind of card design. As you can see from the comments, obviously limiting your opponent to one spell per turn is exactly what a Werewolf deck would want once the Moon comes out. What's tempting to do, when you're making a mechanic like the Werewolf mechanic, is to put a bunch of cards in the file that deliberately and obviously work with it—and some of those cards (like [Moonmist](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moonmist), for example) are perfectly fine and are good for the set. But it's dangerous to include too many of those cards in a file, because at a certain point you get "parasitic" (i.e., your cards become useless in the broader context of **Magic**).

This card, by contrast, takes something we've done numerous times (the "[Rule of Law](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rule+of+Law)" effect) and uses a theme of the set (Curses) to make a more appealing all-upside version of the card. The design is therefore totally self-contained as a **Magic** card. It makes sense in and of itself. But it's also useful and appealing in the secondary context of its game-play environment—in the context of the Werewolf decks that MaRo and Del mention.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card11a.jpg)

> AF 3/25: Powerful with [Stifle](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stifle)!
> 
> TML 4/5/2011: Should this be "nonland?"
> 
> Del 4/15/2011: Note that if you cast this on yourself, all your permanents will come back untapped.
> 
> Del 4/15: Also any Auras that are returning can't be attached to other permanents returning at the same time. If your opponent had a [Spirit Mantle](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spirit+Mantle), it's coming back attached to your guy.
> 
> Tabak 8/15: Super, super late change following FFL discovery of super, super annoying combo. This card is now super, super.

I'm surprised MaRo had no Dev Comments on this card, as he's been trying to print it for something like ten years. It finally got there. However, we had to kill the interaction with lands because of the "super super annoying" combo that Tabak mentions.

What's the combo?

![Sundial of the Infinite](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sundial+of+the+Infinite)

 

Yep. Cast this, then activate Sundial, and suddenly you've stumbled upon a one-sided [Apocalypse](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Apocalypse).

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card13a.jpg)

> Tabak 4/18: The three cards that granted persist did so without the "nontoken" clause. Should we do that here? Willing to trade unlikely rules confusion for better looking card.
> 
> TML 4/18/2011: I think I prefer "nontoken," but I guess I could be convinced otherwise.
> 
> Tabak 4/21: What if I gave you a hug? Or a puppy?

As on our last card, Tabak proves that he's a master of the celebrated art of Dev Comment deftness. Incidentally, he's very persuasive.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card01a.jpg)

> Del 5/13: Seems cheap. Would we print UU, "Up to two target creatures are unblockable this turn"?
> 
> TML 6/15/2011: Yes.

Some questions are more rhetorical than others...

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card12a.jpg)

> ZH 3/17: I am not a fan of more [Think Twice](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Think+Twice)s. I wish this did something else.
> 
> AF 3/25: More dredge cards :/

Throughout the development of *Innistrad* block, I was one of the very vocal opponents of the flashback cards that did nothing but generate raw card advantage. As I explained [in this article](/en/articles/latestdevelopments/2011/12-16-bringing-flashback-back), "flashback" is just a fancy way of saying "draw a card." When that reality isn't oblique enough—when a card straight-up exchanges itself for another card—I feel like it often leads to very dissatisfying incremental-advantage-accumulating game play. Of course, you need some cards that operate like that, and that's why this card got printed. It's just something to be diligent about.

Aaron, by contrast, was worried about "dredge"-style decks that operated almost entirely out of the graveyard. Our [Boneyard Wurm](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Boneyard+Wurm)/[Splinterfright](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Splinterfright) decks first loaded up the graveyard with [Mulch](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mulch), [Armored Skaab](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Armored+Skaab), and [Forbidden Alchemy](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Forbidden+Alchemy), then cast a second wave of Skaab Abominations once the initial threats were dealt with. These decks weren't oppressively powerful, but they had a play style that didn't feel very much like **Magic**: every turn you're having to think about the thirty-plus cards in your opponent's graveyard, and you can't really interact with those cards without altering your deck significantly. It's great for these kinds of decks to exist, of course—they demonstrate the myriad possibilities **Magic** allows. But what's scary is when this kind of deck becomes the best deck. Aaron was afraid that if we gave them too many tools, they'd get out of hand. Further testing revealed they were probably okay, however, and the card was allowed to stay.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card08a.jpg)

> TML 1/14/2011: Erik suggest 3U/2R. This should be good enough.
> 
> AF 3/25: So many of these U and/or R flashback cards are just durdling around to get more cards into your hand/graveyard. Do they do anything if you don't have the enchantments in play?

I consider this comment demonstrable proof of my success at getting the verb "durdle" embedded in the **Magic** R&D lexicon. This is another form of the [Think Twice](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Think+Twice) phenomenon, in the guise of raw card advantage and zone manipulation. "The enchantments" refers to [Burning Vengeance](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Burning+Vengeance) and [Secrets of the Dead](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Secrets+of+the+Dead). Chaining several of these would allow you to trigger the enchantments numerous times while not really doing much of anything. That didn't seem to be too big of a problem, however, so the card was left alone.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card14a.jpg)

> Tabak 5/31: This card would be cooler if the order of the effects were switched. It's the Zombies that destroy the Humans, right?
> 
> Max 6/6/11: Oh wow, I love Tabak's suggestion.
> 
> TML 6/22/2011: Question for later: Do the Zombie Humans survive the [Zombie Apocalypse](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombie+Apocalypse)?
> 
> Tabak 6/22: Natural Human Zombies (and that's the first time I've ever typed that) will be destroyed. I think this only affects changelings though.

A lot of the time, we in development convey the impression that most card changes come as a result of game-play balance or technical number-tweaking or something along those lines. It's important to remember, though, that almost as many changes come about in order to make something a lot more awesome. This comment from Tabak on [Zombie Apocalypse](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Zombie+Apocalypse) reflects that.

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card02a.jpg)

> TML 3/28/2011: Changed slightly.
> 
> Tabak 7/25/11: Changed not-so-slightly. Mana cost from G to 2G to annoy Billy Moreno or something. (From TML)

Other changes happen simply to annoy playtesters.

Okay, well, maybe it's a *little* more complicated (although irritating Billy is assuredly a very high priority). A kind of deck we always hate to exist at high levels is the Turbo-[Fog](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog) deck, which draws a lot of cards with a [Howling Mine](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Howling+Mine)-type effect and locks out the combat phase by repeatedly casting [Fog](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog). These kinds of decks also make very good use of planeswalkers, since it's almost impossible to kill those planeswalkers by attacking them with creatures. The printing of the actual card [Fog](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fog) in the core set discouraged us from pushing another similar effect as aggressively, so we upped the cost on this guy to ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif).

![](https://media.magic.wizards.com/image_legacy_migration/images/magic/daily/ld/ld180_card06a.jpg)

> TML 4/5/2011: New card.
> 
> TML 4/7/2011: Trying at 3WU 2/3.
> 
> TML 4/14/2011: Trying 4WU 2/5.
> 
> TML 4/28/2011: 5WU 3/5.

See, kids, if you try REAL hard, you'll always get there eventually...

No, this comment on [Drogskol Reaver](https://web.archive.org/web/20120203000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drogskol+Reaver) reflects the process by which most cards are actually costed. We try everything. We iterate continuously. Eventually, we happenstance upon something that works. When we write about the design and development process, we simplify a lot of what happens in order to help it make sense as a story. It's important to realize, though, that 90% of the work we do involves playtesting and playtesting and playtesting to trial-and-error a set together until it's right. Rarely do we pluck an idea out of thin air and have it work perfectly the first time around. It happens, but it doesn't happen often.

![](https://i.ormos.uk/6c/2f/6c2f89da9de14b2930f1dcd736a0ed2d3161d0b57bcfab9282baa01c0529ddf9.jpg)

There you have it: (some of) the nuts and bolts of *Dark Ascension*. I hope you enjoyed this romp around the Multiverse. Join me next week when I talk about the next generation of the Pro Tour, and what it means for R&D.

Zac
---
id: mzs2t0hk
kind: article
lang: en
path: /en/articles/latestdevelopments/2013/04-05-gatecrash-ing-the-multiverse
title: Gatecrash ing the Multiverse
published: '2013-04-05'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/241
    lang_detected: en
    capture_id: 231422
    url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/241&print=true
    captured_at: '2013-07-07 06:38:54+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/241
    lang_detected: en
    capture_id: 231422
    url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/241&print=true
    captured_at: '2013-07-07 06:38:54+00'
    rule: aspx.byline_date
  authors:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/241
    lang_detected: en
    capture_id: 231422
    url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/241&print=true
    captured_at: '2013-07-07 06:38:54+00'
    rule: aspx.byline
  column:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/241
    lang_detected: en
    capture_id: 231422
    url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/241&print=true
    captured_at: '2013-07-07 06:38:54+00'
    rule: aspx.archive_link_column
    registry_match: registry.explicit
sources:
- document_id: mzs2t0hk
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/241&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/241
  lang: en
  template: aspx
  captured_at: '2013-07-07 06:38:54+00'
  capture_id: 231422
  wayback_url: https://web.archive.org/web/20130707063854id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/241&print=true
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: mzs2t0hk
  capture_id: 231422
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/241&print=true
  wayback_url: https://web.archive.org/web/20130707063854id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/241&print=true
  captured_at: '2013-07-07 06:38:54+00'
  template: aspx
  sha256: 21b0f17c03f24fa8b9d2d4fdb3507bbe5ff9f8289452ac8884c7f34657986607
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Assault Griffin
  - Crocanura
  - Sphinx's Revelation
  - Bonfire of the Damned
  - Frontline Medic
  - Draining Whelk
  - Daring Leap
  - Aerial Maneuver
  - Neurok Hoversail
  - Cobbled Wings
  - Bane Alley Broker
  - Skyblinder Staff
  - Glaring Spotlight
  - Experiment One
  - Chronozoa
  occurrences: 60
---
For the last few months, Latest Developments has been handled by a number of different developers working on weekly columns. As of this week, I am taking over as the main author of the column, with others jumping in from time to time when they have something they want to say. I'm very excited for this opportunity and look forward to bringing you a behind-the-scenes look at what happens on the development side of the Pit. If there are things any of you out there reading this would like to see, send me an email and I may be able to put an article together in the future. 

With that out of the way, it's time to move on to what the French call "[*content*](http://fr.wiktionary.org/wiki/content#Anglais)." 

Multiverse is the database that R&D uses internally to keep track of the cards in sets. Designers and developers are encourage to go through the database about once a week and leave any comments they may have on cards. Sometimes they discuss power levels, sometimes it's leaving feedback on Limited play, and sometimes they just have a witty comment to leave. These are some of the more interesting comments in *Gatecrash*. 

The cast of commentators

![](https://i.ormos.uk/cc/88/cc886ad1801d000e9f8ccad3e73a31d571306e9ce45cdc656ac198f23d06f9f0.jpg) 

**AF**—[Aaron Forsythe](https://web.archive.org/web/20130706090229/http://www.wizards.com/magic/magazine/archive.aspx?author=aaron%20forsythe)

![](https://i.ormos.uk/a3/b8/a3b88e7d7f0d7e9bc111f4e1149c808d9a8720ad945e30ef48046e924f760e83.jpg) 

**DB**—[Doug Beyer](https://web.archive.org/web/20130106091430/http://www.wizards.com/magic/magazine/archive.aspx?author=doug%20beyer)

![](https://i.ormos.uk/a9/0c/a90c93246e1c543ad1616b44e6648d77c13eeeea6364f3d3e7fbe09ed759b875.jpg) 

**DEL**—Del Laugel 

![](https://i.ormos.uk/ef/72/ef720e25ac1b4ff1389d81c9977841b7deca7e5cf8d15df7528af1b3635b7ad0.jpg) 

**DH**—[Dave Humpherys](https://web.archive.org/web/20130518212357/http://www.wizards.com/magic/magazine/archive.aspx?author=dave%20humpherys)

![](https://i.ormos.uk/71/7e/717ec8ea013fe26416594283aa203c8c086fe7db5bfeb02641f7c432994f20bb.jpg) 

**EEF**—[Ethan Fleischer](https://web.archive.org/web/20130810130139/http://www.wizards.com/magic/magazine/archive.aspx?author=ethan%20fleischer)

![](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg) 

**EVL**—[Erik Lauer](https://web.archive.org/web/20130625182003/http://www.wizards.com/magic/magazine/archive.aspx?author=erik%20lauer)

![](https://i.ormos.uk/89/be/89be87cd13e85cdfa6301f157dc41afff82903d838483860ee14e4361d9d5e30.jpg) 

**GSV**—[Gavin Verhey](https://web.archive.org/web/20130609072254/http://www.wizards.com/magic/magazine/archive.aspx?author=gavin%20verhey)

![](https://i.ormos.uk/73/dc/73dc2c209bef80978eea09781f3075d348fa6472480299108af0945ff889dce7.jpg) 

**KEN**—[Ken Nagle](https://web.archive.org/web/20130615224814/http://www.wizards.com/magic/magazine/archive.aspx?author=ken%20nagle)

![](https://i.ormos.uk/2c/91/2c91c356c244bac703be5454524033ba3e82399c4aa0766ca588b15370ade280.jpg) 

**Mago**—[Mark Gottlieb](https://web.archive.org/web/20130518221510/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20gottlieb)

![](https://i.ormos.uk/36/2b/362b9b8902548d4692f09924d01f0429d5ba1494d3c33b8acce1eeff05988df7.jpg) 

**Max**—[Max McCall](https://web.archive.org/web/20130619102956/http://www.wizards.com/magic/magazine/archive.aspx?author=max%20mccall)

![](https://i.ormos.uk/f8/3c/f83cde49f5aa4cfb338e0e4a5b8d96af7fe22d2b20b7986681c70bc77fe6cc38.jpg) 

 **MJ**—Mons Johnson 

![](https://i.ormos.uk/92/ce/92ceeab73eb3a7f33920535b070768559eb14c5b512cccee052bbb624575be15.jpg) 

**MJG**—[Mark Globus](https://web.archive.org/web/20130615183506/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20globus)

![](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg) 

**MR**—[Mark Rosewater](https://web.archive.org/web/20130921125310/http://www.wizards.com/magic/magazine/archive.aspx?author=mark%20rosewater)

![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg) 

**TML**—[Tom LaPille](https://web.archive.org/web/20130520102427/http://www.wizards.com/magic/magazine/archive.aspx?author=tom%20lapille)

![](https://i.ormos.uk/2d/72/2d72b81445c4e8a88d9f4fe8b3bced02d1310c1683426ad71415285f6c9629c4.jpg) 

**ZH**—[Zac Hill](https://web.archive.org/web/20130523185550/http://www.wizards.com/magic/magazine/archive.aspx?author=zac%20hill)

And onto the show:

 ![Shambleshark](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Shambleshark&options=) 

 

ZH 10/20: This here is a generous common.  
 AF 1/18: Beautiful.  
 KEN 2/21/2012: For my CrabFishBeast deck!  
 DH 2/22: 2/2 - 2/1 so easier to block and possibly more evolving possible  
 Del 6/7: Now with flash. 

You'll notice the last change in here was made by our trusty editor, Del Laugel. As the set nears completion, she "owns" the Multiverse file, and is in charge of making the actual changes that Dave Humphreys, as lead developer, wants done in the file. The final addition of flash was to give Simic a little extra oomph in Limited.

 ![Disciple of the Old Ways](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Disciple%20of%20the%20Old%20Ways&options=) 

 

Mago 10/11/11: Changed from 3G 3/3, 1R: FS to 1G 2/2, R: FS.  
 EVL 12/9: MEOW!  
 ZH 2/14: Confused as to why name is not Zan Zan the Clan Man. 

Zac is sorely missed if for no other reason than his ability to give appropriate nicknames to cards in development.

 ![Assault Griffin](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Assault%20Griffin&options=) 

 

DH 12/6: There is a 3W 2/3 flyer in Hook. Changed to 3/2 for now.  
 KEN 12/12/2011: New World Order and simplicity pushes will have us doing this more.  
 DH 1/3: Renamed to its repeat Assault Griffin, hope 'Assault' isn't named 'Assault'.  
 DB 1/9/2011: Noted :) 

Names can cause confusion internally, from time to time. At the time, battalion was named "assault," so a number of the cards with that ability were just generically called "Assault Whatever." Naming conventions like these can lead to Assault Griffin being very confusing in playtests. 

 ![Crocanura](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Crocanura&options=) 

 

GSV 1/14: Creative gets a hold of our set file and changes a Spider to an Alligator Frog Beast. Line is like some kind of bizarro world!  
 DH 2/6: We need more Alligator Frog Beasts.  
 TML 2/8/2012: Agree. 

One of the most fun parts of working with *Gatecrash* was watching the Simic Combine's creatures wildy change in creature types—some of which stuck, and some of which changed. Usually, it meant the creature getting a little less silly over time, but not Crocanura, which evolved from a lowly Spider into an Alligator Frog Beast before finally ending up as a Crocodile Frog, as Alligator isn't a supported creature type in **Magic**. Yet. 

 ![Frontline Medic](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Frontline%20Medic&options=) 

 

MJG 10/28/11: Cool.  
 GSV 12/9: Playing with this card in my Boros draft deck was fun and worked well. Felt like a good rare without being insane, which was nice.  
 Del 2/7: Note that this affects creatures that enter the battlefield later in the turn.  
 DH 3/9: 3/2 - 3/3  
 Del 6/22: Gained an ability. 

Gained an ability, indeed. As you can see from the dates, this was a relatively late change. We already had a good idea just how strong Sphinx's Revelation would be, but Bonfire of the Damned decks were also making huge waves in the real world. Erik Lauer, as the head of the [FFL](/en/articles/latestdevelopments/2010/03-05-welcome-to-the-future-future), wanted to find a card to adjust slightly to put some pressure on all of the powerful X spells in Standard. In the end, it was decided that Frontline Medic was a card that was already just about good enough for Constructed and could most easily house text that made sense for combating these spells. 

 ![Mystic Genesis](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Mystic%20Genesis&options=) 

 

DH 1/16: Changed to X/X instead of X 1/1s.  
 DH 1/18: I hope Simic players like the letter 'X'  
 Max 1/20/12: The entire set marks the spot.  
 ZH 2/14: Really similar to Draining Whelk, which is probably cool actually.  
 KEN 3/27/2012: Is this supposed to be a creature card doing the same thing?  
 Del 4/17: Not after the art has been commissioned, no. 

The earliest version of this card created a bunch of tokens, but that didn't play well enough into the Simic themes. Now, the card is able to trigger evolve when a large enough spell is countered, and also happens to work better with populate.

 ![Nightveil Specter](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Nightveil%20Specter&options=) 

 

Del 5/10: 2/3 - 3/3.  
 Del 5/17: 3/3 - 3/2.  
 Del 5/31: 3/2 - 2/3.  
 MJ 6/7: life is circular... 

One of the truisms of R&D is that if you aren't sure which is the correct value for a card, try another and see where it leads you. Sometimes it is back to the original, but at least we knew that we had the card at the place we wanted it to be.

 ![Treasury Thrull](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Treasury%20Thrull&options=) 

 

\[original name: Orzhov Vaultbeast\]  
 Max 2/20/12: Misread as 'valuebeast.' Was not disappointed. 

Appropriate comment is appropriate.

 ![Aerial Maneuver](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Aerial%20Maneuver&options=) 

 

Del 1/24: I had no idea the +1/+1 on Daring Leap was the blue part of that spell.  
 DH 2/1: Daring Leap now apparently costs a blue less now. Changed to make better.  
 TML 2/8/2012: I look forward to ambushing things with this spell. 

The original version of this spell only gave the creature flying and first strike, leading to Del's comment. Making better versions of cards is a constant discussion in R&D, but it is something that we have to allow ourselves to do. The game has been around for nearly twenty years now, and trying to always operate within the confines of what exists is too much of a constraint when trying to make fun and exciting formats. Sometimes we do make cards like Aerial Maneuver, which totally outclasses Daring Leap, and sometimes we make worse versions of existing cards. We try and keep all of it to a minimum, but if the right spell for a set is either better or worse than a previously printed **Magic** card, we won't constrain ourselves to trying to not outclass an old card. 

 ![Crowned Ceratok](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Crowned%20Ceratok&options=) 

 

KEN 9/21/2011: MOAR 'Human Elk Wizard' PLZ 

I see you want a Human Elk Wizard. Best I can do is Rhino.

 ![Skyblinder Staff](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Skyblinder%20Staff&options=) 

 

\[playtest name: Umbrella\]  
 Mago 10/26/11: New card. Was Neurok Hoversail, but Cobbled Wings was in ISD. Might not be common.  
 TML 10/28/2011: ella ella hey hey hey  
 EVL 12/11: :-)  
 DH 1/10: Changed from protection to can't be blocked by.  
 EEF 1/17/12: It loses a lot of its flavor when it loses protection, IMO.  
 ZH 2/14: I feel like this is too adorable of a card. When this isn't literally an umbrella, are we going to dig it? 

Often when sets are between design and development, mini-teams will convene to take an aspect of the set that needs some work, such as Planeswalker designs, top-down themes, or mechanics that need some fleshing out. For *Gatecrash*, one such mini-team revolved around getting more cards into the set to bring out the "city" feel that was missing. This is where cards like Bane Alley Broker, Skyblinder Staff, and Glaring Spotlight came from. Often, these teams produce cards that work on paper, but risk losing their identity once a final name is put on the card. 

 ![Gruul Ragebeast](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Gruul%20Ragebeast&options=) 

 

DH 1/23: Added 'an opponent controls'.  
 DH 2/29: Intentionally not optional fwiw.  
 Max 3/30/12: THUNDERDOME 

Once again, Max shows that he has a knack for concise descriptions.

 ![Experiment One](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Experiment%20One&options=) 

 

Del 5/8: Now regenerates.  
 Del 5/17: Activation cost from 1G to 2G.  
 Del 6/7: Activation cost from 2G to remove a +1/+1 counter.  
 Del 6/14: Activation cost from remove one +1/+1 counter to remove two. 

Another card with late changes, Experiment One began as a vanilla 1/1 with evolve, which saw some play in our [Future Future League](/en/articles/latestdevelopments/2010/03-05-welcome-to-the-future-future). We found that the unfun part about decks trying to evolve creatures was that you were just so vulnerable to any sort of wraths. We fiddled around with Experiment One's version of regeneration, quickly finding that the mana cost wasn't helping, since the decks that wanted to use it were forced to tap out if they wanted to put any pressure on White-Blue Control. Changing the activation to removing a counter was the most fun direction to push the card, but it wasn't quite right. Most of the decks we had with Experiment One were good at making it a 3/3 or a 4/4, but once you were there, the trick was to cast a creature of equal size to Experiment One, regenerate it, get the evolve counter, then swing. It was fiddly and not the play pattern we wanted out of those decks. We found that moving it to two counters put the card in the spot we were aiming at: one where regeneration helped it survive removal, but not simply dominate combat. 

 ![Giant Adephage](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Giant%20Adephage&options=) 

 

GSV 1/23: Love it. It's like a Chronozoa for Ken Nagle. 

What else really needs to be said?

As a bonus section, below I've listed a number of playtest names. See if you can guess what the final card name ended up as:

Neighborhood Watch - 

 ![Hold the Gates](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Hold%20the%20Gates&options=) 

  
  
 

Friendly Demon - 

 ![Alms Beast](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Alms%20Beast&options=) 

  
  
 

Last Will and Testament - 

 ![Dying Wish](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Dying%20Wish&options=) 

  
  
 

Stick It to the Man - 

 ![Homing Lightning](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Homing%20Lightning&options=) 

  
  
 

The Roof Is on Fire - 

 ![Five-Alarm Fire](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Five-Alarm%20Fire&options=) 

  
  
 

Balm Lightning - 

 ![Spark Trooper](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Spark%20Trooper&options=) 

  
  
 

G-G-G-Ghost! - 

 ![Voidwalk](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Voidwalk&options=) 

  
  
 

Open the Tombs - 

 ![Immortal Servitude](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Immortal%20Servitude&options=) 

  
  
 

Surprise Me - 

 ![Unexpected Results](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Unexpected%20Results&options=) 

  
  
 

Kickboxing Viashino - 

 ![Ghor-Clan Rampager](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Ghor-Clan%20Rampager&options=) 

  
  
 

Good Lieutenant - 

 ![Boros Elite](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Boros%20Elite&options=) 

  
  
 

Street Smarts - 

 ![Way of the Thief](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Way%20of%20the%20Thief&options=) 

  
  
 

Hurl into the Sun - 

 ![Shattering Blow](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Shattering%20Blow&options=) 

  
  
 

Science! - 

 ![Urban Evolution](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Urban%20Evolution&options=) 

  
  
 

I'm Full of Tinier Men - 

 ![Murder Investigation](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Murder%20Investigation&options=) 

  
  
 

Bear Supply - 

 ![Ooze Flux](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Ooze%20Flux&options=) 

  
  
 

Draft Board - 

 ![Assemble the Legion](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Assemble%20the%20Legion&options=) 

  
  
 

The Joys of Pet Ownership - 

 ![Predator's Rapport](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Predator%27s%20Rapport&options=) 

  
  
 

Zac's Steatopygous Mutant - 

 ![Elusive Krasis](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Elusive%20Krasis&options=) 

  
  
 

Elder Spitemare - 

 ![Boros Reckoner](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Boros%20Reckoner&options=) 

  
  
 

Unexpected Swarm of Weasels - 

 ![Merfolk of the Depths](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Merfolk%20of%20the%20Depths&options=) 

  
  
 

![](https://i.ormos.uk/0d/4d/0d4df1c86071a2369ed32d2ce0f183a1e651fa13b450a88aabd3ff47a77244e5.png)

![](https://i.ormos.uk/9f/a0/9fa07821341a1a7999cfdc7cf7ffde57ad6a1ed6d0d939432d442e456796dd88.png) 

![](http://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_FNM_Top.jpg) 

[![](http://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_FNM_Button01_Static.jpg)](https://web.archive.org/web/20130405000000/http://staging.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/gatecrash/productinfo) [![](http://media.wizards.com/images/magic/daily/footers/EN_GTC_ArticleFooter_FNM_Button02_Static.jpg)](https://web.archive.org/web/20130405000000/http://staging.wizards.com/Magic/TCG/article.aspx?x=mtg/tcg/gatecrash/cig) 

  
  
  

<table>&#10;      <tbody><tr>&#10;        <td>&#10;          <a href="https://twitter.com/share">Tweet</a>&#10;        </td>&#10;        <td>&#10;          <div>Words</div>&#10;        </td>&#10;        <td>&#10;          <div id="fb-root">&#10;            <div>Words</div>&#10;          </div>&#10;        </td>&#10;      </tr>&#10;    </tbody></table>

  
 ![](http://media.wizards.com/images/magic/daily/footers/slice1.jpg) ![](http://media.wizards.com/images/magic/daily/footers/rakdos_02.jpg)

 

![Sam Stoddard](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg "Sam Stoddard")

<table>&#10;    <tbody><tr>&#10;      <td>&#10;        <b>Sam Stoddard</b>&#10;        <br>&#10;        <a href="https://twitter.com/samstod">@SamStod</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130405000000/https://www.wizards.com/company/emailtoauthor.asp?author=Sam%20Stoddard&amp;amp;headline=[Gatecrashing%20the%20Multiverse]">Email Sam</a>&#10;      </td>&#10;      <td>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130405000000/http://staging.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard">Author Archive</a>&#10;        <br>&#10;        <a href="https://web.archive.org/web/20130903232710/http://www.wizards.com/magic/magazine/archive.aspx?tag=latest%20developments&amp;description=latest%20developments">Latest Developments Archive</a>&#10;      </td>&#10;    </tr>&#10;  </tbody></table>

  

Sam Stoddard came to Wizards of the Coast as an intern in May, 2012. He is currently a game designer working on final design and development for **Magic: The Gathering**. 

 
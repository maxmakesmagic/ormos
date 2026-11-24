---
id: dm1t1vmf
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/08-26-the-magic-2012-multiverse-dump-part-2
title: The Magic 2012 Multiverse Dump, Part 2
published: '2011-08-26'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
    lang_detected: en
    capture_id: 727291
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
    captured_at: '2022-10-07 15:42:24+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
    lang_detected: en
    capture_id: 727291
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
    captured_at: '2022-10-07 15:42:24+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
    lang_detected: en
    capture_id: 727291
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
    captured_at: '2022-10-07 15:42:24+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
    lang_detected: en
    capture_id: 727291
    url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
    captured_at: '2022-10-07 15:42:24+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: dm1t1vmf
  url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
  lang: en
  template: drupal
  captured_at: '2022-10-07 15:42:24+00'
  capture_id: 727291
  wayback_url: https://web.archive.org/web/20221007154224id_/https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-26
- document_id: dm1t1vmf
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/157
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/157
  lang: en
  template: aspx
  captured_at: '2013-07-06 05:38:33+00'
  capture_id: 613522
  wayback_url: https://web.archive.org/web/20130706053833id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/157
- document_id: dm1t1vmf
  url: https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-25
  page_key: magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-25
  lang: en
  template: drupal
  captured_at: '2022-07-04 08:32:10+00'
  capture_id: 727290
  wayback_url: https://web.archive.org/web/20220704083210id_/https://magic.wizards.com/en/articles/archive/latest-developments/magic-2012-multiverse-dump-part-2-2011-08-25
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: dm1t1vmf
  capture_id: 613522
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/157
  wayback_url: https://web.archive.org/web/20130706053833id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/157
  captured_at: '2013-07-06 05:38:33+00'
  template: aspx
  sha256: a6f33e0c488b27880cbb7c919bce16095ce94cc802746ef2d27c19a8aa09c18e
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Lightning Elemental
  - Arc Runner
  - Honor of the Pure
  - Glorious Anthem
  - Spined Wurm
  - Falter
  - Tectonic Rift
  - Stone Rain
  - Thicket Basilisk
  - Lure
  - Greater Basilisk
  - Dancing Scimitar
  - Greatsword
  - Ensouled Scimitar
  - Druidic Satchel
  - Jayemdae Tome
  occurrences: 29
---
Next Monday begins our *Innistrad* preview weeks here on **DailyMTG.com**. While I'm excited to start talking about *Innistrad*, which I helped both design and develop, ***Magic** 2012* is the first set I led the development of. The end of its time in the sun strikes me as being slightly bittersweet.

Before we move on to *Innistrad*, though, I've got some more Multiverse comments to go through! Today's cast of characters is a little smaller than normal. Here they are:

> AF: Aaron Forsythe, director of **Magic** R&D  
>  DB: Doug Beyer, **Magic** creative designer  
>  Del: Del Laugel, **Magic** senior editor  
>  KD: Kelly Digges, ***Magic** 2012* developer  
>  MJG: Mark Globus, ***Magic** 2012* lead designer  
>  TML: Tom LaPille, ***Magic** 2012* lead developer

We stopped just before red last time. Let's pick it up there.

![](http://media.wizards.com/images/magic/daily/ld/ld157_card01a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld157_card01b.jpg)

Lightning Elemental is not exciting, new, or format-defining in any way. However, it's an important card for introductory purposes because it is a simple creature with one keyword ability. We call those cards "French vanillas"; they aren't quite vanilla (with no abilities), but they're still pretty easy to understand for a new player. Core set French vanilla cards are especially useful because they get reminder text. We use them in products like the sample decks that we've been giving out at conventions like Gen Con and this weekend's PAX to keep people from needing to look at an insert to know what their cards do.

> Del 6/1: Four cards in the set have the word haste on them. Two of those four cards are creatures.

Del sometimes puts comments like this in the file with the intent of alerting the lead developer to a strange distribution of a particular keyword. In this case, we had fewer cards with haste than normal. Is that okay? I decided that it was.

> KD 7/23: What makes this guy a better choice than Arc Runner? Feels kind of like dancing just to dance.  
>  DB 8/23/2010: \*dances, just because\*

Let's talk about dancing. Core sets have a bunch of reprints in them. Often, there are a few cards that could serve any particular purpose. For example, Honor of the Pure and Glorious Anthem are both fine expressions of the "pump all your creatures" effect. Either of them would be fine for any core set. We could easily have switched from Honor of the Pure in ***Magic** 2011* to Glorious Anthem in ***Magic** 2012*. There are even valid development reasons to do so: maybe I want to encourage white creature decks that splash another color, like the white-black token deck that Luis Scott-Vargas played to the finals of [Pro Tour Kyoto](/en/events/2009/ptkyo09/nassif-the-greater-power) in 2009. However, that ends up feeling like a very marginal change, as the cards aren't that different. The overall effect to some players is to just randomly make them acquire a different card to do the same thing, and that's not particularly satisfying.

I find dancing less problematic when we do it with commons, as we need Limited to feel different from core set to core set. However, it's still good to check ourselves on things like this.

> Del 9/26: Lightning Elemental is a more newbie-friendly card than Arc Runner. It gets to take out Spined Wurm on defense, and it doesn't require that the rest of the deck be massively aggro.

This is basically my opinion as well. I found Arc Runner to be an ultimately unsatisfying card, as the kind of deck that wants an Arc Runner is just really hard to draft. It's good at what it is trying to do, though, so you may still see it again someday.

![](http://media.wizards.com/images/magic/daily/ld/ld157_card02a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld157_card02b.jpg)

The story of this card begins with killing another card, which forced me to come up with a new card. I have always enjoyed the creative concept behind Falter: I shake the ground, knock all your dudes over, and then run by them while they are getting up! Therefore, I put Falter into the set.

> TML 5/7/2010: Was crazy card in Deluded Bravado. Now a clean card that I've wanted to put in core sets for forever.  
>  AF 5/14: I think instant is bad. People will cast it after blockers are declared.  
>  TML 6/4/2010: Agree. I still like this concept. Sorcery you.

Making this into a sorcery meant that it had to be a new card. I was fine with that at the time, but further developments elsewhere changed things. There was an uncommon land destruction spell that was killed for being too strong, and that meant that red had no land destruction effect anywhere in its commons or uncommons. I wanted to fix that. Mike Turian pointed out that blowing up a land seems like a fine way to cause the earthquake that makes creatures unable to block, and Tectonic Rift in its final form was born.

> TML 6/15/2010: Mike's cool idea staples Stone Rain to this for a satisfying new card.

Core set cards are all about being resonant and flavorful. While this card made perfect sense to me, I wanted to check that it made sense to other people too. So I asked.

> TML 6/17/2010: Is this thing just a weirdo that makes no sense?  
>  AF 6/17: Works for me.

It also worked for VP of R&D Bill Rose. ***Magic** 2012* lead designer Mark Globus was suspicious, but I liked it a lot, and so did Bill and Aaron, so I decided to keep it.

> KD 6/30: This got me to put Stone Rain in my Sealed Deck. I don't like that.  
>  MJG 7/2/10: How about 3R "Destroy target land."?

Kelly Digges is an utterly fascinating person to work with when it comes to **Magic** cards. Years of writing about fun and **Magic** have made him almost painfully self-aware about what **Magic** cards he has fun playing with, and land destruction is one of the categories that he really hates. He knows that he'll want to use it in play and that the resulting outcome won't be fun for the opponent or lead to an interactive game if it works, so getting him to feel good about putting anything that might at some point ever destroy a land in a Limited deck is nearly impossible.

While most players are not anywhere near as self-aware as Kelly is, he's still quite right about this card. The Falter effect ends the game, but so can the Stone Rain effect in a Sealed Deck game that has a player stalled on lands.

> TML 7/6/2010: I want to keep this text box, as it's one of the new cards that tells a story. It may go to uncommon though.

As it turned out, this card was pretty annoying when it was a common. As Kelly observed, the combination of mana-screw potential and finishing effect meant that it was correct to play a little more often than I wanted it to be. Moving it up in rarity seemed like a fine solution to that.

> TML 7/6/2010: Now uncommon.

And voila!

![](http://media.wizards.com/images/magic/daily/ld/ld157_card03a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld157_card03b.jpg)

> DB 3/18/2010: Love. <3  
>  AF 3/18: Also.

The combination of Thicket Basilisk and Lure captured the imagination of many **Magic** players early in the game's lifetime. That sort of two-card obvious combination is one of the things that shows people how much bigger **Magic** can be than a game of individual cards. Designers tend to enjoy building these things into the core set for new players to find, and Mark Globus is no exception.

> KD 4/8: I do not love Lure nearly as much in deathtouch world.

Thicket Basilisk works a lot better than Greater Basilisk for this trick, as it gets to kill all of the blocking creatures, whether there are two or two hundred. We like using keywords now, though, so Greater Basilisk and its deathtouch only get to take out three guys at most. Although this works less well than it used to, it still works well enough to make a new player feel clever, as Kelly found out soon after this.

![](http://media.wizards.com/images/magic/daily/ld/ld157_vs.jpg) 

  

> AF 7/19: The Children of Tomorrow will know no other world...  
>  KD 7/23: True. I put this on Greater Basilisk and just demolished people, so I'm feeling better about this.

![](http://media.wizards.com/images/magic/daily/ld/ld157_card04a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld157_card04b.jpg)

> DB 3/8/2010: I liked this for blocking Intimidate guys.  
>  DB 4/1/2010: Someone keep a tally of how many times this picks up a Claymore. :/

Okay, I should stop and explain something. In the design handoff, this slot was Dancing Scimitar. Claymore, as you might guess, later became Greatsword. However, seeing the pair of them together was pretty awkward.

> KD 4/1: I've already seen it happen once, but I consoled myself by imagining that the scimitar taught the claymore to dance and then they did a 4/5 flying tango on the opponent's face.  
>  TML 4/6/2010: Now I want to make a sword theme deck :D

![](http://www.wizards.com/mtg/images/daily/ld/ld157_image.jpg) 

  

> TML 6/15/2010: I hate this and expect to change it.

Yeah, that didn't last long. Swords these days are supposed to be Equipment. The right callback in some sense would be Ensouled Scimitar, but the rules for Equipment becoming creatures are a little wonky. Rather than try to figure this out, I just killed Dancing Scimitar for another, less weird artifact creature.

> TML 6/16/2010: New golem to support Action.  
>  AF 6/17: Heh.  
>  MJG 6/18/10: I like it!  
>  TML 9/1/2010: Worse to make all decks worse.

Now here's an interesting bit. I started this card as a three-mana 3/3 that entered the battlefield tapped, which is a pretty strong card. It was so strong, in fact, that drafters took it over a lot of colored cards. This felt wrong to me. It's obviously not a color balance problem, as every color has equal access to it, but the more power that exists in colorless cards, the less difference there is (or feels like there is) between decks of different colors in terms of what cards matter. This is okay in an artifact set to some degree, but not in ***Magic** 2012*. Therefore, I reacted strongly and made this a four-mana 3/3 instead.

> TML 9/9/2010: A little better.

After I did that, though, no one actually wanted to play the thing. I intended for the card to be a somewhat reasonable creature for otherwise creature-light decks, so I gave the card a fourth point of toughness. At that point, enough people were willing to play it that I was satisfied.

**Magic** development can be a tough gig. Lots of players want their individual cards to be powerful, but the overall feel of the set is just as important. Sometimes, individual cards just have to be a little different, and sometimes worse, to get the experience we're trying to make.

![](http://media.wizards.com/images/magic/daily/ld/ld157_card05a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld157_card05b.jpg)

> TML 5/6/2010: Used to be tap target creature. Now bonks them in the face for Bloodthirst.  
>  AF 5/14: Yay!  
>  TML 5/21/2010: Now does more damage if you are the emperor.  
>  AF 7/19: We should make these actually better in Emperor. Or not.  
>  KD 7/23: (You are the Emperor if you control artifacts named Emperor's Crown, Emperor's Scepter, and Emperor's Throne, or if you are sitting in the middle in an Emperor game.)

![](http://media.wizards.com/images/magic/daily/ld/ld157_card06a.jpg) ![](http://media.wizards.com/images/magic/daily/ld/ld157_card06b.jpg)

One of the challenging things about game design is that you have to make games with other people in mind too, not just yourself. Getting inside other people's heads is challenging, and doing so can also lead you to do things that you wouldn't normally do.

That said, let's talk about my least favorite card (personally speaking) in ***Magic** 2012*.

Druidic Satchel is basically a random marginal effect generator, which takes over slow Limited games and never does anything particularly splashy. I'd rather have a more expensive card like Jayemdae Tome do this in a reliable way. I was the lead developer of ***Magic** 2012*, so I could have just killed this outright. What happened?

> TML 5/10/2010: I am tiring of this card.  
>  AF 5/14: :( seems awesome.

The fact that someone designed this at all and that Aaron Forsythe liked it meant that I felt I had to at least gather more data. Luckily, we have a mechanism for doing that: the rare poll! A few times each set, we send a poll throughout the company that allows employees who play **Magic** to rate each rare and mythic rare in the set on a scale from 1 to 10. We also allow people to give us comments. Druidic Satchel ended up in the top third on the first rare poll, which shocked me. However, that was exactly what I needed to know in order to make a decision.

> TML 5/21/2010: The casuals love it. Keeping for sure.  
>  KD 6/30: I still dislike this card, but I guess I'll bow to the casual poll. Can anyone explain the appeal to me?  
>  TML 7/1/2010: Nope, sure can't. Hooray for data!  
>  AF 7/19: The appeal is, sometimes I get a Snake, sometimes I get a land! Wheeee! Things!  
>  KD 7/23: And here, perhaps, is where Diversity Timmy and Adrenaline Timmy part ways.

I don't know if I will ever meet someone who I made very happy with this card, but I hope some of them exist.

![](https://i.ormos.uk/bd/2d/bd2d5ace8b8f9c9ceb613cef8f1ed759f8cf99bbe030e868ae714ca00ce86d95.jpg) 

  

Well, that's a wrap for ***Magic** 2012* development stories. This coming Monday is the beginning of *Innistrad* previews, and boy do we have some things to talk about. I've got a pretty saucy card for my first preview next Friday too, so be sure to come back for it.

* * *

  

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b> What color do you most like playing against? </b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>Green</td>&#10;    <td>290</td>&#10;    <td>45.0%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>White</td>&#10;    <td>116</td>&#10;    <td>18.0%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Red</td>&#10;    <td>86</td>&#10;    <td>13.4%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Black</td>&#10;    <td>85</td>&#10;    <td>13.2%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Blue</td>&#10;    <td>67</td>&#10;    <td>10.4%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>644</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### This Week's Polls

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>Have you built a Modern deck with physical cards?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <div id="pollmtg_daily_ld_157_poll1">&#10;                    <div>&#10;                      &#10;                      Yes<br>No<br></div>&#10;                    <div>&#10;                      &#10;                    </div>&#10;                    <div></div>&#10;                  </div>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>Have you played a match of Modern on <b>Magic Online</b>?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <div id="pollmtg_daily_ld_157_poll2">&#10;                    <div>&#10;                      &#10;                      Yes<br>No, and I play <b>Magic Online</b><br>No, and I don't play <b>Magic Online</b><br></div>&#10;                    <div>&#10;                      &#10;                    </div>&#10;                    <div></div>&#10;                  </div>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>
---
id: d8408wgx
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/02-14-the-m-files-born-of-the-gods
title: 'The M Files: Born of the Gods'
published: '2014-02-14'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
    lang_detected: en
    capture_id: 726877
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
    captured_at: '2022-08-12 05:53:09+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
    lang_detected: en
    capture_id: 726877
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
    captured_at: '2022-08-12 05:53:09+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
    lang_detected: en
    capture_id: 726877
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
    captured_at: '2022-08-12 05:53:09+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
    lang_detected: en
    capture_id: 726877
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
    captured_at: '2022-08-12 05:53:09+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: d8408wgx
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
  lang: en
  template: drupal
  captured_at: '2022-08-12 05:53:09+00'
  capture_id: 726877
  wayback_url: https://web.archive.org/web/20220812055309id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
- document_id: d8408wgx
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/286&print=true
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/286
  lang: en
  template: aspx
  captured_at: '2014-05-09 10:17:12+00'
  capture_id: 231475
  wayback_url: https://web.archive.org/web/20140509101712id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/286&print=true
- document_id: d8408wgx
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-12
  page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-12
  lang: en
  template: drupal
  captured_at: '2022-06-29 13:06:54+00'
  capture_id: 726872
  wayback_url: https://web.archive.org/web/20220629130654id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-12
- document_id: d8408wgx
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14
  page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14
  lang: en
  template: drupal
  captured_at: '2022-06-26 16:48:49+00'
  capture_id: 726873
  wayback_url: https://web.archive.org/web/20220626164849id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: d8408wgx
  capture_id: 726877
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
  wayback_url: https://web.archive.org/web/20220812055309id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-born-gods-2014-02-14-0
  captured_at: '2022-08-12 05:53:09+00'
  template: drupal
  sha256: 660b6259ea68776307a13f6d3809fa285ba48f9764fca062b79777adb456db51
render_recovery: []
---
![](https://i.ormos.uk/b5/69/b56930fc690389f4a31ddc6cc2f9f6adab6bb27f573708aea3383f83e7fa39fc.jpg)

It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track **Magic** cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and development processes, and a few laughs. You'll find both here.

But first, the cast of characters:

![](https://i.ormos.uk/cc/88/cc886ad1801d000e9f8ccad3e73a31d571306e9ce45cdc656ac198f23d06f9f0.jpg)

**AF**—[Aaron Forsythe](https://web.archive.org/web/20140509102153/http://www.wizards.com/magic/magazine/archive.aspx?author=Aaron%20Forsythe)  
 The Boss

![](https://i.ormos.uk/0c/2e/0c2ec35cadd8d91b0e21792e890f054cbaad34d40898af342c3a5db8370fc72c.jpg)

**BM**—[Billy Moreno](https://web.archive.org/web/20140509102157/http://www.wizards.com/magic/magazine/archive.aspx?author=Billy%20Moreno)  
 Former **Magic** Developer

![](https://i.ormos.uk/a3/b8/a3b88e7d7f0d7e9bc111f4e1149c808d9a8720ad945e30ef48046e924f760e83.jpg)

**DB**—[Doug Beyer](https://web.archive.org/web/20140518165222/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Doug%20Beyer)  
**Magic** Senior Creative Designer

![](https://i.ormos.uk/fe/34/fe34bda5f19bc3c257197e6e13ef131ad3249ccc12e6e4a5d8ec4733970954fe.jpg)

**DE**—Dan Emmons  
**Magic** Designer

![](https://i.ormos.uk/ef/72/ef720e25ac1b4ff1389d81c9977841b7deca7e5cf8d15df7528af1b3635b7ad0.jpg)

**DH**—[Dave Humphreys](https://web.archive.org/web/20140509102202/http://www.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humphreys)  
**Magic** Development Manager

![](https://i.ormos.uk/95/14/951499aa2166025f23f1dadec10c5b834d7d69f4f919392cdf310c9250e80713.jpg)

**DOH**—Dan Helland  
**Magic** Design Coordinator

![](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg)

**EVL**—[Erik Lauer](https://web.archive.org/web/20140430170951/http://www.wizards.com/magic/magazine/archive.aspx?author=Erik%20Lauer)  
 Head Developer

![](https://i.ormos.uk/89/be/89be87cd13e85cdfa6301f157dc41afff82903d838483860ee14e4361d9d5e30.jpg)

**GSV**—[Gavin Verhey](https://web.archive.org/web/20130630084544/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Gavin%20Verhey)  
**Magic** Experience Designer and ReConstructed Columnist

![](https://i.ormos.uk/82/2b/822b917034ff4543ec86ea9e0a479c80f7232f507471856a098422ca9b0c809b.jpg)

**ID**—Ian Duke  
**Magic** Developer

![](https://i.ormos.uk/73/dc/73dc2c209bef80978eea09781f3075d348fa6472480299108af0945ff889dce7.jpg)

**Ken**—[Ken Nagle](https://web.archive.org/web/20140327225845/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ken%20Nagle)  
**Magic** Designer, Lead Designer for *Born of the Gods*

![](https://i.ormos.uk/36/2b/362b9b8902548d4692f09924d01f0429d5ba1494d3c33b8acce1eeff05988df7.jpg)

**Max**—[Max McCall](https://web.archive.org/web/20140508203101/http://www.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)  
**Magic** Digital Developer

![](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg)

**MR**—[Mark Rosewater](https://web.archive.org/web/20140508203058/http://www.wizards.com/magic/magazine/archive.aspx?author=Mark%20Rosewater)  
**Magic**'s Head Designer

![](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg)

**SPS**—[Sam Stoddard](https://web.archive.org/web/20130927012952/http://www.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard)  
 That's a-me

![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg)

**TML**—[Tom LaPille](https://web.archive.org/web/20140508201555/http://www.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)  
**Magic** Developer, Lead Developer for *Born of the Gods*

 

![Pain Seer](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pain+Seer)

 

KEN 1/21/2013: I've had lots of fun optioning this and its strong motivator to attack.  
 Max 2/6: This guy has places to go and people to see.  
 MR 4/17/13: My, we've come a long way since *Innistrad*.  
 SPS 5/6/13: Jiro dreams of card advantage.  
 TML 5/7/13: Please put that in an LD.

Done.

![Raised by Wolves](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Raised+by+Wolves)

 

TML 8/3/2012: Cute.  
 TML 9/27/2012: Tweaked for curve.  
 TML 10/5/2012: I like this card for the blue-green bounce Auras thing, but 2/2 green tokens are boars.  
 TML 10/31/2012: Now back to wolves.  
 SPS 11/15/12: Putting this on my opponent's guys is sometimes correct, and a horrible/bizarre play. Only thing I dislike about this card.  
 TML 10/31/2012: Now back to wolves.  
 TML 11/26/2012: Enchant creature you control? Trying something here.  
 TML 11/28/2012: Hoping this can create two wolves.  
 DE 1/3/12: Can't decide if I love or hate this card. I think I love it.  
 Max 1/8: I love it  
 AF 1/28: It exists to be loved, and I love it. Also, it seems really powerful.  
 KEN 2/28/2013: Is green 5-drop heavy on ASPLAYED? I had this, 2x lifegain tribute common, and Stomphowler tribute, and more 5-drops in Sealed, had to cut the 2x lifegainers.  
 TML 3/18/2013: Added GG when the spider lost it.  
 MR 4/17/13: Do we want to move this away from wolves as the impetus for this card is a Roman myth and not a Greek one?

[As Mark mentioned](/en/articles/makingmagic/2014/02-03-born-to-be-compiled-part-2), the raised by Wolf myth is primarily known as being a Roman myth, and not Greek, but we deemed it more important to meet expectations rather than be 100% accurate. I do still love when this was making Boars, though.

![Charging Badger](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Charging+Badger)

 

\[Playtest name Grumpy Badger\]  
 SPS 11/15/12: I will be forever sad if this card name changes.  
 TML 11/26/2012: You will probably be forever sad by the end of editing. :)  
 TML 12/12/2012: SO GRUMPY  
 Max 2/6: I don't get it.  
 TML 2/18/2013: Put Auras on it!

Sometimes, the hardest part about making cards is giving up on favorite playtest names.

![Scourge of Skola Vale](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scourge+of+Skola+Vale)

 

GSV 02/08/13: Haumph!

I would've also accepted Om nom nom nom.

![Ashiok's Adept](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ashiok%27s+Adept)

 

Max 1/8: I am sad to see another black heroic card that punishes me for completing my quest.  
 TML 1/8/2012: It is what black heroic creatures do in *Theros*. This one has been fun enough so far for a relatively throwaway card.  
 Max 2/6: Why is this symmetrical? Reads like downside.  
 ID 2/8/13: Agree. All the black heroic guys are symmetrical so far, and I never want to bother trying to trigger them. I think this would be way more fun as one-sided and a 2/2, for example.  
 TML 2/8/2013: This is just what black heroes do up to this point. Should we reevaluate that?  
 Max 2/18: I think so. I'm actively not interested in targeting this guy.  
 TML 3/4/2013: Moving to 1/3 and each opponent. Hooray for asymmetry.

This was a change that happened partway through development of *Theros*. In the original version, all the black heroic was both players, but as we worked on the set, we decided to push [Agent of the Fates](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agent+of+the+Fates) away from both player sacrificing a creature, to only an opponent. At that point, things just kind of fell into place, and the other black heroes were able to change their abilities in the same way.

![Fate Unraveler](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fate+Unraveler)

 

AF 1/25: Feels like it wants to make them lose life.  
 TML 1/30/2013: [Kederekt Parasite](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) and [Underworld Dreams](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Dreams) both go this way.  
 DB 2/19/2013: Agree w/ AF that this feels like it should be life loss, not damage. [Underworld Dreams](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Dreams) is too old to be precedent and [Kederekt Parasite](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kederekt+Parasite) requires a red permanent to deal its damage. Cool card though.  
 DH 3/5: Concur with above about this being life loss even though [Underworld Dreams](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Dreams) doesn't.  
 BM 3/5/13: I like that damage allows interaction with PWs. Life loss used to have benefits in world with COPs, now it's just less useful damage. Life loss is still useful for drawback text (see Plague Demon).  
 TML 3/7/2013: Made it life loss. Any defenders of damage other than Billy?  
 SPS 3/8/13: I will speak for Billy.  
 DOH 4/18/13: Agree with Billy. I like the effective hat tip to Hexmage. We still use [Vicious Hunger](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vicious+Hunger) effects anyway.  
 TML 5/3/2013: Damage so it gets Planeswalkers.  
 SPS 5/6/13: I enjoy this change.

As is often the case, people will often have differing opinions on cards based on aesthetics vs. functionality. This is one where we have been debating as a group for a while about how black's color pie should be evolving over time. Life loss, which used to be better than damage, is now worse due to the interaction with Planeswalkers. On the other hand, we try to make sure that black and red feel different as colors, which necessitates black getting some amount of life loss.

[Fate Unraveler](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fate+Unraveler), which was trying to match [Underworld Dreams](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Underworld+Dreams)'s template, ran into the problem of looking not a lot like a card we would do today. In the end, the upside of interacting with Planeswalkers was seen as more important than this one card feeling different than a red card.

![Loyal Pegasus](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Loyal+Pegasus)

 

KEN 6/19/2012: Now W 2/1 flying attacks in tandem, theorycraft [Ember Beast](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ember+Beast) as a white card.  
 SPS 10/1/12: Love this card. I like supporting going wide instead of just tall.  
 ID 10/12: Similar to [War Falcon](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=War+Falcon) but cleaner and more reprintable. I like it.  
 AF 1/10: This ability has only ever been red. I feel like this deserves 5 minutes at Cardcrafting.  
 TML 1/16/2013: Cardcrafting approves expansion into white.

In another example of a card that spurred enough of a discussion to go into Cardcrafting. The result—white gets to do this, now!

![Great Hart](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Great+Hart)

 

TML 11/9/2012: Pumped up to 2/5 for blue-white.  
 SPS 3/8/13: Take that, [Pillarfield Ox](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox).  
 TML 3/8/2013: Now [Pillarfield Ox](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillarfield+Ox).

The Tom giveth, and the Tom taketh away.

![Black Oak of Odunos](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Black+Oak+of+Odunos)

 

TML 11/28/2012: To 2B so you can combine it with other colors' dreamweavers more easily.  
 TML 12/12/2012: Now just B to activate.  
 TML 12/19/2012: Now 0/5 so it doesn't float freely to only inspired players.  
 AF 1/25: Added "untapped."  
 MR 4/18: I don't mind the bleed but this ability is normally in green. Black usually sacrifices creatures while green taps them.  
 TML 4/19/2013: Inspired needs this.

In *Born of the Gods*, black and blue were the two main inspired colors and needed a few extra cards to help them take advantage of that fact. In this case, Black Oak's ability isn't what we normally think of as black, but it worked in the context of the set.

![Reap what is Sown](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Reap+what+is+Sown)

 

KEN 6/12/2012: New card. For GW Heroic growing guys.  
  
  
 New card  
 XGW  
 Instant  
 Put a +1/+1 counter on each of X target creatures.  
  
 SPS 10/1/12: Had heroic in limited. Worked well. Mission accomplished.  
 TML 10/16/2012: Pumped up to get an A.  
  
  
 New card  
 X1GW  
 Instant  
 Put two +1/+1 counters on each of X target creatures.  
  
 Max 2/6: In my head I can't imagine winning games where my opponent casts this mid-combat.  
 ID 2/8/13: This reads strong enough as a sorcery, I think.  
 TML 2/12/2013: New version.  
  
  
 Reap What Is Sown  
 1GW  
 Put a +1/+1 counter on each of up to three target creatures.  
  
 ID 2/18/13: Cool. Like this a lot.  
 TML 4/17/2013: Now up to three instead of any number of.

 

As part of the gold cards in the set, [Reap What Is Sown](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reap+What+Is+Sown) went through a few variations, depending on how strong we wanted it to be. We knew we wanted the card to be strong enough to be an "A" (i.e., stronger than a [Wind Drake](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wind+Drake)), but we also wanted to keep it below the level of cards like [Overrun](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun). The goal was to be an anchor, not to dominate the draft. The second version of the card proved to be pushed too hard, so we pulled back a bit, and ended up with the version you can see today.

![Archetype of Finality](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Archetype+of+Finality)

 

TML 10/4/2012: Trying static abilities one last time.  
 TML 10/5/2012: Got meaner to numbers.  
 TML 12/12/2012: Now extra ability!  
 GSV 12/17/12: This guy seems brutal and not particularly fun. "All of my creatures trade with all of yours" makes size carry little relevance. It's especially brutal in a block with so many Auras.  
 TML 12/19/2012: Now worse due to being unfun. Was 3BB.  
 ID 2/4/13: Brutal to try to beat this without spot removal. There are also lots of ways to recur enchantments, especially in BW.  
 TML 2/4/2013: To 2/3 from 2/4.  
 KEN 4/2/2013: Had a super awesome game where this trumped my opponent's THS Gorgons that can't kill Gorgons and also lost deathtouch.

It's important to make sure that when we are pushing cards, we do it on cards that are fun. More than any other of the Archetypes, Finality proved to risk being incredibly unfun in Limited. As a result, we kept increasing the cost and decreasing the toughness until it got to a point where you would still play it, but it wouldn't dominate every game where it was drawn. The card serves the role we wanted it to, and is at the right level of miserable.

![Swordwise Centaur](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swordwise+Centaur)

 

KEN 3/27/2013: Power uncreep!  
 TML 4/2/2013: I don't want GG 3/3 common.

While [Swordwise Centaur](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Swordwise+Centaur) is, in fact, less powerful than [Kalonian Tusker](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kalonian+Tusker), we need to balance for Limited, and green common wanted a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/green.gif) vanilla to help out green devotion. We are careful about doing too many "strictly betters" and "strictly worses" but with the number of cards we have to make every year, some of that will just happen.

![Eye Gouge](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Eye+Gouge)

 

KEN 8/13/2012: Revived this dead FRI flavor removal design.  
 DH 8/29: Lol  
 AF 9/27: :)  
 SPS 10/1/12: God, I love this card.  
 MJG 10/10/12: Hehe!  
 TML 1/10/2012: New template from Tom Jenkot.  
 AF 1/25: Adorable!  
 MR 4/17/13: I am very happy this card found a home later in the block.

Often during the design process, there are cards that are wonderful, but just don't make it into sets, as [Eye Gouge](https://web.archive.org/web/20140214000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eye+Gouge) was to *Theros*. Luckily, Ken saved this one from the dead, and brought it to *Born of the Gods*.

* * *

Well, that's it for this week's edition. I hope you enjoyed it. Join me next week as we get ready for Pro Tour *Born of the Gods*.

Until next time,

Sam ([@samstod](https://twitter.com/@samstod))
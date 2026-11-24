---
id: q448kmme
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/05-09-the-m-files-journey-into-nyx-part-1-wub
title: 'The M Files: Journey into Nyx, Part 1 (WUB)'
published: '2014-05-09'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
    lang_detected: en
    capture_id: 727022
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
    captured_at: '2022-08-12 17:54:36+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
    lang_detected: en
    capture_id: 727022
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
    captured_at: '2022-08-12 17:54:36+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
    lang_detected: en
    capture_id: 727022
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
    captured_at: '2022-08-12 17:54:36+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
    lang_detected: en
    capture_id: 727022
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
    captured_at: '2022-08-12 17:54:36+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: q448kmme
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
  page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
  lang: en
  template: drupal
  captured_at: '2022-08-12 17:54:36+00'
  capture_id: 727022
  wayback_url: https://web.archive.org/web/20220812175436id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
- document_id: q448kmme
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09
  page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09
  lang: en
  template: drupal
  captured_at: '2022-01-21 09:39:51+00'
  capture_id: 727019
  wayback_url: https://web.archive.org/web/20220121093951id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: q448kmme
  capture_id: 727022
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
  wayback_url: https://web.archive.org/web/20220812175436id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-1-wub-2014-05-09-0
  captured_at: '2022-08-12 17:54:36+00'
  template: drupal
  sha256: 97d7a1aaf94d629946a83698004e9182b6bf7daf2900858962ba03a5682c8d27
render_recovery: []
---
![](https://i.ormos.uk/b5/69/b56930fc690389f4a31ddc6cc2f9f6adab6bb27f573708aea3383f83e7fa39fc.jpg)

It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track **Magic** cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and development processes, and a few laughs. You'll find both here.

*Journey into Nyx* had a lot of great comments in Multiverse, so I am going to actually break this up into two articles to make sure I can get more of them in.

But first, the cast of characters:

![](https://i.ormos.uk/cc/88/cc886ad1801d000e9f8ccad3e73a31d571306e9ce45cdc656ac198f23d06f9f0.jpg)

**AF**—[Aaron Forsythe](https://web.archive.org/web/20140509102153/http://www.wizards.com/magic/magazine/archive.aspx?author=Aaron%20Forsythe)  
**Magic** Senior Director

![](https://i.ormos.uk/a2/de/a2de2be32832ed87f46667ab3a3f163734724710b773497b2812a0b05c61c658.jpg)

**BH**—Ben Hayes  
 Developer

![](https://i.ormos.uk/a9/0c/a90c93246e1c543ad1616b44e6648d77c13eeeea6364f3d3e7fbe09ed759b875.jpg)

**DEL**—Del Laugel  
**Magic** Senior Editor

![](https://i.ormos.uk/fe/34/fe34bda5f19bc3c257197e6e13ef131ad3249ccc12e6e4a5d8ec4733970954fe.jpg)

**DE**—Dan Emmons  
**Magic** Designer

![](https://i.ormos.uk/ef/72/ef720e25ac1b4ff1389d81c9977841b7deca7e5cf8d15df7528af1b3635b7ad0.jpg)

**DH**—[Dave Humphreys](https://web.archive.org/web/20140509102202/http://www.wizards.com/magic/magazine/archive.aspx?author=Dave%20Humphreys)  
*Journey into Nyx*'s Lead Developer and Development Manager

![](https://i.ormos.uk/71/7e/717ec8ea013fe26416594283aa203c8c086fe7db5bfeb02641f7c432994f20bb.jpg)

**EEF**—[Ethan Fleischer](https://web.archive.org/web/20131214045930/http://www.wizards.com/Magic/Magazine/Archive.aspx?author=Ethan%20Fleischer)  
*Journey into Nyx*'s Lead Designer

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
**Magic** Designer, lover of fatties

![](https://i.ormos.uk/36/2b/362b9b8902548d4692f09924d01f0429d5ba1494d3c33b8acce1eeff05988df7.jpg)

**Max**—[Max McCall](https://web.archive.org/web/20140508203101/http://www.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)  
 Former **Magic** Digital Developer

![](https://i.ormos.uk/92/ce/92ceeab73eb3a7f33920535b070768559eb14c5b512cccee052bbb624575be15.jpg)

**MJG**—Mark Globus,  
**Magic** Senior Producer

![](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg)

**SPS**—[Sam Stoddard](https://web.archive.org/web/20130927012952/http://www.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard)  
 That's a-me

![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg)

**TML**—[Tom LaPille](https://web.archive.org/web/20140508201555/http://www.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)  
**Magic** Developer

![Akroan Mastiff](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Akroan+Mastiff)

 

ID 2/11/13: Tappers are brutal in this block, with all the "go tall" mechanics.  
 DH 2/25: We can reduce rates on this but we are intentionally pushing back some on going so tall.  
 TML 2/26/2013: I like this.

As I mentioned in [my recent mailbag article](/en/articles/latestdevelopments/2014/04-25-journey-into-the-mailbag), [Akroan Mastiff](https://web.archive.org/web/20140509000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Akroan+Mastiff) was intended for Limited, not to be too strong against regular Limited strategies, but instead to punish people attempting to go tall—which has been the defining characteristic of the block so far.

![Dictate of Heliod](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Dictate+of+Heliod)

 

DH 2/21: New card for flash symmetric cycle.  
 DH 2/25: Rule of Law variant at 2WW had some enemies. Trying Anthem instead.  
 TML 2/26/2013: Hooray!  
 SPS 3/8/2013: Strong.  
 DH 3/12: Looking to differentiate more from Heliod's Weapon. Moved up numbers. \[*At this point, the card cost 2WW and gave all of your white creatures +2/+2* —Sam\]  
 EEF 3/14/13: Rawr! Git 'em!  
 TML 3/28/2013: Hope this works out.  
 DH 4/2: Still happy with this if it is 3WW and we delete 'white'. Wondering if I should do that preemptively?  
 TML 4/4/2013: I'd let it break first.  
 DH 4/9: Moved to 5 mana and now all your creatures, not just white ones.

It didn't take long when testing with the ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless2.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) version to really push the white aggro decks over the top. I think we found a much more interesting cost—one where you probably will run a few, but probably not run four in every weenie deck.

![Sightless Brawler](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sightless+Brawler)

 

EEF 9/26/12: New card.

As an aside, the original version of the "downside bestow" cycle started off as an even larger downside—they didn't even add to the power and toughness of the creatures. So, this card said that the creature couldn't attack, but didn't give it an extra power and toughness. If for some reason that creature died, then you would end up with a defender. It was an interesting attempt at how to make bestow feel new, but one that was very confusing because of how different it was from the original versions.

EEF 11/13/12: Bestow 1W → 2W.  
 MJG 1/8/13: It is really weird to me that these bestow creatures don't provide p/t.  
 AF 2/8: I can sort of accept this being a Magic card, but I have a hard time accepting it as a common. I imagine that's true for all negative-bestow guys. They require such high levels of understanding things.  
 EVL 2/11: I think the "unusual common" aspect would be acceptable if I enjoyed the game play enough, but I don't think the tradeoff is good in this case.  
 DH 2/25: Moved common negative to uncommon.  
 Max 3/18: Oh I actually like this card.  
 DH 3/29: Not ideal, but adorable in some ways. Wouldn't like this if they all looked this way.  
 DH 3/29: New power based on meeting idea from ID, given we are now apparently doing this in white too. Following model of using stats again, and usually putting on your own creatures but occasionally opponents.

The development that happened with the cards was to add back the power and toughness bonus but to change what the downsides were, so you were more likely to put it on your own creatures but could use it as a trick in a pinch against a creature an opponent controls.

![Banishing Light](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Banishing+Light)

 

EVL 4/26: Made into new-template Oblivion Ring for FFL purposes.  
 ID 4/29: If this is our first new template o ring, it may want a name that's not specific to the plane for reprint/core set.  
 GSV 4/30: Agree with ID. Was my first thought as well.  
 TML 5/1/2013: Agreed.

The card-naming thing here is an interesting thing. While it is creative's job to name cards, development tries to pick out cards we might want to reprint (in places other than core sets), and try to give them generic-enough names that we can use them in other sets when we need to. [Banishing Light](https://web.archive.org/web/20140509000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Banishing+Light) (like [Oblivion Ring](https://web.archive.org/web/20140509000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) before it) could be flavored to fit just about anywhere. If it was given a name like Heliod's Banishment, then we would've needed to create a second version of the card if we decided in two years that we needed the same card in Standard.

![Sage of Hours](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sage+of+Hours)

 

EEF 2/1/13: New card.  
 ID 2/4/13: Feels bad giving my guy -5/-5 to take an extra turn and then not be able to attack with him. Could put "take an extra turn" in the heroic trigger. "...put a +1/+1 counter on it. Then, if it has exactly three +1/+1 counters on it, take an extra turn after this one." Much harder to loop and now pure upside.  
 DH 2/5: Think this has room to be stronger, inclined to just try 4 counters. Think the exact wording still would be too easy to loop via removing/adding.  
 EEF 2/6/13: Five → four. Not sure how to reword it. I'll leave it to the dev team and the editors.  
 Del 2/26: Editing has no reason to suggest other words.  
 DH 3/14: 2U → 1U.  
 SPS 3/26: this +Ajani is just about game. Dangerous card is dangerous.  
 DH 4/2: Noted. We'd seen that interaction. Open to seeing what this does in FFL. It might need to be: "Remove all +1/+1 counters from CARDNAME: If you removed four or more counters this way, take an extra turn after this one." so you can't build it up and increment like with Ajani.  
 DH 4/9: And up to 5 counters.  
 DH 5/7: May want this to be remove some (4–5) counters and return to hand as a further knob. Cleaner way to make sure it doesn't accumulate too many extras.  
 ID 5/7: Returning to hand lets me attack into your blockers before taking an extra turn, without risk of him dying.  
 DH 7/10: Tweaked to always remove all counters. Decided to keep scaling to multiple turns for now. We can revisit.

Any time you have a card that is a repeatable [Time Walk](https://web.archive.org/web/20140509000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk) effect, you need to be pretty careful with it. Early versions were strong enough that we worried that, if we were wrong, it would be very easy to turn games with cards like Ajani into kill-this-now-or-you-die-fests, which really isn't good game play. I think we got the card to a point where you can take infinite turns if you want to jump through a lot of hoops, but there isn't a way to do it incidentally. It's awesome if working hard gets you cool things. It's less awesome if everyone is doing it just because it is powerful.

![Interpret the Signs](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Interpret+the+Signs)

 

DH 3/4: Trying to stick with concept. Does this work? Making a counterpart to Riddle of Lightning. Although this is the same basic effect as the Sphinx I just added at rare.  
 TML 3/4/2013: This is rad.  
 SPS 3/8/2013: This card is sweet, even if it butts up poorly with Opposition in M14.  
 ID 3/11: A satisfying mirror to Riddle of Lightning.  
 KEN 4/11/2013: The best moment of Riddle of Lightning is when the opponent sees you scry 3 to the bottom and knows there's a chance his creature will live. Can this be a Mana Leak or a 1-shot Counterbalance for a similar moment with a dramatic moment where my Lava Axe might still kill you?  
 TML 5/1/2013: I think that moment could still happen if someone gets two lands and a 2cc thing.  
 DH 5/13: 4CC → 5C.

One of the ways we get inspiration for new cards is from the past. We liked [Riddle of Lightning](https://web.archive.org/web/20140509000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riddle+of+Lightning) for the set, especially since it fit well into Keranos's flavor and the mechanics we were going for, with UR having a lot of scry. That cycle didn't have a great solution for blue, so we decided to make up a new card that felt like it would feel right next to Riddle.

![Pharika's Chosen](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pharika%27s+Chosen)

 

FUNCTIONAL REPRINT—Typhoid Rats—ISD  
  
 DH 2/20: 1/2 → 1/1. Functional Reprint.  
 TML 2/26/2013: We have this in THS though, right?  
 DH 2/26: We have a bestow DT at 1B. Different enough I think?  
 TML 3/4/2013: Yup, I think so.  
 SPS 3/8/2013: To me, I'm reminded of the G deathtouch in Theros, not the 1B DT  
 Max 3/18: G 1/1 deathtouch is in THS.  
 DH 3/18: That doesn't really bother me. Should it?  
 Max 3/21: It's another common that is super strong against tall strategies, and in general deathtouch creatures are I think boring.  
 TML 3/28/2013: This is what green-black graveyard decks need, so I think I'd keep it.

I also mentioned this briefly [last week](/en/articles/latestdevelopments/2014/05-02-making-enchantments-matter), but when you have a three-set block, it is hard to not have some overlap in cards. In this case, we had what is basically the same card in both green and black, but both fit individually.

![Worst Fears](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Worst+Fears)

 

DESIGN FAVORITE.  
  
 DH 2/21: Cut the extra turn for them. Added 2 mana.  
 TML 2/26/2013: Well then.  
 BH 3/6/2013: Wow, this card is exciting!  
 ID 3/11/13: Can't wait to cast this off of the tribute guy in BNG  
 KEN 4/4/2013: Now I know to give ID big tribute guys.  
 DH 7/19: 6BB → 7B. Cutting some CC from high rarity.

This card started off cheaper, but your opponent got an extra turn—so it didn't have the "[Time Walk](https://web.archive.org/web/20140509000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Time+Walk)" part of [Mindslaver](https://web.archive.org/web/20140509000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver). The wording was both confusing and meant that the card was much more narrow, so we changed to the newer, actual-[Mindslaver](https://web.archive.org/web/20140509000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mindslaver) text.

You also notice that this card is labeled "Design Favorite." One part of design handoff is that the design team indicates its favorite cards in the set—the ones it would like to see kept to maintain the integrity of the team's vision. It's not required that the development team keeps all of them, especially as-is, but it's important for the development team to do as much as it can to keep the cards in the file, or at least make a good-faith effort to replace the card with something that fulfills the same design goals the design team is happy with.

That's all the space I have for this week. I'll be back next week... with Vintage Masters previews! But, the week after that, I have a sweet new *Conspiracy* card to show you! But in three weeks, I'll be back with the next edition of the M Files, including red, green, and gold, with the Gods of *Journey into Nyx*.
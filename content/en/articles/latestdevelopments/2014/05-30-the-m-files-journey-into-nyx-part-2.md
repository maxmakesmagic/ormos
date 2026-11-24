---
id: 2dy3aagz
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/05-30-the-m-files-journey-into-nyx-part-2
title: 'The M Files: Journey into Nyx, Part 2'
published: '2014-05-30'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
    lang_detected: en
    capture_id: 727023
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
    captured_at: '2022-01-22 02:03:56+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
    lang_detected: en
    capture_id: 727023
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
    captured_at: '2022-01-22 02:03:56+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
    lang_detected: en
    capture_id: 727023
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
    captured_at: '2022-01-22 02:03:56+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
    lang_detected: en
    capture_id: 727023
    url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
    captured_at: '2022-01-22 02:03:56+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 2dy3aagz
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
  page_key: magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
  lang: en
  template: drupal
  captured_at: '2022-01-22 02:03:56+00'
  capture_id: 727023
  wayback_url: https://web.archive.org/web/20220122020356id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 2dy3aagz
  capture_id: 727023
  url: https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
  wayback_url: https://web.archive.org/web/20220122020356id_/https://magic.wizards.com/en/articles/archive/latest-developments/m-files-journey-nyx-part-2-2014-05-30
  captured_at: '2022-01-22 02:03:56+00'
  template: drupal
  sha256: 73895ba5d830a9af053b2163ee74df078a2f2f8316c88501b5c6cc9e1b45b2f4
render_recovery: []
---
It's time once again to return to the Multiverse! Frequent readers of this column will know that Multiverse is our internal database used to track *Magic* cards already printed, early in design, and everything in between. One of the duties of being a designer or developer is making occasional passes on the cards in Multiverse and leaving comments. Looking back on the file a year later provides insights to the design and development processes, and a few laughs. You'll find both here.

But first, the cast of characters:

![](https://i.ormos.uk/cc/88/cc886ad1801d000e9f8ccad3e73a31d571306e9ce45cdc656ac198f23d06f9f0.jpg)  
 AF: [Aaron Forsythe](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Aaron%20Forsythe)—Aaron Forsythe, senior director for *Magic* and M15 Lead designer

![](https://i.ormos.uk/a2/de/a2de2be32832ed87f46667ab3a3f163734724710b773497b2812a0b05c61c658.jpg)  
 BH: Ben Hayes—*Magic* developer

![](https://i.ormos.uk/0c/2e/0c2ec35cadd8d91b0e21792e890f054cbaad34d40898af342c3a5db8370fc72c.jpg)  
 BM: [Billy Moreno](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Billy%20Moreno)—former *Magic* developer and M15 lead Developer

![](https://i.ormos.uk/a3/b8/a3b88e7d7f0d7e9bc111f4e1149c808d9a8720ad945e30ef48046e924f760e83.jpg)  
 DB: [Doug Beyer](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Doug%20Beyer)—*Magic* senior creative designer

![](https://i.ormos.uk/a9/0c/a90c93246e1c543ad1616b44e6648d77c13eeeea6364f3d3e7fbe09ed759b875.jpg)  
 Del: Del Laugel—senior *Magic* editor and editor manager

![](https://i.ormos.uk/89/be/89be87cd13e85cdfa6301f157dc41afff82903d838483860ee14e4361d9d5e30.jpg)  
 GSV: [Gavin Verhey](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Gavin%20Verhey)—*Magic* experience designer

![](https://i.ormos.uk/82/2b/822b917034ff4543ec86ea9e0a479c80f7232f507471856a098422ca9b0c809b.jpg)  
 ID: [Ian Duke](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Ian%20Duke)—*Magic* developer

![](https://i.ormos.uk/51/75/5175531e741eec9c640431a60d5accadcefe6a7f303b40a493b4f7af266d190c.jpg)  
 JCW: [Jennifer Clarke-Wilkes](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Jennifer%20Clarke-Wilkes)—*Magic* creative designer

![](https://i.ormos.uk/73/dc/73dc2c209bef80978eea09781f3075d348fa6472480299108af0945ff889dce7.jpg)  
 Ken: [Ken Nagle](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Ken%20Nagle)—*Magic* designer

![](https://i.ormos.uk/36/2b/362b9b8902548d4692f09924d01f0429d5ba1494d3c33b8acce1eeff05988df7.jpg)  
 Max: [Max McCall](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Max%20McCall)—former *Magic* digital developer

![](https://i.ormos.uk/f8/3b/f83b7c2d164a18a665378b13e7adec05a979b390fc07e360fae3fdfa6f560cab.jpg)  
 SM: [Shawn Main](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Shawn%20Main)—*Magic* designer; in charge of the Designer 15 cards

![](https://i.ormos.uk/10/d0/10d0efafaed92172c7bb146c04b6e71f82b6edbef0b7f8b7586ffbb4adaca9c1.jpg)  
 SPS: [Sam Stoddard](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=sam%20stoddard)—That's A-Me!

![](http://www.wizards.com/magic/images/mtgcom/authorpics/authorpic_stevewarner.jpg)  
 SW: Steve Warner—*Kaijudo* and *Duel Masters* developer; *Magic* playtester

![](https://i.ormos.uk/2c/11/2c11e3c83c00b431c9ce63bd3fec77756dcb56c64267c66df8a0bdfce240983d.jpg)  
 Tabak: [Matt Tabak](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Matt%20Tabak)—*Magic* editor and rules manager

![](https://i.ormos.uk/bc/df/bcdf4b16b64014da6e91f4589e9d89fc4a883b0d88977709b0ce75e68e8ef0a3.jpg)  
 TML: [Tom LaPille](https://web.archive.org/web/20140530000000/http://archive.wizards.com/magic/magazine/archive.aspx?author=Tom%20LaPille)— *Magic* developer

And now, on to the cards.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_devouringlight.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Devouring%20Light)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Devouring%20Light)

AF 11/18: Down from uncommon.  
 Max 11/30: Lots of exiling at white common.  
 TML 1/15/2012: This came out of nowhere to surprise me yesterday and that reminded me why this was uncommon, but I think it was cool how it happened and I could get used to it.  
 BM 3/7/13: Reverting to uncommon

One thing we often try with core sets is moving around the rarities on cards. [Devouring Light](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Devouring+Light), as it turned out, was more than we wanted for a common removal spell to have to constantly play around. It has been much more interesting as an uncommon.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_emhemeralshields.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ephemeral%20Shields)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ephemeral%20Shields)

AF 11/17: Might be only instance of protection in the set, which kind of bugs me. Could be a damage prevention spell.  
 Max 11/26: We should figure out how much protection we want to be doing in core sets. M13/M14 had similar issues  
 BM 8/12/13: Replacing protection with indestructible to simplify card and remove sad interactions with a player's own positive Auras.

Core sets attempt to be more simple than most sets, to give new players a better foothold in the game. Protection really goes against that, since many new players simply can't figure out what protection does without reading the rulebook—and many forget some of the implications. Giving your own creature protection and your Auras falling off, as an example. As a result, we have tried to move away from it

![](http://media.wizards.com/2014/images/cardheaders/cardheader_hushwinggryff.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hushwing%20Gryff)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hushwing%20Gryff)

KEN 4/15/2013: Commander needs [Torpor Orb](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torpor+Orb) redundancy bad.  
 AF 4/22: Needs stats. I'd like him to have some difference from [Aven Mindcensor](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aven+Mindcensor), unless we're really going to sell the link.  
 KEN 4/22/2013: BM verbally shopped it at 2/2, trying that.  
 AF 4/23: If he stays symmetrical (which I hope he does), he can have very aggressive stats.  
 SPS 5/6/13: Reality check: does this mess up anything big for Huey?  
 AF 9/13: Is it positive or negative that this guy looks so much like [Aven Mindcensor](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aven+Mindcensor)?  
 TML 9/13/2013: I think it is positive. People like these goofballs.  
 GSV 10/4: Cool card. I'm interested to see what this does to the Modern [Birthing Pod](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Birthing+Pod) mirror.

Interesting story: We tried out a [Torpor Orb](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Torpor+Orb) guy in M14, but at the time, bestow had the creature enter the battlefield, then turn into an Aura and "snap" onto an opposing creature. Not wanting to accidentally nuke one of the big mechanics from the next set BEFORE we even had a chance to do much design work, that card became [Imposing Sovereign](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imposing+Sovereign). We were a little more confident that [Hushwing Gryff](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hushwing+Gryff) wouldn't blow up everything in "Huey" year, so we went with a design that we felt would be interesting for it and provide some more depth for Standard, Modern, and maybe even Legacy.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_markedforhonor.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Marked%20for%20Honor)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Marked%20for%20Honor)

BM 12/15/12: 2W → 3W for Limited  
 BM 3/7/13: 3W → 2W for quickpointing balancing.  
 BM 8/12/13: 2W → 3W. Card is too swingy at 3cc. Curves more satisfyingly with [Heliod's Pilgrim](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Heliod%27s+Pilgrim) this way too.

As always, getting sets to work for Limited involves a lot of fine tuning and work to get the set to the right point. Things will often move up and down in power not based on the card itself being broken, but getting the environment as a whole to work better.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_pillaroflight.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Pillar%20of%20Light)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Pillar%20of%20Light)

BM 8/12/13: Replacing [Smite the Monstrous](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Smite+the+Monstrous) to break through cards like [Wall of Swords](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Swords) and [Wall of Frost](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall+of+Frost), while still dealing with most bombs.

A new thing we are trying out with white—hating big numbers! White has done this before, with cards like [Reprisal](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reprisal), but trying it out with toughness gives us some new ways for white to get interesting removal and to better tweak balancing for Limited.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_spiritbonds.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Spirit%20Bonds)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spirit%20Bonds)

ID 3/25: Super cool design!  
 BM 4/8/13: Now makes 1/1 white Spirit to consolidate tokens while maintaining power level.  
 BM 6/5/13: Now only protects non-Spirits.  
 BM 7/24/13: Adding W to activation for FFL.  
 BM 8/12/13: Changing ETB trigger to look for non-Spirits instead of nontokens...trying to line up all of the limitations on the card for minimal cognitive load. Looking for FFL feedback on change in power level.  
 BM 9/22/13: 99ed.  
 AF 9/13: What? And this does not look playable to me.  
 TML 9/13/2013: It wasn't particularly fun at lower numbers.  
 Del 10/7: EVL says mana cost 2W →1W, activation cost W → 1W

When we started working on the outside-designer cards for *Magic 2015*, we knew we would have to do some tweaking for them—we wanted cards that were fun and interesting, but wouldn't be over the line for how we usually print cards.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_aeronauttinkerer.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Aeronaut%20Tinkerer)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aeronaut%20Tinkerer)

Max 11/30: This is a C to A upgrade if you turn it on.  
 DH 12/17: It is our definition of a B so guessing it's not a C→A. :P  
 SPS 1/28/13: Wouldn't 2/3 flying be an A too? Is it possible this just wants to gain flying instead of the bonus as well?  
 BM 1/29/13: It is. Definitely an option if we find blue is too strong.  
 BM 3/7/13: Loses +1/+0 for quickpointing Limited rebalancing.

Getting rewards to work properly on build-around commons is hard.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_chasmskulker.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Aeronaut%20Tinkerer)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Aeronaut%20Tinkerer)

BM 1/25/13: Designer card from Mike Neumann. Cthulhu-inspired ancient horror that explodes into a pile of nastiness.  
 BM 1/25/13: Moved to blue to line up with Neumann's request. Replacing Submerging Leviathan as intro pack/Prerelease rare.  
 TML 2/7/2013: Now a death trigger.  
 BM 2/27/13: Adjusted stats and death trigger per miniteam suggestions. Now only counts +1/+1 counters for death trigger.  
 BH 3/6/13: I love the story this card tells but would be more excited if it had a scarier death trigger—would happily accept weaker base stats. Maybe # of Squids = X\*2 the # of counters?  
 AF 3/7: Fun card. Goes well with [Master of Waves](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Master+of+Waves) in the "tokens are blue now" deck :)  
 ID 3/25: Much more appealing now that it doesn't cost a billion.  
 BM 4/9/13: 3UU 4/4 → 1UU 2/2 to push for Constructed.  
 DB 4/10/2013: Now it's teensy. That change makes it hard to keep this concept as a giant Cthulhoid monster (compare to the designer's desired visual, below). Even 3/3 would help...  
 AF 4/22: "Cthulhu Hatchling"  
 KEN 4/26/2013: In D15, tried [Polymorph](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Polymorph)ing a 7/7 this guy into an Emrakul. Whiffed, but the Squids finished the job thanks to [Keep Watch](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Keep+Watch).  
 BM 4/30/13: Got Neumann's OK on this being smaller. Leaving it this way for FFL. Added islandwalk to token.  
 BM 6/18/13: 1UU 2/2 → 2U 1/1 for FFL  
 BM 6/27/13: 2U → 1UU for FFL  
 SW 7/19: Love this card.  
 AF 8/19: If this needs a subtle push, it could say "Sacrifice ~: Put X ..."  
 Del 10/14: Mana cost 1UU → 2U (devotion).

[Chasm Stalker](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Chasm+Stalker) is one of several cards in *Magic 2015* that was made "weaker" by removing colored mana symbols, which is usually the opposite of how things work. Devotion does weird things.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_encrust.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Encrust)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Encrust)

AF 8/7: This [Assassinate](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Assassinate) feels a little similar.  
 BM 8/12/13: Replacing [Assassinate](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Assassinate).

We want the removal in our sets to feel different from each other. Aaron rightfully pointed out that this and [Assassinate](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Assassinate) are rewarding the same thing—attack me, I take one hit then keep you locked down. Separating how blue and black killed creatures means that we can make the decks feel different. [Assassinate](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Assassinate) changed because of how much easier it is to find satisfying removal in black and because [Encrust](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Encrust) was doing good work against all the artifacts in the set.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_ensoulartifact.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ensoul%20Artifact)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ensoul%20Artifact)

Max 10/1: [Ornithopter](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter) earns his paycheck in this set.  
 TML 11/6/2012: I adore this, but I would be ready to throw it out if we had to use the [Animate Artifact](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Animate+Artifact) template.  
 AF 11/17: This template is legit.  
 Max 11/30: What happens if I enchant a 6/6 artifact creature with this?  
 AF 12/3: It's a 5/5. Just as if UB Tezzeret targeted it.  
 BM 8/15/13: 2U → 1U. How onerously high variance is the [Ornithopter](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter) god draw?  
 TML 8/22/2013: This is much more appealing now that [Darksteel Citadel](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Darksteel+Citadel) exists.

Here we see the base power and toughness template helping out make cards like this make more sense to newer players.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_frostlynx.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Frost%20Lynx)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frost%20Lynx)

BM 8/22/13: 2/2 → 2/3 to try to move into top 3.  
 TML 9/5/2013: Back to 2/2 to try to let aggro back in.

Part of the process for balancing Limited that we do is making sure that the top three commons for each color are relatively close to each other, so the colors have reasonable balance. There are plenty of old sets where this did not happen (*Urza's Saga* and *Onslaught* come to mind) where one color has something like five of the top ten commons. Spreading out the balance is important, and it means that even if we are wrong on a few things, the overall Limited experience shouldn't be totally out of whack.

For [Frost Lynx](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Frost+Lynx), we tried a stronger version, but found that it pushed blue too hard. So we moved him back to a 2/2 (and now a mirror of [Kor Hookmaster](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kor+Hookmaster)), which is still plenty strong, but made it so blue no longer totally brick-walled all of the Aggro decks in the format, which we knew was a problem with *Magic 2014*.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_glacialcrasher.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Glacial%20Crasher)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Glacial%20Crasher)

\[Playtest name was Reclusive Yeti\]  
 TML 11/29/2012: I called, but you ran to the forest.  
 Max 11/30: I like this card independent of context but it doesn't do a ton for the set.  
 Tabak 1/24: It's a little weird that in multiplayer I can attack mono-blue opponent if some other opponent has a Mountain. Not bad, just weird. Intentional?  
 BM 3/18/13: Victim of resonance pass. Couldn't straight-face our way through the story here.  
 BM 4/30/13: He's back.  
 TML 5/13/2013: We pushed you away, Yeti, but you begged for it.  
 TML 7/12/2013: He ran to the forest. :(

Tom LaPille, ever the fan of

Bad Lip Reading videos.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_illusoryangel.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Illusory%20Angel)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusory%20Angel)

AF 10/16: Was [Phantasmal Dragon](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Phantasmal+Dragon). Wanted something that rewarded cheap attackers.  
 KEN 1/15/2013: Combo with [Ornithopter](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter).

The secret of M15—everything combos with [Ornithopter](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ornithopter).

![](http://media.wizards.com/2014/images/cardheaders/cardheader_polymorphistsjest.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Polymorphist%27s%20Jest)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Polymorphist%27s%20Jest)

AF 9/13: *(Horses aren't creatures.)*

Well, duh.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_turntofrog.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Turn%20to%20Frog)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turn%20to%20Frog)

ID 10/17: There's been talk of now associating "lose all abilities" on cards like this with a creature type change. It's a shame that [Ovinize](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ovinize) proper doesn't make it a Sheep.  
 TML 11/6/2012: We made [Turn to Frog](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Turn+to+Frog) to try to do this correctly.  
 AF 11/18: Done. Was [Ovinize](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ovinize).  
 AF 3/7: Two versions of this in the same set: feature or bug?  
 BM 3/7/13: Been treating it as a feature.

The original version of [Polymorphist's Jest](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Polymorphist%27s+Jest) was called Mass Turn to Frog in a very D&D way of having both the single-target and hitting-everything version of the spell. We are also much happier with the template of "base power and toughness" moving forward to help people understand what this class of cards do. Hooray!

![](http://media.wizards.com/2014/images/cardheaders/cardheader_bloodhost.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Blood%20Host)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Blood%20Host)

AF 11/6: I like this guy, but I want it on record that we should revisit [Fallen Angel](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fallen+Angel) someday.  
 TML 11/6/2012: HAUMPH  
 SM 11/27: Tests have determined that, like Alf, this guy enjoys eating cats.

Fortunately, [Black Cat](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Black+Cat) survived all the way through the development process, so the above comments make sense. Hooray!

![](http://media.wizards.com/2014/images/cardheaders/cardheader_carrioncrow.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Carrion%20Crow)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carrion%20Crow)

BM 12/15/12: 3B → 1BB, ETB tapped for Limited curve.  
 BM 1/11/13: 1BB 2/3 → 2B 2/2 to ding black  
 BM 7/26/13: Reverting to 1BB → 2/3 to boost black.  
 SPS 8/2: Back to 2B. Too much BB in black.  
 SPS 8/9/13: AAAAAND back to 2/2. I feel like we've been here before.

Time is a flat circle, etc.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_caustictar.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Caustic%20Tar)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Caustic%20Tar)

TML 1/22/2013: Our rhyming couplet reminder text count is pretty low without this.  
 AF 3/7: I will Pilgrim for this!  
 JCW 7/3: New art; might require new flavor text since the Cabal is from Dominaria.

Sorry, Tom. We can't rhyme all the time.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_covenantofblood.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Covenant%20of%20Blood)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Covenant%20of%20Blood)

SM 9/6: Love this.  
 AF 11/30: Will you love it more now that it is 8 mana? (was 7) This was too good a finisher in creature-light control decks.  
 Max 11/30: Expensive convoke removal spells make it hard to use them to push through damage. The messaging here is confusing.  
 BM 12/15/12: Need A's. 6BB → 5BB. Better behave, Ritual. This is your last chance to be a 7cc spell.  
 TML 1/15/2013: It has behaved so far.  
 BM 3/7/13: 5BB → 3BBB for top-15, Limited balancing.  
 BM 7/26/13: 3BBB → 2BBBB to move down to solidly A.  
 SPS 8/2/13: Was too unappealing, hurting black. Trying at 5BB  
 SPS 8/9: Up to 6BB. New removal spell takes the place as best black common.  
 Del 9/29: 6BB → 5BB  
 Del 10/2: 5BB → 6B

Trying this at less mana but extra black mana symbols made it more powerful, but much less appealing. People just couldn't grasp how much easier the card was to cast with their black creatures, and that the ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) or ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif) just didn't keep them from casting it as much as they thought it would. In the end, we moved it to a higher casting cost, but fewer ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)s to make the card work better.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_ulcerate.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ulcerate)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ulcerate)

TML 11/6/2012: Somehow this works better for me as a concept if it's an additional cost, but the words are worse that way.  
 SM 3/15: Dude, I got acid all over me! Sure am clumsy.

This looks painful.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_unmakethegraves.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Unmake%20the%20Graves)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unmake%20the%20Graves)

BM 1/21/13: 1B → B  
 BM 2/6/13: Zombie → black to line up with new color lords as tertiary cycle of themes.  
 AF 2/14: Better than [Disentomb](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disentomb) in three ways.  
 SM 2/26/13: Looks so weird to me.  
 BM 3/7/13: Done  
 SPS 3/8/13: Shouldn't this be at least 2?  
 Del 9/29: B → 4B, one creature card → two creature cards

Ultimately, we need to be okay making better or worse versions of cards to fit the Limited environment, but this card was a bit too much. Originally, it was ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif), instant, with convoke, and if you returned a Zombie, your opponent lost 2. Being better than [Disentomb](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disentomb) isn't a problem, but we have to make cards for a long time in the future, and we could easily do the [Disentomb](https://web.archive.org/web/20140530000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Disentomb) where an opponent loses 2 life as a different card that is also interesting. Putting all of these on the same card just reduces design space in the future. Ultimately, we changed this even further to meet the Limited requirements of the set, and getting two creatures.

![](http://media.wizards.com/2014/images/cardheaders/cardheader_walloflimbs.jpg)[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wall%20of%20Limbs)](https://web.archive.org/web/20140530000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wall%20of%20Limbs)

BM 8/12/13: Changing from "B, Pay 2 life: +2/+2 until EOT" → new ability. Looking for another straight upside draw into the WB archetype.  
 BM 8/22/13: Added new proactive ability to pay off lifegain work.

We like to have uncommons that clearly reward people for doing things. Wall of Limbs was doing that as an uncommon, but it just wasn't clear enough to people. Putting on the trigger for lifegain makes that more obvious and helps the players who need the help in constructing their Limited decks.

That's all the space I have for this week. Next week, I will be back with the rest of the set!
---
id: v0fqgrsh
kind: article
lang: en
path: /en/articles/latestdevelopments/2011/02-04-a-better-creepier-world
title: A Better, Creepier World
published: '2011-02-04'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
    lang_detected: en
    capture_id: 718294
    url: https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
    captured_at: '2022-10-07 20:10:54+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
    lang_detected: en
    capture_id: 718294
    url: https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
    captured_at: '2022-10-07 20:10:54+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
    lang_detected: en
    capture_id: 718294
    url: https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
    captured_at: '2022-10-07 20:10:54+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
    lang_detected: en
    capture_id: 718294
    url: https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
    captured_at: '2022-10-07 20:10:54+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: v0fqgrsh
  url: https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
  page_key: magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
  lang: en
  template: drupal
  captured_at: '2022-10-07 20:10:54+00'
  capture_id: 718294
  wayback_url: https://web.archive.org/web/20221007201054id_/https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-04
- document_id: v0fqgrsh
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/128
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/128
  lang: en
  template: aspx
  captured_at: '2013-07-02 13:07:37+00'
  capture_id: 613003
  wayback_url: https://web.archive.org/web/20130702130737id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/128
- document_id: v0fqgrsh
  url: https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-03
  page_key: magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-03
  lang: en
  template: drupal
  captured_at: '2022-07-05 15:11:50+00'
  capture_id: 718291
  wayback_url: https://web.archive.org/web/20220705151150id_/https://magic.wizards.com/en/articles/archive/latest-developments/better-creepier-world-2011-02-03
source_selection: An alternate source supplies a usable body or more table rows.
archive_source:
  document_id: v0fqgrsh
  capture_id: 613003
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/128
  wayback_url: https://web.archive.org/web/20130702130737id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/ld/128
  captured_at: '2013-07-02 13:07:37+00'
  template: aspx
  sha256: 01fd8c83aa886465eb2e8d8463021e73adbf1556d925e46bde1c24a573730e08
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void()
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - Sunblast Angel
  - Hoard-Smelter Dragon
  - Steel Hellkite
  - Carnifex Demon
  - Contagion Engine
  - Phyrexian Rebirth
  - Massacre Wurm
  - Black Sun's Zenith
  - Carapace Forger
  - Viridian Emissary
  - Priests of Norn
  - Rot Wolf
  - Tine Shrike
  - Blightwidow
  - Scourge Servant
  - Flesh-Eater Imp
  - Phyrexian Juggernaut
  - Giant Growth
  - Phyrexian Vatmother
  - Phyrexian Crusader
  - Plague Myr
  - Inkmoth Nexus
  - Skithiryx
  occurrences: 38
---
Erik Lauer recently gave me some wonderful advice about working on sets that get added to existing environments as opposed to being drafted on their own. As always, he said, I should try to make the set as good as possible for itself, but he suggested that I spend some time thinking about my least favorite parts of the previous environment. Every **Magic** developer was once a person who played tons of **Magic**. The things that I'm tired of after developing a large set are probably the same things that will annoy the most dedicated players by the time they've played with that set for three months. Doing things that solve my least favorite aspects about the big set preceding a small set will make those players happy.

He then blew my mind by telling me that this was the process he used while figuring out what to do with *Mirrodin Besieged*. I was on his development team, and yet I had no idea that this was going on inside his brain. In hindsight, though, it makes perfect sense, and I've put it into my bag of tricks for future development. It also explained the motivation behind several things that Erik did during *Mirrodin Besieged* development that I didn't understand at the time.

![](https://i.ormos.uk/90/4c/904c5bbe50fca84fc00c505c43b0fb702988b434fe571b338331a3e438da7aec.jpg) 

  

Before we begin, I should be clear that today's article is no slight against the *Scars of Mirrodin* development team. Mike Turian (who, by the way, has actually led the development of five **Magic** sets—I forgot *Worldwake* when [I introduced him](/en/articles/latestdevelopments/2011/01-21-development-under-siege) two weeks ago!) is a metaphorical giant, and without standing on the collective shoulders of him and the rest of his development team, we would not have been able to create what we did in *Mirrodin Besieged*. Also, the *Mirrodin Besieged* team had much more time to develop hindsight on what we liked and didn't like about *Scars of Mirrodin*, and we would be doing a disservice to *Scars* if we didn't try to make playing with both sets together as much fun as possible.

With that in mind, let's talk about how *Mirrodin Besieged* changes things.

### The Rare Bombs Don't All Kill Things

Sunblast Angel, Hoard-Smelter Dragon, Steel Hellkite, and Carnifex Demon are all *Scars of Mirrodin* rares that kill other creatures. Contagion Engine, although not a creature, effectively kills all of your opponent's stuff in a few turns and many players consider it to be the strongest Limited rare in the set. I don't regret any of these as individual cards. Sunblast Angel has showed up in Extended, I have seen Steel Hellkites cast off of Mishra's Workshop in Vintage, Contagion Engine is very popular in the **Magic Online** casual rooms, and the other two cards missing a little bit is fine when the hit rate on all of them together is so high. However, I do regret that collectively they make for a ton of rare bomb permanents that kill all your stuff in Sealed Deck and Draft.

In *Mirrodin Besieged*, we tried to avoid making the strongest Limited cards things that killed all your opponent's stuff with upside. I won't pretend that we didn't make any cards like that, but we carefully considered what kind of effects to do before we did. In the end, the cards in *Mirrodin Besieged* that do this are Phyrexian Rebirth, which at least kills all but one of your own creatures, and Massacre Wurm, which only kills smaller creatures and shows up less often due to being mythic rare. Black Sun's Zenith also exists, of course, but it doesn't leave your creatures unscathed.

![](https://i.ormos.uk/6b/29/6b29df9216c6995c5b528a0c48bae7428ffc5df28ee25ba8a4cc0362680f64b7.jpg) 

  

This is not to say that there are no sweet rare creatures in the set, because there are. We just made sure that you have a little more time to kill these guys than the ones in *Scars of Mirrodin* before they wreck you completely.

### The Limited Format Slowed Down

One of the things that continually blows me away about **Magic** players is how smart they are. For example, at the *Mirrodin Besieged* Prerelease near my house, players spent much of the time talking about the environment discussing how much slower everything was going to be.

I was impressed to hear them identify this on their first day of playing with the set, as it's one of the more important things that we tried to do with the set. *Mirrodin Besieged* slows the format down. Both metalcraft and infect can result in decks that have the potential for massively powerful draws that put a game away very quickly. Those decks are exciting to build, but can be oppressive to play against, and we built the set so that the oppressively quick draws happen less often. While it's not exactly true that we made everything cost more mana, the distribution of cards is different. Your two-mana green creature in *Mirrodin Besieged*, rather than being Carapace Forger, is now Viridian Emissary, which pushes games toward higher-mana cards instead of toward quick metalcraft-powered wins.

There's also something subtler at work. In *Scars of Mirrodin*, there are three packs full of two-mana mana Myr. *Mirrodin Besieged* replaces one of those packs with a pack that has no mana acceleration at common, and only two two-mana uncommons that accelerate your mana.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Plague Myr" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Plague%20Myr&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Sphere of the Suns" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Sphere%20of%20the%20Suns&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

Overall, games are going to take longer now, so you'll have some more time to get creative. I'm curious to see what you all will do with it.

### Limited Infect Decks Are Slower

This subcategory was one of my pet issues. My favorite kind of aggressive deck in **Magic** is the kind that can put on early pressure but has things it can do deep into the late game. Playing infect in *Scars of Mirrodin*, though, often felt to me like the more simple-minded blitz aggressive decks that I don't enjoy playing. There was such a mass of cheap creatures, and so few big bodies to follow them up with, that I felt obligated to go for an early assault that left me without much to do if it didn't work.

There's no reason, of course, for that to be true forever. Let's compare, then, the two-mana infect creatures from *Scars of Mirrodin* ...

![](https://i.ormos.uk/c6/9a/c69ac5387fdf847c12ee2ab3aba297f38173cd62e9657293373a8bd9aa5dcdf3.jpg) 

  

... with the ones from *Mirrodin Besieged*:

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Plague Myr" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Plague%20Myr&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Flensermite" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Flensermite&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

The mass infect creatures in *Mirrodin Besieged* starts at three mana, not two, and they're much sturdier overall. Priests of Norn is literally sturdy with four toughness. Rot Wolf is metaphorically sturdy, as it replaces itself with another card when it dies to keep your infect deck gassed up with cards. Tine Shrike, Blightwidow, and Scourge Servant are all common four-mana infect creatures that are either sizable or evasive. There's also more finishing power at lower rarities in *Mirrodin Besieged*, with Flesh-Eater Imp and Phyrexian Juggernaut both easily able to crash through and put a game away.

![](https://i.ormos.uk/bd/1c/bd1c1b2278c360aba2995af22bf1071bb5eb1f37f777091a3f50b10594c88357.jpg) 

  

The net effect of all this is that infect decks will play a little differently. They'll be a bit slower, but significantly steadier. If you like drafting infect, look forward to some more staying power. If your opponents like drafting infect, you won't get out of the woods so quickly anymore.

### Infect Can Be a Normal Constructed Deck

One of the side effects of the focus on cheaper infect creatures in *Scars of Mirrodin* was that Constructed infect decks leaned toward being fast blitz decks without much ability to craft a late game. Erik likes his Constructed decks to have a little more staying power than that, and he knows that many strong competitive **Magic** players feel the same way. I agree with him. Even if a blitz infect deck is one of the strongest decks in a format, I would still not be likely to play it unless I absolutely had to.

Once again, there's no reason that this needs to be true forever. Although green is a perfect match for a blitz infect deck due to its mass of powerful Giant Growth effects in Standard right now, that doesn't mean that black's infect deck can't be a little different.

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Phyrexian Vatmother" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Phyrexian%20Vatmother&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;    <td>&#10;      <div>&#10;        <div>&#10;          <a>&#10;            <img alt="Phyrexian Crusader" src="http://gatherer.wizards.com/Handlers/Image.ashx?size=small&amp;type=card&amp;name=Phyrexian%20Crusader&amp;options=">&#10;          </a>&#10;        </div>&#10;      </div>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

Phyrexian Vatmother and Phyrexian Crusader are a little different than the *Scars of Mirrodin* rare infect creatures. They aren't worried about going directly to the opponent's face with poison counters, because they're resilient. Red and white removal spells can't touch Phyrexian Crusader, and its first strike ability means that it's tough to kill in combat. Phyrexian Vatmother's 5 toughness is a huge deal, and not even Thrun can stand in its way.

 ![Inkmoth Nexus](http://gatherer.wizards.com/Handlers/Image.ashx?size=small&type=card&name=Inkmoth%20Nexus&options=) 

  

There are also the subtler support cards. Plague Myr and Inkmoth Nexus are the sort of cards that you don't put on the movie poster, but do tons of work to get things going. Plague Myr can accelerate you into Phyrexian Vatmothers and Skithiryxes earlier than expected. Inkmoth Nexus keeps the poison coming even after your actual creatures get stopped. Both of them are happy to be part of your mana base, then come crawling out to join the assault once they are no longer casting spells.

We have data that demonstrates infect's sizable popularity with just *Scars of Mirrodin*, but we also saw several people grousing about it. I sympathize with those who didn't love infect decks before *Mirrodin Besieged*, but these cards gave me an infect deck I could love. If you're like me, you might want to give it a try.

[![](https://i.ormos.uk/2a/ac/2aac20cc7e774237190880914dfef467907b47f4dc774437b8f3ff57a6b13dca.jpg)](/en/events/2008/release-facts/worldwide-launch-parties) 

  

This weekend, *Mirrodin Besieged* [Launch Parties](/en/events/2008/release-facts/worldwide-launch-parties) will take place all across the country. That means that today is your first chance to buy cards, and that this weekend is your first chance to experience the full *Scars*-*Besieged* Limited format as we envisioned it. Things have changed, and as you can tell from this article, I think they've changed for the better.

### Last Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td colspan="3">&#10;      <b> Are you attending a Prerelease? </b>&#10;    </td>&#10;  </tr>&#10;  <tr>&#10;    <td>Yes, a large regional Pererelease.</td>&#10;    <td>650</td>&#10;    <td>9.8%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Yes, a store Prerelease.</td>&#10;    <td>4274</td>&#10;    <td>64.1%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>Yes, one of each kind.</td>&#10;    <td>170</td>&#10;    <td>2.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>No.</td>&#10;    <td>1571</td>&#10;    <td>23.6%</td>&#10;  </tr>&#10;  <tr>&#10;    <td>&#10;      <b>Total</b>&#10;    </td>&#10;    <td>&#10;      <b>6665</b>&#10;    </td>&#10;    <td>&#10;      <b>100.0%</b>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

### This Week's Poll

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>Have you played Two Headed Giant Limited in the past year?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <div id="pollmtg_daily_ld_128_polla">&#10;                    <div>&#10;                      &#10;                      Yes<br>No<br></div>&#10;                    <div>&#10;                      &#10;                    </div>&#10;                    <div></div>&#10;                  </div>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>

  

<table>&#10;  <tbody><tr>&#10;    <td>&#10;      <table>&#10;        <tbody><tr>&#10;          <td>&#10;                 <b>How many poison counters do you think it should take to win a game of Two Headed Giant?</b></td>&#10;          <td> </td>&#10;          <td>&#10;            <img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg">&#10;          </td>&#10;        </tr>&#10;        <tr>&#10;          <td colspan="3">&#10;            <table>&#10;              <tbody><tr>&#10;                <td>&#10;                  <div id="pollmtg_daily_ld_128_pollb">&#10;                    <div>&#10;                      &#10;                      10<br>11-14<br>15<br>16+<br></div>&#10;                    <div>&#10;                      &#10;                    </div>&#10;                    <div></div>&#10;                  </div>&#10;                </td>&#10;              </tr>&#10;            </tbody></table>&#10;          </td>&#10;        </tr>&#10;      </tbody></table>&#10;    </td>&#10;  </tr>&#10;</tbody></table>
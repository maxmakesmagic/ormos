---
id: hfnbzxsz
kind: article
lang: en
path: /en/articles/latestdevelopments/2009/07-17-the-core-of-the-multiverse-part-one
title: The Core of the Multiverse, Part One
published: '2009-07-17'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: tom-lapille-059233bf
  name: Tom LaPille
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
    lang_detected: en
    capture_id: 719918
    url: https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
    captured_at: '2022-08-18 18:14:49+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
    lang_detected: en
    capture_id: 719918
    url: https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
    captured_at: '2022-08-18 18:14:49+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
    lang_detected: en
    capture_id: 719918
    url: https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
    captured_at: '2022-08-18 18:14:49+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
    lang_detected: en
    capture_id: 719918
    url: https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
    captured_at: '2022-08-18 18:14:49+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: hfnbzxsz
  url: https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
  page_key: magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
  lang: en
  template: drupal
  captured_at: '2022-08-18 18:14:49+00'
  capture_id: 719918
  wayback_url: https://web.archive.org/web/20220818181449id_/https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
- document_id: hfnbzxsz
  url: https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/47
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/ld/47
  lang: en
  template: aspx
  captured_at: '2013-07-07 17:25:11+00'
  capture_id: 623022
  wayback_url: https://web.archive.org/web/20130707172511id_/https://www.wizards.com/magic/magazine/Article.aspx?x=mtg/daily/ld/47
- document_id: hfnbzxsz
  url: https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-16
  page_key: magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-16
  lang: en
  template: drupal
  captured_at: '2021-12-06 00:39:57+00'
  capture_id: 719916
  wayback_url: https://web.archive.org/web/20211206003957id_/https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-16
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: hfnbzxsz
  capture_id: 719918
  url: https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
  wayback_url: https://web.archive.org/web/20220818181449id_/https://magic.wizards.com/en/articles/archive/latest-developments/core-multiverse-part-one-2009-07-17
  captured_at: '2022-08-18 18:14:49+00'
  template: drupal
  sha256: 9e5ac34ae605c49952dd0ed63a178b2c0e0e3c7e37e39429822b87d0785e8154
render_recovery: []
---
Now that you've had the chance to play ***Magic** 2010* at the Prerelease this past weekend, it's time for me to show you some of what went into its construction. To do that, we'll dive into Multiverse, the internal database we use to collaborate when we make **Magic** cards. There are too many comments I found interesting to do in one article, so I'll be splitting it across two. Let's go!

### Siege Mastodon

![Siege Mastodon](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Siege+Mastodon)

Early in ***Magic** 2010* development, we became unhappy with how fast the Limited games were. The speed of the format felt very similar to *Shards of Alara* Limited with *Alara Reborn*, which was on the faster end of the Limited spectrum. We like **Magic** to change over time so it stays fresh and varied, so we tweaked some cards to encourage slower games. In previous core set development, we would have had to dig through previously printed sets to find cards that would accomplish our goal. However, for ***Magic** 2010* we got to just make up a new card. Here are the comments from [Siege Mastodon](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon).

> EVL 9/3: Another card to slow down the game  
>  AF 9/23: Quickly becoming my favorite common. If people are to get excited about flying and fear, guys with no evasion have to fail regularly at being able to attack. This guy ensures that.

In hindsight, when I talked about [how awesome making new cards was](/en/articles/latestdevelopments/2009/07-10-solving-the-core-sets-dilemma) for the game play of ***Magic** 2010*, I should have talked about a splashier card than this one. [Siege Mastodon](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon) is, after all, a vanilla 3/5 for five mana. However, the first Sealed Deck playtest we did that included this card was totally different from any of the previous ones. [Siege Mastodon](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon)s were gumming up the ground and making it so that white and blue flying creatures had time to outrace ground assaults. I was thrilled that such a small change to an innocuous card gave us the results we wanted, and that made me very glad that we were no longer restricted to cards we had already printed. It's quite possible that ***Magic** 2010* was the first **Magic** set that has really wanted to have a ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless4.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/white.gif) 3/5 vanilla creature, and this time we were not afraid to just make it.

**Magic** developers experience sets very differently from the rest of the world. Despite how mundane [Siege Mastodon](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon) appears, I feel a lot of nostalgia when I look at it and remember how excited I was about new cards in the core set when we made it. I would be shocked if I were not among the three people in the world who like [Siege Mastodon](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon) the most.

### Illusionary Servant

![Illusionary Servant](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Illusionary+Servant)

We have talked a lot on the site recently about how ***Magic** 2010* is a return to resonant fantasy concepts. We also talked a lot about this during ***Magic** 2010* design and development. Some tropes were easy to turn into cards; [Lightning Bolt](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt), for example, is pretty much perfect. On the other hand, there were some concepts that we wanted to have in the set that were more difficult to translate into cards. One example of this was the concept of the illusion. Rather than hem and haw about what the correct implementation of an illusion was, Aaron Forsythe simply put an illusion in the set and watched people comment.

> AF 5/19: Trying Skulking in blue.  
>  DB 5/20/08: Like. This ability is really flavorful for blue. [Gossamer Phantasm](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gossamer+Phantasm) &gt; [Skulking Knight](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skulking+Knight).  
>  AJ 5/20: Don't like how Freeze \[now [Ice Cage](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ice+Cage)\] and Illusion \[[Illusionary Servant](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Illusionary+Servant)\] have two different skulking triggers. This is the sort of thing players tend to shortcut in their memory and will get confused if they work differently.  
>  AF 5/20: I guess this could be "destroy."  
>  AF 5/20: Is it okay that illusions are represented by both "skulking" and "unblockable"?  
>  AJ 5/21: Not just "destroy" vs "sacrifice", but "becomes the target" vs "dealt damage".  
>  AF 7/22: Is this right? There was a popular Djinn submission that flickered out when targeted and you had to pay U when it came back. Is that a better Illusion mechanic than this?  
>  DB 7/23/08: I like "skulking" better for \[Illusion\]. When you disbelieve an illusion, it doesn't just go away for a while, it poofs entirely. The flicker mechanic feels more like a ghost -- also insubstantial, but persistent/recurrent.  
>  DAL 7/28: Skulking is a great match to Illusion to me.  
>  ND 7/28: Love skulking in blue. Very good match to the illusion creature type - feels D&D.  
>  TML 8/4: "When an opponent makes a Will save, sacrifice CARDNAME."

You can see that we decided that this mechanic matched illusions. Interesting, S[kulking Ghost](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=kulking+Ghost) was the first high-profile card that used the "sacrifice me when I am targeted" mechanic. Since then, **Magic** players sometimes called creatures that had that mechanic "skulking" creatures, and that led all the way to *Time Spiral*'s [Skulking Knight](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skulking+Knight). I learned during the discussions that surrounded some of these Multiverse comments that the original concept of [Skulking Ghost](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skulking+Ghost) was chosen because it was a ghost. "Skulking" was just an adjective that described a flighty ghost, but the important part of the concept was the ghost!

Next, Doug Beyer observed a problem with the word "sacrifice."

![](https://i.ormos.uk/5e/38/5e38bcaee87a7ad9475eb1c49b176edb37288d0f19a312137cf0825783c647b1.jpg)

> DB 8/12/08: I know "sacrifice it" is the right template, but "destroy it" is more flavorful on a first read. ("When something touches my illusion, I have to 'sacrifice' it, whatever that means? It doesn't just go poof?")  
>  AF 9/23: Destroy could be awesome here.  
>  TML 8/12: That would raise problems with something like [Loxodon Hierarch](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Loxodon+Hierarch) regenerating all your guys. You shouldn't be able to regenerate from going poof.

I agree with Doug Beyer here. "Sacrifice" is the wrong word for what happens to an illusion, but the actual rules behind sacrificing perfectly match what happens when an illusion goes poof. An illusion is destroyed, but a destroyed illusion in **Magic** would be able to regenerate. Despite our best efforts, sometimes words and flavor don't quite match. Here, we went with the flavor of the rules rather than picking the right word for the situation.

![](https://i.ormos.uk/dc/e7/dce754c9edfb4a48e04f9bfc8af5a7484e0c0be8e4d7fdd98d091b38f778b3e6.jpg)

Note that Aaron's comment on 9/23 came before my comment on 8/12. We have two theories about how this could have happened. One is that he can time travel. The other is that his hand was positioned one key to the right on the keypad from 8/12. Given that he's the director, I'll stick with the time traveling explanation.

There's a small amount of story yet to tell. Here it is:

> AF 7/25: To common to give blue sufficient damage-dealing capability in limited.  
>  EVL 9/11: Moved to 1UU to improve blue.

### Weakness

![Weakness](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Weakness)

Before a set is printed, the only way that we can interact with the cards is by reading Multiverse records or playing with low-quality playtest cards that have no art. Despite that, sometimes we catch glimpses of the majesty that will be when the cards are actually printed. In our internal database, [Unholy Strength](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Strength) comes directly before [Weakness](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Weakness). That prompted this comment from Ken Nagle after ***Magic** 2010* was handed off.

> KEN 1/5/2009: [Unholy Strength](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unholy+Strength) and [Weakness](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Weakness) form most beautiful contiguous pair of Multiverse records I've ever seen.

I'm looking at it now, and it is indeed beautiful.

### Sign in Blood

[Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) is cut from the same cloth as many black card-drawing spells. However, the card's grisly concept is an upgrade over more abstract concepts like [Night's Whisper](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Night%27s+Whisper) or [Skeletal Scrying](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skeletal+Scrying). Early on, Aaron Forsythe asked us whether we thought it should be targeted, and we responded with a resounding yes.

![](https://i.ormos.uk/f1/be/f1be31a026e5d82cbcec596e5a7fb5bc1a8931f8aef668c8f615aa4fd153eec4.jpg)

> AF 6/9: This would be a more fun card if it was targeted: true or false?  
>  AJ 6/09: I thought you didn't want to do drawback cards at black common. And true.  
>  LS 6/9: This is also a good "learn about the choices!" card, and to teach about Magic (new players valuing 2 life more than 2 cards until they learn better).  
>  KEN 6/25: RAWR target player !!  
>  AF 7/14: Trying it.  
>  TML 7/25: I would be very interested in finding out how often this gets pointed at the opponent if it gets out the door as is.

After we decided that [Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) should target, former head developer Devin Low prompted us to try to figure out how good the card was.

> DAL 7/28: Targeted seems fun. Is this the best card drawing in the set, better than all the blue card drawing? [Mind Spring](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Spring), [Jace Beleren](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Jace+Beleren), 2U Draw 2.  
>  TML 8/11: [Mind Spring](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Spring) is stronger than this, but this is stronger than Jace and 2U draw 2.  
>  ps 8/17: this is better than mind spring imho. night's whisper has seen play in vintage and it doesn't even randomly kill people. i think the power level of this is quite high.  
>  TML 8/18: Much of the card's power in vintage is the ability to go land-Mox-Whisper, but after some more play I think you're right about this being better.

![Sign in Blood](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sign+in+Blood)

My statement that [Mind Spring](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Spring) is stronger than [Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) was wildly misguided. At the time, I was playing a lot of mana ramp decks with [Fertile Ground](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fertile+Ground) and [Garruk Wildspeaker](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Garruk+Wildspeaker), and in those decks [Mind Spring](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Spring) was very powerful for me. However, at ![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/colorless1.gif)![](https://magic.wizards.com/sites/all/modules/custom/wiz_autocard/wiz_manacost/manasymbols/black.gif)[Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) was a [Night's Whisper](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Night%27s+Whisper) with random upside. Former R&D member Paul Sottosanti's comment brought me back to earth. ***Magic** 2010* lead developer Erik Lauer also noticed how good it was too, and it received a recosting.

> EVL 8/18: Cost changed from 1B to 2B.

At this cost, however, it compared too easily to blue's [Divination](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination). The flavor of black trading cards for life made sense, but we didn't want [Divination](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination) and [Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) to line up so nicely next to each other. Comparing the two made [Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) look unappealing even though it was actually still a good card. There was a point in our Limited tuning of the set where we wanted to make black stronger, so Erik took the opportunity to both make the card better and distance it from [Divination](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination).

> EVL 8/20: Cost changed to BB.

Now, [Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) serves as both a powerful reward for playing heavy black in Limited and a potential Constructed card. While it is rare that a [Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood) is cast targeting its controller's opponent, I have seen more than one copy of the card take a player below zero life. Unfortunately, I have not seen it deck anyone. The holy grail of [Sign in Blood](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sign+in+Blood)s, however, is targeting an opponent who has both 2 or less life and only one card in his or her library. I'd love to know if you've seen this happen.

### Berserkers of Blood Ridge

![Berserkers of Blood Ridge](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Berserkers+of+Blood+Ridge)

I talked in the [Siege Mastodon](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon) entry about how we did some things to make ***Magic** 2010* Limited slower than *Shards of Alara* block Limited. One of them was to make cards like [Siege Mastodon](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Siege+Mastodon), but another was to be cautious about where we put large creatures. [Berserkers of Blood Ridge](https://web.archive.org/web/20090717000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Berserkers+of+Blood+Ridge) was a card that I tried to get changed to help with this. The influence that **Magic** set development team members have means that most decisions go the way they want them to, but one must always be prepared to lose a fight or two. This was one fight that I did not win. In hindsight, I'm glad that I lost!

> TML 9/3: This guy is too big. I would like to make him smaller to have fewer guys that run over 1/4's and 2/4's.  
>  TML 9/4: Still enormous. I would like to have this card change as part of our campaign to make slower games.

After the set was handed off from development, Aaron made a comment in this card's Multiverse record that I did not discover until I started building this article.

> AF 1/5: The Berserkers have defeated you.

![](https://i.ormos.uk/76/d1/76d13fe7d0724ddc89b417165eae5f31d6b2781d27ded03d68622b3822b8a7dd.jpg)

I'm out of room here, but I'll be back with more ***Magic** 2010* Multiverse comments in a month or so.

### Last Week's Poll

<table><thead><tr><th colspan="3"><b>Are you going to a Prerelease this weekend, or have you already gone to one?</b></th>&#10;		</tr></thead><tbody><tr><td>Yes, I will attend or have attended a local store Prerelease.</td>&#10;			<td>4139</td>&#10;			<td>45.4%</td>&#10;		</tr><tr><td>No.</td>&#10;			<td>2765</td>&#10;			<td>30.3%</td>&#10;		</tr><tr><td>Yes, I will attend or have attended a large regional Prerelease.</td>&#10;			<td>1185</td>&#10;			<td>13.0%</td>&#10;		</tr><tr><td>Yes, I will attend or have attended both kinds of Prereleases.</td>&#10;			<td>362</td>&#10;			<td>4.0%</td>&#10;		</tr><tr><td>No, but I will play in Magic Online release events.</td>&#10;			<td>356</td>&#10;			<td>3.9%</td>&#10;		</tr><tr><td>No, but I will play in Magic Online release events and would have posted angrily in the forums if this option were not here.</td>&#10;			<td>319</td>&#10;			<td>3.5%</td>&#10;		</tr><tr><td><b>Total</b></td>&#10;			<td><b>9126</b></td>&#10;			<td><b>100.0%</b></td>&#10;		</tr></tbody></table>

 

Many R&D members went to the big regional prerelease in Seattle. Personally, I went to a local Prerelease at Shane's Cards and Comics here in Renton. I saw lots of people having fun, and my colleagues reported seeing the same thing at other locations. We hope you continue to have fun playing with ***Magic** 2010* at this weekend's Launch Parties!

On an unrelated note, I refuse to believe that over three hundred of you would have posted angrily in the forums. With that in mind, I have a follow-up question.

  
[![](https://i.ormos.uk/8b/63/8b63facbe850141b6aa3a7d716952a063907a0a6ddb26824a8d7b6bf1ae077dd.jpg)](https://web.archive.org/web/20090717000000/http://archive.wizards.com/magic/tcg/events.aspx?x=mtgcom/events/releases)
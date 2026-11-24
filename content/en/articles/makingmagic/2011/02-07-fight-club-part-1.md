---
id: wr581ap7
kind: article
lang: en
path: /en/articles/makingmagic/2011/02-07-fight-club-part-1
title: Fight Club, Part 1
published: '2011-02-07'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
    lang_detected: en
    capture_id: 220415
    url: https://magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
    captured_at: '2024-05-18 04:00:41+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
    lang_detected: en
    capture_id: 220415
    url: https://magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
    captured_at: '2024-05-18 04:00:41+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
    lang_detected: en
    capture_id: 220415
    url: https://magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
    captured_at: '2024-05-18 04:00:41+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
    lang_detected: en
    capture_id: 220415
    url: https://magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
    captured_at: '2024-05-18 04:00:41+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: wr581ap7
  url: https://magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
  page_key: magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
  lang: en
  template: contentful
  captured_at: '2024-05-18 04:00:41+00'
  capture_id: 220415
  wayback_url: https://web.archive.org/web/20240518040041id_/https://magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
- document_id: wr581ap7
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/129
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/129
  lang: en
  template: aspx
  captured_at: '2013-07-04 03:07:48+00'
  capture_id: 639466
  wayback_url: https://web.archive.org/web/20130704030748id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/129
- document_id: wr581ap7
  url: https://magic.wizards.com/en/articles/archive/making-magic/fight-club-part-1-2011-02-04
  page_key: magic.wizards.com/en/articles/archive/making-magic/fight-club-part-1-2011-02-04
  lang: en
  template: drupal
  captured_at: '2022-09-26 03:33:56+00'
  capture_id: 879669
  wayback_url: https://web.archive.org/web/20220926033356id_/https://magic.wizards.com/en/articles/archive/making-magic/fight-club-part-1-2011-02-04
- document_id: wr581ap7
  url: https://magic.wizards.com/en/articles/archive/making-magic/fight-club-part-1-2011-02-07
  page_key: magic.wizards.com/en/articles/archive/making-magic/fight-club-part-1-2011-02-07
  lang: en
  template: drupal
  captured_at: '2022-01-23 04:23:59+00'
  capture_id: 879682
  wayback_url: https://web.archive.org/web/20220123042359id_/https://magic.wizards.com/en/articles/archive/making-magic/fight-club-part-1-2011-02-07
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: wr581ap7
  capture_id: 220415
  url: https://magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
  wayback_url: https://web.archive.org/web/20240518040041id_/https://magic.wizards.com/en/news/making-magic/fight-club-part-1-2011-02-07
  captured_at: '2024-05-18 04:00:41+00'
  template: contentful
  sha256: 7317c93c4e7ab75d3c7f630a1a7c9f715bcf379e4e0f8ecb92fd8726bab0b671
render_recovery: []
---
Welcome to Battle Cry Week. This week we'll be exploring the Mirran's new mechanic created to help in its war against Phyrexia. As I already talked a bit about this mechanic's creation during the [first preview week](https://web.archive.org/web/20110207000000/https://magic.wizards.com/en/articles/archive/under-besiege-part-1-2011-01-17), I thought that I'd use my column today to explore combat mechanics in general.

My original plan was to break down combat mechanics to their core to examine all the different options available to design when creating a combat mechanic. As I did, though, something interesting happened. There are certain truisms for design that I talk about from time to time, for example "Restrictions breed creativity" or "Fighting human nature is a losing battle". This exercise reminded me of another important truism: "In the micro lies the macro."

What this means is that as you dig deep into a design you will start noticing the very properties that you find when you pull back. Metaphorically, by studying the atom you learn about the universe. So today, I am going to examine the many subsets of combat mechanics and in doing so I'm going to explore some of the fundamentals of game design. If that sounds like fun, stick around.

### Fight! Fight! Fight!

If you took all of **Magic**'s mechanics and sorted them into piles, one of the piles you would get is what R&D calls combat mechanics. A combat mechanic is defined as a mechanic that is relevant in combat. Today, I'm going to explore all the existing combat mechanics (well, all the named ones and a number of the unnamed ones) and walk you through the different design areas that combat mechanics can fill. In doing so, I hope to show how the principles of design run through an idea from the "big picture" to the tiniest of details.

![](https://i.ormos.uk/ee/db/eedbe87d96e062663c679d853ce997b1ad7313ed52004b05d75ccc72602fe490.jpg)  

Before I jump into my long list, let me clarify my category a little. Combat mechanics are ones that are specifically designed to be relevant during combat. With all but a few exceptions, combat mechanics sit on creatures. Note that I am not talking about mechanics that care about what happened in combat, but rather ones that actually affect it. As this is an exhaustive list, I'll say up front that while I tried to hit them all, I'm sure a few fell through the cracks (or would be classified differently than I chose to classify them). Also note that some mechanics fall into multiple categories and that unnamed mechanics are all in quotation marks with some unofficial name.

### Evasion (Prevents Blocks)

> *   **"Can Only Be Blocked By Two Or More"** (red)
> *   **"Can't Be Blocked By Non-Flyers"** (green)
> *   **Fear** (black)
> *   **Flying** (all but most in white and blue)
> *   **"High Flying – Can Only Be Blocked and Block Flyers"** (blue)
> *   **Horsemanship** (all colors)
> *   **Intimidate** (black, can be used in all other colors)
> *   **Landwalk** (everyone but white gets this commonly)
> *   **Protection** (white, can be used in other colors)
> *   **Shadow** (white, blue & black)
> *   **"Unblockable"** (blue)

At first blush, you might think this category doesn't belong. After all, it keeps creatures from getting into combat. The important thing to understand though is that in design the thing that makes something not happen is just as important as the thing that makes it happen. Design is just as defined by absence of something as it is its presence. When you are managing combat, it means looking at the entire substructure. The role of combat mechanics is not just to make something happen during combat, but to make the combat phase itself meaningful.

<table><tbody><tr><td><div><div><img alt="Liliana's Specter" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Liliana%27s+Specter"></div></div></td><td><div><div><img alt="Kor Firewalker" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Kor+Firewalker"></div></div></td></tr></tbody></table>

Evasion is a crucial part of making a healthy environment, especially in Limited formats. Games have to have flow, which means that you want something happening during as many turns as possible. Game states where nothing happens are first and foremost not fun. It is also repetitive and makes the game take longer (both things that obviously tie into the "not fun" issue). As such, a key part of designing an environment is making sure that creature stall doesn't happen. (And yes, there are environments like *Rise of the Eldrazi* where we purposely make stall happen at a little higher frequency.)

<table><tbody><tr><td><div><div><img alt="Covert Operative" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Covert+Operative"></div></div></td><td><div><div><img alt="Glissa's Courier" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Glissa%27s+Courier"></div></div></td></tr></tbody></table>

When you boil it all down, the key factor on whether or not combat is flowing is how much evasion your set has. A very common design playtest note is "evasion too high" or "evasion too low." The balance is crucial because you want to make sure that someone's life total is going down but slowly enough that players have the opportunity to have turn-overs. (A turn-over is when momentum moves from one player to another—it's a crucial part of making game flow work and be fun—worthy of a whole column one of these days.)

When you boil down evasion it's really just a set of blocking restrictions. Anywhere from a small subset to everything is disallowed from blocking. Note that some mechanics, like landwalk, base the unblockability on the existence of some state, most often a particular type of permanent on the battlefield. Allowing the players some ability to turn it on or off.

### Prevents Attacks

> *   **Defender** (all colors)
> *   **"Doesn't Untap Turn After It Attacks"** (green)

<table><tbody><tr><td><div><div><img alt="Wall of Omens" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Wall+of+Omens"></div></div></td><td><div><div><img alt="Apes of Rath" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Apes+of+Rath"></div></div></td></tr></tbody></table>

Just as preventing blocking is important with evasion so too is preventing attacking. Note, though, that this list is small while the evasion list is large. The reason is a key one. The game is better when it pushes towards action rather than inaction. You want the point of the game to be "to win" not "don't lose."

Inertia is a critical component of any game. What I mean by inertia is that the game in its neutral state should push the players towards doing the thing that will end the game. If you don't, the game will take far too long to play and will most likely stall out in an uncomfortable, non-fun state. Remember that players will do whatever the game incentives. It's your role as the designer to make the players want to do what will in the end be the most rewarding for them. You have to force them towards the fun.

### Alters Who Can Block

> *   **"Block Additional"** (white)
> *   **"Can Only Be Blocked By One"** (green)
> *   **"Can Only Be Blocked By Two Or More"** (red)
> *   **"Cannot Block"** (black)
> *   **"High Flying – Can Only Be Blocked and Block Flyers"** (blue)
> *   **Panic – Target creature(s) cannot block this turn"** (red)
> *   **Reach** (green)

<table><tbody><tr><td><div><div><img alt="Kemba's Legion" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Kemba%27s+Legion"></div></div></td><td><div><div><img alt="Giant Spider" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Giant+Spider"></div></div></td></tr></tbody></table>

My goal today is to list these subsets in some logical order. The order is not about importance but just keeping similar things near one another. Since we started with blocking restrictions let's move on to mechanics that grant creatures the ability to change who they can block or alter how the opponent is allowed to block them. (Straight up can't block stuff is listed above in evasion.) I stuck the black "Can't Block" drawback here because it wasn't an evasion ability.

At its mechanical core, **Magic** is a game about defaults. There is a set group of rules that you then allow all the cards to break. This subset is just overwriting the blocking rules. There are plenty of other variants available (such as "CARDNAME blocks if able") that don't appear enough to get listed here.

![Panic Spellbomb](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Panic+Spellbomb)

  

The two most useful tools design-wise on this list are "High Flying" and "Cannot Block." Every once in a while you'll make a neat mechanic that you want to be offensive but ends up being better defensively. To force the player's hand, you use some of these blocking restrictions to make sure that the cards get played the way you desire. (It also keeps you from having to price the cards for the stronger defensive use that you didn't want in the first place.) I'm well aware of this trick as I just had to use it on *Rattle* design.

The meta-issue here is that players don't intuitively do what will be fun for them; rather they will try and do what works best. In other words, they are not focused on the thing that in the end will create the best game experience for them. It's the role of a game designer to push the players in the right direction often fighting against the player's own instincts. Restrictions are a key tool in accomplishing this task.

### Forces Attacks

> *   **"Attacks Each Turn If Able"** (red)
> *   **"Nettling –Target Creature Attacks If Able"** (blue & red)

Sometimes you want to prevent and sometimes you want to force. The best example of this in **Magic** design is the thin line we've drawn between black's "Cannot Block" and red's "Attacks If Able." While these two seem very similar on the surface, they lead to different play patterns. Black is clearly motivated to attack as the creature has no value otherwise, but it is not motivated to attack into bad situations. If attacking isn't in your best interest, you won't attack with it.

![Berserkers of Blood Ridge](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Berserkers+of+Blood+Ridge)

  

Red, on the other hand, forces the attack. What this means is that the red player has to adapt to the fact that he must attack. This might encourage him to attack with more creatures to make the forced attack have value. I bring this up because I think it's important for designers to understand this difference. Forcing players to do something is very different from dis-incentivizing them.

Many designers tend to want to lean towards the latter thinking that giving the players more options will lead to a better game experience, but that's often not the result. The nice thing about forcing players is that there is a freedom of having to do something. The players don't have to stress about it and as such they spend their energy optimizing the forced action. One of the best ways to make a player do something that you believe will be fun for them is just to make them do it.

Here's a different way to think about it. I want to give my child a candy bar and I want to maximize happiness. What works better, giving the one candy bar I believe the child will enjoy most or offering thirty candy bars to choose from? I know the child is going to be happy in the first outcome. I've chosen a proven candy bar and the child won't know that there were twenty-nine other options so enjoyment ensues.

Now let's look at the other option. Choosing might be hard. The child might really enjoy multiple different candy bars and now I'm forcing what might be an unenjoyable choice. Second, the child might choose poorly. Maybe choosing a candy bar that the child hasn't had in a long time results in the discovery that it isn't good. As you can see, there are just more chances for the child to have an unenjoyable experience.

Designers cannot be afraid to force things onto the players. Giving players options *can* be the right answer, but to assume that it's always the best option, which is essentially what a lot of game designers do, is, I believe, patently false.

### Forces Blocks

> *   **"Lure – Everyone Must Block"** (green)
> *   **"Must Be Blocked If Able"** (red & green)
> *   **Provoke** (white, red & green)
> *   **"Targeted Lure – Target Creature Blocks This Creature If Able"** (red & green)

Here's another **Magic** design lesson for you: creature combat is fun. I'm not talking about everything that leads up to it. Figuring out whether you should attack is not particularly fun for many. What I'm talking about is when two creatures finally meet, it's a visceral experience. With instants in the game, you never quite know what's going to happen and as action films have taught us, physical conflict is enjoyable.

<table><tbody><tr><td><div><div><img alt="Lure" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Lure"></div></div></td><td><div><div><img alt="Feral Throwback" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Feral+Throwback"></div></div></td></tr></tbody></table>

The big problem is that many players are scared of creature combat because they worry that they are not making the right choices and are going to regret whatever action they take. This is why most beginners, for example, will avoid attacking at all costs. Another important reason for evasion is that it helps beginners attack. ("Oh, I can attack with my flyer and my opponent can't block it? Okay.")

This subset follows the advice from above and says, "You know what? Creature combat is fun. Let's have some creature combat." This subset just reinforces that it's okay for designers to force the player's hand.

### Creature Attacks That Weren't Anticipated

> *   **Flash** (green, blue & white)
> *   **Haste** (red, black & green)
> *   **"Relentless Assault – Attack More Than Once"** (red)

<table><tbody><tr><td><div><div><img alt="Darksteel Sentinel" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Darksteel+Sentinel"></div></div></td><td><div><div><img alt="Relentless Assault" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Relentless+Assault"></div></div></td></tr></tbody></table>

Another important part of most games, and definitely **Magic**, is surprise. I've talked before about the importance of having some unpredictability and how it adds fun to the game. When talking combat that means having an attacker or even an attack that wasn't known about ahead of time. You don't want too much of this, otherwise it creates the problem above of players being dis-incentivized from attacking. Just think of surprise as salt. A little can give a lot of flavoring but too much can ruin everything.

### Attack Trigger

> *   **Annihilator** (colorless)
> *   **"Attack Tap – When Attacking, Tap a Creature"** (white)
> *   **Battle Cry** (white & red)
> *   **Clockwork – Loses +1/+1 Counters When Attacking or Blocking"** (exclusively on artifacts)
> *   **Exalted** (white, blue & green)
> *   **"Power and/or Toughness Boost When Attacking"** (all colors)
> *   **Provoke** (white, red & green)
> *   **"Targeted Lure – Target Creature Blocks This Creature If Able"** (red & green)
> *   **Vigilance** (white & green)
> *   **"When Attack, Sacrifice At End Of Turn"** (blue & red)

<table><tbody><tr><td><div><div><img alt="Ulamog's Crusher" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Ulamog%27s+Crusher"></div></div></td><td><div><div><img alt="Akrasan Squire" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Akrasan+Squire"></div></div></td></tr></tbody></table>

An important thing to remember in **Magic** design is that a card's use doesn't always match its card type. What I mean by that is that sometimes you can meet the need of a sorcery with a creature (a small creature with an "enter the battlefield" trigger is a good example) or the needs of a creature with a sorcery (a token maker for instance). I bring this up because we are now getting to the trigger portion of our subsets.

These cards act a lot like enchantments in that they can create repeatable effects that happen once per turn. They're on creatures and involve attacking so obviously the creature part of the card is still present. The effects, though, allow you to tap into design space usually reserved for spells. Note that most of these "spells" do things that matter in the combat itself.

<table><tbody><tr><td><div><div><img alt="Clockwork Dragon" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Clockwork+Dragon"></div></div></td><td><div><div><img alt="Accorder Paladin" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Accorder+Paladin"></div></div></td></tr></tbody></table>

This is the first place battle cry shows up. Battle cry's power boost both makes sense flavorfully with its attack and encourages more creatures to be aggressive, helping with the game's inertia. As you can see, the many lessons of today start interconnecting with one another.

Another interesting design question when you have triggers is where to put them. As you will see there are numerous different options and each trigger works best with certain types of effects. Attack triggers, for example, are for things that you want to have happen regardless. With only a few exceptions, there isn't much the opponent can do to stop an attack trigger. Yes, they can kill the creature in combat, but that's only to stop it on future turns.

My big limitation on attack triggers is that I like them to feel like they make sense with the attack. Battle cry, for instance, feels like it wants to happen on the attack because it feels like it's the attack of the creature with battle cry that rallies the troops.

### Blocking or When Blocked Triggers

> *   **Bushido** (white & red, but occasionally in all colors)
> *   **Clockwork – Loses +1/+1 Counters When Attacking or Blocking"** (exclusively on artifacts)
> *   **Flanking** (white & red but occasionally in all colors)
> *   **"Gustcloak – When Blocked Untap and Remove from Combat"** (white)
> *   **"Power and/or Toughness Boost When Blocking"** (all colors)
> *   **Rampage/"New Rampage"** (green & red)
> *   **"When Blocked Deal Damage"** (red)
> *   **"When Blocks, Sacrifice At End Of Turn"** (blue & red)

<table><tbody><tr><td><div><div><img alt="Battle-Mad Ronin" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Battle-Mad+Ronin"></div></div></td><td><div><div><img alt="Craw Giant" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Craw+Giant"></div></div></td></tr></tbody></table>

While I've grouped them together, this subset has two parts: triggers when blocked and triggers when blocking. You can be more aggressive with the first type of triggers because you have less control over them. When blocked triggers tend to want to feel like the combat itself causes the effect. When you allow this creature to get into a fight, this is what's going to happen. The blocking triggers tend to work best with more defensive effects.

One last note about something above, "new rampage." The original rampage showed up in *Legends*. It gave a +1/+1 to your creature for each creature blocking it beyond the first one. The "beyond the first one" rider felt clunky with a modern design eye so "new rampage" gets rid of it, giving the creature a boost for each blocker.

<table><tbody><tr><td><div><div><img alt="Benalish Cavalry" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Benalish+Cavalry"></div></div></td><td><div><div><img alt="Fog Elemental" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Fog+Elemental"></div></div></td></tr></tbody></table>

The meta-issue here is the importance of feel in design. It's very easy to want to use logic to solve all your design issues, but design is more art than science. Oftentimes, the key to making the right decision is getting the feel correct. Most of the separation of the attack and blocking triggers comes from when the effect makes the most sense, not logically but intuitively.

The reason I bring up intuition so much is that a big part of game design is matching player expectation. If you can make something happen when the player expects it, you greatly cut down your complexity and you increase your aesthetics. Another way to think of it is that you are using the players own intuition to play into the game patterns you want. Humans embrace the familiar and fight the unfamiliar. Make human nature your ally as a game designer and not your enemy.

### The Fight's Not Over

I did not expect this to turn into a two-parter when I started it, but then I didn't realize what kind of article I was going to end up with. I have eight more subsets left so I'll save them for Part 2 next week. I hope you enjoyed this column as much as I enjoyed writing it. I find it fascinating to see how the same key lessons keep working their way into design no matter how small a subset you examine.

Join me next week when I talk about the second half of the combat design subsets.

Until then, may you take the time to study the things you do every day.

[![](https://i.ormos.uk/37/d0/37d0f1a78c983267982cab6d0e842460bf845f44366fd9f154d6869f49e612e5.jpg)](/en/events/2010/paris11/magic-weekend-paris-event-information)
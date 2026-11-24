---
id: 3ddded1m
kind: article
lang: en
path: /en/articles/makingmagic/2022/07-18-magic-design-from-a-to-z-part-2
title: Magic Design from A to Z, Part 2
published: '2022-07-18'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
    lang_detected: en
    capture_id: 222767
    url: https://magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
    captured_at: '2024-05-18 01:36:35+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
    lang_detected: en
    capture_id: 222767
    url: https://magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
    captured_at: '2024-05-18 01:36:35+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
    lang_detected: en
    capture_id: 222767
    url: https://magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
    captured_at: '2024-05-18 01:36:35+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
    lang_detected: en
    capture_id: 222767
    url: https://magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
    captured_at: '2024-05-18 01:36:35+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 3ddded1m
  url: https://magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
  page_key: magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
  lang: en
  template: contentful
  captured_at: '2024-05-18 01:36:35+00'
  capture_id: 222767
  wayback_url: https://web.archive.org/web/20240518013635id_/https://magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
- document_id: 3ddded1m
  url: https://magic.wizards.com//en/articles/archive/making-magic/magic-design-z-part-2-2022-07-18
  page_key: magic.wizards.com//en/articles/archive/making-magic/magic-design-z-part-2-2022-07-18
  lang: en
  template: drupal
  captured_at: '2022-07-19 09:32:38+00'
  capture_id: 892349
  wayback_url: https://web.archive.org/web/20220719093238id_/https://magic.wizards.com//en/articles/archive/making-magic/magic-design-z-part-2-2022-07-18
- document_id: 3ddded1m
  url: https://magic.wizards.com/en/articles/archive/making-magic/magic-design-z-part-2-2022-07-18
  page_key: magic.wizards.com/en/articles/archive/making-magic/magic-design-z-part-2-2022-07-18
  lang: en
  template: drupal
  captured_at: '2022-08-08 19:55:50+00'
  capture_id: 892351
  wayback_url: https://web.archive.org/web/20220808195550id_/https://magic.wizards.com/en/articles/archive/making-magic/magic-design-z-part-2-2022-07-18
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 3ddded1m
  capture_id: 222767
  url: https://magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
  wayback_url: https://web.archive.org/web/20240518013635id_/https://magic.wizards.com/en/news/making-magic/magic-design-from-a-to-z-part-2
  captured_at: '2024-05-18 01:36:35+00'
  template: contentful
  sha256: b5b0b0dba3de2a7444c8b7bf0f9f361cfc1ffdb5c96b88fd50cfaee4368db5bb
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email
  occurrences: 1
---
Last week, I started a three-part series telling behind-the-scenes design stories of 26 different cards, starting with each letter of the alphabet. [Last week](/en/articles/makingmagic/2022/07-11-magic-design-from-a-to-z-part-1), I got up to I, so this week, my stories pick up with J.

**Jinxed Idol and Jinxed Ring**

Jinxed IdolJinxed Ring

I've told many stories over the years about cycles we've made that have stretched over numerous sets, from *Odyssey* block's alternate-win cycle of enchantments (Test of Endurance, Battle of Wits, Mortal Combat, Chance Encounter, and Epic Struggle) that took a year to make, to the Atogs (Auratog, Chronatog, Necratog, Atog, and Foratog) that took a couple years to make, to the mega-mega cycle of legendary lands (Kor Haven, Teferi's Isle, Volrath's Stronghold, Keldon Necropolis, and Yavimaya Hollow) that took five years to make, to the Swords of \_\_\_\_\_\_\_\_ and \_\_\_\_\_\_\_\_ cycle (Sword of Truth and Justice, Sword of Sinew and Steel, Sword of Hearth and Home, Sword of Light and Shadow, Sword of Fire and Ice, Sword of Feast and Famine, Sword of War and Peace, and Sword of Body and Mind) that's still ongoing. The original *Mirrodin* block had one of those cycles, the Kaldra Equipment (Sword of Kaldra, Shield of Kaldra, and Helm of Kaldra), but I'd tried doing one years earlier in the first block I led, *Tempest*. This is the story of a three-part cycle that we stopped designing midway and never finished.

Jinxed Idol started as a card called Hot Potato. It damaged its controller but allowed you to sacrifice a creature to give it to another player. The idea behind it was that it made this little mini game where players would pass it back and forth trying not to die to it. I really liked it, so I had an idea. What if we made a cycle across the block of Jinxed items?

The connective tissue would be as such: all of them were artifacts (with generic costs, as that's what artifacts were back then) with a negative effect and the ability to sacrifice a creature to give it to your opponent. The idea behind the cycle was that if you managed to give all three to your opponent at the same time, they would allow you to win the game. Jinxed Ring punished your opponent for things dying, so the mere act of trying to give it back to the opponent would deal damage to them. The third item was called Jinxed Brooch. I couldn't find the original card design, but here it is from the best of my memory:

**Jinxed Brooch**  
 2  
 Artifact  
 At the end of the turn, sacrifice a permanent. If you control the Jinxed Idol, Jinxed Ring, and Jinxed Brooch, sacrifice two permanents instead.  
 Sacrifice a creature: Target opponent gains control of CARDNAME.

The key concept to the deck was that you had to generate more creatures than the opponent, often using token creatures. You then played all three Jinxed items. Once the opponent had no creatures, each turn they took four damage and sacrificed two permanents, usually lands, making it harder and harder to dig their way out.

I managed to get the first two Jinxed items in sets, but the third one got pulled into *Exodus* during development and became Null Brooch. There just weren't enough fans of the full cycle, so a cycle two-thirds in the making got scrapped.

**Keen Sense**

Keen Sense

While building the block structure for *Time Spiral* block, I got the cool idea of matching the three sets in the block with the past, present, and future. The block was about time, and that's how you divide the concept of time into three. Showing the past was easy. Hinting at the future was challenging but doable. The real dilemma concerned figuring out what it means to be in the present. Aren't most sets showing off the present?

The solution I came up with for *Planar Chaos*, the middle set in the block, was to play up the idea of showing off the present in an alternate reality. How could the present have been different? From this core idea, we came up with an altered color pie, one that reflected how the mechanics could have been chosen to represent their philosophies.

Another idea inspired by alternate reality was showing off characters who ended up different in this altered world. As the *Weatherlight* Saga was near and dear to me, I picked a key event in the story and asked, "What if one small thing had changed?"

That one thing was the attack by Selenia on the crew in Volrath's Stronghold. In the real story, Crovax is the one who kills Selenia, thereby fulfilling a curse that makes him become a Vampire. But what if he wasn't the one to do it? Standing right next to him was Mirri. What if instead of being injured by Selenia, she was the one to kill her? That one change would allow us to make two new legendary creature cards:

Mirri the CursedCrovax, Ascendant Hero

Since Mirri is cursed in this reality, her card becomes a Vampire and turns from mono-green to mono-black. Meanwhile, Crovax, watching his friend take the curse that was destined for him, takes a more noble path, and his card changes from mono-black to mono-white.

Later in design, we worked on the bonus sheet (i.e., the "planeshifted" cards) where all of the cards are existing *Magic* cards shifted to a different color. One of the cards we decided to do was Curiosity, a blue enchantment that grants a damage-dealing card-draw trigger ("whenever enchanted creature deals damage to an opponent, you may draw a card"). The Curiosity ability was in both blue and green, and we'd never made a green one, so it seemed like a cool choice for a planeshifted card. I was then reminded of the original printing of the card in *Exodus*.

Curiosity

It showed a story moment between Mirri and Crovax. You see, the crew hadn't figured out that Crovax had been turned into a vampire yet, and Mirri, injured from her interaction with Selenia, senses something is wrong and follows Crovax. This leads to a fight where Mirri is killed. I guess we just couldn't resist Curiosity killing the cat, so we used the card for that story point. I then realized that we were going to make our alternate version of Curiosity, so it seemed like a great opportunity to show a key story point between Mirri and Crovax in this alternate reality. In this version, it's Crovax who has the sense to act, but instead of confronting Mirri as Mirri did to him in the original story, Crovax flees, thus saving himself. A lot of alternate reality packed in one little card.

**Look at Me, I'm the DCI**

Look at Me, I'm the DCI

I've told this story on my blog and on my podcast, but never in my column, and it's one of my favorites, so I'm going to tell it today. One of the things I wanted to do in *Unglued* was have a lot of fun with every aspect of the card. That included the art box, so we did some brainstorming about what might be fun.

One of the ideas we came up with was having a little kid draw a crayon version of the art. ([We would later do something similar in a *Secret Lair*](https://web.archive.org/web/20220718000000/https://secretlair.wizards.com/us/product/694985/extra-life-2021), although there, we had artists then redraw the crayon version.) Having a desire to one day illustrate a *Magic* card but knowing that I have no artistic ability, I realized this might be a golden opportunity. I volunteered that my crayon drawing would look much like a young child's, and I thought the audience would find it funny that I illustrated a card. As soon as I made the offer, everyone was on board.

We didn't know what card I would illustrate, so I looked at all the cards in the file for one with a simple joke that I could communicate. The plan for Look at Me, I'm the DCI was for someone to be throwing darts at a dartboard with *Magic* cards on it, as it was making fun of how we ban cards. I chose that card because I felt I could draw that.

My artistic process is unlike that of any other *Magic* artist. I got my crayons and drew like 60 different versions of the art. I then went through and picked my favorite. A little tidbit I've never told in the telling of this story. I forgot to sign it, realized at the last minute right before it went to imagery (the process where we make a very good digital version of it for printing purposes), and ran to the art director's deck to sign it a minute before it was handed off. I reversed my R to give it a little-kid vibe. The original plan was that I was going to get paid for the art like any artist, but it just felt wrong taking money for my amateur attempt at art. I offered instead to just take $1 instead. (I needed to get paid something so that Wizards would own the art.)

Many months later, I get the following phone call:

**Me**: Hello.  
 **Them**: This is \<name> from accounting. It says on my invoice that we owe you a $1.  
 **Me**: Oh, yes. For my art.  
 **Them**: Could you come down to accounting, so I can give you a dollar bill?  
 **Me**: Oh no, I need a check.  
 **Them**: You do understand it costs us more than a dollar to make a check.  
 **Me**: I didn't know that, but I was going to be paid a lot more for my art and I volunteered to just take a dollar, so the company's saving a lot of money, even if you cut me a check.  
 **Them**: Can I ask you why you need a check?  
 **Me**: Well, I'm planning to frame my art, and I wanted to include the check with it.  
 **Them**: (incredulous) You're not even going to cash it?  
 **Me**: No.  
 **Them**: Uncashed checks throw off our total at the end of the year.  
 **Me**: By a dollar.  
 **Them**: (grumbly) Fine. We'll have a check for you in a few weeks.

And now every Friday when I write my article, I get to look up and see my check.

![Framed Look at Me, I'm the DCI](https://media.wizards.com/2022/images/daily/72nYYWwbndy.jpg)

**Mana Drain**

Mana Drain

This story's actually not a design story, but it's the source for a long-running *Magic* joke/meme, so I thought I'd explain its origins.

The *Legends* designers decided to make a tweaked version of Counterspell. This version, in addition to countering the spell, also generated colorless mana equal to the spell's mana value. At the time, mana burn was a thing (at the end of any phase, if you have unspent mana, it goes away; mana burn would make you lose 1 life for each mana lost in this way), so the thought among the designers was that this was roughly equal in power to Counterspell. They were way, way off. Mana Drain went on to be one of, if not the most, powerful counterspells in *Magic*.

This was the summer of 1994. A little over a year later, I was hired fulltime by R&D. I'd been pretty active on the Usenet (an early version of the internet), so when I came to work for Wizards, I did a lot of unofficial reaching out to the fans. They'd ask questions, and I'd answer. ([Check out my blog](https://markrosewater.tumblr.com/) if this sounds interesting to you as I continue to do it to this day.)

One of the questions I got was "Are you going to reprint Mana Drain?" Unlike the majority of powerful potential reprints back in the day, Mana Drain was not on the Reserved List, being an uncommon in *Legends*, so it was a legal reprint.

At the time, there was only two outlets for reprints. Most of them appeared in the core set, which was printed every other year back then, and premier sets (just called "Type 2 sets" at the time), both of which were Standard legal. Supplemental sets weren't a thing yet. (*Unglued* would be the first one in 1998, and even that was years ahead of its time.) This meant the answer was "no," R&D had no intention of reprinting Mana Drain, as there was no avenue to release it that didn't go through Standard, but it was the internet, and I was trying to be colorful, so what I said was "every member of R&D would have to be hit by a bus before we reprint Mana Drain." This quote was said sometime in 1996 I believe.

In 2009, *Magic Online* released *Masters Edition III*, an online-only set. It reprinted Mana Drain. That's when the jokes started as the thing I said would never happen happened. *Vintage Masters*, another online-only product, was released in 2014. It also had Mana Drain. *Iconic Masters* was released in 2017 (first played in preview events at Hascon) and reprinted Mana Drain in paper for the first time (well, in a product; we had made a judge promo card of it). The first *Commander Legends* and *Double Masters 2022* both reprinted it.

All this has lent itself to endless R&D-being-hit-by-a-bus jokes. If you've heard these but never understood them, it's where the joke comes from. My big takeaway from this is to be careful about what I say we'll never do, because *Magic* keeps surprising me in how it changes and adapts. It has led to a line I use a lot on my blog "I never say never."

**Norin the Wary**

Norin the Wary

*Time Spiral* was a set about the past. We looked for characters that the audience knew but had never gotten a card so we could make legendary creatures. I made several lists for this endeavor. One of the lists included characters mentioned in flavor text. The two at the top of my list were Saffi Eriksdotter and Norin the Wary. Saffi was from the flavor text of original \[autocard mvid="2576"\]Lhurgoyf in *Ice Age*. I had nothing to do with its creation, but it was my favorite piece of flavor text, so over the years, I've designed numerous cards based on it. Norin and I had a little bit different relationship. I, along with the rest of the *Magic* audience, first met Norin the Wary in *Alpha* in the flavor text of the card Jade Statue:

"*Some of the other guys dared me to touch it, but I knew it weren't no ordinary hunk o' rock*."  
 —Norin the Wary

I enjoyed how it helped establish what the card did and introduced a character that you could get a sense of in one line. Norin had survived because he was always on the lookout for danger. Norin showed up next in *The Dark* on the card Goblin Shrine with the following flavor text:

"*I knew it weren't no ordinary pile of—you know*."  
 —Norin the Wary

I worked on the flavor text team for *Fifth Edition*. Although I didn't write the Animate Wall flavor text, I did suggest we attribute it to Norin:

"*When you have been bitten with fangs of granite, you start to long for the ivory sabers of tigers*."  
 —Norin the Wary

Norin showed a long history of being afraid of stone. In the same set, we attributed another quote to Norin, Sabertooth Tiger:

"*I fear anything with teeth measured in handspans*!"  
 —Norin the Wary

When it came time to design Norin, I knew the top-down flavor I was trying to capture; he was afraid of everything and was always willing to take steps preemptively not to die. What did that mean mechanically? What if every time you tried to kill him, he ran away instead?

I ended up using end-of-turn flickering as the means he used to run away. It hit the flavor of him going away for a while. At first, he just ran away when your opponent cast a spell, but I added the "creature attacks" text when he died during a playtest to an effect that made him have to block. I honestly didn't know how the card would get used, as it's a weird effect, but I've been happy seeing all the creatively designed decks players have built around him.

**Opalescence**

Opalescence

The joke in R&D was that *Urza's Saga* block had an enchantment theme that no one knew about. If you actually look through the cards, it's pretty apparent, but the block was called the "artifact cycle," and many of the broken cards in it were artifacts. Nonetheless, we spent a lot of time trying to design cool things for enchantments to do. During *Urza's Destiny* design (remember this was the set I designed by myself), I did an exercise where I looked at every card that mechanically cared about artifacts. I then examined what would happen if we made a new card that did the same thing, but with enchantments. Some of them didn't work as artifacts, and enchantments are different in some ways, but most of them did. One of the cards that caught my eye was Titania's Song from *Antiquities*:

Titania's Song

I had a lot of fun with this card, so I was eager to make an enchantment version. Mostly it was the same, but I made a few tweaks. One, I referenced "global enchantments" so that I wouldn't raise the question of what happens to Auras when they animate. Two, I didn't take the abilities away from the animated enchantments, as it seemed like it would lead to cooler things happening. Three, I took away the effect that made it last until end of turn if the enchantment went away. That was just to simplify the card and make it less wordy. I was really happy with how the card was playing and happily turned it over to development. I think the only thing they did to it was change it from 3W to 2WW.

The card would go on to be a bit of a headache for judges, especially with the card Humility (also designed by me), but it also has allowed a lot of players to do very cool, if sometimes confusing, things.

**Panharmonicon**

Panharmonicon

Regular readers know of my profound love of copying things. One of my early favorite decks was built around four Clones, four Vesuvan Doppelgangers, four Copy Artifacts, and four Forks. So, throughout my *Magic* design career, I've always been on the lookout for new things I could copy. (A bunch of them are listed [in this article](/en/articles/makingmagic/2020/06-01-my-favorite-things).) The story of this card starts during *Kaladesh* design. I told my design team that I wanted some quirky artifacts to build a deck around. *Kaladesh* was a set filled with artifacts with an inventor's theme, so I thought it was very important to have some novel build-around designs.

One design was something I'd been wanting to do forever, but I wasn't sure how. I wanted to copy "enters the battlefield" effects. So, I just made it and assumed the proper people would figure out how to template it. Here's my first stab at it:

**Doubling Doohickey**  
 3  
 Artifact  
 Creatures entering the battlefield have their abilities trigger twice.

The card would mostly stay the same except for three changes. One, the final version affects artifacts in addition to creatures. Shawn Main brought this up when he first saw it, and I agreed that it was a good change. Two, the card only affects your things. That had always been my intent. Three, the cost got changed from three to four. It ended up being a bit stronger than I realized when I made it. What follows are various attempts at templates:

*   Creatures entering the battlefield have their abilities trigger an additional time.

*   Creatures and artifacts entering the battlefield under your control have their abilities trigger an additional time.

*   Enters-the-battlefield abilities of artifacts and creatures you control trigger an additional time.

*   Your abilities that trigger because a creature or artifact entered the battlefield trigger an additional time.

*   If an artifact or creature entering the battlefield would cause a triggered ability of a permanent you control to trigger, that ability triggers twice instead.

I'm happy with how this card turned out and how much the players have embraced it.

**Quirion Ranger**

Quirion Ranger

This card came about for two reasons: one, during *Visions* development, we removed a one-drop Elf; and two, I was determined to prove I was a *Magic* designer. You see, I wasn't hired into R&D as a designer but rather as a developer. What I really wanted to do was *Magic* design, so whenever we made a hole in development, I'd design a bunch of cards to fill the hole. Most of my early designs came from hole filling. (Interestingly, this is still a great way for aspiring designers at Wizards to get noticed.)

This design was inspired by a weenie green-blue deck I used to play. What's a one-drop fit for a deck like that? How about something that let me untap creatures. This, for instance, would let me untap my Llanowar Elves or Birds of Paradise to make more mana or untap my Mishra's Factorys to make them +1/+1 bigger.

I knew a tap would be a little too good, so I was looking for a different cost. I experimented with a few different things, but there aren't a lot of costs you can pay in the early game. I finally settled on returning a forest to your hand. In later turns, it could be turned into upside, because you could tap it for mana, bounce it, and then play it again for a second mana. I really liked the design, so I encouraged Bill Rose, the set's lead developer, to put it into the set. The card was a lot of fun to play and made it all the way to print.

# Man of Letters

That's all my stories for today. As always, I'm eager to hear your feedback. Any thoughts on today's stories or cards? You can email me or contact me through my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](http://markrosewater.tumblr.com/), [Instagram](http://instagram.com/mtgmaro), and [TikTok](https://www.tiktok.com/@markrosewater)) with feedback.

Join me next week for the stories R through Z.

Until then, may you have as much fun playing the cards as we had making them.

*   [**Episode 948**](https://cdn.transistor.fm/file/transistor/m/shows/21454/4d87756f716f9bd3237bbdfeba5ab6c2.mp3) Spice8Rack's *Un-* Video
*   [**Episode 947**](https://cdn.transistor.fm/file/transistor/m/shows/21454/0fa5e8ab10596dad5d97caefd71748a2.mp3) *Dragon's Maze*
*   [**Episode 946**](https://cdn.transistor.fm/file/transistor/m/shows/21454/1afd16526699a180ff961c3a56491a45.mp3) *Gatecrash*
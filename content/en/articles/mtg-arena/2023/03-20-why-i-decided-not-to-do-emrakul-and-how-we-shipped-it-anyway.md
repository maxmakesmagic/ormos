---
id: 8vn8144t
kind: article
lang: en
path: /en/articles/mtg-arena/2023/03-20-why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
title: Why I Decided Not to Do Emrakul, and How We Shipped It Anyway
published: '2023-03-20'
column_slug: mtg-arena
column: MTG Arena
authors:
- slug: ian-adams-1d137168
  name: Ian Adams
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
    lang_detected: en
    capture_id: 243783
    url: https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
    captured_at: '2024-06-20 03:13:30+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
    lang_detected: en
    capture_id: 243783
    url: https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
    captured_at: '2024-06-20 03:13:30+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
    lang_detected: en
    capture_id: 243783
    url: https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
    captured_at: '2024-06-20 03:13:30+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
    lang_detected: en
    capture_id: 243783
    url: https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
    captured_at: '2024-06-20 03:13:30+00'
    rule: url.article_section
sources:
- document_id: 8vn8144t
  url: https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
  page_key: magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
  lang: en
  template: contentful
  captured_at: '2024-06-20 03:13:30+00'
  capture_id: 243783
  wayback_url: https://web.archive.org/web/20240620031330id_/https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
- document_id: 8vn8144t
  url: https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway?s=09
  page_key: magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway?s=09
  lang: en
  template: contentful
  captured_at: '2023-03-27 18:05:33+00'
  capture_id: 243785
  wayback_url: https://web.archive.org/web/20230327180533id_/https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway?s=09
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 8vn8144t
  capture_id: 243783
  url: https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
  wayback_url: https://web.archive.org/web/20240620031330id_/https://magic.wizards.com/en/news/mtg-arena/why-i-decided-not-to-do-emrakul-and-how-we-shipped-it-anyway
  captured_at: '2024-06-20 03:13:30+00'
  template: contentful
  sha256: 2ab6a72182d3a307bfc1af1d98b4a55af71cff842f8c4bfb655aa0cda027df75
render_recovery: []
---
![Artwork for Emrakul, The Promised End by Jaime Jones](https://media.wizards.com/2023/images/daily/vih2q22roswi.jpg)

Emrakul, the Promised End | Art by: [Jaime Jones](https://web.archive.org/web/20230320000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&artist=+[%22Jaime%20Jones%22])

Emrakul, The Promised End is a product owner's nightmare:

*   It's a huge amount of work . . .
*   Most of it is not reusable for anything else . . .
*   . . . And it won't see major competitive play.

Nonetheless, it's the marquee card of the set. I mean, when articles were written about *Shadows over Innistrad Remastered*, the artwork often used featured Emrakul—the community loved and loves Emrakul—a card that *MTG Arena* agreed for years we were *never going to do*.

To back up a little, I'm Ian Adams, the product owner of Card Set on *Magic: The Gathering Arena*. A product owner is the person who defines the priorities and direction of a given product or team. I usually translate that as "I'm in charge of the part of *MTG Arena* where you actually play *Magic*." It's my job to make sure we get new sets out on time, to decide when and how we give features and cards extra polish, and to decide where we need to hold back to maintain a healthy work schedule without overburdening our team.

It's a tightrope.

Despite all this, or perhaps, *because* of this, I try to set aside discretionary time for engineers. There are things like tech debt, or engineer quality of life, that are hard for me to prioritize. They don't have any clear connection to the game for players, but if you're going to maintain a project for years to come (not to mention keep your engineers happy and mentally healthy), you've got to make time for them. Give them flexible work time, so they have the breathing room to do something "just because." This can be things like refactoring code so it's easier to read or maintain, cleaning up spurious error messages or making existing ones more descriptive, improving the build process, or working on a passion project. In other words, it's time that's part of their normal work schedule, but they get to stretch a bit.

Now back to The Otherworldly Ms. Em. When we nailed down the decision that *Shadows over Innistrad Remastered* was going to be something we'd make, I came to the painful conclusion that Emrakul just didn't make sense to implement into *MTG Arena*. There were weeks, probably months, of work to do, and even then, client stability was a still risk. *Magic: The Gathering – Duels of the Planeswalkers* eventually had to cut the card, because the number of potential interactions just made the test space balloon exponentially.

When looking at our upcoming schedule, Emrakul, though clearly beloved and a lot of fun, requires us to build entirely new tech around receiving and responding to the other player's messages, while still sending messages to their client and keeping them up to date with what's happening. Then we need to ensure that works for every action you can take in the game, from casting spells with kicker to sacrificing creatures, and making sure you can pass priority back and forth between yourself during combat. Can you put a Companion in your hand while controlling someone else? What about being able to look at cards that have been exiled face down? Game development requires "or" decisions. You can't have everything you want. You must make choices, and those choices sometimes hurt.

And as painful as it was, I had to make the call not to include Emrakul, The Promised End.

It was less than a month after I made that call before the first completed work came through. Under the umbrella of discretionary time for engineers, a bit of tech debt was marked complete: cleaning up some old code from before *MTG Arena* was even in closed beta. It was a story about correctly handling illegal actions. But specifically, illegal actions when controlling another player.

I sat down with Andy Reiff, the engineer who submitted this fix. I told him we'd talked about this. There's no practical way to get this working. It would take *months*. Any work done on Emrakul was unlikely to go anywhere.

But Andy is not easily deterred. This is a person who runs 100 miles for *fun*. It bothered him that Emrakul was just *there*, the card we couldn't do, stopping us from fully building up the back catalog—this challenge we *weren't* taking on.

As doubtful as I was, this is why we try to account for discretionary time when planning: to give folks like Andy the freedom and flexibility to work on something they're passionate about. I told Andy to go ahead if he wanted, but to avoid discussing it too much with the other Card Set folks. I didn't want my team thinking Emrakul was going to be a thing.

Obviously, this didn't stop anyone, and a few weeks later one of our tech leads, Scott Ward, submitted work dealing with the unique phrasing of Emrakul's extra turn ability. Controlling another player was working in *theory*, but without the card fully parsing through *MTG Arena*'s game engine, we couldn't test it.

![Artwork for Epiphany at the Drownyard by Titus Lunter](https://media.wizards.com/2023/images/daily/yeniphlflwr0.jpg)

Epiphany at the Drownyard | Art by: [Titus Lunter](https://web.archive.org/web/20230320000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&artist=+[%22Titus%20Lunter%22])

So, Scott did his part to address the issues blocking progress. He wanted to make sure other people's work was visible, so he cleared up the issues with the extra turn. Once that was in, I gave the card a shot, and it worked. I mean, sure, it had *every bug imaginable*—timers were wrong; cards didn't retain visibility; and heck, the controlled player was able to quickly hit "pass all," and you wouldn't even get a chance to do anything on their turn. But it essentially worked!

Now the major risk was bugs and interactions. A card like Emrakul touches every other part of the game. QA was ready to help but was cautious, and rightfully so. Great, you have controlling your opponent working, but what if they're running a mutate deck? What if it's all foretell cards? What if they're casting Adventures?

Andy, now working primarily with fellow engineer Ryan George on the client side, was confident it wouldn't be that complicated. We have more than 3,000 automated regression tests for rule behavior, and we'd be adding plenty more as we went. There's a lot to test, but fundamentally, the rules engine models *Magic* correctly, and the client doesn't know the difference. If it's told to show a browser for casting with kicker, it doesn't care which player sent it, it just shows the browser and sends the response.

Little by little, these folks, and the many others who joined them willingly, dedicated their discretionary work time to fixing bugs and cleaning up behaviors; fixing visibility; making the controlled player's client respect the "information only" flags, so it wasn't opening up browsers that didn't do anything; making sure Wish effects didn't allow a controlling player to view their opponent's sideboard.

We ran some small playtests, and then larger playtests, and as time went by, I ran out of concerns. Work went from discretionary time to a budgeted part of the process, and we let art know we'd probably need some very specific VFX. I also got to tell Jiachen "JC" Tao and our Studio X partners that a decision we'd all been disappointed by had been reversed.

We were going to take on Emrakul.

![Emrakul, the Promised End from Shadows over Innistrad Remastered](https://media.wizards.com/2023/sir/en_86606_Printed_EmrakulthePromisedEnd.png) 

All told, Emrakul, the Promised End, by itself, was larger than *either* of the other remastered sets we've previously done. It's by far the single most time and resource intensive card we've done for *MTG Arena*. Not putting Emrakul on the schedule was the right call. My priority has to be protecting the schedule and making sure the workload is reasonable. But I'm incredibly glad that the squad is structured in such a way that these dedicated and passionate team members can come together and find a way to override that call while still delivering on everything else they were asked to do.

Any time you see Emrakul in this game, please remember, it's because *MTG Arena* engineers saw this challenge, and wanted to make some players' day.
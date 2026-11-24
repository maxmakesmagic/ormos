---
id: yjyyxqch
kind: article
lang: en
path: /en/articles/feature/2003/01-03-the-developers-column
title: The Developers' Column
published: '2003-01-03'
column_slug: feature
column: Feature
authors:
- slug: alancomer
  name: Alan Comer
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/articleac010303
    lang_detected: en
    capture_id: 1821814
    url: http://www.wizards.com/default.asp?x=magic/magiconline/articleac010303,,pt
    captured_at: '2004-11-16 14:42:29+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/articleac010303
    lang_detected: en
    capture_id: 1821814
    url: http://www.wizards.com/default.asp?x=magic/magiconline/articleac010303,,pt
    captured_at: '2004-11-16 14:42:29+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/articleac010303
    lang_detected: en
    capture_id: 1821814
    url: http://www.wizards.com/default.asp?x=magic/magiconline/articleac010303,,pt
    captured_at: '2004-11-16 14:42:29+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/articleac010303
    lang_detected: en
    capture_id: 1821814
    url: http://www.wizards.com/default.asp?x=magic/magiconline/articleac010303,,pt
    captured_at: '2004-11-16 14:42:29+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: yjyyxqch
  url: http://www.wizards.com/default.asp?x=magic/magiconline/articleac010303,,pt
  page_key: wizards.com/default.asp?x=magic/magiconline/articleac010303
  lang: en
  template: classic_asp
  captured_at: '2004-11-16 14:42:29+00'
  capture_id: 1821814
  wayback_url: https://web.archive.org/web/20041116144229id_/http://www.wizards.com/default.asp?x=magic/magiconline/articleac010303,,pt
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: yjyyxqch
  capture_id: 1821814
  url: http://www.wizards.com/default.asp?x=magic/magiconline/articleac010303,,pt
  wayback_url: https://web.archive.org/web/20041116144229id_/http://www.wizards.com/default.asp?x=magic/magiconline/articleac010303,,pt
  captured_at: '2004-11-16 14:42:29+00'
  template: classic_asp
  sha256: eb65e82ed6d5684d976f3f69e86685c6eeebd6257b0f27d2d1846334f8eca796
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:autoCardWindow2('Artificial[Evolution','/global/images/magic/general/Artificial_Evolution.jpg')
  reason: The archived link runs JavaScript. The preview kept its text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Artificial[Evolution')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Artificial Evolution
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Yavimaya[Barbarian')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Yavimaya Barbarian
  occurrences: 1
---
### Talking About Formats

* * *

Hello everybody. For those of you who don't know me, my name is Alan Comer, and I am a developer for ***Magic: The Gathering®** Online* here at Wizards of the Coast. I started playing **Magic®** way back with the *Arabian NightsTM* set, and spent many years playing on the Pro Tour. My purpose here today is to kick off a new column giving our players some insight on what goes on here behind the scenes. As most of you know, Leaping Lizard does the majority of development. Less known is that there is also a development team here at Wizards. Over the next few columns, we hope to introduce you to the members of our team.

About now, you are probably wondering what my job here actually entails. To show you, I am going to walk you through the steps we took to develop Casual Format 1. It started off as a request to add more formats. There have been many suggestions on new formats, as I have seen on the boards and heard them from R&D. As far as the official beginning of my involvement with them is concerned, this happens when they are placed on the official wish list and assigned to me by my boss. This is not to say that I don't often suggest what I should be doing to my boss, just the time when I am technically supposed to work on it. Anyways, a while ago I received the word to look into new formats.

So, I researched new formats, something that I really enjoyed. I looked on the boards, included the formats that the invitational commonly used, talked to R&D, and asked Richard Garfield what his favorite formats are. (Getting to discuss things with Mr. Garfield is a really cool perk, by the way.) By the time I was done, I had a list of just under twenty completely separate formats. I am sure I could have found more, but it seemed like an appropriate place to stop and move the process forward.

Now that we had this list, it was time to get everybody into a meeting and discuss what we should do about adding new formats. As a developer, I like the idea of adding as much to the product as I can. However, there are pitfalls to this that were brought up and we needed to avoid them. For example, if you release a bunch of different formats at the same time, you risk people finding one favorite and not playing the other formats.

This can lead to a variety of problems. Say your favorite isn't one lots of other people play and you can't get a game because everybody else is playing the other formats. We want players to get the most out of each format and we believe that releasing more than one in an update reduces their value. Since we have plenty of other things in mind to improve ***Magic** Online* (and new sets on the horizon as well) we decided to limit ourselves to a maximum of one format per update, as time permits. I don't know how often we will complete new formats, just that we can't do more than one per month.

So, in what order should we do the new formats? We decided upon just the first two new formats. We started with what the public affectionately calls Highlander (Casual Format 1) and are planning to continue with the 250 format.

The next step in the development of the format was for it to leave my hands. A request was made for R&D to define the rules. Since they are the people that specialize in making games entertaining, it is their job to write rules. Casual Format 1 came back very quickly, 250 took much longer. We also started hunting for what to call CF1 once it was ready to go live.

Now that I had the rules from R&D, it was time to write the code. This didn't take long, as I had been familiarizing myself with that area of the code the entire time. (I love to program, it's the best part of the job. Writing documents tends to be the most tedious part for me.) Of course, once you have written the code, you then have to check that it works and iron out the bugs. CF1 was a pretty simple change, so everything went pretty smoothly there.

Next I let everybody know that the change was complete and added the code to our internal test server. All that was required was for nobody to find any bugs with it by the patch time and it would go live. Of course, the nature of computer software is to humble even the simplest effort. This piece of code proved to be no different.

Jess, our QA manager, reported back to me three days or so before the release that the Wishes from the *JudgmentTM* set only allowed you to get cards from the *OnslaughtTM* block. I started looking into what went wrong and it wasn't going too well. I went home, came back in the morning, and noticed that the Leaping Lizard team had noticed the bug report and fixed it. (They come into work 3 hours before me due to the time zone differences.) Thanks guys!

Between the time that I finished the code and the wishes bug was reported, bad news came back: we still didn't have a name for the format. Due to the limited time left, we didn't want to use a halfhearted name that might catch on and get stuck with it. (As happened with the *The Dark®*® expansion. You can see the problem.) So, they decided to leave it Casual Format 1 to give more time for a name.

Other than formats, there are many things I get to do to improve the game. Probably one of the most notable is that I'm working on implementing cards for the *Eighth EditionTM* set that do not already work in ***Magic** Online.* Not only is this good because I get to do a lot of coding, but also I need to know what is coming in future sets so that I don't get ambushed with particularly thorny programming problems.

<table><tbody><tr><td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td><td></td><td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td><td><a><img alt="Artificial Evolution" src="https://i.ormos.uk/63/ed/63eda4eed737350967b4c9e008a5d08fe9b749f4ad6dee1d6ac1631e2973998d.jpg"></a></td><td></td></tr>&#10;<tr><td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td><td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td><td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td></tr>&#10;</tbody></table>

A good example of this is Artificial Evolution. Because Leaping Lizards is a long way away, communication isn't always the best. The first they knew about Artificial Evolution was about the time they had to code it. This forced a retrofit of some mechanics and cards. Had they known about this in advance, some of those mechanics and cards would have been coded differently, saving them time. So part of my job is to participate in the Future-Future League (FFL) here at Wizards. This is where cards are playtested in R&D before printing.

Finally, when I get the chance, I go online and play people just to keep an eye on the system. It also allows me to chat with the players. Mostly I do this on update days as I get much better feedback when there are bugs, and it helps me gather information as to what went wrong. I tend to play in the **Casual Play** area, either in serious or casual decks. I go to both because I want to talk to different people, not because of the deck I play.

So, you've listened to me ramble for all this time, eh? Guess it is time to reward you with something much more interesting: the 250 format.

Let's start with what 250 is: A format requiring a deck of at least 250 cards, with a minimum of 18 cards of each color. I have seen 250 played quite a lot over the years, and its endurance and popularity is what stood out as the best candidate for inclusion in ***Magic** Online.* It was popularized by Kurt Hahn, amongst others, and there is a web site at [www.5-color.com](https://web.archive.org/web/20030103000000/http://www.wizards.com/leaving.asp?url=http://www.5-color.com&origin=magic_magiconline_articleac010303).

Unfortunately, there are many parts of 250 that cannot be done effectively online, so the rules that came back from R&D have significant changes. Here is the gist of what I received from R&D:  
  

*   **Deck Construction:** At least 250 cards, with a minimum of 20 cards of each color.
*   **Mulligans:** Before anybody decides on Paris (normal) mulligans, anybody with 0, 1, 6, or 7 lands may take a free mulligan by showing his or her hand to the other players, shuffling it back into the deck, and drawing seven new cards. Whenever a player takes this free mulligan, any other player may also shuffle his or her hand away and draw a new one.
*   **Banned Cards:** Battle of Wits

How is 250 coming? Well, first off, it is currently called Casual Format 2, as a name has not yet been reached. The coding is complete, and about to be handed off for testing. The big problem is an above average chance that it will come back from QA due to bugs. Here is the problem: Take Yavimaya Barbarian, the red/green creature from the *InvasionTM* set. Each card can only be of one color, but of the player's choice. It isn't an option to ask the player which color the card counts towards every time we want to validate the deck. I also don't want to make players save this information when they save a deck.

What needs to happen is the computer must look at the dec, and determine if any combination of color choices would work. If so, the deck is legal. This represents a tricky puzzle to the computer. The obvious, hard and fast, definitely works method: just try every combination. However, this could be quite time consuming, and since this has to happen on the server, would probably cause bad lag. As such, this has been ruled out, too.

What I did was come up with a method of filling colors based on need, with just one pass. The first few algorithms I made I managed to poke holes in and prove they were flawed. I now have one that I think works, but the puzzle is complicated enough that it would not surprise me if somebody managed to disprove it as well.

The best scenario is that it all works as planned, and that it is in the January update. The worst case is that this problem is unsolvable at a reasonable speed for the servers, and that we need to slightly adjust the rules of the format so that the computer can handle it better, hopefully only slipping to the February update.

Keep your fingers crossed.
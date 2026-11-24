---
id: 9etb3dsv
kind: article
lang: en
path: /en/articles/feature/2003/09-26-last-weeks-topics-return
title: Last Week's Topics Return...
published: '2003-09-26'
column_slug: feature
column: Feature
authors:
- slug: danielmyers
  name: Daniel Myers
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/oped092503
    lang_detected: en
    capture_id: 1831848
    url: http://www.wizards.com/default.asp?x=magic/magiconline/oped092503,,pt
    captured_at: '2004-12-30 11:05:01+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/oped092503
    lang_detected: en
    capture_id: 1831848
    url: http://www.wizards.com/default.asp?x=magic/magiconline/oped092503,,pt
    captured_at: '2004-12-30 11:05:01+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/oped092503
    lang_detected: en
    capture_id: 1831848
    url: http://www.wizards.com/default.asp?x=magic/magiconline/oped092503,,pt
    captured_at: '2004-12-30 11:05:01+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/oped092503
    lang_detected: en
    capture_id: 1831848
    url: http://www.wizards.com/default.asp?x=magic/magiconline/oped092503,,pt
    captured_at: '2004-12-30 11:05:01+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: 9etb3dsv
  url: http://www.wizards.com/default.asp?x=magic/magiconline/oped092503,,pt
  page_key: wizards.com/default.asp?x=magic/magiconline/oped092503
  lang: en
  template: classic_asp
  captured_at: '2004-12-30 11:05:01+00'
  capture_id: 1831848
  wayback_url: https://web.archive.org/web/20041230110501id_/http://www.wizards.com/default.asp?x=magic/magiconline/oped092503,,pt
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9etb3dsv
  capture_id: 1831848
  url: http://www.wizards.com/default.asp?x=magic/magiconline/oped092503,,pt
  wayback_url: https://web.archive.org/web/20041230110501id_/http://www.wizards.com/default.asp?x=magic/magiconline/oped092503,,pt
  captured_at: '2004-12-30 11:05:01+00'
  template: classic_asp
  sha256: 3ec0f0a2c3431a606bb2c8397c5c091a567c33486d673be934e7f0c37c71bfdc
render_recovery:
- code: unsupported_link
  element: a
  target: "\n\t\t\tmailto:\n\t\t\tmagicconduct@wizards.com"
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - magicconduct@wizards.com
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Goblin[War[Wagon')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Goblin War Wagon
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Vulshok[Gauntlets')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Vulshok Gauntlets
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Plains')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Plains
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Leonin[Elder')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Leonin Elder
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Nuisance[Engine')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Nuisance Engine
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Broodstar')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Broodstar
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Terror')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Terror
  occurrences: 1
- code: unsupported_link
  element: a
  target: javascript:autoCardWindow2('Brown[Ouphe','/global/images/magic/general/Brown_Ouphe.jpg')
  reason: The archived link runs JavaScript. The preview kept its text.
  labels:
  - used to suck
  occurrences: 1
---
### In A Slightly Different Way

* * *

Another week goes by and another group of items have caught my attention. Here's what's topped my list this week.

### Royal Assassin Avatar

We finally got it out and, just to be consistent, made sure it came with bugs. Yes, we can even make art crash games!

Actually, the game was grabbing the wrong pieces of art for the avatar, which made players' games go "boom." We jammed one fix in that didn't take care of the instance of taking damage from a blue source during a game. (There are different pieces of art for damage from different sources, in case you didn't know.) One more chunk of code and all was well. Enjoy!

If you went to one of the events, but haven't received your avatar yet, you've got until September 30 to let us know. [See this announcement for details.](https://web.archive.org/web/20030926000000/http://boards1.wizards.com/showthread.php?threadid=102078)

### Beta Test Server

For the time being, the beta server won't be coming up. While there's a chance we'll have another open beta before we bring people in to test *Mirrodin* cards, I wouldn't count on it. It looks like future beta testing will be invite-only, so asking folks on the team when the beta server will be running again won't do any good. If you hear from us you're in. If you don't, you aren't. And just because you are or aren't a beta tester for the next round doesn't mean that's the way it'll always be.

Speaking of invites, someone began a thread claiming that beta testers have already been chosen and that a friend had gotten the email. This isn't the case -- testers haven't been chosen yet. I don't know who was trying to pull the wool over whose eyes, but it was a relatively harmless prank.

However, I can already see the attempted scam: "just give us your username and password and we'll tell you how to access the server." It doesn't matter if it's an email asking for a reply or a website "log on" system, if you get anything like this it's a scam. Let me say it again:

***No one who works on* Magic Online *will ever ask you for your password.***

If you get an email or someone contacts you asking for your password, report it to magicconduct@wizards.com.

I know some of you have seen me repeat this *ad nauseum.* Why do I keep saying it? Because people keep falling for it and losing their cards. Giving away your password is like leaving your binder sitting on the table while you walk out of the tournament room.

### 1800 Room

...won't be for long. Since the original rating choice didn't work out, we decided to take our time deciding what was the best level for the room. We also had to decide whether we were counting a player's Composite rating or either Constructed or Limited rating.

In the end, we came up with a 1700 rating in either Constructed or Limited will get you in the door. While my suggestion of simply crossing out "1800" and adding "1700" over the room icon was briefly considered, the team decided they'd like real art for the room. The art is in, the rating is chosen, and we'll be implementing that in the near future.

### *Mirrodin* Prerelease

Nope, sorry, this isn't more information about when we'll be releasing *Mirrodin* online (still sometime in November). I'm bringing this up because Tuesday was our internal prerelease.

And, boy, did I suck.

In four rounds, I garnered a stunning 2-1-1 record, which is all the sadder when you know that my second-round opponent was a no-show. I played artifacts (yeah, duh, I know) with a splash of white and blue. Some things I learned during the tournament: 

*   I like Goblin War Wagon -- it's an awful lot of fun equipped with Vulshok Gauntlets.
*   Possibly the most annoying first turn play in *Mirrodin* Limited: Plains, Leonin Elder.
*   Nuisance Engine is.
*   Broodstar isn't hard to get out.
*   Broodstar is Terror bait.
*   Players get excited over returning cards -- especially if they used to suck.
*   Prediction: The most common in-game problem on ***Magic** Online* post-*Mirrodin* launch will be mana burn due to not counting artifact lands when playing a spell with Affinity for artifacts.

*Mirrodin* block couldn't come soon enough for me. I think it's going to be a fun replacement for our dearly departing *Invasion* block.

And I fully planned on jumping into the IPA fun last weekend. However, I ended up cleaning the apartment all day (my roommate threatened to clean my desk for me -- no, that's not a good thing). I'll try again this weekend.

-Dan
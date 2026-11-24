---
id: txgfd4m2
kind: article
lang: en
path: /en/articles/feature/2004/08-27-casual-constructed-care-package
title: Casual Constructed Care Package
published: '2004-08-27'
column_slug: feature
column: Feature
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/080427a
    lang_detected: en
    capture_id: 1820652
    url: http://www.wizards.com/default.asp?x=magic/magiconline/080427a
    captured_at: '2006-06-17 22:45:36+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/080427a
    lang_detected: en
    capture_id: 1820652
    url: http://www.wizards.com/default.asp?x=magic/magiconline/080427a
    captured_at: '2006-06-17 22:45:36+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/080427a
    lang_detected: en
    capture_id: 1820652
    url: http://www.wizards.com/default.asp?x=magic/magiconline/080427a
    captured_at: '2006-06-17 22:45:36+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/080427a
    lang_detected: en
    capture_id: 1820652
    url: http://www.wizards.com/default.asp?x=magic/magiconline/080427a
    captured_at: '2006-06-17 22:45:36+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: txgfd4m2
  url: http://www.wizards.com/default.asp?x=magic/magiconline/080427a
  page_key: wizards.com/default.asp?x=magic/magiconline/080427a
  lang: en
  template: classic_asp
  captured_at: '2006-06-17 22:45:36+00'
  capture_id: 1820652
  wayback_url: https://web.archive.org/web/20060617224536id_/http://www.wizards.com/default.asp?x=magic/magiconline/080427a
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: txgfd4m2
  capture_id: 1820652
  url: http://www.wizards.com/default.asp?x=magic/magiconline/080427a
  wayback_url: https://web.archive.org/web/20060617224536id_/http://www.wizards.com/default.asp?x=magic/magiconline/080427a
  captured_at: '2006-06-17 22:45:36+00'
  template: classic_asp
  sha256: a5e4548173779aeebdcdeecbd6bfddb422d44363a0c40223d58cf736f2c6c729
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Relentless_Rats')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Relentless Rats
  occurrences: 1
---
* * *

We've done a lot of things for tournament players on ***Magic** Online* ever since we got Premier Events back up and running earlier this year, but that doesn't mean we've forgotten about the rest of you. We know there's more casual play than tournament play on MTGO and the only reason the tournament players have been getting more attention lately is that their stuff was broken. Luckily, nothing about casual play qualifies as broken. However, that doesn't mean we couldn't be doing things better.

Recently, we took a long hard look at casual play to see if there were things we could improve within the constraints of the 2.x code-base. We have lots of ideas about things we could add once we have a stable, scalable, easily modifiable code-base; but as you've probably read elsewhere we don't have that right now. Most of our programming resources are currently being devoted to coding Version 3a (which will replicate all existing MTGO functionality and allow us to start adding new functionality in version 3b). However, we did find a few things that didn't require significant coding, so we hope you'll enjoy these enhancements:

### New Format: Classic

When the Open format was changed to be truly open, many of you complained that you wanted a format where you could play pre-IPA promotional cards (plus any cards that might be banned in Extended) without running into "degenerate" decks. At first, we didn't think it made sense to create a new format that would just be 4 cards off from Extended, but enough of you kept asking that we revisited the issue and decided to give you want you asked for: Online "Vintage." We aren't going to call it "Vintage" though, because we don't want people to confuse it with the paper-based Vintage format. (Note, for example, that paper-Vintage (also known as Type 1) has a number of restricted cards (like Fact or Fiction) that exist on MTGO but do not need to be restricted in the new online Classic format.)

So starting right after the downtime on Thursday Sept. 2nd you'll notice a new constructed format option when you start a casual game. Classic format games have a minimum deck size of 60 cards, they allow a maximum of 4 copies of each card (other than basic land (and Relentless Rats), of course), and every card available in ***Magic** Online* is legal.

### Quarterly Banned and Restricted List Updates

Every three months, R&D makes a recommendation to the DCI about what cards should be banned or restricted in various formats. Starting with the September 1st announcement, we are going to start covering ***Magic** Online* formats too. Here is a rundown on all the relevant formats and our thoughts about each of them:

*Block Constructed:* All of MTGO's block constructed formats follow the same rules as their paper equivalents.

*Standard:* Standard will continue to be the same format on both platforms.

*Extended:* We like to think of Magic as one game that can be played on two platforms. For that reason we have been very hesitant to separate the Online and Paper Extended formats, especially with only a little over a year to go until the formats are synched up anyway. If the environment becomes radically different on the two platforms, we're willing to separate the lists if we have to. However, we don't think that's necessary at this time. (That was a hint, in case you missed it.)

*Prismatic:* We spent a lot of time talking about Prismatic and debating what we want it to be. (We'd also like to thank all of you who chimed in on the message board thread that Matt Place started – we were happy to have your opinions and they were quite helpful.) In the end, we believe the whole point of Prismatic is that it's kind of random and fun. When you're playing with 250 cards, you should get a lot of different draws and lots of diversity of game-play. For this reason, you should expect us to be very aggressive in banning any card that lets you go get specific other cards. All so-called "tutors" got a lot of scrutiny and we'll be announcing quite a few bannings on September 1st. (Note the paper-based "5-color" format that Prismatic is based on also restricts just about every tutor that gets printed.)

*Tribal:* We have no major changes in mind for Tribal.

*Singleton:* Once again we have no major changes up our sleeve.

*Classic:* Our current thoughts are never to ban or restrict any cards in Classic – it is intended to be the format where you can play everything. The other relevant news about Classic is that Singleton, Prismatic, and Tribal will now use Classic as their base so Morphling, Serra Avatar, and Sliver Queen will be legal in those formats now.

The quarterly B&R List changes usually take effect on the 20th of the month. However, since MTGO changes require a downtime, changes will take effect on the first Thursday after the 20th.

### New Constructed Room

We've noticed a lot of arguments and complaints flying back and forth between players in casual constructed rooms who disagree on what counts as "casual." We think part of the problem is that there are too many people using the "middle" room (also known as the "Casual/Casual room") for too many different reasons. We know Magic is more fun for everyone when they are playing against people who have the same motivations that they do, so we're going to rearrange the casual constructed rooms in an effort to give people more options and make it easier for you guys to self-select.

Here's the new set-up of "Constructed Games" rooms that you'll see inside the Casual Play room after the Sept. 2nd downtime:

*New Players*: No change here – this room is still intended for new players and players with very small collections.

*Casual Decks*: The mouse-over text that describes this room isn't changing – "Find a fun game or casual competition." This is intended to be the more casual side of the old casual room and the biggest difference should come about because the more competitive and/or serious denizens of the old version of this room will migrate to the right.

*Anything Goes*: The mouse-over text for this new room says it all – "All's fair in this room – no whiners allowed." This is the room for anyone who's ever gotten frustrated because their opponent conceded after a Stone Rain or a Counterspell or even a turn 1 Seat of the Synod. This is also the room for anyone who took their pet deck into the old Serious Decks room only to get yelled at for playing something that was too "rogue."

*Tournament Practice*: The name says it all this time – this room is for tournament decks. The new "Anything Goes" room should live about halfway between the old Casual room and the old Serious room. Meanwhile, here's the more competitive side of the old Serious Decks room.

One final change you'll see on Thursday is that we've merged the Sealed Deck Games room with the Limited Games room. Neither room gets a lot of traffic so we don't want to split the casual Limited audience up into two rooms. The biggest impact of this merger is that if you want to play a 1 on 1 sealed deck match, you'll now have to set up an 8-person tournament and then start it with just two people. 

### Conclusion

So there you have it – tune in to [magicthegathering.com](https://web.archive.org/web/20060615195556/http://www.wizards.com/magic/) on September 1st to read the first quarterly B&R Announcement that specifically addresses ***Magic** Online* and then turn on the game the next day to enjoy the new Classic format and the new casual constructed rooms. In addition, anytime you have a suggestion for how to make MTGO a better game, please do point it out on the message boards. We're listening and we do have the ability to make a few small improvements over the next year.
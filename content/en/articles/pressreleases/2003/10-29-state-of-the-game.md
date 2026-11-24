---
id: ecz8kmvn
kind: article
lang: en
path: /en/articles/pressreleases/2003/10-29-state-of-the-game
title: State of the Game
published: '2003-10-29'
column_slug: pressreleases
column: Press Releases
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=magic/magiconline/news102903
    lang_detected: en
    capture_id: 1831303
    url: http://www.wizards.com/default.asp?x=magic/magiconline/news102903,,ja
    captured_at: '2005-02-22 18:44:35+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=magic/magiconline/news102903
    lang_detected: en
    capture_id: 1831303
    url: http://www.wizards.com/default.asp?x=magic/magiconline/news102903,,ja
    captured_at: '2005-02-22 18:44:35+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=magic/magiconline/news102903
    lang_detected: en
    capture_id: 1831303
    url: http://www.wizards.com/default.asp?x=magic/magiconline/news102903,,ja
    captured_at: '2005-02-22 18:44:35+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=magic/magiconline/news102903
    lang_detected: en
    capture_id: 1831303
    url: http://www.wizards.com/default.asp?x=magic/magiconline/news102903,,ja
    captured_at: '2005-02-22 18:44:35+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: ecz8kmvn
  url: http://www.wizards.com/default.asp?x=magic/magiconline/news102903,,ja
  page_key: wizards.com/default.asp?x=magic/magiconline/news102903
  lang: en
  template: classic_asp
  captured_at: '2005-02-22 18:44:35+00'
  capture_id: 1831303
  wayback_url: https://web.archive.org/web/20050222184435id_/http://www.wizards.com/default.asp?x=magic/magiconline/news102903,,ja
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ecz8kmvn
  capture_id: 1831303
  url: http://www.wizards.com/default.asp?x=magic/magiconline/news102903,,ja
  wayback_url: https://web.archive.org/web/20050222184435id_/http://www.wizards.com/default.asp?x=magic/magiconline/news102903,,ja
  captured_at: '2005-02-22 18:44:35+00'
  template: classic_asp
  sha256: ec6e302aececf1b52a6c9a2fe7d18272a0c14512178ddb08236f321c72e61657
render_recovery: []
---
* * *

Before going into the current issue, we'd like to take a step back and publicly state the company's opinion of ***Magic** Online:* ***Magic** Online* is a thriving brand that we here at Wizards of the Coast are very happy with. The game was developed to provide **Magic** players who don't have anyone to play against a convenient way to find opponents. We also hoped that we could grow the overall **Magic** brand by bringing computer gamers into the fold. Both of these efforts have worked out beautifully -- thousands of lapsed players have come back to the **Magic** franchise and thousands of new players have started to play. Make no mistake about it, ***Magic** Online* is seen as a big success at Wizards of the Coast and Wizards of the Coast is going to do whatever it takes to make sure that ***Magic** Online* remains healthy and vibrant.

Last Saturday, due mostly to the free sealed deck tournaments that were part of Chuck's Virtual Party, we had more users logged on and playing **Magic** than we have ever had before. Unfortunately, that was more traffic than the system could handle. We ran out of memory and crashed.

It turns out this is not a simple problem to solve. You might think that we could add more servers to deal with this problem, but that's just not how ***Magic** Online* works. We can add more game servers to handle as many games as people want to play, but there is only one master server that handles everything else that goes on (chat, trading, ratings, etc.). Every time any user does anything outside of a "duel," ***Magic** Online* has to spend some time thinking about that user. As we add more cool new features to the game, the amount of memory that needs to be allocated to each user keeps going up. At some point, when enough users are logged in doing enough things, the whole master server comes crashing down. 

The real story behind Version 2.0 is that all the new features we added gave each user more things to do, and thus the number of simultaneous users we could handle came down below the number that wanted to log in on a daily basis. There were a couple of other bugs associated with Version 2.0, but this was the one that was responsible for most of our crashes.

In order to regain stability, we kept taking new features away until we could handle our normal number of users. (We also rewrote some parts of the code so they would use less memory -- something we continue to do whenever we can.) While this helped the situation, it didn't really "solve" the inherent problem -- all it did was raise the maximum number of users to some number above what we had ever gotten before.

Saturday we found out what our new limit is. It's not a hard limit, because the actual limit depends how many different sorts of things those users are doing (and the line will continue to creep up as we find new ways to allocate memory more efficiently), but there is a line and now we know about where it is right now.

We find this situation completely unacceptable. Wizards of the Coast has plans to grow ***Magic** Online* far above its current userbase and we also intend to keep adding new features and functionality whenever we think of new ways to make the game better. We also would like to host more special events that encourage many players to log in at the same time.

In order to have a permanent solution to this problem, we are currently putting together specifications for an overhaul of the system that will allow us to handle more users simply by adding more master servers. This is a major project that will take a lot of time and effort, but our number one priority is to make sure that ***Magic** Online* is fully scalable so that it can handle all the users and all the new features that we could ever hope to add to it.

Here's what this means for our players: 

*   We plan to maintain the current ***Magic** Online* features and functionality while this project goes on. Players will still have access to ***Magic** Online* and their card collections.  
  

*   New card sets are still scheduled to be released about a month after their paper-based counterparts, but they are the only new functionality we intend to add to the game in the near future.  
  

*   As soon as we can, we will add back the proposed Version 2.0 functionality that has been put on hold, such as auto-matching, the **Casual Trade** room, etc. However, we don't expect that to happen until after we have rebuilt the system's architecture and solved our memory problems.  
  

*   We plan to manage our special events so they don't cause a large spike of simultaneous users. This probably means, for example, that we will need to limit the number of people who can participate in big tournaments (like Release Events) at the same time.

The good news is that once we canceled last weekend's free tournaments, the game was stable again. It's frustrating that we can't do anything really special that would cause a dramatic rise in the number of people who are playing, but we're confident we can maintain the game as a stable, healthy, fun environment for all of you to play **Magic** every day.

The big picture is that ***Magic** Online* has been so successful that we're outgrowing the initial design of the game. In a weird way, this is actually a good problem to have. We are truly sorry that we put the ***Magic** Online* community through this, but we are optimistic that ten years from now we'll look back on this as the ***Magic** Online-*equivalent of the *Homelands* set: Mistakes were made and we shouldn't have done it that way, but we learned from it and the game survived just fine.
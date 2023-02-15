
---
[Link to Wayback Machine](https://web.archive.org/web/20220309104030/https://magic.wizards.com/en/articles/archive/december-state-beta-matchmaking-breakdown-2018-12-12)

[_metadata_:author]:- "Chris Clay"
[_metadata_:description]:- "While we've colloquially referred to the 0.10.00.00 December release as the `Rank Matters` update, as we began to do a full breakdown of all the upcoming changes it became very apparent, very quickly that `Rank Matters` didn't accurately describe all the changes where we were making. For starters, to ensure we got to a point where we could use player ranking in a meaningful"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1376956"
[_metadata_:publish_date]:- "2018-12-12"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "December State of the Beta: Matchmaking Breakdown"
[_metadata_:wayback_capture_timestamp]:- "2022-03-09 10:40:30"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20220309104030id_/https://magic.wizards.com/en/articles/archive/december-state-beta-matchmaking-breakdown-2018-12-12"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/december-state-beta-matchmaking-breakdown-2018-12-12"
---


December State of the Beta: Matchmaking Breakdown
=================================================



 Posted in [NEWS](/en/articles)
 on December 12, 2018 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/Chris%20Clay.jpg)
By Chris Clay












While we've colloquially referred to the 0.10.00.00 December release as the "Rank Matters" update, as we began to do a full breakdown of all the upcoming changes it became very apparent, very quickly that "Rank Matters" didn't accurately describe all the changes where we were making. For starters, to ensure we got to a point where we could use player ranking in a meaningful way, we had to do a complete overhaul of the ranking system. The other part of this was updating and adjusting the way we treated matchmaking, both in our Ranked events and elsewhere. This is where we're going to be talking about the latter.


### Matchmaking Weights


To start things off, here's a break down of the various systems we have at our disposal that can be used as part of our matchmaking system.


* Rank
* Win/Loss Record (Within an Event)
* Player Matchmaking Rating (MMR)
* Deck
* Games Played\*

While it might go without saying, we don't use all of these weights in all of our formats. Case and point, the only time rank matters (#namedrop) in our matchmaking system is when you're playing a ranked event. Other weights, such as the amount of games played, are situational. Below, we break down each of our event types, the system/s they used prior to this update, and any changes we've made with the December update.


### Changes to Matchmaking Rating (MMR)


... but before we get into the nitty gritty details of the upcoming changes, we wanted to take some time to explain what we mean when we say 'matchmaking rating', or MMR for short. Matchmaking rating is our way of trying to ensure that you face the best possible opponent at any given time. What our system considers 'best' pulls from a variety of criteria that will vary depending on the format (such as rank, win/loss record, deck, etc.) player skill, and the amount of time you've spent searching for a match. However, in our breakdown below, when you see "MMR" we are referring specifically to a *player's* matchmaking rating.


We wanted to call this out because in addition to changing some of the weights used in matchmaking, we've also adjusted the calculations and criteria for determining a player's MMR. Even if the current vs. 0.10.00.00 doesn't look terribly different, you should see an improvement in the quality of your opponents across the board. As with most live service games, this will be a living breathing system that we'll likely need to make further adjustments to especially in the next few months. The other half of this is breaking down a player's MMR into three distinct categories: Open Play MMR, Constructed MMR, and Limited MMR (Limited, as in the format type e.g. Drafts)


... And yes, this is a big part of why we're running a couple of preseasons before we get into finer details about who, how, and when you can qualify for some of those [MTG Arena Mythic Championships](https://magic.wizards.com/en/competitive-magic) we recently announced. Your feedback is extremely valuable to us as we test these changes out!


As a final note, all existing MMR values and Rank will be reset as a part of the rollout of Rank 1.0.


### Play (Best of One)


**Current System:** N/A


**0.10.00.00:** Open Play MMR, Games Played, Deck Weight


We're adding a new, unranked best-of-one format to replace our previous Ladder Play option. This event will primarily look at one of the new MMR categories we've designated to be used specifically for unranked events: Open Play MMR. Once the queue has matched players within a similar Open Play MMR range, we'll do a secondary check that takes into consideration they deck they're playing. This new system should ensure that players are more accurately matched on both their skill and deck strength, while hopefully cutting down on the amount of mirror matches since MMR and Deck are two independent checks (instead of tied together, as they were previously).


Last, the matchmaking system will look at the number of games played (up to 50) that will allow us to ramp up new players into a larger, more experienced pool of players over time. Combined with the other changes, this should also make some of the earlier matches against other players more new player friendly.


Again, this does replace the previous "Play" option which used a combination of Deck Weight + MMR for matchmaking, and game results affected your constructed rank. For those of you looking for a ranked option without deck weighting, keep reading!


### Traditional Play (Best of Three)


**Current System:** N/A


**0.10.00.00:** Open Play MMR


We're also adding a new unranked best-of-three queue that only matches players based on their Open Play MMR. This is a place for players who want to do some test-driving of their decks before entering into a Traditional Constructed events where they can compete for prizes.


### Ranked (Best of One)


**Current System:** N/A


**0.10.00.00:** Rank, Constructed MMR


With the new Ranked queue for best of one we'll be testing out the new ranking systems. Players will primarily be matched based on of their Rank, with a secondary look at their Constructed MMR. Like our 'Play' option, there’s no entry or rewards in Ranked. Unlike "Play", Ranked won’t use Deck Weight or games played as part of matchmaking, and instead we will primarily be matching players based on (you guessed it), Rank. For the first preseason, all the tiers within a rank will be weighted equally for the purposes of matchmaking (e.g. Bronze 3 carries the same weight as Bronze 1).


### Ranked Draft (Best of One)


**Current System:** Win/Loss Record


**0.10.00.00:** Rank, Win/Loss Record, Limited MMR


With Ranked Draft we will be trying out something new by adding ranking that matters to our limited offerings (#namedrop). The primary matching metrics will be the player's Rank and Win/Loss Record, with a secondary look at their Limited MMR to double check that the pairing is a good match-up. This does mean that as player's increase in rank they will face more challenging opponents, but it also means that players looking to enter into Limited for the first time are more likely to be paired against opponents at their skill level. We'll be watching how this plays out closely, but we believe it will be a large benefit to the game as a whole.


### Traditional Draft (Best of Three)


**Current System:** Win/Loss Record


**0.10.00.00:** Win/Loss Record


We know that an important part of our player base who prefers a more Swiss style of matchmaking, where your first round pairings are randomized and subsequent rounds are based on your Win/Loss record. Traditional Draft is one of those events, and will remain unchanged in how it matches with the release of the December update.


### Sealed (Best of One)


**Current System:** Win/Loss Record


**0.10.00.00:** Win/Loss Record, Limited MMR


Sealed pairings will primarily be on Win/Loss Record, but will now include a secondary check to compare Limited MMRs between players. This is something we hope will ensure newer players have better match-ups for this popular event.


### Constructed Event (Best of One)


**Current System:** Win/Loss Record


**0.10.00.00:** Win/Los Record


While we're implementing changes to our Constructed Events, it's not in the form of matchmaking. As with Traditional Draft, we do believe there is a place in Arena for events that only look at the participating players' Win/Loss record. The 'cause for concern' with Constructed Events is the amount of players who jump into them using unmodified NPE decks, only to find themselves facing off against someone using a deck that was featured prominently at a recent Pro Tour. Our current theory is that by including ICRs as part of the prize pool, newer players are given the impression that this is a event that can help them build out their collection - which *is* the intent behind including ICRs in some of our more casual events like Singleton and Pauper.


To try and combat that, we're removing ICRs and making up for this by adjusting the amount of gold players can earn as prizes. In the future, we may look at other ways we can communicate to players that they should expect a specific level of play, such as recommending a certain Constructed rank before participating.


### Traditional Constructed Event (Best of Three)


**Current System:** Win/Loss Record


**0.10.00.00:** Win/Loss Record


See Above (Constructed Event, Best of One)


### Special Events (Momir, Pauper, Singleton, etc.)


**Current System:** Win/Loss Record


**0.10.00.00:** Win/Loss Record


These events are meant to be fun, casual, and for everyone. We feel we've hit a good spot with the event structure and rewards, making it 'worth your while' without putting too much emphasis on the benefits of winning. We like how the straightforward Win/Loss record works for these type of events, so for now we're going to keep it that way.


### FAQ:


**What's the difference between Rank and Player MMR?**


To put it simply, Rank is a goal, and MMR helps determine who you're competing against to reach that goal.


**Is Player MMR the same as Elo?** 


Elo, or an 'Elo rating' is a well-known method for calculating the relative skill levels of players in games, and has been historically used in matchmaking systems as a way to ensure that pairings are 'fair'. But just like all squares are rectangles but not all rectangles are squares, not all matchmaking systems use Elo. Even with matchmaking systems that do incorporate Elo-based calculations, many competitive organizations will make adjustments or use a derivative system to fit the specific needs of their games and/or competitive scenes (using our rectangle example, you might consider these systems rhombuses). Some games have even forgone Elo entirely, and instead use other established algorithms to quantify skill level or even develop their own in-house system. However, because Elo is such a well-known rating system, some people will use it as shorthand for whatever their player skill rating system is, even if it's being calculated by a completely different method.


... which is a really long way of saying "No, our Player MMR is not the same as Elo." This has always been the case and is not changing with this update, but we wanted to clarify that even if you see someone refer to it as Elo, it's not.


**Why is MMR separate?** 


There are two distinct parts to this. First and foremost, as many long time Magic: The Gathering players will probably attest to - Constructed and Limited are very different formats. Using a singular MMR across all our event types and modes could lead to some unfun, and downright unfair match-ups for people who play regularly in one format, but only occasionally in another. We also wanted to ensure that a players Rank was not wholly dependent on their MMR. While the two are related (matchmaking has a very real impact on a players ability to progress to a certain Rank), we can now make adjustments to our MMR without it changing your Rank. It also means that we can have seasonal rankings and resets without resetting MMR as well.


And yes, it also creates a bit of a 'safety net' against players who are willing to sacrifice their Limited Ranking (or vice versa) to lower their MMR and ensure "easier" matches in their format of choice.









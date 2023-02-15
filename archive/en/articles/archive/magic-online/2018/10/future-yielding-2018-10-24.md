
---
[Link to Wayback Machine](https://web.archive.org/web/20181030130128/https://magic.wizards.com/en/articles/archive/magic-online/future-yielding-2018-10-24)

[_metadata_:author]:- "Madison Mosley"
[_metadata_:description]:- "The yield menu in Magic Online is getting a much-needed quality of life update!"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1356231"
[_metadata_:publish_date]:- "2018-10-24"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "The Future of Yielding"
[_metadata_:wayback_capture_timestamp]:- "2018-10-30 13:01:28"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20181030130128id_/https://magic.wizards.com/en/articles/archive/magic-online/future-yielding-2018-10-24"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/magic-online/future-yielding-2018-10-24"
---


The Future of Yielding
======================



 Posted in **Magic Online**
 on October 24, 2018 






![](https://web.archive.org/web/20190313185225im_/https://magic.wizards.com/sites/mtg/files/styles/auth_small/public/images/hero/2018_Daily_WOTC_icon_0.jpg?itok=-EnkrYxy)
By Madison Mosley











Hi, I'm Madison! I'm one of the developers for *Magic: The Gathering Online*. Most of my work is in updating and maintaining the MTGO client. This includes adding new visual treatment for existing features, improving performance, and implementing client-side support for new game mechanics. When one spends enough time in these areas, they find themselves at the smart end of a deluge of ideas that usually results in a series of saved code changes numbered and titled "Features I Wish Existed." Often, these ideas can have some lofty overhead, and not all these ideas for features persist through the scrutiny necessary to warrant implementation. Sometimes, however, the proposal of a feature demonstrates enough utility that it makes its way through the process. This, dear reader, is the harrowing account of one such feature that has ascended from its abstract form and manifested into reality!


The tale begins not long ago. I was tasked with updating the visual treatment for yielding to triggered abilities, yielding until end of turn, and yielding until a specific point on the phase ladder. While testing my updates, I couldn't shake the feeling that there was something unseen calling out to me, like an ancestral spirit whispering in my ear. "No, you must remove *all* of the yields and start over again. Every time." I turned around slowly to find that this voice belonged to my teammate Shaun, and that the immediate area was still, to my knowledge, not actually haunted. Now that the first mystery was solved, Shaun and I decided it was heart-of-the-matter time.


Yields, we agreed, are underrated. They filter out noisy trigger pop-ups while simultaneously increasing the visibility of the abilities to which you *do* want to respond. They let players skip multiple response prompts at a time, effectively removing would-be obstacles to a more streamlined and custom gameplay flow. The only shortfall is that players can't remove them individually, which becomes a headache if one of those fourteen abilities that cascade into 40 triggers on the stack threatens to steamroll high-impact cards into exile if allowed to resolve. Shaun made some offhand comment about UI for removing yields individually or something when I was struck suddenly with divine inspiration. "I have the solution! UI that lets players see and remove individual auto-yields they have set!" I said, and set out cackling upon my merry path.


Since I had just spent a bunch of time figuring out the auto-yield system, I figured this would be a good focus for the several days of free development time the MTGO team had scheduled. I threw together a prototype of the UI: a context menu that displays all auto-yields the player currently has set, which card the ability belongs to, and the card's owner. Admittedly, this was as far as I expected the project to go. That is, until I showed the prototype to my other teammates. "This actually would be nice to have," they said. "*Actually* . . ." I replied, quickly recalculating my angle of approach, "I'm taking it to the shot-callers right now!" So, taking my *totally* original idea to Design, I was given the greenlight to implement the whole thing as a full feature with the stipulation that I not actually name it "The Madison Menu."


Though my ego had taken an *L*, the initiative for a better tomorrow (with respect to auto-yields in *Magic Online*) was underway. For the yield menu to be fully implemented, we needed a way for the server to remove yields individually instead of all at once. I asked some of my teammates if they could modify the game server to support this. They swiftly obliged with a state message sent from the server to the client at relevant intervals that contained current auto-yield info. I added handling for this type of message and a data class that would hold the information extracted from the message for the lifespan of the game. Next, I wired up the model, a list of data class objects to be referenced for display in a context menu, displaying which auto yields are currently active on the server side, with the added functionality of being marked as "pending removal." From there, I needed only to write a new type of message to the game server that would inform it which auto-yields the client would like to remove. After some visual indicator placement revisions, style template iterations to ensure client appearance uniformity, and an "on mouseover" highlight that adds a more tactile feel (a design tenet I will almost certainly harp on ad nauseum in future dev blogs), it was showtime.


Enter the yield menu! Haven't noticed it yet? Well, everyone get in the lotus pose and follow me in some guided meditation.



![](https://media.wizards.com/2018/images/daily/MTGO20181024_Nightmare.jpg)
Let's say you're building up a board state that has a bunch of upkeep triggers to retain sanity . . .



![](https://media.wizards.com/2018/images/daily/MTGO20181024_Vial.jpg)
You probably want to add all of these to the auto yield list. Before, if you had anything on the nominal auto-yield list you had to dump the whole thing and add back the triggers you still want to ignore.



![](https://media.wizards.com/2018/images/daily/MTGO20181024_Yield.jpg)
However you look at it, it disrupts the flow of gameplay and requires extra effort. But no more!



![](https://media.wizards.com/2018/images/daily/MTGO20181024_Saved.jpg)
Now you can bring up the visual list of all active auto-yields with a single mouse click! Mark only the ones you want to get rid of for removal, leaving the things you still want to ignore in place. If you miss that old-school style of dumping the whole list, there is still a "select all" option for removing! The yield menu is fun for the whole family, making MTGO a little slicker, one yield at a time.








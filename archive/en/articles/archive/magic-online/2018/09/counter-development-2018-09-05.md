
---
[Link to Wayback Machine](https://web.archive.org/web/20180910002951/https://magic.wizards.com/en/articles/archive/magic-online/counter-development-2018-09-05)

[_metadata_:author]:- "Christopher Bellach"
[_metadata_:description]:- "Take a look at the brand-new counter icons coming to Magic Online!"
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
[_metadata_:node]:- "1334846"
[_metadata_:publish_date]:- "2018-09-05"
[_metadata_:source]:- "div-main-content"
[_metadata_:title]:- "Counter Development"
[_metadata_:wayback_capture_timestamp]:- "2018-09-10 00:29:51"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20180910002951id_/https://magic.wizards.com/en/articles/archive/magic-online/counter-development-2018-09-05"
[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/magic-online/counter-development-2018-09-05"
---


Counter Development
===================



 Posted in **Magic Online**
 on September 5, 2018 






![](https://media.magic.wizards.com/styles/auth_small/public/images/person/wizards_authorpic_larger.jpg)
By Christopher Bellach











Welcome, my fellow Planeswalkers and fans of *Magic Online*. My name is Christopher Bellach, and I am one of the client developers for *Magic Online*. Today, I'm excited to share with you the details for an update I have been working on to the *Magic Online* counter system. But before we get to those details, I would like to give you all some of the history on how I came to work on the *Magic Online* client.


I've been playing *Magic: The Gathering* since around when *Mirage* was released and have been a fan ever since. I started playing *Magic Online* around the time *Mirrodin* was released, and it quickly became one of my favorite games. When I started my career as a software developer, I began dreaming of working on *Magic Online* with the hopes that I could help *Magic Online* continue to be the great game we all love to play. When I finally committed to getting a job working on *Magic Online*, I scoured the [Wizards job page](http://company.wizards.com/content/jobs) until I found a post that matched my skill set. Once I had zeroed in on my target, I did everything within my power to earn the job. I even went so far as to find the contact information of the recruiter to ensure I was on their radar. Finally, in February of 2014, I accepted a position at Wizards of the Coast. I've been living the dream ever since.


Now, let's talk about counters. Historically, *Magic Online* hasn't had a whole lot of variety with its counter icons. Before this update, we had five different types of counter icons: plus, minus, loyalty, charge, and generic. With this update, we have 28 distinct icons with a possibility of 84 different variations. This makes it clearer at a glance what counters are on your cards and gives a little personality to the menagerie of counters in *Magic: The Gathering*. We also designed the new counter icons to increase visibility for streamers and their fans, with clear shapes and large numerals.


![](https://media.wizards.com/2018/images/daily/tLOMsmehCX_02.jpg)


Below is a table that details each new counter icon and what they will be used to represent. In general, green counters are used for positive effects, orange counters are used for negative effects, and blue counters are used for neutral effects. I also took some liberties on a couple counters for thematic reasons: the blaze counter is always orange, and the flood counter is blue. If there's only one counter on a card, you won't see a number on the counter icon, but once there are multiple counters on a card, the count will show up.


While updating the way that counters looked like in general, I took the opportunity to improve the visibility of counters in other zones. In the past, counters were hard to access on cards in other zones outside the battlefield or on cards that are attached to other cards. So, I found some solutions that should help alleviate those frustrations. For cards in other zones, like suspend cards, the cards will now detect that they have counters and claim more vertical space to display them fully. For cards attached to other cards, like [Umezawa's Jitte](http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Umezawa%27s+Jitte), the counters will now move to the left side of the card, so you can easily view the counter without zooming in on the card. To accomplish this, I had to flip the rendering of the graphic and adjust the placement of the elements of the counter.


![](https://media.wizards.com/2018/images/daily/7dmx7l9HBs_01.jpg)![](https://media.wizards.com/2018/images/daily/8hIlqQOKjG_03.jpg)


That is all I have for today. Thanks for taking the time to read my article, and I am excited for everyone to get an opportunity to use these new counters. We have some more exciting updates in the pipeline, so stay tuned, and I look forward to sharing those with you all once they are ready. See you next time, and may all of your packs have epic foils!




|  |  |  |  |
| --- | --- | --- | --- |
|   |  

  |  

  |  

  |
|  

  | — | +1/+1 | — |
|  

  | — | — | -1/-1 |
|  

  | — | Egg, Hatchling, Hoofprint | Prey, Shell |
|  

  | — | Credit, Theft, Wage | Bounty, Hit |
|  

  | — | Flame, Fury, Fuse, Shred, Spite, Strife | Blaze |
|  

  | — | Brick, Cage, Tower | — |
|  

  | — | +1/+2, +1/+0, +2/+2, +0/+1 | — |
|  

  | — | Charge, Crystal, Gem | — |
|  

  | Doom | Despair | Death, Mannequin, Paralyzation, Petrification |
|  

  | — | - | -1/-0, -2/-1, -2/-2, -0/-1, -0/-2 |
|  

  | — | Devotion, Divinity, Dream, Elixir, Fate, Healing, Intervention, Omen, Unity, Wish, Hunger | — |
|  

  | Flood, Ice, Tide | — | — |
|  

  | — | Blood, Carrion, Corpse, Eyeball, Infection, Plague | — |
|  

  | — | Fungus, Growth, Petal, Polyp, Spore, Vitality, Matrix | Pupa, Rust |
|  

  | — | Awakening, Echo, Luck | Glyph |
|  

  | — | Ki, Manifestation | Sleight |
|  

  | — | Loyalty | — |
|  

  | — | Pin, Training | Net |
|  

  | — | Mining, Pressure, Winch, Silver, Storage, Trap | Magnet, Mine, Ore |
|  

  | — | Scroll, Verse | Music, Sleep |
|  

  | — | Filibuster, Landmark, Level, Lore, Page, Plot, Quest, Sturdy | — |
|  

  | Scream | Pain | — |
|  

  | — | Aim, Arrow, Arrowhead, Javelin | — |
|  

  | — | Muster, Phylactery, Shield | — |
|  

  | — | Slime, Soot | Mire |
|  

  | Delay, Time | Age, Eon, Fade, Hour, Isolation | Depletion, Hourglass |
|  

  | — | Treasure | Bribery, Gold |
|  

  | — | Feather, Vortex | Velocity, Wind |








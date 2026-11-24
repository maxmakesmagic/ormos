---
id: 45h1epeh
kind: article
lang: en
path: /en/articles/makingmagic/2010/09-05-something-wicked-this-way-comes-part-1
title: Something Wicked This Way Comes, Part 1
published: '2010-09-05'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
    lang_detected: en
    capture_id: 229214
    url: https://magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
    captured_at: '2024-05-18 04:01:56+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
    lang_detected: en
    capture_id: 229214
    url: https://magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
    captured_at: '2024-05-18 04:01:56+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
    lang_detected: en
    capture_id: 229214
    url: https://magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
    captured_at: '2024-05-18 04:01:56+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
    lang_detected: en
    capture_id: 229214
    url: https://magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
    captured_at: '2024-05-18 04:01:56+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 45h1epeh
  url: https://magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
  page_key: magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
  lang: en
  template: contentful
  captured_at: '2024-05-18 04:01:56+00'
  capture_id: 229214
  wayback_url: https://web.archive.org/web/20240518040156id_/https://magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
- document_id: 45h1epeh
  url: http://wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/107
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/mm/107
  lang: en
  template: aspx
  captured_at: '2013-11-28 06:36:27+00'
  capture_id: 639035
  wayback_url: https://web.archive.org/web/20131128063627id_/http://wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/mm/107
- document_id: 45h1epeh
  url: https://magic.wizards.com/en/articles/archive/feature/something-wicked-way-comes-part-1-2010-09-06
  page_key: magic.wizards.com/en/articles/archive/feature/something-wicked-way-comes-part-1-2010-09-06
  lang: en
  template: drupal
  captured_at: '2022-01-20 08:10:09+00'
  capture_id: 681741
  wayback_url: https://web.archive.org/web/20220120081009id_/https://magic.wizards.com/en/articles/archive/feature/something-wicked-way-comes-part-1-2010-09-06
- document_id: 45h1epeh
  url: https://magic.wizards.com/en/articles/archive/making-magic/something-wicked-way-comes-part-1-2010-09-03
  page_key: magic.wizards.com/en/articles/archive/making-magic/something-wicked-way-comes-part-1-2010-09-03
  lang: en
  template: drupal
  captured_at: '2022-07-07 13:50:22+00'
  capture_id: 924042
  wayback_url: https://web.archive.org/web/20220707135022id_/https://magic.wizards.com/en/articles/archive/making-magic/something-wicked-way-comes-part-1-2010-09-03
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 45h1epeh
  capture_id: 229214
  url: https://magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
  wayback_url: https://web.archive.org/web/20240518040156id_/https://magic.wizards.com/en/news/making-magic/something-wicked-this-way-comes-part-1
  captured_at: '2024-05-18 04:01:56+00'
  template: contentful
  sha256: 8a9d1be4ef6460d9600e0dcee54c58f6c8f8f724368b6311419d30c988413533
render_recovery: []
---
Welcome to the first week of *Scars of Mirrodin* previews. Man, that felt good. This set is the culmination of so many things and I've had to bite my tongue about it for years, so the chance to actually talk about it is making me a little giddy. There are many facets to the set and I'll be talking about most of them during the three preview weeks (and beyond). Today, though, is all about the greatest quest I ever undertook as a designer: to get poison into a set as a major element. This quest has taken sixteen years (fourteen from the first time I tried to get it in a set). This column is that story. Well, at least Part I. Also before the column is over, I'll let you meet a mythic creature with infect.

### "If You Build It"

Before I start my story though I need to introduce the co-conspirators in my journey to make a poison set (a.k.a. my design team). The reason the team is bigger than normal is that half way through design we, for a variety of different reasons, changed up the team.

![](https://i.ormos.uk/36/f7/36f721b7d86cd6baa42e539d43b8e75e0b0213a5a1b8570f547b0e9cfc889867.jpg)

**Mark Rosewater (lead)**

I lead the design for *Mirrodin*, I'm a giant fan of the Phyrexians and nothing was going to keep me from making the set that brought poison back. To paraphrase Mel Brooks: It's good to be Head Designer.

![](https://i.ormos.uk/92/ce/92ceeab73eb3a7f33920535b070768559eb14c5b512cccee052bbb624575be15.jpg)

**Mark Globus** 

Mark is probably best known for being one of the Great Designer Search finalists (he tied for fourth) and one of the four to segue it into a fulltime career at Wizards. Mark is now the Producer in **Magic** R&D, overlaying some order to R&D's chaos. His contributions to this set were invaluable.

![](https://i.ormos.uk/2c/91/2c91c356c244bac703be5454524033ba3e82399c4aa0766ca588b15370ade280.jpg)

**Mark Gottlieb**

Now that Mark is no longer my arch-nemesis (as he has handed off the role of Rules Manager to Matt Tabak), I can now openly say that I am always happy to have him on my design teams, as he is an excellent designer. Having spent years defining boundaries, he's really good at venturing outside them.

![](https://i.ormos.uk/0c/b5/0cb54b384001d1acbb5c7a06d75a144e86a09ce888e594b4490baf3bda16e36c.jpg)

**Nate Heiss**

Nate has since moved on to another game company, but I was glad to have him while he was at Wizards. His work came during the early chaotic part of the design so it was nice having his vantage point which was one uniquely his own (an awesome complement for a designer).

![](https://i.ormos.uk/ee/e0/eee0d44326785d6cab5488c0c4ad1ad943d8c6ff2b26281945c039e7527772dc.jpg)

**Alexis Janson**

Alexis was the winner of the Great Designer Search. Alexis won because she's a damn fine designer and my experience with her on *Scars of Mirrodin* did nothing to sway my opinion of her design work.

![](https://i.ormos.uk/62/d7/62d7e2c9ff49bab730e0151784d179a3178e53289b8a9fd4e5f808c086ac4351.jpg)

**Erik Lauer**

No one in R&D thinks like Erik Lauer. Probably no one on this planet thinks like Erik Lauer. I always love to have a development insight on a design team and Erik was our developer for the first half of design.

![](https://i.ormos.uk/ea/a3/eaa36db8b94a55ec752ca93412586ac318b349d51a69f2f46c61d00f9c6668ab.jpg)

**Matt Place**

And the developer for the second half was Matt. As with Nate, Matt has gone on to work for a different game company. As this is Matt's last team appearance and thus the last time I get to talk about him in a bio, I just wanted to take a minute to say how awesome Matt was. Most of the developers are very logical and tend to approach problems systematically. Matt worked much more on feel and I believe a lot of the goodness of the last few years came out of this ability of Matt's to see the bigger picture. *Rise of the Eldrazi* was Matt's last lead (as a lead developer) and his touch is all over that set. I was very sad the day I learned that Matt had chosen to leave and I wish him the best in his future endeavors. They say that the surest way to improve is to work with the best. Working with Matt did a lot to make me a better designer.

### Once Upon a Time

With that out of the way, let's talk about my quest to make a poison set.

Our story begins with the release of the *Legends* expansion. The year is 1994 and I, at the time, was just another **Magic** player. Okay, I was making **Magic** puzzles at the time but I hadn't even started doing my freelance writing for *The Duelist* yet. (That would happen later in the summer at Gen Con. You can read about that story [here](/en/articles/makingmagic/2006/02-20-life-lessons-part-i), in life lesson #5.) I've been working on **Magic** for a long time, but in the beginning I was, like all of you, just a player.

I arrived early at the game store to wait in line because back then if you wanted to get a **Magic** set you had to be there the day it went on sale. I bought two boxes, went back and bought a third and then went back and bought a fourth, you know to put away. (I later traded away my *Legends* box for a case of *Revised*, which years later I sold to buy a giant television that I still watch to this day.)

I remember ripping open my *Legends* booster packs (there was no Draft back then to save them for) when I came across this card:

![](https://i.ormos.uk/36/6d/366d56f5585a2d5b534f21dfe05df912c03fdb5ada5471e0845b2e63571dbaf2.jpg)

Some people don't believe in the existence of love at first sight. I believe those people just haven't experienced the phenomenon. I've often talked about how I'm a Johnny. I love building decks with a challenge to them and poison was right up my alley.

The very next booster pack I opened this:

![Serpent Generator](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Serpent+Generator)

 

Imagine you spot the girl of your dreams across the floor. She then spots your gaze, walks up to you and says, "You play **Magic**? I love that game." I was smitten. Or smitten squared, whatever the proper word is for experiencing love and extreme joy mixed together and served with ice cream. I already had strong feelings for **Magic**. Poison just took the relationship to the next level.

I then started ripping open my *Legends* boosters even faster. More poison. I needed more poison. Alas, Pit Scorpion and Serpent Generator were all I was going to get. *Legends*' poison theme was on two cards. Okay, I was a Johnny. I could adapt. I made some decks. My win ratio was low but I got the taste of poisoning my opponent to death.

The very next expansion, *The Dark*, brought this card:

![Marsh Viper](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Marsh+Viper)

 

Hmm, a creature with poison could give more than one poison counter. I liked. The power level of Marsh Viper matched Pit Scorpion and Serpent Generator—it was low, but I was Johnny and power level scared me not.

Poison did not show up in *Fallen Empires* or *Ice Age*, much to my dismay. Then came *Homelands*. There are many reasons to dislike *Homelands*. I have stated numerous times that I believe it was the biggest failure of **Magic** design in the game's seventeen year history. The reason I hated it most though was one card. *This* card:

![Leeches](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Leeches)

 

This card was a slap in the face of every poison lover. One of the things I had always loved about poison was that it differed fundamentally from life in one important way—you couldn't get rid of it. Once you were poisoned, that poison would always be there. In addition, thanks to the low power level of poison, it was hard enough to win with poison. Did the game really need an answer to a threat this anemic?

![](https://i.ormos.uk/91/23/91236e878dcc222a6b835e49e9431e0567a8f575f1814fd2867bf3f4912b6cb9.jpg)

My hatred of Leeches did one important thing. It cemented in me the importance of poison not just being another life total. (This theme will become very important in *Scars of* *Mirrodin*'s design.) As such, you will not see any card in the entire *Scars of Mirrodin* block that removes poison. It cannot be done. There are answers. There are ways to deal with poison but healing yourself of it is not one of them. If you want to remove poison counters you will only have one way—Leeches.

Now we get to the part of the story where my quest truly begins. You see, I knew if I was going to make the poison set a reality, I had to have some goals. What follows are the steps I took to make my dream a reality.

### The Quest for Poison, Step #1—Get Employed by Magic R&D

For many, *this* is the end step, *this* is the quest. For me, it was just the beginning. I knew if **Magic** was going to have a poison set, I was going to have to do it myself.

Quick aside—is getting into **Magic** R&D to do design your end quest? As I mentioned in my column [last week](https://web.archive.org/web/20100905000000/https://magic.wizards.com/en/articles/archive/thank-you-sir-may-i-have-another-2010-08-30) we are going to be doing The Great Designer Search 2. The winner gets a six-month design internship in **Magic** R&D. You can click the link to see all the details, but the biggest take away is make sure to be back here on September 29th to enter.

Okay, so to try and get a poison set made I had to acquire a job in R&D. This is one of the easier steps so I don't feel a need to go into all the details. (Plus if you're a regular reader of my column, I might have mentioned them once or twice.) My first assignment was being on the development team for *Alliances*. The team had, I believe, thirteen members. Basically, any member of R&D that was able to sit in a chair was put on this team. There's a great story behind this as the release of *Alliances* was a crucial make or break moment in **Magic** history, but that's a story for a different column.

It was during development that I got the first glimpse of this card:

![Swamp Mosquito](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Swamp+Mosquito)

 

One of the things I loved about each new poison card was that they hinted at potential. Swamp Mosquito, for example, didn't have any power. Normally, 0-power creatures don't win games, but the Swamp Mosquito could.

The next set was *Mirage*. I was again on the development team. Remember that I was hired as a developer. My chance to prove myself as a designer was coming but we aren't quite there yet. I don't exactly remember if the *Mirage* design team (Bill Rose, Joel Mick, Charlie Catino, Don Felice, Howard Kahlenberg, and Elliott Segal) created the two poison cards or whether I tried to get them added in development. All I remember is that I pushed hard to include poison in *Mirage*. The end result was these two cards:

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Crypt Cobra" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Crypt+Cobra"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Sabertooth Cobra" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Sabertooth+Cobra"></div>&#10;			</div>&#10;			</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

As always the power level was low and Crypt Cobra killed you with damage before it could kill you with poison (a problem *Scars* would tackle) but I felt I was a least pushing in the right direction. I was also on the development team for *Visions* where this card was released:

![SuqAta Assassin](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=SuqAta+Assassin)

 

This was a long time ago so I'm not sure whether I designed this card or just got the fear added, but I was determined to make a poison card that someone who made poison decks would want. As always it wasn't costed aggressively but at least it managed to finally put evasion on a poison creature. (Yeah, yeah Swamp Mosquito had flying.) I liked it. Good thing I liked it because **Magic** wasn't going to see another poison creature for ten years! Not for lack of me trying though.

### The Quest for Poison, Step #2—Become a Magic Designer

I've told this story before, but here is the synopsis of it. I was hired to be a developer but what I really wanted to do was direct, I mean design. To accomplish this, I had to convince Joel Mick, the then Head Designer & Developer (it was one job once upon a time) to give me a chance to design a set. I mostly accomplished this by convincing Richard Garfield to be on my design team (he hadn't done any **Magic** design in years at the time). The set I was given to prove myself was *Tempest*.

The *Tempest* design team was Richard, Charlie Catino, myself, and a new R&D member named Mike Elliott. Like me, Mike was wanting to prove himself as a **Magic** designer. (Mike would go on to lead design more sets than anyone in **Magic** history save myself—although give Tinsman some time.) Early on I presented the team with my desire to do a **Magic** set where poison was a strong component of the design. They liked my passion and all got on board.

![](https://i.ormos.uk/ff/f1/fff103bd0d5b92fc26476d3265a9a9b8e96e230a7284dea8459764b26a8cc19c.jpg)

The codename for *Tempest* was Bogavhati (Vhati 'il Dal was an Easter egg in the set which referenced the codename). Bogavhati (grossly misspelled by us—the actual name is Bhogavati) is a mythical Hindu land of poisoned snakes. The codename was chosen to specifically play up the strong poison theme. Fifty-eight of the three hundred and thirty cards turned in from design referenced poison on them.

![](https://i.ormos.uk/59/09/59091f47ffa363eac562d7d1db98cfc30efd38788a3209228832fd52830dd529.jpg)

So what happened? At first development just cut down the number. Fifty-eight became thirty-two, then twenty-two, then sixteen, then eight, then four, then two and finally one. Then we had one of our weekly meetings were the topic came up: should we even be supporting poison. It was a weak theme that required tracking a number. The majority of R&D felt as if it didn't have a place in **Magic**. Poison was no longer something **Magic** was going to do.

![](https://i.ormos.uk/06/4e/064e6bd5356fc2f74f606ca8d8b31fe6af2a487d3ac2d353590425ed3b58fc26.jpg)

I won't lie, this was a bit of a setback. But what is a quest if there aren't some obstacles along the way? I wasn't going to let R&D removing the mechanic from the game stop me from making a poison set. I just needed to figure out how I was going to do that.

### The Quest for Poison, Step #3—Think Outside the Box

Despite the removal of poison, my design for *Tempest* was considered a success. I had officially become a **Magic** designer. My next set as lead designer was *Unglued*. It was wacky and different and did all sorts of things **Magic** would never do. Wait, did I just say "things **Magic** would never do"? Let me look back two sentences. I did. Unfortunately, the way the timing worked, I was almost done with *Unglued* at the time R&D punted poison from game. *Unglued* would have been a perfect place for poison if only I had known about it earlier.

![](https://i.ormos.uk/f6/7c/f67c355121661e3b3a162d2283deec705a4db89917c615aeefeb739c8e9c2946.jpg)

The initial buzz for *Unglued* was very high. So much so that it was decided we were going to do a second one the following year. Known internally as *Unglued II: The Obligatory Sequel*, the set was handed to me. If I wasn't allowed to do poison in "real" **Magic**, then I thought I'd do it in silver bordered world.

*Unglued* had a theme of chickens. I wanted *Unglued II* to have an equal silly theme. I also knew I wanted the center of the design to be poison creatures. My plan was to tie the sets overall theme to whatever I chose to be the poison creatures. I ended going up with animated vegetables. My idea was for the poster to say: "Not all vegetables are good for you."

Quick aside, to support the vegetable theme I asked all the artists to hide at least one vegetable in their art. Some of the art from *Unglued II* ended up getting used in *Unhinged*. This is why there are some vegetables hidden in the art of certain *Unhinged* cards.

![](https://i.ormos.uk/f4/f8/f4f8b4ebfee800301480c72fb80797ef7cdb5422c88cb544cf91dbebc9e2ad3e.jpg)

What doomed poison this time was economics. While *Unglued* had a lot of early buzz, we printed too much of it and glutted the market. This soured distributors on the *Un*-sets and it was decided by the **Magic** brand team that *Unglued II* needed to be put on hiatus, one from which it would never return. (To be fair, many of the cards and art from *Unglued II* made their way into *Unhinged* many years later.)

That is, of course, the official story. I believe it was just "the man" trying to keep poison down.

### The Quest for Poison, Step #4—Be Patient

The ultimate solution to many problems is time. Realizing that R&D was not in a place where it was possible to make a poison set, I chose to lay low with poison and wait until R&D shifted to a place where I thought I could try again. My method was to occasionally bring up poison as a joke and see what kind of response I'd get. Eventually I realized that R&D had had enough turnover that it was time to start working in earnest again.

### The Quest for Poison, Step #5—Become Head Designer

It appears that my one-minded quest to create a poison set was good for my career. The reason becoming Head Designer was so important is that it's the Head Designer who's responsible for the big picture of each block. If I was ever going to see poison's return, I realized I had to think bigger. I had to create an environment where poison made sense, an environment where it seemed wrong not to do poison.

![](https://i.ormos.uk/9e/32/9e329751671400d7737ba846fea3a1f66418ef1759471fa7377e2f8ed3eff947.jpg)

And then along came *Future Sight*. It was a set that glimpsed the future, not just the actual future but potential futures. You see, in order to hide the future, we had to offer many futures. While we were showing off things we intended to do we needed to mix in things we had no intention of doing as well, to keep the mystery alive. What better place to include poison. In my mind it was the actual future but the set had to have false futures as well. Those in R&D that didn't think poison would ever come back would merely assume it was one of the false futures.

As I was the one who came up with the concept of *Future Sight* as well as lead its design, you might assume I did so specifically to find a place to include poison once again. Alas, I have to admit that I was not that devious. I found the perfect fit for poison only after I came up with the idea of a set that glimpsed the future.

In order to fit it into the set though, I had to find a way to evolve poison. To demonstrate it was from the future, it had to do something it had never done before. The obvious answer was that when we brought poison back we would keyword it. Poisonous came about because it seemed like the most straightforward way to do it. I liked the number because it allowed us to make sure that the poison to power ratio was high enough that the creatures with poisonous killed with poison before killing with damage.

Those of you that are familiar with *Future Sight* know these two cards:

<table>&#10;	<tbody>&#10;		<tr>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Snake Cult Initiation" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Snake+Cult+Initiation"></div>&#10;			</div>&#10;			</td>&#10;			<td>&#10;			<div>&#10;			<div><img alt="Virulent Sliver" src="http://gatherer.wizards.com/Handlers/Image.ashx?type=card&amp;name=Virulent+Sliver"></div>&#10;			</div>&#10;			</td>&#10;		</tr>&#10;	</tbody>&#10;</table>

What you might not know (or know if you read Aaron Forsythe's [articles](https://web.archive.org/web/20140110115401/http://www.wizards.com/magic/magazine/archive.aspx?author=aaron%20forsythe)) is that I put a third poison card in the design:

> **Poisoned City**  
>  Land  
>  T, Receive a poison counter: Add W or U to your mana pool.

This card was killed at the time in development for being too strong in a vacuum. I tried putting the cycle in *Scars* but development made it clear to me that the full cycle wasn't going to fare any better. In any environment where poison wasn't dominant, these cards were almost as good as *Alpha* dual lands and that was better than development feels dual lands are supposed to be.

R&D felt poison was a good fit for *Future Sight* and after ten years poison reappeared in the game. While I was happy to see poison back (and even happier to see poison win an actual [Pro Tour](/en/articles/theweekthatwas/2007/07-06-rise-of-the-sliver-surfers)), my goal wasn't just to have a few cards. No, I wanted a set where poison was a major player. To do that though I needed not just a set where poison could work, I needed a set that *had* to have poison.

### The Quest for Poison, Step #6—Make a Set That Had To Have Poison

Last week I talked about how when *Mirrodin* was designed we knew then and there that Mirrodin was already under attack from the Phyrexians. The key to this attack was that it was slow and subtle. The Phyrexians (or maybe more accurately the Phyrexian force, or whatever you want to call the essence that drives the oil) planned to take over Mirrodin much as they take over any world by slowly turning it into them.

![](https://i.ormos.uk/73/7d/737dfb5192a51d7ac1b1799202e9d7bf6848f15ea36f9a59d9c778194131a451.jpg)

You see, that's the creepiness of the Phyrexians. They win by turning you into them. Every creature they bring to their side is one less creature you have on yours. (This is why infect is such a perfect name for a Phyrexian mechanic.) In fact, in *Scars of Mirrodin*, the Mirrans—that's what the inhabitants of Mirrodin are called by the way—aren't even aware yet of the Phyrexian's existence. If the name *Mirrodin Besieged* didn't give it away, they figure it out. In *Mirrodin* we saw the beginning of this conversion by the Phyrexians. *Scars of Mirrodin* brings us back where we can see they've slowly been advancing.

Returning to *Mirrodin* meant that we got to finally meet the Phyrexians, not just creatively but mechanically as well. So, returning to Mirrodin meant we finally got to put a mechanical face on the Phyrexians, an unstoppable toxic force that slowly corrupts everything it touches. How could we possibly mechanically represent such an evil, toxic, corrupting force? If only such a mechanic existed ...

I finally had my set that had to have poison. The only thing in my way was an R&D belief that poison didn't have a place in the game. And the opinion by some developers that we'd have problems making it matter without breaking it. Plus there was the small issue that the mechanic had a few kinks that we'd never been able to work out. In addition, my track record with the mechanic didn't exactly inspire confidence.

On the other side, I'm *really* stubborn.

Join me next week when we pick up at week one of *Scars of Mirrodin* design.

Until then ...

Oh wait. I promised you a mythic creature with infect.

Here's a little teaser about how this whole poison thing plays out.

![](https://i.ormos.uk/a4/49/a449cc12e7665bc671c54a0c047c3d9e525e4d18b62736788332a9e6aa6456d2.jpg)  
  
  

Now is that a card worthy of "Legendary Creature – Dragon Skeleton" or what?

Join me next week when I explain how things like that made it to print.

Until then, may you be a little stubborn when you need to be.
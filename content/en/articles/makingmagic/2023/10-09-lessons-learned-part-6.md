---
id: y4attpbt
kind: article
lang: en
path: /en/articles/makingmagic/2023/10-09-lessons-learned-part-6
title: Lessons Learned, Part 6
published: '2023-10-09'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-6
    lang_detected: en
    capture_id: 222569
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-6
    captured_at: '2024-06-22 18:50:44+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-6
    lang_detected: en
    capture_id: 222569
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-6
    captured_at: '2024-06-22 18:50:44+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-6
    lang_detected: en
    capture_id: 222569
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-6
    captured_at: '2024-06-22 18:50:44+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-6
    lang_detected: en
    capture_id: 222569
    url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-6
    captured_at: '2024-06-22 18:50:44+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: y4attpbt
  url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-6
  page_key: magic.wizards.com/en/news/making-magic/lessons-learned-part-6
  lang: en
  template: contentful
  captured_at: '2024-06-22 18:50:44+00'
  capture_id: 222569
  wayback_url: https://web.archive.org/web/20240622185044id_/https://magic.wizards.com/en/news/making-magic/lessons-learned-part-6
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: y4attpbt
  capture_id: 222569
  url: https://magic.wizards.com/en/news/making-magic/lessons-learned-part-6
  wayback_url: https://web.archive.org/web/20240622185044id_/https://magic.wizards.com/en/news/making-magic/lessons-learned-part-6
  captured_at: '2024-06-22 18:50:44+00'
  template: contentful
  sha256: 269faa4f5f21625c2c4c0b79d635280ce356dfd73f418cfa108625d181504027
render_recovery:
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/ab2d0fff/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/4e409c05/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/860e1fd1/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/e387d042/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
- code: unsupported_link
  element: a
  target: mailto:making.magic@hotmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - email
  occurrences: 1
- code: unsupported_embedded_media
  element: iframe
  target: https://share.transistor.fm/e/magic-the-gathering-drive-to-work-podcast/playlist/dark
  reason: The preview omitted the iframe that loads this separate page.
  occurrences: 1
---
At the end of each *Making Magic* article, I post the latest episodes of my *Drive to Work* podcast. I have a recurring series on my podcast called "Lessons Learned" where I go through every set for which I led or co-led the design and talk about what I learned from the experience. This year, I started writing articles for each lesson, complete with links to podcasts for readers hoping to learn more. Here are my five previous "Lessons Learned" articles:

*   [Part 1](/en/articles/makingmagic/2023/03-14-lessons-learned-part-1)
*   [Part 2](/en/articles/makingmagic/2023/03-20-lessons-learned-part-2)
*   [Part 3](/en/articles/makingmagic/2023/05-22-lessons-learned-part-3)
*   [Part 4](/en/articles/makingmagic/2023/06-19-lessons-learned-part-4)
*   [Part 5](/en/articles/makingmagic/2023/08-07-lessons-learned-part-5)

Last time, I got through *War of the Spark*. Up next is *Throne of Eldraine*.

## *Throne of Eldraine*

**Lesson: "Sometimes an idea needs an appropriate companion idea."**

From time to time, I lead a design and learn something important that I didn't know. While I had done a lot of individual top-down card designs, *Innistrad* was the first full top-down set where I led the design. And it wasn't just any type of top-down set; it was one based on a genre (gothic horror). I had known the importance of resonance (it's a frequent theme in *Making Magic*), but I hadn't quite realized how potent it was to tap into story elements that players already knew. There's an existing emotional bond players have formed with certain types of stories and story elements that's very powerful and leads to designs that are clearly and instantly understandable.

The moment I finished the *Innistrad* design, I was eager to find another genre to build a set around. At the time, I was interested in finding something fantasy adjacent. Over the years, we've experimented with genre themes further away from the core of the game, but this was early in our genre exploration. I made a list of potential options, and at the top of my list was fairy tales. Fairy tales had two huge advantages. One, they basically took place in a fantasy setting. They require kingdoms with royalty and witches and faeries and dragons and magical spells. Two, fantasy is a universally known genre. Part of that stems from its prevalence in children's entertainment, but the stories themselves have become archetypal to the point that they show up all the time in popular culture. For example, I learned that the average American in their lifespan will have seen ten different movies with the plot of Cinderella. I was convinced fairy tales were the perfect concept to build a plane around.

From time to time, we will have a meeting where we let anyone in R&D pitch an idea for a new setting. I put together a slide show full of images, pulled from pop culture, that demonstrated both the depth and the familiarity of the genre space. The result was a resounding thud. The concern: it was too juvenile. I stressed that while the genre is associated with children's entertainment, the source material was much darker. Many entertainment properties have played in the more serious space of the fairy-tale genre. The Powers That Be passed.

I tried again several times but was unable to drum up much excitement. Some years later, we were doing another such meeting and Shawn Main pitched the idea for an Arthurian-inspired set. It generated a lot of excitement and was added to the schedule. I noticed that an Arthurian-inspired set wasn't quite as recognizable from a resonance standpoint and hit on themes that *Magic* had done many times, meaning it wouldn't feel particularly novel. Seeing an opportunity, I went to Aaron Forsythe, my boss, and suggested that we supplement the Arthurian set with fairy tales. I argued that Arthurian lore was, in many ways, a collection of fairy tales from England and that Central Europe created many other well-known fairy tales. Aaron signed off, and *Throne of Eldraine* became the set that finally tapped into the fairy-tale genre.

The important takeaway: understanding why I was successful at amending plans for an Arthurian set when I couldn't sell a fairy-tale set on its own. The answer: my idea wasn't grounded enough. I pitched something that, at the time, was a little too far from where R&D saw the game. *Magic* is a collaborative effort. I can't make a set that no one else can visualize.

Part of my job includes understanding the larger context of designs. Fairy tales, due to how they've been popularized, come with certain baggage. The key to making a set with fairy tales is to package them with other elements to offset that perception. Arthurian lore hasn't been juvenilized as much in popular media, so it has a different impression. It complemented fairy tales well because it fit with the aesthetic and shifted the overall tone. Now when trying to sell an idea that doesn't go over well, I won't just keep pitching it but will combine it with a companion element to shift how people see it. The problem wasn't that other people couldn't see my good idea but that I wasn't selling my idea in a way that made them see its potential. A lot of design is salesmanship, and *Throne of Eldraine* taught me an important lesson in how to be a better salesman.

## *Ikoria: Lair of the Behemoths*

**Lesson: "You have to set up the teams after you for success."**

The slot *Ikoria: Lair of the Behemoths* appeared in was originally going to be *Theros Beyond Death*, which was a set later because the original trip to Eldraine was planned for two sets (one set in the courts, and one set in the woods). When the vacancy opened, we ended up pulling forward an idea we had scheduled for years in future, something we originally called "Monster Island."

The main vision for the set was the focus on giant, evolving monsters rather as opposed to the Halloween-type monsters we use in Innistrad sets. The design looked at pop culture to map out the different kinds of monster tropes that we could fill a set with. Mutation, where monsters start small and grow into giant abominations, and bonding, where one or more humanoid individuals connect emotionally with a monster, were two big tropes of the set. These ideas were important enough that each got a mechanic dedicated to it.

The goal of mutate from the start was making a mechanic that lets players "build their own monster." The mechanic was inspired by the champion mechanic from *Lorwyn*. Champion hadn't really been a big success with the players, but we felt the idea of evolution and mutation was quite popular and wanted to use Ikoria as a place to better bring the idea to life mechanically. Mutate started a bit narrower, tying into specific creature types, but broadened as we found the mechanic to be more fun if the players had more flexibility with it. As it became more open-ended, it grew in complexity.

Companion was a mechanic we'd come up with in a hackathon. It tapped into some of the fun of the Commander format where you have a creature that you're more likely to play every game. The concept worked well with the idea of bonding, so we added it to the set. Companion was playing in a dangerous space as the variance of the deck is a huge part of what makes *Magic* work. We'd tried similar things in the past always to abandon them because of play-balance issues. This time, though, we thought we could make it work.

The big lesson of *Ikoria* isn't that we did mutate or companion, but that we did both. The whole point of vision design is to work out the basic vision and structure of the set, enabling the teams downstream to focus their energy on making it the best that it can be. An important part of this, though, is that we have to be careful that what we hand off can be reasonably accomplished by the teams downstream of us. *Ikoria*'s design stumbled because vision design handed off too much. Both mutate and companion are what we now refer to as a "high maintenance" component, meaning it's something that's going to take extra time and care to properly execute and balance. A vision design should only have one high-maintenance component. *Ikoria* even led us to start a new process, what we now call Vision Design Summits (it's evolved a bit), where people downstream look at vision designs, partly to make sure that we're not biting off more than the Set and Play Design teams can chew. It's not every design that creates a new part of the process, so this lesson was a bigger one than most.

## *Zendikar Rising*

**Lesson: "Think beyond the set."**

The first *Zendikar* premiered in 2009. It was an adventure plane with a strong mechanical tie to lands. The original plan for the "year" was to make the last set a large set that occurred on a different plane. The Creative team wasn't set up, at the time, to create two planes in one year, so they came up with a backup plan. There would be an event on Zendikar so large in scope that it would justify a complete mechanical reset. This event would involve the Eldrazi escaping their capture and causing havoc on the plane.

The *Zendikar* block was popular enough that we would return to Zendikar in 2015. Feeling obligated to finish the story we started in *Rise of the Eldrazi*, the second visit to Zendikar would revolve around the natives of the plane fighting the Eldrazi and the formation of the Gatewatch, a collection of Planeswalkers who would help free Zendikar. The *Battle for Zendikar* block was a big departure mechanically, more focused on the battle with the Eldrazi than the adventure-world theme of *Zendikar* and *Worldwake*, and less popular.

For the third visit, I was interested in recapturing what made players fall in love with *Zendikar* in the first place. Part of that involved re-exploring the land theme, but another part was recapturing the feel of an adventure plane. I do want to note before I continue my story that while we had talked about a *Dungeons & Dragons*–themed *Magic* expansion for years, it wasn't yet a thing when *Zendikar Rising* was in vision design. That is why when we started exploring adventure themes that we ended up looking at the concept of the adventure party.

For those not familiar with *Dungeons & Dragons* (D&D), you roleplay characters with different skills and abilities. Quite often, the campaign is built around an adventure, usually with some larger mission, but sometimes you're just adventuring for adventure's sake. Because D&D is a social game, you want to play with other people, and the concept of the adventure party explains why you all work together within the story of the game. There are plenty of stories involving an adventure party (things such as *The Lord of the Rings*), but my biggest influence when thinking about adventure parties was D&D.

In D&D, you often want to diversify the types of characters in your adventure party. Different classes come with different skills and have access to different tools and weapons. In early D&D, when I first played, there were four basic classes: fighter, wizard, rogue, and cleric. Three of those four were creature types in *Magic*. This inspired the idea of a party mechanic where you wanted to get one of each. We ended up swapping in Warrior for fighter, as that was the closest equivalence in a commonly used creature type.

I was most excited by the idea that party cared about creature types in a different way than *Magic* normally did. Usually, typal themes are about playing a lot of the same creature type. Party wanted the player to diversify. The mechanic seemed very flavorful and pushed in new mechanical direction. I was all aboard with using it.

My big lesson from *Zendikar Rising* is understanding that mechanics must live outside conceptual space. It's very easy to build something inside the biosphere of your set environment and forget that *Magic* mechanics have to interact with everything around it. Party is a perfect example of this issue. For starters, it requires a certain mix of creature types. At the time, I thought we were okay because we were using class creature types that show up in most sets. It turns out that we have to be a bit more forward-thinking than that. We can't just have random cards with the creature type. We need to have cards that specifically slot into the decks that the future set is going to make. The fact that these four creature types were more influenced by flavor than mechanics made this trickier than you might assume.

The other big problem is that the mechanic fought the general nature of Constructed formats. I play creatures as threats. My opponent removes the threats. There's back-and-forth. Party doesn't ask the player to get one creature on the board, it asks for four, each of a different creature type. That's just a big ask, bigger than Play Design could easily address. Yes, we made designs where you didn't have to get to four to have them be worth playing, but the mere structure of the format was asking a lot of a player, too much to do consistently, which is key to making viable Constructed designs.

Much like the lessons of *Ikoria*, the lessons of *Zendikar Rising* have changed how we do vision design. There are more check-ins with Play Design to make sure that the mechanics we're making can be properly balanced and designed for Constructed formats.

## *Strixhaven: School of Mages*

**Lesson: "There is variance in familiarity."**

*Strixhaven: School of Mages* came about because we realized several different themes that we were interested in doing could all work in the same set. We wanted to do a top-down set based on the magical school trope. We wanted to do an enemy-color faction set that was structured differently than Ravnica (historically, we've done significantly less enemy-focused sets than ally). We wanted to do an "instants and sorceries matter" set. We wanted to do modal double-faced cards. It was the realization that all of these would synergistically work in the same set that got us to put it on the schedule.

Interestingly, my big lesson on this set had to do with none of those themes. Well, maybe a little bit with the first one. Over the years, I've become a big advocate of every set having resonance (see above). To excite players, you need to tap into something that the players already have emotional connections with. We can do our own spin on it, but it's helpful for design to have pockets of resonance to work with.

The earliest themes we worked with were cultural, historical, and/or mythological. The very first top-down set was *Arabian Nights*. The first top-down block was *Champions of Kamigawa*. These sets took real-world inspirations and built cards based on them. We then began exploring genre space. Like Innistrad being a gothic-horror plane and Eldraine being an Arthurian/fairy-tale plane. It let us tap into popular culture and trope space that the audience was familiar with.

*Strixhaven* started as a top-down genre set. Magical school, as a theme, has appeared in movies, TV shows, books, etc. But as we were designing it, we realized we had stumbled on a brand-new type of resonance, what I'll call "real-world resonance." Yes, players were familiar with the magical school genre, but more so than that, they were familiar with school. Most players have attended a school at some point. This meant that we could make designs that played into that knowledge. In fact, we leaned our factioning heavily into this. We built our colleges around subjects. Quandrix was about math. Lorehold was about history. These are universal things that (almost) everyone could relate to.

Each type of resonance has its issues. Cultural resonance can be limiting in that not everyone is as familiar with the source material as others. For example, when working on *Amonkhet*, we did an exercise where we went around the company asking what knowledge people had about Egyptian mythology and learned it was far lower than we thought.

Genre resonance is a bit more universally known. Many hit movies and, to a lesser extent, TV shows are popular around the world. Genre resonance's biggest issue is that many entrenched tropes can have a troublesome history, so you must be conscious of how you use it.

Real-world resonance has a different issue. Because it's tied to everyday life, there's just a lot more variance. For example, we chose to make *Strixhaven* a magical university (a lot of stories in the genre occur in high school or earlier). We designed many cards based on our own personal college experiences. What we learned is that much of what we did in school wasn't as resonant for many players. They experienced going to school differently. The way schools work varies greatly from country to country. Some things did work. The concept of biology, for example, is much more universal than what a college dorm is like. *Strixhaven* opened my eyes to this new swath of resonance but also taught me the inherent danger of tying something too close to my own personal experience.

## Proper Education

That's all the time I have for today. I hope you enjoyed this insight into some of the things I learned while designing specific sets. If you enjoyed today's column, I heartily recommend you listen to my podcast. I go much more in depth in my 30-minute episodes. If you have any thoughts on today's column, any of my lessons, or on any of the sets I talked about, you can email me or contact me through any of my social media accounts ([Twitter](https://twitter.com/maro254), [Tumblr](https://markrosewater.tumblr.com/), [Instagram](https://www.instagram.com/mtgmaro/), and [TikTok](https://www.tiktok.com/@markrosewater)). I plan to do a seventh installment of this column, but not until after I've recorded my "Lessons Learned" podcasts for the next batch, which probably won't be for at least a few months.

Join me next week for a look at something new.

Until then, may life provide you with as many lessons as it provides me.
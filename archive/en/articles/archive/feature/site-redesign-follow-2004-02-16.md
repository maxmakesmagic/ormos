
---
[Link to Wayback Machine](https://web.archive.org/web/20201025135736/https://magic.wizards.com/en/articles/archive/feature/site-redesign-follow-2004-02-16)

[_metadata_:wayback_url]:- "https://magic.wizards.com/en/articles/archive/feature/site-redesign-follow-2004-02-16"
[_metadata_:wayback_raw_url]:- "https://web.archive.org/web/20201025135736id_/https://magic.wizards.com/en/articles/archive/feature/site-redesign-follow-2004-02-16"
[_metadata_:wayback_capture_timestamp]:- "2020-10-25 13:57:36+00:00"
[_metadata_:description]:- "I'd like to start off by congratulating the magicthegathering.com writers for a great first week of content. I'm a voracious Magic content devourer myself; I'm as happy as anyone that we've doubled the number of weekday columns (and that Ask Wizards, Magic Arcana and Card of the Day are smoothly back to daily updates again, thanks to the organizational powers of one Mr. Scott Johns). I'm proud to work for such a strong source for Magic information. So, like, go us."
[_metadata_:generator]:- "Drupal 7 (http://drupal.org)"
---


Site Redesign Follow-Up
=======================



 Posted in **Feature**
 on February 16, 2004 






![](https://media.magic.wizards.com/styles/auth_small/public/generic-avatar-150_298.png)
By Doug Beyer, Magic Web Developer











I'd like to start off by congratulating the **magicthegathering.com** writers for a great first week of content. I'm a voracious **Magic** content devourer myself; I'm as happy as anyone that we've doubled the number of weekday columns (and that Ask Wizards, Magic Arcana and Card of the Day are smoothly back to daily updates again, thanks to the organizational powers of one Mr. Scott Johns). I'm proud to work for such a strong source for Magic information. So, like, go us.

I'm back in the hot seat this week to follow up on my article [last week](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/196) on the changes to **magicthegathering.com**. (Don't worry, I'm not a Monday regular. After today, this is it for web-developer-guy-writes-**Magic**-columns for a long while: some guy named MIKE is on tap for next Monday.) If you're bored with talk of the redesign of the site, then great, we're done here: go [write Mark some email](/en/articles/archive/making-magic/talk-me-2004-02-16) or something. If you've followed the [thread](http://boards1.wizards.com/showthread.php?s=&threadid=177962) from last week's article and are curious what we've been thinking and doing for the last seven days (which is a long time on the Web), read on. 

### Changes we've made since last week

Let me start by listing briefly the changes that have been made since the launch of the redesign last week. Warning: this list is semi-technical, and may only be interesting for the web-savvy reader.

* **Browser compatibility:** A small error in the way a spacer image was aligned made the article boxes contain areas of unintended space on several browsers. This was fixed.
* **Height of article images:** The size of the main articles' splashy title images combined with the length of introductory text made the top article boxes too tall, pushing the second row of boxes as well Ask Wizards below the fold. The images have scaled down (and no longer simply repeat the headline of the article, which is right there anyway).
* **Length of introductory blurb:** Last week, the day's two articles had a short paragraph of what we call "teaser text" -- a few sentences stolen from the article. But again that was contributing to a long top box full of tiny text. This week, we're focusing on information: instead of lines from the article, it's a hand-written, to-the-point summary of what you'll find in the article. Is this article relevant to you? Is it something you'll want to read? This week and from now on, you'll know.
* **Page load time:** Our friends in the dialup world (and there are a lot of you) noted that the page was pushing 800K, when you factor in the HTML, Javascript includes, and images. Yeah, that's kind of heavy, even for Wizards (we are a visual people; we love graphically involved pages). Several changes throughout the front page have cut that down to a svelte 350K or so: still not great but at least tolerable without cutting into its graphical emphasis.
* **Magic Arcana graphic:** The older graphic was very tall and possibly over-ornate. I personally liked it, but it has been redesigned to save page real estate. It now also focuses more on the "payoff": the part of the graphic where you can see through the "window" in the center is larger.
* **Tournaments box and This Week box:** The second row (the "green row") of article boxes, the boxes that hold tournament information and the weekly feature article, have been redesigned to reduce clutter and further improve the height of the page. Now the graphics are left-aligned and more vertically oriented to break up the look of all the horizontal title images. Also the tournaments box provides more headlines and less blurb, and the weekly feature article doesn't have the introductory blurb at all anymore (after all, you've got a week to click on it, so the blurb probably isn't necessary to get you to go read it in a hurry).
* **[Article Section](/en/articles/archive/magicthegatheringcom-archives-2004-01-13):** To help with the weight of this page, the individual article images have been replaced. Expect to see a more helpful design of this page in the coming week.
* **[Tournament Center](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/tournamentcenter):** We tightened up the graphics, added the DCI Announcements section, and added more Resources for Tournament Players, creating an even more eyeball-friendly and useful Tournament Center.

### Things we intentionally didn't change

Of course, the whole design didn't get rearranged due to reader comments: some things stayed the same. Here's some discussion of the motivations behind some of the non-changes.

**Page width:** Magicthegathering.com is 750 pixels wide, like every page on the Wizards of the Coast website. This does cause a lot of readers with high resolution monitors to see a lot of whitespace on the right side, and to have to scroll down to see all the content available -- believe me, I sympathize. But our page width is a decision rooted in the demographics of our readers; based on our site statistics, we simply have too many readers who browse at 800x600 to move away from this design. (There is the issue of consistency with other Wizards.com sites as well -- we don't want going from **magicthegathering.com** to **[wizards.com/dnd](/en/articles/archive/event-coverage/2006-champs-limited-2006-06-27-15)** to be a shock or a pain -- but mostly it's about the demographics.) Don't worry: as more and more of our readers shift to using 1024x768 and higher resolutions, magicthegathering.com (as well as the rest of Wizards.com) will shift too. Now just wasn't the right time.

**The overall "clean lines" look:** We know a lot of you enjoyed the old site's look and feel, with graphical elements emphasizing **Magic**'s fantasy themes. But like **Magic** itself, the web site undergoes swings of the Big Design Pendulum from time to time, in accordance with shifts in priorities and goals. Since our current mission, our number one goal right now, is to combine the content from multiple sites into one, the site's Big Design Pendulum is swinging toward the clean-lines look of an Internet news site. We wanted to de-emphasize the ornate graphical elements of the previous revision, to replace it with simple boxes to make sure that the new organization of the site, and the individual merits of each article, showed through. That said, we're interested in keeping the right-hand column of the front page more graphical than news-y, so that area will de-emphasize the boxes.

**Lack of a main navigation menu:** The old site had a navigation menu in the left column. Navigation menus are, in general, good, if you can't get to everything you need to find on the page itself, and if they are not taking up space unnecessarily. The reason that there is no main navigation now is that we endeavored to put just about everything a player would need into the page itself: cardlists, new products, rules, tournament information, ***Magic** Online* status, wallpapers. We know via our site statistics that these are the most often-requested **Magic** resources on our site, so they're all there. There are some pages that you can't get to in one click anymore -- the old nav had the ability to traverse multiple menus to select, say, the [World Championship Decks from 2003](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magic/expansion/worldchampionshipdecks2003) directly. But you can still find all those on the [page of all **Magic** products](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magic/products/cardsets) which is linked right there in the Products box. And besides, we've found that a large number of users preferred doing a search using the search box than try to navigate those menus anyway. So that's why that's gone. On any article, like this one, the left nav is a simple list of a few main areas, including a link to get you back to the [front page](/en/events/coverage/pro-tour%E2%80%93amsterdam-standard-qualifier-season-top-8-decklists) where all the action is.

### Thanks, and how to reach me

Before we move on to what I consider the good stuff - the future stuff - I'd like to take a moment to thank everyone who posted on last week's boards thread. It really helped us get a sense of the effect of the redesign on your eyeballs and brains. Although there's no way to please everyone, I got the gratifying sense that our direct communication with you, through our boards, led to a better site and an overall-happier you. That's why I've set up a direct (and for me, happily, spam-free) way for you to communicate with me, personally, about further page design issues.

**How to contact a real live Magic web developer about magicthegathering.com page design issues:** Go to [this form](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=company/feedbackform). Select **Magic: The Gathering** and hit Continue. Select "Comment or question about magicthegathering.com page design" and hit Continue. Enter your note and your email, fire it off, and it will get to me. Simple as that. Don't expect a response for every piece of feedback you send, but I will read and, together with the rest of the **Magic** web team, consider your response for implementation on the site. Consider that our commitment to your thoughts and suggestions: after all, it's you we're trying to serve here. (Non-website-design questions, the ones to be answered by Rune Horvik or by R&D, should still go to [this form](http://archive.wizards.com/Magic/Magazine/Article.aspx?x=company/feedbackform), but you should select "Game rules question for Saturday School" or "Submit question to Ask Wizards" instead.) Enjoy.

### New features to come

THAT SAID -- let's move on to what things are already on their way to **magicthegathering.com**. I'm going to keep this short so that you can get back to reading real **Magic** articles, but I thought it was important enough that I wanted to include it while I still have your attention.

**Magic card database:** The biggest news is that, if all goes according to plan, **magicthegathering.com** will be unveiling a **Magic** card database this year. I'd like to be able to tell you precisely when, but I just don't know. Before autumn, let's say, but after, like, now. But I think you'll like it. It will do lots of things. It will show you all the pretty cards. It will be on its own server so that y'all don't crash Wizards.com. :-) More on that later.

**Other stuff:** What other goodies can you expect to see? Here's sort of a laundry list. For Orb fans: expect the Orb of Insight to return this year... For ***Magic** Online* players: expect to see improvements to the design of the ***Magic** Online* site... For "autocard" fans: expect more functionality to enhance your reading of articles... For new players: expect a cool new area to experience the basics of **Magic: The Gathering**.

Thanks again for your support through our redesign. Now I have to go get my house prepared for my *Darksteel* release party: [Forsythe likes his Altoids](/en/articles/archive/latest-developments/life-and-times-autospell-2004-02-13-0), I hear.








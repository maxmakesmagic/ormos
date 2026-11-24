---
id: 175gn5qv
kind: article
lang: en
path: /en/articles/latestdevelopments/2015/08-21-developing-for-story
title: Developing for Story
published: '2015-08-21'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
    lang_detected: en
    capture_id: 721035
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
    captured_at: '2016-05-01 14:27:58+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
    lang_detected: en
    capture_id: 721035
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
    captured_at: '2016-05-01 14:27:58+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
    lang_detected: en
    capture_id: 721035
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
    captured_at: '2016-05-01 14:27:58+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
    lang_detected: en
    capture_id: 721035
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
    captured_at: '2016-05-01 14:27:58+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: 175gn5qv
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
  lang: en
  template: drupal
  captured_at: '2016-05-01 14:27:58+00'
  capture_id: 721035
  wayback_url: https://web.archive.org/web/20160501142758id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 175gn5qv
  capture_id: 721035
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
  wayback_url: https://web.archive.org/web/20160501142758id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-story-2015-08-21
  captured_at: '2016-05-01 14:27:58+00'
  template: drupal
  sha256: 4b3b0b1110f1ae970886aff09a85538146fed15af52b6e7bf49c2f540c771236
render_recovery: []
---
It's easy to think of development as just the group that tweaks numbers, but a lot of what we do is take the vision and promises that the design team is trying to give to the players and execute on those ideas. While we do tweak most of the numbers, we also do a lot of redesigning of cards so that when we get a set like *Khans* that wants to play up the wedges, we can make sure that those themes pop—not only by making the wedge cards appropriately strong, but also by starving both Limited and Standard of the kinds of things that would easily prey on those strategies.

Creative has created a world and a number of characters they want to show off, and it is up to development to make sure those things can shine. A huge part of *Dragons of Tarkir* was making sure that all the work that creative was putting into the Dragonlords and in their character design, story, and art was maximized by making the cards the kinds of things that players would be excited by at all levels of the game. The fact that a good majority of the khans and Dragonlords have seen Top 8 performances at major tournaments is, I think, a good example of how design, development, and creative working together went a long way toward making the set feel different and highlighting the best parts of the *Magic* storyline.

Because legendaries and planeswalkers have art that shows off the character as more than just their exact power, toughness, and abilities, they allow the most flexibility for late design changes and usually aren't the most important part of the design handoff to development. Design does what it can to try and show who the characters are and come up with new and unique suites of abilities, but it is on development to make sure that the gameplay of these cards lives up to their promise.

![](http://media.wizards.com/2015/images/daily/cardart_DTK_Dragonlord-Atarka.jpg)

[Dragonlord Atarka](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dragonlord+Atarka) | Art by [Karl Kopinski](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Karl+Kopinski%22%5d)

# Living up to Legends

*Legends* was a pretty amazing set, in that it introduced two new concepts to *Magic*—gold cards and legends—but managed to use almost none of the design space in them. Part of the problem with *Legends* was that, at the time, the power level of creatures was abysmally low. The set itself strove to include some cards that had huge stats, but most of them were not very playable. It didn't say much for the (then) creature type of Legend when these were the kinds of things you were seeing:

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lady+Orca)](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lady+Orca)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gosta+Dirk)](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gosta+Dirk)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Riven+Turnbull)](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riven+Turnbull)

These cards are intended to be famous and powerful characters from across the Multiverse, but they are actually very weak cards and have abilities that don't make sense. When you look at [Riven Turnbull](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Riven+Turnbull) as a package, what is that saying to you? Why would you ever care about that character? Why couldn't this have been on a random orc or demon? Ideally, legendaries are supposed to evoke something, and his card just doesn't.

Now, that isn't totally fair. There were some cards in *Legends* that were interesting, such as [Sol'kanar the Swamp King](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sol%27kanar+the+Swamp+King), [Hazezon Tamar](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hazezon+Tamar), and [Nicol Bolas](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nicol+Bolas), but the batch as a whole leaves a lot to be desired. Part of the problem is density. I think if *Legends* had fewer legendaries, but each one was exciting, then the set as a whole might be remembered more for them than for [Mana Drain](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mana+Drain) and [Moat](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Moat).

When *Magic* wanted to try and move story more into the forefront, we began with the multi-year arc of the *Weatherlight* Saga and had some pretty good legendary successes with [Squee](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=370461), [Ertai](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=5146), and [Hanna](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=25977). At the same time, we failed the most egregiously with the main character, [Gerrard Capashen](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gerrard+Capashen)—a creature who should have lived up to his epic status, but instead was relegated to junk binders forever. And this is the challenge of making a legendary. We have found that time and time again, players have a very hard time separating characters from the cards. It turns out that a powerful and fun legendary will help player really care about the character, while giving them a boring and weak card turns them away. We hope to do better justice to [Gerrard Capashen](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gerrard+Capashen)s and [Emmara Tandris](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=368944)es in the future.

![](http://media.wizards.com/2015/images/daily/cardart_JUDGE_Hanna-Ships-Navigator.jpg)

[Hanna, Ship's Navigator](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hanna%2C+Ship%27s+Navigator) | Art by [Terese Nielsen](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Terese+Nielsen%22%5d)

This isn't to say that every legendary needs to be a top-tier Constructed card, but they should be something that people can love. The card should also be something that encompasses who the character is, so that the thing people fall in love with is something that actually fits who the character is. Looking at *Magic Origins*, [Hixus, Prison Warden](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hixus%2C+Prison+Warden) is not something that will be dominating Standard in the near future (at least I don't think so), but his card is fun and interesting. What's more, it really encapsulates a top-down jailer, who punishes creatures that deal damage to you and keeps them locked away for as long as he remains. I think that card goes a long way toward establishing who he is as a character, and gives players something to latch on to when thinking about him—even if they haven't [read the Uncharted Realms](/en/articles/feature/2015/07-01-gideons-origin-kytheon-iora-of-akros).

That is what this is about. While we definitely want to reward players who want to get more into the lore and to read Uncharted Realms or otherwise dig into what we are trying to offer, we know that not everyone will do that. Many players choose to interact with our storyline only through the cards, and it's up to R&D to make sure that those players are getting a satisfying experience. We also do this so that, if they later decide to explore the lore, they aren't surprised by how different their favorite legendaries are in the cards versus in the story. We want them to line up in a satisfying way.

I guarantee you that if we had released [Gerrard Capashen](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gerrard+Capashen) as a vanilla one-mana white 2/2 legendary creature, he would have seen much more tournament play and been a much stronger card—but that would've undercut his character. It wouldn't have told you anything about him, and even though he may have actually seen play, I think that people would've had a worse understanding of the character than they do now.

 

# Capturing the Moments that Matter

As we move into a new era of storytelling in *Magic*, we want to show not just the characters on our cards, but also the moments that matter. We'd like players who look through a set to get an idea of what the storyline is, and at least catch the big takeaways. One of the funny stories I heard about when I started at Wizards was that Mike Turian was surprised to learn *Invasion* was about an invasion. He wasn't someone who was invested in the story, and the images of Dominarians fighting Phyrexians didn't mean anything to him. I think that if in *Battle for Zendikar* we don't let even the least story-interested players know that there is a battle being fought for Zendikar between the Zendikari and the Eldrazi, then we have failed. I think if we don't let them know what our Planeswalkers are doing on the plane, we have also failed. And that's where capturing the pivotal moments in card form is important.

![](http://media.wizards.com/2015/images/daily/cardart_EX_Mind-Over_Matter.jpg)

[Mind Over Matter](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Over+Matter) | Art by [Keith Parkinson](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Keith+Parkinson%22%5d)

In my mind, one of the most successful cards to do this in the pre-Modern era was [Mind Over Matter](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mind+Over+Matter). For players who were invested in the story up to that point, it had huge payoffs, not only showing the *Weatherlight* escaping Rath, but also revealing that Urza was still alive and was at the center of all of these events. It was a real mic-drop kind of card, at least for me. What's also important is that it was a unique and powerful card that saw tournament play, even if it was in an all-too-powerful deck that won on turn one or two and forced bans.

*Magic Origins* acts as a kind of preview of this model, with the important moments of each character's story played out on the cards. Because we needed to fit five of these stories into the set, not everything is given as much importance as the pivotal events will be in the future. In *Magic Origins*, we wanted to make sure that the important part of each character's story was depicted somewhere on a card, so that players who were less engaged would at least get a sense of the progression. And if they chose to read Uncharted Realms or play through one of the *Magic Duels* campaigns, they would find things that reinforce the cards rather than contradict them. As an example of the kind of progression seen in *Magic Origins*, take a look at a few of Nissa's cards.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nissa%27s+Pilgrimage)](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%27s+Pilgrimage)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Nissa%27s+Revelation)](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%27s+Revelation)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gather+the+Pack)](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gather+the+Pack)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Eyeblight+Massacre)](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Eyeblight+Massacre)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=The+Great+Aurora)](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Great+Aurora)

One of the challenges of a card set versus a traditional method of storytelling is that players can see the cards in any order. It's hard for us to make sure that players know that [Nissa's Revelation](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Nissa%27s+Revelation) was the moment she got her spark. That she travelled to Llorwyn afterwards, met up with Dwynen, saw an Eyeblight hunt, became horrified, and then left as [The Great Aurora](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Great+Aurora) began to change the plane. What we can do is make the cards showing off these moments individually succeed at melding story moments to mechanics, and try to leave players wanting to do more. At the same time, a player who started with the story would be very excited to see these cards upon opening up the set, because the actions they saw or read about were portrayed in a clear and accurate way.

![](http://media.wizards.com/2015/images/daily/cardart_ORI_The-Great-Aurora.jpg)

[The Great Aurora](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=The+Great+Aurora) | Art by [Sam Burly](https://web.archive.org/web/20150821000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=visual&action=advanced&artist=+%5b%22Sam+Burley%22%5d)

As we move forward in the new era of *Magic*, there has been a lot more work between story, art, design, and development to get these things right. Having seen what that means for *Battle for Zendikar* and beyond, I am very excited, and I think we are doing a good job of executing on what we are promising you: a stronger and more integrated story in *Magic*. I hope you all enjoy it as much as I do.

That's it for this week. Next week, I'll be back to talk about Limited and the tools we use to make our sets feel different from one another.

Until next time,

Sam ([@samstod](https://twitter.com/samstod))
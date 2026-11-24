---
id: 87gp89a7
kind: article
lang: en
path: /en/articles/feature/2002/02-01-limited-pointing
title: Limited Pointing
published: '2002-02-01'
column_slug: feature
column: Feature
authors:
- slug: randybuehler
  name: Randy Buehler
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
    lang_detected: en
    capture_id: 755615
    url: https://magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
    captured_at: '2022-08-17 05:04:51+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
    lang_detected: en
    capture_id: 755615
    url: https://magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
    captured_at: '2022-08-17 05:04:51+00'
    rule: drupal.posted_in_date
  column:
    page_key: magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
    lang_detected: en
    capture_id: 755615
    url: https://magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
    captured_at: '2022-08-17 05:04:51+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/limited-pointing-2002-02-01
    lang_detected: en
    capture_id: 726613
    url: https://magic.wizards.com/en/articles/archive/latest-developments/limited-pointing-2002-02-01
    captured_at: '2022-01-24 20:44:02+00'
    rule: drupal.div_author
sources:
- document_id: 87gp89a7
  url: https://magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
  page_key: magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
  lang: en
  template: drupal
  captured_at: '2022-08-17 05:04:51+00'
  capture_id: 755615
  wayback_url: https://web.archive.org/web/20220817050451id_/https://magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
- document_id: 87gp89a7
  url: https://magic.wizards.com/en/articles/archive/latest-developments/limited-pointing-2002-02-01
  page_key: magic.wizards.com/en/articles/archive/latest-developments/limited-pointing-2002-02-01
  lang: en
  template: drupal
  captured_at: '2022-01-24 20:44:02+00'
  capture_id: 726613
  wayback_url: https://web.archive.org/web/20220124204402id_/https://magic.wizards.com/en/articles/archive/latest-developments/limited-pointing-2002-02-01
- document_id: 87gp89a7
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb5
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/rb5
  lang: en
  template: aspx
  captured_at: '2012-12-29 21:40:53+00'
  capture_id: 805303
  wayback_url: https://web.archive.org/web/20121229214053id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/rb5
- document_id: 87gp89a7
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/rb5,,fr,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/rb5
  lang: en
  template: classic_asp
  captured_at: '2005-01-22 04:21:24+00'
  capture_id: 1990329
  wayback_url: https://web.archive.org/web/20050122042124id_/http://www.wizards.com/default.asp?x=mtgcom/daily/rb5,,fr,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 87gp89a7
  capture_id: 755615
  url: https://magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
  wayback_url: https://web.archive.org/web/20220817050451id_/https://magic.wizards.com/en/articles/archive/limited-pointing-2002-02-01
  captured_at: '2022-08-17 05:04:51+00'
  template: drupal
  sha256: 2b796dfc232b770d155e8cdc4ce7ce1acaba4ecace83032badc21d706778a104
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:latestdevelopments@wizards.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - latestdevelopments@wizards.com
  occurrences: 1
---
You’ve just been hired by Wizards of the Coast. You got your dream job – developing *Magic* cards! About halfway through development work on *Torment*, the lead developer says, “OK, it’s time to point the set for Limited.”

![](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb5_pic1_en.jpg)

Developer Elaine Chase constructs a sealed deck

Huh? Point?

“Well," he says, "it’s time to rate each card for Limited and then average up everyone's ratings to get an overall score, which allows us to see how well we’re doing at balancing the set." He points you to the relevant section of the "Developer’s Handbook": (Yes, there really is a document called the “Developer’s Handbook” and, yes, this really is a quote from it. No, I can’t send it to you, but I can try to keep getting permission to show you various parts of it in future articles.)

> *Our #1 goal is to obtain information about the color balance of the set (which colors are stronger in Limited, etc.). Our #2 goal is to create ratings that are useful for collating the print runs of the set. These two goals are* inconsistent *with the following, less important goals: a) Gain an understanding of the power level of our set relative to other sets, and b) Have the same card have the same rating in different sets. We therefore decided to abandon those less important goals and we agreed that all ratings should be relative to the current block.*
> 
> *Thus, here is the fundamental definition of our rating: Given that this is the first card you see (of your 75-card sealed deck or first pack, first pick in draft), how happy are you -- on a scale of 0.0 - 5.0 -- to see it? Furthermore, your ratings should be linear (that is, you’d be just as happy with a 3.5 and a 2.5 or with two 3.0’s). Also, to be technically correct, this all assumes that your goal is to win – winning makes you “happy.”*
> 
> *The following elaborations of this scale are merely guidelines, designed to clarify the scale defined above:*
> 
> ***5.0**: I will always play this card. Period.*
> 
> ***4.5**: I will almost always play this card, regardless of what else I get.*
> 
> ***4.0**: I will strongly consider playing this as the only card of its color.*
> 
> ***3.5**: I feel a strong pull into this card’s color.*
> 
> ***3.0**: This card makes me want to play this color. (Given that I’m playing that color, I will play this card 100% of the time.)*
> 
> ***2.5**: Several cards of this power level start to pull me into this color. If playing that color, I essentially always play these. (Given that I’m playing that color, I will play this card 90% of the time.)*
> 
> ***2.0**: If I’m playing this color, I usually play these. (70%)*
> 
> ***1.5**: This card will make the cut into the main deck about half the times I play this color. (50%)*
> 
> ***1.0**: I feel bad when this card is in my main deck. (30%)*
> 
> ***0.5**: There are situations where I might sideboard this into my deck, but I’ll never start it. (10%)*
> 
> ***0.0**: I will never put this card into my deck (main deck or after sideboarding). (0%)*
> 
> *Those guidelines break down for artifacts and gold cards – fall back onto the fundamental definition when rating these categories of cards: the happiness scale.*

The team lead says to fill in your ratings into the spreadsheet that he forwarded to you via email… once everyone fills out his or her spreadsheet, the numbers are all averaged together and then the team can see which cards and which colors are better than the others.

![](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb5_pic2_en.jpg)

There are actually two different goals for this process. On the one hand, we want to make sure each color is at the appropriate power level. Usually, we want each color to have the same overall score, but not always. For example, if we’ve already figured out that we messed up with the base set of a block then we’ll try to balance things out in the later sets. Or if we ever decided to do something crazy, like make a set where one color was more important than all the others, we’d probably let that color have higher-pointing cards.

The second thing we do with our pointing values (other than seeing whether the colors are balanced) is to use them as an aid to collation. When we decide where to place the cards on the sheet that gets printed, we make sure that when they’re assembled into booster packs, the packs will have approximately the same power-level worth of cards. We don’t want to have packs where all the cards are bad or packs where all the cards are good, so we make sure each pack has about the same number of points in it. (We call that process “collation.”)

Now it really is your turn. Try your hand at pointing the black commons from *Torment*. Next week I’ll look at the results and I’ll compare your ratings to R&D’s actual ratings for these 17 cards.

A few words of advice, which are pretty much the same things I say to new developers: Everyone always points the cards too high the first time. The average card is probably only a 1.6 or so because you only actually play about half the cards you get in a booster draft, and much fewer than half the cards you get in a sealed deck. Here are a few sample ratings:

*   [Masticore](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Masticore): 5.0 – There are very few 5’s in the history of the game
*   [Fireball](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fireball): 4.3
*   [Agonizing Demise](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Agonizing+Demise): 3.9 – This is about as good as it should get at common. We no longer do cards that point above 4 at common.
*   [Overrun](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Overrun): 3.5 – Would be higher if it wasn’t triple green, of course
*   [Mystic Zealot](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mystic+Zealot): 2.7
*   [Barbarian Lunatic](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Barbarian+Lunatic): 1.8 – Though some players I respect think this card is worse than I do, and would point it lower
*   [Dematerialize](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Dematerialize): 1.2
*   [Circle of Protection: Green](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Circle+of+Protection%3A+Green): 0.6
*   [Saprazzan Raider](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Saprazzan+Raider): 0.0

Have fun! And tune in next week to see how this experiment turns out.

(Note: Here are the cards you will be asked to "point." You can click on them to see the images, and you can bounce between this window and the survey window if necessary.)

![](http://media.wizards.com/legacy/global/images/mtgcom_daily_rb5_pic3_en.jpg)

*   [Cabal Ritual](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cabal+Ritual)
*   [Cabal Surgeon](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cabal+Surgeon)
*   [Cabal Torturer](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cabal+Torturer)
*   [Carrion Rats](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Carrion+Rats)
*   [Crippling Fatigue](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Crippling+Fatigue)
*   [Faceless Butcher](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Faceless+Butcher)
*   [Gravegouger](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gravegouger)
*   [Mesmeric Fiend](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Mesmeric+Fiend)
*   [Organ Grinder](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Organ+Grinder)
*   [Psychotic Haze](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Psychotic+Haze)
*   [Putrid Imp](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Putrid+Imp)
*   [Rancid Earth](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Rancid+Earth)
*   [Restless Dreams](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Restless+Dreams)
*   [Shade's Form](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shade%27s+Form)
*   [Soul Scourge](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Scourge)
*   [Unhinge](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unhinge)
*   [Waste Away](https://web.archive.org/web/20020201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Waste+Away)

Click here to take the [Limited Pointing Survey!](https://web.archive.org/web/20020201000000/http://archive.wizards.com/Magic/magazine/Article.aspx?x=mtgcom/daily/rb5)

* * *

*Randy may be reached at latestdevelopments@wizards.com.*
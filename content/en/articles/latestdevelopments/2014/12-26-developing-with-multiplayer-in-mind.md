---
id: zswn3w0x
kind: article
lang: en
path: /en/articles/latestdevelopments/2014/12-26-developing-with-multiplayer-in-mind
title: Developing With Multiplayer in Mind
published: '2014-12-26'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: sam-stoddard-0c6b27df
  name: Sam Stoddard
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
    lang_detected: en
    capture_id: 720955
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
    captured_at: '2015-01-17 05:04:42+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
    lang_detected: en
    capture_id: 720955
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
    captured_at: '2015-01-17 05:04:42+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
    lang_detected: en
    capture_id: 720955
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
    captured_at: '2015-01-17 05:04:42+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
    lang_detected: en
    capture_id: 720955
    url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
    captured_at: '2015-01-17 05:04:42+00'
    rule: url.article_section
    registry_match: registry.separator_and_case
sources:
- document_id: zswn3w0x
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
  page_key: magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
  lang: en
  template: drupal
  captured_at: '2015-01-17 05:04:42+00'
  capture_id: 720955
  wayback_url: https://web.archive.org/web/20150117050442id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: zswn3w0x
  capture_id: 720955
  url: http://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
  wayback_url: https://web.archive.org/web/20150117050442id_/http://magic.wizards.com/en/articles/archive/latest-developments/developing-multiplayer-mind-2014-12-26
  captured_at: '2015-01-17 05:04:42+00'
  template: drupal
  sha256: ec98cd62ed81911b65c755f2a0ead84b6376fd4233131a5e0b058d4472570dbf
render_recovery: []
---
It's Multiplayer Week on DailyMTG.com, and I want to take a little time to talk about what goes into our sets when developing cards with multiplayer in mind. I want to separate the differences between cards that started out in multiplayer products that are too strong and/or frustrating in two-player games (I'm looking at you, [True Name Nemesis](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=True+Name+Nemesis)), and cards that ended up missing the mark entirely and not making any impact. But that's another article. Today, I want to talk about cards intended for a multiplayer audience, and how we have succeeded or failed as a whole on those cards.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=True-Name+Nemesis)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=True-Name+Nemesis)

The rise of Commander over the last few years has really highlighted to us a group of players that we were undeserving when creating cards. The success of the first *Commander* decks in 2011 proved not only that this audience existed, but how much design and development space there was for cards that were able to exist without going through Standard. It meant that we could do a lot of effects that had been largely off limits for Standard and create cards that could even have an impact on eternal formats. Instead of being concerned about how a card might play in Limited, we were able to shoot for the stars and allow for huge effects at relatively low mana costs. It was pretty exciting.

Of course, once we try and design cards for an audience, there will be a few misses while we try and find our footing. I think the poster child for this is Worldfire—a card that was created to read as really exciting for multiplayer, but ended up being endlessly frustrating for the players in the games where it was cast. There is some amount of crazy game-affecting effects we want in the game, but Worldfire just went too far. In a similar vein, [Sylvan Primordial](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sylvan+Primordial) was a card that combined a lot of very risky things—scaling removal and ramping—that were too much for [the Commander rules committee](http://mtgcommander.net/rules.php). We learned from these kinds of mistakes, and I think you will see fewer problems in cards as we move forward.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Worldfire)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Worldfire)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sylvan%20Primordial)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sylvan%20Primordial)

There are other changes we made in the recent past that have been more successful in multiplayer. One of my favorite examples is the "[Oblivion Ring](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) into [Banishing Light](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Banishing+Light) change" for templating that lets us create cards that are much more friendly for multiplayer games. In case you didn't realize it, a permanent exiled by [Oblivion Ring](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring) doesn't return to its owner when the [Oblivion Ring](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Oblivion+Ring)'s owner dies—since the card has a trigger to return the card that can't happen. On the other hand, [Banishing Light](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Banishing+Light)'s text was set up in such a way that a player dying won't keep the card from returning. This doesn't fix the old cards, but it lets us print cards in the future that will play better with multiplayer. The more we can make small changes like this one—that make our regular gameplay a little better and help out multiplayer at the same time—the better our releases will be in the future.

# Legends

Another area I feel we have been succeeding in recently is creating fun and interesting legendary creatures. Commander is the most popular multiplayer environment, and therefore the one we spend the most time designing toward. You might have noticed that as the *Commander* product has become more and more popular, we have been producing more and more legendary creatures in our sets. Some of this was a little coincidental—since it coincided with a time when we were pushing harder on getting our creative elements onto cards—but it is still something that we think about. Several creatures in *Theros*—like [Hythonia the Cruel](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hythonia+the+Cruel)—were made into legendary creatures so they could be commanders.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hythonia%20the%20Cruel)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Hythonia%20the%20Cruel)

There is definitely a point where we got close to overdoing it in the past, but the goal now is not to generate legendary creatures for the purpose of generating commanders—it is to generate legendary creatures to create awesome cards that show off our storyline. Between our four main set releases and our annualized *Commander* product, we generate more potential commanders than most players will ever be able to design decks around. It's also pretty hard for our main sets to create legendary creatures that can compete on a Commander power level with the ones in the actual *Commander* product, so trying to get there with each individual legendary creature is a little foolhardy. We'd much rather get to the point where the characters we are generating (and showing off in our cards) inspire people to build decks around them rather than just their raw power.

Looking at the [khans in *Khans of Tarkir*](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&set=+[%22Khans%20of%20Tarkir%22]&type=+[%22Legendary%22]+[%22Creature%22]), we definitely wanted to have cards that could play well in multiplayer. But we wanted them to hit the flavor and gameplay needs of the story, specifically of their clans, first and foremost, and allow them to exist in multiplayer as a secondary concern. To that end, what we've been moving toward is making sure we have a ton of cool legendary creatures, but not that each individual one is focused on being a multiplayer card. As we continue to improve the overlap of story, setting, and gameplay in *Magic*, we want to continue to highlight our most interesting characters as legendary creatures without the need for each one to be the center of a Commander deck. While players can easily generate a Polukranos Commander deck, we didn't design the card to be at the center of one. It is intended to be an awesome monster in the same way that Surrak Dragonclaw is intended to be a card that you would be happy casting in a Standard game.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Polukranos,%20World%20Eater)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Polukranos,%20World%20Eater)

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Surrak%20Dragonclaw)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Surrak%20Dragonclaw)

# Tipping the Scales

I mentioned it earlier, but one of the places where we are still learning a lot is what makes an appropriate scaled effect, and what makes an inappropriate one. A lot of these discussions came out of a pretty innocuous common in *Theros*—[Gray Merchant of Asphode](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Merchant+of+Asphode)l. The card was a fun build-around in Limited, and it even had an impact in Constructed, but we've received feedback from many people about how frustrating it is in multiplayer formats. The problem isn't that it's easier to have a large number of black mana symbols in multiplayer games, it's that the scaling effect gains the caster too much life, which makes it a very frustrating card to try and beat with recursion.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Gray%20Merchant%20of%20Asphodel)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray%20Merchant%20of%20Asphodel)

The card started off in development only hitting one opponent and gaining that much life, but was changed to hitting each player and gaining that much life to make it better for Commander. One of the most interesting parts about designing cards for multiplayer is that you get to play around with the part of the game that is just never in play during one-on-one games—scaling for the number of players. We can take a card that is pretty fun but not Constructed-worthy at its current power level, but frustrating when it is more efficient, and turn it into a card for multiplayer.

This works wonderfully with cards like [Syphon Mind](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Syphon+Mind) because it isn't actually efficient enough to see Constructed play (and it also isn't easy to trigger over and over again)—basically being a four-mana cantrip discard spell—but it really shines in multiplayer environments where it can easily draw four or five cards on turn four. In hindsight, [Gray Merchant of Asphodel](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Merchant+of+Asphodel) is the wrong kind of card to push for multiplayer. Now, I don't think that Gray Merchant is very far over the line, but I don't think we had a good enough grasp of where the line was when we created it.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Syphon%20Mind)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Syphon%20Mind)

Beyond that, this push to having higher-impact cards for multiplayer has generated problems in Two-Headed Giant, a format we don't test much, but one that is very popular among many casual players—especially those who show up for the Prerelease. I don't think there is any question that cards like [Gray Merchant of Asphodel](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Gray+Merchant+of+Asphodel) make for a worse Two-Headed Giant experience, and I hope that we can avoid making them in the future, or at least not at lower rarities. I don't think it is a problem if we have rares that make for a huge Two-Headed Giant blowout, but having them at common warps the format too much.

So, how do these kinds of issues crop up in our sets even if we have a reasonable grasp on the problem? Well, it's complicated. Because most of the developers aren't able to test much multiplayer, we have taken to asking people who play a lot of multiplayer to look through our sets and tell us if cards look like they would be too frustrating, or if there are cards that could be improved. This led to us just increasing the number of cards that scaled with the number of players in general. That improved the feedback we were getting from these multiplayer groups. What it took us a while to learn was which feedback we should take action on and which we shouldn't. Any time we make a card more powerful without a lot of playtesting, we run a risk of making it too powerful. Development itself just doesn't have the ability to play enough with the cards in multiplayer situations.

One of the things that development does a lot of when balancing cards is to play, not only with the cards, but against them. There are many cards that are very fun to play with, but are totally miserable to play against. Because winning games tends to be fun and losing games tends to be not as fun, we want to create an experience between both players that is as net fun as humanly possible. Cards like [Stasis](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stasis) may be fun for the person winning (but probably not a ton of fun) but are utterly miserable for the person losing. It's one of the reasons we don't push the power on cards of that ilk anymore—because the end result of people being forced to play against these kinds of cards in tournaments would be to make fewer people want to attend tournaments.

[![](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Stasis)](https://web.archive.org/web/20141226000000/http://gatherer.wizards.com/Pages/Card/Details.aspx?name=Stasis)

# Making a Better Multiplayer

It takes a long time for feedback from the real world to make its way into sets (we do work about a year in advance, after all), but we are listening when people say they find a card fun or not fun in multiplayer. Then we compare that to what our expectations were. Development is very much based around [iteration](/en/articles/latestdevelopments/2014/03-07-developing-better-sets), and we've had a few years to look at the cards we have released into the wild. We use the feedback we've received from those cards to improve how we make cards in the future.

That's it for this week. Join me next week when I talk about things that don't look like what they seem.

Until next time,

Sam ([@samstod](https://twitter.com/samstod))
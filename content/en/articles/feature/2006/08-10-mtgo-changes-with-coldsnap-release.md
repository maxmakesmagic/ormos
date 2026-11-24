---
id: 9rmz7y04
kind: article
lang: en
path: /en/articles/feature/2006/08-10-mtgo-changes-with-coldsnap-release
title: MTGO Changes with Coldsnap Release!
published: '2006-08-10'
column_slug: feature
column: Feature
authors:
- slug: benniesmith
  name: Bennie Smith
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
    lang_detected: en
    capture_id: 649121
    url: https://magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
    captured_at: '2022-01-23 08:41:57+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
    lang_detected: en
    capture_id: 649121
    url: https://magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
    captured_at: '2022-01-23 08:41:57+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
    lang_detected: en
    capture_id: 649121
    url: https://magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
    captured_at: '2022-01-23 08:41:57+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
    lang_detected: en
    capture_id: 649121
    url: https://magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
    captured_at: '2022-01-23 08:41:57+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: 9rmz7y04
  url: https://magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
  page_key: magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
  lang: en
  template: drupal
  captured_at: '2022-01-23 08:41:57+00'
  capture_id: 649121
  wayback_url: https://web.archive.org/web/20220123084157id_/https://magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9rmz7y04
  capture_id: 649121
  url: https://magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
  wayback_url: https://web.archive.org/web/20220123084157id_/https://magic.wizards.com/en/articles/archive/feature/mtgo-changes-coldsnap-release-2006-08-10
  captured_at: '2022-01-23 08:41:57+00'
  template: drupal
  sha256: 8f20cd329f062852a76d07e94a7e3a2514f2c953414000492fb665b636fb4ea0
render_recovery:
- code: deck_widget_requires_review
  element: a
  reason: The archived deck widget has no visible card rows. The source capture may
    contain data to recover it.
  labels:
  - Decklist
  occurrences: 3
---
### Elf Speaks! MTGO Changes

Hi everyone, this is Michael "elf" Feuell. I'm a Senior Software Developer at Wizards of the Coast and I'm here to talk about some of the changes coming to ***Magic** Online* with the release of *Coldsnap*.

First, automated posters were creating so much traffic and posting so frequently to the Message Board room that it was causing the client to either lag, hang, or crash. Our solution came in 3 parts: 

1.  We're replacing the Message Board with two new boards, "Message Board - Selling", and "Message Board - Buying".
2.  We're adding a post delay so that you have to wait a few minutes before updating or editing your message. This is not a tickertape, and you do not need to update your message every 30 seconds.
3.  The big change! We're adding a client side filter system (it's like a super ignore list). This is implemented as a text file that you edit by hand. You can list usernames and those users you choose will be ignored. This should reduce the overhead in the room considerably as you can pick and choose who you do not see.

But wait - there's more! This client side filter system was something that was actually written a while ago and includes all sorts of neat extras.

The chief power here is the ability for you to have an unlimited block list. With comments. I don't know about you, but for me, I like to know why I blocked someone, or make little notes next to people's names about why they're on my buddy list. With this system you can do that.

But wait - there's still more! Along with the ability to filter users, you can also list the names of rooms and filter types of chat. Don't like lines that are all upper case? Hide them. Don't like the way */me* messages stand out? Fade them.

Wait? Fade them? Ah, the power of fade. In addition to being able to hide someone (i.e. ignore/block) this system has a *partial* block, a fade feature that will change the color of the text of the users of your choice to gray. Very nice if you want to still see text, but have it sort of fade into the background.

Sounds great! How does it all work? Like so—in your ***Magic** Online* folder (typically "C:/Program Files/Wizards of the Coast/Magic Online"), you will create a file called "magic.ini" with the text editor of your choice (like notepad, vi, or emacs).

This magic.ini needs to have a very specific format:

> \[section\]  
>  field=value  
>  field2=value

"Section" will be one of two things, either the label "users" or a room name. "Field" would be a user's name and the value would be how you want that text displayed.

This might sound very simple for some of you, perhaps a little odd for most of you, but an example should make it easier to understand for all:

A sample magic.ini (using some magic legends as user names):

> \[Users\]  
>  Akroma=show  
>  Squee=hide  
>  Volrath=fade

If you had this section in your text, then whenever Squee said something, you would not see it. Volrath's text would appear in all gray, and Akroma's text would show up as normal.

Why even bother with '=show'? Because one of the things you can do with a room is specify a default style.

> \[Marketplace\]  
>  Style=fade

If you have this, all text in the room will be faded, except for users that you have specified to be '=show', or if you have specified certain types of lines to be something other than '=fade'. Consider the following:

> \[Marketplace\]  
>  Style=fade  
>  Upper=hide  
>  Pricecheck=show

With these settings, by default all text will be grayed out. Lines that are in all uppercase will be completely hidden, and lines that are price checks will be shown normally. If you had the above \[users\] section, you would also see Akroma's text normally.

Following so far? Great! Here are some more things to play with. When the filter is determining whether to show|hide|fade someone's text, it only looks at the first four letters after the '='. So anything after that can be used for a comment. Like this:

> \[Users\]  
>  Akroma=show -- great trader!  
>  Squee=hide -- tried to sneak an extra booster from me  
>  Volrath=fade -- owes me 3 tickets!

Finishing it all up, what else is missing? Well you already know about show|fade|hide, what you don't know is all the stuff you can apply them to.

Here's the list:

*   Upper - all upper case
*   Lower - all lower case
*   Action - any /me actions
*   Number - all numbers
*   Pricecheck - lines that begin with "pc "

**Bringing it all Together**

Let's start with the following magic.ini file:

> \[Marketplace\]  
>  Style=fade  
>  Pricecheck=show  
>  Upper=hide
> 
> \[Moderators and Support Staff\]  
>  Action=fade  
>  Upper=fade
> 
> \[Users\]  
>  Akroma=show -- on my buddy list  
>  Squee=hide  
>  Volrath=fade -- owes me 3 tickets!

You can cut and paste that and save it as 'magic.ini' in your ***Magic** Online* folder. Of course you can make this file bigger by adding to it. You can probably come up with new uses that I haven't thought of. One thing to note, none of these options will work on Wizards or Adept accounts. 

The most significant impact will be in trade-related rooms, where hopefully spam will be less of a problem. I don't expect it to go away, but we're providing a tool for you to have more control over what adverts you see, or how you see them.

The option that prevents you from playing spells without putting the mana in your pool first has been removed. This option never did work quite right, and was intended for advanced users, but mostly ended up being used by new users that became confused as to what it did. You still can tap mana first, you're just not forced to. If there is a pressing desire for it to return, we'll consider adding it in to V3 and doing it correctly.

Also coming with *Coldsnap* are some more messages about game state. Originally added to the game to help track down some bugs, they proved so popular they were left in. In the scrolling game text at the bottom of the screen you will see messages when the step changes. This should help players be more aware of what happened at what part of the turn when before it wasn't always clear.

*Coldsnap* is tons of fun, I'm really looking forward to playing it online. I hope you are too. Pardon the *Coldsnap* pun, but I think these changes are pretty cool.

-elf

### *Coldsnap* Release Events!

*Coldsnap* goes on sale for ***Magic** Online* this coming Monday, August 14th. Info for the upcoming [*Coldsnap* Release Events](https://web.archive.org/web/20060810000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magic/magiconline/article080106) (which start next Thursday, August 17th) was posted last week, but in case you haven't seen it or just gave it a glance over, let me highlight a few things.

The sealed events (Leagues, 2x and 4x Premier Events) will require 5 *Coldsnap* booster packs (there are no tournament decks). 

The 2x Premier Events cost 2 Tix (along with product), with all participants getting the participation avatar and the Top 2 getting the prize avatar. Each first place finisher will qualify for the 2x Championship on Saturday, August 26th. 

The 4x Premier Events will cost 4 tix (along with product), with participation avatars given out to all players, and the prize avatar going to the Top 8. The Top 8 players in each 4x Premier event will qualify for the 4x Premier event on Saturday, August 26th.

Note that there will be two separate Championships, and both will be 6x events with prize payouts down to 64th place! The winner of each Championship will get a Premium set of *Coldsnap* cards, and each runner-up will get a full regular set. 

For the release Leagues, everyone gets the participation avatar, and those who go 5-0 win the prize avatar. 

The *Coldsnap* participation avatar is Diamond Faerie; the prize avatar is Haakon, Stromgald Scourge. Since Vanguard is one of my favorite MTGO formats, you know I cannot resist posting a few deck ideas!

![](https://i.ormos.uk/ca/fe/cafe363ac28a38562055df4d88217d75bd2ed22cfac24a172f58749b20fc456b.jpg)**Diamond Faerie**  
 Starting hand size +0  
 Starting life total +5  
: Target creature you control gets +1/+1 until end of turn.

The participation avatar is tied deeply to *Coldsnap*, and will require collecting snow lands to make full use of Diamond Faerie. The dilemma with this ability is that it leaves you particularly vulnerable to instant speed removal; if you use up all your mana to pump your creature and your opponent kills it before damage is put on the stack, they've effectively made you waste your turn and valuable mana. Cards like Silhana Ledgewalker get around this problem, but there are not enough such cards in Standard to fill out your deck. I thought another way to blunt this problem is to make a very aggressive weenie deck that attacks from the very first turn. If your opponent blocks, you use your mana to pump your attacker and kill the blocker (hopefully keeping your attacker alive). If your opponent doesn't block, use your mana instead to play another threat. 

![Bushi Tenderfoot](http://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Bushi+Tenderfoot)

When looking over various weenies I ran across [Bushi Tenderfoot](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bushi+Tenderfoot). Admit it, this guy has piqued your interest—if you can somehow get him to flip he becomes an absolute beating! This sort of deck seems like a perfect fit for the Tenderfoot since it should be relatively easy to get the Tenderfoot into combat, killing an opposing creature and surviving the exchange. If nothing else, he makes a scary blocker with some mana available.

Efficient beaters like Isamaru and [Watchwolf](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Watchwolf) get even fiercer supported by snowy +1/+1 pumps. [Ohran Viper](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ohran+Viper) becomes quite nasty, either getting in for a card or taking down any creature with just enough pump effects to keep it alive.

[Greater Good](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Greater+Good) seems like a great inclusion, able to cash in any pumped creatures for an extra card per snow mana spent pumping. At the top end of the curve, [Seedborn Muse](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Seedborn+Muse) lets you get double duty out of your creatures and mana and should be particularly nice with Scrying Sheets in play.

I added [Soul Warden](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Soul+Warden) to the deck to help combat the scary Nekrataal deck that can win so quickly. Coupled with the starting life boost, it should buy you some turns to stabilize the game.

#### Hurts Snow Good, by Bennie Smith (Standard Vanguard)

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (33)

4 [Soul Warden](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BWarden%5D) 4 [Bushi Tenderfoot](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBushi%5D+%5BTenderfoot%5D) 4 [Isamaru, Hound of Konda](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 4 [Watchwolf](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwolf%5D) 4 [Silhana Ledgewalker](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilhana%5D+%5BLedgewalker%5D) 2 [Seedborn Muse](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeedborn%5D+%5BMuse%5D) 4 [Boreal Druid](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoreal%5D+%5BDruid%5D) 3 [Ronom Unicorn](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRonom%5D+%5BUnicorn%5D) 4 [Ohran Viper](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOhran%5D+%5BViper%5D) 

##### Enchantment (4)

4 [Greater Good](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BGood%5D) 

##### Land (23)

2 [Selesnya Sanctuary](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BSanctuary%5D) 6 [Snow-Covered Forest](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BForest%5D) 7 [Snow-Covered Plains](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BPlains%5D) 4 [Arctic Flats](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArctic%5D+%5BFlats%5D) 4 [Scrying Sheets](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrying%5D+%5BSheets%5D) 

60 Cards 

##### White (15)

4 [Soul Warden](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BWarden%5D) 4 [Bushi Tenderfoot](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBushi%5D+%5BTenderfoot%5D) 4 [Isamaru, Hound of Konda](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 3 [Ronom Unicorn](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRonom%5D+%5BUnicorn%5D) 

##### Green (18)

4 [Silhana Ledgewalker](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilhana%5D+%5BLedgewalker%5D) 2 [Seedborn Muse](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeedborn%5D+%5BMuse%5D) 4 [Boreal Druid](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoreal%5D+%5BDruid%5D) 4 [Ohran Viper](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOhran%5D+%5BViper%5D) 4 [Greater Good](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BGood%5D) 

##### Multi colored (4)

4 [Watchwolf](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwolf%5D) 

##### Colorless (23)

2 [Selesnya Sanctuary](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BSanctuary%5D) 6 [Snow-Covered Forest](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BForest%5D) 7 [Snow-Covered Plains](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BPlains%5D) 4 [Arctic Flats](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArctic%5D+%5BFlats%5D) 4 [Scrying Sheets](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrying%5D+%5BSheets%5D) 

60 Cards 

##### 1 (16)

4 [Soul Warden](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BWarden%5D) 4 [Bushi Tenderfoot](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBushi%5D+%5BTenderfoot%5D) 4 [Isamaru, Hound of Konda](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 4 [Boreal Druid](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoreal%5D+%5BDruid%5D) 

##### 2 (11)

4 [Watchwolf](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwolf%5D) 4 [Silhana Ledgewalker](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilhana%5D+%5BLedgewalker%5D) 3 [Ronom Unicorn](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRonom%5D+%5BUnicorn%5D) 

##### 3 (4)

4 [Ohran Viper](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOhran%5D+%5BViper%5D) 

##### 4 (4)

4 [Greater Good](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BGood%5D) 

##### 5 (2)

2 [Seedborn Muse](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeedborn%5D+%5BMuse%5D) 

37 Cards 

##### Common (28)

6 [Snow-Covered Forest](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BForest%5D) 7 [Snow-Covered Plains](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSnow-Covered%5D+%5BPlains%5D) 4 [Soul Warden](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSoul%5D+%5BWarden%5D) 4 [Silhana Ledgewalker](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSilhana%5D+%5BLedgewalker%5D) 4 [Boreal Druid](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBoreal%5D+%5BDruid%5D) 3 [Ronom Unicorn](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRonom%5D+%5BUnicorn%5D) 

##### Uncommon (14)

2 [Selesnya Sanctuary](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSelesnya%5D+%5BSanctuary%5D) 4 [Arctic Flats](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BArctic%5D+%5BFlats%5D) 4 [Bushi Tenderfoot](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBushi%5D+%5BTenderfoot%5D) 4 [Watchwolf](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWatchwolf%5D) 

##### Rare (18)

4 [Scrying Sheets](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BScrying%5D+%5BSheets%5D) 4 [Isamaru, Hound of Konda](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsamaru,%5D+%5BHound%5D+%5Bof%5D+%5BKonda%5D) 2 [Seedborn Muse](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSeedborn%5D+%5BMuse%5D) 4 [Ohran Viper](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOhran%5D+%5BViper%5D) 4 [Greater Good](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGreater%5D+%5BGood%5D) 

60 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Selesnya+Sanctuary)

[Deal Another Hand](https://web.archive.org/web/20060810000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Greater+Good)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Snow-Covered+Forest)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Scrying+Sheets)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Boreal+Druid)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Isamaru%2C+Hound+of+Konda)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Boreal+Druid)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Soul+Warden)

a:15:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Selesnya Sanctuary";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"6";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Snow-Covered Forest";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"7";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Snow-Covered Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Arctic Flats";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Scrying Sheets";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Soul Warden";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Bushi Tenderfoot";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Isamaru, Hound of Konda";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Watchwolf";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Silhana Ledgewalker";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Seedborn Muse";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Boreal Druid";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Ronom Unicorn";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:11:"Ohran Viper";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:11:"enchantment";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Greater Good";s:22:"field\_card\_image\_front";a:0:{}}}} 

![](https://i.ormos.uk/81/77/817714f4d3604e3156a1aafe22c867751da54fbc22e0b4de6ab93559148c504d.jpg)**Haakon, Stromgald Scourge**  
 Starting hand size +0  
 Starting life total -3  
 Pay 1 life: You may play target creature card in your graveyard this turn.  
 Whenever a creature comes into play, if you played it from your graveyard, it becomes a black Zombie Knight.  
 Whenever a Zombie Knight would be put into your graveyard from play, remove it from the game instead.

For the prize avatar, Haakon has really gotten my mind filled with ideas. The first thought of course was how perfect it would work in a dredge deck, allowing you to access non-dredge creatures by just playing them straight from the graveyard. One card that would go really well in this sort of deck is [Void Maw](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Void+Maw) to circumvent the unfortunate “remove from game” clause. Since you'd control both [Void Maw](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Void+Maw) and Haakon's remove from game triggers, you could choose to stack it so that [Void Maw](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Void+Maw) resolves first and gives you the ability to put that creature into your graveyard to play again. 

A Haakon dredge deck would be pretty easy to concoct, so I thought I'd develop a few other ideas. Next on my mind was how you could use [Martyr of Sands](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Martyr+of+Sands) in order to keep your life total high, both for defense and for continual abuse of Haakon's ability.

#### Sandman, by Bennie Smith (Standard Vanguard)

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (26)

4 [Kami of False Hope](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BFalse%5D+%5BHope%5D) 3 [Azorius Herald](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 4 [Court Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCourt%5D+%5BHussar%5D) 3 [Sky Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BHussar%5D) 4 [Martyr of Sands](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartyr%5D+%5Bof%5D+%5BSands%5D) 4 [Adarkar Valkyrie](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BValkyrie%5D) 4 [Ronom Unicorn](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRonom%5D+%5BUnicorn%5D) 

##### Sorcery (4)

4 [Wrath of God](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWrath%5D+%5Bof%5D+%5BGod%5D) 

##### Instant (6)

4 [Remand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 2 [Ghostway](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhostway%5D) 

##### Land (24)

3 [Azorius Chancery](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 4 [Adarkar Wastes](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 4 [Hallowed Fountain](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHallowed%5D+%5BFountain%5D) 4 [Island](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Plains](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### White (25)

4 [Kami of False Hope](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BFalse%5D+%5BHope%5D) 3 [Azorius Herald](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 4 [Martyr of Sands](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartyr%5D+%5Bof%5D+%5BSands%5D) 4 [Adarkar Valkyrie](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BValkyrie%5D) 4 [Ronom Unicorn](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRonom%5D+%5BUnicorn%5D) 2 [Ghostway](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhostway%5D) 4 [Wrath of God](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWrath%5D+%5Bof%5D+%5BGod%5D) 

##### Blue (8)

4 [Court Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCourt%5D+%5BHussar%5D) 4 [Remand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 

##### Multi colored (3)

3 [Sky Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BHussar%5D) 

##### Colorless (24)

3 [Azorius Chancery](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 4 [Adarkar Wastes](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 4 [Hallowed Fountain](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHallowed%5D+%5BFountain%5D) 4 [Island](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Plains](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 

60 Cards 

##### 1 (8)

4 [Kami of False Hope](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BFalse%5D+%5BHope%5D) 4 [Martyr of Sands](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartyr%5D+%5Bof%5D+%5BSands%5D) 

##### 2 (8)

4 [Ronom Unicorn](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRonom%5D+%5BUnicorn%5D) 4 [Remand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 

##### 3 (9)

3 [Azorius Herald](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 4 [Court Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCourt%5D+%5BHussar%5D) 2 [Ghostway](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhostway%5D) 

##### 4 (4)

4 [Wrath of God](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWrath%5D+%5Bof%5D+%5BGod%5D) 

##### 5 (3)

3 [Sky Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BHussar%5D) 

##### 6 (4)

4 [Adarkar Valkyrie](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BValkyrie%5D) 

36 Cards 

##### Common (33)

4 [Island](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 9 [Plains](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BPlains%5D) 4 [Kami of False Hope](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BKami%5D+%5Bof%5D+%5BFalse%5D+%5BHope%5D) 4 [Court Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCourt%5D+%5BHussar%5D) 4 [Martyr of Sands](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMartyr%5D+%5Bof%5D+%5BSands%5D) 4 [Ronom Unicorn](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRonom%5D+%5BUnicorn%5D) 4 [Remand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 

##### Uncommon (9)

3 [Azorius Chancery](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BChancery%5D) 3 [Azorius Herald](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAzorius%5D+%5BHerald%5D) 3 [Sky Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSky%5D+%5BHussar%5D) 

##### Rare (18)

4 [Adarkar Wastes](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BWastes%5D) 4 [Hallowed Fountain](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHallowed%5D+%5BFountain%5D) 4 [Adarkar Valkyrie](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BAdarkar%5D+%5BValkyrie%5D) 2 [Ghostway](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BGhostway%5D) 4 [Wrath of God](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BWrath%5D+%5Bof%5D+%5BGod%5D) 

60 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Azorius+Chancery)

[Deal Another Hand](https://web.archive.org/web/20060810000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Court+Hussar)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Wrath+of+God)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Kami+of+False+Hope)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Plains)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Remand)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Ronom+Unicorn)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)

a:15:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Azorius Chancery";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Adarkar Wastes";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:17:"Hallowed Fountain";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"9";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Plains";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Kami of False Hope";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:14:"Azorius Herald";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Court Hussar";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:10:"Sky Hussar";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Martyr of Sands";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:16:"Adarkar Valkyrie";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Ronom Unicorn";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Remand";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"2";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:8:"Ghostway";s:22:"field\_card\_image\_front";a:0:{}}}i:14;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:12:"Wrath of God";s:22:"field\_card\_image\_front";a:0:{}}}} 

I also had the Nekrataal deck in mind while building this deck, since getting double use of [Martyr of Sands](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Martyr+of+Sands) and [Kami of False Hope](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Kami+of+False+Hope) should buy some serious time. I also like the thought of getting double use of [Azorius Herald](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Azorius+Herald) and [Court Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Court+Hussar). Being able to get your creatures back (assuming they're not currently Zombie Knights) also makes [Wrath of God](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Wrath+of+God) rather unfair. 

![Adarkar_Valkyrie](https://i.ormos.uk/6e/3c/6e3c1c5d5ead12014c17793443498cb68b56ae169be6ff0091507fd81a372881.jpg)Assuming that you'll have a good amount of creatures in play due to Haakon's recursion, it seems that [Sky Hussar](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sky+Hussar)'s forecast ability can be a big help keeping your hand fueled. [Adarkar Valkyrie](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Adarkar+Valkyrie) is obviously strong in a creature deck, but how crazy is she when she takes two removal spells to permanently take down? 

Lastly, I thought [Ghostway](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Ghostway) would be a good way to “reset” your creatures in play and remove their Zombie Knight status so you can get another use out of them. 

White's lifegaining options make a lot of sense pairing up with Haakon, but there are two artifacts that can help make other color Haakon decks work—[Bottle Gnomes](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Bottle+Gnomes) and [Skullmead Cauldron](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Skullmead+Cauldron). I also wanted to build a blue Haakon deck, since many of blue's card-drawing effects are “balanced” by requiring one or more cards to be pitched to the graveyard, and Haakon cracks that wide open. So long as you have two creatures to pitch, [Compulsive Research](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Compulsive+Research) effectively draws you three cards. And [Vexing Sphinx](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vexing+Sphinx)! So long as you pitch creatures, the upkeep costs you nothing, and even if you cash in the Sphinx to draw cards, you can replay the thing. [Thought Courier](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Thought+Courier) and [Drowned Rusalka](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Drowned+Rusalka) can do similar things on a smaller scale. Meloku makes a fine finisher, especially since opponents will need to handle each copy twice!

#### Stromgald Tango, by Bennie Smith (Standard Vanguard)

##### 

 ![Download Arena Decklist](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download_arena.png) ![](https://magic.wizards.com/sites/all/modules/features/wiz_bean_content_deck_list/icons/decklist_download.png)

[Decklist](#none) [Stats](#none) [Sample Hand](#none) 

Sort by: 

##### Creature (20)

4 [Drowned Rusalka](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrowned%5D+%5BRusalka%5D) 4 [Thought Courier](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThought%5D+%5BCourier%5D) 4 [Bottle Gnomes](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 4 [Meloku the Clouded Mirror](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 4 [Vexing Sphinx](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVexing%5D+%5BSphinx%5D) 

##### Sorcery (4)

4 [Compulsive Research](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCompulsive%5D+%5BResearch%5D) 

##### Instant (8)

4 [Remand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Hinder](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHinder%5D) 

##### Artifact (4)

4 [Skullmead Cauldron](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkullmead%5D+%5BCauldron%5D) 

##### Land (24)

1 [Miren, the Moaning Well](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMiren,%5D+%5Bthe%5D+%5BMoaning%5D+%5BWell%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 1 [Oboro, Palace in the Clouds](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOboro,%5D+%5BPalace%5D+%5Bin%5D+%5Bthe%5D+%5BClouds%5D) 3 [Quicksand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuicksand%5D) 18 [Island](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 

60 Cards 

##### Blue (28)

4 [Drowned Rusalka](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrowned%5D+%5BRusalka%5D) 4 [Thought Courier](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThought%5D+%5BCourier%5D) 4 [Meloku the Clouded Mirror](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 4 [Vexing Sphinx](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVexing%5D+%5BSphinx%5D) 4 [Remand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 4 [Compulsive Research](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCompulsive%5D+%5BResearch%5D) 4 [Hinder](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHinder%5D) 

##### Colorless (32)

1 [Miren, the Moaning Well](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMiren,%5D+%5Bthe%5D+%5BMoaning%5D+%5BWell%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 1 [Oboro, Palace in the Clouds](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOboro,%5D+%5BPalace%5D+%5Bin%5D+%5Bthe%5D+%5BClouds%5D) 3 [Quicksand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuicksand%5D) 18 [Island](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Bottle Gnomes](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 4 [Skullmead Cauldron](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkullmead%5D+%5BCauldron%5D) 

60 Cards 

##### 1 (4)

4 [Drowned Rusalka](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrowned%5D+%5BRusalka%5D) 

##### 2 (8)

4 [Thought Courier](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThought%5D+%5BCourier%5D) 4 [Remand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 

##### 3 (16)

4 [Bottle Gnomes](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 4 [Vexing Sphinx](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVexing%5D+%5BSphinx%5D) 4 [Compulsive Research](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCompulsive%5D+%5BResearch%5D) 4 [Hinder](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHinder%5D) 

##### 4 (4)

4 [Skullmead Cauldron](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkullmead%5D+%5BCauldron%5D) 

##### 5 (4)

4 [Meloku the Clouded Mirror](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 

36 Cards 

##### Common (26)

18 [Island](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BIsland%5D) 4 [Bottle Gnomes](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BBottle%5D+%5BGnomes%5D) 4 [Remand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BRemand%5D) 

##### Uncommon (19)

3 [Quicksand](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BQuicksand%5D) 4 [Drowned Rusalka](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BDrowned%5D+%5BRusalka%5D) 4 [Thought Courier](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BThought%5D+%5BCourier%5D) 4 [Hinder](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BHinder%5D) 4 [Skullmead Cauldron](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BSkullmead%5D+%5BCauldron%5D) 

##### Rare (15)

1 [Miren, the Moaning Well](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMiren,%5D+%5Bthe%5D+%5BMoaning%5D+%5BWell%5D) 1 [Minamo, School at Water's Edge](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMinamo,%5D+%5BSchool%5D+%5Bat%5D+%5BWater%5D+%5BEdge%5D) 1 [Oboro, Palace in the Clouds](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BOboro,%5D+%5BPalace%5D+%5Bin%5D+%5Bthe%5D+%5BClouds%5D) 4 [Meloku the Clouded Mirror](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BMeloku%5D+%5Bthe%5D+%5BClouded%5D+%5BMirror%5D) 4 [Vexing Sphinx](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BVexing%5D+%5BSphinx%5D) 4 [Compulsive Research](https://web.archive.org/web/20060810000000/https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+%5BCompulsive%5D+%5BResearch%5D) 

60 Cards 

![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Miren%2C+the+Moaning+Well)

[Deal Another Hand](https://web.archive.org/web/20060810000000/https://magic.wizards.com/en)

*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Hinder)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Skullmead+Cauldron)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thought+Courier)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Miren%2C+the+Moaning+Well)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Island)
*   ![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Thought+Courier)

a:14:{i:0;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:23:"Miren, the Moaning Well";s:22:"field\_card\_image\_front";a:0:{}}}i:1;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:30:"Minamo, School at Water's Edge";s:22:"field\_card\_image\_front";a:0:{}}}i:2;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"1";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:27:"Oboro, Palace in the Clouds";s:22:"field\_card\_image\_front";a:0:{}}}i:3;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:1:"3";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:9:"Quicksand";s:22:"field\_card\_image\_front";a:0:{}}}i:4;O:8:"stdClass":3:{s:4:"type";s:4:"land";s:10:"deck\_count";s:2:"18";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Island";s:22:"field\_card\_image\_front";a:0:{}}}i:5;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Drowned Rusalka";s:22:"field\_card\_image\_front";a:0:{}}}i:6;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:15:"Thought Courier";s:22:"field\_card\_image\_front";a:0:{}}}i:7;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Bottle Gnomes";s:22:"field\_card\_image\_front";a:0:{}}}i:8;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:25:"Meloku the Clouded Mirror";s:22:"field\_card\_image\_front";a:0:{}}}i:9;O:8:"stdClass":3:{s:4:"type";s:8:"creature";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:13:"Vexing Sphinx";s:22:"field\_card\_image\_front";a:0:{}}}i:10;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Remand";s:22:"field\_card\_image\_front";a:0:{}}}i:11;O:8:"stdClass":3:{s:4:"type";s:7:"sorcery";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:19:"Compulsive Research";s:22:"field\_card\_image\_front";a:0:{}}}i:12;O:8:"stdClass":3:{s:4:"type";s:7:"instant";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:6:"Hinder";s:22:"field\_card\_image\_front";a:0:{}}}i:13;O:8:"stdClass":3:{s:4:"type";s:8:"artifact";s:10:"deck\_count";s:1:"4";s:9:"card\_meta";O:8:"stdClass":2:{s:5:"title";s:18:"Skullmead Cauldron";s:22:"field\_card\_image\_front";a:0:{}}}} 

### Changing of the Guard

While I've been saying “goodbye” for a few weeks now, I just wanted to take a moment to thank Aaron Forsythe for bringing me into the **magicthegathering.com** family four years ago last month ([Single Card Strategy: Forcemage Advocate](https://web.archive.org/web/20060810000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/feature/66)), and Scott Johns for the awesome opportunity to write weekly about ***Magic** Online* back in March of 2005 - has it been that long? It's been great writing for Wizards of the Coast, and I hope that one day perhaps I can help out again. Make sure to check back here next week when the new author and new MTGO column get their start!
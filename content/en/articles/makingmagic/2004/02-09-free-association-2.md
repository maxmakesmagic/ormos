---
id: btz7wfaw
kind: article
lang: en
path: /en/articles/makingmagic/2004/02-09-free-association-2
title: Free Association
published: '2004-02-09'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
    lang_detected: en
    capture_id: 882443
    url: https://magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
    captured_at: '2021-10-27 11:14:52+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
    lang_detected: en
    capture_id: 882443
    url: https://magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
    captured_at: '2021-10-27 11:14:52+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
    lang_detected: en
    capture_id: 882443
    url: https://magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
    captured_at: '2021-10-27 11:14:52+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
    lang_detected: en
    capture_id: 882443
    url: https://magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
    captured_at: '2021-10-27 11:14:52+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: btz7wfaw
  url: https://magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
  page_key: magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
  lang: en
  template: drupal
  captured_at: '2021-10-27 11:14:52+00'
  capture_id: 882443
  wayback_url: https://web.archive.org/web/20211027111452id_/https://magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
- document_id: btz7wfaw
  url: https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr110
  page_key: wizards.com/magic/magazine/article.aspx?x=mtgcom/daily/mr110
  lang: en
  template: aspx
  captured_at: '2009-06-04 14:57:19+00'
  capture_id: 796276
  wayback_url: https://web.archive.org/web/20090604145719id_/https://www.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr110
- document_id: btz7wfaw
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr110,,pt
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr110
  lang: en
  template: classic_asp
  captured_at: '2005-03-18 11:24:22+00'
  capture_id: 1969090
  wayback_url: https://web.archive.org/web/20050318112422id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr110,,pt
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: btz7wfaw
  capture_id: 882443
  url: https://magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
  wayback_url: https://web.archive.org/web/20211027111452id_/https://magic.wizards.com/en/articles/archive/making-magic/free-association-2004-02-09
  captured_at: '2021-10-27 11:14:52+00'
  template: drupal
  sha256: 8a9d3ee1b05e53e42f4b26a5776e8e30a9e0b16e21b0aee11e31435d1b2cd077
render_recovery: []
---
Welcome to the New & Improved **magicthegathering.com**! We've taken all the different official Wizards of the Coast sponsored content sites (**Sideboard.com**, **magicthegathering.com**, and the former ***Magic* Online** website) and combined them into one supersized new site. This new **magicthegathering.com** has kept all the pieces of the old **magicthegathering.com** and added in content and popular elements from both **Sideboard.com** and the ***Magic* Online** website. The end result is a bigger and more exciting site. Instead of one columnist each day, for example, we now have two including columns dedicated to organized play and ***Magic* Online**. 

Now for some of you, this might be your first visit to **magicthegathering.com**, so let me quickly introduce myself. My name is Mark Rosewater. I've recently been promoted to **Magic** Lead Designer. Basically, this means I'm in charge of overseeing the design of **Magic**. And in my column “Making **Magic**” each Monday, I'm going to give you a peek behind the curtain of **Magic** design. 

And to start things off with a bang, I have a very offbeat column. My regular readers are aware that I have a tendency to occasionally do columns a bit off the beaten path. Today's column? It can't even see the beaten path. Today's column is going to be unlike any **Magic** column you have ever read. If you're not a fan of my more untraditional columns, please step away from the keyboard. What I'm about to do is not for the faint of heart.

Last chance. If you like your columns straight and narrow, today is not the day for you.

Okay, everyone left up for a cool little experience? Before I get to what I'm doing, let me start with why. One of the most important parts of designing trading card games is truly understanding trading card games. A good designer needs to appreciate how they function. For starters, as a medium, trading card games are non-linear (I'm using the “follows in a straight line” definition and not the “linear” as in modular/linear definition I explained in my “[Come Together](https://web.archive.org/web/20040209000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr92)” column); that is, they do not force the audience to experience the medium in a preset order. 

Most forms of entertainment are presented in a linear matter. Take books as an example. The author of a book knows you're going to read page 1 before page 2. The director of a movie knows that you'll watch the opening scene before the climatic ending scene. Even the builder of a roller coaster knows you're going down the big hill before you do the loop de loop. But trading card games are non-linear. 

In fact, trading card games take this concept of a non-linear introduction to the extreme. When we design an expansion, we have no idea what order players will see cards in. Any card in the set could be the first thing a player sees. Think of it this way: Imagine that each player kept a list of the order that they experienced the cards in *Mirrodin*. Each player's list would be like a snowflake with its own unique pattern. Each player has their own unique introduction to *Mirrodin*. This huge variance of integration is a very important concept of trading card game design because we, as designers, have to be able to create a game that can be viewed in any order. And it is the impetus of my column today.

“Trading card games take the concept of a non-linear introduction to the extreme…”

So, to give you a better understanding of the non-linear experience, I've decided to write a non-linear column. What does that mean? I'll explain. This article is a collection of mini articles strung together by hyperlinks. That is, words and phrases in each section will connect to other sections. As most sections will have multiple links, the reader will have options of how they will read/explore the article. And the capper is that each reader will start by being randomly inserted into the article. This means that each reader should have their own unique experience reading this column. And don't worry, the column will come to an end. (Although not every reader will have the same ending.)

Finally, I'm hoping to use my column today to explain a question I'm often asked. Just as I used [my choose-your-own-adventure column](https://web.archive.org/web/20040209000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=mtgcom/daily/mr58) to answer “What is it like to work in R&D?”, today's column answers “How does a designers' mind work?” Now, every designer is different, so I can only give you a glimpse into how my mind works. And be warned, it can be a little scary. You see, one of the hallmarks of creativity is the ability to link things together that others don't. Today's column will give you an idea of how a creative mind jumps around from idea to idea. 

If you haven't quit yet, you're in for some fun. I can honestly say that this is something you won't soon forget. So kick back and enjoy the ride. When you're ready hit the link below. 

[Let's get this column started](https://web.archive.org/web/20040209000000/http://archive.wizards.com/Magic/Magazine/Article.aspx?x=magic/mr110.asp).
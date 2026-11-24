---
id: stw7ctc2
kind: event
lang: en
path: /en/events/2015/gpflo15/quick-questions-4
title: 'QUICK QUESTIONS #4'
published: '2015-05-17'
column_slug: null
column: null
authors: []
event_code: gpflo15
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
    lang_detected: en
    capture_id: 49130
    url: https://magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
    captured_at: '2022-06-25 03:05:13+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
    lang_detected: en
    capture_id: 49130
    url: https://magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
    captured_at: '2022-06-25 03:05:13+00'
    rule: drupal.posted_in_date
  event_code:
    page_key: magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
    lang_detected: en
    capture_id: 49130
    url: https://magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
    captured_at: '2022-06-25 03:05:13+00'
    rule: url.event_code
sources:
- document_id: stw7ctc2
  url: https://magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
  page_key: magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
  lang: en
  template: drupal
  captured_at: '2022-06-25 03:05:13+00'
  capture_id: 49130
  wayback_url: https://web.archive.org/web/20220625030513id_/https://magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: stw7ctc2
  capture_id: 49130
  url: https://magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
  wayback_url: https://web.archive.org/web/20220625030513id_/https://magic.wizards.com/en/events/coverage/gpflo15/quick-questions-4-2015-05-17
  captured_at: '2022-06-25 03:05:13+00'
  template: drupal
  sha256: 0fc9a0694f6cd08549ad50f8919a5a827c81cf9f9248dddd2ac22b5ef480e71a
render_recovery: []
---
Early on Saturday, we took to Twitter and asked people for suggestions for quick questions we could ask the pros at this Grand Prix. The yield wasn't particularly big, but a certain someone came up with a question that really intrigued us.

> [@magicprotour](https://twitter.com/magicprotour) If each individual player in your team wins 60% of their matches, what is the probability that your team wins the round? 
> 
> — Frank Karsten (@karsten\_frank) [May 16, 2015](https://twitter.com/karsten_frank/status/599537773641601024)

Here is what our pros came up with ...

 **![](http://media.wizards.com/2015/events/gpflo15/GPFLO15_qq_strasky.jpg)  
 Ondřej Stráský, two time Pro Tour Top 8 competitor:** \[Without knowing who posted the question in the first place.\] "I would ask Frank Karsten!" 

* * *

 **![](http://media.wizards.com/2015/events/gpflo15/GPFLO15_qq_duke.jpg)  
 Reid Duke, No. 21 in the Top 25 Rankings:** \[Took some time to run some calculations in his head ...\] "64.8% of the time!" \[Which is a hundred percent correct.\] 

* * *

 **![](http://media.wizards.com/2015/events/gpflo15/GPFLO15_qq_juza.jpg)  
 Martin Jůza, 22 Grand Prix Top 8s:** \[Making a wild guess ...\] "83.6%!" 

* * *

 **![](http://media.wizards.com/2015/events/gpflo15/GPFLO15_qq_sajgalik.jpg)  
 Eduardo Sajgalik, Top 8 at Grand Prix Milan 2015:** \[Pulled out his notepad, started crunching the numbers, and came up with ...\] "64.8%!" 

* * *

 **![](http://media.wizards.com/2015/events/gpflo15/GPFLO15_qq_mackl.jpg)  
 Valentin Mackl, five Grand Prix Top 8s:** "I don't care. It's over 60%!" 

* * *

 **![](http://media.wizards.com/2015/events/gpflo15/GPFLO15_qq_krautmann.jpg)  
 Wenzel Krautmann, champion of Grand Prix Warsaw 2013:** "I'm a lawyer, not a mathematician! I don't know this stuff." 

* * *

Now you might be interested in a somewhat longer answer, like how to work out the result yourself. We can help you there. When doing probability calculations, there are three simple—well, *simplish*—rules one needs to keep in mind: 

1.  "And" means multiplication. The probability that both thing A *and* thing B will happen, if they are independent, is the probability of A *times* the probability of B.
2.  "Or" means addition. The probability that A *or* B will happen, if they are exclusive, is the probability of A *plus* the probability B.
3.  Very important: You need to account for *all* of the possible combinations that lead to the outcome in question.

Now onto the problem at hand! The answer could be given in the following form: It's the probability that your team wins the first *and* the second *and* the third match, *or* wins the first *and* the second match *and* loses the third, *or* wins the first *and* the third match *and* loses the second, *or* wins the second *and* the third match *and* loses the first. 

Translating that into a formula by simply turning every "and" into a multiplication and exchanging every "or" for a plus sign, we get:

0.6 × 0.6 × 0.6 + 0.6 × 0.6 × 0.4 + 0.6 × 0.6 × 0.4 + 0.6 × 0.6 × 0.4 = 0.648

Q.E.D.

*   [Complete coverage of Grand Prix Florence](https://web.archive.org/web/20150517000000/https://magic.wizards.com/node/384351)
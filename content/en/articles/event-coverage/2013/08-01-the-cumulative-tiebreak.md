---
id: 9mxff2qf
kind: event
lang: en
path: /en/articles/event-coverage/2013/08-01-the-cumulative-tiebreak
title: The Cumulative Tiebreak
published: '2013-08-01'
column_slug: event-coverage
column: Event Coverage
authors: []
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
    lang_detected: en
    capture_id: 337488
    url: https://magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
    captured_at: '2022-05-29 06:29:30+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
    lang_detected: en
    capture_id: 337488
    url: https://magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
    captured_at: '2022-05-29 06:29:30+00'
    rule: drupal.posted_in_date
sources:
- document_id: 9mxff2qf
  url: https://magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
  page_key: magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
  lang: en
  template: drupal
  captured_at: '2022-05-29 06:29:30+00'
  capture_id: 337488
  wayback_url: https://web.archive.org/web/20220529062930id_/https://magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 9mxff2qf
  capture_id: 337488
  url: https://magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
  wayback_url: https://web.archive.org/web/20220529062930id_/https://magic.wizards.com/en/articles/archive/event-coverage/cumulative-tiebreak-2013-08-01
  captured_at: '2022-05-29 06:29:30+00'
  template: drupal
  sha256: 8cab8fb036c13027235dbd50f1bb781a318a2c537f65c726b715bb3176f6fbb6
render_recovery: []
---
The cumulative tiebreak is a formula that mathematically produces the following result – the player (or team) who most recently had more points after a round wins the tiebreak.

To break ties between players with the same number of points, look back to the last time they did not have the same number of points. Whoever’s total was higher at that point will have a higher tiebreaker. The results of a player’s previous round opponents does not have an effect on the cumulative tiebreak.

This also means that if player A has lower tiebreakers than player B, player A can never pass player B unless they end a round with more points.

Here is the formula used to calculate the tiebreaker every round.

 

 

<table><tbody><tr><td>Current Round<br>Tiebreaker</td>&#10;			<td>=</td>&#10;			<td>Previous Round Tiebreaker<br><hr><br>&#10;				4&#10;			</td>&#10;			<td>+</td>&#10;			<td>Current Match<br>Point Total</td>&#10;		</tr></tbody></table>

**Example:**

<table><tbody><tr><td>Round</td>&#10;			<td>Points Earned In Round</td>&#10;			<td>Previous Round Cumulative Tiebreaker</td>&#10;			<td>Match Point Total at Round End</td>&#10;			<td>Current Tiebreaker</td>&#10;		</tr><tr><td>1</td>&#10;			<td>0 (Lose)</td>&#10;			<td>0.000000</td>&#10;			<td>0</td>&#10;			<td>0.000000</td>&#10;		</tr><tr><td>2</td>&#10;			<td>3 (Win)</td>&#10;			<td>0.000000</td>&#10;			<td>3</td>&#10;			<td>3.000000</td>&#10;		</tr><tr><td>3</td>&#10;			<td>1 (Draw)</td>&#10;			<td>3.000000</td>&#10;			<td>4</td>&#10;			<td>4.750000</td>&#10;		</tr><tr><td>4</td>&#10;			<td>3 (Win)</td>&#10;			<td>4.750000</td>&#10;			<td>7</td>&#10;			<td>8.187500</td>&#10;		</tr><tr><td>5</td>&#10;			<td>0 (Lose)</td>&#10;			<td>8.187500</td>&#10;			<td>7</td>&#10;			<td>9.046875</td>&#10;		</tr></tbody></table>

 

For round four, below is an example of us calculating it out so you can see where 8.1875 comes from.

 

 

<table><tbody><tr><td>Current Round<br>&#10;			Tiebreaker</td>&#10;			<td>=</td>&#10;			<td>&#10;				Previous Round Tiebreaker<br><hr><br>&#10;				4&#10;			</td>&#10;			<td>+</td>&#10;			<td>Current Match<br>&#10;			Point Total</td>&#10;		</tr></tbody></table>

 

 

<table><tbody><tr><td>8.187500</td>&#10;			<td>=</td>&#10;			<td>&#10;				4.750000<br><hr><br>&#10;				4&#10;			</td>&#10;			<td>+</td>&#10;			<td>7</td>&#10;		</tr></tbody></table>
---
id: zebb4f19
kind: article
lang: en
path: /en/articles/feature/2013/08-01-the-cumulative-tiebreak
title: The Cumulative Tiebreak
published: '2013-08-01'
column_slug: feature
column: Feature
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
    lang_detected: en
    capture_id: 273001
    url: https://magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
    captured_at: '2021-12-06 00:43:44+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
    lang_detected: en
    capture_id: 273001
    url: https://magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
    captured_at: '2021-12-06 00:43:44+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
    lang_detected: en
    capture_id: 273001
    url: https://magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
    captured_at: '2021-12-06 00:43:44+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
    lang_detected: en
    capture_id: 273001
    url: https://magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
    captured_at: '2021-12-06 00:43:44+00'
    rule: drupal.posted_in_link
    registry_match: registry.explicit
sources:
- document_id: zebb4f19
  url: https://magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
  page_key: magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
  lang: en
  template: drupal
  captured_at: '2021-12-06 00:43:44+00'
  capture_id: 273001
  wayback_url: https://web.archive.org/web/20211206004344id_/https://magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: zebb4f19
  capture_id: 273001
  url: https://magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
  wayback_url: https://web.archive.org/web/20211206004344id_/https://magic.wizards.com/en/articles/archive/cumulative-tiebreak-2013-08-01
  captured_at: '2021-12-06 00:43:44+00'
  template: drupal
  sha256: 24e7b2476e2f7ecf2ffc1ce27c79bd8e87bc1f20503379b2302d5ffbdb834701
render_recovery: []
---
The cumulative tiebreak is a formula that mathematically produces the following result – the player (or team) who most recently had more points after a round wins the tiebreak.

To break ties between players with the same number of points, look back to the last time they did not have the same number of points. Whoever’s total was higher at that point will have a higher tiebreaker. The results of a player’s previous round opponents does not have an effect on the cumulative tiebreak.

This also means that if player A has lower tiebreakers than player B, player A can never pass player B unless they end a round with more points.

Here is the formula used to calculate the tiebreaker every round.

**Current Round Tiebreaker = (Previous Round Tiebreaker / 4) + Current Match Point Total**

******Example:******

<table><tbody><tr><td><b><b>Round</b></b></td>&#10;			<td><b><b>Points Earned In Round</b></b></td>&#10;			<td><b><b>Previous Round Cumulative Tiebreaker</b></b></td>&#10;			<td><b><b>Match Point Total at Round End</b></b></td>&#10;			<td><b><b>Current Tiebreaker</b></b></td>&#10;		</tr><tr><td><b><b>1</b></b></td>&#10;			<td><b><b>0 (Lose)</b></b></td>&#10;			<td><b><b>0.000000</b></b></td>&#10;			<td><b><b>0</b></b></td>&#10;			<td><b><b>0.000000</b></b></td>&#10;		</tr><tr><td><b><b>2</b></b></td>&#10;			<td><b><b>3 (Win)</b></b></td>&#10;			<td><b><b>0.000000</b></b></td>&#10;			<td><b><b>3</b></b></td>&#10;			<td><b><b>3.000000</b></b></td>&#10;		</tr><tr><td><b><b>3</b></b></td>&#10;			<td><b><b>1 (Draw)</b></b></td>&#10;			<td><b><b>3.000000</b></b></td>&#10;			<td><b><b>4</b></b></td>&#10;			<td><b><b>4.750000</b></b></td>&#10;		</tr><tr><td><b><b>4</b></b></td>&#10;			<td><b><b>3 (Win)</b></b></td>&#10;			<td><b><b>4.750000</b></b></td>&#10;			<td><b><b>7</b></b></td>&#10;			<td><b><b>8.187500</b></b></td>&#10;		</tr><tr><td><b><b>5</b></b></td>&#10;			<td><b><b>0 (Lose)</b></b></td>&#10;			<td><b><b>8.187500</b></b></td>&#10;			<td><b><b>7</b></b></td>&#10;			<td><b><b>9.046875</b></b></td>&#10;		</tr></tbody></table>

****For round four, below is an example of us calculating it out so you can see where 8.1875 comes from.****

******Current Round Tiebreaker = (Previous Round Tiebreaker / 4) + Current Match Point Total******

 

******8.187500 = (4.750000 / 4) + 7******
---
id: mxdggzyx
kind: event
lang: en
path: /en/events/2013/wc13/the-cumulative-tiebreak
title: The Cumulative Tiebreak
published: '2013-08-01'
column_slug: null
column: null
authors: []
event_code: wc13
detected_lang: en
metadata_evidence:
  title:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
    lang_detected: en
    capture_id: 556354
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
    captured_at: '2013-09-17 20:57:43+00'
    rule: aspx.article_heading
  published:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
    lang_detected: en
    capture_id: 556354
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
    captured_at: '2013-09-17 20:57:43+00'
    rule: aspx.byline_date
  event_code:
    page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
    lang_detected: en
    capture_id: 556354
    url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
    captured_at: '2013-09-17 20:57:43+00'
    rule: url.event_code
sources:
- document_id: mxdggzyx
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
  lang: en
  template: aspx
  captured_at: '2013-09-17 20:57:43+00'
  capture_id: 556354
  wayback_url: https://web.archive.org/web/20130917205743id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: mxdggzyx
  capture_id: 556354
  url: http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
  wayback_url: https://web.archive.org/web/20130917205743id_/http://www.wizards.com/magic/magazine/article.aspx?x=mtg/daily/eventcoverage/wc13/tiebreakers
  captured_at: '2013-09-17 20:57:43+00'
  template: aspx
  sha256: 351008ab564eba56f7ee0a62577ba485bd3600160d4267f17fe7a69b8859d1a6
render_recovery: []
---
The cumulative tiebreak is a formula that mathematically produces the following result – the player (or team) who most recently had more points after a round wins the tiebreak.

To break ties between players with the same number of points, look back to the last time they did not have the same number of points. Whoever’s total was higher at that point will have a higher tiebreaker. The results of a player’s previous round opponents does not have an effect on the cumulative tiebreak.

This also means that if player A has lower tiebreakers than player B, player A can never pass player B unless they end a round with more points. 

Here is the formula used to calculate the tiebreaker every round.

  

<table>&#10;    <tbody><tr>&#10;      <td>Current Round <br> Tiebreaker</td>&#10;      <td>=</td>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>Previous Round Tiebreaker</td>&#10;          </tr>&#10;          <tr>&#10;            <td>&#10;              <hr>&#10;            </td>&#10;          </tr>&#10;          <tr>&#10;            <td>4</td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;      <td> + </td>&#10;      <td>Current Match <br> Point Total</td>&#10;    </tr>&#10;  </tbody></table>

**Example:** 

<table>&#10;  <tbody><tr>&#10;    <td>Round</td>&#10;    <td>Points Earned In Round</td>&#10;    <td>Previous Round Cumulative Tiebreaker</td>&#10;    <td>Match Point Total at Round End</td>&#10;    <td>Current Tiebreaker</td>&#10;  </tr>&#10;  <tr>&#10;    <td>1</td>&#10;    <td>0 (Lose)</td>&#10;    <td>0.000000</td>&#10;    <td>0</td>&#10;    <td>0.000000</td>&#10;  </tr>&#10;  <tr>&#10;    <td>2</td>&#10;    <td>3 (Win)</td>&#10;    <td>0.000000</td>&#10;    <td>3</td>&#10;    <td>3.000000</td>&#10;  </tr>&#10;  <tr>&#10;    <td>3</td>&#10;    <td>1 (Draw)</td>&#10;    <td>3.000000</td>&#10;    <td>4</td>&#10;    <td>4.750000</td>&#10;  </tr>&#10;  <tr>&#10;    <td>4</td>&#10;    <td>3 (Win)</td>&#10;    <td>4.750000</td>&#10;    <td>7</td>&#10;    <td>8.187500</td>&#10;  </tr>&#10;  <tr>&#10;    <td>5</td>&#10;    <td>0 (Lose)</td>&#10;    <td>8.187500</td>&#10;    <td>7</td>&#10;    <td>9.046875</td>&#10;  </tr>&#10;</tbody></table>

  

For round four, below is an example of us calculating it out so you can see where 8.1875 comes from.

  

<table>&#10;    <tbody><tr>&#10;      <td>Current Round <br> Tiebreaker</td>&#10;      <td>=</td>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>Previous Round Tiebreaker</td>&#10;          </tr>&#10;          <tr>&#10;            <td>&#10;              <hr>&#10;            </td>&#10;          </tr>&#10;          <tr>&#10;            <td>4</td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;      <td> + </td>&#10;      <td>Current Match <br> Point Total</td>&#10;    </tr>&#10;  </tbody></table>

  

<table>&#10;    <tbody><tr>&#10;      <td>8.187500</td>&#10;      <td>=</td>&#10;      <td>&#10;        <table>&#10;          <tbody><tr>&#10;            <td>4.750000</td>&#10;          </tr>&#10;          <tr>&#10;            <td>&#10;              <hr>&#10;            </td>&#10;          </tr>&#10;          <tr>&#10;            <td>4</td>&#10;          </tr>&#10;        </tbody></table>&#10;      </td>&#10;      <td> + </td>&#10;      <td>7</td>&#10;    </tr>&#10;  </tbody></table>
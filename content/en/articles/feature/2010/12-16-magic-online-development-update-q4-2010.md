---
id: gva9kthn
kind: article
lang: en
path: /en/articles/feature/2010/12-16-magic-online-development-update-q4-2010
title: Magic Online Development Update Q4 2010
published: '2010-12-16'
column_slug: feature
column: Feature
authors:
- slug: wizardsofthecoast
  name: Wizards of the Coast
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
    lang_detected: en
    capture_id: 642325
    url: https://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
    captured_at: '2022-05-18 15:39:17+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
    lang_detected: en
    capture_id: 642325
    url: https://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
    captured_at: '2022-05-18 15:39:17+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
    lang_detected: en
    capture_id: 642325
    url: https://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
    captured_at: '2022-05-18 15:39:17+00'
    rule: drupal.div_author
  column:
    page_key: magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
    lang_detected: en
    capture_id: 642325
    url: https://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
    captured_at: '2022-05-18 15:39:17+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: gva9kthn
  url: https://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
  page_key: magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
  lang: en
  template: drupal
  captured_at: '2022-05-18 15:39:17+00'
  capture_id: 642325
  wayback_url: https://web.archive.org/web/20220518153917id_/https://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
- document_id: gva9kthn
  url: http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/12162010d
  page_key: wizards.com/magic/magazine/article.aspx?x=mtg/daily/other/12162010d
  lang: en
  template: aspx
  captured_at: '2013-06-29 09:53:13+00'
  capture_id: 667492
  wayback_url: https://web.archive.org/web/20130629095313id_/http://www.wizards.com/Magic/Magazine/Article.aspx?x=mtg/daily/other/12162010d
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: gva9kthn
  capture_id: 642325
  url: https://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
  wayback_url: https://web.archive.org/web/20220518153917id_/https://magic.wizards.com/en/articles/archive/feature/magic-online-development-update-q4-2010-2010-12-16
  captured_at: '2022-05-18 15:39:17+00'
  template: drupal
  sha256: 7b56c54b96678d6f878363264353b8b99ea2f943ba3b16e71adade226c8dea87
render_recovery: []
---
**Summary**  
 Construction of the new ****Magic Online**** client is running full-bore, and we are targeting late Q1 2011 for a game play beta focused on the new 2-player duel scene. A beta for the full client would follow when all the scenes have finished construction. We continue to work on infrastructure improvements in order to ensure continued system stability. We are starting to take on feature development projects in addition to the infrastructure updates. The system is continuing to perform well as the user base expands. 

**New Client**  
 The new client is being built using Windows Presentation Foundation (WPF). WPF was our chosen platform when the design project began. We explored using Silverlight in the hopes of opening up more access to **Magic Online**. In the end, we were unable to find realistic solutions for several issues relating to integrating a Rich Internet Application with our server infrastructure. The shared design environment for WPF and Silverlight means that very little design time was lost in that exploration process. WPF will offer rapid entry into **Magic Online** for new and existing players with a much lighter install and launch process. WPF provides a richer set of user controls, which is helpful to providing a solid user experience. The platform will allow us to respond rapidly to usability findings. WPF also provides very good support for QA testing.

**Infrastructure Update**  
 Our next major infrastructure project will be to deserialize all of the digital objects. Currently the system stores all digital objects individually in the database as part of the original system design. The system currently does not use the serialization, and stacking like digital objects will further reduce the risk of contention in the database. As this is implemented, we will move away from having to ‘print’ collated product such as boosters and store them in the database. This eliminates the possibility of ‘running out’ of a certain class of product. All of these changes will significantly improve the scalability of the greater system, reduce maintenance downtime, and will improve usability. 

**Q4 Maintenance**  
 The single managed connection module that shipped in September has given us a lot of information about the primary issues that users have been reporting. Logging was significantly improved with that module, and we have been able to isolate the majority of the most reported issues to problems with temporary state management in the client. Our client devs are intensly focused on supporting the new client, so we have chosen to take some aggressive action to solve the current client’s bad behavior on logoff and disconnects. We realize this is less than ideal for a subset of users, but we feel that it is a net gain for those folks who previously were having issues with empty sideboards and not reconnecting to drafts after disconnections.

**2011 Development Plan** 

*   Deliver card set releases
*   WPF Client
*   Alternate Entry Fees
*   Stacked Digital Objects
*   Real-time Collation
*   Multiplayer Support – Improved player management, new multiplayer duel scene in the WPF client.
*   Leagues – Chris (WotC\_K) will talk more about Leagues in Q1 2011. Internal project name = Sandwiches.
*   Additional Features – announcement and details in Q2

Gordon Culp  
 Director – Game Systems Design  
**Magic: The Gathering** Digital Studio  
 Wizards of the Coast, LLC  

*   **[Discuss on the message boards.](https://web.archive.org/web/20101216000000/http://community.wizards.com/go/thread/view/75846/26468501/Q4_2010_Development_Update_Discussion)**
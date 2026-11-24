---
id: ww32dhw4
kind: article
lang: en
path: /en/articles/magiconline/2014/08-28-magic-online-announcements-august-28-2014-client-stability-update
title: 'Magic Online Announcements August 28, 2014: Client Stability Update'
published: '2014-08-28'
column_slug: magiconline
column: Magic Online
authors:
- slug: david-whitfield-21ba2ba3
  name: David Whitfield
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
    lang_detected: en
    capture_id: 778593
    url: https://magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
    captured_at: '2021-10-24 15:05:04+00'
    rule: meta.og_title
  published:
    page_key: magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
    lang_detected: en
    capture_id: 778593
    url: https://magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
    captured_at: '2021-10-24 15:05:04+00'
    rule: drupal.posted_in_date
  authors:
    page_key: magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
    lang_detected: en
    capture_id: 778593
    url: https://magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
    captured_at: '2021-10-24 15:05:04+00'
    rule: drupal.div_author
sources:
- document_id: ww32dhw4
  url: https://magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
  page_key: magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
  lang: en
  template: drupal
  captured_at: '2021-10-24 15:05:04+00'
  capture_id: 778593
  wayback_url: https://web.archive.org/web/20211024150504id_/https://magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: ww32dhw4
  capture_id: 778593
  url: https://magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
  wayback_url: https://web.archive.org/web/20211024150504id_/https://magic.wizards.com/en/articles/archive/magic-online-announcements-august-28-2014-client-stability-update-2014-08-28
  captured_at: '2021-10-24 15:05:04+00'
  template: drupal
  sha256: c2e13325fe1ade8254f3fc8ac55626cb9c7347d8580ba06e124c45929d6db333
render_recovery: []
---
Addressing *Magic Online* Client Stability Issues

 

![](https://i.ormos.uk/c1/b8/c1b82f080e43d3a69425d7d3b42a563fd2546fe0767aca184f56f5912c86d913.png)

This morning, we have deployed an update to the *Magic Online* client. When you start *Magic Online*, the update will automatically download. This update fixes two issues involving trading that were introduced with the [8/20 update](/en/articles/magiconline/2014/08-19-magic-online-announcements-august-19-2014).

The first item addressed was fixing the performance and crashing issues whenever a player interacted in a trade with a trade partner with a large amount of cards. The second item addressed was a crash caused by using the color filters during a trade.

While both of the above items will be resolved with this update, we also want to highlight a known issue so that players are aware while we continue to work to address it. The known issue occurs while in a trade, after you drag and drop cards into the "You Will Receive" pane, the quantity in the "Matches" pane does not update to reflect the drag and drop, then you drag those same cards into the "You Will Receive pane again," a crash will occur. You can avoid this crash by using the right-click context menu instead to move the cards, double-clicking to move the cards, or by not double drag and dropping the same card selection multiple times. While these steps will help avoid the issue in the short-term, we are looking to fix this issue in an upcoming release.

**Build Notes (Download required):**

*   Fixed: Trading with a user with a large amount of cards in their binder will no longer cause performance and crash issues.
*   Fixed: Attempting a trade while using the color filters feature will no longer cause a crash.
*   Known Issue: Dragging and dropping cards into the "You Will Receive" area during a trade will not properly update the quantity owned field. If you drag and drop cards you don't own, via repeated drag actions, this will cause a crash.
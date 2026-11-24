---
id: xvy9xen8
kind: article
lang: ja
path: /ja/articles/youmakethecard2/2003/02-28-you-make-the-card-2-step-3
title: 第２回「カードを作るのは君だ！」
published: '2003-02-28'
column_slug: youmakethecard2
column: You Make the Card 2
authors:
- slug: markrosewater
  name: Mark Rosewater
translation_of: 3vta0pme
detected_lang: ja
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/feature/135
    lang_detected: ja
    capture_id: 2008214
    url: http://www.wizards.com/default.asp?x=mtgcom/feature/135,,ja
    captured_at: '2004-11-20 20:42:31+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/feature/135
    lang_detected: ja
    capture_id: 2008214
    url: http://www.wizards.com/default.asp?x=mtgcom/feature/135,,ja
    captured_at: '2004-11-20 20:42:31+00'
    rule: registry.known_article
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/feature/135
    lang_detected: ja
    capture_id: 2008214
    url: http://www.wizards.com/default.asp?x=mtgcom/feature/135,,ja
    captured_at: '2004-11-20 20:42:31+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/feature/135
    lang_detected: ja
    capture_id: 2008214
    url: http://www.wizards.com/default.asp?x=mtgcom/feature/135,,ja
    captured_at: '2004-11-20 20:42:31+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: xvy9xen8
  url: http://www.wizards.com/default.asp?x=mtgcom/feature/135,,ja
  page_key: wizards.com/default.asp?x=mtgcom/feature/135
  lang: ja
  template: classic_asp
  captured_at: '2004-11-20 20:42:31+00'
  capture_id: 2008214
  wayback_url: https://web.archive.org/web/20041120204231id_/http://www.wizards.com/default.asp?x=mtgcom/feature/135,,ja
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: xvy9xen8
  capture_id: 2008214
  url: http://www.wizards.com/default.asp?x=mtgcom/feature/135,,ja
  wayback_url: https://web.archive.org/web/20041120204231id_/http://www.wizards.com/default.asp?x=mtgcom/feature/135,,ja
  captured_at: '2004-11-20 20:42:31+00'
  template: classic_asp
  sha256: 8d15e795f49d4bc688cba0bf5dcbc01837358a5754da96ca5a42aae7b3106e4d
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Mirari')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Mirari
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Cursed[Scroll')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Cursed Scroll
  occurrences: 1
- code: unsupported_link
  element: a
  target: javascript:void(0)
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - 今すぐ投票を！
  occurrences: 1
---
* * *

　第１回「カードを作るのは君だ！」では、多数が選んだのはクリーチャーでした。

　この話はもういいって？

　さて今回、みなさんが選んだのは――大差をつけて――クリーチャーでないアーティファクトです。

<table><tbody><tr><td><b>クリーチャーでないアーティファクト</b></td>&#10;<td><b>9484</b></td>&#10;<td><b>68.1%</b></td>&#10;</tr>&#10;<tr><td>アーティファクト・クリーチャー</td>&#10;<td>4439</td>&#10;<td>31.9%</td>&#10;</tr>&#10;<tr><td><b>合計</b></td>&#10;<td><b>13923</b></td>&#10;<td><b>100.0%</b></td>&#10;</tr>&#10;</tbody></table>

　それではこの結果を受けて、デザインの次の段階に進むとしましょう。しかしここは分かれ道です。あなたの目の前には、マジックのカードを作る２つの方法への道が開いています。その一方はイメージ先行、もう一方は機能先行です。

![right](https://i.ormos.uk/3e/98/3e98d4085759f3cbb14de80ecedcf5a8e724b8a38eece1e7d25361af93c59764.jpg)

### イメージ先行

　私たちはこの方法を“トップダウン”デザインと呼んでいます。このやり方では、まずいい感じのアーティファクトのイメージを決め、その後、そのアーティファクトはどんな物でどういう働きをするかを考え、それにマッチするメカニズムをデザインするのです。《ミラーリ/Mirari》はこの“トップダウン”デザインのアーティファクトの一例です。ストーリーの中で、それを使う者のパワーを増大する丸い鏡のような球体が登場することになりました。オデッセイのデザインチームは、その能力をいかにしてゲーム上での面白い能力に翻案するかに頭を悩ませたのです。

　この方法の利点は、アーティファクトのイメージが実に奥深いものになることです。欠点は、メカニズムに対する制限が非常に厳しくなることでしょう。

### 機能先行

　このデザインの方法では、まずカードがゲームでどういった動きをするかを決めます。そのメカニズムが決まったら、私たちはそれにふさわしいイメージを与えてやるのです。例えば、《呪われた巻物/Cursed Scroll》は、このやりかたでまずメカニズムが作られ、その後クリエイティブ・チームによってイメージが与えられたものです。

　この方法の利点は、デザイナーにとって自由にメカニズムを考えられるということです。欠点は、そのメカニズムにぴったり来るイメージを作り出すのが非常に難しいということでしょう。さらに、このやり方は第１回の「カードを作るのは君だ！」で採られた方法です。このイベントの目的の一つには、みなさんに様々なタイプのデザインに触れる機会を持ってもらおうということにあります。したがって、二つ目の欠点は、この方法だと前回と同じカードのデザインのやり方になってしまうということでしょう。

　さて、あなたの選択は、 イメージ（Flavor）先行？ それとも機能（Function）先行？

　投票は今日から、３月９日（日）の24:00まで（太平洋標準時）です。

　あなたがどちらを選ぶか、非常に興味深く見守らせてもらうとしましょう。

　今すぐ投票を！
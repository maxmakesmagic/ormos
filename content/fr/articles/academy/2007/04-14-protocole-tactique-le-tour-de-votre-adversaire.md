---
id: s1pgmmjv
kind: article
lang: fr
path: /fr/articles/academy/2007/04-14-protocole-tactique-le-tour-de-votre-adversaire
title: 'Protocole tactique : Le tour de votre adversaire'
published: '2007-04-14'
column_slug: academy
column: Magic Academy
authors:
- slug: jeffcunningham
  name: Jeff Cunningham
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/academy/33
    lang_detected: fr
    capture_id: 1846787
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/33
    captured_at: '2008-05-19 08:03:08+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/academy/33
    lang_detected: fr
    capture_id: 1846787
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/33
    captured_at: '2008-05-19 08:03:08+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/academy/33
    lang_detected: fr
    capture_id: 1846787
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/33
    captured_at: '2008-05-19 08:03:08+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/academy/33
    lang_detected: fr
    capture_id: 1846787
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/33
    captured_at: '2008-05-19 08:03:08+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: s1pgmmjv
  url: http://www.wizards.com/default.asp?x=mtgcom/academy/33
  page_key: wizards.com/default.asp?x=mtgcom/academy/33
  lang: fr
  template: classic_asp
  captured_at: '2008-05-19 08:03:08+00'
  capture_id: 1846787
  wayback_url: https://web.archive.org/web/20080519080308id_/http://www.wizards.com/default.asp?x=mtgcom/academy/33
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: s1pgmmjv
  capture_id: 1846787
  url: http://www.wizards.com/default.asp?x=mtgcom/academy/33
  wayback_url: https://web.archive.org/web/20080519080308id_/http://www.wizards.com/default.asp?x=mtgcom/academy/33
  captured_at: '2008-05-19 08:03:08+00'
  template: classic_asp
  sha256: 49251d5956e3b21a54f86f087fd58b39b3086ba1127a27407e694a51fe7f7b65
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Orim[s_Chant')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Sudden_Impact')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Krosan_Grip')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Angelic_Page')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Lightning_Blast')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Fortify')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Nantuko_Husk')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Fellwar_Stone')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Fact_or_Fiction')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
* * *

![Headlong_Rush](https://i.ormos.uk/8a/31/8a31beac21beef046de62dfa7f24c76d64ccf3bc796a8c7ac46eb930067bcd01.jpg)

Salut tout le monde, et bienvenue à Magic Academy ! Cette semaine, nous continuons d'étudier les aspects techniques du timing : en gros, quand jouer des sorts et des effets, et pourquoi à un moment précis plutôt qu’un autre. [La semaine dernière](/en/articles/academy/2007/04-07-tactical-protocol-your-own-turn) nous avons étudié les options de votre propre tour ; cette semaine, nous allons détailler les difficultés de timing pendant le tour de votre adversaire.

N'oubliez pas, pendant le tour de votre adversaire, c'est lui qui a la priorité. En gros, cela veut dire qu'il a la possibilité de faire des choses en premier (mais vous pouvez y répondre immédiatement). C'est souvent un avantage. Il doit prendre des décisions sans savoir si vous avez l'intention de jouer quelque chose. Si vous choisissez de ne rien faire une fois qu'il a passé, l'étape se termine.

### Le tour de votre adversaire

*Quand initialiser des sorts et pourquoi* 

**1\. Phase de début**

**Étape de dégagement :** Tous les permanents engagés de votre adversaire se dégagent. Rien ne peut être joué pendant cette étape.

**Étape d'entretien :** Aspect tactique le plus important de l'étape d'entretien de votre adversaire : elle se déroule après son dégagement, mais avant sa pioche. C'est aussi votre première occasion de jouer un sort ou une capacité pendant son tour. 

Généralement, si votre adversaire a engagé tout son mana pendant votre tour et qu'il est important que vous résolviez un sort, il vaut mieux le faire pendant votre tour. S'il a déjà des permanents appropriés (généralement des terrains) qui sont dégagés, vous devriez peut-être attendre son entretien. Ainsi, s'il répond, il devra engager des permanents qu'il aurait pu utiliser autrement pendant son tour.

*   **Liés au tour de l'adversaire :** C'est la première phase du tour de votre adversaire. Si vous avez un sort qui doit tout particulièrement être joué pendant le tour de votre adversaire pour être utile, c'est souvent le moment idéal.

    <table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Orim's Chant" src="https://i.ormos.uk/39/df/39df0b1948489c7bf790d2bce95c6278317e33fc8bc907756c27874ee9852bd5.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

    *Exemple* : Pendant mon entretien, vous jouez le Cantique selon Orime.

*   **Liés au manque de mana :** De même, si vous avez des effets qui engagent les sources de mana de l'adversaire, c'est généralement le bon moment pour les jouer. Certes, il peut utiliser le mana pour des sorts pendant sa phase de début, mais pas pour les non-éphémères.

    *Exemple* : Pendant mon entretien, vous activez votre Manipulateur glacial en ciblant mon île.

*   **Liés à un effet d'entretien :** Comme pendant votre propre tour, il est parfois important de naviguer avec différents effets d'entretien.

    *Exemple* : Je vous lance un Choc afin de vider ma main pour un Animal imaginaire. Avant la résolution de sa capacité, vous jouez un Boomerang sur mon île.

  

**Étape de pioche :** Aspect tactique le plus important de l'étape de pioche de votre adversaire : elle se déroule après sa pioche, mais avant qu'il ne puisse initialiser des sorts non-éphémères. [\*](#footnote1)

*   **Liés à la taille de la main :** Si l'utilité d'une carte dépend du nombre de cartes dans la main de votre adversaire, c'est peut-être le bon moment de la jouer.

    <table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Sudden Impact" src="https://i.ormos.uk/c4/b1/c4b1348fc769d29c4d30512f530bede5a993373f5d70c31f6da27d3a659555ee.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

    *Exemple* : Pendant mon étape de pioche, vous me ciblez avec un Choc soudain.

    *Exemple* : Je n'ai pas de carte en main, et je pioche pour mon tour. Pendant mon étape de pioche, vous me ciblez avec la capacité de défausse du Charme funéraire.

**2\. Phase principale**

Aspect tactique le plus important de la première phase principale de votre adversaire : elle se déroule avant le combat. Il se positionne pour réussir son étape de combat. Vous aurez souvent l'occasion de répondre à ses sorts pendant cette phase.

**3\. Phase de combat**

**Étape de début de combat :** Aspect tactique le plus important de l'étape de début de combat de votre adversaire : elle a lieu après qu'il a pu jouer des non-éphémères, mais avant qu’il ne déclare ses attaquants.

  

*   **Effets d'engagement :** C'est le moment d'engager les attaquants potentiels.

    <table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Krosan Grip" src="https://i.ormos.uk/5d/be/5dbea6daeecc2d2efea07337f8fd21e2001f32d7b05ac0274869bb2f43020dbc.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

    Parfois, vous pouvez le faire pendant l'entretien, ou en réponse à une pioche, au cas où votre adversaire piocherait une carte avec la fraction de seconde (disons, une Poigne krosiane pour votre Manipulateur glacial), un contresort ou un effet affectant la capacité de cibler, mais en général, il vaut mieux attendre le dernier moment pour le faire. Ainsi, vous avez toutes les informations relatives à sa première phase principale pour décider de la meilleure stratégie.

    *Exemple* : Pendant mon étape de début de combat, vous activez un Maître leurreur qui cible mon Dragon shivân.

    *Exemple* : J'ai des Grizzlis en jeu. Je joue un Pisteur des sables viashino, qui a la célérité, et je passe à mon étape de début de combat. Vous activez votre Maître leurreur, ciblant le Pisteur des sables viashino.

**Étape de déclaration des attaquants :** Votre adversaire commence son étape de déclaration des attaquants en décidant quelles créatures vont attaquer et en les engageant. Ensuite, chaque joueur a la possibilité de jouer des sorts et des capacités. Aspect tactique le plus important de l'étape de déclaration des attaquants de votre adversaire : elle a lieu après que votre adversaire a décidé ses attaques, mais avant que vous ayez choisi vos bloqueurs. C'est un moment propice à l'analyse d'informations.

*   **Liés aux informations :** Vous pouvez contraindre votre adversaire à utiliser un sort ou une capacité avant qu'il sache comment vous allez bloquer, ou vérifier qu'un de vos sorts ou capacité se résolve comme vous le voulez avant de faire un blocage.

    *Exemple* : J'ai 2 points de vie et des Grizzlis en jeu. Vous m'attaquez avec un Gobelin enragé et une Guivre vorace — Je fais un Obscur bannissement sur la Guivre vorace avant la déclaration des bloqueurs. Si vous avez un contresort pour sauver la Guivre, je serai forcé de la bloquer, mais au moins, je ne serai pas mort. Dans le cas contraire, j'ai simplement à bloquer le Gobelin enragé.



    <table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Angelic Page" src="https://i.ormos.uk/32/aa/32aa8ec079051b9db145e5840cbd7b563d24d4d4db75844988bac42e0cb80872.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

    *Exemple* : Vous m'attaquez avec deux Géants des collines, et vous avez un Page angélique dégagé. J'ai une Guivre vorace. Je balance un Choc sur votre Page angélique. Je peux ne pas bloquer le Géant des collines que vous boostez et encaisser 4 blessures. Celui que vous ne boostez pas, je peux le tuer avec ma Guivre vorace.

  

**Étape de déclaration des bloqueurs :** Vous commencez cette étape en déclarant quelles créatures vont bloquer mes créatures attaquantes et lesquelles. Ensuite, chaque joueur a la possibilité de jouer des sorts ou des capacités.Aspect tactique le plus important de l'étape de déclaration des bloqueurs du tour de votre adversaire : après que vos bloqueurs ont été déclarés, c'est la dernière étape avant l'attribution des blessures de combat, et votre adversaire a la priorité.

*   **Liés à la force ou l'endurance :** Comme pendant votre propre tour, c'est la dernière occasion de booster (ou d'affaiblir) les créatures avant qu'elles n'infligent leurs blessures. Une fois encore, ces effets incluent les pompes directes (Croissance gigantesque), le retrait (Obscur bannissement) et les effets de réduction (Rétrécissement).

    Il y a cependant quelques différences avec votre propre tour. Vous devez à présent prendre en compte les blessures qui devraient vous être infligées.

    <table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Lightning Blast" src="https://i.ormos.uk/16/7a/167ae477645250504258ef4568c20a323e34dc29b0f4d5785c32e5d931b02788.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

    *Exemple* : Je vous attaque avec deux Guerriers serpentiformes. Vous en bloquez un avec une Guivre vorace, et vous tuez l'autre avec une Salve d'éclair avant que les blessures aillent sur la pile pour ne pas subir 3 blessures.

*   **Appât :** Il faut prendre aussi en considération le fait que votre adversaire a la priorité. Cela veut dire que c'est sa dernière chance de booster ses créatures avant l'attribution des blessures de combat et votre dernière chance de la tuer. Donc, si vous avez l'intention de tuer une créature, et que vous ne pensez pas que votre adversaire a un moyen de l'empêcher, vous devriez attendre le dernier moment pour le contraindre à jouer une ruse potentiellement inutile.

    *Exemple* : Vous avez un Obscur bannissement. Je vous attaque avec une Guivre vorace. Vous bloquez avec un Dragon shivân. Je joue une Croissance gigantesque. Vous jouez un Obscur bannissement.

    *OU*

    Vous avez un Obscur bannissement. Je vous attaque avec une Guivre vorace. Vous bloquez avec un Dragon shivân. Je passe la priorité. Vous jouez un Obscur bannissement.

**Étape d'attribution des blessures de combat :** Au début de l'étape d'attribution des blessures de combat, chaque joueur choisit comment les créatures qu'il contrôle infligent leurs blessures. Si une des créatures a l'initiative, il y a deux étapes d'attribution des blessures de combat distinctes. Aspect tactique le plus important de l'étape d'attribution des blessures de combat de votre adversaire : quasi identique à celui du vôtre ; elle se déroule après l'attribution des blessures de combat, mais c'est la dernière étape avant leur résolution. 

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Fortify" src="https://i.ormos.uk/fd/b2/fdb20198ad3967150fa0b2ba0cd2547cab1b1b2370aa6fda475d96bc2526208d.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

*   **Liés à la prévention :** Une fois de plus, cette catégorie inclut la prévention de blessures directe (Mains réparatrices), les pompes (l'option +0/+2 de Fortifier) et le Rebond (Boomerang). Arrivé à ce point du tour, les pompes ne peuvent plus aider à tuer un attaquant. Le rebond d'une créature adverse n'empêchera pas votre créature de mourir, mais un rebond sur votre créature n'empêchera pas la mort de la créature de l'adversaire.

    De plus, vous avez maintenant une bonne motivation pour jouer des cartes telles que le Jour saint pour empêcher les blessures sur *vous.*

  

*   **Effets de sacrifice :** C'est une situation que j'ai oublié la semaine dernière, mais qui survient tout le temps. Une fois que les blessures sont sur la pile — en attente, que les créatures responsables soient encore en jeu ou non quand elles se résolvent — c'est le moment clé pour sacrifier une créature afin de jouer une capacité spécifique, si la créature est sur le point de mourir.

    *Exemple :* Vous bloquez mon Élémental d’éclair avec des Glob-gnomes. Une fois que les blessures de combat sont sur la pile (pendant l'étape d'attribution des blessures de combat), vous sacrifiez les Glob-gnomes pour gagner 3 points de vie. L'étape se termine et mon Élémental d’éclair meurt.

    Un autre détail à ne pas oublier, c'est que la créature sacrifiée ne subit jamais les blessures. C'est parfois important parce que cela peut affecter les effets et les capacités liés aux blessures de combat.

    <table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Nantuko Husk" src="https://i.ormos.uk/29/6e/296e9f970b88edd5e796876e0922ff09f24c02353e8431127afa502fd009bfaa.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

    *Exemple* : J'attaque avec un Géant des collines équipé d'un Marteau de guerre loxodon. Vous bloquez avec une Carapace de nantuko. J'attribue 2 blessures à la Carapace et 4 blessures de piétinement à vous. Alors que les blessures de combat sont sur la pile, vous sacrifiez la Carapace à sa propre capacité. Pour cette raison, une fois que les blessures se résolvent, je ne gagne que 4 points de vie à la place de 6.

**Étape de fin de combat :** Aspect tactique le plus important de l'étape de fin de combat de votre adversaire : elle a lieu après la résolution des blessures, mais pendant que le combat a techniquement encore lieu. C'est une étape utilisée de manière très irrégulière.

*   **Liés à 'l'après-blessures' :** Parfois, il est important d'attendre la résolution des blessures de combat pour utiliser un effet spécifique au combat (comme celui de la Baliste lourde). Cela empêche à votre adversaire d'avoir la possibilité d'utiliser un effet qui pourrait potentiellement affecter le combat après avoir vu ce que vous faites.

    *Exemple* : Après la résolution des blessures normales, j'utilise les Arbalétriers à pied pour exterminer votre Vigile du sanctuaire. Si je l'avais fait avant la résolution des blessures, vous auriez pu l'utiliser pour prévenir les blessures sur un autre de vos bloqueurs. (Si vous l'utilisez pour prévenir les blessures d'un de vos bloqueurs, je garderai au moins des Arbalétriers dégagés pour plus tard.)

*   **Affecter les sources de mana :** Si le combat se termine et que vous avez des ressources (ou des raisons) supplémentaires d'immobiliser les sources de mana de votre adversaire pour sa deuxième phase principale (et une dernière chance de jouer des non-éphémères avant son prochain tour), c'est le dernier moment où vous pouvez le faire.

    <table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Fellwar Stone" src="https://i.ormos.uk/d2/0c/d20c9e57bfa573f5b99bc21380e9d6598f331b4d0a8bf66ad2a2c91dfee944a3.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

    *Exemple* : Vu comment cette attaque s'est déroulée, ma seule chance de gagner est de jouer un Brasier pour 6 ce tour-ci. J'ai 6 terrains et une Pierre de Guermont en jeu. Vous lancez un Fracasser sur ma Pierre de Guermont pendant mon étape de fin de combat.

**4\. Phase principale (encore)**

Aspect tactique le plus important de la deuxième phase principale de votre adversaire : c'est la phase par défaut pendant laquelle il peut jouer des sorts à vitesse de rituel. Vous allez souvent répondre beaucoup pendant cette phase. En dehors de ça, il est rare d'initialiser des sorts ou des capacités à ce moment du tour.

  

**5\. Phase de fin**

**Étape de fin de tour :** Aspects tactiques les plus importants de l'étape de fin de tour de votre adversaire : sa dernière chance de jouer des non-éphémères ce tour-ci est passée et c'est votre dernière phase avant votre dégagement. Pour cette raison, c'est le moment idéal pour jouer des éphémères et des capacités, et c'est surtout ce à quoi cette phase sert le plus souvent.

*   **Résoudre des capacités inutilisées :** C'est le moment pour vous d'utiliser les capacités renouvelables (liées à l'engagement) que vous n'avez pas encore utilisées.

    *Exemple* : À la fin de mon tour, vous me tapez avec votre Pyromancien sybarite.

    Bien entendu, cela s'applique aussi à l'engagement des terrains.

    <table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Fact or Fiction" src="https://i.ormos.uk/38/1b/381b73ad207922372b69ba27a61ea286a3934cd8d159e20c014aec026805566c.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

    *Exemple*:À la fin de mon tour, comme je n'ai rien joué que vous vouliez contrecarrer, vous utilisez votre terrain pour jouer Fait ou fiction.

*   **Provoquez une bagarre :** C'est le moment idéal pour 'provoquer une bagarre', engager votre adversaire dans une bataille d'éphémères et de capacités (généralement ceux qu'il aura une bonne motivation de combattre). Même si cela se passe mal pour vous, ce n’est pas important parce que vous allez dégager tous vos permanents et commencer une nouvelle 'bagarre' pendant votre tour, alors que votre adversaire sera contraint d’être sur la défensive.

    *Exemple* : À la fin de mon tour, vous jouez Fait ou fiction. Je lui lance une Révocation. Vous faites une Fuite de mana sur ma Révocation. J'engage mes derniers terrains pour balancer une Fuite de mana sur votre Fuite de mana. Vous dégagez à votre prochain tour et vous engagez tout votre mana pour jouer un Dragon shivân.

    *Exemple* : À la fin de mon tour, vous utilisez le Pyromancien sybarite pour taper mon Assassin royal. J'engage un Guérisseur sanctif pour prévenir les blessures. Pendant votre tour, vous utilisez à nouveau le Pyromancien. Cette fois, je ne peux pas prévenir les blessures, et mon Assassin meurt.

**Nettoyage :** C'est le moment où les blessures sont retirées des créatures et que les effets 'jusqu'à la fin du tour' cessent de faire effet. Rien ne peut être joué pendant cette étape.

C'est tout pour cette semaine. Retrouvez-moi la semaine prochaine, et nous examinerons les tactiques de façon plus approfondie…

Jeff

\* Il y a une stratégie qui peut être jouée ici, quand les effets au-dessus-de-la-bibliothèque sont utilisés contre des sources de mana. Je me souviens d'une manœuvre particulièrement délicieuse contre Bill Stead au GP: Nouvelle Orléans il y a quelques années. Je jouais Folie bleu/vert contre son deck combo/créature vert. Pendant son étape de pioche, j'ai ciblé des Elfes de Llanowar avec une Submersion. Comme ça, il ne pouvait pas les piocher ce tour-ci, seulement au tour suivant quand ils seraient moins utiles, et il ne pourrait pas non plus en puiser du mana pour jouer des non-éphémères. C'est un cas extrêmement marginal.
---
id: t2ej507d
kind: article
lang: fr
path: /fr/articles/academy/2006/09-30-introduction-au-tempo
title: Introduction au tempo
published: '2006-09-30'
column_slug: academy
column: Magic Academy
authors:
- slug: tedknutson
  name: Ted Knutson
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/academy/12
    lang_detected: fr
    capture_id: 1846339
    url: http://wizards.com/default.asp?x=mtgcom/academy/12
    captured_at: '2007-10-15 10:35:27+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/academy/12
    lang_detected: fr
    capture_id: 1846339
    url: http://wizards.com/default.asp?x=mtgcom/academy/12
    captured_at: '2007-10-15 10:35:27+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/academy/12
    lang_detected: fr
    capture_id: 1846339
    url: http://wizards.com/default.asp?x=mtgcom/academy/12
    captured_at: '2007-10-15 10:35:27+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/academy/12
    lang_detected: fr
    capture_id: 1846339
    url: http://wizards.com/default.asp?x=mtgcom/academy/12
    captured_at: '2007-10-15 10:35:27+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: t2ej507d
  url: http://wizards.com/default.asp?x=mtgcom/academy/12
  page_key: wizards.com/default.asp?x=mtgcom/academy/12
  lang: fr
  template: classic_asp
  captured_at: '2007-10-15 10:35:27+00'
  capture_id: 1846339
  wayback_url: https://web.archive.org/web/20071015103527id_/http://wizards.com/default.asp?x=mtgcom/academy/12
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: t2ej507d
  capture_id: 1846339
  url: http://wizards.com/default.asp?x=mtgcom/academy/12
  wayback_url: https://web.archive.org/web/20071015103527id_/http://wizards.com/default.asp?x=mtgcom/academy/12
  captured_at: '2007-10-15 10:35:27+00'
  template: classic_asp
  sha256: 6b2ea6920dd08add6b245981adfd3bd862195cc5e82008234256534f5fe14361
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Sluggishness')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Last-Ditch_Effort')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Blood_Clock')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: unsupported_link
  element: a
  target: javascript:void(0)
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - cliquez ici
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Rivalry')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Isamaru,_Hound_of_Konda')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Isamaru, chien de Konda
  occurrences: 2
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Vacuumelt')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Time_Stretch')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Minister_of_Impediments')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Golgari_Brownscale')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Azorius_Ploy')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
* * *

Rebonjour, mes chers élèves, ici le professeur Knutson. Tout comme certains films et certaines chansons, certains cours ont été si bien écrits auparavant qu'il est inutile de les refaire. Il suffit de vous les représenter. Comme nous avons parlé de l'avantage des cartes dans [notre article de la semaine dernière](/en/articles/academy/2006/09-23-introduction-to-card-advantage) (avec d'étonnants commentaires positifs), il m'a paru naturel de discuter de la théorie du tempo cette semaine. L'article rédigé par Scott Johns sur le sujet plus tôt cette année n'est pas seulement récent, mais il est aussi suffisamment compréhensible par des novices tout en ayant suffisamment de détails pour satisfaire la plupart des érudits du jeu. Donc, plutôt que d'essayer de réinventer la roue, je souhaite la bienvenue à M. Johns, notre conférencier invité de la semaine, et je vous laisse entre ses mains.

* * *

![Sluggishness](https://i.ormos.uk/1e/38/1e386da32accea78e463affd5b3cce6eca5c1d3e8b41f7b8377abf42800204a8.jpg)

Ayant joué à ce jeu depuis l'époque d'Arabian Nights et d'Antiquities, ayant affronté les meilleurs joueurs pendant des années sur le Pro Tour et ayant été rédacteur ou producteur d'un site consacré à Magic pendant au moins sept ans si l'on compte Mindripper, Brainburst, et **magicthegathering.com**, je pense qu'on peut dire que j'ai lu *énormément* d'articles stratégiques sur Magic. Les meilleurs d'entre eux m'ont ouvert l'esprit à différents aspects du jeu que j'avais mal interprétés ou tout simplement peu appréciés. Malgré tous les articles parus pendant toutes ces années, il reste un aspect majeur encore grandement inexploré, ce qui est étonnant vu son importance dans le jeu. J'ai lu une série presque interminable d'articles sur l'avantage des cartes, mais rien de vraiment *complet* à propos du tempo.

Ce qui m'a toujours frappé dans le passé, c'est qu’il paraissait manquer quelque chose dans tous ces articles. Certains aspects du tempo n’ont jamais été abordés dans la presse écrite, et d'autres sont en désaccord complet avec mes opinions. Ayant dit ça, je n'ai pas non plus la prétention d'écrire l'article définitif sur le tempo. Je vais juste vous montrer comment *moi* je le conçois. Je vois très souvent des exemples où le tempo a été mal interprété dans des articles, des décisions de jeu, et même des constructions de deck, alors je vais tenter de vous expliquer comment à mon avis, le tempo fonctionne. En vous détaillant mon système, je vais me concentrer sur ce que je considère comme l'aspect le plus important (et souvent sous-exploité) du tempo : comment le *mesurer*. Une partie de cet article vous fera sans doute l'effet d'une révision, mais je suis sûr que la plupart d'entre vous y trouveront une ou deux petites choses auxquelles vous n’aviez jamais pensé, ou un concept que vous n'aviez jamais remarqué auparavant.

Et qui sait, si cet article devient populaire, peut-être que d'autres spécialistes donneront aussi enfin leur opinion sur ce concept fondamental. Zvi a récemment dit (ça a fait assez de bruit) que le tempo était désormais probablement plus important que l'avantage des cartes, et je suis d'accord avec lui. Cependant, il n'est important que si vous comprenez suffisamment son fonctionnement pour en bénéficier ! Cela fait environ sept ans que je veux écrire cet article, et c’est devenu moins facile quand j'ai accepté les responsabilités de ce site, mais il devenait urgent pour moi de m'exprimer sur le sujet. Nous n'avons généralement pas le temps de faire ce qu'on veut, alors en me portant volontaire, j'espère attirer l'attention sur le sujet.

Vous êtes prêts ?

### Qu'est-ce que le tempo ?

![Last-Ditch Effort](https://i.ormos.uk/ea/39/ea39d182ed73e592248aa24298444b463ae45fd3e896efed69e038c855138660.jpg) C'est une question simple, non ? En fait, la réponse est très compliquée. Le terme 'tempo' sert à décrire tant de choses dans Magic que cela rend une explication très difficile, les gens utilisant ce mot sans distinction pour des concepts très différents.

Pour les besoins de cet article, quand j'utilise le terme tempo, je fais référence à la course aux blessures sur la table. Ce n’est pas limité à ça, bien sûr, mais une fois que vous comprendrez les bases de la course aux blessures, vous aurez les outils dont vous aurez besoin pour discuter des aspects plus avancés du tempo. Donc, pour l'instant, concentrons-nous sur comment faire chuter les points de vie de votre adversaire de 20 à zéro le plus rapidement et le plus efficacement possible. Pour ce faire, je vais me restreindre au format Limité, parce que les situations que vous rencontrerez en draft ou en Paquet scellé sont les plus simples à aborder, et les formats Limités sont généralement plus associés à la course aux créatures. Je vais commencer par quelques notions de base pour que nous puissions vraiment approfondir le fonctionnement de ce concept. Ensuite, ces outils nous serviront pour aborder d'autres aspects, mais vu que les discussions sur le tempo ont toujours été nébuleuses, je veux avant tout m'assurer que tout soit aussi limpide que possible dans cet article. Gardant cet élément en tête, j'utiliserai les créatures et les sorts qui illustrent le plus clairement ce que je veux vous expliquer. Oubliez les distractions comme le format ou l'environnement de jeu pour l'instant. Ne tombez pas dans le piège du 'mais je ne joue jamais avec ces cartes'. Concentrez-vous sur les principes qu'elles illustrent et je vous garantie que votre jeu va s'améliorer.

### Notre distribution

Permettez-moi de vous présenter la troupe de personnages qui va me donner un coup de main aujourd'hui.

![Grizzly Bears, Gray Ogre, Hill Giant, Giant Growth, Shock](https://i.ormos.uk/c4/88/c488923fd0ff32b2fe0489016f6497d6037b0a4804189830e8ac36504cfdf5bd.jpg)  
*Grizzlis, Ogre gris, Géant des collines, Croissance gigantesque, Choc*

Je vous avais prévenu que j'allais revenir aux bases, non ? Ces cartes et leurs cousines forment la base générique des formats Limité, alors elles sont parfaites pour étudier un concept comme le tempo. En retirant les détails comme les capacités et les autres complexités (pour l'instant), nous pouvons nous concentrer sur leurs caractéristiques fondamentales. Donc, si je fais référence à un 'ours', je parle d'une créature 2/2 pour 2 manas (même si ça marche aussi pour une 2/1). Un 'ogre' représentera une 2/2 pour 3 manas et un 'géant', une 3/3 pour 4 manas.

Vous en avez assez d'entendre qu'on doit commencer par les bases ? Moi aussi. Alors commençons !

### Le compteur de tours est enclenché

![Blood Clock](https://i.ormos.uk/57/b4/57b435ad97281aa1db1d8ef557f50fe6e5a5c55b73ac94bcfd55f4c9a7fd56a6.jpg) Quand on parle du tempo, on parle de la performance de chaque joueur dans la course visant à infliger 20 blessures à l'adversaire sans mourir avant lui. La clé qui vous permet de comprendre cette course est de trouver le moyen de mesurer votre performance. En ce qui me concerne, l'illumination m'est venue le jour où j'ai commencé à conceptualiser cette course en termes de *battements*.

Comme en musique ou au théâtre, le battement est une unité de temps. Chaque action que vous entreprenez pendant un tour est un battement, et c'est pareil pour vos adversaires. Si l'on considère que les battements ont tous la même force relative, gagner la course équivaut à trouver des moyens avoir plus de battements que votre adversaire.

Disons que vous jouez contre un ami en utilisant des decks que vous venez de drafter. Au tour un, vous passez chacun votre tour. Pendant votre deuxième tour, vous jouez un ours quelconque, et votre adversaire passe son deuxième tour. Vous venez de gagner un battement. Au tour trois, vous frappez avec votre ours, et vous sortez un ogre. Pour l'instant, vous avez deux battements d'avance, mais votre adversaire joue lui aussi un ogre. Alors ce tour ne vous a fait rien gagner en fin de compte, mais vous avez toujours un battement d'avance grâce au tour 2.

Vous me suivez ? C'est très simple en fait, et croyez-moi quand je dis que le savoir, ça fait toute la différence. En mesurant le tempo en battements, vous avez un moyen d'évaluer votre position sur la table en la comparant à celle de l'autre joueur dans la course au tempo. Dans l'exemple ci-dessus, une fois que vous avez joué votre troisième tour, vous avez un battement d'avance sur votre adversaire. Plus vous aurez de battements d'avance, meilleure sera votre position et il sera plus difficile pour votre adversaire de vous rattraper.

Ce qu’il faut comprendre, c’est que le tempo se mesure en prenant l’ensemble de votre position en considération et en déterminant qui a le plus de battements et combien. Avec ça en tête, essayons quelque chose qui devrait illustrer ce que je viens de vous dire. Que se passe-t-il quand un deck d'ogres combat un deck de grizzlis ?

Pour nous simplifier les choses, disons que les decks ressemblent à ceci :

<table><tbody><tr><td><table><tbody><tr><td><p><i>Grizzlis !</i></p>&#10;</td>&#10;<td><p><i>Ogres !</i></p>&#10;</td>&#10;</tr>&#10;<tr><td><p>6 forêts</p>&#10;</td>&#10;<td><p>6 montagnes</p>&#10;</td>&#10;</tr>&#10;<tr><td><p><i>14 Grizzlis</i></p>&#10;</td>&#10;<td><p><i>14 Ogres gris</i></p>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

Pour retirer toute notion de hasard de l'équation, chaque joueur va commencer avec la totalité du deck en main, et il n'y aura pas de défausse à cause de la taille de main maximale.

Que se passe-t-il ?

Si vous avez répondu 'qui commence ?' vous avez tout compris. Commençons la partie avec les Grizzlis. Réfléchissez un instant à la manière dont cette partie va évoluer, puis cliquez ici quand vous serez prêt. 

En commençant la partie, le deck Grizzlis obtiendra un ours au tour 2, mais le deck Ogres n'aura rien, ce qui donne un battement d'avance aux Grizzlis. Au troisième tour, il y a égalité car les deux decks sortent une 2/2, ce qui veut dire que les ours gardent le battement d'avance gagné au tour 2. Mais au tour 4, le deck Grizzlis gagne un nouveau battement en jouant deux créatures alors que l'adversaire ne joue qu'un ogre. Ce qui veut dire que le tour 4 donne un battement supplémentaire au deck d'ours, ce qui lui fait deux battements d'avance au total. Sans même se préoccuper des attaques et des blocages, remarquez combien de créatures chaque joueur a lancé à la fin du tour 4 :

![4 Grizzly Bears vs. 2 Gray Ogres](https://i.ormos.uk/dc/a8/dca85128b8a9553596c789c5a4b5ca984a4209ab6497570900eaabe1db21a3df.jpg)

Ceci dit, remarquez aussi qu'il se passera la même chose au tour 5, quand les ours gagnent encore un battement en lançant deux créatures. Au tour 6, les ours récupèrent encore un autre battement d'avance, le deck parvenant à lancer trois ours alors que les ogres ne sortent que deux créatures. Donc, au bout de six tours, les créatures invoquées suivent le schéma suivant :

![9 Grizzly Bears vs. 5 Gray Ogres](https://i.ormos.uk/dc/a8/dca85128b8a9553596c789c5a4b5ca984a4209ab6497570900eaabe1db21a3df.jpg)

Le deck Grizzlis a un total de quatre battements d'avance arrivé à ce point de la partie. Ils ont été gagnés aux tours, 2, 4 et 6, à chaque fois que le decks d'ours a pu jouer plus de créatures que le deck Ogres. Un battement a été remporté à chaque fois.

### Tous les battements ne sont pas égaux

![Rivalry](https://i.ormos.uk/a3/71/a3715810bd847b984df5ce91337fa048d030b247708bc7eac76314cb94f8f8b6.jpg) L'exemple précédent est facile à comprendre parce que chaque carte fait exactement la même chose. La seule importante différence entre les Grizzlis et les Ogres gris, c'est que l'un coûte deux manas, et l'autre, trois. Une fois en jeu, ils font exactement la même chose, alors les battements sont identiques. Cependant, dans la réalité, les cartes ne sont pas si égales que ça.

Les battements sont quelque peu subjectifs, parce qu'à mesure que la partie évolue, la notion du battement change. Au deuxième tour, jouer un ours est un excellent battement. Le faire au tour cinq sans rien faire d'autre n'est pas vraiment folichon. Alors il faut réévaluer la notion de battement en fonction de l'état de la partie. Une 2/2 pour 2 c'est excellent, mais si l'adversaire a joué un Isamaru, chien de Konda au tour 1, c'est vous qui devez le rattraper. Si la table commence à être inondée de 4/4 et de 5/5 aux alentours du tour 5, l'importance de ces premiers battements va aussi être sérieusement amoindrie. Nous y reviendrons un peu plus tard, mais l'important, c'est de se souvenir que même si les battements sont subjectifs, savoir quelle est la position de chaque joueur dans la course aux blessures est toujours utile. Ce ne sera seulement pas toujours aussi clair que dans l'exemple Ogres contre Ours ci-dessus.

### Obtenir l'avantage du tempo

Le tempo fonctionne beaucoup comme l'avantage des cartes en format Limité dans le sens où plus vous gagnez d'avantage, plus vous pourrez le convertir pour obtenir la victoire. Piocher plus de cartes que l'adversaire ne garantie en rien votre victoire, mais cela vous donne des chances supplémentaires de le faire. C'est exactement le même cas pour le tempo. Donc, en gardant toujours le format Limité à l'esprit, il faut comprendre comment générer des battements supplémentaires à ceux de votre adversaire. Voici quelques exemples qui m'aideront à illustrer le concept.

 *Les attaquants efficaces en mana*

Encore un exemple qui vient de la partie opposant les ogres aux ours. Si vous jouez des créatures qui coûtent moins que celles de votre adversaire, mais qui ont un effet relativement identique, vous aurez des occasions de gagner des battements. Souvent, il suffira de sortir un monstre au tour 2 quand l'adversaire ne peut rien faire, ou de pouvoir en lancer deux.

*Les trucs qui ne coûtent pas cher*

Dans beaucoup de formats de draft, une des manières que j'utilise pour obtenir le tempo ressemble un peu à cet exemple.

Je commence, je joue un genre d'ours au tour 2, et mon adversaire n'a rien à faire. (+1 battement)

Au troisième tour, j'attaque avec mon ours, puis je sors un ogre. L'adversaire joue aussi un ogre (toujours +1 battement)

Au quatrième tour, j'attaque avec mes deux créatures, il en bloque une, et j'utilise un truc qui ne coûte pas cher comme la Croissance gigantesque pour tuer sa créature et sauver la mienne. Mon autre créature inflige des blessures à l'adversaire, qui tombe à 16 points de vie, et j'utilise mon mana restant pour jouer un autre ours ou un autre ogre.

Quand on en arrive à ce moment de la partie, en considérant que l'adversaire n'a joué qu'une créature, il a perdu un autre battement. Il est à présent mort à 20% et j'ai trois créatures en jeu, alors que lui n'en a qu'une. Il est tellement en retard en développement qu'il est forcé de bloquer, ce qui rend chacune de mes actions plus puissante. Si les choses continuent ainsi, arrivé à un certain point, je pourrai gagner simplement en attaquant avec toutes mes créatures. Notez qu'à aucun moment de la partie, je n'ai obtenu un avantage des cartes, pas même un deux pour une. J'ai simplement trouvé des moyens de jouer et d'organiser mes cartes de manière plus efficace, ce qui veut dire qu'au bout du compte, j'avais plus de cartes en jeu que mon adversaire. Ce scénario est très facile à obtenir dans la plupart des formats Limités si vous faites très attention à votre jeu, car les cartes telles que Croissance gigantesque sont généralement plus faciles à obtenir que d'autres comme Choc .

 *Retrait bon marché*

Le scénario que je viens de vous présenter est très courant (utiliser un sort comme Croissance gigantesque), mais un sort de retrait tel que le Choc vous en donne une meilleure version. Si vous avez le choix, le retrait (au lieu d'un truc qui vous permet d'éliminer un bloqueur) est la plupart du temps supérieur parce que si la créature n'a même pas l'occasion de bloquer, cela vous permet d'infliger plus de blessures. Mais, et c'est là qu'interviennent les battements, le retrait que vous utilisez ne vous donnera l'avantage du tempo que si vous parvenez à faire autre chose ce tour-ci. Si vous dépensez quatre manas pour tuer leur créature qui en coûte quatre, vous préservez l'état actuel du tempo, mais vous ne l'améliorez pas. C'est la raison principale pour laquelle des cartes comme Choc sont très souvent des prises de choix dans les formats aggro Limités, et que des sorts de retrait plus cher passent en second, même s'ils sont 'plus puissants'. Chaque fois que vous gagnez un battement d'avance, vous prenez un peu plus l'avantage sur votre adversaire !

*Rebond*

![Vacuumelt](https://i.ormos.uk/d2/6b/d26b9ae276604b59989b93e662d19db7bff74c20527c16e1bdade322a79939d4.jpg) Sans oublier ce que nous venons d'apprendre, le moment est venu de parler des sorts de rebond (Boomerang, Désinvocation, etc). Certains pensent que le tempo, c'est juste une utilisation des cartes pour la course aux blessures. C'est en partie vrai, mais cette perception ne prend pas les battements en compte. Et beaucoup de gens pensent d’ailleurs à tort que les cartes de rebond sont des 'cartes de tempo' bien que leur impact sur le tempo dépende entièrement des battements !

Prenons un exemple. Vous commencez la partie, et vous sortez chacun un ours au tour deux. Au tour trois, vous dépensez deux manas pour lancer un Boomerang sur leur créature, et vous attaquez pour infliger deux blessures. Au tour trois, il rejoue son ours.

Le Boomerang a-t-il été une carte de tempo ? Eh bien, cela dépend de ce que vous appelez le 'tempo'. Certes, vous avez infligé deux blessures qui ne seraient peut-être pas passées si les créatures s'étaient affrontées, mais comme l'adversaire a pu rejouer la créature, vous avez terminé avec le même nombre de battements. Donc, le sort de rebond ne vous a donné aucun avantage en battements. Vous avez toujours un développement quasi-identique de chaque côté de la table. Cependant, si vous aviez utilisé la Désinvocation à la place, puis deux autres manas pour jouer un autre ours, vous auriez gagné un battement pour ce tour.

Et voici pourquoi. Le rebond est souvent considéré comme une stratégie de tempo, mais il ne vous procure un avantage de tempo que s'il vous fait gagner des battements ! La raison pour laquelle il est si souvent associé au tempo est son interaction avec une stratégie de tempo, mais à moins de gagner des battements, vous n'utiliserez le rebond que pour préserver les avantages que vous avez déjà acquis. Essayez ça :

<table><tbody><tr><td><table><tbody><tr><td><p><i>Tour</i></p>&#10;</td>&#10;<td><p><i>Vous</i></p>&#10;</td>&#10;<td><p><i>Adversaire</i></p>&#10;</td>&#10;<td><p><i>Résultat</i></p>&#10;</td>&#10;</tr>&#10;<tr><td><p>1</p>&#10;</td>&#10;<td></td>&#10;<td></td>&#10;<td></td>&#10;</tr>&#10;<tr><td><p>2</p>&#10;</td>&#10;<td><p>ours</p>&#10;</td>&#10;<td><p>2ème terrain uniquement</p>&#10;</td>&#10;<td><p>+1 battement</p>&#10;</td>&#10;</tr>&#10;<tr><td><p>3</p>&#10;</td>&#10;<td><p>ours</p>&#10;</td>&#10;<td><p>ogre (un petit Choc)</p>&#10;</td>&#10;<td><p>+1 battement (+2 au total)</p>&#10;</td>&#10;</tr>&#10;<tr><td><p>4</p>&#10;</td>&#10;<td><p>géant</p>&#10;</td>&#10;<td><p>géant</p>&#10;</td>&#10;<td></td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

Arrivé à ce point, vous avez toujours deux battements d'avance sur votre adversaire et il a perdu beaucoup de points de vie, mais son géant menace de minimiser l'avantage des battements obtenu avec vos ours. Par conséquent, si vous utilisez tout votre cinquième tour pour faire rebondir le géant (par exemple avec une Abrogation), vous n'augmenterez pas votre avantage s'il le rejoue, vu que vous aurez joué un battement chacun ce tour. Mais, en faisant rebondir le géant, vous avez maintenu l'état du jeu tel qu'il était, avec vos deux battements d'avance.

En fait, jusqu'à ce que l'adversaire joue son tour, vous avez trois battements d'avance. Ce n’est pas tout ce qui se passe et nous allons bientôt en discuter, mais pour l'instant, cet exemple devrait vous montrer comment les cartes avec des effets de rebond interagissent avec le tempo. L'important, c'est de bien calculer les battements. Parfois, le rebond vous en fait gagner plus que votre adversaire votre adversaire, mais d'autres, il aura l'effet contraire. Cette différence entre rebond et tempo est cruciale. Souvent, des joueurs mettent des cartes comme l'Abrogation dans leur deck à l'aveuglette en croyant qu'ils ont construit un 'deck tempo'. Mais, si elles n’interagissent pas avec le reste du deck pour générer des battements supplémentaires, le rebond à lui seul ne rendra pas le deck plus performant. Au contraire, il risque même de le *ralentir* !

Ce qui me rappelle soudain un des meilleurs articles sur le tempo que vous puissiez consulter. À l’époque de l'IPA, EDT ('Eric taylor' pour les intimes) avait réalisé un excellent papier pour Sideboard : [Controlling Tempo (en anglais uniquement)](https://web.archive.org/web/20060930000000/http://www.wizards.com/sideboard/article.asp?x=sb20010924a). Il s’intéressait surtout à l'équation quantité de mana utilisée pour neutraliser une menace/coût de cette même menace. C'est un excellent article, le mana est en effet au coeur de l'équation, mais je crois qu’il y manque le rôle important des battements.

EDT explique que vous ne voulez pas uniquement dépendre de cartes comme la Répulsion (qui coûte 3 manas) dans un format défini par des ours (qui coûtent 2 manas) parce que 'Quand vous payez trois manas pour détruire une créature qui n'en coûte que deux, tout ce qui arrive, c'est que vous perdez le tempo.' C'est une leçon importante, mais cette équation ne se focalise que sur un moment précis du jeu. Grâce aux battements, nous savons que l'équation est un peu plus complexe que ça. Si vous passez le tour trois à engager trois manas pour tuer un ours avec une Rage selon Urza, ou à dépenser deux manas sur une Terminaison sans utiliser le troisième mana, la situation est du pareil au même : vous avez échangé un battement contre un battement, en maintenant l'état de la course au tempo. *Mais*, si vous utilisez la Terminaison pour tuer cette créature, et que vous utilisez le dernier mana pour gagner un battement en jouant un Choc sur un autre ours ou une Croissance gigantesque dans un combat pour que votre créature survive et que celle de l'adversaire trépasse, vous générez un avantage de battement de +1, et *ça*, c'est important. EDT avait une partie de l'équation, et pas la moins importante. Utiliser moins de mana pour annuler plus de mana ouvre des portes, certes, mais elles ne sont importantes que si vous utilisez le mana économisé pour gagner des battements !

### Tempo et avantage des cartes

Souvent, les gens pensent que le tempo et l'avantage des cartes sont opposés l'un à l'autre : vous essayez de piocher des cartes supplémentaires (et vous perdez le tempo) ou vous balancez toutes vos ressources pour gagner la course aux blessures (et vous gaspillez des cartes). En comprenant mieux le fonctionnement du tempo, vous noterez de par vous-même que ces deux affirmations sont des généralités qui ne sont pas toujours vraies. Magic est un jeu *vraiment* compliqué à expliquer, alors les gens ont trop l'habitude de ce genre de raccourcis. Le tempo et l'avantage des cartes sont souvent des stratégies opposées, mais ce n'est pas *toujours* le cas, par exemple, si vous gagnez un avantage deux pour une sur la table à la place de votre main. Ainsi, une carte comme le Pourrissement cérébral génère une carte d'avantage des cartes au tour trois parce que vous avez utilisé une carte et que votre adversaire en a perdues deux. Mais, si vous passez un tour de développement pour ce faire, et que les cartes éliminées sont en main, et pas en jeu, vous sacrifiez votre développement de tempo pour gagner l'avantage des cartes, comme si vous aviez utilisé votre quatrième tour pour lancer un Cours de pensées pour deux cartes.

Mais, quand vous commencez à retirer plusieurs cartes *depuis le jeu*, le tempo et l'avantage des cartes se chevauchent. Prenons un exemple : votre adversaire peut lancer trois créatures d'endurance 1 pendant ses premiers tours, et vous, rien. Pendant votre troisième tour, vous lancez un Cracheur de peste. Toutes les créatures adverses meurent, et vous gagnez un battement parce que vous avez la seule créature en jeu, ainsi qu'un avantage des cartes 3 pour 1. En bloc Ravnica Limité, un gain courant de tempo *et* d'avantage des cartes provient de la destruction d'une créature qui est enchantée par une aura comme la Marquemage de l'escrimeur. Vous jouez tous les deux des créatures au tour deux. Vous en jouez une au tour trois, mais l’adversaire lance la Marquemage sur sa première créature au lieu d'en jouer une autre. Au tour quatre, si vous lancez un Boulet de démolition sur son unique créature, vous récupérez un avantage des cartes deux pour une et vous gagnez deux battements d'avance, puisque vous avez deux créatures face à une table vide. (Mais rappelez-vous, elles n'ont pas encore joué leur tour.)

Enfin, une autre manière courante d'obtenir des battements en Limité tout en gagnant l'avantage des cartes vient en forçant des blocages de masse de vos monstres en utilisant quelques ruses de combat pour obtenir le dessus. Si vous chargez avec un Élémental de ronces et que l'adversaire bloque avec une paire d'ours, Rassembler son courage va vous donner une carte en avantage des cartes, puisqu'il perdra deux créatures et que vous ne perdrez que votre Rassembler son courage. Encore mieux, vu le prix compétitif de petits sorts comme celui-ci, vous aurez probablement encore du mana pour gagner quelques battements supplémentaires en lançant d'autres créatures ou d'autres sorts de retrait avec ce qui vous reste. Dans ce cas précis, il y a beaucoup de synergie, parce que plus votre deck obtient d'avantage de tempo, plus vous forcez votre adversaire à bloquer ! Ce qui nous amène au problème suivant.

### Initiative

Donc, pour résumer, nous mesurons le tempo en battements, qui sont les actions pendant un même tour. Ce que le battement représente exactement change à mesure que la partie évolue (parce que les tours deviennent plus puissants) et peut être affecté par l'état de la partie, mais l'idée de base reste la même : 'un mouvement de niveau moyen pour ce tour'. Gagner et maintenir l'avantage des battements implique de faire plus de choses pendant un tour que votre adversaire, ce qui peut conduire aussi à l'avantage des cartes. Les battements peuvent aussi être gagnés en utilisant des actions qui annulent les battements multiples de votre adversaire, par exemple en utilisant la Croissance gigantesque pour tuer deux créatures, autrement dit se débarrasser de deux battements pour un petit mana. Mais comment traduire ce tempo en une victoire ? Pour cela, nous devons d'abord comprendre un concept que je vais emprunter aux échecs : l'initiative.

L'initiative faire référence au joueur qui décide du rythme de la partie. Dans beaucoup de parties d'échecs ou de Magic, je jeu n'est pas stable. Il y a toujours un joueur attaquant. Qui a l'initiative a l'avantage du tempo, et son adversaire est contraint de réagir. Une fois de plus, nous devons nous concentrer sur la course aux blessures.

Nous n’avons pas encore discuté d’un autre élément associé au tempo, la moitié de tour, un autre concept des échecs. Le joueur qui commence est considéré comme ayant un avantage d'une 'moitié de tour' de développement parce qu’il se déplace avant son adversaire. Dans Magic, c'est pareil, mais je ne vais pas tergiverser pour savoir si c'est vraiment une moitié de tour 'complète'. Pour simplifier les choses, disons que si vous jouez le premier, vous avez naturellement l'initiative, mais elle ne correspond qu’à un avantage naturel. Si votre deck ne tient pas la route face à celui de l’adversaire, c'est lui qui risque de finir avec l'initiative. Vous commencez avec un avantage. Plus vous maintenez la pression sur l'adversaire, plus cet avantage devient important. Mais si vous prenez du retard sur le tempo, avoir commencé la partie vous soulage un peu.

Je m’explique avec un exemple : jouer Isamaru, chien de Konda dès le premier tour sans avoir commencé la partie en premier, c’est un peu comme jouer un ours au tour deux si vous l’avez commencée, tant que le reste de votre deck est construit de manière similaire. L'important, en ce qui concerne les moitiés de tour, c'est que, même si on compte les battements une fois que chaque joueur a joué son tour pour comparer leurs performances, il y a un jeu à *chaque* tour. Donc, les moitiés de tour considèrent que vous avez fait rebondir une créature et qu'elle reviendra au tour prochain, mais qu'en attendant, elle n'est pas là pour vous empêcher d'attaquer *pour le moment*.

Pourquoi l'initiative est-elle importante ? Quand vous avez l'initiative, vous contrôlez la course. C'est un avantage parce que vous pouvez contraindre votre adversaire à vous bloquer pendant votre tour plus souvent. Il y a un avantage a naturel quand vous forcez des batailles pendant votre tour en format Limité, parce que vous avez plus de chances d'avoir du mana disponible que votre adversaire. Ce qui veut dire que vous avez la capacité d'influencer le combat. Plus vous prenez d'avance, plus vous pouvez acculer vos adversaires en compliquant la progression de la partie.

Une fois qu’un adversaire est retardé, vous pouvez frapper, même avec vos petites bestioles, parce qu’il sera obligé de bloquer vos monstres les plus gros pour rester en vie. Ainsi, vos petites créatures ont encore de la valeur à un moment de la partie où elles ne seraient normalement utiles à rien, un avantage que vous auriez perdu sans l'initiative. Pour le joueur utilisant le tempo, c'est une leçon fondamentale. Si vous vous laissez faire, Magic contient un égaliseur interne qui favorise le défenseur, parce qu'il choisit comment il bloque. Cependant, moins l'adversaire a de points de vie, moins il a la possibilité de bloquer vos petites créatures parce qu'il doit se concentrer sur les plus grosses pour éviter de passer de vie à trépas. Plus vous pourrez générer d'avantage de tempo, plus ce principe empêchera votre adversaire de se défendre en essayant de bloquer de manière stratégique.

### Avantage et entretien du tempo

Maintenant que nous avons une idée précise de ce que sont l'initiative et les moitiés de tour, nous revenons sur un aspect que nous n’avions que survolé. D'abord, petit rappel : l'erreur la plus courante faite par les joueurs concernant le tempo, c'est de confondre l'entretien du tempo avec l'avantage du tempo. Passer tout votre tour à annuler celui de l'adversaire n'est **pas** un gain de tempo ! (Cela fait partie d'une stratégie basée sur le tempo, mais ce n'est pas un **gain** de tempo.) S'il sort un ours au tour deux et que vous lui balancez un Boomerang pendant votre deuxième tour, la situation de tempo est identique à, par exemple, celle que vous auriez en jouant vous aussi un ours. Dans un cas comme dans l'autre, vos tours sont égaux en terme de tempo. Au lieu d'un avantage de tempo, vous obtenez simplement un entretien du tempo.

Prenons un exemple facile : ours de tour 2, ours de tour 2. Vous lancez Physalie pour faire rebondir la créature de l'adversaire. Il joue une autre bestiole (l'originale ou encore un ogre). Vous avez gagné un battement avec votre Physalie en retirant une des créatures de la table, tout en y ajoutant une des vôtres. Donc, à la fin du tour 3, vous avez l'avantage du tempo parce que vous avez un battement d'avance.

Mais l'entretien du tempo, c'est une autre histoire. Si vous avez trois créatures contre une et que vous passez votre tour à faire rebondir la dernière jouée par l'adversaire, vous n'avez pas gagné de tempo vu qu'il va rejouer sa créature pendant son tour. Cependant, comme vous avez déjà deux battements d'avance, entretenir le status quo vous suffit amplement. Le plus longtemps vous pourrez maintenir cet avantage de deux battements, plus votre adversaire perdra de points de vie et plus il lui sera difficile de stabiliser son jeu (rappelez-vous, au bout d'un certain temps, l'avantage du tempo le force à bloquer de manière moins efficace). Dans ce cas, vous utilisez des cartes d'entretien du tempo pour préserver l'avantage du tempo que vous aviez obtenu auparavant. c'est pourquoi des cartes comme l'Abrogation sont souvent considérées comme des 'cartes de tempo' alors qu'elles ne génèrent pas souvent de tempo à elle toutes seules. En fait, elles complémentent une stratégie de tempo en vous permettant de maintenir l'état de la partie quand vous avez un avantage du tempo.

### Battements immédiats et battements investis

![Time Stretch](https://i.ormos.uk/87/87/87876a597203e6980f3ad32afa242d380522d3ac923361b8e193d39bf133ad71.jpg) Mais, et c'est la partie sur laquelle je ne me suis pas attardé plus tôt, c'est en fait un peu plus compliqué que cela, et c'est une fois de plus un élément fondamental de l'équation : retirer des bloqueurs, c'est différent de mettre en jeu de nouveaux attaquants. Pourquoi est-ce vrai ? La réponse courte c'est : 'Les attaquants interviennent plus tard, et les bloqueurs bloquent maintenant.' C'est tellement important que je vais répéter ça pour vous le faire entrer dans le crâne.

* * *

 *Retirer des bloqueurs, c'est différent de mettre en jeu de nouveaux attaquants.*

* * *

C'est l'autre raison pour laquelle le rebond est si souvent associé au tempo. Si vous et votre adversaire êtes à égalité en battements, mais que vos créatures n'arrêtent pas de se foutre sur la figure, les blessures ne passent pas au travers. Mais, si vous retirez ses créatures plutôt qu'en jouer d'autres vous-mêmes, vos blessures sont infligées. C'est une étape cruciale, parce que c'est là que les blessures jouent dans le concept des battements. Regardons ces deux exemples simples. 

<table><tbody><tr><td><table><tbody><tr><td><p><i>Tour</i></p>&#10;</td>&#10;<td><p><i>Vous</i></p>&#10;</td>&#10;<td><p><i>Adversaire</i></p>&#10;</td>&#10;<td><p><i>Résultat</i></p>&#10;</td>&#10;</tr>&#10;<tr><td><p>1</p>&#10;</td>&#10;<td></td>&#10;<td></td>&#10;<td></td>&#10;</tr>&#10;<tr><td><p>2</p>&#10;</td>&#10;<td><p>ours</p>&#10;</td>&#10;<td><p>ours</p>&#10;</td>&#10;<td></td>&#10;</tr>&#10;<tr><td><p>3</p>&#10;</td>&#10;<td><p>ogre</p>&#10;</td>&#10;<td><p>ogre</p>&#10;</td>&#10;<td><p>(les ours frappent ce tour)</p>&#10;</td>&#10;</tr>&#10;<tr><td><p>4</p>&#10;</td>&#10;<td><p>géant</p>&#10;</td>&#10;<td><p>géant</p>&#10;</td>&#10;<td><p>(les ogres frappent ce tour)</p>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

Dans cette partie, les deux joueurs sont à égalité en termes de battements. Au bout du compte, on arrive au tour cinq et les deux joueurs ont 20 points de vie et un géant en jeu. Maintenant, comparons avec un autre jeu à battements égaux.

<table><tbody><tr><td><table><tbody><tr><td><p><i>Tour</i></p>&#10;</td>&#10;<td><p><i>Vous</i></p>&#10;</td>&#10;<td><p><i>Adversaire</i></p>&#10;</td>&#10;</tr>&#10;<tr><td><p>1</p>&#10;</td>&#10;<td></td>&#10;<td></td>&#10;</tr>&#10;<tr><td><p>2</p>&#10;</td>&#10;<td><p>ours</p>&#10;</td>&#10;<td><p>ours</p>&#10;</td>&#10;</tr>&#10;<tr><td><p>3</p>&#10;</td>&#10;<td><p>Sceau du destin sur ours, frappe pour 2</p>&#10;</td>&#10;<td><p>ogre</p>&#10;</td>&#10;</tr>&#10;<tr><td><p>4</p>&#10;</td>&#10;<td><p>Boulet de démolition sur ogre, frappe pour 2</p>&#10;</td>&#10;<td><p>Boulet de démolition sur votre ours</p>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

Comme dans la partie précédente, les deux joueurs sont à égalité en battements. En fait, à la fin du tour quatre, personne n'a rien en jeu excepté des terrains. Mais il y a une grande différence : dans cette partie, l'adversaire a subi quatre blessures ! Pourquoi ?

* * *

*Parce que 'retirer des bloqueurs, c'est différent de mettre en jeu de nouveaux attaquants.'* 

* * *

Les deux joueurs jouent au même rythme de battements. *Mais* le joueur 1 a l'initiative. Nous avons beau dire que chaque joueur joue au même rythme de battements, c'est uniquement le cas si nous considérons chaque tour comme un tour *complet*, en laissant l'adversaire vous rattraper en attendant d'évaluer la position jusqu'à ce que *chacun* d'entre vous ait joué un tour. Mais ce n'est pas comme ça que Magic fonctionne. Comme vous avez commencé, vous avez un avantage d'une moitié de tour. Ce qui signifie que vos créatures attaquent les premières. Donc, à chaque fois que vous retirez des créatures adverses, vos créatures existantes ont une occasion de frapper pour infliger plus de blessures. Une des conclusions à en tirer, c'est que si vous cherchez à gagner par avantage du tempo, vous voudrez éviter d'affronter des bloqueurs autant que possible. Il vaut toujours mieux gagner des battements en utilisant l'esquive, le retrait et d'autres moyens de faire traverser les défenses de l’adversaire par vos attaquants. Ainsi, non seulement vous êtes en tête en ce qui concerne le développement, mais votre adversaire subit aussi plus de blessures.

Pendant que nous y sommes, notez que selon le système d'EDT, vous avez perdu du tempo quand vous avez utilisé le Sceau du destin à 3 manas pour vous débarrasser de l'ours à 2 manas. Mais, avec le système des battements, nous savons que ce n'est pas le cas. Loin de moi l'idée de critiquer EDT. En fait, son article m’a servi de base. Mais c'est une bonne illustration du manque d’articles sur le tempo reflétant vraiment le déroulement d'une partie de Magic. Avec un peu de chance, ce papier changera un peu les choses !

### Tempo virtuel

Maintenant que nous avons une idée plus précise de la manière dont l'avantage par battement peut affecter la partie, nous pouvons commencer à utiliser cette connaissance pour étudier les aspects plus avancés du tempo. Ce qui nous conduit à un concept fondamental que j'appelle le 'tempo virtuel'. Le tempo n'existe pas dans le vide ; c'est un ingrédient dans un mélange complexe. La qualité des cartes entre aussi dans l'équation, et dans ce cas, je parle de qualité des cartes en fonction de *la situation du jeu actuelle*. Un petit scénario rapide : adversaire-ours, vous-rien, adversaire-ogre, vous-ogre, adversaire-ogre, vous-2/4.

![Grizzly Bears and 2 Gray Ogres vs. Scathe Zombies and Foot Soldiers](https://i.ormos.uk/56/2a/562a23349bc7cb74ce71781ab580f444c1252e6c9f44e4e56904b846d3293cf3.jpg)

Donc, votre adversaire a commencé et vous avez chacun joué quatre tours. Quelle est la situation de tempo dans ce scénario ?

Vous êtes en retard d'un battement (2 créatures contre 3) et pourtant, vous n'êtes pas en retard en tempo. Comment est-ce possible ? C'est le point crucial ! Vous êtes en retard sur les battements, certes, mais le tempo ne se limite pas aux battements, c'est la mesure de la course. En raison de la situation sur la table, une 2/4 suffit pour stabiliser, et plus votre situation est stabilisée, moins les battements sont importants. Réfléchissez à ça et vous comprendrez : combien de 1/1 faut-il pour submerger une 2/2 ?

Mais, en dépit d'une table stabilisée, vous avez tout de même un battement de retard dans cette position. Pour expliquer pourquoi c'est important, prenons un exemple plus extrême. Dans celui-là, vous avez même raté votre troisième tour et vous n'avez rien pu faire avant de sortir un Fantassin au tour quatre. Voilà à quoi ressemble la table après quatre tours.

![Grizzly Bears and 2 Gray Ogres vs. just Foot Soldiers](https://i.ormos.uk/5f/03/5f03f20aa575c7b4a0003ac3400f25f6a268be8ffc5a0b5d3a3ad6e545392647.jpg)

Dans cette position, vous avez un retard de deux battements. Pour l'instant, la situation est stabilisée, mais cela ne change rien au fait que vous avez deux battements de retard. Cela signifie simplement qu'il est plus difficile pour votre adversaire de vous toucher malgré l'avantage de tempo qu'il a parce que vous avez stabilisé la table. Vous êtes parvenu à obtenir le tempo virtuel. Même si vous avez deux battements de retard, la carte que vous avez jouée annule les battements supplémentaires de l'adversaire.

Mais le terme 'virtuel' est important. Vous n'êtes pas *vraiment* à égalité sur vos battements, c'est la présence en jeu de cette 2/4 qui en donne l'impression. Si votre adversaire se débarrasse ou tue ce bloqueur, vous allez sentir immédiatement ces deux battements. C'est une leçon importante, un point crucial du jeu offensif ou défensif à Magic.

* * *

*Le tempo virtuel n'annule pas l'avantage du tempo. Il est uniquement aussi stable que la carte (ou les cartes) qui le procure.*

* * *

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Minister of Impediments" src="https://i.ormos.uk/b7/c9/b7c916e2d0074911dfe8dc7adba4ea12e8b4dd60ba4321a4ffbcb81c64a9ee2a.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Donc, plus votre deck Contrôle doit se reposer sur le tempo virtuel, plus il est important que ces cartes de tempo virtuel restent en jeu ! Toujours en format Limité, cela veut dire que les decks tempo offensifs doivent drafter avec le tempo à l'esprit pour avoir de quoi opposer les cartes défensives qui peuvent annuler votre avantage du tempo. Pour ce faire, tout dépend de l'environnement dans lequel vous jouez, mais les meilleurs drafteurs savent exactement quelles menaces vont leur poser des problèmes défensifs, et quelles cartes ils peuvent espérer drafter pour contourner ce problème.

C'est dans cette catégorie qu'on trouve les 'engageurs' tels que le Ministre des impedimenta. Pendant que la partie évolue, chaque battement a tendance à devenir plus puissant en moyenne. L'avantage des engageurs, c'est qu'ils peuvent changer de cible et s'attaquer aux *meilleures* cibles en jeu. Donc, au tour trois, un Ministre des impedimenta est un battement à trois manas, et il annule l'effet de la meilleure créature adverse dès qu'il est actif. Mais ce qui fait la puissance de cette classe de cartes, c'est que l'engageur n'est pas verrouillé. Quand de meilleures cibles font leur apparition, les engageurs se tournent immédiatement vers la meilleure d'entre elles.

Donc, en utilisant le Ministre comme exemple, pour un battement de trois mana, vous annulez l'effet de la meilleure créature à un moment donné, même si cette créature coûte bien plus de mana que vous n'en avez investi quand vous avez lancé votre Ministre. Encore mieux, s'il a été utilisé défensivement, à un moment de votre choix, vous avez la capacité d'utiliser le tant redouté double engagement, en engageant une créature à la fin du tour de l'adversaire, puis autre chose pendant votre tour, ce qui rend la défense de votre adversaire plus difficile. Ce n'est peut-être pas une stratégie intuitive, mais engager des créatures est une formidable tactique pour les decks basés sur le tempo. Dans le passé, l'exception à cette règle a été quand la capacité activée de l'engageur (qui utilise généralement un mana) ralentit votre propre développement (surtout si vous faites une erreur avec votre mana), ce qui montre pourquoi le Ministre des impedimenta est une carte tellement puissante, car elle n'a pas besoin de beaucoup de mana après l'investissement initial.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Golgari Brownscale" src="https://i.ormos.uk/82/24/822406bd20ee22bbf6bdbfa3203ccce8c08e40ad4f2d0928ae896fdd63670be5.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Enfin, tant que nous parlons de la manière dont la qualité des cartes et les battements interagissent, je voudrais mentionner autre chose qui généralement n'attire pas beaucoup l'attention. Selon l'environnement dans lequel vous jouez, il y a souvent une classe de créatures qui, à cause de la nature de ses caractéristiques, a non seulement la capacité d'infliger des blessures pendant votre prochain tour, mais peut aussi prévenir une attaque de l'adversaire en attendant. Le Brunécaille golgari est un excellent exemple. C'est une carte que j'adore utiliser dans les drafts Ravnica qui ont suffisamment de mana vert pour le sortir au tour trois. La raison est simple : la plupart des créatures qui sortent avant le Brunécaille ne peuvent pas le traverser, et la plupart de celles qui arrivent en jeu au même tour ne peuvent pas le bloquer !

Alors, même si votre adversaire a déjà gagné un battement au tour deux quand il a joué un ours et que vous n'avez rien fait, quand vous jouez le Brunécaille, l'ours ne peut pas attaquer. Encore mieux, votre adversaire ne peut probablement pas bloquer quand ce sera votre tour, à moins qu'il ne veuille risquer un double blocage quand vous avez du mana disponible (en supposant qu'il ait une créature de coût typique en jeu pendant son tour).

J'appelle cet effet une 'pause forcée' parce que vous retirez une attaque à votre adversaire tout en continuant votre offensive sans vous arrêter. Mais quel que soit le nom que vous lui donniez, c'est une situation qui arrive *tellement souvent* en format Limité que je voulais le mentionner dans cet article. Le draft Odyssée est un autre excellent exemple, car peu de créatures ont une force de trois. C'est pour ça que le [cycle de créatures 2/3 à quatre manas](https://web.archive.org/web/20060930000000/http://gatherer.wizards.com/?first=1&last=100&term=2%2F3&Field_PT=on&setfilter=Odyssey&colorfilter=All&typefilter=creature&output=summary&sort=cost&x=45&y=27) (dont l'Archer krosian) était particulièrement apprécié ; il empêchait souvent les créatures adverses d'attaquer quand elles arrivaient en jeu, et ensuite elles pouvaient souvent frapper pendant votre tour suivant si vous le vouliez. En pratique, ce genre de créature enlève une phase d'attaque à l'adversaire, même si vous pouvez attaquer pendant votre tour (si c'est ce que vous voulez). Chaque fois que vous jouez une de ces créatures au bon moment, vous faites caler la phase d'attaque de l'adversaire, et vous gagnez un demi tour de course sur lui en l'empêchant de vous infliger des blessures ce tour tout en continuant de développer votre propre offensive. Combinez ce genre d'effets avec d'autres actions qui vous permettent de gagner des battements supplémentaires et votre adversaire vous suppliera à genoux en moins de deux !

### O et D

![Azorius Ploy](https://i.ormos.uk/b3/47/b3470338953448c52525b2696c073754b1299f7f45b02dbea4f4400dcd9149a1.jpg) Voilà qui nous conduit à un autre sujet associé, le tempo offensif et défensif. Jusqu'à présent, nous nous sommes concentrés sur deux decks offensifs qui font la course, mais toutes les parties de Magic ne fonctionnent pas ainsi, surtout en format Construit. Quand vous êtes à l'offensive, jouer quelque chose qui aidera votre offensive vous aide aussi à obtenir le tempo. La défense aussi peut avoir le tempo, avec le plus souvent un objectif stabilisateur visant à atteindre une autre phase de la partie où le deck défensif aura la supériorité.

Donc, dans ces courses au tempo, vous devrez réajuster votre évaluation des battements en fonction de l'environnement de jeu. Un deck offensif jouant contre un deck Contrôle peut récupérer des battements aux tours un et deux en déployant des bagarreurs rapides, mais s'il doit faire une pause au tour trois pour lancer quelque chose du genre d'une Cariatide sculptée, le battement est perdu si le deck adverse n'a pas de créature qui arrive en jeu.

Donc, pour les decks offensifs, il est important de générer des battements qui donnent un avantage contre le deck défensif. Pour la défense, il est souvent important de jouer des battements qui annulent les effets des attaquants adverses. Par exemple, un Mur de lances (en format Limité, évidemment !) peut vraiment faire du mal à un deck offensif rempli de créatures avec une endurance de deux. Dans les exemples ci-dessus, nous vous avons montré comment une carte comme Fantassin pouvait générer un tempo virtuel contre des créatures plus petites en leur rendant l'attaque trop onéreuse. Mais, si vous pouvez établir ce genre de défense en gagnant suffisamment de battements pour ne pas prendre de retard, ce n'est plus un tempo virtuel, mais une stabilisation du tempo, qui est plus efficace. Ce principe explique pourquoi les decks qui sont bons en fin de partie en Limité ont besoin de créatures avec des caractéristiques comme 2/4, puisqu'elles peuvent arrêter la progression de plusieurs créatures adverses (ce qui en soi devient une sorte d'avantage des cartes). Et, en restant proche de l'adversaire en tempo (pas en tempo virtuel), la destruction de vos défenses par le deck aggro est bien plus difficile. Mieux vous comprendrez comment les battements interagissent avec l'offensive et la défensive, plus vous aurez de succès en draftant (et en battant !) des decks offensifs et défensifs.
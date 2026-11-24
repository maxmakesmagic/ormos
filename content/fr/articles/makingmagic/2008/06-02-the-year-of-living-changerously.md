---
id: 3e6x89mr
kind: article
lang: fr
path: /fr/articles/makingmagic/2008/06-02-the-year-of-living-changerously
title: L'année de tous les changements
published: '2008-06-02'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
translation_of: zfkkjngs
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
    lang_detected: fr
    capture_id: 1977137
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,fr
    captured_at: '2008-07-02 04:07:18+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
    lang_detected: fr
    capture_id: 1977137
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,fr
    captured_at: '2008-07-02 04:07:18+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
    lang_detected: fr
    capture_id: 1977137
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,fr
    captured_at: '2008-07-02 04:07:18+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
    lang_detected: fr
    capture_id: 1977137
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,fr
    captured_at: '2008-07-02 04:07:18+00'
    rule: classic.legacy_column_rule
    registry_match: registry.explicit
sources:
- document_id: 3e6x89mr
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,fr
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
  lang: fr
  template: classic_asp
  captured_at: '2008-07-02 04:07:18+00'
  capture_id: 1977137
  wayback_url: https://web.archive.org/web/20080702040718id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,fr
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 3e6x89mr
  capture_id: 1977137
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,fr
  wayback_url: https://web.archive.org/web/20080702040718id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,fr
  captured_at: '2008-07-02 04:07:18+00'
  template: classic_asp
  sha256: 52bbafaa7934374aa10a548264106e2dfa3f89b8f328f4c3dced3d88390c1661
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void(0);
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - ici
  - Cliquez ici
  occurrences: 2
---
* * *

Si vous n'avez pas encore lu [l'annonce officielle d'aujourd'hui](/en/articles/feature/2008/06-02-changes-as-of-shards-of-alara), sachez que **Magic** va subir quelques métamorphoses à partir de l'extension *Les éclats d'Alara*. Alors, autant profiter de ma chronique pour détailler tous ces changements et vous expliquer pourquoi ils sont importants. 

### Tout pour jouer

Avant d'entrer plus dans le détail, laissez-moi vous expliquer les raisons qui motivent tous ces changements. Le boulot de l'équipe créative de **Magic**, c'est principalement d'encourager les joueurs à jouer. Pour ce faire, nous devons concentrer notre attention sur deux groupes distincts. D'abord, il faut motiver les joueurs que nous avons déjà. Ensuite, il faut ouvrir les portes du jeu à de nouveaux joueurs (ou des joueurs qui ont arrêté pendant un temps). Ces deux groupes sont essentiels au succès de **Magic** à long terme. (Pour une version plus détaillée de ce raisonnement, lisez mon article [Assume the Acquisition](/en/articles/makingmagic/2008/03-03-assume-the-acquisition).) La communauté de joueurs existante, même si des innovations sont toujours les bienvenues, est stable et nous lui réservons quelques surprises qui la satisferont encore plus. 

Ce qui veut dire qu'à l'heure actuelle, nos efforts doivent surtout se concentrer sur des méthodes visant à faire découvrir le jeu à de nouveaux joueurs. L'importance d'acquérir de nouveaux joueurs a été un thème constant sur **magicthegathering.com** cette année. Enfin, nous sommes en mesure de vous montrer comment nous espérons y arriver avec nos produits. Cet article va vous détailler toutes leurs modifications, vous expliquer quel impact elles auront sur le produit, et pourquoi nous pensons que ces décisions permettront une meilleure croissance du jeu.

### Remue-méninges

Un des meilleurs moyens d'aborder un problème connu est de prendre du recul et d'y appliquer un regard neuf. De même, il vaut mieux éviter de réfléchir de façon conventionnelle, car vous aboutiriez probablement aux mêmes suppositions, ce qui ne résoudrait pas le problème. Alors, on est reparti de zéro. Comment ouvrir le jeu aux débutants ? Quels sont les handicaps qui rendent l'approche du jeu difficile ? Comment rendre notre jeu plus convivial pour les novices ?

Et c'est avec ces questions que nous avons réalisé quelque chose d'important. Jusqu'à présent, nous avions concentré nos efforts d'acquisition sur les éditions de base et nos efforts de rétention sur les extensions, supposant que le débutant ferait la connaissance du jeu avec notre produit le plus simple et que le joueur plus expérimenté serait plus intéressé par les cartes les plus récentes. Nous avons étudié cette supposition (parmi tant d'autres) et rassemblé quelques données. Vous savez ce qu'on a découvert ? Nous nous trompions. En gros, les nouveaux joueurs ne suivent pas tous le même parcours. Ils commencent par le premier produit **Magic** qu'ils trouvent et, comme ils apprennent à jouer le plus souvent avec des joueurs expérimentés, ils ne découvrent généralement *pas* le jeu avec l'édition de base.

Alors que faire ? Nous avons commencé par nous forcer à comparer nos extensions et nos éditions de base. Et on ne pourrait pas trouver de produits plus différents. Je crois que le mieux, c'est de plonger dans le vif du sujet en vous détaillant le fruit de nos découvertes et de nos observations.

### Premier changement : moins de cartes par an

Permettez-moi de commencer cette partie avec deux mots de jargon, ce qu'on appelle les « années **Magic** ». Dans l'explication qui suit, au lieu de suivre l'année chronologiquement, je commencerai « l'année » par la grande extension d'automne et je continuerai avec les suivantes, jusqu'à la grosse extension de l'automne suivant. Chaque année sera représentée par le nom de l'extension d'automne ou son symbole. 

Maintenant que c'est clair, concentrons-nous sur le point important de cette partie. À partir de l'année *Les éclats d'Alara*, nous publierons moins de cartes chaque année.

À quel point ce changement va-t-il affecter le jeu ? Voyons combien de cartes ont été publiées par année **Magic**, en commençant par *Ère glaciaire*. 

(Autant vous glisser tout de suite quelques notes techniques sur ce tableau parce que je sais que je vais déjà suffisamment recevoir de courrier sur cet article : oui, je considère *Terres natales* comme faisant partie de l'année *Ère glaciaire* pour ce décompte ; non, je ne compte pas les terrains de base pour toutes ces extensions ; oui, je compte la rareté « jeu de découverte » de la *Huitième* et de la *Neuvième édition* ; et non, je ne compte pas les extensions *Un*\- ou les jeux de découverte pour les débutants comme *Portal*. Enfin, je *compte* les terrains de base neigeux de *Souffle glaciaire*, mais pas ceux d'*Ère glaciaire*. Pourquoi ? Parce que les terrains de base neigeux de *Souffle glaciaire* sont considérés comme des cartes courantes dans les boosters.)

![](https://i.ormos.uk/af/8e/af8ecb46d035d76106b0a9e5894158df75b7fa0a9a254f39b61d08348cb53db3.gif)

![](https://i.ormos.uk/d5/63/d563aba7ec040114cf6a0aa1b8eb053d6a3a30545bda66e4cc0082374ec81605.gif)

Maintenant, comparons avec l'année prochaine. Cliquez ici pour l'ajouter à l'image ci-dessus.

Sans compter l'édition de base, nous allons publier moins de cartes pendant l'année *Les éclats d'Alara* que dans les années **Magic** précédentes – 519. Même en comptant l'édition de base, cela représente une bonne centaine de cartes de moins que l'année précédente. Cette décision a deux raisons. Tout d'abord, dans notre étude des obstacles qui limitent l'accès au jeu, la rapidité de publication des nouvelles cartes jouait un rôle important. Si un nouveau joueur se sent vite submergé, il abandonne et ne retente pas l'expérience. Un débutant a toujours du affronter un certain nombre d'obstacles, et ce depuis les débuts de **Magic**, mais aujourd'hui, si par exemple il découvre le jeu au mois de juillet de cette année, il se retrouve face à un environnement en Standard représentant plus de 2 100 cartes. Publier moins de cartes est tout simplement un des moyens les plus faciles de lui faciliter l'accès au jeu.

Ensuite, il faut savoir que les joueurs existants partagent cet avis : nous publions trop de cartes. Même les plus aguerris commencent à avoir des problèmes à suivre le rythme. Comme le montre le graphique ci-dessus, la quantité de cartes produites ces dernières années a augmenté. Et nous en sommes donc arrivés au point où nous publions trop de cartes *à la fois* pour les débutants et les joueurs expérimentés.

Ce changement va nous aider à trouver un bon équilibre. Mais pourquoi choisir une quantité inférieure à celle qui avait été notre moyenne pendant tant d'années ? Parce que nous avons voulu garder un peu de marge au cas où nous aurions des idées intéressantes comme les cartes « décalées dans le temps » de *Spirale temporelle* ou la structure en mini-blocs de *Lorwyn* / *Sombrelande*. 519 cartes, ce n'est pas notre maximum, c'est notre chiffre de base. 

Les plus observateurs d'entre vous auront remarqué que l'annonce officielle indique que la taille de la prochaine édition de base est encore inconnue. Alors pourquoi y a-t-il un nombre sur mon tableau ? Parce que faisant partie de l'équipe qui travaille dessus, je suis à peu près sûr qu'elle contiendra 229 cartes, mais tant que l'édition de base n'est pas finalisée officiellement, son contenu est toujours officiellement indéterminé. Néanmoins, même si les quantités sont légèrement modifiées d'ici-là, nous respecterons notre nouvelle philosophie « moins de cartes publiées ». 

### Deuxième changement : un nouveau niveau de rareté appelé rare mythique

Pour attirer les nouveaux joueurs, il est aussi important de comprendre l'environnement auquel ils appartiennent. Quand **Magic** a commencé, le jeu avait le luxe de pouvoir se définir parce qu'il était le premier de son espèce. Ce n'est plus le cas aujourd'hui. Les jeux de cartes à jouer et à collectionner font partie d'un genre établi. Autrefois, la majorité des joueurs qui essayaient pour la première fois un jeu de cartes à jouer et à collectionner le faisaient avec **Magic**. Avec l'explosion des jeux de ce type, surtout ceux qui sont destinés aux plus jeunes, ce n'est plus vrai. 

Nous avons fini par réaliser que définir **Magic** uniquement par rapport à lui-même était un luxe qu'on ne pouvait plus se permettre. Aujourd'hui, le jeu de cartes à jouer et à collectionner a créé ses propres standards, nés de décisions prises après la création de **Magic**, la rareté figurant parmi les meilleurs exemples. L'idée d'un JCC avec uniquement trois niveaux de rareté est « antique ». (Et avant de recevoir une autre vague de courriers, je sais que techniquement, le terrain de base représente une quatrième rareté ; il n'est pas pris en compte dans cette discussion.) **Magic** est le seul jeu de cartes à jouer et à collectionner à encore avoir uniquement trois niveaux de rareté. Pour rester compétitifs et attirer de nouveaux joueurs, nous devons nous adapter aux standards de l'industrie.

En quoi ces « standards de l'industrie » permettent d'acquérir de nouveaux joueurs ? Deux réponses à cette question. D'abord, il y a l'attente. La majorité des joueurs qui vont découvrir **Magic** connaissent déjà ces standards. Il est donc logique qu'ils s'attendent à les retrouver dans tout nouveau jeu de cartes à jouer et à collectionner qu'ils essaient. Comme je le dis souvent dans cette chronique, répondre aux attentes des joueurs est primordial. Ensuite, si un élément devient un standard de l'industrie, c'est généralement pour une bonne raison : il fonctionne. Savoir que dans chaque boîte de jeu, il y a le potentiel de trouver matière à vous vanter devant vos amis est un aspect très attrayant qui aide à décider les nouveaux joueurs. 

La bonne nouvelle, c'est que nous avons trouvé un moyen qui nous permet d'augmenter la quantité des niveaux de rareté sans affecter l'impression des cartes par rapport à aujourd'hui. En vérifiant les chiffres en détails, on se rend compte que **Magic** a utilisé le mot « rare » pour décrire un éventail de raretés extrêmement large. Pour comprendre où je veux en venir dans le contexte, voici un tableau représentant toutes les extensions de **Magic** disponibles en Standard, avec la quantité de cartes rares correspondant à chaque extension.

![](https://i.ormos.uk/58/c4/58c4711dc82d9280365a6d84a3940503b8133c6c2f59d271150a10b752b005f5.gif)

Comme vous pouvez le constater, « rare » veut dire bien des choses. Les chiffres les plus hauts sont plus de trois fois plus élevés que les plus bas. Ce graphique nous a permis de déterminer qu'il était possible d'ajouter un nouveau niveau de rareté sans imprimer des cartes en quantités moins importantes qu'à l'heure actuelle. Pour vous l'expliquer, le mieux, c'est de vous montrer l'ancien système et le nouveau côte à côte. La rareté de l'extension de l'extension de gauche correspond à la nouvelle rareté indiquée à droite.  

<table><tbody><tr><td><b>Ancien système</b></td>&#10;<td><b>Nouveau système</b></td>&#10;</tr>&#10;<tr><td>Rare <i>Dixième édition</i></td>&#10;<td>Rare mythique, grosse extension</td>&#10;</tr>&#10;<tr><td>Rare <i>Sombrelande</i></td>&#10;<td>Rare mythique, petite extension</td>&#10;</tr>&#10;<tr><td>Rare<i> Vision de l'avenir</i></td>&#10;<td>Rare, grosse extension</td>&#10;</tr>&#10;<tr><td>Rare <i>Chaos planaire</i></td>&#10;<td>Rare, petite extension </td>&#10;</tr>&#10;</tbody></table>

  
 Maintenant que nous avons une échelle des raretés, voyons combien de cartes de chaque rareté seront contenues dans *Les éclats* *d'Alara*.

Courantes – 101  
 Inhabituelles – 60  
 Rares – 53  
 Rares mythiques – 15

Avec quelle fréquence trouve-t-on ces cartes ? Il y aura dix courantes par booster (oui, je sais, je vous expliquerai dans la partie suivante). Il y aura trois inhabituelles et une rare par booster, mais dans un booster sur huit environ, elle sera remplacée par une rare mythique. Avec un booster sur huit, on pourrait croire que les rares mythiques sont sept fois plus rares que les rares. Ce n'est pas le cas ; elles ne sont que deux fois plus rares. (C'est compliqué, mais c'est lié à la manière dont la feuille de cartes est imprimée et au fait qu'il y a plus de cartes rares que de rares mythiques.)

Maintenant, jetons un coup d'œil à « Papier », un exemple de petite extension dans ce nouveau monde. 

Courantes – 60  
 Inhabituelles – 40  
 Rares – 35  
 Rares mythiques – 10

La répartition des raretés est la même que pour *Les éclats d'Alara*, y compris la fréquence avec laquelle la rare mythique remplacera la carte rare. 

Ce qui nous amène à la question suivante : comment les cartes sont-elles réparties entre rares et rares mythiques ? Ou plus exactement, quels types de cartes vont devenir des rares mythiques ? Nous voulons que les rares mythiques aient une saveur à la fois spéciale et unique. Ce qui veut dire qu'en général, ce traitement sera réservé à des cartes comme les planeswalkers, une majeure partie des légendes, les créatures et les sorts les plus épiques. Elles ne se limiteront *pas* à une liste des cartes les plus puissantes en tournoi.

Nous avons aussi décidé que certaines cartes ne seront jamais des rares mythiques. Pour la plupart, ce sont les cartes utilitaires, autrement dit les cartes qui ont une fonction universelle. Parmi les exemples de cette catégorie, on trouvera les cycles de terrains doubles et des cartes telles que le Mutecaveau ou Carboniser. Cela résout aussi le problème que certains joueurs avaient avec certaines rares comme les terrains doubles. Comme nous publions moins de cartes par extension, dans ce nouveau monde, les cartes rares seront plus faciles à acquérir parce qu'une rare apparaîtra en moyenne 25% plus souvent dans une grosse extension. 

Ce qui nous conduit à la question suivant : les rares mythiques existeront-elles aussi en version Premium ? La réponse est oui. En fait, non seulement elles existeront à la fois en version normale et Premium, mais les versions Premium seront légèrement plus fréquentes. (La quantité combinée de rares Premium et de rares mythiques Premium que vous aurez à partir de l'extension *Les éclats d'Alara* sera plus élevée que la quantité de rares Premium actuelle.)

Une dernière question sur les rares mythiques : les rares mythiques auront-elles une nouvelle couleur de symbole d'extension ? Oui. Laquelle ? Je vous promets de vous la montrer avant la fin de cet article. 

### Troisième changement : une carte de terrain de base à la place d'une carte courante dans tous les boosters

C'est un changement que nous avons mis en place dans l'édition de base depuis la *Septième édition*. La raison était toute simple : les débutants avaient des problèmes à obtenir des terrains. Sans terrain, on ne peut pas jouer — on ne peut pas trouver pire obstacle quand on commence à jouer. Avant la *Septième édition*, nous partions du principe que les produits contenant des terrains de base ne manquaient pas sur le marché. C'était une erreur de jugement pour deux raisons. Premièrement, le nouveau joueur n'avait aucun moyen de savoir quel produit contenait des terrains de base, et peu de gens achètent un deuxième produit quand le premier n'est pas auto-suffisant. Deuxièmement, tous les magasins ne vendent pas toute la gamme de produits **Magic**. Certaines boutiques, par exemple, ne vendent que des boosters, ce qui veut dire qu'un joueur qui ne connaît que ce magasin n'a aucun moyen de trouver des terrains.

Maintenant que nous comprenons mieux comment les joueurs découvrent le jeu, il devient clair que si nous voulons garantir des terrains aux débutants, il faut les inclure dans le produit principalement acheté. Par conséquent, à partir de l'extension *Les éclats d'Alara*, chaque booster contiendra une rare (parfois remplacée par une rare mythique), trois inhabituelles, dix courantes, et un terrain de base. Cette répartition sera ensuite appliquée à chaque édition de base et à chaque extension (grosse ou petite).

### Quatrième changement : transformation des decks à thème en packs d'intro

Depuis l'introduction des decks préconstruits, les decks à thème ont dû servir deux maîtres. Ils étaient conçus à la fois comme un produit de niveau Découverte pour aider les nouveaux joueurs à entrer dans le jeu et comme un échantillon pour permettre aux joueurs établis ou qui avaient cessé de jouer d'essayer les thèmes et les mécaniques de la nouvelle extension. Le problème, c'est que ce double rôle ne nous permettait pas de maximiser l'efficacité des decks pour un groupe ou l'autre. L'accent mis sur l'importance d'attirer de nouveaux joueurs a enfin mis fin à cette situation. 

Quand nous avons étudié le placement des produits en magasin, nous avons réalisé que le manque de produits de niveau Découverte disponibles à la vente créait une baisse de l'intérêt des joueurs (surtout dans les supermarchés). Potentiellement, c'est un énorme obstacle pour les débutants, et il s'est révélé crucial de nous assurer qu'un produit de ce type soit disponible de manière constante. Après de longues délibérations, il a été décidé de donner aux decks à thème l'occasion de se concentrer sur leur côté produit de niveau Découverte. Après tout, comme ils accompagnent la sortie de chaque extension, ils garantissent une présence continue du produit désiré dans les rayons.

Dès *Les éclats d'Alara*, les decks à thème seront revampés pour devenir un nouveau produit appelé le « pack d'intro », dont le but est d'aider les débutants à apprendre le jeu. Pour ce faire, nous avons repensé entièrement le contenu d'un produit de niveau Découverte, ce qui a entraîné des changements importants de présentation. Pour l'acheteur de deck à thème habituel, les packs d'intro contiendront toujours un deck préconstruit qui échantillonne les nouveaux thèmes et les nouvelles mécaniques de l'extension et nous avons réussi à augmenter la valeur générale du produit (patience, ça vient !) tout en maintenant son prix. Ceci dit, ce deck fait l'objet de modifications importantes. 

Pour vous rafraîchir la mémoire, voici la composition d'un deck à thème de *Sombrelande*:

2 rares  
 13 inhabituelles  
 45 courantes / terrains  
 1 terrain Premium

Voici maintenant la composition d'un pack d'intro pour *Les éclats d'Alara*:

![](https://i.ormos.uk/43/8e/438ec375bd489382c7d84c784e370b996897e343401bb6a59c6a32c59c141272.jpg)1 rare Premium  
 1 rare non-Premium  
 7 inhabituelles  
 32 courantes / terrains  
 1 booster *Les éclats d'Alara*

On remarque tout de suite deux différences majeures. D'abord, le deck du pack d'intro contient 47 cartes au lieu des 61 cartes du deck à thème. Ensuite, il contient aussi un booster (ce qui amène le total de cartes du pack à 56). En tenant compte des cartes du booster, le pack d'intro a trois inhabituelles de moins, deux courantes de moins, et pas de terrain Premium quand on le compare au deck à thème. Mais en échange, il gagne une rare supplémentaire, et c'est une Premium en plus.

Pourquoi ce changement ? Commençons par le booster. Pour le débutant, le deck préconstruit classique est un peu trompeur quant à sa nature : même si c'est un deck complet, il ne représente pas les possibilités d'un jeu de cartes à jouer et à collectionner. Nous voulions montrer au nouveau joueur le potentiel de jeu de son deck. C'est pour cette raison que nous avons pensé qu'il était primordial de lui mettre un booster dans les mains. C'est uniquement en ouvrant un booster de cartes assorties aléatoirement qu'à notre avis, il va avoir le meilleur avant-goût de **Magic**.

De plus, nous étions convaincus que le pack d'intro devait être conçu pour vous encourager à modifier votre deck. C'est une mission en partie remplie par l'ajout du booster, mais aussi par la réduction du deck à moins de soixante cartes. Cette taille plus petite encourage les joueurs à ajouter des cartes pour parvenir à soixante (encore une autre leçon que nous avons apprise avec les éditions de base). 

Le concept du pack d'intro entraîne aussi un autre changement de contenu, avec la présence de deux feuillets stratégiques. L'un d'eux contient toutes les informations que vous avez l'habitude de trouver dans les decks à thème (le fonctionnement des mécaniques, les listes de deck, etc.), mais il y a à présent un deuxième feuillet réservé aux débutants qui leur apprend à jouer et à adapter leur deck, permettant ainsi au pack d'intro de se doubler d'un produit explicatif de premier achat pour le novice. 

Le remplacement du terrain Premium par une carte rare Premium est une conséquence de la conception du nouveau packaging. Nous voulions créer une boîte à fenêtre qui permettrait au joueur de voir une des cartes. Une carte rare était tout simplement le candidat le plus évident pour remplir cette fonction (et une bonne tant qu'à faire), alors nous n'avons pas hésité. En regardant le produit fini, nous sommes maintenant convaincus d'avoir à la fois amélioré la valeur du produit *et* de l'avoir rendu plus accessible et plus attractif pour les nouveaux joueurs.

### Et voilà !

Je réalise que je viens de vous balancer des tonnes d'informations, mais je pensais qu'il était important que vous sachiez pourquoi nous procédions à ces changements. Au final, si toutes les modifications dont je viens de discuter aujourd'hui ont été apportées, c'est parce que nous croyons fermement qu'elles sont dans le meilleur intérêt du jeu à long terme.

Maintenant, c'est votre tour. Nous aimerions avoir vos avis. Utilisez la page de discussion d'aujourd'hui pour donner votre opinion à la fois sur ces modifications et nous suggérer d'autres détails qui pourraient résoudre les problèmes d'acquisition des nouveaux joueurs. 

Retrouvez-moi la semaine prochaine. Nous aborderons un sujet un peu moins substantiel.

Attendez une minute... J'ai comme l'impression que j'oublie quelque chose. Oh, oui. Cliquez ici pour voir ce à quoi le symbole d'extension de la rare mythique va ressembler. 

![Sarkhan Vol](https://i.ormos.uk/1d/0f/1d0f2cb56b4d05bef7d842629120cb96460f58c3b0e64a845a3886be40cf0cec.jpg "Sarkhan Vol")

Bien, cette fois, j'ai vraiment terminé.

En attendant la prochaine rubrique, puissiez-vous comprendre que le changement est un mal nécessaire.

Mark Rosewater
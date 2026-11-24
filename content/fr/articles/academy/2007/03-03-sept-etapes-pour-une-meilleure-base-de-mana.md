---
id: yajjsnep
kind: article
lang: fr
path: /fr/articles/academy/2007/03-03-sept-etapes-pour-une-meilleure-base-de-mana
title: Sept étapes pour une meilleure base de mana
published: '2007-03-03'
column_slug: academy
column: Magic Academy
authors:
- slug: jeffcunningham
  name: Jeff Cunningham
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/academy/27
    lang_detected: fr
    capture_id: 1846592
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/27
    captured_at: '2008-05-19 08:02:37+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/academy/27
    lang_detected: fr
    capture_id: 1846592
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/27
    captured_at: '2008-05-19 08:02:37+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/academy/27
    lang_detected: fr
    capture_id: 1846592
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/27
    captured_at: '2008-05-19 08:02:37+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/academy/27
    lang_detected: fr
    capture_id: 1846592
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/27
    captured_at: '2008-05-19 08:02:37+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: yajjsnep
  url: http://www.wizards.com/default.asp?x=mtgcom/academy/27
  page_key: wizards.com/default.asp?x=mtgcom/academy/27
  lang: fr
  template: classic_asp
  captured_at: '2008-05-19 08:02:37+00'
  capture_id: 1846592
  wayback_url: https://web.archive.org/web/20080519080237id_/http://www.wizards.com/default.asp?x=mtgcom/academy/27
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: yajjsnep
  capture_id: 1846592
  url: http://www.wizards.com/default.asp?x=mtgcom/academy/27
  wayback_url: https://web.archive.org/web/20080519080237id_/http://www.wizards.com/default.asp?x=mtgcom/academy/27
  captured_at: '2008-05-19 08:02:37+00'
  template: classic_asp
  sha256: 8e5617dd305025f74f8de493c63d872f6fc37ceb4e047f3fed6d43453d4075f7
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Scrying_Sheets')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Frozen_Shade')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Karplusan_Forest')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Battlefield_Forge')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
* * *

Bonjour et bienvenue à Magic Academy !

Cette semaine, nous allons vous présenter des étapes qui vous permettront de construire une base de mana grâce aux principes détaillés dans Introduction à la base de mana, [Première partie](/en/articles/academy/2007/02-17-introduction-to-mana-base) et [Deuxième partie](/en/articles/academy/2007/02-24-introduction-to-mana-base-part-2). 

![Overgrowth](https://i.ormos.uk/31/f4/31f46d4a0e1cceee3f4e23e5d8160d4170367563b579e0bb7c705e644708bf73.jpg)

Il est important de noter, avant de rentrer dans des considérations de système infaillible de construction de mana, que les bases de mana résistent aux approches systématiques. La base de mana d'un deck est très spécifique. Elle dépend d'une importante variété de facteurs : cartes uniques, interactions uniques entre ces cartes, cartes potentiellement disponibles dans le format, pour ne citer qu'eux. C'est pourquoi un guide de construction de base de mana doit toujours rester suffisamment général. Certaines règles peuvent vous aider jusqu'à un certain point, mais si vous pensez trouver une solution miracle dans ce lignes, vous vous fourrez le doigt dans l'œil : elle n'existe pas.

Chaque base de mana présente un nouveau défi spécifique... mais chacun de ces défis a une résolution mathématique. Vu de cette manière, je sais, ça ne donne pas envie. Beaucoup de pros adorent tester des théories de draft ou créer de nouveaux decks, mais ils redoutent de devoir *calculer* une simple base de mana. D'autres trouvent en revanche cette tâche étrangement réconfortante ; il faut dire que quand les théories peuvent être descendues en flammes et que le metagame peut semer le chaos dans un tournoi, savoir qu’une bonne base de mana améliore toujours le deck, quel qu'il soit, c’est plutôt une bonne nouvelle.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Scrying Sheets" src="https://i.ormos.uk/50/bf/50bf692b0375865ac36b62334d34fe00ef806a3353bab934b1a061be77a9201a.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Par où commencer ? Même si un deck termine sa genèse avec 60 cartes de mana et non-mana travaillant en équipe, l’idée initiale commence généralement avec des cartes non-mana. Quand un joueur a une idée de deck, elle vient généralement du potentiel d'une puissante combo ou d'une approche ‘beatdown’ intéressante, mais rarement d'une base de mana particulière. La base de mana sert toujours le deck, et jamais l'inverse. 

Ceci dit, les compromis ne manquent pas. Dans un deck Pacte de la tombe, par exemple, l’idée d’avoir un Chlorophant et un Élémental de l'aube dans un même deck, dans la plupart des formats, ne vaut même pas la peine d’être approfondie. Pour construire une base de mana, le joueur rassemble des cartes non-terrain et de quoi les alimenter raisonnablement dans le format concerné (à moins de vouloir prendre des risques et de voir où la chance vous mène), en espérant avoir la bonne proportion de mana. 

Cependant, souvent, le mana est incorporé dès la conception initiale du deck, dans un contexte plus général : un accélérateur particulier peut s'avérer intéressant (par exemple, *ce deck fonctionnera si je peux utiliser les terrains de sacrifice d'Invasion*), la capacité d'un terrain non-base peut être exigée (il existe des decks basés sur les Strates de scrutation), ou certaines considérations de mana sont tout simplement évidentes (si vous ne n’allez jouer que quatre Guerriers elfes en vert, il est préférable de les remplacer par quatre cartes inférieures d'une autre couleur pour rendre votre base de mana plus efficace). Donc, on peut dire pour résumer qu’on commence la construction d’un deck avec des cartes non-mana, et qu’on jongle ensuite avec les deux aspects (mana et non-mana) jusqu’à obtenir quelque chose qui fonctionne le mieux possible.

### 1\. Assurez-vous que votre deck est au moins raisonnablement adapté au format.

Dans les formats complexes, les terrains multicolores peuvent faciliter les nécessités d'inclusion de couleurs les plus extrêmes. Dans les plus simples (comme Bloc Construit ou Standard sans les terrains multicolores de Ravnica), les options sont moins nombreuses, alors vous devrez faire plus attention. En format Étendu, il serait par exemple possible d’avoir un Guerrier elfe et un Diablotin flétri dans le même deck. En Standard, ou dans un format plus restreint, cela deviendrait tout de suite un problème évident.

Vérifiez toujours avant même de commencer si les cartes non-mana que vous voulez utiliser vont fonctionner avec une base de mana standard. 

### 2\. Déterminez en gros l'espace que vous allez réserver au mana dans votre deck.

![Far_Wanderings](https://i.ormos.uk/8f/be/8fbec01a46e67e14883c16871e12ac80f68da8b0bca0fe51c8d4eb44c15acec5.jpg)

Pour ce faire, vous avez une liste des cartes non-mana potentielles que vous voulez inclure dans votre deck…

En réfléchissant à l’espace que vous allez réserver aux terrains, vous vous demandez en réalité si vous devez retirer ou ajouter des cartes à cette liste ?

Voilà quelques éléments dont il faut tenir compte :

> *   Ce deck va-t-il devoir utiliser l'accélération ? Autrement dit, est-ce qu'il contient des sorts que vous voulez lancer tôt dans la partie ? Ou a-t-il des trous dans sa courbe de mana que l'accélération aiderait à combler ? Ou reste-t-il de la place qui vous permette d'y ajouter de l'accélération ? Rappelez-vous, l'accélération ne remplace pas le mana et nécessite donc de lui réserver des places dans l’espace des sorts non-mana.

Souvent, les joueurs incluent l'accélération dans leur liste de deck avant même de songer au mana, puis ils modifient le deck plus tard dans la construction si cela s’avère nécessaire.

> *   Y a-t-il des sorts coûteux dans votre liste de deck ? Si c'est le cas, vous aurez besoin de suffisamment de mana pour les lancer aussi souvent que possible.
> *   Allez-vous jouer beaucoup de sorts de manipulation/pioche de cartes bon marché ? Si votre stratégie est d’obtenir des cartes supplémentaires dès les premiers tours grâce à des sorts comme le Remue-méninge et la Toupie de divination du sensei, alors il est possible d’utiliser moins de terrains.
> *   Combien de temps la partie va-t-elle de durer ? La relation longueur de partie et mana est assez complexe. D'un côté, un deck Agro qui gagne une partie en quelques tours justifie une utilisation de terrains plus intensive parce qu’il ne risque pas d’être submergé par les terrains plus tard dans la partie, et un deck Contrôle se prépare à une partie longue peut jouer moins de terrains parce qu'il a plus de temps pour les piocher. De l'autre, même si ce raisonnement fonctionne jusqu'à un certain point (Agro et Contrôle n'ont pas tant de différences de mana qu'on pourrait le penser avec des sorts de coûts relativement similaires), un deck Agro doit quand même avoir une bonne main de départ pour gagner une partie courte, et un deck Contrôle doit mettre en jeu des cartes le plus tôt possible pour s'assurer de survivre jusqu'en fin de partie !

![Mana_Severance](https://i.ormos.uk/58/81/5881bdd933af5e2ec4a5c419be0d7646c26078eb5ef98d57b2064f5540a1a600.jpg)

Certes, des curiosités font leur apparition de temps en temps : des decks avec moins de 16 terrains, ou plus de 30, mais la plupart d’entre eux contiennent entre 22 et 26 sources de mana. (22 c'est le minimum pour un deck Agro sans accélération, et 26+ c'est le maximum pour un deck Contrôle qui l'utilise.)

Faites aussi attention aux éléments de votre deck (certaines cartes) qui vous feront jouer plus ou moins de terrains.

Tentez d'évaluer l'espace que vous devriez réserver au mana (puis ajustez si nécessaire).

  
  

### 3\. Déterminez, en gros, quelles quantités de mana coloré vont vous être utiles.

De quelle quantité de mana coloré de chaque couleur avez-vous besoin pour jouer tous vos sorts ? Quelle proportion de terrains est nécessaire pour chaque couleur ? Combien de terrains multicolores et lesquels allez-vous utiliser, le cas échéant ? Aurez-vous de la place à réserver à des terrains incolores avec des capacités ?

Voici quelques éléments dont vous devez tenir compte :

> *   Combien de cartes de chaque couleur avez-vous dans votre jeu ? Cela devrait vous donner une idée générale des proportions de mana à utiliser, mais rappelez-vous de toujours biaiser vers la moyenne. Même si vous n'avez que 4 cartes rouges et 32 vertes, vous voudrez jouer plus de 4/36 manas rouges.
> *   Combien de cartes sont exigeantes en mana coloré et quelles sont-elles ? Alimenter un sort à double mana coloré, surtout quand il ne coûte pas très cher, est plus facile à gérer dans une couleur omniprésente (une couleur principale), mais sera très difficile dans une couleur marginale. Celle-ci ne pourra dans ce cas plus dépendre uniquement de filtres de mana (par exemple, une Croissance luxuriante qui va chercher un terrain) et jouer cette couleur impliquera d’augmenter de manière considérable le nombre de sources adéquates.

Sans prendre en compte les proportions, certains decks ont des exigences de couleur plus importantes que d'autres. Si votre deck rouge/vert n’utilise que des sorts à un mana coloré, votre base de mana sera certainement assez stable pour ajouter quelques terrains incolores avec des capacités. S'il contient plusieurs sorts à double mana coloré (au moins), vous serez probablement obligé d'y consacrer des terrains multicolores.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/d2/a8/d2a8edcd37e08f26e9bfe4a0bd0e9dbd1e50e030448b5c595dfde98394339074.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/81/b2/81b25d31d57a840febf1bb928dad7785877d538d27c202b2fb513d5c36250610.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/82/8e/828e1b258c45956b4dfcf7c845615fe5438d3a5abfe41924eac2dd17ac3f17d5.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/4e/02/4e02de799db0661d48c6bebe0236ce19450e235fa0ffd78cdb1020e005094477.jpg"></td>&#10;<td><a><img alt="Frozen Shade" src="https://i.ormos.uk/9b/74/9b74f4f5a5e58b4f780df70c8f2aeaed4b2448512dd266ab9615f7f33e168600.jpg"></a></td>&#10;<td><img alt="" src="https://i.ormos.uk/1f/2e/1f2e15ffa4ff562b309115825209450a9a30f64b72b9f0981a43a3dbd04b7cb7.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/33/54/3354a42c7b89603c538b1b981942e781012db4791e3e0f368b48f79a18d13c9e.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/86/12/861268c55a3cfea18fe45f2a7dac904d3c36f5df336597d7ce7ebcceae513637.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/55/d0/55d0c7b06f91c98f072bf91c089463e4a2aace798bb3ac296634446b51616c7e.jpg"></td>&#10;</tr>&#10;</tbody></table>

Assurez-vous aussi de prendre en compte les sorts qui vous encouragent à jouer plus une couleur de mana, comme l'Ombre glaciale.

> *   Les cartes de chaque couleur sont-elles coûteuses ? Plus un sort est cher, plus vous aurez pioché de cartes avant d'avoir besoin de le jouer, plus vous aurez de chances de piocher le terrain approprié, et moins vous aurez besoin de soutien couleur.

Répondre aux exigences de mana utilise le principe suivant : pouvoir jouer tous les sorts de votre main. Cela signifie que, même si vous ne jouez que deux sorts blancs dans tout votre deck, si vous les piochez, vous voulez être en mesure de les jouer. Si vous jouiez une quantité proportionnelle de mana blanc, vos chances de piocher à la fois le mana et les sorts seraient très minces. Pour éviter ce problème, il faut avoir suffisamment de mana blanc, même si vous ne piochez pas ces deux sorts. Une carte blanche en main sans mana blanc en jeu est une carte morte. Une plaine en jeu sans carte blanche en main peut toujours être utile.

Au premier tour, vous voyez 7 ou 8 cartes, et comme vous jouez un deck de 60 cartes, pour récupérer une plaine en moyenne à chaque partie, il faut en ajouter au moins 8 dans votre deck (moins si vous considérez que le coût de mana d’une carte d’accent sera généralement élevé, et plus si vous voulez avoir un peu de sécurité).

8 sources de mana, c'est le minimum requis pour alimenter un accent de couleur mineur. Même si vous ne jouez qu'une plaine, vous pouvez ajouter 4 Croissances luxuriantes, quelques Cachets, ou tout autre générateur de mana de votre choix.

À l'inverse, en prenant les mêmes éléments en considération, même pour une couleur principale avec beaucoup de cartes et du mana coloré multiple, 16-24 sources sont amplement suffisantes.

N'oubliez pas de prendre en compte les spécificités de votre deck.

Essayez d'évaluer combien de sources de mana vous voulez attribuer à chaque couleur. (Et n'oubliez pas, certaines d’entre elles peuvent satisfaire toutes les couleurs en même temps, si vous êtes prêt à en payer le prix !)

### 4\. Faites un premier essai.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Karplusan Forest" src="https://i.ormos.uk/bd/01/bd018a8c38037379b0cbf8a5e58a3e8d12fb34cd9f7f024a77f3b99c930b9eb7.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Maintenant que vous avez une idée générale de l'espace disponible et de la quantité de mana de couleur dont vous avez besoin, essayez de constituer votre base de mana.

Vous pouvez par exemple vous fixer un objectif : 'J'ai 26 possibilités de cartes de mana, et je veux en réserver 3 à l'accélération. Il me faut 10 sources blanches, 20 sources bleues et 13 sources rouges. À quoi mon deck ressemble-t-il ?'

Assurez-vous de bien tenir compte de tous les terrains, de l'accélération et des filtres disponibles dans le format. Si un terrain est particulièrement bon (par exemple, une Forêt de Karpluse dans un deck R/V), ajoutez-le tout de suite. Si vous avez trop de 'cartes géniales’, choisissez celles qui feront le mieux l'affaire dans votre cas particulier.

i. Quels terrains multiples utiliser ? *(Landes d'Adarkar, Fontaine sacrée ou Cour de la chancellerie d'Azorius)*

Le deck que vous êtes en train de créer joue un rôle important à ce moment de la construction. Tous ces terrains produisent du mana bleu et blanc. La question est, lequel aura le moins d’inconvénient dans votre deck ? Souvent, le niveau de puissance des cartes est tellement similaire que le compromis reste la meilleure solution : avoir un exemplaire des Landes d'Adarkar et de la Fontaine sacrée dans une main de départ vous donnera plus d'options que deux exemplaires d'une seule carte.

> *   Pensez à la courbe de mana. Si vous n'avez pas de sorts à un mana, vous pourrez utiliser la Fontaine sacrée sans son aspect douleur la plupart du temps. Si les Landes d'Adarkar ne vous servent que pour du mana incolore, mais que vous voulez vous garantir un accès au bleu et au blanc dans des situations plus spécifiques (par exemple, pour un soupçon de couleur), les Landes seront probablement le bon choix.
> *   Pensez aux niveaux de puissance des terrains. Sur une échelle générale, la Fontaine sacrée est probablement un peu plus puissante que les Landes d'Adarkar, et bien plus que la Tour Côtière. Vous voudrez toujours réserver une place aux terrains plus puissants.
> *   Pensez aux aspects uniques des terrains. La Cour de la chancellerie d'Azorius affecte votre base de mana d'une manière très particulière. La Fontaine sacrée a des types de terrain de base (île   et plaine), contrairement à la plupart des terrains non-base, ce qui veut dire qu'elle peut être trouvée par des moyens qui ne fonctionnent pas sur les terrains non-base (par exemple, un Don de domaines).

ii. Quel cocktail de terrains multicolores utiliser ? *(Landes d'Adarkar, Brisants shivâns, Forge de campagne)*

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Battlefield Forge" src="https://i.ormos.uk/09/ca/09ca46d92ff368c402518eb9b560bfa2f040647ce9c502307842ae52d27ab40e.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

C'est une question difficile qui a une réponse différente pour chaque nouveau deck créé. Si vous ajoutez une source rouge, une source bleue et une source blanche à un deck, quel terrain multicolore et quel terrain de base devriez-vous utiliser ?

> *   Pensez à réduire les inconvénients des terrains (les blessures dans ce cas) le plus possible. Supposons que, bien que vous vouliez jouer tous vos sorts quand vous les piochez, vous savez que vous utiliserez principalement du mana rouge, et du blanc et du bleu de temps en temps seulement. Cela implique plusieurs sources de mana rouge fiables et sans douleur (des montagnes) pour commencer (et donc, pour équilibrer, les Landes d'Adarkar) mais aussi un cocktail composé de Brisants et de Forges (et des îles et des plaines) pour augmenter vos chances de lancer vos sorts bleus et blancs plus souvent.
> *   Pensez à maximiser le lancement de vos sorts. Cet aspect est si complexe qu'il mériterait tout un article, mais je vais au moins vous présenter le problème. Supposons que vous jouiez un Filelame boros. Cela vous oblige à avoir un terrain générateur de rouge et un terrain générateur de blanc au tour deux (toujours dans l’optique de jouer la carte aussitôt que possible). D'un côté, il semblerait que la Forge de campagne soit le terrain idéal : elle vous permet de jouer le Filelame avec une montagne ou une plaine seulement. D'un autre côté, comme vous avez un espace mana limité, réunir deux cartes en une (alors qu’il vous faut les deux pour jouer le Filelame) diminue vos chances de récupérer le terrain en temps et en heure. Ce sont deux facteurs à prendre en compte, mais il faut se rappeler qu'en règle générale, jouer autant de terrains possibles qui puissent générer les deux couleurs dont vous avez besoin (dans ce cas, le rouge et le blanc) est un avantage compensé par une grosse quantité de terrains qui génèrent une couleur ou l'autre et une faible quantité de terrains qui n'en génèrent aucune.
> *   Aussi, pensez aux cartes que vous utiliserez en même temps. Par exemple, si vous jouez un deck contenant à la fois les Hommes volants et la Dîme de mana, il vaudra mieux jouer des Brisants shivâns et une plaine que des Landes d'Adarkar et une montagne, parce que la première configuration me permet de jouer les deux sorts et pas l'autre.

Parfois, si le deck n'a aucune exigence spécifique, ces terrains seront interchangeables. (Landes d'Adarkar + montagne ou Brisants shivâns + plaine). Et bien entendu, avoir à la fois un exemplaire des Brisants shivâns et des Landes d'Adarkar en main nous donne plus d'options qu'avoir deux exemplaires d'un seul. Dans une situation où cela ne fait aucune différence, un cocktail est toujours souhaitable. 

iii. Quel terrain de base utiliser ? (*montagne, plaine, île)*

> *   Pensez aux cartes de terrain de base irremplaçables (par exemple le Dragon rajhi a besoin de montagnes) et aux sorts de recherche filtreurs de mana qui trouvent uniquement des terrains de base (ce qui vous encourage à jouer au moins un terrain de base de chaque couleur dont vous pourriez avoir besoin).
> *   Pensez aux terrains que vous allez le plus utiliser. Si vous avez l'intention d'utiliser du mana vert à chaque tour, assurez-vous qu'il provienne d'une source stable et indolore.

Comment décider quels terrains utiliser ? Supposons une fois de plus que vous ayez uniquement 3 places pour deux sources rouges, une source blanche et une source bleue. Vous devez décider (i) quels terrains multicolores jouer (Landes d'Adarkar ou Fontaine sacrée ou Cour de la chancellerie d'Azorius) (ii) quel cocktail de terrains multicolores utiliser (Landes d'Adarkar ou Brisants shivâns ou Forge de campagne) et (iii) quelle source sera un terrain de base.

Si vos exigences de mana sont facilement satisfaites, vous pouvez ajouter des terrains non-base avec des capacités ou introduire une autre couleur qui augmente la puissance et la versatilité de votre deck sans lui ajouter de faiblesse. 

### 5\. Affinez.

Prenez une minute pour comparer votre base de mana et le reste de votre deck. Est-ce que le tout fonctionne ?

Quelques méthodes de vérification :

> *   Êtes-vous contraint d'utiliser tant de terrains multicolores que leurs inconvénients normalement négligeables (comme subir une blessure à chaque fois que vous engagez les Landes d'Adarkar ou les Brisants shivans pour du mana coloré) deviennent des obstacles importants ?
> *   Pensez-vous que vous pourrez lancer tous vos sorts au tour où vous voulez les lancer ? (Si vous voulez jouer la Colère de Dieu sans problème au tour 3, avez-vous suffisamment d'accélération pour être sûr d'accélérer votre mana au tour deux, suffisamment de mana pour en avoir trois en jeu au tour trois, et suffisamment de mana blanc pour payer ![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif) au tour trois ?)
> *   Voyez-vous des éléments qui pourraient être améliorés ? (Par exemple, une carte qui n'est pas si importante dans votre plan de jeu et qui nécessite beaucoup trop de mana.)

Vous pouvez modifier plusieurs éléments du deck. Vous pouvez toujours revoir votre base de mana ou vous étudier à nouveau votre liste de deck pour la rendre plus jouable.

### 6\. Refaites un passage.

![Attunement](https://i.ormos.uk/11/72/1172405489d8797aa78ab8581b38dd9ffcbfaaba0308001deb43ae28f9b7ce48.jpg)

Recommencez l'opération autant de fois que vous le jugerez nécessaire.

### 7\. Affinez.

L'étape finale peut avoir lieu après un véritable test de jeu. Avez-vous des problèmes récurrents avec ce deck ? Une carte reste-t-elle coincée dans votre main ? Quand vous remarquez ce genre de petits détails, c'est qu'il faut encore peaufiner votre deck.

Retrouvez-moi la semaine prochaine pour le dernier chapitre de cette série : une étude de base de mana qui applique ces principes à un véritable deck. Postez vos listes de decks sur les forums et j'en choisirai un comme exemple.

Jeff
---
id: mgv6z4ea
kind: article
lang: fr
path: /fr/articles/academy/2006/11-11-the-art-of-the-block
title: L’art du bloc
published: '2006-08-12'
column_slug: academy
column: Magic Academy
authors:
- slug: tedknutson
  name: Ted Knutson
translation_of: ev5v4qm6
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/academy/5
    lang_detected: fr
    capture_id: 1847379
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/5,,fr
    captured_at: '2008-05-17 22:29:20+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/academy/5
    lang_detected: fr
    capture_id: 1847379
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/5,,fr
    captured_at: '2008-05-17 22:29:20+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/academy/5
    lang_detected: fr
    capture_id: 1847379
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/5,,fr
    captured_at: '2008-05-17 22:29:20+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/academy/5
    lang_detected: fr
    capture_id: 1847379
    url: http://www.wizards.com/default.asp?x=mtgcom/academy/5,,fr
    captured_at: '2008-05-17 22:29:20+00'
    rule: classic.column_marker
    registry_match: registry.explicit
sources:
- document_id: mgv6z4ea
  url: http://www.wizards.com/default.asp?x=mtgcom/academy/5,,fr
  page_key: wizards.com/default.asp?x=mtgcom/academy/5
  lang: fr
  template: classic_asp
  captured_at: '2008-05-17 22:29:20+00'
  capture_id: 1847379
  wayback_url: https://web.archive.org/web/20080517222920id_/http://www.wizards.com/default.asp?x=mtgcom/academy/5,,fr
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: mgv6z4ea
  capture_id: 1847379
  url: http://www.wizards.com/default.asp?x=mtgcom/academy/5,,fr
  wayback_url: https://web.archive.org/web/20080517222920id_/http://www.wizards.com/default.asp?x=mtgcom/academy/5,,fr
  captured_at: '2008-05-17 22:29:20+00'
  template: classic_asp
  sha256: 395b8615b988b23f4b2af4ed4bf19bfe206a8e0c765a5cc8fcfc6cf2a08a7f41
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Giant_Spider')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Cafard_g%C3%A9ant')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Grizzlis')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Ange_aveuglante')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
* * *

*Magic Academy est une rubrique conçue pour aider les nouveaux joueurs à progresser rapidement en les aidant à accroître leur connaissance du jeu et en les aiguillant vers les sources d’informations disponibles sur le WEB susceptibles de les aider à s’améliorer. Cette rubrique est écrite de façon linéaire, comme un livre, de sorte que chaque leçon est construite à partir des notions apprises dans les articles antérieurs. Dès lors, si vous découvrez tout juste cette rubrique, vous pouvez soit commencer à partir du début, soit jeter un coup d’œil aux articles précédents pour déterminer où vous souhaiteriez commencer. Pour approfondir la question et voir la table des matières des précédentes rubriques, il vous suffit d’aller sur [La Page d’Accueil de Magic Academy](/en/articles/academy/2006/07-14-magic-academy) .* 

 *Magic Academy considère que vous avez déjà joué une partie de Magic. Donc, c’est une rubrique pour les joueurs qui connaissent au moins les règles de base, mais pas pour les joueurs qui n’ont jamais vu le jeu ou à qui on n’a jamais expliqué comment il fonctionne. Si vous êtes un novice à Magic, nous vous conseillons d’aller sur [playmagic.com](http://playmagic.com/) Une fois que vous saurez jouer, revenez à l’Académie et nous prendrons bien soin de vous !*

* * *

Salutations et une nouvelle fois bienvenue à notre rendez-vous hebdomadaire pour le jeu **Magic**. Dans [notre dernier article](/en/articles/academy/2006/11-04-the-dynamics-of-a-turn) , je vous ai accompagné pour un tour de jeu afin de passer en revue de nombreuses règles et de les graver dans vos têtes sans pour autant vous donner un mal de crâne carabiné. Je vous ai aussi promis que nous reviendrions sur la Phase de combat car de nombreuses actions peuvent s’y dérouler. Cette phase mérite que l’on s’y attarde et qu’on apporte bien plus d’explications que je ne pouvais le faire dans l’article précédent. Cette semaine, notre article donc sera centré sur le combat et plus particulièrement sur un sujet bien précis : le bloc.

J’avais initialement prévu de parler des attaques mais, à un moment donné, mon petit cerveau a réalisé que de nombreuses attaques avaient lieu uniquement quand l’adversaire n’avait pas la possibilité de bloquer efficacement. Je vais donc commencer par parler du bloc, car je constate que c’est dans ce domaine que les nouveaux joueurs font le plus d’erreurs. Les créatures sont des ressources importantes et apprendre à bloquer avec prudence leur permettra non seulement de survivre plus longtemps mais aussi de mieux résister et ainsi, de gagner plus souvent. 

Deux définitions rapides avant que nous commencions :

*Échange* - Quand deux créatures s’entre-tuent en combat. Bloquer un 4/2 avec un 2/2 s’appelle un échange. Bloquer un 3/3 avec un 2/2 nous amène à notre définition suivante.

*Le chump block* - Quand une créature en bloque une autre sans espoir d’un échange ou d’une victoire. La seule raison de faire cela est d’éviter d’être touché pendant un tour. Donc, quand une 2/2 s’interpose devant une 3/3 avant de finir au cimetière, c’est un chump block. Si, en revanche, un sort après le combat vient tuer la créature attaquante grâce aux dégâts infligés par la créature sacrifiée, ce n’est plus un chump block puisque l’objectif du bloc était d’affaiblir la créature plus puissante afin de l’achever avec un autre effet. Donc, quand nous parlons de chump block, cela désigne strictement le fait qu’une créature en bloque une plus puissante sans autre raison que de vous faire gagner un peu de temps.

### Les secrets du métier

Pour commencer, je me sens dans l’obligation de vous confier un petit secret mais uniquement si vous me promettez de le partager avec tous les nouveaux joueurs que vous rencontrerez. La manière dont fonctionnent les combats dans **Magic** donne un certain avantage à celui qui bloque. Etrange mais pourtant vrai. Puisque le défenseur choisit quelles créatures vont être bloquées et quelles créatures bloqueront, il bénéficie d’un net avantage sur l’attaquant. 

**Principes de base du bloc**  

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/d2/a8/d2a8edcd37e08f26e9bfe4a0bd0e9dbd1e50e030448b5c595dfde98394339074.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/81/b2/81b25d31d57a840febf1bb928dad7785877d538d27c202b2fb513d5c36250610.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/82/8e/828e1b258c45956b4dfcf7c845615fe5438d3a5abfe41924eac2dd17ac3f17d5.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/4e/02/4e02de799db0661d48c6bebe0236ce19450e235fa0ffd78cdb1020e005094477.jpg"></td>&#10;<td><a><img alt="Giant Spider" src="https://i.ormos.uk/2b/f9/2bf991f4c8a12a370717020aea8672b960e934874843151727a032a436d620ee.jpg"></a></td>&#10;<td><img alt="" src="https://i.ormos.uk/1f/2e/1f2e15ffa4ff562b309115825209450a9a30f64b72b9f0981a43a3dbd04b7cb7.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/33/54/3354a42c7b89603c538b1b981942e781012db4791e3e0f368b48f79a18d13c9e.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/86/12/861268c55a3cfea18fe45f2a7dac904d3c36f5df336597d7ce7ebcceae513637.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/55/d0/55d0c7b06f91c98f072bf91c089463e4a2aace798bb3ac296634446b51616c7e.jpg"></td>&#10;</tr>&#10;</tbody></table>

Si vous vous rappelez notre dernière leçon, il existe quelques règles de base concernant la déclaration des bloqueurs. Premièrement, vous ne pouvez déclarer que des blocs valides. Si votre adversaire vous attaque avec des créatures volantes et que vous n’avez pas de créatures volantes ou de créatures sur lesquelles il est spécifié "peut bloquer comme si c’était une créature volante " (comme Araignée géante), alors vous ne pouvez pas bloquer. C’est la même chose pour des éléments comme la peur ou toute autre sorte d’esquive. De plus, vous devez vous souvenir que chaque créature que vous contrôlez ne peut bloquer qu’un seul attaquant bien que plusieurs créatures puissent bloquer le même attaquant.

**Qu’est-ce qu’un bon bloc ?**  
 Les bons blocs sont ceux qui permettent à vos créatures de survivre tout en détruisant les créatures adverses. Il n’est pas nécessaire que toutes les créatures adverses meurent, uniquement que le combat se termine à votre avantage. 

Un bon bloc peut aussi signifier que seules les créatures importantes adverses soient détruites et que les vôtres survivent. Effectuer des blocs qui vous permettent d’atteindre cet objectif vous donnera un avantage certain au fur et à mesure de la partie. 

Un bon bloc peut également signifier que vous effectuez un échange entre vos créatures peu onéreuses et des créatures adverses plus chères. Le bloc dont j’ai parlé ci-dessus concernait un échange entre une créature 2/2 et une créature 4/2. C’est un bon bloc pour celui qui détient la créature 2/2 car il aura certainement payé beaucoup moins de mana que celui qui détient la créature 4/2. 

<table><tbody><tr><td>&#10;<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/d2/a8/d2a8edcd37e08f26e9bfe4a0bd0e9dbd1e50e030448b5c595dfde98394339074.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/81/b2/81b25d31d57a840febf1bb928dad7785877d538d27c202b2fb513d5c36250610.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/82/8e/828e1b258c45956b4dfcf7c845615fe5438d3a5abfe41924eac2dd17ac3f17d5.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/4e/02/4e02de799db0661d48c6bebe0236ce19450e235fa0ffd78cdb1020e005094477.jpg"></td>&#10;<td><a><img alt="Cafard géant" src="http://www.wizards.com/global/images/magic/general/Cafard_g%C3%A9ant.jpg"></a></td>&#10;<td><img alt="" src="https://i.ormos.uk/1f/2e/1f2e15ffa4ff562b309115825209450a9a30f64b72b9f0981a43a3dbd04b7cb7.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/33/54/3354a42c7b89603c538b1b981942e781012db4791e3e0f368b48f79a18d13c9e.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/86/12/861268c55a3cfea18fe45f2a7dac904d3c36f5df336597d7ce7ebcceae513637.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/55/d0/55d0c7b06f91c98f072bf91c089463e4a2aace798bb3ac296634446b51616c7e.jpg"></td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;<td>&#10;<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/d2/a8/d2a8edcd37e08f26e9bfe4a0bd0e9dbd1e50e030448b5c595dfde98394339074.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/81/b2/81b25d31d57a840febf1bb928dad7785877d538d27c202b2fb513d5c36250610.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/82/8e/828e1b258c45956b4dfcf7c845615fe5438d3a5abfe41924eac2dd17ac3f17d5.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/4e/02/4e02de799db0661d48c6bebe0236ce19450e235fa0ffd78cdb1020e005094477.jpg"></td>&#10;<td><a><img alt="Grizzlis" src="http://www.wizards.com/global/images/magic/general/Grizzlis.jpg"></a></td>&#10;<td><img alt="" src="https://i.ormos.uk/1f/2e/1f2e15ffa4ff562b309115825209450a9a30f64b72b9f0981a43a3dbd04b7cb7.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/33/54/3354a42c7b89603c538b1b981942e781012db4791e3e0f368b48f79a18d13c9e.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/86/12/861268c55a3cfea18fe45f2a7dac904d3c36f5df336597d7ce7ebcceae513637.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/55/d0/55d0c7b06f91c98f072bf91c089463e4a2aace798bb3ac296634446b51616c7e.jpg"></td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

Enfin, un bon bloc peut être celui qui vous évite de subir des dégâts sans que votre créature meure. Bien évidemment, il est préférable de détruire les troupes adverses si vous en avez l’occasion mais, si vous survivez à un combat avec tous vos points de vie et toutes vos créatures, vous vous êtes bien débrouillé.

En vérité, vous ne pouvez pas toujours trouver de bons blocs pendant le combat alors si cela vous arrive, ne désespérez pas. Ce qui suit, ce sont des idées et des règles que j’ai apprises au cours des années en assistant aux grands prix et tournois de **Magic**. **Magic** est souvent une affaire de petits détails mais si on n’oublie pas les règles de base, on peut plus facilement savoir comment bien jouer.

### Règles du bloc

**Règle #0 – Votre total de points de vie est une ressource.**  
 Pour de nombreux nouveaux joueurs, comprendre ce simple concept peut radicalement changer leur manière de jouer et d’aborder le jeu. Assimiler ce concept et comprendre ce que cela implique modifiera certainement votre manière de jouer à **Magic** et améliorera votre style de jeu. 

![](https://i.ormos.uk/60/e6/60e636615c85e1b5caeaeaeba1fc6d626aa3f3009c17f5ee02135295691494e5.jpg)

Voilà en gros le principe de base. Dans **Magic**, plus vous avez de points de vie, plus vous avez de possibilités. Avec 20 points de vie, vous pouvez encaisser pas mal de points de dégâts, vous pouvez donc choisir de ne pas bloquer une créature, de ne pas contrer un sort ou de vous opposer à toute autre action sans pour cela subir de graves conséquences. Cependant, s’il ne vous reste qu’un seul point de vie, cela signifie que le moindre point de dégâts vous tuera et vous fera perdre la partie. Avec ceci à l’esprit, il devient plus facile de comprendre que ne pas bloquer est une option viable dans de nombreuses situations de combat. En sacrifiant volontairement quelques-uns de vos points de vie pour vous permettre de développer vos créatures ou vos terrains en jeu, vous en tirerez bénéfice à long terme. Quand vous disposez de votre maximum de points de vie, il vaut souvent mieux éviter le bloc et subir les points de dégâts. 

Si vous devez vous souvenir d’une seule chose, rappelez-vous de ceci : il est inutile de protéger le moindre de vos points de vie ; seul le dernier*est* important.

**Règle #1 – Si le fait de ne pas bloquer implique que vous allez mourir, alors vous devez bloquer.**  
 Cette règle semble assez évidente mais c’est la première à respecter. A chaque phase de combat défensif, vous devez vous poser la question, “Si je ne bloque pas, est-ce que je vais en mourir ?” Si la réponse est oui, alors vous *devez* bloquer. *La manière* dont vous allez bloquer reste importante et je vous donnerai quelques conseils à ce sujet un peu plus tard. Mais la première chose à faire est de savoir si vous *devez* bloquer ou non.

**Règle #2 – Ne chump blocker que si cela est nécessaire.**  
 L’une des plus grosses erreurs que commettent les nouveaux joueurs en combat, c’est qu’ils bloquent un peu à tort et à travers et sacrifient leurs créatures inutilement, surtout en tout début de partie. 

Il faut songer à une chose fondamentale – les créatures ont un coût en mana. Vous avez payé pour elles et elles sont des ressources de valeur. On ne doit pas les envoyer au cimetière sans raison valable. Il est de votre intérêt de veiller sur elles et de vous assurer que leur sacrifice n’est pas vain. Une carte, Grizzlis n’est certes pas très impressionnante en fin de partie, quand le jeu grouille de Vampires, d’Anges et de Dragons mais elle n’est pas pour autant sans valeur. 

![](https://i.ormos.uk/15/90/15902e8e3e07ff843faf378faeb28bc6efe23b1ce73a7132453f7412d78a721c.jpg)

Dans l’exemple de bloc ci-dessus, vous avez sacrifié Grizzlis pour sauvegarder 4 points de vie mais maintenant la carte Grizzlis est au cimetière et il va être beaucoup plus difficile de tuer le Gargantua Phyrexian . Alors que si vous aviez encaissé les 4 points de dégâts en sauvant ainsi votre ours, vous vous seriez donné une chance supplémentaire de répondre à cette menace, même avec quelque chose d’aussi simple qu’une autre carte Grizzlis !

![](https://i.ormos.uk/a3/e3/a3e3292a39047479f1084a7b45720b6ec5f55ee3af7464d5d9d6d3474563e6c4.jpg)

Vous comprenez ? En attendant un tour, vous avez désormais l’occasion de tirer le profit maximum de cet ours, en le combinant avec une autre carte pour éliminer une créature plus puissante dont vous ne pouviez pas vous débarrasser autrement. En agissant ainsi, vous avez stabilisé la situation. A l’inverse, de nombreux débutants auraient tout simplement sacrifié le premier ours et auraient fait exactement la même chose avec le second. Ils se seraient donc retrouvés sans créature pour arrêter le Gargantua. 

En retardant les sacrifices jusqu’à ce que cela soit absolument nécessaire pour survivre ou pour infliger un maximum de dégâts, vous pouvez optimiser les créatures dans lesquelles vous avez déjà investi et utiliser vos points de vie à bon escient. 

**Règle #3 – Bloquez toujours pour maximiser les pertes adverses tout en minimisant les vôtres.**  
 Voici une autre règle qui devient rapidement une seconde nature après avoir joué quelque temps mais qui n’est pas très évidente au début. Quand votre adversaire vous attaque, il faut qu’il le paie chèrement en perdant le plus de créatures possible.

Pour présenter ça d’une autre manière, quand votre adversaire vous attaque, vous devrez faire en sorte qu’il ne lui reste plus que des cartes faibles en ayant tué les créatures les plus puissantes. Si l’armée adverse n’est plus constituée que de troupes faiblardes, cela vous simplifiera la vie quand vous devrez faire votre choix pour les attaques et les bloquages. A l’inverse, vous risquez de vous faire des cheveux blancs si vous ne tuez que les troupes faibles et que vous laissez en jeu les plus puissantes. De plus, si vous privilégiez de bons échanges tout en maintenant en vie le plus grand nombre de vos créatures, vous réduirez considérablement les possibilités de votre adversaire. Attendez-vous à ce que nous passions beaucoup de temps sur ce sujet la semaine prochaine quand nous allons aborder les applications pratiques des principes de bloc. 

<table><tbody><tr><td>&#10;<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/d2/a8/d2a8edcd37e08f26e9bfe4a0bd0e9dbd1e50e030448b5c595dfde98394339074.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/81/b2/81b25d31d57a840febf1bb928dad7785877d538d27c202b2fb513d5c36250610.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/82/8e/828e1b258c45956b4dfcf7c845615fe5438d3a5abfe41924eac2dd17ac3f17d5.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/4e/02/4e02de799db0661d48c6bebe0236ce19450e235fa0ffd78cdb1020e005094477.jpg"></td>&#10;<td><a><img alt="Ange aveuglante" src="http://www.wizards.com/global/images/magic/general/Ange_aveuglante.jpg"></a></td>&#10;<td><img alt="" src="https://i.ormos.uk/1f/2e/1f2e15ffa4ff562b309115825209450a9a30f64b72b9f0981a43a3dbd04b7cb7.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/33/54/3354a42c7b89603c538b1b981942e781012db4791e3e0f368b48f79a18d13c9e.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/86/12/861268c55a3cfea18fe45f2a7dac904d3c36f5df336597d7ce7ebcceae513637.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/55/d0/55d0c7b06f91c98f072bf91c089463e4a2aace798bb3ac296634446b51616c7e.jpg"></td>&#10;</tr>&#10;</tbody></table><br><i>Certaines créatures ont plus de valeur que d’autres.</i></td>&#10;</tr>&#10;</tbody></table>

**Règle #4 – *Règle avancée* - Sachez estimer à sa juste valeur la menace que représente une créature et bloquez en conséquence.**  
 Puisque cette règle nécessite d’estimer le danger que peut représenter une créature, on peut considérer qu’il s’agit d’une règle avancée que vous pouvez ne pas entièrement saisir. Fréquemment, votre adversaire aura quelques créatures que vous devrez impérativement tuer pour remporter la partie. En engageant de telles créatures, un attaquant prend un risque. Quand cela se produit, vous devrez le plus souvent tout faire pour essayer de vous en débarrasser. 

Ce principe vaut aussi pour vos propres créatures. Il y aura des moments où, si vous pouvez résister un seul tour avec une certaine créature en jeu, vous augmenterez nettement vos chances de remporter la partie. Aussi, vous devez vous montrer prudent quand vous risquez ce genre de créatures en combat. Assurez-vous de pouvoir les protéger ou que votre adversaire ne vous prépare pas un sale tour ! Le combat dans **Magic** revient souvent à faire les bons choix dans des situations où risques et gains potentiels sont multiples. Plus vous jouerez, plus vous parviendrez à savoir quels risques sont bons à prendre et quels risques sont inutiles. C’est une règle que vous n’assimilerez que par l’expérience.

Nous reparlerons des astuces de combat la semaine prochaine ainsi que de la manière dont on évalue une menace.

**Règle #5 – *Règle avancée* – Ajustez les choix de bloc en fonction de la situation du jeu, du total des points de vie et de la stratégie de votre deck.**  
 Cette règle comprend deux notions assez pointues : l’analyse de la table et la compréhension de la stratégie d’un deck. Le total des points de vie va définir votre manière de jouer, que ce soit de manière offensive ou défensive. Mais elle va aussi dépendre des cartes que vous avez en main et de celle que peut détenir votre adversaire. En résumé, cette règle représente la quintessence de votre expérience. Il vous faudra toute votre concentration et vous devrez utiliser toutes vos connaissances pour savoir si vous devez bloquer, comment vous devez le faire et quel résultat vous pouvez attendre.

Les détails spécifiques de cette règle sont bien trop complexes pour que nous puissions les aborder de manière adéquate dans cet article. C’est pourquoi, je vais me contenter de vous donner vos devoirs de la journée : Lire l’article de Mike Flores "[Who's the Beatdown?](https://web.archive.org/web/20060812000000/http://www.wizards.com/leaving.asp?url=http://www.starcitygames.com/php/news/article/3692.html&origin=mtgcom_academy_5)" Les cartes utilisées pour cet article sont anciennes mais la logique et les leçons que vous pouvez en tirer sont toujours d’actualité. Elles vous permettront de comprendre ce que peut être la stratégie d’un deck et comment cette stratégie peut évoluer au fur et à mesure que les tours s’enchaînent dans une partie.

### Application pratique

La plupart des exemples pratiques concernant ce sujet vous seront présentés la semaine prochaine. Mais, pour le moment, je vous propose de résoudre cette question. Pour la bonne compréhension de ce problème, nous considérerons *qu’aucun des joueurs n’a de cartes en main* . De plus, puisque les terrains n’ont aucune importance dans ce cas pratique, nous les ignorerons. Vous devez juste vous concentrer sur les créatures en jeu.

C’est au tour d’Opie de jouer. Une fois ses attaques déclarées, le tapis de jeu ressemble à ceci :

**Opie** Engagées et lancées à l’attaque dans la zone rouge : Crocodile Empereur, Chariot gobelin, 2 Grizzlis.  
Non engagées à l’attaque : Elfes de Llanowar  
![](https://i.ormos.uk/ea/bf/eabfacc64728995cf1832adf9fa524ee8084516fe8da867c46ea28ccaccfec96.jpg)  
**Ben** Dégagées : 2 Armodon dressé, 2 Géant des collines 

La question soulevée est assez simple : Vous êtes Ben et il vous reste 10 points de vie. Votre adversaire, Opie, a encore 18 points de vie. Comment bloquez-vous et pourquoi ?

C’est tout pour l’instant. Maintenant que vous avez quelques bases pour vous entraîner, je vous quitte pour vous retrouver la semaine prochaine avec d’autres exemples et la réponse au problème d’aujourd’hui. 

### Lectures additionnelles

Comme je l’ai déjà indiqué ci-dessus, il est indispensable de lire l’article de Mike Flores "[Who's the Beatdown?](https://web.archive.org/web/20060812000000/http://www.wizards.com/leaving.asp?url=http://www.starcitygames.com/php/news/article/3692.html&origin=mtgcom_academy_5)" pour vous améliorer à **Magic**. C’est un des articles les plus complets de **Magic** car les leçons qui y sont données sont certainement les leçons de stratégie les plus importantes que vous puissiez apprendre. Cet article est également à la base de nombreuses théories qui se sont succédées au cours des années. Pour plus d’informations sur les stratégie de jeu, jetez un coup d’œil à "[Picking the Right Plan](https://web.archive.org/web/20060812000000/http://www.wizards.com/leaving.asp?url=http://www.starcitygames.com/php/news/article/6705.html&origin=mtgcom_academy_5)," un autre article à l’actif de Flores.

De plus, en début d’année, j’ai entamé sur StarCityGames.com une série d’articles appelés Thinking It Through. Cette série a pour but de présenter des situations de jeu assez courantes et de demander l’avis des professionnels sur les décisions qu’ils prendraient s’ils se retrouvaient dans ces situations. L’idée sous-jacente est de comprendre comment les joueurs professionnels abordent ces problèmes pour que vous puissiez établir votre propre guide stratégique et tirer parti de leur expérience. Dans un certain sens, c’est ce que propose la Magic Academy mais à un niveau beaucoup plus basique. Bien que je n’ai pas eu le temps récemment de compléter ces articles (je vais m’y replonger à la sortie de *Spirale temporelle*), je vous recommande vivement de lire le [Volume 2](https://web.archive.org/web/20060812000000/http://www.wizards.com/leaving.asp?url=http://www.starcitygames.com/php/news/article/11678.html&origin=mtgcom_academy_5), puisqu’il présente deux scénarios distincts qui concernent la phase de combat et comment savoir s’il est bon de bloquer ou non.
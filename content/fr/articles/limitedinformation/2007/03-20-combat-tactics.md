---
id: bgb2k0yq
kind: article
lang: fr
path: /fr/articles/limitedinformation/2007/03-20-combat-tactics
title: Tactiques de combat
published: '2007-03-20'
column_slug: limitedinformation
column: Limited Information
authors:
- slug: quentinmartin
  name: Quentin Martin
translation_of: 0bwfawb1
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/qm2
    lang_detected: fr
    capture_id: 1985938
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/qm2,,fr
    captured_at: '2008-02-12 06:06:36+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/qm2
    lang_detected: fr
    capture_id: 1985938
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/qm2,,fr
    captured_at: '2008-02-12 06:06:36+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/qm2
    lang_detected: fr
    capture_id: 1985938
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/qm2,,fr
    captured_at: '2008-02-12 06:06:36+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/qm2
    lang_detected: fr
    capture_id: 1985938
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/qm2,,fr
    captured_at: '2008-02-12 06:06:36+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: bgb2k0yq
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/qm2,,fr
  page_key: wizards.com/default.asp?x=mtgcom/daily/qm2
  lang: fr
  template: classic_asp
  captured_at: '2008-02-12 06:06:36+00'
  capture_id: 1985938
  wayback_url: https://web.archive.org/web/20080212060636id_/http://www.wizards.com/default.asp?x=mtgcom/daily/qm2,,fr
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: bgb2k0yq
  capture_id: 1985938
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/qm2,,fr
  wayback_url: https://web.archive.org/web/20080212060636id_/http://www.wizards.com/default.asp?x=mtgcom/daily/qm2,,fr
  captured_at: '2008-02-12 06:06:36+00'
  template: classic_asp
  sha256: bdedd769dd3dd5d924fde8caa2b00cb06f957464c1ecbcb62693bd50c6968172
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Slipstream_Serpent')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Draining_Whelk')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Crookclaw_Transmuter')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Thrill_of_the_Hunt')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
* * *

![dawn_charm](https://i.ormos.uk/d3/ec/d3ec9d559f77b14dfa60312227bf740d6b7ef42de68a0ae338ee324ba15e50bd.jpg)En dehors de déterminer comment jouer votre main de départ et de choisir quoi jouer à chaque tour, l'aspect le plus complexe du format Limité, à l'inverse du format Construit, c'est la phase de combat. En Construit, vous avez presque tous les renseignements nécessaires pour deviner ce que votre adversaire vous réserve ; vous savez toujours quelles cartes seront jouées dans chaque archétype. Dans le format Limité en cours, rien qu’en blanc/vert, il existe 27 cartes qui affectent le combat. Mais autant vous rassurer tout de suite ; en fait, deviner quelles menaces vous guettent est bien plus simple que vous ne le pensez.

Souvent, quand j'observe des novices jouer en format Limité, je vois une table submergée de créatures, parce qu'ils pensent que la victoire s’obtient à grands coups de boutoirs. En fait, c’est très rarement le cas, au point que je n’ai jamais connu ça dans mes parties. Alors pourquoi cette erreur ? Les nouveaux joueurs ne comprennent pas la phase de combat. Ils ont peur de ce que l'adversaire leur réserve, ils ne savent pas déterminer le contenu de sa main à partir de ce qu’il joue ou quelles créatures ils doivent utiliser pour attaquer, et encore moins quelle sélection de bloqueurs l’adversaire va leur opposant, sans même tenir compte d'éventuelles ruses de combat.

Je ne vais pas vous mentir, il est très difficile de deviner quelle est votre meilleure action possible à chaque tour. Pour ce faire, vous devez répondre à un certain nombre de questions à chaque tour, ce qui vous aidera heureusement à prédire l’avenir immédiat de la partie après un peu d’apprentissage. Si le jeu vous semble équilibré, que personne n'a attaqué et que votre adversaire pioche une carte et attaque soudainement, il est évident que la situation vient de changer : il a pioché une ruse de combat ou une créature assez puissante pour assurer sa défense. Votre jeu doit dorénavant tenir compte de toutes les probabilités. 

### Quelle est la situation actuelle ?

Cette première question en déclenche toute une série : Quelle est la température de la table ? Combien de points de vie vous et votre adversaire avez respectivement ? Combien de cartes avez-vous chacun ? Quelles cartes avez-vous en main et comment vont-elles affecter vos décisions ? Qui est en train de gagner ? 

<table><tbody><tr><td>&#10;<h3><i>Quiconque inflige le taux de blessures le plus important en attaquant est le joueur gagnant à ce moment précis de la partie.</i></h3>&#10;</td></tr>&#10;</tbody></table>

Si vous infligez plus de blessures à votre adversaire à chaque tour que vous n'en subissez, comparé à vos points de vie respectifs, vous êtes probablement en train de gagner. Par exemple, si vous lui infligez 3 blessures par tour, que vous en subissez 1 et que vous avez tous les deux 20 points de vie, vous êtes en train de gagner. Cependant, avec les mêmes blessures, si vous aviez 4 points de vie et qu'il en avait 20, il serait proche de la victoire parce votre mort aurait lieu dans 4 tours et la sienne, dans 7 seulement. Quiconque inflige le taux de blessures le plus important en attaquant est le joueur gagnant à ce moment précis de la partie. Excepté dans certains cas extrêmes, c'est un excellent moyen de jauger la situation.

### Une fois la situation actuelle estimée, la question suivante est : comment allez-vous continuer de gagner ?

Que devez-vous jouer pour maintenir votre progression dans la partie ? Est-elle stable ou dépend-elle de l’apport de nouvelles cartes pour l'améliorer? Si vous êtes en train de gagner, quelles sont les cartes que votre adversaire pourrait jouer pour vous mettre des bâtons dans les roues ? Et quelles sont les cartes dont il aura besoin pour retourner la situation à son avantage ? Ce sont les questions qui composent l'étape suivante. Maintenant que vous avez une idée précise de la situation, vous vous assurer que la partie continue en votre faveur, ou dans le cas contraire, de jouer pour améliorer votre situation.

### Quelles sont les informations que votre adversaire vous fournit ?

Quels sorts peut-il lancer ? Quelle créature va-t-il sauver/perdre/tuer ? Que pouvez-vous déduire de son attaque ? Et de ses attaques et blocages précédents ? Quelles conclusions pouvez-vous tirer de toutes ses actions depuis le début de la partie ? 

Une fois de plus, je sais que cela peut paraître énorme à assimiler d'un seul coup. Cependant, il suffit d’examiner sa main et d’avoir une connaissance suffisante du format pour déterminer quelles cartes intéressantes pour lui il pourrait jouer avec son mana disponible. (Note : Pour réussir en Limité, il est important de connaître le texte de règle exact de chaque carte du format.) Je vois tout de suite vos yeux s’écarquiller d’horreur, mais rassurez-vous ; souvent, nous parlons seulement de quatre ou cinq cartes, bon nombre d’entre elles agissant de manière similaire. 

Vous pensez certainement que la déduction est un art difficile dans ce cas, mais en fait, c'est assez simple. Chaque fois que vous jouez quelque chose, vous avez une bonne raison de le faire, et c'est le cas aussi pour votre adversaire. Observez la situation et regardez ce qu'il joue avec un œil différent en vous demandant pourquoi il agit de la sorte. Sous cet angle, une grande partie de sa stratégie se révèle peu à peu : ce qu'il utilise et/ou qu'il n'utilise pas pour attaquer, ce qu'il fait avant le combat, ce qu'il n'a pas fait au tour précédent mais qu'il fait maintenant qu'il a plus de mana ou du mana de couleur différente... tous ces éléments vous parlent. Il suffit simplement de les analyser.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Slipstream Serpent" src="https://i.ormos.uk/7f/b6/7fb6e9d017b0ffd884797c21f97c7dced45ff74d021b33496e371d28eb21a915.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Chaque carte qu'il joue et chacune de ses actions vous fournissent des tonnes de renseignements. Si votre adversaire passe son deuxième tour, et la fin de votre deuxième tour alors qu’il a encore ![White Mana](https://i.ormos.uk/55/78/55785924f8cda9ab2a85364f807ba172c7530e43d94b14aad222ec4bbf2589ca.gif)![Green Mana](https://i.ormos.uk/d9/d5/d9d556256faf839099c06019302393fab57e6e9a77769d6f6813a7c961c4cb59.gif) dans sa réserve, cela vous indique qu'il n'a pas de Ranger de la Scrutaie ou une des deux autres créatures à deux manas de ces deux couleurs. S'il joue les Conte-destins errants, cela signifie qu'il n'a pas de Cavalerie bénaliane, d'Éclaireuse amroue, de Slivoïde à filière, d'Ours à fourrure cendrée ou de Prédateur kavru, parmi tant d'autres. Une créature avec la mue est l'exemple le plus évident. Elle craint d'entrer au combat contre un Slivoïde fondamental depuis qu'elle a été jouée, mais quand le terrain numéro six arrive en jeu, elle s'avance seule dans la zone de combat. Il ne faut pas être sorcier pour deviner qu'il s'agit d'un Serpent des sillages.

On me demande souvent si telle action d’un joueur dans un cas spécifique est bonne ou mauvaise. Mais la plupart du temps, on ne me donne pas tous les renseignements de contexte qui sont primordiaux pour répondre à la question. Savoir ce qui s'est passé dans les tours précédents et visualiser les cartes qu'il pourrait avoir est toujours important. Vous devez être en mesure de déterminer le contenu des decks respectifs des deux joueurs. Ce que j’essaie de vous expliquer, c’est que chaque partie est différente ; elle dépend des nuances de vos actions stratégiques et du contenu de vos decks. La quantité d'information disponible est incroyable ; il suffit de savoir où et comment la trouver.

**Êtes-vous suffisamment satisfait de l’évolution probable de la partie dans les prochains tours ?** 

![](https://i.ormos.uk/91/32/913281b36b728a23739a14a5b050ffc2c095ecb4012a1fed762018dbfa11799a.jpg)C'est souvent le moyen le plus simple de déterminer si vous prenez la bonne décision ou non. Imaginez comment la partie va évoluer après votre action, et si vous êtes satisfait, c'est que votre décision est la bonne. Répétez le processus pour chaque option à votre disposition, et la meilleure sera toujours celle qui est le moins risqué. Attention, cependant, certaines décisions peuvent vous paraître être les meilleures de prime abord, mais en y réfléchissant, souvent, vous vous rendrez compte qu’il y a mieux à faire : vous devez toujours jouer ce qui augmente le plus vos chances de gagner la partie. Par exemple, si vous hésitez entre jouer une Toile d'Æther ou une Suie étrangleuse pour profiter le mieux du combat, réfléchissez un instant. Les deux cartes ont le même effet. Si vous jouez la Suie, la Toile reste dans votre main. En revanche, si vous jouez la Toile, vous avez toujours la Suie et votre créature sera un peu plus pêchue. La plupart du temps, il sera plus avantageux pour vous de booster votre créature et de garder la Suie, votre meilleure carte, dans votre main. Mais en plus, dans ce cas spécifique, il est évident que votre adversaire a un sort de retrait en main et que votre Toile pourra s’en débarrasser plus tard. Avouez que c’est quand même mieux d’esquiver du même coup la prochaine ruse de votre adversaire avant même qu’il la joue.

### Quelle est votre marge d’action ?

Il faut bien l’admettre, parfois, vous serez sous pression et vous n’aurez plus le luxe d'éviter certaines cartes comme Fouler les domaines, l'Invocation de pierrebois, L'union fait la force, Fortifier ou le Front de bourrasque. Si c’est le cas, jouez comme si ces cartes n'existez pas. Inutile de faire monter votre pression artérielle pour rien. Mais la plupart du temps, vous aurez le choix et ce sera à vous de décider si vous voulez jouer la prudence ou non. Disons que vous avez 20 points de vie, une position dominante et que votre adversaire blanc/rouge joue une Désintégration pour tuer votre Sphinx de Serra, votre menace la plus grosse. Vous avez un Bulot puiseur dans votre main, que faites-vous ?

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Draining Whelk" src="https://i.ormos.uk/47/e0/47e0a76857a3588590bfc438c2d963e555296c679172095e3d739a5dbf71377f.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

J'ai évité délibérément de vous donner toutes les informations de jeu. La plupart des joueurs balanceraient leur Bulot sur la table en un rien de temps, un large sourire aux lèvres... Et ils perdraient. Supposons que votre position sur la table post-Désintégration soit suffisamment dominante pour que vous ayez encore de fortes chances d'être le vainqueur, et que l’attaque du Bulot ne sera pas mortelle. Si vous le jouez pour infliger à votre adversaire 7 blessures et qu'il bloque avec tous ses moutons, vous aurez l'air un peu bête quand son Géant de la désolation et son Akroma, ange de la Colère tous frais gagneront la partie ! Dans ce cas précis, la Désintégration ne vaut pas la peine de jouer le Bulot ; vous avez suffisamment de marge pour le garder au chaud jusqu'à ce que votre adversaire joue une carte que vous serez *obligé* de contrecarrer. Si vous pouvez éviter des manœuvres de ce genre pour gagner, de vous en privez pas. Cependant, n’oubliez pas que ce type de stratégie est très avancé et très difficile à appliquer. Faites très attention.

### Avez-vous des ressources limitées pour vous débarrasser de certaines cartes que votre adversaire a ou pourrait avoir ?

Vous pourriez n'avoir qu'une carte dans votre deck qui vous permette de vous débarrasser de ses deux bombes. Il n'en a pioché aucune pour l'instant, mais vous avez en main l'unique sort de retrait qui pourra les faire disparaître. Avez-vous dans ce cas le luxe d'attendre et de voir comment la situation va se développer ? Devez-vous brûler tout de suite et espérer que les deux bombes ne sortiront pas du deck ? Si vous l'utilisez tout de suite, cela limitera-t-il la force de ses bombes s'il les pioche, ou mieux encore, est-ce que cela l'empêchera d'avoir le temps de les piocher ? 

Ce sont les dernières questions qui devraient vous venir à l'esprit dans ce cas spécifique. Pour voir si ce cours de stratégie vous a été utile, voyons comment vous allez réussir dans une série d'exemples pratiques.

**Exercice 1**

C'est le tour de votre adversaire. Il a dégagé et pioché, et il attaque avec des deux Ours à fourrure cendrée. Il n'utilise pas d'accent de couleur. Qu'allez-vous jouer ?

![](https://i.ormos.uk/42/6d/426d0067069443357b51791dc094429d872c83ae5eca8160bb8d57b64a3ea9a9.jpg)

Adversaire :  
 4 points de vie  
 deux cartes en main  
En jeu : 5 plaines dégagées, 5 forêts dégagées, 2 Ours à fourrure cendrée engagés et attaquants

Vous :  
 13 points de vie  
 Pas de carte en main  
 En jeu : 3 îles engagées, 3 montagnes engagées, 1 Jaya Ballard, mage de force et un Parasite forgeur face cachée dégagés, 1 Dragon pardique, 1 Kraken des abîmes, 1 Téfeiri, mage de Zhalfir et un Grand gargadon dégagés.

Réponse :

La première chose à faire, c'est de déterminer comment vous pourriez perdre votre position dominante. Vous n'avez qu'une action correcte possible : vous bloquez les deux Ours en échangeant vos créatures supérieures contre eux. Sa main ne peut contenir que deux combinaisons possibles qui pourraient vous inquiéter. La première est la seule à être vraiment réaliste dans ce cas de figure : un terrain et un Front de bourrasque pioché. L'autre combo possible serait une Salve de sel pour se débarrasser de Téfeiri, mage de Zhalfir et un Charme de l'aube/Flou du caméléon/Grâce de l'ange pour rester en vie et récupérer le Front de bourrasque. Dans cette exemple, vous avez la possibilité d'esquiver toutes les cartes du format, alors faites-le. Cela peut paraître horrible de gâcher des créatures comme ça, mais c'est la solution 100% correcte dans ce cas.

**Exercice 2**

Cet exemple vient d'une partie amicale m'opposant à Dolf Hendrikx, une des stars grimpantes des Pays-Bas. C'est son quatrième tour de la partie. Il a commencé et pour l'instant, sa courbe de mana a été splendide, avec une Cavalerie bénaliane d'ouverture, suivie par un Reclus des Plaines salines. Il a sorti sa quatrième plaine avant le combat et il vous attaque avec tout ce qu'il a. Que faire ?

![](https://i.ormos.uk/ae/35/ae35ac01a5b8ce76562823f4087ccf20aaefdbf52f3567234897baeddcbff76e.jpg)

Adversaire :  
 20 points de vie  
 Quatre cartes en main  
 En jeu : 4 plaines dégagées, une Cavalerie bénaliane et un Reclus des Plaines salines engagés et attaquants

Vous :  
 18 points de vie  
 Six cartes en main  
 En jeu : 3 îles engagées, un Serpent des sillage face cachée dégagé

Réponse :

Une fois de plus, la solution au dilemme est en fait très simple. Il faudrait être fou pour attaquer avec le Reclus sans avoir un atout dans sa manche. Il n'y a vraiment que quatre possibilités sensées : Fortifier, Lion à crinière blanche, Enveloppeur de pierre et Croisé céleste. À moins que ce soit votre deuxième partie et que votre adversaire ait vu tout votre deck dans le duel précédent et qu’il pense que le Changeforme vésuvéen votre seule créature avec la mue (et ce n'est pas le cas), vous pouvez tout de suite oublier Fortifier, parce que perdre le Reclus et Fortifier pour une mue n'en vaut pas la peine à ce moment de la partie. Le Lion est assez improbable parce que votre adversaire n’en tirerait pas grand avantage. L'Enveloppeur de pierre pourrait arriver en jeu et commencer frapper, mais ce serait une manœuvre étrange parce que le Reclus a une présence plus dominante qu'un volant. Il ne reste qu'une solution évidente : le Croisé céleste. Et c’est une mise en jeu agressive, qui indique que l’adversaire ne va pas s'en arrêter là. Attendre votre étape de fin de tour pour le lancer ne lui donnera aucun avantage et à ce point du jeu, il préférera vous infliger 2 blessures supplémentaires avec le Reclus plutôt qu'en prévenir 2.

Il faut remarquer que s'il était sûr que la créature avec la mue était un Changeforme vésuvéen, il serait possible qu’il joue une Faveur de Serra ou des Flèches barbelées, mais dans notre situation, c’est vraiment improbable. C’était le dernier exemple facile de la série.

**Exercise 3**

Ce nouveau cas de figure est issu d'un match opposant la super star (et mon coloc) Ruud Warmenhoven et le champion du monde, Kenji Tsumura. Tard dans une première partie épique, Ruud lance une Salve de sel sur la Jedit Ojanen d'Efrava toute fraîche de Kenji, mais il n'attaque pas avec son Ours à fourrure cendrée alors que Kenji est totalement engagé. C'est le tour du Japonais ; il pioche une autre île. Que devrait-il faire ?

![](https://i.ormos.uk/d6/70/d6707f72e471e3bd96d72d2dccd714b69b5fb11be31d4500bec731ae8d906a6d.jpg)

Ruud :  
 10 points de vie  
 Une carte en main  
 En jeu : 5 forêts (3 engagées, 2 dégagées), 3 plaines (2 engagées, 1 dégagée), Ours à fourrure cendrée dégagé

Kenji :  
 10 points de vie  
 Une île en main  
 En jeu : 3 forêts dégagées, 3 îles dégagées, 1 Drakon de l'Ouktabi dégagé, 1 Transmutateur crocheserre dégagé

Réponse :

La première question évidente, c'est pourquoi diable l'Ours n'a-t-il pas attaqué ? Si vous ne l’avez pas remarqué, vous craignez sûrement l’arrivée d’un Orage de grêle et vous vous préparez à attaquer avec le Drakon de l'Ouktabi. Mais c’est une mauvaise idée. L'Ours n'a pas attaqué pour une bonne raison. Il n'y a que deux choses que Ruud peut jouer si l'Ours n’attaque pas : la Toile d'Æther et la troisième capacité du Charme d'évolution. 

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Crookclaw Transmuter" src="https://i.ormos.uk/98/97/989758501ef3159127d894025b5641aa6023cb48d82536c7650f0cff62e72407.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Le meilleur moyen de déterminer comment attaquer est de songer à ce qui arriverait si toutes vos créatures étaient engagées. Si c'était le cas, et que Ruud avait la Toile, il bloquerait le Drakôn gratuitement, subirait les 7 blessures, et il aurait un bloqueur à échanger contre le Transmutateur crocheserre... Pas un bon plan. Si Ruud avait le the Charme, l'Ours se bagarrerait contre le Transmutateur. Le résultat n'est pas si mauvais que ça. Mais il y a deux options d'attaque supplémentaires à considérer. Le Drakôn peut attaquer seul : un suicide avec une Toile et un bon échange avec un Charme. Si le Transmutateur attaque seul, il est échangé contre l'Ours et l'option de Ruud, quoi qu’il arrive. Maintenant, nous somme sûr que Ruud pourra jouer sa ruse, et que le transmutateur est la seule attaque raisonnable dans ce cas.

Pour finir, dans cette partie, c'est exactement ce que Kanji a fait. Il a attaqué avec son Transmutateur et Ruud a répondu de la façon la plus inattendue : il a encaissé trois blessures. Un des meilleurs plans que j'ai vu ces dernières années : le double bluff. Il m'a expliqué plus tard qu'il avait trois Araignées de la pénombre qu'il espérait récupérer et qu'en n'attaquant pas avec l’Ours, il avait évité 2 blessures supplémentaires. C'était pour lui une course aux blessures impossible à gagner, alors il avait préféré gagner du temps en s'accordant un tour supplémentaire pour trouver une Araignée. Cette manœuvre ne fonctionnerait que contre un adversaire de haut niveau qui n’a plus besoin de suivre consciemment toutes les étapes de raisonnement. Une fois de plus, la règle 'on ne bluffe pas un idiot' se vérifie.

**Exercice 4**

Cet exemple est difficile, mais c’est une situation dans laquelle vous vous retrouverez tout le temps : l'information n'est pas aussi claire que dans les exemples précédents et vous devez tenter de déterminer quelle est l'action correcte face à une multitude de ruses potentielles. Jusqu'à présent, la partie n'a pas connu beaucoup d'interaction car aucun des joueurs n'a eu l'occasion d'effectuer une bonne attaque. Pendant votre tour, vous avez fait monter la pression en engageant des terrains pour un Mage de l'arène. Avant le combat, votre adversaire lui a balancé une Salve de sel et il est à présent face à ses créatures. Qu'allez-vous jouer ?

![](https://i.ormos.uk/e5/30/e530d1b6d563d39e8040ade7986bb31f656a07f648ba6b121fb4388f4163b635.jpg)

Adversaire :  
 20 points de vie  
 Trois cartes en main  
 En jeu : 3 plaines (deux engagées, une dégagée), 4 forêts (3 engagées, une dégagée), un Thallidé encoquillé dégagé avec cinq marqueurs 'spore' , une Dryade de Boiverreux, un Shamane nantuko et des Déchiffre-bois de Citalune engagés et attaquants

Vous :  
 20 points de vie  
 Prise en retour et Hallebardier kelde en main  
 En jeu : 3 îles engagées, 3 montagnes engagées, Askari de la lame brûlante, Chauffeur de charbon et Parasite forgeur face visible dégagés

Pour vous aider, voici la liste des atouts que l’adversaire pourrait avoir dans sa manche : Toile d'Æther, Puissance de l'ancienne Krosia, L'union fait la force, Isolation temporelle, Frisson de la chasse et Lion à crinière blanche (d'autres cartes comme le Scintillement momentané et le Charme de l'aube sont aussi possibles, mais seraient pires).

Réponse :

Examinons toutes les options que nous avons à notre disposition. Comme ce bon vieux Sam Gomersall le dit toujours, le mieux, c'est de bloquer pour voir ce que l’adversaire vous réserve, tant que le blocage ne vous coûte pas trop. C'est une technique qui est souvent applicable en début de partie, quand une ruse fait perdre beaucoup de tempo au lanceur, mais elle peut s’appliquer dans ce cas. 

Le plus évident, ce serait de d'échanger le Parasite forgeur contre le Shamane nantuko et l'Askari de la lame brûlante contre la Dryade de Boiverreux, et de faire rebondir le Chauffeur de charbon avec les Déchiffre-bois de Citalune. Il devrait rapidement vous apparaître que bloquer ainsi ne vous sert pas à grand-chose. Si l’adversaire a un Frisson de la chasse, vous mettrez deux de vos créatures à la poubelle. La Toile d'Æther le laissera avec un très gros Shamane (mais vous avez une Prise en retour en main). Le Lion à crinière blanche récupère le Shamane pour obtenir plus d'avantage des cartes, et le Chauffeur de charbon que vous avez gardé ne peut toujours pas attaquer à cause du Thallidé encoquillé. 

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Thrill of the Hunt" src="https://i.ormos.uk/04/7a/047a458bf67ddc0e12903fc43b472c89eea2e5dc445253b7d4941dbf07df8bf2.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Il y a d’autres combinaisons de blocage, mais elles ne sont pas aussi bonnes. La deuxième possibilité applique la règle de Sam. Jetez l'Askari en pâture à la Dryade et vos deux autres créatures sur les Déchiffre-bois. Cela vous permettra de contourner la plupart des ruses que l’adversaire pourrait vous réserver, et subir 3 blessures à ce moment de la partie n'a aucune importance, donc cela n’a rien d’inquiétant. Le Frisson de la chasse passe toujours, mais ce n’est pas une si mauvaise idée de jouer l'Askari dans ce cas de figure. L'Isolation temporelle, la Puissance de l'ancienne Krosia et L'union fait la force sauvent les Déchiffre-bois et s’échangent contre le Chauffeur de charbon. Le Lion à crinière blanche est excellent pour l’adversaire dans ce cas précis, parce qu’il voudra récupérer les Déchiffre-bois dans sa main si possible.

Ce blocage me paraît excellent, même si le Frisson ou le Lion restent des menaces possibles, et votre utilisation de la Puissance de l'ancienne Krosia est meilleures que dans d'autres cas. Mais il y a mieux que ça. 

Avant d’y songer un peu plus, n'oubliez pas que vous avez une Prise en retour et un Hallebardier kelde. Si vous pouvez bloquer pour priver votre adversaire d'une occasion d'utiliser une ruse (en l’obligeant à gâcher son mana pour le tour ou, dans le cas du Lion, à devoir attendre encore un tour pour ajouter une créature), alors vous gardez le mana de la Prise en retour pour le prochain tour et empêchez-le de remettre ça. Le Hallebardier pourra probablement se débrouiller seul au prochain tour, et si votre adversaire a encore suffisamment confiance en ses forces pour lui foncer dedans, cela limite vraiment l’identité de son atout à une carte. Si vous piochez un terrain, vous pourrez jouer la Prise et le Hallebardier. Alors, l’important, c’est de nuire à sa stratégie pour le moment et de trouver la façon idéale de le bloquer.

Il n'y en a qu'une à notre disposition qui nous assure d’y arriver. C'est le seul blocage qui protège contre le Frisson de la chasse (la ruse la plus puissante dans ce scénario) et qui empêche aussi votre adversaire de jouer un Lion à crinière blanche particulièrement avantageux pour lui ce tour-ci. Le Parasite bloque les Déchiffre-bois et les deux autres créatures bloquent la Dryade. 

Comme dans la situation précédente, nous subissons trois blessures, et ce n'est pas un problème. En surface, cela paraît moins avantageux parce que nous échangeons le Chauffeur de charbon contre la Dryade au lieu de l'Askari, mais aucune des créatures n'a vraiment d'importance sur la table vu qu'elles ne peuvent pas traverser le mur de défense de l'adversaire. Ce blocage est en fait le meilleur parce qu'il prend en compte toutes les cartes qu'il pourrait jouer. Il ne lui laisse aucune occasion intéressante et le force à garder son mana pour une prochaine fois. Ce qui veut dire aussi que vous aurez des cartes en main lors de votre dégagement.

**Exercice 5**

Je vais vous laisser avec un mystère à résoudre, un souvenir d'une de mes parties du Pro Tour – Genève. C'est une situation qui intrigue encore les pros. Aucun d'eux n'arrive à être unanime sur ce qu'il faut jouer dans ce cas. Vous avez trois cartes de valeur moyenne : une ruse sympa, une créature solide et une autre simplement bonne. Votre adversaire et vous êtes tous les deux à 16 points de vie et vous êtes attaqué. Qu'allez-vous jouer ?

![](https://i.ormos.uk/32/5b/325bcfa655156b0e49e52872c33a63e8b508d6c6d619fa263db01f501f65cd7c.jpg)

Adversaire :  
 16 points de vie  
 Trois cartes en main  
 En jeu : 3 îles dégagées, 3 montagnes dégagées, un jeton 1/1 Gobelin dégagé et un Voyant des fonds marins face visible engagé et attaquant

Vous :  
 16 points de vie  
 Trois cartes en main  
 En jeu : 3 forêts engagées, 2 montagnes engagées, Shamane nantuko et Ours à fourrure cendrée dégagés

Amusez-vous bien dans les forums...

Q
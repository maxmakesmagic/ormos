---
id: 82gnzb5s
kind: article
lang: fr
path: /fr/articles/makingmagic/2008/01-21-the-amazing-race-class
title: L’épique mise en place de l’efficace système race/classe
published: '2008-01-21'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
translation_of: f7jhqcv2
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr315
    lang_detected: fr
    capture_id: 1976712
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr315,,fr
    captured_at: '2008-05-07 18:51:17+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr315
    lang_detected: fr
    capture_id: 1976712
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr315,,fr
    captured_at: '2008-05-07 18:51:17+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr315
    lang_detected: fr
    capture_id: 1976712
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr315,,fr
    captured_at: '2008-05-07 18:51:17+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr315
    lang_detected: fr
    capture_id: 1976712
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr315,,fr
    captured_at: '2008-05-07 18:51:17+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: 82gnzb5s
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr315,,fr
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr315
  lang: fr
  template: classic_asp
  captured_at: '2008-05-07 18:51:17+00'
  capture_id: 1976712
  wayback_url: https://web.archive.org/web/20080507185117id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr315,,fr
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: 82gnzb5s
  capture_id: 1976712
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr315,,fr
  wayback_url: https://web.archive.org/web/20080507185117id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr315,,fr
  captured_at: '2008-05-07 18:51:17+00'
  template: classic_asp
  sha256: 3bca43d40ef660b0732bd4444f10fe47d3e0dece5144a87d2b0d177a4448db89
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Artificial_Evolution')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Merfolk_Assassin')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Merfolk Assassin
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Need_for_Speed')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Need for Speed
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Aven_Brigadier')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Sacrifice')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Coat_of_Arms')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Coat of Arms
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Goblin_Assassin')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Goblin Assassin
  occurrences: 2
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Primal_Whisperer')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
* * *

Bonjour tout le monde. J’espère que tous ceux d’entre vous qui sont allés aux Avant-premières se sont bien amusés. Avez-vous joué le Renfort ? Avez-vous aimé ? J’en étais sûr. Quoi qu’il en soit, nous sommes actuellement dans ce que j’appelle la ‘semaine des limbes’. C’est-à-dire la semaine entre les Avant-premières et la sortie de l’extension. La semaine des limbes est toujours une semaine sans thème. Je vais évidemment vous parler de *Lèveciel*, mais je n’ai pas de carte à vous présenter en exclusivité ou de thème à traiter en particulier, ce qui signifie que je suis à la merci de n’importe sujet dont mon subconscient aura envie de vous parler (si cela ne vous effraie pas, c’est que vous n’avez pas encore lu suffisamment de mes articles pour avoir une idée de mon état mental).

Coup de chance, mon subconscient s’est arrêté sur un paragraphe de mon premier article d’avant-première sur *Lèveciel* [Entrez en classe !](/en/articles/makingmagic/2008/01-07-class-is-in-session):

> En fait, notre histoire commence pendant le développement de *Mirrodin*, soit plusieurs années avant que les membres de l’équipe créative de *Lorwyn* ne se rencontrent. Voyez-vous, c’est à cette époque que l’équipe créative parvint à convaincre la R&D qu’il fallait adopter le système de race/classe. Auparavant, les créatures n’avaient qu’un type. Parfois c’était une race, et parfois une classe. Autant dire que c’était un peu le bazar. Le système de race/classe fut créé pour rendre **Magic** plus cohérent avec à peu près tous les autres jeux existants basés sur la fantasy. La seule chose qui me dérangeait (parmi les gars de la R&D, j’étais l’un des plus fervents partisans de l’adoption du modèle race/classe), c’était que nous allions le mettre en place juste après *Carnage* (vous savez bien, le bloc tribal). Mais c’est la vie, les choses n’arrivent pas toujours dans l’ordre où elles auraient dû, et le bloc *Carnage* manqua de peu l’avancée technologique race/classe. Enfin, pensai-je, au moins nous pourrons nous en servir la prochaine fois que nous ferons un bloc tribal.

Dans mon avant-première, j’ai voulu vous expliquer comment nous en sommes arrivés au thème ‘la classe est importante’ de *Lèveciel*. Pour ce faire, j’ai rapidement passé en revue tous les événements qui ont mené à ce résultat, et en cours de route, j’ai écrit ce paragraphe résumant comment le système race/classe est né. En le relisant (pour essayer d’avoir un peu d’inspiration pour l’article d’aujourd’hui), je me suis dit : ‘Mark, tu viens d’exhumer une histoire très intéressante du passé de la R&D.’ Car le système race/classe ne fait pas partie de ces concepts qui apparaissent un beau jour, quand un gars a une idée et que tout le monde s’écrie ‘Génial, on y va !’. Non, il a fallu se battre, et pour des raisons assez peu évidentes. C’est alors que ça m’a frappé. L’histoire de l’origine du système race/classe est cool. Elle est liée à *Lèveciel*. Elle est bourrée de conflits et de complots en coulisses. Et j’étais en plein dedans. Ding ! Ding ! Ding ! On dirait bien que nous tenons un sujet, les amis !

### Camarades de race/classe

![Artificial_Evolution](https://i.ormos.uk/f2/e1/f2e11facb4b03fb99605ed9dab0357a8c7ebe0f3f459b8ef3886060124e4bbbc.jpg)

À la fac, j’avais suivi un cours traitant de l’adaptation des événements de la vie réelle dans un scénario. Comment transformer la réalité en divertissement ? La réponse, c’est que vous devez rester fidèle à l’essence de votre histoire, tout en la considérant d’un point de vue théâtral. L’histoire de l’acceptation de l’idée du système race/classe se déroule sur de longs mois, mais si j’avais à choisir le moment le plus épique du combat, je prendrais cette réunion **Magic** hebdomadaire du mardi après-midi durant laquelle l’équipe créative présenta officiellement l’idée au reste de la R&D de **Magic**, ce que l’équipe créative appelle souvent ‘L’arène’ (c’est-à-dire l’ensemble des designers et des développeurs).

Gardez en mémoire que cette réunion se déroula pendant le développement de *Mirrodin*, autrement dit vers le début de l’année 2003. À l’époque, Randy Buehler était le directeur du développement de **Magic** et c’était à lui que l’équipe créative rendait des comptes. Randy devint peu après le directeur de **Magic**, et environ un an et demi plus tard je fus promu directeur de la conception à mon tour, et ce fut à moi que l’équipe créative dut rendre des comptes (période aujourd’hui révolue, elle rend maintenant des comptes à un homme adorable du nom de Jake Theis). L’équipe créative de l’époque était constituée de Brady Dommermuth, Brandon Bozzi, et Jeremy Cranford (Brady est le seul des trois à faire encore partie de l’équipe créative de **Magic**).

Mis-à-part moi, les designers et les développeurs formaient un groupe presque entièrement différent de celui d’aujourd’hui. Aaron Forsythe s’occupait encore de **magicthgathering.com**. Devin Low devrait attendre six mois avant de faire son entrée. Matt Place et Mike Turian étaient encore des joueurs pro. **Magic** avait perdu la trace d’Erik Lauer, alors occupé à autre chose que jouer à **Magic**. À peu près aucun de ceux qui constituent l’équipe de design et de développement actuelle n’était encore là. Mais Brian Schneider était là. Mike Elliott était là. Tyler Bielman était là. Brian Tinsman était là. (Soit dit en passant, Brian est de retour chez Wizards pour diriger le design de nouveaux projets, et travaille occasionnellement à celui de **Magic**. Il faisait par exemple partie de l’équipe de design de ‘Beignet’.) 

Enfin bref, l’équipe créative était très excitée par la perspective d’adopter un système race/classe. L’Arène, au contraire, n’aimait pas tant que ça cette idée. Ce n’était pas qu’ils soient vraiment contre, mais ils ne voyaient pas trop l’intérêt de ce changement. Et c’était le sujet de la réunion. Randy, en tant que manager de l’équipe créative, voulait respecter les souhaits de son équipe. Mais en tant que directeur du développement, il voulait faire en sorte que les développeurs (et les designers) soient d’accord pour entériner l’idée. Les types de créatures sont le seul élément du jeu qui relève à la fois de l’aspect créatif et de l’aspect mécanique, ce qui en fait quelque chose de très difficile à manipuler, aucune équipe n’ayant de contrôle total dessus. 

Les designers et les développeurs avaient des avis très variés sur la question. Beaucoup n’avaient pas vraiment choisi leur camp, n’ayant pas entendu tous les tenants et aboutissants. Certains étaient plutôt contre, car ils n’aimaient pas l’impact que cela aurait sur le jeu, selon eux. Et enfin, il y avait une personne de l’Arène qui était vraiment pour. En fait, c’était cette personne qui, au départ, avait fait des pieds et des mains pour lancer la machine qui avait conduit à la discussion sur le système race/classe. Cette personne, bien sûr, c’était moi.

### Jouer la carte de la race/classe

Laissez-moi faire un petit retour en arrière. Depuis les premiers temps où j’ai joué à **Magic**, j’ai toujours été un grand amateur des types de créatures. Je fais partie de ces gars qui ont déliré quand Merfolk Assassin (Assassin ondin) fut imprimé dans l’édition *The Dark*, parce que cela me faisait un deuxième ondin pour mon deck Ondin. Quand je suis entré chez Wizards, c’est probablement moi qui ai le plus œuvré pour ajouter ‘NOM DE LA CARTE est considéré comme un \[insérez le type de créature ici\]’ dans les textes de règles. J’étais l’un des plus insistants à proposer d’abandonner cette stupide restriction pour pouvoir tout simplement mettre plusieurs types de créatures sur la ligne de type. J’étais celui qui a le plus insisté pour faire un bloc tribal. Et c’est moi qui, quand j’en ai eu l’opportunité, ai poussé à la roue pour les types de créatures.

Cette opportunité me fut offerte par le bloc *Odyssée*. L’équipe créative d’alors avait récemment quitté Wizards, et Bill Rose s’apprêtait à en recruter une nouvelle. Il m’a donc demandé si je voulais superviser l’univers d’*Odyssée*. Cela signifiait que je serais le responsable, et celui qui aurait le dernier mot sur tous les noms, textes d’ambiance et types de créatures (exception faite de certaines restrictions mécaniques spécifiques, comme le type ‘slivoïde’). La raison pour laquelle Bill me proposa cela, c’est que j’avais toujours été très impliqué dans l’univers : j’avais fait partie de nombreuses équipes de création de noms et de textes d’ambiance, et je m’étais beaucoup investi dans le début de la saga de l’*Aquilon*. L’un de mes objectifs lorsque j’accédai à cette responsabilité fut de chercher des moyens de donner plus d’ampleur à ce que nous faisions. J’expérimentai différents noms de cartes (bon, d’accord, Need for Speed (Besoin de vitesse) n’était peut-être pas génial), différents types de textes d’ambiance (selon nos sondages, ‘Je veux une *grosse* banane’ fut à la fois classé parmi les meilleurs et les pires textes d’ambiance) et, bien sûr, différentes approches de la ligne de type de créature.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Aven Brigadier" src="https://i.ormos.uk/fb/7e/fb7ea8cb80487f18eb2926720a067495b570c0219d24f7fb5b503eef0e245d7a.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Mon plus gros forcing dans ce domaine fut les avemains. Plutôt que de simplement leur donner le type oiseau, je décidai d’essayer de jouer avec leur nature humanoïde en leur donnant à tous le type oiseau et soldat (certains devinrent ensuite des oiseaux et sorciers). De même, j’ai fait de toutes les créatures nantuko des insectes et druides. En fait, j’ai cherché par tous les moyens possibles à mettre des types de créatures multiples sur une même carte, que ce soit zombie et assassin, nain et berserker ou centaure et druide. Lorsque *Carnage* arriva, je n’étais plus responsable des types de créatures, mais j’étais tout de même très impliqué dans le design et je fis en sorte que les types de créatures multiples deviennent intéressants d’un point de vue mécanique, et je gardai donc un œil sur le sujet.

Tout ça pour vous dire que je faisais déjà en douce ce que l’équipe créative proposait officiellement. Bien évidemment, j’étais prêt à faire tout ce qui était en mon pouvoir pour rendre ce changement permanent. Pour en revenir à la réunion, elle se présentait ainsi… L’équipe créative et moi-même étions fortement pour le changement. Randy, je pense, était en faveur de cette idée, principalement parce qu’il sentait que l’équipe créative était en droit de défendre son projet et que ses raisons étaient valables, mais il était clairement disposé à se laisser convaincre du contraire si suffisamment de designers et de développeurs faisaient des d’histoires. À peu près la moitié du reste des participants à la réunion étaient neutres, attendant le déroulement de la discussion pour se décider. La dernière moitié était contre le changement, avec des résistances allant de ‘légère’ à ‘forte’. 

En gros, l’équipe créative devait rallier à sa cause la moitié des participants avant la fin de la réunion pour emporter le morceau. Comme je viens de vous le dire, je pense que la moitié des personnes était venue avec un a priori négatif sur la question, ce qui veut dire que l’équipe devait baratiner pour réussir à récupérer le vote de chaque indécis. Le moindre faux pas condamnerait très probablement le système race/classe.

### Race/classe, ça passe ou ça casse

Les membres de l’équipe créative comprirent bien l’importance de cette réunion. Ils réalisèrent une présentation Power Point expliquant pourquoi ils proposaient ce changement, pourquoi ils pensaient que c’était la bonne chose à faire, ainsi que ses avantages et ses inconvénients. Ce qui suit fut l’une des plus intéressantes réunions **Magic** auxquelles j’aie jamais assisté. Pour bien restituer l’essence de ce qui s’est passé, j’ai décidé d’avancer point par point (avec d’abord les avantages, puis les inconvénients), et de vous présenter ce que chaque camp avait à dire.

**Avantage n°1 : cela ajoute à l’ambiance au jeu**

L’équipe créative commença avec son argument le plus fort. Le système race/classe ajoute de la profondeur à l’univers du jeu de manière simple et élégante. L’autre camp argumenta que cette profondeur supplémentaire avait un prix, et que le nom, l’illustration et le texte d’ambiance conférait aux créatures une personnalité suffisante.

**Avantage n°2 : cela permet de s’aligner avec d’autres jeux de type fantasy**

L’idée était de dire que les joueurs avaient certaines attentes en matière de fantasy, et qu’il n’y avait pas de raison de ne pas répondre à leurs attentes dans le cas présent. La contradiction fut que **Magic** voulait justement se démarquer des autres jeux de fantasy, ce que des choses comme le type de créature unique contribuait à faire. 

**Avantage n°3 : cela donne plus de cohérence au jeu**

Cela n’avait pas de sens que certaines créatures ressemblant à des soldats aient le type soldat, et d’autres non. L’équipe créative fit valoir que ce manque de cohérence nuisait à l’ambiance du jeu. Les adversaires déclarèrent que **Magic** était plein de ce genre d’incohérences, ce que j’appelle l’argument du ‘Comment un terrain animé peut-il rentrer dans un cercueil ?’.

**Avantage n°4 : cela permet plus d’interactions entre les types de créatures**

C’est à ce moment-là qu’ils m’ont regardé et qu’ils m’ont dit : ‘Continue, Mark’. J’ai alors expliqué comment le système race/classe offrirait toutes sortes d’intéressantes possibilités de design. Un contradicteur répliqua : ‘Moi aussi je suis designer, et je ne vois pas comment cela peut créer la moindre possibilité de design’. Je vais maintenant prendre le temps de lui dire : ‘Vous voyez ? Vous aviez tort’. Ahhh, c’était super. Nous pouvons maintenant passer à la suite.

**Avantage n°5 : cela intègre le type de créature ‘humain’ au jeu**

![Sacrifice](https://i.ormos.uk/29/bc/29bcbfd16fd13baabd486275819375dea22c1f7ea1fdaabab37267dcdff55805.jpg)

L’une des choses les plus bizarres au sujet des types de créatures jusqu’alors, c’est que les humains n’avaient jamais été pris en compte sur la ligne de type de créature. Ne me faites pas dire ce que je n’ai pas dit, il existait des tas d’humains, mais cela n’avait aucun impact dans le jeu. L’équipe créative n’aimait pas cet état de faits, pour de multiples raisons. D’une part, c’était horriblement incohérent. Pourquoi pouviez-vous provoquer l’extinction des gobelins et pas des humains ? Pourquoi le Coat of Arms (Blason) aidait-il toutes les races sauf les humains ? D’autre part, presque toutes les créatures n’ayant qu’une classe pour type étaient des humains (puisque les humains ne pouvaient pas avoir de type correspondant à leur race). Et l’équipe créative espérait aussi qu’intégrer le type ‘humain’ à **Magic** créerait une pression en faveur de la diminution du nombre d’humains dans le jeu.

Ce fut l’un des points de friction majeurs. L’autre camp détestait l’idée de mentionner les humains, et eux aussi avaient leurs raisons. Certains avaient l’impression que le jeu perdrait de son aspect fantastique si l’on y ajoutait ce terme réel. (L’argument que l’on peut opposer à cela, c’est bien sûr qu’on trouve des humains dans à peu près toutes les histoires de fantasy.) Certains pensaient que cela modifiait fondamentalement la façon dont le jeu avait été conçu. Certains pensaient que cela poserait problème au niveau du design s’il existait un type ‘humain’ (et pourtant, remarquez qu’à ce jour nous n’avons jamais sorti de carte tribale spécifiquement liée aux humains). Ils n’arrêtaient pas de dire que nous ne pourrions jamais marquer sur une carte : ‘Sacrifiez un humain’. Mais en gros, l’argument était assez subjectif : ce changement ne nous plaît pas.

**Avantage n°6 : cela libère de la place pour le nom de la carte**

Un autre argument consistait à dire qu’une carte comme Goblin Assassin (Assassin gobelin) devait forcément s’appeler Goblin Assassin (Assassin gobelin) si nous voulions faire passer l’idée que c’était un gobelin qui tuait pour de l’argent. Si la ligne des types de créature pouvait transmettre cette information, cela permettrait à la ligne de titre d’être plus évocatrice que descriptive. Pour la partie adverse, il suffisait de laisser l’illustration faire son travail, et de ne pas se préoccuper de passer ce genre d’information dans le nom de la carte.

**Avantage n°7 : cela évite des contradictions**

L’une des raisons pour lesquelles les types de créatures étaient jusque-là très dispersés et hétéroclites, c’est qu’il n’existait pas vraiment de structure pour aider à définir qui devait être quoi. Cela avait entraîné beaucoup de problèmes, des choses cohérentes entre elles sur le plan de l’univers et de l’ambiance ne l’étant pas forcément du point de vue des mécaniques de jeu. Des cartes ayant quasiment le même texte se retrouvaient avec des types radicalement différents. Les opposants au projet dirent que c’était très bien comme ça, que le jeu n’avait pas besoin d’être aussi cadré.

**Avantage n°8 : cela aide à mieux définir les relations entre les couleurs et les types de créatures**

Comme corollaire à ce dernier point, procéder de la sorte nous permettait d’utiliser la race et la classe pour renforcer la roue des couleurs. L’équipe créative (et moi-même) étions convaincus que la roue des couleurs est au cœur du jeu, et que plus nous pourrions lier les éléments du jeu à elle, plus nous renforcerions le jeu. L’autre camp répliqua que nous accordions trop d’importance à cette roue des couleurs.

Venons-en à présent aux inconvénients.

**Inconvénient n°1 : c’est un changement**

L’un des principes de la R&D, c’est que nous ne devons pas changer les choses juste pour le plaisir de les changer. Oui, le jeu doit grandir et évoluer, mais il doit le faire pour de bonnes raisons. Pendant longtemps, les types de créatures ont fonctionné d’une certaine façon. Il n’aurait pas fallu y toucher si on avait pu résoudre le problème par d’autres moyens. C’est l’argument du ‘si ce n’est pas cassé, ne le réparez pas’. Auquel nous avons répondu : ‘c’est cassé’. Le système de l’époque posait des problèmes, il fallait le changer. De plus, nous en tirerions un gros bénéfice : plus d’ambiance et plus de possibilités de design.

**Inconvénient n°2 : cela rajoute des mots**

Un autre principes de la R&D est ‘plus de mots, c’est moins bien’ (personnellement, je ne crois pas complètement à ce principe, voyez mon article [Grokker ou ne pas grokker, là est la question](/en/articles/makingmagic/2006/10-16-between-a-grok-and-a-hard-place) à ce sujet). Chaque mot présent sur une carte a un prix. Pour réussir un bon ‘design et développement’, il faut savoir estimer combien de mots vous pouvez retirer à une carte, tout en lui conservant la même qualité. Notre réplique fut que nous pensions apporter une amélioration significative en très peu de mots, dans la plupart des cas un seul, et même pas dans la case du texte de règles.

**Inconvénient n°3 : la place disponible sur la ligne de type de créature devient un paramètre à prendre en compte**

La ligne de type de créature n’est pas infinie. Mettre plus de choses dessus pourrait causer des problèmes, en particulier pour les légendes (ou maintenant les créatures légendaires). La réponse fut que oui, c’était une considération importante, mais de celles qui pouvaient être gérées au cas-par-cas.

**Inconvénient n°4 : cela banalise les doubles types de créatures**

On nous a dit que les créatures ayant deux types était quelque chose qui impressionnait certains joueurs. Le faire plus souvent rendrait la chose moins originale. La réponse fut que si les joueurs aiment quelque chose, cela pouvait être bien de leur en donner plus.

**Inconvénient n°5 : cela oblige à des errata**

À partir du moment où l’on considère ‘assassin’ comme une classe, il est légitime de se demander pourquoi chaque créature étant conceptuellement un assassin, et en particulier celles dont le nom contient le mot ‘assassin’, ne serait pas du type ‘assassin’. L’autre camp souligna que notre changement obligerait à de nombreux errata, ce que la R&D considère généralement comme une chose à éviter. Notre réponse fut : ‘vous avez raison, c’est un inconvénient majeur’. Nous dûmes reconnaître qu’il s’agissait de l’argument le plus fort contre le changement.

**Inconvénient n°6 : cela intègre le type de créature ‘humain’ au jeu** 

Je ne suis pas certain de parvenir à bien exprimer à quel point certaines personnes refusaient d’écrire ‘humain’ sur des cartes (et pas seulement à la R&D ; j’ai reçu pas mal de mails lorsque nous avons introduit le type ‘humain’ dans le jeu). Néanmoins, chacun ayant son opinion, tout le monde a convenu qu’il ne fallait pas bloquer le débat là-dessus, notre camp ayant considéré que ce point était suffisamment positif pour le classer dans les avantages.

**Inconvénient n°7 : les cas non résolus comme celui des zombies**

Le dernier inconvénient regroupait en réalité de nombreux petits problèmes regroupés. Le terme zombie, par exemple, ne cadrait pas très bien dans le système race/classe, car il est parfois considéré comme une race et parfois comme une classe. Et que faire avec les non-humanoïdes ? Les créatures mythiques (comme les dragons et les anges) devaient-elles suivre le modèle race/classe ? Bref, on nous a dit que tous ces petits problèmes finiraient par s’additionner pour créer un gros problème. Nous avons répondu que la plupart de ces points étaient faciles à régler, et que ceux qui ne l’étaient pas ne suffisaient pas à remettre en cause le système.

### Affaire race/classée

![Primal_Whisperer](https://i.ormos.uk/dd/2b/dd2b0ec3bd1cf8b8a3b80382568379d6b0ecfe37e4454d7beb0f567e4453ec8f.jpg)

Quels furent les arguments qui finirent par faire pencher la balance en faveur du système race/classe ? Premièrement, la plupart des participants à la réunion virent ce système comme un ajout à la richesse de l’univers. Deuxièmement, nous avions mis en évidence assez d’incohérences flagrantes pour être en mesure d’affirmer que le système de l’époque posait des problèmes. Troisièmement, le succès du bloc *Carnage* confirma l’intérêt qu’il y avait à se concentrer davantage sur les types de créatures à l’avenir. Quatrièmement, et c’est selon moi la raison la plus importante : c’est la passion qui remporta la victoire. L’équipe créative était à fond pour ce changement (nous avons rarement droit à une présentation Power Point lors de la réunion **Magic** du mardi). Pour ma part, étant l’une des voix majeures du design, j’ai vraiment clamé haut et fort combien j’étais persuadé de l’importance de ce changement. Ceux d’en face n’approuvaient pas, mais ils n’étaient pas autant ‘contre’ que nous étions ‘pour’. Les indécis furent ralliés à notre cause, et le système race/classe devint une réalité.

J’ai voulu faire resurgir cette histoire aujourd’hui, parce que *Lèveciel* est une conséquence de cette passion. Si nous nous sommes tant battus pour ce changement, c’est justement pour rendre possible le genre de choses que nous faisons dans le bloc *Lorwyn*. Et en voyant tout cela porter ses fruits, je suis vraiment heureux que nous ayons remporté ce combat. C’est agréable de gagner. C’est encore mieux lorsqu’avec du recul, on réalise que l’on était du bon côté.

Et voilà, mes fidèles lecteurs, ce que mon subconscient voulait vous dire aujourd’hui.

Rendez-vous la semaine prochaine, où je vous entraînerai sur la voie des guerriers.

D’ici-là, puissiez-vous repenser aux beaux combats que vous avez livrés et remportés.

Mark Rosewater

*Traduction P.O. Barome*
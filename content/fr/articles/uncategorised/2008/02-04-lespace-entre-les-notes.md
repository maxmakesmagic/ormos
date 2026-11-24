---
id: q3bzk4pk
kind: article
lang: fr
path: /fr/articles/uncategorised/2008/02-04-lespace-entre-les-notes
title: L'espace entre les notes
published: '2008-02-04'
column_slug: uncategorised
column: uncategorised
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr317
    lang_detected: fr
    capture_id: 1976738
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr317,0
    captured_at: '2008-06-16 21:59:57+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr317
    lang_detected: fr
    capture_id: 1976738
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr317,0
    captured_at: '2008-06-16 21:59:57+00'
    rule: registry.known_article
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr317
    lang_detected: fr
    capture_id: 1976738
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr317,0
    captured_at: '2008-06-16 21:59:57+00'
    rule: registry.known_article
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr317
    lang_detected: fr
    capture_id: 1976738
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr317,0
    captured_at: '2008-06-16 21:59:57+00'
    rule: classic.column_marker
sources:
- document_id: q3bzk4pk
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr317,0
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr317
  lang: fr
  template: classic_asp
  captured_at: '2008-06-16 21:59:57+00'
  capture_id: 1976738
  wayback_url: https://web.archive.org/web/20080616215957id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr317,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: q3bzk4pk
  capture_id: 1976738
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr317,0
  wayback_url: https://web.archive.org/web/20080616215957id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr317,0
  captured_at: '2008-06-16 21:59:57+00'
  template: classic_asp
  sha256: efd3ff42482c4c08d217c28703c4e29d194038f03830905d6845fabeb2ca8a53
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Demolish')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Borborygmos')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Train_of_Thought')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Voice_of_Grace')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
  
**Quelle nouvelle latitude de conception le système race/classe nous donne-t-il vraiment ?**  
  

* * *

Pour moi, ce que je trouve génial avec [cette chronique](https://web.archive.org/web/20080516110323/http://www.wizards.com/default.asp?x=mtgcom/columnarchive&column=MakingMagic), c'est que je peux parler de tout ce dont j'ai envie sur le jeu. Aujourd'hui, vous allez avoir droit à, tenez-vous bien, un article philosophique sur la conception des cartes. Pourquoi ça ? On va tâcher de vous résumer ça.

Il y a deux semaines (dans mon article '[L'épique mise en place de l'efficace système race/classe](/en/articles/makingmagic/2008/01-21-the-amazing-race-class)'), je vous ai dit que je pensais que le système race/classe avait un potentiel de conception énorme. Après avoir dit ça, j'ai reçu un certain nombre de courriers me demandant si, au définitif, ce système avait réellement créé un nouvel espace de conception. La lettre suivante devrait parfaitement résumer l'avis général :

> Cher Mark,
> 
> Je lis ta chronique toutes les semaines et je voulais te dire que je pense qu’en règle générale, tu as un impact positif sur le jeu. Maintenant que je t’ai passé la pommade, vas-tu arrêter de vanter les mérites de 'l'étonnante latitude de conception' du système race/classe. Changer 'Tous les gobelins gagnent +1/+1' en 'Tous les soldats gagnent +1/+1' n'a rien de bien novateur ! L'innovation est définie par 'l'introduction de quelque chose de nouveau'. Alors explique-moi comment ce mot peut s’appliquer au traitement des classes comme des races ! *Carnage* l'a déjà fait depuis longtemps. Je sais que c'est ton boulot de nous dire que tout ce qui est nouveau dans le jeu est génialement spectaculaire, mais tu commences à perdre ta crédibilité quand tu essaies de nous vendre des restes mi-cuits comme une nouvelle merveille gastronomique. Accepte une bonne fois pour toute que le système race/classe ne donne pas naissance à un espace de conception qui n'a pas déjà été exploré il y a cinq ans.
> 
> Sincères salutations,
> 
> E.E. Wood

Comment j'ai réagi à ce genre de lettre ? J'étais excité comme un gamin. Vous ne vous attendiez pas à ça, hein ? J’ai réalisé que j'avais mal expliqué ce que j’entendais par nouvel espace de conception qui avait été créé par l'adoption du système race/classe. Ce qui, bien entendu, voulait dire qu’il ne me restait plus qu’à remplir une nouvelle chronique bien juteuse sur le sujet. Croyez-moi, quand vous devez écrire un article par semaine, ce genre de sujet, ça vous excite toujours un peu. De plus, il me permet d'aborder un aspect qui, je pense, est un élément clé présent dans le design de tout jeu de cartes à jouer et à collectionner. Ne me dites pas ce que n’est pas un sujet intéressant.

Et donc voilà ce qui nous amène à la chronique d’aujourd'hui. Alors restez avec nous si le sujet vous intéresse.

**'Tout acte de création est avant tout un acte de destruction.'**

![Demolish](https://i.ormos.uk/2b/c7/2bc7661ee90a735c33231ac5c48876cae8c5a80355a37aed055021cc5e34e2ac.jpg)J'ai fait des études de cinéma et de télévision spécialisées dans l'écriture de scénario. Par conséquent, j'ai suivi un certain nombre de cours d'écriture. De tous ces cours, la citation suivante est une des leçons que j'ai retenues le plus et qui, je crois, a influencé grandement la manière dont j'écris et conçois des cartes. Voici la citation :

> ***Aucune scène ne doit souffrir d'un dialogue ; aucun film ne doit souffrir d'une scène.***

Laissez-moi vous traduire. Mon prof essayait d'expliquer la chose suivante : quand on écrit le scénario d'un film (d'une série télé ou d'une pièce de théâtre ou autre projet similaire), l'ensemble est plus important que les éléments pris séparément. Souvent, les scénaristes tombent amoureux d'une phrase de dialogue ou d'une scène spécifique au point de tenir absolument à la placer dans le film, même si elle n'y a pas vraiment sa place. Chaque réplique d'un bon script doit faire avancer l'histoire. Si le scénariste perd son temps à vouloir placer un élément qu'il aime, mais qui n'accomplit rien dans ce sens, il fait baisser la qualité de son travail.

Cette leçon est cruciale et, comme je l'expliquerai un peu plus loin, au cœur de ce qui fait un bon design de carte à jouer et à collectionner. Tous les artistes ont tendance à tomber amoureux de leurs créations. Ce n'est pas une mauvaise chose. En fait, je crois qu'il est essentiel que l'artiste soit totalement impliqué dans ce qu'il fait pour que le résultat soit bon. Mais dans l'art, il est important à la fois de s'auto-évaluer et de s'autocensurer. La moindre idée, le moindre mot, le moindre détail de votre création doit faire l'objet d'un examen critique. Certes, ce bout de dialogue est peut-être la réplique la plus hallucinante que vous ayez jamais écrite, mais s'il n'est pas à sa place, son ingéniosité n'aura aucune importance.

Mon professeur nous enseignait que pour obtenir les meilleurs résultats, il faut apprendre à couper ce qui ne fonctionne pas. Et faites-moi confiance, parfois, ça fait mal. C'est facile de se débarrasser de quelque chose qu’on n'aime pas. Mais c'est plus difficile de le faire avec quelque chose qu’on aime. Pourtant, c'est une partie intégrante de l'acte de création. 

Alors qu'est-ce que tout ça vient faire dans la conception des cartes à jouer et à collectionner ? C’est une excellente question.

**'Au royaume des aveugles, les borgnes sont roi.'**

![Borborygmos](https://i.ormos.uk/d9/14/d914a6c55e9a861900d53c0f1a41564c40081d3eb4202bef0f006104eb4c0933.jpg)Expliquons à présent comment tout ceci s'applique à la conception des cartes. Quand ils évaluent une extension, la plupart des gens commencent par regarder des cartes individuelles. En fait, la plupart des articles qui annoncent la sortie d'une extension commencent par l'étude de ses cartes une à une. C'est pour cette raison que, je pense, bon nombre de gens en arrivent à la conclusion suivante : la qualité d'une extension est déterminée par la qualité de ses cartes individuelles. Ceux qui sont d'accord avec cette affirmation, levez la main ! Qui n'est pas d'accord ? Groupe deux, vous gagnez une médaille en chocolat. La qualité d'une extension (à mon humble avis) n'est pas déterminée par la qualité de ses cartes prises séparément.

Pour prouver ce que j'avance, faisons une expérience hypothétique. Supposons que je sois le directeur de conception d'une extension et que le mette en place une structure qui explique quel rôle chaque carte va devoir y jouer. Cette carte est une petite créature blanche courante. Cette carte est un sort de blessures directes rouge inhabituelle. Cette carte est un enchantement de base de construction de deck noir rare. Ensuite, j'embauche X des meilleurs concepteurs de cartes au monde, X étant le nombre de cartes dans l'extension. Chacun d'eux a une carte et six mois pour la concevoir. Pendant ces six mois, je fais aussi le design de l'ensemble des cartes de l'extension. Une fois les six mois écoulés, je me retrouve avec deux extensions, une conçue par un groupe des meilleurs designers de cartes, et l'autre, par mes soins. Laquelle devrait être la meilleure ?

Pour les différencier plus facilement, j'appelle la première conception de groupe, et la deuxième, conception unique. Quel sera la meilleure extension ? Sans hésiter, la conception unique. Et non, je ne dis pas que je suis meilleur que les deux cents meilleurs concepteurs de cartes au monde. (J'ai un énorme ego, mais, en dépit de ce que pourrait indiquer ma photo, il n'est pas énorme *à ce point*.) Ce que j'essaie de vous expliquer, c'est que dans la conception unique, chaque carte aura été créée en tenant compte des autres cartes. L'extension aurait une synergie ; les cartes seront conçues pour fonctionner avec les autres cartes. La conception de groupe aura très probablement des cartes incroyables, mais l'extension, de par sa nature, n'aura aucune unité. Elle sera particulièrement chaotique et bon nombre de cartes empièteront sur leurs voisines dans leur couleur ou leur rareté . Certaines même risquent de combattre activement ce que d'autres essaient de faire.

Mais passons à l'aspect le plus intéressant de l'expérience : en admettant que vous preniez ces deux extensions et que vous pratiquiez une étude de marché en montrant certaines cartes choisies aléatoirement, je suis prêt à mettre ma main au feu que la conception de groupe rencontrera plus de succès que la conception unique, étant donné que chaque concepteur aura eu tout le temps possible pour maximiser l'impact de sa carte. Dans un deuxième cas d’étude de marché, nous laisserons les cartes à des joueurs pendant une semaine pour les tester et nous rassemblerons ensuite leurs commentaires. Je suis certain que dans cette situation, la conception unique aura plus de succès que la conception de groupe. 

Si l'une des extensions a plus de succès dans un cas et l'autre, le plus de succès dans l'autre, comment pouvons-nous déterminer avec certitude que la conception unique est la meilleure ? Parce que le premier cas rappelle la manière dont beaucoup de gens font connaissance avec une extension : en regardant des cartes individuellement. Le deuxième cas, lui, rappelle l'expérience du jeu dans le monde réel. Les joueurs jugent leurs cartes en fonction de leur comportement en *jeu*. Qu'est-ce qui se traduira au définitif par plus de ventes à long terme (oui, je crois que les ventes de cartes sont les meilleures données de base qui vous permettent de déterminer la popularité d'une extension), l'extension qui vous a excité quand vous avez ouvert votre premier booster ou celle qui vous a permis de vous éclater ? Je peux vous donner la réponse sans hésiter. Sans citer de noms, je dirai qu'il y a eu des extensions de **Magic** qui avaient l'air fabuleuses mais qui ne se jouaient pas aussi bien que d'autres qui, elles, n'avaient pas l'air folichonnes mais se comportaient de manière extraordinaire en jeu, et ce sont elles qui se sont vendues le mieux à long terme. 

Ce qui m'amène enfin là où je voulais en venir. Les extensions sont jugées par leur fonctionnement en jeu, ce qui veut dire que leur qualité dépend surtout de l'ensemble, et pas de ses éléments pris séparément. La synergie est reine dans un jeu construit autour de l’interaction de ses pièces. Par conséquent, la qualité d'une extension est bien plus basée sur sa synergie que sur la conception individuelle de ses cartes. Vous remarquerez que l'évolution de la technologie de **Magic** s'est orientée de plus en plus sur la synergie. À mesure que nous avons amélioré notre compréhension du design des cartes, nous nous sommes de plus en plus concentrés sur la manière dont les pièces fonctionnent ensemble.

Un petit aparté – je tiens à insister sur le fait que créer la synergie ne veut pas dire qu'on se contente de créer des cartes linéaires. Autrement dit, la synergie ce n'est pas simplement une question de créer des cartes qui vont être jouées avec une autre série limitée de cartes. Les cartes modulaires sans restriction d'utilisation peuvent être créées avec tout autant de potentiel de synergie, surtout à partir du moment où les designers comprennent la direction prise par ces cartes à long terme. 

Ce qui nous ramène à la citation de mon professeur. Appliquons-la à la conception des cartes. Aucune extension ne doit souffrir d'une carte. Ce qui signifie qu'un concepteur ne devrait jamais inclure une carte, la meilleure soit-elle, si elle va à l'encontre du reste de l'extension. (Oui, je sais, ça nous arrive de temps en temps, mais je suis presque toujours d'avis que c'est au détriment de l'extension ; remarquez aussi qu'être neutre dans une extension n'est pas pareil que la contredire.) Rappelez-vous, **Magic** est un véritable consommateur de design. Si vous avez créé une bonne carte, elle trouvera un foyer. Il finira bien par y avoir une extension où elle aura sa synergie (ou sa position neutre dans le pire des cas). Ce foyer, cependant, ne sera pas très souvent l'extension pour laquelle vous l’avez créée. C'est une des leçons les plus importantes à retenir pour un nouveau designer. La pilule est dure à avaler. Il est très difficile de résister au désir de combattre tout de suite pour votre bébé. Mais comme me l'a appris mon professeur il y a des années, s'appliquer à la qualité de votre art, c'est comprendre la priorité de vos choix.

**'La découverte, c'est voir ce que tout le monde a vu et penser ce à quoi personne n'a pensé.'**

![Train_of_Thought](https://i.ormos.uk/e5/a4/e5a40658a839397dbc5a3121f195b30a5efe5669b9d6a58518837eddfa941c51.jpg)Mais quel est le rapport avec ce que le système race/classe offre à la conception ? Pour commencer, cette réflexion montre que ma vision du jeu est très différente quand je prends en compte le système race/classe. Je ne cherche pas à déterminer ce qu'une carte individuelle peut créer, mais plutôt quel style d'*environnement* elle peut créer. Que peut-on faire avec cette race/classe sans avoir un état d'esprit concepteur de carte individuelle, mais un état d'esprit de synergie collective ? Quel type d'environnement le système race/classe pourra créer qu'un type de créature unique ne pourra pas ?

Pour le comprendre, examinons quatre types de créature que j'appellerai Type de créature A, Type de créature B, Type de créature C et Type de créature D. Quels genres de cartes puis-je concevoir en me basant sur un monde de types de créature uniques ? Je peux créer des cartes 'Type de créature A délire', des cartes 'Type de créature B délire', des cartes 'type de créature C délire' et des cartes 'Type de créature D délire'. Quels decks permettront de jouer ces créatures ? Quatre types de deck : les decks de type de créature A, les decks de type de créature B, les decks de type de créature C et les decks de type de créature D.

À présent, passons dans le monde du système race/classe. Nous allons supposer que les types de créature A et B sont des races et que les types de créature C et D sont des classes. Une fois de plus, je crée des cartes 'Type de créature A délire', des cartes 'Type de créature B délire', des cartes 'type de créature C délire' et des cartes 'Type de créature D délire'. Combien de decks puis-je construire ? Bien plus que quatre. Pour commencer, j'aurai toujours les decks précédents : les decks de type de créature A, les decks de type de créature B, les decks de type de créature C et les decks de type de créature D. Ensuite viendront toutes les combinaisons de races et de classes. Puis j’aurai la capacité de donner la priorité à un type de race (ce qui voudra dire que chaque carte de mon deck sera de ce type) et d'avoir un sous-thème avec les deux types de classe, ou encore de donner la priorité à un type de classe et d'avoir un sous-thème avec les deux types de race. Ce qui créera encore quatre decks supplémentaires. Pour résumer, dans un monde de système race/classe, j'ai la liberté de mélanger les types de créature bien plus facilement que dans un monde de types de créature uniques.

Mais attendez, ce n'est pas tout. Examinons les situations créées par ces deux environnements en jeu. Pour ce faire, laissez-moi le temps de créer rapidement quelques cartes.

> **Bonhomme 1**  
> \<coût de mana>  
>  Créature – A  
>  1/1

> **Bonhomme 2**  
> \<coût de mana>  
>  Créature – B  
>  1/1

> **Bonhomme 3**  
> \<coût de mana>  
>  Créature – C  
>  1/1

> **Bonhomme 4**  
> \<coût de mana>  
>  Créature – D  
>  1/1

> **Les A sont géniaux**  
> \<coût de mana>  
>  Enchantement  
>  Les créatures A que vous contrôlez gagnent +1/+1

> **B comme basilic**  
> \<coût de mana>  
>  Enchantement  
>  Les créatures B que vous contrôlez acquièrent le contact mortel

> **Les C sont habiles**  
> \<coût de mana>  
>  Enchantement  
>  Les créatures C que vous contrôlez acquièrent l'initiative

> **Les D sont rusés**  
> \<coût de mana>  
>  Enchantement  
>  Les créatures D que vous contrôlez acquièrent le lien de vie

Dans le monde des types de créature uniques, voilà ce qui peut se passer :

*   Bonhomme 1 devient 2/2.
*   Bonhomme 2 acquiert le contact mortel.
*   Bonhomme 3 acquiert l'initiative.
*   Bonhomme 4 acquiert le lien de vie.

Pour le monde de système race/classe, nous allons garder les mêmes enchantements, mais mettre à jour nos créatures :

> **Bonhomme 1**  
> \<coût de mana>  
>  Créature – AC  
>  1/1

> **Bonhomme 2**  
> \<coût de mana>  
>  Créature – AD  
>  1/1

> **Bonhomme 3**  
> \<coût de mana>  
>  Créature – BC  
>  1/1

> **Bonhomme 4**  
> \<coût de mana>  
>  Créature – BD  
>  1/1

Dans le monde de modèle race/classe, voilà ce qui peut se passer :

*   Bonhomme 1 devient 2/2.
*   Bonhomme 2 acquiert le contact mortel.
*   Bonhomme 3 acquiert l'initiative.
*   Bonhomme 4 acquiert le lien de vie.
*   Bonhomme 1 acquiert l'initiative.
*   Bonhomme 2 acquiert le lien de vie.
*   Bonhomme 3 acquiert le contact mortel.
*   Bonhomme 4 devient 2/2.
*   Bonhomme 1 devient 2/2 et acquiert l'initiative.
*   Bonhomme 2 acquiert le contact mortel et le lien de vie.
*   Bonhomme 3 acquiert le contact mortel et l'initiative.
*   Bonhomme 4 devient 2/2 et acquiert le lien de vie.

Le système race/classe vient de tripler les possibilités de jeu. De plus, il a créé des états de jeu qui seraient impossibles dans un monde de types de créature uniques. Le contact mortel et l'initiative, par exemple, fonctionnent particulièrement bien en combo, mais cette interaction ne serait pas possible dans un monde de types de créature uniques. De plus, remarquez que ces modifications s'accélèrent dès que des options supplémentaires sont ajoutées. 

Le système race/classe accroît les options de construction de deck et l'interaction des cartes, ce qui donnent à l'équipe de conception de nouvelles directions à explorer. Si des decks peuvent être construits autour d'une race et d'une classe, cela permet la création de cartes conçues spécialement pour ce type de deck. Si l'interaction des cartes s'accroît, cela permet la création d'effets spécialement conçus pour l'interaction. Chacune de ces options ouvre de nouvelles disponibilités pour les joueurs, ce qui à son tour permet aux designers de créer de nouvelles possibilités de jeu. 

Vous vous rappelez l'importance de la synergie expliquée un peu plus tôt ? Plus que tout, le système race/classe permet de développer de toutes nouvelles synergies. Plutôt que des types de créature agissant en parallèle, nous avons à présent des types de créature qui s'entrecroisent. Toute carte tribale a maintenant le potentiel de fonctionner avec n'importe quelle autre carte de l'extension. Le système race/classe ajoute une dynamique qui réinvente complètement les possibilités des cartes tribales. C'est *ça* l'espace, la latitude de conception supplémentaire dont je parlais. 

### Bonne nuit les petits

![Voice_of_Grace](https://i.ormos.uk/33/1a/331a819dce61d28761a393d0a66d3a66d003830bed6a091a649f8aea8eac0898.jpg)J'espère que la chronique d'aujourd'hui vous aura donné matière à réfléchir. Je suis impatient de lire vos réactions sur le forum et dans ma boîte email. Et si quelqu'un a envie de m'envoyer un méchant email, faites donc ! J'ai toujours besoin de matière pour alimenter ma chronique. 

Retrouvez-moi la semaine prochaine ; je serai encore plus marquant que d'habitude.

En attendant, j'espère que vous comprenez maintenant quelle est la valeur du détachement.

Mark Rosewater 

*Traduction Bruno Billion*
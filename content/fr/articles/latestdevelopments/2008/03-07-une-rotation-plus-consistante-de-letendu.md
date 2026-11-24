---
id: h9fr8ag9
kind: article
lang: fr
path: /fr/articles/latestdevelopments/2008/03-07-une-rotation-plus-consistante-de-letendu
title: Une rotation plus consistante de l’Étendu
published: '2008-03-07'
column_slug: latestdevelopments
column: Latest Developments
authors:
- slug: devinlow
  name: Devin Low
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?=RSS-MTGCOM,0&x=mtgcom/daily/dl27
    lang_detected: fr
    capture_id: 1262123
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dl27&=RSS-MTGCOM,0
    captured_at: '2008-05-19 08:08:25+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?=RSS-MTGCOM,0&x=mtgcom/daily/dl27
    lang_detected: fr
    capture_id: 1262123
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dl27&=RSS-MTGCOM,0
    captured_at: '2008-05-19 08:08:25+00'
    rule: registry.known_article
  authors:
    page_key: wizards.com/default.asp?=RSS-MTGCOM,0&x=mtgcom/daily/dl27
    lang_detected: fr
    capture_id: 1262123
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dl27&=RSS-MTGCOM,0
    captured_at: '2008-05-19 08:08:25+00'
    rule: classic.byline
  column:
    page_key: wizards.com/default.asp?=RSS-MTGCOM,0&x=mtgcom/daily/dl27
    lang_detected: fr
    capture_id: 1262123
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/dl27&=RSS-MTGCOM,0
    captured_at: '2008-05-19 08:08:25+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: h9fr8ag9
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dl27&=RSS-MTGCOM,0
  page_key: wizards.com/default.asp?=RSS-MTGCOM,0&x=mtgcom/daily/dl27
  lang: fr
  template: classic_asp
  captured_at: '2008-05-19 08:08:25+00'
  capture_id: 1262123
  wayback_url: https://web.archive.org/web/20080519080825id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dl27&=RSS-MTGCOM,0
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: h9fr8ag9
  capture_id: 1262123
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/dl27&=RSS-MTGCOM,0
  wayback_url: https://web.archive.org/web/20080519080825id_/http://www.wizards.com/default.asp?x=mtgcom/daily/dl27&=RSS-MTGCOM,0
  captured_at: '2008-05-19 08:08:25+00'
  template: classic_asp
  sha256: 6d891301d475cfd26f03474b57a4b54be6de9b16587e88e272bfb6c33e1c8c81
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Imperious_Perfect')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Imperious Perfect
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Crop_Rotation')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Incremental_Growth')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Tormod[s_Crypt')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Tormod’s Crypt
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Leyline_of_the_Void')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Leyline of the Void
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Ancestral_Memories')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: unsupported_link
  element: a
  target: javascript:void(0)
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - ici
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Forest')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
  
**Comment et pourquoi nous avons changé la façon dont tourne l’Étendu.**  
  

* * *

Bienvenue. Aujourd’hui je vais vous parler de notre [récente modification](https://web.archive.org/web/20080514111411/http://www.wizards.com/default.asp?x=dci/announce/dci20080229a) de la rotation de l’Étendu. Si les tournois ne sont pas votre tasse de thé, n’hésitez pas à sauter cet article et à revenir plus tard.

<table>&#10;<tbody><tr>&#10;<td>&#10;<table>&#10;<tbody><tr>&#10;<td>&#10;                 <b>Quiz rapide</b></td>&#10;<td> </td>&#10;<td><img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td colspan="3">&#10;<table>&#10;<tbody><tr>&#10;<td> Avec l’ancien système de rotation de l’Étendu, combien d’années d’extensions <b>Magic</b> auraient été légales en octobre 2009, quand l’extension au nom de code ‘Live’ deviendra autorisée en jeu ? </td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

Est-ce que la réponse est un petit peu trop difficile à trouver de tête ? Est-ce que la réponse est ‘je vais de voir regarder’ ? C’est parce que l’ancien système n’est pas très facile à retenir. C’est l’une des raisons de l’annonce récente d’une rationalisation du système de rotation de l’Étendu pour une définition nouvelle, plus simple et tenant en seize mots :

*‘L’Étendu est composé des sept dernières années d’extensions **Magic** et d’éditions de base.’*

### Comment est-ce que la rotation de l’Étendu a été modifiée ?

Mise en œuvre il y a six ans en mai 2002, l’ancien système de rotation de l’Étendu faisait sortir trois blocs **Magic** tous les trois ans. Ce système est facile à décrire dans l’absolu, mais savoir ce qui est légal à un moment donné ou ce qui sera légal dans une paire d’années est difficile. 

<table>&#10;<tbody><tr>&#10;<td>&#10;<table>&#10;<tbody><tr>&#10;<td>&#10;                 <b>Quiz rapide n°2</b></td>&#10;<td> </td>&#10;<td><img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td colspan="3">&#10;<table>&#10;<tbody><tr>&#10;<td>Avec l’ancienne politique de rotation, combien de temps l’<a>Imperious Perfect</a> (Parfaite impérieuse) aurait été légale en Étendu ?</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

  

Avec l’ancienne politique de rotation, pour trouver la réponse, il aurait sans doute fallu avoir accès à l’internet, un crayon numéro deux, un rapporteur, et un livre d’annales du baccalauréat. 

Avec la nouvelle politique de rotation, pour trouver la réponse, répondez juste ‘sept ans’. Parce que maintenant tous les blocs seront légaux en Étendu pour sept ans. 

Donc concrètement comment a été modifié la rotation de l’Étendu? La grande différence est qu’avec l’ancien système, l’Étendu contenait parfois les blocs de six années, parfois les blocs de sept années, et parfois les blocs de huit années. Par contraste, avec le nouveau système de rotation, l’Étendu contient toujours sept années de blocs.

De la même façon, avec l’ancien système, certains blocs étaient légaux en Étendu pour six ans, d’autres étaient légaux pour sept ans, et certains étaient légaux pour huit ans. Avec le nouveau système de rotation, chaque bloc est légal pour exactement sept ans. 

Le meilleur moyen de montrer la différence est visuel :

  

<table><tbody><tr><td colspan="4">ANCIEN SYSTÈME DE ROTATION </td>&#10;</tr>&#10;<tr><td>Oct 2008</td>&#10;<td>Oct 2009</td>&#10;<td>Oct 2010</td>&#10;<td>Oct 2011</td>&#10;</tr>&#10;<tr><td>6 Blocs</td>&#10;<td>7 Blocs</td>&#10;<td>8 Blocs</td>&#10;<td>6 Blocs</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td> </td>&#10;<td> </td>&#10;</tr>&#10;<tr><td><i>Mirrodin</i></td>&#10;<td><i>Mirrodin</i></td>&#10;<td><i>Mirrodin</i></td>&#10;</tr>&#10;<tr><td><i>Kamigawa</i></td>&#10;<td><i>Kamigawa</i></td>&#10;<td><i>Kamigawa</i></td>&#10;</tr>&#10;<tr><td><i>Ravnica</i></td>&#10;<td><i>Ravnica</i></td>&#10;<td><i>Ravnica</i></td>&#10;</tr>&#10;<tr><td><i>Spirale Temporelle</i></td>&#10;<td><i> Spirale Temporelle </i></td>&#10;<td><i> Spirale Temporelle </i></td>&#10;<td><i> Spirale Temporelle </i></td>&#10;</tr>&#10;<tr><td><i>Lorwyn / Sombrelande</i></td>&#10;<td><i>Lorwyn / Sombrelande </i></td>&#10;<td><i>Lorwyn / Sombrelande </i></td>&#10;<td><i>Lorwyn / Sombrelande </i></td>&#10;</tr>&#10;<tr><td> ‘Rock’</td>&#10;<td>‘Rock’</td>&#10;<td>‘Rock’</td>&#10;<td>‘Rock’</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td>‘Live’</td>&#10;<td>‘Live’</td>&#10;<td>‘Live’</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td> </td>&#10;<td>‘Lights’</td>&#10;<td>‘Lights’</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td> </td>&#10;<td> </td>&#10;<td>‘Shake’</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td> </td>&#10;<td> </td>&#10;</tr>&#10;</tbody></table>

  
  

<table><tbody><tr><td colspan="4">NOUVEAU SYSTEME DE ROTATION </td>&#10;</tr>&#10;<tr><td>Oct 2008</td>&#10;<td>Oct 2009</td>&#10;<td>Oct 2010</td>&#10;<td>Oct 2011</td>&#10;</tr>&#10;<tr><td>7 Blocs</td>&#10;<td>7 Blocs</td>&#10;<td>7 Blocs</td>&#10;<td>7 Blocs</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td> </td>&#10;<td> </td>&#10;</tr>&#10;<tr><td><i>Carnage</i></td>&#10;<td> </td>&#10;<td> </td>&#10;</tr>&#10;<tr><td><i>Mirrodin</i></td>&#10;<td><i>Mirrodin</i></td>&#10;<td> </td>&#10;</tr>&#10;<tr><td><i>Kamigawa</i></td>&#10;<td><i>Kamigawa</i></td>&#10;<td><i>Kamigawa</i></td>&#10;</tr>&#10;<tr><td><i>Ravnica</i></td>&#10;<td><i>Ravnica</i></td>&#10;<td><i>Ravnica</i></td>&#10;<td><i>Ravnica</i></td>&#10;</tr>&#10;<tr><td><i>Spirale Temporelle</i></td>&#10;<td><i> Spirale Temporelle </i></td>&#10;<td><i> Spirale Temporelle </i></td>&#10;<td><i> Spirale Temporelle </i></td>&#10;</tr>&#10;<tr><td><i>Lorwyn / Sombrelande</i></td>&#10;<td><i>Lorwyn / Sombrelande </i></td>&#10;<td><i>Lorwyn / Sombrelande </i></td>&#10;<td><i>Lorwyn / Sombrelande </i></td>&#10;</tr>&#10;<tr><td>‘Rock’</td>&#10;<td>‘Rock’</td>&#10;<td>‘Rock’</td>&#10;<td>‘Rock’</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td>‘Live’</td>&#10;<td>‘Live’</td>&#10;<td>‘Live’</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td> </td>&#10;<td>‘Lights’</td>&#10;<td>‘Lights’</td>&#10;</tr>&#10;<tr><td> </td>&#10;<td> </td>&#10;<td> </td>&#10;<td>‘Shake’</td>&#10;</tr>&#10;<tr><td> </td>&#10;</tr>&#10;</tbody></table>

Vous avez pu remarquer que ce tableau contient quelques noms de code des prochaines extensions. En 2005, Mark Rosewater a organisé un sondage pour déterminer les noms de code à venir. Quand [il a annoncé les résultats](/en/articles/makingmagic/2005/05-09-epic-struggles), il a révélé que le bloc débutant en automne cet année aurait pour nom de code ‘Rock’ / ‘Paper’ / ‘Scissors,’ et que le bloc suivant aurait pour nom de code ‘Live’ / ‘Long’ / ‘Prosper.’ Aujourd’hui, j’ai l’honneur d’annoncer en exclusivité que le bloc débutant en automne 2010 aura pour nom de code ‘Lights’ / ‘Camera’ / ‘Action,’ et que le bloc débutant en automne 2011 aura pour nom de code ‘Shake’ / ‘Rattle’ / ‘Roll.’ Chacun d’entre eux sont l’un des triplés qui apparaissaient dans le sondage de Mark. 

### Détails sur la rotation de l’Étendu

*’L’Étendu est composé des sept dernières années d’extensions **Magic** et d’éditions de base.’*

![Crop_Rotation](https://i.ormos.uk/6d/58/6d58a80553d85d518ca52cc0d3f1b010f76c6ccb0f27ddd74a45a22f5cc66335.jpg)Chaque année, quand une nouvelle extension principale sera lancée en automne et deviendra légale en Étendu, les blocs de l’année la plus ancienne encore en Étendu en sortent.

*Souffle glaciaire* sortira de l’Étendu en même temps que le bloc *Spirale Temporelle* en 2013, sept ans après l’entrée de *Spirale Temporelle* dans l’Étendu. (La rotation de *Souffle glaciaire* est attachée à celle du bloc *Spirale Temporelle*, comme en Standard.) 

Le bloc *Lorwyn* / *Lèveciel* et le bloc *Sombrelande* / *Coucheciel* comptent comme ‘le bloc d’une année’. Les quatre extensions sortiront ensemble de l’Étendu, en 2014, sept ans après l’entrée de *Lorwyn* dans l’Étendu.

### Exemples de Rotation de l’Étendu

Quand ‘Rock’ deviendra légal en tournoi cet octobre, les blocs *Odyssée* / *Tourment* / *Jugement* et la *Septième Édition* sortiront de l’Étendu. À ce moment là, les sept années de blocs légaux en Étendu seront *Carnage*, *Mirrodin*, *Kamigawa*, *Ravnica*, *Spirale Temporelle*, *Lorwyn* / *Sombrelande*, et le bloc ‘Rock’. *Souffle glaciaire* sera légal car il reste avec le bloc *Spirale Temporelle*. Toutes les éditions de base à partir de la *Huitième Édition* seront légales. 

Lorsque ‘Live’ deviendra légal en tournoi en octobre 2009, les blocs *Carnage* / *Légions* / *Fléau* sortiront de l’Étendu. À ce moment là, les blocs des sept années légaux en Étendu seront *Mirrodin*, *Kamigawa*, *Ravnica*, *Spirale Temporelle*, *Lorwyn* / *Sombrelande*, le bloc ‘Rock’, et le bloc ‘Live’. *Souffle glaciaire* sera légal car il reste avec le bloc *Spirale Temporelle*. Toutes les éditions de base à partir de la *Huitième Édition* seront légales.

Les éditions de base des sept dernières années seront également légales. Lorsque ‘Rock’ entrera dans l’Étendu cet octobre, les éditions de base des sept dernières années seront en Étendu elles aussi : la *Huitième Édition*, la *Neuvième Édition*, et la *Dixième Édition*. Lorsqu’une édition de base sera lancée en été 2009, rien ne sortira de l’Étendu et la *Huitième Édition* restera légale, puisque la *Huitième Édition* aura été lancée au cours des sept dernières années. Quand ‘Live’ entrera dans l’Étendu en octobre 2009 et que le bloc *Carnage* en sortira, la Huitième Édition sera toujours légale, puisqu’elle a été lancée dans les sept dernières années.

### Pourquoi avons-nous modifié le système de rotation de l’Étendu ?

Il y a trois raisons principales derrière cette modification : 

**1) Chaque bloc devrait être légal en Étendu pour la même durée de temps.**

Avec l’ancien système, il était injuste et bizarre que certains blocs soient légaux en Étendu durant un total de huit ans, que certains l’étaient pour un total de sept ans, et que d’autres l’étaient pour un total de huit ans. Par exemple, avec l’ancien système, *Invasion* aurait été légal en Étendu pour huit ans, *Odyssée* aurait été légal en Étendu pour sept ans, et *Carnage* aurait été légal en Étendu pour seulement six ans.

Pourquoi est-ce que *Carnage* aurait du être condamné à sortir si vite ? Pourquoi est-ce que les cartes de *Carnage* devraient avoir une durée de vie plus courte en Étendu que les cartes d’*Invasion* ? Ces durées de vie différentes étaient complètement arbitraires. Si *Masques de Mercadia* avait été lancé en 2000 au lieu de 1999, ils auraient été légaux en Étendu pour un total de huit ans au lieu de six ans. C’était complètement aléatoire, basé uniquement sur le numéro de l’année de lancement de l’extension. 

La nouvelle politique de rotation est plus consistance et plus équitable pour chaque bloc. Le nouveau système garde les blocs légaux en Étendu pour exactement sept ans, et ce pour tous les blocs.

**2) Historiquement, les formats Étendus couvrant huit années étaient un peu trop gros, et les formats Étendus couvrant six années étaient un peu trop petits. Nous pensons que les formats Étendus couvrant sept années ont eu les meilleurs jouabilité, puissance, vitesse et équilibre entre les types de decks, et niveau d’interaction.**

Après avoir décidé de donner à chaque bloc la même durée de légalité en Étendu, la question devint ‘Combien de temps chaque bloc devrait-il être légal ?’ La popularité de l’Étendu n’a cessé de grandir durant les six dernières années, depuis qu’il s’est séparé il y a plusieurs années de ses racines datant de l’Âge de Pierre, le format ‘Type 1.X’ semblable au Legacy.

![Incremental_Growth](https://i.ormos.uk/77/50/7750dc3b6295087259d93586a6b40a76e1c2dd627b1f7d4f50a689bc8752e6a0.jpg)Durant les six dernières années, le contenu de l’Étendu a oscillé entre six années de cartes et huit années de cartes, et les joueurs ont signalé que cette taille semblait correcte. Il est important pour nous et pour les joueurs que l’Étendu soit très différent du Standard, et très différent du Legacy et du Vintage. L’Étendu s’est vraiment forgé sa propre personnalité.

La durée de vie moyenne d’un bloc en Étendu a été de sept années, et nous pensons que c’est la bonne durée. Pour maintenir le niveau de jouabilité, puissance, vitesse, équilibre entre les types de decks et le niveau d’interaction de l’Étendu de ces dernières années, nous pensons que nous devrions rester à cette durée de vie moyenne de sept ans qui a bien fonctionné pour le format jusqu’à présent. Le meilleur moyen de garder à l’identique les sensations de l’Étendu est de garder à l’identique la durée de vie moyenne d’un bloc en Étendu : sept ans. 

En outre, quand l’Étendu a inclus huit années d’extension (une fois tous les trois ans), il a parfois menacé d’être trop rapide, avec des parties décidées trop vite et avec trop peu d’interactions en jeu. Les decks combos ont toujours été puissants en Étendu, mais ils peuvent être tout particulièrement déments durant ces formats Étendus de huit ans. Par exemple, le format Étendu actuel est fort de huit années d’extensions, et Dredge peut gagner avec consistance au tour deux ou trois, n’étant maintenu sous contrôle que par des réponses à zéro manas telles que Tormod’s Crypt (Crypte de Tormod) et Leyline of the Void (Ligne ley du vide). 

En général, les decks combos sont une part naturelle et saine de l’Étendu, mais les formats Étendus de huit ans permettent aux decks combos d’aller trop hors de portée. Plus il y a de cartes disponibles dans un format, plus les decks combos tendent à être puissants. 

Le développeur **Magic** et vétéran du Top 8 du Pro Tour – Rome 1998 (en Étendu) Erik Lauer donne des détails : 

<table>&#10;<tbody><tr>&#10;<td>&#10;<table>&#10;<tbody><tr>&#10;<td>&#10;                 <b>Erik Lauer</b></td>&#10;<td> </td>&#10;<td><img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td colspan="3">&#10;<table>&#10;<tbody><tr>&#10;<td><img src="https://i.ormos.uk/b7/c2/b7c24cd96722a8fbb2f047f78b572529a10036aa72bbd36721bcbb2f09297fc3.jpg">Lorsqu’un format s’agrandit, les différents types de decks ont un taux de croissance en puissance différent. En particulier les decks combo tendent à mieux bénéficier des choix supplémentaires que ne le font les decks agressifs. Les deux s’améliorent, mais le premier peut devenir bien plus sûr et résistant, outre un gain en vitesse. Nous rendons disponibles toutes sortes de ‘réponses’, donc les decks d’attaque peuvent raisonnablement interagir avec le deck tentant d’assembler sa combinaison de cartes. Cependant ce n’est pas juste un deck combo qui devient plus fort, mais tout un tas. Lorsqu’un format devient trop gros, un trop grand pourcentage de decks victorieux est composé soit des decks combos, soit des decks avec une abondance de sorts de permission pour briser ces combos. </td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

**3) La nouvelle politique de rotation de l’Étendu est plus facile à retenir.**

![Ancestral_Memories](https://i.ormos.uk/58/a7/58a73a844dc881a057f0edfad0f4571c760c4f4716c4eff6fd475e2132aeb495.jpg)Vous l’avez probablement déjà mémorisée : 

*‘L’Étendu est composé des sept dernières années d’extensions **Magic** et d’éditions de base.’*

Plus de questions comme… 

*‘Quand y aura-t-il une rotation de l’Étendu ?’*

ou...

*‘Qu’est-ce qui sort de l’Étendu cette fois ?’*

ou...

*‘Hé, qu’est-ce qui est légal en Étendu en ce moment ?’* 

Parce que maintenant les réponses seront toujours constantes et prédictibles. Selon moi, le résultat obtenu est un format Étendu qui est fondamentalement le même que celui qu’il a toujours été, simplement plus stable et plus équitable envers chaque bloc.

### Pas de bannissements pour le moment

Nous avons récemment gardé un œil attentif sur l’Étendu, observant ses meilleurs decks, leur rapidité, et l’efficacité des outils pouvant les perturber. Globalement, les joueurs d’Étendu ont été contents, et nous avons été contents également. Le format continue d’évoluer semaine après semaine, avec de nouveaux ‘meilleurs decks’ naissant chaque semaine, puis retombant au sein de la masse lorsque d’autres joueurs trouvent un moyen de les contourner. Cela a toujours été un bon signe de format sain. Il n’y a pas de bannissements en Étendu cette fois ci.

Le 31 octobre aura lieu le Pro Tour – Berlin, en format Étendu post-rotation due à ‘Rock’. Je suis impatient de voir le visage du nouveau format. 

### Un regard vers l’avenir

Les détails de la rotation de l’Étendu à la sortie du prochain bloc seront toujours disponibles et à jour sur la [page des formats](https://web.archive.org/web/20080518030627/http://www.wizards.com/default.asp?x=judge/resources/banned) et dans les [règles de **Magic**](https://web.archive.org/web/20080513034122/http://www.wizards.com/default.asp?x=dci/doccenter/home). 

Nous n’avions pas modifié la politique de rotation de l’Étendu depuis mai 2002. Je ne dirais pas que nous ne la changerons plus jamais, mais je soupçonne que cette politique de rotation durera au moins aussi longtemps, ce qui nous amène en 2014 et au delà. Si quelqu’un a des prédictions précoces sur les decks Étendus qui seront bons en 2014, envoyez-les-moi ! 

En ce qui me concerne, j’ai une prédiction précoce sur une carte qui, j’en suis presque sûr, sera très jouable dans l’Étendu de 2014. Cliquez ici pour la voir et approuver ou non : 

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Forest" src="https://i.ormos.uk/3c/82/3c82f99c3217e4f6a818b4dc7cbf0a6cda64c8b88f2aead0f64131fe3ac8142a.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

*Traduction Émilien Wild*
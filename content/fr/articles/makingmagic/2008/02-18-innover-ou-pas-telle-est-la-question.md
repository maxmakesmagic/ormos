---
id: daqvvj14
kind: article
lang: fr
path: /fr/articles/makingmagic/2008/02-18-innover-ou-pas-telle-est-la-question
title: Innover ou pas, telle est la question
published: '2008-02-18'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr319
    lang_detected: fr
    capture_id: 1976755
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr319
    captured_at: '2008-05-14 05:51:22+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr319
    lang_detected: fr
    capture_id: 1976755
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr319
    captured_at: '2008-05-14 05:51:22+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr319
    lang_detected: fr
    capture_id: 1976755
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr319
    captured_at: '2008-05-14 05:51:22+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr319
    lang_detected: fr
    capture_id: 1976755
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr319
    captured_at: '2008-05-14 05:51:22+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: daqvvj14
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr319
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr319
  lang: fr
  template: classic_asp
  captured_at: '2008-05-14 05:51:22+00'
  capture_id: 1976755
  wayback_url: https://web.archive.org/web/20080514055122id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr319
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: daqvvj14
  capture_id: 1976755
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr319
  wayback_url: https://web.archive.org/web/20080514055122id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr319
  captured_at: '2008-05-14 05:51:22+00'
  template: classic_asp
  sha256: 10a36a898089b98a216751a83dba96667e5d506c648c2215c8dbc5d062e61621
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Slobad,_Goblin_Tinkerer')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Demonic_Collusion')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Giant_Growth')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Giant Growth
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Gaea[s_Skyfolk')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Reminisce')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Twinning_Glass')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  occurrences: 1
---
* * *

La chronique d'aujourd'hui est bourrée de bonnes choses. Tout d'abord, un problème survenu suite à ma chronique d'il y a deux semaines ([L'espace entre les notes](/en/articles/makingmagic/2008/02-04-the-space-between-the-notes)) m’a fortement inspiré cette semaine. Ensuite, nous parlerons du bloc *Sombrelande* et je vous offrirai en pâture quelques idées de ce à quoi vous pouvez vous attendre dans les deux extensions à venir. Et si cela ne vous suffit pas, je pose aussi une question à mes lecteurs, et j’ai hâte de connaître vos réponses. Il y en a qui penseront sûrement que c'est un peu maigre, mais faites-moi confiance, c'est plusieurs milliers de mots qui vont remplir votre écran.

### Je n'arrive pas à croire que j'innove

Il y a deux semaines, donc, j'ai consacré une chronique au courrier que je recevais. J'ai imprimé la lettre suivante comme exemple des problèmes soulevés dans vos emails :

> Cher Mark,
> 
> Je lis ta chronique toutes les semaines et je voulais te dire que je pense qu’en règle générale, tu as un impact positif sur le jeu. Maintenant que je t’ai passé la pommade, vas-tu arrêter de vanter les mérites de 'l'étonnante latitude de conception' du système race/classe. Changer 'Tous les gobelins gagnent +1/+1' en 'Tous les soldats gagnent +1/+1' n'a rien de bien novateur ! L'innovation est définie par 'l'introduction de quelque chose de nouveau'. Alors explique-moi comment ce mot peut s’appliquer au traitement des classes comme des races ! *Carnage* l'a déjà fait depuis longtemps. Je sais que c'est ton boulot de nous dire que tout ce qui est nouveau dans le jeu est génialement spectaculaire, mais tu commences à perdre ta crédibilité quand tu essaies de nous vendre des restes mi-cuits comme une nouvelle merveille gastronomique. Accepte une bonne fois pour toute que le système race/classe ne donne pas naissance à un espace de conception qui n'a pas déjà été exploré il y a cinq ans.
> 
> Sincères salutations,  
>  E.E. Wood

![Slobad_Goblin_Tinkerer](https://i.ormos.uk/50/82/508223e4a5f9dcc900c971d73a3e95ce88f698c0e76ced72df3cca884c4da136.jpg)

J'ai passé presque toute ma chronique à répondre à cette lettre. Et bien sûr, cela a déclenché d'autres courriers. Celui que j'imprime aujourd'hui est celui qui, à mon avis, résume le mieux leur contenu (mes lecteurs, semble-t-il, ne sont jamais timides quand ils m'écrivent et ils ne manquent pas d’honnêteté) :

> Cher Mark Rosewater,  
>  À propos de ton article 'L'espace entre les notes' :
> 
> Mark — Rassure-moi, tu plaisantais dans ta chronique ? L'article était intéressant, avec une bonne approche permettant de comprendre ta philosophie de la conception des cartes. Cependant, tu as imprimé une critique valide d'un lecteur, et non seulement tu n'y as pas répondu — tu l'as fortement confirmée !
> 
> Tout ce que tu as expliqué sur les Bonhommes 1-4 et les cartes de sorts d'augmentation ? Oui, on A COMPRIS. Le type qui t'a écrit, il AVAIT COMPRIS aussi. Tu n'as rien dit de particulier (du moins rien de non-philosophique) qui nous ait éclairés un peu plus sur le sujet — tout simplement parce que tu n'avais RIEN à ajouter.
> 
> Les gens ne trouvent pas le système race/classe excitant parce que ce n'est pas le cas ; ils ne pensent pas qu'il ouvre un nouvel espace de conception parce que ce n'est pas le cas. Qu'est-ce qu'un ondin et sorcier a de spécial comparé à un ondin et elfe ou un zombie et assassin ou un guerrier et clerc ? Plusieurs types sur la ligne de type — WOW ! C'est ÉNORME, et c'est un IMPORTANT développement dans l'histoire de **Magic**. En appeler un une race et l'autre une classe ? C'est très limitatif (et très ennuyeux), c'est réduire la fantasy à ce qu'elle a de plus générique, et comme il n'existe aucune différence fonctionnelle entre les races et les classes... Qu'est-ce que ça peut nous faire ?
> 
> Est-ce que j'aime les cartes qui ont plusieurs types de créature ? Oui ! Est-ce que ça m'interpelle qu'un de ces types soit une race et l'autre, une classe, quand ces désignations n'ont aucun effet sur le jeu ? Non !
> 
> Je te respecte parce que tu n'ignores pas les critiques les plus dures et que tu essaies d'y répondre. Mais je t'en prie, retourne lire cet email. Ce n'est pas que tu n'as pas réussi à nous expliquer les choses convenablement. C'est qu'il a raison ; tu prétends que quelque chose est nouveau quand ça ne l'est pas.  
>  --Aaron

J'ai fait exactement ce qu'Aaron a suggéré et j'ai relu ma chronique. Puis j'ai relu la lettre. J'ai ensuite passé plusieurs jours à réfléchir à ce qui avait été dit. Puis j'ai relu les deux une dernière fois. Après y avoir mûrement réfléchi, j'ai quelques petites choses à dire.

D'abord, je crois que E.E. et Aaron ne parlent pas de la même chose que moi quand ils parlent du système race/classe. Cette confusion est en partie due au fait que je n'ai pas corrigé une erreur de E.E. dans sa lettre. Il parle de l'espace de conception et de l'innovation comme de termes qui seraient synonymes. Mais ce n'est pas le cas. Ils sont certes liés, mais ils sont loin d'être la même chose.

laissez-moi m'expliquer. L'espace (ou la latitude, les deux sont bons) de conception concerne la capacité de créer de nouvelles cartes. Quand je parle de créer un nouvel espace de conception, je ne fais qu'exprimer la capacité de générer de nouvelles cartes. Et quand je dis 'nouvelles cartes', je veux vraiment parler de NOUVELLES cartes, avec des nouvelles mécaniques de jeu, des nouveaux thèmes, de nouvelles conceptions de bloc et inter-bloc, de nouveaux outils, de nouvelles ambiances, des tons nouveaux, des humeurs nouvelles, etc... Je veux parler bien sûr de faire évoluer **Magic**. En tant que directeur de la conception, c'est un combat permanent et, à mon humble avis (à long terme du moins), l’aspect le plus important de mon travail.

L'innovation concerne la capacité de faire des choses qui n'ont jamais été faites auparavant. Notez qu'elle existe sous deux formes : le contenu et l'exécution. Je peux créer des choses qui n'ont jamais été créées auparavant et je peux créer des choses d'une manière qui n'a jamais été utilisée auparavant. Dans ces deux cas, on parle d’innovation. L'une est pleinement visible et l'autre se cache dans les coulisses. En supposant de connaître les quelques neuf mille cartes **Magic** existant à l'heure actuelle, vous êtes capable de déterminer si une carte (une mécanique, un thème, etc...) fait quelque chose de nouveau. Mais si c'est dans les coulisses qu'il y a quelque chose de nouveau, ce ne sera pas aussi évident à discerner.

Maintenant que nous avons défini ces termes, je peux passer au point suivant : l'espace de conception et l'innovation sont deux choses différentes. Laissez-moi vous donner quelques exemples.

Les mots-clés des mécaniques permanentes (les dernières en date étant le contact mortel, le lien de vie, la portée et le linceul) ouvrent l'espace de conception. De nombreuses cartes sont restées à l'état embryonnaire pendant des années parce que leur texte de règle était trop long. Raccourcir une ou deux lignes de texte à un ou deux mots auraient dans la plupart des cas suffi à rendre la carte imprimable. De plus, les mots-clés rendent la création de cartes plus facile. ([Ma chronique sur les mots-clés](/en/articles/makingmagic/2003/05-19-keyword-to-the-wise), par exemple, utilise des cartes du bloc *Carnage* qui n'auraient jamais vu le jour sans mots-clés — n'hésitez pas à aller la consulter si vous voulez en savoir plus sur ce problème.) Je le redis, les mots-clés ouvrent l'espace de conception. Mais d'un autre côté, attribuer des mots-clés à des capacités existantes n'a rien d’innovateur. Les cartes font toujours la même chose. Rien de nouveau n'a été créé.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Demonic Collusion" src="https://i.ormos.uk/72/72/7272c1d7efff02f4c255ebbec74fa9fc8eb4e0d3a973d00a6eb78af8ad20c36f.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Dans *Spirale temporelle*, nous avons ravivé une kyrielle d'anciens mots-clés. Pour garder intacte l'ambiance du passé, nous avons institué une règle de conception spécifique interdisant toute innovation dans les mécaniques de jeu. Nous nous sommes contentés de donner des effets de base aux cartes qui n'avaient jamais été utilisées avec cette mécanique : un effet de précepteur sur une carte avec le rappel, des effets 'inflige 1 blessures à une cible, créature ou joueur' sur une carte avec le déluge, etc. Cela nous a permis d'étendre l'espace de conception de *Spirale temporelle* sans rien innover. (Je ferai cependant remarquer que l'idée de faire revenir toutes les anciennes mécaniques de jeu en même temps était novatrice, mais une fois de plus, je parle d'exécution, et pas de contenu.)

Lors de la conception de *Tempête*, nous avions créé une série de cartes que vous pouviez choisir, si elles étaient dans votre bibliothèque, pour piocher une carte de moins et les mettre en suite dans votre main de départ (ne me demandez pas comment on aurait pu intégrer ça dans les règles, nous n'en sommes jamais arrivés à ce niveau de la conception). Nous avions même un cycle de cinq terrains générateurs de couleur avec cette capacité, qui arrivaient en jeu engagés. Il nous a suffi d’un test pour réaliser que la mécanique affecterait **Magic** de manière trop importante. Elle limiterait grandement ce qui serait jouable parce que dans ce style de jeu, l'aspect aléatoire serait grandement sacrifié et la mécanique contraindrait chaque deck à suivre une quantité limitée de stratégies. Cette idée était très novatrice, mais nous l'avons abandonnée en partie parce que nous savions qu'elle limiterait l'espace de conception (et bien sûr, qu'elle rendrait aussi le jeu moins amusant).

### Nuits folles d'innovation

Maintenant que j'ai expliqué ce en quoi l'espace de conception et l'innovation diffèrent, laissez-moi vous dire pourquoi l'espace (ou la latitude) de conception est plus importante dans mon rôle de directeur de la conception. Mon travail, une fois qu'on enlève toutes les couches, c'est de vendre des boosters de **Magic**. Et la méthode que j'ai choisie pour ce faire (et c'est une philosophie partagée par tout le service R&D), est de rendre le jeu le plus distrayant possible. Notre théorie veut que si **Magic** est suffisamment amusant, le jeu encouragera plus de joueurs à l'acheter.

En aparté, je tiens à faire remarquer que **Magic** est très important pour moi à un niveau personnel. Le jeu m'a tant donné à différents niveaux que je me sens personnellement investi dans son évolution. Mon désir de maintenir la qualité de **Magic** va bien plus loin que toucher mon chèque de salaire.

Donc, mon travail est de rendre **Magic** le plus attrayant possible. Comment est-ce que j'y parviens ? Qu'est ce que je dois faire en priorité pour accomplir ma mission ? Surprendre le public ? C'est en effet une priorité, mais ce n'est pas la plus importante. Exciter le public ? Vous chauffez toujours, mais ce n'est pas le principal. Avant tout, ma mission est de plaire au public. Je dois faire le jeu qu'il veut jouer.

Comme je le dis souvent, **Magic** est avant tout un jeu de découverte. Alors oui, je dois constamment tenter de réinventer l'environnement. Mais, plus important, il faut que je fasse attention à ce que **Magic** reste le jeu dont les joueurs sont tombés amoureux. Il serait très novateur de créer une extension sans blessures directes rouges, sans défausse noire et sans effet vert du style Giant Growth (Croissance gigantesque). Il serait très novateur de faire une extension contenant uniquement des rituels. Il serait très novateur de publier des boosters qui ne contiendraient pas de cartes rares. 

L'innovation par elle-même n'est pas ce qui plaît au public.

C'est un outil qui peut être utilisé méticuleusement par la conception pour satisfaire les joueurs. Mais ce n'est pas le seul. C'est un outil parmi tant d'autres. Et oui, l'innovation n'est pas l'outil-clé qui permet de créer une extension qui ravive un ancien thème. Bien sûr, nous pouvons compliquer les choses. Nous pouvons innover dans la manière de concevoir l'extension. Et oui, nous pouvons toujours ajouter un élément (comme les arpenteurs) pour satisfaire les junkies de l'innovation. Mais la clé du système race/classe, ce n'est pas son innovation. Si vous relisez tout ce que j'ai dit, je n'ai jamais prétendu que le système race/classe était innovateur (même si je crois que nous l'avons été dans son utilisation — une fois de plus, exécution et pas contenu). J'ai dit qu'il avait créé un espace, ou une latitude, de conception. Et c'est le cas.

<table>&#10;<tbody><tr>&#10;<td><img alt="" src="https://i.ormos.uk/65/b4/65b44cec90bda938bbb278a79acba1f455a38a19b714807bea68c253b77de30d.jpg"></td>&#10;<td></td>&#10;<td><img alt="" src="https://i.ormos.uk/dd/0a/dd0a617788694ee0e82eed58b0746ab9dbdbdb6e709ee5390dcfb32556a6990e.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/96/f5/96f5d53e3ef958055c4fdf5bf835be99797bd18449a68a882c96ab3801bae612.jpg"></td>&#10;<td><a><img alt="Gaea's Skyfolk" src="https://i.ormos.uk/52/af/52afb4fd72c9122796e808dee9c2bd1251faa0c8a67eefba458092eff8d93b8f.jpg"></a></td>&#10;<td></td>&#10;</tr>&#10;<tr>&#10;<td><img alt="" src="https://i.ormos.uk/a0/a9/a0a91e69ef087e17e689f758224146196f0a29fad934eb2639d2fb73d4cf3c75.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/c0/e2/c0e24bff2fa206011911cb4b5cb20b4559cb82301a77e757b6e86de3c1ae659a.jpg"></td>&#10;<td><img alt="" src="https://i.ormos.uk/fa/ab/faab219b94a5d6a8405ff77aefe6f815ba2bba52fc447652a633eec85e227836.jpg"></td>&#10;</tr>&#10;</tbody></table>

Il ne me reste plus qu'à vous expliquer comment. Il existe une quantité limitée de cartes tribales qui peuvent être conçues. On ne peut améliorer une créature que d'un certain nombre de manières. Pour accéder à l'étape suivante de l'environnement tribal, il fallait trouver des manières de créer des interactions intéressantes entre les différentes cartes tribales. La plupart des premières cartes à types de créature multiples que j'ai créées (voir ma chronique [L'épique mise en place de l'efficace système race/classe](/en/articles/makingmagic/2008/01-21-the-amazing-race-class) pour plus de détails) pour *Odyssée* et *Carnage* exploraient cet espace. Le problème était le suivant : pour que le système fonctionne vraiment, la majorité des créatures avaient besoin de types multiples, mais mes premières tentatives dépendaient de ruses comme l'utilisation de races (avemain et nantuko) qui avaient naturellement deux types ou de types comme zombie qui pouvaient être rattachés à n’importe quel autre type. Dépendre de ce genre de truc limitait grandement les possibilités. (Je dois aussi faire remarquer que ma toute première expérience dans *Invasion*, la juxtaposition simple de deux types de créature — bonjour aux Aériens de Gaia — fait grimacer l'équipe créative actuelle tant elle se fiche complètement de l'ambiance du jeu.)

Alors que j'essayais de solutionner ce puzzle, j'ai soudain reçu une information qui allait avoir son influence. Connaissez-vous la petite extension qui se soit le mieux vendue de toute l'histoire du jeu ? *Légions*. Vous êtes probablement choqués parce que cette extension est aussi célèbre pour contenir peu de cartes utilisables en tournoi Construit, mais les joueurs l'ont littéralement dévorée. Le service R&D a de nombreuses théories expliquant pourquoi cette extension s'est si bien vendue, mais ce qu'on ne peut pas ignorer, c'est que beaucoup de joueurs aiment le tribal (et les créatures, bien sûr). Remarquez aussi que nos études de marché semblent confirmer cette théorie. En attendant, cela voulait dire que mon puzzle devenait obligatoire à résoudre. Nous allions devoir rendre à nouveau visite au thème tribal (et plus d'une fois) parce que les joueurs l'aimaient vraiment.

Et sur ces entrefaites, l'équipe créative a débarqué avec une proposition qui, à son avis, apportait plus d'ambiance au jeu — et par coïncidence, elle parvenait exactement ce que j'essayais désespérément de résoudre. Et elle n’aidait pas la conception, mais la création. C'est pour ça j'ai tant combattu pour faire adopter le système race/classe, pas parce que c’était mon idée, mais parce que la solution (très organique en fait) à mon problème m’avait été livrée sur un plateau d'argent.

Quand je vante les mérites du système race/classe, ce n'est pas parce que je crois que nous innovons. C'est parce qu'il nous permet de construire une fondation qui à son tour crée un jeu fantastique. *Lorwyn* et *Lèveciel* n'ont pas réinventé la roue, ils ont simplement amélioré les conditions de jeu. *Carnage* était l'extension tribale innovatrice. C'est elle qui a prouvé qu'un bloc entier pouvait être construit autour d'un thème qui était à l'époque une chose que seul Timmy (et quelques Johnny) s'amusait à faire. Le bloc *Lorwyn* représentait pour la conception une chance de prouver qu'il était possible de transformer ce thème en quelque chose de plus profond et de plus significatif.

Le système race/classe n'est pas la conception tribale sexy qui vous en met plein les yeux, c'est la structure nécessaire à la conception pour faire son travail. Le bloc *Lorwyn*, même s'il emprunte beaucoup d'éléments au bloc *Carnage*, a sa propre identité. Il a sa propre ambiance et son propre jeu. Comme cette chronique est consacrée à la conception, j'ai fait remarquer que nous pouvions utiliser les outils que le système race/classe nous donne. Une grande partie de cette rubrique consiste à expliquer les coulisses de la conception. Pour le tribal, c'est le système race/classe.

### Innovation pas pour tous

Ces journées de réflexion m'ont fait réaliser autre chose avec ces deux lettres : E.E. et Aaron n'aiment pas le thème tribal. Ce n'est pas la raison pour laquelle ils aiment **Magic**. Et ils ne sont pas les seuls. Je lis mes emails et je consulte internet. Je sais qu'il existe une minorité de joueurs qui n'aiment pas le tribal. En fait, pour chaque thème, il y a toujours une minorité réfractaire. Chaque fois que je passe du temps et de l'énergie à expliquer pourquoi ce thème est génial et tout le travail de conception qu'il a représenté, ce groupe pense que je lui fais perdre son temps. Mais voilà le problème : il existe aussi une majorité de joueurs qui aiment ce thème (et sachez que tribal est en deuxième position dans les thèmes les plus populaires de tous les temps, après le multicolore, d'après nos ventes et nos études de marché). Pour eux, tous les petits détails de la conception de ce thème sont intéressants.

![Reminisce](https://i.ormos.uk/2a/2f/2a2fda36c4457b01594e44e3b5907f6f74ccbd038366ae55a001f4d2395405cd.jpg)

Mais il y a aussi un autre problème qui vient s'ajouter à tout cela. Certains ne supportent pas l'idée de revenir sur d'anciens thèmes. Ils veulent qu'on s'aventure toujours plus loin dans des territoires de conception vierges. Mais comme je l'ai dit plus tôt, mon travail, c'est de plaire aux joueurs. Et la majorité d'entre eux (je dirais même, la majorité des gens) aiment revenir faire un tour dans le passé. Nous ne revenons pas sur d'anciens thèmes par fainéantise. Nous le faisons parce que les joueurs le veulent. Cela ne veut pas dire non plus que nous n'allons pas exploiter de nouvelles mines de conception (une histoire à suivre très rapidement d'ailleurs) ; nous ne sommes simplement pas obligés de le faire pour chaque thème de chaque bloc.

Je pense que les auteurs de ces lettres ont eu l'impression que j'essayais de leur vendre quelque chose dont ils n'avaient pas envie. Très honnêtement, ce n'est pas mon objectif. Si nous décidons de nous impliquer dans un thème, le directeur de la conception et le chroniqueur que je suis doivent s'y impliquer aussi. Je vais déterminer comment tirer le meilleur parti de ce thème et je vais ensuite l'expliquer à mes lecteurs. Je me sens très investi dans le tribal. J'ai passé une année de ma vie à plancher sur le sujet. J'y ai investi plus de temps que vous ne pourriez seulement l'imaginer. Alors, quand je suis tout émoustillé sur le sujet, c'est vraiment parce qu'il me passionne. (Et pour être juste, je suis d'un naturel très excité — vraiment, ce n'est pas un genre que j'essaie de me donner. Ce que vous lisez, c'est vraiment moi.) Faites-moi confiance, je suis peut-être bon à certaines choses, mais ne pas dire ce que je pense n'en fait pas partie.

Ceci dit, pour chaque bloc, nous essayons de créer des cartes hors thème (les arpenteurs, l'évocation et la confrontation n'ont rien à voir avec le thème tribal) et chaque extension contient un soupçon d'innovation (le bloc *Lorwyn* a deux nouveaux types de carte). Pour ma chronique, je fais souvent exprès de choisir des sujets qui n'ont rien à faire avec les thèmes du bloc en cours. Je fais ce que je peux pour plaire au plus de gens possible. Mais je ne peux pas satisfaire tout le monde tout le temps (Lincoln avait raison), alors la plupart du temps, je me contente de plaire aux gens qui sont plus enclins à aimer ce que nous faisons sur le moment. Satisfaire ceux qui ne le sont pas ne sert pas à grand-chose. (Pour plus de détails sur cette philosophie, consultez la Leçon de vie 1 [ici](/en/articles/makingmagic/2006/02-20-life-lessons-part-i).)

La bonne nouvelle, c'est que **Magic** change constamment. Ce qui signifie que le pendule des thèmes bascule toujours dans des directions différentes. Si vous n'aimez pas le contenu de ce bloc, le bloc suivant vous attendra au coin de la rue. Alors, E.E. et Aaron, rassurez-vous, j'ai bien compris que le tribal, ce n'est pas votre tasse de thé. Cependant, respectez les autres pour qui c'est le cas. Ils sont excités par le thème et ils sont contents de constater qu'ils ne sont pas les seuls. Ce qui ne paraît pas 'neuf' pour vous l'est pour eux (principalement parce qu'ils sont intéressés par tous les détails dont vous vous moquez éperdument). Mais j'ai de bonnes nouvelles pour vous. Le bloc tribal touche à sa fin et très vite (dans le prochain paragraphe, en fait) je vais m'intéresser à quelque chose qui vous passionnera peut-être un peu plus. E.E. et Aaron, *Sombrelande* arrive.

### Bienvenue à *Sombrelande*

Et pendant qu'on y est, pourquoi ne pas passer le restant de la chronique à discuter de ce que va nous offrir le prochain bloc ?

Pour commencer, voici les deux Magic Arcanas qui ont annoncé *Sombrelande* et *Coucheciel*, respectivement.

<table>&#10;<tbody><tr>&#10;<td>&#10;<table>&#10;<tbody><tr>&#10;<td>&#10;                 <b>Annonce Sombrelande</b></td>&#10;<td> </td>&#10;<td><img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td colspan="3">&#10;<table>&#10;<tbody><tr>&#10;<td>&#10;<p>La grosse extension de <b>Magic</b> de mai 2008, portant le nom de code 'Jelly' (Gelée), première extension du bloc 'Jelly / Doughnut' (Gelée/Beignet), est appelée <i>Sombrelande</i>.</p><br><p>&#10;</p><div><img alt="Shadowmoor Logo" src="https://i.ormos.uk/0c/9d/0c9d85635bc1e736d895f5fda2b83edd89993441a31ca1a302473dcf7aa17a4b.jpg" title="Shadowmoor Logo"></div>&#10;<p></p>&#10;<p>&#10;<table><tbody><tr><td><b>Nom de l'extension</b></td>&#10;<td><i>Sombrelande</i></td>&#10;</tr>&#10;<tr><td><b>Date de sortie</b></td>&#10;<td>2 mai 2008</td>&#10;</tr>&#10;<tr><td><b>Tournois Avant-premières</b></td>&#10;<td>19-20 avril 2008</td>&#10;</tr>&#10;<tr><td><b>Équipe de conception</b></td>&#10;<td>Mark Rosewater (direction)<br> Sean Fletcher<br> Mark Gottlieb<br> Devin Low<br> Ken Troop</td>&#10;</tr>&#10;<tr><td><b>Équipe de développement</b></td>&#10;<td>Aaron Forsythe (direction)<br> Devin Low<br> Alexis Janson<br> Matt Place<br> Jake Theis<br> Steve Warner<br> Doug Beyer</td>&#10;</tr>&#10;</tbody></table>&#10;</p>&#10;<div><img alt="Shadowmoor Expansion Symbol" src="https://i.ormos.uk/a3/5d/a35df6cf6b5787e8b984ab85fce5cb1539458510b9ab9e266d91688b99e924b6.jpg" title="Shadowmoor Expansion Symbol"></div>&#10;<p>Pour plus de détails sur les structures des blocs <i>Lorwyn</i> et <i>Sombrelande</i> 2007-2008, voir l'article de Mark Rosewater <a href="/en/articles/makingmagic/2007/07-16-two-plus-two">Deux plus deux</a>. Consultez <b>magicthegathering.com</b> régulièrement pour en savoir plus sur <i>Sombrelande</i>.</p>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

* * *

<table>&#10;<tbody><tr>&#10;<td>&#10;<table>&#10;<tbody><tr>&#10;<td>&#10;                 <b>Annonce Coucheciel</b></td>&#10;<td> </td>&#10;<td><img alt="" src="https://i.ormos.uk/7d/ea/7deab367d2187ba6dc0e8758afb21d975578affe86883947e65fa45de83cb2e0.jpg"></td>&#10;</tr>&#10;<tr>&#10;<td colspan="3">&#10;<table>&#10;<tbody><tr>&#10;<td>&#10;<p>La petite extension de <b>Magic</b> de juillet 2008, portant le nombre de code 'Doughnut' (Beignet), deuxième extension du bloc 'Jelly / Doughnut' (Gelée/Beignet), est appelée <i>Coucheciel</i>. </p>&#10;<div><img alt="Eventide" src="https://i.ormos.uk/69/8e/698ef7d290b98a88c7595571732ce8c0f97b9e5eab276d66f415392b7df1bbd2.jpg" title="Eventide"></div>&#10;<table><tbody><tr><td><b>Nom de l'extension</b></td>&#10;<td><i>Coucheciel</i></td>&#10;</tr>&#10;<tr><td><b>Bloc</b></td>&#10;<td>Deuxième des deux extensions du bloc <i>Sombrelande</i></td>&#10;</tr>&#10;<tr><td><b>Nombre de cartes</b></td>&#10;<td>180</td>&#10;</tr>&#10;<tr><td><b>Date de sortie</b></td>&#10;<td>25 juillet 2008</td>&#10;</tr>&#10;<tr><td><b>Tournois Avant-premières</b></td>&#10;<td>12-13 juillet 2008</td>&#10;</tr>&#10;<tr><td><b>Début des avant-premières <br>sur magicthegathering.com</b></td>&#10;<td>1er juillet 2008</td>&#10;</tr>&#10;<tr><td><b>Équipe de conception</b></td>&#10;<td>Mark Rosewater (direction)<br> Alexis Janson<br> Ken Nagle<br> Jake Theis<br>Brian Tinsman</td>&#10;</tr>&#10;<tr><td><b>Équipe de développement</b></td>&#10;<td>Matt Place (direction)<br> Nate Heiss<br> Erik Lauer<br> Ken Nagle<br> Mike Turian</td>&#10;</tr>&#10;</tbody></table>&#10;<div><img alt="Eventide" src="https://i.ormos.uk/69/88/6988ca0fa00e652d335aac1b9fef1cfac0d18b7b447844204a85801fcc0abab1.jpg" title="Eventide"></div>&#10;<p>Pour plus de détails sur les structures des blocs <i>Lorwyn</i> et <i>Sombrelande</i> 2007-2008, voir l'article de Mark Rosewater <a href="/en/articles/makingmagic/2007/07-16-two-plus-two">Deux plus deux</a>. Consultez <b>magicthegathering.com</b> régulièrement pour en savoir plus sur <i>Coucheciel</i>.</p>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>&#10;</td>&#10;</tr>&#10;</tbody></table>

Autant commencer par vous dire que je suis hyper-excité par le bloc *Sombrelande*. Mon avis est bien sûr un peu biaisé parce que je suis le directeur de la conception des deux extensions (peu de designers de **Magic** peuvent prétendre avoir dirigé la conception d'un bloc entier), mais je suis très fier de mes deux bébés. *Sombrelande* est la première grosse extension dont j'ai dirigé la conception depuis *Ravnica*, et j'ai bien l'impression d'avoir maintenu un niveau très élevé pour cette extension.

Alors, à quoi devez-vous vous attendre dans ce nouveau bloc ? Je ne peux pas dire grand-chose parce que nous sommes encore à plusieurs mois de la sortie, mais je vais quand même vous donner quelques petites infos. Pour commencer, voyons ce qu'on peut déterminer des annonces listées ci-dessus. Premièrement : les noms *Sombrelande* et *Coucheciel*. 'Sombrelande' impliquent clairement une certaine obscurité et 'Coucheciel' semble vouloir s'opposer à Lèveciel. Ensuite, comparons les symboles d'extension de *Lèveciel* et de *Coucheciel*.

![](https://i.ormos.uk/46/2e/462e864f92e34ddad97c2752465edb71b59eb1722e2a9091ee3cddf91e746a0c.jpg)

  

![](https://i.ormos.uk/69/88/6988ca0fa00e652d335aac1b9fef1cfac0d18b7b447844204a85801fcc0abab1.jpg)

Hmm, Lorwyn ensoleillé est suivi par un monde obscur avec des noms et des symboles d'extension qui impliquent que le monde est un opposé et/ou un reflet dans un miroir. Eh bien, c'est le cas. Sombrelande, c'est Lorwyn, mais le plan a subi des transformations plutôt radicales. Ce phénomène qu'on appelle l'Aurore a transformé Lorwyn en son opposé. Ses habitants sont toujours là, mais tous sont déformés et corrompus. Alors qu'est-ce que ça veut dire mécaniquement ? Les types de créature que vous avez vu se développer dans le bloc *Lorwyn* sont toujours là. Ils seront différents par bien des manières, mais ils ne s'en vont pas. Par contre, le thème tribal aura disparu. Les transformations du monde de Lorwyn ont des conséquences sur tout, même sur les mécaniques de jeu. **Sombrelande** développe de nouveaux thèmes, mais comme je l'ai expliqué précédemment, ces thèmes auront une synergie avec le bloc *Lorwyn*.

De *nouveaux* thèmes ? Quels nouveaux thèmes ? Quel est le thème du bloc *Sombrelande* ? Si vous avez lu les rumeurs sur internet, il y a quelques théories populaires. La plus répandue est que *Sombrelande* est une extension basée sur le cimetière. Après tout, *Vision de l'avenir* envoyait des signaux assez clairs que nous reviendrions un jour sur les mécaniques de cimetière. Et nous le ferons, seulement, pas tout de suite. Une autre théorie populaire est que *Sombrelande* est un bloc à thème artefacts. Une fois de plus, *Vision de l'avenir* semble soutenir cette idée. C'est en effet un thème que nous explorerons dans les années à venir, mais pas celle-ci. Alors quel thème de bloc allons-nous reprendre pour l’améliorer ? Aucun. Le thème de bloc de *Sombrelande* n'a jamais été abordé auparavant. (Au fait, l'extension contiendra DEUX cartes décalées dans le temps de *Vision de l'avenir*.)

Mais attendez une seconde, allez-vous me dire. Vous avez vu le matériel de promotion publié pour encourager les magasins à acheter *Sombrelande*. Vous y avez lu : 'une mécanique de jeu populaire est de retour'. Et c'est vrai. Mais je vous ferais remarquer qu'une mécanique n'est pas obligatoirement synonyme de mécanique mot-clé. Il n'est écrit nulle part qu'une mécanique mot-clé revient. Bien sûr, il n'est pas non plus écrit quelque part que la mécanique qui revient n'est pas une mécanique mot-clé (j'adore lancer des pistes contradictoires pour alimenter les spéculations sur les forums de rumeurs). De plus, que veut-on dire par 'populaire' ? Nous faisons beaucoup d'études de marché. Cette mécanique arrive en peloton de tête dans nos études. (Au fait, voilà une bonne raison de répondre aux enquêtes qui apparaissent sur **magicthegathering.com** — nous tenons vraiment compte de vos réponses.)

Mais assez dit sur ce que je ne peux pas dire. Que puis-je vraiment vous dire ? La mécanique de retour est au cœur de *Sombrelande*, mais elle est utilisée d'une façon toute nouvelle. Je vous garantie que quand vous vous installerez à une table de tournoi Avant-première de *Sombrelande*, vous serez forcé de prendre des décisions que vous n'aurez jamais prises auparavant. Aussi, l'extension joue sur le thème de dualité entre les blocs *Lorwyn* et *Sombrelande*, à la fois dans les illustrations et les mécaniques. (Oui, ils sont à la fois opposés et synergétiques.) Enfin, je vais faire une déclaration audacieuse : à mon humble avis, l'environnement de draft *Sombrelande* / *Sombrelande* / *Coucheciel* va être le plus dynamique de l'histoire du jeu.

![Twinning_Glass](https://i.ormos.uk/81/cc/81cc279f401195be813f78c68b6ec04346b3d8a9c41ea4225c42be400a519d11.jpg)

Je voudrais vous en dire plus parce que je suis vraiment excité par ce nouveau bloc, mais cela devra attendre encore un peu. Il suffit de dire qu'en mai, vous allez être ensorcelés (et en tant qu'ancien habitant de Boston, je le dis dans les deux sens du terme). *Sombrelande* est son propre bloc stand-alone, mais c'est aussi une pièce importante d'un puzzle plus grand, le méga-bloc *Lorwyn* / *Sombrelande*. Cette extension fait ma grande fierté (dans une liste qui comprend *Tempête*, *La Destinée d'Urza*, *Odyssée*, *Mirrodin*, *La cinquième aube*, *Ravnica*, *Vision de l'avenir* et les deux extensions *Un-*). J'ai hâte que vous puissiez découvrir ces cartes. Et ne vous inquiétez pas, il y aura d'autres détails croustillants (dans cette chronique et sur le reste de **magicthegathering.com**) dans les mois à venir.

C'est tout pour aujourd'hui. J'espère vous avoir donné matière à réflexion et avoir éveillé un sentiment d'excitation chez vous.

retrouvez-moi la semaine prochaine avec une bande de gredins.

Jusque-là, puissiez-vous imaginer un monde qui existe à l'envers du miroir.

Mark Rosewater

### Question-réponse

Mais attendez, ce n'est pas fini. Oui, voici un nouvel épisode de Question-réponse où comme d'habitude, je vous pose une question et j'attends vos réponses, mes chers lecteurs. La question d'aujourd'hui provient d'une discussion que nous avions au service R&D. Nous nous sommes rendus compte qu'à une ou deux exceptions près (la plus importante étant le monologue récent de Seth Rogen dans Saturday Night Live où il disait avoir joué à **Magic**), nous ne savons pas quelles célébrités jouent avec nos cartes magiques.

Alors ma question est la suivante : connaissez-vous des célébrités qui jouent ou qui ont joué à **Magic** ? Savoir comment vous le savez m'intéresse aussi (si par exemple, l'information est directe ou indirecte). Remarquez bien que je n'ai pas l'intention de pointer le doigt sur qui que ce soit. Je ne publierai pas les réponses à cette question. C'est tout simplement de la curiosité.
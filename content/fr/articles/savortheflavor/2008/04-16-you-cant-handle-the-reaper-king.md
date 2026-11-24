---
id: w11rfpfn
kind: article
lang: fr
path: /fr/articles/savortheflavor/2008/04-16-you-cant-handle-the-reaper-king
title: Vous ne Pouvez Pas Appréhender le Roi Faucheur
published: '2008-04-16'
column_slug: savortheflavor
column: Savor the Flavor
authors:
- slug: dougbeyer
  name: Doug Beyer
translation_of: jnh42rzq
detected_lang: fr
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/db32
    lang_detected: fr
    capture_id: 1948616
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/db32,,fr
    captured_at: '2008-06-25 19:07:00+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/db32
    lang_detected: fr
    capture_id: 1948616
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/db32,,fr
    captured_at: '2008-06-25 19:07:00+00'
    rule: registry.known_article
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/db32
    lang_detected: fr
    capture_id: 1948616
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/db32,,fr
    captured_at: '2008-06-25 19:07:00+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/db32
    lang_detected: fr
    capture_id: 1948616
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/db32,,fr
    captured_at: '2008-06-25 19:07:00+00'
    rule: registry.known_article
    registry_match: registry.explicit
sources:
- document_id: w11rfpfn
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/db32,,fr
  page_key: wizards.com/default.asp?x=mtgcom/daily/db32
  lang: fr
  template: classic_asp
  captured_at: '2008-06-25 19:07:00+00'
  capture_id: 1948616
  wayback_url: https://web.archive.org/web/20080625190700id_/http://www.wizards.com/default.asp?x=mtgcom/daily/db32,,fr
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: w11rfpfn
  capture_id: 1948616
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/db32,,fr
  wayback_url: https://web.archive.org/web/20080625190700id_/http://www.wizards.com/default.asp?x=mtgcom/daily/db32,,fr
  captured_at: '2008-06-25 19:07:00+00'
  template: classic_asp
  sha256: f13a20179d9de639cf3d742b1c166627bbcddb320552c3304f164c57585d027f
render_recovery:
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Swamp')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Swamp
  occurrences: 3
- code: unsupported_link
  element: a
  target: javascript:void(0)
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - ici
  occurrences: 1
- code: legacy_card_link
  element: a
  target: javascript:autoCardWindow('Vindicate')
  reason: The archived link uses the old Wizards card popup. The preview kept the
    card text.
  labels:
  - Vindicate
  occurrences: 1
---
* * *

Le Roi faucheur n’est pas pour vous. Vous n’en êtes pas dignes. Il est hors de votre portée et au-delà de votre horizon. Vous ne pouvez pas exercer son pouvoir car vous ne *l’avez* pas. Vous ne pouvez même pas toucher son Épouvantaillité car vous n’avez pas les tripes nécessaires pour lui résister. Vous mériteriez plutôt d’être laissé seuls. Vous devriez cliquer ailleurs et espérer ouvrir quelque chose d’autre à [l’Avant-première](/en/articles/event-coverage/undated/magic-the-gathering-prereleases-3). Parce que vous *n’êtes tout simplement pas dignes*.

À moins que peut-être… vous ne le soyez ?

Aujourd’hui nous jetons un œil non seulement à une carte d’avant-première connue sous le nom de Roi faucheur, mais également aux interactions entre les équipes de conception et de développement de *Sombrelande* et l’équipe créatrice, durant le développement des épouvantails de *Sombrelande*.

### Les Épouvantails Selon leurs Concepteurs

Pour comprendre le Roi faucheur, vous devez d’abord comprendre ses favoris, les épouvantails. Les épouvantails de *Sombrelande* forment une race de créatures artefacts, dont certains, bien qu’eux-mêmes incolores, ont des capacités ‘où la couleur est importante’. Pour savoir pourquoi en premier lieu les épouvantails furent dans l’extension, nous devons remonter à la conception de l’extension. 

![](https://i.ormos.uk/ae/47/ae479e538fd09a4f3ffdb50aa6b8a8ba5edfd21b07c72604aa0c071b1bf44301.jpg) Il a toujours été question de mettre des créatures artefacts dans *Sombrelande*. L’une des particularités du jeu en limité de *Sombrelande* (jouer l’extension via un Paquet Scellé et un Draft, au lieu de construire des decks à partir de votre collection) est la possibilité de construire des decks monochromes, ou au moins des decks n’ayant qu’un seul *type de terrain de base*. Grâce à la puissance des hybrides de *Sombrelande*, votre deck alimenté uniquement grâce à des Swamps (Marais) peut être plein de créatures noires, noires et rouges, et noires et bleues. Votre deck ne contenant que des Swamps (Marais) peut facilement être de trois couleurs – mais même avec l’hybride vous donnant plus de choix de cartes pour votre deck, l’extension avait encore besoin de plus de créatures pouvant soutenir une stratégie monochrome. 

Maintenant, il peut sembler étrange que des créatures artefacts apparaissent dans une extension ‘où la couleur est importante’. Une carte telle que la Foule de scoriacés (issue des [Archives des Cartes d’Avant-première](https://web.archive.org/web/20080518030759/http://www.wizards.com/default.asp?x=magic/shadowmoor/spoiler)) ne devient pas plus grosse lorsque vous ajoutez à la table une créature artefact, et une créature incolore ne vous aide pas à conspirer pour laisser votre Trace de brûlure ([révélée par Steve Sadin](/en/articles/limitedinformation/2008/04-08-blazing-a-trail)) sur quelqu’un pour 6. Mais les créatures artefacts sont les créatures à l’ultime flexibilité en mana. Une créature hybride noire et bleue peut aller dans de nombreux decks, mais une créature artefact peut aller dans n’importe quel deck, quelque soit sa base de mana. Elles étaient dans l’extension depuis les premières idées jusqu’au développement en passant par la conception, pour permettre aux gens d’ouvrir assez de créatures pour leurs decks monochromes et exposer ainsi leur monochromie, et le développement (moi y compris, lors de mon passage) les y a laissées justement dans ce but. 

Il est intéressant de noter que de nombreux épouvantails ont fini avec des capacités ‘où la couleur est importante’, malgré leur absence de couleur. Il y a un cycle d’épouvantails courants dont les capacités ‘s’activent’ lorsque vous contrôlez une créature de la couleur appropriée. Et ces capacités sont là plus souvent que vous pourriez le penser, même dans des decks monochromes. Vous pourriez penser que votre deck ‘mono-Swamp (Marais)’ pourrait n’être capable que de donner la persistance à un Épouvantail à ailes cliquetantes (issu des [Archives des Cartes d’Avant-première](https://web.archive.org/web/20080518030759/http://www.wizards.com/default.asp?x=magic/shadowmoor/spoiler)), mais pas en plus le vol, et puis vous remarquez que vous avez inclus des créatures hybrides bleues et noires. Et voilà, un épouvantail persistant et *volant*.

### Les Épouvantails Prirent Forme

Revenons un peu en arrière. La conception et le développement avaient gardé dans l’extension un nombre plutôt élevé de créatures artefacts. Donc nous, dans l’équipe créative (moi y compris, en tant que travail principal) étions prêts à concevoir des êtres artificiels. C’était assez passionnant ; l’idée de combiner ‘un plan lugubre et effrayant de crépuscule éternel’ avec ‘des créatures artefacts’ m’aiguillonnait. L’idée d’utiliser le type de créatures épouvantail est arrivé sur la table assez tôt, une seconde jeunesse d’un vieux sous-type trouvé uniquement sur la carte Scarecrow (et récemment Oraclisé sur la carte Straw Soldiers de *Portal Three Kingdoms*). Mais nous pensions avoir quelques épouvantails, quelques golems, des constructions, et ainsi de suite, tous rendus lugubres. Ce fut le directeur artistique Jeremy Jarvis qui suggéra que toutes les créatures artefacts puissent être des épouvantails, avec une définition large d’’épouvantail’. Notre illustrateur conceptuel Richard Whitters fut enjoué, et conquis par l’idée, imagina quelques croquis. (Richard, d’ailleurs, aime beaucoup quand je regarde par-dessus son épaule et que je dis ‘Qu’est-ce tu fais ? Tu dessines ? Tu veux pas me dessiner ? Dessine-moi en tant que GÉANT ! Dessine-moi en tant que géant, mangeant un SANGAMI ! Vas-y ! Allez, Richard !’ Ouais, il adore ça. Tout particulièrement quand tu applaudis et lui fait porter un petit fez pour singe.) Voici certains des croquis de Richard, que vous pouvez avoir déjà vus dans l’[article de Jarvis](/en/articles/feature/2008/04-07-shadowmoor-pays-off) de la semaine dernière. 

![](https://i.ormos.uk/85/23/8523ad1729ea5d681a5b5521904ce9a2f20ecd0679c71966745da9f6704e47c0.jpg)

Nous avons adoré ces conceptions. Leur histoire vient ensuite rapidement. 

### La Nature des Épouvantails

![](https://i.ormos.uk/14/ff/14ff1bfb71bedb9ac019a076a64f5cd9cffc576c64c345fccdf0c44d003bb5ba.jpg) L’histoire entourant les épouvantails est déjà lugubre. Ils sont des hommes factices, construits à partir de calebasses, de bouts de paille et de vêtements rapiécés, empalés sur un poteau pour donner une vague impression de présence humanoïde dans le jardin de quelqu’un. Pour *Sombrelande*, cependant, la frayeur qu’ils suscitent devait monter d’encore un cran. La légende commence ainsi. 

La plupart des épouvantails de Sombrelande furent construits par les ravaudeurs sangamis pour effectuer des tâches agricoles basiques. Même sur ce plan sombre, les sangamis doivent élever des sautelièvres et prendre soin de leur récoltes maladives et infestées d’orties, donc d’entreprenants Mage des haies des *dounes* (le terme Sombrelande pour des villages sangamis) ont construit des créatures pour les aider dans leurs corvées. Les ravaudeurs ne peuvent utiliser que quelques outils, os ou bouts de bois pour créer ces trucs, ce qui fit se déplacer les épouvantails d’une façon troublante et saccadée. Certains disent que les premiers créateurs d’épouvantails utilisèrent le bois enchanté d’un sylvain mort, et que leurs mouvements sont indicatifs de la rage intrinsèque de ce bois. Quelque soit la cause de leurs étranges mouvements, ils ne firent pas correctement leur travail, mais au moins quand de sombres choses de la nuit les leur arrachèrent, les fermiers ne perdirent pas grand-chose.

Avec le temps, tandis que les fermiers déménageaient ou mourraient, certains des épouvantails restèrent. La plupart d’entre eux continuèrent d’essayer d’accomplir ce pour quoi ils étaient prévus, mais en dehors de leur contexte, leurs actions semblent bizarres et inappropriées. Un épouvantail conçu pour faucher le grain, par exemple, peut avoir l’air menaçant quand il vient sur vous dans la nuit, son bras-faux levé haut et ses yeux vides tentant de décider si vous êtes mûr pour la récolte. D’autres épouvantails sont d’un usage plus inoffensif, mais peuvent toujours être étranges et effrayants. 

<table><tbody><tr><td><img src="https://i.ormos.uk/ab/ee/abee1e32c45cd57ad97622093074fc41d32497a19dbbc16d90c9540aaa9046ff.jpg"><br><i>Illustration par Carl Critchlow</i></td></tr></tbody></table>

### D’étranges récoltes

Donc, lorsque la vision qu’avaient les créateurs des épouvantails se solidifiait et que les croquis des artistes commençaient à affluer, ils se sentirent immédiatement comme chez eux. Ils étaient devenus une sorte de tribu. Ils avaient leur propre identité, mais seulement dans la mesure où ils étaient tous des bidules issus d’esprits pas tout à fait sains. Le développement étendit le rôle des épouvantails, et entre la conception et le développement, certains d’entre eux inhabituels et mêmes rares furent créés. 

Pendant ce temps, le cycle des cartes hybrides monochromes (telles qu’Implorer la reine, qui coûte ![Two or Black Mana](http://www.wizards.com/images/Symbols/Symbol_2B_mana.gif)![Two or Black Mana](http://www.wizards.com/images/Symbols/Symbol_2B_mana.gif)![Two or Black Mana](http://www.wizards.com/images/Symbols/Symbol_2B_mana.gif)) a inspiré les concepteurs de *Sombrelande* dans leur exploration d’autres moyens d’utiliser l’hybride pour surprendre en mélangeant des coûts incolores et colorés. Mais ça n’a pas marché. Ces conceptions furent toutes rejetées car trop bizarres, trop ‘différentes juste pour faire différent’, ou trop difficiles à comprendre dans une extension déjà remplie de coûts en mana inhabituels. Oui, elles furent toutes rejetées, *sauf* la plus bizarre d’entre elles, qui se trouvait être une créature artefact. 

Cliquez ici pour la voir.

![Le Roi faucheur](https://i.ormos.uk/ec/42/ec4220e96b3262a1278bbcfdd694c40cb69dec709ae07e3ad014560df7bef5a2.jpg "Le Roi faucheur")

Voila quelque chose… de spécial.

Le Roi faucheur fut une carte controversée au sein de la R&D. Son coût en mana est bizarre, et il fonctionne mieux dans un deck de quatre ou cinq couleurs – dans une extension qui est presque entièrement consacrée aux decks monochromes ou de deux couleurs. Il est un ‘seigneur’ tribal, d’une tribu qui n’a presque aucun soutien. Il génère une récompense puissante – des Vindicates (Justification) répétées ! – si vous construisez à partir d’une tribu qui fut sensée servir à remplir les quotas de créatures en limité. Il est une enfreinte, vraiment, à tous les thèmes qu’est *censée* avoir cette extension.

Mais en quelque sorte, pour moi, il était au centre de l’histoire parfaite d’un succès – le Roi faucheur vint et resta grâce à l’*ambiance*. Les gens tombèrent amoureux des épouvantails et de leur lugubre maladresse, et décidèrent que cette nouvelle et adorable tribu avait besoin d’un Roi. Dès que le Roi fut créé on se moqua de lui, de l’étrange abomination ‘orbride’ qu’il était, mais il fit son chemin vers les autocollants et les tests de Scellé. Beaucoup l’adoraient, beaucoup le haïssaient, tous eurent une réaction immédiate en le voyant. Pour ses supporters, chaque accusation dirigée contre lui semblait simplement augmenter son aura. En quelque sorte sa présence même était une sorte d’autojustification irrationnelle. Son inadéquation totale était si adaptée à son ambiance et à sa personnalité, que contre toutes les chances, il survécu jusqu’à apparaître dans les pochettes de *Sombrelande*. Il est troublant, inapproprié, et tout simplement bizarre. Exactement ce que devrait être le Roi des épouvantails. 

Je n’ai pas pour habitude d’approuver l’argument ‘si tu ne l’aime pas, c’est que tu n’étais pas le public à qui c’était destiné’. Mais le Roi faucheur est venu à moi, et je me suis retrouvé à être étrangement protecteur à son sujet. Ne touchez pas à mon Roi faucheur. Si vous n’êtes pas un fan, c’est parce que vous ne pouvez pas l’*appréhender*. Si vous faites la fine bouche, c’est parce que vous d’êtes pas digne de Sa Pourrissante Calebasse. C’est comme si l’un de ces épouvantails grinçants, animé, d’os et de bois en avait eu marre des mauvais traitements infligés à sa race sous appréciée, avait gagné horriblement en stature et en masse, et pris le pouvoir sur ses gredins favoris, couvant ses enfants difformes sous ses bras filiformes en osier. Peut-être ai-je moi aussi un peu d’épouvantail en moi, parce que je me sens un peu plus fort, un peu plus vaillant, en sa présence. Et quand je passe à coté d’une partie **Magic** jouée par quelqu’un d’autre et que je vois la pulpe filandreuse de sa couronne putréfiée, je me sens justifié. 

<table><tbody><tr><td><img src="https://i.ormos.uk/73/84/7384780bb82d5f14845a1c15fb7c537ca29ca813a2f600b33029dd079f01ace8.jpg"><br><i>Illustration par Jeremy Jarvis</i></td></tr></tbody></table>

### La Lettre de la Semaine

La lettre d’aujourd’hui vient de Jacob. 

> Cher Doug Beyer,  
>  Concernant votre article ‘Le Pendule des Ombres’ :  
>  Avez-vous pensé à faire les elfes de Lorwyn verts et blancs et les elfes de Sombrelande noirs et verts ? Les elfes en général et avant Lorwyn semblaient être du coté des ‘bons’, et en étant noirs et verts dans Sombrelande, ils auraient mieux reflété le passage aux ténèbres de l’extension.  
>  – Jacob S.

Il est vrai que les elfes sont une tribu en quelque sorte ‘hors de propos’ au sujet du changement de ton entre Lorwyn et Sombrelande. Dans Lorwyn, ils sont les tyrans impérieux qui règnent sur le plan ensoleillé, dédaignant toute créature ne répondant pas exactement à leurs standards de beauté. Dans Sombrelande, ils sont les nobles chercheurs de lumière et de beauté dans un monde lié par la noirceur. Pendant ce temps, la majorité des autres tribus de Lorwyn fait l’*inverse* - elles deviennent plus effrayantes et lugubres en même temps que le plan. Avons-nous pensé à ne PAS avoir des elfes qui vont à contre-courant ? 

![](https://i.ormos.uk/65/92/65925ffea9c42d5784c96c265fbabab351f826e7dfbb705b97e2d7298e8e678f.jpg)La décision de faire les elfes verts et noirs fut confirmée assez tôt. Tandis que la vision créative de *Lorwyn* devint claire, il devint tout aussi clair que les elfes, en quintessence les enfants de la nature, seraient les maître de ce monde de nature et de beauté. Les elfes sont verts, mais l’ambiance ‘maîtres de’ appartenait au noir, et donc à une nouvelle identité pour les elfes. Nous aimions l’éloignement de l’ambiance traditionnelle des elfes, et cela donnait à *Lorwyn* une race pouvant servir de ‘méchants’ sans aller trop loin dans les terres du ‘Grand Méchant Diabolique’. 

Un autre bonus à jouer les elfes dans le sens de prédateurs hautains était la possibilité d’avoir un retournement de situation très dramatique dans *Sombrelande*. Ce sont de vraies crapules dans *Lorwyn*, régnant sur le royaume et tuant les laids. Ils reçoivent dans *Sombrelande* un sort bien mérité en voyant leur monde devenir bien plus mauvais envers eux, ce qui les fait chuter de leur piédestal. Les elfes sont dépassés en nombre par les autres créatures dans les deux extensions, mais dans Sombrelande, un monde rempli de monstres effrayants, c’est une situation vraiment horrible – et un retournement satisfaisant d’un point de vue narratif. 

Enfin, comme vous pouvez le remarquer, presque toutes les races de Lorwyn sont devenues d’une combinaison de couleurs *alliées* dans *Sombrelande*. Si les elfes étaient passés de verts et blancs à verts et noirs, nous n’aurions pas créé ce schéma, et les elfes n’auraient pas été si bien à leur place dans le thème des manas hybrides de *Sombrelande*.

* * *

Attendre la sortie de *Sombrelande* le 2 mai est trop dur ? Ne manquez pas votre première chance de jouer avec des cartes *Sombrelande* à l’[avant-premières](/en/articles/event-coverage/undated/magic-the-gathering-prereleases-3) des 19 et 20 avril !

*Traduction Émilien Wild*
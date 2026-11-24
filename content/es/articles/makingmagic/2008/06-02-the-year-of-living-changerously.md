---
id: qzhc33gy
kind: article
lang: es
path: /es/articles/makingmagic/2008/06-02-the-year-of-living-changerously
title: El Año que vivimos en cambio
published: '2008-06-02'
column_slug: makingmagic
column: Making Magic
authors:
- slug: markrosewater
  name: Mark Rosewater
translation_of: zfkkjngs
detected_lang: es
metadata_evidence:
  title:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
    lang_detected: es
    capture_id: 1977132
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,es
    captured_at: '2008-07-02 04:07:13+00'
    rule: html.title
  published:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
    lang_detected: es
    capture_id: 1977132
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,es
    captured_at: '2008-07-02 04:07:13+00'
    rule: classic.byline_date
  authors:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
    lang_detected: es
    capture_id: 1977132
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,es
    captured_at: '2008-07-02 04:07:13+00'
    rule: classic.authorarchive_link
  column:
    page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
    lang_detected: es
    capture_id: 1977132
    url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,es
    captured_at: '2008-07-02 04:07:13+00'
    rule: classic.legacy_column_rule
    registry_match: registry.explicit
sources:
- document_id: qzhc33gy
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,es
  page_key: wizards.com/default.asp?x=mtgcom/daily/mr334
  lang: es
  template: classic_asp
  captured_at: '2008-07-02 04:07:13+00'
  capture_id: 1977132
  wayback_url: https://web.archive.org/web/20080702040713id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,es
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: qzhc33gy
  capture_id: 1977132
  url: http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,es
  wayback_url: https://web.archive.org/web/20080702040713id_/http://www.wizards.com/default.asp?x=mtgcom/daily/mr334,,es
  captured_at: '2008-07-02 04:07:13+00'
  template: classic_asp
  sha256: b7f86a3a10d640870619859b5675de03f0a28d78f4dc3f149f1a658ec6e7da7a
render_recovery:
- code: unsupported_link
  element: a
  target: javascript:void(0);
  reason: The link uses a JavaScript placeholder. The preview kept any visible label.
  labels:
  - aquí
  - Haz clic aquí
  occurrences: 2
---
* * *

Si todavía no has leído [el anuncio oficial de hoy](/en/articles/feature/2008/06-02-changes-as-of-shards-of-alara), habrá grandes cambios en **Magic** desde la expansión *Fragmentos de Alara*. En esta columna los guiaré por lo que significan estos cambios y por qué creemos que son importantes para el juego. 

### Jugar es lo importante

Antes de comenzar con los detalles, déjenme explicar el panorama que impulsó todos estos cambios. Si vamos al grano, nuestro trabajo, el de la gente que hace **Magic**, es entusiasmar a las personas a que jueguen nuestro juego. En última instancia, hay dos grupos en los que necesitamos focalizarnos para cumplir esta tarea. Primero, tenemos que retener a los jugadores que tenemos. Segundo, tenemos que conseguir nuevos (o recuperar) jugadores. Ambos son importantes para la salud a largo plazo de **Magic**. (Si te interesa una versión más detallada de este tema, mira mi artículo [Assume the Acquisition](/en/articles/makingmagic/2008/03-03-assume-the-acquisition).) Con la actual base de jugadores, siempre podremos hacer algo más, pero por el momento sabemos que el juego va bien y creemos que lo que viene los hará aún más felices. 

Eso significa que la clave es encontrar mejores maneras de hacer crecer el juego incorporando nuevos jugadores. La importancia de adquirir nuevos jugadores fue un tema recurrente este año en **magicthegathering.com**. Ahora es nuestra oportunidad de mostrarte qué estamos haciendo con el producto para que eso suceda. Mi artículo de hoy les explicará los cambios que estamos haciendo, cómo impactaran el producto y por qué creemos que ayudará al crecimiento del juego.

### Repensar pensar pensar

Una de las mejores maneras de acercarse a un problema es alejarse y tratarlo como un problema nuevo. No confíes en el pensamiento convencional, porque asumirás siempre lo mismo y volverás al mismo lugar. Así que empezamos de cero. ¿Cómo conseguimos nuevos jugadores? ¿Cuáles son los límites que hacen que jugar sea difícil? ¿Qué aspectos de nuestro juego podrían ser más amigables para los nuevos jugadores?

Al empezar las discusiones, nos dimos cuenta de algo importante. Hasta hace poco, focalizamos nuestros esfuerzos de adquisición en las colecciones básicas y nuestros esfuerzos de retención en las expansiones, con la idea de que un jugador nuevo entraría con nuestro producto más simpley el jugador más avanzado le prestaría atención a las últimas cartas. Nos replanteamos esta suposición (como replanteamos toda suposición) y buscamos información. ¿Sabes qué encontramos? Estábamos equivocados. Básicamente, los nuevos jugadores no siguen un camino lineal. Comienzan jugando con el producto de **Magic** que primero conozcan, y como la mayoría de los jugadores aprenden de otros jugadores, su primera impresión *no* es normalmente una colección básica.

¿Qué significa esto? Para empezar, nos obligó a mirar nuestras expansiones de la misma manera en que miramos nuestras colecciones básicas. Y con esa mirada, todo se ve muy distinto. Creo que ya es hora de empezar con los cambios y explicaré muchos de nuestros descubrimientos y observaciones mientras tanto.

### Cambio #1: Vamos a imprimir menos cartas por año

Permítanme empezar esta sección explicando algo de vocabulario. Voy a hablar de "años de **Magic**". Lo que quiero decir es que voy a empezar el "año" con la expansión grande de otoño (del hemisferio norte) y luego incluir todas las expansiones hasta la siguiente expansión grande de otoño (del hemisferio norte). Me voy a referir a cada año con el nombre de la expansión grande o su símbolo de expansión. 

Con eso ya resuelto, vayamos al grano de esta sección. Comenzando con el año de *Fragmentos de Alara*, vamos a imprimir menos cartas por año.

¿De qué tipo de cambio estamos hablando? Bueno, veamos cuántas cartas imprimimos por año de **Magic**, comenzando con *Era Glacial*. 

(Algunas notas técnicas sobre este gráfico porque se que voy a recibir demasiados emails sobre este artículo tal como está: Sí, estoy contando a *Tierras Natales* como parte del año de *Era Glacial* en este caso, no estoy contando tierras básicas para ninguno de estos, estoy contando la rareza del "Starter" de*Octava* y *Novena Edición*, y no estoy contando las colecciones *Un*\- o las colecciones de principiantes como *Portal*. Por último, *sí* estoy contando las tierras básicas nevadas de *Ola de frío* pero no de *Era Glacial*. ¿Por qué? Porque las tierras nevadas de *Ola de frío* estaban en el lugar de una común en los sobres.)

![](https://i.ormos.uk/af/8e/af8ecb46d035d76106b0a9e5894158df75b7fa0a9a254f39b61d08348cb53db3.gif)

![](https://i.ormos.uk/d5/63/d563aba7ec040114cf6a0aa1b8eb053d6a3a30545bda66e4cc0082374ec81605.gif)

Ahora veamos el año siguiente. Haz clic aquí para agregarlo a la imagen de arriba.

Sin contar la colección básica, imprimiremos menos cartas durante el año de *Fragmentos de Alara* de lo que hemos impreso antes en cualquier año de **Magic**: 519. Incluso contando la colección básica, son más de cien cartas menos que el año anterior. Hay dos razones para este cambio. Primero, mientras analizamos las barreras de ingreso al juego, nos dimos cuenta que la velocidad de lanzamiento de nuevas cartas era lo principal. Si los nuevos jugadores se ven rápidamente sobrepasados suelen alejarse, y no volver. Un jugador nuevo hoy intentando entrar al juego tiene las mismas dificultades que todos los nuevos jugadores han tenido históricamente, pero uno que comience en julio, por ejemplo, verá un entorno estándar con más de 2.100 cartas. Una de las maneras más simples de simplicar esto es imprimir menos cartas.

La segunda razón para este cambio fue la opinión de jugadores actuales. Estábamos simplemente imprimiendo demasiadas cartas. Incluso jugadores estables tenían problemas para seguir. Como demuestra el gráfico de arriba, estuvimos aumentando la cantidad de cartas producidas en los últimos años. Fuimos demasiado lejos. Estábamos imprimiendo demasiadas cartas para los jugadores nuevos *y* los estables.

Este cambio ayudará a llegar a equilibrio más estable. ¿Por qué entonces decidimos un número menor de lo que fue nuestro estándar durante tantos años? Porque queremos dejarnos un poco de espacio para cuando tengamos ideas interesantes como las cartas "desplazadas en el tiempo" de *Espiral del tiempo* o la estructura del mini-bloque *Lorwyn* / *Páramo Sombrío*. 519 cartas no es nuestro techo, sino una nueva base. 

Los lectores atentos habrán notado que el anuncio oficial indica que el tamaño de la próxima colección básica es desconocido. ¿Entonces por qué mi gráfico muestra un número? Porque como miembro del equipo que está trabajando en la colección, creo que 229 será un número confiable, pero como la colección todavía no está oficialmente terminada, los números oficiales no son finales. Sin embargo, incluso cuando la colección cambie un poco, definitivamente nos mantendremos en la filosofía de "imprimir menos". 

### Cambio #2: Agregaremos una nueva rareza llamada rara mítica

Otra parte importante de atraer a nuevos jugadores es entender de qué ambiente vienen. Cuando **Magic** empezó, tuvo el lujo de definirse a sí mismo porque era el primero de su clase. Ya no vivimos en ese mundo. Los juegos de cartas intercambiables ya son un género de juego establecido. Tal vez antes la mayoría de los jugadores conocían el género con **Magic**. Con la explosión de los JCI, particularmente los orientados a jugadores de menor edad, esto ya no es cierto. 

Nos dimos cuenta que ya no tenemos el lujo de definir a **Magic** sólo contra sí mismo. El género de juegos de cartas intercambiables ha creado algunos estándares que evolucionaron de decisiones tomadas después de la creación de **Magic**, siendo la rareza uno de los mejores ejemplos. La idea de un JCI con sólo tres rarezas es anticuada. (Y antes de que me escriban, entiendo que técnicamente las tierras básicas son una cuarta rareza; para esta discusión no voy a tenerlo en cuenta.) **Magic** es el único juego de cartas intercambiables importante actualmente impreso con sólo tres rarezas. Si queremos seguir siendo competitivos al atraer a nuevos jugadores, debemos adecuarnos a los estándares de la industria.

¿Qué es eso del "estándar de la industria" que ayudarán a adquirir nuevos jugadores? Dos cosas. El primero es la expectativa. La mayoría de los jugadores se acercarán a **Magic** ya habiendo experimentado este estándar, y esperarán que cualquier nuevo juego de cartas intercambiables que prueben funcione como los juegos que ya conocen. Como siempre digo en esta columna, cumplir con las expectativas es muy importante. Segundo, hay una razón por la cual algo se convierte en un estándar de la industria. Funciona. Saber que tienes el potencial de abrir algo que podrás mostrar a tus amigos es muy tentador y ayuda a atraer nuevos jugadores al juego. 

Las buenas noticias son que encontramos una manera que nos permitirá aumentar la cantidad de rarezas sin tener que imprimir cartas con una rareza más alta de la que imprimimos hoy. Para explicar mejor, cuando revisas los número resulta que **Magic** usó la palabra "rara" para un rango enorme de rareza. Para ponerlo en contexto, aquí hay un gráfico de todas las colecciones de **Magic** disponibles actualmente en Estándar que muestra cuántas raras hay en cada colección.

![](https://i.ormos.uk/58/c4/58c4711dc82d9280365a6d84a3940503b8133c6c2f59d271150a10b752b005f5.gif)

Como pueden ver, hay un espectro gigante de lo que significa "rara". El punto más alto es, por ejemplo, tres veces más grande que el punto más bajo. El descubrimiento más grande que hicimos fue que podíamos agregar un nuevo nivel de rareza sin tener que imprimir cartas más raras que ahora. La mejor manera de explicarlo es simplemente mostrar el sistema nuevo y el viejo lado a lado. La rareza de la colección a la izquierda es igual a la nueva rareza listada a la derecha. 

<table><tbody><tr><td><b>Viejo sistema</b></td>&#10;<td><b>Nuevo sistema</b></td>&#10;</tr>&#10;<tr><td>Rara de <i>Décima Edición</i></td>&#10;<td>Rara mítica, colección grande</td>&#10;</tr>&#10;<tr><td>Rara de <i>Páramo Sombrío</i></td>&#10;<td>Rara mítica, colección pequeña</td>&#10;</tr>&#10;<tr><td>Rara de <i>Visión del futuro</i></td>&#10;<td>Rara, colección grande</td>&#10;</tr>&#10;<tr><td>Rara, <i>Caos planar</i></td>&#10;<td>Rara, colección pequeña </td>&#10;</tr>&#10;</tbody></table>

Ahora que establecimos el rango de rarezas, miremos cuántas cartas de cada rareza tendrá *Fragmentos de* *Alara*.

Comunes – 101  
 Poco comunes – 60  
 Raras – 53  
 Raras míticas – 15

¿Qué tan seguido aparecerá cada una de estas? Las comunes aparecerán diez por sobre (sí, esto es un cambio del que hablaré en la próxima sección). Las poco comunes aparecerán tres por sobre. Las raras aparecerán una por sobre, excepto en aproximadamente uno de cada ocho sobres, en los que tendrás en su lugar una rara mítica. Por cierto, en uno de cada ocho sobres podría parecer que las raras míticas son siete veces más raras que las raras. Pero no, son el doble de raras. (Es complicado, pero tiene que ver con cómo se corta la hoja y el hecho de que hay más raras que raras míticas.)

Ahora veamos "Papel", un ejemplo de una colección pequeña en este nuevo mundo. 

Comunes – 60  
 Poco comunes – 40  
 Raras – 35  
 Raras míticas – 10

Al igual que en *Fragmentos de Alara*, las rarezas tienen la misma cantidad de cartas por sobre, incluyendo la frecuencia con la que obtendrás una rara mítica en lugar de una rara. 

Esto nos lleva ahora a la siguiente pregunta: ¿Cómo se separan las cartas en raras y raras míticas? O más detalladamente, ¿Qué tipo de cartas van a ser raras míticas? Queremos que la ambientación de las raras míticas sea algo que las haga sentir como únicas y especiales. Generalizando, nos referimos a cartas como Planeswalkers, la mayoría de las leyendas y criaturas y hechizos con un tono épico. *No* será simplemente una lista de las cartas más poderosas de la colección a nivel de torneo.

Decidimos que hay ciertas cosas que específicamente no queremos que sean raras míticas. La categoría más grande es la de cartas utilitarias, lo que definiré como cartas que sirven una función universal. Algunos ejemplos de esta categoría serían los ciclos de cartas de tierra dual y cartas como Mutabóveda o Quemar. Eso toca un tema de larga discusión que algunos jugadores plantearon con respecto a ciertas raras, como por ejemplo, las tierras duales. Como estamos haciendo menos cartas por colección, en este nuevo mundo las raras individuales serán más fáciles de adquirir porque cada rara en una colección grande aparecerá ahora un 25% más frecuentemente. 

Lo que lleva a la siguiente pregunta: ¿Las raras míticas tendrán versiones premium? Sí. De hecho, no sólo tendrán una versión normal y premium, sino que las versiones premium aparecerán con una frecuencia un poco mayor. (La cantidad de raras premium y raras míticas premium combinada que obtendrás desde *Fragmentos de Alara* es mayor que la cantidad de raras premium que obtienes ahora.)

La última pregunta de raras míticas: ¿Las raras míticas tendrán un nuevo color de símbolo de expansión? Sí. ¿Cuál es? Prometo que lo mostraré antes de que terminemos. 

### Cambio #3: Todos los sobres tendrán una carta de tierra básica en lugar de una común

Este fue un cambio que introdujimos en la colección básica desde *Séptima Edición*. La razón fue bastante simple: los jugadores principiantes tenían problemas para conseguir tierras. Sin tierras, no pueden jugar: la definición misma de una barrera para jugar. Antes de *Séptima Edición*, creíamos que había suficientes productos que tenían tierras básicas. El error de nuestro razonamiento tenía dos bases. Primero, no había manera de que un jugador nuevo supiera qué producto tenía tierras básicas, y poca gente compra un segundo producto si el primero no sirve por sí mismo. Segundo, no todos los lugares tienen todos los productos de **Magic**. Había tiendas, por ejemplo, que vendían sólo sobres, lo que significa que un jugador que compraba exclusivamente en esa tienda no tenía manera de solucionar ese problema.

Con nuestro nuevo entendimiento de cómo los jugadores se acercan al juego, fue muy claro que si queríamos garantizar que los nuevos jugadores obtuvieran tierras, teníamos que incluirlas en el producto principal que estaban comprando. Por lo tanto, desde *Fragmentos de Alara*, cada sobre tendrá una rara (reemplazada ocasionalmente por una rara mítica), tres poco comunes, diez comunes y una tierra básica. Esta nueva distribución de rareza se aplicará a todas las colecciones básicas y expansiones (grandes y pequeñas) de aquí en más.

### Cambio #4: Los mazos temáticos se convierten en Pack de inicio

Desde la introducción de los mazos preconstruidos, los mazos temáticos han tenido que servir a dos amos. Fueron diseñados como un producto de nivel inicial para ayudar a que nuevos jugadores entren al juego y como un producto de muestra para que los jugadores establecidos y los alejados pudieran experimentar la temática y las mecánicas de una nueva colección. El problema con esto fue que no nos permitió maximizar los mazos para ninguno de los grupos. La importancia de adquirir nuevos jugadores finalmente decidió este empate. 

Cuando nos fijamos cómo se mostraba el producto en las tiendas, nos dimos cuenta que teníamos algunos agujeros (algunos muy grandes, en particular en las tiendas masivas) donde no había producto inicial a la venta. Siendo una enorme barrera potencial para nuevos jugadores, teníamos que encontrar una manera de asegurar que el producto de nivel inicial estuviera siempre disponible. La respuesta, después de mucho investigar, fue que los mazos temáticos se inclinaran hacia el lado del producto de nivel inicial. Como acompañan a todas las colecciones, garantizarían que ese producto estuviera a disposición.

Comenzando con *Fragmentos de Alara*, los mazos temáticos serán un nuevo producto llamado"pack de inicio", orientado específicamente a ayudar a que los principiantes ingresen al juego. Para esto repensamos qué necesitaba un producto inicial, lo que resultó en un cambio sustancial en el contenido del producto. Para el actual comprador de mazo temático, los packs de inicio seguirán teniendo un mazo preconstruido que presenta los nuevos temas y mecánicas de la nueva colección, pero logramos aumentar el valor del producto (más sobre esto en un momento), manteniendo el mismo precio. Dicho eso, este producto sufrirá cambios significativos. 

Para refrescar tu memoria, aquí está el contenido de un mazo temático de *Páramo Sombrío*:

2 raras  
 13 poco comunes  
 45 comunes / tierras  
 1 tierra premium

Ahora este es el contenido de un pack de inicio de *Fragmentos de Alara*:

![](https://i.ormos.uk/43/8e/438ec375bd489382c7d84c784e370b996897e343401bb6a59c6a32c59c141272.jpg)1 rara premium  
 1 rara no premium  
 7 poco comunes  
 32 comunes / tierras  
 1 sobre de *Fragmentos de Alara*

Hay dos diferencias muy importantes. Primero, el mazo del pack de inicio tiene 41 cartas comparado con las 61 del mazo temático. Segundo, el pack de inicio también incluye un sobre (llevando el pack de inicio a 56 cartas). Considerando las cartas del sobre, el pack de inicio tiene tres poco comunes menos, dos comunes menos y ninguna tierra premium. Pero a cambio, obtiene una rara adicional y encima premium.

¿Por qué el cambio? Comencemos con el sobre. Una de las preocupaciones que teníamos con los mazos preconstruidos para principiantes era que son un poco confusos sobre qué es realmente el producto. Un mazo auto contenido no cubre todo lo que es un juego de cartas intercambiables. Queríamos mostrarle al nuevo jugador el potencial de lo que podría ser su mazo. Para hacer esto, necesitábamos poner un sobre en sus manos. Sentíamos que sólo abriendo un sobre de cartas al azar podíamos darle a los nuevos jugadores un poco de lo que **Magic** es realmente.

Además, creíamos que la estrategia del pack de inicio daba más empuje para modificar tu mazo. Esto se da en parte incluyendo un sobre, pero más se da por hacer el mazo más chico que sesenta cartas. El menor tamaño lleva a los jugadores a agregar cartas para llegar a sesenta (otra lección que aprendimos de las colecciones básicas). 

Los packs de inicio también cambiaron para tener dos hojas de reglas. Una tiene todo lo que sueles leer sobre los mazos temáticos (cómo funcionan las mecánicas, listas de mazos, etc.) pero ahora hay además otra hoja escrita para ayudar a los jugadores a aprender a adaptar su mazo, lo que permite a cualquier pack de inicio servir también como producto explicatorio de una primera compra. 

La transformación de la carta premium de una tierra en una rara ocurrió cuando repensábamos el envoltorio. Queríamos crear una caja con una ventana que permitiera al jugador ver una de las cartas. Con esa tecnología, la opción obvia para ese lugar era una carta rara premium (y una buena), así que agregamos una al producto. Una vez que miramos el producto final sentimos que habíamos mejorado el valor final del producto *y* que habíamos logrado hacerlo mucho más accesible y atractivo a los nuevos jugadores.

### Terminando

Entiendo que estoy dándoles muchísima información de pronto, pero quería asegurarme que tuvieran la oportunidad de escuchar el razonamiento de estos cambios. En última instancia, los cambios discutidos hoy fueron realizados porque creemos firmemente en que son para que el juego esté mejor en el largo plazo.

Ahora es su turno. Queremos escuchar qué piensan de todos estos cambios. Por favor usen nuestros foros para darnos su opinión sobre estos cambios en particular y sobre otras cosas que creen que deberíamos hacer para resolver los problemas de los nuevos jugadores que he mencionado. 

Vuelvan la semana que viene, cuando hablaré de algo menos trascendente.

Un momento...tengo la sensación de que me estoy olvidando de algo. Ah, sí. Haz clic aquí para ver cómo se ve el símbolo de expansión de una rara mítica. 

![Sarkhan Vol](https://i.ormos.uk/1d/0f/1d0f2cb56b4d05bef7d842629120cb96460f58c3b0e64a845a3886be40cf0cec.jpg "Sarkhan Vol")

Bien, ahora sí terminé.

Hasta entonces, que puedas entender la necesidad del cambio.

Mark Rosewater
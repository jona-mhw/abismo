# ABISMO · documento de diseño

## La idea en una línea

**Lo trajeron para firmar que los golpes eran ruido del casco.** A las tres, en el compartimento 7, alguien golpea tres veces. Desde 1983.

## Lo que pasó (la verdad que el jugador reconstruye)

- **14 de octubre de 1983, 03:00.** El compartimento 7 del K-417 «Zarya» hace agua en el punto 71° N 38° E. Vólkov, Orlov y Sedykh quedan adentro. El oficial de guardia, Bélov, ordena sellar la puerta para salvar el barco. Golpean durante cuarenta minutos, tres golpes por serie. La Flota suelda la puerta y cierra el caso como «ruido del casco».
- Cada vez que el Zarya vuelve a ese punto, siempre un 14 de octubre, los golpes vuelven a las 03:00.
- **1989.** Con la glasnost, la Flota invita a un acústico estadounidense, el **Dr. Thomas Hale** (Woods Hole). La invitación lo dice sin rodeos: su informe debe confirmar el origen térmico. Una firma occidental cierra el expediente.
- **02:31.** Cede el sello de la cúpula de observación con Hale adentro. La tripulación lo da por ahogado y evacúa en la cápsula. Hale despierta a las 02:52, empapado y solo, a 412 metros.

No hay monstruo. El terror es la oscuridad, el agua, la presión y una puerta que golpea. Lo único ambiguo es si los golpes son de los muertos. El juego no lo resuelve: lo resuelve el informe de Hale.

## Personajes y voces

| Quién | Idioma | Voz |
|---|---|---|
| **Hale** (tú) | Inglés | Monólogo interior, cansado, cerca del micrófono |
| **Bélov** | Ruso y un inglés roto | Altavoz del puente y, después, la radio de la cápsula |
| **Los tres del 7** | Ruso, susurrado | Detrás de la puerta, por el hidrófono. Una vez, en inglés: «Tom…» |
| **El pesquero «Havbris»** | Inglés con acento noruego | Al final, en la tormenta |

Todo va subtitulado en español. Las voces están en `voz/*.mp3`, generadas con `tools/voces.mjs` desde el bloque `VO` de `index.html`. La key de la API nunca entra al repo.

## Arco

Hale llega para firmar una mentira cómoda y termina abriendo la puerta que todos temen. Al final escribe la verdad: **origen de los golpes: no térmico.** Los golpes que le daban miedo son los que guían al pesquero hasta él.

## Estructura (10 a 12 min)

| # | Momento | Qué siente el jugador | Mecánica |
|---|---|---|---|
| — | **Expediente** (4 tarjetas) | Entender antes de temer | 1983: el 7 se inunda, el oficial de guardia cierra la puerta. El informe: «ruido del casco». Tú: Hale, vienes a firmarlo |
| 0 | **Cubierta**, 16:40 | Frío, belleza, el encargo | Bélov dice el trabajo en claro: «Su trabajo es fácil: escuche y escriba que estos sonidos son del submarino». La escotilla se habilita cuando ya lo dijo; se traba al abrirla |
| 1 | **Descenso** en la cúpula | Asombro → presagio → desmayo | Peces, ballena, naufragio. Un sonar chico en la cúpula muestra el contacto grande que se acerca (la ballena) y, al final, un eco rojo «ВНУТРИ · ADENTRO». Al fondo, el foco parpadea y suenan tres golpes desde adentro del submarino (nadie se ve). Se rompe el sello: el agua lo tapa, se marea, la vista se cierra y dice «Annie…» antes de perder el conocimiento |
| 2 | **Despertar**, 02:52 | Soledad, cuenta regresiva | Mantener para levantarse. La linterna parte apagada y no prende a la primera («Vamos. Vamos.» «No me hagas esto.» «Ahí está.»). «Se rompió el sello y el agua me tiró aquí abajo.» «Ocho minutos para las tres.» |
| 3 | **Camarote** | Quién soy, qué me espera | Espejo, foto de Annie, carta de invitación (opcionales) |
| 4 | **Máquinas** | Oficio, primer golpe | Cebar + arrancar soltando en lo verde; el siete contesta |
| 5 | **La radio** | Alivio: Bélov está vivo | Llamada desde la cápsula. La apuesta: el Zarya hace agua y no aguanta hasta el barco; hay que hacerlo subir |
| 6 | **Apagón** | Los golpes caminan | Recorren el casco y se detienen en el siete. La linterna se muere en medio: «No. No, no, ahora no.» |
| 7 | **La puerta** | Hay alguien adentro | Pegar la oreja: «Abran… por favor» |
| 8 | **Ojo de buey** | El vidrio es un espejo | Un marinero detrás de ti, solo en el reflejo |
| 9 | **Oxígeno** | Urgencia, no soy el primero | Válvula agarrotada: tocar rápido. Al lado, una nota en inglés: Whitcombe (1986) y Lindqvist (1988) no firmaron. «No soy el primero… y siguieron trayendo gente» |
| 10 | **03:00** | Terror en rojo | La rueda del siete gira sola: corre y sujétala. «Tom…» |
| 11 | **Sonar** | Certeza | Con los auriculares, el sonar llena la pantalla: el Zarya al centro, tres ecos afuera del casco y la traza del hidrófono. Los ecos se cierran sobre ti, el tubo se apaga y en el vidrio negro hay alguien detrás. «No es el casco» |
| 12 | **Confesión** | Traición, culpa | El oficial de guardia era Bélov. El aire para subir está en el siete: por eso no quería que te acercaras |
| 13 | **Abrir el siete** | Valor | La misma rueda, ahora para abrir. Cuarenta marcas, tres gorras. «Спасибо», y silencio: por primera vez, nada golpea |
| 14 | **Inundación** | Pánico | Corre a la palanca mientras el agua sube y te frena |
| 15 | **Emersión** | Vértigo | Soplado de emergencia: 412 → 0 m |
| 16 | **Rescate** | Último minuto | En cubierta, tres golpes bajo el agua se alejan hacia la niebla y traen al pesquero. Cada seña con la linterna es un golpe. Si no haces señas, llega igual: tú los salvaste, ellos te salvan |
| 17 | **El informe** | Cierre | Woods Hole, 9 de diciembre (el cumpleaños de Annie). La Flota ya escribió «térmico»: lo corriges con un «no» y firmas con el dedo. Bélov firma como testigo. La foto de Annie. Después, solo los tres nombres |

## Muertes (cada una enseña algo)

- **Sin aire:** el oxígeno importa.
- **El siete se abrió:** a las 03:00 hay que sujetar la rueda.
- **El agua fue más rápida:** en la inundación no hay que detenerse.

## Sonido como guion

- **Tres golpes** son la firma de todo: el arranque fallido, el apagón, la puerta, el hidrófono, el final.
- **Rojo = silencio primero.** A las 03:00 se apaga la ventilación antes de que empiecen los golpes.
- **Las voces de los muertos** suenan apagadas y con mucha sala, como a través de acero.

## Cómo se cuenta (regla de claridad)

- **El jugador sabe qué pasó desde el principio**; lo que no sabe es quién cerró la puerta ni si los golpes son de los muertos. La confesión revela el quién, no el qué.
- Cada objetivo en pantalla dice **qué hacer y por qué** («El aire se acaba · restaura el oxígeno en soporte vital»).
- Las notas son color, no información obligatoria: todo lo necesario se oye o se lee en las tarjetas.
- **Todo lo del submarino está en ruso** (placas, válvulas, sonar, papeles). La primera vez que miras una placa, Hale piensa la traducción («HALE · PIENSA»). Las notas se ven en su idioma y abajo «lo que entiendo». La interfaz (objetivo, botones) va en español.
- **Papelitos en inglés** pegados sobre placas rusas (ENGINE RM., AIR / O2, SONAR, DON'T.): orientan al jugador y son la pista de que hubo otros expertos antes.
- **La linterna** se apaga en tres momentos elegidos (los golpes caminando, camino al sonar, al entrar al 7) y cuesta volver a prenderla. Nunca al azar.
- Subtítulos: arriba, quién habla (HALE, BÉLOV · RADIO, DESDE EL 7, PESQUERO). Lo que se oye en ruso va **[entre corchetes]** con la marca RU, solo ese trozo: Bélov mezcla ruso e inglés.
- Lo sobrenatural se insinúa con sonido antes de mostrarse: en el descenso no se ve a nadie.
- Prueba: después de jugar, cualquiera cuenta la historia en tres frases.

## No perderse (regla de orientación)

- El objetivo dice qué, por qué y **hacia dónde** (popa/proa y número de compuerta).
- **Tocar el objetivo**: Hale piensa la dirección y los metros que faltan.
- Si no avanzas: a los 25 s Hale piensa la dirección; a los 50 s, tres golpes suenan desde el objetivo; a los 80 s, otra vez la dirección y los metros. Si estás al lado pero no sabes qué hacer, a los 22 s aparece cómo («MANTÉN el botón…»).
- En las escenas donde no puedes actuar (radio, golpes que caminan, la oreja en la puerta) el oxígeno no baja.
- La nota del médico tacha el nombre del oficial de guardia: el quién lo revela Bélov.

## Personajes en 3D

Modelos humanos de MakeHuman (CC0) con esqueleto `game_engine`, generados por `tools/humanos.py` y exportados a GLB (texturas WebP, ~1,5–2 MB c/u). En el juego se clonan con `SkeletonUtils`, cada uno con sus materiales; los brazos pasan de la pose en A a caídos, respiran y mueven la cabeza y el brazo de la linterna con huesos.

| Quién | Modelo | Dónde aparece |
|---|---|---|
| Hale (tú) | `hale` empapado, linterna en la mano | Solo en reflejos: espejo, ojo de buey |
| El otro | `marinero` pálido, con brillo frío | Detrás de ti, solo en el reflejo |
| Pescadores del «Havbris» | `hale` y `marinero` con impermeable amarillo | En el rescate: uno lanza el cabo, el otro te hace señas |

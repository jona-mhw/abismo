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
| 0 | **Cubierta**, 16:40 | Frío, belleza, el encargo | Mirar, abrir la escotilla (se traba). Bélov: «Golpea a las tres. Siempre a las tres.» |
| 1 | **Descenso** en la cúpula | Asombro → presagio | Peces, ballena, naufragio, alguien en la cubierta. Tres golpes en el vidrio |
| 2 | **Despertar**, 02:52 | Soledad, cuenta regresiva | Mantener para levantarse. «Ocho minutos para las tres.» |
| 3 | **Camarote** | Quién soy, qué me espera | Espejo, foto de Annie, carta de invitación (opcionales) |
| 4 | **Máquinas** | Oficio, primer golpe | Cebar + arrancar soltando en lo verde; el siete contesta |
| 5 | **La radio** | Alivio: Bélov está vivo | Llamada desde la cápsula |
| 6 | **Apagón** | Los golpes caminan | Recorren el casco y se detienen en el siete |
| 7 | **La puerta** | Hay alguien adentro | Pegar la oreja: «Abran… por favor» |
| 8 | **Ojo de buey** | El vidrio es un espejo | Un marinero detrás de ti, solo en el reflejo |
| 9 | **Oxígeno** | Urgencia | Válvula agarrotada: tocar rápido |
| 10 | **03:00** | Terror en rojo | La rueda del siete gira sola: corre y sujétala. «Tom…» |
| 11 | **Sonar** | Certeza | Golpes afuera del casco, voces en el hidrófono. «No es el casco» |
| 12 | **Confesión** | Traición, culpa | Bélov cerró la puerta en el 83. El aire para emerger está en el siete |
| 13 | **Abrir el siete** | Valor | La misma rueda, ahora para abrir. Cuarenta marcas, tres gorras. «Спасибо» |
| 14 | **Inundación** | Pánico | Corre a la palanca mientras el agua sube y te frena |
| 15 | **Emersión** | Vértigo | Soplado de emergencia: 412 → 0 m |
| 16 | **Rescate** | Último minuto | En cubierta al amanecer, el Zarya se hunde. Señas con la linterna, agarrar el cabo |

## Muertes (cada una enseña algo)

- **Sin aire:** el oxígeno importa.
- **El siete se abrió:** a las 03:00 hay que sujetar la rueda.
- **El agua fue más rápida:** en la inundación no hay que detenerse.
- **El mar te llevó:** en cubierta hay que hacer señas pronto.

## Sonido como guion

- **Tres golpes** son la firma de todo: el arranque fallido, el apagón, la puerta, el hidrófono, el final.
- **Rojo = silencio primero.** A las 03:00 se apaga la ventilación antes de que empiecen los golpes.
- **Las voces de los muertos** suenan apagadas y con mucha sala, como a través de acero.

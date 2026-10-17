# ABISMO

Terror en primera persona a bordo del K-417 «Zarya», submarino soviético. Mar de Barents, 14 de octubre de 1989.

Eres el Dr. Thomas Hale, acústico estadounidense invitado por la Flota del Norte. Tu trabajo es escuchar los golpes que salen del compartimento 7 y firmar que son ruido del casco. A las 02:52 despiertas solo, empapado, a 412 metros. A las tres, alguien golpea desde el siete.

- **Sin monstruos:** el miedo está en la puerta del siete, en el agua y en la presión.
- **Voces reales** en inglés y en ruso, subtituladas en español.
- **A las 03:00**, la rueda del siete gira sola: corre y sujétala.
- **Final:** emerger y que te rescaten a último minuto.

Mobile first, three.js, efectos sintetizados con Web Audio. 10 a 12 minutos.

Juega en https://jona-mhw.github.io/abismo/ (con audífonos). El diseño completo está en [DISENO.md](DISENO.md).

Las voces (`voz/*.mp3`) se generan con `GEMINI_API_KEY=... node tools/voces.mjs` a partir del bloque `VO` de `index.html`. La key nunca se sube al repo.

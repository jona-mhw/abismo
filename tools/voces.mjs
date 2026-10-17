// Genera las voces del juego con el TTS de Gemini.
// Uso: GEMINI_API_KEY=... node tools/voces.mjs [id ...]   (sin ids: solo las que faltan)
// Lee el bloque VO de index.html y escribe voz/<id>.mp3. La key nunca se guarda en el repo.
import fs from 'fs';
import { execFileSync } from 'child_process';
const KEY = process.env.GEMINI_API_KEY;
if (!KEY) { console.error('Falta GEMINI_API_KEY'); process.exit(1); }
const root = new URL('..', import.meta.url).pathname;
const src = fs.readFileSync(root + 'index.html', 'utf8');
const block = src.slice(src.indexOf('/*VO*/') + 6, src.indexOf('/*/VO*/'));
const VO = Function('return ' + block.trim().replace(/^const VO = /, '').replace(/;$/, ''))();
const VOICE = { hale: 'Iapetus', belov: 'Algenib', dead: 'Enceladus', res: 'Orus' };
const STYLE = {
  hale: 'Read this as an American man in his early forties, a scientist, exhausted and frightened, speaking quietly to himself, close to the microphone. Natural, not theatrical',
  belov: 'Read this as an old Russian submarine commander, deep gravelly voice, heavy Russian accent when speaking English and native Russian when speaking Russian, tired and grim',
  res: 'Read this as a Norwegian fisherman shouting in English with a Scandinavian accent, over a storm',
  dead: 'Whisper this very slowly and softly, breathy, exhausted, like a man trapped behind a steel door',
};
const out = root + 'voz/'; fs.mkdirSync(out, { recursive: true });
const only = process.argv.slice(2);
const ids = Object.keys(VO).filter(k => only.length ? only.includes(k) : !fs.existsSync(out + k + '.mp3'));
for (const id of ids) {
  const v = VO[id], st = (v.st ? STYLE[v.s] + '; ' + v.st : STYLE[v.s]);
  const body = { contents: [{ parts: [{ text: `${st}:\n${v.t}` }] }], generationConfig: { responseModalities: ['AUDIO'], speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: VOICE[v.s] } } } } };
  let ok = false;
  for (let tries = 0; tries < 4 && !ok; tries++) {
    try {
      const r = await fetch('https://generativelanguage.googleapis.com/v1beta/models/' + (process.env.TTS_MODEL || 'gemini-2.5-pro-preview-tts') + ':generateContent', { method: 'POST', headers: { 'x-goog-api-key': KEY, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      const j = await r.json();
      const d = j?.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (!d) throw new Error(JSON.stringify(j).slice(0, 200));
      fs.writeFileSync('/tmp/vo.pcm', Buffer.from(d, 'base64'));
      // recorta silencios, normaliza y comprime (mono 48 kbps)
      execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 's16le', '-ar', '24000', '-ac', '1', '-i', '/tmp/vo.pcm',
        '-af', 'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.15,areverse,loudnorm=I=-18:TP=-2',
        '-ar', '24000', '-b:a', '48k', out + id + '.mp3']);
      ok = true; console.log('ok', id);
    } catch (e) { console.log('retry', id, e.message.slice(0, 120)); await new Promise(r => setTimeout(r, 4000 * (tries + 1))); }
  }
  if (!ok) console.log('FAIL', id);
}

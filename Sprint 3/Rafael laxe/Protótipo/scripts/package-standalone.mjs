import { readFile, writeFile, readdir } from 'node:fs/promises';

const root = new URL('../', import.meta.url);
let html = await readFile(new URL('dist/index.html', root), 'utf8');
const scriptPath = html.match(/<script[^>]+src="([^"]+)"[^>]*><\/script>/)[1];
const stylePath = html.match(/<link[^>]+href="([^"]+\.css)"[^>]*>/)[1];
const js = await readFile(new URL(`dist${scriptPath}`, root), 'utf8');
const css = await readFile(new URL(`dist${stylePath}`, root), 'utf8');
const images = {};
for (const name of await readdir(new URL('public/assets/', root))) {
  const mime = name.endsWith('.png') ? 'image/png' : 'image/jpeg';
  const bytes = await readFile(new URL(`public/assets/${name}`, root));
  images[`/assets/${name}`] = `data:${mime};base64,${bytes.toString('base64')}`;
}
html = html.replace(/<script[^>]+src="[^"]+"[^>]*><\/script>/, '');
html = html.replace(/<link[^>]+href="[^"]+\.css"[^>]*>/, () => `<style>${css}</style>`);
const safeJs = js.replace(/<\/script/gi, '<\\/script');
html = html.replace('</body>', () => `<script>window.FOODLINK_ASSETS=${JSON.stringify(images)};</script><script type="module">${safeJs}</script></body>`);
await writeFile(new URL('FoodLink-Prototipo.html', root), html);
console.log('FoodLink-Prototipo.html gerado: estilos, código e imagens incorporados.');

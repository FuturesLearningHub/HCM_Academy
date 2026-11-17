/* Job aid screenshots from a video scene: one still per mark() in the timeline, without captions.
   usage: node tools/video/stills.cjs <scene> <out dir>   -> step-01.jpg, step-02.jpg, ... */
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [scene, dir] = process.argv.slice(2); fs.mkdirSync(dir, { recursive:true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport:{ width:1920, height:1080 } });
  const nj = __dirname + '/narration/' + scene + '.json';
  if (fs.existsSync(nj)){ const cl = JSON.parse(fs.readFileSync(nj, 'utf8')).clips; if (cl) await p.addInitScript(d => { window.HCM_NARR = d; }, cl.map(c => c[1] - c[0])); }
  await p.goto('file://' + __dirname + '/' + scene + '.html?capture&still'); await p.waitForFunction(() => window.__ready);
  const marks = await p.evaluate(() => window.__marks);
  for (const [n, m] of Object.entries(marks)){
    await p.evaluate(m => { window.__stillHl = m.hl; window.__seek(m.t); }, m);
    const f = path.join(dir, 'step-' + String(n).padStart(2, '0') + '.png'); await p.screenshot({ path:f });
  }
  await b.close(); console.log(Object.keys(marks).length + ' stills');
})();

const { chromium } = require('playwright'); const { spawn } = require('child_process');
(async () => {
  const FPS = 30, out = process.argv[3];   /* usage: node tools/video/render.cjs <scene> <out.mp4> */
  const b = await chromium.launch(); const p = await b.newPage({ viewport:{ width:1920, height:1080 } });
  const nj = __dirname + '/narration/' + process.argv[2] + '.json';
  if (require('fs').existsSync(nj)){ const cl = JSON.parse(require('fs').readFileSync(nj, 'utf8')).clips; if (cl) await p.addInitScript(d => { window.HCM_NARR = d; }, cl.map(c => c[1] - c[0])); }
  await p.goto('file://' + __dirname + '/' + process.argv[2] + '.html?capture'); await p.waitForFunction(() => window.__ready);
  const dur = await p.evaluate(() => window.__dur), n = Math.ceil(dur * FPS);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-r', String(FPS), out], { stdio:['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < n; i++){
    await p.evaluate(t => window.__seek(t), i / FPS);
    const buf = await p.screenshot({ type:'jpeg', quality:95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 300 === 0) console.log('frame', i, 'of', n);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
  const segs = await p.evaluate(() => window.__segs || null);
  if (segs) require('fs').writeFileSync(out.replace(/\.mp4$/, '.segs.json'), JSON.stringify(segs));
  await b.close(); console.log('done', dur.toFixed(1) + 's');
})();

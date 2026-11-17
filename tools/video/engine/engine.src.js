/* HCM Academy explainer video kit. A scene file builds its screens with C.*, writes its
   timeline with the helpers below, then calls VIDEO.run().
   Preview: open the scene in a browser (space pauses). Render: tools/video/make.sh.
   Generated into engine.js by tools/video/engine/build.py (adds the icon set and header). */
(function(){
'use strict';
var SPRITE = __SPRITE__, HEAD = __HEAD__;
document.body.insertAdjacentHTML('afterbegin', SPRITE);

/* ---------- components (HTML builders) ---------- */
var esc = function(s){ return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); };
var I = function(n, st){ return '<svg class="i"' + (st ? ' style="' + st + '"' : '') + '><use href="#i-' + n + '"/></svg>'; };
var attrs = function(o){ var a = ''; if (o.id) a += ' id="' + o.id + '"'; if (o.if) a += ' data-if="' + o.if + '"'; if (o.cls) a += ' data-cls="' + o.cls + '"'; return a; };
var C = {
  I: I, esc: esc,
  page: function(id, inner, dark){ return '<section class="scr ' + (dark ? 'dark' : 'light') + '" data-screen="' + id + '"><div class="ghs"></div>' + inner + '</section>'; },
  title: function(t, o){ o = o || {}; return '<div class="ptitle"' + attrs(o) + '>' + I('back') + esc(t) + '</div>' + (o.sub ? '<div class="psub">' + esc(o.sub) + '</div>' : ''); },
  btns: function(list){ return '<div class="fbtns">' + list.map(function(b){
      return '<span class="btn ' + (b.cta ? 'cta' + (b.off ? ' off' : '') : 'sec') + '"' + attrs(b) + (b.off ? ' data-cls="' + b.off + ':on"' : '') + '>' + esc(b.t) + (b.down ? I('down', 'width:16px;height:16px;margin-left:6px') : '') + '</span>'; }).join('') + '</div>'; },
  pban: function(p, o){ o = o || {}; return '<div class="pban"' + attrs(o) + '><div class="av" style="background:' + p.c + '">' + p.ini + '</div><div><b>' + esc(p.name) + '</b><small>' + esc(p.sub) + '</small></div></div>'; },
  field: function(o){ /* {id,label,bind,ph,icon,value,ro,dd:[{id,t,s}],ddIf,focus,hint,w} */
    var inner = o.ro !== undefined || o.value !== undefined ? '<span class="grow">' + esc(o.ro !== undefined ? o.ro : o.value) + '</span>'
      : '<span class="grow"><span data-bind="' + o.bind + '"></span><span class="caret" data-caret="' + o.bind + '"></span><span class="ph" data-ph="' + o.bind + '">' + esc(o.ph || '') + '</span></span>';
    var lead = o.icon === 'search' ? I('search') : '', trail = o.icon && o.icon !== 'search' ? I(o.icon) : '';
    var dd = o.dd ? '<div class="dd"' + (o.ddIf ? ' data-if="' + o.ddIf + '"' : '') + '>' + o.dd.map(function(x){ return '<div' + (x.id ? ' id="' + x.id + '" class="hov"' : '') + '>' + esc(x.t) + (x.s ? '<small>' + esc(x.s) + '</small>' : '') + '</div>'; }).join('') + '</div>' : '';
    return '<div class="fw"' + (o.wrapIf ? ' data-if="' + o.wrapIf + '"' : '') + (o.w ? ' style="width:' + o.w + 'px"' : '') + '>' + (o.label ? '<p class="flabel">' + esc(o.label) + '</p>' : '') +
      '<div class="field' + (o.ro !== undefined ? ' ro' : '') + '"' + (o.id ? ' id="' + o.id + '"' : '') + (o.bind ? ' data-focus="' + o.bind + '"' : '') + (o.focusIf ? ' data-cls="' + o.focusIf + ':focus"' : '') + '>' + lead + inner + trail + '</div>' + dd +
      (o.hint ? '<p class="hint">' + esc(o.hint) + '</p>' : '') + '</div>'; },
  sec: function(o){ /* {id,n,title,sum,done,open,later,body} flags */
    return '<div class="sec" id="' + o.id + '"' + (o.later ? ' data-cls="' + o.later + ':later"' : '') + '>' +
      '<div class="sh"><span class="n" data-if="!' + o.done + '">' + o.n + '</span><span class="n ok" data-if="' + o.done + '">' + I('check') + '</span><h3>' + esc(o.title) + '</h3>' +
      '<span class="sum" data-if="' + o.done + '">' + esc(o.sum || '') + '</span><span class="edit" data-if="' + o.done + '">Edit</span></div>' +
      '<div class="sb" data-if="' + o.open + '">' + o.body + '</div></div>'; },
  cont: function(id){ return '<div style="margin-top:20px"><span class="btn cta" id="' + id + '">Continue</span></div>'; },
  table: function(o){ /* {id, cols, head, rows:[{id, cells, cls, if}]} */
    var tr = function(cells, extra){ return '<div class="tr' + (extra || '') + '" style="grid-template-columns:' + o.cols + '">' + cells.map(function(c){ return '<span>' + c + '</span>'; }).join('') + '</div>'; };
    return '<div class="otab"' + (o.id ? ' id="' + o.id + '"' : '') + (o.w ? ' style="width:' + o.w + 'px"' : '') + '>' + tr(o.head.map(esc), ' hd') +
      o.rows.map(function(r){ var h = tr(r.cells); return h.replace('<div class="tr"', '<div class="tr"' + (r.id ? ' id="' + r.id + '"' : '') + (r.cls ? ' data-cls="' + r.cls + '"' : '') + (r.if ? ' data-if="' + r.if + '"' : '')); }).join('') + '</div>'; },
  chk: function(o){ return '<div class="chk"' + (o.id ? ' id="' + o.id + '"' : '') + ' data-cls="' + o.flag + ':on"><span class="cb">' + I('check') + '</span>' + esc(o.t) + '</div>'; },
  card: function(o){ /* {id, theme:'dark'|'cream', eyebrow, h:'big'|'mid', pre, em, post, p, items, meta, extra, logo} */
    var h = o.h === 'big' ? 'h1' : 'h2';
    return '<div class="card' + (o.theme === 'cream' ? ' pc' : '') + '" id="' + o.id + '"><img class="vmark" src="' + VIDEO.root + 'assets/img/vu-v-icon.png" alt="" />' +
      '<div class="in"' + (o.top ? ' style="top:' + o.top + 'px"' : '') + '><div class="e">' + esc(o.eyebrow) + '</div><' + h + '>' + esc(o.pre || '') + (o.em ? '<em>' + esc(o.em) + '</em>' : '') + esc(o.post || '') + '</' + h + '>' +
      (o.p ? '<p>' + esc(o.p) + '</p>' : '') + (o.items ? '<ol>' + o.items.map(function(x){ return '<li>' + esc(x) + '</li>'; }).join('') + '</ol>' : '') + (o.rule ? '<div class="rule"></div>' : '') + (o.inner || '') + '</div>' +
      (o.extra || '') + (o.theme === 'cream' ? '' : '<img class="lock" src="' + VIDEO.root + 'assets/img/vu-lockup-white.png" alt="" />') + (o.meta ? '<div class="meta">' + esc(o.meta) + '</div>' : '') + '</div>'; },
  /* process board: a step rail and one page per step, for steps that happen outside Oracle */
  board: function(o){ /* {id, steps:[labels], pages:[{eyebrow, pre, em, post, lines:[], art}]} */
    var rail = '<ol class="rail">' + o.steps.map(function(l, i){ var k = i + 1; return '<li data-cls="st-' + k + ':on,dn-' + k + ':done"><span class="rn"><i>' + k + '</i>' + I('check') + '</span>' + esc(l) + '</li>'; }).join('') + '</ol>';
    var pages = o.pages.map(function(pg, i){ var k = i + 1;
      return '<div class="bpage" data-if="st-' + k + '"><div class="btext"><div class="e">Step ' + k + ' of ' + o.steps.length + '</div><h2>' + esc(pg.pre || '') + (pg.em ? '<em>' + esc(pg.em) + '</em>' : '') + esc(pg.post || '') + '</h2>' +
        (pg.lines || []).map(function(x, j){ return '<p data-in="st-' + k + '" data-d="' + (.25 + j * .35).toFixed(2) + '">' + esc(x) + '</p>'; }).join('') + '</div>' +
        '<div class="bart" data-in="st-' + k + '" data-d=".15">' + (pg.art || '') + '</div></div>'; }).join('');
    return '<div class="card pc board" id="' + o.id + '">' + rail + pages + '</div>'; },
  doc: function(o){ /* illustration of a document: {kicker, title, rows:[[k,v,flag?]], foot, id} */
    return '<div class="art doc"' + (o.id ? ' id="' + o.id + '"' : '') + '><div class="dk">' + esc(o.kicker || '') + '</div><b>' + esc(o.title) + '</b>' +
      (o.rows || []).map(function(r){ return '<div class="dr"' + (r[2] ? ' data-in="' + r[2] + '" data-d="' + (r[3] || 0) + '"' : '') + '><span>' + esc(r[0]) + '</span><span>' + esc(r[1]) + '</span></div>'; }).join('') +
      (o.foot ? '<div class="df">' + o.foot + '</div>' : '') + '</div>'; },
  home: function(o){ /* Vanderbilt home page, Me and Our Workforce tabs. o.toast, o.notif */
    o = o || {};
    var qa = function(list, id){ return '<ul class="qa"' + (id ? ' id="' + id + '"' : '') + '>' + list.map(function(x){ return '<li' + (x[2] ? ' id="' + x[2] + '"' : '') + '>' + (x[0] ? I(x[0]) : '') + '<span>' + esc(x[1]) + '</span></li>'; }).join('') + '</ul>'; };
    var tile = function(x){ return '<div class="tile"' + (x[2] ? ' id="' + x[2] + '"' : '') + '>' + I(x[0]) + x[1] + '</div>'; };
    return C.page('home',
      '<h1 class="greet">Good afternoon, Jordan Avery</h1>' +
      '<nav class="tabs"><span data-cls="!tab-wf:on">Me</span><span>My Team</span><span id="tab-wf" data-cls="tab-wf:on">Our Workforce</span><span>Help Desk</span><span>Reporting</span><span>Knowledge</span><span>Tools</span><span>Others</span></nav>' +
      '<div class="lbl" style="left:284px">Quick Actions</div><div class="lbl" style="left:575px">Apps</div>' +
      '<div data-if="!tab-wf">' + qa([['doc', 'My Payslips'], ['cal', 'Add Absence'], ['calc', 'Absence Balance'], ['calclock', 'Existing Absences'], ['bank', 'Payroll Payment Methods'], ['walk', 'Grow'], ['skill', 'Skills and Qualifications'], ['book', 'Current Learning'], ['search', 'Search Jobs'], ['person', 'Personal Details']]) +
      '<div class="apps">' + [['clock', 'UKG (Kronos)<br>Timesheets'], ['act', 'My Activity<br>Center'], ['net', 'Connections'], ['compass', 'Journeys'], ['person', 'Personal<br>Information'], ['bank', 'Pay'], ['absence', 'Absences'], ['plane', 'Concur Travel'], ['play', 'Learning Hub'], ['gift', 'Benefits'], ['chart', 'Fidelity<br>Investments'], ['jobs', 'Internal Jobs'], ['id', ''], ['updown', ''], ['wallet', ''], ['help', '']].map(tile).join('') + '</div></div>' +
      '<div data-if="tab-wf">' + qa([['person', 'Employment Info', 'qa-ei'], ['person', 'Costing for Persons', 'qa-cost'], ['skill', 'Change Assignment', 'qa-ca'], ['wallet', 'Individual Compensation'], ['wallet', 'Change Salary'], ['team', 'Add Assignment'], ['person', 'Hire an Employee'], ['skill', 'Pending Workers', 'qa-pending'], ['skill', 'Create Work Relationship'], ['net', 'Areas of Responsibility'], [null, 'Show More', 'qa-more']], 'qa-wf') +
      '<div class="apps five">' + [['hire', 'Hiring', 'app-hiring'], ['compass', 'Journeys'], ['skill', 'Person<br>Management'], ['skill', 'HCM Activity<br>Center'], ['absence', 'Absences'], ['wallet', 'Compensation'], ['goal', 'Goals'], ['person', 'Profiles'], ['updown', 'Career<br>Development'], ['review', 'Talent Review'], ['team', 'Succession Plans'], ['team', 'Talent Pools'], ['net', 'Workforce<br>Structures', 'app-ws'], ['help', 'Journeys Setup'], ['calc', 'Payroll'], ['team', 'Mass Updates'], ['updown', 'Data Exchange']].map(tile).join('') + '<div class="tile plus">' + I('plus') + '</div></div></div>' +
      '<div class="pill">' + I('info') + I('dots') + '</div>' +
      '<svg class="bubble" viewBox="0 0 52 44"><path d="M4 4h34a4 4 0 0 1 4 4v18a4 4 0 0 1-4 4H16l-8 7v-7H4a4 4 0 0 1-4-4V8a4 4 0 0 1 4-4z" fill="#fff"/><text x="21" y="24" text-anchor="middle" font-family="Libre Caslon Display" font-size="20" fill="#B4924A">V</text><circle cx="40" cy="30" r="11" fill="#fff" stroke="#CFAE70" stroke-width="1.5"/><circle cx="36" cy="30" r="1.6" fill="#B4924A"/><circle cx="41" cy="30" r="1.6" fill="#B4924A"/></svg>' +
      (o.toast ? '<div class="toast" data-if="toast">' + I('checkc') + '<span>' + esc(o.toast) + '</span></div>' : '') +
      (o.notif ? '<div class="notif" data-if="notif"><h4>Notifications <span>Show All</span></h4><div class="it new" id="n-item"><div class="dot">' + I('doc') + '</div><div><b>' + esc(o.notif) + '</b><small>Submitted by you · Just now</small></div></div>' +
        '<div class="it"><div class="dot">' + I('cal') + '</div><div><b>Absence request: Sam Patel</b><small>Approved · Yesterday</small></div></div></div>' : ''), true);
  }
};
window.C = C;

/* ---------- timeline ---------- */
var EV = [], T = 0, SEGS = [], MARKS = {}, LEAD = .2, NARR = window.HCM_NARR || [];
function ev(o){ o.t = T; EV.push(o); return o; }
var G = {
  wait: function(d){ T += d; },
  scene: function(n){ ev({ k:'scene', v:n }); },
  flag: function(f, on){ ev({ k:'flag', f:f, on:on !== false }); },
  val: function(key, v){ ev({ k:'val', key:key, v:v }); },
  fset: function(key){ ev({ k:'focus', v:key }); },
  move: function(sel, d){ ev({ k:'move', sel:sel, d:d || 1 }); T += d || 1; },
  click: function(after){ ev({ k:'click', d:.5 }); T += .22; if (after) after(); T += .2; },
  type: function(key, text, d){ ev({ k:'type', key:key, text:text, d:d || Math.max(.5, text.length * .07) }); T += d || Math.max(.5, text.length * .07); },
  camTo: function(sel, s, d, dx, dy){ ev({ k:'cam', sel:sel, s:s || 1, d:d === undefined ? .9 : d, dx:dx || 0, dy:dy || 0 }); },
  cap: function(n, text){ ev({ k:'cap', n:n, text:text }); },
  hl: function(sel){ ev({ k:'hl', sel:sel }); },
  card: function(name, on){ ev({ k:'card', name:name, on:on !== false }); },
  seg: function(){ SEGS.push(T + LEAD); },
  /* hold until this segment's narration has played (less `early` seconds) */
  hold: function(early){ var i = SEGS.length - 1, n = NARR[i] || 0, end = SEGS[i] + n - (early || 0); if (n && T < end) T = end; },
  capS: function(n, text){ G.seg(); G.cap(n, text); },
  stepTo: function(k, n){ for (var i = 1; i <= n; i++){ G.flag('st-' + i, i === k); G.flag('dn-' + i, i < k); } },
  mark: function(n, sel){ MARKS[n] = { t:T - .05, hl:sel || null }; },
  now: function(){ return T; }
};
Object.keys(G).forEach(function(k){ window[k] = G[k]; });

/* ---------- state and drawing ---------- */
var W = 1440, H = 1000, OUT = 1920 / 1440, STEPS = 0;
function clamp(x){ return x < 0 ? 0 : x > 1 ? 1 : x; }
function ease(x){ return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; }
var HOME = { x:W / 2, y:405 };
function compute(t){
  var s = { scene:null, flags:{}, flagT:{}, vals:{}, focus:null, cur:{ x:760, y:560 }, click:null, cam:{ x:HOME.x, y:HOME.y, s:1 }, cap:null, hl:null, cards:{} };
  for (var i = 0; i < EV.length; i++){
    var e = EV[i]; if (e.t > t) break;
    var p = e.d ? clamp((t - e.t) / e.d) : 1;
    switch (e.k){
      case 'scene': s.scene = e.v; break;
      case 'flag': if (e.on && !s.flags[e.f]) s.flagT[e.f] = e.t; s.flags[e.f] = e.on; break;
      case 'val': s.vals[e.key] = e.v; break;
      case 'focus': s.focus = e.v; break;
      case 'move': if (e.to){ var q = ease(p), f = s.cur; s.cur = { x:f.x + (e.to.x - f.x) * q, y:f.y + (e.to.y - f.y) * q }; } break;
      case 'click': s.click = { x:s.cur.x, y:s.cur.y, p:p }; break;
      case 'type': s.vals[e.key] = e.text.slice(0, Math.round(e.text.length * p)); s.focus = e.key; break;
      case 'cam':
        var tg = e.sel ? e.fc : HOME;
        if (tg){ var q2 = ease(p), c = s.cam; s.cam = { x:c.x + (tg.x + e.dx - c.x) * q2, y:c.y + (tg.y + e.dy - c.y) * q2, s:c.s + (e.s - c.s) * q2 }; }
        break;
      case 'cap': s.cap = e.text ? { n:e.n, text:e.text, t0:e.t } : null; break;
      case 'hl': s.hl = e.sel ? { sel:e.sel, t0:e.t } : null; break;
      case 'card': s.cards[e.name] = { on:e.on, t0:e.t }; break;
    }
  }
  return s;
}
var stage, cam, screens, active, cur, rip, hlb, capEl, CARDS;
function q(sel){ return (active && active.querySelector(sel)) || document.querySelector(sel); }
function on(s, expr){ return expr.split(' ').every(function(x){ return x.charAt(0) === '!' ? !s.flags[x.slice(1)] : !!s.flags[x]; }); }
function rectOf(el){ var c = cam.getBoundingClientRect(), r = el.getBoundingClientRect(), k = c.width / W; return { x:(r.left - c.left) / k, y:(r.top - c.top) / k, w:r.width / k, h:r.height / k }; }
function center(el){ var r = rectOf(el); return { x:r.x + r.w / 2, y:r.y + r.h / 2 }; }
function draw(s, t){
  screens.forEach(function(sc){ var me = sc.dataset.screen === s.scene; sc.hidden = !me; if (me) active = sc; });
  document.querySelectorAll('[data-if]').forEach(function(el){ el.hidden = !on(s, el.getAttribute('data-if')); });
  document.querySelectorAll('[data-cls]').forEach(function(el){ el.getAttribute('data-cls').split(',').forEach(function(pair){ var a = pair.split(':'); el.classList.toggle(a[1], on(s, a[0])); }); });
  document.querySelectorAll('[data-in]').forEach(function(el){   /* reveal: fade and rise after its flag turns on */
    var f = el.dataset.in, t0 = s.flagT[f], d = +(el.dataset.d || 0), p = s.flags[f] && t0 !== undefined ? ease(clamp((t - t0 - d) / .5)) : 0;
    el.style.opacity = p.toFixed(3); el.style.transform = 'translateY(' + (24 * (1 - p)).toFixed(1) + 'px)';
  });
  document.querySelectorAll('[data-bind]').forEach(function(el){ el.textContent = s.vals[el.dataset.bind] || ''; });
  document.querySelectorAll('[data-ph]').forEach(function(el){ el.hidden = !!s.vals[el.dataset.ph] || s.focus === el.dataset.ph; });
  document.querySelectorAll('[data-caret]').forEach(function(el){ el.hidden = s.focus !== el.dataset.caret; });
  document.querySelectorAll('[data-focus]').forEach(function(el){ el.classList.toggle('focus', s.focus === el.dataset.focus); });
  var S = OUT * s.cam.s, tx = 960 - s.cam.x * S, ty = 540 - s.cam.y * S;
  tx = Math.min(0, Math.max(1920 - W * S, tx)); ty = Math.min(0, Math.max(1080 - H * S, ty));
  cam.style.transform = 'translate(' + tx.toFixed(2) + 'px,' + ty.toFixed(2) + 'px) scale(' + S.toFixed(4) + ')';
  var inv = 1 / s.cam.s;
  cur.style.transform = 'translate(' + (s.cur.x - 4 * inv).toFixed(2) + 'px,' + (s.cur.y - 2.5 * inv).toFixed(2) + 'px) scale(' + inv.toFixed(4) + ')';
  cur.style.display = s.scene ? '' : 'none';
  if (s.click && s.click.p < 1){
    var r = (8 + 26 * ease(s.click.p)) * inv;
    rip.hidden = false; rip.style.opacity = (1 - s.click.p).toFixed(3);
    rip.style.left = (s.click.x - r) + 'px'; rip.style.top = (s.click.y - r) + 'px'; rip.style.width = rip.style.height = (2 * r) + 'px'; rip.style.borderWidth = (3 * inv) + 'px';
  } else rip.hidden = true;
  var STILL = window.__stillHl, target = STILL ? q(STILL) : s.hl && q(s.hl.sel);
  if (target && target.offsetParent){
    var b = rectOf(target), pad = 6, a = STILL ? 1 : clamp((t - s.hl.t0) / .3);
    hlb.hidden = false; hlb.style.opacity = a;
    hlb.style.left = (b.x - pad) + 'px'; hlb.style.top = (b.y - pad) + 'px'; hlb.style.width = (b.w + 2 * pad) + 'px'; hlb.style.height = (b.h + 2 * pad) + 'px'; hlb.style.borderWidth = (3 * inv) + 'px';
  } else hlb.hidden = true;
  if (s.cap && !/still/.test(location.search)){
    var ca = clamp((t - s.cap.t0) / .35);
    capEl.hidden = false; capEl.style.opacity = ease(ca); capEl.style.transform = 'translateY(' + (16 * (1 - ease(ca))).toFixed(1) + 'px)';
    capEl.firstChild.textContent = 'Step ' + s.cap.n + ' of ' + STEPS; capEl.lastChild.textContent = s.cap.text;
  } else capEl.hidden = true;
  var anyCard = false;
  CARDS.forEach(function(n){
    var c = s.cards[n], el = document.getElementById(n), o = 0;
    if (c){ var p = clamp((t - c.t0) / .6); o = c.on ? (c.t0 === 0 ? 1 : ease(p)) : 1 - ease(p); if (c.on) anyCard = true; }
    el.style.opacity = o; el.hidden = o <= 0;
  });
  document.getElementById('tag').hidden = anyCard;
}
function prime(){
  EV.forEach(function(e){
    if ((e.k === 'move' || (e.k === 'cam' && e.sel)) && !e.to && !e.fc){
      draw(compute(e.t + 1e-4), e.t);
      var el = q(e.sel);
      if (!el || !el.offsetParent) throw new Error('not visible at ' + e.t.toFixed(2) + 's: ' + e.sel);
      if (e.k === 'move'){ var r = rectOf(el); e.to = { x:r.x + Math.min(r.w / 2, 60), y:r.y + r.h / 2 }; if (r.w < 120) e.to.x = r.x + r.w / 2; }
      else e.fc = center(el);
    }
  });
}
function seek(t){ draw(compute(t), t); }

window.VIDEO = {
  root: '../../',
  set: function(o){ if (o.H) H = o.H; if (o.steps) STEPS = o.steps; },
  add: function(html){ document.getElementById('cam').insertAdjacentHTML('beforeend', html); },
  addCard: function(html){ document.getElementById('stage').insertAdjacentHTML('beforeend', html); },
  run: function(){
    stage = document.getElementById('stage'); cam = document.getElementById('cam');
    cam.style.height = H + 'px';
    document.querySelectorAll('.ghs').forEach(function(h){ h.outerHTML = HEAD; });
    cam.insertAdjacentHTML('beforeend', '<div id="hl" hidden></div><div id="ripple" hidden></div><svg id="cursor" viewBox="0 0 30 30"><path d="M4 2.5v21l5.4-5 3.6 8.2 3.6-1.6-3.6-8h7.5z" fill="#161513" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"/></svg>');
    stage.insertAdjacentHTML('beforeend', '<div class="cap" id="cap" hidden><div class="e"></div><div class="t"></div></div><div class="tag" id="tag">Training simulation <b>·</b> fictional names</div>');
    /* cards sit above the caption */
    [].slice.call(stage.querySelectorAll('.card')).forEach(function(c){ stage.appendChild(c); });
    screens = [].slice.call(document.querySelectorAll('[data-screen]'));
    cur = document.getElementById('cursor'); rip = document.getElementById('ripple'); hlb = document.getElementById('hl'); capEl = document.getElementById('cap');
    CARDS = [].map.call(document.querySelectorAll('.card'), function(c){ return c.id; });
    var DUR = T, capture = /capture/.test(location.search);
    Promise.all([document.fonts.ready].concat([].slice.call(document.images).map(function(im){ return im.complete ? 0 : new Promise(function(r){ im.onload = im.onerror = r; }); }))).then(function(){
      prime();
      window.__seek = seek; window.__dur = DUR; window.__segs = SEGS; window.__marks = MARKS; window.__ready = true;
      if (!capture){
        var fit = function(){ var k = Math.min(innerWidth / 1920, innerHeight / 1080); stage.style.transform = 'scale(' + k + ')'; stage.style.transformOrigin = '0 0'; };
        fit(); addEventListener('resize', fit);
        var t0 = performance.now(), paused = false, pt = 0;
        addEventListener('keydown', function(e){ if (e.code === 'Space'){ paused = !paused; if (!paused) t0 = performance.now() - pt * 1000; } });
        (function loop(){ if (!paused){ pt = ((performance.now() - t0) / 1000) % (DUR + 1); seek(pt); } requestAnimationFrame(loop); })();
      }
    }).catch(function(e){ window.__error = String(e); throw e; });
  }
};
})();

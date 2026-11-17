/* Generated from engine.src.js by build.py. Edit the source, then rebuild. */
/* HCM Academy explainer video kit. A scene file builds its screens with C.*, writes its
   timeline with the helpers below, then calls VIDEO.run().
   Preview: open the scene in a browser (space pauses). Render: tools/video/make.sh.
   Generated into engine.js by tools/video/engine/build.py (adds the icon set and header). */
(function(){
'use strict';
var SPRITE = "<svg width=\"0\" height=\"0\" style=\"position:absolute\">\n <defs>\n  <symbol id=\"i-menu\" viewBox=\"0 0 24 24\"><path d=\"M3 6h18M3 12h18M3 18h18\"/></symbol>\n  <symbol id=\"i-home\" viewBox=\"0 0 24 24\"><path d=\"M3.5 11 12 3.5 20.5 11v9.5h-17z\"/></symbol>\n  <symbol id=\"i-star\" viewBox=\"0 0 24 24\"><path d=\"m12 3 2.7 5.6 6.1.8-4.5 4.2 1.1 6.1L12 16.8l-5.4 2.9 1.1-6.1-4.5-4.2 6.1-.8z\"/></symbol>\n  <symbol id=\"i-flag\" viewBox=\"0 0 24 24\"><path d=\"M5 21V4h14l-2.5 4.5L19 13H5\"/></symbol>\n  <symbol id=\"i-bell\" viewBox=\"0 0 24 24\"><path d=\"M6 17V11a6 6 0 0 1 12 0v6l1.5 2h-15zM10 21h4\"/></symbol>\n  <symbol id=\"i-search\" viewBox=\"0 0 24 24\"><circle cx=\"10.5\" cy=\"10.5\" r=\"6.5\"/><path d=\"m15.5 15.5 5 5\"/></symbol>\n  <symbol id=\"i-doc\" viewBox=\"0 0 24 24\"><rect x=\"5\" y=\"3\" width=\"14\" height=\"18\" rx=\"1\"/><path d=\"M8 7h8M8 10h8M8 13h8M8 16h5\"/></symbol>\n  <symbol id=\"i-cal\" viewBox=\"0 0 24 24\"><rect x=\"3.5\" y=\"5\" width=\"17\" height=\"15.5\" rx=\"1\"/><path d=\"M3.5 9.5h17M8 3v4M16 3v4M7 13h2M11 13h2M15 13h2M7 16.5h2M11 16.5h2M15 16.5h2\"/></symbol>\n  <symbol id=\"i-calc\" viewBox=\"0 0 24 24\"><rect x=\"5\" y=\"3\" width=\"14\" height=\"18\" rx=\"1\"/><path d=\"M8 7h8M8 11h2M11 11h2M14 11h2M8 14h2M11 14h2M14 14h2M8 17h2M11 17h2M14 17h2\"/></symbol>\n  <symbol id=\"i-calclock\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"4\" width=\"15\" height=\"13\" rx=\"1\"/><path d=\"M3 8h15M6 11h9M6 14h5\"/><circle cx=\"18\" cy=\"17.5\" r=\"3.5\"/><path d=\"M18 16v1.6l1 .8\"/></symbol>\n  <symbol id=\"i-cal2\" viewBox=\"0 0 24 24\"><rect x=\"3.5\" y=\"4.5\" width=\"17\" height=\"15.5\" rx=\"1\"/><path d=\"M3.5 9h17M7 12.5h4M7 15.5h7\"/></symbol>\n  <symbol id=\"i-bank\" viewBox=\"0 0 24 24\"><path d=\"M3 9.5 12 4l9 5.5zM5 11v7M9.5 11v7M14.5 11v7M19 11v7M3 20.5h18\"/></symbol>\n  <symbol id=\"i-walk\" viewBox=\"0 0 24 24\"><circle cx=\"11\" cy=\"4.5\" r=\"2\"/><path d=\"m8 21 2.5-6 2.5 2 1 4M10.5 15l.5-6.5 3 3 3 1M11 8.5 7.5 11\"/><path d=\"M16 20h5v-4\"/></symbol>\n  <symbol id=\"i-skill\" viewBox=\"0 0 24 24\"><circle cx=\"8\" cy=\"5.5\" r=\"2.2\"/><path d=\"M4 21v-8a4 4 0 0 1 8 0v1M14 17l6-9M17 18l4-4\"/></symbol>\n  <symbol id=\"i-book\" viewBox=\"0 0 24 24\"><rect x=\"5\" y=\"4\" width=\"13\" height=\"16\" rx=\"1\"/><path d=\"M8 4V2.5h13V18h-3M8 8h7M8 11h7M8 14h7\"/></symbol>\n  <symbol id=\"i-person\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"7\" r=\"3.5\"/><path d=\"M5 21v-3.5A5.5 5.5 0 0 1 10.5 12h3a5.5 5.5 0 0 1 5.5 5.5V21z\"/></symbol>\n  <symbol id=\"i-cloud\" viewBox=\"0 0 24 24\"><path d=\"M7 17H6a4 4 0 0 1-.5-8A6 6 0 0 1 17 8a4.5 4.5 0 0 1 1 9h-1\"/><rect x=\"9\" y=\"12\" width=\"6\" height=\"9\" rx=\"1\"/><path d=\"M10.5 15h3M10.5 18h3\"/></symbol>\n  <symbol id=\"i-id\" viewBox=\"0 0 24 24\"><rect x=\"5\" y=\"3\" width=\"14\" height=\"18\" rx=\"1\"/><circle cx=\"12\" cy=\"9\" r=\"2.2\"/><path d=\"M8.5 15a3.5 3.5 0 0 1 7 0M8 18h8\"/></symbol>\n  <symbol id=\"i-clock\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M12 7v5.5h4\"/></symbol>\n  <symbol id=\"i-act\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"9\" r=\"3\"/><path d=\"M7 21v-4a5 5 0 0 1 10 0v4M5 7a8 8 0 0 1 13-3.5M19 11a8 8 0 0 1-1 4\"/></symbol>\n  <symbol id=\"i-net\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"3\"/><circle cx=\"4\" cy=\"4\" r=\"1.6\"/><circle cx=\"20\" cy=\"4\" r=\"1.6\"/><circle cx=\"4\" cy=\"20\" r=\"1.6\"/><circle cx=\"20\" cy=\"20\" r=\"1.6\"/><path d=\"m5.2 5.2 4.6 4.6M18.8 5.2l-4.6 4.6M5.2 18.8l4.6-4.6M18.8 18.8l-4.6-4.6\"/></symbol>\n  <symbol id=\"i-compass\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"m15.5 8.5-2 5-5 2 2-5z\"/></symbol>\n  <symbol id=\"i-absence\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"6\" r=\"3\" stroke-dasharray=\"2 2\"/><path d=\"M6 21v-5a6 6 0 0 1 12 0v5z\" stroke-dasharray=\"2 2\"/></symbol>\n  <symbol id=\"i-plane\" viewBox=\"0 0 24 24\"><path d=\"m3 13 5 1 3-3-6-4 2-1 8 2 3-3a1.5 1.5 0 0 1 2 2l-3 3 2 8-1 2-4-6-3 3 1 5-1.5 1-2.5-4.5L2.5 14.5z\"/></symbol>\n  <symbol id=\"i-play\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M10 8.5v7l5.5-3.5z\"/></symbol>\n  <symbol id=\"i-gift\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"9\" width=\"14\" height=\"12\"/><path d=\"M10 9v12M3 13h14M10 9C8 5 5 5 5 7s3 2 5 2c2 0 5 0 5-2s-3-2-5 2M15 15h6v6h-6zM16 18l1.5-1.5 1.5 3 1.5-1.5\"/></symbol>\n  <symbol id=\"i-chart\" viewBox=\"0 0 24 24\"><path d=\"M4 21v-6h4v6zM10 21v-9h4v9zM16 21V9h4v12zM4 11l6-5 4 2 6-5M17 3h3v3\"/></symbol>\n  <symbol id=\"i-jobs\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"7\" width=\"18\" height=\"13\" rx=\"1.5\"/><path d=\"M9 7V4h6v3\"/><circle cx=\"10\" cy=\"13.5\" r=\"3\"/><path d=\"m12 15.5 3 3\"/></symbol>\n  <symbol id=\"i-team\" viewBox=\"0 0 24 24\"><circle cx=\"7\" cy=\"6\" r=\"2.5\"/><circle cx=\"17\" cy=\"6\" r=\"2.5\"/><circle cx=\"12\" cy=\"5\" r=\"2.5\"/><path d=\"M3 20v-5a4 4 0 0 1 4-4M21 20v-5a4 4 0 0 0-4-4M8 20v-5a4 4 0 0 1 8 0v5z\"/></symbol>\n  <symbol id=\"i-hire\" viewBox=\"0 0 24 24\"><circle cx=\"7\" cy=\"5\" r=\"2.5\"/><circle cx=\"16\" cy=\"5\" r=\"2.5\"/><path d=\"M3 18v-5a4 4 0 0 1 8 0\"/><circle cx=\"16\" cy=\"13\" r=\"3.5\"/><path d=\"m18.5 15.5 3 4\"/></symbol>\n  <symbol id=\"i-review\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"3\" width=\"8\" height=\"8\"/><rect x=\"13\" y=\"3\" width=\"8\" height=\"8\"/><rect x=\"3\" y=\"13\" width=\"8\" height=\"8\"/><rect x=\"13\" y=\"13\" width=\"8\" height=\"8\"/><circle cx=\"7\" cy=\"6.5\" r=\"1.4\"/><circle cx=\"17\" cy=\"16.5\" r=\"1.4\"/></symbol>\n  <symbol id=\"i-badge\" viewBox=\"0 0 24 24\"><path d=\"m12 2 2.4 1.8 3-.2.9 2.9 2.5 1.7-1 2.8 1 2.8-2.5 1.7-.9 2.9-3-.2L12 22l-2.4-1.8-3 .2-.9-2.9-2.5-1.7 1-2.8-1-2.8 2.5-1.7.9-2.9 3 .2z\"/><path d=\"m8.5 12 2.5 2.5 4.5-5\"/></symbol>\n  <symbol id=\"i-goal\" viewBox=\"0 0 24 24\"><circle cx=\"6\" cy=\"6\" r=\"2.5\"/><path d=\"M2.5 19v-4a3.5 3.5 0 0 1 7 0v4z\"/><circle cx=\"16\" cy=\"12\" r=\"6\"/><circle cx=\"16\" cy=\"12\" r=\"2.5\"/></symbol>\n  <symbol id=\"i-plus\" viewBox=\"0 0 24 24\"><path d=\"M12 3v18M3 12h18\"/></symbol>\n  <symbol id=\"i-wallet\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"6\" width=\"18\" height=\"14\" rx=\"1.5\"/><path d=\"M5 6 17 3v3M14 13h7v4h-7a2 2 0 0 1 0-4z\"/></symbol>\n  <symbol id=\"i-help\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.3-1 .9-1 1.7M12 17h.01\"/></symbol>\n  <symbol id=\"i-updown\" viewBox=\"0 0 24 24\"><path d=\"M7 21V4M4 7l3-3 3 3M15 4h4M15 8h4M17 4v13M14 20h6\"/></symbol>\n  <symbol id=\"i-info\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M12 11v6M12 7.5h.01\"/></symbol>\n  <symbol id=\"i-dots\" viewBox=\"0 0 24 24\"><g fill=\"currentColor\" stroke=\"none\"><circle cx=\"6\" cy=\"6\" r=\"1.6\"/><circle cx=\"12\" cy=\"6\" r=\"1.6\"/><circle cx=\"18\" cy=\"6\" r=\"1.6\"/><circle cx=\"6\" cy=\"12\" r=\"1.6\"/><circle cx=\"12\" cy=\"12\" r=\"1.6\"/><circle cx=\"18\" cy=\"12\" r=\"1.6\"/><circle cx=\"6\" cy=\"18\" r=\"1.6\"/><circle cx=\"12\" cy=\"18\" r=\"1.6\"/><circle cx=\"18\" cy=\"18\" r=\"1.6\"/></g></symbol>\n  <symbol id=\"i-back\" viewBox=\"0 0 24 24\"><path d=\"m15 5-7 7 7 7\"/></symbol>\n  <symbol id=\"i-down\" viewBox=\"0 0 24 24\"><path d=\"m6 9 6 6 6-6\"/></symbol>\n  <symbol id=\"i-pen\" viewBox=\"0 0 24 24\"><path d=\"M4 20h4L19 9l-4-4L4 16zM13.5 6.5l4 4\"/></symbol>\n  <symbol id=\"i-check\" viewBox=\"0 0 24 24\"><path d=\"m5 12.5 4.5 4.5L19 7.5\"/></symbol>\n  <symbol id=\"i-checkc\" viewBox=\"0 0 24 24\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"m8 12.5 3 3 5-6\"/></symbol>\n  <symbol id=\"i-up\" viewBox=\"0 0 24 24\"><path d=\"M12 16V4M7 9l5-5 5 5M4 15v5h16v-5\"/></symbol>\n   <symbol id=\"i-kebab\" viewBox=\"0 0 24 24\"><g fill=\"currentColor\" stroke=\"none\"><circle cx=\"12\" cy=\"5\" r=\"1.8\"/><circle cx=\"12\" cy=\"12\" r=\"1.8\"/><circle cx=\"12\" cy=\"19\" r=\"1.8\"/></g></symbol>\n  <symbol id=\"i-clip\" viewBox=\"0 0 24 24\"><path d=\"M20 11.5 12 19.5a5 5 0 0 1-7-7l8.5-8.5a3.3 3.3 0 0 1 4.7 4.7L9.7 17.2a1.7 1.7 0 0 1-2.4-2.4L15 7\"/></symbol>\n  <symbol id=\"i-mail\" viewBox=\"0 0 24 24\"><rect x=\"3\" y=\"5\" width=\"18\" height=\"14\" rx=\"1.5\"/><path d=\"m3.5 6 8.5 7 8.5-7\"/></symbol>\n  <symbol id=\"i-filter\" viewBox=\"0 0 24 24\"><path d=\"M4 5h16l-6 7.5V19l-4 1.5v-8z\"/></symbol>\n  <symbol id=\"i-calcx\" viewBox=\"0 0 24 24\"><rect x=\"5\" y=\"3\" width=\"14\" height=\"18\" rx=\"1.5\"/><path d=\"M8 7h8v3H8zM8 14h2M11 14h2M14 14h2M8 17h2M11 17h2M14 17h2\"/></symbol>\n </defs>\n</svg>", HEAD = "\n <div class=\"gh\">\n  <svg class=\"i menu\"><use href=\"#i-menu\"/></svg>\n  <img class=\"logo\" src=\"../../assets/img/vu-lockup-white.png\" alt=\"\" />\n  <div class=\"search\"><svg class=\"i\"><use href=\"#i-search\"/></svg><span>Search for people and actions</span></div>\n  <svg class=\"i ic\" style=\"left:1236px\"><use href=\"#i-home\"/></svg>\n  <svg class=\"i ic\" style=\"left:1275px\"><use href=\"#i-star\"/></svg>\n  <svg class=\"i ic\" style=\"left:1313px\"><use href=\"#i-flag\"/></svg>\n  <svg class=\"i ic bell\" style=\"left:1352px\"><use href=\"#i-bell\"/></svg>\n  <div class=\"ava\">JA</div>\n </div>\n";
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
  /* Our Workforce > Show More, as on Vanderbilt's screens (groups in their order). ids: more-<slug of item> */
  more: function(){
    var G2 = [
      ['New Person', ['Add a Contingent Worker', 'Add a Nonworker', 'Add a Pending Worker', 'Hire an Employee', 'Pending Workers']],
      ['Document Records', ['Archived Document Records', 'Document Delivery Preferences', 'Document Records', 'Mass Download of Document Records']],
      ['Employment', ['Add Assignment', 'Additional Assignment Info', 'Additional Person Info', 'Allocate Checklists', 'Areas of Responsibility', 'Assigned Journeys', 'Assignment Flexfields Mapping', 'Cancel Work Relationship', 'Change Assignment', 'Change Legal Employer Dashboard', 'Change Location', 'Change Manager', 'Change Photo', 'Change Worker Type', 'Change Working Hours', 'Contact Info', 'Create Work Relationship', 'Direct Reports', 'Eligible Jobs', 'Employment Contracts', 'Employment Info', 'Employment Start Dates', 'Family and Emergency Contacts', 'HCM Professional Activity Center', 'Identification Info', 'Local and Global Transfer', 'Manage Job Offers', 'Manage User Account', 'Mass Legal Employer Change', 'Nudge Configuration', 'Person', 'Person Identifiers for External Applications', 'Personal Details', 'Promote', 'Seniority Dates', 'Share Data Access', 'Terminate Employment', 'Transfer', 'Work Relationship', 'Work Relationship Info', 'Workforce Modeling']],
      ['Compensation', ['Act as Proxy Manager', 'Administer Compensation', 'Administer Workers', 'Balance Definitions', 'Change Salary', 'Compensation Info', 'Derived Factors', 'Download Salaries', 'Elements', 'Eligibility Profiles', 'Fast Formulas', 'Grade Ladders', 'Grade Rates', 'Grades', 'Individual Compensation', 'Rate Definitions', 'Review Proposed Progressions and Salary Updates', 'Salary History', 'Simulate Salary Range', 'User-Defined Tables', 'Values Defined by Criteria', 'View Administration Reports', 'View Compensation History', 'View Generated Statements']],
      ['Learning', ['Learning Assignments', 'Organization New Recommendation Profile', 'Recommendation Profiles', 'Recommendations']],
      ['Journeys Setup', ['Category Security', 'Guided Journey', 'Journey Configurations', 'Journey Integrations', 'Journey Scheduled Allocations', 'Journey Templates', 'Journeys Setup', 'Task Groups', 'Task Library']],
      ['Hiring', ['Create Job Requisition', 'Job Offers', 'Job Requisitions', 'Manage Shared Interview Schedules', 'Recruiting Activity Center']],
      ['Time', ['Team Time Cards', 'View Published Schedule']],
      ['Workforce Structures', ['Area of Responsibility Templates', 'Collective Agreements', 'Disability Organizations', 'Divisions', 'Enterprise HCM Information', 'Grade Ladders', 'Grade Rates', 'Grades', 'Job Families', 'Jobs', 'Legislative Data Groups', 'Locations', 'Maintain Areas of Responsibility', 'Manage Departments - Oracle Search', 'Manage Organization Trees', 'Manage Position Trees', 'Manage Work Unit Trees', 'Manage Work Units', 'Positions', 'Reporting Establishments', 'Worker Unions']]
    ];
    var icon = function(g){ return { 'New Person':'person', 'Document Records':'cloud', 'Employment':'skill', 'Compensation':'wallet', 'Learning':'book', 'Journeys Setup':'doc', 'Hiring':'doc', 'Time':'doc', 'Workforce Structures':'net' }[g]; };
    var slug = function(t){ return t.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); };
    return C.page('more', '<nav class="tabs"><span>Me</span><span>My Team</span><span class="on">Our Workforce</span><span>Help Desk</span><span>Reporting</span><span>Knowledge</span><span>Tools</span><span>Others</span></nav>' +
      '<div class="more"><div class="less">&larr; Show Less</div>' + G2.map(function(g){
        return '<h4 id="more-g-' + slug(g[0]) + '">' + esc(g[0]) + '</h4><div class="mg">' + g[1].map(function(t){ return '<div class="mi" id="more-' + slug(g[0]) + '-' + slug(t) + '">' + I(icon(g[0])) + '<span>' + esc(t) + '</span></div>'; }).join('') + '</div>';
      }).join('') + '</div>', true);
  },
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
  /* click a field and type into it */
  fill: function(sel, bind, text, d){ G.move(sel, .85); G.click(function(){ G.fset(bind); }); G.type(bind, text, d); G.wait(.25); G.fset(null); },
  /* open a dropdown (flag dd) and choose an option */
  pick: function(sel, dd, opt, bind, value){ G.move(sel, .85); G.click(function(){ G.fset(null); G.flag(dd); }); G.wait(.3); G.move(opt, .55); G.click(function(){ G.flag(dd, false); G.val(bind, value); }); G.wait(.25); },
  /* click something, then run `after` (flags) */
  press: function(sel, after, d){ G.move(sel, d || .85); G.click(after); G.wait(.25); },
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

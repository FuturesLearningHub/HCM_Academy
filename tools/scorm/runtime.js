/* HCM Academy SCORM runtime. Runs in scorm.html, the package's launch page.
   - Finds the LMS API (SCORM 1.2 "API" or SCORM 2004 "API_1484_11") in a parent or opener window.
   - Shows the course in a frame. Every course page saves progress through window.HCM_SCORM
     (see bridge.js) instead of localStorage.
   - Keeps progress in cmi.suspend_data, the page in the location field, one objective per course,
     the pre-assessment and final assessment as objectives with scores, and each assessment answer
     as an interaction.
   - Reports passed (1.2) or completed and passed (2004), with the score, when the final assessment
     is passed. The final unlocks only when every course is complete.
   With no LMS, progress is kept in this browser and a notice says so. */
(function(){
  'use strict';
  var CFG = window.HCM_SCORM_CONFIG || { version: '1.2', slugs: [], title: 'HCM Academy' };
  var frame = document.getElementById('content'), note = document.getElementById('note');
  var started = Date.now(), lms = null, ended = false, LOCAL = 'hcm-scorm-state';

  /* ---------- find the LMS ---------- */
  function scan(win, name){
    for (var n = 0; win && n < 500; n++){
      try { if (win[name]) return win[name]; } catch(e){ return null; }
      if (!win.parent || win.parent === win) break;
      win = win.parent;
    }
    return null;
  }
  function find(){
    var order = CFG.version === '2004' ? ['API_1484_11', 'API'] : ['API', 'API_1484_11'];
    for (var i = 0; i < order.length; i++){
      var a = scan(window, order[i]);
      if (!a){ try { if (window.opener) a = scan(window.opener, order[i]); } catch(e){ a = null; } }
      if (a) return { api: a, v: order[i] === 'API' ? '1.2' : '2004' };
    }
    return null;
  }

  /* ---------- talk to it: one set of names, two data models ---------- */
  var F12 = { status: 'cmi.core.lesson_status', location: 'cmi.core.lesson_location', suspend: 'cmi.suspend_data',
              entry: 'cmi.core.entry', exit: 'cmi.core.exit', time: 'cmi.core.session_time',
              raw: 'cmi.core.score.raw', min: 'cmi.core.score.min', max: 'cmi.core.score.max' };
  var F04 = { completion: 'cmi.completion_status', success: 'cmi.success_status', location: 'cmi.location',
              suspend: 'cmi.suspend_data', entry: 'cmi.entry', exit: 'cmi.exit', time: 'cmi.session_time',
              raw: 'cmi.score.raw', min: 'cmi.score.min', max: 'cmi.score.max', scaled: 'cmi.score.scaled',
              progress: 'cmi.progress_measure' };
  function connect(found){
    var a = found.api, v12 = found.v === '1.2';
    var call = function(m12, m04, args){ try { return String(a[v12 ? m12 : m04].apply(a, args || [''])); } catch(e){ return 'false'; } };
    var o = {
      v: found.v, f: v12 ? F12 : F04,
      init: function(){ return call('LMSInitialize', 'Initialize') === 'true'; },
      get: function(k){ var r = call('LMSGetValue', 'GetValue', [k]); return r === 'undefined' || r === 'null' ? '' : r; },
      set: function(k, val){
        var ok = call('LMSSetValue', 'SetValue', [k, String(val)]) === 'true';
        if (!ok && window.console) console.warn('SCORM: could not set ' + k + ' (error ' + call('LMSGetLastError', 'GetLastError') + ')');
        return ok;
      },
      commit: function(){ return call('LMSCommit', 'Commit') === 'true'; },
      finish: function(){ return call('LMSFinish', 'Terminate') === 'true'; }
    };
    return o;
  }

  /* ---------- progress ---------- */
  var S = blank();
  function blank(){ return { p: 0, f: 0, d: [], t: 0, b: null, o: {} }; }
  function total(){ return S.t || CFG.slugs.length; }
  function load(text){
    var s = blank();
    try {
      var j = JSON.parse(text || '{}');
      s.p = j.p ? 1 : 0; s.f = j.f ? 1 : 0; s.t = +j.t || 0; s.b = typeof j.b === 'number' ? j.b : null;
      s.d = Array.isArray(j.d) ? j.d.filter(function(x){ return typeof x === 'string'; }) : [];
      s.o = j.o && typeof j.o === 'object' ? j.o : {};
    } catch(e){}
    return s;
  }
  function pack(){
    var out = { p: S.p, f: S.f, d: S.d, t: S.t, b: S.b };
    var withO = JSON.stringify(Object.keys(S.o).length ? Object.assign({ o: S.o }, out) : out);
    return lms && lms.v === '1.2' && withO.length > 4096 ? JSON.stringify(out) : withO;
  }

  /* objectives: one per course, plus the two assessments */
  var objIndex = {};
  function objId(kind, name){
    return lms.v === '1.2' ? kind + '_' + name : 'urn:vu:hcm-academy:' + kind + ':' + name;
  }
  function readObjectives(){
    var n = parseInt(lms.get('cmi.objectives._count'), 10) || 0;
    for (var i = 0; i < n; i++){ var id = lms.get('cmi.objectives.' + i + '.id'); if (id) objIndex[id] = i; }
  }
  function objective(id){
    if (objIndex[id] === undefined){
      var n = parseInt(lms.get('cmi.objectives._count'), 10) || 0;
      objIndex[id] = n; lms.set('cmi.objectives.' + n + '.id', id);
    }
    return 'cmi.objectives.' + objIndex[id] + '.';
  }
  function courseDone(slug){
    var k = objective(objId('course', slug));
    if (lms.v === '1.2') lms.set(k + 'status', 'completed');
    else { lms.set(k + 'completion_status', 'completed'); }
  }
  function assessment(kind, pct, passed){
    var k = objective(objId('assessment', kind));
    lms.set(k + 'score.raw', pct); lms.set(k + 'score.min', 0); lms.set(k + 'score.max', 100);
    if (lms.v === '1.2') lms.set(k + 'status', kind === 'pre' ? 'completed' : passed ? 'passed' : 'failed');
    else {
      lms.set(k + 'score.scaled', (pct / 100).toFixed(2));
      lms.set(k + 'completion_status', 'completed');
      if (kind === 'final') lms.set(k + 'success_status', passed ? 'passed' : 'failed');
    }
  }

  var lastStatus = '';
  function status(){
    if (!lms) return;
    var f = lms.f;
    if (S.f && S.b !== null){
      lms.set(f.raw, S.b); lms.set(f.min, 0); lms.set(f.max, 100);
      if (f.scaled) lms.set(f.scaled, (S.b / 100).toFixed(2));
    }
    if (lms.v === '1.2'){
      var st = S.f ? 'passed' : 'incomplete';
      var kept = lastStatus === 'passed' || (lastStatus === 'completed' && !S.f);   /* never move a learner backward */
      if (st !== lastStatus && !kept && lms.set(f.status, st)) lastStatus = st;
    } else {
      lms.set(f.completion, S.f ? 'completed' : 'incomplete');
      lms.set(f.success, S.f ? 'passed' : 'unknown');
      var m = (S.d.length + (S.f ? 1 : 0)) / (total() + 1);
      lms.set(f.progress, Math.min(1, m).toFixed(2));
    }
  }
  function save(){
    if (lms){ lms.set(lms.f.suspend, pack()); status(); lms.commit(); }
    else { try { localStorage.setItem(LOCAL, pack()); } catch(e){} }
  }

  /* ---------- what the pages call (through bridge.js); values travel as JSON text ---------- */
  function slugOf(id){ return typeof id === 'string' && id.indexOf('c-') === 0 ? id.slice(2) : null; }
  window.HCM_SCORM = {
    get: function(k){
      if (k === 'hcm-pre') return S.p ? 'true' : null;
      if (k === 'hcm-final') return S.f ? 'true' : null;
      if (k === 'hcm-done') return JSON.stringify(S.d.map(function(s){ return 'c-' + s; }));
      if (k === 'hcm-total') return String(total());
      return S.o.hasOwnProperty(k) ? S.o[k] : null;
    },
    set: function(k, json){
      var v; try { v = JSON.parse(json); } catch(e){ return; }
      if (k === 'hcm-pre') S.p = v ? 1 : 0;
      else if (k === 'hcm-final'){ if (v) S.f = 1; }
      else if (k === 'hcm-total') S.t = +v || 0;
      else if (k === 'hcm-done'){
        var next = [];
        (Array.isArray(v) ? v : []).forEach(function(id){ var s = slugOf(id); if (s && next.indexOf(s) < 0) next.push(s); });
        if (lms) next.forEach(function(s){ if (S.d.indexOf(s) < 0) courseDone(s); });
        S.d = next;
      }
      else S.o[k] = json;
      save();
    },
    clear: function(){ S = blank(); save(); },
    report: function(json){
      var r; try { r = JSON.parse(json); } catch(e){ return; }
      if (r.kind !== 'pre' && r.kind !== 'final') return;
      if (r.kind === 'final' && r.passed){ S.f = 1; S.b = S.b === null ? r.pct : Math.max(S.b, r.pct); }
      if (lms){ assessment(r.kind, r.pct, !!r.passed); interactions(r); }
      save();
    },
    page: function(href){
      var base = location.href.replace(/[?#].*$/, '').replace(/[^\/]*$/, '');
      if (href.indexOf(base) !== 0) return;
      var rel = href.slice(base.length);
      if (lms){ lms.set(lms.f.location, rel.slice(0, lms.v === '1.2' ? 255 : 1000)); lms.commit(); }
      else { try { localStorage.setItem(LOCAL + '-page', rel); } catch(e){} }
    }
  };

  /* each assessment answer as an interaction (answer letters follow the question's original option order) */
  function pad(n){ return (n < 10 ? '0' : '') + n; }
  function interactions(r){
    var L = 'abcdefghij', now = new Date();
    var clock = pad(now.getHours()) + ':' + pad(now.getMinutes()) + ':' + pad(now.getSeconds());
    var stamp = now.getFullYear() + '-' + pad(now.getMonth() + 1) + '-' + pad(now.getDate()) + 'T' + clock;
    (r.items || []).forEach(function(it){
      var n = parseInt(lms.get('cmi.interactions._count'), 10) || 0, k = 'cmi.interactions.' + n + '.';
      var id = r.kind + '_q' + pad(it.n);
      if (lms.v === '1.2'){
        lms.set(k + 'id', id); lms.set(k + 'type', 'choice'); lms.set(k + 'time', clock);
        lms.set(k + 'weighting', 1);
        lms.set(k + 'student_response', L.charAt(it.chose)); lms.set(k + 'correct_responses.0.pattern', L.charAt(it.answer));
        lms.set(k + 'result', it.correct ? 'correct' : 'wrong');
      } else {
        lms.set(k + 'id', 'urn:vu:hcm-academy:' + r.kind + ':q' + pad(it.n)); lms.set(k + 'type', 'choice');
        lms.set(k + 'timestamp', stamp); lms.set(k + 'weighting', 1);
        lms.set(k + 'description', String(it.q || '').slice(0, 250));
        lms.set(k + 'learner_response', L.charAt(it.chose)); lms.set(k + 'correct_responses.0.pattern', L.charAt(it.answer));
        lms.set(k + 'result', it.correct ? 'correct' : 'incorrect');
      }
    });
  }

  /* ---------- session time and exit ---------- */
  function elapsed(){
    var s = Math.max(0, Math.round((Date.now() - started) / 1000)), h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = s % 60;
    return lms.v === '1.2' ? pad(h) + ':' + pad(m) + ':' + pad(x) : 'PT' + h + 'H' + m + 'M' + x + 'S';
  }
  function end(){
    if (ended || !lms) return; ended = true;
    lms.set(lms.f.time, elapsed());
    lms.set(lms.f.exit, 'suspend');   /* keep progress so a learner can come back to the courses as a reference */
    lms.set(lms.f.suspend, pack()); status();
    lms.commit(); lms.finish();
  }
  window.addEventListener('pagehide', end);
  window.addEventListener('beforeunload', end);
  window.addEventListener('unload', end);

  /* ---------- fill the screen when the LMS opens the course in a small pop-up window ---------- */
  function fillScreen(){
    var top = window;
    try { while (top.parent && top.parent !== top && top.parent.document) top = top.parent; } catch(e){}
    try {
      if (!top.opener) return;                       /* only a pop-up window can be resized */
      var sw = screen.availWidth, sh = screen.availHeight;
      if (top.outerWidth >= sw * 0.9 && top.outerHeight >= sh * 0.9) return;
      top.moveTo(screen.availLeft || 0, screen.availTop || 0);
      top.resizeTo(sw, sh);
    } catch(e){}
  }
  fillScreen();

  /* ---------- start ---------- */
  function safe(rel){ return rel && !/^[a-z]+:|^\/|\.\.|\\/i.test(rel) && /\.html(#[\w-]*)?$/.test(rel) ? rel : ''; }
  var found = find(), resume = '';
  if (found){
    lms = connect(found);
    if (!lms.init()){ lms = null; }
  }
  if (lms){
    S = load(lms.get(lms.f.suspend));
    readObjectives();
    if (lms.v === '1.2'){ lastStatus = lms.get(lms.f.status); if (lastStatus === 'not attempted' || !lastStatus) { lms.set(lms.f.status, 'incomplete'); lastStatus = 'incomplete'; } }
    status(); lms.commit();
    resume = safe(lms.get(lms.f.location));
  } else {
    try { S = load(localStorage.getItem(LOCAL)); resume = safe(localStorage.getItem(LOCAL + '-page')); } catch(e){}
    note.hidden = false;
  }
  document.getElementById('dismiss').addEventListener('click', function(){ note.hidden = true; });
  frame.src = resume || 'index.html';
})();

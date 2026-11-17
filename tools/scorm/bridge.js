/* HCM Academy SCORM bridge. Loaded first on every page of the SCORM package (tools/build_scorm.py adds it).
   It looks for the launch page (scorm.html) in a parent window. When found, the pages save progress
   through it to the LMS instead of this browser's localStorage. When not found, it does nothing and
   the pages fall back to localStorage, as on the public site. */
(function(){
  'use strict';
  var shell = null, w = window;
  try {
    for (var i = 0; i < 12 && w; i++){
      if (w.HCM_SCORM){ shell = w.HCM_SCORM; break; }
      if (w === w.parent) break;
      w = w.parent;
    }
  } catch(e){ shell = null; }
  if (!shell) return;

  window.HCM_SCORM_MODE = true;
  /* values cross windows as JSON text so arrays and objects belong to this page */
  window.HCM_STORE = {
    get: function(k, d){ try { var v = shell.get(k); return v === null || v === undefined ? d : JSON.parse(v); } catch(e){ return d; } },
    set: function(k, v){ try { shell.set(k, JSON.stringify(v)); } catch(e){} },
    clear: function(){ try { shell.clear(); } catch(e){} }
  };
  window.HCM_REPORT = function(r){ try { shell.report(JSON.stringify(r)); } catch(e){} };

  document.documentElement.classList.add('scorm');
  var st = document.createElement('style');
  st.textContent = '.scorm .demo{ display:none !important; }';
  (document.head || document.documentElement).appendChild(st);

  /* pages outside the package open in a new tab: many sites refuse to load inside an LMS frame */
  document.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a || (a.protocol !== 'http:' && a.protocol !== 'https:') || a.origin === location.origin) return;
    a.target = '_blank'; a.rel = 'noopener';
  }, true);

  try { shell.page(location.href); } catch(e){}
})();

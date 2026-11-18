/* Hiring, Job Requisitions, and the Create Job Requisition page, shared by the Background checks and Executive search scenes.
   Same screens as the Create a requisition video: Our Workforce follows Vanderbilt's screens; the requisition follows standard
   Oracle Recruiting and the course text (see each course's Screen check). Names are fictional.
   reqPages({ id, title, loc, sum3, csp, acct }) adds one requisition page; call it once per requisition shown. */
window.reqCommon = function(){
  VIDEO.add(C.page('hiring', C.title('Hiring') + '<div class="lp" style="top:160px;width:520px"><div class="otab">' +
    ['Create Job Requisition', 'Job Offers', 'Job Requisitions', 'Manage Shared Interview Schedules', 'Recruiting Activity Center'].map(function(t){
      return '<div class="tr" style="grid-template-columns:28px 1fr"' + (t === 'Job Requisitions' ? ' id="h-reqs"' : '') + '>' + C.I('doc') + '<span>' + t + '</span></div>'; }).join('') + '</div></div>'));
  VIDEO.add(C.page('reqs', C.title('Job Requisitions') + C.btns([{ t:'Create', cta:true, id:'b-create' }]) + '<div class="lp" style="top:160px">' +
    C.table({ cols:'.8fr 1.6fr 1fr 1.3fr .8fr', head:['Requisition', 'Title', 'Status', 'Hiring Manager', 'Openings'], rows:[
      { cells:['2611', 'Lab Manager', 'Open', 'Morgan Ellis', '1'] }, { cells:['2598', 'Research Analyst', 'Filled', 'Morgan Ellis', '1'] } ] }) + '</div>'));
};
window.reqPage = function(o){
  var F = C.field, p = o.id, yn = function(id, label, bind){ return F({ id:p + id, label:label, bind:p + bind, ph:'Select a value', icon:'down' }); };
  var secs = [
    { id:'s1', title:'Basic Information', sum:o.title + ' · New to the department · Limited, 1 opening', body:'' },
    { id:'s2', title:'Hiring Team', sum:'Hiring manager Morgan Ellis · Collaborator Jordan Avery', body:'' },
    { id:'s3', title:'Requisition Type and Location', sum:o.sum3, body:'<div class="fld3">' +
      F({ id:p + 'f-type', label:'Requisition Type', bind:p + 'rtype', ph:'Select a value', icon:'down', ddIf:p + 'dd-type', dd:[{ id:p + 'o-std', t:'Standard', s:'The full recruiting process' }, { id:p + 'o-abb', t:'Abbreviated', s:'You already have a candidate' }, { id:p + 'o-exe', t:'Executive search', s:"Cielo's executive search program only" }] }) +
      F({ id:p + 'f-org', label:'Organization', value:'Vanderbilt', icon:'down' }) +
      F({ id:p + 'f-loc', label:'Primary Location', value:o.loc, icon:'search' }) + '</div>' },
    { id:'s4', title:'Required Details', sum:'Funding internal · Work with minors: Yes · No fingerprinting or MVR', body:'<div class="fld3">' +
      F({ label:'Funding Source', value:'Internal', icon:'down' }) + F({ label:'Driving', value:'No', icon:'down' }) + F({ label:'Replacing a RIF Role', value:'No', icon:'down' }) +
      yn('f-fp', 'Fingerprinting', 'fp') + yn('f-mvr', 'Motor Vehicle Record', 'mvr') +
      F({ id:p + 'f-min', label:'Work With Minors', bind:p + 'min', ph:'Select a value', icon:'down', ddIf:p + 'dd-min', dd:[{ id:p + 'o-miny', t:'Yes', s:'Adds a protection of minors check' }, { t:'No' }] }) + '</div>' },
    { id:'s5', title:'Description', sum:'Internal and external descriptions added', body:'' },
    { id:'s6', title:'Offer Information', sum:'On site', body:'' },
    { id:'s7', title:'Attachments', sum:'Position description and pre-search memo', body:'' },
    { id:'s8', title:'Configuration', sum:o.csp + ' process · HireRight · ' + o.acct, body:'<div class="fld3">' +
      F({ id:p + 'f-csp', label:'Candidate Selection Process', bind:p + 'csp', ph:'Select a value', icon:'down', ddIf:p + 'dd-csp', dd:[{ id:p + 'o-cstd', t:'Standard' }, { id:p + 'o-cny', t:'New York', s:'New York requisitions' }] }) +
      F({ id:p + 'f-ven', label:'Background Check Vendor', value:'HireRight', icon:'down' }) +
      F({ id:p + 'f-acct', label:'Background Check Account', bind:p + 'acct', ph:'Select a value', icon:'down', ddIf:p + 'dd-acct', dd:[{ id:p + 'o-a0', t:'VAN000', s:'Anywhere except New York' }, { id:p + 'o-a9', t:'VAN09', s:'New York' }] }) + '</div>' }
  ];
  var html = '<div class="secs" style="top:160px">' + secs.map(function(x, i){
    return C.sec({ id:p + x.id, n:i + 1, title:x.title, sum:x.sum, done:p + x.id + '-done', open:p + x.id + '-open !' + p + x.id + '-done', later:'!' + p + x.id + '-open !' + p + x.id + '-done', body:x.body + C.cont(p + 'c' + (i + 1)) });
  }).join('') + '</div>';
  VIDEO.add(C.page(p, C.title('Create Job Requisition: ' + o.title) + C.btns([{ t:'Save', id:p + 'b-save' }, { t:'Submit', cta:true, id:p + 'b-submit', off:p + 'can-submit' }]) + html +
    '<div class="scrim" data-if="' + p + 'pkg"></div><div class="modal" data-if="' + p + 'pkg" id="' + p + 'pkg"><h3>Background Check Packages</h3><p style="font-size:14.5px;color:rgba(22,21,19,.7);margin:0 0 18px">Select packages for this requisition.</p>' +
    '<div style="text-align:right"><span class="btn sec" id="' + p + 'b-pkg">Close</span></div></div>'));
};
/* sections before `upto` are shown as done; section `upto` is open */
window.reqAt = function(p, upto){ for (var i = 1; i <= 8; i++){ flag(p + 's' + i + '-done', i < upto); flag(p + 's' + i + '-open', i === upto); } };

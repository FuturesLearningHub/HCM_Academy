/* Pending Workers and the Convert flow, shared by the Convert a pending worker and Non-Workers scenes.
   Pages follow standard Oracle and the course text (see each course's Screen check). Names, numbers, and addresses are fictional. */
window.convertPages = function(o){
  var F = C.field, p = o.person;
  VIDEO.add(C.home({ toast:o.toast }));
  VIDEO.add(C.page('pw', C.title('Pending Workers') + '<div class="lp" style="top:160px">' +
    C.table({ id:'pwtab', cols:'1.4fr 1fr 1fr 1.2fr 1.6fr 40px', head:['Name', 'Worker Type', 'Proposed Start', 'Business Unit', 'Position', ''], rows:[
      { id:'r-p', cells:['<b>' + p.name + '</b>', p.wtype, p.start, 'Arts and Science', p.pos, '<span class="kebab" id="kb">' + C.I('kebab') + '</span>'] },
      { cells:['Dana Brooks', 'Employee', '1/4/2027', 'Arts and Science', 'BIO-LM-01 Lab Manager', '<span class="kebab">' + C.I('kebab') + '</span>'] } ] }) +
    '<div class="omenu" style="left:960px;top:96px" data-if="m-kb"><div>Edit Pending Worker</div><div id="m-conv" class="hov">Convert</div><div>Quick Convert</div></div></div>'));
  VIDEO.add(C.page('pick', C.title('Convert: ' + p.name) + C.pban(p.ban) + '<div class="lp" style="top:236px"><p class="flabel">Select the sections you want to update.</p>' +
    o.sections.map(function(s){ return C.chk({ id:'k-' + s[0], flag:'k-' + s[0], t:s[1] }); }).join('') +
    '<div style="margin-top:18px"><span class="btn cta" id="b-pick">Continue</span></div></div>'));
  var secs = o.flow, html = '<div class="secs" style="top:228px">' + secs.map(function(x, i){
    return C.sec({ id:x.id, n:i + 1, title:x.title, sum:x.sum, done:x.id + '-done', open:(i ? secs[i - 1].id + '-done ' : 'conv ') + '!' + x.id + '-done', later:i ? '!' + secs[i - 1].id + '-done' : null, body:x.body + C.cont('c-' + x.id) });
  }).join('') + '</div>';
  VIDEO.add(C.page('conv', C.title('Convert: ' + p.name) + C.btns([{ t:'Cancel' }, { t:'Submit', cta:true, id:'b-submit', off:'can-submit' }]) + C.pban(p.ban) + html));
};
/* the Convert sections, by key: {id, title, sum, body} */
window.convertSection = function(k, o){
  var F = C.field, E = C.esc;
  var S = {
    why:{ title:'When and Why', sum:o.whySum, body:'<div class="fld3">' +
      F({ id:'f-act', label:'Action', bind:'act', ph:'Select a value', icon:'down', ddIf:'dd-act', dd:[{ id:'o-hire', t:'Hire' }] }) +
      F({ id:'f-rsn', label:'Reason', bind:'rsn', ph:'Select a value', icon:'down', ddIf:'dd-rsn', dd:[{ id:'o-emp', t:'Employment' }, { t:'Service free appointment', s:'Only for students receiving a stipend' }, { id:'o-nonemp', t:'Non-employment', s:'Affiliates' }] }) + '</div>' },
    bu:{ title:'Business Unit and Position', sum:'Arts and Science · ' + o.pos, body:'<div class="fld3">' + F({ label:'Business Unit', ro:'Arts and Science' }) +
      F({ id:'f-pos', label:'Position', value:o.pos, icon:'search' }) + '</div>' },
    bio:{ title:'Biographical Info', sum:'Date of birth confirmed · US citizen: Yes', body:'<div class="fld3">' + F({ id:'f-dob', label:'Date of Birth', ro:'4/12/1994' }) +
      '<div class="fw"><p class="flabel">US Citizen or Permanent Resident</p><div class="field" id="f-cit"><span class="grow"><span data-bind="cit"></span><span class="ph" data-ph="cit">Not entered</span></span>' + C.I('pen') + '</div><div class="dd" data-if="dd-cit"><div id="o-yes" class="hov">Yes</div><div>No</div></div></div></div>' },
    nid:{ title:'National Identifiers', sum:'United States · Social Security Number', body:'<div class="fld3">' + F({ label:'Country', ro:'United States' }) + F({ label:'National ID Type', ro:'Social Security Number' }) +
      F({ id:'f-ssn', label:'National ID', value:'XXX-XX-4821', icon:'pen' }) + '</div><p class="hint">No Social Security number? Email the International Tax Office (ito@vanderbilt.edu) for a placeholder number.</p>' },
    addr:{ title:'Addresses', sum:'Home address in the United States', body:'<div class="fld2">' + F({ id:'f-addr', label:'Home Address', value:'1200 Example Avenue, Nashville, TN 37212' }) + F({ id:'f-ctry', label:'Country', ro:'United States' }) + '</div>' },
    ovr:{ title:'Position Overrides', sum:'Location and working hours reviewed', body:'<div class="fld3">' + F({ id:'f-oloc', label:'Location', value:'Nashville Main Campus', icon:'search' }) +
      F({ id:'f-owh', label:'Working Hours', value:o.hours }) + '<div class="fw"><p class="flabel">Manager</p><div class="chk" id="f-me">' + '<span class="cb">' + C.I('check') + '</span>I am the manager</div><p class="hint">Check only if you are their manager.</p></div></div>' },
    asg:{ title:'Assignment', sum:o.asgSum, body:'<div class="fld3">' +
      F({ id:'f-ptype', label:'Person Type', bind:'ptype', ph:'Select a value', icon:'down', ddIf:'dd-ptype', dd:[{ id:'o-ptype', t:o.ptype }] }) +
      F({ id:'f-aloc', label:'Location', value:'Nashville Main Campus', icon:'search' }) +
      F({ id:'f-min', label:'Working With Minors', bind:'min', ph:'Required', icon:'down', ddIf:'dd-min', dd:[{ id:'o-no', t:'No' }, { t:'Yes', s:'Triggers an additional check' }] }) +
      F({ id:'f-exp', label:'Default Expense Account', bind:'exp', ph:"Your department's usual account", icon:'search' }) +
      F({ id:'f-stat', label:'Assignment Status', bind:'stat', ph:'Select a value', icon:'down', ddIf:'dd-stat', dd:[{ id:'o-pe', t:'Active - Payroll Eligible' }, { id:'o-np', t:'Active - No Payroll', s:'Only for affiliates. They are not paid.' }] }) + '</div>' },
    mgr:{ title:'Managers and Work Relationship', sum:o.mgrSum, body:'<div class="fld3">' +
      '<div class="fw"><p class="flabel">Manager</p><div class="field" id="f-mgr"><span class="grow"><span data-bind="mgr"></span><span class="ph" data-ph="mgr">None</span></span>' + C.I('pen') + '</div></div>' +
      F({ id:'f-nhr', label:'New Hire Report', bind:'nhr', ph:'Select a value', icon:'down', ddIf:'dd-nhr', dd:[{ id:'o-inc', t:'Include', s:'Paid hires' }, { id:'o-exc', t:'Exclude', s:'Affiliates and contractors' }] }) + '</div>' },
    pay:{ title:'Payroll Details', sum:'Monthly', body:'<div class="fld3">' +
      F({ id:'f-pay', label:'Payroll', bind:'pay', ph:'Select a value', icon:'down', ddIf:'dd-pay', dd:[{ id:'o-mon', t:'Monthly', s:'Regular: pays an annual salary' }, { t:'Biweekly', s:'Hourly: overtime biweekly, time card required' }] }) + '</div>' },
    sal:{ title:'Salary', sum:'$58,000 annual at 0.75 FTE', body:'<div class="fld3">' +
      F({ id:'f-sal', label:'Salary Amount (Annual)', bind:'sal', ph:'' }) + F({ label:'FTE', ro:'0.75' }) +
      '<div class="fw"><p class="flabel">Full-Time Equivalent</p><div class="field ro"><span class="grow" data-bind="fte"></span>' + C.I('calcx') + '</div><p class="hint">For reference only.</p></div></div>' },
    att:{ title:'Compensation and Attachments', sum:'Offer letter attached', body:'<p class="flabel">Compensation</p><div class="att" style="margin-top:0">' + C.I('doc') + 'No other payments</div>' +
      '<p class="flabel" style="margin-top:14px">Attachments</p><div class="drop" id="f-att" style="margin-top:0">' + C.I('up') + 'Drag and drop files here or <u>add a file</u></div><div class="att" data-in="att1">' + C.I('clip') + 'Offer letter.pdf</div>' }
  };
  var s = S[k]; s.id = 'x' + k; return s;
};

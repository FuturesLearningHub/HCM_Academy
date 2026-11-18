/* A process-board explainer: an intro card, one board page per course step, and a watch-outs card.
   Used for courses that are concepts or happen outside Oracle. Every line on screen comes from the course.
   boardScene({ eyebrow, pre, em, post, p, meta, rail:[labels], pages:[{pre, em, post, lines, art}], out:{pre, em, post, items} })
   Art helpers: B.doc(n, kicker, title, rows[[k, v]], foot) and B.lines(n, kicker, title, items[[ok, text]]). */
window.B = {
  doc: function(n, kicker, title, rows, foot){
    return C.doc({ kicker:kicker, title:title, rows:rows.map(function(r, i){ return [r[0], r[1], 'st-' + n, .5 + i * .3]; }),
      foot:foot ? '<span data-in="st-' + n + '" data-d="' + (.6 + rows.length * .3) + '">' + C.esc(foot) + '</span>' : null });
  },
  lines: function(n, kicker, title, items){
    return '<div class="art"><div class="dk">' + C.esc(kicker) + '</div><b>' + C.esc(title) + '</b>' + items.map(function(x, i){
      return '<div class="ln' + (x[0] ? '' : ' no') + '" data-in="st-' + n + '" data-d="' + (.6 + i * .4) + '">' + C.I(x[0] ? 'checkc' : 'info') + '<span>' + C.esc(x[1]) + '</span></div>'; }).join('') + '</div>';
  }
};
window.boardScene = function(o){
  var n = o.pages.length;
  VIDEO.set({ steps:n });
  VIDEO.addCard(C.card({ id:'intro', h:'big', eyebrow:o.eyebrow, pre:o.pre, em:o.em, post:o.post, rule:true, p:o.p, meta:o.meta }));
  VIDEO.addCard(C.board({ id:'board', steps:o.rail, pages:o.pages }));
  VIDEO.addCard(C.card({ id:'out', eyebrow:'Watch-outs', pre:o.out.pre, em:o.out.em, post:o.out.post, items:o.out.items, meta:o.out.meta || 'Questions: pcb@vanderbilt.edu' }));
  seg(); card('intro'); wait(3.5); hold(-.5);
  for (var k = 1; k <= n; k++){
    seg(); if (k === 1){ card('board'); wait(.6); card('intro', false); }
    stepTo(k, n); wait(3.2); mark(k); hold(-.7);
  }
  seg(); card('out'); wait(.6); card('board', false); wait(2); hold(-2.2);
  VIDEO.run();
};

#!/usr/bin/env python3
"""Build HCM Academy micro-course pages from tools/course_content.py.
Writes courses/<slug>/index.html, the two assessment pages (assessment/pre, assessment/final),
and changes/index.html (what changed, by date). Owners, versions, the change log, and the
"Before you submit" block come from tools/governance.py.
Run: python3 tools/build_courses.py"""
import html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from course_content import COURSES, VERIFY  # noqa: E402
import governance as G  # noqa: E402
ROOT = os.path.dirname(HERE)
E = lambda s: html.escape(s, quote=True)
NUM = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six"}

WARN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l9 16H3z"/><path d="M12 10v4M12 17.5v.01"/></svg>'
BOOK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg>'
PRINT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M6 14h12v7H6z"/></svg>'

def step_items(steps, checklist):
    out = []
    for i, s in enumerate(steps):
        t, sub, d = (s, [], "") if isinstance(s, str) else (s["t"], s.get("sub", []), s.get("d", ""))
        subs = ("<ul>" + "".join(f"<li>{E(x)}</li>" for x in sub) + "</ul>") if sub else ""
        if checklist:
            det = f'<span class="sd">{E(d)}</span>' if d else ""
            out.append(f'<li><label><input type="checkbox" /><span class="st"><strong>{E(t)}</strong>{det}{subs}</span></label></li>')
        else:
            out.append(f"<li>{E(t)}{subs}</li>")
    return "\n".join(out)

def table(tb):
    """A reference table. Tables with four or more columns stack into labeled rows on small screens (data-th)."""
    if not tb: return ""
    head = "".join(f'<th scope="col">{E(h)}</th>' for h in tb["head"])
    rows = "".join("<tr>" + "".join(f'<td data-th="{E(h)}">{confirm(c)}</td>' for h, c in zip(tb["head"], r)) + "</tr>" for r in tb["rows"])
    cls = "ref wide" if len(tb["head"]) >= 4 else "ref tl" if tb.get("tight_last") else "ref"
    return f'<table class="{cls}"><caption>{E(tb["title"])}</caption><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>'

CHECKED = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/></svg>'

def confirm(s):
    """Escape text, marking any 'To confirm: ...' part so an open point reads the same everywhere."""
    if "To confirm: " not in s: return E(s)
    a, b = s.split("To confirm: ", 1)
    return f'{E(a)}<span class="tb">To confirm: {E(b)}</span>'

def before_html(c):
    """The Before you submit block on a pay-impacting course: attach, check, cutoff, who does what."""
    b = G.before(c["slug"])
    if not b: return ""
    if b.get("docs_none"): docs = f"<p>{E(b['docs_none'])}</p>"
    elif b["docs"]: docs = "<ul>" + "".join(f'<li>{E(d)} <span class="tag">{E(st)}</span></li>' for d, st in b["docs"]) + "</ul>"
    else: docs = "<p>None named yet.</p>"
    gap = f'<p class="tbc"><b>To confirm</b>{E(b["docs_gap"])}</p>' if b.get("docs_gap") else ""
    conf = f'<p class="tbc"><b>To confirm</b>{E(b["confirm"])}</p>' if b.get("confirm") else ""
    checks = "".join(f"<li>{E(x)}</li>" for x in b["checks"])
    cut = f'<div><h4>Cutoff</h4><p>{confirm(G.CUTOFF[b["cutoff"]])}</p></div>' if b.get("cutoff") else ""
    who = (f'<li><b>Who starts it:</b> {confirm(G.sentence(b["submits"]))}</li>'
           f'<li><b>Who approves:</b> {confirm(b["approves"])}</li>'
           f'<li><b>What happens next:</b> {confirm(b["then"])}</li>')
    std = f"<p>{E(G.STANDARD_CHECK)}</p>" if b.get("standard", True) else ""
    return (f'<div class="before" id="before"><h3>{CHECKED}{E(b.get("title", "Before you submit"))}</h3>'
            f'<p class="blede">The same four checks on every pay-impacting transaction. Draft: the owner for this area confirms anything marked To confirm.</p>'
            f'<div class="bgrid"><div><h4>Attach</h4>{docs}{gap}</div>'
            f'<div><h4>Check</h4>{std}<ul>{checks}</ul>{conf}</div>'
            f'{cut}<div><h4>Who does what</h4><ul class="who">{who}</ul></div></div></div>')

def before_ja(c):
    """The same block in three lines, for the printed job aid."""
    b = G.before(c["slug"])
    if not b: return ""
    lines = [f"<li><b>Attach:</b> {confirm(G.attach_line(b))}</li>", f"<li><b>Check:</b> {E(' '.join(b['checks']))}</li>"]
    if b.get("cutoff"): lines.append(f"<li><b>Cutoff:</b> {confirm(G.CUTOFF_SHORT[b['cutoff']])}</li>")
    return f'<h3>{E(b.get("title", "Before you submit"))}</h3><ul class="jw">{"".join(lines)}</ul>'

def review_status(c):
    p = c.get("pending", "")
    if not p: return "Built from SME sessions and Vanderbilt guides. Validation by the HCM group is pending."
    return p

def record_html(c):
    """Course record: owner, version, review status, and what changed."""
    own = G.owner(c)
    items = "".join(f"<li><b>{E(d)}</b>{E(x)}</li>" for d, x in G.changes(c))
    scope = G.OWNER_SCOPE[own]
    return f'''<section class="part record" id="record" aria-labelledby="h5">
      <p class="mono num">Course record</p>
      <h2 id="h5">Owner and <em>changes</em>.</h2>
      <dl class="recl">
        <div><dt>Owner</dt><dd>{E(own)}<span>{E(scope)}</span></dd></div>
        <div><dt>Version</dt><dd>{E(G.EDITION)}<span>Updated {E(G.updated(c))}</span></dd></div>
        <div><dt>Review</dt><dd>{E(review_status(c))}</dd></div>
      </dl>
      <h3 class="rech">What changed</h3>
      <ul class="chg">{items}</ul>
      <p class="recf"><a href="../../changes/">See changes across all courses</a>. Something out of date? Email <a href="mailto:pcb@vanderbilt.edu">pcb@vanderbilt.edu</a>.</p>
    </section>'''

def page(c, n, total):
    title_html = f'{E(c["title_pre"])} <em>{E(c["title_em"])}</em>.'
    src = "; ".join(c["sources"])
    pending = f'<p class="draft"><b>{G.EDITION}</b>{E(c["pending"])}</p>' if c.get("pending") else \
              f'<p class="draft"><b>{G.EDITION}</b>Built from SME sessions and Vanderbilt guides. Validate with the HCM group before release.</p>'
    intro = "".join(f"<p>{E(p)}</p>" for p in c["intro"])
    video = ""
    if c.get("video"):
        v = c["video"]
        if v["src"].endswith(".mp4"):   # explainer video kept with the course (no sound; the captions are on screen)
            video = (f'<figure class="video"><div class="frame"><video controls playsinline preload="metadata" poster="{E(v["poster"])}" '
                     f'aria-label="Video: {E(v["title"])}"><source src="{E(v["src"])}" type="video/mp4" /></video></div>'
                     '<figcaption>Watch first, then read the details below. No sound: the steps are captioned on screen. '
                     'A training simulation with fictional names, built from standard Oracle screens; Vanderbilt\'s screens may differ slightly.</figcaption></figure>')
        else:
          video = (f'<figure class="video"><div class="frame"><iframe src="{E(v["src"])}" title="Video: {E(v["title"])}" loading="lazy" '
                   'allow="autoplay; fullscreen; clipboard-write" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
                   '<figcaption>Watch first, then read the details below.</figcaption></figure>')
    vf = VERIFY.get(c["slug"])
    if vf:
        pending += f'<p class="draft"><b>Screen check</b>Confirm in Vanderbilt\'s Oracle or UKG during a recorded demo: {E("; ".join(vf))}.</p>'
    quiz = []
    for qi, q in enumerate(c["quiz"]):
        opts = "".join(f'<label><input type="radio" name="q{qi}" value="{oi}" />{E(o)}</label>' for oi, o in enumerate(q["o"]))
        quiz.append(f'<fieldset data-a="{q["a"]}" data-why="{E(q["why"])}" data-hint="Look back at the walkthrough."><legend><span class="qn">Q{qi+1}</span>{E(q["q"])}</legend>{opts}<p class="fb" aria-live="polite"></p></fieldset>')
    watch = "".join(f"<li>{E(w)}</li>" for w in c["watch"])
    back = f'../../index.html#{c["topic"]}'
    docs_box = ""
    if c.get("docs"):
        items = "".join(f'<li><a href="{E(u)}" target="_blank" rel="noopener">{E(l)}<span class="sr"> (opens in a new tab)</span></a></li>' for l, u in c["docs"])
        docs_box = f'<div class="docs"><h3>{BOOK}Official documentation</h3><p>Vendor documentation describes the standard process. Vanderbilt\'s setup, codes, and rules in this course take priority.</p><ul>{items}</ul></div>'
    det = c.get("detailed")
    detailed_html = ""
    if det:
        items = "".join(
            f'<li class="dstep"><h3><span class="dn">{i:02d}</span>{E(x["t"])}</h3><p>{E(x["d"])}</p>'
            f'<img src="img/{E(x["img"])}" alt="Screenshot: {E(x["t"].rstrip("."))}" width="1400" height="1138" loading="lazy" /></li>'
            for i, x in enumerate(det["steps"], 1))
        detailed_html = (f'<article class="jobaid ja-detail" aria-label="Detailed job aid">'
                         f'<div class="ja-head"><img src="../../assets/img/vu-lockup-black.png" alt="Vanderbilt University" width="100" height="26" /><span class="mono">HCM Academy detailed job aid &middot; {E(c["topic_label"])}</span></div>'
                         f'<h2>{E(det["title"])}</h2><p class="ja-use">Step by step with screenshots. {E(det["source"])}</p>'
                         f'<ol class="dsteps">{items}</ol>'
                         f'<div class="ja-foot"><span>{G.EDITION}, updated {G.updated(c)}.</span><span>Questions: pcb@vanderbilt.edu</span></div></article>')
        ja_intro = "<p>Two parts: a one-page <b>quick guide</b>, then a <b>detailed job aid</b> with a screenshot for every step. Print either one, or save it as a PDF.</p>"
        ja_buttons = f'<button type="button" class="btn" data-print="quick">{PRINT}Print quick guide</button><button type="button" class="btn ghost" data-print>{PRINT}Print quick guide and detailed job aid</button>'
    else:
        ja_intro = "<p>A one-page version of the steps and watch-outs. Print it or save it as a PDF.</p>"
        ja_buttons = f'<button type="button" class="btn" data-print>{PRINT}Print job aid</button>'
    st = c.get("steps_title", "Step by step")
    w = st.rsplit(" ", 1)
    steps_h = f'{E(w[0])} <em>{E(w[1])}</em>.'
    nq = len(c["quiz"]); nw = NUM[nq]; own = G.owner(c)
    follow = "Check off each item as you read." if c["system"] == "Overview" or c.get("steps_title") else f'Follow along in {E(c["system"].split(" (")[0].split(" +")[0])}. Check off each step as you go.'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{E(c["name"])} · HCM Academy</title>
<meta name="description" content="{E(c["use_when"])}" />
<meta name="theme-color" content="#1C1C1C" />
<link rel="icon" href="../../assets/img/favicon.svg" type="image/svg+xml" />
<link rel="stylesheet" href="../course.css?v={ver('courses/course.css')}" />
<!-- Generated by tools/build_courses.py from tools/course_content.py. Edit the content file, not this page. -->
</head>
<body>
<a href="#main" class="skip">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="{back}" aria-label="HCM Academy home"><img src="../../assets/img/vu-lockup-white.png" alt="" width="122" height="32" /><span class="mono" aria-hidden="true">HCM Academy</span></a>
    <a class="back" href="{back}">&larr; All courses</a>
  </div>
</header>
<section class="hero" aria-labelledby="t">
  <div class="wrap">
    <p class="mono crumb">{E(c["topic_label"])} &middot; Course {n} of {total}</p>
    <h1 id="t">{title_html}</h1>
    <ul class="meta" aria-label="Course details"><li class="v">{G.EDITION}</li><li>Micro-learning</li><li>{E(c["time"])}</li>{'<li>Video</li>' if c.get("video") else ''}<li>{E(c["system"])}</li><li>{nq}-question check</li><li>Printable job aid</li></ul>
    <p class="rec"><span>Owner: <b>{E(own)}</b></span><span>Updated {E(G.updated(c))}</span><a href="#record">What changed</a></p>
  </div>
  <nav class="parts" aria-label="Course parts"><ol>
    <li><a href="#intro"><span>1</span>Intro</a></li><li><a href="#steps"><span>2</span>Walk through</a></li><li><a href="#check"><span>3</span>Check</a></li><li><a href="#jobaid"><span>4</span>Job aid</a></li>
  </ol></nav>
</section>
<main id="main" data-slug="{c["slug"]}">
  <div class="wrap">
    <section class="part" id="locked" aria-labelledby="hl" hidden>
      <p class="mono num">Locked</p>
      <h2 id="hl">Take the <em>pre-assessment</em> first.</h2>
      <p>Courses unlock once you've taken the pre-assessment. It takes about 5 minutes, it's not graded, and your results show which topics to start with.</p>
      <div class="acts"><a class="btn" href="../../assessment/pre/">Take the pre-assessment</a><a class="btn ghost" href="{back}">Back to all courses</a></div>
    </section>
    {pending}
    <section class="part" id="intro" aria-labelledby="h1">
      <p class="mono num">1 &middot; Intro</p>
      <h2 id="h1">When to <em>use</em> it.</h2>
      {video}
      {intro}
      <p class="use"><b>Use this when</b>{E(c["use_when"])}</p>
    </section>
    <section class="part" id="steps" aria-labelledby="h2">
      <p class="mono num">2 &middot; Walk through</p>
      <h2 id="h2">{steps_h}</h2>
      <p>{follow}</p>
      <ol class="steps">
{step_items(c["steps"], True)}
      </ol>
      <p class="stepcount" id="stepcount" aria-live="polite"></p>
      {table(c.get("table"))}
      {before_html(c)}
      <div class="watch"><h3>{WARN}Watch-outs</h3><ul>{watch}</ul></div>
      {docs_box}
    </section>
    <section class="part quiz" id="check" aria-labelledby="h3">
      <p class="mono num">3 &middot; Knowledge check</p>
      <h2 id="h3">Check your <em>understanding</em>.</h2>
      <p>{nw} questions. You get feedback on each answer. All {nw.lower()} right completes the course.</p>
      {"".join(quiz)}
      <p class="score" id="score" hidden></p>
    </section>
    <section class="part" id="jobaid" aria-labelledby="h4">
      <p class="mono num">4 &middot; Job aid</p>
      <h2 id="h4">Keep it <em>handy</em>.</h2>
      {ja_intro}
      <div class="acts">{ja_buttons}<a class="btn ghost" href="{back}">Back to all courses</a></div>
      <div class="ja-preview">
        <article class="jobaid{" ja-b" if G.before(c["slug"]) else ""}" aria-label="{"Quick guide" if det else "Job aid"} preview">
          <div class="ja-head"><img src="../../assets/img/vu-lockup-black.png" alt="Vanderbilt University" width="100" height="26" /><span class="mono">HCM Academy {"quick guide" if det else "job aid"} &middot; {E(c["topic_label"])}</span></div>
          <h2>{E(c["name"])}</h2>
          <p class="ja-use"><b>Use when:</b> {E(c["use_when"])} &middot; <b>System:</b> {E(c["system"])}</p>
          <ol>
{step_items(c["steps"], False)}
          </ol>
          {table(c.get("table"))}
          {before_ja(c)}
          <h3>Watch-outs</h3>
          <ul class="jw">{watch}</ul>
          <div class="ja-foot"><span>{G.EDITION}, updated {G.updated(c)}. Owner: {E(own)}. Sources: {E(src)}.</span><span>Questions: pcb@vanderbilt.edu</span></div>
        </article>
        {detailed_html}
      </div>
    </section>
    {record_html(c)}
  </div>
</main>
<p id="live" class="sr" role="status" aria-live="polite" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)"></p>
<footer>
  <div class="wrap">
    <p>HCM Academy &middot; {G.EDITION}. Sources: {E(src)}.</p>
    <p>An internal training prototype, not an official Vanderbilt University site. Questions or accessibility needs: <a href="mailto:pcb@vanderbilt.edu">pcb@vanderbilt.edu</a></p>
  </div>
</footer>
<script src="../course.js?v={ver('courses/course.js')}"></script>
</body>
</html>
'''

ASSESS = {
    "pre": dict(name="Pre-assessment", crumb="Before you begin", h1='Find your <em>starting</em> point.', time="About 5 min",
                desc="Two questions on each topic show what you already know, so you can start where it helps most.",
                meta=["Not graded", "Results point you to topics"],
                lede="Answer every question, then submit. It is not graded. Your results list the topics to start with."),
    "final": dict(name="Final assessment", crumb="Finish HCM Academy", h1='Show what you <em>know</em>.', time="About 15 min",
                  desc="Questions across every topic. Score 90% or higher to complete HCM Academy.",
                  meta=["90% to pass", "Retake if you need to"],
                  lede="Answer every question, then submit. You need 90% or higher to complete HCM Academy. If you miss it, your results list the topics to review before you retake it."),
}

def ver(rel):
    """Short content hash added to stylesheet and script URLs, so browsers fetch the new file after every change."""
    import hashlib
    return hashlib.sha1(open(os.path.join(ROOT, rel), "rb").read()).hexdigest()[:8]

def inline(rel):
    """Contents of a script file, inlined into the assessment pages so the page and its questions never get out of step in a browser cache."""
    return open(os.path.join(ROOT, rel), encoding="utf-8").read().replace("</script", "<\\/script").rstrip()

def assessment_counts():
    import re
    t = open(os.path.join(ROOT, "assets", "assessments.js"), encoding="utf-8").read()
    pre, final = t.split("\n  final:", 1)
    return {"pre": pre.count('"topic"'), "final": final.count('"topic"')}

def assessment_page(kind, count):
    a = ASSESS[kind]; back = "../../index.html"
    meta = "".join(f"<li>{E(m)}</li>" for m in [f"{count} questions", a["time"]] + a["meta"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{a["name"]} · HCM Academy</title>
<meta name="description" content="{E(a["desc"])}" />
<meta name="theme-color" content="#1C1C1C" />
<link rel="icon" href="../../assets/img/favicon.svg" type="image/svg+xml" />
<link rel="stylesheet" href="../../courses/course.css?v={ver('courses/course.css')}" />
<!-- Generated by tools/build_courses.py. Questions live in assets/assessments.js; edit there and rebuild. -->
</head>
<body>
<a href="#main" class="skip">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="{back}" aria-label="HCM Academy home"><img src="../../assets/img/vu-lockup-white.png" alt="" width="122" height="32" /><span class="mono" aria-hidden="true">HCM Academy</span></a>
    <a class="back" href="{back}">&larr; All courses</a>
  </div>
</header>
<section class="hero" aria-labelledby="t">
  <div class="wrap">
    <p class="mono crumb">HCM Academy &middot; {a["crumb"]}</p>
    <h1 id="t">{a["h1"]}</h1>
    <ul class="meta" aria-label="Assessment details">{meta}</ul>
  </div>
</section>
<main id="main" class="assess" data-kind="{kind}">
  <div class="wrap">
    <section class="part" id="locked" aria-labelledby="hl" hidden>
      <p class="mono num">Locked</p>
      <h2 id="hl">Finish every <em>course</em> first.</h2>
      <p>The final assessment unlocks when every course on your HCM Academy page is complete.</p>
      <div class="acts"><a class="btn" href="{back}">Back to all courses</a></div>
    </section>
    <section class="part quiz" id="questions" aria-labelledby="hq">
      <p class="mono num">{a["name"]}</p>
      <h2 id="hq">Answer every <em>question</em>.</h2>
      <p>{E(a["lede"])}</p>
      <form id="aform" novalidate>
        <div id="qs"></div>
        <div class="acts"><button type="submit" class="btn">Submit {a["name"].lower()}</button><span class="aerr" id="aerr" role="alert"></span></div>
      </form>
    </section>
    <section class="part" id="results" aria-labelledby="hr" tabindex="-1" hidden>
      <p class="mono num">Results</p>
      <h2 id="hr">Your <em>results</em>.</h2>
      <p class="score" id="ascore"></p>
      <ul class="topics" id="atopics"></ul>
      <div class="acts" id="aacts"></div>
    </section>
  </div>
</main>
<footer>
  <div class="wrap">
    <p>HCM Academy &middot; {G.EDITION}.</p>
    <p>An internal training prototype, not an official Vanderbilt University site. Questions or accessibility needs: <a href="mailto:pcb@vanderbilt.edu">pcb@vanderbilt.edu</a></p>
  </div>
</footer>
<!-- Questions and behavior are inlined so a cached copy of this page is always complete. -->
<script>
{inline('assets/assessments.js')}
</script>
<script>
{inline('assessment/assessment.js')}
</script>
</body>
</html>
'''

def build_assessments():
    counts = assessment_counts()
    for kind in ASSESS:
        d = os.path.join(ROOT, "assessment", kind); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(assessment_page(kind, counts[kind]))
    print(f"built assessments: pre {counts['pre']} questions, final {counts['final']} questions")

def build_changes():
    """changes/index.html: how updates work, who owns what area, and what changed, newest first."""
    from collections import Counter
    link = lambda c: f'<a href="../courses/{c["slug"]}/">{E(c["name"])}</a>'
    lst = lambda cs: "".join(f"<li>{link(c)}</li>" for c in cs)
    new = [c for c in COURSES if c["slug"] in G.NEW_IN_V02]
    bef = [c for c in COURSES if c["slug"] in G.BEFORE]
    rule = [c for c in COURSES if c["slug"] in G.TIME_CARD_RULE]
    counts = Counter(G.owner(c) for c in COURSES)
    owners = "".join(f'<tr><td data-th="Owner">{E(o)}</td><td data-th="Covers">{E(G.OWNER_SCOPE[o])}</td><td data-th="Courses">{counts[o]}</td></tr>' for o in (G.PAY, G.HIRE, G.TBD) if counts[o])
    unowned = f'<p class="tbc"><b>To confirm</b>An owner for the {counts[G.TBD]} courses marked To be named.</p>' if counts[G.TBD] else ""
    had_none = sum(1 for c in COURSES if G.owner_first(c) is None)
    back = "../index.html"; n_first = len(COURSES) - len(new)
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>What changed · HCM Academy</title>
<meta name="description" content="Changes to HCM Academy courses, by date, and who owns each area." />
<meta name="theme-color" content="#1C1C1C" />
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml" />
<link rel="stylesheet" href="../courses/course.css?v={ver('courses/course.css')}" />
<!-- Generated by tools/build_courses.py from tools/governance.py. Edit there and rebuild. -->
</head>
<body>
<a href="#main" class="skip">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="{back}" aria-label="HCM Academy home"><img src="../assets/img/vu-lockup-white.png" alt="" width="122" height="32" /><span class="mono" aria-hidden="true">HCM Academy</span></a>
    <a class="back" href="{back}">&larr; All courses</a>
  </div>
</header>
<section class="hero flat" aria-labelledby="t">
  <div class="wrap">
    <p class="mono crumb">HCM Academy &middot; Course updates</p>
    <h1 id="t">What <em>changed</em>.</h1>
    <ul class="meta" aria-label="Edition"><li class="v">{G.EDITION}</li><li>Updated {E(G.LATEST)}</li><li>{len(COURSES)} courses</li></ul>
  </div>
</section>
<main id="main">
  <div class="wrap">
    <section class="part" aria-labelledby="c1">
      <p class="mono num">How updates work</p>
      <h2 id="c1">Every change is <em>logged</em>.</h2>
      <p>Guidance goes out of date when a process changes and nobody says so. From {E(G.EDITION.split()[0])}, every course shows who owns it, its version, and the date it was last updated, and every change is listed on the course and on this page.</p>
      <ul class="plain">
        <li>Each course has a <b>Course record</b> at the bottom: owner, version, review status, and what changed.</li>
        <li>Pay-impacting courses carry a <b>Before you submit</b> block: what to attach, what to check, the cutoff, and who does what.</li>
        <li>Anything not yet confirmed is marked <b>To confirm</b> or listed as an open item, so nobody mistakes a draft for a rule.</li>
      </ul>
      <p class="tbc"><b>To confirm</b>Who tells HCMs when a pay-impacting course changes, how the notice is sent, and how often each course is reviewed.</p>
    </section>
    <section class="part" aria-labelledby="c2">
      <p class="mono num">Owners</p>
      <h2 id="c2">Which team owns each <em>course</em>.</h2>
      <p>The owning team keeps its courses current and confirms the open items. Owners are teams, not individuals.</p>
      <table class="ref tl"><caption>Course owners</caption><thead><tr><th scope="col">Owner</th><th scope="col">Covers</th><th scope="col">Courses</th></tr></thead><tbody>{owners}</tbody></table>
      {unowned}
    </section>
    <section class="part" aria-labelledby="c5">
      <p class="mono num">{E(G.OWNERS_SET)} &middot; {E(G.EDITION)}</p>
      <h2 id="c5">Owners are <em>teams</em>.</h2>
      <p>Each course is owned by a team. The owner shows at the top of the course, on its job aid, and in its Course record.</p>
      <ul class="plain">
        <li><b>{E(G.PAY)}</b> owns all payroll and financial topics: {counts[G.PAY]} courses.</li>
        <li><b>{E(G.HIRE)}</b> owns everything else, from recruiting and hiring through assignment changes, offboarding, leave, records and reporting, and the foundations: {counts[G.HIRE]} courses.</li>
      </ul>
      <p>The draft first showed the owners as Payroll and Finance and as Recruiting and Hiring, and {had_none} courses had no owner. Every course now has one.</p>
      <h3 class="rech">From Vanderbilt's published pages</h3>
      <p>These facts were read from the HR/Payroll Calendar for 2026 and 2027 and from the Vanderbilt Student Privacy Statement. They replace guesses and close open items.</p>
      <ul class="plain">
        <li><b>The Shared Administrative Calendar</b> now follows the published calendar: where it is, each cutoff, and when time cards are due.</li>
        <li><b>Monthly cutoff:</b> the 18th in most months and earlier in December. Courses that said the 15th to the 18th are corrected.</li>
        <li><b>Time cards:</b> due at noon on the Monday after the pay period ends. Holiday weeks move it.</li>
        <li><b>Off-cycle runs:</b> about two a month, with a cutoff of noon two days before.</li>
        <li><b>FERPA:</b> Vanderbilt's directory information list, and the University Registrar as the contact.</li>
      </ul>
      <p class="tbc"><b>To confirm</b>The 2027 calendar adds a Semi Monthly payroll that no course covers yet, and the Retro Change Cutoff used by the costing courses is not on the published calendar.</p>
    </section>
    <section class="part" aria-labelledby="c3">
      <p class="mono num">{E(G.UPDATED)} &middot; {E(G.EDITION)}</p>
      <h2 id="c3">Getting pay right the first <em>time</em>.</h2>
      <p>These changes add standard documents and checks, clearer ownership, cutoffs, the time card approval rule, and pay rules to the courses. All of it is a draft for the owners to confirm.</p>
      <h3 class="rech">New courses ({len(new)})</h3>
      <ul class="chgl">{lst(new)}</ul>
      <h3 class="rech">Before you submit added ({len(bef)})</h3>
      <ul class="chgl">{lst(bef)}</ul>
      <h3 class="rech">Time card approval rule added ({len(rule)})</h3>
      <ul class="chgl">{lst(rule)}</ul>
      <h3 class="rech">On every course ({len(COURSES)})</h3>
      <ul class="plain"><li>Owner, version, and updated date at the top, and a Course record with the change log at the bottom.</li></ul>
      <h3 class="rech">Assessment</h3>
      <ul class="plain"><li>Four questions added to the final assessment: time card approval, a change still pending at the cutoff, your part in a pay error, and what to attach.</li></ul>
    </section>
    <section class="part" aria-labelledby="c4">
      <p class="mono num">{E(G.FIRST)} &middot; V.01 draft</p>
      <h2 id="c4">First <em>drafts</em>.</h2>
      <p>{n_first} courses drafted from SME sessions, Vanderbilt guides, and official documentation, each with a walkthrough, a knowledge check, and a printable job aid.</p>
    </section>
  </div>
</main>
<footer>
  <div class="wrap">
    <p>HCM Academy &middot; {G.EDITION}.</p>
    <p>An internal training prototype, not an official Vanderbilt University site. Questions or accessibility needs: <a href="mailto:pcb@vanderbilt.edu">pcb@vanderbilt.edu</a></p>
  </div>
</footer>
</body>
</html>
'''
    d = os.path.join(ROOT, "changes"); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(doc)
    print(f"built changes page: {len(new)} new courses, {len(bef)} with Before you submit, owners {dict(counts)}")

def main():
    total = len(COURSES)
    for i, c in enumerate(COURSES, 1):
        d = os.path.join(ROOT, "courses", c["slug"]); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(c, i, total))
    print(f"built {total} courses")
    build_assessments()
    build_changes()
    sync_landing()

def sync_landing():
    """Keep the landing page rows (li[data-course]) in step with each course's name, use-when line, and time."""
    import re
    p = os.path.join(ROOT, "index.html")
    t = open(p, encoding="utf-8").read(); n = 0
    esc = lambda s: html.escape(s, quote=False)
    for c in COURSES:
        pat = re.compile(r'(<li(?: class="sub")? data-course="' + c["slug"] + r'"><span class="nm"><span class="tt">)[^<]*(</span><span class="ds">)[^<]*(</span></span><span class="tm"><span class="sr-l">Time: </span>)[^<]*(</span>)')
        t, k = pat.subn(lambda m: m.group(1) + esc(c["name"]) + m.group(2) + esc(c["use_when"]) + m.group(3) + esc(c["time"]) + m.group(4), t); n += k
    open(p, "w", encoding="utf-8").write(t)
    print(f"synced {n} landing rows")

if __name__ == "__main__":
    main()

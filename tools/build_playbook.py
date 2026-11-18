#!/usr/bin/env python3
"""Build the HCM Playbook: every course job aid in one branded, print-ready document.
Writes playbook/index.html (fixed US Letter pages). Render the PDF with:
  python3 tools/build_playbook.py && node tools/render_playbook.cjs"""
import html, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from course_content import COURSES  # noqa: E402
import governance as G  # noqa: E402
ROOT = os.path.dirname(HERE)
E = lambda s: html.escape(str(s), quote=True)
SITE = "me5231979.github.io/HCM_Academy"
EDITION = f"{G.EDITION} · {G.EDITION_MONTH}"
TABLE_ROWS = 16   # rows of a long table on each continuation page

# Topic order, names, and blurbs come from the landing page cards; course order follows the rows.
landing = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
TOPICS = []
for m in re.finditer(r'<section class="card[^"]*" id="([a-z]+)" data-short="([^"]*)">(.*?)</section>', landing, re.S):
    cid, short, body = m.groups()
    name = html.unescape(re.search(r"<h3>(.*?)</h3>", body).group(1))
    blurb = html.unescape(re.search(r"</h3>\s*<p>(.*?)</p>", body, re.S).group(1))
    no = re.search(r'<span class="no"[^>]*>(\d+)</span>', body).group(1)
    slugs = re.findall(r'data-course="([^"]+)"', body)
    TOPICS.append(dict(id=cid, short=html.unescape(short), name=name, blurb=blurb, no=no, slugs=slugs))
BY = {c["slug"]: c for c in COURSES}

def steps_html(steps, start=1):
    out = []
    for i, s in enumerate(steps, start):
        sub = "".join(f"<li>{E(x)}</li>" for x in s.get("sub", []))
        out.append(f'<li><span class="n">{i}</span><div><p class="st">{E(s["t"])}</p>{f"<ul>{sub}</ul>" if sub else ""}</div></li>')
    return "\n".join(out)

def table_html(tb, rows=None, part=""):
    if not tb: return ""
    head = "".join(f"<th>{E(h)}</th>" for h in tb["head"])
    body = "".join("<tr>" + "".join(f"<td>{E(c)}</td>" for c in r) + "</tr>" for r in (tb["rows"] if rows is None else rows))
    return f'<table class="c{len(tb["head"])}"><caption>{E(tb["title"])}{E(part)}</caption><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'

def before_html(c):
    """Before you submit, in three lines: attach, check, cutoff (from tools/governance.py)."""
    b = G.before(c["slug"])
    if not b: return ""
    lines = [f"<li><b>Attach</b>{E(G.attach_line(b))}</li>", f"<li><b>Check</b>{E(' '.join(b['checks']))}</li>"]
    if b.get("cutoff"): lines.append(f"<li><b>Cutoff</b>{E(G.CUTOFF_SHORT[b['cutoff']])}</li>")
    return f'<div class="before"><p class="wh">{E(b.get("title", "Before you submit"))}</p><ul>{"".join(lines)}</ul></div>'

GUIDE_CHARS = 2200  # a guide with more text than this moves its table to its own page

def long_table(c):
    """True when the table gets its own page(s): too many rows, or too much text to share the guide's page."""
    if not c.get("table"): return False
    text = sum(len(s["t"]) + sum(map(len, s.get("sub", []))) for s in c["steps"]) + sum(map(len, c["watch"]))
    text += sum(len(" ".join(map(str, r))) for r in c["table"]["rows"])
    return len(c["table"]["rows"]) > TABLE_ROWS or text > GUIDE_CHARS

def chrome(topic, page, inner, cls=""):
    return (f'<section class="page guide {cls}"><header class="run"><span>HCM Playbook</span><span>{E(topic["no"])} &middot; {E(topic["short"])}</span></header>'
            f'{inner}<footer class="foot"><span>{E(EDITION)} &middot; Questions: pcb@vanderbilt.edu</span><span class="pg">{page:02d}</span></footer></section>')

def _w(s):
    """Rough height of a step on the page, in lines."""
    return 1.2 + len(s["t"]) / 80 + sum(1 + len(x) / 95 for x in s.get("sub", []))

STEP_LINES = (24, 40)   # lines of steps on a guide's first page, and on a continuation page

def guide_pages(c, topic, start):
    """A guide, continued onto extra pages when its steps don't fit on one."""
    draft = '<span class="tag">Pending SME review</span>' if c.get("pending", "").startswith("Built from") else ""
    watch = "".join(f"<li>{E(w)}</li>" for w in c["watch"])
    tb = "" if long_table(c) else table_html(c.get("table"))   # a long table gets its own pages
    tail = (f'{tb}{before_html(c)}<div class="watch"><p class="wh">Watch-outs</p><ul>{watch}</ul></div>'
            f'<p class="src">Course: {SITE}/courses/{E(c["slug"])}/ &middot; Sources: {E("; ".join(c["sources"]))}</p>')
    head = (f'<div class="head"><p class="eyebrow">{E(c["topic_label"])}</p><h2>{E(c["name"])}</h2>'
            f'<p class="meta"><span>{E(c["system"])}</span><span>{E(c["time"])} micro-learning</span><span>Owner: {E(G.owner(c))}</span>{draft}</p>'
            f'<p class="use"><b>Use when</b>{E(c["use_when"])}</p></div>')
    chunks, cur, room = [], [], STEP_LINES[0]
    for s in c["steps"]:
        if cur and sum(map(_w, cur)) + _w(s) > room:
            chunks.append(cur); cur, room = [], STEP_LINES[1]
        cur.append(s)
    chunks.append(cur)
    tail_lines = (len(c.get("table", {}).get("rows", [])) * 1.6 if tb else 0) + (6 if before_html(c) else 0) + sum(1 + len(w) / 95 for w in c["watch"]) + 3
    split_tail = len(chunks) > 1 and sum(map(_w, chunks[-1])) + tail_lines > STEP_LINES[1] + 6
    pages, n = [], 1
    for k, ch in enumerate(chunks):
        top = head if k == 0 else f'<div class="head"><p class="eyebrow">{E(c["name"])} &middot; continued</p></div>'
        last = k == len(chunks) - 1
        pages.append(chrome(topic, start + len(pages), f'{top}<ol class="steps">{steps_html(ch, n)}</ol>' + (tail if last and not split_tail else "")))
        n += len(ch)
    if split_tail:
        pages.append(chrome(topic, start + len(pages), f'<div class="head"><p class="eyebrow">{E(c["name"])} &middot; continued</p></div>' + tail))
    return pages

def table_pages(c, topic, start):
    """Continuation pages for a table too long to share the guide's page."""
    tb = c["table"]; rows = tb["rows"]; chunks = [rows[k:k + TABLE_ROWS] for k in range(0, len(rows), TABLE_ROWS)]
    pages = []
    for i, ch in enumerate(chunks, 1):
        head = f'<div class="head"><p class="eyebrow">{E(c["name"])}</p></div>'
        pages.append(chrome(topic, start + len(pages), head + table_html(tb, ch, f" · {i} of {len(chunks)}" if len(chunks) > 1 else ""), "tablepage"))
    return pages

def detail_pages(c, topic, start):
    det = c["detailed"]; pages = []; st = det["steps"]
    for k in range(0, len(st), 2):
        items = "".join(
            f'<li><p class="st"><span class="dn">{i:02d}</span>{E(x["t"])}</p><p class="dd">{E(x["d"])}</p>'
            + (f'<img src="../courses/{E(c["slug"])}/img/{E(x["img"])}" alt="Screenshot: {E(x["t"].rstrip("."))}" />' if x.get("img") else "") + '</li>'
            for i, x in enumerate(st[k:k + 2], k + 1))
        head = (f'<div class="head"><p class="eyebrow">Detailed job aid &middot; {E(c["name"])}</p><h2>{E(det["title"])}</h2>'
                f'<p class="meta"><span>{E(det["source"])}</span></p></div>') if k == 0 else ""
        pages.append(chrome(topic, start + len(pages), f'{head}<ol class="dsteps">{items}</ol>', "detail"))
    return pages

# Paginate: cover 1, how to use 2, contents 3, then a divider and the guides for each topic.
page = 4; body = []; toc = []
for t in TOPICS:
    t["page"] = page; entries = []
    divider_at = page; page += 1; guides = []
    for sl in t["slugs"]:
        c = BY[sl]; entries.append((c["name"], page)); d = guide_pages(c, t, page); guides += d; page += len(d)
        if long_table(c):
            d = table_pages(c, t, page); guides += d; page += len(d)
        if c.get("detailed"):
            d = detail_pages(c, t, page); guides += d; page += len(d)
    t["entries"] = entries
    lst = "".join(f'<li><span>{E(n)}</span><i></i><b>{p:02d}</b></li>' for n, p in entries)
    body.append(f'<section class="page divider"><p class="dno">{E(t["no"])}</p><div class="dtext"><p class="eyebrow">Section {E(t["no"])}</p>'
                f'<h2>{E(t["name"])}</h2><p class="blurb">{E(t["blurb"])}</p></div><ol class="dlist">{lst}</ol>'
                f'<footer class="foot"><span>HCM Playbook</span><span class="pg">{divider_at:02d}</span></footer></section>')
    body += guides
total = page - 1

toc_html = "".join(
    f'<div class="ts"><p class="tt"><span class="tn">{E(t["no"])}</span>{E(t["name"])}<b>{t["page"]:02d}</b></p><ul>'
    + "".join(f'<li><span>{E(n)}</span><i></i><b>{p:02d}</b></li>' for n, p in t["entries"]) + "</ul></div>"
    for t in TOPICS)
topics_strip = "".join(f'<li><b>{E(t["no"])}</b>{E(t["short"])}</li>' for t in TOPICS)
n_guides = sum(len(t["entries"]) for t in TOPICS)

doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>HCM Playbook · HCM Academy</title>
<meta name="description" content="Every HCM Academy quick guide in one branded, printable playbook." />
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml" />
<link rel="stylesheet" href="playbook.css" />
<!-- Generated by tools/build_playbook.py from tools/course_content.py. Do not edit by hand. -->
</head>
<body>
<p class="screen-bar"><a href="../index.html">&larr; HCM Academy</a><a href="HCM_Playbook.pdf" download>Download the PDF</a></p>
<main>
<section class="page cover">
  <img class="lockup" src="../assets/img/vu-lockup-white.png" alt="Vanderbilt University" />
  <img class="mark" src="../assets/img/vu-v-icon.png" alt="" />
  <div class="ctext">
    <p class="eyebrow">Vanderbilt University &middot; HCM Academy</p>
    <h1>The HCM <em>Playbook</em>.</h1>
    <p class="sub">Quick guides for the people work you own: hiring, pay and time, assignments, leave, costing, students and faculty, and records.</p>
  </div>
  <ol class="strip">{topics_strip}</ol>
  <p class="edition">{E(EDITION)} &middot; {n_guides} quick guides</p>
</section>
<section class="page intro">
  <header class="run"><span>HCM Playbook</span><span>How to use it</span></header>
  <p class="eyebrow">Before you start</p>
  <h2>How to use this <em>playbook</em>.</h2>
  <div class="cols">
    <div><p class="k">01</p><h3>Find the task</h3><p>Guides are grouped into the eight HCM Academy topics. Use the contents page, or go to the topic's divider page for its list.</p></div>
    <div><p class="k">02</p><h3>Follow the steps</h3><p>Each guide is one page: when to use it, the steps in order, and the watch-outs that cause send-backs. The same steps are in the matching micro-learning course.</p></div>
    <div><p class="k">03</p><h3>Check before you submit</h3><p>Pay-impacting guides end with Before you submit: what to attach, what to check, and the cutoff. Bad data in is bad data out: what you enter flows into pay, costing, and reports.</p></div>
  </div>
  <div class="note"><p><b>Where things are.</b> Oracle: Home page &gt; Our Workforce &gt; Quick Actions (Show More). Employee records: Our Workforce &gt; Employment Info. UKG: Oracle Me tab &gt; Apps &gt; UKG (Kronos) Timesheets. Track approvals with the notifications bell.</p>
  <p><b>This is a {E(G.EDITION)}.</b> Guides marked <span class="tag">Pending SME review</span> were built from official documentation or from other guides and are waiting on Vanderbilt review. Each guide names the area that owns it. Anything marked To confirm is not yet a rule. The payroll calendar and your PCB consultant are the source of truth.</p>
  <p><b>Online.</b> Every guide links to its course at {SITE}. Questions: pcb@vanderbilt.edu</p></div>
  <footer class="foot"><span>{E(EDITION)}</span><span class="pg">02</span></footer>
</section>
<section class="page contents">
  <header class="run"><span>HCM Playbook</span><span>Contents</span></header>
  <h2><em>Contents</em>.</h2>
  <div class="toc">{toc_html}</div>
  <footer class="foot"><span>{E(EDITION)}</span><span class="pg">03</span></footer>
</section>
{chr(10).join(body)}
<section class="page back">
  <img class="lockup" src="../assets/img/vu-centered-white.png" alt="Vanderbilt University" />
  <p class="eyebrow">HCM Academy</p>
  <p class="bq">Learn the work. Share what works. Meet the people doing the same job. Get answers when something comes up.</p>
  <p class="edition">Questions or corrections: pcb@vanderbilt.edu &middot; {SITE}</p>
</section>
</main>
</body>
</html>
'''
os.makedirs(os.path.join(ROOT, "playbook"), exist_ok=True)
open(os.path.join(ROOT, "playbook", "index.html"), "w", encoding="utf-8").write(doc)
print(f"playbook: {total + 1} pages ({n_guides} guides, {len(TOPICS)} sections)")

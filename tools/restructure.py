# Start Here, slimmed from nine courses to six (Nov 18, 2026), with nothing dropped:
#   What is an HCM?  (new)  + Who owns what
#   Oracle HCM structure    + Data integrity
#   Quick actions           + Workflow and worklists
#   Employee or contractor  + I-9 and background checks by worker type
# A merged course keeps every step, table, watch-out, and question of its parts, in order, and shows each part's
# video as Part 1 and Part 2. Its job aid pictures are the parts' stills (a part's files are renamed <part>-step-NN.jpg
# in the merged course's folder). The old addresses become redirect pages (tools/build_redirects.py).
import videos as V

NOTE = "New course: what the HCM role is, who HCMs serve and work with, and their part in each area. Who owns what is now part of it."

ROLE = dict(
    slug="what-is-an-hcm", topic="start", topic_label="Start Here",
    title_pre="The role of the", title_em="HCM", name="What is an HCM?", system="Overview", time="8 min",
    sources=["HCM Academy: the HCM role (home page)", "The other HCM Academy courses"],
    intro=["At Vanderbilt, HCM is a role. HCMs work inside the business: they sit in schools, departments, and units across "
           "Vanderbilt, close to the managers and employees they support, and they own the people work for their area.",
           "HCMs do that work in Oracle HCM, Oracle's human capital management system, and in UKG for time. This course shows "
           "what the role covers, who HCMs work with, and who owns each part of the work."],
    use_when="You are new to the HCM role, or you want to see everything the role covers before you start the other courses.",
    steps_title="The role, and who owns what",
    steps=[
        {"t": "HCM means the role: you.",
         "d": "In HCM Academy, an HCM is the person who owns the people work for the departments and teams in their area. "
              "Oracle HCM is the system HCMs use to do that work. When a course means the system, it says Oracle HCM."},
        {"t": "You serve the departments and teams in your area.",
         "d": "You sit close to the managers and employees you support. You enter the hires, changes, and terminations "
              "their work needs, and you check that time and pay are right, working with managers, FUMs, and others."},
        {"t": "You do the work in Oracle HCM and UKG.",
         "d": "You reach Oracle HCM through Our Workforce on the Oracle home page. Payroll can only pay what the record says.",
         "sub": ["Oracle HCM: positions, requisitions, hires, assignment changes, terminations, leave, costing, document records, and reports.",
                 "UKG (Kronos): weekly time cards and time off for non-exempt staff."]},
        {"t": "Your work covers seven areas.",
         "d": "Each area has its own topic in HCM Academy.",
         "sub": ["Hiring: positions, the compensation memo, requisitions, background checks, and converting pending workers.",
                 "Payroll and time cards: weekly time card checks, one-time payments, supplements, and off-cycle requests.",
                 "Assignments: changes to hours, salary, and managers; transfers, promotions, and terminations.",
                 "Leave: FMLA and TMLA transactions, and exempt time off, in Oracle.",
                 "Costing: entering costing with the string from your FUM, and checking it before every cutoff.",
                 "Students and faculty: student workers, faculty, and their assignments between terms.",
                 "Records and reporting: document records and the reports your area needs."]},
    ],
    watch=["When a course says HCM, it means you, the role. When it means the system, it says Oracle HCM.",
           "Payroll can only pay what the record says, and you enter the record."],
    docs=[],
    quiz=[{"q": "In HCM Academy, what does HCM mean?",
           "o": ["Oracle's human capital management system", "The role: the person who owns the people work for their area", "Central HR"],
           "a": 1, "why": "HCM is the role. Oracle HCM is the system HCMs use to do the work."},
          {"q": "Where does the costing string for a hire come from?",
           "o": ["Your FUM (financial unit manager)", "Payroll", "The new hire"],
           "a": 0, "why": "Get the costing string from your FUM. In many areas the FUM also enters costing."}],
)

MERGES = [
    dict(slug="what-is-an-hcm", parts=["what-is-an-hcm", "who-owns-what"], before="hcm-structure",
         name=ROLE["name"], title_pre=ROLE["title_pre"], title_em=ROLE["title_em"], system="Overview", time="10 min",
         intro=ROLE["intro"], use_when=ROLE["use_when"], steps_title=ROLE["steps_title"]),
    dict(slug="hcm-structure", parts=["hcm-structure", "data-integrity"],
         name="Oracle HCM structure and data integrity", title_pre="How Oracle HCM is organized, and why its", title_em="data matters",
         system="Overview", time="10 min", steps_title="How the pieces fit, and why every field matters",
         intro=["Oracle HCM stores every person inside a set of structures: who legally employs them, which business unit and work unit "
                "they belong to, what job and position they hold, and how they are paid. Each transaction you submit changes one or more of them.",
                "One record feeds the next. A wrong value on a position or assignment does not stay put; it flows into pay, costing, and every "
                "report built on it. Getting it right the first time is far cheaper than fixing it after payroll runs."],
         use_when="You are new to Oracle HCM, a screen uses a term you are not sure about, or you are entering person, position, or assignment data."),
    dict(slug="quick-actions-person-info", parts=["quick-actions-person-info", "workflow-worklists"],
         name="Working in Oracle HCM: find a person, read the record, track approvals",
         title_pre="Find a person, read the record, and track your", title_em="approvals",
         system="Oracle HCM", time="9 min", steps_title="Find, read, and track",
         intro=["Almost every HCM task starts the same way: open Our Workforce, pick a quick action, and search for the person. Before you "
                "change anything, read the Employment Info page so you know the current assignment and recent history.",
                "Most transactions you submit do not take effect right away. They route to approvers, so know where to look, and what "
                "Withdraw and Request More Information do, to keep transactions from stalling before the payroll cutoff."],
         use_when="You need to look up a person, start a transaction for someone in your area, or check where a transaction you submitted is."),
    dict(slug="i9-background-by-worker-type", parts=["employee-vs-contractor", "i9-background-by-worker-type"],
         name="Worker types, classification, and required checks", title_pre="Classify the worker, then match the", title_em="checks",
         system="Process", time="10 min", steps_title="How to decide",
         intro=["Whether someone is an employee or an independent contractor is set by law and the facts of the work, not by what anyone calls "
                "it or how they want to be paid. Misclassifying a worker can mean unpaid taxes, missed overtime, and penalties.",
                "Once you know the worker type, match the checks to it. Federal law requires a Form I-9 for every employee, and Vanderbilt "
                "requires background checks for some worker types. Get it wrong and you delay a start, or start someone without clearance."],
         use_when="You are bringing on a new person, or someone wants to pay a person through a contract or invoice instead of hiring them."),
]
REMOVED = {"who-owns-what": "what-is-an-hcm", "data-integrity": "hcm-structure",
           "workflow-worklists": "quick-actions-person-info", "employee-vs-contractor": "i9-background-by-worker-type"}
NOTES = {
    "hcm-structure": "Data integrity: bad data in, bad data out is now part of this course, as Part 2.",
    "quick-actions-person-info": "Oracle HCM Workflow and Worklists is now part of this course, as Part 2.",
    "i9-background-by-worker-type": "Employee or independent contractor? is now part of this course, as Part 1.",
}
_MIXED = "Pictures from the course's explainer videos: diagrams for concepts, and training-simulation screens of Oracle HCM with fictional names."

def _uniq(xs):
    out = []
    for x in xs:
        if x not in out: out.append(x)
    return out

import re
_FUM = re.compile(r"\bFUM\b(?! \()")

def define_fum(c):
    """Spell out FUM the first time a course uses it, unless the course already defines it."""
    if re.search("financial unit manager", str(c), re.I): return
    done = [False]
    def fix(s):
        if done[0] or not isinstance(s, str) or not _FUM.search(s): return s
        done[0] = True
        return _FUM.sub("FUM (financial unit manager)", s, count=1)
    c["intro"] = [fix(x) for x in c["intro"]]
    c["use_when"] = fix(c["use_when"])
    for s in c["steps"]:
        s["t"] = fix(s["t"]); s["d"] = fix(s.get("d", ""))
        if s.get("sub"): s["sub"] = [fix(x) for x in s["sub"]]
    if c.get("table"): c["table"] = dict(c["table"], rows=[[fix(x) for x in r] for r in c["table"]["rows"]])
    c["watch"] = [fix(x) for x in c["watch"]]

def apply(courses, verify):
    by = {c["slug"]: c for c in courses}
    role = dict(ROLE); role["pending"] = by["who-owns-what"]["pending"]
    role["video"] = {"src": "video/what-is-an-hcm.mp4", "poster": "video/what-is-an-hcm.jpg", "title": "What an HCM does", "narrated": True, "kind": "board"}
    role["detailed"] = {"title": "The HCM role", "source": V.BOARD,
                        "steps": [{"t": s["t"], "d": s.get("d", ""), "img": f"step-{i:02d}.jpg"} for i, s in enumerate(role["steps"], 1)]}
    by["what-is-an-hcm"] = role
    merged = {}
    for m in MERGES:
        parts = [by[p] for p in m["parts"]]
        c = dict(by[m["slug"]] if m["slug"] in by else parts[0])
        c.update({k: m[k] for k in ("slug", "name", "title_pre", "title_em", "system", "time", "intro", "use_when", "steps_title")})
        c["topic"], c["topic_label"] = parts[0]["topic"], parts[0]["topic_label"]
        c["steps"] = [s for p in parts for s in p["steps"]]
        c["watch"] = [w for p in parts for w in p["watch"]]
        c["quiz"] = [q for p in parts for q in p["quiz"]]
        c["sources"] = _uniq([s for p in parts for s in p["sources"]])
        c["docs"] = _uniq([d for p in parts for d in p.get("docs", [])])
        tables = [p["table"] for p in parts if p.get("table")]
        c.pop("table", None)
        if tables: c["table"] = tables[0]
        pend = [p.get("pending", "") for p in parts]
        c["pending"] = next((x for x in pend if not x.startswith("Reviewed")), pend[0])
        vids, det = [], []
        for n, p in enumerate(parts, 1):
            own = p["slug"] == m["slug"]
            v = dict(p["video"]); v["part"] = n
            if not own: v["src"], v["poster"] = f"video/{p['slug']}.mp4", f"video/{p['slug']}.jpg"
            vids.append(v)
            for x in p["detailed"]["steps"]:
                det.append(dict(x, img=x["img"] if own else f"{p['slug']}-{x['img']}"))
        c["videos"], c["video"] = vids, vids[0]
        srcs = {p["detailed"]["source"] for p in parts}
        c["detailed"] = {"title": c["name"] + ", step by step", "source": srcs.pop() if len(srcs) == 1 else _MIXED, "steps": det}
        vf = _uniq([x for p in m["parts"] for x in verify.get(p, [])])
        if vf: verify[m["slug"]] = vf
        merged[m["slug"]] = c
    for gone in REMOVED: verify.pop(gone, None)
    out = []
    for c in courses:
        if c["slug"] in REMOVED: continue
        if c["slug"] == "hcm-structure": out.append(merged["what-is-an-hcm"])
        out.append(merged.get(c["slug"], c))
    courses[:] = out
    for c in courses: define_fum(c)
    return courses

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
    # Across the sections (Nov 18, 2026): awareness and best-practice courses fold into the process they extend, or into one
    # essentials course per section. Steps and processes stay standalone.
    dict(slug="create-position", parts=["create-position", "position-best-practices"],
         name="Create a position", title_pre="Create a", title_em="position", system="Oracle HCM", time="11 min",
         steps_title="Create the position, then keep it clean",
         intro=["Every hire starts with a position. The requisition is built from it, and the new hire's assignment inherits from it, so a "
                "mistake here follows the person all the way through. First decide whether you need a new position or an update to an existing one.",
                "Most position approval errors come from inaccurate or outdated positions and a few easy-to-miss fields. The best practices at the "
                "end keep positions active, clean, and correct."],
         use_when="You need a new position for a hire, or you manage positions for your business unit and want to avoid send-backs."),
    dict(slug="create-requisition", parts=["create-requisition", "executive-search"],
         name="Create a requisition", title_pre="Create a", title_em="requisition", system="Oracle Recruiting", time="11 min",
         steps_title="Create the requisition, and when a search firm is involved",
         intro=["A requisition is the request to recruit. It's built from a position, and it copies that position the moment you submit, so check "
                "the position first. Vanderbilt's recruiting is outsourced to Cielo, which bills for every opening and every fill.",
                "Executive roles usually go to a search firm, which changes how the requisition is created. The last steps cover that case."],
         use_when="An approved position needs to be filled, including through an executive search or an outside search firm."),
    dict(slug="hcm-role-in-payroll", parts=["hcm-role-in-payroll", "pay-rules", "comp-impacts-payroll", "common-pay-errors"],
         name="Payroll essentials: your role, pay rules, and common errors", title_pre="Get pay right: your role, the rules, and the common",
         title_em="errors", system="Overview", time="15 min", steps_title="Your role, the rules, how a change pays, and the errors to catch",
         intro=["HCMs don't run payroll. Payroll runs payroll. Your job is getting records and time cards right so payroll can run cleanly.",
                "This course covers what you own and what payroll owns, the pay rules that change non-exempt pay, which paycheck a change will hit, "
                "and the errors that most often cause a late or wrong paycheck."],
         use_when="You are new to the HCM role, you are not sure whether a pay issue is yours, or you want to check your work before a cutoff."),
    dict(slug="ukg-time-cards", parts=["weekly-time-card-check", "ukg-time-cards"], detailed_from="weekly-time-card-check",
         name="UKG time cards: the weekly check, edits, and time off", title_pre="Check, fix, and add time off on UKG", title_em="time cards",
         system="UKG (Kronos)", time="13 min", steps_title="The weekly check, then editing time and entering PTO",
         intro=["Non-exempt (weekly and biweekly) pay depends on UKG time cards. The employee submits, the line manager approves, and payroll "
                "signs off before payroll runs. Run the weekly check so no one is paid late or wrong.",
                "Your part as the HCM is to check, follow up, and step in when an employee can't enter their own time. Approving is the line manager's job."],
         use_when="Every week for your non-exempt employees, or when you need to enter hours or PTO for an employee who can't."),
    dict(slug="transfer-without-requisition", parts=["transfer-with-requisition", "transfer-without-requisition"],
         name="Transfers and promotions: with or without a requisition", title_pre="Transfer or promote, with or without a", title_em="requisition",
         system="Oracle HCM", time="7 min", steps_title="Who processes it, then how you submit one",
         intro=["When an employee applies for and gets a job through a requisition, the transfer or promotion flows from recruiting. Central HR "
                "processes it, not the HCM.",
                "Without a requisition, the HCM in the employee's current business unit submits the transfer: an organization transfer planned "
                "within the business unit, or a transfer to faculty status."],
         use_when="An employee is moving to a new job, through recruiting or a move planned within your business unit."),
    dict(slug="end-assignment-vs-terminate", parts=["end-assignment-vs-terminate", "terminate-multiple-assignments"],
         name="End an assignment or terminate employment, including multiple assignments", title_pre="End one job, or end", title_em="employment",
         system="Oracle HCM", time="8 min", steps_title="Decide which, then handle more than one job",
         intro=["Oracle has two ways to end work. End Assignment stops one job. Terminate Employment ends the whole work relationship and every "
                "assignment in it, including jobs in other areas.",
                "Picking the wrong one either leaves a job running that should have stopped, or stops a job the person is keeping. When someone "
                "holds more than one job, check every job and talk to the other HCM before you submit."],
         use_when="Someone is leaving a job, and you need to decide whether they leave one job or Vanderbilt employment, including when they hold more than one job."),
    dict(slug="costing-fundamentals", parts=["costing-fundamentals", "costing-impacts", "when-to-update-costing"],
         name="Costing essentials: what it is, why it matters, and when to update it", title_pre="Costing: what it is, why it matters, and when to",
         title_em="update it", system="Oracle HCM", time="15 min", steps_title="How Oracle picks the account, how costing flows, and when to check it",
         intro=["Payroll costing decides which costing string (COA or POET) pays for a person's compensation, and for which periods. Each payroll "
                "run turns pay into costing results that move to the General Ledger, so wrong costing means wrong department, grant, and project financials.",
                "An assignment with no costing is not an error: the work unit default applies. Changes to a job or funding may require a costing "
                "update, and fixing costing after payroll runs takes a retro cost transfer."],
         use_when="You set up or review costing for a hire, transfer, or funding change, or you need to decide whether an employee can stay on the default."),
    dict(slug="add-assignment", parts=["work-relationship-vs-assignment", "add-assignment"],
         name="Add Assignment, or add a work relationship?", title_pre="Add an assignment, or a work", title_em="relationship",
         system="Oracle HCM", time="8 min", steps_title="Pick the action, then add the assignment",
         intro=["In Oracle, a person has one person record, one or more work relationships with a legal employer, and one or more assignments "
                "inside each work relationship. The record the person already has tells you which action to use.",
                "Add Assignment gives a person a second job inside the work relationship they already have. The first job keeps running; the new "
                "one gets its own position, hours, salary, and manager."],
         use_when="A person already in Oracle is taking on another job, or you are setting up paid work for a student."),
    dict(slug="bi-intro-playbook", parts=["bi-intro-playbook", "reporting-101"],
         name="Reporting basics: BI reporting, the Departmental Playbook, and running reports", title_pre="Run the reports your area", title_em="needs",
         system="Oracle BI (OTBI)", time="9 min", steps_title="Start with the Playbook, then run and read a report",
         intro=["Oracle Transactional Business Intelligence (OTBI) reports on live Oracle HCM data. You use it to check your area's people, "
                "assignments, and costing without opening records one at a time. The Departmental Playbook gives HCMs a starting set of reports.",
                "Most of your reporting is running a report someone already built and reading the results correctly. The key choices are the "
                "prompts you answer and the date you run it for."],
         use_when="You need a list or check across your area, such as everyone's costing, or you need to run an existing report and trust what it shows."),
]
REMOVED = {"who-owns-what": "what-is-an-hcm", "data-integrity": "hcm-structure",
           "workflow-worklists": "quick-actions-person-info", "employee-vs-contractor": "i9-background-by-worker-type",
           "position-best-practices": "create-position", "executive-search": "create-requisition",
           "pay-rules": "hcm-role-in-payroll", "comp-impacts-payroll": "hcm-role-in-payroll", "common-pay-errors": "hcm-role-in-payroll",
           "weekly-time-card-check": "ukg-time-cards", "transfer-with-requisition": "transfer-without-requisition",
           "terminate-multiple-assignments": "end-assignment-vs-terminate", "costing-impacts": "costing-fundamentals",
           "when-to-update-costing": "costing-fundamentals", "work-relationship-vs-assignment": "add-assignment", "reporting-101": "bi-intro-playbook"}
NOTES = {
    "hcm-structure": "Data integrity: bad data in, bad data out is now part of this course, as Part 2.",
    "quick-actions-person-info": "Oracle HCM Workflow and Worklists is now part of this course, as Part 2.",
    "i9-background-by-worker-type": "Employee or independent contractor? is now part of this course, as Part 1.",
    "create-position": "Position management best practices is now part of this course: its habits are the last steps.",
    "create-requisition": "Executive or external search is now part of this course: the last steps, with its video as Part 2.",
    "hcm-role-in-payroll": "Now Payroll essentials: Pay rules, Compensation impacts on payroll processing, and Common pay errors are part of this course.",
    "ukg-time-cards": "Weekly time card check is now part of this course, as its first steps.",
    "transfer-without-requisition": "Transfer or promotion from a requisition is now part of this course, as its first steps.",
    "end-assignment-vs-terminate": "How to handle a termination when an employee has multiple assignments is now part of this course.",
    "costing-fundamentals": "Now Costing essentials: How costing impacts payroll and financial reporting, and When costing must be updated, are part of this course.",
    "add-assignment": "Add a Work Relationship or add an Assignment? is now part of this course, as its first steps.",
    "bi-intro-playbook": "Now Reporting basics: Reporting 101 is part of this course.",
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
        vids, det, srcs = [], [], set()
        for p in parts:
            own = p["slug"] == m["slug"]
            if p.get("video", {}).get("src", "").endswith(".mp4"):     # an embedded (non-mp4) video is not carried into a merge
                v = dict(p["video"]); v["part"] = len(vids) + 1
                if not own: v["src"], v["poster"] = f"video/{p['slug']}.mp4", f"video/{p['slug']}.jpg"
                vids.append(v)
            if m.get("detailed_from") and p["slug"] != m["detailed_from"]: continue
            if p.get("detailed"):
                srcs.add(p["detailed"]["source"])
                for x in p["detailed"]["steps"]:
                    det.append(dict(x, img=x["img"] if own else f"{p['slug']}-{x['img']}"))
            else:
                det += [{"t": s["t"], "d": s.get("d", ""), "img": None} for s in p["steps"]]
        c.pop("videos", None); c.pop("video", None); c.pop("detailed", None)
        if len(vids) > 1: c["videos"] = vids
        if vids: c["video"] = vids[0]
        if any(x["img"] for x in det):
            c["detailed"] = {"title": (by[m["detailed_from"]]["detailed"]["title"] if m.get("detailed_from") else c["name"] + ", step by step"), "source": srcs.pop() if len(srcs) == 1 else _MIXED, "steps": det}
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

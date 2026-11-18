# Explainer videos and screenshot job aids, by course. Each video is built from tools/video/<slug>.html
# (see README, Explainer videos). The detailed job aid reuses the course's own steps, one still per step,
# so the job aid and the course never disagree.
SIM = "Screens from the HCM Academy training simulation of Oracle HCM. Names are fictional; check labels against Vanderbilt's Oracle."
BOARD = "Diagrams from the HCM Academy explainer video. The steps are the course's own."

VIDEOS = {
    "compensation-memo": dict(title="Getting the compensation memo", aid="Getting the compensation memo, step by step", source=BOARD),
    "background-checks": dict(title="Background checks in Oracle Recruiting", aid="Background checks, step by step", source=SIM),
    "executive-search": dict(title="Executive or external search in Oracle Recruiting", aid="Executive or external search, step by step", source=SIM),
    "hire-staff": dict(title="Hiring staff: the whole chain", aid="Hiring staff, from memo to day one", source=BOARD),
    "create-position": dict(title="Create a position in Oracle HCM", aid="Creating a position, step by step", source=SIM),
    "update-position": dict(title="Update a position in Oracle HCM", aid="Updating a position, step by step", source=SIM),
    "create-requisition": dict(title="Create a requisition in Oracle Recruiting", aid="Creating a requisition, step by step", source=SIM),
    "convert-pending-worker": dict(title="Convert a pending worker in Oracle HCM", aid="Converting a pending worker, step by step", source=SIM),
    "hire-non-worker": dict(title="Add a non-worker in Oracle HCM", aid="Converting a non-worker, step by step", source=SIM),
    "rehire-eligibility": dict(title="Rehires in Oracle HCM", aid="Rehires, step by step", source=SIM),
    "hcm-structure": dict(title="How Oracle HCM is organized", aid="Oracle HCM structure, concept by concept", source=BOARD),
    "workflow-worklists": dict(title="Approvals and worklists in Oracle HCM", aid="Workflow and worklists, step by step", source=SIM),
    "who-owns-what": dict(title="Who owns what", aid="Who owns what, team by team", source=BOARD),
    "quick-actions-person-info": dict(title="Find a person in Oracle HCM", aid="Finding a person and reading their record, step by step", source=SIM),
    "shared-calendar": dict(title="Working to the HR/Payroll Calendar", aid="Reading the HR/Payroll Calendar, step by step", source=BOARD),
    "ferpa-for-staff": dict(title="FERPA for staff", aid="FERPA, point by point", source=BOARD),
    "i9-background-by-worker-type": dict(title="I-9 and background checks by worker type", aid="I-9 and background checks, step by step", source=BOARD),
    "employee-vs-contractor": dict(title="Employee or independent contractor?", aid="Classifying a worker, step by step", source=BOARD),
    "data-integrity": dict(title="Bad data in, bad data out", aid="Data integrity, step by step", source=BOARD),
}

def apply(courses):
    by = {c["slug"]: c for c in courses}
    for slug, v in VIDEOS.items():
        c = by[slug]
        c["video"] = {"src": f"video/{slug}.mp4", "poster": f"video/{slug}.jpg", "title": v["title"], "narrated": True,
                      "kind": "board" if v["source"] == BOARD else "sim"}
        c["detailed"] = {"title": v["aid"], "source": v["source"],
                         "steps": [{"t": s["t"], "d": s.get("d", ""), "img": f"step-{i:02d}.jpg"} for i, s in enumerate(c["steps"], 1)]}

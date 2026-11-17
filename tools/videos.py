# Explainer videos and screenshot job aids, by course. Each video is built from tools/video/<slug>.html
# (see README, Explainer videos). The detailed job aid reuses the course's own steps, one still per step,
# so the job aid and the course never disagree.
SIM = "Screens from the HCM Academy training simulation of Oracle HCM. Names are fictional; check labels against Vanderbilt's Oracle."
BOARD = "Diagrams from the HCM Academy explainer video. The steps are the course's own."

VIDEOS = {
    "compensation-memo": dict(title="Getting the compensation memo", aid="Getting the compensation memo, step by step", source=BOARD),
    "background-checks": dict(title="Background checks", aid="Background checks, step by step", source=BOARD),
    "executive-search": dict(title="Executive or external search", aid="Executive or external search, step by step", source=BOARD),
    "hire-staff": dict(title="Hiring staff: the whole chain", aid="Hiring staff, from memo to day one", source=BOARD),
}

def apply(courses):
    by = {c["slug"]: c for c in courses}
    for slug, v in VIDEOS.items():
        c = by[slug]
        c["video"] = {"src": f"video/{slug}.mp4", "poster": f"video/{slug}.jpg", "title": v["title"], "narrated": True,
                      "kind": "board" if v["source"] == BOARD else "sim"}
        c["detailed"] = {"title": v["aid"], "source": v["source"],
                         "steps": [{"t": s["t"], "d": s.get("d", ""), "img": f"step-{i:02d}.jpg"} for i, s in enumerate(c["steps"], 1)]}

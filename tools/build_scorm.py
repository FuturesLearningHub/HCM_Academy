#!/usr/bin/env python3
"""Package HCM Academy as SCORM 1.2 and SCORM 2004 (4th Edition) zip files for an LMS.

  python3 tools/build_courses.py      # first, so the pages are current
  python3 tools/build_scorm.py        # writes dist/HCM_Academy_SCORM_1.2.zip and dist/HCM_Academy_SCORM_2004.zip

One SCO holds the whole academy: landing page, courses, pre-assessment, final assessment, Playbook and
What changed. scorm.html is the launch page: it connects to the LMS and shows the academy in a frame.
Each page loads scorm/bridge.js first, which saves progress through the launch page to the LMS.
The public site is not changed by this build: without the launch page the bridge does nothing.

In the package (only):
  - folder links (courses/x/) point at index.html, since LMS file servers often do not serve folders
  - the Mock-up buttons (Mark all complete, Reset demo) are hidden
  - rows with no course yet are shown but do not count toward completion
  - pages outside the package open in a new tab
"""
import html, json, os, re, shutil, subprocess, sys, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import governance as G  # noqa: E402

SRC = os.path.join(HERE, "scorm")
DIST = os.path.join(ROOT, "dist")
INCLUDE = ["index.html", "assets", "courses", "assessment", "changes",
           "playbook/index.html", "playbook/playbook.css", "playbook/HCM_Playbook.pdf"]
SKIP = re.compile(r"(^|/)(__pycache__|\.DS_Store|Thumbs\.db)(/|$)|\.pyc$")
TITLE = "HCM Academy"
IDENT = "vu-hcm-academy"

landing = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
SLUGS = list(dict.fromkeys(re.findall(r'data-course="([^"]+)"', landing)))
PASS = float(re.search(r"\bpass:\s*([0-9.]+)", open(os.path.join(ROOT, "assets", "assessments.js"), encoding="utf-8").read()).group(1))
MASTERY = round(PASS * 100)


def course_minutes():
    from course_content import COURSES
    return sum(int(re.match(r"\d+", c["time"]).group()) for c in COURSES if c["slug"] in SLUGS)


def stage_files(stage):
    for item in INCLUDE:
        src = os.path.join(ROOT, item)
        if os.path.isdir(src):
            for dp, dn, fn in os.walk(src):
                dn[:] = [d for d in dn if not SKIP.search(d)]
                for f in fn:
                    rel = os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/")
                    if SKIP.search(rel): continue
                    os.makedirs(os.path.dirname(os.path.join(stage, rel)), exist_ok=True)
                    shutil.copy2(os.path.join(dp, f), os.path.join(stage, rel))
        else:
            os.makedirs(os.path.dirname(os.path.join(stage, item)) or stage, exist_ok=True)
            shutil.copy2(src, os.path.join(stage, item))


FOLDER = re.compile(r'(href)="((?:\.\./|\./|[A-Za-z0-9_.-]+/)*)(#[^"]*)?"')


def rewrite(stage):
    """Bridge first in every page; folder links to index.html."""
    pages = []
    for dp, _, fn in os.walk(stage):
        for f in fn:
            if f.endswith(".html"): pages.append(os.path.join(dp, f))
    for p in pages:
        rel = os.path.relpath(p, stage).replace(os.sep, "/")
        up = "../" * rel.count("/")
        s = open(p, encoding="utf-8").read()

        def fix(m):
            path, frag = m.group(2), m.group(3) or ""
            if path == "" and frag: return m.group(0)          # in-page anchor
            if path in ("", "./"): path = "./"
            return f'{m.group(1)}="{path}index.html{frag}"'
        s = FOLDER.sub(fix, s)
        assert s.count("<head>") == 1, rel
        s = s.replace("<head>", f'<head>\n<script src="{up}scorm/bridge.js"></script>', 1)
        open(p, "w", encoding="utf-8").write(s)
    return pages


REF = re.compile(r'(?:href|src)="([^"]*)"')
CSSURL = re.compile(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)")


def check_links(stage):
    """Every link and asset inside the package must point at a file in it."""
    missing = []
    for dp, _, fn in os.walk(stage):
        for f in fn:
            if not f.endswith((".html", ".css")): continue
            p = os.path.join(dp, f); s = open(p, encoding="utf-8").read()
            s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
            refs = REF.findall(s) if f.endswith(".html") else CSSURL.findall(s)
            if f.endswith(".html"):
                for st in re.findall(r"<style[^>]*>(.*?)</style>", s, re.S): refs += CSSURL.findall(st)
            for r in refs:
                r = html.unescape(r)
                if re.match(r"^[a-z][a-z0-9+.-]*:|^//|^#|^$", r, re.I): continue
                path = r.split("#")[0].split("?")[0]
                if not path: continue
                tgt = os.path.normpath(os.path.join(dp, path))
                if not tgt.startswith(stage) or not os.path.isfile(tgt):
                    missing.append(f"{os.path.relpath(p, stage)} -> {r}")
    return missing


def manifest_12(files, minutes):
    fl = "\n".join(f'      <file href="{html.escape(f)}"/>' for f in files)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{IDENT}" version="1.0"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="org-hcm-academy">
    <organization identifier="org-hcm-academy">
      <title>{TITLE} ({G.EDITION})</title>
      <item identifier="item-hcm-academy" identifierref="res-hcm-academy" isvisible="true">
        <title>{TITLE}: {len(SLUGS)} courses, about {round(minutes / 60, 1)} hours</title>
        <adlcp:masteryscore>{MASTERY}</adlcp:masteryscore>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="res-hcm-academy" type="webcontent" adlcp:scormtype="sco" href="scorm.html">
{fl}
    </resource>
  </resources>
</manifest>
'''


def manifest_2004(files, minutes):
    fl = "\n".join(f'      <file href="{html.escape(f)}"/>' for f in files)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{IDENT}" version="1.0"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_v1p3"
  xmlns:adlseq="http://www.adlnet.org/xsd/adlseq_v1p3"
  xmlns:adlnav="http://www.adlnet.org/xsd/adlnav_v1p3"
  xmlns:imsss="http://www.imsglobal.org/xsd/imsss"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd http://www.adlnet.org/xsd/adlcp_v1p3 adlcp_v1p3.xsd http://www.adlnet.org/xsd/adlseq_v1p3 adlseq_v1p3.xsd http://www.adlnet.org/xsd/adlnav_v1p3 adlnav_v1p3.xsd http://www.imsglobal.org/xsd/imsss imsss_v1p0.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>2004 4th Edition</schemaversion>
  </metadata>
  <organizations default="org-hcm-academy">
    <organization identifier="org-hcm-academy">
      <title>{TITLE} ({G.EDITION})</title>
      <item identifier="item-hcm-academy" identifierref="res-hcm-academy" isvisible="true">
        <title>{TITLE}: {len(SLUGS)} courses, about {round(minutes / 60, 1)} hours</title>
        <imsss:sequencing>
          <imsss:deliveryControls tracked="true" completionSetByContent="true" objectiveSetByContent="true"/>
        </imsss:sequencing>
        <adlnav:presentation>
          <adlnav:navigationInterface>
            <adlnav:hideLMSUI>previous</adlnav:hideLMSUI>
            <adlnav:hideLMSUI>continue</adlnav:hideLMSUI>
          </adlnav:navigationInterface>
        </adlnav:presentation>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="res-hcm-academy" type="webcontent" adlcp:scormType="sco" href="scorm.html">
{fl}
    </resource>
  </resources>
</manifest>
'''


def build(version, minutes):
    tag = "1.2" if version == "1.2" else "2004"
    stage = os.path.join(DIST, f"scorm-{tag}")
    if os.path.isdir(stage): shutil.rmtree(stage)
    os.makedirs(stage)
    stage_files(stage)
    pages = rewrite(stage)
    os.makedirs(os.path.join(stage, "scorm"))
    for f in ("runtime.js", "bridge.js"): shutil.copy2(os.path.join(SRC, f), os.path.join(stage, "scorm", f))
    cfg = dict(version=tag, slugs=SLUGS, pass_mark=PASS, title=TITLE, edition=G.EDITION)
    shell = open(os.path.join(SRC, "scorm.html"), encoding="utf-8").read()
    assert "/*CONFIG*/{}" in shell
    open(os.path.join(stage, "scorm.html"), "w", encoding="utf-8").write(shell.replace("/*CONFIG*/{}", json.dumps(cfg)))

    missing = check_links(stage)
    if missing:
        print("\n".join(missing[:40])); sys.exit(f"SCORM {tag}: {len(missing)} links point outside the package")

    files = []
    for dp, _, fn in os.walk(stage):
        for f in fn: files.append(os.path.relpath(os.path.join(dp, f), stage).replace(os.sep, "/"))
    files.sort(key=lambda f: (f != "scorm.html", f))
    xsd_dir = os.path.join(SRC, "xsd", "12" if tag == "1.2" else "2004")
    for f in sorted(os.listdir(xsd_dir)): shutil.copy2(os.path.join(xsd_dir, f), os.path.join(stage, f))
    man = (manifest_12 if tag == "1.2" else manifest_2004)(files, minutes)
    open(os.path.join(stage, "imsmanifest.xml"), "w", encoding="utf-8").write(man)
    subprocess.run(["xmllint", "--noout", os.path.join(stage, "imsmanifest.xml")], check=True)

    out = os.path.join(DIST, f"HCM_Academy_SCORM_{tag}.zip")
    if os.path.exists(out): os.remove(out)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        allf = ["imsmanifest.xml"] + sorted(f for f in os.listdir(stage) if f.endswith((".xsd", ".dtd"))) + files
        for f in allf:
            zi = zipfile.ZipInfo(f, date_time=(2026, 11, 17, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_STORED if f.endswith((".pdf", ".woff2", ".png", ".jpg")) else zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(os.path.join(stage, f), "rb") as fh: z.writestr(zi, fh.read())
    print(f"SCORM {tag}: {out} ({os.path.getsize(out) / 1e6:.1f} MB, {len(files)} files, {len(pages)} pages)")
    return out


if __name__ == "__main__":
    # the longest progress record must fit SCORM 1.2's 4,096-character suspend_data
    worst = len(json.dumps({"p": 1, "f": 1, "d": SLUGS, "t": len(SLUGS), "b": 100}))
    assert worst < 3800, f"progress record is {worst} characters"
    minutes = course_minutes()
    print(f"{len(SLUGS)} courses, {minutes} minutes of courses, pass mark {MASTERY}%, progress record up to {worst} characters")
    os.makedirs(DIST, exist_ok=True)
    for v in ("1.2", "2004"): build(v, minutes)

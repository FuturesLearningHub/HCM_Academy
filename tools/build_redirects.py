#!/usr/bin/env python3
"""Courses merged by the SME review keep a page at their old address that sends people to the course
that absorbed them, so bookmarks and links in emails still work. Run after build_courses.py."""
import html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from course_content import COURSES  # noqa: E402
import reviews  # noqa: E402
import restructure  # noqa: E402
BY = {c["slug"]: c for c in COURSES}
for old, new in list(reviews.REMOVED.items()) + list(restructure.REMOVED.items()):
    name = html.escape(BY[new]["name"])
    d = os.path.join(ROOT, "courses", old); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<title>This course moved · HCM Academy</title><meta name="robots" content="noindex" />
<meta http-equiv="refresh" content="0; url=../{new}/index.html" /><link rel="canonical" href="../{new}/" />
<style>body{{font:17px/1.5 Inter,Arial,sans-serif;color:#1C1C1C;background:#F5F3EF;margin:0;padding:48px 24px}}main{{max-width:560px;margin:0 auto}}a{{color:#946E24}}</style></head>
<body><main><p>This course is now part of <a href="../{new}/index.html">{name}</a>.</p></main></body></html>
""")
    print(f"redirect: courses/{old}/ -> courses/{new}/")

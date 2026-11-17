#!/usr/bin/env python3
"""Write engine.js from engine.src.js, adding the icon set and the Vanderbilt header (from sprite.svg and head.html)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, "engine.src.js"), encoding="utf-8").read()
src = src.replace("__SPRITE__", json.dumps(open(os.path.join(D, "sprite.svg"), encoding="utf-8").read()))
src = src.replace("__HEAD__", json.dumps(open(os.path.join(D, "head.html"), encoding="utf-8").read()))
open(os.path.join(D, "engine.js"), "w", encoding="utf-8").write("/* Generated from engine.src.js by build.py. Edit the source, then rebuild. */\n" + src)
print("engine.js written")

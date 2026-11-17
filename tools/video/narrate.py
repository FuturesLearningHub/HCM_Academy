#!/usr/bin/env python3
"""Lay the narration under a rendered video.
  node tools/video/render.cjs <scene> /tmp/silent.mp4      # also writes /tmp/silent.segs.json
  python3 tools/video/narrate.py <scene> /tmp/silent.mp4 courses/<slug>/video/<slug>.mp4
Each clip in tools/video/narration/<scene>.json is cut from tools/video/narration/<scene>.mp3 and
starts when its segment starts in the scene. The mix is normalized to -16 LUFS for speech."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
scene, silent, out = sys.argv[1:4]
cfg = json.load(open(os.path.join(HERE, "narration", scene + ".json")))
segs = json.load(open(silent[:-4] + ".segs.json"))
assert len(segs) == len(cfg["clips"]), (len(segs), len(cfg["clips"]))
parts, labels = [], []
for i, ((a, b), at) in enumerate(zip(cfg["clips"], segs)):
    a, b = max(0, a - .08), b + .08
    ms = int(round(at * 1000))
    parts.append(f"[1:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st={b - a - .06:.3f}:d=0.06,adelay={ms}|{ms}[c{i}]")
    labels.append(f"[c{i}]")
graph = ";".join(parts) + ";" + "".join(labels) + f"amix=inputs={len(labels)}:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11,apad[a]"   # pad, so the video sets the length
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", os.path.join(HERE, "narration", scene + ".mp3"),
                "-filter_complex", graph, "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                "-ar", "48000", "-shortest", "-movflags", "+faststart", out], check=True)
print("narrated:", out)

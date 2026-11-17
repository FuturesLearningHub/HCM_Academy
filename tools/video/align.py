#!/usr/bin/env python3
"""Cut a narration read into one clip per paragraph of the script.
  python3 tools/video/align.py <scene>
Reads tools/video/narration/<scene>.mp3 and the "script" in <scene>.json, finds the pauses, and
matches every sentence break in the script to a pause, in order, using where each break should
fall at an even speaking rate. Paragraph breaks become the clip edges. Writes "clips" back to the
json and prints each clip's speaking rate so a bad match stands out."""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def silences(mp3, noise="-38dB", d="0.22"):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp3, "-af", f"silencedetect=noise={noise}:d={d}", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: (-?[0-9.]+)", err)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    dur = float(re.search(r"Duration: (\d+):(\d+):([0-9.]+)", err).group(3)) + 60 * float(re.search(r"Duration: (\d+):(\d+)", err).group(2))
    return list(zip(st, en)), dur

def letters(s): return len(re.sub(r"[^A-Za-z0-9]", "", s))

def align(mp3, paras):
    sil, dur = silences(mp3)
    lead = sil[0][1] if sil and sil[0][0] <= 0.05 else 0.0
    tail = sil[-1][0] if sil and sil[-1][1] >= dur - 0.05 else dur
    inner = [s for s in sil if s[0] > lead + 0.05 and s[1] < tail - 0.05]
    sents, pbreak = [], []
    for i, p in enumerate(paras):
        parts = [x for x in re.split(r"(?<=[.!?:])\s+", p.strip()) if x]
        for j, x in enumerate(parts):
            sents.append(x); pbreak.append(j == len(parts) - 1 and i < len(paras) - 1)
    pbreak = pbreak[:-1]                       # breaks between sentences
    nb = len(pbreak)
    pause = sum(e - s for s, e in inner) / max(1, len(inner))
    L = [letters(x) for x in sents]
    rate = (tail - lead - nb * pause) / sum(L)  # seconds per letter
    exp, acc = [], lead
    for k in range(nb):
        acc += L[k] * rate; exp.append(acc + pause / 2); acc += pause
    mids = [(s + e) / 2 for s, e in inner]
    n, INF = len(mids), float("inf")
    # dp[k][i]: best cost with break k on pause i (pauses used in order, extra pauses skipped)
    dp = [[INF] * n for _ in range(nb)]; bk = [[-1] * n for _ in range(nb)]
    for i in range(n): dp[0][i] = (mids[i] - exp[0]) ** 2
    for k in range(1, nb):
        best, bi = INF, -1
        for i in range(n):
            if i - 1 >= 0 and dp[k - 1][i - 1] < best: best, bi = dp[k - 1][i - 1], i - 1
            if best < INF: dp[k][i] = best + (mids[i] - exp[k]) ** 2; bk[k][i] = bi
    i = min(range(n), key=lambda x: dp[nb - 1][x]); pick = [0] * nb
    for k in range(nb - 1, -1, -1): pick[k] = i; i = bk[k][i]
    edges = [inner[pick[k]] for k in range(nb) if pbreak[k]]
    starts = [lead] + [e for s, e in edges]; ends = [s for s, e in edges] + [tail]
    clips = [[round(a, 2), round(b, 2)] for a, b in zip(starts, ends)]
    return clips, [letters(p) / (b - a) for p, (a, b) in zip(paras, clips)]

if __name__ == "__main__":
    scene = sys.argv[1]
    jp = os.path.join(HERE, "narration", scene + ".json"); cfg = json.load(open(jp, encoding="utf-8"))
    if cfg.get("locked") or any(len(c) > 2 for c in cfg.get("clips", [])):
        print("cut points were set by hand or include a separate line; keeping them"); sys.exit(0)
    clips, rates = align(os.path.join(HERE, "narration", scene + ".mp3"), cfg["script"])
    avg = sum(rates) / len(rates)
    for c, r, p in zip(clips, rates, cfg["script"]):
        print(f"{c[0]:7.2f} {c[1]:7.2f}  {r:5.1f} letters/s {'  CHECK' if abs(r - avg) > 0.22 * avg else ''}  {p[:60]}")
    if "--dry" not in sys.argv:
        cfg["clips"] = clips; json.dump(cfg, open(jp, "w", encoding="utf-8"), indent=2, ensure_ascii=False); print("clips saved")

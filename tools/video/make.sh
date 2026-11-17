#!/usr/bin/env bash
# Build one explainer: cut the narration, render, mix, take job aid stills and the poster.
#   tools/video/make.sh <scene> <course-slug>
# Needs tools/video/<scene>.html and tools/video/narration/<scene>.{json,mp3}.
set -euo pipefail
cd "$(dirname "$0")/../.."
scene=$1; slug=$2; tmp=$(mktemp -d)
python3 tools/video/align.py "$scene"
node tools/video/render.cjs "$scene" "$tmp/silent.mp4"
mkdir -p "courses/$slug/video" "courses/$slug/img"
python3 tools/video/narrate.py "$scene" "$tmp/silent.mp4" "courses/$slug/video/$slug.mp4"
node tools/video/stills.cjs "$scene" "$tmp/stills"
for f in "$tmp"/stills/step-*.png; do ffmpeg -v error -y -i "$f" -vf scale=1280:-2 -q:v 3 "courses/$slug/img/$(basename "$f" .png).jpg"; done
ffmpeg -v error -y -ss 2.5 -i "courses/$slug/video/$slug.mp4" -frames:v 1 -vf scale=1280:-2 -q:v 3 "courses/$slug/video/$slug.jpg"
rm -rf "$tmp"
echo "built courses/$slug/video/$slug.mp4 and $(ls courses/$slug/img/step-*.jpg | wc -l) stills"

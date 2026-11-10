#!/usr/bin/env python3
"""Bedah video referensi: info, titik potong adegan, frame per adegan, contact sheet.

Pemakaian:
    python3 bedah_video.py video.mp4 [--out folder] [--threshold 0.3] [--step 0.5]

Butuh ffmpeg + ffprobe di PATH. Kalau tidak ada, coba: pip install imageio-ffmpeg
(script akan memakai binary dari paket itu).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys


def find_ffmpeg():
    ff = shutil.which("ffmpeg")
    fp = shutil.which("ffprobe")
    if ff:
        return ff, fp
    try:
        import imageio_ffmpeg  # type: ignore

        return imageio_ffmpeg.get_ffmpeg_exe(), None
    except Exception:
        sys.exit("ffmpeg tidak ditemukan. Install ffmpeg atau `pip install imageio-ffmpeg`.")


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(ffmpeg, ffprobe, path):
    if ffprobe:
        r = run([ffprobe, "-v", "error", "-print_format", "json", "-show_format", "-show_streams", path])
        data = json.loads(r.stdout or "{}")
        dur = float(data.get("format", {}).get("duration", 0) or 0)
        v = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
        has_audio = any(s.get("codec_type") == "audio" for s in data.get("streams", []))
        fps = v.get("avg_frame_rate", "0/1")
        try:
            n, d = fps.split("/")
            fps = round(float(n) / float(d), 2) if float(d) else 0
        except Exception:
            fps = 0
        return dur, v.get("width"), v.get("height"), fps, has_audio
    # fallback: parse ffmpeg -i stderr
    err = run([ffmpeg, "-i", path]).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0
    m = re.search(r"Video:.*?(\d{2,5})x(\d{2,5}).*?([\d.]+) fps", err)
    w, h, fps = (int(m.group(1)), int(m.group(2)), float(m.group(3))) if m else (None, None, 0)
    return dur, w, h, fps, "Audio:" in err


def detect_cuts(ffmpeg, path, threshold):
    r = run([ffmpeg, "-hide_banner", "-i", path, "-vf", f"select='gt(scene,{threshold})',showinfo", "-an", "-f", "null", "-"])
    return [float(t) for t in re.findall(r"pts_time:([\d.]+)", r.stderr)]


def fmt(t):
    return f"{t:.1f}".replace(".", ",")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--out", default="bedah_out")
    ap.add_argument("--threshold", type=float, default=0.3, help="0.2 lebih sensitif, 0.45 kurang sensitif")
    ap.add_argument("--step", type=float, default=0.5, help="jarak frame contact sheet (detik)")
    a = ap.parse_args()

    ffmpeg, ffprobe = find_ffmpeg()
    os.makedirs(os.path.join(a.out, "frames"), exist_ok=True)

    dur, w, h, fps, has_audio = probe(ffmpeg, ffprobe, a.video)
    with open(os.path.join(a.out, "info.txt"), "w") as f:
        f.write(f"durasi: {fmt(dur)} dtk\nresolusi: {w}x{h}\nfps: {fps}\naudio: {'ada' if has_audio else 'tidak ada'}\n")

    cuts = [c for c in detect_cuts(ffmpeg, a.video, a.threshold) if 0.2 < c < dur - 0.2]
    bounds = [0.0] + cuts + [dur]
    scenes = [(bounds[i], bounds[i + 1]) for i in range(len(bounds) - 1) if bounds[i + 1] - bounds[i] > 0.1]

    lines = []
    for i, (s, e) in enumerate(scenes, 1):
        mid = (s + e) / 2
        out = os.path.join(a.out, "frames", f"adegan_{i:02d}.jpg")
        run([ffmpeg, "-y", "-loglevel", "error", "-ss", f"{mid:.2f}", "-i", a.video, "-frames:v", "1", "-vf", "scale=540:-2", out])
        lines.append(f"Adegan {i}: {fmt(s)}–{fmt(e)} dtk ({fmt(e - s)} dtk) -> frames/adegan_{i:02d}.jpg")
    with open(os.path.join(a.out, "adegan.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")

    # contact sheets: 4x5 grid per sheet, timecode burned in each tile
    per_sheet = 20
    total = max(1, int(dur / a.step))
    sheets = (total + per_sheet - 1) // per_sheet
    for k in range(sheets):
        start = k * per_sheet * a.step
        vf = (
            f"fps=1/{a.step},scale=270:-2,"
            "drawtext=text='%{pts\\:hms}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6,"
            "tile=4x5"
        )
        r = run([ffmpeg, "-y", "-loglevel", "error", "-ss", f"{start:.2f}", "-t", f"{per_sheet * a.step:.2f}",
                 "-i", a.video, "-vf", vf, "-frames:v", "1", "-copyts", os.path.join(a.out, f"sheet_{k + 1:02d}.jpg")])
        if r.returncode != 0:  # drawtext may be missing (no fontconfig); retry without timecode
            vf = f"fps=1/{a.step},scale=270:-2,tile=4x5"
            run([ffmpeg, "-y", "-loglevel", "error", "-ss", f"{start:.2f}", "-t", f"{per_sheet * a.step:.2f}",
                 "-i", a.video, "-vf", vf, "-frames:v", "1", os.path.join(a.out, f"sheet_{k + 1:02d}.jpg")])

    print(open(os.path.join(a.out, "info.txt")).read())
    print("\n".join(lines))
    print(f"\n{sheets} contact sheet (tiap {a.step} dtk) di {a.out}/sheet_XX.jpg")


if __name__ == "__main__":
    main()

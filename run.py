"""Read the daily/weekly/monthly Lark sheets, open every document they link, analyze, and write a report.

Usage:
    python run.py --config config.yaml [--only daily] [--limit 3] [--dry-run]
"""
import argparse
import datetime as dt
import json
import pathlib
import re

import yaml

from neuralabi.analyze import analyze
from neuralabi.browser import chrome_profile
from neuralabi.fetch import fetch_text
from neuralabi.lark_sheet import read_sheet

URL_RE = re.compile(r"https?://\S+")


def doc_links(row: dict, link_column: str | None) -> list[str]:
    cells = [row.get(link_column, "")] if link_column else row.values()
    return [u for c in cells for u in URL_RE.findall(c or "")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--only", help="run one sheet, e.g. daily")
    ap.add_argument("--limit", type=int, help="max rows per sheet")
    ap.add_argument("--dry-run", action="store_true", help="read sheets only, skip analysis")
    args = ap.parse_args()

    cfg = yaml.safe_load(pathlib.Path(args.config).read_text())
    out_dir = pathlib.Path(cfg.get("output_dir", "reports"))
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")

    with chrome_profile(cfg["chrome"]["user_data_dir"], cfg["chrome"].get("profile_directory", "Default")) as ctx:
        for period, sheet in cfg["sheets"].items():
            if args.only and period != args.only:
                continue
            rows = read_sheet(ctx, sheet["url"])
            print(f"[{period}] {len(rows)} baris")
            (out_dir / f"{period}-{stamp}-rows.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))
            if args.dry_run:
                continue

            report = [f"# Analisa {period} ({stamp})\n"]
            for i, row in enumerate(rows[: args.limit]):
                for url in doc_links(row, sheet.get("link_column")):
                    print(f"  baris {i + 1}: {url}")
                    try:
                        text = fetch_text(ctx, url)
                        result = analyze(text, row, period, cfg.get("model", "claude-opus-5-5"))
                    except Exception as e:  # keep going on one bad link
                        result = f"GAGAL: {e}"
                    report.append(f"## Baris {i + 1}\n{url}\n\n{result}\n")
            path = out_dir / f"{period}-{stamp}.md"
            path.write_text("\n".join(report))
            print(f"[{period}] laporan: {path}")


if __name__ == "__main__":
    main()

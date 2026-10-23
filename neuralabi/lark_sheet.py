"""Read a Lark (Larksuite) sheet that is open in the browser.

Lark draws the grid on a canvas, so cells are not in the DOM. Instead we select
the whole sheet, copy it, and read the clipboard as tab-separated text.
"""
import csv
import io
import sys
from urllib.parse import urlparse

from playwright.sync_api import BrowserContext

MOD = "Meta" if sys.platform == "darwin" else "Control"


def read_sheet(context: BrowserContext, url: str, wait_ms: int = 6000) -> list[dict]:
    origin = "{0.scheme}://{0.netloc}".format(urlparse(url))
    context.grant_permissions(["clipboard-read", "clipboard-write"], origin=origin)

    page = context.new_page()
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(wait_ms)  # let the sheet render

    # Click a cell in the grid, then select all and copy.
    box = page.viewport_size
    page.mouse.click(box["width"] * 0.4, box["height"] * 0.45)
    page.keyboard.press(f"{MOD}+A")
    page.keyboard.press(f"{MOD}+C")
    page.wait_for_timeout(1000)
    tsv = page.evaluate("navigator.clipboard.readText()")
    page.close()

    if not tsv.strip():
        raise RuntimeError(f"Clipboard empty after copying {url}; is the profile logged in to Lark?")
    return parse_tsv(tsv)


def parse_tsv(tsv: str) -> list[dict]:
    rows = [r for r in csv.reader(io.StringIO(tsv), delimiter="\t") if any(c.strip() for c in r)]
    if not rows:
        return []
    header = [h.strip() for h in rows[0]]
    return [dict(zip(header, r)) for r in rows[1:]]

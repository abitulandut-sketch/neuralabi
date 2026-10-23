"""Open a document link in the logged-in browser and extract its visible text."""
from playwright.sync_api import BrowserContext


def fetch_text(context: BrowserContext, url: str, wait_ms: int = 5000, max_chars: int = 60000) -> str:
    page = context.new_page()
    try:
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(wait_ms)
        # Lark docs lazy-load blocks while scrolling.
        for _ in range(10):
            page.mouse.wheel(0, 3000)
            page.wait_for_timeout(300)
        text = page.evaluate("document.body.innerText")
    finally:
        page.close()
    return text[:max_chars]

"""Launch Chrome with an existing (logged-in) user profile via Playwright."""
from contextlib import contextmanager

from playwright.sync_api import sync_playwright


@contextmanager
def chrome_profile(user_data_dir: str, profile_directory: str = "Default", headless: bool = False):
    """Yield a persistent browser context that reuses the cookies of a Chrome profile.

    Chrome must be closed first: a profile can only be opened by one process at a time.
    """
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir,
            channel="chrome",
            headless=headless,
            args=[f"--profile-directory={profile_directory}"],
            viewport={"width": 1600, "height": 1000},
        )
        try:
            yield context
        finally:
            context.close()

import pytest
from playwright.sync_api import Page, expect , BrowserContext

def test_docs(browser_name: str, page: Page):
    if browser_name == "firefox":
        page.goto("https://playwright.dev/python/")
        docs_link = page.get_by_role("link", name="Docs")
        expect(docs_link).to_be_visible()

def test_get_started(browser_name: str,context: BrowserContext):
    if browser_name == "chromium":
        page = context.new_page()
        page.goto("https://playwright.dev/python/")
        get_started = page.get_by_role("link", name = "Get started")
        get_started.click()
        expect(page).to_have_url("https://playwright.dev/python/docs/intro")

# in the above code snippet, both will run and passes even you explicitly given the browser name as chromium(pytest test_browser_name.py -v --browser=chromium), it wont skip
# so for this we must use pytest marker. Refer test_marker.py 
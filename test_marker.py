import pytest
from playwright.sync_api import Page, expect , BrowserContext

@pytest.mark.skip_browser("chromium")
def test_docs( page: Page):
    page.goto("https://playwright.dev/python/")
    docs_link = page.get_by_role("link", name="Docs")
    expect(docs_link).to_be_visible()

@pytest.mark.only_browser("chromium")
def test_get_started(context: BrowserContext):
    page = context.new_page()
    page.goto("https://playwright.dev/python/")
    get_started = page.get_by_role("link", name = "Get started")
    get_started.click()
    expect(page).to_have_url("https://playwright.dev/python/docs/intro")
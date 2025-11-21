import pytest
from playwright.sync_api import sync_playwright, BrowserContext, Page

@pytest.fixture(autouse=True)
def trace(context: BrowserContext):
    context.tracing.start(
        name="sample",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    yield
    context.tracing.stop(path="trace.zip")

def test_sample(page: Page):
    page.goto("https://playwright.dev/docs/test-snapshots")
    content = page.locator(".table-of-contents")
    content.screenshot(path = "screenshots/content.jpeg")
import pytest
from playwright.sync_api import sync_playwright, Page

def test_for_screenshot(page: Page):
    page.goto("https://playwright.dev/python/docs/screenshots")
    page.screenshot(path="screenshots/sample.png", type="jpeg", full_page=True)
    page.screenshot(path="screenshots/sample_1.png")
    heading = page.locator("h1")
    heading.screenshot(path="screenshots/heading.png")

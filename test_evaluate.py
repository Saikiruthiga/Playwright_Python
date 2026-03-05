import pytest
from playwright.sync_api import *

def test_custom_js(page: Page):
    page.goto("https://playwright.dev/python/")
    page.evaluate("window.scrollBy(0,document.body.scrollHeight)")
    page.screenshot(path="end.png",full_page=True)
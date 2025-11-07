from playwright.sync_api import sync_playwright
from creds import *
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless = False, slow_mo =1500)
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json"
    )
    page = context.new_page()
    page.goto("https://accounts.google.com")
    page.pause()
    context.close()
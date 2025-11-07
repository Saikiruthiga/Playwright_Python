from playwright.sync_api import sync_playwright
from creds import *

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless = False, slow_mo = 1500,
                                        args=["--disable-dev-shm-Usage", "--disable-blink-features=AutomationControlled"])
    context = browser.new_context()
    page = context.new_page()
    url = "https://accounts.google.com"
    page.goto(url)
    email_input = page.get_by_label("Email or phone")
    email_input.type(email)
    page.get_by_role("button", name = "Next").click()
    password_input = page.get_by_label("Enter your password")
    password_input.type(password)
    page.get_by_role("button", name = "Next").click()
    #To do something manually in the browser we can use 
    page.pause()
    #To save the authentication state
    context.storage_state(path = "playwright/.auth/storage_state.json")
    context.close()
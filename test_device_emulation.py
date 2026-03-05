import pytest
from playwright.sync_api import *

def test_sample(browser: Browser, playwright: Playwright):
    pixel_5_args = playwright.devices["Pixel 5"]
    #context = browser.new_context(**pixel_5_args)
    # **pixel_5_args means all the args set to true, if we want specific config, we can set separateley
    context = browser.new_context(
        viewport={
            "width" : 1000,
            "height" : 500
        },
        color_scheme="light"

    )
    page = context.new_page()
    page.goto("https://playwright.dev/python/")
    docs_link = page.get_by_role("link", name = "Docs")
    docs_link.click()
    page.set_viewport_size({
        "width":300,
        "height":500
    })
import pytest
from playwright.sync_api import Page, expect, Route

def on_route(route: Route):
    print("Request aborted :", route.request)
    route.abort()

def test_visit_docs(page: Page):
    page.route("**.svg", on_route) # if we are using, ** it means the relatiove path including //, * means some words between the slashes
    page.goto("https://playwright.dev/python/")
    page.screenshot(path="screenshots/no_logo.jpg")
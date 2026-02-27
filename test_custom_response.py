import pytest
from playwright.async_api import Page, expect, Route

def on_route(route: Route):
    route.fulfill(
        status=200,
        body="<html><body><h1>Hi Kiruthiga</h1></body></html>"
    )

def test_visit_docs(page: Page):
    page.route("https://playwright.dev/python/",on_route)
    page.goto("https://playwright.dev/python/")
    page.pause()

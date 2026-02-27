import pytest
from playwright.sync_api import Page, expect, Route

def on_route(route: Route):
    response = route.fetch()
    body = response.text()
    print("Route triggered for:",route.request.url)
    if "Playwright" in body:
        print("Text found")
        body = body.replace("Playwright enables reliable end-to-end testing for modern web apps", "Kiruthiga is a Software Developer")
    else:
        print("Text not found")

    route.fulfill(
        response=response,
        body=body
    )
    
def test_visit_docs(page: Page):
    page.route("**/*/", on_route)
    

    page.goto("https://playwright.dev/python/")
    page.pause()
    

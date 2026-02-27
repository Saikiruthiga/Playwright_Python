import pytest
from playwright.sync_api import Page, expect, Route

def on_route(route: Route):
    if route.request.resource_type == "image" :
        route.abort()
        print("Route aborted :", route.request)
    else:
        route.continue_()
        

def test_visit_docs(page : Page):
    page.route("**", on_route) 
    page.goto("https://playwright.dev/python/")
    page.screenshot(path="screenshots/no_image.jpg",full_page=True)
import pytest
from playwright.sync_api import *

# Special built-in fixture, need to use the exact name browser_context_args. It launches the browser with js script disabled
@pytest.fixture()
def browser_context_args():
    return{
        "java_script_enabled" : False
    }

NOT_ALLOWED_RESOURCES = "image", "stylesheet", "media" # we can also use "script", here to avoid the loading of js script but this is just stop the loading
def on_route(route: Route):
    if route.request.resource_type in NOT_ALLOWED_RESOURCES:
        route.abort()
    else:
        route.continue_()


@pytest.fixture(autouse=True)
def skip_resource(page: Page):
    page.route("**", on_route) # ** means for the all url in the tests


def test_check_link(page: Page):
    page.goto("https://playwright.dev/python/")
    link = page.get_by_role("link", name = "Docs")
    expect(link).to_be_visible()

def test_get_started(page: Page):
    page.goto("https://playwright.dev/python/")
    get_started = page.get_by_role("link", name = "Get started")
    get_started.click()
    expect(page).to_have_url("https://playwright.dev/python/docs/intro")

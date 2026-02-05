import pytest
from playwright.async_api import Page, expect


# Run this file by commenting the 2nd line (addopts = --headed --slowmo=1000 -s -v) in pytest.ini file

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args): # the name inside () is original fixture
    return{
        **browser_type_launch_args, # extend the original fixture
        "headless" : False,
        "slow_mo" : 1000  # overide the properties of headless and slow_mo, remaining are same

    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return{
        **browser_context_args,
        "storage_state" : "playwright/.auth/storage_state.json"
    }

def test_visit_google_accouunt(page: Page):
    page.goto("https://accounts.google.com")
    page.screenshot(path="account.jpg")




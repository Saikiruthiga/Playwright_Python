from playwright.sync_api import Page
import pytest

url = "https://playwright.dev/python/"

@pytest.fixture(autouse=True)
def visit_page(page:Page):
    page.goto(url)
    yield page
    page.close()
    print("\n [Fixture] : Page closed !")

def test_page_has_docs_link(page:Page):
    link = page.get_by_role("link",name = "Docs")
    assert link.is_visible()

def test_page_has_get_started_link(page: Page):
    link = page.get_by_role("link", name = "Get started")
    link.click()
    page_url = page.url
    assert page_url == "https://playwright.dev/python/docs/intro"

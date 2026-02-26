from models.playwright_docs import PlaywrightPage
from playwright.sync_api import Page, expect

def test_docs_link(page: Page):
    home_page = PlaywrightPage(page)
    home_page.visit_docs()
    expect(home_page.page).to_have_url("https://playwright.dev/docs/intro")



def test_docs_search(page: Page):
    query = "assertions"
    home_page = PlaywrightPage(page)
    home_page.search(query)

    expect(home_page.search_results()).to_contain_text("Soft assertions")



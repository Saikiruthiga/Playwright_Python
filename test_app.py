from playwright.sync_api import Page

url = "https://playwright.dev/python/"
# page_title = "Installation | Playwright Python"
page_url = "https://playwright.dev/python/docs/intro"

def test_page_has_link(page : Page):
    page.goto(url)
    link = page.get_by_role("link", name = "Get started")
    link.click()
    # page.wait_for_url(page_url)
    # title = page.title()
    # assert title == page_title
    new_url = page.url
    assert new_url == page_url


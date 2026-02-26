from playwright.sync_api import Page, Locator

class PlaywrightPage:
    
    def __init__(self,page: Page):
        self.page = page
        self.page.goto("https://playwright.dev/")
        self.docs_link = page.get_by_role("link", name = "Docs")
        self.search_input = self.page.get_by_placeholder("Search docs")

    def visit_docs(self):
        self.docs_link.click()

    def search(self,query):
        self.page.keyboard.press("Control+KeyK")
        self.search_input.fill(query)

    def search_results(self)-> Locator:
        return self.page.locator("div.DocSearch-Dropdown")
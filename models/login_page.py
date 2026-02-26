from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        page.goto("http://uitestingplayground.com/sampleapp")

        self.user_input = self.page.get_by_placeholder("User Name")
        self.password_input = self.page.get_by_placeholder("********")

        self.login_button = self.page.get_by_role("button", name = "Log In")

        self.message_label = self.page.locator("label#loginstatus")

    def login(self,username,password):
        self.user_input.fill(username)
        self.password_input.fill(password)

        self.login_button.click()
        
        
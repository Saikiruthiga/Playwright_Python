from models.login_page import LoginPage
from playwright.sync_api import Page, expect

# @pytest.fixture(autouse=True)
# def visit_test_page(page: Page):
#     page.goto("http://uitestingplayground.com/sampleapp")

def test_valid_login(page: Page):
    username = "dan"
    password = "pwd"

    login_page = LoginPage(page)
    login_page.login(username,password)

    expect(login_page.message_label).to_have_text(f"Welcome, {username}!")

def test_invalid_login(page: Page):
    username = "invalid"
    password = "invalid"

    login_page = LoginPage(page)
    login_page.login(username,password)

    expect(login_page.message_label).to_have_text("Invalid username/password")
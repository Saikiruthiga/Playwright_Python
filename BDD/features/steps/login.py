from behave import *
from playwright.sync_api import expect

@given("username and pwd password")
def fill_credentials(context):
    context.page.goto("http://uitestingplayground.com/sampleapp")
    context.page.get_by_placeholder("User Name").fill("User")
    context.page.get_by_placeholder("********").fill("pwd")

@when("log In button is clicked")
def click_login(context):
    login_button = context.page.get_by_role("button", name = "Log In")
    login_button.click()
    

@then("show welcome message")
def expect_welcome_message(context):
    message = context.page.locator("label#loginstatus")
    expect(message).to_have_text("Welcome, User!")
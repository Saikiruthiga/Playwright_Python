import pytest, re
from playwright.sync_api import sync_playwright, Page, expect

def test_assertions(page: Page):
    page.goto("https://playwright.dev/python/")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright Python")
    heading = page.locator("h1[class = 'hero__title heroTitle_ohkl']")
    expect(heading).to_contain_text("reliable")
    expect(heading).to_have_text(" Playwright enables reliable end-to-end testing for modern web apps.")
    expect(heading).to_have_class("hero__title heroTitle_ohkl")
    expect(heading).to_have_class(
        re.compile("heroTitle_ohkl")
    )
    input = page.get_by_placeholder("Search docs")
    expect(input).to_be_hidden()
    input_button = page.get_by_role("button", name = "Search")
    input_button.press("Control+k")
    expect(input).to_be_enabled()
    expect(input).to_be_empty()
    expect(input).to_be_editable()
    input.fill("Screenshots")
    expect(input).to_have_value("Screenshots")
    page.goto("https://bootswatch.com/default/")
    default_checkbox = page.get_by_label("Default checkbox")
    expect(default_checkbox).not_to_be_checked()
    checked_checkbox = page.get_by_label("Checked checkbox")
    expect(checked_checkbox).to_be_checked()
    # disabled_select = page.get_by_label("Example disabled select")
    # expect(disabled_select).to_be_disabled()
    disable = page.locator("select[id='exampleDisabledSelect1']")
    expect(disable).to_be_disabled()
    Example_select = page.get_by_label("Example select")
    expect(Example_select).to_have_value("1")
    multiple_options = page.get_by_label("Example multiple select")
    multiple_options.select_option(["2","4","5"])
    expect(multiple_options).to_have_values(["2","4","5"])

    

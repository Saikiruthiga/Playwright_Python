import pytest
from playwright.sync_api import Page, expect, Request, Response

def on_request(request: Request):
    print("Request :", request)

def on_response(response: Response):
    print("Response :", response)
    print("Status code :", response.status)

def test_docs(page: Page):
    page.on("request", on_request)
    page.on("response",on_response)
    page.goto("https://playwright.dev/python/")
    docs_link = page.get_by_role("link", name = "Docs")
    docs_link.click()
    expect(page).to_have_url("https://playwright.dev/python/docs/intro")
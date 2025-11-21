import pytest
from playwright.sync_api import sync_playwright, Browser ,Page

@pytest.fixture
def recording(browser: Browser):
    context = browser.new_context(
       record_video_dir="video/",
       record_video_size={"width":1280, "height":720}    )
    page = context.new_page()
    yield page
    context.close()

def test_for_record_video(recording):
    page = recording
    page.goto("https://playwright.dev/docs/test-snapshots")
    content = page.locator(".table-of-contents")
    content.screenshot(path = "screenshots/content.jpeg")
    page.locator("//button[@aria-label = 'Switch between dark and light mode (currently system mode)']").click()

   


from playwright.sync_api import Page

def test_api_users(page: Page):
    response = page.goto("https://dummyjson.com/users/1")

    user_data = response.json()

    assert "firstName" in user_data
    assert user_data["firstName"] == "Emily"
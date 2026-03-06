import pytest
from creds import GITHUB_ACCESS_TOKEN, GITHUB_REPO, GITHUB_USERNAME
from playwright.sync_api import *

def test_create_issue(api_context: APIRequestContext):
    issue_data = {
        "title" : "bug",
        "body" : "When doing this test, it failed"
    }

    post_response = api_context.post(
        f"/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/issues",
        data = issue_data
    )

    assert post_response.ok

def test_issues_screenshot(page: Page):
    page.goto(f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}/issues")
    page.screenshot(path = "screenshots/issues.png", full_page=True)

def test_new_issue_in_repo(api_context: APIRequestContext):
    get_response = api_context.get(
        f"/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/issues"
    )

    assert get_response.ok

    all_issues = get_response.json()

    new_issue = None
    for issue in all_issues:
        if issue["title"] == "bug":
            new_issue = issue
            break

    assert new_issue is not None        
    assert new_issue["body"] == "When doing this test, it failed"
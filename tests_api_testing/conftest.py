from dotenv import load_dotenv
load_dotenv()

import pytest
from creds import GITHUB_ACCESS_TOKEN, GITHUB_REPO, GITHUB_USERNAME
from playwright.sync_api import Playwright, APIRequestContext

# whatever created in the conftest.py, we can access all over the files without importing the fixtures or methods

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}"
        }
    )
    yield context
    context.dispose()

@pytest.fixture(autouse=True,scope="session")
def test_create_repo(api_context: APIRequestContext):
    # create repo
    post_response = api_context.post(
        "/user/repos",
        data = {"name": GITHUB_REPO}
    )
    assert post_response.ok
    yield

    # delete repo
    delete_response = api_context.delete(
        f"/repos/{GITHUB_USERNAME}/{GITHUB_REPO}"
    )
    assert delete_response.ok
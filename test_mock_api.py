from playwright.sync_api import *

def on_api_call(route: Route):
    # route.fulfill(
    #     json={
    #     "firstName":"Daniel",
    #     "lastName":"Smith"
    #     }
    # )

    # to modify the data we can use fetch
    response = route.fetch()
    user_data = response.json()
    print(user_data)
    user_data["firstName"] = "Kennedy"
    route.fulfill(
        response=response,
        json=user_data
    )


def test_mock_data(page: Page):
    USER_API = "https://dummyjson.com/users/1"
    page.route(USER_API, on_api_call)
    response = page.goto(USER_API)
    print(response.json())
import pytest
from playwright.sync_api import *

@pytest.fixture
def api_context(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url= "https://dummyjson.com",
        extra_http_headers={'Content-Type':'application/json'}
    )

    yield api_context # it gives the api_context to the test and once the test finishes runs the remaining code means cleanup done
    api_context.dispose() # close the api context delete all the data

def test_api_query(api_context: APIRequestContext):
    query = "Emily"
    response = api_context.get(f"/users/search?q={query}")
    user_data = response.json()

    print("Users found :", user_data["total"])

    for user in user_data["users"]:
        first = user["firstName"]
        last = user["lastName"]
        print("User name : ", first, last)
        assert (
            query.lower() in first.lower() or
            query.lower() in last.lower()
        )

def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
        "/users/add",
        headers={'Content-Type':'application/json'},
        data = {
            "firstName": "Tony",
            "lastName":"Guy"
        }
    )
    user_data = response.json()
    print(user_data)

    assert user_data["firstName"] == "Tony"

def test_update(api_context: APIRequestContext):
    print(api_context.get("/users/2").json())
    response = api_context.put(
        "/users/2",
        headers={'Content-Type':'application/json'},
        data = {
            "age":103
        }
    )
    user_data = response.json()
    print("\n Updated user record : ", user_data)

    assert user_data["age"] == 103

def test_delete_user(api_context: APIRequestContext):
    print("User record : ",api_context.get("/users/1").json())
    response = api_context.delete("/users/1")
    print("\n After deleting the record : " , response.status)
    assert response.status in [200,204]
    get_response = api_context.get("users/1")
    print("\n" , get_response.status)
    #assert get_response.status == 404
    #assert get_response["isDeleted"] is True


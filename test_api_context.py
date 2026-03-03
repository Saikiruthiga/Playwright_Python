from playwright.sync_api import Playwright, Page

def test_api_req(playwright: Playwright):

    # api_context = playwright.request.new_context()

    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )

    response = api_context.get("https://dummyjson.com/users/1") # if we are not giving the base url , we need to give the full url

    response_product = api_context.get("/products")

    user_data = response.json()
    product_data = response.json

    assert user_data["firstName"] == "Emiley"
    print(response_product)
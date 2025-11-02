from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)

    #Lauch a new page or new tab
    page = browser.new_page()

    #Visit the url
    page.goto("https://playwright.dev/python/")

    #Locate the element using its role and its name and click on the element
    docs_button = page.get_by_role('link', name="Docs")
    docs_button.click()

    #get the url
    print("Docs link :", page.url)

    #Closing the browser
    browser.close()

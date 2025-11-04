from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=1500)
    page = browser.new_page()
    url = "https://bootswatch.com/default"
    page.goto(url)
    #Locating element by its role
    page.get_by_role("link", name="Themes").click()
    #clicking outside so that the drowdown closes
    page.mouse.click(0,0)
    #Locating element by label
    page.get_by_label("Example textarea").fill("kkk")
    #Locating by text
    page.get_by_text("Radio 2").click()
    #Locating by placeholder
    page.get_by_placeholder("Recipient's username").fill("kkk")
    #Locating by title
    page.get_by_title("attribute").click()


    #Locating by CSS selector id
    page.locator("#inputLarge").fill("kkkl")
    #Locating by class name
    #new_page = page.locator(".bi.bi-github").click()
    #Locating by parent/child class name
    page.locator(".navbar.fixed-top .navbar-brand").click()
    page.go_back()
    #Locating by css attribue/value
    page.locator("button[id='btnGroupDrop3']").click()
    #Locating with pseudo class text()
    page.locator(".btn-outline-warning:text('Warning')").click()
    #Locating with pseudo class text-is()
    page.locator(".btn.btn-primary:text-is('Checkbox 2')").click()
    #nth-match
    page.locator(":nth-match(input[type=search], 1)").fill("hello")


    #XPath with functions
    page.locator("//input[contains(@value,'option2')]").check()
    #Xpath with function for visible text
    page.locator("//a[contains(text(),'Link with href')]").click()
    page.mouse.click(0,0)
    
    browser.close()
import pytest
from playwright.sync_api import Page,expect, TimeoutError

url = "http://uitestingplayground.com/"

@pytest.fixture(autouse= True)
def visit_test_page(page: Page):
    page.goto(url)

def test_dynamicid(page : Page):
    page.goto(url+"dynamicid")
    button = page.get_by_role("button", name = "Button with Dynamic ID")
    expect(button).to_be_visible()
    button.click()

def test_class(page: Page):
    page.goto("http://uitestingplayground.com/classattr")
    primary_button = page.locator("button.btn-primary")
    expect(primary_button).to_be_visible()
    primary_button.click()
    success_button = page.locator("//button[contains(@class,'btn-success')]")
    expect(success_button).to_be_visible()
    success_button.click()

def test_hiddenlayers(page: Page):
    page.goto("http://uitestingplayground.com/hiddenlayers")
    green_button = page.locator("button#greenButton")
    green_button.click()
    with pytest.raises(TimeoutError):
        green_button.click(timeout=2000)

def test_load_delay(page : Page):
    page.goto("http://uitestingplayground.com/")
    link = page.get_by_role("link", name = "Load Delay")
    expect(link).to_be_visible()
    link.click()
    button = page.get_by_role("button", name = "Button Appearing After Delay")
    expect(button).to_be_visible(timeout=5000)
    button.click()

def test_ajax(page: Page):
    page.goto("http://uitestingplayground.com/ajax")
    button = page.get_by_role("button", name = "Button Triggering AJAX Request")
    expect(button).to_be_visible()
    button.click()
    p = page.locator("p.bg-success")
    p.wait_for()
    expect(p).to_be_visible()

def test_click(page: Page):
    page.goto("http://uitestingplayground.com/click")
    btn = page.get_by_role("button",name = "Button That Ignores DOM Click Event")
    btn.click()
    expect(btn).to_have_class("btn btn-success")

def test_input(page : Page):
    page.goto("http://uitestingplayground.com/textinput")
    input = page.get_by_placeholder("MyButton")
    input.fill("Python")
    btn = page.locator("button.btn-primary")
    btn.click()
    expect(btn).to_have_text("Python") # exact match, to_contain_text => Partial match

def test_scrollbars(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")
    btn = page.get_by_role("button",name = "Hiding Button")
    btn.click()
    page.screenshot(path="screenshot.png")

def test_verify_text(page: Page):
    page.goto("http://uitestingplayground.com/verifytext")
    text = page.locator("div.bg-primary").get_by_text("Welcome")
    expect(text).to_have_text("Welcome UserName")

def test_progressbar(page : Page):
    page.goto("http://uitestingplayground.com/progressbar")
    progress_bar = page.get_by_role("progressbar")
    start_btn = page.get_by_role("button", name = "Start")
    stop_btn = page.get_by_role("button", name = "Stop")
    start_btn.click()
    while True:
        valuenow = int(progress_bar.get_attribute("aria-valuenow"))
        if valuenow >= 75:
            break
    stop_btn.click()
    assert valuenow >= 75

def test_success_login(page: Page):
    page.goto(url + "sampleapp")
    username = page.get_by_placeholder("User Name")
    password = page.get_by_placeholder("********")

    user_name = "Dan"
    pwd = "pwd"

    username.fill(user_name)
    password.fill(pwd)

    login_btn = page.get_by_role("button", name = "Log In")
    login_btn.click()

    
    label = page.locator("label#loginstatus")

    expect(label).to_have_text(f"Welcome, {user_name}! ")

def test_mouse_hover(page: Page):
    page.goto(url + "mouseover")
    
    link = page.get_by_title("Click me")
    link.hover()

    active_link = page.get_by_title("Active link")
    active_link.click(click_count=3) #we can use dblclick if we want to click the button twice

    click_count = page.locator("span#clickCount")
    expect(click_count).to_have_text("3")

def test_nbsp(page: Page):
    page.goto("http://uitestingplayground.com/nbsp")
    # btn = page.locator("button.btn-primary")
    # btn.click(timeout=2000)

    #if we want to click the button by its text MY Button, it wont work since it uses nbsp
    #//button[text()='My Button'] => this will fail


    nbsp_btn = page.locator("//button[text()='My\u00a0Button']")
    nbsp_btn.click()

def test_overlapped(page: Page):
    page.goto("http://uitestingplayground.com/overlapped")
    input = page.get_by_placeholder("Name")
    div = input.locator("..") # moving to its parent
    div.hover()
    page.mouse.wheel(0,200) # need to move vertically so x axis(horizontal move) 0
    input.fill("python")
    div.screenshot(path = "overlapped_screenshot.jpg") # just for checking
    expect(input).to_have_value("python")
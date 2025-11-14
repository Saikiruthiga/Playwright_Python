from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless = False,slow_mo = 1500, args=["--disable-dev-shm-Usage--","--disable-blink-features=AutomationControlled"])
    context = browser.new_context(storage_state="playwright/.auth/storage_state.json")
    page = context.new_page()
    page.goto("https://gmail.com")
    new_emails = []
    emails = page.locator("div.Cp table tr")
    for email in emails.all():
        is_new_email = email.locator("td li[data-tooltip='Mark as read']").count()==1
        if is_new_email:
            sender = email.locator("td span[email]:visible").inner_text()
            title = email.locator("td span[data-thread-id]:visible").inner_text()
            new_emails.append([sender,title])
    if len(new_emails) == 0:
        print("No new email")
    else:
        print(f"{len(new_emails)} new emails")
        print("-"*20)

    for new_email in new_emails:
        print(new_email[0] + ":" + new_email[1])
        print("-" * 20)
    context.close()
    
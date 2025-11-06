import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False,slow_mo=1500)
        page = await browser.new_page()
        url = "https://www.scrapethissite.com/pages/ajax-javascript/"
        await page.goto(url)
        await page.get_by_role("link",name="2015").click()
        #await page.get_by_text("Spotlight").click()
        first_td = page.locator("td.film-title").first
        await first_td.wait_for()
        #we can use wait_for_selector instead of wait_for as well like page.wait_for_selector(selector="locator")
        await first_td.click()
        await browser.close()



asyncio.run(main())
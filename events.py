import asyncio
from playwright.async_api import async_playwright 
from time import perf_counter


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False,slow_mo=1500)
        page = await browser.new_page()
        url = "https://bootswatch.com/default"
        print ("page loading....")
        start = perf_counter()
        await page.goto(url,wait_until="networkidle")
        print(await page.title())
        time = perf_counter() - start
        print (f"time taken is {round(time,2)}s")
        await browser.close()

asyncio.run(main())
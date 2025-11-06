import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless = False,slow_mo=1500)
        page = await browser.new_page()
        url = "https://unsplash.com/photos/qe2RkzzMx9A"
        await page.goto(url)
        download_button = page.get_by_role("link", name = "Download free")
        async with page.expect_download() as download_info:
            await download_button.click()
        download = await download_info.value
        await download.save_as("nature.jpg")
        await browser.close()
        
asyncio.run(main())
import asyncio
import re
from playwright.async_api import async_playwright

# Paste your seeds here as copied from the exam
SEED_INPUT = """
Seed 62
Seed 63
Seed 64
Seed 65
Seed 66
Seed 67
Seed 68
Seed 69
Seed 70
Seed 71
"""

SEEDS = re.findall(r"\d+", SEED_INPUT)
BASE_URL = "https://sanand0.github.io/tdsdata/js_table/?seed={}"

async def main():
    total_sum = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for seed in SEEDS:
            url = BASE_URL.format(seed)
            await page.goto(url)
            print(f"Scraping: {url}")

            cells = await page.locator("table td").all_inner_texts()
            for val in cells:
                try:
                    total_sum += float(val.strip())
                except ValueError:
                    continue

        await browser.close()

    print(f"\nTotal Sum: {total_sum:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
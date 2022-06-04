
from pyppeteer import launch
from src.my_logger import log

async def get_items():
    log('Fetching items...')
    browser = await launch({'headless': True, 'args': ['--no-sandbox']})
    page = await browser.newPage()
    await page.goto("https://www.lagonika.gr/")
    elementItems = await page.querySelectorAll('.la-listview-title')

    items = []
    for elementItem in elementItems:
        text = await elementItem.getProperty('innerText')
        a = await elementItem.querySelector('a')
        a_href = await a.getProperty('href')

        items.append({'text': text.toString(), 'href': a_href.toString()})
    # close the browser
    await browser.close()

    return items
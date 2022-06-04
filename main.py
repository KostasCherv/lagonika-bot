import asyncio
import time
import schedule
from src.config import INTERVAL_SECONDS
from src.my_logger import log
from src.items_controller import ItemsController
from src.scraper import get_items
from src.send_email import send_email

async def job():
    log('Starting job...')
    items = await get_items()
    items_controller = ItemsController('items.json')
    existing_items = items_controller.get()
    log('Checking for new items...')
    #  check if there are new items
    new_items = []
    for item in items:
        if item not in existing_items:
            new_items.append(item)    

    if len(new_items) > 0:
        log(f'Found {len(new_items)} new items!')
        send_email(new_items)
        items_controller.update(items)
    else:
        log('No new items found')

print('Starting bot...')
schedule.every(INTERVAL_SECONDS).seconds.do(lambda: asyncio.get_event_loop().run_until_complete(job()))

while True:
    schedule.run_pending()
    time.sleep(1)

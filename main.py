import time
import schedule
from src.config import INTERVAL_SECONDS
from src.my_logger import log
from src.items_service import ItemsService
from src.scraper import get_items
from src.item import Item
from src.send_email import send_email

items_controller = ItemsService('items.json')

def job():
    log('Starting job...')
    items = get_items()
    
    log("Got %s items" % len(items))
    existing_items = items_controller.get()
    
    log('Checking for new items...')
    new_items: list[Item] = []
    for item in items:
        if item not in existing_items:
            new_items.append(item)    

    if len(new_items) > 0:
        log(f'Found {len(new_items)} new items!')
        send_email(new_items)
        items_controller.update(items)
    else:
        log('No new items found')

log('Starting bot...')
schedule.every(INTERVAL_SECONDS).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


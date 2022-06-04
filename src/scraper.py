
from src.my_logger import log

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_items():
    log('Fetching items...')
    site = 'https://www.lagonika.gr/'
    web_request = Request(site, headers={'User-Agent':'Mozilla/5.0'})

    web_page = urlopen(web_request).read()
    soup = BeautifulSoup(web_page, 'html.parser')

    elementItems = soup.find_all('h3', class_='la-listview-title')
    items = []
    for element in elementItems:
        items.append({
            'text': element.text,
            'href': element.find('a')['href']
        })
    return items
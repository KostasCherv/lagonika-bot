from src.my_logger import log
from src.item import Item

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_items() -> list[Item]:
    log('Fetching items...')
    site = 'https://www.lagonika.gr/'
    web_request = Request(site, headers={'User-Agent':'Mozilla/5.0'})

    web_page = urlopen(web_request).read()
    soup = BeautifulSoup(web_page, 'html.parser')

    divElements = soup.find_all('div', class_='lagonika-listview-offer')
    
    items: list(Item) = []
    for element in divElements:
        img_div = element.find('div', class_='lagonika-listview-offer-top-image')
        img_src = img_div.find('img')['src']
        title = img_div.find('img')['title']
        href = element.find('a')['href']
        items.append(Item(img_src, title, href))
    return items
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

    deal_elems = soup.find_all('div', class_='prosfores')
    
    items: list(Item) = []
    for deal_elem in deal_elems:
        id = deal_elem.attrs['class'][0].split('-')[1]
        offer_elem = deal_elem.find('div', class_='lagonika-listview-offer')
        img_div = offer_elem.find('div', class_='lagonika-listview-offer-top-image')
        img_src = img_div.find('img')['src']
        price = offer_elem.find('div', class_='la-offer-price').text.strip()
        title = img_div.find('img')['title']
        href = offer_elem.find('a')['href']
        items.append(Item(id, img_src, title, href, price))
    return items
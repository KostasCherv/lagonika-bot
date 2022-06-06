
class Item:
    def __init__(self, img_src:str, title: str, href: str, price: str):
        self.img_src = img_src
        self.title = title
        self.href = href
        self.price = price

    # check equality
    def __eq__(self, other):
        return self.img_src == other['img_src'] and self.title == other['title']\
                and self.href == other['href'] and self.price == other['price']

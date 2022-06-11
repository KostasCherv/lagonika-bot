
class Item:
    def __init__(self, id: str, img_src:str, title: str, href: str, price: str):
        self.id = id
        self.img_src = img_src
        self.title = title
        self.href = href
        self.price = price

    # check equality
    def __eq__(self, other):
        return self.id == other.id

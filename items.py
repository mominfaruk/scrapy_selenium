from scrapy.item import Item, Field

class DeSpiderItem(Item):
    # define the fields for your item here like:
    basic_info = Field()
    amenities = Field()
    address = Field()
    price = Field()
    
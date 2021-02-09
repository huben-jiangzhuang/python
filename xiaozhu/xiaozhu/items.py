# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 导入包
from scrapy.item import Item,Field


class ScrapyXiaozhuItem(Item):
    # define the fields for your item here like:
    title = Field()
    address = Field()
    price = Field()
    lease_type = Field()
    suggestion = Field()
    bed = Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class KoaParks(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    state = scrapy.Field()
    city = scrapy.Field()
    zip = scrapy.Field()
    


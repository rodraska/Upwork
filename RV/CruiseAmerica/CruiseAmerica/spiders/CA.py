import scrapy


class CaSpider(scrapy.Spider):
    name = 'CA'
    allowed_domains = ['www.cruiseamerica.com']
    start_urls = ['http://www.cruiseamerica.com/']

    def parse(self, response):
        pass

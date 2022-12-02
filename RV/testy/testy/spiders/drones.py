import scrapy


class DronesSpider(scrapy.Spider):
    name = 'drones'
    allowed_domains = ['jessops.com/drones']
    start_urls = ['http://jessops.com/drones/']

    def parse(self, response):
        products = response.css('div.details-pricing')
        for product in products:
            item = {
            'name': product.css('a::text').get(),
            'price': product.css('p.price.larger::text').get().replace(',','')
            }
            yield item
        pass

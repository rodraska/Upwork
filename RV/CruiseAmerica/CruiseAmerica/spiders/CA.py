import scrapy
from scrapy_splash import SplashRequest
import cloudscraper

class CaSpider(scrapy.Spider):
    name = 'CA'
    allowed_domains = ['www.cruiseamerica.com']
    start_urls = ['http://www.cruiseamerica.com/']

    def start_requests(self):
        url = 'https://www.cruiseamerica.com/rv-rental-locations/alabama'
        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
#        scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
#        response = scraper.get(url)
        yield {'1': response.xpath('//*[@id="AnnistonAlabama"]/text()').get()}

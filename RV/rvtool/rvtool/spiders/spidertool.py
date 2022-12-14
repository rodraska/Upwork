import scrapy
from rvtool.items import RVDealer
import pandas as pd

df = pd.read_csv("coordinates.csv")

class SpidertoolSpider(scrapy.Spider):
    name = 'spidertool'
    allowed_domains = ['rvtool.com']
    start_urls = ['http://rvtool.com/']

    def give_coord(self, zip):
        lat = df[df.ZIP == zip].LAT.item()
        lng = df[df.ZIP == zip].LNG.item()
        return (lat, lng)

    def parse_dealer(self, response):
        item = RVDealer()
        item['name'] = response.css('h1[itemprop="name"]::text').get()
        bloco = response.css('td.valign-middle')
        item['address'] = bloco.css('span[itemprop="streetAddress"]::text').get()[:-1]
        item['city'] = bloco.css('span[itemprop="addressLocality"]::text').get()
        st = bloco.css('span[itemprop="addressRegion"]::text').get()
        item['state'] = response.css('span[itemprop="name"]::text').get()[:-11]
        zip = bloco.css('span[itemprop="postalCode"]::text').get()
        item['zip'] = zip
        item['lat'], item['lng'] = self.give_coord(int(zip))
        yield (item)

    def parse_pages(self, response):
        items = response.css('div.listing-list__item__label.flex-auto')
        links = items.css('a::attr(href)').getall()
        for link in links:
            yield scrapy.Request(url='http://rvtool.com/' + link, callback=self.parse_dealer)

    def parse_states(self, response):
        pagination = response.css('ul.pagination')
        if len(pagination) == 0:
            items = response.css('div.listing-list__item__label.flex-auto')
            links = items.css('a::attr(href)').getall()
            for link in links:
                yield scrapy.Request(url='http://rvtool.com/' + link, callback=self.parse_dealer)
            # link = response.url
            # yield scrapy.Request(url=link, callback=self.parse_pages)
        else:
            if response.url == 'https://rvtool.com/California/?page=15':
                pages = pagination.css('a::attr(href)').getall()[1:-1]
            elif response.url == 'https://rvtool.com/California/?page=24':
                pages = pagination.css('a::attr(href)').getall()[1:]
            if response.url == 'https://rvtool.com/Texas/?page=20':
                pages = pagination.css('a::attr(href)').getall()[1:]
            else:
                pages = pagination.css('a::attr(href)').getall()[:-1]
            all_state_links = []
            for page in pages:
                all_state_links.append('http://rvtool.com' + page)
            for link in all_state_links:
                yield scrapy.Request(url=link, callback=self.parse_pages)
        

    def parse(self, response):
        select = response.css('select.field.block.mr1')
        states_no = select.css('option::text').getall()
        states = []
        for state in states_no:
            states.append(state.replace(' ', '-'))
        states.append('California/?page=15')
        states.append('California/?page=24')
        states.append('Texas/?page=20')
        for state in states:
            yield scrapy.Request(url='http://rvtool.com/' + state, callback=self.parse_states)

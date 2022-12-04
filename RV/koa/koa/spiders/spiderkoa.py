import scrapy
from koa.items import KoaParks
import re
import pandas as pd

""" df = pd.read_csv("coordinates.csv")

print(df) """

class SpiderkoaSpider(scrapy.Spider):
    name = 'spiderkoa'
    allowed_domains = ['koa.com']
    start_urls = ['https://koa.com/campgrounds/']
    state = ""

    """ def give_coord(self, zip):
        lat = df[df.ZIP == zip].LAT.item()
        lng = df[df.ZIP == zip].LNG.item()
        return (lat, lng) """

    def separate_ziptotal(self, ziptotal):
        city = re.sub(r',[ ](\w)*[ ](\w)*', '', ziptotal)
        zip = re.sub(r'((\w)*.)?((\w)*[ ]?)*,[ ](\w)*[ ]', '', ziptotal)
        state_small = re.sub(r'[ ](\w)*$','',(re.sub(r'((\w)*.)?((\w)*[ ]?)*,[ ]', '', ziptotal)))
        return (city, zip, state_small)

    def parse_parks(self, response):
        item = KoaParks()
        camp_info = response.css('div.col-xs-11.col-sm-10.col-lg-7')
        city, zip, state_small = self.separate_ziptotal(camp_info.css('b::text')[4].get())
        item['name'] = camp_info.css('h2.mt-0.font-size-h1::text').get()
        item['address'] = camp_info.css('b::text')[3].get()
        item['state'] = self.state
        item['city'] = city
        item['zip'] = zip[:5]
        yield (item)
    
    def parse_states(self, response):
        state_camps = response.css('div.col-xs-6.col-sm-6.col-md-6.col-lg-4.margin-bottom-15.campground-listing-container')
        camps_links = state_camps.css('a.btn.btn-red.text-upper.state-reserve::attr(href)').getall()
        self.state=response.xpath('//span[@class="title"]/text()').get()[19:]
        for camp in camps_links:
            yield scrapy.Request(url='https://koa.com' + camp, callback=self.parse_parks)

    def parse(self, response):
        states_odd = response.css('li.odd')
        states_even = response.css('li.even')
        all_states = states_odd + states_even
        states_links = []
        for state in all_states:
            states_links.append(state.css('a::attr(href)')[0].get())
        for state_link in states_links:
            yield scrapy.Request(url='https://koa.com' + state_link, callback=self.parse_states)

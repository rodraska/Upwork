import scrapy
from CampingWorld.items import CampingworldItem
import re


class CwSpider(scrapy.Spider):
    name = 'CW'
    allowed_domains = ['rv.campingworld.com']
    start_urls = ['https://rv.campingworld.com/state-directory']

    def separate_city_zipcode(self, cities_zipcodes):
        cities = []
        zipcodes = []
        states_small = []
        for elem in cities_zipcodes:
            cities.append(re.sub(r',[ ](\w)*[ ](\w)*', '', elem))
            zipcodes.append(re.sub(r'((\w)*.)?((\w)*[ ]?)*,[ ](\w)*[ ]', '', elem))
            states_small.append(re.sub(r'[ ](\w)*$','',(re.sub(r'((\w)*.)?((\w)*[ ]?)*,[ ]', '', elem))))
        return (cities, zipcodes, states_small)
    
    def creat_states_dict(self, states, states_small):
        states_small = sorted(list(set(states_small)))
        states = sorted(states)
        states_dict = {}
        for state, state_small in zip(states, states_small):
            states_dict[state_small] = state
        return (states_dict)

    def parse(self, response):
        item = CampingworldItem()
        names = response.xpath('//div[@class="container max1296 stateList"]//li/a/text()').getall()
        addresses  = response.xpath('//div[@class="container max1296 stateList"]//li/p[@class="billing_street"]/text()').getall()
        states = response.xpath('//div[@class="container max1296 stateList"]/h3/text()').getall()
        cities, zipcodes, states_small = self.separate_city_zipcode(response.xpath('//div[@class="container max1296 stateList"]//li/p[2]/text()').getall())
        states_dict = self.creat_states_dict(states, states_small)
        print(sorted(list(set(states_small))))
        for name, address, state_small, city, zipcode in zip(names, addresses, states_small, cities, zipcodes):
            item['name'] = name
            item['address'] = address
            item['state'] = states_dict[state_small]
            item['city'] = city
            item['zipcode'] = zipcode
            yield item

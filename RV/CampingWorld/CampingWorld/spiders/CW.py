import scrapy
from CampingWorld.items import CampingworldItem
import re
import pandas as pd


class CwSpider(scrapy.Spider):
    name = 'CW'
    allowed_domains = ['rv.campingworld.com']
    start_urls = ['https://rv.campingworld.com/state-directory']
    states_dict = {'AL': 'ALABAMA',
                'AZ': 'ARIZONA', 
                'AR': 'ARKANSAS', 
                'CA': 'CALIFORNIA', 
                'CO': 'COLORADO', 
                'FL': 'FLORIDA', 
                'GA': 'GEORGIA', 
                'ID': 'IDAHO', 
                'IL': 'ILLINOIS', 
                'IN': 'INDIANA', 
                'IA': 'IOWA', 
                'KS': 'KANSAS', 
                'KY': 'KENTUCKY', 
                'LA': 'LOUISIANA', 
                'ME': 'MAINE', 
                'MA': 'MASSACHUSETTS', 
                'MI': 'MICHIGAN', 
                'MN': 'MINNESOTA', 
                'MS': 'MISSISSIPPI', 
                'MO': 'MISSOURI', 
                'NE': 'NEBRASKA', 
                'NV': 'NEVADA', 
                'NH': 'NEW HAMPSHIRE', 
                'NJ': 'NEW JERSEY', 
                'NM': 'NEW MEXICO', 
                'NY': 'NEW YORK', 
                'NC': 'NORTH CAROLINA', 
                'ND': 'NORTH DAKOTA', 
                'OH': 'OHIO', 
                'OK': 'OKLAHOMA', 
                'OR': 'OREGON', 
                'PA': 'PENNSYLVANIA', 
                'SC': 'SOUTH CAROLINA', 
                'SD': 'SOUTH DAKOTA', 
                'TN': 'TENNESSEE', 
                'TX': 'TEXAS', 
                'UT': 'UTAH', 
                'VA': 'VIRGINIA', 
                'WA': 'WASHINGTON', 
                'WV': 'WEST VIRGINIA', 
                'WI': 'WISCONSIN', 
                'WY': 'WYOMING'}

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
        for name, address, state_small, city, zipcode in zip(names, addresses, states_small, cities, zipcodes):
            item['name'] = name
            item['address'] = address
            item['state'] = self.states_dict[state_small]
            item['city'] = city
            item['zipcode'] = zipcode
            yield item
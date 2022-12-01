# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class house_details(scrapy.Item):
	item = scrapy.Field()
	tipologia = scrapy.Field()
	preco = scrapy.Field()
	wc = scrapy.Field()
	area = scrapy.Field()
	address = scrapy.Field()
	listing_name = scrapy.Field()
	descricao = scrapy.Field()
	bairro = scrapy.Field()
	ano_de_construcao = scrapy.Field()
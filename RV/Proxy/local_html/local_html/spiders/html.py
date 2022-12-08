import scrapy
from local_html.items import LocalHtmlItem

class HtmlSpider(scrapy.Spider):
	name = 'html'
	start_urls = ['file:///home/miguel/Desktop/Upwork/RV/Proxy/rvt.html']

	def parse(self, response):
		item = LocalHtmlItem()
		names = response.xpath('//ul[@class="three-col-list"]/li/span[1]/text()').getall()
		places = response.xpath('//ul[@class="three-col-list"]/li/span[2]/text()').getall()
		numbers = response.xpath('//ul[@class="three-col-list"]/li/span[3]/text()').getall()
		for name, place, number in zip(names, places, numbers):
			item['name'] = name
			item['place'] = place
			item['number'] = number
			yield item
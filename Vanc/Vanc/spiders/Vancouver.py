import scrapy
from Vanc.items import house_details

class VancouverSpider(scrapy.Spider):
    name = 'Vancouver'
    allowed_domains = ['www.zumper.com']
    start_urls = ['https://www.zumper.com/apartment-buildings/p780822/burrard-place-rental-downtown-vancouver-vancouver-bc',
        'https://www.zumper.com/apartment-buildings/p615374/chronicle-west-end-vancouver-bc',
        'https://www.zumper.com/apartment-buildings/p561687/arbutus-residences-quilchena-vancouver-bc']

    def parse(self, response):
        item = house_details()
        item['address'] = response.xpath('//h1[@class="Header_headerText__39zS4"]/span/text()').get()
        item['listing_name'] = response.xpath('//h1[@class="Header_headerText__39zS4"]/text()').get()
        item['descricao'] = response.xpath('//div[@class="css-voxcx"]/text()').get()
        item['bairro'] = response.xpath('//div[@class="Header_subHeader__Am2F2"]/p/text()').getall()[2]
        item['ano_de_construcao'] = response.xpath('//div[@class="css-8jkrjq"]//dd/text()').get()

        tipos = response.xpath('//div[@class="css-zjik7"]//div[@class="css-1jwryq8"]').getall()
        precos = response.xpath('//div[@class="css-zjik7"]//div[@class="css-11mm0h3"]/text()').getall()
        wcs = response.xpath('//div[@class="css-zjik7"]//div[@class="css-1ukfvem"]/span/text()').getall()
        areas = response.xpath('//div[@class="css-zjik7"]//div[@class="css-13koqug"]/span/text()').getall()

        for tipo, preco, wc, area in zip(tipos, precos, wcs, areas):
            item['tipologia'] = tipo
            item['preco'] = preco
            item['wc'] = wc
            item['area'] = area
            yield item
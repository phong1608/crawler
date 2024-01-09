from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingspidernewSpider(CrawlSpider):
    name = "spider"
    allowed_domains = ["homedy.com"]
    start_urls = ["https://homedy.com/cho-thue-nha-tro-phong-tro-ha-noi"]
    rules = (
        Rule(LinkExtractor(allow="cho-thue-nha-tro-phong-tro-ha-noi/"),callback='parse_item'),
    )
    
    def parse_item(self,response):
        item = {
            "name": response.css('.title.padding-hoz::text').getall(),
            "price": response.css('.price::text').getall(),
            'acreage': response.css('.acreage::text').getall(),
            'location': response.css('.address::text').getall(),
        }        

        yield item
    

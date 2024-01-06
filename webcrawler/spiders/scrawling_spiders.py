from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name="mcrawler"
    allowed_domains =['phongtro123.com']
    start_urls = ["https://phongtro123.com/tinh-thanh/ha-noi"]
    rules = (
        Rule(LinkExtractor(allow="tinh-thanh/ha-noi"),callback='parse_item'),
    )
    
    def parse_item(self,response):
        item = {
            "name": response.css('.post-title a::text').get(),
            "price": response.css('.post-price::text').get(),
            'acreage': response.css('.post-acreage::text').get(),
            'location': response.css('.post-location a::text').get(),
        }        

        yield item
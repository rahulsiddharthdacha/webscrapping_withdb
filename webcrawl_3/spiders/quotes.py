import scrapy
from ..items import Webcrawl3Item
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items=Webcrawl3Item()
        rows = response.xpath('//div[@class="quote"]')
        for row in rows:
            quote = "".join(row.xpath('span[@class="text"]/text()').extract())
            author = "".join(row.xpath('span/small[@class="author"]/text()').extract())
            tags=",".join(row.xpath('div[@class="tags"]/a[@class="tag"]/text()').extract())
            items['quote']= quote
            items['author']= author
            items['tags']=tags
            yield items

import scrapy
from ..items import QuotesscraperItem
class QuotesSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]
    def parse(self, response):
        item=QuotesscraperItem()
        quote_container=response.css('div.quote')
        for quotes in quote_container:
            quote=quotes.css('span.text::text').extract()
            author=quotes.css('.author::text').extract()
            tag=quotes.css('.tag::text').extract()
            item['quote']=quote
            item['author']=author
            item['tag']=tag
            yield item
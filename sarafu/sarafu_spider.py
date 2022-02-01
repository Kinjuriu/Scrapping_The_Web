import scrapy


class SarafuSpiderSpider(scrapy.Spider):
    name = 'sarafu_spider'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/']

    def parse(self, response):
        pass

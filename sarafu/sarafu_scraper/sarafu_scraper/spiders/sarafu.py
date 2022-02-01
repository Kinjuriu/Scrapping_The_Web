import scrapy


class SarafuSpider(scrapy.Spider):
    name = 'sarafu'
    allowed_domains = ['grassrootseconomics.org']
    start_urls = ['http://grassrootseconomics.org/post/independent-survey-of-325-sarafu-users']

    def parse(self, response):
        return {
            'title' : response.xpath('//span[@class="blog-post-title-font blog-post-title-color"]/text()').get(),
             #'title': response.xpath('//span[@class="blog-post-title-font blog-post-title-color"]/text()').get(),
             'date' : response.xpath('//span[@class="post-metadata__date time-ago"]/text()').get(),
             # 'date': response.xpath('//meta[@name="post-metadata__date time-ago"]/@content').get(),
             #'author': response.xpath('//span[@class="iYG_V user-name _4AzY3"]/text()').get(),
             'author': response.xpath('//span[@class="iYG_V user-name _4AzY3"]/text()').get(),
             }

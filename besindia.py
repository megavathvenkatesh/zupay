import scrapy


class BesindiaSpider(scrapy.Spider):
    name = "besindia"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass

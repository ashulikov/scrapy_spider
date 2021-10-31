import logging
import scrapy
from lxml.html import fromstring

from macrumors.items import MacrumorsItem
from scrapy.loader import ItemLoader

log = logging.getLogger(__name__)

class MacrumorsSpider(scrapy.Spider):
    name = "macrumors"
    start_urls = [
        "https://www.macrumors.com/",
    ]

    def parse_page(self, response):
        html = fromstring(response.text)
        html.make_links_absolute(response.url)
        for article in html.xpath("//div[@class='titlebar--3N4MCKxL']/h2/a/@href"):
            yield scrapy.Request(article, callback=self.parse_article)
        for next_page in html.xpath("//div[@class='link--1OlCtRel right']/a/@href"):
            yield scrapy.Request(next_page, callback=self.parse_page)

    def parse_article(self, response):
        loader = ItemLoader(MacrumorsItem(), response)
        
        loader.add_xpath("published_date", "//div[@class='byline--3Eec5bcq']//@datetime")
        loader.add_xpath("text", "//div[@class='content--2u3grYDr js-content']//div[@class='ugc--2nTu61bm minor--3O_9dH4U']/p//text()")
        loader.add_xpath("title", "//h1[@class='heading--1cooZo6n heading--h5--3l5xQ3lN heading--white--2vAPsAl1 heading--noMargin--mnRHPAnD']/text()")

        yield loader.load_item()
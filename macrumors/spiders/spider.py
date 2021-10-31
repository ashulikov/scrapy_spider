import logging

import scrapy
from lxml.html import fromstring
from scrapy.loader import ItemLoader

from macrumors.items import MacrumorsItem

log = logging.getLogger(__name__)


class MacrumorsSpider(scrapy.Spider):
    name = 'macrumors'
    start_urls = [
        'https://www.macrumors.com/',
    ]

    def parse(self, response):
        html = fromstring(response.text)
        html.make_links_absolute(response.url)
        articles = html.xpath("//div[@class='titlebar--3N4MCKxL']/h2/a/@href")
        pagination = html.xpath("//div[@class='link--1OlCtRel right']/a/@href")
        for article in articles:
            yield scrapy.Request(article, callback=self.parse_article)
        for next_page in pagination:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_article(self, response):
        loader = ItemLoader(MacrumorsItem(), response)

        loader.add_xpath(
            'published_date',
            "//div[@class='byline--3Eec5bcq']//@datetime",
        )
        loader.add_xpath(
            'text', "//div[@class='content--2u3grYDr js-content']" +
            "//div[@class='ugc--2nTu61bm minor--3O_9dH4U']/p//text()",
        )
        loader.add_xpath(
            'title', "//h1[@class='heading--1cooZo6n heading--h5--3l5xQ3lN " +
            "heading--white--2vAPsAl1 heading--noMargin--mnRHPAnD']/text()",
        )

        yield loader.load_item()

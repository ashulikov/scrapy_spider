# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join

class MacrumorsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor=Join())
    published_date = scrapy.Field()
    text = scrapy.Field(input_processor=Join())

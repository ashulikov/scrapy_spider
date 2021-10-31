# Scrapy settings for macrumors project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'macrumors'

SPIDER_MODULES = ['macrumors.spiders']
NEWSPIDER_MODULE = 'macrumors.spiders'

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1
ITEM_PIPELINES = {
    'macrumors.pipelines.MacrumorsPipeline': 0,
}

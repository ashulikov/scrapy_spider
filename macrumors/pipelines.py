# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import yaml


class MacrumorsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        with open(f"data/{adapter.get('published_date')[0][:-6]}.yaml", 'w') as file:
            yaml.dump(adapter.asdict(), file)
        return item

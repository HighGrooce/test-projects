# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from pymongo import MongoClient


class WangyiPipeline:
    def open_spider(self, spider):
        if spider.name == 'job':
            self.file = open('wangyi.json','w')

    def process_item(self, item, spider):
        if spider.name == 'job':
            item = dict(item)
            str_data = json.dumps(item,ensure_ascii=False) + ',\n'
            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        if spider.name == 'job':
            self.file.close()

class Wangyi2Pipeline:
    def open_spider(self, spider):
        if spider.name == 'job2':
            self.file = open('wangyi2.json','w')

    def process_item(self, item, spider):
        if spider.name == 'job2':
            item = dict(item)
            str_data = json.dumps(item,ensure_ascii=False) + ',\n'
            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        if spider.name == 'job2':
            self.file.close()

class MongoPipline(object):
    def open_spider(self, spider):
        if spider.name == 'job2':
            self.client = MongoClient('127.0.0.1',27017)
            self.db = self.client['client']
            self.col = self.db['wangyi']

    def process_item(self, item, spider):
        if spider.name == 'job2':
            data = dict(item)
            self.col.insert_many(data)
            return item

    def close_spider(self, spider):
        if spider.name == 'job2':
            self.client.close()
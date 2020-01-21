# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QsbkPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self):
        self.f = open("demo.json","wb+")

    def process_item(self,item,spider):
        content = json.dumps(dict(item),ensure_ascii =False) + ",\n"
        return item

    def close_spider(self,spider):
        self.f.close()

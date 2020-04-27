# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class FanziPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient()
    def process_item(self, item, spider):
        self.client.fanzi.fantepy.insert_one({'_id':item['fid'],'title':item['title'],'fanshi':item['fanshi'],'money':item['money']})
    def close_spider(self,spider):
        self.client.close()
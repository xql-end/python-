# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class XiaoshuoPipeline(object):
    def open_spider(self,spider):
        self.findname = open('xiaoshou.txt','a',encoding='utf-8')
    def process_item(self, item, spider):
        title = item['title']
        counter= item['counter']
        info = title+'\n'+counter+'\n'
        self.findname.write(info)
        return item
    def close_spider(self,spider):
        self.findname.close()

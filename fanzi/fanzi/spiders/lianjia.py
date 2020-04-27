# -*- coding: utf-8 -*-
import scrapy
import re

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/zufang/pg{}/#contentList'.format (i) for i in range(1,100)]

    def parse(self, response):
        urls = response.xpath('//div[@class="content__list--item--main"]/p[1]/a[1]/@href').extract()
        for url in urls:
            urlf = 'https://bj.lianjia.com'+url
            yield scrapy.Request(urlf,callback=self.parse_info)

    def parse_info(self,response):
        print("---------------------------------------------------------------------------")
        money = response.xpath('//div[@class="content__aside--title"]/span/text()').extract_first()
        title = response.xpath('//p[@class="content__title"]/text()').extract_first()
        fanshi = response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').extract_first()
        idr = response.xpath('//i[@class="house_code"]/text()').extract_first()
        fid = "".join(re.findall(r'：\S(.*)',idr))
        yield {
            'money':money,
            'title':title,
            'fanshi':fanshi,
            'fid':fid
        }

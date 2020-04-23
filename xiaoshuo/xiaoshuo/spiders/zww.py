# -*- coding: utf-8 -*-
import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['81zhongwen.com']
    start_urls = ['https://www.81zw.com.tw/book/806/36285059.html']

    def parse(self, response):
       title = response.xpath('//h1/text()').extract_first()
       counter = "".join(response.xpath('//div[@class="panel-body"]/text()').extract())
       yield {
           'title':title,
           'counter':counter
       }
       new_url = response.xpath('//a[@id="linkNext"]/@href').extract_first()
       print(response.urljoin(new_url))
       if new_url.find('.html')!=-1:
           print(response.urljoin(new_url))
           yield scrapy.Request(response.urljoin(new_url), callback=self.parse)

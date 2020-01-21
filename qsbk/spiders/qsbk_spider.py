# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qbspider'
    allowed_domains = ['aitaotu.com']
    start_urls = ['https://www.aitaotu.com/weimei/48593.html']

    def parse(self, response):
        print('*' * 40)
        # node_list = response.xpath("//div[@id='big_pic']")
        node_list = response.xpath("//a[@href='/weimei/48095.html']")
        for node in node_list:
            item = QsbkItem()
            name = node.xpath("img/@src").extract()
            item['url'] = name[0]
            yield item
        print('*' * 40)

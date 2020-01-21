# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qbspider'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        print('*' * 40)
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            item = QsbkItem()
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()
            item['name'] = name
            item['title'] = title
            item['info'] = info
            yield item
        print('*' * 40)

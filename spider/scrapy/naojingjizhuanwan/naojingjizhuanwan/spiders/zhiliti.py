# -*- coding: utf-8 -*-
import scrapy


class ZhilitiSpider(scrapy.Spider):
    name = 'zhiliti'
    allowed_domains = ['zhiliti.com.cn/html/jizhuanwan/list3_1.html']
    start_urls = ['http://zhiliti.com.cn/html/jizhuanwan/list3_1.html/']

    def parse(self, response):
        pass

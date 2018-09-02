# -*- coding: utf-8 -*-
import scrapy
import re

class ZhilitiSpider(scrapy.Spider):
    name = 'zhiliti'
    start_urls = ['http://www.zhiliti.com.cn/html/jizhuanwan/']

    def parse(self, response):
        for part in response.css("li"):
            if(part.css("span::attr(onclick)").extract_first() == None):
                continue

            yield {
                'description': part.css("h2 > a::text").extract(),
                'answer': part.css("span::attr(onclick)").extract_first().replace("javascript:innerText=(","").replace(");","")
            }
        next_page_url = response.css("div.pagebar > a.next_page::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

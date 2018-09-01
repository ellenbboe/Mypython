# -*- coding: utf-8 -*-
import scrapy


class JuzimiSpider(scrapy.Spider):
    name = 'juzimi'
    start_urls = ['http://juzimi.com/recommend/']

    def parse(self, response):
        for said in response.css("div.views-field-phpcode"):
            yield {
                'description': said.css("div.views-field-phpcode-1 > a::text").extract(),
                'author': said.css("div.xqjulistwafo > a::text").extract_first()
            }
        next_page_url = response.css("li.pager-next > a::attr(href)").extract_first()
        #next_page_url = None
        if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url),callback=self.parse)
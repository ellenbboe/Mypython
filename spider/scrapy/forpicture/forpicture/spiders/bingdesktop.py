# -*- coding: utf-8 -*-
import scrapy


class BingdesktopSpider(scrapy.Spider):
    name = 'bingdesktop'
    start_urls = ['https://bing.ioliu.cn/']

    def parse(self, response):
        for onepicture in response.css("div.item"):
            yield {
                'description' : onepicture.css("div.description > h3::text").extract_first(),
                'time' : onepicture.css("div.description > p.calendar > em::text").extract_first(),
                'location' : onepicture.css("div.description > p.location > em::text").extract_first(),
                'download' : onepicture.css("img::attr(src)").extract_first().replace("400x240","1920x1080")
            }
        #next_page_url = response.css("div.page > a::attr(href)").extract()[1] #所有页面
        next_page_url = None#只有一页
        if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url),callback=self.parse)



# -*- coding: utf-8 -*-
import scrapy


class AnimationlistSpider(scrapy.Spider):
    name = 'animationlist'
    #allowed_domains = ['bilibili.com/anime/index']
    start_urls = ['https://www.bilibili.com/anime/index/']

    def parse(self, response):
        for anime in response.css("li.bangumi-item"):
            yield{
                '番剧名':anime.css('a.bangumi-title::text').extract_first(),
                '更新':anime.css("p::text").extract_first(),
                '追番人数':anime.css("a.cover-wrapper > div.shadow::text").extract_first(),
                '播放链接':anime.css('a.bangumi-title::attr(href)').extract_first(),
                '封面链接':'http:'+anime.css("div.common-lazy-img > img::attr(src)").extract_first()
            }
        nextpage = None
        if nextpage is not None:
                yield scrapy.Request(response.urljoin(nextpage),callback=self.parse)


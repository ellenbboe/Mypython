# -*- coding: utf-8 -*-
import scrapy


class StartSpider(scrapy.Spider):
    name = 'start'
    fromplace="from=shanghai"
    toplace="&to=beijing"
    date="&day=2018-09-06"
    start_urls = ['http://trains.ctrip.com/TrainBooking/Search.aspx?'+fromplace+toplace+date]

    def parse(self, response):
        pass

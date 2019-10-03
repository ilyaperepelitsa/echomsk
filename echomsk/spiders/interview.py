# -*- coding: utf-8 -*-
import scrapy


class InterviewSpider(scrapy.Spider):
    name = 'interview'
    allowed_domains = ['echo.msk.ru']
    start_urls = ['http://echo.msk.ru/']

    def parse(self, response):
        pass

    def parse_interview(self, response):
        # date
        response.xpath('//div[@class="date left"]//strong/text()').get()
        # gue
        pass

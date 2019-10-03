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
        # guest name
        response.xpath('//div[contains(@class, "author")]//*[@class="name"]/text()').get()
        # guest title
        response.xpath('//div[contains(@class, "author")]//*[@class="post"]/text()').get()
        # host name
        //div[contains(@class, "lead")]//a//text()

        text = response.xpath('//div[@class="mmcontainer"]//p//text()').getall()
        text = [i.replace('\r\n', '').strip() for i in text]
        # text = [i for i in text if i != "\r\n"]
        text = [re.sub(r'^НОВОСТИ|новости$', '', i) for i in text]
        text = [i.strip() for i in text]
        pass

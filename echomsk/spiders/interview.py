# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

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

        text = response.xpath('//div[@class="mmcontainer"]//p').getall()
        whole_interview = []
        current_text = ""
        current_speaker = ""
        for index, paragraph in enumerate(text):
            chunk = Selector(text=paragraph).xpath('//text()').getall()
            chunk = [i.replace('\r\n', '').strip() for i in chunk]
            chunk = [re.sub(r'^НОВОСТИ|новости$', '', i) for i in chunk]
            chunk = [i.strip() for i in chunk]
            chunk = [i for i in chunk if len(i) > 1]
            if len(chunk) > 1:
                current_speaker = chunk[0]
                current_text = chunk[-1]
            elif len(chunk) == 1:
                current_text += " "
                current_text += chunk[0]


            next_chunk = text[index + 1]
            next_chunk = Selector(text=paragraph).xpath('//text()').getall()
            chunk = [i.replace('\r\n', '').strip() for i in chunk]
            chunk = [re.sub(r'^НОВОСТИ|новости$', '', i) for i in chunk]
            chunk = [i.strip() for i in chunk]
            chunk = [i for i in chunk if len(i) > 1]

            if index < len(text) and text[index + 1]

        # text = [i.replace('\r\n', '').strip() for i in text]
        # # text = [i for i in text if i != "\r\n"]
        # text = [re.sub(r'^НОВОСТИ|новости$', '', i) for i in text]
        # text = [i.strip() for i in text]
        # text = [i for i in text if len(i) > 1]
        pass



pew = ['a', 'b', 'c', 'd']
pew[::2]
pew[1::2]

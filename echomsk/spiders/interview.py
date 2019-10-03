# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


def clean_chunk(text):
    chunk = Selector(text=text).xpath('//text()').getall()
    chunk = [i.replace('\r\n', '').strip() for i in chunk]
    chunk = [re.sub(r'^НОВОСТИ|новости$', '', i) for i in chunk]
    chunk = [i.strip() for i in chunk]
    chunk = [i for i in chunk if len(i) > 1]
    return chunk

class InterviewSpider(scrapy.Spider):
    name = 'interview'
    allowed_domains = ['echo.msk.ru']
    start_urls = ['https://echo.msk.ru/programs/personalno/']

    rules = [
        Rule(
            LinkExtractor(
                restrict_xpaths = '//*[@class="pager"]',
                # canonicalize=True,
                unique=True

            ),
            callback="parse",
            follow=True),
        Rule(
            LinkExtractor(
                restrict_xpaths = '//*[@class="content"]//div[@class="rel"]//div[contains(@class, "preview")]//*[@class="txt"]',
                # canonicalize=True,
                unique=True,

            ),
            callback="parse_interview",
            follow=True)

    ]


    def parse(self, response):
        # print(response.url)
        print(response.xpath('//*[@class="content"]//div[@class="rel"]//div[contains(@class, "preview")]//*[@class="txt"]').getall())
        # pass

    def parse_interview(self, response):
        # # date
        # response.xpath('//div[@class="date left"]//strong/text()').get()
        # # guest name
        # response.xpath('//div[contains(@class, "author")]//*[@class="name"]/text()').get()
        # # guest title
        # response.xpath('//div[contains(@class, "author")]//*[@class="post"]/text()').get()
        # # host name
        # //div[contains(@class, "lead")]//a//text()

        text = response.xpath('//div[@class="mmcontainer"]//p').getall()
        whole_interview = []
        current_text = ""
        current_speaker = ""
        for index, paragraph in enumerate(text):
            chunk = clean_chunk(paragraph)
            if len(chunk) > 1:
                current_speaker = chunk[0]
                current_text = chunk[-1]
            elif len(chunk) == 1:
                current_text += " "
                current_text += chunk[0]

            if (index + 1) < len(text):
                next_chunk = clean_chunk(text[index + 1])
                if len(next_chunk) != 1:
                    whole_interview.append(tuple(index, current_speaker,
                                                        current_text))
                    current_text = ""
                    current_speaker = ""
                else:
                    pass
            else:
                whole_interview.append(tuple(index, current_speaker,
                                                    current_text))
                # current_text = ""
                # current_speaker = ""
        print(whole_interview)




        # text = [i.replace('\r\n', '').strip() for i in text]
        # # text = [i for i in text if i != "\r\n"]
        # text = [re.sub(r'^НОВОСТИ|новости$', '', i) for i in text]
        # text = [i.strip() for i in text]
        # text = [i for i in text if len(i) > 1]
        pass



# pew = ['a', 'b', 'c', 'd']
# pew[::2]
# pew[1::2]
#
#
# response.xpath('//div[@class = "content")]\
#                 //div[@class = "rel")]\
#                 //div[contains(@class, "preview")]').get()
#
#
#
# response.xpath('//*[@class="content"]//div[@class="rel"]//div[contains(@class, "preview")]//p[@class="text"]').get()

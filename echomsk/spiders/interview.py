# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
import re

def clean_chunk(text):

    chunk = Selector(text=text).xpath('//text()').getall()
    chunk = [i.replace('\r\n', '').strip() for i in chunk]
    chunk = [re.sub(r'^НОВОСТИ|новости$', '', i) for i in chunk]
    chunk = [i.strip() for i in chunk]
    chunk = [i for i in chunk if len(i) > 1]
    return chunk

class InterviewSpider(CrawlSpider):
    name = 'interview'
    # allowed_domains = ['echo.msk.ru']
    start_urls = ['https://echo.msk.ru/programs/personalno/']

    rules = [
        Rule(
            LinkExtractor(
                restrict_xpaths = '//*[@class="pager"]',
                canonicalize = True,
                unique=True
            ),
            follow=True),
        Rule(
            LinkExtractor(
                restrict_xpaths = '//*[@class="content"]//div[@class="rel"]//div[contains(@class, "preview")]//*[@class="txt"]',
                canonicalize = True,
                unique=True
            ),
            follow=True,
            callback="parse_interview")
            ]




    # def parse(self, response):
    #     # print(self.rules)
    #     # print(response.url)
    #     # print(response.xpath('//*[@class="content"]//div[@class="rel"]//div[contains(@class, "preview")]//*[@class="txt"]//@href').getall())
    #     pass

    def parse_interview(self, response):
        # # date
        # response.xpath('//div[@class="date left"]//strong/text()').get()
        # # guest name
        # response.xpath('//div[contains(@class, "author")]//*[@class="name"]/text()').get()
        # # guest title
        # response.xpath('//div[contains(@class, "author")]//*[@class="post"]/text()').get()
        # # host name
        # //div[contains(@class, "lead")]//a//text()

        text = response.xpath('//div[@class="mmplayer"]//div[contains(@class, "typical")]//*[not(name()="blockquote")]').getall()
        whole_interview = []
        current_text = ""
        current_speaker = ""
        for index, paragraph in enumerate(text):
            chunk = Selector(text=text)
            # chunk_name = chnk.xpath('name()')
            print(paragraph)
        #
        #     chunk = clean_chunk(paragraph)
        #     if len(chunk) > 1:
        #         current_speaker = chunk[0]
        #         current_text = chunk[-1]
        #     elif len(chunk) == 1:
        #         current_text += " "
        #         current_text += chunk[0]
        #
        #     if (index + 1) < len(text):
        #         next_chunk = clean_chunk(text[index + 1])
        #         if len(next_chunk) != 1:
        #             whole_interview.append([index, current_speaker,
        #                                                 current_text])
        #             current_text = ""
        #             current_speaker = ""
        #         else:
        #             pass
        #     else:
        #         whole_interview.append([index, current_speaker,
        #                                             current_text])
        #
        # for i in whole_interview:
        #     print(i)




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

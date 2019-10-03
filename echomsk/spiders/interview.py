# -*- coding: utf-8 -*-
import scrapy
import locale
import datetime

from scrapy.selector import Selector

from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
import re


from scrapy.loader import ItemLoader
import json
from echomsk.items import InterviewParagraph
from echomsk.models import *
from echomsk.functions import *

from sqlalchemy import and_

def clean_chunk(text):

    chunk = Selector(text=text).xpath('//text()').getall()
    chunk = [i.replace('\r\n', '').strip() for i in chunk]
    chunk = [re.sub(r'^НОВОСТИ|новости|РЕКЛАМА|реклама$', '', i) for i in chunk]
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
        broadcast_date = response.xpath('//div[@class="date left"]//strong/text()').get()
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        broadcast_date = datetime.datetime.strptime(broadcast_date, u'%d %B %Y').date()

        # guest name
        guest_name = response.xpath('//div[contains(@class, "author")]//*[@class="name"]/text()').get()
        # # guest title
        guest_title = response.xpath('//div[contains(@class, "author")]//*[@class="post"]/text()').get()
        # # host name
        host_name = response.xpath('//div[contains(@class, "lead")]//a//text()').get()

        interview_exists = session_test.query(exists().where(and_(
                    InterviewParagraph.date == broadcast_date,
                    InterviewParagraph.guest_name == guest_name
                    ))).scalar()
        if not interview_exists:
            text = response.xpath('//div[@class="mmplayer"]//p').getall()
            whole_interview = []
            current_text = ""
            current_speaker = ""
            for index, paragraph in enumerate(text):
                # chunk_name = paragraph.xpath('name()')

                chunk = clean_chunk(paragraph)
                if len(chunk) > 1:
                    current_speaker = chunk[0]
                    current_text = chunk[-1]
                elif len(chunk) == 1:
                    current_text += " "
                    current_text += chunk[0]

                if (index + 1) < len(text):
                    next_chunk = clean_chunk(text[index + 1])
                    if len(next_chunk) != 1 and len(current_text) > 0:
                        if len(current_speaker) > 0:
                            whole_interview.append([index, current_speaker,
                                                                current_text])
                        else:
                            whole_interview[-1][2] = whole_interview[-1][2] + " " + current_text
                        current_text = ""
                        current_speaker = ""
                    else:
                        pass
                else:
                    if len(current_text) > 0: whole_interview.append([index, current_speaker,
                                                        current_text])
                    # current_text = ""
                    # current_speaker = ""
            # print(whole_interview)
            # for i in whole_interview:
            #     # print(i)
            #     pass

            entry = {"date": broadcast_date,
                    "guest_name" : guest_name,
                    "guest_title" : guest_title,
                    "host_name" : host_name,
                    "interview" : whole_interview,
                    }

            if len(entry['interview']) > 10:

                print("=======================================")
                print(entry['date'])
                print(entry['guest_name'])
                print(len(entry['interview']))


                for i in entry['interview']:
                    interview_item = ItemLoader(item = InterviewParagraph(), response = response)

                    interview_item.add_value('date', meta['date'])

                    interview_item.add_value('guest_name', meta['guest_name'])
                    # ['guest_name'] = entry['guest_name']
                    interview_item.add_value('guest_title', meta['guest_title'])
                    # ['guest_title'] = entry['guest_title']
                    interview_item.add_value('host_name', meta['host_name'])
                    # ['host_name'] = entry['host_name']
                    interview_item.add_value('index', int(i[0]))
                    # ['index'] =
                    interview_item.add_value('speaker', str(i[1]))
                    ['speaker'] =
                    interview_item.add_value('paragraph', str(i[2]))
                    # ['paragraph'] = str(i[2])
                    # .encode('ascii','ignore')
                    interview_item.add_value('url', respone.url())
                    # ['url'] = respone.url()

                    item = interview_item.load_item()
                    yield item




        # text = [i.replace('\r\n', '').strip() for i in text]
        # # text = [i for i in text if i != "\r\n"]
        # text = [re.sub(r'^НОВОСТИ|новости$', '', i) for i in text]
        # text = [i.strip() for i in text]
        # text = [i for i in text if len(i) > 1]
        # pass



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

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from echomsk.models import *
from echomsk.functions import *

from sqlalchemy import and_

class EchomskPipeline(object):
    def process_item(self, item, spider):

        try:
            date = item["date"][0]
        except:
            date = None

        try:
            guest_name = item["guest_name"][0]
        except:
            guest_name = None

        try:
            guest_title = item["guest_title"][0]
        except:
            guest_title = None

        try:
            host_name = item["host_name"][0]
        except:
            host_name = None

        try:
            index = item["index"][0]
        except:
            index = None

        try:
            speaker = item["speaker"][0]
        except:
            speaker = None

        try:
            text = item["text"][0]
        except:
            text = None

        try:
            url = item["url"][0]
        except:
            url = None

        data_entry = {"date" = date,
                        "guest_name" : guest_name,
                        "guest_title" : guest_title,
                        "host_name" : host_name"][0],
                        "index" : item["index"][0],
                        "speaker" : item["speaker"][0],
                        "text" : item["text"][0],
                        "url" : item["url"][0]
                        }

        # data_exists = session_test.query(exists().where(
        #             VideoUrlEntry.url == data_entry['url']
        #             )).scalar()
        #
        # if data_exists:
        #     log_url_error(url = item["url"], session = session_test)



        adding_data = InterviewParagraph(**data_entry)
        session_test.add(adding_data)
        session_test.commit()
        # return item

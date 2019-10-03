# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field


class InterviewItem(Item):
    # Meta data
    date = Field()
    guest_name = Field()
    guest_title = Field()

    host_name = Field()

    index = Field()
    speaker = Field()
    paragraph = Field()
    url = Field()
    pass

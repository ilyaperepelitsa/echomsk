# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field


class InterviewParagraph(Item):
    # Meta data
    date = Field()
    guest_name = Field()


    job_position = Field()
    job_salary_med = Field()
    job_company = Field()
    job_text = Field()
    job_lists = Field()
    job_apply_link = Field()
    job_apply_text = Field()

    company_website = Field()
    company_size = Field()
    company_type = Field()
    company_revenue = Field()
    company_headquarters = Field()
    company_founded = Field()
    company_industry = Field()
    company_description = Field()

    rating_rating = Field()
    rating_recommend = Field()
    rating_approve = Field()


    pass

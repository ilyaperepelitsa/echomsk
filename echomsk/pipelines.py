# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EchomskPipeline(object):
    def process_item(self, item, spider):
        return item


class APIDataPipeline(object):
    def process_item(self, item, spider):

        data_entry = {"bmid" : item["bmid"],
                        "nid" : item["nid"],
                        "total_games" : item["total_games"],
                        "url" : item["url"],
                        "match_name" : item["match_name"],
                        "title" : item["title"],
                        "subtitle" : item["subtitle"],
                        "title_pos" : item["title_pos"],
                        "video_list_size" : item["video_list_size"],
                        "basic_index" : item["basic_index"],
                        "terminal_title" : item["terminal_title"],
                        "terminal_title_pos" : item["terminal_title_pos"]
                        }

        data_exists = session_test.query(exists().where(
                    VideoUrlEntry.url == data_entry['url']
                    )).scalar()

        if data_exists:
            log_url_error(url = item["url"], session = session_test)



        adding_data = VideoUrlEntry(**data_entry)
        session_test.add(adding_data)
        session_test.commit()
        return item

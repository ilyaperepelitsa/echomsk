# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EchomskPipeline(object):
    def process_item(self, item, spider):

        data_entry = {"date" : item["date"],
                        "guest_name" : item["guest_name"],
                        "guest_title" : item["guest_title"],
                        "host_name" : item["host_name"],
                        "index" : item["index"],
                        "speaker" : item["speaker"],
                        "text" : item["text"],
                        "url" : item["url"]
                        }

        # data_exists = session_test.query(exists().where(
        #             VideoUrlEntry.url == data_entry['url']
        #             )).scalar()
        #
        # if data_exists:
        #     log_url_error(url = item["url"], session = session_test)



        adding_data = VideoUrlEntry(**data_entry)
        session_test.add(adding_data)
        session_test.commit()
        return item


date = Field()
guest_name = Field()
guest_title = Field()

host_name = Field()

index = Field()
speaker = Field()
text = Field()
url = Field()
pass

import json
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey

from sqlalchemy.types import TEXT, VARCHAR, INTEGER, FLOAT, TIMESTAMP, ARRAY, Date


from sqlalchemy.sql import select
from sqlalchemy.sql import exists

engine_test = create_engine('sqlite:///echo.db')
Base_item = declarative_base()

# class MainEntry(Base_item):
#     __tablename__ = "main_entries"
#     id = Column(INTEGER, primary_key = True)
#     bmid = Column(INTEGER, nullable=True)
#     nid = Column(INTEGER, nullable=True)
#     url = Column(TEXT, unique = False)
#
#     def __repr__(self):
#         return "<Base_item(id='%s', bmid='%s',\
#                         nid='%s', url='%s')>"\
#         %(self.id, self.bmid,
#             self.nid, self.url)

class InterviewParagraph(Base_item):
    __tablename__ = "video_url_entries"
    id = Column(INTEGER, primary_key = True)
    date = Column(Date, nullable=False)
    guest_name = Column(VARCHAR(50), nullable=True)
    guest_title = Column(INTEGER, nullable=True)
    url = Column(TEXT, unique = False)
    match_name = Column(TEXT, unique = False, nullable=True)
    title = Column(TEXT, unique = False, nullable=True)
    subtitle = Column(TEXT, unique = False, nullable=True)
    title_pos = Column(INTEGER, nullable=True)
    video_list_size = Column(INTEGER, nullable=True)
    basic_index = Column(INTEGER, nullable=True)
    terminal_title = Column(TEXT, unique = False, nullable=True)
    terminal_title_pos = Column(INTEGER, nullable=True)

    def __repr__(self):
        return "<Base_item(id='%s', bmid='%s', nid='%s',\
                        total_games='%s', url='%s', match_name='%s',\
                        title='%s', subtitle='%s',\
                        title_pos='%s',\
                        video_list_size='%s', basic_index='%s',\
                        terminal_title='%s', terminal_title_pos='%s')>"\
        %(self.id, self.bmid, self.nid,
            self.total_games,
            self.url, self.match_name,
            self.title, self.subtitle,
            self.title_pos,
            self.video_list_size,
            self.basic_index,
            self.terminal_title,
            self.terminal_title_pos)


# class FailedBMIDs(Base_item):
#     __tablename__ = "failed_bmids"
#     id = Column(INTEGER, primary_key = True)
#     bmid = Column(INTEGER, nullable=True)
#
#     def __repr__(self):
#         return "<Base_item(id='%s', bmid='%s')>"\
#         %(self.id, self.bmid)

class Errors(Base_item):
    __tablename__ = "errors"
    id = Column(INTEGER, primary_key = True)
    bmid = Column(VARCHAR(10), nullable=True)
    nid = Column(VARCHAR(15), nullable=True)
    error_type = Column(VARCHAR(20))

    def __repr__(self):
        return "<Base_item(id='%s', bmid='%s',\
                    nid='%s', error_type='%s')>"\
        %(self.id, self.bmid, self.nid, self.error_type)


class DupUrlErrors(Base_item):
    __tablename__ = "dup_url_errors"
    id = Column(INTEGER, primary_key = True)
    url = Column(TEXT, unique = False)

    def __repr__(self):
        return "<Base_item(id='%s', url='%s')>"\
        %(self.id, self.url)


Base_item.metadata.create_all(engine_test)
Session_test = sessionmaker(bind = engine_test)
session_test = Session_test()

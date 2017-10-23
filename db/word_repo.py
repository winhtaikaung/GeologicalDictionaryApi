from sqlalchemy_paginator import Paginator
from tornado.ioloop import IOLoop

from db import generate_meta, serialize_alchemy
from model import DBSession
from model.word_entity import Word


class WordRepository(object):
    def __init__(self, io_loop=None):

        # self.db = database.Connection()
        self.io_loop = io_loop or IOLoop.instance()
        self.db_session = DBSession
        self.serialize_alchemy = serialize_alchemy
        pass

    def get_word_by_id(self, user_id, callback=None):
        """
        Get Word By id 
        :param user_id: UUID-4 bd65600d-8669-4903-8a14-af88203add38
        :param callback: 
        :return: 
        """
        session = self.db_session
        result = None

        try:
            result = session.query(Word).filter(Word.id == user_id).one()
            callback(result)
        except Exception as e:
            result = e
        callback(result)

    def get_words(self, limit, page_number, callback=None):
        session = self.db_session
        result = None
        word = Word()
        meta_obj = {}
        try:
            query = session.query(Word)
            paginator = Paginator(query, int(limit))
            page = paginator.page(int(page_number))

            result = self.serialize_alchemy(page.object_list)

            meta_obj = {"page": page_number,
                        "limit": limit,
                        "next_page": page.has_next() and page.next_page_number or None,
                        "previous_page": page.has_previous() and page.previous_page_number or None,
                        "page_count": paginator.total_pages,
                        "total_count": paginator.count,
                        "Links": generate_meta(type(word).__name__.lower(), limit, page_number, paginator.total_pages)}
        except Exception as e:
            result = []
        callback(result, meta_obj)

    def get_words_by_word_index(self, limit, page_number, model={}, callback=None):
        session = self.db_session
        result = None
        word = Word()
        meta_obj = {}
        try:
            query = session.query(model)
            paginator = Paginator(query, int(limit))
            page = paginator.page(int(page_number))

            result = self.serialize_alchemy(page.object_list)
            total_pages = 0
            if paginator.total_pages != 1 :
                total_pages = paginator.total_pages
            meta_obj = {"page": page_number,
                        "limit": limit,
                        "next_page": page.has_next() and page.next_page_number or None,
                        "previous_page": page.has_previous() and page.previous_page_number or None,
                        "page_count":total_pages,
                        "total_count": paginator.count,
                        "Links": generate_meta(type(word).__name__.lower(), limit, page_number, paginator.total_pages)}
        except Exception as e:
            result = []
        callback(result, meta_obj)

    def create_word(self, word_model, callback=None):
        """
        Create a user in DB by passing user_orm
        :param word_model: 
        :param callback: 
        :return: 
        """
        session = self.db_session
        result = True
        try:
            session.add(word_model)
            session.commit()
        except Exception as e:
            session.rollback()
            result = e
        session.close()
        callback(result)

    def bulk_insert(self, word_list=[], model={}):
        session = self.db_session
        user_list = word_list
        try:
            session.bulk_insert_mappings(model, user_list)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
        session.close()



        # def get_users(self, limit, page, callback=None):
        #     """
        #
        #     :param limit:
        #     :param page:
        #     :param callback:
        #     :return:
        #     """
        #     try:
        #         limit = int(limit)
        #         page = int(page)
        #         offset = 0 if page == 0 else (page - 1) * limit
        #
        #         query = "SELECT * FROM '" + str("users") + "' LIMIT '" + str(limit) + "' OFFSET '" + str(
        #             offset) + "'"
        #
        #         response = self.db.query(query)
        #         print response
        #
        #         rowarray_list = []
        #         for row in response:
        #             d = dict((k.lower(), v.lower()) for k, v in row.iteritems())
        #             rowarray_list.append(collections.OrderedDict(reversed(list(d.items()))))
        #
        #         rows = self.db.query("SELECT COUNT(*) as COUNT FROM 'users'")
        #
        #         rowCount = int(rows[0]['COUNT'])
        #         page_count = rowCount / limit if rowCount % limit == 0 else (rowCount / limit) + 1
        #
        #         # prepare links for metadata
        #
        #
        #         from db import generate_meta
        #         metaObj = {"page": page,
        #                    "limit": limit,
        #                    "page_count": page_count,
        #                    "total_count": rowCount,
        #                    "Links": generate_meta('user', limit, page, page_count)}
        #
        #         callback(None, rowarray_list, metaObj)
        #         return
        #     except Exception as e:
        #         callback(e)
        #         return

import string

import tornado.web
from tornado import gen

from db import word_repo
from handlers.base_handler import BaseHandler
from utils import dict_utils


class APIConfigHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    # @token_validator # <------ this middleware method will validate token on the method that was applied
    @gen.engine
    def get(self, params):
        limit = self.get_argument("limit", int(100), True)  # <--- get query_argement
        page = self.get_argument("page", int(1), True)
        word_repository = word_repo.WordRepository()
        dict_util = dict_utils.DictUtils()
        result = []

        for char in string.ascii_lowercase:
            response = yield gen.Task(word_repository.get_words_by_word_index, int(limit), int(page),
                                      dict_util.get_model(str(char).lower()))
            result.append(dict(wordIndex=char, page_count=response.args[1].get('page_count')))

        result.append(dict(wordIndex="last", page_count=1))
        self.respond({"config": result}, {}, 200)

    @tornado.web.asynchronous
    @gen.engine
    def post(self, action):
        self.respond({}, 200)

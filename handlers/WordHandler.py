import uuid

import tornado.web
from tornado import gen
from db import WordRepository
from handlers.BaseHandler import BaseHandler, NO_CONTENT_ERROR
from model.User import User

from utils import DictUtils


class WordHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    # @token_validator # <------ this middleware method will validate token on the method that was applied
    @gen.engine
    def get(self, params):

        if self.get_query_arguments("id", True):
            id = self.get_argument("id", strip=True)
            word_repository = WordRepository.WordRepository()
            response = yield gen.Task(word_repository.get_word_by_id, str(id))
            if hasattr(response, '_get_val'):
                self.respond(response._get_val(), 200)
            self.respond({}, NO_CONTENT_ERROR, code=NO_CONTENT_ERROR)
        elif self.get_query_arguments("word", True):
            word = self.get_argument("word", strip=True)
            limit = self.get_argument("limit", int(10), True)  # <--- get query_argement
            page = self.get_argument("page", int(1), True)
            word_repository = WordRepository.WordRepository()
            dict_utils = DictUtils.DictUtils()
            response = yield gen.Task(word_repository.get_words_by_word_index, int(limit), int(page),
                                      dict_utils.get_model(word))
            self.respond(response.args[0], response.args[1], 200)

    @tornado.web.asynchronous
    @gen.engine
    def post(self, action):
        self.respond({}, 200)

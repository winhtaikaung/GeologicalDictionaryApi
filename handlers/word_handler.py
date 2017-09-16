import tornado.web
from tornado import gen

from db import word_repo
from handlers.base_handler import BaseHandler, NO_CONTENT_ERROR
from utils import dict_utils


class WordHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    # @token_validator # <------ this middleware method will validate token on the method that was applied
    @gen.engine
    def get(self, params):

        if self.get_query_arguments("id", True):
            id = self.get_argument("id", strip=True)
            word_repository = word_repo.WordRepository()
            response = yield gen.Task(word_repository.get_word_by_id, str(id))
            if hasattr(response, '_get_val'):
                self.respond(response._get_val(), 200)
            self.respond({}, NO_CONTENT_ERROR, code=NO_CONTENT_ERROR)
        elif self.get_query_arguments("word", True):
            word = self.get_argument("word", strip=True)
            limit = self.get_argument("limit", int(10), True)  # <--- get query_argement
            page = self.get_argument("page", int(1), True)
            word_repository = word_repo.WordRepository()
            dict_util = dict_utils.DictUtils()
            response = yield gen.Task(word_repository.get_words_by_word_index, int(limit), int(page),
                                      dict_util.get_model(str(word).lower()))
            self.respond(response.args[0], response.args[1], 200)

    @tornado.web.asynchronous
    @gen.engine
    def post(self, action):
        self.respond({}, 200)

import uuid

import tornado.web
from tornado import gen
from db import WordRepository
from handlers.BaseHandler import BaseHandler, NO_CONTENT_ERROR
from model.User import User


class DataFetchHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    # @token_validator # <------ this middleware method will validate token on the method that was applied
    @gen.engine
    def get(self, params):

        if self.get_query_arguments("id", True):
            id = self.get_argument("id", strip=True)
            user_repository = WordRepository.WordRepository()
            response = yield gen.Task(user_repository.get_user_by_id, str(id))
            if hasattr(response, '_get_val'):
                self.respond(response._get_val(), 200)
            self.respond({}, NO_CONTENT_ERROR, code=NO_CONTENT_ERROR)
        else:
            limit = self.get_argument("limit", int(10), True)  # <--- get query_argement
            page = self.get_argument("page", int(1), True)
            user_repository = WordRepository.WordRepository()
            response = yield gen.Task(user_repository.get_words, int(limit), int(page))
            self.respond(response.args[0], response.args[1], 200)

    @tornado.web.asynchronous
    @gen.engine
    def post(self, action):
        user_repository = WordRepository.WordRepository()
        user = User(id=str(uuid.uuid4().hex), name=self.get_body_argument("name"),
                    email=self.get_body_argument("email"),
                    profile=self.get_body_argument("profile"),
                    nric_no=self.get_body_argument("nricno"),
                    pass_code=self.get_body_argument("passcode"),
                    address=self.get_body_argument("address"),
                    zipcode=self.get_body_argument("zipcode"),
                    )

        response = yield gen.Task(user_repository.create_user, user)
        self.respond(response, 200)

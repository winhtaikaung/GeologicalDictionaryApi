import uuid
import gspread
import tornado.web

from tornado import gen
from oauth2client.service_account import ServiceAccountCredentials
from db import WordRepository
from handlers.BaseHandler import BaseHandler, NO_CONTENT_ERROR, SUCCESS
from model.User import User


class DataFetchHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    # @token_validator # <------ this middleware method will validate token on the method that was applied
    @gen.engine
    def get(self, params):
        if self.get_argument("fetch", True):
            scope = ['https://spreadsheets.google.com/feeds']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
            word_repository = WordRepository.WordRepository()
            try:
                gc = gspread.authorize(credentials)
                sh = gc.open_by_key("1QeU3AoSghCAvYBD8kauC8oEZ0wA6j_gPj1pkvIY4MPU")

                for ws_count, worksheets in enumerate(sh.worksheets()):
                    word_list = worksheets.col_values(1)
                    type_list = worksheets.col_values(2)
                    meaning_list = worksheets.col_values(3)

                    if ws_count < 26:
                        word_tuple_list = []
                        for i, (word, word_type, meaning) in enumerate(zip(word_list, type_list, meaning_list)):
                            if i > 0:
                                if word != '':
                                    word_tuple_list.append(dict(id=str(uuid.uuid1().hex), word=str(word),
                                                                type=str(word_type),
                                                                meaning_zg=meaning,
                                                                meaning_uni=meaning))
                            else:
                                pass

                        word_repository.bulk_insert(word_tuple_list)

                    else:
                        self.respond({}, NO_CONTENT_ERROR, code=SUCCESS)

            except Exception as ex:
                print ex.message
            self.respond({}, NO_CONTENT_ERROR, code=SUCCESS)

        else:
            self.respond({}, NO_CONTENT_ERROR, code=NO_CONTENT_ERROR)


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

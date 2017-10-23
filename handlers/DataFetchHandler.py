import uuid
import gspread
import tornado.web

from tornado import gen
from oauth2client.service_account import ServiceAccountCredentials

from db.word_repo import WordRepository
from handlers.base_handler import BaseHandler, SUCCESS, SERVER_ERROR, NO_CONTENT_ERROR
from utils.dict_utils import DictUtils


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
            dict_utils = DictUtils.DictUtils()

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

                                    word_tuple_list.append(dict(id=str(uuid.uuid1().hex), word=word,
                                                                type=word_type,
                                                                meaning_zg=meaning,
                                                                meaning_uni=meaning))
                            else:
                                pass
                        word_repository.bulk_insert(word_tuple_list, dict_utils.get_model(str(worksheets.title).lower()))

                    else:
                        self.respond({}, NO_CONTENT_ERROR, code=SUCCESS)

            except Exception as ex:
                print ex.message
                self.respond({}, ex.message, code=SERVER_ERROR)
            self.respond({}, SUCCESS, code=SUCCESS)

        else:
            self.respond({}, NO_CONTENT_ERROR, code=NO_CONTENT_ERROR)


@tornado.web.asynchronous
@gen.engine
def post(self, action):
    self.respond({}, 200)

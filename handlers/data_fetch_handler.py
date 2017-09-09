import uuid
import gspread
import tornado.web

from tornado import gen
from oauth2client.service_account import ServiceAccountCredentials
from db import word_repo
from handlers.base_handler import BaseHandler, NO_CONTENT_ERROR, SUCCESS, SERVER_ERROR
from utils import dict_utils


class DataFetchHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    # @token_validator # <------ this middleware method will validate token on the method that was applied
    @gen.engine
    def get(self, params):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        gc = gspread.authorize(credentials)
        sh = gc.open_by_key("1QeU3AoSghCAvYBD8kauC8oEZ0wA6j_gPj1pkvIY4MPU")
        word_repository = word_repo.WordRepository()
        dict_util = dict_utils.DictUtils()
        if self.get_argument("fetch", False):
            fetch_char = self.get_argument("fetch")
            try:

                work_sheet = sh.get_worksheet(dict_util.get_spreadsheet_index_by_word(fetch_char))
                word_list = work_sheet.col_values(1)
                type_list = work_sheet.col_values(2)
                meaning_list = work_sheet.col_values(3)

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
                word_repository.bulk_insert(word_tuple_list,
                                            dict_util.get_model(fetch_char))

            except Exception as ex:
                print ex.message
                self.respond({}, ex.message, code=SERVER_ERROR)
            self.respond({}, SUCCESS, code=SUCCESS)
        else:
            try:

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
                        word_repository.bulk_insert(word_tuple_list,
                                                    dict_util.get_model(str(worksheets.title).lower()))
                    else:
                        self.respond({}, NO_CONTENT_ERROR, code=SUCCESS)

            except Exception as ex:
                print ex.message
                self.respond({}, ex.message, code=SERVER_ERROR)
            self.respond({}, SUCCESS, code=SUCCESS)


@tornado.web.asynchronous
@gen.engine
def post(self, action):
    self.respond({}, 200)

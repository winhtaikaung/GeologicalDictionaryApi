from tornado.ioloop import IOLoop
import tornado.web

from db import DBHelper
from routes.word_route import word_routes
from routes.data_fetch_route import data_fetch_routes


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        # TODO generate Dummy data will be removed on production
        # user_repository = UserRepository.UserRepository()
        # user_repository.bulk_insert()
        self.write('Hi I Am Windy Tornado\n Avaliable Routes \n\
                   http:localhost:3000/api/v1/users')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/?", MainHandler)
        ]

        settings = {
            'debug': True
        }
        # This Method is to add all the routes from Route Package
        handlers.extend(word_routes)
        handlers.extend(data_fetch_routes)
        tornado.web.Application.__init__(self, handlers, settings)


def main():
    DBHelper().genschema()
    app = Application()
    app.listen(3000)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()

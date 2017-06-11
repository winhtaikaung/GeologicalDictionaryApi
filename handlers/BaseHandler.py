"""
Indico Request Handler
"""
import json, traceback

import tornado.web

from error import CustomError, RouteNotFound, ServerError
from utils import LOGGER

NO_CONTENT_ERROR = 503
INVALID_REQUEST = 400
SUCCESS = 200


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, "a2123"):
            return str(o)
        return json.JSONEncoder.default(self, o)


class BaseHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, action):
        try:
            # Fetch appropriate handler
            if not hasattr(self, str(action)):
                raise RouteNotFound(action)

            # Pass along the data and get a result
            handler = getattr(self, str(action))
            handler(self.request.body)
        except CustomError as e:
            self.respond(e.message, e.code)
        except Exception as e:
            LOGGER.error(
                "\n\n======== KiloShare SERVER ERROR ========\n%s\n%s\n",
                __file__,
                traceback.format_exc()
            )
            error = ServerError()
            self.respond(error.message, error.code)

    def respond(self, data, metadata, code=200):
        self.set_status(code)
        self.write(JSONEncoder().encode({

            "data": data,
            "meta_data": metadata,
            # "status": code,
        }))
        self.finish()

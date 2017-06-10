from handlers.WordHandler import WordHandler

word_routes = [
    # (r'/api/v1/user/(?P<param1>[^\/]+)/?(?P<param2>[^\/]+)?/?(?P<param3>[^\/]+)?', UserHandler),
    (r'/api/v1/word/?(.*)', WordHandler)
]

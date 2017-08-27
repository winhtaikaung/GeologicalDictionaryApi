from handlers.data_fetch_handler import DataFetchHandler
data_fetch_routes = [
    # (r'/api/v1/user/(?P<param1>[^\/]+)/?(?P<param2>[^\/]+)?/?(?P<param3>[^\/]+)?', UserHandler),
    (r'/api/v1/fetch/?(.*)',DataFetchHandler)
]

from handlers.api_config_handler import APIConfigHandler

api_config_route = [
    # (r'/api/v1/user/(?P<param1>[^\/]+)/?(?P<param2>[^\/]+)?/?(?P<param3>[^\/]+)?', UserHandler),
    (r'/api/config/?(.*)', APIConfigHandler)
]

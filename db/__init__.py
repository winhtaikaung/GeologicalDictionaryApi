from tornado.options import define, options

define("db_connection_str", default="sqlite:///db_geodictionary.sqlite",
       help="Database connection string for application")  # db connection string
from sqlalchemy import create_engine

from model import Base as model_base, DBSession

db_engine = create_engine(options.db_connection_str)


def generate_meta(table_view_name, limit, page, page_count):
    """
    This method help to generate links and metadata object
    :param table_view_name: 
    :param limit: 
    :param page: 
    :param page_count: 
    :return: 
    """
    url = "/api/v1/%s?page=%d&limit=%d"
    links = {"self": url % (table_view_name, page, limit),
             "first": url % (table_view_name, 1, limit)}
    if page > 1:
        links.update({"previous": url % (table_view_name, page - 1, limit)})
    if page < page_count:
        links.update({"next": url % (table_view_name, page + 1, limit)})
    links.update({"last": url % (table_view_name, page_count, limit)})
    return links


def serialize_alchemy(alchemy_object_list):
    user_dictionary = [];
    fields = {}
    for row in alchemy_object_list:
        for field in [x for x in dir(row) if not x.startswith('_') and x != 'metadata' and x != 'query']:
            fields[field] = row.__getattribute__(field)
        user_dictionary.append(fields)
    return user_dictionary


class DBHelper:
    def __init__(self):
        DBSession.configure(bind=db_engine)
        pass

    def genschema(self):
        model_base.metadata.create_all(db_engine)

from datetime import datetime, date

# import isodate as iso
from bson import ObjectId
from flask.json import JSONEncoder
from importlib import import_module
from werkzeug.routing import BaseConverter


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        # if isinstance(o, (datetime, date)):
        #     return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)


def include_routers(module, api):
    """
    Include all the urls in module
    """
    mod = import_module(module)
    routes = getattr(mod, 'initialize_routes')
    routes(api)

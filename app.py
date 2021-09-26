import os

from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api

from config.db_connect import DBConnector, MysqlDBConnector, PostgresDBConnector

from config.settings import DevConfig
from utils.middlewares import OperationLogMiddleware
from utils.utils import MongoJSONEncoder, ObjectIdConverter

from flask_caching import Cache
from config.celery.celery import make_celery

# Flask app creation
app = Flask(__name__)
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

app.config.from_object(DevConfig())

# CORS 
cors = CORS(app, resources={r"/api/*": {"origins": '*'}})

# middleware
app.wsgi_app = OperationLogMiddleware(app.wsgi_app)

# Falsk -RestApi
api = Api(app, prefix='/api/v1')

print(app.config)
# Flask Redis Caching
cache = Cache(app, config=app.config['CACHE'])

# datbase connect
mongo = DBConnector.connect_with_pool(app)

# mysql = MysqlDBConnector.connect_with_pool(app)

postgres = PostgresDBConnector.connect_with_pool(app)

celery = make_celery(app)

#init urls
from apps.routers import initialize_routes
initialize_routes(api)
app.url_map.strict_slashes = False

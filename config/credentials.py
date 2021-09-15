"""
"""
SECRET_KEY = '6\xd4\x8e\x1d\xca\x02[\xe8\xf3\xabC\xe1\xe1\xe8&\xb9p\x00\x04U\x16\x7f!\x87'

# Allowed host for CORS 
ALLOWED_HOSTS = []

AWS_ACCESS_KEY_ID = 'AKIARQHRTM2NYYIHZKFY'
AWS_SECRET_KEY = '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'
AWS_PRODUCT_BUCKET = 'cityapl-product-images'
FAST2SMS_API = ''
AWS_REGION = 'ap-south-1'

DATABASES = {
    'mysql_rds': {
        'NAME': 'cityapl',
        'USER': 'admin',
        'PASSWORD': 'cityapl_rds123',
        'HOST': 'cityapl-database-1.cyvpsljpkc8d.ap-south-1.rds.amazonaws.com',
        'PORT': '3306',
        },
    'postgres': {
        'NAME': 'cityapl',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        },
    'mongo': {
        'MONGODB_DB': '',
        'MONGODB_HOST': '',
        'MONGODB_PORT': '',
        'MONGODB_USERNAME': '',
        'MONGODB_PASSWORD': ''
    },
    'production': {
        'SERVICE_NAME':'********',
        'USER': '********',
        'PASSWORD': '********',
        'HOST': '********',
        'PORT': '********',
    },
    'testing':{
        'SERVICE_NAME':'********',
        'USER': '********',
        'PASSWORD': '********',
        'HOST': '********',
        'PORT': '********',

    }

}

REDIS_CACHE = {
        'CACHE_TYPE':'RedisCache',
        'CACHE_REDIS_HOST':'localhost',
        'CACHE_REDIS_PORT': 6379,
        'CACHE_REDIS_DB':0,
        'CACHE_REDIS_URL':'redis://localhost:6379/0',
        'CACHE_DEFAULT_TIMEOUT':500
    }

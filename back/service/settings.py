from os import getenv


class RestplusConfig(object):
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False
    API_VERSION = 'v1'


class Config(RestplusConfig):
    FLASK_SERVER_NAME = 'test.su'  # NOT SERVER_NAME !!!
    PORT = int(getenv('APP_PORT', 5000))
    DEBUG = True  # Do not use debug mode in production
    FLASK_DEBUG_DISABLE_STRICT = True

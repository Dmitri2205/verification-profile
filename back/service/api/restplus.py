import logging
from os import getenv
from flask import Blueprint, current_app
from flask_restx import Api, abort
from service.api.namespaces.verication_profile_ns import api as verication_profile


log = logging.getLogger(__name__)

if getenv('API_VERSION') is not None:
    api_version = getenv('API_VERSION')
else:
    api_version = 1

print('!!!!!!!!!!!!!!!!!!!!!!!', api_version)
bp = Blueprint("api", __name__, url_prefix=f"/api/v{api_version}")
api = Api(bp, version=str(1), title='API', description='Skylove Admin Moderator API service')

api.add_namespace(verication_profile)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not current_app.debug:
        abort(500, message)

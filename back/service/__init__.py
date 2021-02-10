from flask import Flask
from service.settings import Config
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={r'/*': {'origins': '*'}})

    with app.app_context():
        from service.api.restplus import bp as api_bp
        app.register_blueprint(api_bp)

    return app

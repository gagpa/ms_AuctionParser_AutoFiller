from ms_app.configs.main_config import config

from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    """Созадние объекта приложения"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    from .api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return app


app = create_app(environ.get('APP_MODE') or 'development')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)

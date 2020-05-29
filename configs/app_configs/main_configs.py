import os

TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class Config:
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = TRACK_MODIFICATIONS


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = TRACK_MODIFICATIONS


main_configs = {'default': DevelopmentConfig,
                'development': DevelopmentConfig,
                'production': ProductionConfig}

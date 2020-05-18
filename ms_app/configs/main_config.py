import os

basedir = os.path.abspath('')


class Config:
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    PORT = '8080'
    IP = '0.0.0.0'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


config = {'default': DevelopmentConfig,
          'development': DevelopmentConfig,
          'production': ProductionConfig}

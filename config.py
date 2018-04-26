import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET_KEY_NOT_SET'


class DevelopmentConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True


class ProductionConfig(Config):
    # import logging
    # log = logging.getLogger('werkzeug')
    # log.setLevel(logging.ERROR)
    pass


class TestingConfig(Config):
    TESTING = True


configs = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'test': TestingConfig,
    'default': DevelopmentConfig
}

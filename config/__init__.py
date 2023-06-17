import os
import inspect


def _get_class_dict(klass):
    class_dict = {}
    for key, value in inspect.getmembers(klass):
        if not key.startswith('_'):
            # Ignores methods
            if not inspect.ismethod(value):
                class_dict[key] = value
    return class_dict

SERVER_DOMAIN = "wsl2-localhost"

class Config:
    SERVER_TYPE = 'none'
    DATABASE_URI = os.environ.get('DATABASE_URL') or \
        ("postgresql+asyncpg://db_user:aBcd123456@" + SERVER_DOMAIN +\
        ":5432/suerp")
    REDIS_URL = os.getenv('REDIS_URL') or (SERVER_DOMAIN + ':6379')
    SUPER_SECRET_TOKEN = "50d92252-1175-42e7-9b5b-3ff805e1743f"

    SECRET_KEY = \
        "44c16e6a662d60120012edcf0c8bb4244101b51c3484ee041fe664d91dadcc48"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @classmethod
    def init_app(cls, app):
        print('==== choose server type ====')
        # Config 데이터를 app.config 에 저장한다.
        app.config = {}
        # Config 데이터를 app.config 에 저장한다.
        app.config = _get_class_dict(cls)



class DevelopmentConfig(Config):
    SERVER_TYPE = 'development'

    @classmethod
    def init_app(cls, app):
        print('==== THIS APP IS IN DevelopmentConfig MODE ====')
        app.config = _get_class_dict(cls)

    @classmethod
    def get_super_secret_token(cls):
        return cls.SUPER_SECRET_TOKEN


class UnittestConfig(Config):
    SERVER_TYPE = 'unittest'

    @classmethod
    def init_app(cls, app):
        print('==== THIS APP IS IN TestConfig MODE ====')
        app.config = _get_class_dict(cls)

    @classmethod
    def get_super_secret_token(cls):
        return cls.SUPER_SECRET_TOKEN

class ProductionConfig(Config):
    SERVER_TYPE = 'production'
    SUPER_SECRET_TOKEN = ""
    SECRET_KEY = \
        "80f8bc3b8b7cfc6f751c9729ab430dde6d804463711d7a153df50ecc9ce86f23"

    @classmethod
    def init_app(cls, app):
        print('==== THIS APP IS IN production MODE ====')
        app.config = _get_class_dict(cls)

    @classmethod
    def get_super_secret_token(cls):
        return cls.SUPER_SECRET_TOKEN

config = {
    'unittest': UnittestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

def get_config():
    FASTAPI_CONFIG = os.getenv('FASTAPI_CONFIG') or 'development'
    return config[FASTAPI_CONFIG]

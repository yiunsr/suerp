import os
import inspect

class Config:
    SERVER_TYPE = 'none'
    DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        "postgresql+asyncpg://db_user:aBcd123456@127.0.0.1:5433/suerp"
    REDIS_URL = os.getenv('REDISTOGO_URL') or 'http://localhost:6379'
    SUPER_SECRET_TOKEN = "50d92252-1175-42e7-9b5b-3ff805e1743f"

    @classmethod
    def init_app(cls, app):
        print('==== choose server type ====')
        app.config = {}
        # Config 데이터를 app.config 에 저장한다.
        for key, value in inspect.getmembers(cls):
            if not key.startswith('_'):
                # Ignores methods
                if not inspect.ismethod(value):
                    app.config[key] = value



class DevelopmentConfig(Config):
    SERVER_TYPE = 'development'

    @classmethod
    def init_app(cls, app):
        print('==== THIS APP IS IN DevelopmentConfig MODE ====')
        Config.init_app(app)
    
    @classmethod
    def get_super_secret_token(cls):
        return cls.SUPER_SECRET_TOKEN

config = {
    'development': DevelopmentConfig,
}

def get_config():
    FASTAPI_CONFIG = os.getenv('FASTAPI_CONFIG') or 'development'
    return config[FASTAPI_CONFIG]

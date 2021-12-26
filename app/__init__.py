import asyncio

from fastapi import FastAPI

from config import config
from config import urls
from config import db

def create_app(config_name):
    app = FastAPI()
    config[config_name].init_app(app)
    urls.init_app(app)
    asyncio.run(db.init_models())
    return app

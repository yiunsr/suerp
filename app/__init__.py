import asyncio

from fastapi import FastAPI

from config import config
from config import urls
from config import db
from config import middleware
from config import http_err

def create_app(config_name):
    app = FastAPI()
    config[config_name].init_app(app)
    urls.init_app(app)
    middleware.init_app(app)
    http_err.init_app(app)
    db.init_app(app)
  
    return app

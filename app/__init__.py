import asyncio

from fastapi import FastAPI
from contextlib import asynccontextmanager

from config import config
from config import urls
from config import db
from config import middleware
from config import http_err
from config import cache

@asynccontextmanager
async def lifespan(app):
    print("fastapi start")
    await cache.init_cache(app)
    yield
    print("fastapi end")

def create_app(config_name):
    app = FastAPI(lifespan=lifespan)
    config[config_name].init_app(app)
    urls.init_app(app)
    middleware.init_app(app)
    http_err.init_app(app)
    db.init_app(app)
    cache.init_app(app)
  
    return app

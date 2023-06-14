from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import Any, Dict, List, NoReturn, Optional, Tuple, Type, TypeVar
from fastapi import Request

from . import get_config

config = get_config()
server_type = config.SERVER_TYPE
DATABASE_URL = config.DATABASE_URI

if server_type != "unittest":
    engine = create_async_engine(DATABASE_URL, future=True, echo=True)
    SessionLocal = sessionmaker(
        engine, expire_on_commit=True, class_=AsyncSession)

# Dependency
if server_type != "unittest":
    async def get_db_session(request: Request)-> AsyncSession:
        async with SessionLocal() as db_session:
            yield db_session
else:
    async def get_db_session(request: Request)-> AsyncSession:
        db_session_= request.app.db_session
        # await db_session_.begin()
        yield request.app.db_session

async def get_db_session2()-> AsyncSession:
    async with SessionLocal() as db_session:
        yield db_session

def init_app(app):
    if server_type != "unittest":
        app.db = SessionLocal

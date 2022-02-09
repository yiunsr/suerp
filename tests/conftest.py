import os
import pytest
import pytest_asyncio
import asyncio
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.asyncio import create_async_engine
from starlette.testclient import TestClient

FASTAPI_CONFIG = 'unittest'
os.environ["FASTAPI_CONFIG"] = FASTAPI_CONFIG

from config import get_config
from config.db import get_db_session
from app import create_app

config = get_config()
server_type = config.SERVER_TYPE
DATABASE_URL = config.DATABASE_URI

@pytest.fixture(scope="class")
def event_loop(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    request.cls.loop = loop
    yield loop
    loop.close()

@pytest.fixture(scope="class")
def app(request):
    app_ = create_app("unittest")
    request.cls.app = app_
    request.cls.client = TestClient(app_)

@pytest_asyncio.fixture(scope="class")
async def engine(request) -> Session:
    engine_ = create_async_engine(DATABASE_URL, future=True, echo=True)
    request.cls.engine = engine_
    async with engine_.connect() as connection:
        request.cls.connection = connection
        yield engine_
    engine_.dispose()

@pytest_asyncio.fixture(scope="function")
async def db_session(request, engine):
    connection = request.cls.connection
    # trans = connection.sync_connection.begin()
    nested = await connection.begin_nested()
    async_session = AsyncSession(bind=connection)

    @event.listens_for(async_session.sync_session, "after_transaction_end")
    def end_savepoint(session_, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = connection.sync_connection.begin_nested()

    request.cls.db_session = async_session 
    request.cls.app.db_session = async_session 
    yield async_session
    async_session.close()
    trans.rollback()
    connection.close()
    print("db_session end 1")

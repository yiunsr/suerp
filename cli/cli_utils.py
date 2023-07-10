from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy import func
from sqlalchemy.future import select

from app.models.user import User
from app.models.app_meta import AppMeta
from app.models.table_meta import TableMeta

def get_db_session(config):
    DATABASE_URL = config.DATABASE_URI
    engine = create_async_engine(DATABASE_URL, future=True, echo=True)
    SessionLocal = sessionmaker(
        engine, expire_on_commit=True, class_=AsyncSession)
    return SessionLocal


async def add_user(db_session, data):
    query = select(User).where(User.email==data["email"])
    result = await db_session.execute(query)
    db_user = result.scalars().first()
    if db_user:
        return
    password = data.get("password")
    if password:
        del data["password"]
    db_user = User(**data)
    if password:
        db_user.hash_password = User.gen_password_hash(password)
    db_user.password_last_ets = func.now_ets()
    db_user.api_key = db_user.gen_api_key()
    db_user.api_key_last_ets = func.now_ets()
    db_session.add(db_user)

async def add_app_meta(db_session, data):
    query = select(AppMeta).where(AppMeta.name==data["name"])
    result = await db_session.execute(query)
    db_app_meta = result.scalars().first()
    if db_app_meta:
        return
    db_app_meta = AppMeta(**data)
    db_session.add(db_app_meta)

async def get_app_meta(db_session, name):
    query = select(AppMeta).where(AppMeta.name==name)
    result = await db_session.execute(query)
    return result.scalars().first()

async def add_table_meta(db_session, data):
    query = select(TableMeta).where(TableMeta.code==data["code"])
    result = await db_session.execute(query)
    db_table_meta = result.scalars().first()
    if db_table_meta:
        return
    db_table_meta = TableMeta(**data)
    db_session.add(db_table_meta)

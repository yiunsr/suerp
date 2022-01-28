from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import as_declarative
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.future import select
from typing import Any, Dict, List, NoReturn, Optional, Tuple, Type, TypeVar
from fastapi import Request

from . import get_config

config = get_config()
DATABASE_URL = config.DATABASE_URI

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @classmethod
    async def get(cls, session, id):
        query = select(cls).where(cls.id==int(id))
        result = await session.execute(query)
        return result.scalars().first()

    def pydantic(self, schema):
        # https://stackoverflow.com/a/1398059/6652082
        members = list(schema.__fields__.keys())
        result = {}
        for member in members:
            result[member] = getattr(self, member)
        return result

async def init_models():
    from app.models.user import User
    from app.models.person import Person
    from app.models.permission import Permission
    from app.models.deal import Deal

# Dependency
async def get_session(request: Request)-> AsyncSession:
    async with SessionLocal() as session:
        yield session

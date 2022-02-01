from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import Any, Dict, List, NoReturn, Optional, Tuple, Type, TypeVar
from fastapi import Request

from . import get_config

config = get_config()
DATABASE_URL = config.DATABASE_URI

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Dependency
async def get_db_session(request: Request)-> AsyncSession:
    async with SessionLocal() as db_session:
        yield db_session

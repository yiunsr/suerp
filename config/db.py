from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from . import get_config

config = get_config()
DATABASE_URL = config.DATABASE_URI

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

async def init_models():
    from app.models.user import User
    from app.models.person import Person
    from app.models.permission import Permission
    from app.models.deal import Deal

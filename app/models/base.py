from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.orm import as_declarative
from sqlalchemy.orm import declared_attr
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.future import select

@as_declarative()
class Base:
    @declared_attr
    # pylint: disable=no-member, no-self-argument
    def __tablename__(cls):
        return cls.__name__.lower()

    @classmethod
    async def get(cls, db_session, id):
        query = select(cls).where(cls.id==int(id))
        result = await db_session.execute(query)
        return result.scalars().first()

    @classmethod
    async def listing(cls, db_session, filter_={}):
        query = select(cls)
        result = await db_session.execute(query)
        return result.scalars().all()

    def pydantic(self, schema):
        # https://stackoverflow.com/a/1398059/6652082
        members = list(schema.__fields__.keys())
        result = {}
        for member in members:
            result[member] = getattr(self, member)
        return result

class BaseInfo():  # Base Of All Table
    id = Column(Integer, primary_key=True)
    testmode = Column(String(1), nullable=False, server_default=text("''"))
    status = Column(String(1), nullable=False, server_default=text("'A'"))

    ref_id0 = Column(Integer, nullable=True)
    ref_id1 = Column(Integer, nullable=True)
    ref_id2 = Column(Integer, nullable=True)
    ref_id3 = Column(Integer, nullable=True)


class BaseCU():  # BaseCreateUpdate
    created_user_id = Column(Integer)
    updated_user_id = Column(Integer)
    created_at = Column(DateTime(True), default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(True), default=func.now(), onupdate=func.now(), nullable=False
    )

class BaseCT():  # BaseCategory
    category = Column(Integer)
    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    category_data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    category_tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))

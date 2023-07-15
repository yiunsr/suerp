from sqlalchemy import Column
from sqlalchemy import SmallInteger
from sqlalchemy import Integer
from sqlalchemy import CHAR
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
    async def count(cls, db_session, filters={}):
        count_query = select(func.count()).select_from(cls)

        for k, v in filters.items():
            count_query = count_query.where(getattr(cls, k) == v)

        result = await db_session.scalar(count_query)
        return result

    @classmethod
    async def listing(cls, db_session, filters={}):
        query = select(cls)
        result = await db_session.execute(query)
        return result.scalars().all()
    
    @classmethod
    async def update(cls, db_session, db_obj, **kwargs):
        for k, v in kwargs.items():
            setattr(db_obj, k, v)
        return db_obj

    def pydantic(self, schema):
        # https://stackoverflow.com/a/1398059/6652082
        members = list(schema.__fields__.keys())
        result = {}
        for member in members:
            result[member] = getattr(self, member)
        return result

class BaseInfo():  # Base Of All Table
    app_meta_id = Column(SmallInteger, nullable=True)
    testmode = Column(CHAR(1), nullable=False, server_default=text("''"))
    status = Column(CHAR(1), nullable=False, server_default=text("'A'"))

    ref_id0 = Column(Integer, nullable=True)
    ref_id1 = Column(Integer, nullable=True)
    ref_id2 = Column(Integer, nullable=True)
    ref_id3 = Column(Integer, nullable=True)


class BaseCU():  # BaseCreateUpdate
    created_user_id = Column(Integer)
    updated_user_id = Column(Integer)
    create_ets = Column(Integer, default=func.now_ets(), nullable=False)
    update_ets = Column(
        Integer, default=func.now_ets(), onupdate=func.now_ets(), nullable=False
    )

class BaseCT():  # BaseCategory
    category = Column(Integer)
    data_jb = Column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    tags_jb = Column(JSONB, nullable=False, server_default=text("'[]'::jsonb"))
    category_data_jb = Column(
        JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    category_tags_jb = Column(
        JSONB, nullable=False, server_default=text("'[]'::jsonb"))

from sqlalchemy import Column
from sqlalchemy import SmallInteger
from sqlalchemy import Integer
from sqlalchemy import CHAR
from sqlalchemy import text
from sqlalchemy import desc
from sqlalchemy import asc
from sqlalchemy import func
from sqlalchemy import Text
from sqlalchemy import cast
from sqlalchemy.orm import as_declarative
from sqlalchemy.orm import declared_attr
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.future import select

def query_filter(cls, query, filter_param):
    new_query = query
    for key, value in filter_param.items():
        if value in (None, ""):
            continue
        new_key = key.replace("__in", "")
        column = getattr(cls, new_key)
        class_name = column.type.__class__.__name__
        if class_name in ("Integer", ):
            value = int(value)
            new_query = new_query.where(column == value)
        elif class_name in ("String", ):
            new_query = new_query.filter(column.like('%'+value+'%'))
        elif class_name in ("JSONB", ):
            if "__in" in key:
                value = '%' + value +'%'
                new_query = new_query.filter(
                    cast(column, Text).like('%'+value+'%'))
            else:
                new_query = new_query.where(column == value)
        else:
            new_query = new_query.where(column == value)
    return new_query


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
    async def count(cls, db_session, filter_param={}):
        count_query = select(func.count()).select_from(cls)
        count_query = query_filter(cls, count_query, filter_param)

        result = await db_session.scalar(count_query)
        return result

    @classmethod
    async def listing(cls, db_session, filter_param, order_param, paging_param):
        query = select(cls)
        query = query_filter(cls, query, filter_param)

        if order_param:
            orders = order_param.split(",") or "-id".split(",")
            for order in orders:
                key = order
                if key[0] == "-":
                    key = key[1:]
                    query = query.order_by(desc(getattr(cls, key)))
                else:
                    query = query.order_by(asc(getattr(cls, key)))
        skip = paging_param.get("skip")
        limit = paging_param.get("limit")
        query = query.offset(skip).limit(limit)
        result = await db_session.execute(query)
        return result.scalars().all()
    
    @classmethod
    async def insert(cls, db_session, param):
        query = select(cls).where(cls.id==int(id))
        result = await db_session.execute(query)
        return result.scalars().first()

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

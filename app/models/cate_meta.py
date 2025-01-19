from sqlalchemy import Column
from sqlalchemy import SmallInteger
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import CHAR
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base

class CateMeta(Base):
    __tablename__ = "cate_meta"

    id = Column(Integer, primary_key=True)
    table_meta_id = Column(SmallInteger, nullable=False)
    name = Column(String(128), nullable=False, server_default=text("''"))
    testmode = Column(CHAR(1), nullable=False, server_default=text("''"))
    status = Column(CHAR(1), nullable=False, server_default=text("'A'"))
    db_key = Column(CHAR(3), nullable=False, server_default=text("''"))
    api_key = Column(CHAR(3), nullable=False, server_default=text("''"))

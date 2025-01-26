from sqlalchemy import Column
from sqlalchemy import SmallInteger
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import CHAR
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base

class CategoryMeta(Base):
    __tablename__ = "category_meta"

    id = Column(Integer, primary_key=True)
    table_meta_id = Column(SmallInteger, nullable=False)
    status = Column(CHAR(1), nullable=False, server_default=text("'A'"))
    name = Column(String(128), nullable=False, server_default=text("''"))

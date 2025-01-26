from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import CHAR
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base

class TableMeta(Base):
    __tablename__ = "table_meta"

    id = Column(Integer, primary_key=True)
    status = Column(CHAR(1), nullable=False, server_default=text("'A'"))
    code = Column(String(32), nullable=False, server_default=text("''"))
    detail = Column(String(256), nullable=False, server_default=text("''"))
    name_lang_jb = Column(
        JSONB, nullable=False, server_default=text("'{}'::jsonb"))

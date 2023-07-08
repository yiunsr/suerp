from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import SmallInteger
from sqlalchemy import CHAR
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base
from .base import BaseCU

class ColMeta(Base, BaseCU):
    __tablename__ = "col_meta"
    id = Column(Integer, primary_key=True)
    
    table_meta_id = Column(SmallInteger, nullable=False)
    testmode = Column(CHAR(1), nullable=False, server_default=text("''"))
    status = Column(CHAR(1), nullable=False, server_default=text("'A'"))
    col_meta = Column(CHAR(1), nullable=False, server_default=text("''"))
    data_type = Column(CHAR(1), nullable=False, server_default=text("''"))

    code = Column(CHAR(16), nullable=False, server_default=text("''"))
    name_lang_jb = Column(
        JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    options_jb = Column(
        JSONB, nullable=False, server_default=text("'[]'::jsonb"))
    default_jb = Column(
        JSONB, nullable=False, server_default=text("'null'::jsonb"))
    html_type = Column(
        String(128), nullable=False, server_default=text("''"))
    html_pattern = Column(
        String(128), nullable=False, server_default=text("''"))
    detail = Column(
        String(128), nullable=False, server_default=text("''"))

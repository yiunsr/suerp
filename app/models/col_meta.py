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
    category_meta_id = Column(SmallInteger, nullable=False)
    status = Column(CHAR(1), nullable=False, server_default=text("'A'"))
    column_meta = Column(CHAR(1), nullable=False, server_default=text("''"))
    data_type = Column(CHAR(1), nullable=False, server_default=text("''"))
    name = Column(String(32), nullable=False, server_default=text("''"))
    detail = Column(
        String(128), nullable=False, server_default=text("''"))

    options_jb = Column(
        JSONB, nullable=False, server_default=text("'[]'::jsonb"))
    default_jb = Column(
        JSONB, nullable=False, server_default=text("'null'::jsonb"))
    visible = Column(
        SmallInteger, nullable=False, server_default=text("3"))
    html_type = Column(
        String(128), nullable=False, server_default=text("''"))
    html_pattern = Column(
        String(128), nullable=False, server_default=text("''"))
    html_detail = Column(
        String(128), nullable=False, server_default=text("''"))


    @property
    def code(self):
        return "_" + str(self.id).zfill(7)

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import CHAR
from sqlalchemy import VARCHAR
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base

class AppMeta(Base):
    __tablename__ = "app_meta"

    id = Column(Integer, primary_key=True)
    status = Column(CHAR(1), nullable=False, server_default=text("'A'"))
    name = Column(VARCHAR(16), nullable=False, server_default=text("''"))
    detail = Column(VARCHAR(128), nullable=False, server_default=text("''"))

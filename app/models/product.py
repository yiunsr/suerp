from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import BIT

from .base import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    status = Column(String(1), nullable=False, server_default=text("''"))
    testmode = Column(String(1), nullable=False, server_default=text("''"))
    create_user = Column(Integer, nullable=False)
    update_user = Column(Integer, nullable=False)

    name = Column(String(128), nullable=False, server_default=text("''"))
    display = Column(String(128), nullable=False, server_default=text("''"))

    ref_id1 = Column(Integer)
    ref_id0 = Column(Integer)

    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    category_data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    category_tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))

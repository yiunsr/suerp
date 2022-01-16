from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import BIT

from config.db import Base

class Deal(Base):
    __tablename__ = "deal"

    id = Column(Integer, primary_key=True)
    name = Column(String(1), nullable=False, server_default=text("''"))
    status = Column(String(1), nullable=False, server_default=text("''"))
    testmode = Column(String(1), nullable=False, server_default=text("''"))

    ref_id1 = Column(Integer)
    ref_id0 = Column(Integer)

    create_user = Column(Integer, nullable=False)
    update_user = Column(Integer, nullable=False)
    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    category_data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    category_tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))

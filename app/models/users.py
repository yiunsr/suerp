from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB

from config.db import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, server_default=text("'0'::bigint"))
    email = Column(String(256), nullable=False)
    first_name = Column(String(64))
    last_name = Column(String(64))
    display = Column(String(64))
    nickname = Column(String(64))
    avatar = Column(String(256))
    status = Column(String(1))
    password = Column(String(256))
    password_last_at = Column(DateTime(True), nullable=False)
    created_at = Column(DateTime(True), default=func.now(), nullable=False)
    updated_at = Column(DateTime(True), default=func.now(),
                        onupdate=func.now(), nullable=False)
    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))

# metadata = Base.metadata
# metadata = dbManager.Base.metadata

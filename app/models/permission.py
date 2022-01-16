from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import BIT

from config.db import Base

class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, server_default=text("''"))
    detail = Column(String(256), nullable=False, server_default=text("''"))
    key = Column(String(8), nullable=False, server_default=text("''"))


class UserPermission(Base):
    __tablename__ = "user_permission"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    permission_id = Column(Integer)
    created_at = Column(DateTime(True), default=func.now(), nullable=False)

class UgroupPermission(Base):
    __tablename__ = "ugroup_permission"

    id = Column(Integer, primary_key=True)
    ugroup_id = Column(Integer)
    permission_id = Column(Integer)
    created_at = Column(DateTime(True), default=func.now(), nullable=False)

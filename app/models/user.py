import string
import secrets
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import BIT

from config.db import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    status = Column(String(1), nullable=False, server_default=text("''"))
    testmode = Column(String(1), nullable=False, server_default=text("''"))

    ref_id1 = Column(Integer)
    ref_id0 = Column(Integer)

    name = Column(String(64), nullable=False, server_default=text("''"))
    email = Column(String(256), nullable=False)
    first_name = Column(String(64), nullable=False, server_default=text("''"))
    last_name = Column(String(64), nullable=False, server_default=text("''"))
    display = Column(String(64), nullable=False, server_default=text("''"))
    nickname = Column(String(64), nullable=False, server_default=text("''"))
    avatar = Column(String(256), nullable=False, server_default=text("''"))

    api_key = Column(String(256), nullable=False, server_default=text("''"))
    api_key_last_at = Column(DateTime(True), nullable=False)

    password = Column(String(256), nullable=False, server_default=text("''"))
    password_last_at = Column(DateTime(True), nullable=False)
    created_at = Column(DateTime(True), default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(True), default=func.now(), onupdate=func.now(), nullable=False
    )
    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))

    def gen_api_key(self):
        alphabet = string.ascii_letters + string.digits
        key = ''.join(secrets.choice(alphabet) for i in range(20))
        return key



class UGroup(Base):
    __tablename__ = "ugroup"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, server_default=text("''"))
    detail = Column(String(64), nullable=False, server_default=text("''"))
    status = Column(String(1), nullable=False, server_default=text("''"))
    testmode = Column(String(1), nullable=False, server_default=text("''"))

    created_at = Column(DateTime(True), default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(True), default=func.now(), onupdate=func.now(), nullable=False
    )
    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))


class UserUGroup(Base):
    __tablename__ = "user_ugroup"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    group_id = Column(Integer)

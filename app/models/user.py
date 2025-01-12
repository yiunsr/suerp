import string
import secrets
from passlib.hash import pbkdf2_sha256
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import BIT
from sqlalchemy.future import select

from .base import Base
from .base import BaseInfo
from .base import BaseCU
from .base import BaseCT

class User(Base, BaseInfo, BaseCT):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user_role = Column(String(1), nullable=False, server_default=text("'N'"))

    email = Column(String(256), nullable=False, unique=True)
    first_name = Column(String(64), nullable=False, server_default=text("''"))
    last_name = Column(String(64), nullable=False, server_default=text("''"))
    display = Column(String(64), nullable=False, server_default=text("''"))
    nickname = Column(String(64), nullable=False, server_default=text("''"))
    avatar = Column(String(256), nullable=False, server_default=text("''"))

    api_key = Column(String(256), nullable=False, server_default=text("''"))
    api_key_last_ets = Column(Integer, nullable=False)

    hash_password = Column(
        String(256), nullable=False, server_default=text("''"))
    password_last_ets = Column(Integer, nullable=False)
    last_join_ets = Column(Integer)
    create_ets = Column(Integer, default=func.now_ets(), nullable=False)
    update_ets = Column(
        Integer, default=func.now_ets(), onupdate=func.now_ets(), nullable=False
    )

    @staticmethod
    def gen_api_key() -> str:
        alphabet = string.ascii_letters + string.digits
        key = ''.join(secrets.choice(alphabet) for i in range(20))
        return key

    @staticmethod
    def gen_password_hash( password) -> str:
        hash_pw = pbkdf2_sha256.hash(password)
        return hash_pw

    def check_password(self, password) -> bool:
        return pbkdf2_sha256.verify(password, self.hash_password)

    @classmethod
    async def get_by_email(cls, db_session, email):
        query = select(cls).where(cls.email==email)
        result = await db_session.execute(query)
        return result.scalars().first()

    @property
    def user_role_str_en(self):
        if self.user_role == "M":
            return "Manager"
        elif self.user_role == "N":
            return "Normal"
        return ""
    

class UGroup(Base, BaseInfo, BaseCU):
    __tablename__ = "ugroup"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, server_default=text("''"))
    detail = Column(String(64), nullable=False, server_default=text("''"))

    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))

class UserUGroup(Base):
    __tablename__ = "user_ugroup"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    ugroup_id = Column(Integer)

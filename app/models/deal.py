from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import BIT

from .base import Base
from .base import BaseInfo
from .base import BaseCU
from .base import BaseCT

class Deal(Base, BaseInfo, BaseCU, BaseCT):
    __tablename__ = "deal"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False, server_default=text("''"))
    detail = Column(String(256), nullable=False, server_default=text("''"))
    owner_user_id = Column(Integer)
    owner_group_id = Column(Integer)
    owner_person_id = Column(Integer)

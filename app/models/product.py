from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import BIT

from .base import Base
from .base import BaseInfo
from .base import BaseCU
from .base import BaseCT

class Product(Base, BaseInfo, BaseCU, BaseCT):
    __tablename__ = "product"

    name = Column(String(128), nullable=False, server_default=text("''"))
    display = Column(String(128), nullable=False, server_default=text("''"))

    owner_user_id = Column(Integer, nullable=True)
    owner_group_id = Column(Integer, nullable=True)
    owner_person_id = Column(Integer, nullable=True)

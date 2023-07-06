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

class Project(Base, BaseInfo, BaseCU, BaseCT):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    
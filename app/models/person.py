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

class Person(Base, BaseInfo, BaseCU, BaseCT):
    __tablename__ = "person"

    name = Column(String(64), nullable=False, server_default=text("''"))
    first_name = Column(String(64), nullable=False, server_default=text("''"))
    last_name = Column(String(64), nullable=False, server_default=text("''"))

    address_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    phone_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    email_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    messenger_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    url_jb = Column(JSONB, server_default=text("'[]'::jsonb"))


class Organization(Base, BaseInfo, BaseCU, BaseCT):
    __tablename__ = "organization"

    name = Column(String(64), nullable=False, server_default=text("''"))

    address_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    phone_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    email_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    messenger_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    url_jb = Column(JSONB, server_default=text("'[]'::jsonb"))


class PersonOrganization(Base):
    __tablename__ = "person_organization"

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    org_id = Column(Integer)

    created_at = Column(DateTime(True), default=func.now(), nullable=False)
    status = Column(String(1), nullable=False, server_default=text("''"))
    testmode = Column(String(1), nullable=False, server_default=text("''"))
    role_jsonb = Column(JSONB, server_default=text("'[]'::jsonb"))

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import BIT

from config.db import Base

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    status = Column(String(1), nullable=False, server_default=text("''"))
    testmode = Column(String(1), nullable=False, server_default=text("''"))
    name = Column(String(64), nullable=False, server_default=text("''"))
    first_name = Column(String(64), nullable=False, server_default=text("''"))
    last_name = Column(String(64), nullable=False, server_default=text("''"))

    ref_id0 = Column(Integer)
    ref_id1 = Column(Integer)
    created_user_id = Column(Integer)
    updated_user_id = Column(Integer)
    created_at = Column(DateTime(True), default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(True), default=func.now(), onupdate=func.now(), nullable=False
    )
    address_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    phone_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    email_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    messenger_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    category = Column(Integer)
    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    category_data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    category_tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, server_default=text("''"))
    status = Column(String(1), nullable=False, server_default=text("''"))
    testmode = Column(String(1), nullable=False, server_default=text("''"))

    ref_id0 = Column(Integer)
    ref_id1 = Column(Integer)
    created_user_id = Column(Integer)
    updated_user_id = Column(Integer)
    created_at = Column(DateTime(True), default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(True), default=func.now(), onupdate=func.now(), nullable=False
    )
    address_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    phone_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    email_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    messenger_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    category = Column(Integer)
    data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))
    category_data_jb = Column(JSONB, server_default=text("'{}'::jsonb"))
    category_tags_jb = Column(JSONB, server_default=text("'[]'::jsonb"))


class PersonCompany(Base):
    __tablename__ = "person_company"

    id = Column(Integer, primary_key=True)
    person = Column(Integer)
    company_id = Column(Integer)
    role_jsonb = Column(JSONB, server_default=text("'[]'::jsonb"))
    created_at = Column(DateTime(True), default=func.now(), nullable=False)
    status = Column(String(1), nullable=False, server_default=text("''"))
    testmode = Column(String(1), nullable=False, server_default=text("''"))

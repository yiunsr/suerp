from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.models.user import User as DB_User

class UserBase(BaseModel):
    id: int
    email: Optional[EmailStr] = None
    first_name: str = None
    last_name: str = None
    display: str = None
    user_role: str = None
    status: str = None

class UserSignup(UserBase):
    email: EmailStr
    password: str

class UserCreate(UserBase):
    email: EmailStr

class UserUpdate(UserBase):
    old_password: str = None
    new_password: str = None

class UserPublic(UserBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UserPublicList(BaseModel):
    total: int
    data: list[UserPublic]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UserPrivate(UserBase):
    last_join_ets: int = None
    password_last_ets: int
    ref_id0: int = None
    ref_id1: int = None
    ref_id2: int = None
    ref_id3: int = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UserPrivateList(BaseModel):
    total: int
    data: list[UserPrivate]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.models.user import User as DB_User

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    name: str = None
    first_name: str = None
    last_name: str = None

class UserSignup(UserBase):
    email: EmailStr
    password: str

class UserCreate(UserBase):
    email: EmailStr

class UserUpdate(UserBase):
    old_password: str = None
    new_password: str = None

class UserPublic(BaseModel):
    id: int
    email: EmailStr
    name: str = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UserPublicList(BaseModel):
    total: int
    data: list[UserPublic]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UserPrivate(BaseModel):
    id: int
    email: EmailStr
    name: str
    first_name: str
    last_name: str
    password_last_ets: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UserPrivateList(BaseModel):
    total: int
    data: list[UserPrivate]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

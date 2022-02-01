from typing import Optional
from pendulum import datetime
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

class UserPubSimple(BaseModel):
    id: int
    email: EmailStr
    name: str = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserPrivateDetail(BaseModel):
    id: int
    email: EmailStr
    name: str
    first_name: str
    last_name: str
    last_password_at: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

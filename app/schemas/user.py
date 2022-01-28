from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.user import User as DB_User

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    email: EmailStr

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserSimple(BaseModel):
    id: int
    email: EmailStr
    name: str = None
    first_name: str = None
    last_name: str = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

    # @classmethod
    # def from_db(DB_User):
    #     pass

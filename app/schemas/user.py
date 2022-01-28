from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    email: EmailStr

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserResDetail(BaseModel):
    id: int
    email: EmailStr
    name: str = None
    first_name: str = None
    last_name: str = None

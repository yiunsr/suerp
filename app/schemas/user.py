from typing import Optional, ClassVar
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from app.models.user import User as DB_User

class UserBase(BaseModel):
    id: Optional[int]
    email: Optional[EmailStr]
    first_name: str = ""
    last_name: str = ""
    display: str = ""
    user_role: str = ""
    status: str = ""
    create_ets: Optional[int]

class UserSignup(UserBase):
    email: EmailStr
    password: str

class UserChangePassword(UserBase):
    old_password: str = None
    new_password: str = None

class UserPublic(UserBase):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class UserPublicList(BaseModel):
    total: int
    data: list[UserPublic]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class UserPrivate(UserBase):
    nickname: str = None
    last_join_ets: Optional[int] = None
    password_last_ets: Optional[int] = None
    ref_id0: Optional[int] = None
    ref_id1: Optional[int] = None
    ref_id2: Optional[int] = None
    ref_id3: Optional[int] = None

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class UserPrivateCreate(UserBase):
    id: ClassVar
    create_ets: ClassVar
    
    nickname: str = None
    ref_id0: int | None = None
    ref_id1: int | None = None
    ref_id2: int | None = None
    ref_id3: int | None = None

    class Config:
        exclude = {"id"}

class UserPrivateUpdate(UserPrivateCreate):
    pass

class UserPrivateList(BaseModel):
    total: int
    data: list[UserPrivate]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

from typing import Optional, ClassVar
from typing import Any
from typing_extensions import Self

from datetime import datetime
from pydantic import BaseModel, ModelWrapValidatorHandler, ConfigDict, ValidationError,\
    EmailStr, Field, ValidationInfo, FieldValidationInfo, model_validator

from config.cache import get_extra_fields_sync

from app.models.user import User as DB_User
from app.models.base import Base


class UserBase(BaseModel):
    model_config  = ConfigDict(extra="allow")

    id: Optional[int]
    email: Optional[EmailStr]
    first_name: str = ""
    last_name: str = ""
    nickname: str = ""
    user_role: str = ""
    status: str = ""
    create_ets: Optional[int]
    category_meta_id: int
    data_jb: dict = Field(exclude=True, default={})

    @model_validator(mode='wrap')
    @classmethod
    def set_extra_columns(cls, data: Any, 
            handler: ModelWrapValidatorHandler[Self],
            info: FieldValidationInfo) -> Self:
        try:
            is_db_data = isinstance(data, Base)
            is_pydantic_model = isinstance(data, BaseModel)
            validated_self = handler(data)

            context = info.context or {}
            extra_fields = context.get("extra_fields") or []

            if is_db_data is False:
                return validated_self
            validated_self._set_extra_columns(data, extra_fields)
            return validated_self
        except ValidationError:
            logging.error('Model %s failed to validate with data %s', cls, data)
            raise
    
    def _set_extra_columns(self, data: Any, extra_fields: []):
        data_jb = data.data_jb
        for field in extra_fields:
            value = data_jb.get(field)
            setattr(self, "user_" + field, value)


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
        extra="allow"

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

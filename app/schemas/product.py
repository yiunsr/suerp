from typing import Optional
from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr
from app.models.product import Product as DB_Product
from app.schemas.common_field import EmailField
from app.schemas.common_field import AddressField
from app.schemas.common_field import PhoneField
from app.schemas.common_field import MessengerField
from app.schemas.common_field import UrlField

class ProductBase(BaseModel):
    name: str
    display: str = None
    memo: str = None
    owner_user_id: int = None
    owner_group_id: int = None
    owner_person_id: int = None

class PersonPublic(ProductBase):
    id: int
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

from typing import Optional
from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr
from app.models.person import Person as DB_Person
from app.schemas.common_field import EmailField
from app.schemas.common_field import AddressField
from app.schemas.common_field import PhoneField
from app.schemas.common_field import MessengerField
from app.schemas.common_field import UrlField

class PersonBase(BaseModel):
    name: str
    first_name: str = None
    last_name: str = None
    email_jb: List[EmailField] = []
    address_jb: List[AddressField] = []
    phone_jb: List[PhoneField] = []
    url_jb: List[UrlField] = []


class PersonPublic(PersonBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

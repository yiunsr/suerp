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
    id: Optional[int]
    first_name: str = ""
    last_name: str = ""
    display: str = ""
    email_jb: List[EmailField] = []
    phone_jb: List[PhoneField] = []
    url_jb: List[UrlField] = []
    status: str = ""
    create_ets: Optional[int] = None

class PersonPublic(PersonBase):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class PersonPrivate(PersonBase):
    ref_id0: Optional[int] = None
    ref_id1: Optional[int] = None
    ref_id2: Optional[int] = None
    ref_id3: Optional[int] = None

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
    
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.models.person import Person as DB_Person

class EmailField(BaseModel):
    email: EmailStr = None
    type: str = None

class AddressField(BaseModel):
    address: str = None
    type: str = None

class PhoneField(BaseModel):
    phone: str = None
    type: str = None

class MessengerField(BaseModel):
    messenge: str = None
    type: str = None

class UrlField(BaseModel):
    url: str = None
    type: str = None

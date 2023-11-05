from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.models.person import Person as DB_Person

class EmailField(BaseModel):
    value: EmailStr = None
    type: str = None

class AddressField(BaseModel):
    value: str = None
    type: str = None

class PhoneField(BaseModel):
    value: str = None
    type: str = None

class MessengerField(BaseModel):
    value: str = None
    type: str = None

class UrlField(BaseModel):
    value: str = None
    type: str = None

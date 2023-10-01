from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from app.models.person import Person as DB_Person
from pydantic import BaseModel, EmailStr

class EmailField:
    email: EmailStr = None
    type: str = None

class AddressField:
    address: str = None
    type: str = None

class PhoneField:
    phone: str = None
    type: str = None

class MessengerField:
    messenge: str = None
    type: str = None

class UrlField:
    url: str = None
    type: str = None

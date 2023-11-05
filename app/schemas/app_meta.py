from typing import Optional
from typing import Any
from pydantic import BaseModel
from pydantic import Json

class AppMetaSchema(BaseModel):
    id: int
    status: str = "A"
    name: str
    detail: str

    class Config:
        from_attributes = True

class AppMetaCreate(BaseModel):
    status: str = "A"
    name: str
    detail: str

    class Config:
        from_attributes = True

class AppMetaUpdate(BaseModel):
    status: str = "A"
    name: str
    detail: str

    class Config:
        from_attributes = True

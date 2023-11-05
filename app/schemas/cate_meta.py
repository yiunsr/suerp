from typing import Optional
from typing import Any
from pydantic import BaseModel
from pydantic import Json
from app.models.cate_meta import CateMeta

class CateMetaSchema(BaseModel):
    id: int
    app_meta_id: int = None
    table_meta_id: int
    status: str
    testmode: str
    db_key: str
    api_key: str

    class Config:
        from_attributes = True

class CateMetaCreate(BaseModel):
    app_meta_id: int = None
    table_meta_id: int
    status: str
    testmode: str
    db_key: str
    api_key: str

class CateMetaUpdate(BaseModel):
    app_meta_id: int = None
    table_meta_id: int
    status: str
    testmode: str
    db_key: str
    api_key: str

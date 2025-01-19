from typing import Optional
from typing import Any
from pydantic import BaseModel
from pydantic import Json
from app.models.cate_meta import CateMeta

class CateMetaSchema(BaseModel):
    id: int
    table_meta_id: int
    status: str
    testmode: str
    name: str
    db_key: str
    api_key: str

    class Config:
        from_attributes = True

class CateMetaSchemaListBase(CateMetaSchema):
    id: int

class CateMetaSchemaCreate(BaseModel):
    class Config:
        exclude = {"id"}
        from_attributes = True
    
    table_meta_id: int
    status: str
    name: str

class CateMetaSchemaUpdate(BaseModel):
    id: int
    table_meta_id: int
    status: str
    name: str

class CateMetaPrivateDetail(CateMetaSchema):
    id: int
    
    class Config:
        from_attributes = True

from typing import Optional
from typing import Any
from pydantic import BaseModel
from pydantic import Json
from app.models.category_meta import CategoryMeta

class CategoryMetaSchema(BaseModel):
    id: int
    table_meta_id: int
    status: str
    name: str
    db_key: str
    api_key: str

    class Config:
        from_attributes = True

class CategoryMetaSchemaListBase(CategoryMetaSchema):
    id: int

class CategoryMetaSchemaCreate(BaseModel):
    class Config:
        exclude = {"id"}
        from_attributes = True
    
    table_meta_id: int
    status: str
    name: str

class CategoryMetaSchemaUpdate(BaseModel):
    id: int
    table_meta_id: int
    status: str
    name: str

class CategoryMetaPrivateDetail(CategoryMetaSchema):
    id: int
    
    class Config:
        from_attributes = True

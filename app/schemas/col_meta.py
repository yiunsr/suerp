from typing import Optional
from typing import Any
from typing import List
from pydantic import BaseModel
from pydantic import Json
from pydantic import Field
from app.models.col_meta import ColMeta as ColMeta

class ColMetaSchema(BaseModel):
    # id: int
    table_meta_id: int
    status: str
    column_meta: str
    data_type: str
    name: str
    detail: str
    category_meta_id: int

    options_jb: list
    default_jb: int|bool|None|str
    visible: int
    html_type: str
    html_pattern: str
    html_detail: str

    class Config:
        from_attributes = True

class ColMetaSchemaListBase(ColMetaSchema):
    id: int
    code: str=""

    class Config:
        from_attributes = True

class ColMetaCreate(ColMetaSchema):
    class Config:
        exclude = {"id"}

class ColMetaUpdate(ColMetaSchema):
    table_meta_id: int
    col_meta: str
    data_type: str
    name: str

class ColMetaPrivateDetail(ColMetaSchema):
    id: int
    code: str=""
    
    class Config:
        from_attributes = True
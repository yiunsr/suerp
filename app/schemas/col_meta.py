from typing import Optional
from typing import Any
from pydantic import BaseModel
from pydantic import Json
from app.models.col_meta import ColMeta as ColMeta

class ColMetaSchema(BaseModel):
    id: int
    table_meta_id: int
    status: str
    col_meta: str
    data_type: str
    name_lang_jb: dict
    options_jb: dict
    default_jb: Json[Any]
    html_type: str
    html_pattern: str
    detail: str

    class Config:
        orm_mode = True

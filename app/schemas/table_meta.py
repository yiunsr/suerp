from typing import Optional
from pydantic import BaseModel
from app.models.table_meta import TableMeta as DBTableMeta

class TableMetaSchema(BaseModel):
    id: int
    code: str
    status: str
    detail: str
    name_lang_jb: dict

    class Config:
        orm_mode = True

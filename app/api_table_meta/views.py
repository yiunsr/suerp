import traceback
from typing import Any, List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from pydantic import parse_obj_as

from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.table_meta import TableMeta
from app.schemas.table_meta import TableMetaSchema

from . import api_table_meta

@api_table_meta.get("/")
async def list_obj(
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_table_metas = await TableMeta.listing(db_session)
    return parse_obj_as(List[TableMetaSchema], db_table_metas)

@api_table_meta.get("/{id}")
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await TableMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return parse_obj_as(TableMetaSchema, db_obj)

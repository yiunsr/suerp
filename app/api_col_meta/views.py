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
from app.models.col_meta import ColMeta
from app.schemas.col_meta import ColMetaSchema

from . import api_col_meta

@api_col_meta.get("/")
async def list_obj(db_session: Session = Depends(get_db_session)) -> Any:
    db_table_metas = await ColMeta.listing(db_session)
    return parse_obj_as(List[ColMetaSchema], db_table_metas)

@api_col_meta.get("/{id}")
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session)) -> Any:
    db_obj = await ColMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return parse_obj_as(ColMeta, db_obj)

@api_col_meta.post("/{id}")
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session)) -> Any:
    db_obj = await ColMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return parse_obj_as(ColMeta, db_obj)

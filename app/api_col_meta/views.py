import traceback
from typing import Annotated
from typing import Any, List, Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session
from pydantic import parse_obj_as

from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.col_meta import ColMeta
from app.schemas.col_meta import ColMetaSchema
from app.utils.common_param_utils import common_paging_param
from app.utils.common_param_utils import common_order_param
from . import api_col_meta

def col_meta_filter_param(
        id: str = "", display: str = "",
        first_name: str = "", last_name: str = "",
        phone: str = "", email: str = ""
        ):
    return {"id": id, "display": display,
        "first_name": first_name, "last_name": last_name,
        "phone_jb": phone, "email_jb__in": email}

@api_col_meta.get("/")
async def list_obj(
        filter_param: Annotated[dict, Depends(col_meta_filter_param)],
        paging_param: Annotated[dict, Depends(common_paging_param)],
        order_param: Annotated[dict, Depends(common_order_param)],
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_count = await ColMeta.count(db_session, filter_param)
    db_col_metas = await ColMeta.listing(db_session, filter_param, order_param, paging_param)
    return dict(total=db_count, data=db_col_metas)

@api_col_meta.get("/{id}")
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await ColMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return parse_obj_as(ColMeta, db_obj)

@api_col_meta.post("/")
async def get_obj(
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await ColMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return parse_obj_as(ColMeta, db_obj)

@api_col_meta.post(
        "/", response_model=ColMetaSchema, status_code=status.HTTP_201_CREATED)
async def create(
        data: ColMetaSchema, db_session: Session = Depends(get_db_session)) -> Any:
    db_obj = Person(**data.model_dump())
    db_session.add(db_obj)
    await db_session.commit()
    await db_session.refresh(db_obj)
    db_data = ColMetaSchema.model_validate(db_obj)
    return db_data
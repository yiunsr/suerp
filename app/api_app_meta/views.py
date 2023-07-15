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
from app.models.app_meta import AppMeta
from app.schemas.app_meta import AppMetaSchema
from app.schemas.app_meta import AppMetaCreate
from app.schemas.app_meta import AppMetaUpdate

from . import api_app_meta

@api_app_meta.get("/")
async def list_obj(db_session: Session = Depends(get_db_session),
                   _ = Depends(get_current_active_user)) -> Any:
    db_app_metas = await AppMeta.listing(db_session)
    return parse_obj_as(List[AppMetaSchema], db_app_metas)

@api_app_meta.get("/{id}")
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await AppMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return parse_obj_as(AppMetaSchema, db_obj)

@api_app_meta.post("/")
async def create_obj(
        data: AppMetaCreate, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_cate_meta = AppMeta(**data.dict())
    db_session.add(db_cate_meta)

    try:
        await db_session.commit()
    except Exception as e:
        err_text = traceback.format_exc()
        print(err_text)
    
    # https://stackoverflow.com/a/76038520
    # 가장 최고의 방법은 이 코드가 없이 비동기로 동작하는게 가장 좋은데.
    # 함수내에서 
    await db_session.refresh(db_cate_meta)
    return db_cate_meta.pydantic(AppMetaSchema)

@api_app_meta.put("/{id}")
async def put_obj(
        id: int, data: AppMetaUpdate, 
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await AppMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    await AppMeta.update(db_session, db_obj, **data.dict())
    await db_session.commit()
    await db_session.refresh(db_obj)
    return parse_obj_as(AppMetaSchema, db_obj)

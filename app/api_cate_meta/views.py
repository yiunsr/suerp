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
from app.models.cate_meta import CateMeta
from app.schemas.cate_meta import CateMetaSchema
from app.schemas.cate_meta import CateMetaCreate

from . import api_cate_meta

@api_cate_meta.get("/")
async def list_obj(db_session: Session = Depends(get_db_session),
                   _ = Depends(get_current_active_user)) -> Any:
    db_cate_metas = await CateMeta.listing(db_session)
    return parse_obj_as(List[CateMetaSchema], db_cate_metas)

@api_cate_meta.get("/{id}")
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await CateMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return parse_obj_as(CateMeta, db_obj)

@api_cate_meta.post("/")
async def get_obj(
        data: CateMetaCreate, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_cate_meta = CateMeta(**data.dict())
    db_session.add(db_cate_meta)

    try:
        await db_session.commit()
    except Exception as e:
        err_text = traceback.format_exc()
        print(err_text)
    return db_cate_meta.pydantic(CateMetaSchema)

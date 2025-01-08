import traceback
from typing import Annotated
from typing import Any, List, Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session
from pydantic import parse_obj_as
from pydantic import TypeAdapter


from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.col_meta import ColMeta
from app.schemas.col_meta import ColMetaSchema, ColMetaCreate, \
    ColMetaSchemaListBase, ColMetaPrivateDetail
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
        _ = Depends(get_current_active_user),
        ) -> Any:
    db_count = await ColMeta.count(db_session, filter_param)
    db_col_metas = await ColMeta.listing(db_session, filter_param, order_param, paging_param)
    #col_metas = [ColMetaSchemaList.from_orm(db_obj) for db_obj in db_col_metas]

    # https://stackoverflow.com/a/61021183/6652082
    ta = TypeAdapter(List[ColMetaSchemaListBase])
    col_metas = ta.validate_python(db_col_metas)
    return dict(total=db_count, data=col_metas)

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
    ta = TypeAdapter(ColMetaPrivateDetail)
    col_metas = ta.validate_python(db_obj)
    return col_metas

@api_col_meta.put("/{id}", response_model=ColMetaSchema)
async def update(
        id: int, data: ColMetaCreate, db_session: Session=Depends(get_db_session)) -> Any:
    db_obj = await ColMeta.get(db_session, id)
    db_obj = await ColMeta.update(db_session, db_obj, **data.model_dump())
    db_session.add(db_obj)
    try:
        await db_session.commit()
    except Exception as e:
        err_text = traceback.format_exc()
        print(err_text)
    await db_session.refresh(db_obj)
    return db_obj.pydantic(ColMetaSchema)


@api_col_meta.post(
        "/", response_model=ColMetaSchema, status_code=status.HTTP_201_CREATED)
async def create(
        data: ColMetaSchema, db_session: Session = Depends(get_db_session)) -> Any:
    db_obj = ColMeta(**data.model_dump())
    db_session.add(db_obj)
    await db_session.commit()
    await db_session.refresh(db_obj)
    db_data = ColMetaSchema.model_validate(db_obj)
    return db_data
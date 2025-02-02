import traceback
from typing import Annotated, Any, List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session
from pydantic import TypeAdapter, parse_obj_as

from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.category_meta import CategoryMeta
from app.schemas.category_meta import CategoryMetaSchema, \
    CategoryMetaSchemaCreate, CategoryMetaSchemaUpdate, \
    CategoryMetaSchemaListBase, CategoryMetaPrivateDetail

from app.utils.common_param_utils import common_paging_param
from app.utils.common_param_utils import common_order_param
from . import api_category_meta

def category_meta_filter_param(
        id: str = "", name: str = "",
        ):
    return {"id": id, "name": name}

@api_category_meta.get("/")
async def list_obj(
        filter_param: Annotated[dict, Depends(category_meta_filter_param)],
        paging_param: Annotated[dict, Depends(common_paging_param)],
        order_param: Annotated[dict, Depends(common_order_param)],
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user),
        ) -> Any:
    
    db_count = await CategoryMeta.count(db_session, filter_param)
    db_category_metas = await CategoryMeta.listing(db_session, filter_param, order_param, paging_param)
    
    ta = TypeAdapter(List[CategoryMetaSchemaListBase])
    category_metas = ta.validate_python(db_category_metas)
    return dict(total=db_count, data=category_metas)

@api_category_meta.get("/user")
async def get_user_categorys(
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    filter_param = {"table_meta_id": 1}
    db_count = await CategoryMeta.count(db_session, filter_param)
    db_category_metas = await CategoryMeta.listing(db_session, filter_param, {}, {})
    ta = TypeAdapter(List[CategoryMetaSchemaListBase])
    category_metas = ta.validate_python(db_category_metas)
    return dict(total=db_count, data=category_metas)

@api_category_meta.get("/{id}")
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await CategoryMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    ta = TypeAdapter(CategoryMetaPrivateDetail)
    col_metas = ta.validate_python(db_obj)
    return col_metas

@api_category_meta.post("/", response_model=CategoryMetaSchema, 
        status_code=status.HTTP_201_CREATED)
async def create(
        data: CategoryMetaSchemaCreate, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = CategoryMeta(**data.model_dump())
    db_session.add(db_obj)
    await db_session.commit()
    await db_session.refresh(db_obj)
    db_data = CategoryMetaSchema.model_validate(db_obj)
    return db_data

@api_category_meta.put("/{id}")
async def put_obj(
        id: int, data: CategoryMetaSchemaUpdate, 
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await CategoryMeta.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    await CategoryMeta.update(db_session, db_obj, **data.dict())
    await db_session.commit()
    await db_session.refresh(db_obj)
    return db_obj.pydantic(CategoryMetaSchema)

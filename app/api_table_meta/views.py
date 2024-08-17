import traceback
from typing import Annotated
from typing import Any, List, Optional
from fastapi import Depends
from fastapi import status
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Integer

from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.table_meta import TableMeta
from app.schemas.table_meta import TableMetaSchema
from app.utils.common_param_utils import common_paging_param
from app.utils.common_param_utils import common_order_param

from . import api_table_meta

def col_meta_filter_param(
        id: str="", table_meta_id: str="", status: str="", col_meta: str="",
        data_type: str=""
        ):
    return {"id": id, "table_meta_id": table_meta_id,
        "status": status, "col_meta": col_meta,
        "data_type": data_type}

@api_table_meta.get("/")
async def list_obj(
        filter_param: Annotated[dict, Depends(col_meta_filter_param)],
        paging_param: Annotated[dict, Depends(common_paging_param)],
        order_param: Annotated[dict, Depends(common_order_param)],
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_count = await Person.count(db_session, filter_param)
    db_persons = await Person.listing(db_session, filter_param, order_param, paging_param)
    return dict(total=db_count, data=objs_to_schemas(db_persons, "pub"))


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

import copy
import json
import traceback
from typing import Annotated
from typing import Any, List, Optional
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import Depends
from fastapi import status
from fastapi import Query
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Integer

from pydantic import TypeAdapter

from config.db import get_db_session
from config.cache import get_extra_fields
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.user import User
from app.schemas.user import UserPublic, UserPublicList
from app.schemas.user import UserPrivate, UserPrivateList
from app.schemas.user import UserPrivateUpdate, UserPrivateCreate
from app.schemas.user import UserSignup
from app.utils import util
from app.utils.common_param_utils import common_paging_param
from app.utils.common_param_utils import common_order_param
from . import api_user, api_pub_user

def user_filter_param(id: str="", email: str="", 
        status: Optional[List[str]]=Query(None), user_role: Optional[List[str]]=Query(None),
        first_name: str="", last_name: str=""):
    return {"id": id, "email": email, "status": status, "user_role": user_role,
        "first_name": first_name, "last_name": last_name,
    }

async def user_extra(item_id: int):
    return {"item_id": item_id}

@api_pub_user.post(
        "/", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def create(
        data: UserPrivateCreate, db_session: Session = Depends(get_db_session)) -> Any:
    db_user = User(**data.model_dump())
    db_user.password_last_ets = func.now_ets()
    db_user.api_key = db_user.gen_api_key()
    db_user.api_key_last_ets = func.now_ets()
    db_session.add(db_user)
    try:
        await db_session.commit()
    except IntegrityError as err:
        if "user_email_key" in err.args[0]:
            raise ResError(
                status_code=409,
                err_code=ErrCode.EMAIL_DUPLICATED
            )
    await db_session.refresh(db_user)
    db_data = UserPrivate.model_validate(db_user)
    return db_data

@api_pub_user.post("/singup", response_model=UserPublic, 
        status_code=status.HTTP_201_CREATED)
async def singup_user(
        data: UserSignup, db_session: Session=Depends(get_db_session)) -> Any:
    db_user = User(**data.model_dump(exclude={'password'}))
    db_user.hash_password = User.gen_password_hash(data.password)
    db_user.password_last_ets = func.now_ets()
    db_user.api_key = db_user.gen_api_key()
    db_user.api_key_last_ets = func.now_ets()
    db_session.add(db_user)
    try:
        await db_session.commit()
    except IntegrityError as err:
        if "user_email_key" in err.args[0]:
            raise ResError(
                status_code=409,
                err_code=ErrCode.EMAIL_DUPLICATED
            )
    except Exception as e:
        err_text = traceback.format_exc()
        print(err_text)
    await db_session.refresh(db_user)
    return db_user.pydantic(UserPublic)

@api_pub_user.put("/{id}", response_model=UserPrivate, 
        status_code=status.HTTP_201_CREATED)
async def update(
        id: int, req_scheme: UserPrivateUpdate, request: Request,
        extra_fields: [] = Depends(get_extra_fields),
        db_session: Session=Depends(get_db_session)) -> Any:
    db_obj = await User.get(db_session, id)
    req_json = req_scheme.model_dump()
    data_jb = util.merge_selective_dict(
        db_obj.data_jb, req_json, "user_", extra_fields)
    req_json["data_jb"] = data_jb
    db_obj = await User.update(db_session, db_obj, **req_json)
    if "password" in req_scheme and req_scheme.password:
        db_obj.hash_password = User.gen_password_hash(req_scheme.password)
        db_obj.password_last_ets = func.now_ets()
    db_session.add(db_obj)
    try:
        await db_session.commit()
    except IntegrityError as err:
        if "user_email_key" in err.args[0]:
            raise ResError(
                status_code=409,
                err_code=ErrCode.EMAIL_DUPLICATED
            )
    except Exception as e:
        err_text = traceback.format_exc()
        print(err_text)
    await db_session.refresh(db_obj)
    return db_obj.pydantic(UserPrivate)


@api_user.get("/{id}", response_model=UserPrivate)
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session),
        extra_fields: [] = Depends(get_extra_fields),
        _ = Depends(get_current_active_user)
        ) -> Any:
    db_user = await User.get(db_session, id)
    if db_user is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    context = {"extra_fields": extra_fields}
    ret_model = UserPrivate.model_validate(db_user, context=context)
    ret_json = ret_model.model_dump()
    ret = JSONResponse(content=ret_json)
    return ret

@api_user.get("/")
async def list_user(
        request: Request,
        filter_param: Annotated[dict, Depends(user_filter_param)],
        paging_param: Annotated[dict, Depends(common_paging_param)],
        order_param: Annotated[dict, Depends(common_order_param)],
        db_session: Session = Depends(get_db_session),
        
        _ = Depends(get_current_active_user)) -> Any:
    db_count = await User.count(db_session, filter_param)
    db_users = await User.listing(db_session, filter_param, order_param, paging_param)

    extra_field_str = request.app.cache.get("user_define.user")
    extra_field_info = json.loads(extra_field_str)
    extra_fields = extra_field_info["code"].keys()
    return dict(total=db_count, data=objs_to_schemas(db_users, "pri", extra_fields))


@api_user.get("/me/", response_model=UserPrivate)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


UserPubList = TypeAdapter(List[UserPublic]) 
UserPriList = TypeAdapter(List[UserPrivate]) 
def objs_to_schemas(db_users, share_type, extra_fields):
    context = {"extra_fields": extra_fields}
    ta = None
    if share_type == "pub":
        ta = UserPubList
    elif share_type == "pri":
        ta = UserPriList
    else:
        raise
    return ta.validate_python(db_users, context=context)

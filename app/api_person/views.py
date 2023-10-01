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

from pydantic import parse_obj_as

from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.person import Person
from app.schemas.person import UserPublic, UserPublicList
from app.schemas.user import UserPrivate, UserPrivateList
from app.schemas.user import UserCreate
from app.schemas.user import UserSignup
from app.utils.common_param_utils import common_paging_param
from app.utils.common_param_utils import common_order_param
from . import api_user, api_pub_user

def person_filter_param(
        id: str = "", first_name: str = "", last_name: str = "",
        phone: str = "", email: str = ""
        ):
    return {"id": id, "first_name": first_name, "last_name": last_name,
        "phone": phone, "email": email}

@api_pub_user.post(
        "/", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def create_user(
        data: UserCreate, db_session: Session = Depends(get_db_session)) -> Any:
    db_user = User(**data.dict())
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
    return db_user.pydantic(UserPublic)

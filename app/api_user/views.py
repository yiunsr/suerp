import traceback
from typing import Any, List
from fastapi import Depends
from fastapi import status
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from pydantic import parse_obj_as

from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.user import User
from app.schemas.user import UserPublic
from app.schemas.user import UserPrivate
from app.schemas.user import UserCreate
from app.schemas.user import UserSignup
from . import api_user, api_pub_user

@api_pub_user.post(
        "/", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def create_user(
        data: UserCreate, db_session: Session = Depends(get_db_session)) -> Any:
    db_user = User(**data.dict())
    db_user.password_last_at = func.now()
    db_user.api_key = db_user.gen_api_key()
    db_user.api_key_last_at = func.now()
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

@api_pub_user.post("/singup", response_model=UserPublic, 
        status_code=status.HTTP_201_CREATED)
async def singup_user(
        data: UserSignup, db_session: Session=Depends(get_db_session)) -> Any:
    db_user = User(**data.dict(exclude={'password'}))
    db_user.hash_password = User.gen_password_hash(data.password)
    db_user.password_last_at = func.now()
    db_user.api_key = db_user.gen_api_key()
    db_user.api_key_last_at = func.now()
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
    return db_user.pydantic(UserPublic)

@api_user.get("/{id}", response_model=UserPublic)
async def get_user(
        id: int, db_session: Session = Depends(get_db_session)) -> Any:
    db_user = await User.get(db_session, id)
    if db_user is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return UserPublic.from_orm(db_user)

@api_user.get("/", response_model=(List[UserPrivate] | List[UserPublic]))
async def list_user(db_session: Session = Depends(get_db_session)) -> Any:
    db_users = await User.listing(db_session)
    # return parse_obj_as(List[UserPublic], db_users)
    return parse_users_as(db_users, "pri")

@api_user.get("/me/", response_model=UserPrivate)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

def parse_users_as(db_users, share_type):
    results = []
    for db_user in db_users:
        if share_type == "pub":
            item = parse_obj_as(UserPublic, db_user)
        elif share_type == "pri":
            item = parse_obj_as(UserPrivate, db_user)
        results.append(item)
    return results

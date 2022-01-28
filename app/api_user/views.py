from typing import Any, List
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from pydantic import parse_obj_as

from config.db import get_session
from app.models.user import User
from app.schemas.user import UserSimple
from app.schemas.user import UserCreate
from app.app_utils import get_token_header
from . import api_user, api_pub_user

@api_pub_user.post("/", response_model=UserSimple)
async def create_user(
        data: UserCreate, session: Session = Depends(get_session)) -> Any:
    db_user = User(**data.dict())
    db_user.password_last_at = func.now()
    db_user.api_key = db_user.gen_api_key()
    db_user.api_key_last_at = func.now()
    session.add(db_user)
    await session.commit()
    return db_user.pydantic(UserSimple)

@api_user.get("/{id}", response_model=UserSimple)
async def get_user(
        id: int, session: Session = Depends(get_session)) -> Any:
    db_user = await User.get(session, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return UserSimple.from_orm(db_user)

@api_user.get("/", response_model=List[UserSimple])
async def list_user(session: Session = Depends(get_session)) -> Any:
    db_users = await User.listing(session)
    return parse_obj_as(List[UserSimple], db_users)

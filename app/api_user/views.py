from typing import Any, List
from fastapi import Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from config.db import get_session
from app.models.user import User
from app.schemas.user import UserResDetail
from app.schemas.user import UserCreate
from app.app_utils import get_token_header
from . import api_user

@api_user.post("/", response_model=UserResDetail)
async def create_user(
        data: UserCreate, session: Session = Depends(get_session)) -> Any:
    db_user = User(**data.dict())
    db_user.password_last_at = func.now()
    session.add(db_user)
    await session.commit()
    return db_user.pydantic(UserResDetail)

@api_user.get("/{id}", response_model=UserResDetail)
async def get_user(
        id: int, session: Session = Depends(get_session)) -> Any:
    db_user = await User.get(session, id)
    return db_user.pydantic(UserResDetail)

from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

from config import get_config
from config.auth import create_access_token
from config.auth import authenticate_user
from config.db import get_db_session
from app.models.user import User
from app.schemas.token import Token
from app.schemas.token import TokenClientSecret
from . import api_auth


@api_auth.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Union[
            OAuth2PasswordBearer, OAuth2PasswordRequestForm ]=Depends(),
        # form_data: OAuth2PasswordRequestForm = Depends(),
        db_session: Session=Depends(get_db_session)):
    user = await authenticate_user(
        db_session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    app_config = get_config()
    access_token_expire_minutes = app_config.ACCESS_TOKEN_EXPIRE_MINUTES
    access_token_expires = timedelta(minutes=access_token_expire_minutes)
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


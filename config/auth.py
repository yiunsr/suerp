from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from config import get_config
from config.db import get_db_session
from app.schemas.token import TokenData
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    app_config = get_config()
    secret_token = app_config.SECRET_KEY
    algorithm = app_config.ALGORITHM

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_token, algorithm=algorithm)
    return encoded_jwt


async def get_current_user(
        db_session: Session = Depends(get_db_session),
        token: str = Depends(oauth2_scheme)):
    app_config = get_config()
    secret_token = app_config.SECRET_KEY
    algorithm = app_config.ALGORITHM

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret_token, algorithms=[algorithm])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = await User.get_by_email(db_session, email)
    if user is None:
        raise credentials_exception
    return user

async def authenticate_user(db_session: Session, email: str, password: str,
        token: str=Depends(oauth2_scheme)):
    user = await User.get_by_email(db_session, email)
    if not user:
        return False
    if not user.check_password(password):
        return False
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.status == 'A':
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
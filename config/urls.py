from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Header


def init_app(app):
    from app.main import main
    from app.api_user import api_pub_user, api_user
    from app.auth import auth

    app.include_router(main)
    app.include_router(api_pub_user)
    app.include_router(api_user)
    app.include_router(auth)

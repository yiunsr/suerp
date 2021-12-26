from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Header


def init_app(app):
    from app.main import main

    app.include_router(main)


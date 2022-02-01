from fastapi import APIRouter
from fastapi import Depends

api_pub_user = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

api_user = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

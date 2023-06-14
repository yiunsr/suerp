from fastapi import APIRouter
from fastapi import Depends

api_auth = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

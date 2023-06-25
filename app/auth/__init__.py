from fastapi import APIRouter
from fastapi import Depends

auth = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

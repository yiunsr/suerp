from fastapi import APIRouter
from fastapi import Depends

api_table_meta = APIRouter(
    prefix="/table_meta",
    tags=["table_metas"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

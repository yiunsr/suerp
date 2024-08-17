from fastapi import APIRouter
from fastapi import Depends

api_table_meta = APIRouter(
    prefix="/api/table_metas",
    tags=["table_metas"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

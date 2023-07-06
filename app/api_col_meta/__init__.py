from fastapi import APIRouter

api_col_meta = APIRouter(
    prefix="/col_meta",
    tags=["col_metas"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

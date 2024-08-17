from fastapi import APIRouter

api_col_meta = APIRouter(
    prefix="/api/col_metas",
    tags=["col_metas"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

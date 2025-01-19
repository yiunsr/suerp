from fastapi import APIRouter

api_cate_meta = APIRouter(
    prefix="/api/cate_metas",
    tags=["cate_metas"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

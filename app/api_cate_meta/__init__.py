from fastapi import APIRouter

api_cate_meta = APIRouter(
    prefix="/cate_meta",
    tags=["cate_metas"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

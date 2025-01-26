from fastapi import APIRouter

api_category_meta = APIRouter(
    prefix="/api/category_metas",
    tags=["category_metas"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

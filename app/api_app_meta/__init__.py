from fastapi import APIRouter

api_app_meta = APIRouter(
    prefix="/app_meta",
    tags=["app_meta"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

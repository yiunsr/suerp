from fastapi import APIRouter
from fastapi import Depends

api_product = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

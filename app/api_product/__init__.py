from fastapi import APIRouter
from fastapi import Depends
from app.app_utils import get_token_header

api_product = APIRouter(
    prefix="/products",
    tags=["products"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

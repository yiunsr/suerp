from fastapi import APIRouter
from fastapi import Depends
from app.app_utils import get_token_header

main = APIRouter(
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

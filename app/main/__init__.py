from fastapi import APIRouter
from fastapi import Depends

main = APIRouter(
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

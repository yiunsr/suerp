from fastapi import APIRouter
from fastapi import Depends

# api_pub_person = APIRouter(
#     prefix="/api/persons",
#     tags=["persons"],
#     responses={404: {"description": "Not found"}},
# )

api_person = APIRouter(
    prefix="/api/persons",
    tags=["persons"],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

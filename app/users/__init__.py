from fastapi import APIRouter
from fastapi import Depends

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

from fastapi import APIRouter
# from fastapi import Depends
# from app.app_utils import get_token_header

api_user = APIRouter(
    prefix="/users",
    tags=["users"],
#     dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

from . import views # noqa

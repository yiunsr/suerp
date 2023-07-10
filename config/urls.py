from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Header


def init_app(app):
    from app.main import main
    from app.api_user import api_pub_user, api_user
    from app.api_app_meta import api_app_meta
    from app.api_table_meta import api_table_meta
    from app.api_col_meta import api_col_meta
    from app.api_cate_meta import api_cate_meta
    from app.auth import auth

    app.include_router(main)
    app.include_router(api_pub_user)
    app.include_router(api_user)
    app.include_router(api_app_meta)
    app.include_router(api_table_meta)
    app.include_router(api_col_meta)
    app.include_router(api_cate_meta)
    app.include_router(auth)

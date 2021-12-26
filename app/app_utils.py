from fastapi import Header
from fastapi import HTTPException

from config import get_config

async def get_token_header(x_token: str = Header(...)):
    app_config = get_config()
    super_secret_token = app_config.get_super_secret_token()
    if x_token != super_secret_token:
        raise HTTPException(status_code=400, detail="X-Token header invalid")

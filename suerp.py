import os
import uvicorn

from app import create_app

import sys
import asyncio

if sys.platform.startswith('win'):
  	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

FASTAPI_CONFIG = os.getenv('FASTAPI_CONFIG') or 'default'

application = create_app(FASTAPI_CONFIG)


@application.get("/tt")
def root():
    return {"url": "/tt" }


if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8070)

from enum import Enum, auto
from fastapi import Request
from fastapi.responses import JSONResponse

class ErrCode(Enum):
    NO_ERROR = 0
    EMAIL_DUPLICATED = auto()
    NO_ITEM = auto()

ErrDict = {
    ErrCode.NO_ERROR: "정상",
    ErrCode.EMAIL_DUPLICATED: "동일한 이메일이 존재합니다.",
    ErrCode.NO_ITEM: "해당 항목이 존재하지 않습니다. ",
}


class ResError(Exception):
    status_code = 0
    err_code = ErrCode.NO_ERROR
    def __init__(self, status_code: int, err_code: ErrCode):
        self.status_code = status_code
        self.err_code = err_code

def init_app(app):
    @app.exception_handler(ResError)
    async def exception_handler(request: Request, err: ResError):
        content = {
            "err_code": err.err_code.name,
            "detail": ErrDict[err.err_code],
        }
        return JSONResponse(
            status_code=err.status_code,
            content=content,
        )

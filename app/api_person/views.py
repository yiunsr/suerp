import traceback
from typing import Annotated
from typing import Any, List, Optional
from fastapi import Depends
from fastapi import status
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Integer

from pydantic import parse_obj_as

from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.person import Person
from app.schemas.person import PersonPublic
from app.utils.common_param_utils import common_paging_param
from app.utils.common_param_utils import common_order_param
from . import api_person

def person_filter_param(
        id: str = "", name: str = "",
        first_name: str = "", last_name: str = "",
        phone: str = "", email: str = ""
        ):
    return {"id": id, "name": name,
        "first_name": first_name, "last_name": last_name,
        "phone_jb": phone, "email_jb__in": email}

@api_person.post(
        "/", response_model=PersonPublic, status_code=status.HTTP_201_CREATED)
async def create_user(
        data: PersonPublic, db_session: Session = Depends(get_db_session)) -> Any:
    db_person = Person(**data.dict())
    db_session.add(db_person)
    # try:
    #     await db_session.commit()
    # except IntegrityError as err:
    #     if "user_email_key" in err.args[0]:
    #         raise ResError(
    #             status_code=409,
    #             err_code=ErrCode.EMAIL_DUPLICATED
    #         )
    return db_person.pydantic(PersonPublic)

@api_person.get("/")
async def list_user(
        filter_param: Annotated[dict, Depends(person_filter_param)],
        paging_param: Annotated[dict, Depends(common_paging_param)],
        order_param: Annotated[dict, Depends(common_order_param)],
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_count = await Person.count(db_session, filter_param)
    db_persons = await Person.listing(db_session, filter_param, order_param, paging_param)
    return dict(total=db_count, data=parse_person_as(db_persons, "pub"))

def parse_person_as(db_persons, share_type):
    results = []
    for db_person in db_persons:
        if share_type == "pub":
            item = parse_obj_as(PersonPublic, db_person)
        else:
            raise
        results.append(item)
    return results

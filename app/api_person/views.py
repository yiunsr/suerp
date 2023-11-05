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


from config.db import get_db_session
from config.http_err import ErrCode
from config.http_err import ResError
from config.auth import get_current_active_user
from app.models.person import Person
from app.schemas.person import PersonPublic, PersonPrivate
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
async def create(
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
async def list_obj(
        filter_param: Annotated[dict, Depends(person_filter_param)],
        paging_param: Annotated[dict, Depends(common_paging_param)],
        order_param: Annotated[dict, Depends(common_order_param)],
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_count = await Person.count(db_session, filter_param)
    db_persons = await Person.listing(db_session, filter_param, order_param, paging_param)
    return dict(total=db_count, data=parse_person_as(db_persons, "pub"))

@api_person.get("/{id}", response_model=PersonPrivate)
async def get_obj(
        id: int, db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_obj = await Person.get(db_session, id)
    if db_obj is None:
        raise ResError(
                status_code=404,
                err_code=ErrCode.NO_ITEM
            )
    return PersonPrivate.model_validate(db_obj)

def parse_person_as(db_persons, share_type):
    results = []
    for db_person in db_persons:
        if share_type == "pub":
            item = PersonPublic.model_validate(db_person)
        elif share_type == "pri":
            item = PersonPrivate.model_validate(db_person)
        else:
            raise
        results.append(item)
    return results

# @api_person.post("/")
# async def add_user(
#         person_add_param: Annotated[dict, Depends(person_add_param)],
#         db_session: Session = Depends(get_db_session),
#         _ = Depends(get_current_active_user)) -> Any:
#     db_person = await Person.insert(db_session, person_add_param)
#     data = parse_obj_as(PersonPublic, db_person)
#     return data

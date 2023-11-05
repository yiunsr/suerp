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
from app.schemas.person import PersonPrivateCreate, PersonPrivateUpdate
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

@api_person.get("/")
async def list_obj(
        filter_param: Annotated[dict, Depends(person_filter_param)],
        paging_param: Annotated[dict, Depends(common_paging_param)],
        order_param: Annotated[dict, Depends(common_order_param)],
        db_session: Session = Depends(get_db_session),
        _ = Depends(get_current_active_user)) -> Any:
    db_count = await Person.count(db_session, filter_param)
    db_persons = await Person.listing(db_session, filter_param, order_param, paging_param)
    return dict(total=db_count, data=objs_to_schemas(db_persons, "pub"))

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


@api_person.post(
        "/", response_model=PersonPrivate, status_code=status.HTTP_201_CREATED)
async def create(
        data: PersonPrivateCreate, db_session: Session = Depends(get_db_session)) -> Any:
    db_obj = Person(**data.model_dump())
    db_session.add(db_obj)
    await db_session.commit()
    await db_session.refresh(db_obj)
    db_data = PersonPrivate.model_validate(db_obj)
    return db_data


@api_person.put("/{id}", response_model=PersonPrivate)
async def update(
        id: int, data: PersonPrivateUpdate, db_session: Session=Depends(get_db_session)) -> Any:
    db_obj = await Person.get(db_session, id)
    db_obj = await Person.update(db_session, db_obj, **data.model_dump())
    db_session.add(db_obj)
    try:
        await db_session.commit()
    except Exception as e:
        err_text = traceback.format_exc()
        print(err_text)
    await db_session.refresh(db_obj)
    return db_obj.pydantic(PersonPrivate)


def objs_to_schemas(db_users, share_type):
    results = []
    for db_user in db_users:
        if share_type == "pub":
            item = PersonPublic.model_validate(db_user)
        elif share_type == "pri":
            item = PersonPrivate.model_validate(db_user)
        else:
            raise
        results.append(item)
    return results

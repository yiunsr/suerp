import click
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from app.models.user import User
from app.models.table_meta import TableMeta

from .cli_utils import get_db_session
from .cli_utils import add_user, add_person
from .cli_utils import get_app_meta

async def script(config):
    click.echo('== start _init_test_user ==')
    SessionLocal = get_db_session(config)

    app_id = None
    async with SessionLocal() as db_session:
        param = {"name": "default", "detail": "기본앱"}
        default_app = await get_app_meta(db_session, "default")
        app_id = default_app.id

    async with SessionLocal() as db_session:
        await add_test_user(db_session)
        await db_session.commit()
    
    async with SessionLocal() as db_session:
        await add_test_person(db_session)
        await db_session.commit()
    
    # async with SessionLocal() as db_session:
    #     await add_test_org(db_session)
    #     await db_session.commit()


async def add_test_user(db_session):
    param = {"email": "manager0001@test.com", "display": "manager0001",
        "first_name": "first0001", "last_name": "last0001", "status": "S",
        "user_role": "M", "password": "man_0001"}
    await add_user(db_session, param)

    param = {"email": "manager0002@test.com", "display": "manager0002",
        "first_name": "first0002", "last_name": "last0002", "status": "S",
        "user_role": "M", "password": "man_0002"}
    await add_user(db_session, param)

    param = {"email": "manager0003@test.com", "display": "manager0003",
        "first_name": "first0003", "last_name": "last0003", "status": "A",
        "user_role": "M", "password": "man_0003"}

    param = {"email": "manager0004@test.com", "display": "manager0004",
        "first_name": "first0004", "last_name": "last0004", "status": "A",
        "user_role": "M", "password": "man_0004"}
    await add_user(db_session, param)

    param = {"email": "tester0005@test.com", "display": "tester0005",
        "first_name": "first0005", "last_name": "last0005", "status": "A",
        "user_role": "N", "password": "test_0005"}
    await add_user(db_session, param)

    param = {"email": "tester0006@test.com", "display": "tester0006",
        "first_name": "first0006", "last_name": "last0006", "status": "A",
        "user_role": "N", "password": "test_0006"}
    await add_user(db_session, param)

    param = {"email": "tester0007@test.com", "display": "tester0007",
        "first_name": "first0007", "last_name": "last0007", "status": "A",
        "user_role": "N", "password": "test_0007"}
    await add_user(db_session, param)

    param = {"email": "tester0008@test.com", "display": "tester0008",
        "first_name": "first0008", "last_name": "last0008", "status": "A",
        "user_role": "N", "password": "test_0008"}
    await add_user(db_session, param)

    param = {"email": "tester0009@test.com", "display": "tester0009",
        "first_name": "first0009", "last_name": "last0009", "status": "A",
        "user_role": "N", "password": "test_0009"}
    await add_user(db_session, param)

    param = {"email": "tester0010@test.com", "display": "tester0010",
        "first_name": "first0010", "last_name": "last0010", "status": "A",
        "user_role": "N", "password": "test_0010"}
    await add_user(db_session, param)
    click.echo('== end _init_test_user ==')

async def add_test_person(db_session):
    email_jb = [{"type": "work", "value":"test0001@test.work"},
        {"value":"test0001@test.kr", "type": "home"}]
    param = {"display": "person0001", "first_name": "first0001",
        "last_name": "last0001", "status": "A", "email_jb": email_jb,
        "created_user_id":1, "updated_user_id":1}
    await add_person(db_session, param)

    email_jb = [{"type": "work", "value":"test0002@test.work"},
        {"value":"test0002@test.kr", "type": "home"}]
    param = {"display": "person0002", "first_name": "first0002",
        "last_name": "last0002", "status": "A", "email_jb": email_jb,
        "created_user_id":1, "updated_user_id":1}
    await add_person(db_session, param)

    email_jb = [{"type": "work", "value":"test0003@test.work"},
        {"value":"test0003@test.kr", "type": "home"}]
    param = {"display": "person0003", "first_name": "first0003",
        "last_name": "last0003", "status": "A", "email_jb": email_jb,
        "created_user_id":1, "updated_user_id":1}
    await add_person(db_session, param)

    phone_jb = [{"type":"work", "value":"010-0000-0004",},
        {"type":"home", "value":"010-0001-0004"}]
    param = {"display": "person0004", "first_name": "first0004",
        "last_name": "last0004", "status": "A", "phone_jb": phone_jb,
        "created_user_id":1, "updated_user_id":1}
    await add_person(db_session, param)

    phone_jb = [{"type":"work", "value":"010-0000-0005",},
        {"type":"home", "value":"010-0001-0005"}]
    param = {"display": "person0005", "first_name": "first0005",
        "last_name": "last0005", "status": "A", "phone_jb": phone_jb,
        "created_user_id":1, "updated_user_id":1}
    await add_person(db_session, param)

    phone_jb = [{"type":"work", "value":"010-0000-0006"},
        {"type":"home", "value":"010-0001-0006"}]
    param = {"display": "person0006", "first_name": "first0006",
        "last_name": "last0006", "status": "A", "phone_jb": phone_jb,
        "created_user_id":1, "updated_user_id":1}
    await add_person(db_session, param)


# async def add_test_org(db_session):
#     email_jb = [{"type": "work", "value":"test0001@test.work"},
#         {"type": "home", "value":"test0001@test.org"}]
#     param = {"name": "person0001", "first_name": "first0001",
#         "last_name": "last0001", "status": "A", "email_jb": email_jb,
#         "created_user_id": 1, "updated_user_id": 1}
#     await add_person(db_session, param)

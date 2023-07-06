import click
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from app.models.user import User
from app.models.table_meta import TableMeta

def get_db_session(config):
    DATABASE_URL = config.DATABASE_URI
    engine = create_async_engine(DATABASE_URL, future=True, echo=True)
    SessionLocal = sessionmaker(
        engine, expire_on_commit=True, class_=AsyncSession)
    return SessionLocal

async def _add_user(db_session, data):
    query = select(User).where(User.email==data["email"])
    result = await db_session.execute(query)
    db_user = result.scalars().first()
    if db_user:
        return
    password = data.get("password")
    if password:
        del data["password"]
    db_user = User(**data)
    if password:
        db_user.hash_password = User.gen_password_hash(password)
    db_user.password_last_ets = func.now_ets()
    db_user.api_key = db_user.gen_api_key()
    db_user.api_key_last_ets = func.now_ets()
    db_session.add(db_user)


async def script(config):
    click.echo('== start _init_test_user ==')
    SessionLocal = get_db_session(config)
    async with SessionLocal() as db_session:
        param = dict(email="manager0001@test.com", name="manager0001",
            first_name="first0001", last_name="last0001", status="S", 
            user_role="M", password="man_0001")
        await _add_user(db_session, param)

        param = dict(email="manager0002@test.com", name="manager0002",
            first_name="first0002", last_name="last0002", status="S", 
            user_role="M", password="man_0002")
        await _add_user(db_session, param)

        param = dict(email="manager0003@test.com", name="manager0003",
            first_name="first0003", last_name="last0003", status="S", 
            user_role="M", password="man_0003")
        await _add_user(db_session, param)

        param = dict(email="manager0004@test.com", name="manager0004",
            first_name="first0004", last_name="last0004", status="S", 
            user_role="M", password="man_0004")
        await _add_user(db_session, param)

        param = dict(email="tester0005@test.com", name="tester0005",
            first_name="first0005", last_name="last0005", status="S", 
            user_role="N", password="test_0005")
        await _add_user(db_session, param)

        param = dict(email="tester0006@test.com", name="tester0006",
            first_name="first0006", last_name="last0006", status="S", 
            user_role="N", password="test_0006")
        await _add_user(db_session, param)

        param = dict(email="tester0007@test.com", name="tester0007",
            first_name="first0007", last_name="last0007", status="S", 
            user_role="N", password="test_0007")
        await _add_user(db_session, param)

        param = dict(email="tester0008@test.com", name="tester0008",
            first_name="first0008", last_name="last0008", status="S", 
            user_role="N", password="test_0008")
        await _add_user(db_session, param)
        
        await db_session.commit()
    click.echo('== end _init_test_user ==')

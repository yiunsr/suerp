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

async def _add_table_meta(db_session, data):
    query = select(TableMeta).where(TableMeta.code==data["code"])
    result = await db_session.execute(query)
    db_table_meta = result.scalars().first()
    if db_table_meta:
        return
    db_table_meta = TableMeta(**data)
    db_session.add(db_table_meta)

async def script(config):
    click.echo('== start init_db script ==')
    print("== start init_db script ==")
    SessionLocal = get_db_session(config)
    async with SessionLocal() as db_session:
        param = dict(email="system@system.system", name="system",
            first_name="system", last_name="system", status="S", 
            user_role="M")
        await _add_user(db_session, param)

        param = dict(email="readonly@system.system", name="readonly",
            first_name="systemreadonly", last_name="systemreadonly", 
            status="S", user_role="M")
        await _add_user(db_session, param)

        param = dict(email="api@system.system", name="api",
            first_name="api", last_name="api", 
            status="S", user_role="M")
        await _add_user(db_session, param)

        await db_session.commit()

    async with SessionLocal() as db_session:
        param = dict(code="user", name_lang_jb=dict(ko="사용자", en="user"), 
            detail="로그인 가능한 관리 유저")
        await _add_table_meta(db_session, param)

        param = dict(code="ugroup", name_lang_jb=dict(
            ko="사용자그룹", en="usergroup"),  detail="user 의 그룹")
        await _add_table_meta(db_session, param)

        param = dict(code="user_ugroup", name_lang_jb=dict(
            ko="사용자-사용자그룹", en="user-usergroup"), 
            detail="user 와 ugroup 의 M:N 연결을 위한 테이블")
        await _add_table_meta(db_session, param)

        param = dict(code="per", name_lang_jb=dict(
            ko="사람", en="person"),  
            detail="인명(고객, 소비자, 생산업체 직원 등)")
        await _add_table_meta(db_session, param)

        param = dict(code="org", name_lang_jb=dict(
            ko="조직", en="organization"),  
            detail="person 의 그룹.  회사, 법인, 학교 같은 인명의 조직")
        await _add_table_meta(db_session, param)

        param = dict(code="per_org", name_lang_jb=dict(
            ko="인명-조직", en="person-organization"), 
            detail="person 와 organization 의 M:N 연결을 위한 테이블")
        await _add_table_meta(db_session, param)

        param = dict(code="permission", name_lang_jb=dict(
            ko="권한", en="perm"), 
            detail="권한. user 들의 데이터 접속을 허용하거나 제한할 때 사용하는 권한 종류들")
        await _add_table_meta(db_session, param)

        await db_session.commit()

    click.echo('== end start init_db script ==')
    print("== end start init_db script ==")

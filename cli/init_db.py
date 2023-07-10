import click

from app.models.user import User
from app.models.app_meta import AppMeta
from app.models.table_meta import TableMeta

from .cli_utils import get_db_session
from .cli_utils import add_app_meta
from .cli_utils import get_app_meta
from .cli_utils import add_user
from .cli_utils import add_table_meta


async def script(config):
    click.echo('== start init_db script ==')
    print("== start init_db script ==")
    SessionLocal = get_db_session(config)

    app_id = None
    async with SessionLocal() as db_session:
        param = dict(name="default", detail="기본앱", )
        await add_app_meta(db_session, param)
        await db_session.commit()
        # default_app = await get_app_meta(db_session, "default")
        # app_id = default_app.id

    async with SessionLocal() as db_session:
        param = dict(email="system@system.system", name="system",
            first_name="system", last_name="system", status="S", 
            user_role="M")
        await add_user(db_session, param)

        param = dict(email="readonly@system.system", name="readonly",
            first_name="systemreadonly", last_name="systemreadonly", 
            status="S", user_role="M")
        await add_user(db_session, param)

        param = dict(email="api@system.system", name="api",
            first_name="api", last_name="api", 
            status="S", user_role="M")
        await add_user(db_session, param)
        await db_session.commit()

    async with SessionLocal() as db_session:
        param = dict(code="user", name_lang_jb=dict(ko="사용자", en="user"), 
            detail="로그인 가능한 관리 유저")
        await add_table_meta(db_session, param)

        param = dict(code="ugroup", name_lang_jb=dict(
            ko="사용자그룹", en="usergroup"),  detail="user 의 그룹")
        await add_table_meta(db_session, param)

        param = dict(code="user_ugroup", name_lang_jb=dict(
            ko="사용자-사용자그룹", en="user-usergroup"), 
            detail="user 와 ugroup 의 M:N 연결을 위한 테이블")
        await add_table_meta(db_session, param)

        param = dict(code="per", name_lang_jb=dict(
            ko="사람", en="person"),  
            detail="인명(고객, 소비자, 생산업체 직원 등)")
        await add_table_meta(db_session, param)

        param = dict(code="org", name_lang_jb=dict(
            ko="조직", en="organization"),  
            detail="person 의 그룹.  회사, 법인, 학교 같은 인명의 조직")
        await add_table_meta(db_session, param)

        param = dict(code="per_org", name_lang_jb=dict(
            ko="인명-조직", en="person-organization"), 
            detail="person 와 organization 의 M:N 연결을 위한 테이블")
        await add_table_meta(db_session, param)

        param = dict(code="permission", name_lang_jb=dict(
            ko="권한", en="perm"), 
            detail="권한. user 들의 데이터 접속을 허용하거나 제한할 때 사용하는 권한 종류들")
        await add_table_meta(db_session, param)

        param = dict(code="app_meta", name_lang_jb=dict(ko="앱", en="app"), 
            detail="app 정보")
        await add_table_meta(db_session, param)

        param = dict(code="table_meta", name_lang_jb=dict(ko="테이블 메타", en="table meta"), 
            detail="테이블 정보")
        await add_table_meta(db_session, param)

        param = dict(code="col_meta", name_lang_jb=dict(ko="컬럼 메타", en="column meta"), 
            detail="테이블 정보")
        await add_table_meta(db_session, param)

        param = dict(code="cate_meta", name_lang_jb=dict(ko="카테고리 메타", en="category meta"), 
            detail="테이블내 카테고리 정보")
        await add_table_meta(db_session, param)

        await db_session.commit()

    click.echo('== end start init_db script ==')
    print("== end start init_db script ==")

import click
import asyncio
import sys

from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from config import get_config
from app.models.user import User
from app.models.table_meta import TableMeta

from cli.init_system_db import script as init_system_db_script
from cli.init_test_db import script as init_test_db_script

config = get_config()
server_type = config.SERVER_TYPE
DATABASE_URL = config.DATABASE_URI

@click.group()
def cli():
    pass

def get_db_session():
    engine = create_async_engine(DATABASE_URL, future=True, echo=True)
    SessionLocal = sessionmaker(
        engine, expire_on_commit=True, class_=AsyncSession)
    return SessionLocal

@click.command()
def init_system_db():
    click.echo('==== start init_system_db ====')
    py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
    if py_ver > 37 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(init_system_db_script(config))
    click.echo('==== end initdb ====')

@click.command()
def init_test_db():
    click.echo('==== start init-test-db ====')
    py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
    if py_ver > 37 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(init_test_db_script(config))
    click.echo('==== end init-test-db ====')

cli.add_command(init_system_db)
cli.add_command(init_test_db)

if __name__ == '__main__':
    cli()

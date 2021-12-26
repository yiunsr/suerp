import os
import sys
import asyncio
import debugpy

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context
from alembic.config import Config

# debugpy.listen(5678)
# print("Waiting for debugger attach")
# debugpy.wait_for_client()
# debugpy.breakpoint()
# print('break on this line')
# print("==== start alembic ==")

# https://stackoverflow.com/a/66772223/6652082
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
 
from config.db import Base
from app import create_app

try:
    config = context.config  # noqa
except Exception:
    ini_path = os.path.join(
         os.path.dirname(
             os.path.abspath(__file__)), "../alembic.ini")
    ini_path = os.path.abspath(ini_path)
    config = Config(ini_path)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# https://gist.github.com/utek/6163250
def exclude_tables_from_config(config_):
    tables_ = config_.get("tables", None)
    if tables_ is not None:
        tables = tables_.split(",")
    else:
        tables = []
    new_tables = []
    for table in tables:
        table = table.strip()
        new_tables.append(table)
    return new_tables

# [alembic:exclude]
# table_col = products.create_at, users.updated_at
def exclude_colum_from_config(config_):
    columns_ = config_.get("table_col")
    if columns_ is not None:
            columns = columns_.split(",")
    else:
        columns = []
    new_columns = []
    for column in columns:
        column = column.strip()
        new_columns.append(column)
    return new_columns

        
exclude_tables = exclude_tables_from_config(config.get_section('alembic:exclude'))
exclude_table_cols = exclude_colum_from_config(config.get_section('alembic:exclude'))

def include_object(object, name, type_, *args, **kwargs):
    ret_table = not (type_ == 'table' and name in exclude_tables)
    ret_col = not (type_ == 'column' and name in exclude_table_cols)
    return ret_table and ret_col


application = create_app(os.getenv('FASTAPI_CONFIG') or 'default')
target_metadata = Base.metadata


def get_url():
    global application
    url = application.config['DATABASE_URI']
    return url

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    print("offline mode")
    global configure
    url = get_url()
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True,
        include_object=include_object,
        dialect_opts={"paramstyle": "named"})

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(
        connection=connection, target_metadata=target_metadata,
        include_object=include_object)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    print("online mode")
    url = get_url()
    # connectable = AsyncEngine(
    #     engine_from_config(
    #         config,
    #         url=url,
    #         prefix="sqlalchemy.",
    #         poolclass=pool.NullPool,
    #         future=True,
    #     )
    # )
    connectable = create_async_engine(url, future=True, echo=True)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

if __name__ == '__main__':
    # run_migrations_offline()
    asyncio.run(run_migrations_online())
else:
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        asyncio.run(run_migrations_online())

print("==== end alembic ==")

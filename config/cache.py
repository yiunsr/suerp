import redis
import json
from fastapi import Depends
from fastapi import Request
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from app.models.col_meta import ColMeta
from config.db import get_db_session

def init_app(app):
    config = app.config
    redis_url = app.config["REDIS_URL"]
    cache = redis.from_url(redis_url)
    app.cache = cache

async def init_cache(app, db_session: Session = Depends(get_db_session)):
    print("cahce parpare")
    query = select(ColMeta).where()
    result = await (app.db()).execute(query)
    rows = result.scalars().all()
    # user, product, person, deal, accouting
    dict_items = {
        "user": {"code": {}, "all": []},
        "product": {"code": {}, "all": []},
        "person": {"code": {}, "all": []},
        "deal": {"code": {}, "all": []},
        "accouting": {"code": {}, "all": []},
    }
    for row in rows:
        item = {}
        item["id"] = row.id
        table_meta_id = row.table_meta_id
        dict_index = {
            1: "user", 2: "product", 3: "person", 4: "deal", 5: "accouting",
        }[table_meta_id]
        dict_item = dict_items[dict_index]

        item["status"] = row.status
        item["data_type"] = row.data_type
        item["detail"] = row.detail
        code = item["code"] = row.code
        name = item["name"] = row.name
        display = item["display"] = row.display
        item["options_jb"] = row.options_jb
        item["default_jb"] = row.default_jb
        item["html_type"] = row.html_type
        item["html_pattern"] = row.html_pattern
        item["html_detail"] = row.html_detail
        dict_item["code"][code] = {"name": name, "display": display}
        dict_item["all"].append(item)

    app.cache.set("user_define.user", 
        json.dumps(dict_items["user"], ensure_ascii=True))
    app.cache.set("user_define.product", 
        json.dumps(dict_items["product"], ensure_ascii=True))
    app.cache.set("user_define.person", 
        json.dumps(dict_items["person"], ensure_ascii=True))
    app.cache.set("user_define.deal",
        json.dumps(dict_items["deal"], ensure_ascii=True))
    app.cache.set("accouting.accouting",
        json.dumps(dict_items["accouting"], ensure_ascii=True))
    print("cahce parpared")


async def get_extra_fields(request: Request):
    extra_field_str = request.app.cache.get("user_define.user")
    extra_field_info = json.loads(extra_field_str)
    extra_fields = extra_field_info["code"].keys()
    return extra_fields

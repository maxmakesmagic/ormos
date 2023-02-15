from datetime import datetime
import hashlib

from pony import orm

db = orm.Database()


def url_hash(url: str) -> str:
    m = hashlib.sha256()
    m.update(url.encode("utf-8"))
    return m.hexdigest()


class Scraped(db.Entity):
    hash_raw_url = orm.PrimaryKey(str)
    raw_url = orm.Required(orm.LongUnicode)
    url = orm.Required(orm.LongUnicode)
    mime_type = orm.Required(str)
    status_code = orm.Required(int)
    time = orm.Required(datetime)
    view_url = orm.Required(orm.LongUnicode)
    html_content = orm.Required(bytes, lazy=True)
    distinct = orm.Optional("DistinctPage")


class DistinctPage(db.Entity):
    hash_url = orm.PrimaryKey(str)
    url = orm.Required(orm.LongUnicode)
    scraped = orm.Required(Scraped)


class ImageUrl(db.Entity):
    input_url = orm.Required(str, unique=True, max_len=384)
    output_url = orm.Required(str, max_len=384)
    strategy = orm.Required(str)


class ImageUrl2(db.Entity):
    hash_input_url = orm.PrimaryKey(str)
    input_url = orm.Required(orm.LongUnicode, lazy=False)
    output_url = orm.Required(orm.LongUnicode, lazy=False)
    strategy = orm.Required(str)

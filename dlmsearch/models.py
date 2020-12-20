from pony.orm import Database, db_session
from pony.orm import Required, Optional

from .config import config

db = Database()

class Location(db.Entity):
    type = Required(int)
    name = Required(str)
    var_name = Optional(str)
    lon = Required(float)
    lat = Required(float)

db.bind(**config['PONY'])
db.generate_mapping(create_tables=True)

from pony.orm import Database, db_session
from pony.orm import Required, Optional

from .config import config

db = Database()


class Location(db.Entity):
    category = Required(int)
    name = Required(str)
    var_name = Optional(str)
    lon = Required(float)
    lat = Required(float)

    @classmethod
    def filter_locations(cls, needle, category=None, limit=1024):
        """Return locations filtered by name and category."""
        def filter_locations(location):
            return (needle and needle in location.name.lower()) \
                and (category == location.category or not category)
        def order_by_locations(location):
            return len(location.name), location.name, len(location.name)
        return cls.select() \
            .filter(filter_locations) \
            .order_by(order_by_locations) \
            .limit(limit)


db.bind(**config["PONY"])
db.generate_mapping(create_tables=True)

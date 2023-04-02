import os

PACKAGE_DIR: str = os.path.dirname(__file__)
VIEWS_DIR: str = os.path.join(PACKAGE_DIR, "views")

config: dict = {
    "PONY": {
        "provider": "sqlite",
        "filename": "local.db",
        "create_db": True
    }
}
